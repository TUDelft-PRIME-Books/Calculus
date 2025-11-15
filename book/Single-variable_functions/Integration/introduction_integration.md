# Integration
In this chapter: Under Construction

```{tableofcontents}
```

In this chapter we will cover the concept of integration. An **integral** will be introduced as a limit of sums. So, we start with summations.

**Notation for sums**

The notation $\sum$ (capital Greek letter sigma) is used to denote a (finite) sum:
::::::{prf:Definition}
:label: Def:Integration:IntroductionNotationSum
If $a_m,a_{m+1},\ldots,a_n$ are real or complex numbers and $m$ and $n$ are integers with $m\leq n$, then

$$
\sum_{i=m}^na_i:=a_m+a_{m+1}+\ldots+a_n.
$$

::::::
The letter $i$ is called the **index of summation**.

::::::{prf:Example}
:label: Ex:Integration:IntroductionExamplesSum
* $\displaystyle\sum_{i=3}^5i^2=3^2+4^2+5^2=9+16+25=50$;
* $\displaystyle\sum_{j=-1}^15^{\frac{1}{2}j}=5^{-\frac{1}{2}}+5^0+5^{\frac{1}{2}}=\frac{1}{\sqrt{5}}+1+\sqrt{5}=1+\frac{6}{5}\sqrt{5}$;
* $\displaystyle\sum_{k=0}^32^k=2^0+2^1+2^2+2^3=1+2+4+8=15$.
::::::

::::::{prf:Example}
:label: Ex:Integration:IntroductionSumIntegers
Show that the sum $S$ of the first $n$ positive integers equals $\frac{1}{2}n(n+1)$.

Solution. Let $S:=\displaystyle\sum_{i=1}^ni$, then we have:

$$
\begin{align*}
S&=1&+2&+\ldots&+(n-1)&+n\\
S&=n&+(n-1)&+\ldots&+2&+1.
\end{align*}
$$

Adding the two expressions we obtain

$$
2S=\underbrace{(n+1)+(n+1)+\ldots+(n+1)+(n+1)}_{n\;\text{times}}.
$$

Hence we have: $2S=n(n+1)$ and therefore $S=\frac{1}{2}n(n+1)$.
::::::

::::::{prf:Example}
:label: Ex:Integration:IntroductionFiniteGeometric
Let $S=\displaystyle\sum_{i=1}^nar^{i-1}=a+ar+ar^2+\ldots+ar^{n-1}$ with $r\neq1$ and $n$ a positive integer. 

Show that $S=\dfrac{a(1-r^n)}{1-r}$.

Solution.

$$
\begin{align*}
S&=a&+ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&\\
rS&=&ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&+ar^n.
\end{align*}
$$

Subtracting the two equations we obtain

$$
(1-r)S=a-ar^n=a(1-r^n)\quad\Longrightarrow\quad S=\frac{a(1-r^n)}{1-r},\quad r\neq1.
$$

::::::

See chapter 7 for more details about finite sums and series (infinite sums).

**Notation for products**

Similarly, the notation $\prod$ (capital Greek letter pi) is used to denote a (finite) product:
::::::{prf:Definition}
:label: Def:Integration:IntroductionNotationProduct
If $a_m,a_{m+1},\ldots,a_n$ are real or complex numbers and $m$ and $n$ are integers with $m\leq n$, then

$$
\prod_{i=m}^na_i:=a_m\cdot a_{m+1}\cdots a_n.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:IntroductionExamplesProduct
For $n\in\{1,2,3,\ldots\}$ we have
* $\displaystyle\prod_{i=1}^ni=1\cdot2\cdot3\cdots(n-1)\cdot n=n!$;
* $\displaystyle\prod_{j=1}^n\frac{j}{j+1}=\frac{1}{2}\cdot\frac{2}{3}\cdot\frac{3}{4}\cdots\frac{n-1}{n}\cdot\frac{n}{n+1}=\frac{1}{n+1}$;
* $\displaystyle\prod_{k=1}^n\frac{2k+1}{2k}=\frac{3}{2}\cdot\frac{5}{4}\cdot\frac{7}{6}\cdots\frac{2n-1}{2n-2}\cdot\frac{2n+1}{2n}=\frac{3\cdot5\cdot7\cdots(2n+1)}{2\cdot4\cdot6\cdots2n}$.
::::::

Although we will not cover infinite products in this book we mention the following example.

::::::{prf:Remark}
:label: Ex:Integration:IntroductionExamplesProductSine
It can be shown that

$$
\sin(\pi x)=\pi x\prod_{n=1}^{\infty}\left(1-\frac{x^2}{n^2}\right).
$$

The factors of this infinite product give rise to all zeros of $\sin(\pi x)$ being $0,\pm1,\pm2,\ldots$.
::::::