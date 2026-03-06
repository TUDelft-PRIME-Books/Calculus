// Functionality for multiple-choice single-select questions in Teachbooks
document.addEventListener('click', function(event) {
  // Find the closest div with both sd-card and option classes
  const optionDiv = event.target.closest('div.sd-card.option');

  // Check if it is a multiple-choice single-select questions
  // Get the parent div with class admonition and class question
  const questionDiv = optionDiv.closest('div.admonition.question');
  if (!questionDiv) {
    return; // not a question, do nothing
  }
  if (!questionDiv.classList.contains('multiple-choice')) {
    return; // not a multiple-choice question, do nothing
  }
  if (!questionDiv.classList.contains('single-select')) {
    return; // not a single-select question, do nothing
  }

  if (optionDiv) {
    // if already selected, unselect it and return
    if (optionDiv.querySelector('div.sd-card-body.selected')) {
      optionDiv.querySelector('div.sd-card-body').classList.remove('selected');
      optionDiv.querySelector('div.sd-card-footer').classList.remove('correct');
      optionDiv.querySelector('div.sd-card-footer').classList.remove('incorrect');
      return;
    }

    // find the parent section with class question-options
    const questionSection = optionDiv.closest('section.question-options');
    if (questionSection) {
      // if anything is selected, deselect it
      // so all div.sd-card-body with "selected" class should have it removed
      const selectedOptions = questionSection.querySelectorAll('div.sd-card-body.selected');
      selectedOptions.forEach(function(selectedOption) {
        selectedOption.classList.remove('selected');
      });
      // and for all div.sd-card-footer with "correct" or "incorrect" class should have it removed
      const feedbackOptions = questionSection.querySelectorAll('div.sd-card-footer.correct, div.sd-card-footer.incorrect');
      feedbackOptions.forEach(function(feedbackOption) {
        feedbackOption.classList.remove('correct');
        feedbackOption.classList.remove('incorrect');
      });
    }
    // Now find the div.sd-card-body inside the clicked option and add "selected" class to it
    const optionBody = optionDiv.querySelector('div.sd-card-body');
    if (optionBody) {
      optionBody.classList.add('selected');
    }
    // find the div.sd-card-footer inside the clicked option and add "correct" or "incorrect" class to it based on the class of child section
    const optionFooter = optionDiv.querySelector('div.sd-card-footer');
    if (optionFooter) {
      // get the section with class question-options that contains this option
      optionFooterSection = optionFooter.querySelector('section.question-feedback');
      if (optionFooterSection) {
        const isCorrect = optionFooterSection.classList.contains('correct');
        if (isCorrect) {
          optionFooter.classList.add('correct');
        } else {
          optionFooter.classList.add('incorrect');
        }
      }
    }
  }
});
