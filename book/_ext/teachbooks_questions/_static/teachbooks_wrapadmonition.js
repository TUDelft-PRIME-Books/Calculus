document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("section.question-options div.admonition")
    .forEach(admonition => {
      // wrap the admonition in a div with class "wrap-admonition"
      const wrap = document.createElement("div");
      wrap.classList.add("wrap-admonition");
      admonition.parentNode.insertBefore(wrap, admonition);
      wrap.appendChild(admonition);
    });
});