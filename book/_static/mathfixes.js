
document.addEventListener("click", (event) => {
  const container = event.target.closest(".toggle, .admonition.dropdown, details");

  if (container) {
    // 1. Locate all the MathJax items currently alive inside this container
    const mathItems = MathJax.startup.document.getMathItemsWithin(container);

    // 2. Loop backwards through items to safely replace rendered HTML with original text
    for (let i = mathItems.length - 1; i >= 0; i--) {
      const item = mathItems[i];
      
      // Get the original wrappers (e.g., $$ or \() and the core formula text
      const openDelimiter = item.start.delim;
      const closeDelimiter = item.end.delim;
      const originalText = item.math; 

      // Reconstruct the unrendered text string
      const rawFormula = `${openDelimiter}\\class{tud-yellow}{${originalText}}${closeDelimiter}`;
      
      // Replace the rendered MathJax element wrapper in the DOM with the raw text
      if (item.typesetRoot && item.typesetRoot.parentNode) {
        item.typesetRoot.outerHTML = rawFormula;
      }
    }

    // 3. Clear MathJax's internal registry for these specific wrappers
  MathJax.typesetClear([container]);
  
  // 4. Hard re-render the raw text exactly like a page reload
  MathJax.typesetPromise([container])
  }
});
