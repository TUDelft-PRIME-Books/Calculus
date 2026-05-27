(Chapter:Series:Introduction)=
# Series, sums and convergence

## Introduction

In {numref}`Chapter:Sequences` we have studied sequences, which are ordered lists of numbers. In this chapter we will study what happens if we add the terms of a sequence.Because sequences can be finite or infinite, we will have to distinguish between the addition of a finite number of numbers and the addition of an infinite number of numbers.

We start with defining the term series, which is the addition of a sequence of numbers. We will also introduce the notation $\sum$ to denote the addition of a finite or an infinite number of numbers. We will then study the convergence of series, which is the question whether the sum of a(n in)finite number of numbers makes sense.

## Series and sums

In {numref}`Sec:SumsAndProducts:Sums` we have already introduced the summation symbol $\sum$ (capital Greek letter sigma) to denote the addition of any number of numbers. As sequences are (ordered) sets of numbers, we can use the summation symbol to denote the addition of the terms of a sequence. This is called a series:

::::{prf:definition}
:label: Def:Series:Definition

A **series** is the addition of all of the terms of a sequence.

A series is called a **finite series** if the sequence is finite.

A series is called an **infinite series** if the sequence is infinite.
::::

::::{prf:notation}
:label: Not:Series:Definition

For a finite sequence $\{a_n\}_{n=p}^q$, the corresponding finite series is denoted by

$$
\sum_{n=p}^q a_n.
$$

For an infinite sequence $\{a_n\}_{n=p}^{\infty}$, the corresponding infinite series is denoted by

$$
\sum_{n=p}^{\infty}a_n.
$$

::::

::::{prf:definition}
:label: Def:Series:SummationIndex

The letter $n$ in the notation $\displaystyle\sum_{n=p}^qa_n$ or $\displaystyle\sum_{n=p}^{\infty}a_n$ is called the **index of summation**.
::::

Because the index of summation is just a dummy variable, we can replace it by any other letter. For example, we can write $\displaystyle\sum_{k=p}^qa_k$ or $\displaystyle\sum_{m=p}^{\infty}a_m$ instead of $\displaystyle\sum_{n=p}^qa_n$ or $\displaystyle\sum_{n=p}^{\infty}a_n$, respectively.

The result of a series can be a number, but it can also be a function, but it can also result nothing. To distinguish between these cases, we will use the following terminology:

::::{prf:definition}
:label: Def:Series:Sum

If a series results in a number or a function, then we call this number or function the **sum** of the series.
::::

To have a simple notation for the sum of a series, we will use the following notation:

::::{prf:notation}
:label: Not:Series:Sum

If a series $\displaystyle\sum_{n=p}^qa_n$ or $\displaystyle\sum_{n=p}^{\infty}a_n$ has the sum $S$, then we write

$$
\sum_{n=p}^qa_n=S \quad\text{or}\quad \sum_{n=p}^{\infty}a_n=S,
$$

respectively.
::::

We will first turn our attention to finite series, which is just the addition of a finite number of numbers. We will then turn our attention to the sum of an infinite series, which is more complicated and requires the notion of convergence.

(Sec:Series:FiniteSeries)=
## Finite series

We start with a short but important theorem about the sum of a finite series, which will be used in the next section to find the sum of an infinite series:

::::{prf:theorem}
:label: Thm:Series:FiniteSeries

The sum of a finite series exists.
::::

::::{admonition} Proof of {prf:ref}`Thm:Series:FiniteSeries`
:class: tudproof, dropdown

Assume $\{a_n\}_{n=p}^q$ is a finite sequence of terms, then we have

$$
\sum_{n=p}^qa_n=a_p+a_{p+1}+a_{p+2}+\cdots+a_q.
$$

Using brackets, we can write this as

$$
\sum_{n=p}^qa_n=\left(\cdots\left(\left(a_p+a_{p+1}\right)+a_{p+2}\right)+\cdots\right)+a_q.
$$

Since the addition of two numbers is well-defined, we can add $a_p$ and $a_{p+1}$ to get a number, which we can then add to $a_{p+2}$ to get another number, and so on until we have added all the terms of the series. Hence, the sum of a finite series exists.

::::

::::{prf:remark}
:label: Rem:Series:FiniteSeries
Because of {prf:ref}`Thm:Series:FiniteSeries` often the term _finite series_ is not used, but the term **finite sum** is used instead.

As a consequence of this, a _series_ is often implicitly assumed to be an _infinite series_, unless it is explicitly stated that the series is a finite series or a finite sum.
::::

Because of the clear overlap with finite sums, we refer to {numref}`Sec:SumsAndProducts:Sums` for more details on finite series and finite sums.

(Sec:Series:InfiniteSeries)=
## Infinite series and partial sums

We will now turn our attention to infinite series, or by {prf:ref}`Rem:Series:FiniteSeries` just series, which is more complicated and requires some extra definitions to handle the summation of an infinite number of terms.

::::{prf:definition}
:label: Def:Series:PartialSum

Given a series $\displaystyle\sum_{n=p}^{\infty}a_n$, we define the $n$th **partial sum** of this series as

$$
s_n=\displaystyle\sum_{k=p}^{n+p-1}a_k=a_p+a_{p+1}+a_{p+2}+\cdots+a_{n+p-1}.
$$
::::

In other words, the $n$th partial sum of a series is the sum of the first $n-p+1$ terms of the series.

::::::{note}
For $\displaystyle\sum_{n=1}^{\infty}a_n$ the $N$th partial sum $s_N$ is the sum of the first $N$ terms. However, we call $s_N$ still the $N$th partial sum of the series even when the series $\displaystyle\sum a_n$ does not start at $n=1$. So, for instance, if $\displaystyle\sum_{n=2}^{\infty}\frac{\ln(n)}{n}$ then $s_N=\displaystyle\sum_{n=2}^N\frac{\ln(n)}{n}$ is the sum of the first $N-1$ terms and if $\displaystyle\sum_{n=0}^{\infty}\frac{1}{n^2+1}$ then $s_N=\displaystyle\sum_{n=0}^N\frac{1}{n^2+1}$ is the sum of the first $N+1$ terms.
::::::

## Convergence and divergence

Using these partial sums we can now look at the infinite series:

\begin{align*}
\sum_{n=p}^{\infty}a_n &= \lim_{n\to\infty}\sum_{k=p}^{n+p-1}a_k \\
&= \lim_{n\to\infty}s_n.
\end{align*}

So if $\lim\limits_{n\to\infty}s_n$ would exist, then the sum of the infinite series $\displaystyle\sum_{n=p}^{\infty}a_n$ would be equal to this limit. If $\lim\limits_{n\to\infty}s_n$ does not exist, then we cannot determine the sum of the infinite series $\displaystyle\sum_{n=p}^{\infty}a_n$. This is summarised in the next theorem:

::::{prf:theorem}
:label: Thm:Series:ConvergenceSum

Let $\displaystyle\sum_{n=p}^{\infty}a_n$ be an infinite series and let $s_n$ be its $n$th partial sum.

The sum $S$ of the series $\displaystyle\sum_{n=p}^{\infty}a_n$ exists if and only if the limit $\lim\limits_{n\to\infty}s_n=S$ exists.

If the sum exists we write $\displaystyle\sum_{n=p}^{\infty}a_n=S$.

::::

We do not give a formal proof of this theorem, but it is a direct consequence of the definition of the sum of an infinite series and the definition of the limit of a sequence. Because the existence of the sum of an infinite series is equivalent to the existence of the limit of the sequence of partial sums, we can use all the tools that we have developed in {numref}`Chapter:Sequences` to determine whether the limit of the sequence of partial sums converges or diverges and to find the sum of a series. Because if this close link between infinite series and limits of sequences, we will reuse the terms _convergence_ and _divergence_ for series, which we have already used for sequences:

::::{prf:definition}
:label: Def:Series:ConvergenceSum

Let $\displaystyle\sum_{n=p}^{\infty}a_n$ be an infinite series, let $s_n$ be its $n$th partial sum and let $S$ be a number.

If the limit $\lim\limits_{n\to\infty}s_n$ exists and equals $S$, then we say that the series $\displaystyle\sum_{n=p}^{\infty}a_n$ **converges** to $S$.

If the limit $\lim\limits_{n\to\infty}s_n$ does not exist, then we say that the series $\displaystyle\sum_{n=p}^{\infty}a_n$ **diverges**.
::::

One major result for of this definition of converges using partial sums, is that we can proof the next theorem:

::::::{prf:theorem}
:label: Thm:Series:GeneralTerm
If the series $\displaystyle\sum a_n$ is convergent, then $\lim\limits_{n\to\infty}a_n=0$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:GeneralTerm`
:class: tudproof
Let $\{s_n\}$ be the sequence of partial sums of the series $\displaystyle\sum a_n$.

If $\displaystyle\sum a_n$ is convergent, then $\lim\limits_{n\to\infty}s_n=s$ exists. Then we have

$$
\lim_{n\to\infty}a_n=\lim_{n\to\infty}\left(s_n-s_{n-1}\right)=\lim_{n\to\infty}s_n-\lim_{n\to\infty}s_{n-1}=s-s=0.
$$

::::::

We want to stress the following:

::::::{warning}
The converse of {prf:ref}`Thm:Series:GeneralTerm` is not true: if $\lim\limits_{n\to\infty}a_n=0$ the series needs not to be convergent!
::::::

This is shown by the following example:

::::::{prf:example}
:label: Ex:Series:HarmonicSeries
Consider the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$.

First note that $\lim\limits_{n\to\infty}\frac{1}{n}=0$, so the general term of the series tends to zero.

Now consider the $n$th partial sum of the series:

$$
s_n=\displaystyle\sum_{k=1}^n\frac{1}{k}=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}.
$$

{numref}`Fig:Series:HarmonicSeries` gives a visualisation of the $n$th partial sum of the series.

```{figure} Images/harmonic.png
---
width: 50%
name: Fig:Series:HarmonicSeries
align: center
---
Visualisation of the $n$th partial sum of the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$, which is given by the sum of the areas of the rectangles. The graph of $f(x)=\frac{1}{x}$ is also given for comparison.
```

:::{todo}
Replace {numref}`Fig:Series:HarmonicSeries` with an applet.
:::

Note that the top left corner of each rectangle aligns with the function $f(x)=\frac{1}{x}$. Because $f$ is a strictly decreasing function, the upper right corner of each rectangle is above the graph of $f$. This means that the area of each rectangle is greater than the area under the graph of $f$ between $n$ and $n+1$. Hence, we have

$$
s_n = \sum_{k=1}^n\frac{1}{k} > \sum_{k=1}^n\int_{k}^{k+1}\frac{1}{x}\,dx = \int_1^{n+1}\frac{1}{x}\,dx.
$$

The last integral we can easily evaluate:

$$
\int_1^{n+1}\frac{1}{x}\,dx=\bigg[\ln(x)\bigg]_1^{n+1}=\ln(n+1).
$$

This means that

$$
\lim_{n\to\infty}s_n > \lim_{n\to\infty}\ln(n+1) = \infty,
$$

and so the series is divergent by {prf:ref}`Def:Series:ConvergenceSum`.

This proves that the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$ is divergent.
::::::

Because the example uses an integral to test for convergence/divergence, it is commonly called the **integral test** for convergence/divergence, which we will discuss in more detail in {numref}`Sec:Series:PositiveSeries:IntegralTest`.

Although the contrary of {prf:ref}`Thm:Series:GeneralTerm` is not true, the theorem still gives us a useful test for divergence of series, by contraposition of the theorem. Contraposition of a statement of the form "If $P$, then $Q$." is the statement "if not $Q$ then not $P$".

Based on {prf:ref}`Thm:Series:GeneralTerm`, we have

$$
P = \text{the series $\displaystyle\sum a_n$ is convergent},
$$

which means that

$$
\text{not }P = \text{the series $\displaystyle\sum a_n$ is not convergent} = \text{the series $\displaystyle\sum a_n$ is divergent}.
$$

For the next part the statement, $Q$, we have (in a longer form):

$$
Q = \text{the limit $\lim\limits_{n\to\infty}a_n$ exists and equals $0$},
$$

which means that

$$
\text{not }Q = \text{the limit $\lim\limits_{n\to\infty}a_n$ does not exist or the limit $\lim\limits_{n\to\infty}a_n$ exists but does not equal $0$}.
$$

Hence, contraposition of {prf:ref}`Thm:Series:GeneralTerm` gives us the following corollary:

::::::{prf:corollary}
:label: Thm:Series:GeneralTermCorollary
If $\lim\limits_{n\to\infty}a_n$ does not exist or if $\lim\limits_{n\to\infty}a_n\ne 0$, then the series $\sum a_n$ is divergent.
::::::

::::::{prf:definition}
:label: Def:Series:TestForDivergence

{prf:ref}`Thm:Series:GeneralTermCorollary` is called **the test for divergence**.
::::::

::::{prf:example}
:label: Ex:Series:DivergenceTest1

The general term of the series $\displaystyle\sum_{n=1}^{\infty}\frac{2n}{3n+1}$ satsifies 

$$
\lim_{n\to\infty}\frac{2n}{3n+1}=\frac{2}{3}\neq0,
$$

so by the _test for divergence_, the series $\displaystyle\sum_{n=1}^{\infty}\frac{2n}{3n+1}$ is divergent.

::::

::::{prf:example}
:label: Ex:Series:DivergenceTest2

The series $\displaystyle\sum_{n=0}^{\infty}\left(\frac{3}{2}\right)^n$ is divergent, since, by the _test for divergence_, $\displaystyle\lim_{n\to\infty}\left(\frac{3}{2}\right)^n$ does not exist.

::::


::::{prf:example}
:label: Ex:Series:DivergenceTest3

The series $\displaystyle\sum_{n=1}^{\infty}\sin(n)$ is divergent, since $\displaystyle\lim_{n\to\infty}\sin(n)$ does not exist.
::::

::::{prf:example}
:label: Ex:Series:DivergenceTest4

Consider the sequence $\{\arctan(n)\}_{n=1}^{\infty}$. Then we have

$$
\lim_{n\to\infty}\arctan(n)=\frac{1}{2}\pi\neq0.
$$

So by the _test for divergence_ the series $\displaystyle\sum_{n=1}^{\infty}\arctan(n)$ is divergent.
::::

The test for divergence only gives us a test for divergence, but it does not give us a test for convergence. In most cases one has to resort to other tests for convergence/divergence, which we will discuss in the next sections. For several special types of series, however, we can already determine whether they are convergent or divergent and find their sum if they are convergent, which we will treat in {numref}`Sec:Series:SpecialSeries`.

## Calculating with sums of series

If you have determined that an infinite series $\displaystyle\sum_{n=1}^{\infty}a_n$ is convergent with sum $S$, then you could also ask yourself whether the new series $\displaystyle\sum_{n=1}^{\infty}ca_n$ for some number $c$ is also convergent and if so, what its sum is. The next theorem gives us the answer to this question and even some more useful properties of sums of infinite series:

::::{prf:theorem}
:label: Thm:Series:CalculatingSums
If the series $\displaystyle\sum_{n=p}^{\infty}a_n$ is convergent with sum $A$, the series $\displaystyle\sum_{n=p}^{\infty}b_n$ is convergent with sum $B$, $c$ is a number and $t$ is an integer, then we have

$$
\sum_{n=p}^{\infty}(a_n+b_n) = A+B,
$$

$$
\sum_{n=p}^{\infty}ca_n = cA
$$

and

$$
\sum_{n=1+t}^{\infty}a_{n-t} = A.
$$

::::

Because of the last properties in {prf:ref}`Thm:Series:PropertiesFiniteSeries` and {prf:ref}`Thm:Series:CalculatingSums`, we will make the following assumption about the index of summation for the rest of this chapter:

::::{prf:assumption} Index of summation
:label: Conv:Series:IndexOfSummation

All series in this chapter will start at $n=1$ unless otherwise specified.

::::

This will make subsequent definitions, theorems and similar texts easier to state and understand.

## Absolute and conditional convergence

In many cases the terms of a series do not have to be positive, but they can also be (sometimes) negative. Sometimes it is useful to consider a new series which has as terms the absolute values of the terms of the original series, which is called the **absolute value series** of the original series. If such an absolute value series converges or diverges, then we can also deduce something about the convergence/divergence of the original series.

We start with a new definition:

::::::{prf:definition} Absolute convergence
:label: Def:Series:AbsoluteConvergence
A series $\displaystyle\sum a_n$ is called **absolutely convergent** if the series of absolute values $\displaystyle\sum|a_n|$ is convergent.
::::::

One of the most important results about absolute convergence is that if a series is absolutely convergent, then it is convergent:

::::::{prf:theorem}
:label: Thm:Series:AbsoluteConvergence
If a series $\displaystyle\sum a_n$ is absolutely convergent, then it is convergent.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:AbsoluteConvergence`
:class: tudproof, dropdown

Without loss of generality we can assume that the series $\displaystyle\sum a_n$ starts at $n=1$.[^changeIndex]

[^changeIndex]: If the series $\displaystyle\sum a_n$ starts at $n=p$ with $p\ne1$, then we can change the index of summation to make the series start at $n=1$.

First we define two new series $\displaystyle\sum a_n^+$ with $a_n^+=\max\{a_n,0\}$ for all $n$ and $\displaystyle\sum a_n^-$ with $a_n^-=\max\{-a_n,0\}$ for all $n$. Note that $a_n=a_n^+-a_n^-$ for all $n$ and $|a_n|=a_n^++a_n^-$ for all $n$.

Now consider the following three partials sums:

\begin{align*}
t_n = \sum_{k=1}^n |a_k| \\
p_n = \sum_{k=1}^n a_k^+ \\
q_n = \sum_{k=1}^n a_k^-.
\end{align*}

From the convergence of $\displaystyle\sum|a_n|$ we have that $\lim\limits_{n\to\infty}t_n=t$ exists. We also have that 

$$
t_{n+1}-t_n = \sum_{k=1}^{n+1}|a_k|-\sum_{k=1}^n|a_k| = |a_{n+1}|\geq0,
$$

so the sequence $\{t_n\}$ is non-decreasing with $t$ as an upper bound: $t_n\leq t$ for all $n$.

For the partial sum $p_n$ we have

$$
p_{n+1}-p_n = \sum_{k=1}^{n+1}a_k^+-\sum_{k=1}^na_k^+ = a_{n+1}^+=\max\{a_{n+1},0\}\geq0,
$$

so the sequence $\{p_n\}$ is non-decreasing. Also,

$$
p_n = \sum_{k=1}^n a_k^+ \leq \sum_{k=1}^n (a_k^++a_k^-) = \sum_{k=1}^n |a_k| = t_n \leq t,
$$

which makes the sequence $\{p_n\}$ bounded from above. By {prf:ref}`Thm:Sequences:MonotonicBounded` the sequence $\{p_n\}$ is convergent, so $\lim\limits_{n\to\infty}p_n=p$ exists.

For the partial sum $q_n$ we have

$$
q_{n+1}-q_n = \sum_{k=1}^{n+1}a_k^- - \sum_{k=1}^na_k^- = a_{n+1}^-=\max\{-a_{n+1},0\}\geq0,
$$

so the sequence $\{q_n\}$ is also non-decreasing. Also,

$$
q_n = \sum_{k=1}^n a_k^- \leq \sum_{k=1}^n (a_k^++a_k^-) = \sum_{k=1}^n |a_k| = t_n \leq t,
$$

so the sequence $\{q_n\}$ is also bounded from above. By {prf:ref}`Thm:Sequences:MonotonicBounded` the sequence $\{q_n\}$ is also convergent, so $\lim\limits_{n\to\infty}q_n=q$ exists.

Now can turn to the original series $\displaystyle\sum a_n$. The $n$th partial sum of this series is

\begin{align*}
s_n&=\sum_{k=1}^na_k=\sum_{k=1}^n(a_k^+-a_k^-)\\
&=\sum_{k=1}^na_k^+-\sum_{k=1}^na_k^-\\
&=p_n-q_n.
\end{align*}

Because $\lim\limits_{n\to\infty}p_n=p$ and $\lim\limits_{n\to\infty}q_n=q$, we have

$$
\lim_{n\to\infty}s_n = \lim_{n\to\infty}p_n - q_n = \lim_{n\to\infty}p_n - \lim_{n\to\infty}q_n = p-q.
$$

This shows that $\displaystyle\sum a_n$ is convergent, which proves the theorem.

:::

::::::{prf:example}
:label: Ex:Series:AbsoluteConvergence1

Consider the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}$. The absolute value series of this series is $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$.

In {numref}`Fig:Series:AbsoluteConvergence1` we have a visualisation of the $n$th partial sum $t_n$ of the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$.

```{figure} Images/integral.png
:name: Fig:Series:AbsoluteConvergence1

Visualisation of the $n$th partial sum $t_n$ of the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$, which is given by the sum of the areas of the rectangles. The graph of $f(x)=\frac{1}{x^2}$ is also given for comparison.
```

:::{todo}
Replace {numref}`Fig:Series:AbsoluteConvergence1` with an applet.
:::

Note that for the $n$th rectangle the top right corner aligns with the graph of $f(x)=\frac{1}{x^2}$ for $x\geq1$. This means that the area of each rectangle is less than the area under the graph of $f$ between $n-1$ and $n$ for $n\geq2$. Hence, we have

\begin{align*}
t_n &= \sum_{k=1}^n\frac{1}{k^2} \\
&= 1+\sum_{k=2}^n\frac{1}{k^2} \\
&< 1+\sum_{k=2}^n\int_{k-1}^{k}\frac{1}{x^2}\,dx \\
&= 1+\int_1^{n}\frac{1}{x^2}\,dx \\
&= 1+\bigg[-\frac{1}{x}\bigg]_1^{n} \\
&= 2+\left(-\frac{1}{n}+1\right) \\
&= 2-\frac{1}{n} \\
&< 2.
\end{align*}

This means that the sequence of partial sums $\{t_n\}$ is bounded from above by $2$. Also, we have

$$
t_{n+1}-t_n = \frac{1}{(n+1)^2} > 0,
$$

so the sequence $\{t_n\}$ is strictly increasing. By {prf:ref}`Thm:Sequences:MonotonicBounded` the sequence $\{t_n\}$ is convergent, so $\lim\limits_{n\to\infty}t_n=t$ exists.

This means that the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$ is convergent, so the original series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}$ is absolutely convergent by {prf:ref}`Def:Series:AbsoluteConvergence`, which means that $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}$ is also convergent by {prf:ref}`Thm:Series:AbsoluteConvergence`.

::::::


::::::{prf:example}
:label: Ex:Series:AbsoluteConvergence2
Now we consider the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$. The absolute value series of this series is $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$, which we have shown to be divergent in {prf:ref}`Ex:Series:HarmonicSeries`.

So the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$ is not absolutely convergent.

But, we can show something more about this series. Consider the $n$th partial sum of this series:

$$
s_n = \sum_{k=1}^n\frac{(-1)^{k-1}}{k}.
$$

For these partial sums we have the following property:

\begin{align*}
s_{2n+2}-s_{2n} &= \sum_{k=1}^{2n+2}\frac{(-1)^{k-1}}{k}-\sum_{k=1}^{2n}\frac{(-1)^{k-1}}{k} \\
&= \sum_{k=2n+1}^{2n+2}\frac{(-1)^{k-1}}{k} \\
&= \frac{(-1)^{2n}}{2n+1}+\frac{(-1)^{2n+1}}{2n+2} \\
&= \frac{1}{2n+1}-\frac{1}{2n+2} \\
&= \frac{1}{(2n+1)(2n+2)}.
\end{align*}

As the last value is positive, the sequence $\{s_{2n}\}$ is strictly increasing. If  we now consider only the partial sum $s_{2n}$ we find

\begin{align*}
s_{2n} &= \sum_{k=1}^{2n}\frac{(-1)^{k-1}}{k} \\
&= 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} - \frac{1}{7} + \cdots - \frac{1}{2n-2} + \frac{1}{2n-1} - \frac{1}{2n} \\
&= 1 - \left(\frac{1}{2} - \frac{1}{3}\right) - \left(\frac{1}{4} - \frac{1}{5}\right) - \left(\frac{1}{6} - \frac{1}{7}\right) - \cdots - \left(\frac{1}{2n-2} - \frac{1}{2n-1}\right) - \frac{1}{2n} \\
&= 1 - \sum_{k=1}^{n-1}\left(\frac{1}{2k} - \frac{1}{2k+1}\right) - \frac{1}{2n} \\
&= 1 - \sum_{k=1}^{n-1}\frac{1}{(2k)(2k+1)} - \frac{1}{2n}.
\end{align*}

Because of the positivity of all terms in the sum $\displaystyle\sum_{k=1}^{n-1}\frac{1}{(2k)(2k+1)}$ and the term $\frac{1}{2n}$, we have found that $\{s_n\}$ is bounded from above by $1$. Also, we have already found that $\{s_{2n}\}$ is strictly increasing. By {prf:ref}`Thm:Sequences:MonotonicBounded` the sequence $\{s_{2n}\}$ is convergent, so $\lim\limits_{n\to\infty}s_{2n}=s$ exists.

Now we turn to the sequence $\{s_{2n+1}\}$. We have

\begin{align*}
s_{2n+1} &= \sum_{k=1}^{2n+1}\frac{(-1)^{k-1}}{k} \\
&= \sum_{k=1}^{2n}\frac{(-1)^{k-1}}{k} + \frac{(-1)^{2n}}{2n+1} \\
&= s_{2n} + \frac{1}{2n+1}.
\end{align*}

But this means that

$$
\lim_{n\to\infty}s_{2n+1} = \lim_{n\to\infty}s_{2n} + \lim_{n\to\infty}\frac{1}{2n+1} = s + 0 = s.
$$

This tells us that all even partial sums ánd all odd partial sums converge to the same limit $s$, so all partial sums converge to $s$. Hence, the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$ is convergent.

::::::

{prf:ref}`Ex:Series:AbsoluteConvergence2` shows that a series can be convergent, but not absolutely convergent. In that case we say that the series is conditionally convergent:

::::::{prf:definition} Conditional convergence
:label: Def:Series:RelativeConvergence
A series $\displaystyle\sum a_n$ is called **conditionally convergent** if it is convergent, but not absolute convergent.
::::::


::::::{note}
Later we will be able to show that $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}=\ln(2)$.
::::::

This concludes our treatment of absolute and conditional convergence. As you may have noticed, showing (absolute/conditional) convergence can be a lot of work. In {numref}`Sec:Series:SpecialSeries`, we will see some special types of series for which we can easily determine whether they are convergent or divergent and find their sum if they are convergent. For other series, we will need to use more advanced tests for convergence/divergence, which we will discuss in the sections after that.

## Grasple exercises

:::{todo}
Add Grasple exercises for {numref}`Chapter:Series:Introduction`.
:::

## Exercises

::::{exercise}
:label: Exc:Series:FibonacciExercise
The sequence $\{F_n\}_{n=1}^{\infty}$ of Fibonacci numbers is defined by $F_{n+2}=F_n+F_{n+1}$ for $n=1,2,3,\ldots$ and $F_1=F_2=2$.

(a) Use partial fractions $\dfrac{1}{F_nF_{n+2}}=\dfrac{A}{F_n}+\dfrac{B}{F_{n+2}}$ to show that

$$
\frac{1}{F_nF_{n+2}}=\frac{1}{F_nF_{n+1}}-\frac{1}{F_{n+1}F_{n+2}},\quad n=1,2,3,\ldots.
$$

(b) Find the sum of $\displaystyle\sum_{n=1}^{\infty}\frac{1}{F_nF_{n+2}}$.

(c) Find the sum of $\displaystyle\sum_{n=1}^{\infty}\frac{F_{n+1}}{F_nF_{n+2}}$.

(d) Use partial fractions $\dfrac{1}{F_nF_{n+4}}=\dfrac{A}{F_n}+\dfrac{B}{F_{n+4}}$ to show that

$$
\frac{1}{F_nF_{n+4}}=\frac{1}{3F_nF_{n+2}}+\frac{1}{3F_{n+2}F_{n+4}},\quad n=1,2,3,\ldots.
$$

(e) Find the sum of $\displaystyle\sum_{n=1}^{\infty}\frac{1}{F_nF_{n+4}}$.
::::

:::{admonition} Solution of {numref}`Exc:Series:FibonacciExercise`
:class: solution, dropdown
(a) Note that

\begin{align*}
\frac{1}{F_nF_{n+2}}&=\frac{A}{F_n}+\frac{B}{F_{n+2}}=\frac{AF_{n+2}+BF_n}{F_nF_{n+2}}\\
&=\frac{A\left(F_n+F_{n+1}\right)+BF_n}{F_nF_{n+2}}=\frac{(A+B)F_n+AF_{n+1}}{F_nF_{n+2}}.
\end{align*}
This implies that $A=\dfrac{1}{F_{n+1}}$ and $B=-\dfrac{1}{F_{n+1}}$. Hence we have

$$
\frac{1}{F_nF_{n+2}}=\frac{1}{F_nF_{n+1}}-\frac{1}{F_{n+1}F_{n+2}}.
$$

(b) Now we use the telescoping property to obtain

\begin{align*}
\sum_{n=1}^{\infty}\frac{1}{F_nF_{n+2}}&=\lim\limits_{N\to\infty}\sum_{n=1}^N\left(\frac{1}{F_nF_{n+1}}-\frac{1}{F_{n+1}F_{n+2}}\right)\\
&=\lim\limits_{N\to\infty}\left(\frac{1}{F_1F_2}-\frac{1}{F_{N+1}F_{N+2}}\right)=1.
\end{align*}
(c) Again, we use the telescoping property to obtain

\begin{align*}
\sum_{n=1}^{\infty}\frac{F_{n+1}}{F_nF_{n+2}}&=\lim\limits_{N\to\infty}\sum_{n=1}^{\infty}\left(\frac{1}{F_n}-\frac{1}{F_{n+2}}\right)\\
&=\lim\limits_{N\to\infty}\left(\frac{1}{F_1}+\frac{1}{F_2}-\frac{1}{F_{N+1}}-\frac{1}{F_{N+2}}\right)=1+1=2.
\end{align*}
(d) Note that

\begin{align*}
\frac{1}{F_nF_{n+4}}&=\frac{A}{F_n}+\frac{B}{F_{n+4}}=\frac{AF_{n+4}+BF_n}{F_nF_{n+4}}=\frac{A\left(F_{n+2}+F_{n+3}\right)+BF_n}{F_nF_{n+4}}\\
&=\frac{A\left(F_{n+2}+F_{n+1}+F_{n+2}\right)+BF_n}{F_nF_{n+4}}\\
&=\frac{A\left(2F_{n+2}+F_{n+2}-F_n\right)+BF_n}{F_nF_{n+4}}=\frac{A\left(3F_{n+2}-F_n\right)+BF_n}{F_nF_{n+4}}\\
&=\frac{3AF_{n+2}+(B-A)F_n}{F_nF_{n+4}}\quad\Longrightarrow\quad A=B=\frac{1}{3F_{n+2}}.
\end{align*}
(e) This implies that

\begin{align*}
\sum_{n=1}^{\infty}\frac{1}{F_nF_{n+4}}&=\sum_{n=1}^{\infty}\left(\frac{1}{3F_nF_{n+2}}+\frac{1}{3F_{n+2}F_{n+4}}\right)\\
&=\frac{1}{3}\left(\sum_{n=1}^{\infty}\frac{1}{F_nF_{n+2}}+\sum_{n=1}^{\infty}\frac{1}{F_nF_{n+2}}-\frac{1}{F_1F_3}-\frac{1}{F_2F_4}\right)\\
&=\frac{1}{3}\left(1+1-\frac{1}{2}-\frac{1}{3}\right)=\frac{7}{18}.
\end{align*}
:::

