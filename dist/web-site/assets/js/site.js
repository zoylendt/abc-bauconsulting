(() => {
  const searchForms = document.querySelectorAll(".search-form");
  const legacyQuery = new URLSearchParams(location.search).get("s");
  if (legacyQuery !== null && !document.querySelector("#search-results")) {
    const target = new URL(searchForms[0].action);
    target.searchParams.set("q", legacyQuery);
    location.replace(target.href);
    return;
  }
  if (location.protocol === "file:") {
    searchForms.forEach((form) => form.addEventListener("submit", (event) => {
      event.preventDefault();
      const target = new URL(form.action);
      target.search = new URLSearchParams(new FormData(form)).toString();
      location.assign(target.href);
    }));
  }

  const header = document.querySelector(".navbar");
  const menuToggle = document.querySelector(".menu-toggle");
  const searchToggle = document.querySelector(".search-toggle");
  const searchItem = document.querySelector(".menu-search");
  const mobile = matchMedia("(max-width: 768px)");
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
  const hero = document.querySelector(".page-hero");
  const heroImage = document.querySelector(".hero-image");
  const backToTop = document.querySelector(".back-to-top");

  function setSubmenu(item, open) {
    item.classList.toggle("is-open", open);
    item.querySelector(".submenu-toggle").setAttribute("aria-expanded", String(open));
  }

  function closeSubmenus(except) {
    document.querySelectorAll(".has-submenu.is-open").forEach((item) => {
      if (item === except) return;
      setSubmenu(item, false);
    });
  }

  function setMenu(open) {
    header.classList.toggle("is-open", open);
    document.body.classList.toggle("menu-open", open);
    menuToggle.setAttribute("aria-expanded", String(open));
    menuToggle.querySelector(".sr-only").textContent = open ? "Menü schließen" : "Menü öffnen";
    if (!open) closeSubmenus();
  }

  function setSearch(open) {
    searchItem.classList.toggle("is-open", open);
    searchToggle.setAttribute("aria-expanded", String(open));
    if (open) document.querySelector("#header-search-input").focus();
  }

  menuToggle.addEventListener("click", () => setMenu(!header.classList.contains("is-open")));
  searchToggle.addEventListener("click", () => setSearch(!searchItem.classList.contains("is-open")));
  document.querySelectorAll(".submenu-toggle").forEach((button) => {
    button.addEventListener("click", () => {
      const item = button.closest(".has-submenu");
      const open = !item.classList.contains("is-open");
      closeSubmenus(item);
      setSubmenu(item, open);
    });
  });
  document.querySelectorAll(".has-submenu").forEach((item) => {
    item.addEventListener("pointerenter", (event) => {
      if (mobile.matches || event.pointerType !== "mouse") return;
      closeSubmenus(item);
      setSubmenu(item, true);
    });
    item.addEventListener("pointerleave", () => {
      if (!mobile.matches && !item.contains(document.activeElement)) setSubmenu(item, false);
    });
    item.addEventListener("focusin", (event) => {
      if (!mobile.matches && event.target.matches(":focus-visible")) {
        closeSubmenus(item);
        setSubmenu(item, true);
      }
    });
    item.addEventListener("focusout", (event) => {
      if (!mobile.matches && !item.contains(event.relatedTarget)) setSubmenu(item, false);
    });
  });
  document.addEventListener("click", (event) => {
    if (!header.contains(event.target)) {
      setMenu(false);
      setSearch(false);
      closeSubmenus();
    }
  });
  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    if (searchItem.classList.contains("is-open")) {
      setSearch(false);
      searchToggle.focus();
    } else if (header.classList.contains("is-open")) {
      setMenu(false);
      menuToggle.focus();
    } else {
      const item = document.activeElement?.closest(".has-submenu");
      if (item) item.querySelector(".menu-link-row > a").focus();
      closeSubmenus();
    }
  });

  function updateScroll() {
    header.classList.toggle("is-scrolled", scrollY > 40);
    backToTop.classList.toggle("is-visible", scrollY > hero.offsetHeight);
    const shift = !mobile.matches && !reducedMotion.matches ? Math.min(scrollY, hero.offsetHeight) / 3 : 0;
    heroImage.style.transform = `translateY(${shift}px)`;
  }

  function measureHeader() {
    const compact = header.classList.contains("is-scrolled");
    header.classList.remove("is-scrolled");
    document.documentElement.style.setProperty("--navbar-height", `${header.offsetHeight}px`);
    header.classList.toggle("is-scrolled", compact);
    if (!mobile.matches) setMenu(false);
    updateScroll();
  }

  let scrollPending = false;
  addEventListener("scroll", () => {
    if (scrollPending) return;
    scrollPending = true;
    requestAnimationFrame(() => {
      updateScroll();
      scrollPending = false;
    });
  }, { passive: true });
  addEventListener("resize", measureHeader);
  reducedMotion.addEventListener("change", updateScroll);
  measureHeader();
})();
