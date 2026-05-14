(Sec:Series:GeneratingFunctions)=
# Generating functions

In this section we cover:

- Generating functions
- Harmonic numbers
- Fibonacci numbers

## Introduction

Something about number sequences and generating functions.

## Generating functions

Some definition and examples of generating functions.

## The harmonic numbers

We have seen the *harmonic series* $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$ as an example of a divergent series although the general term tends to zero. The partial sums

$$
H_n=\sum_{k=1}^n\frac{1}{k},\quad n=1,2,3,\ldots
$$

are called the **harmonic numbers**. The first ten are

\begin{align*}
&H_1=1,\quad H_2=1+\tfrac{1}{2}=\tfrac{3}{2},\quad H_3=\tfrac{3}{2}+\tfrac{1}{3}=\tfrac{11}{6},\quad H_4=\tfrac{11}{6}+\tfrac{1}{4}=\tfrac{25}{12},\\
&\quad H_5=\tfrac{25}{12}+\tfrac{1}{5}=\tfrac{137}{60},\quad H_6=\tfrac{137}{60}+\tfrac{1}{6}=\tfrac{49}{20},\quad H_7=\tfrac{49}{20}+\tfrac{1}{7}=\tfrac{363}{140},\\
&\quad\quad H_8=\tfrac{363}{140}+\tfrac{1}{8}=\tfrac{761}{280},\quad H_9=\tfrac{761}{280}+\tfrac{1}{9}=\tfrac{7129}{2520},\quad H_{10}=\tfrac{7129}{2520}+\tfrac{1}{10}=\tfrac{7381}{2520}.
\end{align*}
Note that

\begin{align*}
\sum_{n=1}^{\infty}\frac{H_n}{n^2}&=\sum_{n=1}^{\infty}\frac{1}{n^2}\sum_{k=1}^n\frac{1}{k}
=\sum_{k=1}^{\infty}\sum_{n=k}^{\infty}\frac{1}{kn^2}=\sum_{k=1}^{\infty}\sum_{n=0}^{\infty}\frac{1}{k(n+k)^2}\\
&=\sum_{k=1}^{\infty}\frac{1}{k^3}+\sum_{k=1}^{\infty}\sum_{n=1}^{\infty}\frac{1}{k(n+k)^2}.
\end{align*}
Now we have

\begin{align*}
\sum_{k=1}^{\infty}\sum_{n=1}^{\infty}\frac{1}{k(n+k)^2}
&=\frac{1}{2}\sum_{k=1}^{\infty}\sum_{n=1}^{\infty}\left(\frac{1}{k(n+k)^2}+\frac{1}{n(k+n)^2}\right)\\
&=\frac{1}{2}\sum_{k=1}^{\infty}\sum_{n=1}^{\infty}\frac{k+n}{kn(k+n)^2}
=\frac{1}{2}\sum_{k=1}^{\infty}\sum_{n=1}^{\infty}\frac{1}{kn(k+n)}\\
&=\frac{1}{2}\sum_{k=1}^{\infty}\sum_{n=1}^{\infty}\frac{1}{n^2}\left(\frac{1}{k}-\frac{1}{k+n}\right)=\frac{1}{2}\sum_{n=1}^{\infty}\frac{1}{n^2}\sum_{k=1}^{\infty}\left(\frac{1}{k}-\frac{1}{k+n}\right)\\
&=\frac{1}{2}\sum_{n=1}^{\infty}\frac{1}{n^2}\sum_{k=1}^n\frac{1}{k}=\frac{1}{2}\sum_{n=1}^{\infty}\frac{H_n}{n^2}.
\end{align*}
So we conclude that $\displaystyle\sum_{n=1}^{\infty}\frac{H_n}{n^2}=\sum_{k=1}^{\infty}\frac{1}{k^3}+\frac{1}{2}\sum_{n=1}^{\infty}\frac{H_n}{n^2}$, which implies that

$$
\displaystyle\sum_{n=1}^{\infty}\frac{H_n}{n^2}=2\sum_{k=1}^{\infty}\frac{1}{k^3}=2\zeta(3).
$$

Here $\zeta(s)$ denotes the *Riemann zeta function*, named after the German mathematician [Georg Friedrich Bernhard Riemann (1826-1866)](https://en.wikipedia.org/wiki/Bernhard_Riemann). The value of $\zeta(3)\approx1.202057$ is also known as *Apéry's constant*, named after the Greek-French mathematician [Roger Apéry (1916-1994)](https://en.wikipedia.org/wiki/Roger_Ap%C3%A9ry).

The harmonic numbers satisfy the recurrence relation

$$
H_{n+1}=H_n+\frac{1}{n+1},\quad n=1,2,3,\ldots\quad\text{with}\quad H_1=1.
$$

If we multiply by $x^{n+1}$ and sum over $n=1,2,3,\ldots$ we obtain

$$
\sum_{n=1}^{\infty}H_{n+1}x^{n+1}=\sum_{n=1}^{\infty}H_nx^{n+1}+\sum_{n=1}^{\infty}\frac{x^{n+1}}{n+1}.
$$

Let $G(x)=\displaystyle\sum_{n=1}^{\infty}H_nx^n$, which is called a *generating function* for the harmonic numbers, then we have

$$
\sum_{n=1}^{\infty}H_{n+1}x^{n+1}=\sum_{n=2}^{\infty}H_nx^n=G(x)-H_1x=G(x)-x.
$$

Further we have by integration of $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ for $|x|<1$ that

$$
-\ln(1-x)=C+\sum_{n=0}^{\infty}\frac{x^{n+1}}{n+1},\quad|x|<1.
$$

For $x=0$ this reads $0=-\ln(1)=C+0$ which implies that $C=0$. Hence we have

$$
\sum_{n=1}^{\infty}\frac{x^{n+1}}{n+1}=\sum_{n=0}^{\infty}\frac{x^{n+1}}{n+1}-x=-\ln(1-x)-x.
$$

Finally, we have

$$
G(x)-x=xG(x)-\ln(1-x)-x\quad\Longleftrightarrow\quad (1-x)G(x)=-\ln(1-x).
$$

This implies that $G(x)=\displaystyle-\frac{\ln(1-x)}{1-x}$. Applying the ratio test

$$
\lim_{n\to\infty}\left|\frac{H_{n+1}x^{n+1}}{H_nx^n}\right|=\lim_{n\to\infty}\frac{H_{n+1}}{H_n}|x|=\lim_{n\to\infty}\left(1+\frac{1}{(n+1)H_n}\right)|x|=|x|,
$$

we conclude that the radius of convergence is $R=1$. For instance, this implies that

$$
\sum_{n=1}^{\infty}\frac{H_n}{2^n}=G(\tfrac{1}{2})=-\frac{\ln\left(1-\frac{1}{2}\right)}{1-\frac{1}{2}}=-2\ln(\tfrac{1}{2})=2\ln(2).
$$

Since $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ and $-\ln(1-x)=\displaystyle\sum_{k=1}^{\infty}\frac{x^k}{k}$, the Cauchy product implies that

\begin{align*}
-\frac{\ln(1-x)}{1-x}&=\sum_{n=0}^{\infty}x^n\sum_{k=1}^{\infty}\frac{x^k}{k}=\sum_{n=0}^{\infty}\sum_{k=1}^{\infty}\frac{x^{n+k}}{k}
=\sum_{k=1}^{\infty}\sum_{n=0}^{\infty}\frac{x^{n+k}}{k}=\sum_{k=1}^{\infty}\sum_{n=k}^{\infty}\frac{x^n}{k}\\
&=\sum_{n=1}^{\infty}\left(\sum_{k=1}^n\frac{1}{k}\right)x^n=\sum_{n=1}^{\infty}H_nx^n,\quad |x| < 1.
\end{align*}
Differentiation leads to

$$
\sum_{n=1}^{\infty}nH_nx^{n-1}=\frac{1}{(1-x)^2}-\frac{\ln(1-x)}{(1-x)^2}=\frac{1-\ln(1-x)}{(1-x)^2},\quad|x| < 1.
$$

For instance, this implies that $\displaystyle\sum_{n=1}^{\infty}\frac{nH_n}{2^n}=\frac{1}{2}\cdot\frac{1-\ln(\frac{1}{2})}{(\frac{1}{2})^2}=2+2\ln(2)$.

Differentiation once more gives

\begin{align*}
\sum_{n=2}^{\infty}n(n-1)H_nx^{n-2}&=\frac{1-x+2(1-x)\left(1-\ln(1-x)\right)}{(1-x)^4}\\
&=\frac{1+2\left(1-\ln(1-x)\right)}{(1-x)^3}=\frac{3-2\ln(1-x)}{(1-x)^3},\quad|x|<1.
\end{align*}
For instance, this implies that $\displaystyle\sum_{n=2}^{\infty}\frac{n(n-1)H_n}{2^n}=\frac{1}{4}\cdot\frac{3-2\ln(\frac{1}{2})}{(\frac{1}{2})^3}=6+4\ln(2)$.

## A generating function for the Fibonacci numbers

Earlier we have seen that the sequence of *Fibonacci numbers* 

$$
1,1,2,3,5,8,13,21,34,55,89,\ldots
$$

is defined by $F_{n+2}=F_n+F_{n+1}$ for $n=1,2,3,\ldots$ with $F_1=F_2=1$.

For computational reasons we use $F_{n+2}=F_n+F_{n+1}$ for $n=0,1,2,\ldots$ with $F_0=0$ and $F_1=1$ instead.

Now we consider the *generating function* $G(x)=\displaystyle\sum_{n=1}^{\infty}F_nx^n=\sum_{n=0}^{\infty}F_nx^n$, then we have

\begin{align*}
x^2G(x)&=\sum_{n=0}^{\infty}F_nx^{n+2}=\sum_{n=0}^{\infty}F_{n+2}x^{n+2}-\sum_{n=0}^{\infty}F_{n+1}x^{n+2}\\
&=\sum_{n=1}^{\infty}F_nx^n-F_1x-x\sum_{n=1}^{\infty}F_nx^n=G(x)-x-xG(x). 
\end{align*}
This implies that

$$
(1-x-x^2)G(x)=x\quad\Longrightarrow\quad G(x)=\frac{x}{1-x-x^2}.
$$
 
In order to find the radius of convergence we apply the ratio test: for $x\neq0$ let $a_n=F_nx^n$, then we have:

$$ 
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim\limits_{n\to\infty}\left|\frac{F_{n+1}x^{n+1}}{F_nx^n}\right|
=\lim\limits_{n\to\infty}\frac{F_{n+1}}{F_n}|x|=\varphi|x|, 
$$ 
 
where $\displaystyle\lim\limits_{n\to\infty}\frac{F_{n+1}}{F_n}=\varphi=\frac{1+\sqrt{5}}{2}\approx1.618$ denotes the *golden ratio*.

Now the ratio test implies that the generating series is absolutely convergent if $|x| < \displaystyle\frac{1}{\varphi}=\varphi-1\approx0.618$.

For instance, this implies that $\displaystyle\sum_{n=1}^{\infty}\frac{F_n}{2^n}=G(\tfrac{1}{2})=\frac{\frac{1}{2}}{1-\frac{1}{2}-\frac{1}{4}}=2$.

Differentiation leads to

$$
\sum_{n=1}^{\infty}nF_nx^{n-1}=G'(x)=\frac{1-x-x^2+x+2x^2}{(1-x-x^2)^2}=\frac{1+x^2}{(1-x-x^2)^2}.
$$

For instance, this implies that $\displaystyle\sum_{n=1}^{\infty}\frac{nF_n}{2^n}=\tfrac{1}{2}G'(\tfrac{1}{2})=\frac{1+\frac{1}{4}}{2\left(1-\frac{1}{2}-\frac{1}{4}\right)^2}=10$.

Differentiating once more we obtain

\begin{align*}
\sum_{n=2}^{\infty}n(n-1)F_nx^{n-2}&=G''(x)\\
&=\frac{2x(1-x-x^2)^2-2(1-x-x^2)(-1-2x)(1+x^2)}{(1-x-x^2)^4}\\
&=\frac{2(x-x^2-x^3+1+x^2+2x+2x^3)}{(1-x-x^2)^3}=\frac{2(1+3x+x^3)}{(1-x-x^2)^3}.
\end{align*}
For instance, this implies that $\displaystyle\sum_{n=2}^{\infty}\frac{n(n-1)F_n}{2^n}=\tfrac{1}{4}G''(\tfrac{1}{2})=\frac{2\left(1+\frac{3}{2}+\frac{1}{8}\right)}{4\left(1-\frac{1}{2}-\frac{1}{4}\right)^3}=84$.

Finally, let's try to solve $G(x)=1$ with $\displaystyle|x|<\frac{1}{\varphi}=\varphi-1\approx0.618$:

\begin{align*}
\frac{x}{1-x-x^2}=1&\quad\Longleftrightarrow\quad x=1-x-x^2\\
&\quad\Longleftrightarrow\quad(x+1)^2=2\\
&\quad\Longleftrightarrow\quad x=-1\pm\sqrt{2}.
\end{align*}
Since $\sqrt{2}-1\approx0.414$ this leads to the remarkable result that $\displaystyle\sum_{n=1}^{\infty}\left(\sqrt{2}-1\right)^nF_n=1$.

## Grasple exercises

:::{todo}
Select exercises from Grasple and add them in {numref}`Sec:Series:GeneratingFunctions`.
:::

## Exercises

::::{exercise}
:label: Exc:Series:GeneratingFibonacciExercise
Find $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}\frac{F_n}{2^n}$, $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}\frac{nF_n}{2^n}$ and $\displaystyle\sum_{n=2}^{\infty}(-1)^n\frac{n(n-1)F_n}{2^n}$.
::::

:::{admonition} Solution of {numref}`Exc:Series:GeneratingFibonacciExercise`
:class: solution, dropdown
Note that

$$
\sum_{n=1}^{\infty}(-1)^{n-1}\frac{F_n}{2^n}=-G(-\tfrac{1}{2})=-\frac{-\frac{1}{2}}{1+\frac{1}{2}-\frac{1}{4}}=\frac{2}{5},
$$

$$
\sum_{n=1}^{\infty}(-1)^{n-1}\frac{nF_n}{2^n}=\tfrac{1}{2}G'(-\tfrac{1}{2})=\frac{1+\frac{1}{4}}{2(1+\frac{1}{2}-\frac{1}{4})^2}=\frac{2}{5}.
$$

and

$$
\sum_{n=2}^{\infty}(-1)^n\frac{n(n-1)F_n}{2^n}=\tfrac{1}{4}G''(-\tfrac{1}{2})=\frac{2(1-\frac{1}{2}-\frac{1}{8})}{4(1+\frac{1}{2}-\frac{1}{4})^3}=\frac{4}{25}.
$$

:::

::::{exercise}
:label: Exc:Series:GeneratingLucasExercise
Consider the sequence of *Lucas numbers* 

$$
1,3,4,7,11,18,29,47,76,123,199,\ldots
$$

is defined by $L_{n+2}=L_n+L_{n+1}$ for $n=1,2,3,\ldots$ with $L_1=1$ and $L_2=3$.

For computational reasons we use $L_{n+2}=L_n+L_{n+1}$ for $n=0,1,2,\ldots$ with $L_0=2$ and $L_1=1$ instead.

(a) Find the generating function $F(x)=\displaystyle\sum_{n=0}^{\infty}L_nx^n$.

(b) Find $\displaystyle\sum_{n=1}^{\infty}\frac{L_n}{2^n}$, $\displaystyle\sum_{n=1}^{\infty}\frac{nL_n}{2^n}$ and $\displaystyle\sum_{n=2}^{\infty}\frac{n(n-1)L_n}{2^n}$.

(c) Find $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}\frac{L_n}{2^n}$ and $\displaystyle\sum_{n=1}^{\infty}\frac{L_n}{3^n}$.

(d) Find $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{nL_n}{2^n}$ and $\displaystyle\sum_{n=2}^{\infty}(-1)^n\frac{n(n-1)L_n}{2^n}$.
::::

:::{admonition} Solution of {numref}`Exc:Series:GeneratingLucasExercise`
:class: solution, dropdown
(a) Using $F(x)=\displaystyle\sum_{n=0}^{\infty}L_nx^n$ we obtain

\begin{align*}
x^2F(x)&=\sum_{n=0}^{\infty}L_nx^{n+2}=\sum_{n=0}^{\infty}L_{n+2}x^{n+2}-x\sum_{n=0}^{\infty}L_{n+1}x^{n+1}\\
&=\sum_{n=0}^{\infty}L_nx^n-L_0-L_1x-x\left(\sum_{n=0}^{\infty}L_nx^n-L_0\right)\\
&=F(x)-2-x-x\left(F(x)-2\right).
\end{align*}
This implies that

$$
(1-x-x^2)F(x)=2+x-2x=2-x\quad\Longrightarrow\quad F(x)=\frac{2-x}{1-x-x^2}.
$$

In order to find the radius of convergence, we apply the ratio test: for $x\neq0$ let $a_n=L_nx^n$, then we have:

$$
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim\limits_{n\to\infty}\left|\frac{L_{n+1}x^{n+1}}{L_nx^n}\right|
=\lim\limits_{n\to\infty}\frac{L_{n+1}}{L_n}|x|=\varphi|x|,
$$

where $\displaystyle\lim\limits_{n\to\infty}\frac{L_{n+1}}{L_n}=\varphi=\frac{1+\sqrt{5}}{2}\approx1.618$ denotes the *golden ratio*.

Now the ratio test implies that the generating series is absolutely convergent for $|x| < \displaystyle\frac{1}{\varphi}=\varphi-1\approx0.618$.

(b) Hence, we have $\displaystyle\sum_{n=0}^{\infty}\frac{L_n}{2^n}=F(\tfrac{1}{2})=\frac{\frac{3}{2}}{1-\frac{1}{2}-\frac{1}{4}}=6$. This implies that $\displaystyle\sum_{n=1}^{\infty}\frac{L_n}{2^n}=4$.

Differentiation leads to

$$
\sum_{n=1}^{\infty}nL_nx^{n-1}=F'(x)=\frac{-1+x+x^2+(1+2x)(2-x)}{(1-x-x^2)^2}=\frac{1+4x-x^2}{(1-x-x^2)^2}.
$$

Hence, we have $\displaystyle\sum_{n=1}^{\infty}\frac{nL_n}{2^n}=\tfrac{1}{2}F'(\tfrac{1}{2})=\frac{1+2-\frac{1}{4}}{2\left(1-\frac{1}{2}-\frac{1}{4}\right)^2}=22$.

Differentiating once more, we obtain

\begin{align*}
&\sum_{n=2}^{\infty}n(n-1)L_nx^{n-2}=F''(x)\\
&=\frac{(4-2x)(1-x-x^2)^2-2(1-x-x^2)(-1-2x)(1+4x-x^2)}{(1-x-x^2)^4}\\
&=\frac{2(2-x+1+4x-x^2+2x+8x^2-2x^3)}{(1-x-x^2)^3}=\frac{2(3+3x+6x^2-x^3)}{(1-x-x^2)^3}.
\end{align*}
Hence, we have $\displaystyle\sum_{n=2}^{\infty}\frac{n(n-1)L_n}{2^n}=\tfrac{1}{4}F''(\tfrac{1}{2})=\frac{2\left(3+\frac{3}{2}+\frac{3}{2}-\frac{1}{8}\right)}{4\left(1-\frac{1}{2}-\frac{1}{4}\right)^3}=188$.

(c) For $x=-\frac{1}{2}$ we obtain: $\displaystyle\sum_{n=0}^{\infty}\left(-\tfrac{1}{2}\right)^nL_n=F(-\tfrac{1}{2})=2$. This implies that $\displaystyle\sum_{n=1}^{\infty}\left(-\tfrac{1}{2}\right)^nL_n=0$ and therefore $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}\frac{L_n}{2^n}=0$.

For $x=\frac{1}{3}$ we obtain: $\displaystyle\sum_{n=0}^{\infty}\frac{L_n}{3^n}=F(\tfrac{1}{3})=3$. This implies that $\displaystyle\sum_{n=1}^{\infty}\frac{L_n}{3^n}=1$.

(d) We have

$$
\sum_{n=1}^{\infty}(-1)^n\frac{nL_n}{2^n}=-\tfrac{1}{2}F'(-\tfrac{1}{2})=-\frac{1-2-\frac{1}{4}}{2(1+\frac{1}{2}-\frac{1}{4})^2}=\frac{2}{5}
$$

and

$$
\sum_{n=2}^{\infty}(-1)^n\frac{n(n-1)L_n}{2^n}=\tfrac{1}{4}F''(-\tfrac{1}{2})=\frac{2(3-\frac{3}{2}+\frac{3}{2}+\frac{1}{8})}{4(1+\frac{1}{2}-\frac{1}{4})^3}=\frac{4}{5}.
$$

:::
