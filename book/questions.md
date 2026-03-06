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

Within the options part, a new option is indicated with a `[ ] ` or `[x] ` at the beginning of the line. Any previous option is then closed. An option with `[x] ` is considered correct, an option with `[ ] ` incorrect.

Each option can have feedback, which is indicated by a line starting with `> `. The feedback is associated with the most recently opened option.

The lines starting with `[ ]  `, `[x] ` or `> ` cannot be empty (after the indicator).

If no feedback is provided, the feedback will be `Correct!` or `Incorrect. Try again.`.

Questions will not be numbered.

## Options

- A title is optional
- `:label:` for use with `{ref}`, can be omitted.
- `:type:` for now, only `multiple-choice` is available (and the default), so the option can be omitted.
- `:variant:` for now, only `single-select` is available (and the default), so the option can be omitted.
- `:columns:` number of columns to use for the options, 2 by default, so the option can be omitted.

## Example

``````
::::{question} Optional title
:label: reference
:type: multiple-choice
:variant: single-select
:columns: 2

This is a question with direct feedback. Select one of the options below by clicking.

---
[ ] Answer A

This answer has several lines.

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

::::

You can deselect the option by clicking the same option.

You can select another option by clicking another option. The previous selected option will be deselected.
``````

::::{question} Optional title
:label: reference
:type: multiple-choice
:variant: single-select
:columns: 2

This is a question with direct feedback. Select one of the options below by clicking.

---
[ ] Answer A

This answer has several lines.

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

::::