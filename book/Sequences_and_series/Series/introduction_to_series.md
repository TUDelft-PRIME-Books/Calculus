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


Without stating a formal proof, we will also state some important properties of the sum of a finite series:

::::{prf:theorem}
:label: Thm:Series:PropertiesFiniteSeries

If $\displaystyle\sum_{n=p}^qa_n=A$ and $\sum_{n=p}^qb_n=B$, then we have

$$
\sum_{n=p}^q(a_n+b_n)=A+B.
$$

If $\displaystyle\sum_{n=p}^qa_n=A$ and $c$ is a number, then we have

$$
\sum_{n=p}^qc a_n=cA.
$$

If $\displaystyle\sum_{n=p}^qa_n=A$ and $\displaystyle\sum_{n=q+1}^ra_n=B$, then we have

$$
\sum_{n=p}^ra_n=A+B.
$$

If $\displaystyle\sum_{n=p}^qa_n=A$ and $t$ is an integer, then we have

$$
\sum_{n=p-t}^{q-t} a_{n+t} = A.
$$

::::

::::::{prf:remark}
:label: Rem:Series:PropertiesFiniteSeries

In {prf:ref}`Thm:Series:PropertiesFiniteSeries` the first and third property are focussed on addition of series, the second property is focussed on multiplication of a series by a number, and the fourth property is focussed on the change of the index of summation.

Combining the second property with the first property, we can also find the following property: if $\displaystyle\sum_{n=p}^qa_n=A$ and $\displaystyle\sum_{n=p}^qb_n=B$, then we have

$$
\sum_{n=p}^q(a_n-b_n)=A-B,
$$

and

$$
\sum_{n=p}^q(ca_n+db_n)
$$

for any numbers $c$ and $d$.

Likewise, the third property can also be used for subtraction and the fourth property can also be used for a change of the index of summation in the opposite direction.
::::::

In {prf:ref}`Ex:Integration:IntroductionExamplesSum` we have seen the following result, which we summarise in a theorem:

::::{prf:theorem}
:label: Thm:Series:SumOfIntegers

The finite sequence of the first $n$ positive integers, $\{k\}_{k=1}^n$ and the related finite series $\displaystyle\sum_{k=1}^nk$ have the following sum:

$$
\sum_{k=1}^nk=\frac{1}{2}n(n+1)
$$

for all $n\in\{1,2,3,\ldots\}$.

::::

This theorem can also be proved using the principle of mathematical induction:

::::{admonition} Proof of {prf:ref}`Thm:Series:SumOfIntegers`
:class: tudproof, dropdown

For $n=1$ we obtain

$$
\sum_{k=1}^1k = 1
$$

and 

$$
\frac{1}{2}\cdot1\cdot2 = 1,
$$

which makes the statement true for $n=1$.

Now suppose that $\displaystyle\sum_{k=1}^nk=\frac{1}{2}n(n+1)$ holds for certain value of $n$. Then we have

\begin{align*}
\sum_{k=1}^{n+1}k &= \left(\sum_{k=1}^nk\right)+(n+1) \\
&= \frac{1}{2}n(n+1)+(n+1) \\
&= \frac12n^2+\frac12n+n+1 \\
&= \frac12n^2+\frac32n+1 \\
&= \frac12(n^2+3n+2) \\
&= \frac12(n+1)(n+2) \\
&= \frac12(n+1)((n+1)+1).
\end{align*}

Since this is exactly the formula with $n$ replaced by $n+1$, this proves the statement for all $n\in\{1,2,3,\ldots\}$.

::::

::::::{prf:example}
:label: Ex:Series:SumOfIntegersSquares
Using the previous theorem, we can show that

$$
\sum_{k=n^2+1}^{(n+1)^2}k=n^3+(n+1)^3
$$

for all $n\in\{1,2,3,\ldots\}$.

First, consider the series that starts at $1$ and ends at $(n+1)^2$, then we have

:::{math}
:label: Eq:Series:SumOfIntegersSquares1
\sum_{k=1}^{(n+1)^2}k=\frac{1}{2}(n+1)^2((n+1)^2+1) = \frac12(n^4+4n^3+7n^2+6n+2).
:::

Next, consider the series that starts at $1$ and ends at $n^2$, then we have

:::{math}
:label: Eq:Series:SumOfIntegersSquares2
\sum_{k=1}^{n^2}k=\frac{1}{2}n^2(n^2+1) = \frac12(n^4+n^2).
:::

If we subtract Equation {eq}`Eq:Series:SumOfIntegersSquares2` from Equation {eq}`Eq:Series:SumOfIntegersSquares1`, we obtain the sum

\begin{align*}
\sum_{k=n^2+1}^{(n+1)^2}k&=\sum_{k=1}^{(n+1)^2}k-\sum_{k=1}^{n^2}k\\
&=\frac12(n^4+4n^3+7n^2+6n+2)-\frac12(n^4+n^2)\\
&=\frac12(4n^3+6n^2+6n+2)\\
&=2n^3+3n^2+3n+1 \\
&=n^3+(n+1)^3.
\end{align*}

::::::

:::::{margin}
::::{figure} Images/telescope.png
:name: Fig:Series:Telescope

A pirate using a telescope.
::::
:::::

We now look at the sum of the first $n$ terms of the Fibonacci sequence to introduce the concept of a telescoping sum:

::::{prf:example}
:label: Ex:Series:FibonacciTelescoping

The Fibonacci sequence $\{F_n\}_{n=1}^{\infty}$ is defined by $F_{n+2}=F_n+F_{n+1}$ for $n=1,2,3,\ldots$ with $F_1=F_2=1$. Note that this also implies that $F_k=F_{k+2}-F_{k+1}$ for all $k\in\{1,2,3,\ldots\}$.

If we only consider the _finite_ sequence $\{F_k\}_{k=1}^n$, then we can find the sum of the related finite series $\displaystyle\sum_{k=1}^nF_k$ as follows:

:::{math}
:label: Eq:Series:FibonacciTelescoping
\begin{align*}
\sum_{k=1}^nF_k&=\sum_{k=1}^n\left(F_{k+2}-F_{k+1}\right)\\
&=F_{n+2}-\cancel{F_{n+1}}+\cancel{F_{n+1}}-\cancel{F_n}+\cdots+\cancel{F_4}-\cancel{F_3}+\cancel{F_3}-F_2\\
&=F_{n+2}-2.
\end{align*}
:::

So the sum of the first $n$ terms of the Fibonacci sequence equals $F_{n+2}-2$. Note that in the second line of Equation {eq}`Eq:Series:FibonacciTelescoping` we have _cancelled_ many terms because those terms appear twice with opposite signs.

::::

As you may have observed, we could _cancel_ many terms in the sum because those terms appear twice with opposite signs. Obviously, this is not a coincidence. This has lead to the following definition:

::::{prf:definition}
:label: Def:Series:TelescopingSum

A finite series $\displaystyle\sum_{k=m}^na_k$ is called a **telescoping sum** if there exists a sequence $\{b_k\}_{k=m}^{n+p}$ and an integer $p\geq1$ such that $a_k=b_{k}-b_{k+p}$ for all $k\in\{m,m+1,\ldots,n\}$.

The property that allows us to cancel many terms in a telescoping sum is called the **telescoping property**.
::::

In {prf:ref}`Def:Series:TelescopingSum` the number $p$ is often equal to $1$, but it can also be larger than $1$, as the next example shows:

::::{prf:example}
:label: Ex:Series:TelescopingSumExample

Consider the finite series $\displaystyle\sum_{k=2}^n\frac{1}{k^2-1}$.

Using a partial fraction decomposition, we can find for $k\in\{2,3,\ldots\}$ that

\begin{align*}
a_k &= \frac{1}{k^2-1} \\
&= \frac{1}{(k-1)(k+1)} \\
&= \frac{1}{2}\frac{1}{k-1}-\frac{1}{2}\frac{1}{k+1}.
\end{align*}

So if we take $p=2$ and $b_k=\frac{1}{2}\frac{1}{k-1}$ for $k\in\{2,3,\ldots,n+2\}$, then we have $a_k=b_{k}-b_{k+2}$ for all $k\in\{2,3,\ldots,n\}$, which means that $\displaystyle\sum_{k=2}^n\frac{1}{k^2-1}$ is a telescoping sum.

Using the telescoping property, we can also determine the sum of this telescoping sum as follows:

\begin{align*}
\sum_{k=2}^n\frac{1}{k^2-1}&=\sum_{k=2}^n\left(\frac{1}{2}\frac{1}{k-1}-\frac{1}{2}\frac{1}{k+1}\right) \\
&=\frac{1}{2}\sum_{k=2}^n\left(\frac{1}{k-1}-\frac{1}{k+1}\right) \\
&=\frac{1}{2}\left(\sum_{k=2}^n\frac{1}{k-1}-\sum_{k=2}^n\frac{1}{k+1}\right) \\
&=\frac{1}{2}\left(\sum_{k=0}^{n-2}\frac{1}{k+1}-\sum_{k=2}^n\frac{1}{k+1}\right) \\
&=\frac{1}{2}\left(\sum_{k=0}^{1}\frac{1}{k+1}-\sum_{k=n-1}^n\frac{1}{k+1}\right) \\
&=\frac{1}{2}\left(\left(1+\frac{1}{2}\right)-\left(\frac{1}{n}+\frac{1}{n+1}\right)\right) \\
&= \frac{3}{4}-\frac{1}{2}\frac{2n+1}{n^2+n}.
\end{align*}

Notice that in the fifth line we have used the change of the index of summation to make the two sums look more similar, which makes it easier to see that many terms will cancel. Also notice that in the sixth line we have used the telescoping property to cancel many terms and find the sum of the telescoping sum.

Even better, notice that the sum of the telescoping sum is the addition of the first two terms of the sequence $\left\{\frac{1}{2}\frac{1}{k+1}\right\}_{k=0}^{n+2}$ minus the addition of the last two terms of this sequence, which is a direct consequence of the telescoping property. We summarise this in the next theorem:

::::

::::{prf:theorem}
:label: Thm:Series:SumTelescopingSum
If $\displaystyle\sum_{k=m}^na_k$ is a telescoping sum with $a_k=b_{k}-b_{k+p}$ for all $k\in\{m,m+1,\ldots,n\}$ and some integer $p\geq1$, then we have

$$
\sum_{k=m}^na_k=\sum_{k=m}^{m+p-1}b_k-\sum_{k=n+1}^{n+p}b_k.
$$
::::

::::{admonition} Proof of {prf:ref}`Thm:Series:SumTelescopingSum`
:class: tudproof, dropdown

Using the telescoping property we have

\begin{align*}
\sum_{k=m}^na_k&=\sum_{k=m}^n\left(b_{k}-b_{k+p}\right)\\
&=\sum_{k=m}^nb_k-\sum_{k=m}^nb_{k+p}\\
&=\sum_{k=m}^nb_k-\sum_{k=m+p}^{n+p}b_{k}\\
&=\left(\sum_{k=m}^{m+p-1}b_k+\sum_{k=m+p}^nb_k\right)-\left(\sum_{k=m+p}^{n}b_{k}+\sum_{k=n+1}^{n+p}b_{k}\right)\\
&=\sum_{k=m}^{m+p-1}b_k+\left(\sum_{k=m+p}^nb_k-\sum_{k=m+p}^{n}b_{k}\right)-\sum_{k=n+1}^{n+p}b_{k}\\
&= \sum_{k=m}^{m+p-1}b_k-\sum_{k=n+1}^{n+p}b_{k},
\end{align*}

which proves the theorem.

::::

Now, we consider the sum of a finite geometric series, which is a very important example of a finite series. We will also use this result in the next section to find the sum of an infinite geometric series.

::::::{prf:Example}
:label: Ex:Integration:IntroductionFiniteGeometric
Let $S=\displaystyle\sum_{k=1}^nar^{k-1}=a+ar+ar^2+\ldots+ar^{n-1}$ with $r\neq1$ and $n$ a positive integer. 

Then we have:

\begin{align*}
S&=a&+ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&\\
rS&=&ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&+ar^n.
\end{align*}
Subtracting the two equations we obtain

$$
(1-r)S=a-ar^n=a(1-r^n)\quad\Longrightarrow\quad S=\frac{a(1-r^n)}{1-r},\quad r\neq1.
$$

::::::

With this we end our treatment of finite series.

## Convergence and divergence of infinite series

We will now turn our attention to infinite series, or by {prf:ref}`Rem:Series:FiniteSeries` just series, which is more complicated and requires some extra definitions to handle the summation of an infinite number of terms.

::::{prf:definition}
:label: Def:Series:PartialSum

Given a series $\displaystyle\sum_{n=p}^{\infty}a_n$, we define the $n$th **partial sum** of this series as

$$
s_n=\displaystyle\sum_{k=p}^{n+p-1}a_k=a_p+a_{p+1}+a_{p+2}+\cdots+a_{n+p-1}.
$$
::::

In other words, the $n$th partial sum of a series is the sum of the first $n$ terms of the series.

Using these  partial sums we can now look at the infinite series:

\begin{align*}
\sum_{n=p}^{\infty}a_n &= \lim_{n\to\infty}\sum_{k=p}^{n+p-1}a_k \\
&= \lim_{n\to\infty}s_n.
\end{align*}

So if $\lim\limits_{n\to\infty}s_n$ would exist, then we the sum of the infinite series $\displaystyle\sum_{n=p}^{\infty}a_n$ would be equal to this limit. If $\lim\limits_{n\to\infty}s_n$ does not exist, then we cannot determine the sum of the infinite series $\displaystyle\sum_{n=p}^{\infty}a_n$. This is summarised in the next theorem:

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

::::::{prf:example} The harmonic series
:label: Ex:Series:HarmonicSeries
Consider the  **harmonic series** $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$.

First note that $\lim\limits_{n\to\infty}\frac{1}{n}=0$, so the general term of the harmonic series tends to zero.

Now consider the $n$th partial sum of the harmonic series:

$$
s_n=\displaystyle\sum_{k=1}^n\frac{1}{k}=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}.
$$

Figure {numref}`Fig:Series:HarmonicSeries` gives a visualisation of the $n$th partial sum of the harmonic series.

```{figure} Images/harmonic.png
---
width: 50%
name: Fig:Series:HarmonicSeries
align: center
---
Visualisation of the $n$th partial sum of the harmonic series, which is given by the sum of the areas of the rectangles. The graph of $f(x)=\frac{1}{x}$ is also given for comparison.
```

:::{todo}
Replace {numref}`Fig:Series:HarmonicSeries` with an applet.
:::

Note that the top left corner of each rectangle aligns with the function $f(x)=\frac{1}{x}$. Because $f$ is a decreasing function, the upper right corner of each rectangle is above the graph of $f$. This means that the area of each rectangle is greater than the area under the graph of $f$ between $n$ and $n+1$. Hence, we have

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

and so the harmonic series is divergent by {prf:ref}`Def:Series:ConvergenceSum`.

This proves that the harmonic series is divergent.
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

The geometric series $\displaystyle\sum_{n=0}^{\infty}\left(\frac{3}{2}\right)^n$ is divergent, since, by the _test for divergence_, $\displaystyle\lim_{n\to\infty}\left(\frac{3}{2}\right)^n$ does not exist.

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

The test for divergence only gives us a test for divergence, but it does not give us a test for convergence. In most cases one has to resort to other tests for convergence/divergence, which we will discuss in the next sections. For three special types of series, however, we can already determine whether they are convergent or divergent and find their sum if they are convergent, which we will treat in {numref}`Sec:Series:SpecialSeries`.

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

```{figure} Images/temp_2series.png
:name: Fig:Series:AbsoluteConvergence1

Visualisation of the $n$th partial sum $t_n$ of the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$, which is given by the sum of the areas of the rectangles. The graph of $f(x)=\frac{1}{(x-1)^2}$ is also given for comparison.
```

:::{todo}
Replace {numref}`Fig:Series:AbsoluteConvergence1` with an applet.
:::

Note that for the $n$th rectangle the top right corner aligns with the graph of $f(x)=\frac{1}{(x-1)^2}$ for $x\geq1$. This means that the area of each rectangle is less than the area under the graph of $f$ between $n$ and $n+1$. Hence, we have

\begin{align*}
t_n &= \sum_{k=1}^n\frac{1}{k^2} \\
&= 1+\sum_{k=2}^n\frac{1}{k^2} \\
&< 1+\sum_{k=2}^n\int_{k}^{k+1}\frac{1}{(x-1)^2}\,dx \\
&= 1+\int_2^{n+1}\frac{1}{(x-1)^2}\,dx \\
&= 1+\bigg[-\frac{1}{x-1}\bigg]_2^{n+1} \\
&= 2-\frac{1}{n} < 2.
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
Now we consider the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$. The absolute value series of this series is $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$, which is the harmonic series, which we have shown to be divergent in {prf:ref}`Ex:Series:HarmonicSeries`.

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
Add Grasple exercises.
:::

## Exercises

### Finite series

::::{exercise}
:label: Exc:Series:IntroductionInduction1
Show that $\displaystyle\sum_{k=1}^nk^2=\frac{1}{6}n(n+1)(2n+1)$ for all $n\in\{1,2,3,\ldots\}$.
::::

:::{admonition} Solution of {numref}`Exc:Series:IntroductionInduction1`
:class: solution, dropdown
For $n=1$ this reads: $1=\frac{1}{6}\cdot1\cdot2\cdot3$, which is true. 

Suppose that $\displaystyle\sum_{k=1}^nk^2=\frac{1}{6}n(n+1)(2n+1)$ holds for certain value of $n$. Then we have

\begin{align*}
\sum_{k=1}^{n+1}k^2&=\sum_{k=1}^nk^2+(n+1)^2=\frac{1}{6}n(n+1)(2n+1)+(n+1)^2\\
&=\frac{1}{6}(n+1)\left\{n(2n+1)+6(n+1)\right\}\\
&=\frac{1}{6}(n+1)(2n^2+7n+6)=\frac{1}{6}(n+1)(n+2)(2n+3).
\end{align*}
Since this is exactly the formula with $n$ replaced by $n+1$, this proves the statement for all $n\in\{1,2,3,\ldots\}$.
:::

::::{exercise}
:label: Exc:Series:IntroductionInduction2
Show that $\displaystyle\sum_{k=1}^nk^3=\left(\sum_{k=1}^nk\right)^2=\frac{1}{4}n^2(n+1)^2$ for all $n\in\{1,2,3,\ldots\}$.
::::

:::{admonition} Solution of {numref}`Exc:Series:IntroductionInduction2`
:class: solution, dropdown
For $n=1$ this reads: $1=\frac{1}{4}\cdot1^2\cdot2^2$, which is true. 

Suppose that $\displaystyle\sum_{k=1}^nk^3=\frac{1}{4}n^2(n+1)^2$ holds for certain value of $n$. Then we have

\begin{align*}
\sum_{k=1}^{n+1}k^3&=\sum_{k=1}^nk^3+(n+1)^3=\frac{1}{4}n^2(n+1)^2+(n+1)^3\\
&=\frac{1}{4}(n+1)^2\left\{n^2+4(n+1)\right\}\\
&=\frac{1}{4}(n+1)^2(n^2+4n+4)=\frac{1}{4}(n+1)^2(n+2)^2.
\end{align*}
Since this is exactly the formula with $n$ replaced by $n+1$, this proves the statement for all $n\in\{1,2,3,\ldots\}$.
:::

::::{exercise}
:label: Exc:Series:LucasTelescoping
The Lucas sequence $\{L_n\}_{n=1}^{\infty}$ is defined by $L_{n+2}=L_n+L_{n+1}$ for $n=1,2,3,\ldots$ with $L_1=1$ and $L_2=3$.

Simplify $\displaystyle\sum_{k=1}^nL_k$.
::::

:::{admonition} Solution of {numref}`Exc:Series:LucasTelescoping`
:class: solution, dropdown
Again we use the *telescoping property* to find

\begin{align*}
\sum_{k=1}^nL_k&=\sum_{n=1}^n\left(L_{k+2}-L_{k+1}\right)\\
&=L_{n+2}-\cancel{L_{n+1}}+\cancel{L_{n+1}}-\cancel{L_n}+\ldots+\cancel{L_4}-\cancel{L_3}+\cancel{L_3}-L_2\\
&=L_{n+2}-3.
\end{align*}
:::

::::{exercise}
:label: Exc:Series:TelescopingExercise
Use the facts that $n^4+n^2+1=n^4+2n^2+1-n^2=(n^2+1)^2-n^2$ and $2n=n^2+1+n-(n^2+1-n)$ to find the sum of

$$
\sum_{n=1}^{100}\frac{n}{n^4+n^2+1}.
$$

::::

:::{admonition} Solution of {numref}`Exc:Series:TelescopingExercise`
:class: solution, dropdown
Using $n^4+n^2+1=(n^2+1)^2-n^2=(n^2+1+n)(n^2+1-n)$ and $2n=n^2+1+n-(n^2+1-n)$ we obtain

\begin{align*}
\frac{n}{n^4+n^2+1}&=\frac{1}{2}\frac{n^2+1+n-(n^2+1-n)}{(n^2+1+n)(n^2+1-n)} \\
&=\frac{1}{2}\left(\frac{1}{n^2+1-n}-\frac{1}{n^2+1+n}\right).
\end{align*}

In order to see that this is a telescoping sum, let $c_n=n^2+1-n$, then

$$
c_{n+1}=(n+1)^2+1-(n+1)=n^2+2n+1+1-n-1=n^2+1+n.
$$

So if we set $b_n=\dfrac12\dfrac{1}{c_n}$, then we have $a_n=b_n-b_{n+1}$ for all $n\in\{1,2,3,\ldots\}$, then we have a telescoping sum.

Hence, we have by {prf:ref}`Thm:Series:SumTelescopingSum` that

\begin{align*}
\sum_{n=1}^{100}\left(\frac{1}{n^2+1-n}-\frac{1}{n^2+1+n}\right) &= b_1-b_{101} \\
&= \frac12\frac{1}{c_1}-\frac12\frac{1}{c_{101}} \\
&= \frac12\frac{1}{1^2+1-1}-\frac12\frac{1}{101^2+1-101} \\
&= \frac12\frac11-\frac12\frac{1}{10101} \\
&= \frac12-\frac{1}{20202} \\
&= \frac{10101}{20202}-\frac{1}{20202} \\
&= \frac{10100}{20202} \\
&= \frac{5050}{10101} \\
&= 0.\overline{499950}.
\end{align*}

:::

### Infinite series

::::{exercise}
:label: Exc:Series:DecimalsOne
Is the number $r=0.\overline{9}=0.99999\ldots$ smaller than $1$?

Find an easier expression for $r$.
::::

:::{admonition} Solution of {numref}`Exc:Series:DecimalsOne`
:class: solution, dropdown
Solution 1. Write $r=0.\overline{9}$ as a geometric series:

$$
r=0.\overline{9}=\sum_{n=1}^{\infty}\frac{9}{10^n}.
$$

This is a geometric series with common ratio $\dfrac{1}{10}$. Therefore, it is convergent and

$$
r=0.\overline{9}=\frac{\dfrac{9}{10}}{1-\dfrac{1}{10}}=\frac{9}{10-1}=\frac{9}{9}=1.
$$

Solution 2. If $r=0.\overline{9}$, then we have

$$
10r=9.\overline{9}=9+0.\overline{9}=9+r\quad\Longrightarrow\quad9r=9\quad\Longleftrightarrow\quad r=1.
$$

So, the notation $0.\overline{9}=0.99999\ldots$ is just a clumsy way to represent the number $1$.
:::

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

