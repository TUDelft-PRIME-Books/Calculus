// Functionality for short-answer block questions in Teachbooks

// Define the compute engine for math questions
const ce = new ComputeEngine.ComputeEngine();

function valueInInterval(value, interval) {
  // parse the interval string and evaluate the bounds
  // format for possible strings:
  // - `x < a` for values less than `a`.
  // - `x <= a` for values less than or equal to `a`.
  // - `x > a` for values greater than `a`.
  // - `x >= a` for values greater than or equal to `a`.
  // - `a < x < b` for values between `a` and `b`,
  // - `a <= x < b` for values between `a` and `b`, including `a` but not `b`.
  // - `a < x <= b` for values between `a` and `b`, including `b` but not `a`.
  // - `a <= x <= b` for values between `a` and `b`, including both `a` and `b`.
  const regex = /(?:(-?\d*\.?\d+)\s*(<=|<)\s*x\s*(<=|<)\s*(-?\d*\.?\d+))|(?:(x)\s*(<=|<|>=|>)\s*(-?\d*\.?\d+))/;
  const match = interval.replace(/\s+/g, '').match(regex);
  if (!match) {
    console.error('Invalid interval format: ', interval);
    return false;
  }
  eval_value = ce.parse(value).evaluate();
  if (!eval_value.isReal) {
    return false;
  }
  if (match[1] !== undefined) {
    const a = ce.parse(match[1]).evaluate();
    const b = ce.parse(match[4]).evaluate();
    if (match[2] === '<' && !(eval_value > a)) return false;
    if (match[2] === '<=' && !(eval_value >= a)) return false;
    if (match[3] === '<' && !(eval_value < b)) return false;
    if (match[3] === '<=' && !(eval_value <= b)) return false;
  } else {
    const a = ce.parse(match[6]).evaluate();
    if (match[5] === '<' && !(eval_value < a)) return false;
    if (match[5] === '<=' && !(eval_value <= a)) return false;
    if (match[5] === '>' && !(eval_value > a)) return false;
    if (match[5] === '>=' && !(eval_value >= a)) return false;
  }

  return true;
}

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
    if (textArea.classList.contains('type-MR')) return 'MR';
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
        // convert both to Expressions and compare
        try {
          const studentExpr = ce.parse(stripped);
          const correctExpr = ce.parse(correctAnswer);
          const studentEquation = studentExpr.head === 'Equal';
          const correctEquation = correctExpr.head === 'Equal';
          if (studentEquation && correctEquation) {
            const evalStudentExpr = ce.box(["Subtract", studentExpr.ops[0], studentExpr.ops[1]]).simplify();
            const evalCorrectExpr = ce.box(["Subtract", correctExpr.ops[0], correctExpr.ops[1]]).simplify();
            if (evalStudentExpr.is(evalCorrectExpr)) {
              return true;
            }
            negateStudent = ce.box(["Negate", evalStudentExpr]).simplify();
            if (negateStudent.is(evalCorrectExpr)) {
              return true;
            }
            return false;
          } else if (!studentEquation && !correctEquation) {
            return studentExpr.is(correctExpr);
          } else {
            return false;
          }

        }
        catch (e) {
          console.error('Error parsing math input: ', e);
          return false;
        }
      case 'MR':
        try {
          return valueInInterval(stripped, correctAnswer);
        }
        catch (e) {
          console.error('Error parsing math input for range checking: ', e);
          return false;
        }
      default:
        console.error('Answer checking for type '+answerType+' is not implemented yet');
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
        const mathField = optionCard.querySelector('math-field.question-option-input');

        if (footer) {
          footer.classList.remove('correct', 'incorrect');
        }
        if (textArea) {
          textArea.value = '';
          textArea.classList.remove('show-answer');
        }
        if (mathField) {
          mathField.value = '';
          mathField.classList.remove('show-answer');
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
    document.querySelectorAll('math-field.question-option-input.show-answer').forEach(function (ta) {
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
      const mathField = optionCard.querySelector('math-field.question-option-input');
      const answerSection = optionCard.querySelector('section.question-option-answer');

      
      if (!footer || (!textArea && !mathField)) {
        return;
      }

      footer.classList.remove('correct', 'incorrect');

      const answerType = getAnswerType(textArea || mathField);
      const correctAnswer = answerSection ? answerSection.textContent.trim() : null;
      const isCorrect = checkAnswer(textArea ? textArea.value : mathField.value, correctAnswer, answerType);

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
      const mathField = optionCard.querySelector('math-field.question-option-input');
      const answerSection = optionCard.querySelector('section.question-option-answer');

      if (!footer || (!textArea && !mathField)) {
        return;
      }

      footer.classList.remove('incorrect');
      footer.classList.add('correct');

      if (textArea) {
        textArea.classList.add('show-answer');
      }
      if (mathField) {
        mathField.classList.add('show-answer');
      }

      if (answerSection) {
        if (textArea) {
          textArea.value = answerSection.textContent.trim();
        }
        if (mathField) {
          mathField.value = answerSection.textContent.trim();
        }
      }
    });
  }

  function handleFocus(element) {
    // get the parent question div
    const questionDiv = getQuestionDiv(element);
    if (!questionDiv) {
      return;
    }
    // Remove all answers
    questionDiv.querySelectorAll('textarea.question-option-input.show-answer').forEach(function (ta) {
      ta.value = '';
      ta.classList.remove('show-answer');
    });
    questionDiv.querySelectorAll('math-field.question-option-input.show-answer').forEach(function (mf) {
      mf.value = '';
      mf.classList.remove('show-answer');
    });
    // Remove all feedback
    questionDiv.querySelectorAll('div.sd-card-footer').forEach(function (footer) {
      footer.classList.remove('correct', 'incorrect');
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
      handleFocus(event.target);
    }
    if (event.target.tagName === 'MATH-FIELD') {
      handleFocus(event.target);
    }
  }, true);
})();