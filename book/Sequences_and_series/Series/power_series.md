(Sec:Series:PowerSeries)=

# Power series

In this section we cover:

- Power series
- Interval of convergence
- Representation of functions as power series using geometric series
- Rules of calculation (sums, substitutions, differentiation, integration, products)

## Introduction

::::::{prf:definition}
:label: Def:Series:PowerSeries
A series of the form

$$
\sum_{n=0}^{\infty}c_nx^n=c_0+c_1x+c_2x^2+\cdots
$$
 
is called a **power series** in $x$. The constants $\{c_n\}_{n=0}^{\infty}$ are called the **coefficients** of the power series.

More generally, a series of the form

$$
\sum_{n=0}^{\infty}c_n(x-a)^n=c_0+c_1(x-a)+c_2(x-a)^2+\cdots
$$
 
is called a power series in $x-a$ or a power series centered at $x=a$ or a power series about $a$.
::::::

::::::{prf:example}
:label: Ex:Series:GeometricSeries
The power series $\displaystyle\sum_{n=0}^{\infty}x^n$ is a *geometric series* with common ratio $x$. Hence, this power series is absolutely convergent if $|x|<1$ and is divergent if $|x|\geq1$. Moreover, for $|x|<1$ the sum of the series is $\dfrac{1}{1-x}$.
::::::

::::::{prf:example}
The series $\displaystyle\sum_{n=1}^{\infty}\frac{(x-2)^{n-1}}{n}$ is a power series about $2$. Note that the series converges for $x=2$ (with sum $1$). For $x\neq2$ we might apply the ratio test: let $a_n=\displaystyle\frac{(x-2)^{n-1}}{n}$, then we have:

\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|\frac{(x-2)^n}{n+1}\cdot\frac{n}{(x-2)^{n-1}}\right|\\
&=\lim\limits_{n\to\infty}\frac{n}{n+1}\cdot|x-2|=|x-2|.
\end{align*}
Hence, the series is absolutely convergent if $|x-2|<1$ and is divergent if $|x-2|>1$. The ratio test is inconclusive if  $|x-2|=1$.

For $x=3$ the series equals the harmonic series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$, which is divergent.

For $x=1$ the series equals the alternating harmonic series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$, which is (conditionally) convergent.

We conclude that the series converges if $x\in[1,3)$ and diverges otherwise. The interval $[1,3)$ is called the **interval of convergence** of the power series.
::::::

::::::{prf:theorem}
:label: Thm:Series:PowerSeries
For a given power series

$$
\sum_{n=0}^{\infty}c_n(x-a)^n=c_0+c_1(x-a)+c_2(x-a)^2+\cdots,
$$
 
there are only three possibilities:

1) The series only converges for $x=a$;

2) The series converges for all $x\in\mathbb{R}$;

3) There is a positive number $R$ such that the series absolutely converges for $|x-a|<R$ and diverges for $|x-a|>R$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:PowerSeries`
:class: tudproof, dropdown
If the power series $\displaystyle\sum_{n=0}^{\infty}c_n(x-a)^n$ absolutely converges for $x=b$, then $\displaystyle\sum_{n=0}^{\infty}\left|c_n(b-a)^n\right|$ converges. Then the {prf:ref}`comparison test <Thm:Series:DirectComparisonTest>` implies that $\displaystyle\sum_{n=0}^{\infty}\left|c_n(x-a)^n\right|$ converges for all $x$ such that $|x-a|<|b-a|$.

If there are values of $x$ for which the series diverges, then there exists a maximum value of $|b-a|=R$ such that the series absolutely converges for $|x-a|<R$.

This proves the theorem.
::::::

::::::{prf:definition}
:label: Def:Series:RadiusOfConvergence

The number $R$ in {prf:ref}`Thm:Series:PowerSeries` is called the **radius of convergence** of the power series. If the series only converges for $x=a$, then $R=0$, and if the series converges for all $x\in\mathbb{R}$, then $R=\infty$.

The interval containing all $x$ for which the series converges is called the **interval of convergence** of the power series.
::::::

::::::{prf:example}
1) The series $\displaystyle\sum_{n=0}^{\infty}n!(x-1)^n$ is a power series about $1$. Hence, the series converges for $x=1$ (with sum $1$). For $x\neq1$ we apply the ratio test: let $a_n=n!(x-1)^n$, then we have:

$$ 
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim\limits_{n\to\infty}\left|\frac{(n+1)!(x-1)^{n+1}}{n!(x-1)^n}\right|
=\lim\limits_{n\to\infty}(n+1)|x-1|=\infty, 
$$ 
  
since $|x-1| > 0$. This implies that the series diverges for all $x\neq1$. Hence, the series only converges for $x=1$ and the radius of convergence is $R=0$.

2) The series $\displaystyle\sum_{n=0}^{\infty}\frac{(x+2)^n}{n!}$ is a power series about $-2$. Hence, the series converges for $x=-2$ (with sum $1$). For $x\neq-2$ we apply the ratio test: let $a_n=\displaystyle\frac{(x+2)^n}{n!}$, then we have:

$$ 
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim\limits_{n\to\infty}\left|\frac{(x+2)^{n+1}}{(n+1)!}\cdot\frac{n!}{(x+2)^n}\right|
=\lim\limits_{n\to\infty}\frac{|x+2|}{n+1}=0. 
$$ 
 
This implies that the series converges for all $x\neq-2$ as well. Hence, the series converges for all $x\in\mathbb{R}$ and the radius of convergence is $R=\infty$.

3) The series $\displaystyle\sum_{n=1}^{\infty}\frac{x^{n+1}}{n^2}$ is a power series about $0$. Hence, the series converges for $x=0$ (with sum $0$). For $x\neq0$ we apply the ratio test: let $a_n=\displaystyle\frac{x^{n+1}}{n^2}$, then we have:

$$ 
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim\limits_{n\to\infty}\left|\frac{x^{n+2}}{(n+1)^2}\cdot\frac{n^2}{x^{n+1}}\right|
=\lim\limits_{n\to\infty}\left(\frac{n}{n+1}\right)^2|x|=|x|. 
$$ 
 
This implies that the series absolutely converges for $|x| < 1$ and diverges for $|x| > 1$. So the radius of convergence is $R=1$. For $x=1$ we have $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$ which is a $p$-series with $p=2>1$ and therefore (absolutely) convergent. For $x=-1$ we have $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}$ which is absolutely convergent as well. Hence, the interval of convergence is $[-1,1]$.

4) The series $\displaystyle\sum_{n=0}^{\infty}\frac{(3-x)^n}{n+1}$ is a power series about $3$. Hence, the series converges for $x=3$ (with sum $1$). For $x\neq3$ we might apply the ratio test: let $a_n=\displaystyle\frac{(3-x)^n}{n+1}$, then we have:

\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|\frac{(3-x)^{n+1}}{n+2}\cdot\frac{n+1}{(3-x)^n}\right|\\
&=\lim\limits_{n\to\infty}\frac{n+1}{n+2}\cdot|3-x|=|3-x|.
\end{align*}
Hence, the series is absolutely convergent if $|3-x| < 1$ and is divergent if $|3-x| > 1$. So the radius of convergence is $R=1$. For $x=2$ the series equals the harmonic series $\displaystyle\sum_{n=0}^{\infty}\frac{1}{n+1}$, which is divergent and for $x=4$ the series equals the alternating harmonic series $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}$, which is (conditionally) convergent. Hence, the interval of convergence is $(2,4]$.

5) The series $\displaystyle\sum_{n=1}^{\infty}n\left(\frac{x-5}{2}\right)^n$ is a power series about $5$. Hence, the series converges for $x=5$ (with sum $0$). For $x\neq5$ we might apply the ratio test: let $a_n=\displaystyle n\left(\frac{x-5}{2}\right)^n$, then we have:

\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|(n+1)\left(\frac{x-5}{2}\right)^{n+1}\cdot\frac{1}{n}\left(\frac{2}{x-5}\right)^n\right|\\
&=\lim\limits_{n\to\infty}\frac{n+1}{n}\cdot\left|\frac{x-5}{2}\right|=\left|\frac{x-5}{2}\right|.
\end{align*}
Hence, the series is absolutely convergent if $\displaystyle\left|\frac{x-5}{2}\right| < 1$ or $|x-5| < 2$ and is divergent if $\displaystyle\left|\frac{x-5}{2}\right| > 1$ or $|x-5| > 2$. So the radius of convergence is $R=2$. For $x=7$ the series reads $\displaystyle\sum_{n=1}^{\infty}n$, which is divergent and for $x=3$ the series reads $\displaystyle\sum_{n=1}^{\infty}n(-1)^n$, which is divergent as well. Hence, the interval of convergence is $(3,7)$.
::::::

::::::{prf:example} Bessel functions
:label: Ex:Series:Bessel

Bessel functions are defined in terms of power series. The German mathematician [Friedrich Wilhelm Bessel (1784-1846)](https://en.wikipedia.org/wiki/Friedrich_Wilhelm_Bessel) introduced these functions when solving Kepler's equation for describing planetary motion. Later, these Bessel functions have been applied in many different physical situations, including the temperature distribution in a circular plate and the shape of a vibrating drumhead.

:::{figure} Images/bessel.gif
:width: 50%
:name: bessel function
:align: center

The motion of a vibrating drumhead.
Source: https://en.wikipedia.org/wiki/Vibrations_of_a_circular_membrane.
:::

The Bessel function $J_0(x)$ of the first kind of order $0$ is defined by: 

$$
J_0(x)=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n}}{2^{2n}(n!)^2}.
$$

Note that this is a power series in $x$ which is convergent for $x=0$. For $x\neq0$ we might apply the ratio test: let $a_n=\displaystyle\frac{(-1)^nx^{2n}}{2^{2n}(n!)^2}$, then we have:

$$ 
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim\limits_{n\to\infty}\left|\frac{(-1)^{n+1}x^{2n+2}}{2^{2n+2}((n+1)!)^2}\cdot\frac{2^{2n}(n!)^2}{(-1)^nx^{2n}}\right|
=\lim\limits_{n\to\infty}\frac{x^2}{4(n+1)^2}=0. 
$$ 
 
Hence, the series converges for all $x\neq0$ as well. We conclude that the power series converges for all $x\in\mathbb{R}$ (the radius of convergence is $R=\infty$). This implies that the domain of the Bessel function $J_0(x)$, the interval of convergence of the series, is $(-\infty,\infty)=\mathbb{R}$.
::::::

## Power series representations

In {prf:ref}`Ex:Series:GeometricSeries` we have seen that the power series $\displaystyle\sum_{n=0}^{\infty}x^n$ is absolutely convergent for $|x|<1$ and divergent for $|x|\geq1$. Furthermore, we have

:::{math}
:label: Eq:Series:GeometricSeries
\sum_{n=0}^{\infty}x^n=\frac{1}{1-x},\quad|x|<1.
:::

Hence, for $-1<x<1$ the function $f(x)=\dfrac{1}{1-x}$ can be written as the power series $\displaystyle\sum_{n=0}^{\infty}x^n$. This is called a **power series representation** of $f$.

Using substitutions, this leads to power series representations for other functions. For instance, if we set $-x$ instead of $x$ we obtain

$$
\frac{1}{1+x}=\sum_{n=0}^{\infty}(-x)^n=\sum_{n=0}^{\infty}(-1)^nx^n,
$$

which is valid for $|-x|<1$ or equivalenty for $|x|<1$.

A power series representation for a function is not unique.

::::::{prf:example}
Consider the function $\dfrac{1}{5+x}$. 

Replacing $x$ by $-x-4$ in {eq}`Eq:Series:GeometricSeries` we obtain

$$
\frac{1}{5+x}=\frac{1}{1-(-x-4)}=\sum_{n=0}^{\infty}(-x-4)^n=\sum_{n=0}^{\infty}(-1)^n(x+4)^n,
$$

which is valid for $|-x-4|<1$ or equivalently for $|x+4|<1$. This is a power series about $-4$ with radius of convergence $R=1$. Note that both for $x=-5$ and $x=-3$ the series diverges. This implies that the interval of convergence is the open interval $(-5,-3)$.

We also have with $-\dfrac{x}{5}$ instead of $x$ in {eq}`Eq:Series:GeometricSeries`

$$
\frac{1}{5+x}=\frac{1}{5}\cdot\frac{1}{1+\dfrac{x}{5}}=\frac{1}{5}\sum_{n=0}^{\infty}\left(-\frac{x}{5}\right)^n=\sum_{n=0}^{\infty}\frac{(-1)^n}{5^{n+1}}x^n,
$$

which is valid for $\left|-\dfrac{x}{5}\right|<1$ or equivalently for $|x|<5$. This is a power series about $0$ with radius of convergence $R=5$. Note that both for $x=-5$ and for $x=5$ the series diverges. This implies that the interval of convergence is the open interval $(-5,5)$.

Note that the latter power series representation is much more useful than the first one.
::::::

::::::{prf:example}
Find a power series representation of $\dfrac{x^2}{5+x}$. 

Solution. In the previous example we have found that

$$
\frac{1}{5+x}=\sum_{n=0}^{\infty}\frac{(-1)^n}{5^{n+1}}x^n,\quad|x|<5.
$$

Multiplication by $x^2$ leads to

$$
\frac{x^2}{5+x}=\sum_{n=0}^{\infty}\frac{(-1)^n}{5^{n+1}}x^{n+2},\quad|x|<5.
$$

::::::

::::::{prf:example}
Find a power series representation of $\dfrac{1}{1+x^2}$. 

Solution. If we replace $x$ by $-x^2$ in {eq}`Eq:Series:GeometricSeries` we obtain

$$
\frac{1}{1+x^2}=\sum_{n=0}^{\infty}(-x^2)^n=\sum_{n=0}^{\infty}(-1)^nx^{2n},
$$

which is valid for $\left|-x^2\right|<1$ or equivalently for $|x|<1$. This is a power series about $0$ with radius of convergence $R=1$. Note that the series diverges for both $x=-1$ and for $x=1$. This implies that the interval of convergence is the open interval $(-1,1)$.
::::::

Note that the function $\dfrac{1}{1+x^2}$ is the derivative of $\arctan(x)$.

What happens if we differentiate or integrate a power series representation of a function $f$? 

The next theorem states that we can differentiate and integrate a power series term by term and that the radius of convergence stays the same.

::::::{prf:theorem}
:label: Thm:Series:DifferentiationIntegration
If the power series $\displaystyle\sum c_n(x-a)^n$ has radius of convergence $R>0$, then the function $f$ defined by

$$
f(x)=c_0+c_1(x-a)+c_2(x-a)^2+\cdots=\sum_{n=0}^{\infty}c_n(x-a)^n
$$

is differentiable (and therefore continuous) on the interval $(a-R,a+R)$ and

$$
f'(x)=c_1+2c_2(x-a)+3c_3(x-a)^2+\cdots=\sum_{n=1}^{\infty}nc_n(x-a)^{n-1}
$$

and

\begin{align*}
\int f(x)\,dx&=C+c_0(x-a)+\frac{1}{2}c_1(x-a)^2+\frac{1}{3}c_2(x-a)^3+\cdots\\
&=C+\sum_{n=0}^{\infty}\frac{c_n}{n+1}(x-a)^{n+1}.
\end{align*}
::::::

::::::{note}
We skip the proof of this theorem.

After differentiating or integrating a power series representation of a function $f$ the radius of convergence $R$ stays the same. However, at the endpoints of the interval of convergence the behaviour might be different. The interval of convergence can be $(a-R,a+R)$, $[a-R,a+R)$, $(a-R,a+R]$ or even $[a-R,a+R]$.
::::::

::::::{prf:example}
:label: Ex:Series:LogTwo
Consider the power series representation $\displaystyle\frac{1}{1+x}=\sum_{n=0}^{\infty}(-1)^nx^n$ for $-1<x<1$. Differentiation leads to

\begin{align*}
&-\frac{1}{(1+x)^2}=\sum_{n=1}^{\infty}n(-1)^nx^{n-1}\\
&{}\quad\Longleftrightarrow\quad\frac{1}{(1+x)^2}=\sum_{n=1}^{\infty}n(-1)^{n-1}x^{n-1}=\sum_{n=0}^{\infty}(n+1)(-1)^nx^n.
\end{align*}
Note that this power series is only convergent for $-1<x<1$. For instance, this implies that

$$
\sum_{n=0}^{\infty}\frac{n+1}{2^n}=\frac{1}{\left(1-\frac{1}{2}\right)^2}=4\quad\text{and}\quad\sum_{n=0}^{\infty}(-1)^n\frac{n+1}{2^n}=\frac{1}{\left(1+\frac{1}{2}\right)^2}=\frac{4}{9}.
$$

Integration leads to

$$
\ln|1+x|=C+\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}x^{n+1}.
$$

For $x=0$ this reads: $0=\ln(1)=C+0$ which implies that $C=0$. Hence we have

$$
\ln|x+1|=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}x^{n+1},\quad-1<x<1.
$$

For $x=-1$ we obtain the series $\displaystyle-\sum_{n=0}^{\infty}\frac{1}{n+1}$ which is divergent (this is minus the harmonic series). For $x=1$ we obtain the series $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}$ which is (conditionally) convergent (this is the alternating harmonic series). Since $\ln|x+1|$ is continuous at $x=1$ we conclude that

$$
\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}=\lim_{x\to1}\ln|x+1|=\ln(2).
$$

::::::

::::::{prf:example}
Integrating the power series representation $\displaystyle\frac{1}{1+x^2}=\sum_{n=0}^{\infty}(-1)^nx^{2n}$ for $-1<x<1$ we obtain

$$
\arctan(x)=C+\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}x^{2n+1}.
$$

For $x=0$ this reads $0=\arctan(0)=C+0$ which implies that $C=0$. Hence we have

$$
\arctan(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}x^{2n+1},\quad-1<x<1.
$$

This series is sometimes called **Gregory's series** after the Scottish mathematician [James Gregory (1638-1675)](https://en.wikipedia.org/wiki/James_Gregory_(mathematician)).

Note that this series is also convergent for both $x=-1$ and $x=1$, since $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}$ is convergent due to the {prf:ref}`alternating series test <Thm:Series:AlternatingSeriesTest>`. Hence, by continuity, we have

$$
\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}=\arctan(1)=\frac{1}{4}\pi.
$$

This result

$$
1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\frac{1}{9}-\frac{1}{11}+\cdots=\frac{1}{4}\pi
$$

is known as the **Leibniz formula** for $\pi$, named after the German mathematician [Gottfried Wilhelm Leibniz (1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz).
::::::

::::{exercise}
:label: Exc:Series:DifferentiationExercise
Consider the power series representation $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ for $|x|<1$.

Use differentiation to find the sums of the series

$$
\sum_{n=1}^{\infty}\frac{n}{2^n},\quad\sum_{n=1}^{\infty}(-1)^{n-1}\frac{n}{2^n},\quad\sum_{n=2}^{\infty}\frac{n(n-1)}{2^n}\quad\text{and}\quad\sum_{n=2}^{\infty}(-1)^n\frac{n(n-1)}{2^n}.
$$
::::

:::{admonition} Solution of {numref}`Exc:Series:DifferentiationExercise`
:class: solution, dropdown
Differentiation of $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ leads to

$$
\frac{1}{(1-x)^2}=\sum_{n=1}^{\infty}nx^{n-1}\quad\text{and}\quad\frac{2}{(1-x)^3}=\sum_{n=2}^{\infty}n(n-1)x^{n-2}
$$

for $|x|<1$. This implies that

$$
\frac{x}{(1-x)^2}=\sum_{n=1}^{\infty}nx^n\quad\text{and}\quad\frac{2x^2}{(1-x)^3}=\sum_{n=2}^{\infty}n(n-1)x^n
$$

for $|x|<1$. For $x=\frac{1}{2}$ and $x=-\frac{1}{2}$ we now obtain $\displaystyle\sum_{n=1}^{\infty}\frac{n}{2^n}=\frac{\frac{1}{2}}{\left(1-\frac{1}{2}\right)^2}=2$,

$$
\sum_{n=1}^{\infty}(-1)^{n-1}\frac{n}{2^n}=-\frac{-\frac{1}{2}}{\left(1+\frac{1}{2}\right)^2}=\frac{2}{9},\quad\sum_{n=2}^{\infty}\frac{n(n-1)}{2^n}=\frac{2(\frac{1}{2})^2}{\left(1-\frac{1}{2}\right)^3}=4
$$

and

$$
\sum_{n=2}^{\infty}(-1)^n\frac{n(n-1)}{2^n}=\frac{2\left(-\frac{1}{2}\right)^2}{\left(1+\frac{1}{2}\right)^3}=\frac{27}{16}.
$$

:::

::::::{prf:example} Application
Consider the integral $\displaystyle\int_0^{0.5}\frac{x^2}{1+x^8}\,dx$.

It is difficult to evaluate this integral exactly. However, we may use a power series representation of the integrand to find an approximation. Start with $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ for $|x|<1$. This implies that

\begin{align*}
&\frac{1}{1+x^8}=\sum_{n=0}^{\infty}(-1)^nx^{8n}\quad\Longrightarrow\quad\frac{x^2}{1+x^8}=\sum_{n=0}^{\infty}(-1)^nx^{8n+2}\\
&{}\quad\Longrightarrow\quad\int\frac{x^2}{1+x^8}\,dx=C+\sum_{n=0}^{\infty}\frac{(-1)^n}{8n+3}x^{8n+3},\quad |x| < 1. 
\end{align*}
This implies that

\begin{align*}
\int_0^{0.5}\frac{x^2}{1+x^8}\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n(0.5)^{8n+3}}{8n+3}\\
&=\frac{(0.5)^3}{3}-\frac{(0.5)^{11}}{11}+\frac{(0.5)^{19}}{19}-\frac{(0.5)^{27}}{27}+\cdots\\
&\approx\frac{(0.5)^3}{3}=0.041666\ldots.
\end{align*}
::::::

:::{admonition} Remarkable decimal fractions (bonus material)
:class: solution, dropdown
We will prove that $\dfrac{1}{81}=\dfrac{1}{9^2}=0.\overline{012345679}$.

We start with the geometric series $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ for $|x|<1$. Differentiation now leads to $\displaystyle\sum_{n=1}^{\infty}nx^{n-1}=\frac{1}{(1-x)^2}$ for $|x|<1$. This implies that $\displaystyle\sum_{n=1}^{\infty}nx^{n+1}=\frac{x^2}{(1-x)^2}=\left(\frac{x}{1-x}\right)^2$ for $|x|<1$. Substitution of $x=\displaystyle\frac{1}{10}$ leads to $\displaystyle\sum_{n=1}^{\infty}\frac{n}{10^{n+1}}=\left(\frac{1}{9}\right)^2=\frac{1}{81}$.

For the first nine terms we have

$$
\sum_{n=1}^9\frac{n}{10^{n+1}}=0.01+0.002+0.0003+\cdots+0.0000000009=0.0123456789.
$$
 
For the tenth term we have: $\displaystyle\frac{10}{10^{11}}=\frac{1}{10^{10}}=0.0000000001$. Hence:

$$
\sum_{n=1}^{10}\frac{n}{10^{n+1}}=0.0123456789+0.0000000001=0.0123456790.
$$

Now suppose that $p=0.\overline{012345679}$, then we have:

$$
10^9p=12345679.\overline{012345679}=12345679+0.\overline{012345679}=12345679+p.
$$

Since we have $10^9-1=999999999=9^2\cdot12345679$, this implies that

\begin{align*}
(10^9-1)p=12345679&\quad\Longleftrightarrow\quad9^2\cdot12345679p=12345679\\
&\quad\Longleftrightarrow\quad p=\frac{1}{9^2}=\frac{1}{81}.
\end{align*}
Similarly, the substitution $x=\displaystyle\frac{1}{100}$ leads to $\displaystyle\sum_{n=1}^{\infty}\frac{n}{100^{n+1}}=\left(\frac{1}{99}\right)^2=\frac{1}{9801}$.

For the first ninety-nine terms we now have

$$
\sum_{n=1}^{99}\frac{n}{100^{n+1}}=0.0001020304\ldots9596979899.
$$

For the hundredth term we have: $\displaystyle\frac{100}{100^{101}}=\frac{1}{100^{100}}$. Hence:

$$
\sum_{n=1}^{100}\frac{n}{100^{n+1}}=0.0001020304\ldots9596979900.
$$
 
Now suppose that $q=0.\overline{0001020304\ldots95969799}$, then we have:

\begin{align*}
100^{99}q&=1020304\ldots95969799.\overline{0001020304\ldots95969799}\\
&=1020304\ldots95969799+q.
\end{align*}
Since we have $100^{99}-1=99^2\cdot1020304\ldots95969799$, this implies that

\begin{align*}
&(100^{99}-1)q=1020304\ldots95969799\\
&\quad\Longleftrightarrow\quad99^2\cdot1020304\ldots95969799q=1020304\ldots95969799\\
&\quad\Longleftrightarrow\quad q=\frac{1}{99^2}=\frac{1}{9801}.
\end{align*}
Similarly if follows that

$$
\frac{1}{998001}=\frac{1}{999^2}=0.\overline{00001002003004\ldots995996997999},
$$

$$
\frac{1}{99980001}=\frac{1}{9999^2}=0.\overline{000001000200030004\ldots9995999699979999},
$$

\begin{align*}
\frac{1}{9999800001}&=\frac{1}{99999^2}\\
&=0.\overline{0000001000020000300004\ldots99995999969999799999}
\end{align*}
and so on.
:::

::::::{prf:theorem} Cauchy product
:label: Thm:Series:CauchyProduct
Let $\displaystyle\sum_{i=0}^{\infty}a_i(x-a)^i$ and $\displaystyle\sum_{j=0}^{\infty}b_j(x-a)^j$ be two power series centered at $x=a$, then

$$
\left(\sum_{i=0}^{\infty}a_i(x-a)^i\right)\left(\sum_{j=0}^{\infty}b_j(x-a)^j\right)=\sum_{n=0}^{\infty}c_n(x-a)^n
$$

with $c_n=\displaystyle\sum_{k=0}^na_kb_{n-k}$.

This is called the **Cauchy product** of the two power series, named after the French mathematician [Augustin-Louis Cauchy (1789-1857)](https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy).
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:CauchyProduct`
:class: tudproof, dropdown
Note that we have by setting $i+j=n$

\begin{align*}
\left(\sum_{i=0}^{\infty}a_i(x-a)^i\right)\left(\sum_{j=0}^{\infty}b_j(x-a)^j\right)&=\sum_{i=0}^{\infty}\sum_{j=0}^{\infty}a_ib_j(x-a)^{i+j}\\
&=\sum_{n=0}^{\infty}\sum_{k=0}^na_kb_{n-k}(x-a)^n.
\end{align*}
::::::

::::::{prf:example}
Consider the geometric series $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}$ for $|x|<1$. Then differentiation leads to

$$
\frac{1}{(1-x)^2}=\sum_{n=1}^{\infty}nx^{n-1},\quad |x|<1.
$$

Using the Cauchy product we obtain

$$
\frac{1}{(1-x)^2}=\frac{1}{1-x}\cdot\frac{1}{1-x}=\left(\sum_{i=0}^{\infty}x^i\right)\left(\sum_{j=0}^{\infty}x^j\right)=\sum_{n=0}^{\infty}c_nx^n,
$$

with $c_n=\displaystyle\sum_{k=0}^n1=n+1$. Now we have

$$
\sum_{n=0}^{\infty}(n+1)x^n=\sum_{n=1}^{\infty}nx^{n-1}.
$$

::::::

::::::{prf:example}
Consider

$$
\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n\quad\text{and}\quad\frac{1}{(1-x)^2}=\sum_{n=1}^{\infty}nx^{n-1}\quad\text{for}\quad|x|<1.
$$

Then the Cauchy product implies that

$$
\frac{1}{(1-x)^3}=\frac{1}{1-x}\cdot\frac{1}{(1-x)^2}=\left(\sum_{n=0}^{\infty}x^n\right)\left(\sum_{n=0}^{\infty}(n+1)x^n\right)=\sum_{n=0}^{\infty}c_nx^n
$$

with $c_n=\displaystyle\sum_{k=0}^n1\cdot(k+1)=\sum_{k=1}^{n+1}k=\tfrac{1}{2}(n+1)(n+2)$. Hence we have

$$
\frac{1}{(1-x)^3}=\frac{1}{2}\sum_{n=0}^{\infty}(n+1)(n+2)x^n.
$$

Note that differentiation of $\displaystyle\frac{1}{(1-x)^2}=\sum_{n=1}^{\infty}nx^{n-1}$ also leads to

$$
\frac{2}{(1-x)^3}=\sum_{n=2}^{\infty}n(n-1)x^{n-2}=\sum_{n=0}^{\infty}(n+1)(n+2)x^n,\quad|x|<1.
$$

::::::

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
