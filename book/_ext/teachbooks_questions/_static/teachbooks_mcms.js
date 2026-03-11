// Functionality for multiple-choice multiple-select questions in Teachbooks.
(function () {
  function getQuestionDiv(element) {
    return element.closest('div.multiple-choice.multiple-select');
  }

  function getQuestionOptionsSection(questionDiv) {
    return document.querySelector(`section.question-options#${questionDiv.id}-options`);
  }

  function getOverallFeedbackSection(questionDiv) {
    return document.querySelector(`section.question-feedback.overall-feedback#${questionDiv.id}-overall-feedback`);
  }

  function clearOverallFeedback(questionDiv) {
    const overallFeedbackSection = getOverallFeedbackSection(questionDiv);
    if (!overallFeedbackSection) {
      return;
    }

    overallFeedbackSection.querySelectorAll('div.sd-card').forEach(function (feedbackCard) {
      feedbackCard.classList.remove('show');
    });
  }

  function clearOptionFeedback(questionSection) {
    questionSection
      .querySelectorAll('div.sd-card-footer.correct, div.sd-card-footer.incorrect')
      .forEach(function (feedbackOption) {
        feedbackOption.classList.remove('correct', 'incorrect');
      });

    questionSection
      .querySelectorAll('div.sd-card-body.correct, div.sd-card-body.incorrect')
      .forEach(function (bodyOption) {
        bodyOption.classList.remove('correct', 'incorrect');
      });
  }

  function handleOptionClick(optionCard) {
    const questionDiv = getQuestionDiv(optionCard);
    if (!questionDiv) {
      return;
    }

    const questionSection = optionCard.closest('section.question-options');
    if (questionSection) {
      clearOptionFeedback(questionSection);
    }
    clearOverallFeedback(questionDiv);

    const optionBody = optionCard.querySelector('div.sd-card-body');
    if (!optionBody) {
      return;
    }

    optionBody.classList.toggle('selected');
  }

  function handleResetClick(resetButton) {
    const questionDiv = getQuestionDiv(resetButton);
    if (!questionDiv) {
      return;
    }

    const questionOptionsSection = getQuestionOptionsSection(questionDiv);
    if (questionOptionsSection) {
      questionOptionsSection.querySelectorAll('div.sd-card.option').forEach(function (optionCard) {
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

    clearOverallFeedback(questionDiv);
  }

  function handleSubmitClick(submitButton) {
    const questionDiv = getQuestionDiv(submitButton);
    if (!questionDiv) {
      return;
    }

    const questionOptionsSection = getQuestionOptionsSection(questionDiv);
    if (!questionOptionsSection) {
      return;
    }

    const optionCards = questionOptionsSection.querySelectorAll('div.sd-card.option');
    let numberOfCorrectSelected = 0;
    let numberOfIncorrectSelected = 0;
    let numberOfCorrect = 0;

    // Single pass: clear classes, count correct, and mark feedback
    optionCards.forEach(function (optionCard) {
      const body = optionCard.querySelector('div.sd-card-body');
      const footer = optionCard.querySelector('div.sd-card-footer');
      const feedbackSection = footer ? footer.querySelector('section.question-feedback') : null;
      const isCorrect = !!feedbackSection && feedbackSection.classList.contains('correct');

      if (body) {
        body.classList.remove('correct', 'incorrect');
      }

      if (isCorrect) {
        numberOfCorrect += 1;
        if (body && body.classList.contains('selected')) {
          numberOfCorrectSelected += 1;
          if (footer) {
            footer.classList.add('correct');
          }
        }
      } else if (body && body.classList.contains('selected')) {
        numberOfIncorrectSelected += 1;
        if (footer) {
          footer.classList.add('incorrect');
        }
      }
    });

    const classesToShow = [];
    if (numberOfCorrectSelected === numberOfCorrect && numberOfIncorrectSelected === 0) {
      classesToShow.push('correct');
    } else {
      if (numberOfCorrect > numberOfCorrectSelected) {
        classesToShow.push('missed');
      }
      if (numberOfIncorrectSelected > 0) {
        classesToShow.push('incorrect');
      }
    }

    const overallFeedbackSection = getOverallFeedbackSection(questionDiv);
    if (!overallFeedbackSection) {
      return;
    }

    overallFeedbackSection.querySelectorAll('div.sd-card').forEach(function (feedbackCard) {
      const shouldShow = classesToShow.some(function (className) {
        return feedbackCard.classList.contains(className);
      });
      feedbackCard.classList.toggle('show', shouldShow);
    });
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

    clearOverallFeedback(questionDiv);
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

    const submitButton = event.target.closest('div.sd-card.submit-button');
    if (submitButton) {
      handleSubmitClick(submitButton);
      return;
    }

    const showButton = event.target.closest('div.sd-card.show-button');
    if (showButton) {
      handleShowClick(showButton);
    }
  });
})();