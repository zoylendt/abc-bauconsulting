# deploy_gh_pages: default github.io deployment

Workflow: [`.github/workflows/deploy_gh_pages.yml`](../.github/workflows/deploy_gh_pages.yml).
Read the [shared setup and deletion guide](deploy_gh.md) first for credentials,
the protected `github-pages` environment and the shared-site limitation.

## URL

- An ordinary repository publishes at `https://owner.github.io/repository/`.
- A repository named `owner.github.io` publishes at `https://owner.github.io/`.
- `owner` is the user or organization that owns the repository.

This workflow explicitly removes this repository's custom domain. It has no
`custom_domain` input and ignores the `PAGES_CUSTOM_DOMAIN` variable, so that
variable can remain configured for the other workflow.

GitHub's actual Pages URL drives generated links, assets, search, canonical URLs
and sitemap entries. The helper requires the returned hostname to be
`owner.github.io`. If the owner's user/organization site has an inherited custom
domain, remove that setting or use a different account; see the
[inheritance caveat](deploy_gh.md#url-and-domain-selection).

## Publish

1. Open **Actions > deploy_gh_pages > Run workflow** on a trusted branch.
2. Select `operation: deploy` and approve the environment if required.
3. Open the deployment URL shown by the job and check **Settings > Pages**.
4. Verify a nested page, image, search result and canonical URL include the
   repository path for a project site.

The workflow builds and tests before updating Pages settings, prepares
`dist/web-site/`, uploads it and publishes it. A previous custom-domain deployment
is replaced. Update or remove DNS records for that old custom domain separately.
Existing `noindex` behavior is preserved.

## Delete

1. Run **Actions > deploy_gh_pages > Run workflow** with `operation: delete`.
2. Set `delete_confirmation` to exactly `DELETE owner/repository`, including
   the actual repository's case.
3. Approve the environment if required and check **Settings > Pages** afterward.

Deletion skips the Node setup, build and upload. It disables the entire Pages
site for this repository, **even if `deploy_gh_custom` last published it**.
It does not delete source files, the repository or DNS records. The same
confirmation and token requirements apply to both workflows.

For testing both modes, follow the [switching test](deploy_gh.md#suggested-switching-test).
For permitted use, see [GitHub Pages and company websites](github-pages-company-hosting.md).
