# Tests for general series 2

In this section we cover:

- Ratio test
- Root test
- Rearrangements

Error estimations included in each test where applicable.

## Introduction

In {numref}`Chapter:Series:Introduction` we discussed one single test that can be used to determine whether a general series is divergent, namely the test for divergence, {prf:ref}`Thm:Series:GeneralTermCorollary`. In {numref}`Sec:Series:SpecialSeries` we discussed several special series, which was continued in {numref}`Sec:Series:PositiveSeries`.

All of these series and their corresponding tests and theorems limit their applicability. For example, the alternating series test from {prf:ref}`Thm:Series:AlternatingSeriesTest` only works for alternating series, and the tests from {numref}`Sec:Series:PositiveSeries` only work for positive series. Also not every series is might be a geometric or $p$-series, so also the theorems {prf:ref}`Thm:Series:GeometricSeries` and {prf:ref}`Thm:Series:pSeries` have a limited applicability.

In this section we will give some tests that can be used to determine whether a general series is absolutely convergent or divergent. These tests work for all series, but they are not always conclusive.

Let us repeat the definition of absolute convergence, since it is important for the tests in this section:

:::{repeat} {prf:ref}`Def:Series:AbsoluteConvergence`
:::

## The ratio test

::::::{prf:Theorem} Ratio test
:label: Thm:Series:RatioTest
Consider the series $\displaystyle\sum a_n$ with $a_n\in\mathbb{R}$ for all $n$. Then

1) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L<1$, then the series $\displaystyle\sum a_n$ is absolutely convergent;

2) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\infty$, then the series $\displaystyle\sum a_n$ is divergent;

3) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=1$, then this test is inconclusive: the series $\displaystyle\sum a_n$ might be convergent or divergent.
::::::

::::::{note}
Sometimes the ratio test is called **d'Alembert's criterion**, named after the French mathematician  [Jean-Baptiste le Rond d'Alembert (1717-1783)](https://en.wikipedia.org/wiki/Jean_le_Rond_d%27Alembert).
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:RatioTest`
:class: tudproof, dropdown
1) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L<1$ we can choose a number $r$ such that $L<r<1$. Then $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L$ implies that there exists an integer $N$ such that $\displaystyle\left|\frac{a_{n+1}}{a_n}\right| < r$ for all $n\geq N$ or equivalently $|a_{n+1}| < |a_n|r$ for all $n\geq N$. Hence we have:

\begin{align*}
&|a_{N+1}| < |a_N|r,\quad |a_{N+2}| < |a_{N+1}|r < |a_N|r^2,\\
&{}\quad|a_{N+3}| < |a_{N+2}|r < |a_N|r^3,\quad\ldots.
\end{align*}
So we have: $|a_{N+k}| < |a_N|r^k$ for $k=1,2,3,\ldots$. Now the series $\displaystyle\sum_{k=1}^{\infty}|a_N|r^k$ is convergent because it is a geometric series with common ratio $r$ and $0 < r < 1$. This implies that the series $\displaystyle\sum_{n=N+1}^{\infty}|a_n|=\sum_{k=1}^{\infty}|a_{N+k}|$ is convergent. Hence the series $\displaystyle\sum|a_n|$ is convergent.

2) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\infty$ we can choose a number $r$ such that $1<r<L$. Then $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L$ implies that the ratio $\displaystyle\left|\frac{a_{n+1}}{a_n}\right|$ will eventually be greater than $r$, that is: there exists an integer $N$ such that $\displaystyle\left|\frac{a_{n+1}}{a_n}\right|>r$ for all $n\geq N$. This implies that $|a_{N+k}|>r^{N+k}$ for $k=0,1,2,\ldots$. This implies that $\displaystyle\sum_{k=0}^{\infty}|a_{N+k}|$ is divergent, since $\displaystyle\sum_{k=1}^{\infty}r^{N+k}$ is a geometric series with common ratio $r>1$ which is divergent.

3) In order to show that the test is inconclusive if $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=1$, consider the divergent series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$ and the convergent series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$. Note that

$$
\lim\limits_{n\to\infty}\frac{\dfrac{1}{n+1}}{\dfrac{1}{n}}=\lim\limits_{n\to\infty}\frac{n}{n+1}=1
$$

and

$$
\lim\limits_{n\to\infty}\frac{\dfrac{1}{(n+1)^2}}{\dfrac{1}{n^2}}=\lim\limits_{n\to\infty}\frac{n^2}{(n+1)^2}=\lim\limits_{n\to\infty}\left(\frac{n}{n+1}\right)^2=1.
$$

:::

::::::{prf:example}
1) Consider the alternating series $\displaystyle\sum_{n=0}^{\infty}(-1)^n\frac{2n+1}{2^n}$. Let $a_n=\displaystyle(-1)^n\frac{2n+1}{2^n}$, then we have:

\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|(-1)^{n+1}\frac{2n+3}{2^{n+1}}\cdot(-1)^n\frac{2^n}{2n+1}\right|\\
&=\lim\limits_{n\to\infty}\frac{2n+3}{2n+1}\cdot\frac{1}{2}=\frac{1}{2}<1.
\end{align*}
This implies that the series is absolutely convergent.

2) Consider the series $\displaystyle\sum_{n=0}^{\infty}\frac{n!}{5^n}$. Let $a_n=\displaystyle\frac{n!}{5^n}$, then we have:

$$
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim\limits_{n\to\infty}\left|\frac{(n+1)!}{5^{n+1}}\cdot\frac{5^n}{n!}\right|
=\lim\limits_{n\to\infty}\frac{1}{5}(n+1)=\infty.
$$ 
 
This implies that the series is divergent.
::::::

## The root test

::::::{prf:Theorem} Root test
:label: Thm:Series:RootTest
Consider the series $\displaystyle\sum a_n$ with $a_n\in\mathbb{R}$ for all $n$. Then

1) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L<1$, then the series $\displaystyle\sum a_n$ is absolutely convergent;

2) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\infty$, then the series $\displaystyle\sum a_n$ is divergent;

3) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=1$, then this test is inconclusive: the series $\displaystyle\sum a_n$ might be convergent or divergent.
::::::

::::::{note}
Sometimes the root test is called **Cauchy's criterion**, named after the French mathematician  [Augustin-Louis Cauchy (1789-1857)](https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy).
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:RootTest`
:class: tudproof, dropdown
1) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L<1$ we can choose a number $r$ such that $L<r<1$. Then $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L$ implies that there exists an integer $N$ such that $\displaystyle\sqrt[n]{|a_n|} < r$. This implies that

$$
\sqrt[N+k]{|a_{N+k}|} < r\quad\Longrightarrow\quad |a_{N+k}| < r^{N+k},\quad k=0,1,2,\ldots.
$$

This implies that $\displaystyle\sum_{k=0}^{\infty}|a_{N+k}|$ is convergent, since $\displaystyle\sum_{k=0}^{\infty}r^{N+k}$ is a geometric series with common ratio $r$ with $0 < r < 1$ which is convergent.

2) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\infty$, we can choose a number $r$ such that $1<r<L$. Then $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L$ implies that $\displaystyle\sqrt[n]{|a_n|}$ will eventually be greater than $r$, that is: there exists an integer $N$ such that $\displaystyle\sqrt[n]{|a_n|}>r$ for all $n\geq N$. This implies that

$$
\sqrt[N+k]{|a_{N+k}|} > r\quad\Longrightarrow\quad |a_{N+k}| > r^{N+k},\quad k=0,1,2,\ldots.
$$

This implies that $\displaystyle\sum_{k=0}^{\infty}|a_{N+k}|$ is divergent, since $\displaystyle\sum_{k=0}^{\infty}r^{N+k}$ is a geometric series with common ratio $r$ with $r > 1$ which is divergent.

3) In order to show that the test is inconclusive if $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=1$, consider the series $\displaystyle\sum a_n$ with $a_n=e^{-\sqrt{n}}$ and the series $\displaystyle\sum b_n$ with $b_n=\left(1+\dfrac{1}{n}\right)^n$. Then we have

$$
\lim_{n\to\infty}\sqrt[n]{|a_n|}=\lim_{n\to\infty}e^{-\frac{1}{\sqrt{n}}}=e^0=1
$$

and

$$
\lim_{n\to\infty}\sqrt[n]{|b_n|}=\lim_{n\to\infty}\left(1+\frac{1}{n}\right)=1+0=1.
$$

The series $\displaystyle\sum a_n$ is convergent due to the integral test, since by using the substitution $x=t^2$ and integration by parts we have

\begin{align*}
\int_0^{\infty}e^{-\sqrt{x}}\,dx&=\int_0^{\infty}e^{-t}\,2t\,dt=-\int_0^{\infty}2t\,de^{-t}\\
&=-2te^{-t}\bigg|_0^{\infty}+2\int_0^{\infty}e^{-t}\,dt=0-2e^{-t}\bigg|_0^{\infty}=2.
\end{align*}
The series $\displaystyle\sum b_n$ is divergent, since 

$$
\lim_{n\to\infty}b_n=\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e\neq0.
$$

:::

::::::{prf:example}
1) Consider the alternating series $\displaystyle\sum_{n=0}^{\infty}\left(\frac{2n+1}{3n+4}\right)^n$. Let $a_n=\displaystyle\left(\frac{2n+1}{3n+4}\right)^n$, then we have:

$$ 
\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\lim\limits_{n\to\infty}\left|\frac{2n+1}{3n+4}\right|=\frac{2}{3}<1.
$$ 
 
This implies that the series is absolutely convergent.

2) Consider the series $\displaystyle\sum_{n=1}^{\infty}\left(\frac{2n+1}{n}\right)^n$. Let $a_n=\displaystyle\frac{2n+1}{n}$, then we have:

$$
\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\lim\limits_{n\to\infty}\left|\frac{2n+1}{n}\right|=2.
$$ 
 
This implies that the series is divergent.
::::::
