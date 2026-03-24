# Summation and product symbols

In this section we introduce the notation for summations and products which will be used in the rest of this book.

We assume that the reader is familiar with basic operations on rational numbers such as addition, multiplication, subtraction, and division.

These operations can be extended to rational real numbers ({numref}`Section:RealNumbers`) and complex numbers ({numref}`Ch:ComplexNumbersCartesian`).

This chapter is not meant to be an exhaustive introduction to summations and products, but rather a brief introduction to the notation that will be used in the rest of this book.

(Sec:SumsAndProducts:Sums)=
## Summation symbol

The summation symbol $\sum$ (the capital Greek letter sigma) is used to denote the addition of any number of numbers:

::::::{prf:definition}
:label: Def:Integration:IntroductionNotationSum

The **summation symbol** $\sum$ is used to denote the addition of a set of ordered numbers.
::::::


If $a_m,a_{m+1},\ldots,a_n$ are numbers and $m$ and $n$ are integers with $m\leq n$, then

$$
\sum_{k=m}^na_k
$$

is an abbreviation for the addition of the numbers $a_m,a_{m+1},\ldots,a_n$, that is

$$
a_m+a_{m+1}+\ldots+a_n.
$$

We also allow the addition of an infinite number of numbers, which can be written as

$$
\sum_{k=m}^\infty a_k,
$$

where $a_k$ is a number for each integer $k\geq m$.

::::::

The next examples only consider the addition of a finite number of numbers.

::::::{prf:Example}
:label: Ex:Integration:IntroductionExamplesSum

* $\displaystyle\sum_{i=3}^5i^2=3^2+4^2+5^2=9+16+25=50$;
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

See {numref}`Chapter:Series:Introduction` for more details about the addition of a finite or an infinite number of numbers.

## Product symbol

Similarly, the product symbol $\prod$ (capital Greek letter pi) is used to denote multiplication of a any number of numbers:

::::::{prf:Definition}
:label: Def:Integration:IntroductionNotationProduct

The **product symbol** $\prod$ is used to denote the multiplication of a set of ordered numbers.

::::::


If $a_m,a_{m+1},\ldots,a_n$ are numbers and $m$ and $n$ are integers with $m\leq n$, then

$$
\prod_{k=m}^na_k
$$

is an abbreviation for the multiplication of the numbers $a_m,a_{m+1},\ldots,a_n$, that is

$$
a_m\cdot a_{m+1}\cdots a_n.
$$

We also allow the multiplication of an infinite number of numbers, which can be written as

$$
\prod_{k=m}^\infty a_k,
$$

where $a_k$ is a number for each integer $k\geq m$.

The next examples only consider the multiplication of a finite number of numbers.

::::::{prf:Example}
:label: Ex:Integration:IntroductionExamplesProduct

For $n\in\{1,2,3,\ldots\}$ we have
* $\displaystyle\prod_{p=1}^np=1\cdot2\cdot3\cdots(n-1)\cdot n=n!$;
* $\displaystyle\prod_{j=1}^n\frac{j}{j+1}=\frac{1}{2}\cdot\frac{2}{3}\cdot\frac{3}{4}\cdots\frac{n-1}{n}\cdot\frac{n}{n+1}=\frac{1}{n+1}$;
* $\displaystyle\prod_{k=1}^n\frac{2k+1}{2k}=\frac{3}{2}\cdot\frac{5}{4}\cdot\frac{7}{6}\cdots\frac{2n-1}{2n-2}\cdot\frac{2n+1}{2n}=\frac{3\cdot5\cdot7\cdots(2n+1)}{2\cdot4\cdot6\cdots2n}$.
::::::
