(() => {
  const container = document.querySelector("#search-results");
  if (!Array.isArray(window.ABC_LOCAL_SEARCH)) {
    document.querySelector("#search-error").hidden = false;
    return;
  }
  const form = document.createElement("form");
  form.className = "search-form";
  form.setAttribute("role", "search");
  const label = document.createElement("label");
  label.htmlFor = "offline-query";
  label.className = "sr-only";
  label.textContent = "Website durchsuchen";
  const input = document.createElement("input");
  input.id = "offline-query";
  input.type = "search";
  input.placeholder = "Website durchsuchen";
  const button = document.createElement("button");
  button.type = "submit";
  button.textContent = "Suchen";
  const status = document.createElement("p");
  status.setAttribute("role", "status");
  const results = document.createElement("ul");
  results.className = "offline-search-results";
  form.append(label, input, button);
  container.append(form, status, results);

  const normalize = (text) => text.normalize("NFD").replace(/\p{M}/gu, "").toLocaleLowerCase("de").replaceAll("ß", "ss");
  function render() {
    const terms = normalize(input.value).trim().split(/\s+/).filter(Boolean);
    results.replaceChildren();
    if (!terms.length) {
      status.textContent = "Suchbegriff eingeben.";
      return;
    }
    const matches = window.ABC_LOCAL_SEARCH.filter((page) =>
      terms.every((term) => normalize(`${page.title} ${page.text}`).includes(term)));
    status.textContent = `${matches.length} ${matches.length === 1 ? "Ergebnis" : "Ergebnisse"}`;
    for (const page of matches) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = page.url;
      link.textContent = page.title;
      const excerpt = document.createElement("p");
      const position = Math.max(0, normalize(page.text).indexOf(terms[0]) - 60);
      excerpt.textContent = `${position ? "… " : ""}${page.text.slice(position, position + 220)}${page.text.length > position + 220 ? " …" : ""}`;
      item.append(link, excerpt);
      results.append(item);
    }
  }
  form.addEventListener("submit", (event) => { event.preventDefault(); render(); });
  input.addEventListener("input", render);
  input.value = new URLSearchParams(location.search).get("q") || "";
  render();
})();
