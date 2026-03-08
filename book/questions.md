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

## Options

- A title is optional, and is the first argument.

- `:label:` for use with `{ref}`, can be omitted.
- `:type:` for now, only `multiple-choice` is available (and the default), so the option can be omitted.
- `:variant:` for now, only `single-select`  (the default) and `multiple-select` are available.
- `:columns:` number of columns to use for the options for multiple-choice questions. Default value is `1 1 2 2`. See [Grids](https://sphinx-design.readthedocs.io/en/latest/grids.html), second paragraph for more details. Either one single number or 4 numbers can be provided. If one single number is provided, it will be used for all screen sizes. If 4 numbers are provided, they will be used for the 4 screen sizes (small, medium, large and extra large) in that order. 
- `:class:` The class(es) to add to the containing `<div>` for styling. Adding a class might trigger existing css, so be careful. Default value is nothing/empty.
- `:admonition:` If included, `admonition` will be added to the classes of the containing `<div>`. Can also be done through the `:class:` option.
- `:nocaption:` If included, no caption will be added to the question. By default, a caption is added with the text "Question". This option can be used to hide the caption. If also no title is provided, the question will have neither a title nor a caption shown. If a title is provided, the title will be shown without surrounding brackets.

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