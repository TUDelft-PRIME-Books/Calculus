// Functionality for multiple-choice multiple-select questions in Teachbooks
document.addEventListener('click', function(event) {
  // Find the closest div with both sd-card and option classes
  const optionDiv = event.target.closest('div.sd-card.option');

  if (optionDiv) {
    // Check if it is a multiple-choice multiple-select questions
    // Get the parent div with class admonition and class question
    const questionDiv = optionDiv.closest('div.multiple-choice.multiple-select');
    if (!questionDiv) {
      return; // not a question, do nothing
    }
  
    // if already selected, unselect it and return
    if (optionDiv.querySelector('div.sd-card-body.selected')) {
      optionDiv.querySelector('div.sd-card-body').classList.remove('selected');
      // if the feedback is already shown, we still remove it
      optionDiv.querySelector('div.sd-card-footer').classList.remove('correct');
      optionDiv.querySelector('div.sd-card-footer').classList.remove('incorrect');
      return;
    }

    // Now find the div.sd-card-body inside the clicked option and add "selected" class to it
    const optionBody = optionDiv.querySelector('div.sd-card-body');
    if (optionBody) {
      optionBody.classList.add('selected');
    }
  }

  // if the click is outside of any option, maybe it was the reset button, so we check if it was the reset button and if so, we reset all options in the question
  const resetButton = event.target.closest('div.sd-card.reset-button');
  if (resetButton) {
    // Check if it is a multiple-choice multiple-select questions
    // Get the parent div with class admonition and class question
    const questionDiv = resetButton.closest('div.multiple-choice.multiple-select');
    if (!questionDiv) {
      return; // not a question, do nothing
    }
    // extract the id
    const questionId = questionDiv.id
    const questionOptionsSection = document.querySelector(`section.question-options#${questionId}-options`);
    if (questionOptionsSection) {
      // deselect all selected options
      const optionCards = questionOptionsSection.querySelectorAll('div.sd-card.option');
      optionCards.forEach(function(optionCard) {
        optionCard.querySelector('div.sd-card-body').classList.remove('selected');
        optionCard.querySelector('div.sd-card-footer').classList.remove('correct');
        optionCard.querySelector('div.sd-card-footer').classList.remove('incorrect');
      });
    }
    // also reset the overall feedback
    const overallFeedbackSection = document.querySelector(`section.question-feedback.overall-feedback#${questionId}-overall-feedback`);
    if (overallFeedbackSection) {
        const feedbackCards = overallFeedbackSection.querySelectorAll('div.sd-card');
        feedbackCards.forEach(function(feedbackCard) {
            feedbackCard.classList.remove('show');
        });
    }
  }

  // it could also be the submit button, so we check if it was the submit button and if so, we show the feedback for all selected options in the question
  const submitButton = event.target.closest('div.sd-card.submit-button');
  if (submitButton) {
    // Check if it is a multiple-choice multiple-select questions
    // Get the parent div with class admonition and class question
    const questionDiv = submitButton.closest('div.multiple-choice.multiple-select');
    if (!questionDiv) {
        return; // not a question, do nothing
    }
    // extract the id
    const questionId = questionDiv.id;
    const questionOptionsSection = document.querySelector(`section.question-options#${questionId}-options`);
    if (questionOptionsSection) {
      // find all selected options
      const selectedOptions = questionOptionsSection.querySelectorAll('div.sd-card.option div.sd-card-body.selected');
      let numberOfCorrectSelected = 0;
      let numberOfIncorrectSelected = 0;
      selectedOptions.forEach(function(selectedOption) {
        // find the parent div with class sd-card option
        const optionCard = selectedOption.closest('div.sd-card.option');
        if (optionCard) {
          // find the div.sd-card-footer inside the option card and add "correct" or "incorrect" class to it based on the class of child section
          const optionFooter = optionCard.querySelector('div.sd-card-footer');
          if (optionFooter) {
            // get the section with class question-options that contains this option
            optionFooterSection = optionFooter.querySelector('section.question-feedback');
            // count the number of correct selected and incorrect selected
            if (optionFooterSection) {
                const isCorrect = optionFooterSection.classList.contains('correct');
                if (isCorrect) {
                optionFooter.classList.add('correct');
                numberOfCorrectSelected += 1;
                } else {
                optionFooter.classList.add('incorrect');
                numberOfIncorrectSelected += 1;
                }
            }
        }
        }
      });
      // find all correct options
      const Footers = questionOptionsSection.querySelectorAll('div.sd-card.option div.sd-card-footer');
      let numberOfCorrect = 0;
      Footers.forEach(function(Footer) {
        optionFooterSection = Footer.querySelector('section.question-feedback');
        // count the number of correct options
        if (optionFooterSection) {
            const isCorrect = optionFooterSection.classList.contains('correct');
            if (isCorrect) {
                numberOfCorrect += 1;
            }
        }
      });
      // Determine which overall feedback to show based on the number of correct selected, incorrect selected, and total correct options
      // classes to select from: correct, incorrect, missed
      let classesToFind = [];
      if (numberOfCorrectSelected === numberOfCorrect && numberOfIncorrectSelected === 0) {
        classesToFind.push("correct");
      } else {
        if (numberOfCorrect > 0 && numberOfCorrect > numberOfCorrectSelected) {
            classesToFind.push("missed");
        }
        if (numberOfIncorrectSelected > 0) {
            classesToFind.push("incorrect");
        }
      }
      // show the overall feedback based on the classToFind
      // Find the relevant section with feedback and the correct ID
      const overallFeedbackSection = document.querySelector(`section.question-feedback.overall-feedback#${questionId}-overall-feedback`);
      if (overallFeedbackSection) {
        // find all feedback cards, add show if it is the correct one, and remove show from the others
        const feedbackCards = overallFeedbackSection.querySelectorAll('div.sd-card');
        feedbackCards.forEach(function(feedbackCard) {
            const shouldShow = classesToFind.some(cls => feedbackCard.classList.contains(cls));
            if (shouldShow) {
                feedbackCard.classList.add('show');
            } else {
                feedbackCard.classList.remove('show');
            }
        });
      }
    }
  }
});