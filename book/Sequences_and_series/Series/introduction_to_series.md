(Chapter:Series:Introduction)=
# Introduction to series

## Introduction

In {numref}`Chapter:Sequences` we have studied sequences, which are ordered lists of numbers. In this chapter we will study what happens if we add the terms of a sequence. Since sequences can be finite or infinite, we will have to distinguish between the addition of a finite number of terms and the addition of an infinite number of terms.

Since we already dealt with finite summations in {numref}`Sec:SumsAndProducts`, we only consider summations of infinite sequences in this chapter. We will study the convergence of series, which is the question whether the sum of an infinite number of terms makes sense.

In {numref}`Sec:SumsAndProducts:Sums` we have already introduced the summation symbol $\sum$ (capital Greek letter sigma) to denote the addition of any (finite) number of terms. As sequences are (ordered) sets of numbers, we can use the summation symbol to denote the addition of the terms of an infinite sequence as well. Let $\left(a_n\right)_{n=1}^{\infty}$ be an infinite sequence, then we write

$$
\sum_{n=1}^{\infty}a_n=a_1+a_2+a_3+\cdots.
$$

Does this make sense? 

We start informally with two examples to get an idea. 

The next examples show that such a summation can either give a finite or an infinite result.

:::::{prf:example}
:label: Ex:Series:NaturalNumbers

It is clear that 

$$
\sum_{n=1}^{\infty}n=1+2+3+\cdots=\infty,
$$

since the result grows beyond any finite real number.
:::::

:::::{prf:example}
:label: Ex:Series:GeometricSeriesExample1

$$
\sum_{n=1}^{\infty}\frac{1}{2^n}=\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots=1.
$$

This result can be visualised as shown in {numref}`Fig:Series:GeometricSeries`. The idea behind the visualisation is that when you take a unit square, which has area $1$, and you cut half of it off, then you are left with a rectangle with area $\frac{1}{2}$. If you cut half of this rectangle off, then you are left with a square with area $\frac{1}{4}$. If you cut half of this square off, then you are left with a rectangle with area $\frac{1}{8}$, and so on. If you keep cutting half of the remaining rectangle or square off, then the total area of the cut off rectangles or squares will be $\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots$, which in the end approaches the area of the original unit square, which is $1$.

```{figure} Images/geometric.png
---
width: 50%
name: Fig:Series:GeometricSeries
align: center
---
A visual proof of $\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots=1$.
```

:::{todo}
Replace {numref}`Fig:Series:GeometricSeries` with an applet.
::: 

:::::

The formal definition of a *series* is the limit of the sequence of *partial sums* as we will see below. So we start with *partial sums*.

(Sec:Series:PartialSums)=
## Partial sums

Let $\left(a_n\right)_{n=p}^{\infty}$ with $p$ an integer be a sequence, then we consider the *series*

$$
\sum_{n=p}^{\infty}a_n=a_p+a_{p+1}+a_{p+2}+\cdots.
$$

We start with the definition of partial sums of an infinite series. A _partial sum_ of an infinite series is the summation of a _finite_ number of its first terms, which always exists as we have seen in {prf:ref}`Thm:SumsAndProducts:Sum`.

::::{prf:definition}
:label: Def:Series:PartialSum

Given a series $\displaystyle\sum_{n=p}^{\infty}a_n$, we define the $N$th **partial sum** of this series as

$$
s_N=\displaystyle\sum_{n=p}^{N}a_n=a_p+a_{p+1}+a_{p+2}+\cdots+a_{N}.
$$

Here we assume that $N\geq p$.
::::

In other words, the $N$th partial sum of a series is the sum of the first $N-p+1$ terms of the series.

::::::{note}
For $\displaystyle\sum_{n=1}^{\infty}a_n$ the $N$th partial sum $s_N$ is the sum of the first $N$ terms. However, we call $s_N$ still the $N$th partial sum of the series even when the series $\displaystyle\sum a_n$ does not start at $n=1$. So, for instance, if $\displaystyle\sum_{n=2}^{\infty}\frac{\ln(n)}{n}$ then $s_N=\displaystyle\sum_{n=2}^N\frac{\ln(n)}{n}$ is the sum of the first $N-1$ terms and if $\displaystyle\sum_{n=0}^{\infty}\frac{1}{n^2+1}$ then $s_N=\displaystyle\sum_{n=0}^N\frac{1}{n^2+1}$ is the sum of the first $N+1$ terms.
::::::

::::{prf:definition}
:label: Def:Series:SummationIndex

The letter $n$ in the notation $\displaystyle\sum_{n=p}^{\infty}a_n$ is called the **index of summation**.
::::

Because the index of summation is just a dummy variable, we can replace it by any other letter. For example, we can write $\displaystyle\sum_{m=p}^{\infty}a_m$ instead of $\displaystyle\sum_{n=p}^{\infty}a_n$.

The starting index $p$ can be any integer, but it is often convenient to start with $p=1$ or $p=0$.

Sometimes we just write $\sum a_n$ when it is not relevant what the starting index is.

## Series and sums

Now we can formally define what a *series* is. 

::::{prf:definition}
:label: Def:Series:Series

Let $\left(a_n\right)_{n=p}^{\infty}$, with $p$ an integer, be a sequence and let $\left(s_N\right)_{N=p}^{\infty}$ denote the sequence of partial sums

$$
s_N=\sum_{n=p}^Na_n=a_p+a_{p+1}+a_{p+2}+\cdots+a_N,
$$

then 

$$
\sum_{n=p}^{\infty}a_n=\lim\limits_{N\to\infty}s_N.
$$

::::

Since the existence of the sum of an infinite series is equivalent to the existence of the limit of the sequence of partial sums, we can use all the tools that we have developed in {numref}`Chapter:Sequences` to determine whether the limit of the sequence of partial sums converges or diverges and to find the sum of a series if it exists. Because of this close link between infinite series and limits of sequences, we will reuse the terms _convergence_ and _divergence_ for series, which we have already used for sequences:

::::{prf:definition}
:label: Def:Series:ConvergenceSum

If the limit $\lim\limits_{N\to\infty}s_N=S$ exists, the series is called **convergent** and $S$ is called the **sum** of the series.

Otherwise, if the limit $\lim\limits_{N\to\infty}s_N$ does not exist, the series is called **divergent**
::::

For simplicity we will use the following notation:

::::{prf:notation}
:label: Not:Series:Sum

If a series $\displaystyle\sum_{n=p}^{\infty}a_n$ has the sum $S$, then we just write

$$
\sum_{n=p}^{\infty}a_n=S.
$$

::::

In {prf:ref}`Ex:Series:GeometricSeriesExample1` we showed that $\displaystyle\sum_{n=1}^{\infty}\frac{1}{2^n}=1$. Now we use the definition to obtain this result.

:::::{prf:example}
:label: Ex:Series:GeometricSeriesExample2

Note that we have

$$
\sum_{n=1}^{\infty}\frac{1}{2^n}=\sum_{n=1}^{\infty}\left(\frac{1}{2}\right)^n=\lim\limits_{N\to\infty}\sum_{n=1}^N\left(\frac{1}{2}\right)^n.
$$

Now we use {prf:ref}`Ex:SumsAndProducts:IntroductionFiniteGeometric` with $a=r=\frac{1}{2}$ to find that

$$
\sum_{n=1}^N\left(\frac{1}{2}\right)^n=\frac{\frac{1}{2}\left(1-\left(\frac{1}{2}\right)^N\right)}{1-\frac{1}{2}}=1-\frac{1}{2^N},\quad N=1,2,3,\ldots.
$$

Hence, we have

$$
\sum_{n=1}^{\infty}\frac{1}{2^n}=\lim\limits_{N\to\infty}\left(1-\frac{1}{2^N}\right)=1.
$$

:::::

:::::{prf:example}
:label: Ex:Series:AlternatingExample

$$
\sum_{n=0}^{\infty}(-1)^n=1+(-1)+1+(-1)+\cdots
$$

does not exist. The sequence of partial sums is $\left(1,0,1,0,1,0,\ldots\right)$ which has no limit.

:::::

:::::{prf:definition}
:label: Def:Series:GeneralTerms

If $\sum a_n$ is a series, then $a_n$ is called the **general term** of the series.

The sequence $\left(a_n\right)$ is called the sequence of general terms of the series.
:::::

The convergence of a series only depends on the so-called **tail** of the series, since a finite number of terms leads to a finite summation which always exists.

:::::{prf:theorem}
:label: Thm:Series:Tail

For all positive integers $p$ and $q$ we have

$$
\sum_{n=p}^{\infty}a_n\;\text{is convergent}\;\Longleftrightarrow\quad\sum_{n=q}^{\infty}a_n\;\text{is convergent}.
$$

:::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:Tail`
:class: tudproof

Without loss of generality we assume that $p\leq q$. The case $p=q$ is trivial, so let $p<q$. 

If $\displaystyle\sum_{n=q}^{\infty}a_n$ is convergent with sum $S$, then

\begin{align*}
\sum_{n=p}^{\infty}a_n&=a_p+a_{p+1}+a_{p+2}+\cdots+a_{q-1}+\sum_{n=q}^{\infty}a_n\\
&=a_p+a_{p+1}+a_{p+2}+\cdots+a_{q-1}+S.
\end{align*}

Note that $a_p+a_{p+1}+a_{p+2}+\cdots+a_{q-1}$ is a finite summation of $q-p$ terms. This implies that $\displaystyle\sum_{n=p}^{\infty}a_n$ is convergent as well, which proves the theorem.
::::::

## Convergence and divergence

A direct consequence of the definition of a convergent series is:

::::::{prf:theorem}
:label: Thm:Series:GeneralTerm
If the series $\displaystyle\sum a_n$ is convergent, then $\lim\limits_{n\to\infty}a_n=0$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:GeneralTerm`
:class: tudproof

Let $\left(s_n\right)$ be the sequence of partial sums of the series $\displaystyle\sum a_n$.

If $\displaystyle\sum a_n$ is convergent, then $\lim\limits_{n\to\infty}s_n=S$ exists. Then we have

$$
\lim_{n\to\infty}a_n=\lim_{n\to\infty}\left(s_n-s_{n-1}\right)=\lim_{n\to\infty}s_n-\lim_{n\to\infty}s_{n-1}=S-S=0.
$$

::::::

We want to stress the following:

::::::{warning}
The converse of {prf:ref}`Thm:Series:GeneralTerm` is not true: if $\lim\limits_{n\to\infty}a_n=0$ the series does not need to be convergent!
::::::

This is shown by the following example:

::::::{prf:example} The harmonic series
:label: Ex:Series:HarmonicSeries
Consider the **harmonic series** $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$.

First note that $\lim\limits_{n\to\infty}\dfrac{1}{n}=0$, so the general term of the series tends to zero.

Now consider the $N$th partial sum of the series:

$$
s_N=\displaystyle\sum_{n=1}^N\frac{1}{n}=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{N}.
$$

{numref}`Fig:Series:HarmonicSeries` gives a visualisation of the $N$th partial sum of the series.

```{figure} Images/harmonic.png
---
width: 50%
name: Fig:Series:HarmonicSeries
align: center
---
Visualisation of the $N$th partial sum of the harmonic series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$, which is given by the sum of the areas of the rectangles. The graph of $f(x)=\dfrac{1}{x}$ is also given for comparison.
```

:::{todo}
Replace {numref}`Fig:Series:HarmonicSeries` with an applet.
:::

Note that the top left corner of each rectangle aligns with the function $f(x)=\dfrac{1}{x}$. Because $f$ is a strictly decreasing function, the upper side of each rectangle is above the graph of $f$. This means that the area of each rectangle is greater than the area under the graph of $f$ between $n$ and $n+1$. Hence, we have

$$
s_N = \sum_{n=1}^N\frac{1}{n} > \sum_{n=1}^N\int_{n}^{n+1}\frac{1}{x}\,dx = \int_1^{N+1}\frac{1}{x}\,dx.
$$

We can easily evaluate the last integral:

$$
\int_1^{N+1}\frac{1}{x}\,dx=\bigg[\ln(x)\bigg]_1^{N+1}=\ln(N+1).
$$

This means that

$$
\lim_{N\to\infty}s_N > \lim_{N\to\infty}\ln(N+1) = \infty,
$$

and so the series is divergent by {prf:ref}`Def:Series:ConvergenceSum`.

This proves that the harmonic series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$ is divergent even though the terms tend to zero.
::::::

In the example we used an integral to test for convergence/divergence. This is commonly called the **integral test** for convergence/divergence and we will discuss it in more detail in {numref}`Sec:Series:PositiveSeries:IntegralTest`.

Although the contrary of {prf:ref}`Thm:Series:GeneralTerm` is not true, the theorem still gives us a useful test for divergence of series, by contraposition of the theorem. Contraposition of a statement of the form "If $P$, then $Q$." is the statement "if not $Q$, then not $P$".

Based on {prf:ref}`Thm:Series:GeneralTerm`, we have

$$
P : \text{"the series $\displaystyle\sum a_n$ is convergent"},
$$

which means that

$$
\text{not }P : \text{"the series $\displaystyle\sum a_n$ is not convergent" or "the series $\displaystyle\sum a_n$ is divergent"}.
$$

For the next part, the statement, $Q$, we have (in a longer form):

$$
Q : \text{"the limit $\lim\limits_{n\to\infty}a_n$ exists and equals $0$"},
$$

which means that

$$
\text{not }Q : \text{"the limit $\lim\limits_{n\to\infty}a_n$ does not exist or the limit $\lim\limits_{n\to\infty}a_n$ exists but does not equal $0$"}.
$$

Hence, contraposition of {prf:ref}`Thm:Series:GeneralTerm` gives us the following corollary:

::::::{prf:corollary} The test for divergence
:label: Thm:Series:GeneralTermCorollary

If $\lim\limits_{n\to\infty}a_n$ does not exist or if $\lim\limits_{n\to\infty}a_n\ne 0$, then the series $\sum a_n$ is divergent.
::::::

::::::{warning}
Although {prf:ref}`Thm:Series:GeneralTermCorollary` is usually called **the test for divergence**, we emphasise that a series might be divergent even when $\lim\limits_{n\to\infty}a_n=0$. Think about the harmonic series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$.
::::::

::::{prf:example}
:label: Ex:Series:DivergenceTest1

The general term of the series $\displaystyle\sum_{n=1}^{\infty}\frac{2n}{3n+1}$ satisfies 

$$
\lim_{n\to\infty}\frac{2n}{3n+1}=\frac{2}{3}\neq0,
$$

so by {prf:ref}`the test for divergence <Thm:Series:GeneralTermCorollary>`, the series $\displaystyle\sum_{n=1}^{\infty}\frac{2n}{3n+1}$ is divergent.

::::

::::{prf:example}
:label: Ex:Series:DivergenceTest2

The series $\displaystyle\sum_{n=1}^{\infty}\sin(n)$ is divergent, since $\displaystyle\lim_{n\to\infty}\sin(n)$ does not exist.
::::

::::{question}
:type: short-answer
:variant: gaps
:admonition:
:class: question
:showanswer:

Fill in the gaps:

---
M[\frac{1}{2}\pi]
TI[divergent]
^^^
? Consider the sequence $\left(\arctan(n)\right)_{n=1}^{\infty}$.

Then we have $\displaystyle\lim\limits_{n\to\infty}\arctan(n)=${gap}.

So, by the test for divergence, 

the series $\displaystyle\sum_{n=1}^{\infty}\arctan(n)$ is {gap}.
---
::::

The test for divergence only gives us a test for divergence, but it does not give us a test for convergence. In most cases one has to resort to other tests for convergence/divergence, which we will discuss in the next sections. For several special types of series, however, we can already determine whether they are convergent or divergent and find their sum if they are convergent, which we will treat in {numref}`Sec:Series:SpecialSeries`.

## Computation rules for series

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
\sum_{n=p+t}^{\infty}a_{n-t} = A.
$$

::::

The last property in {prf:ref}`Thm:Series:CalculatingSums` shows that the starting index of a series varies if we make a shift in the index of summation.

We can also multiply two series, which leads to another series called the **Cauchy product** of the two series. The coefficients of this series can be written in terms of the coefficients of the two original series as is given by the following theorem.

::::::{prf:theorem} Cauchy product
:label: Thm:Series:CauchyProduct
Let $\displaystyle\sum_{n=0}^{\infty}a_n$ and $\displaystyle\sum_{n=0}^{\infty}b_n$ be two series, then

$$
\left(\sum_{n=0}^{\infty}a_n\right)\left(\sum_{n=0}^{\infty}b_n\right)=\sum_{n=0}^{\infty}c_n\quad\text{with}\quad c_n=\sum_{k=0}^na_kb_{n-k}.
$$

::::::

The Cauchy product is named after the French mathematician [Augustin-Louis Cauchy (1789-1857)](https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy). The Cauchy product is sometimes called the **discrete convolution** of the two series.

:::{warning}
Even when both series are convergent, it is not guaranteed that the Cauchy product also converges.
:::

In the next subsection we will distinguish between absolute and conditional convergence. It can be shown that if at least one of the two series is absolutely convergent and the other one converges, then the product series converges as well. Only when both series are conditionally convergent, it might be possible that the product series diverges. See: {prf:ref}`Ex:Series:CauchyProductExample`.

## Absolute and conditional convergence

Sometimes it is useful to consider a new series which has as terms the absolute values of the terms of the original series, which is called the **absolute value series** of the original series. If such an absolute value series converges or diverges, then we can also deduce something about the convergence/divergence of the original series.

We start with a new definition:

::::::{prf:definition} Absolute convergence
:label: Def:Series:AbsoluteConvergence
A series $\displaystyle\sum_{n=p}^{\infty} a_n$ is called **absolutely convergent** if the series of absolute values $\displaystyle\sum_{n=p}^{\infty}|a_n|$ is convergent.
::::::

One of the most important results about absolute convergence is that if a series is absolutely convergent, then it is convergent:

::::::{prf:theorem}
:label: Thm:Series:AbsoluteConvergence
If a series $\displaystyle\sum a_n$ is absolutely convergent, then it is convergent.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:AbsoluteConvergence`
:class: tudproof, dropdown

Without loss of generality, we assume that the series $\displaystyle\sum a_n$ starts at $n=1$.[^changeIndex]

[^changeIndex]: If the series $\displaystyle\sum a_n$ starts at $n=p$ with $p\ne1$, then we can change the index of summation to make the series start at $n=1$.

First we define two new series $\displaystyle\sum a_n^+$ with $a_n^+=\max\{a_n,0\}$ for all $n$ and $\displaystyle\sum a_n^-$ with $a_n^-=\max\{-a_n,0\}$ for all $n$. Note that $a_n=a_n^+-a_n^-$ for all $n$ and $|a_n|=a_n^++a_n^-$ for all $n$.

Now consider the following three partials sums:

\begin{align*}
t_N = \sum_{n=1}^N |a_n| \\
p_N = \sum_{n=1}^N a_n^+ \\
q_N = \sum_{n=1}^N a_n^-.
\end{align*}

From the convergence of $\displaystyle\sum|a_n|$ we have that $\lim\limits_{N\to\infty}t_N=T$ exists. We also have that 

$$
t_{N+1}-t_N = \sum_{n=1}^{N+1}|a_n|-\sum_{n=1}^N|a_n| = |a_{N+1}|\geq0,
$$

so the sequence $\left(t_N\right)$ is non-decreasing with $T$ as an upper bound: $t_N\leq T$ for all $N$.

For the partial sum $p_N$ we have

$$
p_{N+1}-p_N = \sum_{n=1}^{N+1}a_n^+-\sum_{n=1}^Na_n^+ = a_{N+1}^+=\max\{a_{N+1},0\}\geq0,
$$

so the sequence $\left(p_N\right)$ is non-decreasing. Also,

$$
p_N = \sum_{n=1}^N a_n^+ \leq \sum_{n=1}^N (a_n^++a_n^-) = \sum_{n=1}^N |a_n| = t_N \leq T,
$$

which makes the sequence $\left(p_N\right)$ bounded from above. By {prf:ref}`Thm:Sequences:MonotonicBounded` the sequence $\left(p_N\right)$ is convergent, so $\lim\limits_{N\to\infty}p_N=P$ exists.

For the partial sum $q_N$ we have

$$
q_{N+1}-q_N = \sum_{n=1}^{N+1}a_n^- - \sum_{n=1}^Na_n^- = a_{N+1}^-=\max\{-a_{N+1},0\}\geq0,
$$

so the sequence $\left(q_N\right)$ is also non-decreasing. Also,

$$
q_N = \sum_{n=1}^N a_n^- \leq \sum_{n=1}^N (a_n^++a_n^-) = \sum_{n=1}^N |a_n| = t_N \leq T,
$$

so the sequence $\left(q_N\right)$ is also bounded from above. By {prf:ref}`Thm:Sequences:MonotonicBounded` the sequence $\left(q_N\right)$ is also convergent, so $\lim\limits_{N\to\infty}q_N=Q$ exists.

Now we can turn to the original series $\displaystyle\sum a_n$. The $n$th partial sum of this series is

\begin{align*}
s_N&=\sum_{n=1}^Na_n=\sum_{n=1}^N(a_n^+-a_n^-)\\
&=\sum_{n=1}^Na_n^+-\sum_{n=1}^Na_n^-\\
&=p_N-q_N.
\end{align*}

Because $\lim\limits_{N\to\infty}p_N=P$ and $\lim\limits_{N\to\infty}q_N=Q$, we have

$$
\lim_{N\to\infty}s_N = \lim_{N\to\infty}\left(p_N - q_N\right) = \lim_{N\to\infty}p_nN- \lim_{N\to\infty}q_N = P-Q.
$$

This shows that $\displaystyle\sum_{n=1}^{\infty}a_n$ is convergent, which proves the theorem.

:::

::::::{prf:example}
:label: Ex:Series:AbsoluteConvergence1

Consider the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}$. The absolute value series of this series is $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$.

In {numref}`Fig:Series:AbsoluteConvergence1` we have a visualisation of the $n$th partial sum $t_n$ of the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$.

```{figure} Images/integral.png
:name: Fig:Series:AbsoluteConvergence1

Visualisation of the $N$th partial sum $t_N$ of the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$, which is given by the sum of the areas of the rectangles. The graph of $f(x)=\dfrac{1}{x^2}$ is also given for comparison.
```

:::{todo}
Replace {numref}`Fig:Series:AbsoluteConvergence1` with an applet.
:::

Note that for the $N$th rectangle the top right corner aligns with the graph of $f(x)=\dfrac{1}{x^2}$ for $x\geq1$. This means that the area of the $N$th rectangle is less than the area under the graph of $f$ between $N-1$ and $N$ for $N\geq2$. Hence, we have

\begin{align*}
t_N &= \sum_{n=1}^N\frac{1}{n^2} \\
&= 1+\sum_{n=2}^N\frac{1}{n^2} \\
&< 1+\sum_{n=2}^N\int_{n-1}^{n}\frac{1}{x^2}\,dx \\
&= 1+\int_1^N\frac{1}{x^2}\,dx \\
&= 1+\bigg[-\frac{1}{x}\bigg]_1^N \\
&= 1+\left(-\frac{1}{N}+1\right) \\
&= 2-\frac{1}{N} \\
&< 2.
\end{align*}

This means that the sequence of partial sums $\left(t_N\right)$ is bounded from above by $2$. Also, we have

$$
t_{N+1}-t_N = \frac{1}{(N+1)^2} > 0,
$$

so the sequence $\left(t_N\right)$ is strictly increasing. By {prf:ref}`Thm:Sequences:MonotonicBounded` the sequence $\left(t_N\right)$ is convergent, so $\lim\limits_{n\to\infty}t_N=T$ exists.

This means that the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$ is convergent, so the original series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}$ is absolutely convergent by {prf:ref}`Def:Series:AbsoluteConvergence`, which means that $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}$ is also convergent by {prf:ref}`Thm:Series:AbsoluteConvergence`.

::::::

::::::{prf:example}
:label: Ex:Series:AbsoluteConvergence2
Now we consider the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$. The absolute value series of this series is $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$, which we have shown to be divergent in {prf:ref}`Ex:Series:HarmonicSeries`.

So the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$ is not absolutely convergent.

But, we can show something more about this series. Consider the $N$th partial sum of this series:

$$
s_N = \sum_{n=1}^N\frac{(-1)^{n-1}}{n}.
$$

For these partial sums we have the following property:

\begin{align*}
s_{2N+2}-s_{2N} &= \sum_{n=1}^{2N+2}\frac{(-1)^{n-1}}{n}-\sum_{n=1}^{2N}\frac{(-1)^{n-1}}{n} \\
&= \sum_{n=2N+1}^{2N+2}\frac{(-1)^{n-1}}{n} \\
&= \frac{(-1)^{2N}}{2N+1}+\frac{(-1)^{2N+1}}{2N+2} \\
&= \frac{1}{2N+1}-\frac{1}{2N+2} \\
&= \frac{1}{(2N+1)(2N+2)}.
\end{align*}

As this value is positive, the sequence $\left(s_{2N}\right)$ is strictly increasing. If we now consider only the partial sum $s_{2N}$ we find

\begin{align*}
s_{2N} &= \sum_{n=1}^{2N}\frac{(-1)^{n-1}}{n} \\
&= 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} - \frac{1}{7} + \cdots - \frac{1}{2n-2} + \frac{1}{2n-1} - \frac{1}{2N} \\
&= 1 - \left(\frac{1}{2} - \frac{1}{3}\right) - \left(\frac{1}{4} - \frac{1}{5}\right) - \left(\frac{1}{6} - \frac{1}{7}\right) \\
&{}\quad{}- \cdots - \left(\frac{1}{2N-2} - \frac{1}{2N-1}\right) - \frac{1}{2N} \\
&= 1 - \sum_{n=1}^{N-1}\left(\frac{1}{2n} - \frac{1}{2n+1}\right) - \frac{1}{2N} \\
&= 1 - \sum_{n=1}^{N-1}\frac{1}{(2n)(2n+1)} - \frac{1}{2N}.
\end{align*}

Because of the positivity of all terms in the sum $\displaystyle\sum_{n=1}^{N-1}\frac{1}{(2n)(2n+1)}$ and the term $\dfrac{1}{2N}$, we have found that $\{s_{2N}\}$ is bounded from above by $1$. Also, we have already found that $\{s_{2N}\}$ is strictly increasing. By {prf:ref}`Thm:Sequences:MonotonicBounded` the sequence $\left(s_{2N}\right)$ is convergent, so $\lim\limits_{n\to\infty}s_{2N}=S$ exists.

Now we turn to the sequence $\left(s_{2N+1}\right)$. We have

\begin{align*}
s_{2N+1} &= \sum_{n=1}^{2N+1}\frac{(-1)^{n-1}}{n} \\
&= \sum_{n=1}^{2N}\frac{(-1)^{n-1}}{n} + \frac{(-1)^{2N}}{2N+1} \\
&= s_{2N} + \frac{1}{2N+1}.
\end{align*}

But this means that

$$
\lim_{N\to\infty}s_{2N+1} = \lim_{N\to\infty}s_{2N} + \lim_{N\to\infty}\frac{1}{2N+1} = S + 0 = S.
$$

This tells us that all even partial sums *and* all odd partial sums converge to the same limit $S$, so all partial sums converge to $S$. Hence, the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$ is convergent.

::::::

{prf:ref}`Ex:Series:AbsoluteConvergence2` shows that a series can be convergent, but not absolutely convergent. In that case we say that the series is *conditionally convergent*:

::::::{prf:definition} Conditional convergence
:label: Def:Series:RelativeConvergence
A series $\displaystyle\sum a_n$ is called **conditionally convergent** if it is convergent, but not absolutely convergent.
::::::

::::::{note}
Later we will be able to show that $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}=\ln(2)$. See {prf:ref}`Ex:Series:PowerSeriesExample2`.
::::::

This concludes our treatment of absolute and conditional convergence. As you may have noticed, showing (absolute or conditional) convergence can be a lot of work. In {numref}`Sec:Series:SpecialSeries`, we will see some special types of series for which we can easily determine whether they are convergent or divergent and find their sum if they are convergent. For other series, we will need to use more advanced tests, which we will discuss in the sections after that.

## Grasple exercises

:::{todo}
Add Grasple exercises for {numref}`Chapter:Series:Introduction`.
:::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f54ec086-b25e-4f0c-8cb6-a5e8c036622f?id=65170
:label: Grasple:65170
:dropdown:
:description: True or false?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/22eb9936-cc95-47d8-a682-c4603f2c32fc?id=65173
:label: Grasple:65173
:dropdown:
:description: True or false?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9024f57a-707f-4b0a-a84c-6da8dfb9fcb2?id=79273
:label: Grasple:79273
:dropdown:
:description: Does the series converge?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e632e2c7-88fe-4bd1-adde-527eeacfeab9?id=79274
:label: Grasple:79274
:dropdown:
:description: Does the series converge?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ed622393-536c-4f30-ae34-6a2b62567aec?id=65041
:label: Grasple:65041
:dropdown:
:description: Does the series converge?

::::
