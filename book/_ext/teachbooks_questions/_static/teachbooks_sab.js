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
  
  // first split the interval into parts based on the x. We expect either "x < a" or "a < x < b" type formats
  const parts = interval.replace(/\s+/g, '').split('x');
  Nvalue = ce.parse(value).evaluate().valueOf();
  // If the first part is empty, we have a format with one bound
  if (parts[0] === '') {
    // first get the operator and the number
    if (parts[1].startsWith('<=')) {
      bound = ce.parse(parts[1].split('<=')[1]).evaluate().valueOf();
      return (Nvalue <= bound);
    } else if (parts[1].startsWith('<')) {
      bound = ce.parse(parts[1].split('<')[1]).evaluate().valueOf();
      return (Nvalue < bound);
    } else if (parts[1].startsWith('>=')) {
      bound = ce.parse(parts[1].split('>=')[1]).evaluate().valueOf();
      return (Nvalue >= bound);
    } else if (parts[1].startsWith('>')) {
      bound = ce.parse(parts[1].split('>')[1]).evaluate().valueOf();
      return (Nvalue > bound);
    } else {
      console.error('Invalid interval format: ', interval);
      return false;
    }
  } else if (parts[1] === '') {
    console.error('Invalid interval format: ', interval);
    return false;
  } else {
    // we have a format with two bounds, so we need to check both
    // start with the left part
    let left = false;
    let right = false;
    if (parts[0].endsWith('<=')) {
      bound = ce.parse(parts[0].split('<=')[0]).evaluate().valueOf();
      if (Nvalue >= bound) left = true;
    } else if (parts[0].endsWith('<')) {
      bound = ce.parse(parts[0].split('<')[0]).evaluate().valueOf();
      if (Nvalue > bound) left = true;
    }
    // now check the right part
    if (parts[1].startsWith('<=')) {
      bound = ce.parse(parts[1].split('<=')[1]).evaluate().valueOf();
      if (Nvalue <= bound) right = true;
    } else if (parts[1].startsWith('<')) {
      bound = ce.parse(parts[1].split('<')[1]).evaluate().valueOf();
      if (Nvalue < bound) right = true;
    }
    return (left && right);
  }
}

function valueInIntervalNumerical(value, interval) {
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
  
  // first split the interval into parts based on the x. We expect either "x < a" or "a < x < b" type formats
  const parts = interval.replace(/\s+/g, '').split('x');
  Nvalue = ce.parse(value).N().valueOf();
  // If the first part is empty, we have a format with one bound
  if (parts[0] === '') {
    // first get the operator and the number
    if (parts[1].startsWith('<=')) {
      bound = ce.parse(parts[1].split('<=')[1]).N().valueOf();
      return (Nvalue <= bound);
    } else if (parts[1].startsWith('<')) {
      bound = ce.parse(parts[1].split('<')[1]).N().valueOf();
      return (Nvalue < bound);
    } else if (parts[1].startsWith('>=')) {
      bound = ce.parse(parts[1].split('>=')[1]).N().valueOf();
      return (Nvalue >= bound);
    } else if (parts[1].startsWith('>')) {
      bound = ce.parse(parts[1].split('>')[1]).N().valueOf();
      return (Nvalue > bound);
    } else {
      console.error('Invalid interval format: ', interval);
      return false;
    }
  } else if (parts[1] === '') {
    console.error('Invalid interval format: ', interval);
    return false;
  } else {
    // we have a format with two bounds, so we need to check both
    // start with the left part
    let left = false;
    let right = false;
    if (parts[0].endsWith('<=')) {
      bound = ce.parse(parts[0].split('<=')[0]).N().valueOf();
      if (Nvalue >= bound) left = true;
    } else if (parts[0].endsWith('<')) {
      bound = ce.parse(parts[0].split('<')[0]).N().valueOf();
      if (Nvalue > bound) left = true;
    }
    // now check the right part
    if (parts[1].startsWith('<=')) {
      bound = ce.parse(parts[1].split('<=')[1]).N().valueOf();
      if (Nvalue <= bound) right = true;
    } else if (parts[1].startsWith('<')) {
      bound = ce.parse(parts[1].split('<')[1]).N().valueOf();
      if (Nvalue < bound) right = true;
    }
    return (left && right);
  }
}

function checkAbsolutePrecision(value, correct, precision) {
  // Convert to interval format and use the valueInIntervalNumerical function
  const lowerBound = ce.box(["Subtract", ce.parse(correct), ce.parse(precision)]).valueOf();
  const upperBound = ce.box(["Add", ce.parse(correct), ce.parse(precision)]).valueOf();
  const interval = `${lowerBound} <= x <= ${upperBound}`;
  return valueInIntervalNumerical(value, interval);
}

function checkRelativePrecision(value, correct, precision) {
  // Reuse absolute precision checking by calculating the absolute precision from the relative precision
  const absCenter = ce.box(["Abs", ce.parse(correct)]).evaluate().valueOf();
  const absPrecision = ce.box(["Multiply", absCenter, ce.parse(precision)]).valueOf();
  return checkAbsolutePrecision(value, correct, absPrecision);
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
    if (textArea.classList.contains('type-MNR')) return 'MNR';
    if (textArea.classList.contains('type-MAP')) return 'MAP';
    if (textArea.classList.contains('type-MRP')) return 'MRP';
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
            if (evalStudentExpr.isEqual(evalCorrectExpr)) {
              return true;
            }
            negateStudent = ce.box(["Negate", evalStudentExpr]).simplify();
            if (negateStudent.isEqual(evalCorrectExpr)) {
              return true;
            }
            return false;
          } else if (!studentEquation && !correctEquation) {
            return studentExpr.isEqual(correctExpr);
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
      case 'MNR':
        try {
          return valueInIntervalNumerical(stripped, correctAnswer);
        }
        catch (e) {
          console.error('Error parsing math input for numerical range checking: ', e);
          return false;
        }
      case 'MAP':
        try {
          const parts = correctAnswer.split(';');
          if (parts.length !== 2) {
            console.error('Invalid correct answer format for MAP type. Expected "centre;precision". Got: ', correctAnswer);
            return false;
          }
          return checkAbsolutePrecision(stripped, parts[0], parts[1]);
        }
        catch (e) {
          console.error('Error parsing math input for absolute precision checking: ', e);
          return false;
        }
      case 'MRP':
        try {
          const parts = correctAnswer.split(';');
          if (parts.length !== 2) {
            console.error('Invalid correct answer format for MRP type. Expected "centre;precision". Got: ', correctAnswer);
            return false;
          }
          return checkRelativePrecision(stripped, parts[0], parts[1]);
        }
        catch (e) {
          console.error('Error parsing math input for absolute precision checking: ', e);
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
          if (mathField.classList.contains('type-M')) {
            mathField.value = answerSection.textContent.trim();
          } else if (mathField.classList.contains('type-MR') || mathField.classList.contains('type-MNR')) {
            // for M(N)R type, we want to show some extra text to indicate the correct answer is a range
            mathField.value = '\\text\{any number \}x\\text\{ such that \}' + answerSection.textContent.trim().replace(">=", "\\geq").replace("<=", "\\leq");
          } else if (mathField.classList.contains('type-MAP')) {
            // for MAP type, we want to show some extra text to indicate the correct answer is a range
            parts = answerSection.textContent.trim().split(';');
            centre = parts[0].trim();
            radius = parts[1].trim();
            mathField.value = '\\text\{any number \}x\\text\{ such that \} |x - ' + centre + '| \\leq ' + radius;
          } else if (mathField.classList.contains('type-MRP')) {
            // for MRP type, we want to show some extra text to indicate the correct answer is a range
            parts = answerSection.textContent.trim().split(';');
            centre = parts[0].trim();
            radius = parts[1].trim();
            mathField.value = '\\text\{any number \}x\\text\{ such that \} |x - ' + centre + '| \\leq ' + radius + '\\cdot |' + centre + '|';
          }
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