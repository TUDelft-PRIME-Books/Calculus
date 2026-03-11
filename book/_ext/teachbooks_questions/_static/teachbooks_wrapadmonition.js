document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("section.question-options div.admonition")
    .forEach(admonition => {
      // wrap the admonition in a div with class "wrap-admonition"
      const wrap = document.createElement("div");
      wrap.classList.add("wrap-admonition");
      // add the border radius to the wrap based on the admonition style
      const style = window.getComputedStyle(admonition);
      wrap.style.borderRadius = style.borderRadius;
      // move the admonition inside the wrap 
      admonition.parentNode.insertBefore(wrap, admonition);
      wrap.appendChild(admonition);
      
    });
});