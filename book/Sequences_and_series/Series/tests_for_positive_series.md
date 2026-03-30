(Sec:Series:PositiveSeries)=
    
# Tests for positive series

In this section we cover:

- Integral test
- Direct comparison test
- Limit comparison test

Error estimations included in each test where applicable.


## Introduction

In {numref}`Sec:Series:InfiniteSeries` we have talked about infinite series, wether they are convergent or divergent. We also introduced the concept of absolute convergence and conditional convergence. In this section we will give some tests to determine whether a series is convergent or divergent. These tests only work for series with *positive terms*, which we call **positive series**:

:::{prf:definition} Positive series
A series $\displaystyle\sum a_n$ is called a **positive series** if $a_n>0$ for all $n$.
:::

(Sec:Series:PositiveSeries:IntegralTest)=
## The integral test

In {prf:ref}`Ex:Series:HarmonicSeries`, {prf:ref}`Ex:Series:AbsoluteConvergence1` and the proof of {prf:ref}`Thm:Series:pSeries` we investigate $p$-series, which are series of the form $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^p}$, where $p$ is a positive real number. In the two examples and the proof, we compared the series with the integral of an appropriate function.

This concept can be generalized to the **integral test**. {numref}`Fig:Series:IntegralTest` gives the idea behind the integral test: you either search for a function that always lies above the rectangles (for convergence) or a function that always lies below the rectangles (for divergence). In both cases, the function should be continuous, positive and decreasing on $[1,\infty)$ and $a_n=f(n)$.

:::{figure-start}
:width: 100%
:name: Fig:Series:IntegralTest

The two cases for the integral test are illustrated in the following two figures. In both cases we have $a_n=f(n)$, where $f$ is a continuous, positive and decreasing function on $[1,\infty)$. The rectangles represent the terms of the series $\displaystyle\sum a_n$ and the area under the graph of $f$ represents the integral $\displaystyle\int_1^nf(x)\,dx$.
:::

::::{grid} 2
:gutter: 5

:::{grid-item}
![number1](Images/integral1.png)
+++
(_a_) $\displaystyle a_2+a_3+a_4+\cdots+a_n\leq\int_1^nf(x)\,dx$.
:::

:::{grid-item}
![number2](Images/integral2.png)
+++ 
(_b_) $\displaystyle\int_1^nf(x)\,dx\leq a_1+a_2+a_3+\cdots+a_{n-1}$.
:::

::::

:::{figure-end}
:::

::::{todo}
Replace the two figures in {numref}`Fig:Series:IntegralTest` with applets.
::::

::::::{prf:Theorem} Integral test
:label: Thm:Series:IntegralTest
Suppose $f$ is a _continuous_, _positive_ and _non-increasing_ function on $[1,\infty)$, $\displaystyle\sum_{n=1}^{\infty} a_n$ is a _positive series_ and let $a_n=f(n)$. Then we have:

$$
\sum_{n=1}^{\infty}a_n\;\text{is convergent}\quad\Longleftrightarrow\quad\int_1^{\infty}f(x)\,dx\;\text{is convergent.}
$$

::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:IntegralTest`
:class: tudproof, dropdown
The proof follows the same idea as in {prf:ref}`Ex:Series:HarmonicSeries`, {prf:ref}`Ex:Series:AbsoluteConvergence1` and the proof of {prf:ref}`Thm:Series:pSeries`. For *convergence* we draw the rectangles to the *left* (below the graph of $f$) and for *divergence* we draw the rectangles to the *right* (above the graph of $f$), see {numref}`Fig:Series:IntegralTest`.

Let us start with the convergent case. If we draw the rectangles to the left, then we have, see {numref}`Fig:Series:IntegralTest`(a):

\begin{align*}
s_n &= \sum_{k=1}^na_k \\
&= a_1 + \sum_{k=2}^na_k \\
&= a_1 + \sum_{k=2}^n f(k) \\
&\leq a_1 + \sum_{k=2}^n\int_{k}^{k+1}f(x)\,dx \\
&= a_1 + \int_1^nf(x)\,dx.
\end{align*}

This follows from the fact that $a_n=f(n)$ and $f$ is non-increasing on $[1,\infty)$. Now, if $\displaystyle\int_1^{\infty}f(x)\,dx$ is convergent, then we have


$$
\int_{1}^{\infty}f(x)\,dx = \int_{1}^{n}f(x)\,dx + \int_{n}^{\infty}f(x)\,dx > \int_{1}^{n}f(x)\,dx,
$$

since $f$ is positive on $[1,\infty)$. Therefore, if $\displaystyle\int_1^{\infty}f(x)\,dx=M$, then

$$
s_n\leq a_1+\int_1^{\infty}f(x)\,dx\leq a_1+M.
$$

This means that $\{s_n\}$ is bounded above. Further we have

$$
s_{n+1}=s_n+a_{n+1} > s_n,
$$

since $a_{n+1}=f(n+1) > 0$. Thus, $\{s_n\}$ is an increasing sequence that is bounded above. Hence, it is convergent by {prf:ref}`Thm:Sequences:MonotonicBounded`. This means by {prf:ref}`Thm:Series:ConvergenceSum` that $\displaystyle\sum_{n=1}^{\infty} a_n$ is convergent if $\displaystyle\int_1^{\infty}f(x)\,dx$ is convergent.


Now we prove the divergent case. If we draw the rectangles to the right, then we have, see {numref}`Fig:Series:IntegralTest`(b):

\begin{align*}
s_n &= \sum_{k=1}^na_k \\
&> \sum_{k=1}^{n-1}a_k \\
&\geq \int_1^nf(x)\,dx.
\end{align*}

If $\displaystyle\int_1^{\infty}f(x)\,dx$ is divergent, then

$$
\lim_{n\to\infty}\int_1^nf(x)\,dx=\infty
$$

since $f$ is positive on $[1,\infty)$. Because $s_{n}>\displaystyle\int_1^nf(x)\,dx$ for all $n$, we must have $\lim\limits_{n\to\infty}s_{n}=\infty$. So $\displaystyle\sum a_n$ diverges if $\displaystyle\int_1^{\infty}f(x)\,dx$ is divergent.

::::::


::::::{prf:remark}
In other words we have:

1) If $\displaystyle\int_1^{\infty}f(x)\,dx$ is convergent, then $\displaystyle\sum_{n=1}^{\infty}a_n$ is convergent.

2) If $\displaystyle\int_1^{\infty}f(x)\,dx$ is divergent, then $\displaystyle\sum_{n=1}^{\infty}a_n$ is divergent.

::::::


We apply the integral test in the following examples.

::::::{prf:Example}
:label: Ex:Series:IntegralTestExample1

Consider the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+1}$.

The function $f(x)=\displaystyle\frac{1}{x^2+1}$ is continuous, positive and non-increasing on $[1,\infty)$ and

$$
\int_1^{\infty}\frac{1}{x^2+1}\,dx=\arctan(x)\bigg|_1^{\infty}=\frac{1}{2}\pi-\frac{\pi}{4}=\frac{\pi}{4}.
$$ 

The integral $\displaystyle\int_1^{\infty}\frac{1}{x^2+1}\,dx$ is therefore convergent, which implies that the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+1}$ is convergent as well.

In order to find an upper bound for the sum of the series, we note that the first rectangle corresponding to $n=1$ has an area $\frac{1}{2}$. Since the rectangles are drawn to the left, we have

\begin{align*}
\sum_{n=1}^{\infty}\frac{1}{n^2+1} &= \frac12+\sum_{n=2}^{\infty}\frac{1}{n^2+1} \\
&\leq \frac12+\int_1^{\infty}\frac{1}{x^2+1}\,dx \\
=&\frac12+\frac{\pi}{4}=\frac{1}{2}+\frac{\pi}{4} \\
&\approx 1.28540.
\end{align*}

::::::

::::::{note}
It is not easy to find the sum of the series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+1}$. Using more advanced methods, which are beyond the scope of this book, it can be shown that

$$
\sum_{n=1}^{\infty}\frac{1}{n^2+1}=-\frac{1}{2}+\frac{\pi}{2}\cdot\frac{e^{\pi}+e^{-\pi}}{e^{\pi}-e^{-\pi}}=-\frac{1}{2}+\frac{\pi}{2}\cdot\frac{e^{2\pi}+1}{e^{2\pi}-1}\approx1.0767.
$$

::::::

:::{todo}
Rewrite everything below this point.
::: 

::::::{prf:remark}
:label: Remark:IntegralTest
It is not necessary to start at $1$ (both for the series and the integral). The integral test can be applied to $\displaystyle\sum_{n=p}^{\infty}a_n$ and $\displaystyle\int_p^{\infty}f(x)\,dx$ for any fixed integer $p$ as long as $f$ is continuous, positive and non-increasing on $[p,\infty)$ and $a_n=f(n)$ for all $n\geq p$.
::::::

::::::{prf:Example}
:label: Ex:Series:IntegralTestExample2

Consider the series $\displaystyle\sum_{n=2}^{\infty}\frac{\ln(n)}{n}$.

First note that the function $f(x)=\displaystyle\frac{\ln(x)}{x}$ is positive and continuous for $x > 1$. Further we have:

$$
f'(x)=\frac{\dfrac{1}{x}\cdot x-\ln(x)}{x^2}=\frac{1-\ln(x)}{x^2}.
$$ 
 
This implies that the function $f$ is non-increasing for $x > e$ and that we can apply the integral test with $p=\lceil e\rceil=3$. We have

$$
\int_3^{\infty}\frac{\ln(x)}{x}\,dx=\frac{1}{2}(\ln(x))^2\bigg|_3^{\infty}=\infty.
$$

This implies that the series $\displaystyle\sum_{n=3}^{\infty}\frac{\ln(n)}{n}$ is divergent.

Because $\displaystyle\sum_{n=2}^{\infty}\frac{\ln(n)}{n}=\frac{\ln(2)}{2}+\displaystyle\sum_{n=3}^{\infty}\frac{\ln(n)}{n}$, we conclude that $\displaystyle\sum_{n=2}^{\infty}\frac{\ln(n)}{n}$ is divergent as well.
::::::


The integral test can be used to find an estimation of the sum of a convergent series that satisfies the integral test.

::::::{prf:Theorem} Estimating the sum of a series
:label: Thm:Series:IntegralTestEstimatingSum
Suppose that $a_n=f(n)$, where $f$ is a continuous, positive and decreasing function for $x\geq N$ and $\displaystyle\sum a_n$ is convergent. If $s$ is the sum of the series and $s_N=\displaystyle\sum_{n=1}^Na_n$ is the $N$th partial sum with remainder $R_N=s-s_N$, then

$$
\int_{N+1}^{\infty}f(x)\,dx\leq R_N\leq\int_N^{\infty}f(x)\,dx.
$$

::::::

```{figure} Images/remainder1.png
---
width: 50%
name: remainder1
align: right
---
$R_N\leq\displaystyle\int_N^{\infty}f(x)\,dx$
```

```{figure} Images/remainder2.png
---
width: 50%
name: remainder2
align: left
---
$\displaystyle\int_{N+1}^{\infty}f(x)\,dx\leq R_N$
```

::::::{admonition} Proof of {prf:ref}`Thm:Series:IntegralTestEstimatingSum`
:class: tudproof, dropdown
Note that

$$
R_N=s-s_N=a_{N+1}+a_{N+2}+a_{N+3}+\cdots
$$

is the **remainder**, id est the error made when the $N$th partial sum $s_N$ is used as an approximation of the sum $s$.

We use the same idea as for the integral test, assuming that $f$ is decreasing on $[N,\infty)$. Comparing the areas of the rectangles with the area under the graph of $f$ on $[N,\infty)$, we obtain

$$
R_N=a_{N+1}+a_{N+2}+a_{N+3}+\cdots\leq\int_N^{\infty}f(x)\,dx
$$

and

$$
R_N=a_{N+1}+a_{N+2}+a_{N+3}+\cdots\geq\int_{N+1}^{\infty}f(x)\,dx.
$$

This proves the theorem.
::::::

::::::{note}
For $\displaystyle\sum_{n=1}^{\infty}a_n$ the $N$th partial sum $s_N$ is the sum of the first $N$ terms. However, we call $s_N$ the $N$th partial sum of the series even when the series $\displaystyle\sum a_n$ does not start at $n=1$. So, for instance, if $\displaystyle\sum_{n=2}^{\infty}\frac{\ln(n)}{n}$ then $s_N=\displaystyle\sum_{n=2}^N\frac{\ln(n)}{n}$ is the sum of the first $N-1$ terms and if $\displaystyle\sum_{n=0}^{\infty}\frac{1}{n^2+1}$ then $s_N=\displaystyle\sum_{n=0}^N\frac{1}{n^2+1}$ is the sum of the first $N+1$ terms.
::::::

::::::{prf:Corollary} Improved estimation of the sum of a series
:label: Thm:Series:IntegralTestImprovedEstimation
Let $T_N=\displaystyle\int_N^{\infty}f(x)\,dx$, then the error $|s-s^*|$ in the approximation

$$
s\approx s^*=s_N+\frac{T_N+T_{N+1}}{2}
$$

satisfies $|s-s^*|\leq\displaystyle\frac{T_N-T_{N+1}}{2}$.
::::::

::::::{prf:Example}
Consider $\displaystyle\sum_{n=0}^{\infty}\frac{1}{n^2+1}$ and let $s$ denote its sum.

Let's use $s_{10}$ as an approximation of $s\approx2.07667$ (see a note above):

\begin{align*}
s_{10}=\sum_{n=0}^{10}\frac{1}{n^2+1}&=1+\frac{1}{2}+\frac{1}{5}+\frac{1}{10}+\frac{1}{17}+\frac{1}{26}+\frac{1}{37}+\frac{1}{50}\\
&{}\quad\quad{}+\frac{1}{65}+\frac{1}{82}+\frac{1}{101}=\frac{3355270077}{1693047850}\approx1.98179.
\end{align*}
How good is this approximation? Let

$$
T_N=\int_N^{\infty}\frac{dx}{x^2+1}=\arctan(x)\bigg|_N^{\infty}=\frac{1}{2}\pi-\arctan(N).
$$

Then, for $R_N=s-s_N$ we have

$$
T_{N+1}\leq R_N\leq T_N.
$$

For $N=10$ we obtain

$$
0.09066\approx T_{11}\leq R_{10}\leq T_{10}\approx0.09967.
$$

Since $s=S_{10}+R_{10}$ this implies that

$$
1.98179+0.09066\leq s\leq1.98179+0.09967
$$

or

$$
2.07245\leq s\leq2.08146.
$$

Finally, we have

$$
\frac{T_{10}+T_{11}}{2}\approx\frac{0.09967+0.09066}{2}\approx0.09516
$$

and therefore

$$
s^*=s_{10}+\frac{T_{10}+T_{11}}{2}\approx1.98179+0.09516\approx2.07695.
$$

::::::

## Direct comparison tests

::::{admonition} Moved from integral test section
These $p$-series will often be used in *comparison tests* in order to determine whether a more difficult series is convergent or divergent. As an example we note that

$$
\frac{1}{n^2+1}<\frac{1}{n^2}\quad\Longrightarrow\quad\sum_{n=1}^{\infty}\frac{1}{n^2+1}<\sum_{n=1}^{\infty}\frac{1}{n^2}.
$$

Since $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$ is a $p$-series with $p=2>1$, which is convergent, we conclude that $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+1}$ is convergent as well.

::::

Earlier we compared the series $\displaystyle\sum_{n=1}^{\infty}$ with the $p$-series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$:

$$
\frac{1}{n^2+1}<\frac{1}{n^2}\quad\Longrightarrow\quad\sum_{n=1}^{\infty}\frac{1}{n^2+1}<\sum_{n=1}^{\infty}\frac{1}{n^2}.
$$

Since $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$ is a $p$-series with $p=2>1$ it is convergent, which implies that $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+1}$ is convergent as well.

Now we generalize this concept in the following theorem.

::::::{prf:Theorem} Direct comparison tests
:label: Thm:Series:DirectComparisonTest
Suppose that $\displaystyle\sum a_n$ and $\displaystyle\sum b_n$ are series with *positive terms*.

1) If $a_n\leq b_n$ for all $n$ and $\displaystyle\sum b_n$ is convergent, then $\displaystyle\sum a_n$ is also convergent.

2) If $a_n\geq b_n$ for all $n$ and $\displaystyle\sum b_n$ is divergent, then $\displaystyle\sum a_n$ is also divergent.
::::::

::::::{note}
Since the sum of a finite number of terms is finite, the conditions only need to hold for $n\geq N$, where $N$ is some fixed integer.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:DirectComparisonTest`
:class: tudproof, dropdown
Consider $s_n=\displaystyle\sum_{k=1}^na_k$ and $t_n=\displaystyle\sum_{k=1}^nb_k$. 

1) Since $\displaystyle\sum b_n$ is convergent, the limit $\lim\limits_{n\to\infty}t_n=t$ exists.
Since $a_k\leq b_k$ for all $k$ we conclude that $s_n\leq t_n\leq t$ for all $n$. Furthermore, $s_{n+1}=s_n+a_{n+1}>s_n$ since $a_{n+1}$ is positive. Hence, $\{s_n\}$ is an increasing sequence that is bounded above which is convergent. This implies that $\displaystyle\sum a_n$ is convergent.

2) If $\displaystyle\sum b_n$ is divergent, then $\lim\limits_{n\to\infty}t_n=\infty$ since $\{t_n\}$ is an increasing sequence ($b_n$ is positive for all $n$). Now, since $a_n\geq b_n$ for all $n$, we have $s_n\geq t_n$ for all $n$. Thus $\lim\limits_{n\to\infty}s_n=\infty$ and therefore $\displaystyle\sum a_n$ is divergent.
::::::

We often use standard series such as $p$-series or geometric series to compare with. For a $p$-series $\displaystyle\sum\frac{1}{n^p}$ we know that it is convergent for $p>1$ and divergent for $p\leq1$. For a geometric series $\displaystyle\sum ar^{n-1}$ we know that it is convergent for $|r|<1$ and divergent for $|r|\geq1$.

::::::{prf:Example}
1) $\displaystyle\frac{1}{n^2+1}\leq\frac{1}{n^2}$ for all $n\geq1$ and $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$ is a $p$-series with $p=2>1$ which is convergent. This implies that $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+1}$ is convergent.

2) $\displaystyle\frac{\ln(n)}{n}\geq\frac{1}{n}$ for all $n\geq3$ and $\displaystyle\sum_{n=3}^{\infty}\frac{1}{n}$ is a $p$-series with $p=1$ which is divergent. This implies that $\displaystyle\sum_{n=3}^{\infty}\frac{\ln(n)}{n}$ is divergent.

3) $\displaystyle\frac{1}{2^n+1}\leq\frac{1}{2^n}$ for all $n\geq0$ and $\displaystyle\sum_{n=0}^{\infty}\frac{1}{2^n}$ is a geometric series with common ratio $r=\dfrac{1}{2}$ which is convergent. This implies that $\displaystyle\sum_{n=0}^{\infty}\frac{1}{2^n+1}$ is convergent.
::::::

## The limit comparison test

Since $\displaystyle\frac{1}{2^n+1}<\frac{1}{2^n}$ and $\displaystyle\sum\frac{1}{2^n}$ is a geometric series with common ratio $r=\dfrac{1}{2}$, we easily conclude that $\displaystyle\sum\frac{1}{2^n+1}$ is convergent as well.

However, what can be said about $\displaystyle\sum_{n=1}^{\infty}\frac{1}{2^n-1}$? Now we have $\displaystyle\frac{1}{2^n-1}>\frac{1}{2^n}$, which implies that $\displaystyle\sum_{n=1}^{\infty}\frac{1}{2^n-1}$ is larger than $\displaystyle\sum_{n=1}^{\infty}\frac{1}{2^n}$. The convergence of the latter series does not imply that the larger series is finite as well. So, the direct comparison test doesn't work in this case. However, for large values of $n$ the fraction $\dfrac{1}{2^n-1}$ becomes very close to $\dfrac{1}{2^n}$.

::::::{prf:Theorem} Limit comparison test
:label: Thm:Series:LimitComparisonTest
Suppose that $\displaystyle\sum a_n$ and $\displaystyle\sum b_n$ are series with *positive terms*. Let

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=L,
$$

where $L\geq0$ or $L=\infty$.

1) If $L<\infty$ and $\displaystyle\sum b_n$ converges, then $\displaystyle\sum a_n$ also converges.

2) If $L>0$ and $\displaystyle\sum b_n$ diverges, then $\displaystyle\sum a_n$ also diverges.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:LimitComparisonTest`
:class: tudproof, dropdown

1) If $L<\infty$, then

$$
0<\frac{a_n}{b_n}<L+1
$$

for $n$ sufficiently large. Hence, we have $0<a_n<(L+1)b_n$ for $n$ sufficiently large. This implies that $\displaystyle\sum a_n$ converges whenever $\displaystyle\sum b_n$ converges.

2) If $L>0$, then

$$
\frac{a_n}{b_n}>\frac{L}{2}
$$

for $n$ sufficiently large. Hence, we have $0<b_n<\dfrac{2}{L}a_n$ for $n$ sufficiently large. This implies that $\displaystyle\sum a_n$ diverges whenever $\displaystyle\sum b_n$ diverges.
::::::

::::::{prf:Example}
1) Consider $\displaystyle\sum_{n=1}^{\infty}\frac{1}{2^n-1}$. Let $a_n=\dfrac{1}{2^n-1}$ and $b_n=\dfrac{1}{2^n}$, then

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=\lim_{n\to\infty}\frac{\dfrac{1}{2^n-1}}{\dfrac{1}{2^n}}=\lim_{n\to\infty}\frac{2^n}{2^n-1}=\lim_{n\to\infty}\frac{1}{1-\dfrac{1}{2^n}}=\frac{1}{1-0}=1.
$$

Since $\displaystyle\sum_{n=1}^{\infty}\frac{1}{2^n}$ converges (geometric series with common ratio $\frac{1}{2}$), we conclude that $\displaystyle\sum_{n=1}^{\infty}\frac{1}{2^n-1}$ converges too.

2) Consider $\displaystyle\sum_{n=1}^{\infty}\frac{1}{1+\sqrt{n}}$. Let $a_n=\dfrac{1}{1+\sqrt{n}}$ and $b_n=\dfrac{1}{\sqrt{n}}$, then

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=\lim_{n\to\infty}\frac{\dfrac{1}{1+\sqrt{n}}}{\dfrac{1}{\sqrt{n}}}=\lim_{n\to\infty}\frac{\sqrt{n}}{1+\sqrt{n}}=\lim_{n\to\infty}\frac{1}{\dfrac{1}{\sqrt{n}}+1}=\frac{1}{0+1}=1.
$$

Since $\displaystyle\sum_{n=1}^{\infty}\frac{1}{\sqrt{n}}$ is divergent ($p$-series with $p=\frac{1}{2}\leq1$), we conclude that $\displaystyle\sum_{n=1}^{\infty}\frac{1}{1+\sqrt{n}}$ is also divergent.


3) Consider $\displaystyle\sum_{n=1}^{\infty}\frac{2n+3}{n^3-2n+5}$. Let $a_n=\dfrac{2n+3}{n^3-2n+5}$, then for large $n$ we have $a_n\sim\dfrac{2n}{n^3}=\dfrac{2}{n^2}$. So, let $b_n=\dfrac{1}{n^2}$, then

\begin{align*}
\lim_{n\to\infty}\frac{a_n}{b_n}&=\lim_{n\to\infty}\frac{\dfrac{2n+3}{n^3-2n+5}}{\dfrac{1}{n^2}}=\lim_{n\to\infty}\frac{(2n+3)n^2}{n^3-2n+5}\\
&=\lim_{n\to\infty}\frac{2+\dfrac{3}{n}}{1-\dfrac{2}{n^2}+\dfrac{5}{n^3}}=\frac{2+0}{1-0+0}=2.
\end{align*}
Since $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$ converges ($p$-series with $p=2>1$), we conclude that $\displaystyle\sum_{n=1}^{\infty}\frac{2n+3}{n^3-2n+5}$ converges as well.

4) Consider $\displaystyle\sum_{n=0}^{\infty}\frac{\sqrt{n^4+4n+5}}{2n^5+3n^2+1}$. Let $a_n=\displaystyle\frac{\sqrt{n^4+4n+5}}{2n^5+3n^2+1}$ and $b_n=\displaystyle\frac{\sqrt{n^4}}{n^5}=\frac{n^2}{n^5}=\frac{1}{n^3}$, then

\begin{align*}
\lim\limits_{n\to\infty}\frac{a_n}{b_n}&=\lim\limits_{n\to\infty}\frac{\sqrt{n^4+4n+5}}{2n^5+3n^2+1}\cdot\frac{n^3}{1}=\lim\limits_{n\to\infty}\frac{\sqrt{1+4n^{-3}+5n^{-4}}}{2+3n^{-3}+n^{-5}}\\
&=\frac{\sqrt{1+0+0}}{2+0+0}=\frac{1}{2}>0.
\end{align*}
Since $\displaystyle\sum_{n=1}^{\infty}b_n=\sum_{n=1}^{\infty}\frac{1}{n^3}$ is a $p$-series with $p=3>1$, which is convergent, we concluse that $\displaystyle\sum_{n=0}^{\infty}a_n=\sum_{n=0}^{\infty}\frac{\sqrt{n^4+4n+5}}{2n^5+3n^2+1}$ is convergent too.

5) Consider $\displaystyle\sum_{n=0}^{\infty}\frac{3n^2+5n+2}{\sqrt{2n^5+4n^3+3}}$. Let $a_n=\displaystyle\frac{3n^2+5n+2}{\sqrt{2n^5+4n^3+3}}$ and $b_n=\displaystyle\frac{n^2}{\sqrt{n^5}}=\frac{n^2}{n^{\frac{5}{2}}}=\frac{1}{n^{\frac{1}{2}}}$, then

\begin{align*}
\lim\limits_{n\to\infty}\frac{a_n}{b_n}&=\lim\limits_{n\to\infty}\frac{3n^2+5n+2}{\sqrt{2n^5+4n^3+3}}\cdot\frac{n^{\frac{1}{2}}}{1}=\lim\limits_{n\to\infty}\frac{3+5n^{-1}+2n^{-2}}{\sqrt{2+4n^{-2}+3n^{-5}}}\\
&=\frac{3+0+0}{\sqrt{2+0+0}}=\frac{3}{\sqrt{2}}>0.
\end{align*}
Since $\displaystyle\sum_{n=1}^{\infty}b_n=\sum_{n=1}^{\infty}\frac{1}{n^{\frac{1}{2}}}$ is a $p$-series with $p=\displaystyle\frac{1}{2}\leq1$, which is divergent, we conclude that $\displaystyle\sum_{n=0}^{\infty}a_n=\sum_{n=0}^{\infty}\frac{3n^2+5n+2}{\sqrt{2n^5+4n^3+3}}$ is divergent too.
::::::

## The ratio comparison test

::::::{prf:Theorem} Ratio comparison test
:label: Thm:Series:RatioComparisonTest
Suppose that $\displaystyle\sum a_n$ and $\displaystyle\sum b_n$ are series with *positive terms*. 

1) If $\dfrac{a_{n+1}}{a_n}\leq\dfrac{b_{n+1}}{b_n}$ for all $n$ and $\displaystyle\sum b_n$ is convergent, then $\displaystyle\sum a_n$ is also convergent.

2) If $\dfrac{a_{n+1}}{a_n}\geq\dfrac{b_{n+1}}{b_n}$ for all $n$ and $\displaystyle\sum b_n$ is divergent, then $\displaystyle\sum a_n$ is also divergent.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:RatioComparisonTest`
:class: tudproof, dropdown

1) If $\dfrac{a_{n+1}}{a_n}\leq\dfrac{b_{n+1}}{b_n}$ for all $n$, then $\dfrac{a_{n+1}}{b_{n+1}}\leq\dfrac{a_n}{b_n}$ for all $n$, which implies that $\dfrac{a_n}{b_n}\leq\dfrac{a_1}{b_1}$ for all $n$. Hence: $a_n\leq\dfrac{a_1}{b_1}b_n$ for all $n$. Then the direct comparison test implies that if $\displaystyle\sum b_n$ converges, then $\displaystyle\sum a_n$ converges too.

2) If $\dfrac{a_{n+1}}{a_n}\geq\dfrac{b_{n+1}}{b_n}$ for all $n$, then $\dfrac{a_{n+1}}{b_{n+1}}\geq\dfrac{a_n}{b_n}$ for all $n$, which implies that $\dfrac{a_n}{b_n}\geq\dfrac{a_1}{b_1}$ for all $n$. Hence: $a_n\geq\dfrac{a_1}{b_1}b_n$ for all $n$. Then the direct comparison test implies that if $\displaystyle\sum b_n$ diverges, then $\displaystyle\sum a_n$ diverges too.
::::::

Dit misschien maar weglaten? Ik kan geen zinnige toepassingen bedenken.
