document.addEventListener("DOMContentLoaded", () => {
  const selector = "div.dropdown.full-width-dropdown";

  const observer = new MutationObserver((mutations) => {
    for (const m of mutations) {
      const el = m.target;
      const wasHidden = (m.oldValue || "").split(/\s+/).includes("toggle-hidden");
      const isHidden = el.classList.contains("toggle-hidden");
      if (wasHidden && !isHidden) {
        el.classList.add("full-width");
      } else if (!wasHidden && isHidden) {
        el.classList.remove("full-width");
      }
    }
  });

  document.querySelectorAll(selector).forEach((el) => {
    el.classList.toggle("full-width", !el.classList.contains("toggle-hidden"));
    observer.observe(el, { attributes: true, attributeFilter: ["class"], attributeOldValue: true });
  });
});
