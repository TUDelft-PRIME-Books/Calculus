document.addEventListener('DOMContentLoaded', function() {
  document.addEventListener('click', function(event) {
    const button = event.target.closest('.thebe-run-button, .thebe-runall-button');
    if (button) {
      // Handle click on thebe run buttons
      console.log('Thebe button clicked:', button);
      
      // Check if button has an id, if not generate a random one
      if (!button.id) {
        button.id = 'thebe-button-' + Math.random().toString(36).slice(2, 11);
      }
      
      // Replace the URL anchor with the button id
      window.history.replaceState(null, null, '#' + button.id);
      
      // Scroll the button to the top of the page
      button.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
