# Adding a new reference

This guide describes the current Eleventy implementation. All paths below are relative to the **`rebuild/` repository root**, unless stated otherwise.

Creating a Markdown file creates a page automatically. **Category listings and previous/next project links are maintained manually**: putting a file in a folder does not add it to those links.

## 1. Choose a category and create the page

Create a new `.md` file inside the appropriate folder under `src/content/Referenzen/`. The easiest starting point is a copy of a real project in that folder, **not** the category overview or `src/content/referenz-template.md`.

| Category folder | Category overview file inside that folder | `navigationParent` |
|---|---|---|
| `Ingenieurbau/` | `ingenieurbau.md` | `/ingenieurbau/` |
| `Spezialtiefbau/` | `spezialtiefbau.md` | `/spezialtiefbau/` |
| `Hochbau & Schlüsselfertigbau/` | `hochbau-schluesselfertigbau.md` | `/hochbau-schluesselfertigbau/` |
| `Tiefbau & Straßenbau/` | `tiefbau-strassenbau.md` | `/tiefbau-strassenbau/` |
| `Gutachten/` | `gutachten-2.md` | `/gutachten-2/` |
| `Beweisfähige Baustellendokumentationen/` | `beweisfaehige-baustellendokumentationen.md` | `/beweisfaehige-baustellendokumentationen/` |
| `Adjudikation/` | `adjudikation.md` | `/adjudikation/` |

For example, create:

```text
src/content/Referenzen/Ingenieurbau/neue-bruecke.md
```

Use the following structure, replacing the example project details with the real information:

```markdown
---
title: "Neue Brücke"
permalink: "/neue-bruecke/"
hero: "IMG-067"
navigationParent: "/ingenieurbau/"
referenceNavigation:
  previous: "/ingenieurbau/"
  all: "/referenzen/"
  next: "/ingenieurbau/"
---

![Neue Brücke – Überblick](/assets/images/img-027.svg)

| | |
|---|---|
| Objekt: | Beschreibung des Bauvorhabens |
| Bauherr: | Name des Bauherrn |
| Auftraggeber: | Name des Auftraggebers |
| Leistungen: | Beschreibung der Leistungen<br>Weitere Angaben oder Ergebnisse |
```

The example reuses an existing image placeholder so it can build before you add a real project photograph. Replace it with the project's own image as described below.

Important fields:

- **`title`** is the visible hero title.
- **`permalink`** is the public URL. Choose a unique, root-relative URL ending in `/`. The folder name and Markdown filename do not determine it; the example is served at `/neue-bruecke/`, not at a nested category URL.
- **`hero`** identifies a registered image in `src/_data/images.json`. `IMG-067` is the existing general reference hero.
- **`navigationParent`** must match the category route in the table above. This also keeps the reference menu group active.
- **`referenceNavigation`** controls the project-navigation buttons. The example uses the category overview as a safe previous/next destination; wire in neighboring projects in step 4.

If you copied a project with a `documentTitle`, update that field too, or remove it to use the automatic `<title> – ABC Abel Bau-Consulting` browser title. Existing `order` values are inventory metadata; they do not sort the manually written category list or generate previous/next links, and may be omitted on a new project.

Keep the four facts rows (`Objekt`, `Bauherr`, `Auftraggeber`, `Leistungen`). The blank Markdown table header is intentional: the renderer removes it so the visible table has no extra header row. Use `<br>` for line breaks inside a cell. Add further photographs or paragraphs after the table as needed.

The shared layout and page-collection tag are inherited automatically. Do not copy `noindex: true` or `searchable: false` from a sample/template page unless you deliberately want to exclude the new project from the sitemap or search.

## 2. Add project photographs

You can reuse an already registered image without changing configuration. For a new photograph:

1. Add the file under `src/assets/images/`, for example `src/assets/images/neue-bruecke/bauwerk.jpg`. Optimize its size before committing and confirm permission to publish it.
2. Add a new, uniquely named entry to `src/_data/images.json`. For example, use `IMG-085` only if that ID is still unused. Merge the entry into the existing JSON object; do not replace the other entries.
3. Use the actual pixel dimensions and meaningful alt text. Set `placeholder` to `false` for a real photograph.

Example manifest entry:

```json
{
  "IMG-085": {
    "src": "/assets/images/neue-bruecke/bauwerk.jpg",
    "alt": "Neue Brücke – Gesamtansicht des Bauwerks",
    "width": 1600,
    "height": 1200,
    "original": "Company archive: neue-bruecke/bauwerk.jpg",
    "description": "New project photograph, not a migrated WordPress image",
    "variants": [],
    "placeholder": false
  }
}
```

Replace the example dimensions and provenance with the real values. For a genuinely new company photograph, `original` can record its source rather than inventing a WordPress upload URL.

**The current image checks require every image's `original` value to appear in [`src/assets/images/REPLACEMENTS.md`](../src/assets/images/REPLACEMENTS.md).** For a new photograph, add a separate provenance section there, outside the old WordPress-placeholder table, for example:

```markdown
## Additional project photographs

| ID | Local file | Source |
|---|---|---|
| IMG-085 | `neue-bruecke/bauwerk.jpg` | Company archive: neue-bruecke/bauwerk.jpg |
```

Then reference the registered local path in the project Markdown:

```markdown
![Neue Brücke – Gesamtansicht des Bauwerks](/assets/images/neue-bruecke/bauwerk.jpg)
```

Markdown alt text is page-specific. The manifest's `alt` text is used by shared image templates. All local content-image paths must be registered in the manifest; an unregistered path causes a build error.

To replace an existing placeholder everywhere instead, follow the replacement guide and update its existing manifest entry. Existing Markdown links to that placeholder resolve to the replacement at build time.

## 3. Add the project to the category overview

Open the category overview file from step 1 and add a link to its existing project list:

```markdown
- [Neue Brücke](/neue-bruecke/)
```

For the example, edit:

```text
src/content/Referenzen/Ingenieurbau/ingenieurbau.md
```

The list order is the order written in this Markdown file. Put the new link where you want it to appear. The reference overview `src/content/Referenzen/referenzen.md` and the main menu do not need to change when adding a project to an existing category.

## 4. Connect previous/next navigation

Set the new project's `referenceNavigation` destinations to existing public URLs, not filesystem paths. Keep `all: "/referenzen/"` to match the current site's "Alle Referenzen" button.

When inserting the new project between two existing projects:

1. Set the new project's `previous` to the preceding project's permalink and `next` to the following project's permalink.
2. Change the preceding project's `next` to `/neue-bruecke/`.
3. Change the following project's `previous` to `/neue-bruecke/`.

At the start or end of a category, use the category-overview URL for the missing neighbor. Update the existing first or last project's corresponding link when adding a new project at that end. Check the actual links rather than assuming the source site's historical sequence is perfectly linear.

If you intentionally omit `referenceNavigation`, no project-navigation buttons are rendered.

## 5. Build and inspect

Requirements are documented in the [README](../README.md): Node.js 22+ with npm and Python 3.10+.

From `rebuild/`, with dependencies already installed, run:

```sh
npm test
python3 preview.py
```

`npm test` builds the pages and Pagefind index, then checks routes, links/assets, category placement and four-row reference tables. On a fresh checkout, install the locked dependencies with `npm ci` first; the Python preview helper also installs them automatically when needed.

The Python command rebuilds and opens the site at `http://127.0.0.1:8000/`. Stop it with Ctrl+C. From the parent folder, the equivalent command is `python3 rebuild/preview.py`.

Check the new project URL directly, its category-list link, image proportions and alt text, table contents, previous/next links in both directions, and mobile layout. Search for a distinctive phrase from the new project's body to confirm it appears in search.

Normal new pages are included automatically in the shared layout, sitemap and search index after a full build. The development watch server rebuilds pages but does not refresh Pagefind; use a full build after content changes. The site's global pre-launch `noindex` setting is separate and does not need changing just to add a reference.

No Eleventy configuration or main-menu change is needed for a new project in an existing category.
