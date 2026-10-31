# deploy_local: downloadable, browser-openable website

Workflow: [`.github/workflows/deploy_local.yml`](../.github/workflows/deploy_local.yml).

## Repository setup

Make the current `rebuild/` directory the **root of the GitHub repository**.
The workflow expects `package.json`, `.nvmrc`, `scripts/` and `src/` at that root.
Enable GitHub Actions and put the workflow file on the default branch so its
manual **Run workflow** button appears. No deployment account or secrets are needed.

All three deployment workflows are manual only. A push does not publish a site.

## Build and download

1. Open **Actions → deploy_local → Run workflow** and select the desired branch.
2. Wait for the build to finish.
3. Open the completed run and download **abc-site-local** from **Artifacts**.
4. Extract the **whole ZIP**, preserving all subdirectories.
5. Open its top-level **index.html** in a browser.

Do not open `index.html` from inside the ZIP preview. Keep `assets/`, `suche/`
and the page directories next to it. The download is GitHub's artifact archive;
there is no second ZIP inside it. Artifacts expire after **14 days**, subject
to repository/organization retention limits. Download a copy to keep it longer.
The ZIP is a website export, not a backup of the Markdown source.

The workflow installs the locked npm dependencies, builds the site, runs its
checks and generates `dist/local-site/`. Only that generated directory is
uploaded: no Markdown source, deployment credentials, `node_modules/` or Python
environment is included.

## What works without a server

Internal navigation, images, styles, menus, reference links and search work from
`file://`. Directory links become relative links to explicit `index.html` files.
The search form and old `?s=...` redirects use those same portable destinations.

Pagefind's fetch/WASM index is replaced **only in this export** by a classic
JavaScript text index. It searches the same nonempty, searchable page bodies,
excluding the shared sidebar. All whitespace-separated terms must match,
case/diacritics are ignored, and results use simple excerpts rather than
Pagefind's ranked/sub-result presentation. No network request or local server
is needed for search. JavaScript must be enabled.

Telephone, email, map and other external links still depend on the appropriate
applications or Internet access. The archive is not intended for deployment:
use one of the hosted workflows for public canonical URLs and hosted Pagefind.

## Generate the same export on your computer

Inside the repository, with Node.js 22+ and Python 3.10+ installed:

```sh
npm ci
npm run build:local
```

Open `dist/local-site/index.html`. To create a ZIP yourself, archive the entire
contents of `dist/local-site/`, not just the HTML files. Generated output is
ignored by Git.

For the normal HTTP preview, continue using:

```sh
python3 preview.py
```

If GitHub reports a build or test error, fix it before rerunning. If the run
succeeded but an old artifact expired, run `deploy_local` again.
