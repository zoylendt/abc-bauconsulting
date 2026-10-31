(() => {
  const error = document.querySelector("#search-error");
  if (!window.PagefindUI) {
    error.hidden = false;
    return;
  }
  const bundle = new URL("./", document.querySelector('script[src$="/pagefind/pagefind-ui.js"]').src);
  const search = new window.PagefindUI({
    element: "#search-results",
    bundlePath: bundle.pathname,
    baseUrl: new URL("../", bundle).pathname,
    showSubResults: true,
    showImages: false,
    resetStyles: false,
    translations: {
      placeholder: "Website durchsuchen",
      clear_search: "Löschen",
      load_more: "Weitere Ergebnisse laden",
      search_label: "Website durchsuchen",
      searching: "Suche nach [SEARCH_TERM] …",
      zero_results: "Keine Ergebnisse für [SEARCH_TERM]",
      one_result: "[COUNT] Ergebnis für [SEARCH_TERM]",
      many_results: "[COUNT] Ergebnisse für [SEARCH_TERM]",
      alt_search: "Keine Ergebnisse für [SEARCH_TERM]. Stattdessen Ergebnisse für [DIFFERENT_TERM]:",
      search_suggestion: "Keine Ergebnisse für [SEARCH_TERM]. Versuchen Sie einen der folgenden Begriffe:",
    },
  });
  const input = document.querySelector(".pagefind-ui__search-input");
  input.addEventListener("input", () => {
    const url = new URL(location.href);
    const value = input.value.trim();
    if (value) url.searchParams.set("q", value);
    else url.searchParams.delete("q");
    history.replaceState(null, "", url);
  });
  const query = new URLSearchParams(location.search).get("q") || "";
  if (query) search.triggerSearch(query);
})();
