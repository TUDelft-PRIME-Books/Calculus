(Sec:Series:TestsForGeneralSeries)=
# Tests for general series

## Introduction

In {numref}`Chapter:Series:Introduction` we discussed one single test that can be used to determine whether a general series is divergent, namely the test for divergence, {prf:ref}`Thm:Series:GeneralTermCorollary`. In {numref}`Sec:Series:SpecialSeries` we discussed several special series, which was continued in {numref}`Sec:Series:PositiveSeries`.

All of these series and their corresponding tests and theorems limit their applicability. For example, the alternating series test from {prf:ref}`Thm:Series:AlternatingSeriesTest` only works for alternating series, and the tests from {numref}`Sec:Series:PositiveSeries` only work for positive series. Also not every series is might be a geometric or $p$-series, so also the theorems {prf:ref}`Thm:Series:GeometricSeries` and {prf:ref}`Thm:Series:pSeries` have a limited applicability.

In this section we will give some tests that can be used to determine whether a general series is absolutely convergent or divergent. These tests work for all series, but they are not always conclusive.

Let us repeat the definitions of convergence, divergence, absolute convergence and conditional convergence, since those are important for the tests in this section:

:::{fetch} {prf:ref}`Def:Series:ConvergenceSum`
:::

:::{fetch} {prf:ref}`Def:Series:AbsoluteConvergence`
:::

:::{fetch} {prf:ref}`Def:Series:RelativeConvergence`
:::

## Reusing existing tests

Because taking the absolute value of the terms of a series creates a new series with only positive terms, we can apply the tests for positive series from {numref}`Sec:Series:PositiveSeries` to determine whether the original series is absolutely convergent. If taking the absolute value of the terms of a series creates a new series that is a geometric series or a $p$-series, we can use the tests for geometric series and $p$-series from {prf:ref}`Thm:Series:GeometricSeries` and {prf:ref}`Thm:Series:pSeries` to determine whether the original series is absolutely convergent. The same holds if the new series created by taking the absolute value of the terms of a series is a telescoping series, which means we can apply the test for telescoping series from {prf:ref}`Thm:Series:SumTelescopingSeries` to determine whether the original series is absolutely convergent.

However, what we cannot do with these tests, is conclude that a series is divergent if the series created by taking the absolute value of the terms of a series is divergent, which is shown in the next example.

:::{prf:example}
:label: Ex:Series:NoConclusionFromAbsoluteValue

Consider the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$.

If we take the absolute value of the terms of the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$, we get the *harmonic series* $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$, which is a divergent $p$-series with $p=1$ by {prf:ref}`Thm:Series:pSeries`. So we conclude that the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$ is not absolutely convergent.

It would be false to conclude at this moment that the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$ is divergent, because we only investigated the absolute convergence, and by {prf:ref}`Def:Series:RelativeConvergence` a series can be conditionally convergent, which means that it is convergent but not absolutely convergent.

Note that the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$ is an alternating series. Using {prf:ref}`Thm:Series:AlternatingSeriesTest` with $b_n=\dfrac{1}{n}$, we conclude that the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$ is convergent.

This means, by {prf:ref}`Def:Series:RelativeConvergence`, that the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$ is conditionally convergent, and not divergent.
:::

In conclusion:

:::{prf:remark}
If the series $\displaystyle\sum|a_n|$ is divergent, then the series $\displaystyle\sum a_n$ is not absolutely convergent, but it might still be convergent or divergent.
:::

This means that you have to be careful when you apply a test from {numref}`Sec:Series:SpecialSeries` or {numref}`Sec:Series:PositiveSeries` to determine whether a series is absolutely convergent, because if the test concludes that the series $\displaystyle\sum|a_n|$ is divergent, then you cannot conclude that the original series $\displaystyle\sum a_n$ is divergent, since it might still be conditionally convergent. This means you might have to apply other tests to make conclusions.

Luckily, there are some tests that can be applied to determine whether a series is absolutely convergent or divergent, and only in some special cases you have to use a test from {numref}`Sec:Series:SpecialSeries` or {numref}`Sec:Series:PositiveSeries` to determine whether a series is absolutely convergent. These tests are the ratio test and the root test, which we will discuss in the next two subsections. 

## The ratio test

To introduce the ratio test, first consider the following theorem again:

:::{fetch} {prf:ref}`Thm:Series:GeneralTerm`
:::

A direct consequence of this theorem is that if a series $\displaystyle\sum a_n$ is absolutely convergent, so $\displaystyle\sum|a_n|$ is convergent, then we must have

$$
\lim\limits_{n\to\infty}|a_n|=0.
$$

This implies that the terms of the sequence $\{|a_n|\}$ become smaller and smaller and therefore

$$
|a_{n+1}|<|a_n|\quad\Longrightarrow\quad\left|\frac{a_{n+1}}{a_n}\right|\leq\frac{|a_{n+1}|}{|a_n|}<1
$$

for $n$ large enough. This gives rise to a very useful test to determine whether a series is absolutely convergent or divergent, and it can be applied to all series. This test is called the ratio test:

::::::{prf:Theorem} Ratio test
:label: Thm:Series:RatioTest
Consider the series $\displaystyle\sum a_n$ with $a_n\in\mathbb{R}$ for all $n$. Then

1) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L<1$, then the series $\displaystyle\sum a_n$ is absolutely convergent;

2) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\infty$, then the series $\displaystyle\sum a_n$ is divergent;

3) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=1$, then this test is inconclusive: the series $\displaystyle\sum a_n$ might be absolutely convergent, conditionally convergent or divergent.

4) In all other cases, this test is also inconclusive: the series $\displaystyle\sum a_n$ might be absolutely convergent, conditionally convergent or divergent.
::::::

::::::{note}
Sometimes the ratio test is called **d'Alembert's criterion**, named after the French mathematician  [Jean-Baptiste le Rond d'Alembert (1717-1783)](https://en.wikipedia.org/wiki/Jean_le_Rond_d%27Alembert).
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:RatioTest`
:class: tudproof, dropdown
1) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L<1$ we can choose a number $r$ such that $L<r<1$. Then $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L$ implies that there exists an integer $N$ such that $\displaystyle\left|\frac{a_{n+1}}{a_n}\right| < r$ for all $n\geq N$ or equivalently $|a_{n+1}| < |a_n|r$ for all $n\geq N$. Hence we have:

   \begin{align*}
   &|a_{N+1}| < |a_N|r,\quad |a_{N+2}| < |a_{N+1}|r < |a_N|r^2,\\
   &{}\quad|a_{N+3}| < |a_{N+2}|r < |a_N|r^3,\quad\ldots
   \end{align*}
  
   So we have: $|a_{N+k}| < |a_N|r^k$ for $k=1,2,3,\ldots$. Now the series $\displaystyle\sum_{k=1}^{\infty}|a_N|r^k$ is convergent because it is a geometric series with common ratio $r$ and $0 < r < 1$. This implies that the series $\displaystyle\sum_{n=N+1}^{\infty}|a_n|=\sum_{k=1}^{\infty}|a_{N+k}|$ is convergent. Hence the series $\displaystyle\sum|a_n|$ is convergent.

2) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\infty$ we can choose a number $r$ such that $1<r<L$. Then $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L$ implies that the ratio $\displaystyle\left|\frac{a_{n+1}}{a_n}\right|$ will eventually be greater than $r$, that is: there exists an integer $N$ such that $\displaystyle\left|\frac{a_{n+1}}{a_n}\right|>r$ for all $n\geq N$. This implies that $|a_{N+k}|>r^{N+k}$ for $k=0,1,2,\ldots$. This implies that $\displaystyle\sum_{k=0}^{\infty}|a_{N+k}|$ is divergent, since $\displaystyle\sum_{k=1}^{\infty}r^{N+k}$ is a geometric series with common ratio $r>1$ which is divergent.

3) See {prf:ref}`Ex:Series:RatioTest3` for a proof of this part of the test.

4) The "in all other cases" part indicates that $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|$ does not exist ánd $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|\neq\infty$. See {prf:ref}`Ex:Series:RatioTest4` for a proof of this part of the test.
:::

After the neat proof above, we turn to some examples to show how to apply the ratio test in practice. Note that the ratio test can be applied to all series, but it is not always conclusive, so you might have to apply other tests if the ratio test is inconclusive.

:::{prf:example}
:label: Ex:Series:RatioTest1
Consider the alternating series $\displaystyle\sum_{n=0}^{\infty}(-1)^n\frac{2n+1}{2^n}$.

Let $a_n=\displaystyle(-1)^n\frac{2n+1}{2^n}$, then we have:

\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|(-1)^{n+1}\frac{2n+3}{2^{n+1}}\cdot(-1)^n\frac{2^n}{2n+1}\right|\\
&=\lim\limits_{n\to\infty}\frac{2n+3}{2n+1}\cdot\frac{1}{2} \\
&=\frac{1}{2} \\
&<1.
\end{align*}

This implies that the series is absolutely convergent.

:::

:::{prf:example}
:label: Ex:Series:RatioTest2
Consider the series $\displaystyle\sum_{n=0}^{\infty}\frac{n!}{5^n}$.

Let $a_n=\displaystyle\frac{n!}{5^n}$, then we have:

\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right| &= \lim\limits_{n\to\infty}\left|\frac{(n+1)!}{5^{n+1}}\cdot\frac{5^n}{n!}\right| \\
&=\lim\limits_{n\to\infty}\frac{1}{5}(n+1) \\
&=\infty.
\end{align*}
 
This implies that the series is divergent.
::::::

:::{prf:example}
:label: Ex:Series:RatioTest3

In order to show that the ratio test cannot be conclusive if $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=1$, consider the divergent series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$ and the convergent series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$. Note that

$$
\lim\limits_{n\to\infty}\frac{\dfrac{1}{n+1}}{\dfrac{1}{n}}=\lim\limits_{n\to\infty}\frac{n}{n+1}=1
$$

and

$$
\lim\limits_{n\to\infty}\frac{\dfrac{1}{(n+1)^2}}{\dfrac{1}{n^2}}=\lim\limits_{n\to\infty}\frac{n^2}{(n+1)^2}=\lim\limits_{n\to\infty}\left(\frac{n}{n+1}\right)^2=1.
$$

This shows that the test is inconclusive if $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=1$, as we have given one example for which the series is divergent and one example for which the series is convergent, while in both cases we have $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=1$.
:::

:::{prf:example}
:label: Ex:Series:RatioTest4

In order to show that the ratio test is inconclusive if $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|$ does not exist and does not equal $\infty$, consider the series $\displaystyle\sum_{n=1}^{\infty}a_n$ and the series $\displaystyle\sum_{n=1}^{\infty}b_n$ with

$$
a_n = \begin{cases}
\frac{1}{2^{n}} & \text{if }n\text{ is odd},\\
\frac{1}{2^{n-2}} & \text{if }n\text{ is even},
\end{cases}
\quad\text{and}\quad
b_n = \begin{cases}
2^{n-1} & \text{if }n\text{ is odd},\\
2^{n-3} & \text{if }n\text{ is even}.
\end{cases}
$$

We first consider the series $\displaystyle\sum_{n=1}^{\infty}a_n$. If $n=2m$ for some positive integer $m$ (so $n$ is even), then we have

$$
\left|\frac{a_{n+1}}{a_n}\right|=\frac{a_{2m+1}}{a_{2m}}=\frac{\dfrac{1}{2^{2m-1}}}{\dfrac{1}{2^{2m}}}=\frac{2^{2m}}{2^{2m-1}}=2.
$$

If however $n=2m-1$ for some positive integer $m$ (so $n$ is odd), then we have

$$
\left|\frac{a_{n+1}}{a_n}\right|=\frac{a_{2m}}{a_{2m-1}}=\frac{\dfrac{1}{2^{2m}}}{\dfrac{1}{2^{2m-3}}}=\frac{2^{2m-3}}{2^{2m}}=\frac{1}{2^3}=\frac{1}{8}.
$$

This means that the ratio $\displaystyle\left|\frac{a_{n+1}}{a_n}\right|$ does not have a limit as $n$ tends to infinity, since for even $n$ the ratio equals 2 and for odd $n$ the ratio equals $\dfrac{1}{8}$.

Similarly, we can show that the ratio $\displaystyle\left|\frac{b_{n+1}}{b_n}\right|$ satisfies

$$
\left|\frac{b_{n+1}}{b_n}\right|=\begin{cases}
\frac12 & \text{if }n\text{ is odd},\\
8 & \text{if }n\text{ is even},
\end{cases}
$$

so the ratio $\displaystyle\left|\frac{b_{n+1}}{b_n}\right|$ also does not have a limit as $n$ tends to infinity, since for even $n$ the ratio is equal to 8 and for odd $n$ the ratio is equal to $\dfrac{1}{2}$.

For the series $\displaystyle\sum_{n=1}^{\infty}b_n$ we have

$$
\lim_{n\to\infty}b_{n}=\infty,
$$

so by the divergence test, the series $\displaystyle\sum_{n=1}^{\infty}b_n$ is divergent.

However, for the series $\displaystyle\sum_{n=1}^{\infty}a_n$ we have

\begin{align*}
\sum_{n=1}^{\infty}a_n&=\sum_{\substack{n=1\\n\text{ odd}}}^{\infty}a_n+\sum_{\substack{n=1\\n\text{ even}}}^{\infty}a_n\\
&=\sum_{\substack{n=1\\n\text{ odd}}}^{\infty}\frac{1}{2^{n}}+\sum_{\substack{n=1\\n\text{ even}}}^{\infty}\frac{1}{2^{n-2}}\\
&=\sum_{m=1}^{\infty}\frac{1}{2^{2m-1}}+\sum_{m=1}^{\infty}\frac{1}{2^{2m-2}} \\
&=\sum_{m=1}^{\infty}2\left(\frac{1}{4}\right)^{m}+\sum_{m=1}^{\infty}4\left(\frac{1}{4}\right)^{m} \\
&=\sum_{m=1}^{\infty}\frac{1}{2}\left(\frac{1}{4}\right)^{m-1}+\sum_{m=1}^{\infty}\left(\frac{1}{4}\right)^{m-1} \\
&= \frac{\frac{1}{2}}{1-\frac{1}{4}}+\frac{1}{1-\frac{1}{4}} \\
&=\frac{2}{3}+\frac{4}{3} \\
&=2.
\end{align*}

This shows that the series $\displaystyle\sum_{n=1}^{\infty}a_n$ is (absolutely) convergent, while the series $\displaystyle\sum_{n=1}^{\infty}b_n$ is divergent, even though the ratios $\displaystyle\left|\frac{a_{n+1}}{a_n}\right|$ and $\displaystyle\left|\frac{b_{n+1}}{b_n}\right|$ do not have a limit as $n$ tends to infinity.

This shows that the ratio test is inconclusive if $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|$ does not exist, as we have given one example for which the series is divergent and one example for which the series is convergent, while in both cases we have that the ratio does not have a limit as $n$ tends to infinity.

:::

In some cases where the ratio test fails to give a conclusion, the root test, which we will discuss in the next subsection, might be conclusive, so it is always good to try both tests if one of them fails to give a conclusion.

## The root test

In {prf:ref}`Ex:Series:RatioTest4` we used the series $\displaystyle\sum_{n=1}^{\infty}a_n$ with

$$
a_n = \begin{cases}
\frac{1}{2^{n}} & \text{if }n\text{ is odd},\\
\frac{1}{2^{n-2}} & \text{if }n\text{ is even},
\end{cases}
$$

and showed that it converges by splitting the series into two subseries, one with the odd terms and one with the even terms. These two series where both geometric series, so we could easily determine whether they were convergent or divergent.

For the simple (shifted) geometric series $\displaystyle\sum_{n=0}^{\infty}r^{n}$, each term satisfies

$$
\sqrt[n]{|r^{n}|}=\sqrt[n]{|r|^n}=|r|^{\frac{n}{n}}=|r|.
$$

This also means that

$$
\lim_{n\to\infty}\sqrt[n]{|r^{n}|}=\lim_{n\to\infty}|r|=|r|.
$$

By {prf:ref}`Thm:Series:GeometricSeries` we know that the series $\displaystyle\sum_{n=0}^{\infty}r^{n}$ is convergent if $|r|<1$ and divergent if $|r|\geq 1$. This means that the limit $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|r^{n}|}$ can be used to determine whether the series $\displaystyle\sum_{n=0}^{\infty}r^{n}$ is convergent or divergent.

The _root test_ is a generalisation of this idea, where we use the limit $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}$ to determine whether the series $\displaystyle\sum a_n$ is absolutely convergent or divergent. This test is called the root test:

::::::{prf:Theorem} Root test
:label: Thm:Series:RootTest
Consider the series $\displaystyle\sum a_n$ with $a_n\in\mathbb{R}$ for all $n$. Then

1) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L<1$, then the series $\displaystyle\sum a_n$ is absolutely convergent;

2) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\infty$, then the series $\displaystyle\sum a_n$ is divergent;

3) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=1$, then this test is inconclusive: the series $\displaystyle\sum a_n$ might be convergent or divergent.

4) In all other cases, this test is inconclusive: the series $\displaystyle\sum a_n$ might be convergent or divergent.
::::::

::::::{note}
Sometimes the root test is called **Cauchy's criterion**, named after the French mathematician  [Augustin-Louis Cauchy (1789-1857)](https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy).
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:RootTest`
:class: tudproof, dropdown
1) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L<1$ we can choose a number $r$ such that $L<r<1$. Then $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L$ implies that there exists an integer $N$ such that $\displaystyle\sqrt[n]{|a_n|} < r$. This implies that

   $$
   \sqrt[N+k]{|a_{N+k}|} < r\quad\Longrightarrow\quad |a_{N+k}| < r^{N+k},\quad k=0,1,2,\ldots
   $$

   This implies that $\displaystyle\sum_{k=0}^{\infty}|a_{N+k}|$ is convergent, since $\displaystyle\sum_{k=0}^{\infty}r^{N+k}$ is a geometric series with common ratio $r$ with $0 < r < 1$ which is convergent.

2) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\infty$, we can choose a number $r$ such that $1<r<L$. Then $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L$ implies that $\displaystyle\sqrt[n]{|a_n|}$ will eventually be greater than $r$, that is: there exists an integer $N$ such that $\displaystyle\sqrt[n]{|a_n|}>r$ for all $n\geq N$. This implies that

   $$
   \sqrt[N+k]{|a_{N+k}|} > r\quad\Longrightarrow\quad |a_{N+k}| > r^{N+k},\quad k=0,1,2,\ldots
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

   The series $\displaystyle\sum a_n$ is convergent due to the integral test, since by using the substitution $t=\sqrt{x}$ and integration by parts we have

   \begin{align*}
   \int_0^{\infty}e^{-\sqrt{x}}\,dx&=\int_0^{\infty}e^{-t}\,2t\,dt\\
   &=-2te^{-t}\bigg|_0^{\infty}+2\int_0^{\infty}e^{-t}\,dt \\
   &=0-2e^{-t}\bigg|_0^{\infty}\\
   &=2.
   \end{align*}

   The series $\displaystyle\sum b_n$ is divergent, since 

   $$
   \lim_{n\to\infty}b_n=\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e\neq0.
   $$

4) See {prf:ref}`Ex:Series:RootTest4` for a proof of this part of the test.

:::

:::{prf:example}
:label: Ex:Series:RootTest1
Consider the alternating series $\displaystyle\sum_{n=0}^{\infty}\left(\frac{2n+1}{3n+4}\right)^n$. Let $a_n=\displaystyle\left(\frac{2n+1}{3n+4}\right)^n$, then we have:

$$ 
\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\lim\limits_{n\to\infty}\left|\frac{2n+1}{3n+4}\right|=\frac{2}{3}<1.
$$ 
 
This implies that the series is absolutely convergent.
:::

:::{prf:example}
:label: Ex:Series:RootTest2
Consider the series $\displaystyle\sum_{n=1}^{\infty}\left(\frac{2n+1}{n}\right)^n$. Let $a_n=\displaystyle\frac{2n+1}{n}$, then we have:

$$
\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\lim\limits_{n\to\infty}\left|\frac{2n+1}{n}\right|=2.
$$ 
 
This implies that the series is divergent.
:::

:::{prf:example}
:label: Ex:Series:RootTest3
We revisit the two series from {prf:ref}`Ex:Series:RatioTest4` to show that the root test is conclusive for these series. Let $a_n$ and $b_n$ be as defined in {prf:ref}`Ex:Series:RatioTest4`, then we have for $n$ odd that

$$
\lim_{\substack{n\to\infty\\n\text{ odd}}}\sqrt[n]{|a_n|}=\lim_{\substack{n\to\infty\\n\text{ odd}}}\sqrt[n]{\left|\frac{1}{2^n}\right|}=\lim_{\substack{n\to\infty\\n\text{ odd}}}\frac{1}{2}=\frac{1}{2},
$$

and for $n$ even that

$$
\lim_{\substack{n\to\infty\\n\text{ even}}}\sqrt[n]{|a_n|}=\lim_{\substack{n\to\infty\\n\text{ even}}}\sqrt[n]{\left|\frac{1}{2^{n-2}}\right|}=\lim_{\substack{n\to\infty\\n\text{ even}}}\frac{\sqrt[n]{4}}{2}=\frac{1}{2}.
$$

As both limits are the same, we can conclude that

$$
\lim_{n\to\infty}\sqrt[n]{|a_n|}=\frac{1}{2}<1,
$$

and by the root test the series $\displaystyle\sum_{n=1}^{\infty}a_n$ is absolutely convergent.

Similarly, for $n$ odd we have

$$
\lim_{\substack{n\to\infty\\n\text{ odd}}}\sqrt[n]{|b_n|}=\lim_{\substack{n\to\infty\\n\text{ even}}}\sqrt[n]{|b_n|}=\lim_{n\to\infty}\sqrt[n]{|b_n|}=2>1,
$$

so the series $\displaystyle\sum_{n=1}^{\infty}b_n$ is divergent by the root test.

:::

:::{prf:example}
:label: Ex:Series:RootTest4

Consider the series $\displaystyle\sum_{n=1}^{\infty}a_n$ and the series $\displaystyle\sum_{n=1}^{\infty}b_n$ with

$$
a_n = \begin{cases}
\frac{1}{2^{n}} & \text{if }n\text{ is odd},\\
0 & \text{if }n\text{ is even},
\end{cases}
\quad\text{and}\quad
b_n = \begin{cases}
2^{n} & \text{if }n\text{ is odd},\\
0 & \text{if }n\text{ is even}.
\end{cases}
$$

The series $\displaystyle\sum_{n=1}^{\infty}a_n$ is convergent, since

\begin{align*}
\sum_{n=1}^{\infty}a_n&=\sum_{\substack{n=1\\n\text{ odd}}}^{\infty}a_n+\sum_{\substack{n=1\\n\text{ even}}}^{\infty}a_n\\
&=\sum_{\substack{n=1\\n\text{ odd}}}^{\infty}\frac{1}{2^{n}}+\sum_{\substack{n=1\\n\text{ even}}}^{\infty}0 \\
&=\sum_{m=1}^{\infty}\frac{1}{2^{2m-1}} + 0 \\
&=\sum_{m=1}^{\infty}\frac{1}{4}\left(\frac{1}{4}\right)^{m-1} \\
&=\frac{\frac{1}{4}}{1-\frac{1}{4}} \\
&=\frac{1}{3}.
\end{align*}

The series $\displaystyle\sum_{n=1}^{\infty}b_n$ is divergent, since $\lim\limits_{n\to\infty}b_n$ does not exist.

However, we have

$$
\sqrt[n]{|a_n|} = \begin{cases}
\frac{1}{2} & \text{if }n\text{ is odd},\\
0 & \text{if }n\text{ is even},
\end{cases}
\quad\text{and}\quad
\sqrt[n]{|b_n|} = \begin{cases}
2 & \text{if }n\text{ is odd},\\
0 & \text{if }n\text{ is even}.
\end{cases}
$$

So the limits $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}$ and $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|b_n|}$ do not exist.

:::

This examples show that if $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}$ does not exist, then the series $\displaystyle\sum a_n$ might be convergent or divergent, as we have given one example for which the series is convergent and one example for which the series is divergent, which is exactly what the fourth statement in the root test says.

## Grasple exercises

:::{todo}
Select exercises from Grasple and add them in {numref}`Sec:Series:TestsForGeneralSeries`.