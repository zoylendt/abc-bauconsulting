import { readFileSync, rmSync } from "node:fs";
import MarkdownIt from "markdown-it";

const images = JSON.parse(readFileSync(new URL("./src/_data/images.json", import.meta.url), "utf8"));
const bySource = new Map(Object.values(images).map((image) => [image.src, image]));
const byPlaceholder = new Map(
  Object.entries(images).map(([id, image]) => [`/assets/images/${id.toLowerCase()}.svg`, image]),
);

export default function (eleventyConfig) {
  eleventyConfig.ignores.add("src/assets/images/**/*.md");
  eleventyConfig.on("eleventy.before", ({ runMode }) => {
    if (runMode === "build") rmSync(new URL("./_site", import.meta.url), { recursive: true, force: true });
  });
  const markdown = new MarkdownIt({ html: true, linkify: false, typographer: false });
  const imageParagraph = (token) => token?.type === "inline" &&
    token.children.some((child) => child.type === "image") &&
    !token.children.some((child) => child.type === "text" && child.content.trim());
  markdown.renderer.rules.paragraph_open = (tokens, index) =>
    imageParagraph(tokens[index + 1]) ? '<figure class="content-image">' : "<p>";
  markdown.renderer.rules.paragraph_close = (tokens, index) =>
    imageParagraph(tokens[index - 1]) ? "</figure>\n" : "</p>\n";
  const renderImage = markdown.renderer.rules.image;
  markdown.renderer.rules.image = (tokens, index, options, env, renderer) => {
    const token = tokens[index];
    const source = token.attrGet("src");
    const image = bySource.get(source) || byPlaceholder.get(source);
    if (source.startsWith("/assets/images/") && !image) {
      throw new Error(`Image is not registered in src/_data/images.json: ${source}`);
    }
    if (image) {
      token.attrSet("src", image.src);
      token.attrSet("width", String(image.width));
      token.attrSet("height", String(image.height));
      token.attrSet("loading", "lazy");
      token.attrSet("decoding", "async");
    }
    return renderImage(tokens, index, options, env, renderer);
  };
  markdown.renderer.rules.heading_open = (tokens, index) => {
    const token = tokens[index];
    if (token.tag !== "h1") return `<${token.tag}>`;
    const medium = tokens[index + 1]?.content === "Gestaltung und Umsetzung";
    return `<h2 class="body-title${medium ? " body-title-medium" : ""}">`;
  };
  markdown.renderer.rules.heading_close = (tokens, index) =>
    `</${tokens[index].tag === "h1" ? "h2" : tokens[index].tag}>\n`;
  const renderTableOpen = markdown.renderer.rules.table_open;
  const renderTableClose = markdown.renderer.rules.table_close;
  markdown.renderer.rules.table_open = (...args) =>
    `<div class="table-scroll">${renderTableOpen ? renderTableOpen(...args) : "<table>\n"}`;
  markdown.renderer.rules.table_close = (...args) =>
    `${renderTableClose ? renderTableClose(...args) : "</table>\n"}</div>\n`;
  const render = markdown.render.bind(markdown);
  markdown.render = (...args) => render(...args).replace(/<thead>\s*<tr>(?:\s*<th>\s*<\/th>)+\s*<\/tr>\s*<\/thead>/g, "");
  eleventyConfig.setLibrary("md", markdown);
  eleventyConfig.addFilter("image", (id) => {
    if (!images[id]) throw new Error(`Unknown image ID: ${id}`);
    return images[id];
  });
  eleventyConfig.addFilter("activeMenu", (item, url, parent) =>
    item.url === url || item.url === parent ||
    (item.children || []).some((child) => child.url === url || child.url === parent),
  );
  eleventyConfig.addFilter("json", (value) => JSON.stringify(value));
  eleventyConfig.addPassthroughCopy({ "src/assets/css": "assets/css" });
  eleventyConfig.addPassthroughCopy({ "src/assets/js": "assets/js" });
  eleventyConfig.addPassthroughCopy("src/assets/images/**/*.{svg,png,jpg,jpeg,webp,avif,gif,ico}");
  eleventyConfig.setNunjucksEnvironmentOptions({ autoescape: true });
  return {
    dir: { input: "src", output: "_site", includes: "_includes", data: "_data" },
    templateFormats: ["md", "njk"],
    markdownTemplateEngine: false,
    htmlTemplateEngine: "njk",
  };
}
