(Sec:Algebra:SetTheoryAndLogic)=

# Set theory and logic

In this section, we will introduce the basic concepts of set theory and logic, which are fundamental to understanding mathematical structures and reasoning. We will cover topics such as sets, subsets, unions, intersections, and logical connectives. This will provide a solid foundation for the more advanced topics that we will encounter later in the book.

We will also introduce the special notations for natural numbers, integers and rational numbers. These sets of numbers are essential for various mathematical operations and will be used throughout the book.

:::{todo}
Write {numref}`Sec:Algebra:SetTheoryAndLogic` in more detail, including examples and exercises.
:::

## Mathematical induction

Sometimes we will consider a statement $S_n$ in terms of an integer $n$. In order to prove that the statement holds for all $n\in\mathbb{N}$ we often use the **principle of mathematical induction**, which is explained in the following theorem.

::::::{prf:theorem} Principle of mathematical induction
:label: Thm:Algebra:MathematicalInduction

Let $S_n$ be a statement for all integers $n$ larger than or equal to $p$.

If 

1) $S_p$ is true,

and

2) $S_{k+1}$ is true whenever $S_k$ is true for some $k$,

then $S_n$ is true for all integers $n\geq p$.

::::::

::::::{note}
This procedure describes the *domino effect*. Since $S_p$ is true, the second condition with $k=p$ implies that $S_{p+1}$ is true as well. Then, using the second condition with $k=p+1$ we conclude that $S_{p+2}$ is true. Again, using the second condition with $k=p+2$, we conclude that $S_{p+3}$ is true. This procedure can be followed indefinitely.

More information about the principle of mathematical induction can be found in [Section 3.4. Mathematical Induction of the book Delftse Foundations of Computation](https://interactivetextbooks.tudelft.nl/delftse-foundations-of-computation/content/logic/induction.html).
::::::
