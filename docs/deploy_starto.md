# deploy_starto: STRATO deployment and deletion

Workflow: [`.github/workflows/deploy_starto.yml`](../.github/workflows/deploy_starto.yml).
The name **deploy_starto** deliberately preserves the requested spelling;
the hosting provider is **STRATO**.

The current `rebuild/` directory must become the repository root. Runs are
manual: **Actions → deploy_starto → Run workflow**.

## Hosting Starter: what is required

The site needs only ordinary **HTML webspace**, HTTPS for the public website,
and an encrypted file-transfer account. The build runs on GitHub's runner;
**Node.js, Python, a database and SSH shell access are not needed at STRATO**.

STRATO's current official documentation recommends **SFTP on port 22**, with a
personalized server hostname and generated username shown in **Datenbanken und
Webspace → SFTP & SSH**. An SFTP-only account is sufficient. Do not copy a
hostname/username from an example or assume that a website domain is the
transfer server.

**“Hosting Starter” is not a reliable specification for every contract generation.**
The current public product names differ, and STRATO's documentation/account UI
can differ for legacy packages. Public documentation does not establish the
entitlements of your particular Starter contract. Confirm that your account
actually provides HTML webspace, SFTP and domain-to-directory assignment in
the customer login. STRATO explicitly distinguishes a domain-only package,
which has no webspace/SFTP. If these facilities are missing, ask STRATO about
your contract before configuring the workflow; do not assume an upgrade is
needed merely because shell access is absent.

The implementation also supports **explicit FTPS (FTP over TLS)** if your
account actually offers it. This is not SFTP and must use that service's own
hostname/port. Unencrypted FTP and implicit FTPS/port 990 are not supported;
there is no insecure automatic fallback.

## Prepare a separate deployment directory

**Back up the existing WordPress website before changing domain routing.**
Do not deploy over its installation or use the account's root directory.

1. Create a dedicated empty directory such as `/abc-static/`.
2. Create a separate SFTP account, preferably restricted to a parent containing
   only this deployment directory. No shell permission is required.
3. In **Domains → Domainverwaltung → your domain → Webserver**, select an
   **internal** directory assignment to that directory, not an external redirect.
   For a migration, test using a temporary subdomain before switching the
   production domain.
4. Enable/check the domain's SSL certificate and HTTPS in STRATO.

`STRATO_REMOTE_DIR` is the path **as seen by the transfer account**, not the
server's absolute Unix filesystem path. Example: if the account is restricted
to webspace `/deployments/`, the transfer path `/abc-static` corresponds to
webspace `/deployments/abc-static/`. Assign the domain to that actual webspace
directory. The restricted account must still see `abc-static` as a child: the
workflow intentionally refuses `STRATO_REMOTE_DIR=/`, even for restricted users.

The workflow may create missing destination directories. Its first deployment
requires an empty target directory. It will refuse a directory containing
WordPress, an existing unrelated site or any other files without its ownership
manifest. Use ordinary ASCII directory names with letters, numbers, `_`, `-`
or `~`; `/` separates nested directories. Do not include a trailing slash,
spaces, dot segments or symlinks.

## GitHub environment and secrets

Create a GitHub environment named **strato** under **Settings → Environments**.
Restrict allowed deployment branches and add required reviewers where available.
Place these values in that environment's Actions **secrets**, or repository
Actions secrets. Do not put credentials in workflow inputs, committed files or
`site.json`.

| Secret | Required | Meaning / example |
|---|---|---|
| `STRATO_HOST` | Yes | Exact transfer hostname shown by STRATO, without scheme or path. |
| `STRATO_USERNAME` | Yes | Transfer-account username. |
| `STRATO_PASSWORD` | Yes | That account's password. Password authentication is used. |
| `STRATO_REMOTE_DIR` | Yes | Dedicated non-root destination, e.g. `/abc-static`. |
| `STRATO_SITE_URL` | Yes | Public HTTPS URL, e.g. `https://abc-bauconsulting.de`, **not** the SFTP URL or remote directory. No credentials, query, fragment or custom port. |
| `STRATO_PROTOCOL` | No | `sftp` (default) or `ftps` (explicit TLS only). |
| `STRATO_PORT` | No | Defaults to `22` for SFTP, `21` for explicit FTPS. |
| `STRATO_KNOWN_HOSTS` | SFTP only | Verified OpenSSH `known_hosts` entry/entries for the exact hostname and port. |

`STRATO_SITE_URL` can include a simple public path prefix if you really publish
under one. A domain internally assigned to `/abc-static/` normally still has
the URL `https://example.com`, **not** `https://example.com/abc-static`.
The generated navigation, search, canonical URLs and sitemap use this public URL.
The source files are not changed. The noindex switch is **not** overridden:
review the launch checklist in the README before enabling indexing.

### Verify the SFTP host key

The workflow rejects unknown or changed host keys. Obtain the server's OpenSSH
public host key and independently verify its fingerprint, for example against
STRATO support or an already independently verified connection.

You can collect a **candidate** locally:

```sh
ssh-keyscan -p 22 YOUR-EXACT-STRATO-HOST > strato-known-hosts
ssh-keygen -lf strato-known-hosts
```

**A key scan alone does not authenticate the server.** Compare fingerprints
through a trusted independent source before saving the verified lines as
`STRATO_KNOWN_HOSTS`. For nondefault ports the host field normally has the form
`[hostname]:port`; use the entry for that exact host/port. Never disable host-key
checking or auto-trust a fresh scan in CI. The temporary host-key file is
permission-restricted and removed after the connection.

For FTPS, Python validates the hostname and certificate chain using the runner's
trusted certificate authorities and requires TLS on both control and data
connections. The FTPS server must support machine-readable **MLSD** directory
listings; unsupported servers fail rather than risk ambiguous deletion.

## Deploy

1. Run `deploy_starto` with `operation: deploy`.
2. Approve the environment if required.
3. Once it finishes, open the public URL and check several subpages and search.

The workflow builds and checks the site, prepares `dist/web-site/`, installs
the pinned SFTP client dependency, then transfers static files. It also writes
an Apache `.htaccess` that chooses `index.html`, serves the custom `404.html`
with HTTP 404, and denies HTTP access to its ownership manifest.

The remote `.abc-deployment.json` records a hash binding the deployment to this
repository and normalized public URL, plus a list of managed paths. It contains
**no password, private key or other connection credentials**. Keep it in place.

Later deployments update managed files and remove files that disappeared from
the build. An unmanaged file is never silently overwritten or deleted. Symlinks,
unsafe paths, ownership mismatches and invalid manifests stop the run.
This tool is specifically for the static site, not a general-purpose webspace
mirror. Do not edit managed files remotely: the next deployment will overwrite
those edits. Update the Markdown/source repository instead.

Transfers are **not atomic**: visitors may briefly encounter a mixed old/new
version during an upload, and network failures can leave a partial publication.
The manifest records the old/new union before uploads so a retry or delete can
normally finish safely. If a failure damages the manifest itself, the tool
fails closed; restore a trusted manifest/backup or deploy to a new empty directory.
Do not remove the marker merely to bypass ownership checks. Scheduled snapshots/
backups and an initial staging-subdomain check are recommended.

## Delete the deployed website

1. Run with `operation: delete`.
2. Enter exactly **`DELETE owner/repository`** in `delete_confirmation`, using
   the real repository name and matching case.
3. Approve the protected environment if configured.

No site build is performed. The tool checks the repository/URL ownership marker,
deletes only its listed files, removes their now-empty subdirectories, then
removes the marker. It preserves the target directory itself and every unmanaged
file. Missing files from an interrupted run are tolerated; missing or invalid
ownership is not.

With the required dedicated directory, this removes the published website.
It does **not** cancel the hosting package, delete domains, change DNS/internal
domain assignments, alter other websites, remove WordPress elsewhere, or delete
repository content. STRATO/proxy/browser caches may briefly retain old responses.
If unmanaged files were manually added, they remain and might still be publicly
accessible; inspect the directory with your transfer client.

To restore, rerun `deploy` into the now-empty directory. If changing the
repository name or `STRATO_SITE_URL`, remove the old managed deployment using
the **old** configuration first (or publish to a new empty directory); changing
those values changes ownership and cannot silently adopt the old deployment.
Deploy/delete runs are serialized; a newer run does not cancel a running transfer.

## Troubleshooting

- **Authentication error:** use the transfer account's credentials, hostname and
  protocol from the customer login, not your STRATO customer-login password.
- **Host key mismatch:** stop and independently verify a legitimate server-key
  change before updating `STRATO_KNOWN_HOSTS`.
- **Permission/path error:** check the account's start directory and the
  difference between transfer-relative and domain/webspace paths.
- **Unowned/nonempty directory:** choose a fresh empty dedicated directory;
  do not point at WordPress or delete its files to force adoption.
- **Public URL still shows WordPress:** check the domain's internal directory
  assignment and caches; uploading to a new folder does not change domain routing.
- **HTTP 500 after upload:** verify `.htaccess` support/overrides for your
  particular contract with STRATO and inspect its error log. The generated
  directives assume an Apache-compatible hosting configuration.
- **HTTP/SSL failure despite a successful transfer:** check DNS, domain routing
  and the certificate separately; a successful file transfer cannot validate
  public DNS/HTTPS configuration.

## Official research sources

Checked **2026-10-29**. Account-specific values and legacy Starter entitlements
must be confirmed in your own contract/customer login.

- [SFTP connection details and domain-only package limitation](https://www.strato.de/faq/hosting/so-verbinden-sie-sich-mit-dem-strato-sftp-server/)
- [SFTP-only vs. SFTP+SSH, per-project start directories and personalized server details](https://www.strato.de/faq/hosting/so-nutzen-sie-ihren-ssh-sftp-zugang/)
- [Internal domain-to-directory assignment](https://www.strato.de/faq/domains/alles-zur-domainumleitung/)
- [Current hosting products](https://www.strato.de/hosting/)
