// Functionality for short-answer block questions in Teachbooks

function jaroWinkler(a, b) {
  if (a === b) return 1;

  const m = Math.floor(Math.max(a.length, b.length) / 2) - 1;
  let matches = 0;
  let transpositions = 0;
  const aMatches = [];
  const bMatches = [];

  // matching window
  for (let i = 0; i < a.length; i++) {
    const start = Math.max(0, i - m);
    const end = Math.min(i + m + 1, b.length);
    for (let j = start; j < end; j++) {
      if (!bMatches[j] && a[i] === b[j]) {
        aMatches[i] = bMatches[j] = true;
        matches++;
        break;
      }
    }
  }
  if (!matches) return 0;

  // transpositions
  let k = 0;
  for (let i = 0; i < a.length; i++) {
    if (aMatches[i]) {
      while (!bMatches[k]) k++;
      if (a[i] !== b[k]) transpositions++;
      k++;
    }
  }
  transpositions /= 2;

  const jaro = (
    (matches / a.length) +
    (matches / b.length) +
    ((matches - transpositions) / matches)
  ) / 3;

  // Winkler prefix
  let prefix = 0;
  for (let i = 0; i < Math.min(4, a.length, b.length); i++) {
    if (a[i] === b[i]) prefix++;
    else break;
  }

  return jaro + prefix * 0.05 * (1 - jaro);
}

function tunedSimilarity(student, correct) {
  const s = student.normalize("NFC").trim().toLowerCase();
  const c = correct.normalize("NFC").trim().toLowerCase();

  if (s === c) return 1;

  const base = jaroWinkler(s, c);

  // 1. prefix penalty (detects un-, in-, dis-, non-, mis-, etc.)
  const prefixFlips = ['un', 'in', 'im', 'il', 'ir', 'non', 'dis', 'mis'];
  let prefixPenalty = 0;

  for (let p of prefixFlips) {
    if (correct.startsWith(p) !== student.startsWith(p)) {
      prefixPenalty += 0.08;
    }
  }

  // 2. keyword sensitivity: important words in the correct answer
  const keywords = correct
    .toLowerCase()
    .match(/[a-zA-Z]+/g)
    .filter(w => w.length >= 4);

  let keywordPenalty = 0;
  keywords.forEach(word => {
    if (!student.toLowerCase().includes(word)) {
      keywordPenalty += 0.02;
    }
  });

  // 3. length ratio penalty
  const lenRatio = student.length / correct.length;
  let lengthPenalty = 0;
  if (lenRatio < 0.75 || lenRatio > 1.35) {
    lengthPenalty = 0.05;
  }

  // final combined score
  let score = base - prefixPenalty - keywordPenalty - lengthPenalty;
  score = Math.max(0, Math.min(1, score));

  return score;
}

(function () {
  function getQuestionDiv(element) {
    return element.closest('div.short-answer.blocks');
  }

  function getQuestionOptionsSection(questionDiv) {
    return document.querySelector(`section.question-options#${questionDiv.id}-options`);
  }

  function getAnswerType(textArea) {
    if (textArea.classList.contains('type-T')) return 'T';
    if (textArea.classList.contains('type-TI')) return 'TI';
    if (textArea.classList.contains('type-TF')) return 'TF';
    if (textArea.classList.contains('type-M')) return 'M';
    return null;
  }

  function checkAnswer(studentAnswer, correctAnswer, answerType) {
    const stripped = studentAnswer.trim();

    if (stripped === '') {
      return false;
    }

    if (!answerType || !correctAnswer) {
      return false;
    }

    switch (answerType) {
      case 'T':
        return stripped === correctAnswer;
      case 'TI':
        return stripped.toLowerCase() === correctAnswer.toLowerCase();
      case 'TF':
        return tunedSimilarity(stripped, correctAnswer) >= 0.95;
      case 'M':
        return false;
      default:
        return false;
    }
  }

  function handleResetClick(resetButton) {
    const questionDiv = getQuestionDiv(resetButton);
    if (!questionDiv) {
      return;
    }

    const questionOptionsSection = getQuestionOptionsSection(questionDiv);
    if (questionOptionsSection) {
      questionOptionsSection.querySelectorAll('div.sd-card.option').forEach(function (optionCard) {
        const footer = optionCard.querySelector('div.sd-card-footer');
        const textArea = optionCard.querySelector('textarea.question-option-input');

        if (footer) {
          footer.classList.remove('correct', 'incorrect');
        }
        if (textArea) {
          textArea.value = '';
          textArea.classList.remove('show-answer');
        }
      });
    }
  }

  function handleSubmitClick(submitButton) {
    const questionDiv = getQuestionDiv(submitButton);
    if (!questionDiv) {
      return;
    }

    // Clear any textareas with show-answer class
    document.querySelectorAll('textarea.question-option-input.show-answer').forEach(function (ta) {
      ta.value = '';
      ta.classList.remove('show-answer');
    });

    const questionOptionsSection = getQuestionOptionsSection(questionDiv);
    if (!questionOptionsSection) {
      return;
    }

    questionOptionsSection.querySelectorAll('div.sd-card.option').forEach(function (optionCard) {
      const footer = optionCard.querySelector('div.sd-card-footer');
      const textArea = optionCard.querySelector('textarea.question-option-input');
      const answerSection = optionCard.querySelector('section.question-option-answer');

      if (!footer || !textArea) {
        return;
      }

      footer.classList.remove('correct', 'incorrect');

      const answerType = getAnswerType(textArea);
      const correctAnswer = answerSection ? answerSection.textContent.trim() : null;
      const isCorrect = checkAnswer(textArea.value, correctAnswer, answerType);

      footer.classList.add(isCorrect ? 'correct' : 'incorrect');
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
      const textArea = optionCard.querySelector('textarea.question-option-input');
      const answerSection = optionCard.querySelector('section.question-option-answer');

      if (!footer || !textArea) {
        return;
      }

      footer.classList.remove('correct', 'incorrect');
      textArea.classList.add('show-answer');

      if (answerSection) {
        textArea.value = answerSection.textContent.trim();
      }
    });
  }

  function handleTextareaFocus(textArea) {
    document.querySelectorAll('textarea.question-option-input.show-answer').forEach(function (ta) {
      ta.value = '';
      ta.classList.remove('show-answer');
    });
  }

  document.addEventListener('click', function (event) {
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

  document.addEventListener('focus', function (event) {
    if (event.target.tagName === 'TEXTAREA') {
      handleTextareaFocus(event.target);
    }
  }, true);
})();