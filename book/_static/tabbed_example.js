document.addEventListener("DOMContentLoaded", () => {

  document.querySelectorAll(".admonition.dual").forEach(admonition => {
    const header = admonition.querySelector("p.admonition-title");
    const textEl = admonition.querySelector('.example-text');
    const animEl = admonition.querySelector('.example-animation');

    if (!header) return;

    // Avoid inserting multiple buttons
    if (header.querySelector(".dual-btn")) return;

    const btn = document.createElement("button");
    btn.className = "dual-btn";
    
    // Create a temporary element to measure the width of bold "Animated"
    const tempSpan = document.createElement("span");
    tempSpan.innerHTML = "<strong>Animated</strong>";
    tempSpan.style.visibility = "hidden";
    tempSpan.style.position = "absolute";
    tempSpan.style.whiteSpace = "nowrap";
    document.body.appendChild(tempSpan);
    const animatedWidth = Math.ceil(tempSpan.offsetWidth) + 5; // Add 5px padding
    document.body.removeChild(tempSpan);
    
    // Also measure "Textual" for consistency
    const tempSpan2 = document.createElement("span");
    tempSpan2.innerHTML = "<strong>Textual</strong>";
    tempSpan2.style.visibility = "hidden";
    tempSpan2.style.position = "absolute";
    tempSpan2.style.whiteSpace = "nowrap";
    document.body.appendChild(tempSpan2);
    const textualWidth = Math.ceil(tempSpan2.offsetWidth) + 5; // Add 5px padding
    document.body.removeChild(tempSpan2);
    
    btn.innerHTML = `<span class="active" style="display:inline-block;width:${textualWidth}px;text-align:right;"><strong>Textual</strong></span>&nbsp;<i class="fa-solid fa-toggle-off fa-lg"></i>&nbsp;<span style="display:inline-block;width:${animatedWidth}px;text-align:left;">Animated</span>`;
    btn.onclick = function () {
      if (admonition.classList.contains("animated")) {
        admonition.classList.remove("animated");
        btn.innerHTML = `<span class="active" style="display:inline-block;width:${textualWidth}px;text-align:right;"><strong>Textual</strong></span>&nbsp;<i class="fa-solid fa-toggle-off fa-lg"></i>&nbsp;<span style="display:inline-block;width:${animatedWidth}px;text-align:left;">Animated</span>`;
        textEl.style.display = "block";
        animEl.style.display = "none";
      } else {
        btn.innerHTML = `<span style="display:inline-block;width:${textualWidth}px;text-align:right;">Textual</span>&nbsp;<i class="fa-solid fa-toggle-off fa-flip-horizontal fa-lg"></i>&nbsp;<span class="active" style="display:inline-block;width:${animatedWidth}px;text-align:left;"><strong>Animated</strong></span>`;
        admonition.classList.add("animated");
        textEl.style.display = "none";
        animEl.style.display = "block";
      }
    };

    // Style the button into the title bar
    header.style.position = "relative";
    btn.style.position = "absolute";
    btn.style.right = "0.5em";
    btn.style.top = "0.2em";

    header.appendChild(btn);
  });
});
