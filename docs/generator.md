**I’d choose Eleventy (11ty), with a small custom theme reproducing the current design.** For this particular website, it offers the best balance of visual fidelity, readable Markdown content and low-maintenance implementation.

The key distinction is that **visual fidelity comes from the HTML templates and CSS—not from the generator**. Eleventy, Astro and Quartz can all produce a similar-looking site, but they require different amounts of customization to get there.

## Why Eleventy fits this website

The design document shows a conventional company website: service descriptions, project references, contact/legal pages, and a largely shared layout. Its interactive requirements are small: dropdown navigation, mobile menu, search and a back-to-top button.

[Eleventy](https://www.11ty.dev/docs/) maps directly to that structure:

- **Ordinary Markdown files** for page text, project descriptions, tables and photographs; YAML front matter for titles, hero images, categories and URLs.
- **Shared HTML-like templates**, using Nunjucks, for the header, hero, sidebar, footer and reference navigation.
- **Custom CSS with full control** over the existing layout, spacing, colors and responsive behavior.
- **Plain static output**, with no browser-side framework required. Small JavaScript modules handle the few interactive controls.

You would not need WordPress, PHP, a database, React or MDX. Editing a project description would not require understanding the template implementation.

## How the options compare

| Generator | Fit for this project | Main trade-off |
|---|---|---|
| **Eleventy — recommended** | Direct Markdown-to-HTML workflow; flexible templates; little imposed structure | We implement the theme and configure image processing/search explicitly |
| **Astro — strong alternative** | Excellent for company websites; reusable components, image tooling and schema-validated Markdown collections | More framework-specific concepts and project structure than this site needs |
| **Quartz** | Familiar Markdown workflow and built-in search | Its starting point is publishing interconnected notes; recreating this company-site layout means replacing or disabling much of its default presentation |

**Quartz is capable, but I wouldn’t choose it for a fresh implementation here.** Its [documented strengths](https://quartz.jzhao.xyz/)—backlinks, graph views, wikilinks, transclusions and note navigation—are largely unrelated to presenting services and completed construction projects. Your existing experience helps, but you would spend some of that advantage adapting its assumptions.

[Astro](https://docs.astro.build/en/guides/content-collections/) would be my second choice, especially if you value typed content validation or expect richer interactive features later. It can also generate a fully static site without shipping a client framework; it is not inherently a heavy option.

## Suggested repository structure

For Eleventy, I would keep the implementation approximately this simple:

```text
src/
  pages/                 # Markdown: services, about, contact, legal
  references/            # One Markdown file per project
  _data/                 # Shared company details and navigation
  _includes/             # Layouts and reusable template fragments
  assets/
    images/              # Photographs, logos and hero images
    css/
    js/
eleventy.config.js
package.json
package-lock.json
.github/workflows/deploy.yml
```

A GitHub Actions workflow would build the repository and deploy the generated files to GitHub Pages or another static host. Content edits and image additions would be normal Git commits, including edits through GitHub’s web interface.

I’d preserve the existing public URLs, use a small image-processing setup to generate responsive sizes rather than maintaining all 354 WordPress derivatives, and use **Pagefind** for static search if retaining search is important. Company details and navigation would live in one place, not be duplicated across the content files.

**My recommendation: Eleventy + Nunjucks + ordinary Markdown + custom CSS, with minimal JavaScript.** That gives this site a close visual match without carrying WordPress’s machinery or Quartz’s knowledge-base features into the rebuild.
