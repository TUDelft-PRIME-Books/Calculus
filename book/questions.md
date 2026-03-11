# Questions 

## Syntax

The structure inside the admonition is always

```
text
---
options
---
text
```

The text parts are optional, but the `---` separators are required.

Questions will not be numbered.

### Multiple-choice

Within the options part, a new option is indicated with a `[ ] ` or `[x] ` at the beginning of the line. Any previous option is then closed. An option with `[x] ` is considered correct, an option with `[ ] ` incorrect.

Each option can have feedback, which is indicated by a line starting with `> `. The feedback is associated with the most recently opened option.

The lines starting with `[ ]  `, `[x] ` or `> ` cannot be empty (after the indicator).

If no feedback is provided for an option, the feedback will be `Correct!` or `Incorrect. Try again.`.

Zero correct options is allowed for `multiple-select`, not for `single-select`.

All correct options is allowed for `multiple-select` and `single-select`.

For `multiple-select` variants some overall feedback will be shown.

### Short-answer Blocks

Within an options part, a new answer is indicated with a line starting with one of the following options, where `Answer` is the correct answer (indicator). `Answer` cannot be empty, but can be any length of characters, and can be textual, numerical and/or include $\LaTeX$ math:

- `T[Answer] ` for a short answer question with a text input field, which will be checked for an exact match with the provided answer.
- `TI[Answer] ` for a short answer question with a text input field, which will be checked for a case-insensitive match with the provided answer.
- `TF[Answer] ` for a short answer question with a text input field, which will be checked for a fuzzy case-insensitive match with the provided answer. Be aware that this can lead to some unexpected answers being marked as (in)correct, and it is recommended to use this option only for longer answers where minor typos are more likely to occur, and to check the provided answer carefully for potential issues with the fuzzy matching.
- `M[Answer] ` for a short answer question with a math input field, which will check for a (simple) equality check with the provided answer using the function [`is()`](https://mathlive.io/compute-engine/guides/symbolic-computing/#smart-comparison-is) from the [MathLive Compute Engine](https://mathlive.io/compute-engine/).
- `MR[Answer]` for a short answer question with a math input field, which will check whether the provided answer is falls within the range defined by `Answer`. In this case `Answer` should be given as one of the following, where `a` and/or `b` should be replaced with the desired numbers, which can also include $\LaTeX$ math expressions that will be evaluated using the [MathLive Compute Engine](https://mathlive.io/compute-engine/). The value provided by the user will also be evaluated using the MathLive Compute Engine, and it will be checked whether this value falls within the defined range.

  - `x < a` for values less than `a`.
  - `x <= a` for values less than or equal to `a`.
  - `x > a` for values greater than `a`.
  - `x >= a` for values greater than or equal to `a`.
  - `a < x < b` for values between `a` and `b`,
  - `a <= x < b` for values between `a` and `b`, including `a` but not `b`.
  - `a < x <= b` for values between `a` and `b`, including `b` but not `a`.
  - `a <= x <= b` for values between `a` and `b`, including both `a` and `b`.

This can be optionally followed with a label that will be placed above the input field in the rendering. These can be multi lined.

A line starting with `= ` after the answer line is considered feedback for that answer if correctly answered. The feedback is associated with the most recently opened option.

A line starting with `> ` after an answer line is considered feedback for that answer if incorrectly answered. The feedback is associated with the most recently opened option.

Feedback is optional, and if not provided, the feedback will be `Correct!` or `Incorrect. Try again.`.

The lines starting with `..[Answer]  `, `= ` or `> ` cannot be empty (after the indicator, if present).

Lines following `..[Answer]  `, `= ` or `> ` that do not start with one of these indicators are considered part of the answer or feedback, and can be used to include multiple lines in the answer or feedback.

If multiple `= ` or `> ` lines are provided, these will be concatenated together to form the feedback for correctly or incorrectly answered questions, respectively.

## Options

- A title is optional, and is the first argument.

- `:label:` for use with `{ref}`, can be omitted.
- `:type:` for now, only `multiple-choice` (the default) and `short-answer` are available.
- `:variant:` for now, only `single-select` (the default for `multiple-choice`), `multiple-select` (the alternative for `multiple-choice`) and `blocks` (the default for `short-answer`) are available.
- `:columns:` number of columns to use for the options for `multiple-choice` questions. Default value is `1 1 2 2`. See [Grids](https://sphinx-design.readthedocs.io/en/latest/grids.html), second paragraph for more details. Either one single number or 4 numbers can be provided. If one single number is provided, it will be used for all screen sizes. If 4 numbers are provided, they will be used for the 4 screen sizes (small, medium, large and extra large) in that order. 
- `:class:` The class(es) to add to the containing `<div>` for styling. Adding a class might trigger existing css, so be careful. Default value is nothing/empty.
- `:admonition:` If included, `admonition` will be added to the classes of the containing `<div>`. Can also be done through the `:class:` option.
- `:nocaption:` If included, no caption will be added to the question. By default, a caption is added with the text "Question". This option can be used to hide the caption. If also no title is provided, the question will have neither a title nor a caption shown. If a title is provided, the title will be shown without surrounding brackets.
- `:show:` If included, a button will be added to show the correct answer.

## Examples

### Multiple-choice Single-select

``````
::::{question} Multiple-choice Single-select
:label: reference
:type: multiple-choice
:variant: single-select
:nocaption:

This is a question with direct feedback. Select one of the options below by clicking.

---
[x] Answer A

This answer has several lines and is also correct.

> :::{note}
:name: feedback-note
You can include admonitions.
:::

[ ] Answer C
> Math feedback: $\partial$.
[ ] Answers do not have to be numbered. Feedback is also not required.
[x] Correct answer including some display math:

  $$
  \int_0^1 x^2 dx
  $$
---

You can deselect the option by clicking the same option.

You can select another option by clicking another option. The previous selected option will be deselected.

You can reset the question with the button.

::::
``````

::::{question} Multiple-choice Single-select
:label: reference
:type: multiple-choice
:variant: single-select
:nocaption:
:showanswer:

This is a question with direct feedback. Select one of the options below by clicking.

---
[x] Answer A

This answer has several lines and is also correct.

> :::{note}
:name: feedback-note
You can include admonitions.
:::

[ ] Answer C
> Math feedback: $\partial$.
[ ] Answers do not have to be numbered. Feedback is also not required.
[x] Correct answer including some display math:

  $$
  \int_0^1 x^2 dx
  $$
---

You can deselect the option by clicking the same option.

You can select another option by clicking another option. The previous selected option will be deselected.

You can reset the question with the button.

::::

### Multiple-choice Multiple-select

``````
::::{question} Multiple-choice Multiple-select
:label: reference2
:type: multiple-choice
:variant: multiple-select
:columns: 2
:admonition:
:class: example

This is a question with feedback on submission. Select zero or more of the options below by clicking.

---
[x] Answer A

This answer has several lines and is also correct.

> :::{note}
:name: feedback-note2
You can include admonitions.
:::

[ ] Answer C
> Math feedback: $\partial$.
[ ] Answers do not have to be numbered. Feedback is also not required.
[x] Correct answer including some display math:

  $$
  \int_0^1 x^2 dx
  $$
---

You can deselect the option by clicking the same option.

You can reset the question with the reset button.

You can submit your selection using the submit button.

::::
``````

::::{question} Multiple-choice Multiple-select
:label: reference2
:type: multiple-choice
:variant: multiple-select
:columns: 1 2 3 4
:admonition:
:class: example
:showanswer:

This is a question with feedback on submission. Select zero or more of the options below by clicking.

---
[x] Answer A

This answer has several lines and is also correct.

> :::{note}
:name: feedback-note2
You can include admonitions.
:::

[ ] Answer C
> Math feedback: $\partial$.
[ ] Answers do not have to be numbered. Feedback is also not required.
[x] Correct answer including some display math:

  $$
  \int_0^1 x^2 dx
  $$
---

You can deselect the option by clicking the same option.

You can select another option by clicking another option. The previous selected option will be deselected.

You can reset the question with the button.

::::

### Short-answer Blocks

::::{question} Short-answer Blocks
:label: reference3
:type: short-answer
:variant: blocks
:admonition:
:showanswer:
:class: question

This is a short-answer question with a single wide text input per defined answer. Type your answer in the text box and press the submit button.

The correct answers are **Answer A** and _Omnia bona_ and `no feedback is not better than any feedback`.

---
T[Answer A] A math input field with exact matching.
> Negative feedback for Answer A.
= Positive feedback for Answer A.

with multiple lines.
TI[Omnia bona] A text input field with case-insensitive matching.
> Negative feedback for Omnia bona.
= Positive feedback for Omnia bona.
> More negative feedback if the answer is incorrect.
= More positive feedback if the answer is correct.
TF[No feedback is not better than any feedback] A text input field with

fuzzy case-insensitive matching.

M[x^2 + y^2 - z^2] A math input field with mathematical equivalence checking.
> Negative feedback for the math question.
= Positive feedback for the math question.

MR[3<x<=4] A math input field with range checking.
> Negative feedback for the range question.
= Positive feedback for the range question.
---

Text after the options part.

You can reset the question with the reset button.

::::