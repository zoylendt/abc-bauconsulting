# ABC Abel Bau-Consulting: existing-site design and content specification

Source: <https://abc-bauconsulting.de/>  
Inspection date: 29 October 2026  
Purpose: a faithful inventory for rebuilding the existing WordPress website as a static, Markdown-authored website. This document describes the existing site, not a proposed redesign.

## 1. Scope, evidence and reading conventions

The homepage and every recursively linked internal HTML page were retrieved, including links inside dropdowns, reference-category lists, project navigation and legal text. The result was cross-checked against `robots.txt`, the WordPress sitemap index and its page sitemap. There are **54 live pages: 51 reachable through the site's page links and three additional sitemap-only pages**. Two linked legacy URLs return HTTP 404. All 54 live pages are transcribed below, including empty landing pages, the empty blog, and the published sample/template pages.

The inventory includes visible text, original heading levels, paragraphs, explicit line breaks, emphasis, nested lists, tables, captions, links, header/background pictures, content photographs, shared branding, badges and browser icons. Shared content is recorded once in section 3 and applies to every standard page; it is not silently omitted from the page descriptions. The blog exception is identified explicitly.

Evidence comes from the live HTML, the Hestia theme stylesheets and JavaScript, and browser inspection. The homepage, a reference detail page, navigation and image assets were inspected visually. Responsive layout was inspected at 390, 1000 and 1440 CSS pixels; some screenshots are rendered at twice the CSS-pixel size because the inspection browser uses device-pixel-ratio 2. Source CSS supplies the intervening breakpoints. The browser also fetched all 54 sitemap pages independently and loaded the 82 distinct displayed image families in a contact sheet. Browser icons are additional to those 82 families.

Text in the per-page `markdown` blocks is the page-specific content in source order. German wording, outdated dates, inconsistent spelling, amounts, abbreviations, empty fields and duplicated headings are intentional transcriptions, not editorial corrections. HTML entities and nonbreaking whitespace are normalized for readable Markdown; meaningful line breaks, emphasis, list nesting and table cells are retained. The labels “Body”, “Layout” and image IDs are documentation, not text displayed on the original site.

Pictures have stable `IMG-...` references. A Markdown image reference in a page's transcript identifies its exact position in the content. The per-page image table records the source's actual displayed `src`, declared dimensions and any wrapping link. Section 6 maps every picture ID to its path and includes **all 354 distinct referenced upload paths**, including responsive-size derivatives and four browser-icon sizes. Paths beginning `/2020/`, `/2021/`, `/2022/` or `/2024/` are relative to the upload base:

```text
https://abc-bauconsulting.de/wp-content/uploads
```

That base is deliberately omitted from the image tables. Do not interpret these as paths relative to an individual page. HTTP and HTTPS spellings of the same upload are one asset, not two pictures. Only paths actually referenced by the source are listed; an unreferenced full-resolution original is not invented by removing a size suffix. A missing image outside the uploads directory is recorded separately with its real resolved site path.

## 2. Visual design and layout

### 2.1 Overall composition

The visual language is the **Hestia** WordPress theme: an expansive photographic title header, a raised white content panel, restrained blue accents, light-weight sans-serif body text, and a dark utility strip and footer. It is an informational consultancy site rather than an application, shop, portfolio-card grid or one-page scrolling microsite.

The standard page is arranged vertically:

1. Dark utility/contact strip.
2. White centered-logo navigation, with dropdown menus and search.
3. Full-width photographic hero with a dark overlay and centered white page title.
4. White raised main panel, with a persistent contact/credential sidebar on the left and page-specific content to its right on sufficiently wide screens.
5. Dark footer with legal/contact navigation and theme credit.
6. A fixed circular back-to-top control after scrolling.

There is no breadcrumb trail, introductory hero subtitle, prominent hero CTA, social-media strip, cookie-consent overlay, contact form, shopping basket, carousel or inline map in the inspected pages. Although WordPress ships styles/scripts for many such features, their presence in a stylesheet does not make them part of this site's design.

### 2.2 Color and typography

| Element | Observed value / treatment |
|---|---|
| Outer page background | `#c4c4c4` |
| Main panel and navigation | White, `#ffffff` |
| Utility strip | `#363537` |
| Footer | `#323437` |
| Main content text | `#3c4858` |
| Sidebar/widget text | `#5e5e5e` |
| Navigation text | `#555555` |
| Configured theme accent | `#1f29ef`; used for active subpages, hover/focus and theme controls |
| Sidebar links | Computed normal color `#23527c`; do not assume every link is the accent blue |
| Reference-navigation pills | Background `#32373c`, white text |
| Back-to-top circle | `#999999`, white double-chevron icon |
| Hero title | White, bold, centered |
| Branding | Blue/gray geometric building logo; red handwritten slogan on a gray image background |

The declared body/navigation/content stack is `Roboto, Helvetica, Arial, sans-serif`. The sidebar widget heading uses `"Roboto Slab", "Times New Roman", serif`, bold. **No downloadable font faces were registered in the inspected browser**, so the rendered appearance uses available fallbacks; specifying the family name alone does not demonstrate that Google Fonts loaded. Do not silently introduce a different webfont and call it pixel-identical.

| Text role | Desktop | At widths up to 768px |
|---|---|---|
| Base body outside main content | 14px, weight 300, line-height about 1.618 | Same |
| Main paragraphs/lists/tables | 18px, weight 300, line-height about 29.12px | 16px, line-height about 25.89px |
| Hero H1 | 42px, weight 700, line-height 1.4 | 26px |
| Main-content H1 | 42px | 30px |
| Main-content H2 | 37px | 28px |
| Main-content H3 | 32px | 24px |
| Main-content H4 | 27px | 22px |
| Main-content H5 | 23px | 20px |
| Main-content H6 | 18px | 18px |
| Sidebar heading | 18px, serif, weight 700, line-height about 29.12px | Same |
| Navigation | 12px, weight 400, line-height 20px, uppercase | 12px menu text; stacked items |
| Utility strip | 12px, weight 300 | Same |

Main-content headings are generally weight 500 with 15px bottom spacing. Main body lists use normal disc bullets, indented about 40px, with generous line height. Some “lists” in the original are paragraphs containing literal `•`, `–` or `›` characters and manual breaks; these remain identifiable in the transcripts rather than being rewritten as new prose. Bold and italic emphasis are retained.

One explicit heading-size exception is **“Gestaltung und Umsetzung”** in the Impressum: it is structurally an H1 but carries WordPress's medium-size class and renders at **20px**, not the normal H1 size. The composting-facility reference also puts the medium-size class on its table wrapper, but the table and cells themselves still compute to the normal 18px desktop body size.

### 2.3 Header and hero

The utility strip is 40px high. Its contact sentence is on the left and a small Kontakt / Impressum / Datenschutz menu is on the right on wider screens. The address and email are white links; the telephone is plain text and inherits the muted widget color, resulting in low contrast. At phone width the contact sentence wraps inside the constrained strip and the small right-hand navigation is not visible.

The brand is an image of a gray/blue geometric building with “ABC” and “Abel Bau-Consulting” lettering. The source declares 190 × 100px; the theme limits its visible height to 50px, giving a 95 × 50 CSS-pixel logo in the inspected views. Clicking it goes to the homepage.

Before scrolling, the white navigation is centered: logo above the menu; menu items flow in one row when there is room, or wrap to a second row at intermediate widths. At 1440px the settled navbar was about 121px high; at the 1000px inspection it was about 172px. Items have about 15px padding. Small down-chevron/caret icons identify dropdowns. The search magnifier appears at the end of the desktop menu.

The navigation initially occupies an absolute layer above the hero. After passing its scroll threshold, it becomes fixed at the top, gains the `navbar-scroll-point` state and compacts (about 71px high in the wide-screen inspection). The utility strip scrolls out of view. There is a subtle navbar shadow:

```css
box-shadow:
  0 1px 10px -6px rgba(0,0,0,.42),
  0 1px 10px 0 rgba(0,0,0,.12),
  0 4px 5px -2px rgba(0,0,0,.10);
```

Every page has a route-specific title and one assigned hero image, recorded in the page catalog. The photograph is a centered `background-image`, `background-size: cover`, without tiling, darkened by a `rgba(0,0,0,.5)` overlay. Wide source photographs are cropped by the hero viewport; preserve the actual asset rather than reconstructing collages from separate photographs. The homepage image itself contains bridge/tunnel imagery. Services use the timetable/bridge collage; seminars use a desk/plans still life; contact uses a village/castle landscape; legal pages use the Rennsteig tunnel. About pages and the general reference/default pages use different crops of Volker Abel at a bridge construction site.

The hero is not a single universal fixed height. Height and top spacing depend on navbar height, wrapping title lines, breakpoint and theme JavaScript. At 1000px the homepage header was approximately 530px high, starting below the 40px strip; at wide-screen reference inspection the settled header was about 429px. At 390px the homepage hero/header was 276px high, including the area behind the 70px mobile navbar. Long reference titles wrap naturally; they must not be truncated or ellipsized.

The source enables desktop parallax: while the header is in view, scrolling translates it vertically by approximately one third of scroll distance. The theme skips that behavior below 768px.

### 2.4 Main panel and grid

On desktop the white main panel overlaps the hero by 60px. The homepage at the 1000px inspection had 15px side margins, 6px rounded top corners and squared lower corners. At wide widths the theme can use larger side gutters. The characteristic raised-panel shadow is:

```css
box-shadow:
  0 16px 24px 2px rgba(0,0,0,.14),
  0 6px 30px 5px rgba(0,0,0,.12),
  0 8px 10px -5px rgba(0,0,0,.20);
```

Content sits in a centered Bootstrap-style container with 15px horizontal internal padding and negative row gutters. The observed container is 750px in the 1000px source view, and 1170px at 1440px. The standard sidebar is `.col-md-3` and the body is `.col-md-8`, leaving an unused grid column rather than filling a strict 25/75 split. At 1440px the sidebar wrapper measured 292.5px and the body wrapper 780px, including their gutters; the inner body width was 750px.

The important site-specific detail is that **the sidebar stacks above the body at widths up to 991px**. The tablet view is not a miniature two-column layout. At 1000px outer viewport, accounting for scrollbars and theme/container rules, the inspection also showed the stacked arrangement. The static rebuild should check actual usable layout width around this boundary rather than assuming a nominal screenshot width guarantees two columns.

The standard article starts with about 70px top padding on desktop. Sidebar widgets are separated by generous vertical spacing. At mobile size the main panel is full-width, with no negative overlap, rounded corners or raised outer shadow; the article uses about 30px vertical padding and 15px horizontal content gutters. The contact/sidebar content comes before the page-specific text, even when that pushes the latter below the first screen.

### 2.5 Content patterns

**Standard text page:** shared shell and sidebar; paragraphs, headings and occasional bullet lists. The hero already supplies an H1, but Kontakt, Impressum, Datenschutz, Disclaimer and Aktuelles also have body H1 headings. Preserve those existing duplicates in a faithful transcription; changing the heading hierarchy later is an explicit accessibility/editorial improvement.

**Section/category index:** ordinary text links or a simple bulleted link list, not illustrated cards. Referenzen has an introductory sentence followed by separate category links. Leistungsspektrum is a list of five links. Ingenieurbau adds a linked bridge photograph with the caption “Lockwitz – Talbrücke bei Dresden”. The other category indexes are mainly link lists.

**Reference detail:** a lead photograph, a four-row two-column project facts table, zero or more additional photographs, then three pill-shaped navigation links: “Vorherige”, “Alle Referenzen”, “Nächste”. The table labels are normally “Objekt:”, “Bauherr:”, “Auftraggeber:” and “Leistungen:”. Paragraphs, explicit breaks, bold emphasis and result figures inside the wide second cell matter. The tables span the body width, use collapsed borders, about 9px cell padding and 1px current-text-color borders (`#3c4858` in the inspected page). They are not zebra-striped and have no source header row. The blank Markdown table header in the transcripts is only a Markdown-formatting aid, not additional displayed source content. The narrow label column is content-sized, not always exactly the same percentage.

Content images retain aspect ratio, fit within the available column (`max-width:100%; height:auto`) and are generally left-aligned, without the badge shadows. Portrait-oriented construction photos are deliberately tall. Images are independent full-width blocks in source order, not a slider or a lightbox gallery. Only the Ingenieurbau overview image and the broken agency image are wrapped in explicit body links. No active content-image lightbox was found.

The table wrapper has horizontal overflow set to `auto`, and the table uses automatic column layout. Narrow layouts retain the two-column facts structure, with text wrapping or horizontal scrolling as necessary; there is no mobile conversion into separate labeled cards.

Reference navigation uses flex layout and wrapping, with a 9px gap in the inspected desktop page. Pills have `border-radius:9999px`, white text, dark gray fill, and padding of approximately 14px vertically and 26px horizontally at desktop body size. They are links, not form-submit buttons. Previous/next links at the ends of a project category return to that category page; categories do not necessarily connect into one global linear sequence. The exact targets are retained in each transcript, including an irregular link in the Gutachten sequence.

**Biography:** an H4 name, office portrait, a chronological bullet list with bold dates and a nested list under 2008, then a second construction-site portrait.

**Contact:** body H1, short contact text, a bold email link and a parenthetical explanation that the former contact form was removed. It is not a functioning form.

**Legal:** long plain text with bold/italic labels; no accordions, tabs or PDF downloads. The Impressum contains a nonloading legacy agency image. The privacy text includes statements about Google Maps, Webfonts and Facebook, but the inspected site contains no corresponding embedded map/Facebook UI; these statements are legacy page content, not evidence to add those features.

**Empty pages:** Über Uns, Adjudikation and Seminare & Schulungen have an empty page-specific body, but still render the hero, contact sidebar and footer. Do not invent summaries for them. The sitemap-only Blog has an empty posts area and no sidebar. Referenz-Template and Sample Page contain publicly served placeholder content and are inventoried as such.

### 2.6 Responsive behavior and interaction

| Range / state | Existing behavior |
|---|---|
| Wide desktop, e.g. 1440px | Centered logo above a single-row main menu; side-by-side contact sidebar and body; raised panel and photographic hero |
| Intermediate desktop/tablet | Menu wraps if needed; sidebar stacks above body when the grid breakpoint is crossed; all body content remains present |
| Up to 768px | Logo aligns left; right-hand three-stroke hamburger; 70px white navbar; main menu collapsed; hero title 26px; 16px body; full-width unraised main panel |
| Mobile menu open | White fixed dropdown panel below the header; vertically stacked navigation, separately expandable submenus, scrolling when content exceeds viewport height |
| Dropdowns | Desktop hover/focus disclosure; keyboard-focusable caret controls; on mobile, caret toggles the submenu separately from following the parent link |
| Active page | Active subpage uses accent color; keep exact route identity even for pages with the same “Gutachten” title |
| Search open | Desktop magnifier toggles a focused search field; mobile menu exposes the search form directly |
| After scrolling | Navbar compacts and sticks; gray circular back-to-top button becomes visible near the lower right |

The search form is a GET request to `/` with parameter `s`. Its label is “Suchen nach:”, placeholder “Suchen …” and submit value “Suchen”. It relies on WordPress server-side search; a static rebuild needs an explicit replacement or an intentional documented removal, not a form that silently stops working. Arbitrary search-query results are dynamic states, not additional authored pages in this inventory.

The hamburger's assistive label is “Navigation umschalten”. Caret controls use “Open Submenu” in the source. The back-to-top title is `„Nach oben scrollen“ aktivieren`; it is a roughly 50px gray circle, 15px from the right and bottom, with a white double up-chevron SVG. It appears after passing approximately the current hero height, fades in, and scrolls smoothly to the top when clicked.

The search magnifier, dropdown chevrons, hamburger strokes and double up-chevron are vector/CSS interface graphics, not uploads; the raster-image table must not be mistaken for an inventory of those controls. Source icons use inline SVG paths and CSS. Avoid bringing in a whole icon-font dependency just to reproduce them.

The original has many empty `alt` attributes, repeated H1s, small controls and low-contrast utility text. These are existing conditions, not recommended accessibility standards. Appropriate alt text, keyboard disclosure state and focus visibility should be addressed deliberately during implementation without changing factual content.

## 3. Shared content and navigation

### 3.1 Site identity and metadata

Site name: **ABC Abel Bau-Consulting**  
Tagline: **Bauen mit Gewinn!**  
Language: German (`lang="de"`), except the published English Sample Page.  
Homepage document title: `ABC Abel Bau-Consulting – Bauen mit Gewinn!`  
Other page document titles: `<page title> – ABC Abel Bau-Consulting`.

The header logo is [IMG-004](#img-004). Browser favicon/touch/tile graphics are [IMG-003](#img-003), supplied in the four exact sizes listed in section 6.

### 3.2 Utility strip

The visible contact line, with spacing between its parts:

```text
Hauptstraße 27a, 35435 Wettenberg   info@abc-bauconsulting.de   Tel: 0641 96968-30
```

| Label | Destination / behavior |
|---|---|
| Hauptstraße 27a, 35435 Wettenberg | `https://goo.gl/maps/6c4mciL32HP26Yr98` |
| info@abc-bauconsulting.de | `mailto:info@abc-bauconsulting.de` |
| Tel: 0641 96968-30 | Plain text, not a `tel:` link in the source |
| Kontakt | `/kontakt/` |
| Impressum | `/impressum/` |
| Datenschutz | `/datenschutz/` |

### 3.3 Primary menu

Labels are shown uppercase by CSS; title case below records the underlying text. Preserve this order and nesting. Parent items are clickable pages in their own right.

| Menu label / nesting | Route |
|---|---|
| Startseite | `/` |
| Leistungsspektrum | `/leistungsspektrum-2/` |
| ↳ Warum Baubetriebsberatung? | `/warum-baubetriebsberatung/` |
| ↳ Leistungen für Auftragnehmer | `/leistungen-fuer-auftragnehmer/` |
| ↳ Leistungen für Auftraggeber | `/leistungen-fuer-auftraggeber/` |
| ↳ Gutachten | `/gutachten/` |
| ↳ Außergerichtliche Streitbeilegung | `/aussergerichtliche-streitbeilegung/` |
| Über Uns | `/ueber-uns/` |
| ↳ Ihr Berater | `/ihr-berater/` |
| ↳ Unser Standort | `/unser-standort/` |
| Referenzen | `/referenzen/` |
| ↳ Ingenieurbau | `/ingenieurbau/` |
| ↳ Spezialtiefbau | `/spezialtiefbau/` |
| ↳ Hochbau & Schlüsselfertigbau | `/hochbau-schluesselfertigbau/` |
| ↳ Tiefbau & Straßenbau | `/tiefbau-strassenbau/` |
| ↳ Gutachten | `/gutachten-2/` |
| ↳ Beweisfähige Baustellendokumentationen | `/beweisfaehige-baustellendokumentationen/` |
| ↳ Adjudikation | `/adjudikation/` |
| Seminare & Schulungen | `/seminare-schulungen/` |
| ↳ Aktuelles | `/aktuelles/` |
| ↳ Allgemeine Übersicht | `/allgemeine-uebersicht/` |
| Kontakt | `/kontakt/` |
| Impressum | `/impressum/` |
| ↳ Datenschutz | `/datenschutz/` |
| ↳ Disclaimer | `/disclaimer/` |

### 3.4 Contact/credential sidebar

All standard pages, including empty landing pages, display this sidebar. `/blog/` is the exception.

Heading:

```text
ABC Abel Bau – Consulting
```

Contact list, in order:

```text
Hauptstraße 27a, 35435 Wettenberg
info@abc-bauconsulting.de
Tel: 0641 96968-30
Fax: 0641 96968-31
```

The address links to `https://goo.gl/maps/6c4mciL32HP26Yr98`; the email links to `mailto:info@abc-bauconsulting.de`. Telephone and fax are plain text. The list has no visible bullet markers in the widget.

Below it is a small legacy WordPress gallery configured for three equal-width slots, but containing only **two** credential images, hence leaving unused space. The first is [IMG-012](#img-012), declared 74 × 73px, captioned **IHK.de**. The caption links in a new tab (`rel="noreferrer noopener"`) to:

```text
https://svv.ihk.de/svw-suche/4931566/suche-extern?plz=35435&ort=Wettenberg&isConcreteOrt=false&umkreis=0&suchbegriffe=Abel,%20Volker
```

The second is [IMG-061](#img-061), source thumbnail 150 × 150px, captioned **DGA-Bau.de**. Its caption links in a new tab to:

```text
https://www.dga-bau.de/streitloeserliste
```

These are not a row of client/project logos. The images have 6px rounded corners and a conspicuous soft layered shadow:

```css
box-shadow:
  0 16px 38px -12px rgba(0,0,0,.56),
  0 4px 25px 0 rgba(0,0,0,.12),
  0 8px 10px -5px rgba(0,0,0,.20);
```

Caption links sit below the images and wrap when their gallery slot is narrow. On stacked layouts the gallery still uses a proportion of the much wider sidebar area; do not stretch the original IHK mark to the full article width.

Last is [IMG-002](#img-002): **“Bauen mit Gewinn!”** in red handwritten lettering on a gray rectangle. The source uses its 300 × 47px derivative, constrained to available width; the original referenced alternative is 385px wide. There is no link or separate caption. The slogan is text inside the raster image, not a missing text paragraph.

### 3.5 Footer

Footer links, in this order, are visually uppercase:

```text
Kontakt   Impressum   Datenschutz
```

Destinations are `/kontakt/`, `/impressum/`, `/datenschutz/`. The right-hand theme credit is:

```text
Hestia | Entwickelt von ThemeIsle
```

“ThemeIsle” links to `https://themeisle.com` with `rel="nofollow"`. There is no additional copyright year or company-address column. Footer navigation and credit are left/right aligned when space allows and center/stack on narrower layouts. Padding is about 30px at top, with an 18–26px lower region depending on breakpoint.

## 4. Complete page catalog

The catalog includes all pages in the WordPress page sitemap. “Linked” means discoverable from recursive internal page links; “sitemap only” means published but not linked from the normal menu/content graph. Every row links to its full transcription in section 5.

| ID / transcript | Page / hero H1 | Route | Pattern | Hero image | Discovery |
|---|---|---|---|---|---|
| [P01](#page-p01) | Startseite | `/` | Standard page | [IMG-005](#img-005) | Linked |
| [P02](#page-p02) | Leistungsspektrum | `/leistungsspektrum-2/` | Standard page | [IMG-009](#img-009) | Linked |
| [P03](#page-p03) | Warum Baubetriebsberatung? | `/warum-baubetriebsberatung/` | Standard page | [IMG-009](#img-009) | Linked |
| [P04](#page-p04) | Leistungen für Auftragnehmer | `/leistungen-fuer-auftragnehmer/` | Standard page | [IMG-009](#img-009) | Linked |
| [P05](#page-p05) | Leistungen für Auftraggeber | `/leistungen-fuer-auftraggeber/` | Standard page | [IMG-009](#img-009) | Linked |
| [P06](#page-p06) | Gutachten | `/gutachten/` | Standard page | [IMG-009](#img-009) | Linked |
| [P07](#page-p07) | Außergerichtliche Streitbeilegung | `/aussergerichtliche-streitbeilegung/` | Standard page | [IMG-009](#img-009) | Linked |
| [P08](#page-p08) | Über Uns | `/ueber-uns/` | Empty landing page | [IMG-064](#img-064) | Linked |
| [P09](#page-p09) | Ihr Berater | `/ihr-berater/` | Standard page | [IMG-064](#img-064) | Linked |
| [P10](#page-p10) | Unser Standort | `/unser-standort/` | Standard page | [IMG-064](#img-064) | Linked |
| [P11](#page-p11) | Referenzen | `/referenzen/` | Standard page | [IMG-010](#img-010) | Linked |
| [P12](#page-p12) | Ingenieurbau | `/ingenieurbau/` | Standard page | [IMG-067](#img-067) | Linked |
| [P13](#page-p13) | BAB A 17, Lockwitz – Talbrücke bei Dresden | `/bab-a-17-lockwitz-talbruecke-bei-dresden/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P14](#page-p14) | BAB A 38, Steinbach – Talbrücke bei Heiligenstadt/Thür. | `/bab-a-38-steinbach-talbruecke-bei-heiligenstadt-thuer/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P15](#page-p15) | BAB A 71, Saale – Talbrücke bei Bad Neustadt/S. | `/bab-a-71-saale-talbruecke-bei-bad-neustadt-s/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P16](#page-p16) | BAB A 71, Thalwasser-Talbrücke bei Münnerstadt/Ufr. | `/bab-a-71-thalwasser-talbruecke-bei-muennerstadt-ufr/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P17](#page-p17) | BAB A 4, Teufelstalbrücke (Nord) bei Hermsdorfer Kreuz/Thür. | `/bab-a-4-teufelstalbruecke-nord-bei-hermsdorfer-kreuz-thuer/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P18](#page-p18) | L 3012, Abbruch und Neubau von 2 Brücken bei Trebur/Hessen | `/l-3012-abbruch-und-neubau-von-2-bruecken-bei-trebur-hessen/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P19](#page-p19) | BAB A2, BW 683 bei Hannover | `/bab-a2-bw-683-bei-hannover/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P20](#page-p20) | Spezialtiefbau | `/spezialtiefbau/` | Standard page | [IMG-067](#img-067) | Linked |
| [P21](#page-p21) | B 29, Ortsumgehung Schwäbisch Gmünd, Trogbauwerk | `/b-29-ortsumgehung-schwaebisch-gmuend-trogbauwerk/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P22](#page-p22) | Hochbau & Schlüsselfertigbau | `/hochbau-schluesselfertigbau/` | Standard page | [IMG-067](#img-067) | Linked |
| [P23](#page-p23) | Westpfalz-Klinikum Kaiserslautern, Hs. 7 mit Hubschrauberlandeplattform | `/westpfalz-klinikum-kaiserslautern-hs-7-mit-hubschrauberlandeplattform/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P24](#page-p24) | Umbau Dachgeschoss in hochwertige Wohnung, inkl. Aufzuganlage | `/umbau-dachgeschoss-in-hochwertige-wohnung-inkl-aufzuganlage/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P25](#page-p25) | Neubau Kleintier- u. Vogelklinik,Universität Gießen | `/neubau-kleintier-u-vogelklinikuniversitaet-giessen/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P26](#page-p26) | Flughafen Frankfurt, Terminal 3 | `/flughafen-frankfurt-terminal-3/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P27](#page-p27) | Tiefbau & Straßenbau | `/tiefbau-strassenbau/` | Standard page | [IMG-067](#img-067) | Linked |
| [P28](#page-p28) | Wasserversorgung US-Liegenschaften Sembach, Los 1 | `/wasserversorgung-us-liegenschaften-sembach-los-1/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P29](#page-p29) | Wasserversorgung US-Liegenschaften Sembach, Los 2 | `/wasserversorgung-us-liegenschaften-sembach-los-2/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P30](#page-p30) | Tiefbauarbeiten für Erweiterung Universitätsgebäude | `/tiefbauarbeiten-fuer-erweiterung-universitaetsgebaeude/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P31](#page-p31) | Infrastrukturarbeiten für Kompost.- u. Vergärungsanlage | `/infrastrukturarbeiten-fuer-kompost-u-vergaerungsanlage/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P32](#page-p32) | Trassenumlegung mit Straßenbau (innerstädtisch) | `/trassenumlegung-mit-strassenbau-innerstaedtisch/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P33](#page-p33) | Bahnhof Ffm-Höchst (Umgestaltung Bahnhofsareal) | `/bahnhof-ffm-hoechst-umgestaltung-bahnhofsareal/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P34](#page-p34) | Univers. Marburg – Neubau Bibliothek (Außenanlage) | `/univers-marburg-neubau-bibliothek-aussenanlage/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P35](#page-p35) | Univers. Marburg, Neubau Dokument.-zentrum (Außenanlagen) | `/univers-marburg-neubau-dokument-zentrum-aussenanlagen/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P36](#page-p36) | Gutachten | `/gutachten-2/` | Standard page | [IMG-067](#img-067) | Linked |
| [P37](#page-p37) | Mängelbeseitigungskosten bei MF – Wohnhaus (Privatgutachten) | `/maengelbeseitigungskosten-bei-mf-wohnhaus-privatgutachten/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P38](#page-p38) | Gegengutachten zu gerichtl. Sachverständigengutachten | `/gegengutachten-zu-gerichtl-sachverstaendigengutachten/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P39](#page-p39) | Institut für Hirnforschung (MPI), Frankfurt a. M. | `/institut-fuer-hirnforschung-mpi-frankfurt-a-m/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P40](#page-p40) | 2 Hochhäuser mit 60 Wohnanlagen, Frankfurt/M. | `/2-hochhaeuser-mit-60-wohnanlagen-frankfurt-m/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P41](#page-p41) | Instandsetzung Stützwand, Alter Botanischer Garten, Marburg/L. | `/instandsetzung-stuetzwand-alter-botanischer-garten-marburg-l/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P42](#page-p42) | Beweisfähige Baustellendokumentationen | `/beweisfaehige-baustellendokumentationen/` | Standard page | [IMG-067](#img-067) | Linked |
| [P43](#page-p43) | Westpfalzklinikum Kaiserslautern, Neubau der Bettenhäuser 3 & 4 | `/westpfalzklinikum-kaiserslautern-neubau-der-bettenhaeuser-3-4/` | Reference detail | [IMG-067](#img-067) | Linked |
| [P44](#page-p44) | Adjudikation | `/adjudikation/` | Empty landing page | [IMG-067](#img-067) | Linked |
| [P45](#page-p45) | Seminare & Schulungen | `/seminare-schulungen/` | Empty landing page | [IMG-011](#img-011) | Linked |
| [P46](#page-p46) | Aktuelles | `/aktuelles/` | Standard page | [IMG-011](#img-011) | Linked |
| [P47](#page-p47) | Allgemeine Übersicht | `/allgemeine-uebersicht/` | Standard page | [IMG-011](#img-011) | Linked |
| [P48](#page-p48) | Kontakt | `/kontakt/` | Standard page | [IMG-008](#img-008) | Linked |
| [P49](#page-p49) | Impressum | `/impressum/` | Standard page | [IMG-007](#img-007) | Linked |
| [P50](#page-p50) | Datenschutz | `/datenschutz/` | Standard page | [IMG-007](#img-007) | Linked |
| [P51](#page-p51) | Disclaimer | `/disclaimer/` | Standard page | [IMG-007](#img-007) | Linked |
| [P52](#page-p52) | Referenz-Template | `/referenz-template/` | Published reference template | [IMG-067](#img-067) | Sitemap only |
| [P53](#page-p53) | Blog | `/blog/` | Empty blog; no sidebar | [IMG-067](#img-067) | Sitemap only |
| [P54](#page-p54) | Sample Page | `/sample-page/` | Published sample page | [IMG-067](#img-067) | Sitemap only |

## 5. Page-by-page layout and complete content

Each section inherits all shared content in section 3 unless stated otherwise. The hero H1 is recorded separately from the body transcript. Every reference's photographs appear in their original order, and all project table fields and previous/next destinations are preserved.

<a id="page-p01"></a>
### P01. Startseite

**URL:** <https://abc-bauconsulting.de/>  
**Document title:** ABC Abel Bau-Consulting – Bauen mit Gewinn!  
**Hero H1:** Startseite  
**Hero image:** [IMG-005](#img-005) — `/2020/09/Kopfbild_Start.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Complete body, in source order:**

```markdown
## Herzlich Willkommen!

##### Wenn Sie es bis hierher geschafft haben, besteht große Hoffnung, dass wir gemeinsam die Abwicklung Ihres Bauauftrags zu einem positiven Ende bringen. Unsere Kernkompetenz liegt in der Lösung von baubetrieblichen Aufgabenstellungen wie:

- baubegleitendes Vertrags und Nachtragsmanagement für Auftragnehmer und Auftraggeber
- professionelle Erstellung oder Prüfung von Nachträgen
- Sachverständige Ermittlung von Forderungen und Prüfung von Ansprüchen aus gestörtem Bauablauf
- gutachtliche Prüfung von Bauabrechnungen mit Aufdeckung weiterer Abrechnungspotentiale
- baubegleitende Termin- und Kostenüberwachung für Auftragnehmer und Auftraggeber
- aktive Unterstützung bei der Einführung eines systematischen Nachtragserfassungssystems im Bauunternehmen
- Einführung und Überwachung einer beweisfähigen Baustellendokumentation für Auftragnehmer und Auftraggeber
- umfassende baubetriebliche Beratungsleistungen
- Seminare und Schulungen, auch firmenspezifisch, zu den bauvertraglichen Schwerpunkten
- Erstattung von Sachverständigengutachten
- außergerichtliche Streitbeilegung

![IMG-006][IMG-006]
```

**Body heading levels:** H2: Herzlich Willkommen!; H5: Wenn Sie es bis hierher geschafft haben, besteht große Hoffnung, dass wir gemeinsam die Abwicklung Ihres Bauauftrags zu einem positiven Ende bringen. Unsere Kernkompetenz liegt in der Lösung von baubetrieblichen Aufgabenstellungen wie:.

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-006](#img-006) | `/2020/09/Volker.jpg` | 440 × 381 | Empty | None |

<a id="page-p02"></a>
### P02. Leistungsspektrum

**URL:** <https://abc-bauconsulting.de/leistungsspektrum-2/>  
**Document title:** Leistungsspektrum – ABC Abel Bau-Consulting  
**Hero H1:** Leistungsspektrum  
**Hero image:** [IMG-009](#img-009) — `/2020/10/Kopfbild_Leistungsspektrum.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Complete body, in source order:**

```markdown
- [Warum Baubetriebsberatung?](https://abc-bauconsulting.de/warum-baubetriebsberatung/)
- [Leistungen für Auftragnehmer](https://abc-bauconsulting.de/leistungen-fuer-auftragnehmer/)
- [Leistungen für Auftraggeber](https://abc-bauconsulting.de/leistungen-fuer-auftraggeber/)
- [Gutachten](https://abc-bauconsulting.de/gutachten/)
- [Außergerichtliche Streitbeilegung](https://abc-bauconsulting.de/aussergerichtliche-streitbeilegung/)
```

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Warum Baubetriebsberatung? | `https://abc-bauconsulting.de/warum-baubetriebsberatung/` | Same as href | Same tab |
| Leistungen für Auftragnehmer | `https://abc-bauconsulting.de/leistungen-fuer-auftragnehmer/` | Same as href | Same tab |
| Leistungen für Auftraggeber | `https://abc-bauconsulting.de/leistungen-fuer-auftraggeber/` | Same as href | Same tab |
| Gutachten | `https://abc-bauconsulting.de/gutachten/` | Same as href | Same tab |
| Außergerichtliche Streitbeilegung | `https://abc-bauconsulting.de/aussergerichtliche-streitbeilegung/` | Same as href | Same tab |

<a id="page-p03"></a>
### P03. Warum Baubetriebsberatung?

**URL:** <https://abc-bauconsulting.de/warum-baubetriebsberatung/>  
**Document title:** Warum Baubetriebsberatung? – ABC Abel Bau-Consulting  
**Hero H1:** Warum Baubetriebsberatung?  
**Hero image:** [IMG-009](#img-009) — `/2020/10/Kopfbild_Leistungsspektrum.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P02](#page-p02) — `/leistungsspektrum-2/`.

**Complete body, in source order:**

```markdown
Die erfolgreiche Umsetzung eines Bauprojekts im Spannungsfeld **Termine** – **Kosten** – **Technik** erfordert heutzutage von den Beteiligten auch detaillierte betriebswirtschaftliche und baurechtliche Kenntnisse. Ein nachhaltig erfolgreiches Bestehen unter den Bedingungen der wettbewerblichen Auftragsakquisen bzw. -vergaben ist ohne Beachtung der baubetrieblichen Zusammenhänge nicht möglich. Dies gilt gleichermaßen für Auftragnehmer und Auftraggeber.

Die Geltendmachung von Ansprüchen aus dem Bauvertrag und deren Realisierung ist dabei für alle Vertragspartner von entscheidender Bedeutung. Gerade hier, bei der Erkennung, Sicherung, Aufbereitung und Durchsetzung von Ansprüchen, d.h. im **Nachtragsmanagement** (Claim-Management) liegt unsere Kompetenz.

Unsere Arbeit erfolgt auf den Grundlagen unserer Erfahrung, einer sachverständigen und damit sachorientierten sowie objektiven Herangehensweise und immer unter Einbindung Ihrer Planungs- und Ausführungsvorgaben sowie Ihrer projektbeteiligten Personen, von der Geschäftsleitung bis zum Polier oder Bauüberwacher auf der Baustelle.

Auf den nächsten Seiten erfahren Sie, welche Leistungen wir in diesem Sinne für Ihr Bauprojekt anbieten können.
```

<a id="page-p04"></a>
### P04. Leistungen für Auftragnehmer

**URL:** <https://abc-bauconsulting.de/leistungen-fuer-auftragnehmer/>  
**Document title:** Leistungen für Auftragnehmer – ABC Abel Bau-Consulting  
**Hero H1:** Leistungen für Auftragnehmer  
**Hero image:** [IMG-009](#img-009) — `/2020/10/Kopfbild_Leistungsspektrum.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P02](#page-p02) — `/leistungsspektrum-2/`.

**Complete body, in source order:**

```markdown
**• Nachtragsmanagement (Claim-Management)**  
Beinhaltet das Erkennen, Beschreiben, Begründen und vertragskonformes Kalkulieren von Sach-Nachträgen. Mitwirkung bei Nachtragsverhandlungen mit Darlegungen und Erläuterungen zur Sache. Argumentative Unterstützung des Auftragnehmers.

**• Gestörter Bauablauf**  
Bearbeitung von Bauablaufstörungen aus AG-seitigen Ursachen. Erstellung eines Soll-Bauablaufplanes mit Darstellung des geplanten Bauablaufs, der kalkulierten Ressourcen, sowie der technologischen und kapazitiven Zusammenhänge. Ermittlung eines resultierenden Bauzeitverlängerungsanspruchs des Auftragnehmers unter Beachtung der rechtlichen Anforderungen. Berechnung des Mehrkostenanspruchs aus Gestörtem Bauablauf.

**• Aufdeckung Abrechnungspotentiale aus VOB-Verträgen**  
Überprüfung von Mengenberechnungen auf Basis Vertrag und VOB/C. Abrechnung gekündigter oder teilgekündigter Bauverträge. Neuerstellung strittiger Mengenberechnungen und Abrechnungen. Prüfung auf bisher nicht geltend gemachte Nachtrags-Sachverhalte. Ausgleichsberechnung nach §2 Abs. 3 VOB/B.

**• Abwehr unberechtigter Vertragsstrafen- und Schadensersatzforderungen**  
mit Beratung zu vertragskonformen und interessensgerechtem Handeln bei Schriftverkehr, Besprechungen und in Verhandlungen.

**• Nachtragserfassungs-/Nachtragsmeldesystem**  
Installation eines umfassenden Nachtragserfassungssystems bzw. Optimierung vorhandener betrieblicher Verfahren zur Behandlung außervertraglicher Leistungen. Überwachung der Umsetzung dieses Systems bis zur erfolgreichen Etablierung im Unternehmen.

**• Beweisfähige Dokumentation von Bauabläufen**  
Vorgabe von Konzepten und Werkzeugen zur Dokumentation von Bauleistungen für spätere Beweiszwecke, als Ersatz der üblichen Bautagesberichte.  
Hierdurch Erfassung von ausgeführten LV- oder Nachtragsleistungen mit Kolonneneinsatz, Arbeitsdauer und Tagesleistungen. Im Vergleich zur „ungestörten“ Bauausführung sind hiermit u.a. Produktivitätsverluste infolge Störungen nachweisbar. Überwachung der Umsetzung durch die Baustellen.

Wie eine beweisfähige Baustellendokumentation aussehen kann, erfahren Sie [*hier*](https://abc-bauconsulting.de/beweisfaehige-baustellendokumentationen/).

**• Schulung von Führungspersonal**  
Praxisgerechte Schulungen von Führungspersonal (Projektleiter, Kalkulatoren, Bauleitern, Polieren etc.) zur Sensibilisierung und Weiterbildung in wesentlichen baubetrieblichen Aspekten für das Tagesgeschäft. Durchführung vor Ort an der Baustelle oder im Firmensitz der Bauunternehmung.

**• Baubegleitende Baubetriebsberatung**  
Empfehlenswert ist die frühzeitige Einschaltung eines baubetrieblichen Beraters, damit die fast immer entstehenden Vertragsänderungen zeitnah aufgearbeitet und beauftragt werden können, da nur so der betriebswirtschaftlich zwingend notwendige Zahlungsfluß erreicht werden kann. Des Weiteren wird die erfahrungsgemäß eher zögerliche Akzeptanz und Bearbeitung von Nachforderungen, bei einer verspäteten Geltendmachung bei dem AG, hierdurch vermieden.  
Vertragsergänzungen sollten zeitnah, jedenfalls innerhalb der Bauzeit, da verhandelt werden wo sie entstanden sind: **auf der Baustelle**.
```

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| hier | `https://abc-bauconsulting.de/beweisfaehige-baustellendokumentationen/` | Same as href | Same tab |

<a id="page-p05"></a>
### P05. Leistungen für Auftraggeber

**URL:** <https://abc-bauconsulting.de/leistungen-fuer-auftraggeber/>  
**Document title:** Leistungen für Auftraggeber – ABC Abel Bau-Consulting  
**Hero H1:** Leistungen für Auftraggeber  
**Hero image:** [IMG-009](#img-009) — `/2020/10/Kopfbild_Leistungsspektrum.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P02](#page-p02) — `/leistungsspektrum-2/`.

**Complete body, in source order:**

```markdown
**• Nachtragsmanagement (Claim-Management)**  
Prüfung von Nachträgen auf vertraglichen und baubetrieblichen Grundlagen.  
Erstellung Gutachtlicher Stellungnahmen mit Bewertung Anspruchsgrundlage, Plausibilitätsprüfung der  
AN-Forderungen in preislicher Hinsicht und in den Auswirkungen auf den Bauablauf.  
Prüfung unter Beachtung auftraggeberseitiger Regelwerke, wie VHB, HVA-StB u.a.  
Darlegung der Prüfungsergebnisse in Verhandlungen und argumentative Unterstützung des Auftraggebers.  
Operative Beratung des Auftraggebers in Bezug auf ein wirtschaftliches und vertragsgerechtes Handeln.

**• Gestörter Bauablauf**  
Sachgerechte Prüfung von auftragnehmerseitigen Forderungen hinsichtlich Anspruchsgrundlage, Kausalitätsnachweisen sowie auf Berechnungsmethodik der Mehrkosten.  
Untersuchung auf, vom Auftragnehmer, selbst verursachte Verzüge.

**• Kostenmanagement**  
Erstellung und Aktualisierung eines sogenannten Kostencontrolling unter Einbeziehung Nachträge, Mengenänderungen, Gegenforderungen und gegebenenfalls Sondernachträgen.

**• Dokumentation der Arbeitsabläufe**  
Durchführung von Zeitstudien mit Leistungserfassung zur Ermittlung von Ist-Leistungen an der Baustelle.  
Hieraus Schlussfolgerungen für den Bauablauf.

**• Abrechnungs- bzw. Rechnungsprüfung**  
Vertragskonforme Prüfung von Abrechnungsunterlagen.  
Aufdeckung von Berechnungsfehlern.  
Termingerechte Rechnungsprüfung zur Sicherstellung der vertraglichen Zahlungsfristen.

**• Prüfung von Ausschreibungsunterlagen auf Schwachstellen**  
Prüfung der Leistungsbeschreibung auf Unstimmigkeiten, Fehler, Plausibilität der Mengen, Terminschiene etc.  
Prüfung der Ausschreibungsunterlagen auf Übereinstimmung mit VOB/A und VOB/C.  
Prüfung aus „Blickwinkel“ der späteren Anbieter.

**• Baubegleitende Baubetriebsberatung**  
Durch rechtzeitige Einschaltung eines baubetrieblichen Beraters werden die vertraglichen Handlungen/Entscheidungen des Auftraggebers in ihren Auswirkungen frühzeitig planbar. Die Gefahr verspäteter oder objektiv falscher Entscheidungen wird vermindert, bzw. eliminiert. Kostensteigerungen und/oder Terminverlängerungen sind nicht grundsätzlich auszuschließen; sie bleiben aber maßgeblich beeinfluss- und somit steuerbar.

Der Auftraggeber heißt nicht nur Bauherr, er bleibt es auch.
```

<a id="page-p06"></a>
### P06. Gutachten

**URL:** <https://abc-bauconsulting.de/gutachten/>  
**Document title:** Gutachten – ABC Abel Bau-Consulting  
**Hero H1:** Gutachten  
**Hero image:** [IMG-009](#img-009) — `/2020/10/Kopfbild_Leistungsspektrum.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P02](#page-p02) — `/leistungsspektrum-2/`.

**Complete body, in source order:**

```markdown
Die Erstattung von Gutachten setzt u. a. eine besondere Sachkunde voraus, welche im Zusammenhang mit einer öffentlichen Bestellung durch eine Prüfung nachzuweisen ist.  

Herr Abel wurde in 2008 durch die Industrie- und Handelskammer Lahn – Dill für das  
baubetriebliche Sachgebiet

**Baupreisermittlung und Abrechnung im Hoch- und Ingenieurbau sowie Bauablaufstörungen**

[http://svv.ihk.de](http://svv.ihk.de/svv/content/home/sachverstaendiger.ihk?OID=12446)

bestellt und vereidigt. Seither erfolgt die Erstattung auch von Gerichtsgutachten im Zusammenhang von Bauprozessen mit baubetrieblichen Streitpunkten. Hierunter sind vorrangig Vergütungsfragen hinsichtlich Abrechnungsmengen und Baupreisen, insbesondere von Nachträgen sowie Ansprüche aus Gestörten Bauabläufen zu verstehen.

Die gutachterliche Tätigkeit erfolgt in Form von  
• Privatgutachten ( Parteigutachten )  
• Privatgutachten ( als Gegengutachten im Prozess )  
• Gerichtsgutachten  
• Schiedsgutachten  

Aufgrund des Bürositzes sowie der Niederlassungen ist eine Registrierung bei folgenden Industrie- und Handelskammern gegeben :  
IHK Lahn – Dill  
IHK Kassel – Marburg  
IHK Rhein – Main  

Unabhängig davon ist die Erstellung von Gutachten auch bundesweit möglich.
```

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| http://svv.ihk.de | `http://svv.ihk.de/svv/content/home/sachverstaendiger.ihk?OID=12446` | Same as href | New tab |

<a id="page-p07"></a>
### P07. Außergerichtliche Streitbeilegung

**URL:** <https://abc-bauconsulting.de/aussergerichtliche-streitbeilegung/>  
**Document title:** Außergerichtliche Streitbeilegung – ABC Abel Bau-Consulting  
**Hero H1:** Außergerichtliche Streitbeilegung  
**Hero image:** [IMG-009](#img-009) — `/2020/10/Kopfbild_Leistungsspektrum.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P02](#page-p02) — `/leistungsspektrum-2/`.

**Complete body, in source order:**

```markdown
Der häufig für alle Parteien unbefriedigende Verlauf und das Ergebnis von Baustreitigkeiten verlangen nach Alternativen zu Gerichtsprozessen.  
Derzeit bestehen bei Streitigkeiten folgende Möglichkeiten :  

• Verfahren nach § 18 Abs. 2, VOB/B (sofern Umsetzbar)  
• Schiedsgerichtsverfahren (sofern vertraglich vereinbart)  
• Mediation (gem. Mediationsgesetz)  
• Bauverfügung (nach § 650d BGB)   
• Adjudikation (gem. Mediationsgesetz bzw. § 18 Abs. 3, VOB/B)  

Aus diesem Pool von Streitbeilegungsmöglichkeiten erscheint, nicht nur uns, das **Adjudikationsverfahren** das mit Abstand zielführendste Konzept zu sein. Bereits 2010 empfahl der Deutsche Baugerichtstag e.V., dieses Verfahren auf gesetzlicher Basis einzuführen.  

Bei dem Adjudikationsverfahren erfolgt auf Antrag des Auftraggebers oder des Auftragnehmers die Einschaltung eines sog. Adjudikators, welcher baubegleitend und innerhalb kurzer Zeit eine begründete Entscheidung im Streitfall fällt. Diese Entscheidung soll vorläufig bindend sein, kann aber durch die „unterlegene“ Seite in einem anschließenden Gerichtsverfahren überprüft und gfls. aufgehoben werden. In 2013 erfolgte die Vorlage eines umfassenden Rechtsgutachtens, in welchem die grundsätzliche verfassungsrechtliche Möglichkeit zur Einführung des Adjudikationsverfahrens bestätigt wird. Zur Umsetzung des Verfahrens existieren bereits Verfahrensordnungen, welche jedoch wegen der fehlenden gesetzlichen Regelung immer individuell im Vertrag vereinbart werden müssen (Vertragliche Adjudikation).  

Bei einer vereinbarten vertraglichen Adjudikation wäre folgender Ablauf denkbar :  
Tag 1:   
Stellung des Antrags auf Adjudikation durch AN (z. B. wegen Streitigkeiten über Anspruch bzw. Höhe einer Nachtragsforderung) mit Begründung und Benennung Adjudikator bzw. „Adjudikatoren – Tandem“  
Tag 3:  
Bestätigung der Übernahme des Auftrags durch den Adjudikator und Aufforderung an AG, seine gegenteilige Sichtweise begründet darzulegen (Frist : 2 Wochen).  
Tag 18:   
Eingang der Stellungnahme des AG. Beginn der Ermittlungen / Untersuchungen / Recherchen durch den Adjudikator u. a. durch Ortstermine an der laufenden Baustelle, Einholung benötigter Unterlagen bei AN und/oder AG etc.  
Tag 30:  
Durchführung einer mündlichen Verhandlung des Adjudikators mit AN und AG. Hierbei Erörterung von Fragen und Sachverhaltsaufklärung mit Fristsetzung an Parteien zur Einreichung weiterer schriftlicher Darlegungen (Frist: 10 Tage). Fortsetzung der Ermittlungen durch den Adjudikator.  
Tag 40:  
Eingang der weiteren schriftlichen Darlegungen der Parteien  
Tag 41–62:  
Auswertung der weiteren Darlegungen der Parteien sowie weitere Ermittlungen nach Erfordernis  
Tag 63 (spätestens):  
Vorlage des begründeten Adjudikatorenspruchs (schriftlich, z. B. in Form einer Gutachtlichen Feststellung); gfls. auch zusätzlich mündliche Erläuterung der Entscheidung.  
Tag 74 (spätestens):  
Spätester Tag bis Eingang schriftliche Ablehnung durch AN oder AG; andernfalls gilt die Entscheidung als anerkannt und ist von den Parteien umzusetzen. Auch bei Ablehnung durch eine Seite gilt der Adjudikationsspruch als vorläufig bindend. In diesem Fall steht der unterlegenen Partei der ordentliche Rechtsweg zum Gericht frei, welches den Adjudikationsspruch im nachfolgenden Bauprozess überprüft.  

Für die Anwendung einer **vertraglichen Adjudikation** stehen diverse Adjudikationsordnungen zur Verfügung. Die Vorteile des Adjudikationsverfahrens auf einen Blick :  
• kurzfristige Entscheidung / zeitnahe Lösungen  
• kostengünstig  
• Führungspersonal der Parteien wird nicht unnötig in langwierigen Prozessen gebunden  
• Liquiditätssicherung bei AN / Kostensicherheit bei AG  
• Ermittlungen durch qualifizierten und neutralen Sachverständigen + Baujuristen (bei Tandemlösung)  
• Untersuchungen umfassender möglich wie bei gerichtl. Beweisbeschlüssen  
• alle Verhandlungen erfolgen nichtöffentlich , keine Einschaltung von Juristen auf Seiten der Parteien nötig  
• vorläufige Bindung des Spruches ; bei Nichtanerkennung jedoch gerichtlich überprüfbar  
• Kooperationspflichten der Parteien werden befördert

Wir empfehlen die Vereinbarung einer Vertraglichen Adjudikation bei allen Bauverträgen.
```

<a id="page-p08"></a>
### P08. Über Uns

**URL:** <https://abc-bauconsulting.de/ueber-uns/>  
**Document title:** Über Uns – ABC Abel Bau-Consulting  
**Hero H1:** Über Uns  
**Hero image:** [IMG-064](#img-064) — `/2021/08/54C2555_logo2_cut-scaled.jpg`  
**Pattern:** Empty landing page. Global header/menu/contact sidebar/footer.

**Body:** No page-specific text, images, list or table. The shared contact sidebar remains visible.

<a id="page-p09"></a>
### P09. Ihr Berater

**URL:** <https://abc-bauconsulting.de/ihr-berater/>  
**Document title:** Ihr Berater – ABC Abel Bau-Consulting  
**Hero H1:** Ihr Berater  
**Hero image:** [IMG-064](#img-064) — `/2021/08/54C2555_logo2_cut-scaled.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P08](#page-p08) — `/ueber-uns/`.

**Complete body, in source order:**

```markdown
#### Dipl.-Ing. Volker Abel

![IMG-059][IMG-059]

- Bauingenieurstudium an der Fachhochschule Gießen – Friedberg
- **1987 – 1989** Bauleitung bei der Fritz Herzog AG Marburg/Lahn in Hoch-, Tief- und Ingenieurbau
- **1989 – 1996** Bauleitung bei der Baugesellschaft J.G. Müller, Wetzlar mit Schwerpunkt Ingenieurbau, Instandsetzung von Verkehrsbauwerken, Hochbau
- **1996 – 1999** Mitinhaber und Geschäftsführer des Ingenieurbüro ITB, Erfurt / Wetzlar, Tätigkeiten: Bauüberwachung, Bauoberleitung, externe Firmenbauleitung
- **2000- 2004** Oberbauleitung bei der Baugesellschaft J.G. Müller, Wetzlar für Sparte Ingenieurbau/ BW- Instandsetzung sowie Abteilungsleiter  
  „Bauverträge/ Nachtragsmanagement „
- **2004** Gründung des Ing.- und Sachverständigenbüros ABC
- **2008** Öffentliche Bestellung und Vereidigung als Sachverständiger für
  - Baupreisermittlung und Abrechnung im Hoch- und Ingenieurbau
  - Bauablaufstörungendurch die Industrie- und Handelskammer Lahn-Dill [(www.svv.ihk.de)](https://svv.ihk.de/svv/content/home/sachverstaendiger.ihk?OID=12446)
- ab **2009** Mitwirkung im Arbeitskreis VII des Deutschen Baugerichtstag zum Thema „außergerichtliche Streitbeilegung“, Förderung der Einführung der [Adjudikation](https://abc-bauconsulting.de/aussergerichtliche-streitbeilegung/) zur Lösung von Baustreitigkeiten
- **2014** Mitglied in DGA–Bau (Deutsche Gesellschaft für Außergerichtliche  
  Streitbeilegung im Bauwesen e.V.)
- **2021** Aufnahme in die [Streitlöserliste der DGA-Bau](https://www.dga-bau.de/streitloeserliste) mit den Schwerpunkten Hochbau, Ingenieurbau & Öffentlich bestellte und vereidigte Sachverständige

![IMG-060][IMG-060]
```

**Body heading levels:** H4: Dipl.-Ing. Volker Abel.

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-059](#img-059) | `/2020/10/Volker_1-1024x683.jpg` | 1024 × 683 | Empty | None |
| 2 | [IMG-060](#img-060) | `/2020/10/Volker_2-scaled.jpg` | 2560 × 1707 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| (www.svv.ihk.de) | `https://svv.ihk.de/svv/content/home/sachverstaendiger.ihk?OID=12446` | Same as href | New tab |
| Adjudikation | `https://abc-bauconsulting.de/aussergerichtliche-streitbeilegung/` | Same as href | Same tab |
| Streitlöserliste der DGA-Bau | `https://www.dga-bau.de/streitloeserliste` | Same as href | New tab |

**Layout:** H4 name → office portrait → chronological list; the two qualification lines under 2008 are nested bullets → bridge-site portrait. The joined word “Bauablaufstörungendurch” is present in the source.

<a id="page-p10"></a>
### P10. Unser Standort

**URL:** <https://abc-bauconsulting.de/unser-standort/>  
**Document title:** Unser Standort – ABC Abel Bau-Consulting  
**Hero H1:** Unser Standort  
**Hero image:** [IMG-064](#img-064) — `/2021/08/54C2555_logo2_cut-scaled.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P08](#page-p08) — `/ueber-uns/`.

**Complete body, in source order:**

```markdown
Unser Büro befindet sich seit 2007 in Wettenberg bei Gießen, Region Mittelhessen. Durch diese zentrale Lage in Hessen und damit auch Deutschland können Projekte im gesamten Bundesgebiet, auch baubegleitend, betreut werden.

Unser Standort bei:

- [Google Maps](https://goo.gl/maps/6c4mciL32HP26Yr98)
- [OpenStreetMap](https://osm.org/go/0D1dX6bxp)
```

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Google Maps | `https://goo.gl/maps/6c4mciL32HP26Yr98` | Same as href | New tab |
| OpenStreetMap | `https://osm.org/go/0D1dX6bxp` | Same as href | New tab |

<a id="page-p11"></a>
### P11. Referenzen

**URL:** <https://abc-bauconsulting.de/referenzen/>  
**Document title:** Referenzen – ABC Abel Bau-Consulting  
**Hero H1:** Referenzen  
**Hero image:** [IMG-010](#img-010) — `/2020/10/Kopfbild_Referenzen.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Complete body, in source order:**

```markdown
Ein Auszug unserer Referenzobjekte, unterteilt nach unterschiedlichen Sachgebieten:

[Ingenieurbau](https://abc-bauconsulting.de/ingenieurbau/)

[Spezialtiefbau](https://abc-bauconsulting.de/spezialtiefbau/)

[Hochbau & Schlüsselfertigbau](https://abc-bauconsulting.de/hochbau-schluesselfertigbau/)

[Tiefbau & Straßenbau](https://abc-bauconsulting.de/tiefbau-strassenbau/)

[Gutachten](https://abc-bauconsulting.de/gutachten-2/)

[Beweisfähige Baustellendokumentationen](https://abc-bauconsulting.de/beweisfaehige-baustellendokumentationen/)

[Adjudikation](https://abc-bauconsulting.de/adjudikation/)
```

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Ingenieurbau | `https://abc-bauconsulting.de/ingenieurbau/` | Same as href | Same tab |
| Spezialtiefbau | `https://abc-bauconsulting.de/spezialtiefbau/` | Same as href | Same tab |
| Hochbau & Schlüsselfertigbau | `https://abc-bauconsulting.de/hochbau-schluesselfertigbau/` | Same as href | Same tab |
| Tiefbau & Straßenbau | `https://abc-bauconsulting.de/tiefbau-strassenbau/` | Same as href | Same tab |
| Gutachten | `https://abc-bauconsulting.de/gutachten-2/` | Same as href | Same tab |
| Beweisfähige Baustellendokumentationen | `https://abc-bauconsulting.de/beweisfaehige-baustellendokumentationen/` | Same as href | Same tab |
| Adjudikation | `https://abc-bauconsulting.de/adjudikation/` | Same as href | Same tab |

<a id="page-p12"></a>
### P12. Ingenieurbau

**URL:** <https://abc-bauconsulting.de/ingenieurbau/>  
**Document title:** Ingenieurbau – ABC Abel Bau-Consulting  
**Hero H1:** Ingenieurbau  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P11](#page-p11) — `/referenzen/`.

**Complete body, in source order:**

```markdown
- [BAB A 17, Lockwitz – Talbrücke bei Dresden](https://abc-bauconsulting.de/bab-a-17-lockwitz-talbruecke-bei-dresden/)
- [BAB A 38, Steinbach – Talbrücke bei Heiligenstadt/Thür.](https://abc-bauconsulting.de/bab-a-38-steinbach-talbruecke-bei-heiligenstadt-thuer/)
- [BAB A 71, Saale – Talbrücke bei Bad Neustadt/S.](https://abc-bauconsulting.de/bab-a-71-saale-talbruecke-bei-bad-neustadt-s/)
- [BAB A 71, Thalwasser-Talbrücke bei Münnerstadt/Ufr.](https://abc-bauconsulting.de/bab-a-71-thalwasser-talbruecke-bei-muennerstadt-ufr/)
- [BAB A 4, Teufelstalbrücke (Nord) bei Hermsdorfer Kreuz/Thür.](https://abc-bauconsulting.de/bab-a-4-teufelstalbruecke-nord-bei-hermsdorfer-kreuz-thuer/)
- [L 3012, Abbruch und Neubau von 2 Brücken bei Trebur/Hessen](https://abc-bauconsulting.de/l-3012-abbruch-und-neubau-von-2-bruecken-bei-trebur-hessen/)
- [BAB A2, BW 683 bei Hannover](https://abc-bauconsulting.de/bab-a2-bw-683-bei-hannover/)

[![IMG-027][IMG-027]](https://abc-bauconsulting.de/bab-a-17-lockwitz-talbruecke-bei-dresden/)

Lockwitz – Talbrücke bei Dresden
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-027](#img-027) | `/2020/10/Ref_Ing_Lockwitz_3-1024x768.jpg` | 1024 × 768 | Empty | `https://abc-bauconsulting.de/bab-a-17-lockwitz-talbruecke-bei-dresden/` |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| BAB A 17, Lockwitz – Talbrücke bei Dresden | `https://abc-bauconsulting.de/bab-a-17-lockwitz-talbruecke-bei-dresden/` | Same as href | Same tab |
| BAB A 38, Steinbach – Talbrücke bei Heiligenstadt/Thür. | `https://abc-bauconsulting.de/bab-a-38-steinbach-talbruecke-bei-heiligenstadt-thuer/` | Same as href | Same tab |
| BAB A 71, Saale – Talbrücke bei Bad Neustadt/S. | `https://abc-bauconsulting.de/bab-a-71-saale-talbruecke-bei-bad-neustadt-s/` | Same as href | Same tab |
| BAB A 71, Thalwasser-Talbrücke bei Münnerstadt/Ufr. | `https://abc-bauconsulting.de/bab-a-71-thalwasser-talbruecke-bei-muennerstadt-ufr/` | Same as href | Same tab |
| BAB A 4, Teufelstalbrücke (Nord) bei Hermsdorfer Kreuz/Thür. | `https://abc-bauconsulting.de/bab-a-4-teufelstalbruecke-nord-bei-hermsdorfer-kreuz-thuer/` | Same as href | Same tab |
| L 3012, Abbruch und Neubau von 2 Brücken bei Trebur/Hessen | `https://abc-bauconsulting.de/l-3012-abbruch-und-neubau-von-2-bruecken-bei-trebur-hessen/` | Same as href | Same tab |
| BAB A2, BW 683 bei Hannover | `https://abc-bauconsulting.de/bab-a2-bw-683-bei-hannover/` | Same as href | Same tab |
| IMG-027 | `https://abc-bauconsulting.de/bab-a-17-lockwitz-talbruecke-bei-dresden/` | Same as href | Same tab |

**Layout:** Seven project links in a bulleted list → linked Lockwitz photograph → caption “Lockwitz – Talbrücke bei Dresden”. The caption is separate from the image link.

<a id="page-p13"></a>
### P13. BAB A 17, Lockwitz – Talbrücke bei Dresden

**URL:** <https://abc-bauconsulting.de/bab-a-17-lockwitz-talbruecke-bei-dresden/>  
**Document title:** BAB A 17, Lockwitz – Talbrücke bei Dresden – ABC Abel Bau-Consulting  
**Hero H1:** BAB A 17, Lockwitz – Talbrücke bei Dresden  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P12](#page-p12) — `/ingenieurbau/`.

**Complete body, in source order:**

```markdown
![IMG-027][IMG-027]

| | |
|---|---|
| Objekt: | Neubau einer Stahlverbundbrücke an der BAB A 17 Dresden-Prag bei Dresden-Lockwitz<br>Auftragssumme (nur Anteil Massivbau): netto € 15,35 Mio. |
| Bauherr: | DEGES, Deutsche Einheit Fernstraßenplanungs- und -bau GmbH, Berlin |
| Auftraggeber: | Arge Fa. J.G.Müller / Fa. Brückenbau Plauen |
| Leistungen: | Erstellung von insgesamt 34 Sach-Nachträgen mit der Summe von netto € 5,042 Mio. (= 33% der Auftragssumme). Mitwirkung bei Nachtragsverhandlungen. Baubetriebliche Beratung in Klageverfahren über strittige Nachträge.<br>Erstellung Parteigutachten „Gestörter Bauablauf“ hinsichtlich der Auswirkungen von AG- und AN-seitigen Störungen auf vertragl. Zwischentermin „Überfahrbarkeit Überbau 1“ zur Abwehr von Schadenersatzforderungen.<br>Ergebnis : 16,5 Monate Zwischentermin-Verschiebung nur aufgrund AG-seitiger Störungen |

![IMG-026][IMG-026]

![IMG-028][IMG-028]

[Vorherige](https://abc-bauconsulting.de/ingenieurbau/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/bab-a-38-steinbach-talbruecke-bei-heiligenstadt-thuer/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-027](#img-027) | `/2020/10/Ref_Ing_Lockwitz_3-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-026](#img-026) | `/2020/10/Ref_Ing_Lockwitz_1-1024x768.jpg` | 1024 × 768 | Empty | None |
| 3 | [IMG-028](#img-028) | `/2020/10/Ref_Ing_Lockwitz_4-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/ingenieurbau/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/bab-a-38-steinbach-talbruecke-bei-heiligenstadt-thuer/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p14"></a>
### P14. BAB A 38, Steinbach – Talbrücke bei Heiligenstadt/Thür.

**URL:** <https://abc-bauconsulting.de/bab-a-38-steinbach-talbruecke-bei-heiligenstadt-thuer/>  
**Document title:** BAB A 38, Steinbach – Talbrücke bei Heiligenstadt/Thür. – ABC Abel Bau-Consulting  
**Hero H1:** BAB A 38, Steinbach – Talbrücke bei Heiligenstadt/Thür.  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P12](#page-p12) — `/ingenieurbau/`.

**Complete body, in source order:**

```markdown
![IMG-034][IMG-034]

| | |
|---|---|
| Objekt: | Neubau einer Stahlverbundbrücke ( 1-zelliger Überbauquerschnitt) an der BAB A 38 Göttingen – Halle bei Heiligenstadt/Thüringen. Auftragssumme: netto DM 24,333 Mio. |
| Bauherr: | DEGES, Deutsche Einheit Fernstraßenplanungs– und –bau GmbH, Berlin |
| Auftraggeber: | Arge Fa. J.G.Müller, Wetzlar / Fa. MCE Voest GmbH, A-Linz<br>(später : Insolvenzverwaltung eines Arge-Partners) |
| Leistungen: | Erstellung von insges. 31 Sach-Nachträgen mit der Summe von netto DM 3,54 Mio. (= 15 % der Auftragssumme). Mitwirkung bei Nachtragsverhandlungen. Baubetriebliche Beratung in Klageverfahren über strittige Nachträge.<br>Erstellung eines Nachtrags „Gestörter Bauablauf“ unter Auswertung von 26 AG-seitigen Störungen sowie witterungsbedingter Sekundärstörungen und Umstellungen im Bauablauf.<br>Ergebnis: Mehrkostenanspruch netto DM 2,234 Mio. (= 9,2 % der Auftragssumme)<br>Ermittlung einer Kündigungsvergütung zugunsten des AN gemäß § 8 (1),VOB/B.<br>Bearbeitung baubetrieblicher Aufgaben im Rahmen Insolvenzverfahren eines beteiligten AN |

![IMG-033][IMG-033]

![IMG-032][IMG-032]

[Vorherige](https://abc-bauconsulting.de/bab-a-17-lockwitz-talbruecke-bei-dresden/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/bab-a-71-saale-talbruecke-bei-bad-neustadt-s/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-034](#img-034) | `/2020/10/Ref_Ing_Steinbach_3-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-033](#img-033) | `/2020/10/Ref_Ing_Steinbach_2-768x1024.jpg` | 768 × 1024 | Empty | None |
| 3 | [IMG-032](#img-032) | `/2020/10/Ref_Ing_Steinbach_1-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/bab-a-17-lockwitz-talbruecke-bei-dresden/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/bab-a-71-saale-talbruecke-bei-bad-neustadt-s/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p15"></a>
### P15. BAB A 71, Saale – Talbrücke bei Bad Neustadt/S.

**URL:** <https://abc-bauconsulting.de/bab-a-71-saale-talbruecke-bei-bad-neustadt-s/>  
**Document title:** BAB A 71, Saale – Talbrücke bei Bad Neustadt/S. – ABC Abel Bau-Consulting  
**Hero H1:** BAB A 71, Saale – Talbrücke bei Bad Neustadt/S.  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P12](#page-p12) — `/ingenieurbau/`.

**Complete body, in source order:**

```markdown
![IMG-029][IMG-029]

| | |
|---|---|
| Objekt: | Neubau einer Spannbetonbrücke im Takt – Schiebe – Verfahren an der BAB A 71, Erfurt – Schweinfurt Auftragssumme: netto € 14,2 Mio. |
| Bauherr: | Autobahndirektion Nordbayern |
| Auftraggeber: | Fa. J. G. Müller, Wetzlar (vertreten durch Insolvenzverwaltung) |
| Leistungen: | nach Eröffnung Insolvenzverfahren :<br>• Überprüfung bereits gestellter und Erarbeitung aller weiteren Nachträge aus Bauleistung, Summe = netto 1,10 Mio. €<br>• Erstellung Abrechnung und zugehörige Schlussrechnung für Auftraggeber<br>• Erstellung NT Gestörter Bauablauf, Summe = netto € 0,38 Mio.<br>• Verhandlungen mit Bauherr über Nachträge, Schlussrechnungspositionen, Bauablaufstörungen<br>• Prüfung Schadenersatzforderungen Bauherr aus Vertragskündigung/Restfertigstellung<br>• Prüfungen zur Inanspruchnahme Vertragserfüllungsbürgschaft<br>• baubetriebliche Beratung der Insolvenzverwaltung |

![IMG-031][IMG-031]

![IMG-030][IMG-030]

[Vorherige](https://abc-bauconsulting.de/bab-a-38-steinbach-talbruecke-bei-heiligenstadt-thuer/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/bab-a-71-thalwasser-talbruecke-bei-muennerstadt-ufr/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-029](#img-029) | `/2020/10/Ref_Ing_Saale_1-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-031](#img-031) | `/2020/10/Ref_Ing_Saale_3-1024x768.jpg` | 1024 × 768 | Empty | None |
| 3 | [IMG-030](#img-030) | `/2020/10/Ref_Ing_Saale_2-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/bab-a-38-steinbach-talbruecke-bei-heiligenstadt-thuer/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/bab-a-71-thalwasser-talbruecke-bei-muennerstadt-ufr/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p16"></a>
### P16. BAB A 71, Thalwasser-Talbrücke bei Münnerstadt/Ufr.

**URL:** <https://abc-bauconsulting.de/bab-a-71-thalwasser-talbruecke-bei-muennerstadt-ufr/>  
**Document title:** BAB A 71, Thalwasser-Talbrücke bei Münnerstadt/Ufr. – ABC Abel Bau-Consulting  
**Hero H1:** BAB A 71, Thalwasser-Talbrücke bei Münnerstadt/Ufr.  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P12](#page-p12) — `/ingenieurbau/`.

**Complete body, in source order:**

```markdown
![IMG-036][IMG-036]

| | |
|---|---|
| Objekt: | Neubau einer Spannbetonbrücke im Takt – Schiebe – Verfahren an der BAB A 71, Erfurt – Schweinfurt Auftragssumme: netto € 9, 15 Mio. |
| Bauherr: | Autobahndirektion Nordbayern |
| Auftraggeber: | Fa. J.G. Müller, Wetzlar (vertreten durch Insolvenzverwaltung) |
| Leistungen: | nach Eröffnung Insolvenzverfahren :<br>• Überprüfung bereits gestellter und Erarbeitung aller weiteren Nachträge aus Bauleistung, Summe = netto 1,298 Mio. €<br>• Erstellung Abrechnung und zugehörige Schlussrechnung<br>• Erstellung NT Gestörter Bauablauf, Summe = netto € 1,054 Mio.<br>• Verhandlungen mit Bauherr über Nachträge, gestörter Bauablauf, Schlussrechnung<br>• Prüfung Schadenersatzforderungen Bauherr aus Vertragskündigung/Restfertigstellung<br>• Prüfungen zur Inanspruchnahme Vertragserfüllungsbürgschaft<br>• baubetriebliche Beratung der Insolvenzverwaltung |

![IMG-037][IMG-037]

![IMG-038][IMG-038]

[Vorherige](https://abc-bauconsulting.de/bab-a-71-saale-talbruecke-bei-bad-neustadt-s/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/bab-a-4-teufelstalbruecke-nord-bei-hermsdorfer-kreuz-thuer/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-036](#img-036) | `/2020/10/Ref_Ing_Thalwasser_1-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-037](#img-037) | `/2020/10/Ref_Ing_Thalwasser_2-1024x768.jpg` | 1024 × 768 | Empty | None |
| 3 | [IMG-038](#img-038) | `/2020/10/Ref_Ing_Thalwasser_3-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/bab-a-71-saale-talbruecke-bei-bad-neustadt-s/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/bab-a-4-teufelstalbruecke-nord-bei-hermsdorfer-kreuz-thuer/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p17"></a>
### P17. BAB A 4, Teufelstalbrücke (Nord) bei Hermsdorfer Kreuz/Thür.

**URL:** <https://abc-bauconsulting.de/bab-a-4-teufelstalbruecke-nord-bei-hermsdorfer-kreuz-thuer/>  
**Document title:** BAB A 4, Teufelstalbrücke (Nord) bei Hermsdorfer Kreuz/Thür. – ABC Abel Bau-Consulting  
**Hero H1:** BAB A 4, Teufelstalbrücke (Nord) bei Hermsdorfer Kreuz/Thür.  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P12](#page-p12) — `/ingenieurbau/`.

**Complete body, in source order:**

```markdown
![IMG-035][IMG-035]

| | |
|---|---|
| Objekt: | Abbruch bestehende Bogenbrücke (Bj. 1938) und Ersatzneubau gleichartige Bogenbrücke an der BAB A 4 bei Hermsdorf, Einsatz querverschiebliches Bogentraggerüst. Kämpferabstand : 138 m, max. Höhe über Tal : 53 m<br>Auftragssumme: netto DM 15,24 Mio. |
| Bauherr: | Autobahnamt Thüringen |
| Auftraggeber: | Fa. J.G. Müller, Wetzlar (vertreten durch Insolvenzverwaltung) |
| Leistungen: | nach Eröffnung Insolvenzverfahren :<br>• baubetriebl. Begleitung /Beratung der Insolvenzverwaltung in Werklohnklage<br>• Erstellung Parteigutachten zu Gestörtem Bauablauf (Forderungssumme, netto DM 4,57 Mio.)<br>• Überprüfung und Überarbeitung div. Sach – Nachtragsforderungen im Zuge Klage<br>• Überprüfung Gewährleistungsmängel<br>• gutachtliche Stellungnahmen zu insges. 22 Gerichtsgutachten im Prozessverlauf |

[Vorherige](https://abc-bauconsulting.de/bab-a-71-thalwasser-talbruecke-bei-muennerstadt-ufr/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/l-3012-abbruch-und-neubau-von-2-bruecken-bei-trebur-hessen/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-035](#img-035) | `/2020/10/Ref_Ing_Teufelstal_1-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/bab-a-71-thalwasser-talbruecke-bei-muennerstadt-ufr/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/l-3012-abbruch-und-neubau-von-2-bruecken-bei-trebur-hessen/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p18"></a>
### P18. L 3012, Abbruch und Neubau von 2 Brücken bei Trebur/Hessen

**URL:** <https://abc-bauconsulting.de/l-3012-abbruch-und-neubau-von-2-bruecken-bei-trebur-hessen/>  
**Document title:** L 3012, Abbruch und Neubau von 2 Brücken bei Trebur/Hessen – ABC Abel Bau-Consulting  
**Hero H1:** L 3012, Abbruch und Neubau von 2 Brücken bei Trebur/Hessen  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P12](#page-p12) — `/ingenieurbau/`.

**Complete body, in source order:**

```markdown
![IMG-040][IMG-040]

| | |
|---|---|
| Objekt: | Abbruch Bestandsbauwerke und Ersatzneubau von 2 Brücken<br>Auftragssumme: netto 988 T€ |
| Bauherr: | Hess. Straßen- und Verkehrsverwaltung |
| Auftraggeber: | Fa. H. Schneider Bauunternehmung GmbH, Merxheim |
| Leistungen: | • Erstellung von komplexen Sach – Nachträgen, Forderungssumme: netto 200 T€<br>• Erstellung Nachtrag Gestörter Bauablauf, Forderungssumme : netto 31 T€<br>• baubetriebliche Beratung des Bau – AN |

![IMG-039][IMG-039]

![IMG-041][IMG-041]

[Vorherige](https://abc-bauconsulting.de/bab-a-4-teufelstalbruecke-nord-bei-hermsdorfer-kreuz-thuer/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/bab-a2-bw-683-bei-hannover/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-040](#img-040) | `/2020/10/Ref_Ing_Trebur_2-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-039](#img-039) | `/2020/10/Ref_Ing_Trebur_1-1024x768.jpg` | 1024 × 768 | Empty | None |
| 3 | [IMG-041](#img-041) | `/2020/10/Ref_Ing_Trebur_3-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/bab-a-4-teufelstalbruecke-nord-bei-hermsdorfer-kreuz-thuer/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/bab-a2-bw-683-bei-hannover/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p19"></a>
### P19. BAB A2, BW 683 bei Hannover

**URL:** <https://abc-bauconsulting.de/bab-a2-bw-683-bei-hannover/>  
**Document title:** BAB A2, BW 683 bei Hannover – ABC Abel Bau-Consulting  
**Hero H1:** BAB A2, BW 683 bei Hannover  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P12](#page-p12) — `/ingenieurbau/`.

**Complete body, in source order:**

```markdown
![IMG-080][IMG-080]

| | |
|---|---|
| Objekt: | Verstärkungsmaßnahmen an Stahlverbundbrücke Bw 683, BAB A2, über den Mittellandkanal bei Hannover – Dedensen.<br>Auftragssumme:<br>Soll – Bauzeit: 3,5 Mt. (06.07. bis 23.10.20**20**)<br>Tatsächlicher Baubeginn: Ende Februar 20**22** |
| Bauherr: | Nieders. Landesamt für Straßenbau & Verkehr<br>später: Autobahn GmbH des Bundes |
| Auftraggeber: | Eurovia Beton GmbH<br>NL Bauwerksinstandsetzung, Hamburg |
| Leistungen: | Ausarbeitung eines Nachtrags für den Verzug im Baubeginn (~ 20 Mt.) infolge Annahmeverzug des AG ( § 642 BGB ) bzw. aus Anordnungen nach § 2 Abs. 5 VOB/B.<br>Berechnung eines monetären Entschädigungsanspruchs des AN, auf Basis Urkalkulation, unter Berücksichtigung bereits erbrachter Planungsleistungen, tatsächlich ersparter Aufwendungen und anderweitigem Erwerb durch die eingeplanten Arbeitskräfte auf sonstigen Baustellen des AN.<br>Ergebnis angemess. Entschädigungsanspruch: |

![IMG-079][IMG-079]

![IMG-078][IMG-078]

[Vorherige](https://abc-bauconsulting.de/l-3012-abbruch-und-neubau-von-2-bruecken-bei-trebur-hessen/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/ingenieurbau/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-080](#img-080) | `/2022/08/20210617_112506-1024x576.jpg` | 1024 × 576 | Empty | None |
| 2 | [IMG-079](#img-079) | `/2022/08/20210617_110237-1024x576.jpg` | 1024 × 576 | Empty | None |
| 3 | [IMG-078](#img-078) | `/2022/08/20210617_104541-1024x576.jpg` | 1024 × 576 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/l-3012-abbruch-und-neubau-von-2-bruecken-bei-trebur-hessen/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/ingenieurbau/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p20"></a>
### P20. Spezialtiefbau

**URL:** <https://abc-bauconsulting.de/spezialtiefbau/>  
**Document title:** Spezialtiefbau – ABC Abel Bau-Consulting  
**Hero H1:** Spezialtiefbau  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P11](#page-p11) — `/referenzen/`.

**Complete body, in source order:**

```markdown
- [B 29, Ortsumgehung Schwäbisch Gmünd, Trogbauwerk](https://abc-bauconsulting.de/b-29-ortsumgehung-schwaebisch-gmuend-trogbauwerk/)
```

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| B 29, Ortsumgehung Schwäbisch Gmünd, Trogbauwerk | `https://abc-bauconsulting.de/b-29-ortsumgehung-schwaebisch-gmuend-trogbauwerk/` | Same as href | Same tab |

<a id="page-p21"></a>
### P21. B 29, Ortsumgehung Schwäbisch Gmünd, Trogbauwerk

**URL:** <https://abc-bauconsulting.de/b-29-ortsumgehung-schwaebisch-gmuend-trogbauwerk/>  
**Document title:** B 29, Ortsumgehung Schwäbisch Gmünd, Trogbauwerk – ABC Abel Bau-Consulting  
**Hero H1:** B 29, Ortsumgehung Schwäbisch Gmünd, Trogbauwerk  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P20](#page-p20) — `/spezialtiefbau/`.

**Complete body, in source order:**

```markdown
![IMG-045][IMG-045]

| | |
|---|---|
| Objekt: | Bau eines Trogbauwerks als Tunnelrampe (in offener Bauweise innerhalb rückverankerter Bohrpfahlwandung), mit Üf – Bauwerk im Zuge der B 29 , Ortsumgehung Schwäbisch Gmünd.<br>Auftragssumme: netto € 7,3 Mio. |
| Bauherr: | Land Baden – Württemberg, vertreten durch Regierungspräsidium Stuttgart |
| Auftraggeber: | Alpine Bau Deutschland AG |
| Leistungen: | Erstellung aller Sach – Nachträge (netto 1, 681 Mio. € / 23% der Auftragssumme). Mitwirkung bei Nachtragsverhandlungen. Bauparallele Erstellung Nachtrag Gestörter Bauablauf. |

![IMG-042][IMG-042]

![IMG-043][IMG-043]

![IMG-044][IMG-044]

![IMG-046][IMG-046]

[Vorherige](https://abc-bauconsulting.de/spezialtiefbau/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/spezialtiefbau/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-045](#img-045) | `/2020/10/Ref_Spezi_SGTrog_5-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-042](#img-042) | `/2020/10/Ref_Spezi_SGTrog_1-1024x768.jpg` | 1024 × 768 | Empty | None |
| 3 | [IMG-043](#img-043) | `/2020/10/Ref_Spezi_SGTrog_3-1024x768.jpg` | 1024 × 768 | Empty | None |
| 4 | [IMG-044](#img-044) | `/2020/10/Ref_Spezi_SGTrog_4-1024x768.jpg` | 1024 × 768 | Empty | None |
| 5 | [IMG-046](#img-046) | `/2020/10/Ref_Spezi_SGTrog_6-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/spezialtiefbau/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/spezialtiefbau/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p22"></a>
### P22. Hochbau & Schlüsselfertigbau

**URL:** <https://abc-bauconsulting.de/hochbau-schluesselfertigbau/>  
**Document title:** Hochbau & Schlüsselfertigbau – ABC Abel Bau-Consulting  
**Hero H1:** Hochbau & Schlüsselfertigbau  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P11](#page-p11) — `/referenzen/`.

**Complete body, in source order:**

```markdown
- [Westpfalz-Klinikum Kaiserslautern, Hs. 7 mit Hubschrauberlandeplattform](https://abc-bauconsulting.de/westpfalz-klinikum-kaiserslautern-hs-7-mit-hubschrauberlandeplattform/)
- [Umbau Dachgeschoss in hochwertige Wohnung, inkl. Aufzuganlage](https://abc-bauconsulting.de/umbau-dachgeschoss-in-hochwertige-wohnung-inkl-aufzuganlage/)
- [Neubau Kleintier- u. Vogelklinik,Universität Gießen](https://abc-bauconsulting.de/neubau-kleintier-u-vogelklinikuniversitaet-giessen/)
- [Flughafen Frankfurt/M. Terminal 3](https://abc-bauconsulting.de/flughafen-frankfurt-terminal-3/)
```

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Westpfalz-Klinikum Kaiserslautern, Hs. 7 mit Hubschrauberlandeplattform | `https://abc-bauconsulting.de/westpfalz-klinikum-kaiserslautern-hs-7-mit-hubschrauberlandeplattform/` | Same as href | Same tab |
| Umbau Dachgeschoss in hochwertige Wohnung, inkl. Aufzuganlage | `https://abc-bauconsulting.de/umbau-dachgeschoss-in-hochwertige-wohnung-inkl-aufzuganlage/` | Same as href | Same tab |
| Neubau Kleintier- u. Vogelklinik,Universität Gießen | `https://abc-bauconsulting.de/neubau-kleintier-u-vogelklinikuniversitaet-giessen/` | Same as href | Same tab |
| Flughafen Frankfurt/M. Terminal 3 | `https://abc-bauconsulting.de/flughafen-frankfurt-terminal-3/` | Same as href | Same tab |

<a id="page-p23"></a>
### P23. Westpfalz-Klinikum Kaiserslautern, Hs. 7 mit Hubschrauberlandeplattform

**URL:** <https://abc-bauconsulting.de/westpfalz-klinikum-kaiserslautern-hs-7-mit-hubschrauberlandeplattform/>  
**Document title:** Westpfalz-Klinikum Kaiserslautern, Hs. 7 mit Hubschrauberlandeplattform – ABC Abel Bau-Consulting  
**Hero H1:** Westpfalz-Klinikum Kaiserslautern, Hs. 7 mit Hubschrauberlandeplattform  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P22](#page-p22) — `/hochbau-schluesselfertigbau/`.

**Complete body, in source order:**

```markdown
![IMG-022][IMG-022]

| | |
|---|---|
| Objekt: | Umbau Teilgebäude eines Großklinikums in Kaiserslautern mit Anbau Aufzugschächten und Hubschrauberlandeplattform<br>Auftragssumme: netto 1,10 Mio. € |
| Bauherr: | Westpfalz-Klinikum GmbH, Kaiserslautern |
| Auftraggeber: | Fa. P. A. Budau GmbH, Idar – Oberstein |
| Leistungen: | Erstellung baubetriebliches Sachverständigengutachten als Privatgutachten über Bauablaufstörungen als Ersatz für einen AN – Bauzeitnachtrag.<br>Untersuchung und Auswertung von 16 Störungseinflüssen des AG.<br>Ergebnis: Nachweis einer verkürzten Bauzeit des AN, bei ungestörten Bauablauf, von 1,3 Monaten.<br>Hierauf bezogener Bauzeitverlängerungsanspruch des AN von 3,2 Monaten.<br>Mehrkostenanspruch hieraus: netto 78 T€ ( = 7 % der Auftragssumme ) |

![IMG-025][IMG-025]

![IMG-023][IMG-023]

![IMG-024][IMG-024]

[Vorherige](https://abc-bauconsulting.de/hochbau-schluesselfertigbau/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/umbau-dachgeschoss-in-hochwertige-wohnung-inkl-aufzuganlage/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-022](#img-022) | `/2020/10/Ref_Hoch_WPKlinik_1-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-025](#img-025) | `/2020/10/Ref_Hoch_WPKlinik_4-1024x768.jpg` | 1024 × 768 | Empty | None |
| 3 | [IMG-023](#img-023) | `/2020/10/Ref_Hoch_WPKlinik_2-1024x768.jpg` | 1024 × 768 | Empty | None |
| 4 | [IMG-024](#img-024) | `/2020/10/Ref_Hoch_WPKlinik_3-768x1024.jpg` | 768 × 1024 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/hochbau-schluesselfertigbau/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/umbau-dachgeschoss-in-hochwertige-wohnung-inkl-aufzuganlage/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p24"></a>
### P24. Umbau Dachgeschoss in hochwertige Wohnung, inkl. Aufzuganlage

**URL:** <https://abc-bauconsulting.de/umbau-dachgeschoss-in-hochwertige-wohnung-inkl-aufzuganlage/>  
**Document title:** Umbau Dachgeschoss in hochwertige Wohnung, inkl. Aufzuganlage – ABC Abel Bau-Consulting  
**Hero H1:** Umbau Dachgeschoss in hochwertige Wohnung, inkl. Aufzuganlage  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P22](#page-p22) — `/hochbau-schluesselfertigbau/`.

**Complete body, in source order:**

```markdown
![IMG-018][IMG-018]

| | |
|---|---|
| Objekt: | Ausbau eines bisher ungenutzten Dachgeschosses in eine<br>2 – geschossige Maisonette – Wohnung in hochwertiger<br>Ausführung, mit Anbau separater Aufzugschacht in DG.<br>Lage : innerstädt. in Frankfurt/Main, Westend<br>Auftragssumme : netto 954 T€<br>Vertragliche Bauzeit : 7 Monate<br>Tatsächliche Bauzeit : 21,3 Monate |
| Bauherr: | Immobilienbau- und -vermietungsgesellschaft |
| Auftraggeber: | Bauunternehmung F. Kellermann, Hanau |
| Leistungen: | Baubegleitende Unterstützung und Beratung der ausführ.<br>Bauunternehmung in baubetrieblichen Sachfragen.<br>Erstellung komplexer Sach-Nachtrag (Verbauarbeiten).<br>Erstellung eines umfassenden baubetrieblichen Sachverständigengutachtens als Privatgutachten.<br>Hierin Untersuchung und Auswertung von 15 Störungs-<br>sachverhalten des AG sowie von 2 maßgeblichen Umstellung<br>im Bauablauf durch den AN.<br>Ergebnis : Ermittlung eines Bauzeitverlängerungsanspruchs des AN von 12,8 Monaten.<br>Mehrkostenanspruch des AN hieraus : netto 242 T€<br>( = 25 % der Auftragssumme ) |

![IMG-017][IMG-017]

![IMG-019][IMG-019]

[Vorherige](https://abc-bauconsulting.de/westpfalz-klinikum-kaiserslautern-hs-7-mit-hubschrauberlandeplattform/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/neubau-kleintier-u-vogelklinikuniversitaet-giessen/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-018](#img-018) | `/2020/10/Ref_Hoch_Dachgeschoss_2-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-017](#img-017) | `/2020/10/Ref_Hoch_Dachgeschoss_1-768x1024.jpg` | 768 × 1024 | Empty | None |
| 3 | [IMG-019](#img-019) | `/2020/10/Ref_Hoch_Dachgeschoss_3-768x1024.jpg` | 768 × 1024 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/westpfalz-klinikum-kaiserslautern-hs-7-mit-hubschrauberlandeplattform/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/neubau-kleintier-u-vogelklinikuniversitaet-giessen/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p25"></a>
### P25. Neubau Kleintier- u. Vogelklinik,Universität Gießen

**URL:** <https://abc-bauconsulting.de/neubau-kleintier-u-vogelklinikuniversitaet-giessen/>  
**Document title:** Neubau Kleintier- u. Vogelklinik,Universität Gießen – ABC Abel Bau-Consulting  
**Hero H1:** Neubau Kleintier- u. Vogelklinik,Universität Gießen  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P22](#page-p22) — `/hochbau-schluesselfertigbau/`.

**Complete body, in source order:**

```markdown
![IMG-020][IMG-020]

| | |
|---|---|
| Objekt: | Neubau einer Kleintier- u. Vogelklinik der Justus-Liebig-Universität Gießen<br>hier : Techn. Gebäudeausbau (TGA – Einzelgewerke)<br>• Sanitäre Anlagen<br>• Elektroinstallation<br>• Trockenbau (Wände)<br>• Raumlufttechn. Anlagen<br>Auftragssumme dieser Gewerke : netto 8,06 Mio. €<br>vertragl. Bauzeit : Mitte 2012 – Frühj. 2014<br>massive Bauzeitverlängerung aufgrund AG – Planungsbüros,<br>angemeld. NT – Forderungen der TGA – AN: netto ca. 750 T€ |
| Bauherr: | Hessisches Baumanagement hbm |
| Auftraggeber: | hbm ( später: LBIH ), Regionalniederl. Mitte, Gießen |
| Leistungen: | Baubegleitende Unterstützung und Beratung des Auftrag-<br>gebers, AG-Bauleitung und -projektsteuerung zu Forderungen der TGA – AN bezüglich der eingetretenen Bauzeitverlängerung.<br>Untersuchung / Prüfung der vorliegenden Nachtragsforderungen sowie externer Sachverständigen – Gutachten.<br>Untersuchungen zu Anspruchsgrundlagen, Bauablaufstörungen, Kalkulationsunterlagen sowie sonstiger, baubetrieblicher Detailaspekte. Erstellung von eigenen Sachverständigengutachten als Verhandlungsgrundlage für AG.<br>Unterstützung des AG bei Verhandlungen und Nachtragsvereinbarungen zur Bauzeit – Thematik. |

![IMG-021][IMG-021]

[Vorherige](https://abc-bauconsulting.de/umbau-dachgeschoss-in-hochwertige-wohnung-inkl-aufzuganlage/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/flughafen-frankfurt-terminal-3/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-020](#img-020) | `/2020/10/Ref_Hoch_Kleintier_1-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-021](#img-021) | `/2020/10/Ref_Hoch_Kleintier_2-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/umbau-dachgeschoss-in-hochwertige-wohnung-inkl-aufzuganlage/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/flughafen-frankfurt-terminal-3/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p26"></a>
### P26. Flughafen Frankfurt, Terminal 3

**URL:** <https://abc-bauconsulting.de/flughafen-frankfurt-terminal-3/>  
**Document title:** Flughafen Frankfurt, Terminal 3 – ABC Abel Bau-Consulting  
**Hero H1:** Flughafen Frankfurt, Terminal 3  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P22](#page-p22) — `/hochbau-schluesselfertigbau/`.

**Complete body, in source order:**

```markdown
![IMG-070][IMG-070]

| | |
|---|---|
| Objekt: | Flughafen Frankfurt/Main, Neubau Terminal 3, Flugsteig G<br>Gewerk: Rohbauarbeiten, einschl. Erd- und Tiefbauarbeiten, Betonelemente Fassade<br>Auftragssumme: netto 59, 6 Mio. €<br>vertragl. Bauzeit: 12 Mt. Kernbauzeit + 2 Mt. Nachlaufphase |
| Bauherr: | Fraport Ausbau Süd (FAS) GmbH |
| Auftraggeber: | Adolf Lupp GmbH + Co. KG, Nidda ( innerhalb ARGE Pier G ) |
| Leistungen: | • Ausarbeitung Gutachtliche Stellungnahme mit Analyse von Bauablaufstörungen ( verspätete Planungsvorleistungen / Planungsänderungen ) und Berechnung Mehrkostenansprüche AN. Auswertung Bauablauf hinsichtlich Zeiträume mit AG-Annahmeverzug i. S. § 642 BGB sowie resultierender Entschädigungsanspruch. Berücksichtigung ersparter Kosten und anderweitiger Erwerb des AN.<br>Ergebnis: Dauer Annahmeverzüge je Bauabschnitt: 0,6 – 16,2 Mt.<br>Mehrkosten / Entschädigungsanspruch: netto 3, 904 Mio. €<br>• Untersuchungen zu Beschleunigungsmaßnahmen |

![IMG-071][IMG-071]

![IMG-069][IMG-069]

![IMG-068][IMG-068]

[Vorherige](https://abc-bauconsulting.de/neubau-kleintier-u-vogelklinikuniversitaet-giessen/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/hochbau-schluesselfertigbau/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-070](#img-070) | `/2022/06/20200608_163259-1024x576.jpg` | 1024 × 576 | Empty | None |
| 2 | [IMG-071](#img-071) | `/2022/06/bd1f2ab3-1867-4262-bebf-c51f00105417.png` | 1024 × 415 | Empty | None |
| 3 | [IMG-069](#img-069) | `/2022/06/20200430_133907-1024x250.jpg` | 1024 × 250 | Empty | None |
| 4 | [IMG-068](#img-068) | `/2022/06/20200430_125134-1024x576.jpg` | 1024 × 576 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/neubau-kleintier-u-vogelklinikuniversitaet-giessen/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/hochbau-schluesselfertigbau/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p27"></a>
### P27. Tiefbau & Straßenbau

**URL:** <https://abc-bauconsulting.de/tiefbau-strassenbau/>  
**Document title:** Tiefbau & Straßenbau – ABC Abel Bau-Consulting  
**Hero H1:** Tiefbau & Straßenbau  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P11](#page-p11) — `/referenzen/`.

**Complete body, in source order:**

```markdown
- [Wasserversorgung US-Liegenschaften Sembach, Los 1](https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-1/)
- [Wasserversorgung US-Liegenschaften Sembach, Los 2](https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-2/)
- [Tiefbauarbeiten für Erweiterung Universitätsgebäude](https://abc-bauconsulting.de/tiefbauarbeiten-fuer-erweiterung-universitaetsgebaeude/)
- [Infrastrukturarbeiten für Kompost.- u. Vergärungsanlage](https://abc-bauconsulting.de/infrastrukturarbeiten-fuer-kompost-u-vergaerungsanlage/)
- [Trassenumlegung mit Straßenbau (innerstädtisch)](https://abc-bauconsulting.de/trassenumlegung-mit-strassenbau-innerstaedtisch/)
- [Bahnhof Ffm-Höchst (Umgestaltung Bahnhofsareal)](https://abc-bauconsulting.de/bahnhof-ffm-hoechst-umgestaltung-bahnhofsareal/)
- [Univers. Marburg – Neubau Bibliothek (Außenanlage)](https://abc-bauconsulting.de/univers-marburg-neubau-bibliothek-aussenanlage/)
- [Univers. Marburg, Neubau Dokument.-zentrum (Außenanlagen)](https://abc-bauconsulting.de/univers-marburg-neubau-dokument-zentrum-aussenanlagen/)
```

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Wasserversorgung US-Liegenschaften Sembach, Los 1 | `https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-1/` | Same as href | Same tab |
| Wasserversorgung US-Liegenschaften Sembach, Los 2 | `https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-2/` | Same as href | Same tab |
| Tiefbauarbeiten für Erweiterung Universitätsgebäude | `https://abc-bauconsulting.de/tiefbauarbeiten-fuer-erweiterung-universitaetsgebaeude/` | Same as href | Same tab |
| Infrastrukturarbeiten für Kompost.- u. Vergärungsanlage | `https://abc-bauconsulting.de/infrastrukturarbeiten-fuer-kompost-u-vergaerungsanlage/` | Same as href | Same tab |
| Trassenumlegung mit Straßenbau (innerstädtisch) | `https://abc-bauconsulting.de/trassenumlegung-mit-strassenbau-innerstaedtisch/` | Same as href | Same tab |
| Bahnhof Ffm-Höchst (Umgestaltung Bahnhofsareal) | `https://abc-bauconsulting.de/bahnhof-ffm-hoechst-umgestaltung-bahnhofsareal/` | Same as href | Same tab |
| Univers. Marburg – Neubau Bibliothek (Außenanlage) | `https://abc-bauconsulting.de/univers-marburg-neubau-bibliothek-aussenanlage/` | Same as href | Same tab |
| Univers. Marburg, Neubau Dokument.-zentrum (Außenanlagen) | `https://abc-bauconsulting.de/univers-marburg-neubau-dokument-zentrum-aussenanlagen/` | Same as href | Same tab |

<a id="page-p28"></a>
### P28. Wasserversorgung US-Liegenschaften Sembach, Los 1

**URL:** <https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-1/>  
**Document title:** Wasserversorgung US-Liegenschaften Sembach, Los 1 – ABC Abel Bau-Consulting  
**Hero H1:** Wasserversorgung US-Liegenschaften Sembach, Los 1  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P27](#page-p27) — `/tiefbau-strassenbau/`.

**Complete body, in source order:**

```markdown
![IMG-053][IMG-053]

| | |
|---|---|
| Objekt: | Herstellung einer Anschlussleitung zur Wasserversorgung der US – Liegenschaften im Sembach an übergeordnete Wasserversorgung.<br>Streckenlänge Kanalbau : 2,30 km<br>Auftragssumme : netto 382 T€ |
| Bauherr: | örtliche Verbandsgemeindewerke |
| Auftraggeber: | Hans Schneider Bauunternehmung GmbH, Merxheim |
| Leistungen: | Erstellen von 2 komplexen Sach – Nachträgen mit Forderungssumme von netto 107 T€ (= 28 % der Auftragssumme).<br>Erstellung Nachtrag Gestörter Bauablauf.<br>Baubetriebliche Verhandlungsbegleitung. |

[Vorherige](https://abc-bauconsulting.de/tiefbau-strassenbau/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-2/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-053](#img-053) | `/2020/10/Ref_Tief_Sembach1_1-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/tiefbau-strassenbau/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-2/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p29"></a>
### P29. Wasserversorgung US-Liegenschaften Sembach, Los 2

**URL:** <https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-2/>  
**Document title:** Wasserversorgung US-Liegenschaften Sembach, Los 2 – ABC Abel Bau-Consulting  
**Hero H1:** Wasserversorgung US-Liegenschaften Sembach, Los 2  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P27](#page-p27) — `/tiefbau-strassenbau/`.

**Complete body, in source order:**

```markdown
![IMG-054][IMG-054]

| | |
|---|---|
| Objekt: | Herstellung einer Anschlussleitung zur Wasserversorgung einschl. Pumpstation und zugehöriger Bauwerke.<br>Streckenlänge Kanalbau : 2,10 km<br>Auftragssumme : netto 738 T€ |
| Bauherr: | örtliche Verbandsgemeindewerke |
| Auftraggeber: | Hans Schneider Bauunternehmung GmbH, Merxheim |
| Leistungen: | Erstellung komplexer Sach – Nachtrag (geänderte Grabentiefen, Baugrundverhältnisse, Verbau sowie Trassenänderungen ),<br>Forderungssumme von netto 294 T€ (= 40 % der Auftragssumme).<br>Parallele Vorbereitung Nachtrag Gestörter Bauablauf.<br>Baubetriebliche Verhandlungsbegleitung. |

![IMG-055][IMG-055]

[Vorherige](https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-1/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/tiefbauarbeiten-fuer-erweiterung-universitaetsgebaeude/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-054](#img-054) | `/2020/10/Ref_Tief_Sembach2_1-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-055](#img-055) | `/2020/10/Ref_Tief_Sembach2_2-768x1024.jpg` | 768 × 1024 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-1/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/tiefbauarbeiten-fuer-erweiterung-universitaetsgebaeude/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p30"></a>
### P30. Tiefbauarbeiten für Erweiterung Universitätsgebäude

**URL:** <https://abc-bauconsulting.de/tiefbauarbeiten-fuer-erweiterung-universitaetsgebaeude/>  
**Document title:** Tiefbauarbeiten für Erweiterung Universitätsgebäude – ABC Abel Bau-Consulting  
**Hero H1:** Tiefbauarbeiten für Erweiterung Universitätsgebäude  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P27](#page-p27) — `/tiefbau-strassenbau/`.

**Complete body, in source order:**

```markdown
![IMG-047][IMG-047]

| | |
|---|---|
| Objekt: | Straßenbau-, Asphalt- und Erdarbeiten für Erweiterungsbau FB Mikrobiologie der Univers. Marburg/Lahn<br>Auftragssumme : netto 273 T€<br>vertragliche Bauzeit : 5,5 Monate ( Mai bis Oktober ) |
| Bauherr: | Philipps – Universität Marburg/Lahn |
| Auftraggeber: | Bauunternehmung H. Geissler, Kirchhain |
| Leistungen: | Ausgangssituation :<br>Verschiebung des Baubeginns um 5 Monate ( von Mai auf Oktober ), hierdurch Verschiebung der Bauausführung tlw. in die Wintermonate.<br>**Gutachten I** : Ermittlung der Mehrkostenansprüche des AN infolge Verschiebung des Baubeginns ( unter Berücksichtigung ersparter Kosten bzw. anderweitigem Erwerb lt. § 642 BGB ).<br>Ergebnis : netto 163 T€<br>**Gutachten II** : Ermittlung der weiteren Mehrkostenansprüche des AN aus Bauzeitverlängerung, Winterbau bzw. sonst. Sekundärstörungen.<br>Ergebnis: zusätzl. netto 64 T€<br>Gesamt: netto 227 T€ ( > 80 % Auftragssumme )<br>Teilnahme bei Nachtragsverhandlungen sowie in Verfahren nach § 18 (2) VOB/B. |

![IMG-048][IMG-048]

![IMG-049][IMG-049]

[Vorherige](https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-2/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/infrastrukturarbeiten-fuer-kompost-u-vergaerungsanlage/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-047](#img-047) | `/2020/10/Ref_Tief_ErwUni_1-768x1024.jpg` | 768 × 1024 | Empty | None |
| 2 | [IMG-048](#img-048) | `/2020/10/Ref_Tief_ErwUni_2-1024x768.jpg` | 1024 × 768 | Empty | None |
| 3 | [IMG-049](#img-049) | `/2020/10/Ref_Tief_ErwUni_3-1024x576.jpg` | 1024 × 576 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/wasserversorgung-us-liegenschaften-sembach-los-2/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/infrastrukturarbeiten-fuer-kompost-u-vergaerungsanlage/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p31"></a>
### P31. Infrastrukturarbeiten für Kompost.- u. Vergärungsanlage

**URL:** <https://abc-bauconsulting.de/infrastrukturarbeiten-fuer-kompost-u-vergaerungsanlage/>  
**Document title:** Infrastrukturarbeiten für Kompost.- u. Vergärungsanlage – ABC Abel Bau-Consulting  
**Hero H1:** Infrastrukturarbeiten für Kompost.- u. Vergärungsanlage  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P27](#page-p27) — `/tiefbau-strassenbau/`.

**Complete body, in source order:**

```markdown
![IMG-052][IMG-052]

| | |
|---|---|
| Objekt: | Abbruch-, Tief- und Straßenbauarbeiten, Stahlbetonarbeiten zum Bau einer Kompostierungs- und Vergärungsanlage in Kirchhain – Stausebach.<br>Auftragssumme : netto 1,94 Mio. €<br>vertragliche Bauzeit : 8,3 Monate |
| Bauherr: | EAM Natur GmbH, Dillenburg |
| Auftraggeber: | Bauunternehmung H. Geissler, Kirchhain |
| Leistungen: | Ausarbeitung eines Nachtrags für<br>„**Mehrkosten aus Bauzeitverlängerung**“ mit Berücksichtigung von Auswirkungen aus<br>Mengenänderung in Vertragspositionen, Behinderungen durch AG, ca. 50 Sach – Nachträge, Produktivitätsverluste sowie bereits erlöste, zeitabh., Deckungsbeträge aus Umlagen.<br>Erstellung eines Soll – Bauablaufplans ( ca. 180 Einzelvorgänge ) sowie Rekonstruktion eines Ist – Bauablaufplans anhand der Bau-Tagesberichte des AN.<br>Mitwirkung bei Nachtragsverhandlungen.<br>Ergebnis :<br>› nachgewiesene Bauzeitverlängerung : 13 Monate<br>› Mehrkosten aus Bauzeitverlängerung: netto 682 T€ ( = 35 % der Auftragssumme ) |

![IMG-051][IMG-051]

![IMG-050][IMG-050]

[Vorherige](https://abc-bauconsulting.de/tiefbauarbeiten-fuer-erweiterung-universitaetsgebaeude/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/trassenumlegung-mit-strassenbau-innerstaedtisch/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-052](#img-052) | `/2020/10/Ref_Tief_Kompost_3-1024x576.jpg` | 1024 × 576 | Empty | None |
| 2 | [IMG-051](#img-051) | `/2020/10/Ref_Tief_Kompost_2-1024x768.jpg` | 1024 × 768 | Empty | None |
| 3 | [IMG-050](#img-050) | `/2020/10/Ref_Tief_Kompost_1-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/tiefbauarbeiten-fuer-erweiterung-universitaetsgebaeude/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/trassenumlegung-mit-strassenbau-innerstaedtisch/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p32"></a>
### P32. Trassenumlegung mit Straßenbau (innerstädtisch)

**URL:** <https://abc-bauconsulting.de/trassenumlegung-mit-strassenbau-innerstaedtisch/>  
**Document title:** Trassenumlegung mit Straßenbau (innerstädtisch) – ABC Abel Bau-Consulting  
**Hero H1:** Trassenumlegung mit Straßenbau (innerstädtisch)  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P27](#page-p27) — `/tiefbau-strassenbau/`.

**Complete body, in source order:**

```markdown
![IMG-056][IMG-056]

| | |
|---|---|
| Objekt: | Umlegung von Leitungstrassen ( Strom-Hochspannung bis – Niederspannung, Gas, Wasser, Kanalisation, Telekommunik.) mit Straßenbaumaßnahmen zur Baufeldfreimachung für Neubau U-Bahnstation „Skyline Plaza“ (U5), Frankfurt/M. – Güterplatz<br>Auftragssumme : netto 4,285 Mio. € ( innerh. ARGE )<br>vertragliche Bauzeit : 12 Monate<br>tatsächliche Bauzeit : 20 Monate |
| Bauherr: | VGF Stadtwerke Verkehrsgesellschaft Frankfurt/M. |
| Auftraggeber: | Wilhelm Schütz, Straßen- und Tiefbau, Weilbg.- Gaudernbach |
| Leistungen: | Baubegleitende baubetriebliche Beratung und Ausarbeitung<br>von insgesamt 7 Sach-Nachträgen ( netto 1,42 Mio. € ), Ermittlung einer Kündigungsvergütung wegen Entfall eines LV – Titels ( netto 23 T€ ), Ermittlung Entschädigung nach § 642 BGB für Teilstillstand 2 Wochen Baustelle ( netto 83 T€ ), Ausarbeitung Mehrkostenanspruch aus Gestörtem Bauablauf / Bauzeitverlängerung ( netto 438 T€ )<br>unmittelbar gesamt : netto 1,96 Mio. € ( = 46 % der Auftragssumme )<br>Zusätzliche Begründungen für weitere Sach – Nachträge des AN.<br>Teilnahme an Baubesprechungen.<br>Teilnahme und Unterstützung bei Nachtragsverhandlungen. |

![IMG-057][IMG-057]

![IMG-058][IMG-058]

[Vorherige](https://abc-bauconsulting.de/infrastrukturarbeiten-fuer-kompost-u-vergaerungsanlage/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/bahnhof-ffm-hoechst-umgestaltung-bahnhofsareal/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-056](#img-056) | `/2020/10/Ref_Tief_Trassenumlegung_1-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-057](#img-057) | `/2020/10/Ref_Tief_Trassenumlegung_2-1024x768.jpg` | 1024 × 768 | Empty | None |
| 3 | [IMG-058](#img-058) | `/2020/10/Ref_Tief_Trassenumlegung_3-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/infrastrukturarbeiten-fuer-kompost-u-vergaerungsanlage/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/bahnhof-ffm-hoechst-umgestaltung-bahnhofsareal/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p33"></a>
### P33. Bahnhof Ffm-Höchst (Umgestaltung Bahnhofsareal)

**URL:** <https://abc-bauconsulting.de/bahnhof-ffm-hoechst-umgestaltung-bahnhofsareal/>  
**Document title:** Bahnhof Ffm-Höchst (Umgestaltung Bahnhofsareal) – ABC Abel Bau-Consulting  
**Hero H1:** Bahnhof Ffm-Höchst (Umgestaltung Bahnhofsareal)  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P27](#page-p27) — `/tiefbau-strassenbau/`.

**Complete body, in source order:**

```markdown
![IMG-075][IMG-075]

| | |
|---|---|
| Objekt: | Vollständige Um- und Neugestaltung des Bahnhofsareals, Bhf. Ffm-Höchst mit zentralem Busbahnhof, Bahnhofsvorplatz sowie Einmündungen Anliegerstraßen, unter Aufrechterhaltung öffentlicher Verkehr.<br>Auftragssumme: netto 2,80 Mio. €<br>Soll – Bauzeit: 23,5 Mt.<br>Ist – Bauzeit: ~27 Mt. |
| Bauherr: | Stadt Frankfurt/Main, Amt für Straßenbau & Erschließung |
| Auftraggeber: | Wilhelm Schütz, Straßen- und Tiefbau, Weilbg. – Gaudernbach |
| Leistungen: | Ausarbeitung Nachtrag und Sachverständigengutachten wegen Gestörtem Bauablauf ( Bauzeitverlängerung + Beschleunigungsmaßnahmen ), netto 713 T€ ( = 25% der Auftragssumme).<br>Auswertung von 202 Vorkommnissen im Bauablauf, detaillierte Analyse von 8 relevanten Bauablaufsstörungen durch AG, mit Einarbeitung in störungsmodifizierte Soll – Bauablaufspläne.<br>Ermittlung von Mehrkostenansprüchen lt. § 642 BGB ( Entschädigung ) sowie für Beschleunigungsmaßnahmen und Ressourcenaufstockung. |

![IMG-074][IMG-074]

![IMG-076][IMG-076]

[Vorherige](https://abc-bauconsulting.de/trassenumlegung-mit-strassenbau-innerstaedtisch/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/univers-marburg-neubau-bibliothek-aussenanlage/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-075](#img-075) | `/2022/08/20190708_140833-1024x576.jpg` | 1024 × 576 | Empty | None |
| 2 | [IMG-074](#img-074) | `/2022/08/20190708_140031-1024x576.jpg` | 1024 × 576 | Empty | None |
| 3 | [IMG-076](#img-076) | `/2022/08/20200526_132041-1024x576.jpg` | 1024 × 576 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/trassenumlegung-mit-strassenbau-innerstaedtisch/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/univers-marburg-neubau-bibliothek-aussenanlage/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p34"></a>
### P34. Univers. Marburg – Neubau Bibliothek (Außenanlage)

**URL:** <https://abc-bauconsulting.de/univers-marburg-neubau-bibliothek-aussenanlage/>  
**Document title:** Univers. Marburg – Neubau Bibliothek (Außenanlage) – ABC Abel Bau-Consulting  
**Hero H1:** Univers. Marburg – Neubau Bibliothek (Außenanlage)  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P27](#page-p27) — `/tiefbau-strassenbau/`.

**Complete body, in source order:**

```markdown
![IMG-072][IMG-072]

| | |
|---|---|
| Objekt: | Abbruch-, Erd- und Verkehrswegebauarbeiten im Außenbereich eines Bibliotheksneubaus in innerstädtischer Lage in Marburg.<br>Auftragssumme: netto 2,44 Mio. €<br>Soll – Bauzeit: 12 Mt. ( Hauptbauphase )<br>Ist – Bauzeit: 18,3 Mt. |
| Bauherr: | Land Hessen, vertreten durch hbm Hessisches Baumanagement |
| Auftraggeber: | Bauunternehmung Heinrich Geissler, Kirchhain |
| Leistungen: | Erstellung Sachverständigengutachten zur kausalen Nachweisführung von AG – seitigen Bauablaufstörungen.<br>Detaillierte Analyse von 23 wesentlichen Störungseinflüssen, mit Bestimmung des resultierenden Bauzeitverlängerungsanspruchs ( haftungsbegründ. Kausalität ).<br>Ermittlung des AN – Mehrkostenanspruchs gem. § 642 BGB, §2 Abs. 5 VOB/B sowie aus Baubeschleunigung mit gesamt netto 1,00 Mio. €.<br>Mitwirkung und Unterstützung des AN in einem Verfahren nach § 18, Abs. 2 VOB/B. |

![IMG-077][IMG-077]

![IMG-073][IMG-073]

[Vorherige](https://abc-bauconsulting.de/bahnhof-ffm-hoechst-umgestaltung-bahnhofsareal/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/univers-marburg-neubau-dokument-zentrum-aussenanlagen/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-072](#img-072) | `/2022/08/20160912_134023-1024x576.jpg` | 1024 × 576 | Empty | None |
| 2 | [IMG-077](#img-077) | `/2022/08/20200625_134809-1024x576.jpg` | 1024 × 576 | Empty | None |
| 3 | [IMG-073](#img-073) | `/2022/08/20170711_120217-576x1024.jpg` | 576 × 1024 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/bahnhof-ffm-hoechst-umgestaltung-bahnhofsareal/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/univers-marburg-neubau-dokument-zentrum-aussenanlagen/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p35"></a>
### P35. Univers. Marburg, Neubau Dokument.-zentrum (Außenanlagen)

**URL:** <https://abc-bauconsulting.de/univers-marburg-neubau-dokument-zentrum-aussenanlagen/>  
**Document title:** Univers. Marburg, Neubau Dokument.-zentrum (Außenanlagen) – ABC Abel Bau-Consulting  
**Hero H1:** Univers. Marburg, Neubau Dokument.-zentrum (Außenanlagen)  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P27](#page-p27) — `/tiefbau-strassenbau/`.

**Complete body, in source order:**

```markdown
![IMG-083][IMG-083]

| | |
|---|---|
| Objekt: | Landschaftsbauarbeiten (ATV DIN 18320) im Außenbereich Neubau Deutsches Dokumentat.-zentrum für Kunstgeschichte mit Seminargebäude in innerstädtischer Lage in Marburg.<br>Auftragssumme: netto 630 T€<br>Soll-Bauzeit:  **Juli** 2021 – April 2022 (8,5 Mt.)<br>Ist-Bauzeit: **Nov.** 2021 – Juni 2022 (7,5 Mt.) |
| Bauherr: | Land Hessen, vertreten durch LBIH (Landesbetrieb Bau u. Immobilien Hessen) |
| Auftraggeber: | Bernshausen Bau, Bad Laasphe |
| Leistungen: | Baubegleitende baubetriebliche Beratung des AN.<br>Ausarbeitung eines Bauzeit-Nachtrags für AN-Ansprüche aus Verzug im Baubeginn von **4,5 Monaten**.<br>Definition des vertragl. Bauablaufs (Soll – Tpl.).<br>Analyse des Anfangsverzugs (Darstell. Sachverhalt, Dokumentationsquellen, Feststell. rechtl. Anspruchsgrundlage (hier: **§ 642 BGB / Annahmeverzug des AG**), ansetzbare Störungsdauer).<br>Ermittlung AN-Entschädigungsanspruch lt. § 642 BGB, unter Berücksichtigung ersparter Kosten sowie anderweitiger (produktiver) Erwerb der betreff. Arbeitsressourcen des AN im Verzugszeitraum.<br>**Ergebnis Entschädigungsanspruch: 61 T€** (für Zeitraum Verzug Baubeginn) |

![IMG-082][IMG-082]

![IMG-081][IMG-081]

[Vorherige](https://abc-bauconsulting.de/univers-marburg-neubau-bibliothek-aussenanlage/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/tiefbau-strassenbau/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-083](#img-083) | `/2024/02/20230329_110311-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-082](#img-082) | `/2024/02/20211122_155355-1024x768.jpg` | 1024 × 768 | Empty | None |
| 3 | [IMG-081](#img-081) | `/2024/02/20211122_155153-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/univers-marburg-neubau-bibliothek-aussenanlage/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/tiefbau-strassenbau/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p36"></a>
### P36. Gutachten

**URL:** <https://abc-bauconsulting.de/gutachten-2/>  
**Document title:** Gutachten – ABC Abel Bau-Consulting  
**Hero H1:** Gutachten  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P11](#page-p11) — `/referenzen/`.

**Complete body, in source order:**

```markdown
- [Mängelbeseitigungskosten bei MF – Wohnhaus (Privatgutachten)](https://abc-bauconsulting.de/maengelbeseitigungskosten-bei-mf-wohnhaus-privatgutachten/)
- [BAB A 7, Döllbach – Talbrücke (Gegengutachten in Rechtsstreit)](https://abc-bauconsulting.de/gegengutachten-zu-gerichtl-sachverstaendigengutachten/)
- [Institut für Hirnforschung (MPI), Frankfurt a. M.](https://abc-bauconsulting.de/institut-fuer-hirnforschung-mpi-frankfurt-a-m/)
- [2 Hochhäuser mit 60 Wohnanlagen, Frankfurt/M.](https://abc-bauconsulting.de/2-hochhaeuser-mit-60-wohnanlagen-frankfurt-m/)
- [Instandsetzung Stützwand, Alter Botanischer Garten, Marburg/L.](https://abc-bauconsulting.de/instandsetzung-stuetzwand-alter-botanischer-garten-marburg-l/)
```

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Mängelbeseitigungskosten bei MF – Wohnhaus (Privatgutachten) | `https://abc-bauconsulting.de/maengelbeseitigungskosten-bei-mf-wohnhaus-privatgutachten/` | Same as href | Same tab |
| BAB A 7, Döllbach – Talbrücke (Gegengutachten in Rechtsstreit) | `https://abc-bauconsulting.de/gegengutachten-zu-gerichtl-sachverstaendigengutachten/` | Same as href | Same tab |
| Institut für Hirnforschung (MPI), Frankfurt a. M. | `https://abc-bauconsulting.de/institut-fuer-hirnforschung-mpi-frankfurt-a-m/` | Same as href | Same tab |
| 2 Hochhäuser mit 60 Wohnanlagen, Frankfurt/M. | `https://abc-bauconsulting.de/2-hochhaeuser-mit-60-wohnanlagen-frankfurt-m/` | Same as href | Same tab |
| Instandsetzung Stützwand, Alter Botanischer Garten, Marburg/L. | `https://abc-bauconsulting.de/instandsetzung-stuetzwand-alter-botanischer-garten-marburg-l/` | Same as href | Same tab |

<a id="page-p37"></a>
### P37. Mängelbeseitigungskosten bei MF – Wohnhaus (Privatgutachten)

**URL:** <https://abc-bauconsulting.de/maengelbeseitigungskosten-bei-mf-wohnhaus-privatgutachten/>  
**Document title:** Mängelbeseitigungskosten bei MF – Wohnhaus (Privatgutachten) – ABC Abel Bau-Consulting  
**Hero H1:** Mängelbeseitigungskosten bei MF – Wohnhaus (Privatgutachten)  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P36](#page-p36) — `/gutachten-2/`.

**Complete body, in source order:**

```markdown
![IMG-016][IMG-016]

| | |
|---|---|
| Objekt: | Neubau eines Mehrfamilien – Wohnhauses, Bj. 1997, mit zusätzlichen Bauarbeiten für Außenanlage,<br>Lage : Gemeinde Reiskirchen, Mittelhessen |
| Bauherr: | privater Auftraggeber |
| Auftraggeber: | Bauherr |
| Leistungen: | Festlegung von technischen Mängelbeseitigungsmaßnahmen<br>auf Grundlage mehrerer Gerichtsgutachten.<br>Erstellung eines Leistungsverzeichnis inkl. Mengenermittlung<br>für die festgelegten Mängelbeseitigungsarbeiten.<br>Kalkulation der einzelnen LV-Positionen der Mängelbeseitigungsarbeiten nach ortsüblichen Preisen<br>(Basis : 2008).<br>Ermittelte Mängelbeseitigungskosten : netto 168 T€<br>Übergabe des Gutachtens als Privatgutachten im laufenden Rechtsstreit. |

[Vorherige](https://abc-bauconsulting.de/gutachten-2/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/gegengutachten-zu-gerichtl-sachverstaendigengutachten/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-016](#img-016) | `/2020/10/Ref_Gutachten_Radny_1-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/gutachten-2/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/gegengutachten-zu-gerichtl-sachverstaendigengutachten/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p38"></a>
### P38. Gegengutachten zu gerichtl. Sachverständigengutachten

**URL:** <https://abc-bauconsulting.de/gegengutachten-zu-gerichtl-sachverstaendigengutachten/>  
**Document title:** Gegengutachten zu gerichtl. Sachverständigengutachten – ABC Abel Bau-Consulting  
**Hero H1:** Gegengutachten zu gerichtl. Sachverständigengutachten  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P36](#page-p36) — `/gutachten-2/`.

**Complete body, in source order:**

```markdown
![IMG-013][IMG-013]

| | |
|---|---|
| Objekt: | Bauvertrag zur temporären Verstärkung eines Brückenüberbaus der Döllbach-Talbrücke i. Z. der BAB A7 bei Fulda.<br>(Rechtsstreit wegen offener Werklohnforderungen / Vorlage gerichtl. bestelltes Sachverständigengutachten zu gerichtl. Beschlußfragen) |
| Bauherr: | Hessische Straßen- u. Verkehrsverwaltung |
| Auftraggeber: | Fa. A. Lupp GmbH+Co. KG, Nidda |
| Leistungen: | Detaillierte Untersuchung und Überprüfung eines gerichtl. bestellten Sachverständigengutachtens auf inhaltliche und formelle Schlüssigkeit bzw. Richtigkeit.<br>Ergebnis : Feststellung, dass das vorliegende Gerichtsgutachten wesentliche Prozeßunterlagen sowie technische und baubetriebliche Zusammenhänge nicht berücksichtigt. Gerichtsgutachten war somit ungeeignet, die Beschlußfragen umfassend und zutreffend zu beantworten. Aufdeckung von offensichtlichen Verständnis- und Auslegungsproblemen innerhalb des Gerichtsgutachtens. |

![IMG-014][IMG-014]

[Vorherige](https://abc-bauconsulting.de/maengelbeseitigungskosten-bei-mf-wohnhaus-privatgutachten/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/institut-fuer-hirnforschung-mpi-frankfurt-a-m/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-013](#img-013) | `/2020/10/Ref_Gutachten_Doellbach_1-1024x768.jpg` | 1024 × 768 | Empty | None |
| 2 | [IMG-014](#img-014) | `/2020/10/Ref_Gutachten_Doellbach_2-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/maengelbeseitigungskosten-bei-mf-wohnhaus-privatgutachten/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/institut-fuer-hirnforschung-mpi-frankfurt-a-m/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p39"></a>
### P39. Institut für Hirnforschung (MPI), Frankfurt a. M.

**URL:** <https://abc-bauconsulting.de/institut-fuer-hirnforschung-mpi-frankfurt-a-m/>  
**Document title:** Institut für Hirnforschung (MPI), Frankfurt a. M. – ABC Abel Bau-Consulting  
**Hero H1:** Institut für Hirnforschung (MPI), Frankfurt a. M.  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P36](#page-p36) — `/gutachten-2/`.

**Complete body, in source order:**

```markdown
![IMG-015][IMG-015]

| | |
|---|---|
| Objekt: | Neubau Institut für Hirnforschung mit Tierhaus am<br>MPI-Standort in Frankfurt/Main<br>(Gewerk: Stark- und Schwachstromanlagen, Auftrags-<br>summe: netto 4,92 Mio. €),<br>AN – Forderungen aus Bauzeitverlängerung |
| Bauherr: | Max – Planck Gesellschaft |
| Auftraggeber: | Fa. Elektro – Klein AG, Biebergemünd |
| Leistungen: | Gutachtliche Stellungnahme zu einer Prüfung der AN –<br>Mehrkostenforderung durch einen ö.b.u.v. Sachverständigen.<br>Ergebnis : Feststellung, dass das vorliegende Prüfungsergebnis teilweise nicht nachvollziehbar bzw. partiell unzutreffend ist.<br>Neuberechnung der bestehenden AN – Mehrkostenansprüche<br>mit netto 1,93 Mio. € ( = 39 % v. Auftragssumme ). |

[Vorherige](https://abc-bauconsulting.de/gegengutachten-zu-gerichtl-sachverstaendigengutachten/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/gutachten-2/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-015](#img-015) | `/2020/10/Ref_Gutachten_Hirnforschung_1.jpg` | 800 × 533 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/gegengutachten-zu-gerichtl-sachverstaendigengutachten/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/gutachten-2/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p40"></a>
### P40. 2 Hochhäuser mit 60 Wohnanlagen, Frankfurt/M.

**URL:** <https://abc-bauconsulting.de/2-hochhaeuser-mit-60-wohnanlagen-frankfurt-m/>  
**Document title:** 2 Hochhäuser mit 60 Wohnanlagen, Frankfurt/M. – ABC Abel Bau-Consulting  
**Hero H1:** 2 Hochhäuser mit 60 Wohnanlagen, Frankfurt/M.  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P36](#page-p36) — `/gutachten-2/`.

**Complete body, in source order:**

```markdown
![IMG-063][IMG-063]

| | |
|---|---|
| Objekt: | 2 Hochhäuser mit 60 Wohnanlagen, 10 – geschossig, Frankfurt/Main<br>Massive Kostenüberschreitung und Bauzeitverlängerung bei energetischer Gebäude-Instandsetzung<br>vertragl. Bauzeit : 5 Monate<br>tatsächl. Bauzeit : 16 Monate |
| Bauherr: | privat |
| Auftraggeber: | WEG (Wohnungseigentümergesellschaft) |
| Leistungen: | – Analysen der Bauzeitverlängerung auf Ursachen und Verantwortlichkeiten der Baubeteiligten<br>– Darstellung und Auswertung des Ist – Bauablaufs gegenüber Soll – Bauablauf<br>– Untersuchung der Abrechnung des AN auf Unregelmäßigkeiten / Auffälligkeiten<br>– Erstellung SV – Gutachten, Zwischenberichte<br>– baubetriebl. Beratung während Bauprozeß ( Rückforderungen der WEG / Schadensersatz ) |

[Vorherige](https://abc-bauconsulting.de/institut-fuer-hirnforschung-mpi-frankfurt-a-m/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/instandsetzung-stuetzwand-alter-botanischer-garten-marburg-l/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-063](#img-063) | `/2021/08/20180803_130745-1024x576.jpg` | 1024 × 576 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/institut-fuer-hirnforschung-mpi-frankfurt-a-m/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/instandsetzung-stuetzwand-alter-botanischer-garten-marburg-l/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p41"></a>
### P41. Instandsetzung Stützwand, Alter Botanischer Garten, Marburg/L.

**URL:** <https://abc-bauconsulting.de/instandsetzung-stuetzwand-alter-botanischer-garten-marburg-l/>  
**Document title:** Instandsetzung Stützwand, Alter Botanischer Garten, Marburg/L. – ABC Abel Bau-Consulting  
**Hero H1:** Instandsetzung Stützwand, Alter Botanischer Garten, Marburg/L.  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P36](#page-p36) — `/gutachten-2/`.

**Complete body, in source order:**

```markdown
![IMG-062][IMG-062]

| | |
|---|---|
| Objekt: | Instandsetzung einer Stützwand am Alten Botanischen Garten, Marburg/L.<br>Auftragssumme : netto 1,12 Mio. €<br>vertragl. Bauzeit : 7 Monate<br>tatsächl. Bauzeit : 13,5 Monate<br>Schlussrechnung : netto 1,58 Mio. € ( = 141 % der Auftragssumme ) |
| Bauherr: | Universitätsstadt Marburg/L. |
| Auftraggeber: | Univ.-stadt Marburg/L., Fachdienst Tiefbau |
| Leistungen: | Analysen zu AN – Nachtragsforderungen aus Gestörtem Bauablauf in Höhe netto 115 T€, u. a. aus ungedeckten bauzeitabhängigen Baustellengemeinkosten (BGK).<br>Erstellung baubetriebliches Sachverständigengutachten.<br>Teilnahme an Nachtragsverhandlungen |

![IMG-065][IMG-065]

![IMG-066][IMG-066]

[Vorherige](https://abc-bauconsulting.de/2-hochhaeuser-mit-60-wohnanlagen-frankfurt-m/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/gutachten-2/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-062](#img-062) | `/2021/08/20180426_102012-1024x576.jpg` | 1024 × 576 | Empty | None |
| 2 | [IMG-065](#img-065) | `/2021/08/Screenshot-2021-08-24-153609-1024x640.png` | 1024 × 640 | Empty | None |
| 3 | [IMG-066](#img-066) | `/2021/08/Unbenannt-980x1024.png` | 980 × 1024 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/2-hochhaeuser-mit-60-wohnanlagen-frankfurt-m/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/gutachten-2/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p42"></a>
### P42. Beweisfähige Baustellendokumentationen

**URL:** <https://abc-bauconsulting.de/beweisfaehige-baustellendokumentationen/>  
**Document title:** Beweisfähige Baustellendokumentationen – ABC Abel Bau-Consulting  
**Hero H1:** Beweisfähige Baustellendokumentationen  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P11](#page-p11) — `/referenzen/`.

**Complete body, in source order:**

```markdown
- [Westpfalzklinikum Kaiserslautern](https://abc-bauconsulting.de/westpfalzklinikum-kaiserslautern-neubau-der-bettenhaeuser-3-4/)
```

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Westpfalzklinikum Kaiserslautern | `https://abc-bauconsulting.de/westpfalzklinikum-kaiserslautern-neubau-der-bettenhaeuser-3-4/` | Same as href | Same tab |

<a id="page-p43"></a>
### P43. Westpfalzklinikum Kaiserslautern, Neubau der Bettenhäuser 3 & 4

**URL:** <https://abc-bauconsulting.de/westpfalzklinikum-kaiserslautern-neubau-der-bettenhaeuser-3-4/>  
**Document title:** Westpfalzklinikum Kaiserslautern, Neubau der Bettenhäuser 3 & 4 – ABC Abel Bau-Consulting  
**Hero H1:** Westpfalzklinikum Kaiserslautern, Neubau der Bettenhäuser 3 & 4  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Reference detail. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P42](#page-p42) — `/beweisfaehige-baustellendokumentationen/`.

**Complete body, in source order:**

```markdown
![IMG-025][IMG-025]

| | |
|---|---|
| Objekt: | Neubau der Bettenhäuser 3 und 4 am Westfpfalz-Klinikum in Kaiserslautern.<br>Auftragssumme ( Rohbauarbeiten ) : netto 6,37 Mio. € |
| Bauherr: | Westpfalz – Klinikum GmbH |
| Auftraggeber: | Fa. P. A. Budau GmbH, Idar-Oberstein |
| Leistungen: | Beweisfähige Dokumentation des tatsächl. Bauablaufs unter besonderer Erfassung von Behinderungssachverhalten und deren Auswirkungen auf die Bauarbeiten.<br>Erfassung von Produktivitätsverlusten.<br>Einbindung der Poliere in die Tätigkeitserfassung.<br>Einbindung des vertragsrelevanten Schriftverkehrs in die beweisfähige Baustellendokumentation.<br>Durchführung regelmäßiger Ortstermine an der Baustelle.<br>Übergabe der erstellten Dokumentationsunterlagen an die<br>Bauleitung des ausführ. Bauunternehmens.<br>Dokumentation über Zeitraum von 28 Monate erstellt. |

[Vorherige](https://abc-bauconsulting.de/beweisfaehige-baustellendokumentationen/)

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste](https://abc-bauconsulting.de/beweisfaehige-baustellendokumentationen/)
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-025](#img-025) | `/2020/10/Ref_Hoch_WPKlinik_4-1024x768.jpg` | 1024 × 768 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Vorherige | `https://abc-bauconsulting.de/beweisfaehige-baustellendokumentationen/` | Same as href | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `https://abc-bauconsulting.de/beweisfaehige-baustellendokumentationen/` | Same as href | Same tab |

**Layout:** Lead photo → four-row facts table → remaining photos, if any → three reference-navigation pills. Image order and exact pill destinations are shown above.

<a id="page-p44"></a>
### P44. Adjudikation

**URL:** <https://abc-bauconsulting.de/adjudikation/>  
**Document title:** Adjudikation – ABC Abel Bau-Consulting  
**Hero H1:** Adjudikation  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Empty landing page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P11](#page-p11) — `/referenzen/`.

**Body:** No page-specific text, images, list or table. The shared contact sidebar remains visible.

<a id="page-p45"></a>
### P45. Seminare & Schulungen

**URL:** <https://abc-bauconsulting.de/seminare-schulungen/>  
**Document title:** Seminare & Schulungen – ABC Abel Bau-Consulting  
**Hero H1:** Seminare & Schulungen  
**Hero image:** [IMG-011](#img-011) — `/2020/10/Kopfbild_Seminare.jpg`  
**Pattern:** Empty landing page. Global header/menu/contact sidebar/footer.

**Body:** No page-specific text, images, list or table. The shared contact sidebar remains visible.

<a id="page-p46"></a>
### P46. Aktuelles

**URL:** <https://abc-bauconsulting.de/aktuelles/>  
**Document title:** Aktuelles – ABC Abel Bau-Consulting  
**Hero H1:** Aktuelles  
**Hero image:** [IMG-011](#img-011) — `/2020/10/Kopfbild_Seminare.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P45](#page-p45) — `/seminare-schulungen/`.

**Complete body, in source order:**

```markdown
# Seminare ab Frühjahr 2023

Nach der pandemiebedingten Unterbrechung finden wieder Seminare / Schulungsveranstaltungen statt.

In den Monaten Februar und März werden aktuell Schulungen für Bau-Auftragnehmer angeboten bzw. durchgeführt.

Bei Interesse nehmen Sie bitte Kontakt mit uns auf.
```

**Body heading levels:** H1: Seminare ab Frühjahr 2023.

<a id="page-p47"></a>
### P47. Allgemeine Übersicht

**URL:** <https://abc-bauconsulting.de/allgemeine-uebersicht/>  
**Document title:** Allgemeine Übersicht – ABC Abel Bau-Consulting  
**Hero H1:** Allgemeine Übersicht  
**Hero image:** [IMG-011](#img-011) — `/2020/10/Kopfbild_Seminare.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P45](#page-p45) — `/seminare-schulungen/`.

**Complete body, in source order:**

```markdown
Seminare oder Schulungen sind eine effiziente Art der Wissensvermittlung zur,  
auch wirtschaftlich erfolgreichen, Abwicklungen von Bauverträgen.  

Gerne bieten wir Ihnen hierzu die Möglichkeiten für Seminare in folgenden wichtigen Bereichen an, die auch an Ihre individuellen Anforderungen angepasst werden können :

• Nachträge am Bau  
• Der Gestörte Bauablauf  
• Beweisfähige Baustellendokumentation / Produktivitätsverluste dokumentieren  
• Kalkulationen lesen und verstehen (für Auftraggeber)  
• wettbewerbsgerecht kalkulieren (für Auftragnehmer)  
• Kalkulation von Gemeinkosten und Umlagen  
• Nachtragsprüfung für Auftraggeber  
• VOB für Bauleiter   
• Vermeidung von Nachträgen durch die richtige Ausschreibung  
(für Auftraggeber)  

Für Bauunternehmen und Auftraggeber besteht auch die Möglichkeit von  
Inhouse – Schulungen in deren Räumlichkeiten oder sogar an der Baustelle.  

In den letzten Jahren wurden Seminare und Schulungen für folgende Veranstalter durchgeführt :  

Ingenieur – Akademie Hessen  
Bund Deutscher Baumeister (BDB)  
Zweckverband Lollar – Staufenberg (ZLS)  
Verband baugewerblicher Unternehmer Hessen  
div. Bauunternehmungen
```

<a id="page-p48"></a>
### P48. Kontakt

**URL:** <https://abc-bauconsulting.de/kontakt/>  
**Document title:** Kontakt – ABC Abel Bau-Consulting  
**Hero H1:** Kontakt  
**Hero image:** [IMG-008](#img-008) — `/2020/10/Kopfbild_Kontakt.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Complete body, in source order:**

```markdown
# Kontakt

Wenn Sie Fragen zu unseren Leistungen und Angeboten haben,  
können Sie uns eine E-Mail senden oder gleich anrufen!  
Wir werden uns umgehend bei Ihnen melden.  

  
[**Email jetzt senden**](mailto:info@abc-bauconsulting.de%20)

(Hier war mal ein schönes Kontaktformular,  
doch wegen der neuen Datenschutzreform haben wir es besser entfernt.)
```

**Body heading levels:** H1: Kontakt.

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Email jetzt senden | `mailto:info@abc-bauconsulting.de%20` | Same as href | Same tab / email handler |

<a id="page-p49"></a>
### P49. Impressum

**URL:** <https://abc-bauconsulting.de/impressum/>  
**Document title:** Impressum – ABC Abel Bau-Consulting  
**Hero H1:** Impressum  
**Hero image:** [IMG-007](#img-007) — `/2020/10/Kopfbild_Impressum.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Complete body, in source order:**

```markdown
# Impressum

**Impressum**  

Angaben gem. § 5 TMG  

**Betreiber und Kontakt:**  
ABC Abel Bau – Consulting  
Hauptstraße 27a  
35435 Wettenberg / Hessen

Tel: 0641 96968-30  
Fax: 0641 96968-31  
Mobil: 0163 7766839  
E-Mail: info@abc-bauconsulting.de  
www.abc-bauconsulting.de

**Vertretung:**  
ABC Abel Bau – Consulting wird vertreten durch:  
Dipl.-Ing. Volker Abel

Öffentlich bestellter und vereidigter Sachverständiger für:  
„Baupreisermittlung und Abrechnung im Hoch- und Ingenieurbau, Bauablaufstörungen“  

**Umsatzsteuer-Identifikationsnummer gemäß § 27 a Umsatzsteuergesetz: DE 214990374**

# Gestaltung und Umsetzung

[![IMG-084][IMG-084]](http://www.designintime.de/)

Ursprüngliches Layout & Grundgestaltung:

design in time  
werbeagentur  
christian wack  
[www.designintime.de](http://www.designintime.de/)
```

**Body heading levels:** H1: Impressum; H1: Gestaltung und Umsetzung.

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-084](#img-084) | `/impressum/fileadmin/user_upload/8c7ec5e7d4.jpg` | unspecified × unspecified | Empty | `http://www.designintime.de/` |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| IMG-084 | `http://www.designintime.de/` | Same as href | New tab |
| www.designintime.de | `http://www.designintime.de/` | Same as href | New tab |

**Typography exception:** “Gestaltung und Umsetzung” is an H1 with the `has-medium-font-size` class, rendering at 20px rather than the standard H1 size.

<a id="page-p50"></a>
### P50. Datenschutz

**URL:** <https://abc-bauconsulting.de/datenschutz/>  
**Document title:** Datenschutz – ABC Abel Bau-Consulting  
**Hero H1:** Datenschutz  
**Hero image:** [IMG-007](#img-007) — `/2020/10/Kopfbild_Impressum.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P49](#page-p49) — `/impressum/`.

**Complete body, in source order:**

```markdown
# Datenschutzerklärung

Eine Nutzung unseres Onlineauftrittes ist grundsätzlich ohne Angabe personenbezogener Daten möglich. Sofern eine betroffene Person Services unseres Unternehmens über unseren Onlineauftritt in Anspruch nehmen möchte, kann jedoch eine Verarbeitung personenbezogener Daten (im Folgenden kurz „Daten“) erforderlich werden.

Eine Verarbeitung dieser Daten (z. B. Name, Anschrift, E-Mail-Adresse, Telefonnummer), erfolgt stets im Einklang mit der Datenschutz-Grundverordnung und in Übereinstimmung mit den für ABC Abel Bau – Consulting geltenden landesspezifischen Datenschutzbestimmungen.

ABC Abel Bau – Consulting ist bemüht, einen möglichst lückenlosen Schutz der über diese Internetseite verarbeiteten Daten sicherzustellen. Dennoch kann ein absoluter Schutz nicht gewährleistet werden, da Internetbasierte Datenübertragungen grundsätzlich Sicherheitslücken aufweisen können.

**Name und Kontaktdaten des Verantwortlichen**

ABC Abel Bau – Consulting  
Dipl.-Ing. Volker Abel  
Hauptstraße 27a  
35435 Wettenberg / Hessen

Tel: 0641 96968-30  
Fax: 0641 96968-31  
Mobil: 0163 7766839  
E-Mail: info@abc-bauconsulting.de  
[www.abc-bauconsulting.de](../index.html)

**Erfassung allgemeiner Daten und Informationen**

Diese Internetseite erfasst mit jedem Aufruf eine Reihe von allgemeinen Daten und Informationen. Diese werden in den Logfiles des Servers gespeichert.

Erfasst werden können

– die verwendeten Browsertypen und Versionen

– das vom zugreifenden System verwendete Betriebssystem

– die Website, von der aus der Zugriff erfolgt (Referrer-URL)

– die Unterwebseiten, die über ein zugreifendes System auf diese Internetseite angesteuert werden

– das Datum und die Uhrzeit eines Zugriffs

– eine Internet-Protokoll-Adresse (IP-Adresse)

– der Internet-Service-Provider des zugreifenden Systems

– sonstige ähnliche Daten und Informationen, die der Gefahrenabwehr im Falle von Angriffen auf unsere informationstechnologischen Systeme dienen

Bei der Nutzung dieser allgemeinen Daten und Informationen zieht ABC Abel Bau – Consulting keine Rückschlüsse auf die betroffene Person.

Diese Informationen werden vielmehr benötigt, um

– die Inhalte unserer Internetseite korrekt auszuliefern

– die dauerhafte Funktionsfähigkeit unserer informationstechnologischen Systeme und der Technik unserer Internetseite zu gewährleisten

– um Strafverfolgungsbehörden im Falle eines Cyberangriffes die zur Strafverfolgung notwendigen Informationen bereitzustellen

**Datenübermittlung an Auftragsverarbeiter**

Ist es im Rahmen unserer Verarbeitung nötig, Dritte mit der Verarbeitung von Daten auf Grundlage eines sog. „Auftragsverarbeitungsvertrages“ zu beauftragen, geschieht das auf Grundlage des Art. 28 DSGVO.

**Verwendung von Scriptbibliotheken (Google Webfonts)**

Um unsere Inhalte browserübergreifend korrekt und grafisch ansprechend darzustellen, verwenden wir auf dieser Website Scriptbibliotheken und Schriftbibliotheken wie z. B. Google Webfonts (https://www.google.com/webfonts/). Google Webfonts werden zur Vermeidung mehrfachen Ladens in den Cache Ihres Browsers übertragen. Falls der Browser die Google Webfonts nicht unterstützt oder den Zugriff unterbindet, werden Inhalte in einer Standardschrift angezeigt.

Der Aufruf von Scriptbibliotheken oder Schriftbibliotheken löst automatisch eine Verbindung zum Betreiber der Bibliothek aus. Dabei ist es theoretisch möglich – aktuell allerdings auch unklar ob und ggf. zu welchen Zwecken – dass Betreiber entsprechender Bibliotheken Daten erheben.

Die Datenschutzrichtlinie des Bibliothekbetreibers Google finden Sie hier: [www.google.com/policies/privacy/](https://www.google.com/policies/privacy/)

**Verwendung von Google Maps**

Diese Webseite verwendet Google Maps API, um geographische Informationen visuell darzustellen. Bei der Nutzung von Google Maps werden von Google auch Daten über die Nutzung der Kartenfunktionen durch Besucher erhoben, verarbeitet und genutzt. Nähere Informationen über die Datenverarbeitung durch Google können Sie den [Google-Datenschutzhinweisen](https://policies.google.com/privacy?hl=de) entnehmen. Dort können Sie im Datenschutzcenter auch Ihre persönlichen Datenschutz-Einstellungen verändern.

Ausführliche Anleitungen zur Verwaltung der eigenen Daten im Zusammenhang mit Google-Produkten [finden Sie hier](https://support.google.com/accounts/answer/3024190).

**Datenschutzerklärung für die Nutzung von Facebook-Plugins (Like-Button)**

Auf unseren Seiten sind Plugins des sozialen Netzwerks Facebook (Facebook Inc., 1601 Willow Road, Menlo Park, California, 94025, USA) integriert. Sie erkennen sie an dem Facebook-Logo auf unserer Website. Eine Übersicht über die Facebook-Plugins finden Sie hier: [developers.facebook.com/docs/plugins/](http://developers.facebook.com/docs/plugins/).

Wenn Sie unsere Seiten besuchen, wird über das Plugin eine direkte Verbindung zwischen Ihrem Browser und dem Facebook-Server hergestellt. Facebook erhält dadurch die Information, dass Sie mit Ihrer IP-Adresse unsere Seite besucht haben. Wenn Sie den Facebook-Button anklicken während Sie in Ihrem Facebook-Account eingeloggt sind, können Sie die Inhalte unserer Seiten auf Ihrem Facebook-Profil verlinken. Dadurch kann Facebook den Besuch unserer Seiten Ihrem Benutzerkonto zuordnen. Wir weisen darauf hin, dass wir als Anbieter der Seiten keine Kenntnis vom Inhalt der übermittelten Daten sowie deren Nutzung durch Facebook erhalten. Weitere Informationen hierzu finden Sie in der Datenschutzerklärung von facebook unter [de-de.facebook.com/policy.php](http://de-de.facebook.com/policy.php)

Wenn Sie nicht wünschen, dass Facebook den Besuch unserer Seiten Ihrem Facebook-Nutzerkonto zuordnen kann, loggen Sie sich bitte aus Ihrem Facebook-Benutzerkonto aus.

**Routinemäßige Löschung und Sperrung von personenbezogenen Daten**

Die Daten der betroffenen Person werden nur für den Zeitraum verarbeitet und gespeichert, der zur Erreichung des Speicherungszwecks erforderlich ist oder dies durch den Europäischen Richtlinien- und Verordnungsgeber oder einen anderen Gesetzgeber in Gesetzen oder Vorschriften, welchen der für die Verarbeitung Verantwortliche unterliegt, vorgesehen wurde.

Entfällt der Speicherungszweck oder läuft eine vom Europäischen Richtlinien- und Verordnungsgeber oder einem anderen zuständigen Gesetzgeber vorgeschriebene Speicherfrist ab, werden die personenbezogenen Daten routinemäßig und entsprechend den gesetzlichen Vorschriften gesperrt oder gelöscht.

**Rechte betroffener Person**

Sie haben das Recht

– gemäß Art. 15 DSGVO Auskunft über Ihre von uns verarbeiteten personenbezogenen Daten zu verlangen

– gemäß Art. 16 DSGVO unverzüglich die Berichtigung unrichtiger oder Vervollständigung Ihrer bei uns gespeicherten personenbezogenen Daten zu verlangen

– gemäß Art. 17 DSGVO die Löschung Ihrer bei uns gespeicherten personenbezogenen Daten zu verlangen, soweit nicht die Verarbeitung zur Ausübung des Rechts auf freie Meinungsäußerung und Information, zur Erfüllung einer rechtlichen Verpflichtung, aus Gründen des öffentlichen Interesses oder zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen erforderlich ist

– gemäß Art. 18 DSGVO die Einschränkung der Verarbeitung Ihrer personenbezogenen Daten zu verlangen, soweit die Richtigkeit der Daten von Ihnen bestritten wird, die Verarbeitung unrechtmäßig ist, Sie aber deren Löschung ablehnen und wir die Daten nicht mehr benötigen, Sie jedoch diese zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen benötigen oder Sie gemäß Art. 21 DSGVO Widerspruch gegen die Verarbeitung eingelegt haben

– gemäß Art. 20 DSGVO Ihre personenbezogenen Daten, die Sie uns bereitgestellt haben, in einem strukturierten, gängigen und maschinenlesebaren Format zu erhalten oder die Übermittlung an einen anderen Verantwortlichen zu verlangen

– gemäß Art. 7 Abs. 3 DSGVO Ihre einmal erteilte Einwilligung jederzeit gegenüber uns zu widerrufen. Dies hat zur Folge, dass wir die Datenverarbeitung, die auf dieser Einwilligung beruhte, für die Zukunft nicht mehr fortführen dürfen

– gemäß Art. 77 DSGVO sich bei einer Aufsichtsbehörde zu beschweren.

**Aktualität und Änderung dieser Datenschutzerklärung**

Diese Datenschutzerklärung ist aktuell gültig (Stand Mai 2018).

Durch die Weiterentwicklung unserer Website und Angebote darüber oder aufgrund geänderter gesetzlicher beziehungsweise behördlicher Vorgaben kann es notwendig werden, diese Datenschutzerklärung zu ändern. Die jeweils aktuelle Datenschutzerklärung kann jederzeit auf der Website unter *[www.abc-bauconsulting.de/datenschutz.html](../datenschutz.html)* von Ihnen abgerufen und ausgedruckt werden.

Teile der Datenschutzerklärung wurden mit dem [Datenschutzerklärungs-Generator der activeMind AG](https://www.activemind.de/datenschutz/datenschutzhinweis-generator/) erstellt.
```

**Body heading levels:** H1: Datenschutzerklärung.

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| www.abc-bauconsulting.de | `../index.html` | `https://abc-bauconsulting.de/index.html` | New tab |
| www.google.com/policies/privacy/ | `https://www.google.com/policies/privacy/` | Same as href | New tab |
| Google-Datenschutzhinweisen | `https://policies.google.com/privacy?hl=de` | Same as href | New tab |
| finden Sie hier | `https://support.google.com/accounts/answer/3024190` | Same as href | New tab |
| developers.facebook.com/docs/plugins/ | `http://developers.facebook.com/docs/plugins/` | Same as href | New tab |
| de-de.facebook.com/policy.php | `http://de-de.facebook.com/policy.php` | Same as href | New tab |
| www.abc-bauconsulting.de/datenschutz.html | `../datenschutz.html` | `https://abc-bauconsulting.de/datenschutz.html` | New tab |
| Datenschutzerklärungs-Generator der activeMind AG | `https://www.activemind.de/datenschutz/datenschutzhinweis-generator/` | Same as href | New tab |

<a id="page-p51"></a>
### P51. Disclaimer

**URL:** <https://abc-bauconsulting.de/disclaimer/>  
**Document title:** Disclaimer – ABC Abel Bau-Consulting  
**Hero H1:** Disclaimer  
**Hero image:** [IMG-007](#img-007) — `/2020/10/Kopfbild_Impressum.jpg`  
**Pattern:** Standard page. Global header/menu/contact sidebar/footer.

**Navigation parent/category:** [P49](#page-p49) — `/impressum/`.

**Complete body, in source order:**

```markdown
# Disclaimer

*Haftung für Inhalte*  

Die Inhalte unserer Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen.  

Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei bekannt werden von entsprechenden Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.

**Haftung für Links**  
Unser Angebot enthält Links zu externen Webseiten Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei bekannt werden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.  

**Urheberrecht**  
Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Beiträge Dritter sind als solche gekennzeichnet. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers. Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet.  

Die Betreiber der Seiten sind bemüht, stets die Urheberrechte anderer zu beachten bzw. auf selbst erstellte sowie lizenzfreie Werke zurückzugreifen.

**Datenschutz**  
Soweit auf unseren Seiten personenbezogene Daten (beispielsweise Name, Anschrift oder eMail-Adressen) erhoben werden, erfolgt dies soweit möglich stets auf freiwilliger Basis. Die Nutzung der Angebote und Dienste ist, soweit möglich, stets ohne Angabe personenbezogener Daten möglich.  

Wir weisen darauf hin, dass die Datenübertragung im Internet (z.B. bei der Kommunikation per E-Mail) Sicherheitslücken aufweisen kann. Ein lückenloser Schutz der Daten vor dem Zugriff durch Dritte ist nicht möglich.  

Der Nutzung von im Rahmen der Impressumspflicht veröffentlichten Kontaktdaten durch Dritte zur Übersendung von nicht ausdrücklich angeforderter Werbung und Informationsmaterialien wird hiermit ausdrücklich widersprochen. Die Betreiber der Seiten behalten sich ausdrücklich rechtliche Schritte im Falle der unverlangten Zusendung von Werbeinformationen, etwa durch Spam-Mails, vor.  

Quelle: eRecht24.de
```

**Body heading levels:** H1: Disclaimer.

<a id="page-p52"></a>
### P52. Referenz-Template

**URL:** <https://abc-bauconsulting.de/referenz-template/>  
**Document title:** Referenz-Template – ABC Abel Bau-Consulting  
**Hero H1:** Referenz-Template  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Published reference template. Global header/menu/contact sidebar/footer.

**Discovery:** Published page found in the WordPress sitemap; absent from the normal menu and incoming content links.

**Complete body, in source order:**

```markdown
![IMG-001][IMG-001]

| | |
|---|---|
| Objekt: | … |
| Bauherr: | … |
| Auftraggeber: | … |
| Leistungen: | … |

- Vorherige Referenz
- [Alle Referenzen](https://abc-bauconsulting.de/referenzen/)
- Nächste Referenz

[Vorherige]()

[Alle Referenzen](https://abc-bauconsulting.de/referenzen/)

[Nächste]()
```

**Body image placement / exact source attributes:**

| Order | Picture | Source path | Declared width × height | Alt text | Wrapping link |
|---|---|---|---|---|---|
| 1 | [IMG-001](#img-001) | `/2020/08/Abel_Logo.png` | 190 × 100 | Empty | None |

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Vorherige | `` | `https://abc-bauconsulting.de/referenz-template/` | Same tab |
| Alle Referenzen | `https://abc-bauconsulting.de/referenzen/` | Same as href | Same tab |
| Nächste | `` | `https://abc-bauconsulting.de/referenz-template/` | Same tab |

<a id="page-p53"></a>
### P53. Blog

**URL:** <https://abc-bauconsulting.de/blog/>  
**Document title:** Blog – ABC Abel Bau-Consulting  
**Hero H1:** Blog  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Empty blog; no sidebar. Global header/menu/footer; no contact sidebar.

**Discovery:** Published page found in the WordPress sitemap; absent from the normal menu and incoming content links.

**Body:** Empty posts area, no posts, empty-state message, pagination or sidebar.

<a id="page-p54"></a>
### P54. Sample Page

**URL:** <https://abc-bauconsulting.de/sample-page/>  
**Document title:** Sample Page – ABC Abel Bau-Consulting  
**Hero H1:** Sample Page  
**Hero image:** [IMG-067](#img-067) — `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg`  
**Pattern:** Published sample page. Global header/menu/contact sidebar/footer.

**Discovery:** Published page found in the WordPress sitemap; absent from the normal menu and incoming content links.

**Complete body, in source order:**

```markdown
This is an example page. It’s different from a blog post because it will stay in one place and will show up in your site navigation (in most themes). Most people start with an About page that introduces them to potential site visitors. It might say something like this:

> Hi there! I’m a bike messenger by day, aspiring actor by night, and this is my website. I live in Los Angeles, have a great dog named Jack, and I like piña coladas. (And gettin‘ caught in the rain.)

…or something like this:

> The XYZ Doohickey Company was founded in 1971, and has been providing quality doohickeys to the public ever since. Located in Gotham City, XYZ employs over 2,000 people and does all kinds of awesome things for the Gotham community.

As a new WordPress user, you should go to [your dashboard](http://abc-bauconsulting.de/wp-admin/) to delete this page and create new pages for your content. Have fun!
```

**Body link behavior:**

| Label / image | Original href | Resolved destination if relative | Opens |
|---|---|---|---|
| your dashboard | `http://abc-bauconsulting.de/wp-admin/` | Same as href | Same tab |

**Layout:** Introductory English paragraph → blockquote example → linking phrase → second blockquote example → dashboard instruction. This is a public WordPress default page, not company-authored consultancy copy.


### Linked legacy URLs: existing 404 state

The two recursively discovered URLs `/index.html` and `/datenschutz.html` both return HTTP 404 with the same themed error page. They are not additional published pages in the 54-page catalog, but their existing user-facing state is part of the link audit.

**Document title:** `Seite nicht gefunden – ABC Abel Bau-Consulting`  
**Hero image:** [IMG-067](#img-067)  
**Hero H1, verbatim:**

```text
Diese Seite konnte leider nicht gefunden werden.
```

**Body, verbatim:**

```text
Das Gesuchte konnte leider nicht gefunden werden. Vielleicht hilft die Suchfunktion.
```

A body search form follows, with assistive label “Suchen nach:”, visible search label/placeholder “Suchen …”, and submit label “Suchen”. It uses the same GET `/` form and `s` parameter as the navbar search. The page has the shared utility strip, logo, main menu and footer, but no contact/credential sidebar. The body is a centered, narrow column inside the white raised-panel/blog-style layout. No new image asset is introduced by this error state.

## 6. Complete image register

The register identifies **83 available picture families**: 82 displayed logo/photo/header families plus the browser-icon family. It also records one missing legacy image, for **84 picture references in total**. The source references **354 distinct upload paths** across these families; every one returned HTTP 200 during the audit. The separately listed legacy agency image returns HTTP 404.

A family groups only WordPress size derivatives, the corresponding `-scaled` file, or the rotated variant of the same photograph. Distinct cropped header/logo assets remain distinct families. “Primary source” is an exact URL path used by the site, not an assumed original. Remaining exact paths in the last column are alternatives actually found in `srcset` or icon metadata, not extra photographs.

Image descriptions below are inspection notes, not new captions or assertions of image ownership. Original body/sidebar images have empty `alt` text except the header logo (`ABC Abel Bau-Consulting`). For the missing legacy image, its intended appearance cannot be verified.

| Picture reference | Description / role | Primary source path | Other exact source variants |
|---|---|---|---|
| <a id="img-001"></a>**IMG-001** | Original ABC blue/gray building logo with the company name; used in the published reference template. | `/2020/08/Abel_Logo.png` | None |
| <a id="img-002"></a>**IMG-002** | Red handwritten lettering “Bauen mit Gewinn!” on a gray rectangular background; shared sidebar slogan. | `/2020/08/bauen_mit_gewinn-300x47.png` | `/2020/08/bauen_mit_gewinn.png` |
| <a id="img-003"></a>**IMG-003** | Browser/site-icon crop of the ABC branding; favicon, touch icon and Microsoft tile sizes. | `/2020/08/cropped-Abel_Logo-1-180x180.png` | `/2020/08/cropped-Abel_Logo-1-192x192.png`<br>`/2020/08/cropped-Abel_Logo-1-270x270.png`<br>`/2020/08/cropped-Abel_Logo-1-32x32.png` |
| <a id="img-004"></a>**IMG-004** | Cropped blue/gray geometric building logo, ABC lettering and Abel Bau-Consulting wordmark; shared header home link. | `/2020/08/cropped-Abel_Logo.png` | None |
| <a id="img-005"></a>**IMG-005** | Wide collage of a pedestrian bridge, Rennsteig road-tunnel portals and a tall highway bridge; homepage hero. | `/2020/09/Kopfbild_Start.jpg` | None |
| <a id="img-006"></a>**IMG-006** | Portrait crop of Volker Abel wearing a white hard hat and red checked shirt at a bridge construction site. | `/2020/09/Volker.jpg` | `/2020/09/Volker-300x260.jpg` |
| <a id="img-007"></a>**IMG-007** | Wide photograph of the twin Rennsteig tunnel portals, roadway, wooded hillside and traffic; legal-page hero. | `/2020/10/Kopfbild_Impressum.jpg` | None |
| <a id="img-008"></a>**IMG-008** | Wide village panorama below a hilltop castle/tower, with fields and clouds; contact-page hero. | `/2020/10/Kopfbild_Kontakt.jpg` | None |
| <a id="img-009"></a>**IMG-009** | Construction schedule/Gantt table blended with the underside of a tall concrete bridge; services hero. | `/2020/10/Kopfbild_Leistungsspektrum.jpg` | None |
| <a id="img-010"></a>**IMG-010** | Curved pedestrian bridge above road/rail infrastructure with houses and trees behind; reference-index hero. | `/2020/10/Kopfbild_Referenzen.jpg` | None |
| <a id="img-011"></a>**IMG-011** | Desk still life with drawings/maps, calculator, pen, yellow book and ABC-branded hard hat; seminar-page hero. | `/2020/10/Kopfbild_Seminare.jpg` | None |
| <a id="img-012"></a>**IMG-012** | Blue/gray abstract expert-witness credential mark; IHK.de sidebar badge. | `/2020/10/Logo_Sachverstand.png` | None |
| <a id="img-013"></a>**IMG-013** | Portrait view along the tall Döllbach bridge piers and underside. | `/2020/10/Ref_Gutachten_Doellbach_1-1024x768.jpg` | `/2020/10/Ref_Gutachten_Doellbach_1-1536x1152.jpg`<br>`/2020/10/Ref_Gutachten_Doellbach_1-2048x1536.jpg`<br>`/2020/10/Ref_Gutachten_Doellbach_1-300x225.jpg`<br>`/2020/10/Ref_Gutachten_Doellbach_1-768x576.jpg` |
| <a id="img-014"></a>**IMG-014** | Bridge deck/roadway undergoing works, with exposed work areas and barriers. | `/2020/10/Ref_Gutachten_Doellbach_2-1024x768.jpg` | `/2020/10/Ref_Gutachten_Doellbach_2-1536x1152.jpg`<br>`/2020/10/Ref_Gutachten_Doellbach_2-2048x1536.jpg`<br>`/2020/10/Ref_Gutachten_Doellbach_2-300x225.jpg`<br>`/2020/10/Ref_Gutachten_Doellbach_2-768x576.jpg` |
| <a id="img-015"></a>**IMG-015** | Modern Max Planck institute building complex and paved forecourt. | `/2020/10/Ref_Gutachten_Hirnforschung_1.jpg` | `/2020/10/Ref_Gutachten_Hirnforschung_1-300x200.jpg`<br>`/2020/10/Ref_Gutachten_Hirnforschung_1-360x240.jpg`<br>`/2020/10/Ref_Gutachten_Hirnforschung_1-768x512.jpg` |
| <a id="img-016"></a>**IMG-016** | White multi-family house with balconies and parked cars; defect-remediation-cost case. | `/2020/10/Ref_Gutachten_Radny_1-1024x768.jpg` | `/2020/10/Ref_Gutachten_Radny_1-1536x1152.jpg`<br>`/2020/10/Ref_Gutachten_Radny_1-2048x1536.jpg`<br>`/2020/10/Ref_Gutachten_Radny_1-300x225.jpg`<br>`/2020/10/Ref_Gutachten_Radny_1-768x576.jpg` |
| <a id="img-017"></a>**IMG-017** | Portrait street view of a scaffolded building during attic conversion. | `/2020/10/Ref_Hoch_Dachgeschoss_1-768x1024.jpg` | `/2020/10/Ref_Hoch_Dachgeschoss_1-1152x1536.jpg`<br>`/2020/10/Ref_Hoch_Dachgeschoss_1-1536x2048.jpg`<br>`/2020/10/Ref_Hoch_Dachgeschoss_1-225x300.jpg`<br>`/2020/10/Ref_Hoch_Dachgeschoss_1-scaled.jpg` |
| <a id="img-018"></a>**IMG-018** | Finished bright attic/maisonette interior with exposed white structure, roof windows and stair opening. | `/2020/10/Ref_Hoch_Dachgeschoss_2-1024x768.jpg` | `/2020/10/Ref_Hoch_Dachgeschoss_2-1536x1152.jpg`<br>`/2020/10/Ref_Hoch_Dachgeschoss_2-2048x1536.jpg`<br>`/2020/10/Ref_Hoch_Dachgeschoss_2-300x225.jpg`<br>`/2020/10/Ref_Hoch_Dachgeschoss_2-768x576.jpg` |
| <a id="img-019"></a>**IMG-019** | Portrait street view of the completed residential facade and attic conversion. | `/2020/10/Ref_Hoch_Dachgeschoss_3-768x1024.jpg` | `/2020/10/Ref_Hoch_Dachgeschoss_3-1152x1536.jpg`<br>`/2020/10/Ref_Hoch_Dachgeschoss_3-1536x2048.jpg`<br>`/2020/10/Ref_Hoch_Dachgeschoss_3-225x300.jpg`<br>`/2020/10/Ref_Hoch_Dachgeschoss_3-scaled.jpg` |
| <a id="img-020"></a>**IMG-020** | Exterior of the modern light-clad university veterinary clinic building. | `/2020/10/Ref_Hoch_Kleintier_1-1024x768.jpg` | `/2020/10/Ref_Hoch_Kleintier_1-1536x1152.jpg`<br>`/2020/10/Ref_Hoch_Kleintier_1-2048x1536.jpg`<br>`/2020/10/Ref_Hoch_Kleintier_1-300x225.jpg`<br>`/2020/10/Ref_Hoch_Kleintier_1-768x576.jpg` |
| <a id="img-021"></a>**IMG-021** | Clinic construction/exterior seen across rail tracks. | `/2020/10/Ref_Hoch_Kleintier_2-1024x768.jpg` | `/2020/10/Ref_Hoch_Kleintier_2-1536x1152.jpg`<br>`/2020/10/Ref_Hoch_Kleintier_2-2048x1536.jpg`<br>`/2020/10/Ref_Hoch_Kleintier_2-300x225.jpg`<br>`/2020/10/Ref_Hoch_Kleintier_2-768x576.jpg` |
| <a id="img-022"></a>**IMG-022** | Westpfalz hospital tower with the circular helicopter landing platform. | `/2020/10/Ref_Hoch_WPKlinik_1-1024x768.jpg` | `/2020/10/Ref_Hoch_WPKlinik_1-1536x1152.jpg`<br>`/2020/10/Ref_Hoch_WPKlinik_1-2048x1536.jpg`<br>`/2020/10/Ref_Hoch_WPKlinik_1-300x225.jpg`<br>`/2020/10/Ref_Hoch_WPKlinik_1-768x576.jpg` |
| <a id="img-023"></a>**IMG-023** | Hospital complex and helipad seen above a low foreground roof. | `/2020/10/Ref_Hoch_WPKlinik_2-1024x768.jpg` | `/2020/10/Ref_Hoch_WPKlinik_2-1536x1152.jpg`<br>`/2020/10/Ref_Hoch_WPKlinik_2-2048x1536.jpg`<br>`/2020/10/Ref_Hoch_WPKlinik_2-300x225.jpg`<br>`/2020/10/Ref_Hoch_WPKlinik_2-768x576.jpg` |
| <a id="img-024"></a>**IMG-024** | Portrait night view of the illuminated hospital tower and helicopter platform; source includes rotated derivative. | `/2020/10/Ref_Hoch_WPKlinik_3-768x1024.jpg` | `/2020/10/Ref_Hoch_WPKlinik_3-1152x1536.jpg`<br>`/2020/10/Ref_Hoch_WPKlinik_3-225x300.jpg`<br>`/2020/10/Ref_Hoch_WPKlinik_3-rotated.jpg` |
| <a id="img-025"></a>**IMG-025** | Scaffolded hospital building/tower under construction, with crane. | `/2020/10/Ref_Hoch_WPKlinik_4-1024x768.jpg` | `/2020/10/Ref_Hoch_WPKlinik_4-1536x1152.jpg`<br>`/2020/10/Ref_Hoch_WPKlinik_4-2048x1536.jpg`<br>`/2020/10/Ref_Hoch_WPKlinik_4-300x225.jpg`<br>`/2020/10/Ref_Hoch_WPKlinik_4-768x576.jpg` |
| <a id="img-026"></a>**IMG-026** | Distant panorama of the Lockwitz valley bridge above wooded slopes. | `/2020/10/Ref_Ing_Lockwitz_1-1024x768.jpg` | `/2020/10/Ref_Ing_Lockwitz_1-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Lockwitz_1-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Lockwitz_1-300x225.jpg`<br>`/2020/10/Ref_Ing_Lockwitz_1-768x576.jpg` |
| <a id="img-027"></a>**IMG-027** | Close low-angle view of the Lockwitz bridge's concrete piers and arched supports against blue sky. | `/2020/10/Ref_Ing_Lockwitz_3-1024x768.jpg` | `/2020/10/Ref_Ing_Lockwitz_3-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Lockwitz_3-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Lockwitz_3-300x225.jpg`<br>`/2020/10/Ref_Ing_Lockwitz_3-768x576.jpg` |
| <a id="img-028"></a>**IMG-028** | Side view of the Lockwitz bridge's arches and piers with snow on the ground. | `/2020/10/Ref_Ing_Lockwitz_4-1024x768.jpg` | `/2020/10/Ref_Ing_Lockwitz_4-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Lockwitz_4-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Lockwitz_4-300x225.jpg`<br>`/2020/10/Ref_Ing_Lockwitz_4-768x576.jpg` |
| <a id="img-029"></a>**IMG-029** | Long side view of the Saale valley bridge above a road and fields. | `/2020/10/Ref_Ing_Saale_1-1024x768.jpg` | `/2020/10/Ref_Ing_Saale_1-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Saale_1-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Saale_1-300x225.jpg`<br>`/2020/10/Ref_Ing_Saale_1-768x576.jpg` |
| <a id="img-030"></a>**IMG-030** | Side view of the Saale bridge from the grassy embankment. | `/2020/10/Ref_Ing_Saale_2-1024x768.jpg` | `/2020/10/Ref_Ing_Saale_2-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Saale_2-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Saale_2-300x225.jpg`<br>`/2020/10/Ref_Ing_Saale_2-768x576.jpg` |
| <a id="img-031"></a>**IMG-031** | View beneath the Saale bridge beside a local road with a parked car. | `/2020/10/Ref_Ing_Saale_3-1024x768.jpg` | `/2020/10/Ref_Ing_Saale_3-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Saale_3-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Saale_3-300x225.jpg`<br>`/2020/10/Ref_Ing_Saale_3-768x576.jpg` |
| <a id="img-032"></a>**IMG-032** | Long side view of the Steinbach bridge spanning a rural valley and fields. | `/2020/10/Ref_Ing_Steinbach_1-1024x768.jpg` | `/2020/10/Ref_Ing_Steinbach_1-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Steinbach_1-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Steinbach_1-300x225.jpg`<br>`/2020/10/Ref_Ing_Steinbach_1-768x576.jpg` |
| <a id="img-033"></a>**IMG-033** | Portrait-format oblique view along the Steinbach bridge deck and piers. | `/2020/10/Ref_Ing_Steinbach_2-768x1024.jpg` | `/2020/10/Ref_Ing_Steinbach_2-1152x1536.jpg`<br>`/2020/10/Ref_Ing_Steinbach_2-1536x2048.jpg`<br>`/2020/10/Ref_Ing_Steinbach_2-225x300.jpg`<br>`/2020/10/Ref_Ing_Steinbach_2-scaled.jpg` |
| <a id="img-034"></a>**IMG-034** | View from beneath the Steinbach bridge deck, showing piers and grassy valley floor. | `/2020/10/Ref_Ing_Steinbach_3-1024x768.jpg` | `/2020/10/Ref_Ing_Steinbach_3-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Steinbach_3-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Steinbach_3-300x225.jpg`<br>`/2020/10/Ref_Ing_Steinbach_3-768x576.jpg` |
| <a id="img-035"></a>**IMG-035** | Low view between the two Teufelstal bridge structures, emphasizing the curved supports. | `/2020/10/Ref_Ing_Teufelstal_1-1024x768.jpg` | `/2020/10/Ref_Ing_Teufelstal_1-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Teufelstal_1-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Teufelstal_1-300x225.jpg`<br>`/2020/10/Ref_Ing_Teufelstal_1-768x576.jpg` |
| <a id="img-036"></a>**IMG-036** | Oblique side view of the Thalwasser bridge and its piers above grassland. | `/2020/10/Ref_Ing_Thalwasser_1-1024x768.jpg` | `/2020/10/Ref_Ing_Thalwasser_1-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Thalwasser_1-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Thalwasser_1-300x225.jpg`<br>`/2020/10/Ref_Ing_Thalwasser_1-768x576.jpg` |
| <a id="img-037"></a>**IMG-037** | View along the underside of the Thalwasser bridge, piers and service track. | `/2020/10/Ref_Ing_Thalwasser_2-1024x768.jpg` | `/2020/10/Ref_Ing_Thalwasser_2-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Thalwasser_2-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Thalwasser_2-300x225.jpg`<br>`/2020/10/Ref_Ing_Thalwasser_2-768x576.jpg` |
| <a id="img-038"></a>**IMG-038** | Low-angle view of the Thalwasser bridge underside and branching pier heads. | `/2020/10/Ref_Ing_Thalwasser_3-1024x768.jpg` | `/2020/10/Ref_Ing_Thalwasser_3-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Thalwasser_3-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Thalwasser_3-300x225.jpg`<br>`/2020/10/Ref_Ing_Thalwasser_3-768x576.jpg` |
| <a id="img-039"></a>**IMG-039** | Bridge works over a watercourse, with temporary sheet-pile walls and crossing supports. | `/2020/10/Ref_Ing_Trebur_1-1024x768.jpg` | `/2020/10/Ref_Ing_Trebur_1-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Trebur_1-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Trebur_1-300x225.jpg`<br>`/2020/10/Ref_Ing_Trebur_1-768x576.jpg` |
| <a id="img-040"></a>**IMG-040** | Small bridge over a stream during construction, with works equipment and autumn trees. | `/2020/10/Ref_Ing_Trebur_2-1024x768.jpg` | `/2020/10/Ref_Ing_Trebur_2-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Trebur_2-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Trebur_2-300x225.jpg`<br>`/2020/10/Ref_Ing_Trebur_2-768x576.jpg` |
| <a id="img-041"></a>**IMG-041** | Completed small road bridge/culvert over the watercourse with grassy banks. | `/2020/10/Ref_Ing_Trebur_3-1024x768.jpg` | `/2020/10/Ref_Ing_Trebur_3-1536x1152.jpg`<br>`/2020/10/Ref_Ing_Trebur_3-2048x1536.jpg`<br>`/2020/10/Ref_Ing_Trebur_3-300x225.jpg`<br>`/2020/10/Ref_Ing_Trebur_3-768x576.jpg` |
| <a id="img-042"></a>**IMG-042** | Overview of a large deep excavation enclosed by retaining/piled walls, with excavators. | `/2020/10/Ref_Spezi_SGTrog_1-1024x768.jpg` | `/2020/10/Ref_Spezi_SGTrog_1-1536x1152.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_1-300x225.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_1-768x576.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_1.jpg` |
| <a id="img-043"></a>**IMG-043** | Concrete trough/ramp under construction with cranes and site equipment. | `/2020/10/Ref_Spezi_SGTrog_3-1024x768.jpg` | `/2020/10/Ref_Spezi_SGTrog_3-1536x1152.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_3-2048x1536.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_3-300x225.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_3-768x576.jpg` |
| <a id="img-044"></a>**IMG-044** | Close view along tall concrete trough walls and active construction works. | `/2020/10/Ref_Spezi_SGTrog_4-1024x768.jpg` | `/2020/10/Ref_Spezi_SGTrog_4-1536x1152.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_4-2048x1536.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_4-300x225.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_4-768x576.jpg` |
| <a id="img-045"></a>**IMG-045** | Excavator at the bottom of the excavation beside exposed piled retaining walls. | `/2020/10/Ref_Spezi_SGTrog_5-1024x768.jpg` | `/2020/10/Ref_Spezi_SGTrog_5-1536x1152.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_5-300x225.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_5-768x576.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_5.jpg` |
| <a id="img-046"></a>**IMG-046** | Curved and straight concrete trough walls near completion. | `/2020/10/Ref_Spezi_SGTrog_6-1024x768.jpg` | `/2020/10/Ref_Spezi_SGTrog_6-1536x1152.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_6-2048x1536.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_6-300x225.jpg`<br>`/2020/10/Ref_Spezi_SGTrog_6-768x576.jpg` |
| <a id="img-047"></a>**IMG-047** | Portrait view of trench/road works and excavator beside a university building. | `/2020/10/Ref_Tief_ErwUni_1-768x1024.jpg` | `/2020/10/Ref_Tief_ErwUni_1-1152x1536.jpg`<br>`/2020/10/Ref_Tief_ErwUni_1-1536x2048.jpg`<br>`/2020/10/Ref_Tief_ErwUni_1-225x300.jpg`<br>`/2020/10/Ref_Tief_ErwUni_1-scaled.jpg` |
| <a id="img-048"></a>**IMG-048** | Excavated ground and earthmoving equipment next to the university extension. | `/2020/10/Ref_Tief_ErwUni_2-1024x768.jpg` | `/2020/10/Ref_Tief_ErwUni_2-1536x1152.jpg`<br>`/2020/10/Ref_Tief_ErwUni_2-2048x1536.jpg`<br>`/2020/10/Ref_Tief_ErwUni_2-300x225.jpg`<br>`/2020/10/Ref_Tief_ErwUni_2-768x576.jpg` |
| <a id="img-049"></a>**IMG-049** | Excavator working on earth piles at the university site in misty conditions. | `/2020/10/Ref_Tief_ErwUni_3-1024x576.jpg` | `/2020/10/Ref_Tief_ErwUni_3-300x169.jpg`<br>`/2020/10/Ref_Tief_ErwUni_3-768x432.jpg`<br>`/2020/10/Ref_Tief_ErwUni_3.jpg` |
| <a id="img-050"></a>**IMG-050** | Asphalt paving machine working beside an open industrial shed. | `/2020/10/Ref_Tief_Kompost_1-1024x768.jpg` | `/2020/10/Ref_Tief_Kompost_1-1536x1152.jpg`<br>`/2020/10/Ref_Tief_Kompost_1-2048x1536.jpg`<br>`/2020/10/Ref_Tief_Kompost_1-300x225.jpg`<br>`/2020/10/Ref_Tief_Kompost_1-768x576.jpg` |
| <a id="img-051"></a>**IMG-051** | Surfaced industrial yard between composting/processing buildings. | `/2020/10/Ref_Tief_Kompost_2-1024x768.jpg` | `/2020/10/Ref_Tief_Kompost_2-1536x1152.jpg`<br>`/2020/10/Ref_Tief_Kompost_2-2048x1536.jpg`<br>`/2020/10/Ref_Tief_Kompost_2-300x225.jpg`<br>`/2020/10/Ref_Tief_Kompost_2-768x576.jpg` |
| <a id="img-052"></a>**IMG-052** | Exterior panorama of the composting/biogas facility, with bare foreground earth. | `/2020/10/Ref_Tief_Kompost_3-1024x576.jpg` | `/2020/10/Ref_Tief_Kompost_3-1536x864.jpg`<br>`/2020/10/Ref_Tief_Kompost_3-2048x1152.jpg`<br>`/2020/10/Ref_Tief_Kompost_3-300x169.jpg`<br>`/2020/10/Ref_Tief_Kompost_3-768x432.jpg` |
| <a id="img-053"></a>**IMG-053** | Excavators and red-earth trenching works on a rural water-supply route. | `/2020/10/Ref_Tief_Sembach1_1-1024x768.jpg` | `/2020/10/Ref_Tief_Sembach1_1-1536x1152.jpg`<br>`/2020/10/Ref_Tief_Sembach1_1-2048x1536.jpg`<br>`/2020/10/Ref_Tief_Sembach1_1-300x225.jpg`<br>`/2020/10/Ref_Tief_Sembach1_1-768x576.jpg` |
| <a id="img-054"></a>**IMG-054** | Earthworks and trench route across a field, with excavating machinery. | `/2020/10/Ref_Tief_Sembach2_1-1024x768.jpg` | `/2020/10/Ref_Tief_Sembach2_1-1536x1152.jpg`<br>`/2020/10/Ref_Tief_Sembach2_1-2048x1536.jpg`<br>`/2020/10/Ref_Tief_Sembach2_1-300x225.jpg`<br>`/2020/10/Ref_Tief_Sembach2_1-768x576.jpg` |
| <a id="img-055"></a>**IMG-055** | Portrait view of a narrow trench with blue water pipe and a worker. | `/2020/10/Ref_Tief_Sembach2_2-768x1024.jpg` | `/2020/10/Ref_Tief_Sembach2_2-1152x1536.jpg`<br>`/2020/10/Ref_Tief_Sembach2_2-1536x2048.jpg`<br>`/2020/10/Ref_Tief_Sembach2_2-225x300.jpg`<br>`/2020/10/Ref_Tief_Sembach2_2-scaled.jpg` |
| <a id="img-056"></a>**IMG-056** | Elevated overview of extensive urban utility/road works around Skyline Plaza. | `/2020/10/Ref_Tief_Trassenumlegung_1-1024x768.jpg` | `/2020/10/Ref_Tief_Trassenumlegung_1-1536x1152.jpg`<br>`/2020/10/Ref_Tief_Trassenumlegung_1-2048x1536.jpg`<br>`/2020/10/Ref_Tief_Trassenumlegung_1-300x225.jpg`<br>`/2020/10/Ref_Tief_Trassenumlegung_1-768x576.jpg` |
| <a id="img-057"></a>**IMG-057** | Street-level Skyline Plaza junction with barriers and road signs. | `/2020/10/Ref_Tief_Trassenumlegung_2-1024x768.jpg` | `/2020/10/Ref_Tief_Trassenumlegung_2-1536x1152.jpg`<br>`/2020/10/Ref_Tief_Trassenumlegung_2-2048x1536.jpg`<br>`/2020/10/Ref_Tief_Trassenumlegung_2-300x225.jpg`<br>`/2020/10/Ref_Tief_Trassenumlegung_2-768x576.jpg` |
| <a id="img-058"></a>**IMG-058** | Exposed utility pipes and cables in a street excavation with site machinery. | `/2020/10/Ref_Tief_Trassenumlegung_3-1024x768.jpg` | `/2020/10/Ref_Tief_Trassenumlegung_3-1536x1152.jpg`<br>`/2020/10/Ref_Tief_Trassenumlegung_3-2048x1536.jpg`<br>`/2020/10/Ref_Tief_Trassenumlegung_3-300x225.jpg`<br>`/2020/10/Ref_Tief_Trassenumlegung_3-768x576.jpg` |
| <a id="img-059"></a>**IMG-059** | Volker Abel seated at his office desk, with drawings, computer, books and window behind. | `/2020/10/Volker_1-1024x683.jpg` | `/2020/10/Volker_1-2048x1365.jpg`<br>`/2020/10/Volker_1-300x200.jpg`<br>`/2020/10/Volker_1-360x240.jpg`<br>`/2020/10/Volker_1-768x512.jpg` |
| <a id="img-060"></a>**IMG-060** | Volker Abel in hard hat standing beside bridge construction, temporary support frames and concrete works. | `/2020/10/Volker_2-scaled.jpg` | `/2020/10/Volker_2-2048x1365.jpg`<br>`/2020/10/Volker_2-300x200.jpg`<br>`/2020/10/Volker_2-768x512.jpg` |
| <a id="img-061"></a>**IMG-061** | DGA BAU logo with dark blue DGA and red BAU lettering on white; sidebar badge. | `/2021/05/DGA_BAU_Logo_neu-150x150.jpg` | None |
| <a id="img-062"></a>**IMG-062** | Old masonry retaining wall with metal railing beside the botanical garden. | `/2021/08/20180426_102012-1024x576.jpg` | `/2021/08/20180426_102012-1536x864.jpg`<br>`/2021/08/20180426_102012-2048x1152.jpg`<br>`/2021/08/20180426_102012-300x169.jpg`<br>`/2021/08/20180426_102012-768x432.jpg` |
| <a id="img-063"></a>**IMG-063** | Residential high-rise wrapped in scaffolding during facade/energy renovation. | `/2021/08/20180803_130745-1024x576.jpg` | `/2021/08/20180803_130745-1536x864.jpg`<br>`/2021/08/20180803_130745-2048x1152.jpg`<br>`/2021/08/20180803_130745-300x169.jpg`<br>`/2021/08/20180803_130745-768x432.jpg` |
| <a id="img-064"></a>**IMG-064** | Panoramic crop of Volker Abel at a bridge construction site; he appears toward the left of the scene; about-page hero. | `/2021/08/54C2555_logo2_cut-scaled.jpg` | None |
| <a id="img-065"></a>**IMG-065** | Colored technical section/detail drawing associated with the retaining-wall works. | `/2021/08/Screenshot-2021-08-24-153609-1024x640.png` | `/2021/08/Screenshot-2021-08-24-153609-300x188.png`<br>`/2021/08/Screenshot-2021-08-24-153609-768x480.png`<br>`/2021/08/Screenshot-2021-08-24-153609.png` |
| <a id="img-066"></a>**IMG-066** | Portrait site/location plan headed “Übersichtslageplan M = 1:1000”, showing the botanical-garden retaining wall. | `/2021/08/Unbenannt-980x1024.png` | `/2021/08/Unbenannt-1470x1536.png`<br>`/2021/08/Unbenannt-1960x2048.png`<br>`/2021/08/Unbenannt-287x300.png`<br>`/2021/08/Unbenannt-768x803.png` |
| <a id="img-067"></a>**IMG-067** | Volker Abel in a white hard hat and checked shirt at bridge works, placed toward the right; reference/default hero. | `/2021/08/cropped-54C2554_logo_2-scaled-1.jpg` | None |
| <a id="img-068"></a>**IMG-068** | Concrete terminal structure under construction, showing columns, walls and cranes. | `/2022/06/20200430_125134-1024x576.jpg` | `/2022/06/20200430_125134-1536x864.jpg`<br>`/2022/06/20200430_125134-2048x1152.jpg`<br>`/2022/06/20200430_125134-300x169.jpg`<br>`/2022/06/20200430_125134-768x432.jpg` |
| <a id="img-069"></a>**IMG-069** | Panoramic view across the Terminal 3 construction site and cranes. | `/2022/06/20200430_133907-1024x250.jpg` | `/2022/06/20200430_133907-1536x375.jpg`<br>`/2022/06/20200430_133907-2048x499.jpg`<br>`/2022/06/20200430_133907-300x73.jpg`<br>`/2022/06/20200430_133907-768x187.jpg` |
| <a id="img-070"></a>**IMG-070** | Frankfurt Terminal 3 construction site with cranes, concrete works and mobile crane. | `/2022/06/20200608_163259-1024x576.jpg` | `/2022/06/20200608_163259-1536x864.jpg`<br>`/2022/06/20200608_163259-2048x1152.jpg`<br>`/2022/06/20200608_163259-300x169.jpg`<br>`/2022/06/20200608_163259-768x432.jpg` |
| <a id="img-071"></a>**IMG-071** | Aerial terminal/airport overview with colored Flugsteig G construction-phase diagram and legend. | `/2022/06/bd1f2ab3-1867-4262-bebf-c51f00105417.png` | `/2022/06/bd1f2ab3-1867-4262-bebf-c51f00105417-300x122.png`<br>`/2022/06/bd1f2ab3-1867-4262-bebf-c51f00105417-768x311.png` |
| <a id="img-072"></a>**IMG-072** | Urban street and exterior works beside the new Marburg library; church towers in the distance. | `/2022/08/20160912_134023-1024x576.jpg` | `/2022/08/20160912_134023-1536x864.jpg`<br>`/2022/08/20160912_134023-2048x1152.jpg`<br>`/2022/08/20160912_134023-300x169.jpg`<br>`/2022/08/20160912_134023-768x432.jpg` |
| <a id="img-073"></a>**IMG-073** | Portrait view along the modern library facade and newly finished exterior paving. | `/2022/08/20170711_120217-576x1024.jpg` | `/2022/08/20170711_120217-1152x2048.jpg`<br>`/2022/08/20170711_120217-169x300.jpg`<br>`/2022/08/20170711_120217-768x1365.jpg`<br>`/2022/08/20170711_120217-864x1536.jpg`<br>`/2022/08/20170711_120217-scaled.jpg` |
| <a id="img-074"></a>**IMG-074** | Forecourt paving/landscaping works with protected tree trunks and site barriers. | `/2022/08/20190708_140031-1024x576.jpg` | `/2022/08/20190708_140031-1536x864.jpg`<br>`/2022/08/20190708_140031-2048x1152.jpg`<br>`/2022/08/20190708_140031-300x169.jpg`<br>`/2022/08/20190708_140031-768x432.jpg` |
| <a id="img-075"></a>**IMG-075** | Frankfurt-Höchst station building and forecourt during roadworks. | `/2022/08/20190708_140833-1024x576.jpg` | `/2022/08/20190708_140833-1536x864.jpg`<br>`/2022/08/20190708_140833-2048x1152.jpg`<br>`/2022/08/20190708_140833-300x169.jpg`<br>`/2022/08/20190708_140833-768x432.jpg` |
| <a id="img-076"></a>**IMG-076** | Completed station-area road/bus-station space with shelter, signs and paving. | `/2022/08/20200526_132041-1024x576.jpg` | `/2022/08/20200526_132041-1536x864.jpg`<br>`/2022/08/20200526_132041-2048x1152.jpg`<br>`/2022/08/20200526_132041-300x169.jpg`<br>`/2022/08/20200526_132041-768x432.jpg` |
| <a id="img-077"></a>**IMG-077** | Completed Marburg university library entrance/facade with its name signage. | `/2022/08/20200625_134809-1024x576.jpg` | `/2022/08/20200625_134809-1536x864.jpg`<br>`/2022/08/20200625_134809-2048x1152.jpg`<br>`/2022/08/20200625_134809-300x169.jpg`<br>`/2022/08/20200625_134809-768x432.jpg` |
| <a id="img-078"></a>**IMG-078** | Close view of the bridge underside and strengthening structure above the canal. | `/2022/08/20210617_104541-1024x576.jpg` | `/2022/08/20210617_104541-1536x864.jpg`<br>`/2022/08/20210617_104541-2048x1152.jpg`<br>`/2022/08/20210617_104541-300x169.jpg`<br>`/2022/08/20210617_104541-768x432.jpg` |
| <a id="img-079"></a>**IMG-079** | View under the canal bridge with a passing cargo vessel. | `/2022/08/20210617_110237-1024x576.jpg` | `/2022/08/20210617_110237-1536x864.jpg`<br>`/2022/08/20210617_110237-2048x1152.jpg`<br>`/2022/08/20210617_110237-300x169.jpg`<br>`/2022/08/20210617_110237-768x432.jpg` |
| <a id="img-080"></a>**IMG-080** | Side view of the BAB A2 bridge crossing the Mittelland Canal. | `/2022/08/20210617_112506-1024x576.jpg` | `/2022/08/20210617_112506-1536x864.jpg`<br>`/2022/08/20210617_112506-2048x1152.jpg`<br>`/2022/08/20210617_112506-300x169.jpg`<br>`/2022/08/20210617_112506-768x432.jpg` |
| <a id="img-081"></a>**IMG-081** | Narrow exterior work area between university buildings, with scaffolding and containers. | `/2024/02/20211122_155153-1024x768.jpg` | `/2024/02/20211122_155153-1536x1152.jpg`<br>`/2024/02/20211122_155153-2048x1536.jpg`<br>`/2024/02/20211122_155153-300x225.jpg`<br>`/2024/02/20211122_155153-768x576.jpg` |
| <a id="img-082"></a>**IMG-082** | Small tracked excavators and earthworks beside the documentation-center buildings. | `/2024/02/20211122_155355-1024x768.jpg` | `/2024/02/20211122_155355-1536x1152.jpg`<br>`/2024/02/20211122_155355-2048x1536.jpg`<br>`/2024/02/20211122_155355-300x225.jpg`<br>`/2024/02/20211122_155355-768x576.jpg` |
| <a id="img-083"></a>**IMG-083** | Street and sidewalk works beside Marburg's documentation-center/university buildings. | `/2024/02/20230329_110311-1024x768.jpg` | `/2024/02/20230329_110311-1536x1152.jpg`<br>`/2024/02/20230329_110311-2048x1536.jpg`<br>`/2024/02/20230329_110311-300x225.jpg`<br>`/2024/02/20230329_110311-768x576.jpg` |
| <a id="img-084"></a>**IMG-084** | Missing legacy design-agency image, linked to designintime.de; appearance unavailable, HTTP 404. Outside uploads. | `/impressum/fileadmin/user_upload/8c7ec5e7d4.jpg` | Original relative `src`: `fileadmin/user_upload/8c7ec5e7d4.jpg`; no dimensions or alt text provided |

### 6.1 Markdown image-reference definitions

These definitions resolve the `![IMG-...][IMG-...]` markers in the transcribed Markdown. Table paths above omit the upload base as requested; definitions retain fully qualified live URLs for unambiguous resolution. Body transcripts are fenced so that the design document does not expand all photographs at full size.

[IMG-001]: https://abc-bauconsulting.de/wp-content/uploads/2020/08/Abel_Logo.png
[IMG-002]: https://abc-bauconsulting.de/wp-content/uploads/2020/08/bauen_mit_gewinn-300x47.png
[IMG-003]: https://abc-bauconsulting.de/wp-content/uploads/2020/08/cropped-Abel_Logo-1-180x180.png
[IMG-004]: https://abc-bauconsulting.de/wp-content/uploads/2020/08/cropped-Abel_Logo.png
[IMG-005]: https://abc-bauconsulting.de/wp-content/uploads/2020/09/Kopfbild_Start.jpg
[IMG-006]: https://abc-bauconsulting.de/wp-content/uploads/2020/09/Volker.jpg
[IMG-007]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Kopfbild_Impressum.jpg
[IMG-008]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Kopfbild_Kontakt.jpg
[IMG-009]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Kopfbild_Leistungsspektrum.jpg
[IMG-010]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Kopfbild_Referenzen.jpg
[IMG-011]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Kopfbild_Seminare.jpg
[IMG-012]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Logo_Sachverstand.png
[IMG-013]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Gutachten_Doellbach_1-1024x768.jpg
[IMG-014]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Gutachten_Doellbach_2-1024x768.jpg
[IMG-015]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Gutachten_Hirnforschung_1.jpg
[IMG-016]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Gutachten_Radny_1-1024x768.jpg
[IMG-017]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Hoch_Dachgeschoss_1-768x1024.jpg
[IMG-018]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Hoch_Dachgeschoss_2-1024x768.jpg
[IMG-019]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Hoch_Dachgeschoss_3-768x1024.jpg
[IMG-020]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Hoch_Kleintier_1-1024x768.jpg
[IMG-021]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Hoch_Kleintier_2-1024x768.jpg
[IMG-022]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Hoch_WPKlinik_1-1024x768.jpg
[IMG-023]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Hoch_WPKlinik_2-1024x768.jpg
[IMG-024]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Hoch_WPKlinik_3-768x1024.jpg
[IMG-025]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Hoch_WPKlinik_4-1024x768.jpg
[IMG-026]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Lockwitz_1-1024x768.jpg
[IMG-027]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Lockwitz_3-1024x768.jpg
[IMG-028]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Lockwitz_4-1024x768.jpg
[IMG-029]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Saale_1-1024x768.jpg
[IMG-030]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Saale_2-1024x768.jpg
[IMG-031]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Saale_3-1024x768.jpg
[IMG-032]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Steinbach_1-1024x768.jpg
[IMG-033]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Steinbach_2-768x1024.jpg
[IMG-034]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Steinbach_3-1024x768.jpg
[IMG-035]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Teufelstal_1-1024x768.jpg
[IMG-036]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Thalwasser_1-1024x768.jpg
[IMG-037]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Thalwasser_2-1024x768.jpg
[IMG-038]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Thalwasser_3-1024x768.jpg
[IMG-039]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Trebur_1-1024x768.jpg
[IMG-040]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Trebur_2-1024x768.jpg
[IMG-041]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Ing_Trebur_3-1024x768.jpg
[IMG-042]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Spezi_SGTrog_1-1024x768.jpg
[IMG-043]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Spezi_SGTrog_3-1024x768.jpg
[IMG-044]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Spezi_SGTrog_4-1024x768.jpg
[IMG-045]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Spezi_SGTrog_5-1024x768.jpg
[IMG-046]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Spezi_SGTrog_6-1024x768.jpg
[IMG-047]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_ErwUni_1-768x1024.jpg
[IMG-048]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_ErwUni_2-1024x768.jpg
[IMG-049]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_ErwUni_3-1024x576.jpg
[IMG-050]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_Kompost_1-1024x768.jpg
[IMG-051]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_Kompost_2-1024x768.jpg
[IMG-052]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_Kompost_3-1024x576.jpg
[IMG-053]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_Sembach1_1-1024x768.jpg
[IMG-054]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_Sembach2_1-1024x768.jpg
[IMG-055]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_Sembach2_2-768x1024.jpg
[IMG-056]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_Trassenumlegung_1-1024x768.jpg
[IMG-057]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_Trassenumlegung_2-1024x768.jpg
[IMG-058]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Ref_Tief_Trassenumlegung_3-1024x768.jpg
[IMG-059]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Volker_1-1024x683.jpg
[IMG-060]: https://abc-bauconsulting.de/wp-content/uploads/2020/10/Volker_2-scaled.jpg
[IMG-061]: https://abc-bauconsulting.de/wp-content/uploads/2021/05/DGA_BAU_Logo_neu-150x150.jpg
[IMG-062]: https://abc-bauconsulting.de/wp-content/uploads/2021/08/20180426_102012-1024x576.jpg
[IMG-063]: https://abc-bauconsulting.de/wp-content/uploads/2021/08/20180803_130745-1024x576.jpg
[IMG-064]: https://abc-bauconsulting.de/wp-content/uploads/2021/08/54C2555_logo2_cut-scaled.jpg
[IMG-065]: https://abc-bauconsulting.de/wp-content/uploads/2021/08/Screenshot-2021-08-24-153609-1024x640.png
[IMG-066]: https://abc-bauconsulting.de/wp-content/uploads/2021/08/Unbenannt-980x1024.png
[IMG-067]: https://abc-bauconsulting.de/wp-content/uploads/2021/08/cropped-54C2554_logo_2-scaled-1.jpg
[IMG-068]: https://abc-bauconsulting.de/wp-content/uploads/2022/06/20200430_125134-1024x576.jpg
[IMG-069]: https://abc-bauconsulting.de/wp-content/uploads/2022/06/20200430_133907-1024x250.jpg
[IMG-070]: https://abc-bauconsulting.de/wp-content/uploads/2022/06/20200608_163259-1024x576.jpg
[IMG-071]: https://abc-bauconsulting.de/wp-content/uploads/2022/06/bd1f2ab3-1867-4262-bebf-c51f00105417.png
[IMG-072]: https://abc-bauconsulting.de/wp-content/uploads/2022/08/20160912_134023-1024x576.jpg
[IMG-073]: https://abc-bauconsulting.de/wp-content/uploads/2022/08/20170711_120217-576x1024.jpg
[IMG-074]: https://abc-bauconsulting.de/wp-content/uploads/2022/08/20190708_140031-1024x576.jpg
[IMG-075]: https://abc-bauconsulting.de/wp-content/uploads/2022/08/20190708_140833-1024x576.jpg
[IMG-076]: https://abc-bauconsulting.de/wp-content/uploads/2022/08/20200526_132041-1024x576.jpg
[IMG-077]: https://abc-bauconsulting.de/wp-content/uploads/2022/08/20200625_134809-1024x576.jpg
[IMG-078]: https://abc-bauconsulting.de/wp-content/uploads/2022/08/20210617_104541-1024x576.jpg
[IMG-079]: https://abc-bauconsulting.de/wp-content/uploads/2022/08/20210617_110237-1024x576.jpg
[IMG-080]: https://abc-bauconsulting.de/wp-content/uploads/2022/08/20210617_112506-1024x576.jpg
[IMG-081]: https://abc-bauconsulting.de/wp-content/uploads/2024/02/20211122_155153-1024x768.jpg
[IMG-082]: https://abc-bauconsulting.de/wp-content/uploads/2024/02/20211122_155355-1024x768.jpg
[IMG-083]: https://abc-bauconsulting.de/wp-content/uploads/2024/02/20230329_110311-1024x768.jpg
[IMG-084]: https://abc-bauconsulting.de/impressum/fileadmin/user_upload/8c7ec5e7d4.jpg

## 7. Existing irregularities and migration cautions

| Existing condition | Where / implication |
|---|---|
| Broken homepage link | Datenschutz's `../index.html` resolves to `/index.html`, which returns 404; the real homepage is `/` |
| Broken privacy link | Datenschutz's `../datenschutz.html` resolves to `/datenschutz.html`, which returns 404; the real privacy route is `/datenschutz/` |
| Broken image | Impressum references `fileadmin/user_upload/8c7ec5e7d4.jpg`, resolving to `/impressum/fileadmin/user_upload/8c7ec5e7d4.jpg`, HTTP 404; do not fabricate replacement artwork |
| Trailing encoded space in email CTA | Kontakt uses `mailto:info@abc-bauconsulting.de%20`; preserve in the audit, normalize intentionally when implementing |
| HTTP image source attributes | Many content images use `http://` `src` with HTTPS `srcset`; the verified assets are available over HTTPS |
| Empty landing pages | Über Uns, Seminare & Schulungen, Adjudikation: shared shell only; absence of body copy is real |
| Empty blog | Sitemap-only `/blog/` has no published posts in the rendered page, no contact sidebar and no body text |
| Published placeholders | `/referenz-template/` and `/sample-page/` are sitemap-only and fully recorded, but should not automatically be promoted into the rebuilt primary menu |
| Two different Gutachten pages | `/gutachten/` describes the service; `/gutachten-2/` is the reference-category index. Titles match but content and hero assignments differ |
| Irregular reference navigation | The MPI/Hirnforschung detail's “Nächste” returns to `/gutachten-2/`, despite two further entries in that category list; the exact existing graph is preserved below |
| Incomplete project fields | BAB A2/BW 683 leaves “Auftragssumme:” and “Ergebnis angemess. Entschädigungsanspruch:” without figures. Do not invent values |
| Stale seminar announcement | Aktuelles still says “Seminare ab Frühjahr 2023”; no newer notice was substituted |
| Old privacy-policy date and feature claims | Privacy text says “Stand Mai 2018” and refers to Maps/Facebook/Webfonts. Content review is needed before reuse, not an automatic technical implementation of those claims |
| Empty previous/next targets | Referenz-Template has empty `href` attributes on its pill links. These are placeholders, not missing discovered projects |
| Original spelling/formatting | Includes “Bauablaufstörungendurch”, “Westfpfalz”, inconsistent spacing and abbreviations. These are transcribed, not silently corrected |
| Existing accessibility issues | Empty image alt text, repeated H1s, English submenu control labels and low-contrast utility telephone text should be improved deliberately |
| Rights and attribution | Project photos, logos, maps/plans/screenshots, legal copy and sample content require appropriate rights/approval before republication; inventory is not a license grant |

No PDF, downloadable document, video, audio or embedded iframe was discovered in the recursively linked authored-page content. External links such as Google Maps, OpenStreetMap, IHK, DGA-Bau, privacy references and the agency/theme credits are recorded, but their external websites are outside the crawl scope. WordPress RSS, REST/oEmbed, login/admin routes, arbitrary search queries and asset files are technical endpoints, not additional authored subpages. The sitemap checks found no further published page URLs beyond the 54 in section 4.

## 8. Markdown-oriented static rebuild guidance

This is guidance for the subsequent rebuild, distinct from the existing-site observations above. No static-site implementation or content rewrite is included in this task.

Keep one readable Markdown file per existing page and retain the original route explicitly. Store shared identity, navigation, contact details and footer once rather than copying them into 54 files. Give images stable identifiers mapped to local asset paths; preserve the correspondence with this register during migration. The renderer should supply the hero and shared shell, while Markdown supplies body headings, paragraphs, lists, tables, images and links in the recorded order.

A minimal page's front matter could be:

```yaml
---
title: "Leistungen für Auftragnehmer"
permalink: "/leistungen-fuer-auftragnehmer/"
layout: "page"
hero: "<image ID from section 4>"
sidebar: true
---
```

A reference can use the same Markdown-capable layout with its facts expressed as a readable two-column Markdown table and explicit `previous`, `next` and `all_references` routes in front matter. Do not infer adjacency from alphabetical filenames: use the actual links recorded for each page. Preserve nested lists and manually emphasized figures. Empty bodies must remain expressible without placeholder text.

Retain German Unicode characters and UTF-8. Download the required images, use HTTPS only during acquisition, and serve them locally in the static build. Responsive variants can be regenerated from verified source assets, but preserve their aspect ratios and do not distort portrait photos or diagrams. Replace WordPress search intentionally with a static index/client-side search if search remains part of the rebuilt interface. Do not copy WordPress/admin URLs, dependency bundles or server-side form behavior into a static site merely because they occur in old markup.

Before publishing the rebuild, reconcile the page catalog, every image reference, project-table figures, link destinations and mobile/desktop layouts against this document. Broken legacy links, stale legal text, placeholder pages and accessibility improvements need explicit treatment rather than accidental omission.
