(Sec:SumsAndProducts)=
# Finite sums and products

## Introduction
In this section we introduce the terminology and notation for finite sums and products which will be used in the rest of this book.

We assume that the reader is familiar with basic operations on rational numbers such as addition, multiplication, subtraction, and division.

These operations can be extended to rational real numbers ({numref}`Section:RealNumbers`) and complex numbers ({numref}`Ch:ComplexNumbersCartesian`).

This chapter is not meant to be an exhaustive introduction to summations and products, but rather a brief introduction to the terminology and notation that will be used in the rest of this book.

(Sec:SumsAndProducts:FiniteSequences)=
## Finite sequences

We start of with the definition of finite sequences and some relevant terminology.

::::::{prf:definition}
:label: Def:SumsAndProducts:Definition

A **finite sequence** is an ordered list of a finite set of numbers arranged in a specific order.

Each number in a sequence is called a **term** of the sequence.

The position of a term in a sequence is called the **index** of the term. The value of the index depends on the position of the term in the sequence and the choice of the **starting index**. The **ending index** is the index of the last term of the sequence.
::::::

Note that a sequence does not have to be defined by a pattern. Also, the starting index can be any integer, but it is often convenient to start with $1$ or $0$.

There are several ways to represent a sequence:

::::{prf:notation}
:label: Not:SumsAndProducts:SequenceNotation

The following are all different notations for the same _finite_ sequence:

- $\displaystyle\{a_n\}_{n=p}^{q}$.
- $\displaystyle a_p,a_{p+1},a_{p+2},\ldots,a_q$.

In this case $p$ is the starting index and $q$ is the ending index.

The choice for the letter $a$ is arbitrary, and we can use any letter to denote the terms of the sequence. The letter $n$ is often used to denote the index, but we can also use any other letter for the index.

Sometimes we just write $\{a_n\}$ to denote a sequence, so if we do, please be aware that the context is relevant in that case.

::::

In many cases the terms of an sequence are defined by an explicit formula for the general term in terms of the index:

::::{prf:definition}
:label: Def:SumsAndProducts:ExplicitFormula

An **explicit formula for a sequence** $\{a_n\}$ is a formula that gives the $n$th term $a_n$ of the sequence directly in terms of the index $n$ for all integers $n$ larger than the starting index.
::::

::::{prf:example}
:label: Ex:SumsAndProducts:PositiveIntegersExplicitFormula
The sequence of the first $q$ positive integers $1,2,3,4,5,\ldots,q$ can be defined by the explicit formula

$$
a_n=n\quad\text{for}\quad n=1,2,3,\ldots,q.
$$

Note that it makes sense to start with $n=1$ since the first term of the sequence is $1$. We could also have started with $n=0$ and define $a_n=n+1$ for $n=0,1,2,\ldots,q-1$, but this seems unnecessary.
::::

::::{prf:example}
:label: Ex:SumsAndProducts:ReciprocalPerfectSquaresExplicitFormula
The sequence of reciprocals of the first $q$ perfect squares $1,\frac{1}{4},\frac{1}{9},\frac{1}{16},\frac{1}{25},\ldots,\frac{1}{q^2}$ can be defined by the explicit formula

$$
a_n=\frac{1}{n^2}\quad\text{for}\quad n=1,2,3,\ldots,q.
$$
::::

::::{prf:example}
:label: Ex:SumsAndProducts:ExplicitFormula

Now consider the sequence $\{a_n\}_{n=1}^{q}$ with $a_n=\dfrac{n}{n^2+1}$ for $n=1,2,3,\ldots,q$.

This means, by substituting $n=1$ in the explicit formula, that the first term of the sequence is

$$
a_1=\frac{1}{2},
$$

by substituting $n=2$ that the second term of the sequence is

$$
a_2=\frac{2}{5},
$$

by substituting $n=3$ that the third term of the sequence is

$$
a_3=\frac{3}{10},
$$

and so on. We could write the sequence out as

$$
\{a_n\}_{n=1}^{q} = \frac{1}{2},\frac{2}{5},\frac{3}{10},\frac{4}{17},\frac{5}{26},\ldots,\frac{q}{q^2+1}
$$

::::

In other cases, or even the same, the terms of a sequence are not expressed with an explicit formula, but with a recursive formula:

::::{prf:definition}
:label: Def:SumsAndProducts:RecursiveFormula

A **recursive formula for a sequence** $\{a_n\}_{n=p}^{q}$ is a formula that gives the $n$th term $a_n$ of the sequence in terms of $k$ of the preceding terms for all integers $n>p+k$ in combination with formulas for the first $k$ terms $a_p,a_{p+1},\ldots,a_{p+k}$ of the sequence.

::::

::::{prf:example}
:label: Ex:SumsAndProducts:PositiveIntegersRecursiveFormula
The sequence of the first $q$ positive integers $1,2,3,4,5,\ldots,q$ can be defined by the recursive formula

$$
a_1=1,\quad a_{n+1}=a_n+1\quad\text{for}\quad n=1,2,3,\ldots.
$$

::::

::::{prf:example} 
:label: Ex:SumsAndProducts:RecursiveFormula

The sequence $\{a_n\}_{n=0}^{q}$ defined by $a_{n+1}=-\dfrac12a_n$ with $n=0,1,2,\ldots,q-1$ and $a_0=1$ can be written out as:

$$
\{a_n\}_{n=0}^{q} = 1,-\frac{1}{2},\frac{1}{4},-\frac{1}{8},\frac{1}{16},-\frac{1}{32},\ldots,\frac{(-1)^q}{2^q}.
$$

::::

(Sec:SumsAndProducts:Sums)=
## Finite sums

The summation symbol $\sum$ (the capital Greek letter sigma) is used to denote the addition of a finite sequence of numbers:

::::::{prf:definition}
:label: Def:Integration:IntroductionNotationSum

The **summation symbol** $\sum$ is used to denote the addition of a finite sequence.

If $\{a_n\}_{n=p}^{q}$ is a finite sequence, then $\displaystyle\sum_{n=p}^qa_n$ is an abbreviation for the addition of the numbers $a_p,a_{p+1},\ldots,a_q$, that is

$$
\sum_{n=p}^qa_n=a_p+a_{p+1}+\ldots+a_q.
$$

If the result of the addition exists, then we call that result the **finite sum** of the numbers $a_p,a_{p+1},\ldots,a_q$ and we write

$$
\sum_{n=p}^qa_n = S,
$$

for some number $S$.

The letter $n$ in the notation $\displaystyle\sum_{n=p}^qa_n$ is called the **index of multiplication**. The number $p$ is called the **starting index of multiplication** and the number $q$ is called the **ending index of multiplication**.

::::::

The next examples only consider the addition of some finite sequences, and also show the finite sum.

::::::{prf:Example}
:label: Ex:Integration:IntroductionExamplesSum

* $\displaystyle\sum_{p=3}^5p^2=3^2+4^2+5^2=9+16+25=50$;
* $\displaystyle\sum_{j=-1}^15^{j}=5^{-1}+5^0+5^{1}=\frac{1}{5}+1+5=\frac{31}{5}$;
* $\displaystyle\sum_{k=0}^32^k=2^0+2^1+2^2+2^3=1+2+4+8=15$.
::::::

::::::{prf:Example}
:label: Ex:Integration:IntroductionSumIntegers

We can show that the addition of the first $n$ positive integers equals $\frac{1}{2}n(n+1)$.

Let $S=\displaystyle\sum_{k=1}^nk$, then we have:

\begin{align*}
S&=1&+2&+\ldots&+(n-1)&+n\\
S&=n&+(n-1)&+\ldots&+2&+1.
\end{align*}

Adding the two expressions we obtain

$$
2S=\underbrace{(n+1)+(n+1)+\ldots+(n+1)+(n+1)}_{n\;\text{times}}.
$$

Hence we have $2S=n(n+1)$ and therefore $S=\frac{1}{2}n(n+1)$.
::::::

Without stating a formal proof, we will also state some important properties of the finite sums:

::::{prf:theorem}
:label: Thm:Series:PropertiesFiniteSeries

If $\displaystyle\sum_{n=p}^qa_n=A$ and $\displaystyle\sum_{n=p}^qb_n=B$, then we have

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

In {prf:ref}`Thm:Series:PropertiesFiniteSeries` the first and third property are focussed on addition of finite sums, the second property is focussed on multiplication of a finite sums by a number, and the fourth property is focussed on the change of the index of summation.

Combining the second property with the first property, we can also find the following properties if $\displaystyle\sum_{n=p}^qa_n=A$ and $\displaystyle\sum_{n=p}^qb_n=B$, then we have

$$
\sum_{n=p}^q(a_n-b_n)=A-B,
$$

and

$$
\sum_{n=p}^q(ca_n+db_n)=cA+dB
$$

for any numbers $c$ and $d$.

Likewise, the third property can also be used for subtraction and the fourth property can also be used for a change of the index of summation in the opposite direction.
::::::

In {prf:ref}`Ex:Integration:IntroductionExamplesSum` we have seen the following result, which we summarise in a theorem:

::::{prf:theorem}
:label: Thm:Series:SumOfIntegers

The finite sequence of the first $n$ positive integers, $\{k\}_{k=1}^n$ and the related finite sum $\displaystyle\sum_{k=1}^nk$ have the following sum:

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

:::::{prf:example}
:label: Ex:Series:SumOfSquares

The finite sequence of the first $n$ positive integers squared, $\{k^2\}_{k=1}^n$ and the related finite sum $\displaystyle\sum_{k=1}^nk^2$ have the following sum:

$$
\sum_{k=1}^nk^2=\frac{1}{6}n(n+1)(2n+1)
$$

for all $n\in\{1,2,3,\ldots\}$.

This can be proved using the principle of mathematical induction.

For $n=1$ we have

$$
\sum_{k=1}^1k^2 = 1\quad\text{and}\quad\frac{1}{6}\cdot1\cdot2\cdot3=1,
$$

so it holds for $n=1$. Now assume that $\displaystyle\sum_{k=1}^nk^2=\frac{1}{6}n(n+1)(2n+1)$ holds for certain value of $n=N$. Then we have for $n=N+1$ that

\begin{align*}
\sum_{k=1}^{N+1}k^2&=\left(\sum_{k=1}^Nk^2\right)+(N+1)^2 \\
&=\frac{1}{6}N(N+1)(2N+1)+(N+1)^2 \\
&=\frac{1}{6}N(N+1)(2N+1)+\frac{6}{6}(N+1)^2 \\
&=\frac{1}{6}(N(N+1)(2N+1)+6(N+1)^2) \\
&=\frac{1}{6}(2N^3+9N^2+13N+6) \\
&=\frac{1}{6}(N+1)(2N^2+7N+6) \\
&=\frac{1}{6}(N+1)(N+2)(2N+3) \\
&=\frac{1}{6}(N+1)((N+1)+1)(2(N+1)+1).
\end{align*}

Since this is exactly the formula with $n$ replaced by $N+1$, this proves the statement for all $n\in\{1,2,3,\ldots\}$.
:::::

::::::{prf:example}
:label: Ex:Series:SubSum
Using the previous theorem, we can show that

$$
\sum_{k=n^2+1}^{(n+1)^2}k=n^3+(n+1)^3
$$

for all $n\in\{1,2,3,\ldots\}$.

First, consider the finite sum that starts at $1$ and ends at $(n+1)^2$, then we have

:::{math}
:label: Eq:Series:SumOfIntegersSquares1
\sum_{k=1}^{(n+1)^2}k=\frac{1}{2}(n+1)^2((n+1)^2+1) = \frac12(n^4+4n^3+7n^2+6n+2).
:::

Next, consider the finite sum that starts at $1$ and ends at $n^2$, then we have

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

If we only consider the _finite_ sequence $\{F_k\}_{k=1}^n$, then we can find the sum of the related finite sum $\displaystyle\sum_{k=1}^nF_k$ as follows:

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

A finite sum $\displaystyle\sum_{k=m}^na_k$ is called a **telescoping sum** if there exists a sequence $\{b_k\}_{k=m}^{n+p}$ and an integer $p\geq1$ such that $a_k=b_{k}-b_{k+p}$ for all $k\in\{m,m+1,\ldots,n\}$.

The property that allows us to cancel many terms in a telescoping sum is called the **telescoping property**.
::::

In {prf:ref}`Def:Series:TelescopingSum` the number $p$ is often equal to $1$, but it can also be larger than $1$, as the next example shows:

::::{prf:example}
:label: Ex:Series:TelescopingSumExample

Consider the finite sum $\displaystyle\sum_{k=2}^n\frac{1}{k^2-1}$.

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

Now, we consider the sum of a finite geometric sum, which is a very important example of a finite sum. We will also use this result in {numref}`Sec:Series:GeometricSeries` to find the sum of a geometric series.

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

We finish this section with a very useful result that is often used:

:::{prf:theorem}
:label: Thm:SumsAndProducts:MagicRule

Assume $a$ and $b$ are real numbers and $n$ is an integer. Then we have

$$
(a-b)\sum_{k=1}^{n}a^{n-k}b^{k-1}=a^n-b^n.
$$

:::

:::{admonition} Proof of {prf:ref}`Thm:SumsAndProducts:MagicRule`
:class: tudproof, dropdown

We prove the theorem by induction on $n$.

For $n=1$ we have on the left-hand side that

$$
(a-b)\sum_{k=1}^{1}a^{1-k}b^{k-1} = (a-b)a^{1-1}b^{1-1} = a-b,
$$

and on the right-hand side that

$$
a^1-b^1 = a-b,
$$

so the statement holds for $n=1$.

Now assume that the statement holds for certain value of $n=N$, so

$$
(a-b)\sum_{k=1}^{N}a^{N-k}b^{k-1}=a^N-b^N.
$$

 then we have for $n=N+1$ that

\begin{align*}
(a-b)\sum_{k=1}^{N+1}a^{N+1-k}b^{k-1}&=(a-b)\left(\sum_{k=1}^{N}a^{N+1-k}b^{k-1}+a^{N+1-(N+1)}b^{(N+1)-1}\right) \\
&=(a-b)\left(a\sum_{k=1}^{N}a^{N-k}b^{k-1}+b^N\right) \\
&=(a-b)a\sum_{k=1}^{N}a^{N-k}b^{k-1}+(a-b)b^N \\
&=a(a-b)\sum_{k=1}^{N}a^{N-k}b^{k-1}+(a-b)b^N \\
&=a\left(a^N-b^N\right)+(a-b)b^N \\
&=a^{N+1}-ab^N+ab^N-b^{N+1} \\
&=a^{N+1}-b^{N+1}.
\end{align*}

This proves the statement for all $n\in\{1,2,3,\ldots\}$.

:::

With this we end our treatment of finite sums.

## Finite products

Similarly, the product symbol $\prod$ (capital Greek letter pi) is used to denote multiplication of a any number of numbers:

::::::{prf:Definition}
:label: Def:Integration:IntroductionNotationProduct

The **product symbol** $\prod$ is used to denote the multiplication of a set of ordered numbers.

If $\{a_n\}_{n=m}^{n}$ is a finite sequence, then $\displaystyle\prod_{k=m}^na_k$ is an abbreviation for the multiplication of the numbers $a_m,a_{m+1},\ldots,a_n$, that is

$$
\prod_{k=m}^na_k=a_m\cdot a_{m+1}\cdots a_n.
$$

If the result of the multiplication exists, then we call that result the **finite product** of the numbers $a_m,a_{m+1},\ldots,a_n$ and we write

$$
\prod_{k=m}^na_k = P,
$$

for some number $P$.

The letter $k$ in the notation $\displaystyle\prod_{k=m}^na_k$ is called the **index of multiplication**. The number $m$ is called the **starting index of multiplication** and the number $n$ is called the **ending index of multiplication**.

::::::

The next examples only consider the multiplication of a finite number of numbers.

::::::{prf:Example}
:label: Ex:Integration:IntroductionExamplesProduct

For $n\in\{1,2,3,\ldots\}$ we have
* $\displaystyle\prod_{p=1}^np=1\cdot2\cdot3\cdots(n-1)\cdot n$;
* $\displaystyle\prod_{j=1}^n\frac{j}{j+1}=\frac{1}{2}\cdot\frac{2}{3}\cdot\frac{3}{4}\cdots\frac{n-1}{n}\cdot\frac{n}{n+1}=\frac{1}{n+1}$;
* $\displaystyle\prod_{k=1}^n\frac{2k+1}{2k}=\frac{3}{2}\cdot\frac{5}{4}\cdot\frac{7}{6}\cdots\frac{2n-1}{2n-2}\cdot\frac{2n+1}{2n}=\frac{3\cdot5\cdot7\cdots(2n+1)}{2\cdot4\cdot6\cdots2n}$.
::::::

The first item in {prf:ref}`Ex:Integration:IntroductionExamplesProduct` often occurs in mathematics and therefore is given a special name:

::::{prf:definition}
:label: Def:SumsAndProducts:Factorial
The **factorial** of a positive integer $n$ is the finite product of the first $n$ positive integers, that is

$$
n!=\prod_{k=1}^nk=1\cdot2\cdot3\cdots(n-1)\cdot n.
$$

By convention, we also define $0!=1$.
::::

Without stating a formal proof, we will also state some important properties of the finite products:

::::{prf:theorem}
:label: Thm:Series:PropertiesFiniteProducts

If $\displaystyle\prod_{n=p}^qa_n=A$ and $\displaystyle\prod_{n=p}^qb_n=B$, then we have

$$
\prod_{n=p}^q(a_nb_n)=AB.
$$

If $\displaystyle\prod_{n=p}^qa_n=A$ and $c$ is a number, then we have

$$
\prod_{n=p}^qc a_n=c^{q-p+1}A.
$$

If $\displaystyle\prod_{n=p}^qa_n=A$ and $\displaystyle\prod_{n=q+1}^ra_n=B$, then we have

$$
\prod_{n=p}^ra_n=AB.
$$

If $\displaystyle\prod_{n=p}^qa_n=A$ and $t$ is an integer, then we have

$$
\prod_{n=p-t}^{q-t} a_{n+t} = A.
$$

::::

::::::{prf:remark}
:label: Rem:Series:PropertiesFiniteProducts

In {prf:ref}`Thm:Series:PropertiesFiniteProducts` the first and third property are focussed on addition of finite products, the second property is focussed on multiplication of a finite products by a number, and the fourth property is focussed on the change of the index of multiplication.

Combining the second property with the first property, we can also find the following properties if $\displaystyle\prod_{n=p}^qa_n=A$ and $\displaystyle\prod_{n=p}^qb_n=B$, with $B\neq0$ and $b_n\neq0$ for all $n\in\{p,p+1,\ldots,q\}$, then we have

$$
\prod_{n=p}^q\frac{a_n}{b_n}=\frac{A}{B},
$$

and

$$
\prod_{n=p}^q\frac{ca_n}{db_n}=\frac{c^{q-p+1}A}{d^{q-p+1}B}
$$

for any numbers $c$ and $d\neq 0$.

Likewise, the third property can also be used for division and the fourth property can also be used for a change of the index of multiplication in the opposite direction.
::::::

## Grasple exercises

:::{todo}
Add Grasple exercises to {numref}`Sec:SumsAndProducts`.
:::

## Exercises

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
