# deploy_gh_custom: custom-domain Pages deployment

Workflow: [`.github/workflows/deploy_gh_custom.yml`](../.github/workflows/deploy_gh_custom.yml).
Read the [shared setup and deletion guide](deploy_gh.md) first for credentials,
the protected `github-pages` environment and the shared-site limitation.

## Domain configuration

Supply a hostname through either:

1. The manual `custom_domain` input; a nonempty value takes precedence.
2. The Actions variable `PAGES_CUSTOM_DOMAIN`, used when the input is empty.

For testing, prefer a dedicated hostname such as `preview.example.com`, rather
than moving an existing production website's domain. Enter only the hostname:
no `https://`, path, port or trailing slash. International names must use
punycode. Hostnames are normalized to lowercase.

The input is optional in the dispatch form so deletion does not require a
domain and deployment can use the variable. **Deployment itself requires a
valid, nonempty domain**: missing or invalid values fail before any Pages
settings API call. This workflow never silently falls back to `github.io`.

Verify domain ownership in the GitHub account/organization before use. Configure
DNS according to [GitHub's custom-domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).
A subdomain's CNAME points to `owner.github.io`, not a repository path. Apex
domains require the provider's appropriate A/ALIAS/ANAME configuration.
The workflow does not modify DNS or request changes at your registrar.

## Publish

1. Open **Actions > deploy_gh_custom > Run workflow** on a trusted branch.
2. Select `operation: deploy` and supply `custom_domain` unless the variable
   already contains the desired hostname.
3. Approve the environment if required.
4. Check the deployment URL and **Settings > Pages**, including the DNS check
   and certificate status. Enable **Enforce HTTPS** once the certificate is ready.
5. Verify nested pages, assets, search, canonicals and sitemap use the custom URL.

The workflow builds and tests, configures Pages, prepares `dist/web-site/`
using GitHub's returned URL, uploads and publishes it. No committed `CNAME`
file or Markdown-link changes are needed. DNS/certificate readiness is separate
from deployment success; HTTPS can take time to become available.

This replaces a prior `deploy_gh_pages` deployment; it does not create another
site alongside it. Existing `noindex` behavior is preserved.

## Delete or switch back

1. Run **Actions > deploy_gh_custom > Run workflow** with `operation: delete`.
2. Enter exactly `DELETE owner/repository` in `delete_confirmation`, including
   the actual repository's case. Leave `custom_domain` empty if desired.
3. Approve the environment if required and check **Settings > Pages** afterward.
4. Remove or update DNS records pointing at the disabled Pages site; retain
   domain verification to help prevent domain takeover.

Deletion skips the Node setup, build and upload and disables the entire
repository's Pages site, **even if `deploy_gh_pages` last published it**.
It does not delete the domain registration, DNS records, repository or source.

To switch back without a separate deletion, run `deploy_gh_pages` with `deploy`.
It clears the repository's custom domain without changing `PAGES_CUSTOM_DOMAIN`.
Clean up the old DNS configuration separately.

For testing both modes, follow the [switching test](deploy_gh.md#suggested-switching-test).
A custom domain does not change hosting eligibility; see
[GitHub Pages and company websites](github-pages-company-hosting.md).
