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

- A title is optional
- `:label:` for use with `{ref}`, can be omitted.
- `:type:` for now, only `multiple-choice` is available (and the default), so the option can be omitted.
- `:variant:` for now, only `single-select`  (the default) and `multiple-select` are available.
- `:columns:` number of columns to use for the options, 2 by default, so the option can be omitted.
- `:class:` The class(es) to add to the containing `<div>` for styling.
- `:admonition:` If included, `admonition` will be added to the classes of the containing `<div>`. Can also be done through the `:class:` option.

## Examples

### Multiple-choice Single-select

``````
::::{question} Multiple-choice Single-select
:label: reference
:type: multiple-choice
:variant: single-select
:columns: 2
:admonition:

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
:columns: 2
:admonition:

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

This is a question with direct feedback. Select one of the options below by clicking.

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

::::{question} Multiple-choice Single-select
:label: reference2
:type: multiple-choice
:variant: multiple-select
:columns: 4
:admonition:
:class: example

This is a question with direct feedback. Select one of the options below by clicking.

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