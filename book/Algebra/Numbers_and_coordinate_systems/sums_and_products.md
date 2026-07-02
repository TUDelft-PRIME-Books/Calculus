(Sec:SumsAndProducts)=
# Finite summations and multiplications

## Introduction
In this section we introduce the terminology and notation for finite summations and multiplications which will be used in this book.

Although it can also be done for complex numbers, we restrict ourselves to real numbers. We assume that the reader is familiar with basic operations on real numbers such as addition, multiplication, subtraction, and division.

This section is not meant to be an exhaustive introduction to summations and multiplications, but rather a brief introduction to the terminology and notation that will be used in this book.

(Sec:SumsAndProducts:FiniteSequences)=
## Finite sequences

We start of with the definition of a finite sequence and some relevant terminology.

::::::{prf:definition}
:label: Def:SumsAndProducts:Definition

A **finite sequence** is a list of a finite set of numbers arranged in a specific order.

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

Here, the integer $p$ is the starting index and the integer $q$ is the ending index.

The letter $n$ is often used to denote the index, but we can also use any other letter for the index.

Sometimes we just write $\{a_n\}$ to denote a sequence, so if we do, please be aware that the context is relevant in that case.

::::

In many cases the terms of a sequence are defined by an explicit formula for the general term in terms of the index:

::::{prf:definition}
:label: Def:SumsAndProducts:ExplicitFormula

An **explicit formula for a sequence** $\{a_n\}$ is a formula that gives the $n$th term $a_n$ of the sequence directly in terms of the index $n$ for all integers $n$ larger than or equal to the starting index and smaller than or equal to the ending index.
::::

::::{prf:example}
:label: Ex:SumsAndProducts:PositiveIntegersExplicitFormula
The sequence of the first $q$ positive integers $1,2,3,4,5,\ldots,q$ can be defined by the explicit formula

$$
a_n=n\quad\text{for}\quad n=1,2,3,\ldots,q.
$$

Note that it makes sense to start with $n=1$ since the first term of the sequence is $1$. We could also have started with $n=0$ and define $a_n=n+1$ for $n=0,1,2,\ldots,q-1$, which gives rise to the same sequence.
::::

::::{prf:example}
:label: Ex:SumsAndProducts:ReciprocalPerfectSquaresExplicitFormula
The sequence of reciprocals of the first $q$ perfect squares $1,\frac{1}{4},\frac{1}{9},\frac{1}{16},\frac{1}{25},\ldots,\frac{1}{q^2}$ can be defined by the explicit formula

$$
b_n=\frac{1}{n^2}\quad\text{for}\quad n=1,2,3,\ldots,q.
$$
::::

::::{prf:example}
:label: Ex:SumsAndProducts:ExplicitFormula

Now consider the sequence $\{c_n\}_{n=1}^{q}$ with $c_n=\dfrac{n}{n^2+1}$ for $n=1,2,3,\ldots,q$.

This means, by substituting $n=1$ in the explicit formula, that the first term of the sequence is

$$
c_1=\frac{1}{2},
$$

by substituting $n=2$ that the second term of the sequence is

$$
c_2=\frac{2}{5},
$$

by substituting $n=3$ that the third term of the sequence is

$$
c_3=\frac{3}{10},
$$

and so on. We could write the sequence out as

$$
\{c_n\}_{n=1}^{q} = \left\{\frac{1}{2},\frac{2}{5},\frac{3}{10},\frac{4}{17},\frac{5}{26},\ldots,\frac{q}{q^2+1}\right\}.
$$

::::

In other cases, or even the same, the terms of a sequence are not expressed with an explicit formula, but with a recursive formula:

::::{prf:definition}
:label: Def:SumsAndProducts:RecursiveFormula

A **recursive formula for a sequence** $\{a_n\}_{n=p}^{q}$ is a formula that gives the $n$th term $a_n$ of the sequence in terms of $k$ of the preceding terms for all integers $n>p+k$ in combination with formulas for the first $k$ terms $a_p,a_{p+1},a_{p+2},\ldots,a_{p+k}$ of the sequence.

::::

::::{prf:example}
:label: Ex:SumsAndProducts:PositiveIntegersRecursiveFormula
The sequence of the first $q$ positive integers $1,2,3,4,5,\ldots,q$ can be defined by the recursive formula

$$
a_1=1,\quad a_{n+1}=a_n+1\quad\text{for}\quad n=1,2,3,\ldots
$$

::::

::::{prf:example} 
:label: Ex:SumsAndProducts:RecursiveFormula

The sequence $\{b_n\}_{n=0}^{q}$ defined by $b_{n+1}=-\dfrac12b_n$ with $n=0,1,2,\ldots,q-1$ and $b_0=1$ can be written out as:

$$
\{b_n\}_{n=0}^{q} = \left\{1,-\frac{1}{2},\frac{1}{4},-\frac{1}{8},\frac{1}{16},-\frac{1}{32},\ldots,\frac{(-1)^q}{2^q}\right\}.
$$

::::

(Sec:SumsAndProducts:Sums)=
## Finite summations

The summation symbol $\sum$ (the capital Greek letter sigma) is used to denote the addition of the terms a finite sequence of numbers:

::::::{prf:definition}
:label: Def:Integration:IntroductionNotationSum

The **summation symbol** $\sum$ is used to denote the addition of a finite sequence.

If $\{a_n\}_{n=p}^{q}$ is a finite sequence, then $\displaystyle\sum_{n=p}^qa_n$ is an abbreviation for the addition of the numbers $a_p,a_{p+1},a_{p+2},\ldots,a_q$, that is

$$
\sum_{n=p}^qa_n=a_p+a_{p+1}+a_{p+2}+\cdots+a_q.
$$

The result $S$ of the addition is called the **sum** of the numbers $a_p,a_{p+1},a_{p+2},\ldots,a_q$ and we write

$$
\sum_{n=p}^qa_n = S.
$$

The letter $n$ in the notation $\displaystyle\sum_{n=p}^qa_n$ is called the **index of summation**. The integer $p$ is called the **starting index of summation** and the integer $q$ is called the **ending index of summation**.

::::::

::::{prf:theorem}
:label: Thm:SumsAndProducts:Sum

The sum of a finite summation exists.
::::

::::{admonition} Proof of {prf:ref}`Thm:SumsAndProducts:Sum`
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

In the next examples we consider the summation of some finite sequences.

::::::{prf:Example}
:label: Ex:SumsAndProducts:IntroductionExamplesSum

* $\displaystyle\sum_{p=3}^5p^2=3^2+4^2+5^2=9+16+25=50$;
* $\displaystyle\sum_{j=-1}^15^j=5^{-1}+5^0+5^{1}=\frac{1}{5}+1+5=\frac{31}{5}$;
* $\displaystyle\sum_{k=0}^32^k=2^0+2^1+2^2+2^3=1+2+4+8=15$.

::::::

::::::{prf:Example}
:label: Ex:SumsAndProducts:IntroductionSumIntegers

We show that the sum $S$ of the first $n$ positive integers equals $\frac{1}{2}n(n+1)$.

Let $S=\displaystyle\sum_{k=1}^nk$, then we have:

$$
\class{compact}{
\begin{array}{ccccccccccc}
S & = & 1 & + &     2 & + & \cdots & + & (n-1) & + & n \\
S & = & n & + & (n-1) & + & \cdots & + &     2 & + & 1.
\end{array}
}
$$

Adding the two expressions we obtain

$$
2S=\underbrace{(n+1)+(n+1)+\cdots+(n+1)+(n+1)}_{n\;\text{times}}.
$$

Hence we have $2S=n(n+1)$ and therefore $S=\frac{1}{2}n(n+1)$.
::::::

Without stating a formal proof, we will also state some important properties of finite summations:

::::{prf:theorem}
:label: Thm:SumsAndProducts:PropertiesFiniteSums

If $\displaystyle\sum_{n=p}^qa_n=A$ and $\displaystyle\sum_{n=p}^qb_n=B$, then we have

$$
\sum_{n=p}^q(a_n+b_n)=A+B.
$$

If $\displaystyle\sum_{n=p}^qa_n=A$ and $c$ is a real number, then we have

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
:label: Rem:SumsAndProducts:PropertiesFiniteSums

In {prf:ref}`Thm:SumsAndProducts:PropertiesFiniteSums` the first and third property are focussed on the addition of finite summations, the second property is focussed on the multiplication of a finite summation by a number, and the fourth property is focussed on the change of the index of summation.

Combining the second property and the first property, we also obtain the following properties. If $\displaystyle\sum_{n=p}^qa_n=A$ and $\displaystyle\sum_{n=p}^qb_n=B$, then we have

$$
\sum_{n=p}^q(a_n-b_n)=A-B,
$$

and

$$
\sum_{n=p}^q(ca_n+db_n)=cA+dB
$$

for any real numbers $c$ and $d$.

The fourth property can also be used for a change of the index of summation in the opposite direction:

$$
\sum_{n=p+t}^{q+t} a_{n-t} = A.
$$

::::::

In {prf:ref}`Ex:SumsAndProducts:IntroductionExamplesSum` we have seen the following result, which we summarise in a theorem:

::::{prf:theorem}
:label: Thm:SumsAndProducts:SumOfIntegers

The finite summation $\displaystyle\sum_{k=1}^nk$, that is the addition of the terms of the sequence of the first $n$ positive integers, has the following sum:

$$
\sum_{k=1}^nk=\frac{1}{2}n(n+1)
$$

for all $n\in\{1,2,3,\ldots\}$.

::::

This theorem can also be proved using the {prf:ref}`principle of mathematical induction <Thm:Algebra:MathematicalInduction>`:

::::{admonition} Proof of {prf:ref}`Thm:SumsAndProducts:SumOfIntegers` (mathematical induction)
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

Now suppose that $\displaystyle\sum_{k=1}^nk=\frac{1}{2}n(n+1)$ holds for a certain value of $n$. Then we have

\begin{align*}
\sum_{k=1}^{n+1}k &= \left(\sum_{k=1}^nk\right)+(n+1) \\
&= \frac{1}{2}n(n+1)+(n+1) \\
&= \frac{1}{2}n(n+1)+\frac{2}{2}(n+1) \\
&= \frac{1}{2}(n+1)(n+2) \\
&= \frac{1}{2}(n+1)((n+1)+1).
\end{align*}

Since this is exactly the formula with $n$ replaced by $n+1$, this proves the statement for all $n\in\{1,2,3,\ldots\}$.

::::

::::::{prf:example}
:label: Ex:SumsAndProducts:SubSum

Using the previous theorem, we can show that

$$
\sum_{k=n^2+1}^{(n+1)^2}k=n^3+(n+1)^3
$$

for all $n\in\{1,2,3,\ldots\}$.

First, consider the finite summation that starts at $1$ and ends at $(n+1)^2$, then we have

:::{math}
:label: Eq:SumsAndProducts:SumOfIntegersSquares1
\begin{align*}
\sum_{k=1}^{(n+1)^2}k&=\frac{1}{2}(n+1)^2((n+1)^2+1)\\
&=\frac12(n^4+4n^3+7n^2+6n+2).
\end{align*}
:::

Next, consider the finite summation that starts at $1$ and ends at $n^2$, then we have

:::{math}
:label: Eq:SumsAndProducts:SumOfIntegersSquares2
\sum_{k=1}^{n^2}k=\frac{1}{2}n^2(n^2+1) = \frac12(n^4+n^2).
:::

If we subtract Equation {eq}`Eq:SumsAndProducts:SumOfIntegersSquares2` from Equation {eq}`Eq:SumsAndProducts:SumOfIntegersSquares1`, we obtain

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
:name: Fig:SumsAndProducts:Telescope

A pirate using a telescope.
::::
:::::

We now look at the summation of the terms of the sequence $\displaystyle\left\{\frac{1}{k(k+1)}\right\}_{k=1}^n$ to introduce the concept of a _telescoping_ sum:

::::{prf:example}
:label: Ex:SumsAndProducts:TelescopingSumExample1

Note that it seems not so easy to find the sum of

$$
\sum_{k=1}^n\frac{1}{k(k+1)}=\frac{1}{1\cdot2}+\frac{1}{2\cdot3}+\frac{1}{3\cdot4}+\cdots+\frac{1}{n(n+1)}.
$$

However, notice that

$$
\frac{1}{k(k+1)}=\frac{1}{k}-\frac{1}{k+1},
$$

which implies that

\begin{align*}
\sum_{k=1}^n\frac{1}{k(k+1)}&=\sum_{k=1}^n\left(\frac{1}{k}-\frac{1}{k+1}\right)\\
&=\frac{1}{1}-\cancel{\frac{1}{2}}+\cancel{\frac{1}{2}}-\cancel{\frac{1}{3}}\\
&{}\hspace{10mm}{}+\cdots+\cancel{\frac{1}{n-1}}-\cancel{\frac{1}{n}}+\cancel{\frac{1}{n}}-\frac{1}{n+1}\\
&=1-\frac{1}{n+1}\\
&=\frac{n}{n+1}.
\end{align*}

::::

As you may have observed, we could _cancel_ many terms in the series because those terms appear twice with opposite signs. Obviously, this is not a coincidence. This leads to the following definition:

::::{prf:definition}
:label: Def:SumsAndProducts:TelescopingSum

A finite summation $\displaystyle\sum_{k=m}^na_k$ is called a **telescoping summation** if there exists a sequence $\{b_k\}_{k=m}^{n+p}$ and an integer $p\geq1$ such that $a_k=b_{k}-b_{k+p}$ for all $k\in\{m,m+1,m+2,\ldots,n\}$.

The property that allows us to cancel many terms in a telescoping summation is called the **telescoping property**.
::::

In {prf:ref}`Def:SumsAndProducts:TelescopingSum` the number $p$ is often equal to $1$, but it can also be larger than $1$, as the next example shows:

::::{prf:example}
:label: Ex:SumsAndProducts:TelescopingSumExample2

Consider the finite summation $\displaystyle\sum_{k=2}^n\frac{1}{k^2-1}$.

Notice that for $k\in\{2,3,4,\ldots,n\}$ we have

$$
a_k=\frac{1}{k^2-1}=\frac{1}{2}\frac{1}{k-1}-\frac{1}{2}\frac{1}{k+1}.
$$

So if we take $p=2$ and $b_k=\dfrac{1}{2}\dfrac{1}{k-1}$ for $k\in\{2,3,4,\ldots,n+2\}$, then we have $a_k=b_{k}-b_{k+2}$ for all $k\in\{2,3,4,\ldots,n\}$, which means that $\displaystyle\sum_{k=2}^n\frac{1}{k^2-1}$ is a telescoping summation.

Using the telescoping property, we can also determine the sum of this telescoping summation as follows:

\begin{align*}
\sum_{k=2}^n\frac{1}{k^2-1}&=\sum_{k=2}^n\left(\frac{1}{2}\frac{1}{k-1}-\frac{1}{2}\frac{1}{k+1}\right) \\
&=\frac{1}{2}\sum_{k=2}^n\left(\frac{1}{k-1}-\frac{1}{k+1}\right) \\
&=\frac{1}{2}\left(\sum_{k=2}^n\frac{1}{k-1}-\sum_{k=2}^n\frac{1}{k+1}\right) \\
&=\frac{1}{2}\left(\sum_{k=0}^{n-2}\frac{1}{k+1}-\sum_{k=2}^n\frac{1}{k+1}\right) \\
&=\frac{1}{2}\left(\sum_{k=0}^{1}\frac{1}{k+1}-\sum_{k=n-1}^n\frac{1}{k+1}\right) \\
&=\frac{1}{2}\left(\left(1+\frac{1}{2}\right)-\left(\frac{1}{n}+\frac{1}{n+1}\right)\right) \\
&= \frac{3}{4}-\frac{1}{2}\frac{2n+1}{n(n+1)}.
\end{align*}

Notice that in the fourth line we have used the change of the index of summation to make the two summations look more similar, which makes it easier to see that many terms cancel. Also notice that in the fifth line we have used the telescoping property to cancel many terms and find the sum of the telescoping summation.

Even better, notice that the sum of the telescoping summation is the sum of the first two terms of the sequence $\left\{\dfrac{1}{2}\dfrac{1}{k+1}\right\}_{k=0}^{n+2}$ minus the sum of the last two terms of this sequence, which is a direct consequence of the telescoping property. We summarise this in the next theorem:

::::

::::{prf:theorem}
:label: Thm:SumsAndProducts:SumTelescopingSum
If $\displaystyle\sum_{k=m}^na_k$ is a telescoping summation with $a_k=b_{k}-b_{k+p}$ for all $k\in\{m,m+1,m+2,\ldots,n\}$ and some integer $p\geq1$, then we have

$$
\sum_{k=m}^na_k=\sum_{k=m}^{m+p-1}b_k-\sum_{k=n+1}^{n+p}b_k.
$$
::::

::::{admonition} Proof of {prf:ref}`Thm:SumsAndProducts:SumTelescopingSum`
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

Now, we consider the sum of a finite geometric summation, which is a very important example of a finite summation. We will also use this result in {numref}`Sec:Series:GeometricSeries` to find the sum of a infinite geometric series.

::::::{prf:Example}
:label: Ex:SumsAndProducts:IntroductionFiniteGeometric
Let $S=\displaystyle\sum_{k=1}^nar^{k-1}=a+ar+ar^2+\cdots+ar^{n-1}$ with $r\neq1$ and $n$ a positive integer. 

Then we have:

$$
\class{compact}{
\begin{array}{lllllllllllllllllllll}
 S & = & a & + & ar & + & ar^2 & + & \cdots & + & ar^{n-2} & + & ar^{n-1} \\
rS & = &   &   & ar & + & ar^2 & + & \cdots & + & ar^{n-2} & + & ar^{n-1} & + & ar^n.
\end{array}
}
$$

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

We prove the theorem by induction on $n$. See: {prf:ref}`Thm:Algebra:MathematicalInduction`.

For $n=1$ we have on the left-hand side

$$
(a-b)\sum_{k=1}^{1}a^{1-k}b^{k-1} = (a-b)a^{1-1}b^{1-1} = a-b,
$$

and on the right-hand side

$$
a^1-b^1 = a-b,
$$

so the statement holds for $n=1$.

Now assume that the statement holds for a certain value of $n$, so

$$
(a-b)\sum_{k=1}^{n}a^{n-k}b^{k-1}=a^n-b^n.
$$

then we have

\begin{align*}
(a-b)\sum_{k=1}^{n+1}a^{n+1-k}b^{k-1}&=(a-b)\left(\sum_{k=1}^{n}a^{n+1-k}b^{k-1}+a^{n+1-(n+1)}b^{(n+1)-1}\right) \\
&=(a-b)\left(a\sum_{k=1}^{n}a^{n-k}b^{k-1}+b^n\right) \\
&=a(a-b)\sum_{k=1}^{n}a^{n-k}b^{k-1}+(a-b)b^n \\
&=a\left(a^n-b^n\right)+(a-b)b^n \\
&=a^{n+1}-ab^n+ab^n-b^{n+1} \\
&=a^{n+1}-b^{n+1}.
\end{align*}

This proves the statement for all $n\in\{1,2,3,\ldots\}$.

:::

With this we end our treatment of finite summations.

## Finite multiplications

Similarly, the multiplication symbol $\prod$ (capital Greek letter pi) is used to denote the multiplication of a finite set of numbers:

::::::{prf:Definition}
:label: Def:SumsAndProducts:IntroductionNotationProduct

The **product symbol** $\prod$ is used to denote the multiplication of a set of ordered numbers.

If $\{a_n\}_{n=p}^{q}$ is a finite sequence, then $\displaystyle\prod_{n=p}^qa_n$ is an abbreviation for the multiplication of the numbers $a_p,a_{p+1},a_{p+2},\ldots,a_q$, that is

$$
\prod_{n=p}^qa_n=a_p\cdot a_{p+1}\cdots a_q.
$$

The result $P$ is called the **product** of the numbers $a_p,a_{p+1},a_{p+2},\ldots,a_q$ and we write

$$
\prod_{n=p}^qa_n = P.
$$

The letter $n$ in the notation $\displaystyle\prod_{n=p}^qa_n$ is called the **index of multiplication**. The integer $p$ is called the **starting index of multiplication** and the integer $q$ is called the **ending index of multiplication**.

::::::

The next examples only consider the multiplication of a finite set of numbers.

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

By convention, we also define $0!=1$. Then we may also write

$$
n!=n(n-1)!\quad\text{for}\quad n=1,2,3,\ldots.
$$

::::

:::::{note}
Sometimes, for $n\in\{1,2,3,\ldots\}$ the following notation is used:

$$
\prod_{k=0}^n(2k+1)=1\cdot3\cdot5\cdots(2n+1)=(2n+1)!!
$$

and

$$
\prod_{k=1}^n(2k)=2\cdot4\cdot6\cdots(2n)=(2n)!!
$$

This is called the **double factorial** and can also be defined as

$$
n!!=n\cdot(n-2)\cdot(n-4)\cdots4\cdot2\;\text{for}\;n\;\text{even}
$$

and

$$
n!!=n\cdot(n-2)\cdot(n-4)\cdots3\cdot1\;\text{for}\;n\;\text{odd.}
$$

By convention, we also define $0!!=1$ and $1!!=1$. Then we may also write

$$
n!!=n(n-2)!!\quad\text{for}\quad n=2,3,4,\ldots.
$$

:::::

Without stating a formal proof, we will also state some important properties of finite products:

::::{prf:theorem}
:label: Thm:SumsAndProducts:PropertiesFiniteProducts

If $\displaystyle\prod_{n=p}^qa_n=A$ and $\displaystyle\prod_{n=p}^qb_n=B$, then we have

$$
\prod_{n=p}^q(a_nb_n)=AB.
$$

If $\displaystyle\prod_{n=p}^qa_n=A$ and $c$ is a real number, then we have

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
:label: Rem:SumsAndProducts:PropertiesFiniteProducts

In {prf:ref}`Thm:SumsAndProducts:PropertiesFiniteProducts` the first and third property are focussed on the addition of finite multiplications, the second property is focussed on the multiplication of a finite multiplication by a number, and the fourth property is focussed on the change of the index of multiplication.

Combining the second property and the first property, we also obtain the following properties. If $\displaystyle\prod_{n=p}^qa_n=A$ and $\displaystyle\prod_{n=p}^qb_n=B$, with $B\neq0$ and $b_n\neq0$ for all $n\in\{p,p+1,p+2,\ldots,q\}$, then we have

$$
\prod_{n=p}^q\frac{a_n}{b_n}=\frac{A}{B},
$$

and

$$
\prod_{n=p}^q\frac{ca_n}{db_n}=\frac{c^{q-p+1}A}{d^{q-p+1}B}
$$

for any real numbers $c$ and $d\neq 0$.

The fourth property can also be used for a change of the index of multiplication in the opposite direction:

$$
\prod_{n=p+t}^{q+t} a_{n-t} = A.
$$

::::::

## Grasple exercises

:::{todo}
Add Grasple exercises to {numref}`Sec:SumsAndProducts`.
:::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bc4a2c94-546c-423a-8420-f63a61d83720?id=133025
:label: Grasple:133025
:dropdown:
:description: Find the sum.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/310bb414-e0e0-435d-b9e9-f9af1cfe16a5?id=133077
:label: Grasple:133077
:dropdown:
:description: Find the sum.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2587cd2f-9e61-4946-b119-ed2d1c21d8b5?id=133022
:label: Grasple:133022
:dropdown:
:description: Find a closed formula for the sum.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1998ab5f-af87-4c1d-bfa2-f6c812d14da3?id=133023
:label: Grasple:133023
:dropdown:
:description: Find a closed formula for the sum.

::::

## Exercises

::::{exercise}
:label: Exc:SumsAndProducts:SumOfSquares
Show that $\displaystyle\sum_{k=1}^nk^2=\frac{1}{6}n(n+1)(2n+1)$ for all $n\in\{1,2,3,\ldots\}$.
::::

:::{admonition} Solution of {numref}`Exc:SumsAndProducts:SumOfSquares`
:class: solution, dropdown

For $n=1$ this reads: $1=\frac{1}{6}\cdot1\cdot2\cdot3$, which is true. 

Suppose that $\displaystyle\sum_{k=1}^nk^2=\frac{1}{6}n(n+1)(2n+1)$ holds for certain value of $n$. Then we have

\begin{align*}
\sum_{k=1}^{n+1}k^2&=\sum_{k=1}^nk^2+(n+1)^2\\
&=\frac{1}{6}n(n+1)(2n+1)+(n+1)^2\\
&=\frac{1}{6}(n+1)\left(n(2n+1)+6(n+1)\right)\\
&=\frac{1}{6}(n+1)(2n^2+7n+6)\\
&=\frac{1}{6}(n+1)(n+2)(2n+3).
\end{align*}

Since this is exactly the formula with $n$ replaced by $n+1$, this proves the statement for all $n\in\{1,2,3,\ldots\}$.
:::

::::{exercise}
:label: Exc:SumsAndProducts:SumOfCubes

Show that $\displaystyle\sum_{k=1}^nk^3=\left(\sum_{k=1}^nk\right)^2=\frac{1}{4}n^2(n+1)^2$ for all $n\in\{1,2,3,\ldots\}$.
::::

:::{admonition} Solution of {numref}`Exc:SumsAndProducts:SumOfCubes`
:class: solution, dropdown

For $n=1$ this reads: $1=\frac{1}{4}\cdot1^2\cdot2^2$, which is true. 

Suppose that $\displaystyle\sum_{k=1}^nk^3=\frac{1}{4}n^2(n+1)^2$ holds for certain value of $n$. Then we have

\begin{align*}
\sum_{k=1}^{n+1}k^3&=\sum_{k=1}^nk^3+(n+1)^3\\
&=\frac{1}{4}n^2(n+1)^2+(n+1)^3\\
&=\frac{1}{4}(n+1)^2\left(n^2+4(n+1)\right)\\
&=\frac{1}{4}(n+1)^2(n^2+4n+4)\\
&=\frac{1}{4}(n+1)^2(n+2)^2.
\end{align*}

Since this is exactly the formula with $n$ replaced by $n+1$, this proves the statement for all $n\in\{1,2,3,\ldots\}$.
:::

::::{exercise}
:label: Exc:SumsAndProducts:TelescopingExercise
Use the facts that $n^4+n^2+1=n^4+2n^2+1-n^2=(n^2+1)^2-n^2$ and $2n=n^2+1+n-(n^2+1-n)$ to find the sum of

$$
\sum_{n=1}^{100}\frac{n}{n^4+n^2+1}.
$$

::::

:::{admonition} Solution of {numref}`Exc:SumsAndProducts:TelescopingExercise`
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

Hence, we have by {prf:ref}`Thm:SumsAndProducts:SumTelescopingSum` that

\begin{align*}
\sum_{n=1}^{100}\left(\frac{1}{n^2+1-n}-\frac{1}{n^2+1+n}\right) &= b_1-b_{101} \\
&= \frac12\frac{1}{c_1}-\frac12\frac{1}{c_{101}} \\
&= \frac12\frac{1}{1^2+1-1}-\frac12\frac{1}{101^2+1-101} \\
&= \frac12\frac11-\frac12\frac{1}{10101} \\
&= \frac12-\frac{1}{20202} \\
&= \frac{10101}{20202}-\frac{1}{20202} \\
&= \frac{10100}{20202} \\
&= \frac{5050}{10101} \\
&=0.\overline{499950}.
\end{align*}

See {numref}`Sec:Decimals` for the notation $0.\overline{499950}$.
:::
