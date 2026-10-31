# GitHub Pages: shared setup, switching and deletion

The former `deploy_gh` workflow is replaced by two manual workflows:

| Workflow | Deployment URL | Instructions |
|---|---|---|
| [`deploy_gh_pages`](../.github/workflows/deploy_gh_pages.yml) | `https://owner.github.io/repository/`, or `https://owner.github.io/` for an `owner.github.io` repository | [Default-domain guide](deploy_gh_pages.md) |
| [`deploy_gh_custom`](../.github/workflows/deploy_gh_custom.yml) | A required custom hostname, such as `https://preview.example.com/` | [Custom-domain guide](deploy_gh_custom.md) |

Both have `operation: deploy` and `operation: delete` manual inputs.
The current `rebuild/` directory must be the repository root.

**These are two deployment modes for the same site, not two independent sites.**
GitHub permits only one Pages site per repository. Deploying either workflow
replaces the repository's published site/domain configuration; deleting from
either workflow disables the whole site, including a deployment made by the
other workflow. Use separate repositories if simultaneous sites are needed.

Before publicly hosting the company site, read
[GitHub Pages and company websites](github-pages-company-hosting.md). Custom
domains and short-lived previews do not exempt a site from GitHub's usage terms.

## One-time setup

GitHub Pages must be available for the repository's visibility and account plan.
In **Settings → Pages**, select **GitHub Actions** as the source. The workflow
can also create the Pages configuration if it has not yet been enabled.

Create a GitHub environment named **github-pages** under **Settings →
Environments**. Restrict its allowed deployment branches and, where your plan
supports it, add required reviewers. Both publishing and deletion use this
environment. Only run deployment code from trusted branches; a workflow that
can read a deployment secret can use its privileges.

Create this Actions secret, preferably in that protected environment:

| Secret | Value |
|---|---|
| `PAGES_ADMIN_TOKEN` | An expiring fine-grained personal access token, restricted to this repository, with repository **Administration: Read and write** and **Pages: Read and write** permissions. |

Use an account permitted to manage Pages for this repository. Approve the token
for the organization/SSO if required, and rotate it before expiry. The administration
token is necessary for the workflow's Pages settings/custom-domain and deletion
REST calls. It is not stored in the checkout or published artifact.

Normal site publishing uses the built-in `GITHUB_TOKEN` with `pages: write` and
an OIDC token (`id-token: write`), through GitHub's official deployment action.
The PAT is scoped to the settings/deletion steps, not the npm build.

## URL and domain selection

`deploy_gh_pages` has no domain input. It always clears this repository's
custom-domain setting and ignores `PAGES_CUSTOM_DOMAIN`, even if that variable
is set for custom-domain tests. No variable needs to be cleared to switch back.

`deploy_gh_custom` uses the nonempty manual `custom_domain` input, falling back
to the Actions **variable** `PAGES_CUSTOM_DOMAIN`. At least one must contain a
valid hostname, such as `preview.example.com` or `www.example.com`; missing or
invalid values fail before any Pages settings API call. There is no fallback
to `github.io`. Do not include `https://`, slashes or a port. Use punycode for
international domains. The domain is not required for deletion.

Each workflow configures the domain through the Pages REST API, then reads the
effective public URL from GitHub. It prepares navigation, assets, search,
canonical links, robots sitemap reference and sitemap locations for that URL.
Both root-level sites and default project sites such as
`https://owner.github.io/repository/` are supported. There is no need to change
every Markdown link or commit a `CNAME` file.

**Inherited custom domains:** a custom domain on the owner's user/organization
site can also affect project-site URLs. Clearing the project's custom domain
does not override that inheritance. The helper checks the returned hostname
and refuses publication when the default workflow would use a non-`github.io`
host. Remove the custom domain on the owner's user/organization Pages site, or
use a different account for a strictly `owner.github.io/repository/` test.
This failure can occur after the repository's Pages configuration was updated,
but before artifact upload/deployment; it does not roll back those settings.

**DNS and HTTPS are separate prerequisites.** Verify ownership of your domain
in your GitHub account/organization, configure the correct DNS records using
GitHub's current instructions, and wait for Pages' DNS check and certificate.
A subdomain's CNAME points to `owner.github.io`, not to a repository path.
The workflow does not modify registrar/DNS-provider settings. Once the certificate
is ready, enable **Enforce HTTPS** in Pages settings. Deployment builds use HTTPS
canonical URLs; a newly configured domain may not serve HTTPS immediately.

## Deploy

1. Select **Actions → deploy_gh_pages** or **Actions → deploy_gh_custom** and run
   the workflow with `operation: deploy`.
2. For `deploy_gh_custom`, supply `custom_domain` or set `PAGES_CUSTOM_DOMAIN`.
3. Approve the environment deployment if protection requires it.
4. Open the deployment URL shown by the job and check **Settings → Pages**.

The workflow installs dependencies, builds, runs checks, prepares
`dist/web-site/`, uploads a Pages artifact and deploys it. Source files are
unchanged. A failed build never reaches the Pages settings/deployment steps.
GitHub's Pages artifact is a deployment payload, **not** the browser-openable
archive from `deploy_local`.

The source's **noindex** setting remains in effect. Before a production launch,
replace placeholders, review the historical legal/content text, then deliberately
set `indexable: true` in `src/_data/site.json`. The deployment URL overrides the
source's canonical URL in the generated deployment only; `site.url` still sets
the default for normal local builds.

## Delete / unpublish

1. Run either workflow with `operation: delete`.
2. In `delete_confirmation`, enter exactly `DELETE owner/repository`,
   replacing `owner/repository` with the actual repository name, including case.
3. Approve the protected environment if required.

This calls `DELETE /repos/{owner}/{repo}/pages` and verifies that the Pages
configuration is absent. It disables **this repository's entire Pages website**,
not just its latest artifact. No build is performed; no source branch, repository,
custom domain registration or DNS record is deleted.

**Remove or update custom-domain DNS records when unpublishing or moving the
site.** Do not leave a dangling Pages CNAME. Domain verification should already
be in place. GitHub/CDN caches may retain old responses briefly.

To restore, run `deploy` again with the desired domain. The workflow recreates
the Pages configuration; DNS and HTTPS readiness must be checked again.
Both workflows share the `github-pages` concurrency group and protected
environment. A later run does not cancel an in-progress publication or deletion.
With this concurrency configuration, GitHub allows only one pending run in a
group and may replace an older pending run, so wait for each test run to finish
before starting the next.
Deletion without the exact confirmation fails before any API call.

## Suggested switching test

1. Run `deploy_gh_pages` with `deploy`; check the returned `github.io` URL,
   including a project path, navigation, images, search and canonical links.
2. Run `deploy_gh_pages` with `delete` and the confirmation; check that
   **Settings → Pages** no longer lists an enabled site.
3. Configure and verify a dedicated test hostname, then run `deploy_gh_custom`
   with `deploy`; check the custom URL, DNS and HTTPS.
4. Run `deploy_gh_custom` with `delete` and the confirmation. Remove or update
   test-domain DNS records as part of cleanup.
5. To test switching without deletion, deploy the other workflow directly.
   The prior mode is replaced, not preserved. Clean up the old custom-domain
   DNS records when switching back to `github.io`.

No deployment or deletion is triggered by a push. A `noindex` preview is public,
not access-controlled, and is not in itself a terms-of-service exemption.

## Troubleshooting and references

- **403/404 or token error:** check token expiry, selected repository, both
  permission groups, account role, organization approval and Pages availability.
  Private resources may appear as 404 when authorization is missing.
- **Domain configuration rejected:** check hostname format, ownership, DNS and
  whether another Pages site already uses that domain.
- **OIDC/deployment rejected:** check the Pages source, job permissions and
  environment branch/protection rules.
- **Deployment succeeds but domain fails:** allow DNS/certificate propagation;
  inspect Pages' DNS/HTTPS status. Deployment does not prove DNS readiness.
- **Deletion fails because no site exists:** Pages is already disabled, or the
  administration token cannot see it; inspect Settings before changing anything.

Official references, checked 2026-10-31:

- [GitHub Pages REST API](https://docs.github.com/en/rest/pages/pages)
- [Fine-grained token permissions](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens)
- [Custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Domain verification](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)
- [Pages site types and one-site limit](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [Inherited custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages#using-a-custom-domain-across-multiple-repositories)
- [Workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency)
