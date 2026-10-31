# ABC Abel Bau-Consulting static rebuild

Eleventy + Nunjucks + ordinary Markdown, with a small local stylesheet and vanilla JavaScript. No WordPress, database, React, CMS, remote fonts, analytics or image-CDN dependency.

The site includes all **54 published pages** inventoried in [`docs/DESIGN.md`](docs/DESIGN.md), including the 26 real project references and three sitemap-only sample/template pages. Routes, German text, project facts, photo order, category links and project-navigation destinations are retained. The design document is a migration reference, **not a build dependency**.

## Documentation

- [Adding a new reference](docs/adding-a-reference.md): page metadata, images, category listings and project navigation.
- [Original website design and content inventory](docs/DESIGN.md).
- [Original generator recommendation](docs/generator.md): the initial proposal; use this README for the implemented folder structure.
- [deploy_local](docs/deploy_local.md): download an archive and open `index.html` without a server.
- [GitHub Pages shared setup](docs/deploy_gh.md): credentials, switching modes and deletion.
- [deploy_gh_pages](docs/deploy_gh_pages.md): publish/unpublish using the default `owner.github.io/repository/` URL.
- [deploy_gh_custom](docs/deploy_gh_custom.md): publish/unpublish using a required custom domain.
- [GitHub Pages and company websites](docs/github-pages-company-hosting.md): hosting restrictions, custom domains and test/PoC use.
- [deploy_starto](docs/deploy_starto.md): publish/delete at STRATO using SFTP or explicit FTPS.

## Build and view locally

Prerequisites: **Node.js 22+ with npm** (Node 24 LTS recommended) and **Python 3.10+**.

From the folder containing `rebuild/`:

```sh
python3 rebuild/preview.py
```

This installs the locked npm dependencies when necessary, builds the HTML and search index, starts a loopback-only server at **http://127.0.0.1:8000/**, and opens your browser. Stop with Ctrl+C. It does not watch for edits; rerun it to rebuild.

From inside this folder, use `python3 preview.py`. Options:

```sh
python3 preview.py --port 8080 --no-browser
python3 preview.py --skip-build
```

For editing with automatic HTML/CSS rebuilds:

```sh
npm ci
npm run build
npm run dev
```

Eleventy's development server prints its address. Run `npm run build` again to refresh the **search index** after content edits; the watch server rebuilds pages, not Pagefind. `npm test` performs a clean build and checks routes, links/assets, image mappings, reference tables, shared markup and deployment helpers. It now also requires Python 3.10+; helper tests use only the standard library and make no external API/transfer calls.

## Where to edit

| Location | Responsibility |
|---|---|
| `src/content/Startseite/` | Homepage |
| `src/content/Leistungsspektrum/` | Service overview and service descriptions |
| `src/content/Über uns/` | Company overview, consultant biography and location |
| `src/content/Referenzen/` | Reference overview; category subfolders containing their overview and project pages |
| `src/content/Seminare/` | Seminar overview, current information and general overview |
| `src/content/Kontakt/` | Contact page |
| `src/content/Impressum/` | Legal notice, privacy policy and disclaimer |
| `src/content/*.md` | Uncategorized pages: Blog, Sample Page and Referenz-Template |
| `src/_data/site.json` | Shared company details, canonical domain and indexing switch |
| `src/_data/navigation.json` | Ordered menu and submenu links |
| `src/_data/images.json` | Image IDs, local paths, dimensions, alt text and source provenance |
| `src/assets/images/` | Local images and `REPLACEMENTS.md` |
| `src/_includes/` | Shared page layout, header, sidebar, footer and reusable macros |
| `src/assets/css/site.css` | Layout, typography, colors and responsive rules |
| `src/assets/js/` | Menu, sticky header, back-to-top, legacy search redirect and search UI |
| `eleventy.config.js` | Markdown rendering, image resolution, copying and output settings |
| `_site/` | Generated deployable site; never edit or commit this folder |
| `dist/` | Generated local/hosted exports with deployment-specific links; never commit |
| `.github/workflows/` | Four manually triggered export/deployment workflows |
| `scripts/` | Portable export, Pages settings and scoped STRATO transfer helpers |

Reference content is grouped by the same categories as the reference menu:

```text
src/content/Referenzen/
  referenzen.md
  Ingenieurbau/
  Spezialtiefbau/
  Hochbau & Schlüsselfertigbau/
  Tiefbau & Straßenbau/
  Gutachten/
  Beweisfähige Baustellendokumentationen/
  Adjudikation/
```

Each category folder contains its existing category-overview Markdown file and the matching project pages. `referenzen.md` remains the main reference overview. These folders only organize the source; public URLs and previous/all/next project links stay unchanged.

Page files use readable YAML front matter followed by regular Markdown:

```markdown
---
title: "Projektname"
permalink: "/projektname/"
hero: "IMG-067"
documentTitle: "Projektname – ABC Abel Bau-Consulting"
navigationParent: "/ingenieurbau/"
referenceNavigation:
  previous: "/ingenieurbau/"
  all: "/referenzen/"
  next: "/anderes-projekt/"
---

![Projektname – Überblick](/assets/images/img-027.svg)

| | |
|---|---|
| Objekt: | Beschreibung |
| Bauherr: | Name |
| Auftraggeber: | Name |
| Leistungen: | Erste Zeile<br>Zweite Zeile |
```

Keep published `permalink` values stable: folder names organize the source files, **not the public URLs**. Moving a Markdown file between categories does not change its URL or navigation. Put pages without a suitable category directly in `src/content/`.

The importer used inline YAML objects for project navigation; multiline YAML as above works equally well. `navigationParent` determines the active menu group. `src/content/content.json` gives every Markdown page, including uncategorized root-level pages, the shared `sitePage` collection tag. The layout and other site-wide defaults remain inherited from `src/src.json`. A new page need not have `documentTitle`; it otherwise uses its title and the company name.

The empty Markdown table heading exists only to make ordinary Markdown valid; the renderer removes it so the visible facts table retains exactly the original four rows. Body H1s render as visually equivalent H2s, leaving one semantic H1 in the hero.

## Replace the placeholder images

**Every image is currently a labeled local SVG placeholder, including the logo, credentials, favicon and slogan.** The hero crops, body-image order and dimensions are represented, but placeholder artwork cannot match the original photographs, handwriting or licensed marks.

See **[`src/assets/images/REPLACEMENTS.md`](src/assets/images/REPLACEMENTS.md)** for all **84 IDs**, their placeholder filenames, exact original paths and available WordPress size variants. Upload paths intentionally omit `https://abc-bauconsulting.de/wp-content/uploads`.

Add a real image, then update its `src`, `width`, `height`, `alt` and `placeholder` fields in `src/_data/images.json`. Existing Markdown references to the SVG filenames are resolved through the manifest at build time, as are hero/sidebar IDs, so replacing an image does not require editing all its page occurrences. Shared templates use the manifest's alt text; content images retain their page-specific Markdown alt text. New images should also be registered. The passthrough rule supports SVG, PNG, JPEG, WebP, AVIF, GIF and ICO, including image subfolders.

Use the documented served size or generate an appropriately sized replacement offline; this setup deliberately avoids native image-processing dependencies. CSS preserves aspect ratios and constrains photos to the content width. Content photos lazy-load, while the logo and hero load eagerly.

The old agency image **IMG-084** already returned 404 on the source site. Its guide entry gives the non-uploads legacy URL; obtain an approved replacement rather than assuming it can be downloaded.

## Fidelity and intentional differences

The shell reproduces the dark contact strip, centered desktop logo/menu, wrapping navigation, darkened hero, overlapping white panel, original sidebar-before-body stacking, three-column/two-badge credentials, company slogan, four-row project tables, navigation pills and dark footer. Mobile keeps the 70px header, smaller typography, expandable menu and full-width content. Live comparison clarified a source-theme detail: the mobile **homepage** loses its overlap/shadow, while **subpages retain a 60px overlap and shadow**, despite having no side margins or rounded corners. This distinction is reproduced. Desktop keeps sticky navigation and lightweight hero parallax, disabled for reduced-motion preferences.

Intentional corrections/replacements:

- The WordPress search is replaced by **local Pagefind search** at `/suche/`; old `?s=...` requests redirect there in JavaScript. There is no search backend or third-party search request.
- Internal links point to the local routes. The two broken privacy links are corrected, and the trailing space in the contact email link is removed.
- Exactly one H1 is used per page; body-title sizes are retained. Placeholders have alt text, controls have keyboard focus styles, and utility telephone contrast is improved.
- Empty parent pages remain empty. Blog, Sample Page and Referenz-Template remain reachable but outside the menu, search and sitemap. Empty template navigation destinations are omitted rather than emitting nonfunctional buttons.
- The missing legacy agency artwork gets an honest placeholder, not a deliberately broken image.
- The original visible Hestia/ThemeIsle footer credit is retained as part of the reconstruction; no theme code is required by the build.

**Content is transcribed, not legally or commercially refreshed.** It still includes the source's old seminar date, typos and privacy/legal wording. Before launch, have the company review contact/project claims, legal text (including old TMG/privacy references), image rights and whether to remove the three sample pages. No contact form, map embed, Facebook integration, cookies or external font request has been added.

## GitHub and deployment

Make **`rebuild/` the repository root** when pushing this implementation to GitHub; its lockfile and `.github/workflows/` are self-contained. If keeping it as a subdirectory of a larger repository, adapt the top-level workflows and paths accordingly.

All workflows run **only manually**, from the GitHub Actions tab. The former push-triggered workflow has been replaced:

| Workflow | Result | Configuration |
|---|---|---|
| [`deploy_local`](docs/deploy_local.md) | Downloadable ZIP; extract and open `index.html`, including offline search | No secrets |
| [`deploy_gh_pages`](docs/deploy_gh_pages.md) | Default `owner.github.io/repository/` URL, or `owner.github.io/` for the user/organization repository; `deploy`/`delete` operations | `PAGES_ADMIN_TOKEN` secret; ignores custom-domain configuration |
| [`deploy_gh_custom`](docs/deploy_gh_custom.md) | GitHub Pages with a required custom domain; `deploy`/`delete` operations | `PAGES_ADMIN_TOKEN` secret; `PAGES_CUSTOM_DOMAIN` variable or manual domain input |
| [`deploy_starto`](docs/deploy_starto.md) | STRATO deployment via verified SFTP or explicit FTPS; `deploy`/`delete` operations | Connection, dedicated target directory and public URL as `STRATO_*` secrets |

The hosted workflows prepare `dist/web-site/`, adapting links, search, canonicals and sitemap URLs to the actual deployment target without editing Markdown. The local export in `dist/local-site/` uses relative file links and a small offline search index instead. Generate it locally with `npm run build:local`. `_site/` retains the ordinary root-relative HTTP preview.

Create protected `github-pages` and `strato` environments and configure the required credentials as described in the linked guides. Deletion requires the exact `DELETE owner/repository` confirmation. Pages deletion unpublishes this repository's Pages site; STRATO deletion removes only manifest-owned files from its dedicated directory, never the webspace root or an unrelated WordPress installation. DNS, SSL setup and domain routing remain separate host/provider configuration.

The two Pages workflows switch **one repository's single site** between deployment modes; they do not publish independent sites. Both share the same concurrency group and protected environment. Deleting through either workflow also removes a site deployed by the other. See the [switching test and shared setup](docs/deploy_gh.md). For simultaneous sites, use separate repositories.

Before using Pages for the company's public website, review [GitHub Pages and company websites](docs/github-pages-company-hosting.md). The absence of a shop, use of a custom domain or a short-lived PoC does not by itself establish permission under GitHub's business-use restrictions; seek GitHub Support clarification or use a suitable business host.

Preview builds intentionally default to **noindex** and `robots.txt: Disallow: /` while placeholder images and historical legal text remain. After replacement and review, set `indexable` to `true` and confirm `url` in `src/_data/site.json`, then rebuild. Per-page sample/search/404 `noindex` remains in effect. `sitemap.xml` contains the 51 substantive published routes and no generated timestamps.

The Python preview serves `404.html` with an actual HTTP 404 status. GitHub Pages recognizes that file; the STRATO helper generates the corresponding Apache `.htaccess` configuration.
