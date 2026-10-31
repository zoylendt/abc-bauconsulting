# GitHub authentication in the Dev Container

This setup keeps GitHub authentication out of the Docker image and out of the
Mac user's global Git configuration. It uses the GitHub CLI with a fine-grained
token and configures Git's credential helper inside the container. The image
definition is [Dockerfile](./Dockerfile), next to this Dev Container
configuration.

## First-time setup

1. Copy the example configuration:

   ```sh
   cp .devcontainer/github.local.yaml.example .devcontainer/github.local.yaml
   ```

2. Edit `.devcontainer/github.local.yaml`:
   - Set `github.repository` to the private repository in `OWNER/REPOSITORY`
     form.
   - Optionally set `github.token` to a fine-grained GitHub token with access
     to that repository and **Contents: Read and write** permission. If the
     value is omitted, empty, or still contains `REPLACE_ME`, startup reuses
     an existing session-only `gh` login. On a fresh container, a token is
     required and startup stops before synchronization.
   - Set the local commit identity under `git`.

3. In the Mac version of VS Code, install **Dev Containers**, open this folder,
   and run **Dev Containers: Rebuild Container Without Cache**. This is
   important after changing `devcontainer.json`; reopening an existing
   container can continue using its old post-start metadata.

The workspace is explicitly mounted at `/workspace`, and the expected startup
command in the Dev Container log is:

```text
/bin/sh -c bash /workspace/.devcontainer/startup.sh
```

The container is started with Docker's `--rm` option. VS Code stops the
container when the Dev Container window closes, and Docker then removes that
container automatically. The image remains cached for faster entry, while the
bind-mounted workspace and any ignored local configuration remain on the Mac.
The temporary `/tmp/devcontainer-gh-config` authentication state is removed
with the container. This setting is for the single-container Dockerfile
workflow used here; Docker Compose has a different lifecycle.

The post-start command runs [.devcontainer/startup.sh](./startup.sh) whenever
the container starts. It:

- enforces mode `600` on `github.local.yaml`;
- initializes Git if needed and configures `origin`;
- authenticates `gh` and enables GitHub's Git credential helper;
- fetches the remote and force-checks out the configured default branch.

If a token is configured, the script authenticates `gh` and verifies access to
the configured repository. An invalid configured token stops startup with an
actionable error. Without a token in YAML, an existing session-only `gh` login
is used; on a fresh container, startup stops and explains that authentication
is required. Authenticated state is stored under
`/tmp/devcontainer-gh-config`, and `GH_CONFIG_DIR` is also set to this location
for VS Code terminal commands. No token is requested interactively.

Startup synchronizes the configured branch destructively: it fetches the
remote, removes local tracked and untracked changes, and force-checks out
`origin/<default_branch>`. The only workspace file explicitly preserved is
`.devcontainer/github.local.yaml`. Do not keep other local-only files in the
workspace unless they are committed to the remote; they will be removed on
startup. After startup, use the VS Code Source Control view or normal Git
commands from the container:

```sh
git pull origin main
git push -u origin main
```

## Security boundary

`github.local.yaml` is ignored by Git, and the token is never copied into the
Docker image or written to the repository's `.git/config`. The local
`.git/config` contains the repository URL, commit identity, and a credential
helper command without the token; the authenticated state is stored in the
temporary container directory described above.

Because the workspace is bind-mounted from macOS, an ignored file located under
`.devcontainer` is still physically present on the Mac. This satisfies the
convenience requirement of persisting one local YAML file with the workspace,
but it is not a container-only secret. A token placed in the YAML file is
therefore still physically present on the Mac. For a strict host exclusion,
omit the token from YAML and provide an existing container-only `gh` session,
or keep secrets in a Docker named volume.
