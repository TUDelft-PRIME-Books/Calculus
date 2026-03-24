(Chapter:Series:Introduction)=
# Series and their types

In this section we cover (see note in section convergence of series):

- Series and partial sums
- Convergence of sum(a_n+b_n)
- Geometric series
- Telescoping series
- Harmonic series and p-series (i.e. sum 1/n^p)
- Convergence and divergence
- Absolute and conditional convergence

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

A finite series $\displaystyle\sum_{k=m}^na_k$ is called a **telescoping sum** if there exists a sequence $\{b_k\}_{k=m}^{n+p}$ and an integer $p\geq1$ such that $a_k=b_{k+p}-b_k$ for all $k\in\{m,m+1,\ldots,n\}$.

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

So if we take $p=2$ and $b_k=-\frac{1}{2}\frac{1}{k-1}$ for $k\in\{2,3,\ldots,n+2\}$, then we have $a_k=b_{k+2}-b_k$ for all $k\in\{2,3,\ldots,n\}$, which means that $\displaystyle\sum_{k=2}^n\frac{1}{k^2-1}$ is a telescoping sum.

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
::::

## Old stuff


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
\sum_{n=1}^{100}\frac{n}{n^4+n^2+1}&=\frac{1}{2}\sum_{n=1}^{100}\frac{n^2+1+n-(n^2+1-n)}{(n^2+1+n)(n^2+1-n)}\\
&=\frac{1}{2}\sum_{n=1}^{100}\left(\frac{1}{n^2+1-n}-\frac{1}{n^2+1+n}\right).
\end{align*}
In order to see that this is a telescoping sum, let $f(n)=n^2+1-n$, then $f(n+1)=(n+1)^2+1-(n+1)=n^2+2n+1+1-n-1=n^2+1+n$. Hence, we have

\begin{align*}
&\sum_{n=1}^{100}\left(\frac{1}{n^2+1-n}-\frac{1}{n^2+1+n}\right)=\sum_{n=1}^{100}\left(\frac{1}{f(n)}-\frac{1}{f(n+1)}\right)\\
&{}=\frac{1}{f(1)}-\cancel{\frac{1}{f(2)}}+\cancel{\frac{1}{f(2)}}-\cancel{\frac{1}{f(3)}}+\cdots+\cancel{\frac{1}{f(100)}}-\frac{1}{f(101)}\\
&=\frac{1}{f(1)}-\frac{1}{f(101)}.
\end{align*}
We conclude that

\begin{align*}
\sum_{n=1}^{100}\frac{n}{n^4+n^2+1}&=\frac{1}{2}\left(\frac{1}{f(1)}-\frac{1}{f(101)}\right)=\frac{1}{2}\left(1-\frac{1}{100^2+1+100}\right)\\
&=\frac{1}{2}\cdot\frac{10101-1}{10101}=\frac{5050}{10101}.
\end{align*}
:::






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


## Introduction

If we add the terms of a finite sum, the order of the terms is not relevant, since by the associative law for addition we have

$$
(a_1+a_2)+a_3=a_1+(a_2+a_3).
$$

It turns out that in certain situations, this is no longer true if we try to add an infinite number of terms. So, in that case we use the convention that

$$
a_1+a_2+a_3+a_4+a_5+\cdots\quad\text{means}\quad \cdots((((a_1+a_2)+a_3)+a_4)+a_5)+\cdots.
$$

::::::{prf:definition}
:label: Def:Series:Definition
Let $\{a_n\}_{n=1}^{\infty}$ be a sequence of real numbers $a_1,a_2,a_3,\ldots$. If we try to add these numbers we get an expression of the form $a_1+a_2+a_3+\cdots$, which is called an **infinite series** or just **series** and is denoted by $\displaystyle\sum_{n=1}^{\infty}a_n$ or just by $\displaystyle\sum a_n$.
::::::

Does this make sense? What does it mean?

Given a series $\displaystyle\sum_{n=1}^{\infty}a_n=a_1+a_2+a_3+\cdots$, let $s_n$ denote its $n$th **partial sum**

$$
s_n=\displaystyle\sum_{k=1}^na_k=a_1+a_2+a_3+\cdots+a_n.
$$

These partial sums form a sequence $\{s_n\}_{n=1}^{\infty}$. Now we consider $\lim\limits_{n\to\infty}s_n$.

::::::{prf:definition}
:label: Def:Series:ConvergenceSum
If the limit $\lim\limits_{n\to\infty}s_n=s$ exists, then the series $\displaystyle\sum a_n$ is called **convergent** and we write $\displaystyle\sum_{n=1}^{\infty}a_n=s$ or $a_1+a_2+a_3+\cdots=s$.

The number $s$ is called the **sum** of the series. 

If the limit $\lim\limits_{n\to\infty}s_n$ does not exist, then the series is called **divergent**.
::::::

::::::{prf:example} 

```{figure} Images/geometric.png
---
width: 50%
name: geometric series
align: center
---
A visual proof of $\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots=1$
```

$$
\sum_{n=1}^{\infty}\left(\frac{1}{2}\right)^n=\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots=1.
$$

::::::

::::::{prf:theorem} Geometric series
:label: Thm:Series:GeometricSeries
A **geometric series** $\displaystyle\sum_{n=1}^{\infty}ar^{n-1}=a+ar+ar^2+\cdots$ with $a\neq0$ and **common ratio** $r$ is convergent if $|r|<1$ and divergent if $|r|\geq1$.

For $|r|<1$ the sum of the series equals $\displaystyle\frac{a}{1-r}$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:GeometricSeries`
:class: tudproof, dropdown
For $r=1$ the series trivially diverges. For $r\neq1$ consider the $n$th partial sum

$$
s_n=\displaystyle\sum_{k=1}^nar^{k-1}=a+ar+ar^2+\cdots+ar^{n-1}.
$$

Then we have (compare with {prf:ref}`Ex:Integration:IntroductionFiniteGeometric`)

\begin{align*}
s_n&=a&+ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&\\
rs_n&=&ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&+ar^n.
\end{align*}
Subtracting the two equations we obtain

$$
(1-r)s_n=a-ar^n=a(1-r^n)\quad\Longrightarrow\quad s_n=\frac{a(1-r^n)}{1-r},\quad r\neq1.
$$

In {prf:ref}`Thm:Sequences:ConvergenceGeometric` we have seen that $\lim\limits_{n\to\infty}r^n$ only converges for $-1<r\leq1$ and 

$$
\lim\limits_{n\to\infty}r^n=\begin{cases}0, &-1<r<1\\1, &r=1.\end{cases}
$$

We conclude that the series $\displaystyle\sum_{n=1}^{\infty}ar^{n-1}$ converges for $|r|<1$ and diverges for $|r|\geq1$.

Furthermore, for $|r|<1$ the sum of the series equals $\displaystyle\frac{a}{1-r}$.
::::::

::::::{important}
The best way to remember the sum of a convergent geometric series is

$$
\text{sum}=\frac{\text{first term}}{1-\text{common ratio}}.
$$

::::::

::::::{note}
The special case $a=1$ reads

$$
\sum_{n=0}^{\infty}r^n=1+r+r^2+\cdots=\frac{1}{1-r},\quad|r|<1.
$$

In {numref}`Sec:Series:PowerSeries` on power series we will often make use of this result.
::::::

::::::{prf:example} 
1) $\displaystyle\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots=\sum_{n=1}^{\infty}\left(\frac{1}{2}\right)^n=\frac{\frac{1}{2}}{1-\frac{1}{2}}=1$.

2) $\displaystyle\frac{1}{5}-\frac{2}{25}+\frac{4}{125}-\frac{8}{625}+\cdots=\frac{1}{5}\sum_{n=0}^{\infty}\left(-\frac{2}{5}\right)^n=\frac{1}{5}\cdot\frac{1}{1+\frac{2}{5}}=\frac{1}{7}$.

3) $\displaystyle0.\overline{12}=0.1212121212\ldots=\sum_{n=1}^{\infty}\frac{12}{100^n}=\frac{\frac{12}{100}}{1-\frac{1}{100}}=\frac{12}{100-1}=\frac{4}{33}$.
::::::

In the last example $\overline{12}$ denotes that $12$ is repeated indefinitely. The number $p=0.\overline{12}$ is an example of a convergent geometric series. However, it is easier to note that

$$
100p=12.\overline{12}=12+0.\overline{12}=12+p\quad\Longrightarrow\quad99p=12\quad\Longleftrightarrow\quad p=\frac{12}{99}=\frac{4}{33}.
$$

::::::{prf:example} 
Express the number $0.\overline{135}=0.135135135\ldots$ as a quotient of integers.

Solution 1. The number can be written as a geometric series:

$$
0.\overline{135}=\sum_{n=1}^{\infty}\frac{135}{1000^n}.
$$
 
Then, the common ratio is $\dfrac{1}{1000}$ and therefore the geometric series converges and

$$
0.\overline{135}=\frac{\dfrac{135}{1000}}{1-\dfrac{1}{1000}}=\frac{135}{1000-1}=\frac{135}{999}=\frac{15}{111}=\frac{5}{37}.
$$

Solution 2. Let $q=0.\overline{135}$, then we have

\begin{align*}
&1000q=135.\overline{135}=135+0.\overline{135}=135+q\\
&\quad\Longrightarrow\quad999q=135\quad\Longleftrightarrow\quad q=\frac{135}{999}=\frac{15}{111}=\frac{5}{37}.
\end{align*}
::::::

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

## Telescoping series

In {eq}`Eq:Series:FibonacciTelescoping` we have seen the *telescoping property* of the (finite) sum of the first $n$ Fibonacci numbers. Sometimes this property can be used to find the sum of a **telescoping series**.

:::::{margin}
::::{figure} Images/telescope.png
:name: Fig:Series:Telescope

A pirate using a telescope.
::::
:::::

::::::{prf:example}
:label: Ex:Series:TelescopingSeries1
An example of a *telescoping series* is: $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n+1)}$.

Then the $n$th partial sum is: $s_n=\displaystyle\sum_{k=1}^n\frac{1}{k(k+1)}=\sum_{k=1}^n\left(\frac{1}{k}-\frac{1}{k+1}\right)$. Hence we have

$$
s_n=\frac{1}{1}-\cancel{\frac{1}{2}}+\cancel{\frac{1}{2}}-\cancel{\frac{1}{3}}+\cancel{\frac{1}{3}}-\cancel{\frac{1}{4}}+\cdots+\cancel{\frac{1}{n}}-\frac{1}{n+1}=1-\frac{1}{n+1}.
$$

Hence we have $\lim\limits_{n\to\infty}s_n=1$. This implies that the series is convergent and that 

$$
\sum_{n=1}^{\infty}\frac{1}{n(n+1)}=1.
$$

::::::

::::::{prf:example}
:label: Ex:Series:TelescopingSeries2
Another example is: $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n^2-1}$. Then we have

\begin{align*}
\sum_{k=2}^n\frac{1}{k^2-1}&=\sum_{k=2}^n\frac{1}{(k-1)(k+1)}=\frac{1}{2}\sum_{k=2}^n\left(\frac{1}{k-1}-\frac{1}{k+1}\right)\\
&=\frac{1}{2}\left(\frac{1}{1}-\cancel{\frac{1}{3}}+\frac{1}{2}-\cancel{\frac{1}{4}}+\cancel{\frac{1}{3}}-\cancel{\frac{1}{5}}+\cancel{\frac{1}{4}}-\cancel{\frac{1}{6}}+\right.\\
&{}\quad\quad\quad\quad\quad\left.{}\cdots+\cancel{\frac{1}{n-2}}-\frac{1}{n}+\cancel{\frac{1}{n-1}}-\frac{1}{n+1}\right)\\
&=\frac{1}{2}\left(1+\frac{1}{2}-\frac{1}{n}-\frac{1}{n+1}\right).
\end{align*}
This implies that the series converges and that 

$$
\sum_{n=2}^{\infty}\frac{1}{n^2-1}
=\lim\limits_{n\to\infty}\frac{1}{2}\left(\frac{3}{2}-\frac{1}{n}-\frac{1}{n+1}\right)=\frac{3}{4}.
$$

::::::

::::::{prf:example}
:label: Ex:Series:TelescopingSeries3
A third example is: $\displaystyle\sum_{n=2}^{\infty}\frac{1}{(n-1)(n+2)}$. Then we have

\begin{align*}
&\sum_{k=2}^n\frac{1}{(k-1)(k+2)}=\frac{1}{3}\sum_{k=2}^n\left(\frac{1}{k-1}-\frac{1}{k+2}\right)\\
&=\frac{1}{3}\left(\frac{1}{1}-\cancel{\frac{1}{4}}+\frac{1}{2}-\cancel{\frac{1}{5}}+\frac{1}{3}-\cancel{\frac{1}{6}}+\cancel{\frac{1}{4}}-\cancel{\frac{1}{7}}+\right.\\
&{}\quad\quad\quad\quad\quad\left.{}\cdots+\cancel{\frac{1}{n-3}}-\frac{1}{n}+\cancel{\frac{1}{n-2}}-\frac{1}{n+1}+\cancel{\frac{1}{n-1}}-\frac{1}{n+2}\right)\\
&=\frac{1}{3}\left(1+\frac{1}{2}+\frac{1}{3}-\frac{1}{n}-\frac{1}{n+1}-\frac{1}{n+2}\right).
\end{align*}
This implies that the series converges and that 

$$
\sum_{n=2}^{\infty}\frac{1}{(n-1)(n+2)}
=\lim\limits_{n\to\infty}\frac{1}{3}\left(\frac{11}{6}-\frac{1}{n}-\frac{1}{n+1}-\frac{1}{n+2}\right)=\frac{11}{18}.
$$

::::::

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

## A divergence test

If a series is convergent, its general term should tend to zero:

::::::{prf:theorem}
:label: Thm:Series:GeneralTerm
If the series $\displaystyle\sum a_n$ is convergent, then $\lim\limits_{n\to\infty}a_n=0$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:GeneralTerm`
:class: tudproof, dropdown
Let $\{s_n\}$ be the sequence of partial sums of the series $\displaystyle\sum a_n$.

If $\displaystyle\sum a_n$ is convergent, then $\lim\limits_{n\to\infty}s_n=s$ exists. Then we have

$$
\lim_{n\to\infty}a_n=\lim_{n\to\infty}\left(s_n-s_{n-1}\right)=\lim_{n\to\infty}s_n-\lim_{n\to\infty}s_{n-1}=s-s=0.
$$

::::::

::::::{prf:corollary}
:label: Thm:Series:GeneralTermCorollary
If $\lim\limits_{n\to\infty}a_n$ does not exist or if $\lim\limits_{n\to\infty}a_n\ne 0$, then the series $\sum a_n$ is divergent.
::::::

::::::{note}
{prf:ref}`Thm:Series:GeneralTermCorollary` is sometimes called "*the test for divergence*" which suggests that a series can only be divergent if the general term does not tend to zero. However, as we will see, this is not true!
::::::

::::::{prf:example}
:label: Ex:Series:DivergentSeries
1) The series $\displaystyle\sum_{n=1}^{\infty}\frac{2n}{3n+1}$ diverges, since $\displaystyle\lim_{n\to\infty}\frac{2n}{3n+1}=\frac{2}{3}\neq0$.

2) The series $\displaystyle\sum_{n=0}^{\infty}\left(\frac{3}{2}\right)^n$ diverges, since $\displaystyle\lim_{n\to\infty}\left(\frac{3}{2}\right)^n=\infty$ does not exist.

3) The series $\displaystyle\sum_{n=1}^{\infty}\sin(n)$ is divergent, since $\displaystyle\lim_{n\to\infty}\sin(n)$ does not exist.

4) The series $\displaystyle\sum_{n=1}^{\infty}\arctan(n)$ is divergent, since $\displaystyle\lim_{n\to\infty}\arctan(n)=\frac{1}{2}\pi\neq0$.

5) The series $\displaystyle\sum_{n=0}^{\infty}\cos(n\pi)$ is divergent, since $\displaystyle\lim_{n\to\infty}\cos(n\pi)$ does not exist.
::::::

::::::{warning}
The converse is not true: if $\lim\limits_{n\to\infty}a_n=0$ the series needs not to be convergent!
::::::

::::::{prf:example} The harmonic series
:label: Ex:Series:HarmonicSeries
The **harmonic series** $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$ is divergent.

Proof. Note that the terms of the *harmonic series* lie on the graph of $f(x)=\dfrac{1}{x}$:

```{figure} Images/harmonic.png
---
width: 50%
name: harmonic series
align: center
---
Proof of the divergence of the harmonic series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$
```

At each point $n$ we draw a rectangle with width $1$ and height $\dfrac{1}{n}$ to the right. Then, the upper side of each rectangle is above the graph of $f$ since $f$ is decreasing. Hence, we have

$$
\sum_{n=1}^{\infty}\frac{1}{n}=1+\frac{1}{2}+\frac{1}{3}+\cdots > \int_1^{\infty}\frac{1}{x}\,dx.
$$

Now we have: $\displaystyle\int_1^{\infty}\frac{1}{x}\,dx=\bigg[\ln(x)\bigg]_1^{\infty}=\infty$.

This proves that the harmonic series is divergent.
::::::

This proof uses the *integral test*, which will be treated in more details in the next section.

## Exercises

