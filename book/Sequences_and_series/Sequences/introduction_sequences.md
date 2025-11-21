# Sequences
In this chapter: Under Construction

```{tableofcontents}
```

This chapter deals with (infinite) sequences $a_1,a_2,a_3,\ldots$.

In order to prove statements for all positive integers we often use the **principle of mathematical induction**:

::::::{topic} The principle of mathematical induction
Let $S_n$ be a statement about a positive integer $n$. Suppose that

1) $S_1$ is true,

2) $S_{k+1}$ is true whenever $S_k$ is true.

Then $S_n$ is true for all positive integers $n$.
::::::

::::::{note}
This procedure describes the *domino effect*. Since $S_1$ is true, the second condition with $k=1$ implies that $S_2$ is true as well. Then, using the second condition with $k=2$ we conclude that $S_3$ is true. Again, using the second condition with $k=3$, we conclude that $S_4$ is true. This procedure can be followed indefinitely.
::::::
