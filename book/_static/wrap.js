// wrap each admonition inside another admonition inside a div.wrap-admonition to add a background to the admonition
// without affecting the border radius and margin of the original admonition
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("div.admonition div.admonition")
    .forEach(admonition => {
      // wrap the admonition in a div with class "wrap-admonition"
      const wrap = document.createElement("div");
      wrap.classList.add("wrap-admonition");
      // add the border radius to the wrap based on the admonition style
      const style = window.getComputedStyle(admonition);
      wrap.style.borderRadius = style.borderRadius;
      // add margin to the wrap based on the admonition margin
      wrap.style.margin = style.margin;
      // move the admonition inside the wrap 
      admonition.parentNode.insertBefore(wrap, admonition);
      wrap.appendChild(admonition);
      
    });
});