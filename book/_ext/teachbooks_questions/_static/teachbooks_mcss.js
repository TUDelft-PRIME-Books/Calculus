// Functionality for multiple-choice single-select questions in Teachbooks.
(function () {
  function getQuestionDiv(element) {
    return element.closest('div.multiple-choice.single-select');
  }

  function getQuestionOptionsSection(questionDiv) {
    return document.querySelector(`section.question-options#${questionDiv.id}-options`);
  }

  function clearAllOptions(questionSection) {
    questionSection.querySelectorAll('div.sd-card.option').forEach(function (optionCard) {
      const body = optionCard.querySelector('div.sd-card-body');
      const footer = optionCard.querySelector('div.sd-card-footer');
      if (body) {
        body.classList.remove('selected', 'correct', 'incorrect');
      }
      if (footer) {
        footer.classList.remove('correct', 'incorrect');
      }
    });
  }

  function markOptionWithFeedback(optionCard) {
    const body = optionCard.querySelector('div.sd-card-body');
    const footer = optionCard.querySelector('div.sd-card-footer');

    if (!body || !footer) {
      return;
    }

    body.classList.add('selected');

    const feedbackSection = footer.querySelector('section.question-feedback');
    const isCorrect = !!feedbackSection && feedbackSection.classList.contains('correct');

    if (isCorrect) {
      footer.classList.add('correct');
    } else {
      footer.classList.add('incorrect');
    }
  }

  function handleOptionClick(optionCard) {
    const questionDiv = getQuestionDiv(optionCard);
    if (!questionDiv) {
      return;
    }

    const body = optionCard.querySelector('div.sd-card-body');
    const footer = optionCard.querySelector('div.sd-card-footer');

    if (body && body.classList.contains('selected')) {
      // Toggle unselect
      body.classList.remove('selected', 'correct', 'incorrect');
      if (footer) {
        footer.classList.remove('correct', 'incorrect');
      }
      return;
    }

    const questionSection = optionCard.closest('section.question-options');
    if (questionSection) {
      clearAllOptions(questionSection);
    }

    markOptionWithFeedback(optionCard);
  }

  function handleResetClick(resetButton) {
    const questionDiv = getQuestionDiv(resetButton);
    if (!questionDiv) {
      return;
    }

    const questionOptionsSection = getQuestionOptionsSection(questionDiv);
    if (questionOptionsSection) {
      clearAllOptions(questionOptionsSection);
    }
  }

  function handleShowClick(showButton) {
    const questionDiv = getQuestionDiv(showButton);
    if (!questionDiv) {
      return;
    }

    const questionOptionsSection = getQuestionOptionsSection(questionDiv);
    if (!questionOptionsSection) {
      return;
    }

    questionOptionsSection.querySelectorAll('div.sd-card.option').forEach(function (optionCard) {
      const footer = optionCard.querySelector('div.sd-card-footer');
      const body = optionCard.querySelector('div.sd-card-body');

      if (!footer || !body) {
        return;
      }

      const feedbackSection = footer.querySelector('section.question-feedback');
      const isCorrect = !!feedbackSection && feedbackSection.classList.contains('correct');

      footer.classList.remove('correct', 'incorrect');
      body.classList.remove('selected', 'correct', 'incorrect');
      footer.classList.add(isCorrect ? 'correct' : 'incorrect');
      body.classList.add(isCorrect ? 'correct' : 'incorrect');
    });
  }

  document.addEventListener('click', function (event) {
    const optionCard = event.target.closest('div.sd-card.option');
    if (optionCard) {
      handleOptionClick(optionCard);
      return;
    }

    const resetButton = event.target.closest('div.sd-card.reset-button');
    if (resetButton) {
      handleResetClick(resetButton);
      return;
    }

    const showButton = event.target.closest('div.sd-card.show-button');
    if (showButton) {
      handleShowClick(showButton);
    }
  });
})();