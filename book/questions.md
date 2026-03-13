# Polling questions

Use the following base codes to create polling questions in your book.

Details for the syntax and options can be found in the manual: [TeachBooks Questions](https://teachbooks.io/manual/_git/github.com_TeachBooks_TeachBooks-Questions/main/MANUAL.html).

### Multiple-choice single-select question

````text
::::{question} Multiple-choice Single-select
:type: multiple-choice
:variant: single-select
:admonition:
:class: question

Select a correct answer.
---
[x] This is an answer.
> Which is also a correct answer.
[ ] This is an incorrect answer.
[ ] This is the third answer.
> :::{warning}
That is not correct.
:::
[x] This is the correct answer.
---
Did you find all correct answers?
::::
````

::::{question} Multiple-choice Single-select
:type: multiple-choice
:variant: single-select
:admonition:
:class: question

Select a correct answer.
---
[x] This is an answer.
> Which is also a correct answer.
[ ] This is an incorrect answer.
[ ] This is the third answer.
> :::{warning}
That is not correct.
:::
[x] This is the correct answer.
---
Did you find all correct answers?
::::

### Multiple-choice multiple-select question

````text
::::{question} Multiple-choice Multiple-select
:type: multiple-choice
:variant: multiple-select
:admonition:
:class: question

Select a correct answer.
---
[x] This is an answer.
> Which is also a correct answer.
[ ] This is an incorrect answer.
[ ] This is the third answer.
> :::{warning}
That is not correct.
:::
[x] This is the correct answer.
---
Did you find all correct answers?
::::
````

::::{question} Multiple-choice Multiple-select
:type: multiple-choice
:variant: multiple-select
:admonition:
:class: question

Select a correct answer.
---
[x] This is an answer.
> Which is also a correct answer.
[ ] This is an incorrect answer.
[ ] This is the third answer.
> :::{warning}
That is not correct.
:::
[x] This is the correct answer.
---
Did you find all correct answers?
::::

### Short-answer blocks question

For this example we will only show case two input blocks, but more can be added if needed.

````text
::::{question} Short-answer blocks
:type: short-answer
:variant: blocks
:admonition:
:class: question

Fill in the correct answer in the input fields.
---
T[TeachBooks] The correct answer is _TeachBooks_:
= Perfect!
> Did you make a typo? Try again. Remember that the answer is case-sensitive.

MR[0<x<=1] The correct answer is a number between 0 and 1, but not including 0:
---
What do you think?
::::
````

::::{question} Short-answer blocks
:type: short-answer
:variant: blocks
:admonition:
:class: question

Fill in the correct answer in the input fields.
---
T[TeachBooks] The correct answer is _TeachBooks_:
= Perfect!
> Did you make a typo? Try again. Remember that the answer is case-sensitive.

MR[0<x<=1] The correct answer is a number between 0 and 1, but not including 0:
---
What do you think?
::::