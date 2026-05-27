(Sec:Series:BinomialSeries)=
# Binomial series

## Introduction

In this section we will investigate functions of the form $f(x)=(1+x)^{\alpha}$ where $\alpha\in\mathbb{R}$. We will find that such functions can be represented by a power series, called a **binomial series**. The coefficients of the terms in a binomial series are called **binomial coefficients** and they are closely related to the binomial coefficients appearing in Pascal's triangle and the binomial theorem. In turn, these two subjects are related to permutations and combinations. That is why we will start with the latter subjects.

## Permutations and combinations

Recall from {prf:ref}`Def:SumsAndProducts:Factorial` that *factorials* are defined as $0!=1$ and $n!=n(n-1)!$ for $n=1,2,3,\ldots$.

Factorials are used to indicate the number of ways to order $n$ distinct objects in a row.

:::{prf:example}
:label: Ex:Series:Factorials
Consider the set $\{a,b,c\}$, then there are $3!=6$ ways to arrange the elements in a row:

\begin{align*}
\{a,b,c\}, &~ \{a,c,b\}, \\
\{b,a,c\}, &~ \{b,c,a\}, \\
\{c,a,b\}, &~ \{c,b,a\}.
\end{align*}
:::

If we want to select $k$ elements from a set of $n$ distinct elements and order matters, the number of possible arrangements $P(n,k)$ is given by multiplying the number of options for the first choice with the number of options for the second choice, etcetera, until we have made $k$ choices. This leads to

\begin{align*}
P(n,k) &= n(n-1)(n-2)\cdots(n-k+1) \\
&= \prod_{j=0}^{k-1}(n-j) \\
&= \prod_{j=0}^{k-1}(n-j)\frac{\prod\limits_{j=k}^{n-1}(n-j)}{\prod\limits_{j=k}^{n-1}(n-j)} \\
&= \frac{\prod\limits_{j=0}^{n-1}(n-j)}{\prod\limits_{j=k}^{n-1}(n-j)} \\
&= \frac{\prod\limits_{q=1}^{n}q}{\prod\limits_{p=1}^{n-k}p} \\
&= \frac{n!}{(n-k)!}.
\end{align*}

This number $P(n,k)$ is called the number of **permutations** of $n$ distinct objects taken $k$ at a time:

:::{prf:definition}
:label: Def:Series:Permutations

The number of **permutations** of $n$ distinct objects taken $k$ at a time is given by

$$
P(n,k)=\frac{n!}{(n-k)!},\quad k=1,2,3,\ldots,n.
$$

If $k>n$, then we define $P(n,k)=0$.
::::

If order does not matter, then we have to divide $P(n,k)$ by the number of ways to order $k$ distinct objects in a row, which is $k!$. This leads to

$$
C(n,k)=\frac{P(n,k)}{k!}=\frac{n!}{k!(n-k)!}.
$$

This number $C(n,k)$ is called the number of **combinations** of $n$ distinct objects taken $k$ at a time:

::::{prf:definition}
:label: Def:Series:Combinations

The number of **combinations** of $n$ distinct objects taken $k$ at a time is given by

:::{math}
:label: Eq:Series:BinomialCoefficient
C(n,k)=\frac{n!}{k!(n-k)!},\quad k=0,1,2,\ldots,n.
:::

The number $C(n,k)$ is also denoted by $\displaystyle\binom{n}{k}$ and is called the **binomial coefficient**.

If $k>n$, then we define $C(n,k)=0$.
::::

::::::{prf:example}
Consider the set $\{a,b,c,d\}$, then choosing two elements leads to $P(4,2)=\frac{4!}{(4-2)!}=\frac{4!}{2!}=12$ where order matters:

\begin{align*}
\{a,b\}, &~ \{a,c\}, &~ \{a,d\}, &~ \{b,a\}, &~ \{b,c\}, &~ \{b,d\},\\
\{c,a\}, &~ \{c,b\}, &~ \{c,d\}, &~ \{d,a\}, &~ \{d,b\}, &~ \{d,c\}.
\end{align*}

If order does not matter, then we have $C(4,2)=\binom{4}{2}=\frac{4!}{2!\,2!}=\frac{3\cdot4}{1\cdot2}=6$ combinations:

$$
\{a,b\},\quad\{a,c\},\quad\{a,d\},\quad\{b,c\},\quad\{b,d\}\quad\text{and}\quad\{c,d\}.
$$

::::::

## Pascal's triangle and the binomial theorem

Let us investigate the binomial coefficients $\displaystyle\binom{n}{k}$ for $n=0,1,2,\ldots$ and $k=0,1,2,\ldots,n$ a little bit more. Below you can find a table for the first few values of $n$ and $k$:

```{list-table} $64$ binomial coefficients for $n=0,1,2,\ldots,7$ and $k=0,1,2,\ldots,7$.
:header-rows: 1
:stub-columns: 1

* - $n\backslash k$
  - 0
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
* - 0
  - 1
  - 0
  - 0
  - 0
  - 0
  - 0
  - 0
  - 0
* - 1
  - 1
  - 1
  - 0
  - 0
  - 0
  - 0
  - 0
  - 0
* - 2
  - 1
  - 2
  - 1
  - 0
  - 0
  - 0
  - 0
  - 0
* - 3
  - 1
  - 3
  - 3
  - 1
  - 0
  - 0
  - 0
  - 0
* - 4
  - 1
  - 4
  - 6
  - 4
  - 1
  - 0
  - 0
  - 0
* - 5
  - 1
  - 5
  - 10
  - 10
  - 5
  - 1
  - 0
  - 0
* - 6
  - 1
  - 6
  - 15
  - 20
  - 15
  - 6
  - 1
  - 0
* - 7
  - 1
  - 7
  - 21
  - 35
  - 35
  - 21
  - 7
  - 1
```

At a first glance, the numbers in the table do not seem to have any special properties, but if we drop all the zeros and write all rows (without headers) in a centered way, we obtain the triangular array you can see in {numref}`Fig:Series:PascalsTriangle`.

:::{figure-start}
:name: Fig:Series:PascalsTriangle
:align: center

The first eight rows of Pascal's triangle. The numbers between brackets indicate the row number, starting with row 1 at the top.
:::

$$
\begin{array}{cllccccccccccccccc}
(1)&&&&&&&&&& 1\\[2.5mm]
(2)&&&&&&&&& 1 && 1\\[2.5mm]
(3)&&&&&&&& 1 && 2 && 1\\[2.5mm]
(4)&&&&&&& 1 && 3 && 3 && 1\\[2.5mm]
(5)&&&&&& 1 && 4 && 6 && 4 && 1\\[2.5mm]
(6)&&&&& 1 && 5 && 10 && 10 && 5 && 1\\[2.5mm]
(7)&&&& 1 && 6 && 15 && 20 && 15 && 6 && 1\\[2.5mm]
(8)&&&1 && 7 && 21 && 35 && 35 && 21 && 7 && 1
\end{array}
$$

:::{figure-end}
:::

This triangle is called **Pascal's triangle**, named after the French mathematician [Blaise Pascal (1623-1662)](https://en.wikipedia.org/wiki/Blaise_Pascal).

If you inspect Pascal's triangle, you should notice that from the third row onwards, each number is the sum of the two nearest numbers in the row directly above it. For example, the left number $10$ in the sixth row is the sum of the two nearest numbers $4$ and $6$ in the fifth row, and the right number $10$. The same holds for all other numbers in Pascal's triangle, except for the numbers at the left and right edge of each row which are always equal to $1$.

In terms of *binomial coefficients* this property can be given as a theorem:

::::{prf:theorem}
:label: Thm:Series:Pascal
For a positive integer $n\geq0$ and $k=1,2,3,\ldots,n$ we have

$$
\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}.
$$

::::

:::{admonition} Proof of {prf:ref}`Thm:Series:Pascal`
:class: tudproof, dropdown

\begin{align*}
\binom{n-1}{k-1}+\binom{n-1}{k}&=\frac{(n-1)!}{(k-1)!\,(n-k)!}+\frac{(n-1)!}{k!\,(n-k-1)!}\\
&=\frac{(n-1)!}{k!\,(n-k)!}\left[k+(n-k)\right]\\
&=\frac{n\,(n-1)!}{k!\,(n-k)!}=\frac{n!}{k!\,(n-k)!}=\binom{n}{k}.
\end{align*}
:::

So what do the binomial coefficients and Pascal's triangle have to do with series?

Well consider the expansion of the binomials $(a+b)^n$ for $n=0,1,2,\ldots$:

\begin{align*}
(a+b)^0&=1,\\[2.5mm]
(a+b)^1&=a+b,\\[2.5mm]
(a+b)^2&=a^2+2ab+b^2,\\[2.5mm]
(a+b)^3&=a^3+3a^2b+3ab^2+b^3,\\[2.5mm]
(a+b)^4&=a^4+4a^3b+6a^2b^2+4ab^3+b^4,\\[2.5mm]
\text{etcetera.}
\end{align*}

As you may notice, each term in the expansion of $(a+b)^n$ has a coefficient which is a binomial coefficient occurring in Pascal's triangle. For example, the coefficient of the term $a^2b^2$ in the expansion of $(a+b)^4$ is $6$, which is equal to $\displaystyle\binom{4}{2}$, and corresponds with the third(as $2+1=3$) number in the fifth (as $4+1=5$) row of Pascal's triangle.

Pascal's triangle can thus be used to find the coefficients of the terms in the expansion of $(a+b)^n$ for $n=0,1,2,\ldots$.

In general, the expansion of the binomial $(a+b)^n$ is given by the binomial theorem:

::::::{prf:theorem} Binomial theorem
:label: Thm:Series:BinomialTheorem

$$
(a+b)^n=\sum_{k=0}^n\binom{n}{k}a^{n-k}b^k=\sum_{k=0}^n\binom{n}{k}a^kb^{n-k},\quad n=0,1,2,\ldots
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:BinomialTheorem`
:class: tudproof, dropdown
By mathematical induction: for $n=0$ it reads $(a+b)^0=1=\displaystyle\binom{0}{0}a^0b^0$ which is true by definition. Suppose that the formula is true for certain value of $n$, then we have:

\begin{align*}
(a+b)^{n+1}&=(a+b)(a+b)^n \\
&=(a+b)\sum_{k=0}^n\binom{n}{k}a^{n-k}b^k\\
&=\sum_{k=0}^n\binom{n}{k}a^{n-k+1}b^k+\sum_{k=0}^n\binom{n}{k}a^{n-k}b^{k+1}\\
&=\sum_{k=0}^n\binom{n}{k}a^{n-k+1}b^k+\sum_{k=1}^{n+1}\binom{n}{k-1}a^{n-k+1}b^k\\
&=a^{n+1}+\sum_{k=1}^n\left\{\binom{n}{k}+\binom{n}{k-1}\right\}a^{n-k+1}b^k+b^{n+1}\\
&=a^{n+1}+\sum_{k=1}^n\binom{n+1}{k}a^{n+1-k}b^k+b^{n+1} \\
&=\sum_{k=0}^{n+1}\binom{n+1}{k}a^{n+1-k}b^k.
\end{align*}
Since this is exactly the formula with $n$ replaced by $n+1$, this proves the theorem.
:::

::::::{prf:example}
:label: Ex:Series:BinomialTheorem

To expand $(1+x)^7$ we can use the binomial theorem with $a=1$, $b=x$ and $n=7$, which gives

\begin{align*}
(1+x)^7 &= \sum_{k=0}^7\binom{7}{k}(1)^{7-k}x^k \\
&= \binom{7}{0}+\binom{7}{1}x+\binom{7}{2}x^2+\binom{7}{3}x^3+\binom{7}{4}x^4+\binom{7}{5}x^5+\binom{7}{6}x^6+\binom{7}{7}x^7.
\end{align*}

Using the eight row of Pascal's triangle, see {numref}`Fig:Series:PascalsTriangle`, we can find the binomial coefficients $\binom{7}{0}=1$, $\binom{7}{1}=7$, $\binom{7}{2}=21$, $\binom{7}{3}=35$, $\binom{7}{4}=35$, $\binom{7}{5}=21$, $\binom{7}{6}=7$ and $\binom{7}{7}=1$. This gives

$$
(1+x)^7=1+7x+21x^2+35x^3+35x^4+21x^5+7x^6+x^7.
$$

::::::

::::::::{admonition} Fibonacci numbers and Pascal's triangle
:class: bonus, dropdown

The *Fibonacci numbers* appear in Pascal's triangle as follows:

:::{figure} Images/fibonacci.png
:width: 75%
:name: Fig:Series:FibonacciPascal
:align: center

The Fibonacci numbers appearing in Pascal's triangle.
:::

:::{todo}
Replace the image in {numref}`Fig:Series:FibonacciPascal` with a $\LaTeX$ version if possible. Perhaps using `tikz` commands and [Jupyter-TikZ
](https://jupyter-tikz.readthedocs.io/stable/)
:::

This can be written as $F_n=\displaystyle\sum_{k=0}^{\lfloor\frac{n-1}{2}\rfloor}\binom{n-k-1}{k}$  for $n=1,2,3,\ldots$. Here $\lfloor{\alpha}\rfloor$ denotes the greatest integer less than or equal to $\alpha$. This is equivalent to

$$
F_{2n-1}=\sum_{k=0}^{n-1}\binom{2n-k-2}{k}\quad\text{and}\quad F_{2n}=\sum_{k=0}^n\binom{2n-k-1}{k},\quad n=1,2,3,\ldots
$$

The proof is by mathematical induction. For $n=1$ we have 

$$
F_1=\displaystyle\binom{0}{0}=1\quad\text{and}\quad F_2=\displaystyle\sum_{k=0}^1\binom{1-k}{k}=\binom{1}{0}+\binom{0}{1}=1.
$$

Now we assume that

$$
F_{2n-1}=\displaystyle\sum_{k=0}^{n-1}\binom{2n-k-2}{k}\quad\text{and}\quad F_{2n}=\displaystyle\sum_{k=0}^n\binom{2n-k-1}{k}
$$

for a certain value of $n$, then we have

\begin{align*}
\sum_{k=0}^n\binom{2n-k}{k} &= 1+\sum_{k=1}^n\binom{2n-k-1}{k}+\sum_{k=1}^n\binom{2n-k-1}{k-1}\\
&=\sum_{k=0}^n\binom{2n-k-1}{k}+\sum_{k=0}^{n-1}\binom{2n-k-2}{k} \\
&= F_{2n}+F_{2n-1} \\
&=F_{2n+1}
\end{align*}

and

\begin{align*}
\sum_{k=0}^{n+1}\binom{2n-k+1}{k}&=1+\sum_{k=1}^{n+1}\binom{2n-k}{k}+\sum_{k=1}^{n+1}\binom{2n-k}{k-1}\\
&=\sum_{k=0}^{n+1}\binom{2n-k}{k}+\sum_{k=0}^n\binom{2n-k-1}{k} \\
&= F_{2n+1}+F_{2n} \\
&= F_{2n+2}.
\end{align*}

Using these results, we can prove the next theorem:

:::{prf:theorem}
:label: Thm:Series:FibonacciPascal

For each $m\in\mathbb{N}$ we also have

$$
F_{m+2n}=\displaystyle\sum_{k=0}^n\binom{n}{k}F_{m+k},\quad n=1,2,3,\ldots
$$

:::

:::{admonition} Proof of {prf:ref}`Thm:Series:FibonacciPascal`
:class: tudproof, dropdown
The proof is by mathematical induction. For $n=1$ we have: $F_{m+2}=\displaystyle\sum_{k=0}^1\binom{1}{k}F_{m+k}=F_m+F_{m+1}$ which is true. Now we assume that 

$$
F_{m+2n}=\displaystyle\sum_{k=0}^n\binom{n}{k}F_{m+k}
$$

for a certain value of $n$. Then we have

\begin{align*}
\sum_{k=0}^{n+1}\binom{n+1}{k}F_{m+k}&=F_m+\sum_{k=1}^{n+1}\left\{\binom{n}{k}+\binom{n}{k-1}\right\}F_{m+k}\\
&=\sum_{k=0}^n\binom{n}{k}F_{m+k}+\sum_{k=0}^n\binom{n}{k}F_{m+k+1}\\
&=F_{m+2n}+F_{m+2n+1}=F_{m+2n+2}.
\end{align*}
This is the original formula with $n$ replaced by $n+1$, which proves {prf:ref}`Thm:Series:FibonacciPascal`.
:::

The special case $m=0$ of {prf:ref}`Thm:Series:FibonacciPascal` reads

$$
F_{2n}=\displaystyle\sum_{k=0}^n\binom{n}{k}F_k,\quad n=1,2,3,\ldots
$$

::::::::

## Binomial series

In {prf:ref}`Ex:Series:BinomialTheorem` we have seen that the binomial theorem can be used to expand the binomial $(1+x)^7$ for $n=0,1,2,\ldots$. In that case we achieve a _finite_ series expansion of the binomial. If we set $f(x)=(1+x)^7$, and would calculate the Taylor series expansion of $f$ around $x=0$, the first step is determining the derivatives of $f$:

\begin{align*}
f(x) &= (1+x)^7,\\
f'(x) &= 7(1+x)^6,\\
f''(x) &= 7\cdot6(1+x)^5,\\
f^{(3)}(x) &= 7\cdot6\cdot5(1+x)^4,\\
f^{(4)}(x) &= 7\cdot6\cdot5\cdot4(1+x)^3,\\
f^{(5)}(x) &= 7\cdot6\cdot5\cdot4\cdot3(1+x)^2,\\
f^{(6)}(x) &= 7\cdot6\cdot5\cdot4\cdot3\cdot2(1+x),\\
f^{(7)}(x) &= 7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1,\\
f^{(n)}(x) &= 0\quad\text{for }n=8,9,10,\ldots
\end{align*}

Substituting $x=0$ gives 

\begin{align*}
f(0) &= 1 = \dfrac{7!}{7!} ,\\
f'(0) &= 7 = \dfrac{7!}{6!} ,\\
f''(0) &= 7\cdot6 = \dfrac{7!}{5!} ,\\
f^{(3)}(0) &= 7\cdot6\cdot5 = \dfrac{7!}{4!} ,\\
f^{(4)}(0) &= 7\cdot6\cdot5\cdot4 = \dfrac{7!}{3!} ,\\
f^{(5)}(0) &= 7\cdot6\cdot5\cdot4\cdot3 = \dfrac{7!}{2!} ,\\
f^{(6)}(0) &= 7\cdot6\cdot5\cdot4\cdot3\cdot2 = \dfrac{7!}{1!} ,\\
f^{(7)}(0) &= 7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1 = \dfrac{7!}{0!} ,\\
f^{(n)}(0) &= 0\quad\text{for }n=8,9,10,\ldots
\end{align*}

This means that the Taylor series expansion of $f$ around $x=0$ is given by

$$
\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n=\sum_{n=0}^7\frac{7!}{(7-n)!n!}x^n=\sum_{n=0}^7\binom{7}{n}x^n,
$$

which is exactly the same as the expansion of $(1+x)^7$ given by the binomial theorem in {prf:ref}`Ex:Series:BinomialTheorem`.

So what happens if we replace the exponent $7$ by an arbitrary real number $\alpha$? Can we still find a Taylor series expansion of the function $f(x)=(1+x)^{\alpha}$ around $x=0$?

To that end, consider the function $f(x)=(1+x)^{\alpha}$ with $\alpha\in\mathbb{R}$. then we have

\begin{align*}
f(x) &= (1+x)^{\alpha},\\
f'(x) &= \alpha(1+x)^{\alpha-1}, \\
f''(x) &= \alpha(\alpha-1)(1+x)^{\alpha-2}, \\
f^{(3)}(x) &= \alpha(\alpha-1)(\alpha-2)(1+x)^{\alpha-3}, \\
&\vdots \\
\end{align*}

This implies that

$$
f^{(n)}(0)=\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-n+1)\quad\text{for }n=1,2,3,\ldots
$$

But as a consequence, the Taylor series expansion $\displaystyle\sum_{n=0}^{\infty}c_nx^n$ of $f$ around $x=0$ is given by the coefficients

$$
c_n=\frac{f^{(n)}(0)}{n!}=\frac{\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-n+1)}{n!}\quad\text{for }n=1,2,3,\ldots
$$

If $\alpha$ would be a positive integer, then we can write

$$
c_n = \frac{\alpha!}{n!(n-\alpha)!} = \binom{\alpha}{n}\quad\text{for }n=0,1,2,\ldots,\alpha.
$$

However, if $\alpha$ is not a positive integer, then the coefficients $c_n$ are not given by the binomial coefficients $\displaystyle\binom{\alpha}{n}$ defined in Equation {eq}`Eq:Series:BinomialCoefficient` as these binomial coefficients are only defined for non-negative integers. However, we can generalise the definition of the binomial coefficients to arbitrary real numbers $\alpha$ as follows:

:::{math}
:label: Eq:Series:BinomialCoefficients


\binom{\alpha}{0}=1,\quad\binom{\alpha}{n}=\frac{\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-n+1)}{n!},\quad n=1,2,3,\ldots,
:::

In that case, we have a short and precise form for the Taylor series expansion of $(1+x)^{\alpha}$ around $x=0$:

::::::{prf:theorem}
:label: Thm:Series:BinomialSeries
If $\alpha\in\mathbb{R}$, then we have

\begin{align*}
(1+x)^{\alpha}&=\sum_{n=0}^{\infty}\binom{\alpha}{n}x^n\\
&=1+\frac{\alpha}{1!}x+\frac{\alpha(\alpha-1)}{2!}x^2+\frac{\alpha(\alpha-1)(\alpha-2)}{3!}x^3+\ldots,\quad|x| < 1.
\end{align*}

::::::

::::::{prf:definition}
:label: Def:Series:BinomialSeries

The Taylor series expansion of $(1+x)^{\alpha}$ around $x=0$ is called a **binomial series**.
::::::

:::{prf:remark}
:label: Rmk:Series:BinomialSeries

The convergence of the binomial series is not guaranteed for all $x\in\mathbb{R}$, but only for $|x|<1$, in which case it converges absolutely.

The convergence for $|x|=1$ depends on the value of $\alpha$ an $x$. Without further proof, the following results hold:

- If $\alpha>0$, then the binomial series converges for $x=-1$ and converges for $x=1$.

- If $-1<\alpha\leq0$, then the binomial series diverges for $x=-1$ and converges for $x=1$.

- If $\alpha\leq-1$, then the binomial series diverges for $x=-1$ and diverges for $x=1$.

:::

:::{admonition} Proof of {prf:ref}`Thm:Series:BinomialSeries`
:class: tudproof, dropdown

The proof of this theorem is by construction of the Taylor series expansion of $f(x)=(1+x)^{\alpha}$ around $x=0$ as we have done above. The only thing that remains to be shown is that the radius of convergence of this Taylor series expansion equals $R=1$.

In order to see that the radius of convergence equals $R=1$ we apply the ratio test: for $x\neq0$ let $a_n=\displaystyle\binom{\alpha}{n}x^n$, then we have:

\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|\binom{\alpha}{n+1}x^{n+1}\bigg/\binom{\alpha}{n}x^n\right|\\
&=\lim\limits_{n\to\infty}\left|\frac{\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-n+1)(\alpha-n)}{\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-n+1)}\frac{n!}{(n+1)!}x\right|\\
&=\lim\limits_{n\to\infty}\left|\frac{\alpha-n}{n+1}x\right|=|x|.
\end{align*}

This shows that the radius of convergence equals $R=1$.

:::

::::{prf:example}
:label: Ex:Series:BinomialSeriesSqrt

Consider $\displaystyle\sqrt{1+x}=(1+x)^{\frac{1}{2}}=\sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}x^n$ for $|x|<1$. Then we have

\begin{align*}
\binom{\frac{1}{2}}{0} &=1, \\
\binom{\frac{1}{2}}{1} &= \frac{1}{2}, \\
\binom{\frac{1}{2}}{2} &= \frac{\frac{1}{2}\left(\frac{1}{2}-1\right)}{2!}=-\frac{1}{8},\\
\binom{\frac{1}{2}}{3} &= \frac{\frac{1}{2}\left(\frac{1}{2}-1\right)\left(\frac{1}{2}-2\right)}{3!}=\frac{1}{16},\\
\binom{\frac{1}{2}}{4} &= \frac{\frac{1}{2}\left(\frac{1}{2}-1\right)\left(\frac{1}{2}-2\right)\left(\frac{1}{2}-3\right)}{4!}=-\frac{5}{128},\\
\end{align*}

and so on, and therefore

\begin{align*}
\sqrt{1+x}&=(1+x)^{\frac{1}{2}} \\
&=\sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}x^n\\
&=1+\frac{1}{2}x-\frac{1}{8}x^2+\frac{1}{16}x^3-\frac{5}{128}x^4+\ldots,
\end{align*}

provided that $|x|<1$.

::::

::::{prf:example}
:label: Ex:Series:BinomialSeriesSqrtInverse
Consider $\displaystyle\frac{1}{\sqrt{1+x}}=(1+x)^{-\frac{1}{2}}=\sum_{n=0}^{\infty}\binom{-\frac{1}{2}}{n}x^n$ for $|x|<1$. Then we have

\begin{align*}
\binom{-\frac{1}{2}}{0} &= 1, \\
\binom{-\frac{1}{2}}{1} &= -\frac{1}{2}, \\
\binom{-\frac{1}{2}}{2} &= \frac{-\frac{1}{2}\left(-\frac{1}{2}-1\right)}{2!}=\frac{3}{8},\\
\binom{-\frac{1}{2}}{3} &= \frac{-\frac{1}{2}\left(-\frac{1}{2}-1\right)\left(-\frac{1}{2}-2\right)}{3!}=\frac{5}{16},\\
\end{align*}

and so on, and therefore

\begin{align*}
\frac{1}{\sqrt{1+x}} &= (1+x)^{-\frac{1}{2}} \\
&= \sum_{n=0}^{\infty}\binom{-\frac{1}{2}}{n}x^n \\
&= 1-\frac{1}{2}x+\frac{3}{8}x^2-\frac{5}{16}x^3+\ldots,\quad |x|<1.
\end{align*}
::::

:::{prf:example}
:label: Ex:Series:BinomialSeriesArcsinArccos

Replacing $x$ by $-x^2$ in the {prf:ref}`Ex:Series:BinomialSeriesSqrtInverse` implies that 

$$
\frac{1}{\sqrt{1-x^2}}=\sum_{n=0}^{\infty}(-1)^n\binom{-\frac{1}{2}}{n}x^{2n}=1+\frac{1}{2}x+\frac{3}{8}x^2+\frac{5}{16}x^3+\ldots
$$

for $|-x^2| < 1\;\;\Longleftrightarrow\;\;|x| < 1$. Using integration we obtain

$$
\arcsin(x)=\int\frac{1}{\sqrt{1-x^2}}\,dx=C+\sum_{n=0}^{\infty}(-1)^n\binom{-\frac{1}{2}}{n}\frac{x^{2n+1}}{2n+1},\quad|x| < 1
$$ 
 
and since $\arcsin(0)=0$ we conclude that $C=0$.

Similarly, we obtain after multiplication by $-1$ and integration that

$$
\arccos(x)=-\int\frac{1}{\sqrt{1-x^2}}\,dx=K-\sum_{n=0}^{\infty}(-1)^n\binom{-\frac{1}{2}}{n}\frac{x^{2n+1}}{2n+1},\quad|x| <1
$$ 
 
and since $\arccos(0)=\frac{1}{2}\pi$ we conclude that $K=\frac{1}{2}\pi$.

Hence we have

$$
\arcsin(x)=\sum_{n=0}^{\infty}(-1)^n\binom{-\frac{1}{2}}{n}\frac{x^{2n+1}}{2n+1},\quad|x| < 1
$$

and

$$
\arccos(x)=\frac{1}{2}\pi-\sum_{n=0}^{\infty}(-1)^n\binom{-\frac{1}{2}}{n}\frac{x^{2n+1}}{2n+1},\quad|x| < 1.
$$ 

:::

::::::{prf:example}
:label: Ex:Series:BinomialSeriesApplication1

The binomial series can be used to calculate limits. For example we can use $\displaystyle\sqrt{1+x^2}=\sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}x^{2n}=1+\frac{1}{2}x^2-\frac{1}{8}x^4+\frac{1}{16}x^6+\ldots$ for $|x|<1$ and find that

\begin{align*}
\lim\limits_{x\to 0}\frac{\sqrt{1+x^2}-1-\frac{1}{2}x^2}{x^4} &= \lim\limits_{x\to 0}\frac{1+\frac{1}{2}x^2-\frac{1}{8}x^4++\frac{1}{16}x^6+\ldots-1-\frac{1}{2}x^2}{x^4} \\
&= \lim\limits_{x\to 0}\frac{-\frac{1}{8}x^4+\frac{1}{16}x^6+\ldots}{x^4} \\
&= \lim\limits_{x\to 0}-\frac{1}{8}+\frac{1}{16}x^2+\ldots
=-\frac{1}{8}.
\end{align*}

::::::

::::::{prf:example}
:label: Ex:Series:BinomialSeriesApplication2

Similarly, using $\displaystyle\sqrt{1+x^3}=\sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}x^{3n}$ for $|x|<1$ we find that

\begin{align*}
\int_0^{\frac{1}{2}}\sqrt{1+x^3}\,dx &= \int_0^{\frac{1}{2}}\sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}x^{3n}\,dx \\
&= \sum_{n=0}^{\infty}\int_0^{\frac{1}{2}}\binom{\frac{1}{2}}{n}x^{3n}\,dx \\
&= \sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}\int_0^{\frac{1}{2}}x^{3n}\,dx \\
&= \sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}\frac{(\frac{1}{2})^{3n+1}}{3n+1} \\
&= \frac{1}{2}+\frac{1}{128}-\frac{1}{7168}+\ldots \\
&= 0.507678\ldots
\end{align*}

::::::


## Grasple exercises

:::{todo}
Add Grasple exercises in {numref}`Sec:Series:BinomialSeries`.
:::