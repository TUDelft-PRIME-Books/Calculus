(Sec:Series:PowerSeries)=

# Power series

In this section we cover:

- Power series
- Interval of convergence
- Representation of functions as power series using geometric series
- Rules of calculation (sums, substitutions, differentiation, integration, products)

## Introduction

In {numref}`Sec:Series:GeometricSeries` you have encountered geometric series, which are series of the form $\displaystyle\sum_{n=0}^{\infty}ar^n$ for some constants $a$ and $r$. You also have seen in {prf:ref}`Thm:Series:GeometricSeries` that these series converge when $|r|<1$ and diverge when $|r|\geq1$, and in case of convergence, the sum of the series is $\dfrac{a}{1-r}$.

If we would consider $r$ not as a value, but as a variable $x$, then we would have a series of the form $\displaystyle\sum_{n=0}^{\infty}ax^n$ and if $|x|<1$ we would have $\displaystyle\sum_{n=0}^{\infty}ax^n=\frac{a}{1-x}=f(x)$.

In {numref}`Fig:PowerSeries:Introduction` we have plotted the function $f(x)=\dfrac{1}{1-x}$ and the partial sums $s_n(x)=\displaystyle\sum_{k=0}^n x^k$ of the power series $\displaystyle\sum_{n=0}^{\infty}x^n$ for $n=3$. As you can see in the figure, the function $f$ and the partial sum $s_3$ are close to each other for $x$ close to $0$, but they are not close to each other for $x$ close to $1$.

:::{figure} Images/PowerSeriesIntroduction.png
:name: Fig:PowerSeries:Introduction

The function $f(x)=\dfrac{1}{1-x}$ and the partial sum $s_n(x)$ of the power series $\displaystyle\sum_{n=0}^{\infty}x^n$. You can change the value of $n$ to see how the partial sums change when $n$ increases.
:::

:::{todo}
Replace {numref}`Fig:PowerSeries:Introduction` by an applet where the user can change the value of $n$ to see how the partial sums change when $n$ increases.
:::

Now, increase yourself in the image the value of $n$ to see how the partial sums change when $n$ increases. You should see that the partial sums get closer and closer to the function $f$ between $-1$ and $1$, but they do not get closer and closer to $f$ outside the interval $(-1,1)$. This behavior is something special and is the subject of this section.

Instead of only focussing on geometric series of the form $\displaystyle\sum_{n=0}^{\infty}ax^n$, we will now consider more general series of the form $\displaystyle\sum_{n=0}^{\infty}a_nx^n$ for some sequence $\{a_n\}_{n=0}^{\infty}$. These series are called power series and they have similar convergence properties as geometric series. Moreover, we can use geometric series to find power series representations of functions.

## Power series

We start with a formal definition of what we consider as a power series:

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
 
is called a **power series in $x-a$** or a **power series centered at $x=a$** or a **power series about $a$**.
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

## Grasple exercises

:::{todo}
Select exercises from Grasple and add them in {numref}`Sec:Series:PowerSeries`.
:::

## Exercises

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