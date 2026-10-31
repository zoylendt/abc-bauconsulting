import assert from "node:assert/strict";
import { existsSync, readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

const root = fileURLToPath(new URL("../", import.meta.url));
const output = path.join(root, "_site");
const read = (file) => readFileSync(file, "utf8");
const files = (directory, suffix) => readdirSync(directory, { recursive: true })
  .filter((name) => name.endsWith(suffix)).map((name) => path.join(directory, name));
const contentDirectory = path.join(root, "src/content");
const pages = files(contentDirectory, ".md");
const field = (source, name) => {
  const raw = source.split("\n---\n")[0].match(new RegExp(`^${name}:\\s*(.+)$`, "m"))?.[1];
  if (!raw) return undefined;
  return raw.startsWith('"') ? JSON.parse(raw) : raw;
};
const pageFile = (url) => path.join(output, url.endsWith("/") ? `${url}index.html` : url);
const escape = (text) => text.replaceAll("&", "&amp;").replaceAll('"', "&quot;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");

test("content is grouped into categories with shared collection defaults", () => {
  for (const category of ["Startseite", "Leistungsspektrum", "Über uns", "Referenzen", "Seminare", "Kontakt", "Impressum"]) {
    assert.ok(existsSync(path.join(contentDirectory, category)), `Missing content category: ${category}`);
  }
  for (const name of ["blog.md", "sample-page.md", "referenz-template.md"]) {
    assert.ok(existsSync(path.join(contentDirectory, name)), `Uncategorized page must live at the content root: ${name}`);
  }
  const defaults = JSON.parse(read(path.join(contentDirectory, "content.json")));
  assert.ok(defaults.tags.includes("sitePage"), "All content must inherit the sitePage collection tag");
});

test("reference overviews and projects live in their matching category folders", () => {
  const directory = path.join(contentDirectory, "Referenzen");
  const navigation = JSON.parse(read(path.join(root, "src/_data/navigation.json")));
  const categories = navigation.find((item) => item.url === "/referenzen/").children;
  assert.ok(existsSync(path.join(directory, "referenzen.md")), "The reference overview must remain at the reference root");
  for (const category of categories) {
    const categoryDirectory = path.join(directory, category.title);
    assert.ok(existsSync(categoryDirectory), `Missing reference category: ${category.title}`);
    assert.ok(files(categoryDirectory, ".md").some((file) => field(read(file), "permalink") === category.url),
      `Missing category overview in ${category.title}`);
  }
  for (const file of files(directory, ".md")) {
    const source = read(file);
    const category = categories.find((item) =>
      item.url === field(source, "permalink") || item.url === field(source, "navigationParent"));
    if (category) {
      assert.equal(path.dirname(file), path.join(directory, category.title), `Reference is in the wrong category: ${file}`);
    }
  }
});

test("the documented pages retain their routes, titles and shared shell", () => {
  assert.ok(pages.length >= 54, "All 54 inventoried pages must be retained");
  const seen = new Set();
  for (const file of pages) {
    const source = read(file);
    const route = field(source, "permalink");
    assert.ok(route?.startsWith("/"), `${file}: missing root-relative permalink`);
    assert.ok(!seen.has(route), `Duplicate route: ${route}`);
    seen.add(route);
    assert.ok(existsSync(pageFile(route)), `Missing built route: ${route}`);
    const html = read(pageFile(route));
    const title = field(source, "documentTitle") || `${field(source, "title")} – ABC Abel Bau-Consulting`;
    assert.ok(html.includes(`<title>${escape(title)}</title>`), `${route}: document title changed`);
    assert.equal((html.match(/<h1(?:\s|>)/g) || []).length, 1, `${route}: expected exactly one H1`);
    assert.match(html, /id="primary-navigation"/);
    assert.match(html, /id="content"/);
    assert.match(html, /class="site-footer"/);
    assert.doesNotMatch(html, /src="https?:\/\/abc-bauconsulting\.de\/wp-content/);
    assert.doesNotMatch(html, /!\[IMG-\d+\]/, `${route}: unresolved Markdown image`);
  }
});

test("every local link, image and script in the built pages resolves", () => {
  for (const file of files(output, ".html")) {
    const route = "/" + path.relative(output, file).split(path.sep).join("/");
    for (const match of read(file).matchAll(/\b(?:href|src)="([^"]*)"/g)) {
      const value = match[1].replaceAll("&amp;", "&");
      assert.notEqual(value, "", `${route}: empty link or asset URL`);
      if (/^(?:https?:|mailto:|tel:|data:|#)/.test(value)) continue;
      const target = new URL(value, `https://preview.invalid${route}`);
      const pathname = decodeURIComponent(target.pathname);
      assert.ok(existsSync(pageFile(pathname)), `${route}: missing local target ${value}`);
    }
  }
});

test("all registered placeholders have positive dimensions, local files and replacement instructions", () => {
  const images = JSON.parse(read(path.join(root, "src/_data/images.json")));
  const guide = read(path.join(root, "src/assets/images/REPLACEMENTS.md"));
  assert.ok(!existsSync(pageFile("/assets/images/REPLACEMENTS/")), "Editorial image guide must not become a public page");
  assert.ok(Object.keys(images).length >= 84);
  for (const [id, image] of Object.entries(images)) {
    assert.ok(image.width > 0 && image.height > 0, `${id}: invalid size`);
    assert.ok(image.src.startsWith("/assets/images/"), `${id}: image must be local`);
    assert.ok(existsSync(pageFile(image.src)), `${id}: image missing from build`);
    assert.ok(image.original && guide.includes(image.original), `${id}: missing original path`);
  }
  const imageDirectory = path.join(root, "src/assets/images");
  for (const source of files(imageDirectory, "").filter((file) => /\.(svg|png|jpe?g|webp|avif|gif|ico)$/.test(file))) {
    const relative = path.relative(imageDirectory, source);
    assert.ok(existsSync(path.join(output, "assets/images", relative)), `Image folder structure lost: ${relative}`);
  }
});

test("reference facts remain four-row tables without a dummy header", () => {
  const references = pages.filter((file) => /^referenceNavigation:/m.test(read(file).split("\n---\n")[0]));
  assert.ok(references.length >= 27, "All project pages and the reference template must be checked");
  for (const file of references) {
    const route = field(read(file), "permalink");
    const html = read(pageFile(route));
    assert.doesNotMatch(html, /<thead>/, `${route}: synthetic Markdown header leaked into page`);
    const table = html.match(/<tbody>([\s\S]*?)<\/tbody>/);
    assert.ok(table, `${route}: facts table missing`);
    assert.equal((table[1].match(/<tr>/g) || []).length, 4, `${route}: expected four facts rows`);
  }
});

test("empty pages, samples, search, sitemap and the custom 404 retain their intended behavior", () => {
  for (const route of ["/ueber-uns/", "/adjudikation/", "/seminare-schulungen/"]) {
    assert.match(read(pageFile(route)), /<article[^>]*>\s*<\/article>/);
  }
  assert.doesNotMatch(read(pageFile("/blog/")), /<aside/);
  const sitemap = read(pageFile("/sitemap.xml"));
  for (const route of ["/sample-page/", "/blog/", "/referenz-template/"]) {
    assert.doesNotMatch(sitemap, new RegExp(`<loc>[^<]*${route}</loc>`));
    assert.match(read(pageFile(route)), /name="robots" content="noindex, nofollow"/);
  }
  for (const asset of ["/pagefind/pagefind.js", "/pagefind/pagefind-ui.js", "/pagefind/pagefind-ui.css"]) {
    assert.ok(existsSync(pageFile(asset)), `Missing search asset: ${asset}`);
  }
  assert.match(read(pageFile("/suche/")), /id="search-results"/);
  assert.match(read(pageFile("/404.html")), /Das Gesuchte konnte leider nicht gefunden werden/);
});
