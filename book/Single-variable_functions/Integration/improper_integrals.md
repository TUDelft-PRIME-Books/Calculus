(Sec:Integration:ImproperIntegrals)=

# Improper integrals

## Introduction

We have defined a definite integral $\displaystyle\int_a^bf(x)\,dx$ in {numref}`Sec:Integration:DefiniteIntegrals`, where the integrand $f$ is a *piecewise-continuous function* on the *closed* and *finite* interval $[a,b]$. Such a function is always *bounded*, which implies that the integral is a finite number. This coincides with the idea behind definite integrals being *finite* areas.

In this section we will extend the concept of definite integrals to more general functions and intervals.

## Proper and improper

To this end we need the following definition to make a distinction between the integrals we have defined so far and the more general integrals we will define in this section:

::::{prf:definition}
:label: Def:Integration:ProperIntegrals

A **proper integral** is a definite integral $\displaystyle\int_a^bf(x)\,dx$ where $f$ is a *continuous function* on the *finite interval* $[a,b]$.

Any other definite integral $\displaystyle\int_a^bf(x)\,dx$ is called an **improper integral**.
::::

Note that $[a,b]$ is always considered closed for all definite integrals from now on, so we will not explicitly mention that anymore.

But this means that an integral is improper if

- the interval of integration is not closed and/or not finite,

and/or

- the integrand is not continuous.

In the next sections we will consider first the two cases separately and then the combination of both cases.

## Infinite interval of integration

Let us first focus on the term *not finite*. This means that the interval of integration is infinite, i.e., it is of the form $(-\infty,b]$, $[a,\infty)$ or $(-\infty,\infty)$. Note that these intervals remain closed.

Improper integral over such intervals are defined as a (sum of) limit(s) which may or may not exist. We will give a definition for each of the three types of infinite intervals of integration.

::::::{prf:Definition} Improper integrals with right-infinite interval of integration
:label: Def:Integration:ImproperIntegralInfiniteIntervalRight

If $f$ is continuous on the interval $[a,\infty)$, then

$$
\int_a^{\infty}f(x)\,dx=\lim_{R\to\infty}\int_a^Rf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the proper integral $\displaystyle\int_a^{\infty}f(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_a^{\infty}f(x)\,dx$ is **divergent**. If the limit does not exist but approaches $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_a^{\infty}f(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::


::::::{prf:Definition} Improper integrals with left-infinite interval of integration
:label: Def:Integration:ImproperIntegralInfiniteIntervalLeft

If $f$ is continuous on the interval $(-\infty,b]$, then

$$
\int_{-\infty}^bf(x)\,dx=\lim_{R\to-\infty}\int_R^bf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the proper integral $\displaystyle\int_{-\infty}^bf(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_{-\infty}^bf(x)\,dx$ is **divergent**. If the limit does not exist but approaches $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_{-\infty}^bf(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::

::::::{prf:Definition} Improper integrals with double-infinite interval of integration
:label: Def:Integration:ImproperIntegralInfiniteIntervalDouble

If $f$ is continuous on the interval $(-\infty,\infty)$, then

$$
\int_{-\infty}^{\infty}f(x)\,dx=\int_{-\infty}^cf(x)\,dx+\int_c^{\infty}f(x)\,dx
$$
provided the two improper integrals on the right converge for some value of $c\in\mathbb{R}$.

If the two improper integrals converge, we say that the proper integral $\displaystyle\int_{-\infty}^{\infty}f(x)\,dx$ is **convergent**.

If at least one of the two improper integrals does not converge, we say that the improper integral $\displaystyle\int_{-\infty}^{\infty}f(x)\,dx$ is **divergent**.

If both improper integrals on the right diverge to infinity, we say that the improper integral $\displaystyle\int_{-\infty}^{\infty}f(x)\,dx$ **diverges to infinity**. If both improper integrals on the right diverge to negative infinity, we say that the improper integral $\displaystyle\int_{-\infty}^{\infty}f(x)\,dx$ **diverges to negative infinity**.

::::::

So how do we evaluate an improper integral? We will see that in some cases we can evaluate the limit(s) and therefore the improper integral. In other cases we cannot evaluate the limit(s) but we can still determine whether the improper integral is convergent or divergent. In yet other cases we cannot even determine whether the improper integral is convergent or divergent.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample1

Consider the function $\displaystyle\frac{1}{x\sqrt{x}}$ on the interval $[1,\infty)$:

```{figure} Images/improper1.png
---
width: 50%
name: Fig:Integration:ImproperIntegral1
align: center
---
The function $\displaystyle\frac{1}{x\sqrt{x}}$ on the interval $[1,\infty)$.
```

This function $f$ is continuous on $[1,\infty)$ and therefore we can define the improper integral $\displaystyle\int_1^{\infty}\frac{dx}{x\sqrt{x}}$ as in {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalRight`. We have

\begin{align*}
\int_1^{\infty}\frac{dx}{x\sqrt{x}} &= \lim_{R\to\infty}\int_1^R\frac{dx}{x\sqrt{x}} \\
&= \lim_{R\to\infty}\bigg[-\frac{2}{\sqrt{x}}\bigg]_1^R \\
&= \lim_{R\to\infty}\left(2-\frac{2}{\sqrt{R}}\right) \\
&= 2.
\end{align*}

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample2
Now consider the function $\displaystyle\frac{1}{\sqrt{x}}$ on the same interval $[1,\infty)$:

```{figure} Images/improper2.png
---
width: 50%
name: Fig:Integration:ImproperIntegral2
align: center
---
The function $\displaystyle\frac{1}{\sqrt{x}}$ on the interval $[1,\infty)$.
```

In this case we have another function that is continuous on $[1,\infty)$ and therefore we can define the improper integral $\displaystyle\int_1^{\infty}\frac{dx}{\sqrt{x}}$ as in {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalRight`. We have 

\begin{align*}
\int_1^{\infty}\frac{dx}{\sqrt{x}} &= \lim_{R\to\infty}\int_1^R\frac{dx}{\sqrt{x}} \\
&= \lim_{R\to\infty}\bigg[2\sqrt{x}\bigg]_1^R \\
&= \lim_{R\to\infty}\left(2\sqrt{R}-2\right) \\
\end{align*}

This last limit does not exist, but approaches $\infty$. In this case we say that the improper integral diverges to infinity.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample3

Now we consider the function $\dfrac{dx}{1+x^2}$ that is continuous on $(-\infty,\infty)$ and therefore we can define the improper integral $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$ as in {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalDouble`.

```{figure} Images/improper3.png
---
width: 50%
name: Fig:Integration:ImproperIntegral3
align: center
---
The function $\displaystyle\frac{1}{1+x^2}$ on the interval $(-\infty,\infty)$.
```

We start by splitting the integral into two integrals as in {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalDouble`:

$$
\int_{-\infty}^{\infty}\frac{dx}{1+x^2}=\int_{-\infty}^0\frac{dx}{1+x^2}+\int_0^{\infty}\frac{dx}{1+x^2}.
$$

In this case we choose the central point $c=0$ but we could have chosen any other value of $c\in\mathbb{R}$ as well. The value of the integral does, ultimately, not depend on the choice of $c$. 

Now we have for the first integral

\begin{align*}
\int_{-\infty}^0\frac{dx}{1+x^2} &= \lim_{R\to-\infty}\int_R^0\frac{dx}{1+x^2} \\
&= \lim_{R\to-\infty}\bigg[\arctan(x)\bigg]_R^0\\
&= \lim_{R\to-\infty}\left(-\arctan(R)\right) \\
&=\frac{1}{2}\pi
\end{align*}

and for the second integral

\begin{align*}
\int_0^{\infty}\frac{dx}{1+x^2}&=\lim_{R\to\infty}\int_0^R\frac{dx}{1+x^2}\\
&=\lim_{R\to\infty}\bigg[\arctan(x)\bigg]_0^R\\
&=\lim_{R\to\infty}\arctan(R)\\
&=\frac{1}{2}\pi.
\end{align*}

Hence, we have

\begin{align*}
\int_{-\infty}^{\infty}\frac{dx}{1+x^2} &= \int_{-\infty}^0\frac{dx}{1+x^2}+\int_0^{\infty}\frac{dx}{1+x^2} \\
&= \frac{1}{2}\pi+\frac{1}{2}\pi \\
&= \pi.
\end{align*}

::::::

::::::{note}
:name: Note:Integration:ImproperIntegralsInfiniteIntervalExample3

```{figure} Images/cauchy.png
---
width: 50%
name: Fig:Integration:CauchyDistribution
align: center
---
The probability density function of the standard Cauchy distribution.
```

In probability and statistics the function $\displaystyle\frac{1}{\pi}\cdot\frac{1}{1+x^2}$ is the probability density function of the standard Cauchy distribution, which is named after the French mathematician [Augustin-Louis Cauchy (1789-1857)](https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy).

{prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalDouble` implies that the integral $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$ is convergent and equal to $\pi$. Hence, the total area under the curve of the probability density function of the standard Cauchy distribution is equal to $1$ as expected for a probability density function.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample4

We can also attempt to integrate trigonometric functions over infinite intervals, for example the cosine function over the interval $[0,\infty)$:

```{figure} Images/improper4.png
---
width: 50%
name: Fig:Integration:ImproperIntegral4
align: center
---
The function $\displaystyle\cos(x)$ on the interval $[0,\infty)$.
```

\begin{align*}
\int_0^{\infty}\cos(x)\,dx &= \lim_{R\to\infty}\int_0^R\cos(x)\,dx \\
&= \lim_{R\to\infty}\bigg[\sin(x)\bigg]_0^R \\
&=\lim_{R\to\infty}\sin(R).
\end{align*}

This limit does not exist and is neither $\infty$ nor $-\infty$. In this case we can only say that the integral diverges.

::::::

## Discontinuous integrands

Now we have covered the intervals, it is time to consider the integrand. For this subsection we assume that the interval of integration is closed and finite, i.e., of the form $[a,b]$.

{numref}`Section:Continuity` discusses what we consider to be continuity with respect to a function. As continuity is a local property, we will focus on three possible cases of discontinuity of the integrand $f$ on the interval $[a,b]$:

- the integrand $f$ is not right-continuous at $x=a$ (i.e. at the left of the interval).
- the integrand $f$ is not left-continuous at $x=b$ (i.e. at the right of the interval).
- the integrand $f$ is discontinuous at some point $c\in(a,b)$ (i.e. in the interior of the interval).

Note that we consider discontinuity or (not continuity) in general. Examples of discontinuity include jump discontinuity, infinite discontinuity and removable discontinuity.

In particular, we do not require the integrand to be unbounded near the point of discontinuity, but it may be unbounded as well.

Note that also piecewise-continuity of the integrand is not required, but is one, or even a combination, of the above  cases.

This way of defining improper integrals with discontinuous integrand is more general than the way it is often defined in other textbooks, where the integrand is required to be unbounded near the point of discontinuity.

For each of the three cases we will define how to handle the improper integral $\displaystyle\int_a^bf(x)\,dx$.

::::::{prf:Definition} Improper integrals with discontinuous integrand at left endpoint
:label: Def:Integration:ImproperIntegralLeftDiscontinuousIntegrand

If $f$ is continuous on the interval $(a,b]$, then

$$
\int_a^bf(x)\,dx=\lim_{c\downarrow a}\int_c^bf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the proper integral $\displaystyle\int_a^bf(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ is **divergent**. If the limit does not exist but approaches $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::

::::::{prf:Definition} Improper integrals with discontinuous integrand at right endpoint
:label: Def:Integration:ImproperIntegralRightDiscontinuousIntegrand

If $f$ is continuous on the interval $[a,b)$, then

$$
\int_a^bf(x)\,dx=\lim_{c\uparrow b}\int_a^cf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the proper integral $\displaystyle\int_a^bf(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ is **divergent**. If the limit does not exist but approaches $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::

::::::{prf:Definition} Improper integrals with discontinuous integrand at internal point
:label: Def:Integration:ImproperIntegralInternalDiscontinuousIntegrand

If $f$ is discontinuous at some point $c\in(a,b)$, then

$$
\int_a^bf(x)\,dx=\int_a^cf(x)\,dx+\int_c^bf(x)\,dx
$$
provided the two improper integrals on the right converge for some value of $c\in\mathbb{R}$.

If the two improper integrals converge, we say that the proper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ is **convergent**.

If at least one of the two improper integrals does not converge, we say that the improper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ is **divergent**.

If both improper integrals on the right diverge to infinity, we say that the improper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ **diverges to infinity**. If both improper integrals on the right diverge to negative infinity, we say that the improper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ **diverges to negative infinity**.

::::::

We start with an example of an improper integral with a discontinuous integrand at an internal point of the interval of integration.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsDiscontinuousIntegrandExample1

```{figure} Images/improper5.png
---
width: 50%
name: Fig:Integration:ImproperIntegral5
align: center
figclass: margin
---
The function $\displaystyle\frac{1}{x^2}$.
```

We integrate the function $\displaystyle\frac{1}{x^2}$ on the interval $[-1,1]$. This function is continuous on $[-1,0)$ and on $(0,1]$ but is not continuous at $x=0$. Hence, we can define the improper integral $\displaystyle\int_{-1}^1\frac{dx}{x^2}$ as in {prf:ref}`Def:Integration:ImproperIntegralInternalDiscontinuousIntegrand`. We have

$$
\int_{-1}^1\frac{dx}{x^2}=\int_{-1}^0\frac{dx}{x^2}+\int_0^1\frac{dx}{x^2}.
$$

Now we have

\begin{align*}
\int_{-1}^0\frac{dx}{x^2} &= \lim_{c\uparrow0}\int_{-1}^c\frac{dx}{x^2} \\
&= \lim_{c\uparrow0}\bigg[-\frac{1}{x}\bigg]_{-1}^c \\
&= \lim_{c\uparrow0}\left(-\frac{1}{c}+1\right) \\
&= \infty.
\end{align*}

At this point we can already conclude that the integral $\displaystyle\int_{-1}^1\frac{dx}{x^2}$ is divergent, but we will also evaluate the second integral to see that it also diverges to infinity:

\begin{align*}
\int_0^1\frac{dx}{x^2} &= \lim_{c\downarrow0}\int_c^1\frac{dx}{x^2} \\
&= \lim_{c\downarrow0}\bigg[-\frac{1}{x}\bigg]_c^1 \\
&= \lim_{c\downarrow0}\left(-1+\frac{1}{c}\right) \\
&=\infty.
\end{align*}

Because both integrals diverge to infinity, we say that the improper integral $\displaystyle\int_{-1}^1\frac{dx}{x^2}$ diverges to infinity, which we can write (informally) as

$$
\int_{-1}^1\frac{dx}{x^2}=\infty.
$$

::::::

::::::{warning}
:name: Warning:Integration:ImproperIntegralsDiscontinuousIntegrandWarning1

The calculation

$$
\int_{-1}^1\frac{dx}{x^2}=-\frac{1}{x}\bigg|_{-1}^1=-1-1=-2
$$

is clearly wrong! Note that the integrand is positive on $[-1,1]$. The evaluation is incorrect because the integrand is not continuous at $x=0$. So, the fundamental theorem of calculus cannot be applied directly.
::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsDiscontinuousIntegrandExample2

```{figure} Images/improper6.png
---
width: 50%
name: Fig:Integration:ImproperIntegral6
align: center
figclass: margin
---
The function $\displaystyle\frac{1}{x-1}$.
```

Since $\dfrac{1}{x-1}$ is continuous for all $x\in\mathbb{R}$ except at $x=1$, we have

$$
\int_0^3\frac{dx}{x-1}=\int_0^1\frac{dx}{x-1}+\int_1^3\frac{dx}{x-1}
$$

with

\begin{align*}
\int_0^1\frac{dx}{x-1} &= \lim_{c\uparrow1}\int_0^c\frac{dx}{x-1} \\
&= \lim_{c\uparrow1}\bigg[\ln|x-1|\bigg]_0^c \\
&= \lim_{c\uparrow1}\ln|c-1| \\
&= -\infty
\end{align*}

and

\begin{align*}
\int_1^3\frac{dx}{x-1} &= \lim_{c\downarrow1}\int_c^3\frac{dx}{x-1} \\
&= \lim_{c\downarrow1}\bigg[\ln|x-1|\bigg]_c^3 \\
&= \lim_{c\downarrow1}\left(\ln(2)-\ln|c-1|\right) \\
&= \infty.
\end{align*}

Because both integrals diverge, we say that the improper integral $\displaystyle\int_0^3\frac{dx}{x-1}$ diverges to infinity.

::::::

::::::{warning}
:name: Warning:Integration:ImproperIntegralsDiscontinuousIntegrandWarning2

It would be wrong to conclude that

$$
\int_0^3\frac{dx}{x-1}=\infty-\infty=0
$$

and it is also incorrect to state that

$$
\int_0^3\frac{dx}{x-1}=\ln|x-1|\bigg|_0^3=\ln(2)-\ln(1)=\ln(2).
$$

Since the integrand is discontinuous at $x=1$ the fundamental theorem cannot be applied in this way.
::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsDiscontinuousIntegrandExample3
```{figure} Images/improper7.png
---
width: 50%
name: Fig:Integration:ImproperIntegral7
align: center
figclass: margin
---
The function $\displaystyle\ln(x)$.
```

Consider $\displaystyle\int_0^1\ln(x)\,dx$. 

Using integration by parts, we have

\begin{align*}
\int\ln(x)\,dx &= x\ln(x)-\int x\cdot\frac{1}{x}\,dx \\
&= x\ln(x)-x+C.
\end{align*}

Hence, we have

\begin{align*}
\int_0^1\ln(x)\,dx &= \lim_{c\downarrow0}\bigg[x\ln(x)-x\bigg]_c^1 \\
&= \lim_{c\downarrow0}\left(-1-c\ln(c)+c\right).
\end{align*}

Using l'Hospital's rule we obtain

\begin{align*}
\lim_{c\downarrow0}c\ln(c) &= \lim_{c\downarrow0}\frac{\ln(c)}{\frac{1}{c}} \\
&= \lim_{c\downarrow0}\frac{\frac{1}{c}}{-\frac{1}{c^2}} \\
&= \lim_{c\downarrow0}\left(-c\right) \\
&=0.
\end{align*}

We conclude that

$$
\int_0^1\ln(x)\,dx=\lim_{c\downarrow0}\left(-1-c\ln(c)+c\right)=-1-0+0=-1.
$$

::::::

## Comparing improper integrals

Sometimes integrals are not easy to evaluate. However, in many cases evaluation is not necessary as long as we can find out whether the integral is convergent or divergent. In case of convergence we might able to find a lower and upper bound for the integral. The following theorem might be helpful.

::::::{prf:Theorem} Comparison theorem for improper integrals
:label: Thm:Integration:ImproperIntegralsComparison
Assume $f$ and $g$ are continuous on $(a,b)$ with $-\infty\leq a<b\leq\infty$ and $0\leq f(x)\leq g(x)$, then:

(a) If $\displaystyle\int_a^bg(x)\,dx$ is convergent, then $\displaystyle\int_a^bf(x)\,dx$ is convergent.

(b) If $\displaystyle\int_a^bf(x)\,dx$ is divergent, then $\displaystyle\int_a^bg(x)\,dx$ is divergent.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsComparisonExample1
Without evaluating the integral, we determine whether $\displaystyle\int_0^{\infty}\frac{x}{1+x^3}\,dx$ is convergent or divergent and give an interval containing its value.

First, let $\displaystyle\int_0^{\infty}\frac{x}{1+x^3}\,dx=\int_0^1\frac{x}{1+x^3}\,dx+\int_1^{\infty}\frac{x}{1+x^3}\,dx$.

The first integral on the right involves a continuous function on a finite interval, which is convergent. 

Since $0\leq\dfrac{x}{1+x^3}\le\dfrac{1}{1+x^3}<1$ for $0\le x\le 1$, we have

$$
0 \leq \int_0^1\frac{x}{1+x^3}\,dx<1.
$$

Note that $0\leq\dfrac{x}{1+x^3}\leq\dfrac{x}{x^3}=\dfrac{1}{x^2}$ for $x\geq1$ and since

$$
\int_1^{\infty}\frac{dx}{x^2}=\bigg[-\frac{1}{x}\bigg]_1^{\infty}=1,
$$

we conclude that the second integral is convergent as well and that 

$$
0 \leq \int_1^{\infty}\frac{x}{1+x^3}\,dx\le 1.
$$

We conclude that $\displaystyle\int_0^{\infty}\frac{x}{1+x^3}\,dx$ is convergent and that

$$
0 \leq \int_0^{\infty}\frac{x}{1+x^3}\,dx<2.
$$

::::::

::::::{note}
:name: Note:Integration:ImproperIntegralsComparisonExample1

We will often use the short notation $\displaystyle\int_1^{\infty}\frac{dx}{x^2}=\bigg[-\frac{1}{x}\bigg]_1^{\infty}=1$ instead of

$$
\int_1^{\infty}\frac{dx}{x^2}=\lim_{R\to\infty}\bigg[-\frac{1}{x}\bigg]_1^R=\lim_{R\to\infty}\left(1-\frac{1}{R}\right)=1.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsComparisonExample2
Consider $\displaystyle\int_0^{\infty}e^{-x^2}\,dx$.

It is impossible to find an antiderivative of $e^{-x^2}$, but for $e^{-x}$ this is easy. However, the inequality $e^{-x^2}\leq e^{-x}$ only holds for $x\geq1$. Therefore, we consider

$$
\int_0^{\infty}e^{-x^2}\,dx=\int_0^1e^{-x^2}\,dx+\int_1^{\infty}e^{-x^2}\,dx.
$$

For $0\leq x\leq1$ we have $0<e^{-x^2}\leq1$, and thus

$$
0<\int_0^{\infty}e^{-x^2}\,dx\leq\int_0^1\,dx=1.
$$

For $x\geq1$ we have $x^2\geq x$, so $-x^2\leq-x$ and $0<e^{-x^2}\leq e^{-x}$. Thus

$$
0<\int_1^{\infty}e^{-x^2}\,dx\leq\int_1^{\infty}e^{-x}\,dx=\bigg[-e^{-x}\bigg]_1^{\infty}=e^{-1}.
$$

We conclude that $\displaystyle\int_0^{\infty}e^{-x^2}\,dx$ is convergent and that

$$
0<\int_0^{\infty}e^{-x^2}\,dx<1+e^{-1}\approx1.36788.
$$

::::::

::::::{note}
:name: Note:Integration:ImproperIntegralsGaussianIntegral

Later we will see that $\displaystyle\int_0^{\infty}e^{-x^2}\,dx=\tfrac{1}{2}\sqrt{\pi}\approx0.88623$.

By symmetry, we also have: $\displaystyle\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt{\pi}$, which is called the **Gaussian integral**, named after the German mathematician [Johann Carl Friedrich Gauss (1777-1855)](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss).

```{figure} Images/normal.png
---
width: 50%
name: Fig:Integration:NormalDistribution
align: center
---
The probability density function of the standard normal distribution.
```

In probability and statistics the function $\displaystyle\frac{1}{\sqrt{2\pi}}\cdot e^{-\frac12x^2}$ is known as the probability density function of the **standard normal distribution** or **Gaussian distribution**. The curve is sometimes referred to as the **bell curve**.
::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsComparisonExample3
Consider $\displaystyle\int_1^{\infty}\frac{2+\cos(x)}{x}\,dx$.

Note that $-1\leq\cos(x)\leq1$ and therefore $1\leq2+\cos(x)\leq3$. This implies that

$$
\frac{2+\cos(x)}{x}\geq\frac{1}{x}\quad\text{and}\quad\int_1^{\infty}\frac{dx}{x}=\ln(x)\bigg|_1^{\infty}=\infty.
$$

This implies that $\displaystyle\int_1^{\infty}\frac{2+\cos(x)}{x}\,dx$ is divergent.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsComparisonExample4
Consider $\displaystyle\int_1^{\infty}\frac{1+e^{-x}}{\sqrt{x}}\,dx$.

Note that $1+e^{-x}>1$ and

$$
\int_1^{\infty}\frac{dx}{\sqrt{x}}=2\sqrt{x}\bigg|_1^{\infty}=\infty.
$$

We conclude that $\displaystyle\int_1^{\infty}\frac{1+e^{-x}}{\sqrt{x}}\,dx$ is divergent.
::::::

## The Feynman method

Sometimes an integral is easier to evaluate if we modify the integrand using a parameter such that a specific value of this parameter leads to the original integral. This method was developed by the American theoretical physicist [Richard Phillips Feynman (1918-1988)](https://en.wikipedia.org/wiki/Richard_Feynman) and is based on the following theorem.

::::::{prf:Theorem}
:label: Thm:Integration:ImproperIntegralsFeynmanMethod
If $g(x,t)$ and $\displaystyle\frac{\partial}{\partial t}g(x,t)$ are both continuous for all $x\in[a,b]$, then

$$
\frac{d}{dt}\int_a^bg(x,t)\,dx=\int_a^b\frac{\partial}{\partial t}g(x,t)\,dx.
$$

::::::

::::::{note}
:name: Note:Integration:ImproperIntegralsMultivariableFunctionsAndPartialDerivatives

The notation $g(x,t)$ indicates that $g$ is a function of two variables, $x$ and $t$ and will be explained in more detail in {numref}`Sec:MultivariableFunctions`. For now, just assume that $g(x,t)$ is a function of two variables and that $g(x,t_0)$ means that you must substitute $t$ with $t_0$ in the function $g$.

The notation $\dfrac{\partial}{\partial t}$ denotes the derivative with respect to $t$ and will be explained in {numref}`Sec:PartialDerivatives`. For now, just assume that $\dfrac{\partial}{\partial t}$ means that you must take the derivative of the function with respect to $t$ while treating $x$ as a constant. For example, if $f(x,t)=x^t$, then $\dfrac{\partial}{\partial t}f(x,t)=x^t\ln(x)$.
::::::

The Feynman method itself is captured best in an algorithmic way:

:::{prf:algorithm} Feynman method
For any definite integral of the form $\displaystyle\int_a^bf(x)\,dx$ perform the following steps:

1. Introduce new function $g$ based on the integrand $f$ and define $I(t)=\displaystyle\int_a^bg(x,t)\,dx$ such that

    - $I(t_0)=\alpha$ for some value of $t_0$ and some constant $\alpha\in\mathbb{R}$.

    - $g(x,t_1)=f(x)$ for some value of $t_1$. This implies that $I(t_1)=\displaystyle\int_a^bf(x)\,dx$.

3. Compute the partial derivative $\displaystyle\frac{d}{dt}g(x,t)$.

4. Compute the integral $I'(t)=\displaystyle\int_a^b\frac{d}{dt}g(x,t)\,dx$.

5. Integrate $I'(t)$ with respect to $t$ to find $I(t)$ (including a constant of integration).

6. Determine the value of the constant of integration using the value of $I(t_0)=\alpha$.

6. Evaluate $I(t_1)$ to find the value of the original integral $\displaystyle\int_a^bf(x)\,dx$.
:::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsFeynmanExample1
Consider the improper integral $\displaystyle\int_0^1\frac{x-1}{\ln(x)}\,dx$, which is extremely difficult to evaluate.

Define $g(t,x)=\frac{x^t-1}{\ln(x)}$ and $I(t)=\displaystyle\int_0^1\frac{x^t-1}{\ln(x)}\,dx$ for $t\geq0$, then we have $I(0)=0$,

$$
\frac{\partial}{\partial t}g(t,x)=\frac{x^t\ln(x)}{\ln(x)}=x^t,
$$

and

$$
I'(t)=\int_0^1\frac{\partial}{\partial t}\frac{x^t-1}{\ln(x)}\,dx=\int_0^1x^t\,dx=\frac{x^{t+1}}{t+1}\bigg|_0^1=\frac{1}{t+1}.
$$

This implies that $I(t)=\ln|t+1|+C$ with $C=I(0)=0$. This gives

$$
I(t)=\int_0^1\frac{x^t-1}{\ln(x)}\,dx=\ln(t+1)
$$

for $t\geq0$. We conclude that

$$
\int_0^1\frac{x-1}{\ln(x)}\,dx=\ln(2).
$$

Similarly, we find that $\displaystyle I(2)=\int_0^1\frac{x^2-1}{\ln(x)}\,dx=\ln(3)$ and $\displaystyle I(\tfrac{1}{2})=\int_0^1\frac{\sqrt{x}-1}{\ln(x)}\,dx=\ln\left(\tfrac{3}{2}\right)$, for instance.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsFeynmanExample2
Consider the integral $\displaystyle\int_0^1\frac{\sin(\ln(x))}{\ln(x)}\,dx$.

Let $I(t)=\displaystyle\int_0^1\frac{\sin(t\ln(x))}{\ln(x)}\,dx$, then we have $I(0)=0$ and using the substitution $\ln(x)=y$ or $x=e^y$

$$
I'(t)=\int_0^1\cos(t\ln(x))\,dx=\int_{-\infty}^0\cos(ty)e^y\,dy=\int_0^{\infty}e^{-y}\cos(ty)\,dy.
$$

Now we have using integration by parts

\begin{align*}
\int_0^{\infty}e^{-y}\cos(ty)\,dy&=-e^{-y}\cos(ty)\bigg|_0^{\infty}-t\int_0^{\infty}e^{-y}\sin(ty)\,dy\\
&=1+te^{-y}\sin(ty)\bigg|_0^{\infty}-t^2\int_0^{\infty}e^{-y}\cos(ty)\,dy\\
&=1-t^2\int_0^{\infty}e^{-y}\cos(ty)\,dy.
\end{align*}

Because the integral $I'(t)$ appears on both sides of the equation, we can solve for $I'(t)$ to find that

$$
I'(t)=\int_0^{\infty}e^{-y}\cos(ty)\,dy=\frac{1}{1+t^2}+C.
$$

Since $I(0)=0$ this implies that $I(t)=\arctan(t)$.

We finally arrive at

$$
\int_0^1\frac{\sin(\ln(x))}{\ln(x)}\,dx=I(1)=\arctan(1)=\tfrac{1}{4}\pi.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsFeynmanExample3
Consider the integral $I(t)=\displaystyle\int_0^{\infty}\frac{e^{-\alpha x}\sin(xt)}{x}\,dx$ for $\alpha>0$ and $t\geq0$. Since $\displaystyle\lim\limits_{x\downarrow0}\frac{\sin(xt)}{x}=t$, the integral is convergent. Then we have $I(0)=0$ and using integration by parts

\begin{align*}
I'(t)&=\int_0^{\infty}e^{-\alpha x}\cos(xt)\,dx\\
&=\left[\frac{t}{\alpha^2+t^2}e^{-\alpha x}\sin(xt)-\frac{\alpha}{\alpha^2+t^2}e^{-\alpha x}\cos(xt)\right]_0^{\infty}\\
&=\frac{\alpha}{\alpha^2+t^2}.
\end{align*}
This implies that $I(t)=\displaystyle\arctan\left(\frac{t}{\alpha}\right)$.

For instance, this implies that $\displaystyle\int_0^{\infty}\frac{e^{-\alpha x}\sin(\alpha x)}{x}\,dx=\arctan(1)=\tfrac{1}{4}\pi$ for all $\alpha>0$. Furthermore, we have

$$
\int_0^{\infty}\frac{e^{-x\sqrt{3}}\sin(x)}{x}\,dx=\arctan\left(\frac{1}{\sqrt{3}}\right)=\frac{1}{6}\pi
$$

and

$$
\int_0^{\infty}\frac{e^{-x}\sin(x\sqrt{3})}{x}\,dx=\arctan\left(\sqrt{3}\right)=\frac{1}{3}\pi.
$$

::::::

## Special improper integrals

There exist many special improper integrals that are often used in various applications. We will discuss some of them here.

We start with the so-called $p$-integrals:

:::{prf:definition} $p$-integrals
:label: Def:Integration:ImproperIntegralsPIntegrals
An integral of the form $\displaystyle\int_a^{\infty}\frac{dx}{x^p}$ or $\displaystyle\int_0^a\frac{dx}{x^p}$ for some $a>0$ and $p\in\mathbb{R}$ is called a **$p$-integral**.
:::

$p$-integrals can easily be analysed using the next theorem.

::::::{prf:Theorem}
:label: Thm:Integration:ImproperIntegralsPIntegrals
For $0<a<\infty$ we have

(a) $\displaystyle\int_a^{\infty}\frac{dx}{x^p}=\begin{cases}\dfrac{a^{1-p}}{p-1}, &p>1\\\infty, &p\leq1.\end{cases}$

(b) $\displaystyle\int_0^a\frac{dx}{x^p}=\begin{cases}\dfrac{a^{1-p}}{1-p}, &p<1\\\infty, &p\geq1.\end{cases}$
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Integration:ImproperIntegralsPIntegrals`
:class: tudproof, dropdown
:name: Proof:Integration:ImproperIntegralsPIntegrals

(a) We have

$$
\int_a^{\infty}\frac{dx}{x^p}=\lim_{R\to\infty}\int_a^R\frac{dx}{x^p}=\lim_{R\to\infty}\bigg[\frac{x^{1-p}}{1-p}\bigg]_a^R=\lim_{R\to\infty}\left(\frac{R^{1-p}}{1-p}-\frac{a^{1-p}}{1-p}\right).
$$

This limit exists if $1-p<0$ (then: $\displaystyle\lim_{R\to\infty}\frac{R^{1-p}}{1-p}=0$) and $\displaystyle\lim_{R\to\infty}\frac{R^{1-p}}{1-p}$ equals $\infty$ if $1-p>0$. For $p=1$ the integral reads $\displaystyle\int_a^{\infty}\frac{dx}{x}$ which is divergent.

(b) We have

$$
\int_0^a\frac{dx}{x^p}=\lim_{c\downarrow0}\int_c^a\frac{dx}{x^p}=\lim_{c\downarrow0}\bigg[\frac{x^{1-p}}{1-p}\bigg]_c^a=\lim_{c\downarrow0}\left(\frac{a^{1-p}}{1-p}-\frac{c^{1-p}}{1-p}\right).
$$

This limit exists if $1-p>0$ (then: $\displaystyle\lim_{c\downarrow0}\frac{c^{1-p}}{1-p}=0$) and $\displaystyle\lim_{c\downarrow0}\frac{c^{1-p}}{1-p}$ equals $-\infty$ if $1-p<0$. For $p=1$ the integral reads $\displaystyle\int_0^a\frac{dx}{x}$ which is divergent.

::::::

Next up is the gamma function:

:::{prf:definition} The gamma function
:label: Def:Integration:ImproperIntegralsGammaFunction

The **gamma function** $\Gamma(x)$ is defined by the improper integral

$$
\Gamma(x)=\int_0^{\infty}t^{x-1}e^{-t}\,dt,\quad x>0.
$$
:::

This gamma function converges for all $x>0$ and has many interesting properties. We start by showing this convergence and then we will discuss some of its properties.

Let $\displaystyle\int_0^{\infty}t^{x-1}e^{-t}\,dt=\int_0^1t^{x-1}e^{-t}\,dt+\int_1^{\infty}t^{x-1}e^{-t}\,dt$.

For $0\leq t\leq1$ we have: $t^{x-1}e^{-1}\leq t^{x-1}e^{-t}\leq t^{x-1}$ and 

$$
\int_0^1t^{x-1}\,dt=\frac{t^x}{x}\bigg|_0^1=\frac{1}{x},\quad x>0.
$$

For $t\geq1$ we have: $0<t^{x-1}e^{-t}\leq e^{-t}$ and

$$
\int_1^{\infty}e^{-t}\,dt=-e^{-t}\bigg|_1^{\infty}=e^{-1}.
$$

We conclude that $\displaystyle\int_0^{\infty}t^{x-1}e^{-t}\,dt$ converges for $x>0$.

Note that $\Gamma(1)=\displaystyle\int_0^{\infty}e^{-t}\,dt=-e^{-t}\bigg|_0^{\infty}=1$.

Using integration by parts we obtain for $x>0$

\begin{align*}
\Gamma(x+1)&=\int_0^{\infty}t^xe^{-t}\,dt\\
&=-\int_0^{\infty}t^x\,de^{-t}\\
&=-t^xe^{-t}\bigg|_0^{\infty}+\int_0^{\infty}e^{-t}\,dt^x\\
&=0+x\int_0^{\infty}t^{x-1}e^{-t}\,dt\\
&=x\Gamma(x).
\end{align*}

This implies that $\Gamma(n+1)=n!$ for $n=0,1,2,\ldots$. So, the gamma function can be seen as a generalisation of the factorial.

Furthermore, using the substitution $t=x^2$ we have

$$
\Gamma(\tfrac{1}{2})=\int_0^{\infty}t^{-\frac{1}{2}}e^{-t}\,dt=\int_0^{\infty}x^{-1}e^{-x^2}\cdot2x\,dx=2\int_0^{\infty}e^{-x^2}\,dx.
$$
 
Later we will prove that $\displaystyle\int_0^{\infty}e^{-x^2}\,dx=\tfrac{1}{2}\sqrt{\pi}$. This implies that $\Gamma(\frac{1}{2})=\sqrt{\pi}$.

Now we turn our attention to the Dirichlet integral:

:::{prf:definition} The Dirichlet integral
:label: Def:Integration:ImproperIntegralsDirichletIntegral

The **Dirichlet integral** is defined by the improper integral

$$
\int_0^{\infty}\frac{\sin(x)}{x}\,dx.
$$

:::

This integral is named after the German mathematician [Johann Peter Gustav Lejeune Dirichlet (1805-1859)](https://en.wikipedia.org/wiki/Peter_Gustav_Lejeune_Dirichlet).

This special integral can be evaluated using the Feynman method, which leads to the following result.

::::::{prf:Theorem} The Dirichlet integral
:label: Thm:Integration:ImproperIntegralsDirichletIntegral

$$
\int_0^{\infty}\frac{\sin(x)}{x}\,dx=\frac{1}{2}\pi.
$$

::::::

::::::{admonition} Proof of {prf:ref}`Thm:Integration:ImproperIntegralsDirichletIntegral`
:class: tudproof, dropdown
:name: Proof:Integration:ImproperIntegralsDirichletIntegral

Since $\displaystyle\lim\limits_{x\downarrow0}\frac{\sin(x)}{x}=1$, the integrand is continuous and the integral is convergent. 

Now let: $I(t)=\displaystyle\int_0^{\infty}e^{-xt}\frac{\sin(x)}{x}\,dx$. Then we have

\begin{align*}
I'(t)&=-\int_0^{\infty}e^{-xt}\sin(x)\,dx\\
&=\int_0^{\infty}e^{-xt}\,d\cos(x)\\
&=e^{-xt}\cos(x)\bigg|_0^{\infty}-\int_0^{\infty}\cos(x)\,de^{-xt}\\
&=-1+t\int_0^{\infty}e^{-xt}\cos(x)\,dx\\
&=-1+t\int_0^{\infty}e^{-xt}\,d\sin(x)\\
&=-1+te^{-xt}\sin(x)\bigg|_0^{\infty}-t\int_0^{\infty}\sin(x)\,de^{-xt}\\
&=-1+t^2\int_0^{\infty}e^{-xt}\sin(x)\,dt.
\end{align*}

This implies that $\displaystyle\int_0^{\infty}e^{-xt}\sin(x)\,dx=\frac{1}{1+t^2}$ and therefore $I'(t)=-\dfrac{1}{1+t^2}$. So

$$
I(t)=-\arctan(t)+C.
$$

Note that $0=\displaystyle\lim\limits_{t\to\infty}I(t)=-\tfrac{1}{2}\pi+C$, which implies that $C=\tfrac{1}{2}\pi$. We conclude that

$$
I(t)=-\arctan(t)+\frac{1}{2}\pi
$$

and finally that

$$
\int_0^{\infty}\frac{\sin(x)}{x}\,dx=I(0)=\tfrac{1}{2}\pi.
$$

::::::

In {prf:ref}`Ex:Integration:SubstitutionTrigSerretsIntegral` and {prf:ref}`Ex:Integration:IntegrationByPartsSerretsIntegral` we already evaluated Serret's integral $\displaystyle\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx$ using substitution and integration by parts, respectively. The Feynman method also leads to the same result.

::::::{admonition} A different approach to Serret's integral (bonus material)
:class: bonus, dropdown
:name: Bonus:Integration:SerretsIntegralFeynmanMethod

The results in Equation {eq}`Eq:Integration:PartsSerret` can also be obtained using the Feynman method.

Note that Serret's integral is a special case of $I(\alpha)=\displaystyle\int_0^{\alpha}\frac{\ln(1+\alpha x)}{1+x^2}\,dx$.

Differentiation with respect to $\alpha$ leads to 

$$
I'(\alpha)=\displaystyle\frac{\ln(1+\alpha^2)}{1+\alpha^2}+\int_0^{\alpha}\frac{x}{(1+x^2)(1+\alpha x)}\,dx.
$$ 

Now we use (see the section on integration of rational functions for more details) 
 
$$
\frac{x}{(1+x^2)(1+\alpha x)}=\frac{1}{1+\alpha^2}\left(\frac{\alpha+x}{1+x^2}-\frac{\alpha}{1+\alpha x}\right)
$$

to obtain

\begin{align*}
&\int_0^{\alpha}\frac{x}{(1+x^2)(1+\alpha x)}\,dx\\
&=\frac{1}{1+\alpha^2}\int_0^{\alpha}\left(\frac{\alpha+x}{1+x^2}-\frac{\alpha}{1+\alpha x}\right)\,dx\\
&=\frac{1}{1+\alpha^2}\bigg[\alpha\arctan(x)+\frac{1}{2}\ln(1+x)-\ln(1+\alpha x)\bigg]_0^{\alpha}\\
&=\frac{1}{1+\alpha^2}\left(\alpha\arctan(\alpha)+\frac{1}{2}\ln(1+\alpha^2)-\ln(1+\alpha^2)\right)\\
&=\frac{\alpha}{1+\alpha^2}\arctan(\alpha)-\frac{\ln(1+\alpha^2)}{2(1+\alpha^2)}.
\end{align*}
Hence we have: $I'(\alpha)=\displaystyle\frac{\alpha}{1+\alpha^2}\arctan(\alpha)+\frac{\ln(1+\alpha^2)}{2(1+\alpha^2)}$. Since $I(0)=0$, this implies that

\begin{align*}
I(\alpha)&=\int\frac{\alpha}{1+\alpha^2}\arctan(\alpha)\,d\alpha+\int\frac{\ln(1+\alpha^2)}{2(1+\alpha^2)}\,d\alpha\\
&=\frac{1}{2}\int\arctan(\alpha)\,d\ln(1+\alpha^2)+\int\frac{\ln(1+\alpha^2)}{2(1+\alpha^2)}\,d\alpha\\
&=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2)-\frac{1}{2}\int\ln(1+\alpha^2)\,d\arctan(\alpha)\\
&{}\quad\quad\quad{}+\frac{1}{2}\int\frac{\ln(1+\alpha^2)}{1+\alpha^2}\,d\alpha\\
&=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2)-\frac{1}{2}\int\frac{\ln(1+\alpha^2)}{1+\alpha^2}\,d\alpha\\
&{}\quad\quad\quad{}+\frac{1}{2}\int\frac{\ln(1+\alpha^2)}{1+\alpha^2}\,d\alpha\\
&=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2)+C\quad\Longrightarrow\quad I(\alpha)=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2).
\end{align*}
Hence we have: $\displaystyle\int_0^{\alpha}\frac{\ln(1+\alpha x)}{1+x^2}\,dx=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2)$.

The special case $\alpha=1$ now reads

$$
\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx=\frac{1}{2}\arctan(1)\ln(2)=\frac{1}{2}\cdot\frac{1}{4}\pi\cdot\ln(2)=\frac{1}{8}\pi\ln(2).
$$

Similarly, the integral $\displaystyle\int_0^1\frac{\arctan(x)}{1+x}\,dx$ is a special case of

\begin{align*}
\alpha\int_0^{\alpha}\frac{\arctan(x)}{1+\alpha x}\,dx&=\int_0^{\alpha}\arctan(x)\,d\ln(1+\alpha x)\\
&=\arctan(x)\ln(1+\alpha x)\bigg|_0^{\alpha}-\int_0^{\alpha}\ln(1+\alpha x)\,d\arctan(x)\\
&=\arctan(\alpha)\ln(1+\alpha^2)-\int_0^{\alpha}\frac{\ln(1+\alpha x)}{1+x^2}\,dx.
\end{align*}
This implies that: 

$$
\alpha\int_0^{\alpha}\frac{\arctan(x)}{1+\alpha x}\,dx=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2)=\int_0^{\alpha}\frac{\ln(1+\alpha x)}{1+x^2}\,dx.
$$

For $\alpha=1$ this gives Equation {eq}`Eq:Integration:PartsSerret`.

::::::


## Exercises

::::{exercise}
:label: Exc:Integration:ImproperIntegralsExercise1
Determine whether $\displaystyle\int\frac{dx}{x^2}$ is convergent or divergent. 
::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsExercise1`
:class: solution, dropdown
:name: Solution:Integration:ImproperIntegralsExercise1

$$
\int_1^{\infty}\frac{dx}{x^2}=\lim_{R\to\infty}\int_1^R\frac{dx}{x^2}=\lim_{R\to\infty}\bigg[-\frac{1}{x}\bigg]_1^R=\lim_{R\to\infty}\left(1-\frac{1}{R}\right)=1.
$$

So, $\displaystyle\int_1^{\infty}\frac{dx}{x^2}$ is convergent.
:::

::::{exercise}
:label: Exc:Integration:ImproperIntegralsExercise2
Determine whether $\displaystyle\int\frac{dx}{x}$ is convergent or divergent. 
::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsExercise2`
:class: solution, dropdown
:name: Solution:Integration:ImproperIntegralsExercise2

$$
\int_1^{\infty}\frac{dx}{x}=\lim_{R\to\infty}\int_1^R\frac{dx}{x}=\lim_{R\to\infty}\bigg[\ln(x)\bigg]_1^R=\lim_{R\to\infty}\ln(R)=\infty.
$$

So, $\displaystyle\int_1^{\infty}\frac{dx}{x}$ is divergent.
:::


::::{exercise}
:label: Exc:Integration:ImproperIntegralsExercise3
The integral $\displaystyle\int_0^{\infty}\frac{dx}{(1+x)\sqrt{x}}$ is improper both because of the infinite interval of integration and the discontinuous integrand at $x=0$. Evaluate the integral by splitting it into

$$
\int_0^{\infty}\frac{dx}{(1+x)\sqrt{x}}=\int_0^1\frac{dx}{(1+x)\sqrt{x}}+\int_1^{\infty}\frac{dx}{(1+x)\sqrt{x}}.
$$

::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsExercise3`
:class: solution, dropdown
:name: Solution:Integration:ImproperIntegralsExercise3

Using the substitution $\sqrt{x}=t$ or $x=t^2$, we have $dx=2t\,dt$ and therefore

\begin{align*}
\int\frac{dx}{(1+x)\sqrt{x}}&=\int\frac{2t\,dt}{(1+t^2)t}=\int\frac{2}{1+t^2}\,dt=2\arctan(t)+C\\
&=2\arctan\left(\sqrt{x}\right)+C.
\end{align*}
Now we obtain

\begin{align*}
\int_0^1\frac{dx}{(1+x)\sqrt{x}}&=\lim_{c\downarrow0}\int_c^1\frac{dx}{(1+x)\sqrt{x}}=\lim_{c\downarrow0}\bigg[2\arctan\left(\sqrt{x}\right)\bigg]_c^1\\
&=2\arctan(1)=\frac{1}{2}\pi
\end{align*}
and

\begin{align*}
\int_1^{\infty}\frac{dx}{(1+x)\sqrt{x}}&=\lim_{R\to\infty}\int_1^R\frac{dx}{(1+x)\sqrt{x}}=\lim_{R\to\infty}\bigg[2\arctan\left(\sqrt{x}\right)\bigg]_1^R\\
&=\pi-\frac{1}{2}\pi=\frac{1}{2}\pi.
\end{align*}
Hence we have

$$
\int_0^{\infty}\frac{dx}{(1+x)\sqrt{x}}=\int_0^1\frac{dx}{(1+x)\sqrt{x}}+\int_1^{\infty}\frac{dx}{(1+x)\sqrt{x}}=\frac{1}{2}\pi+\frac{1}{2}\pi=\pi.
$$

:::

::::{exercise}
:label: Exc:Integration:ImproperIntegralsExercise4
Show that $\displaystyle\int_0^{\infty}\frac{\ln(x)}{1+x^2}\,dx=0$ by splitting it into

$$
\int_0^{\infty}\frac{\ln(x)}{1+x^2}\,dx=\int_0^1\frac{\ln(x)}{1+x^2}\,dx+\int_1^{\infty}\frac{\ln(x)}{1+x^2}\,dx.
$$

::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsExercise4`
:class: solution, dropdown
:name: Solution:Integration:ImproperIntegralsExercise4

Use the substitution $x=\dfrac{1}{t}$ and therefore $dx=-\dfrac{dt}{t^2}$ to find that

$$
\int_1^{\infty}\frac{\ln(x)}{1+x^2}\,dx=-\int_1^0\frac{\ln\left(\frac{1}{t}\right)}{1+\dfrac{1}{t^2}}\cdot\frac{dt}{t^2}=\int_0^1\frac{-\ln(t)}{t^2+1}\,dt=-\int_0^1\frac{\ln(t)}{1+t^2}\,dt.
$$

We conclude that $\displaystyle\int_0^{\infty}\frac{\ln(x)}{1+x^2}\,dx=0$.
:::

::::::{note}
:name: Note:Integration:CatalansConstant

Here we showed that $\displaystyle-\int_0^1\frac{\ln(x)}{1+x^2}\,dx=\int_1^{\infty}\frac{\ln(x)}{1+x^2}\,dx$ without evaluating the integrals. Later we will see that the value is equal to *Catalan's constant*.
::::::

::::{exercise} A remarkable class of integrals
:label: Exc:Integration:ImproperIntegralsExercise5
Show that $\displaystyle\int_0^{\infty}\frac{dx}{(1+x^2)(1+x^k)}=\frac{1}{4}\pi$ for all $k\in\mathbb{Z}=\{\ldots,-2,-1,0,1,2,\ldots\}$ using the following steps:

(a) Prove the formula for $k=0$.

(b) Split the integral into

$$
\int_0^{\infty}\frac{dx}{(1+x^2)(1+x^k)}=\int_0^1\frac{dx}{(1+x^2)(1+x^k)}+\int_1^{\infty}\frac{dx}{(1+x^2)(1+x^k)}
$$

and use the substitution $x=\dfrac{1}{t}$ to prove the formula for $k\in\{1,2,3,\ldots\}$.

(c) Replace $k$ by $-k$ and use the substitution $x=\dfrac{1}{t}$ again to prove the formula for $k\in\{\ldots,-3,-2,-1\}$ as well.
::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsExercise5`
:class: solution, dropdown
:name: Solution:Integration:ImproperIntegralsExercise5

(a) For $k=0$ we obtain: $\displaystyle\int_0^{\infty}\frac{dx}{(1+x^2)(1+x^0)}=\frac{1}{2}\int_0^{\infty}\frac{dx}{1+x^2}=\frac{1}{2}\arctan(x)\bigg|_0^{\infty}=\frac{1}{4}\pi$.

(b) For $k\in\{1,2,3,\ldots\}$ we use the substitution $x=\dfrac{1}{t}$ and therefore $dx=-\dfrac{dt}{t^2}$ to find that

\begin{align*}
\int_1^{\infty}\frac{dx}{(1+x^2)(1+x^k)}&=\int_1^0\frac{1}{(1+t^{-2})(1+t^{-k})}\left(-\frac{1}{t^2}\right)\,dt\\
&=\int_0^1\frac{dt}{(t^2+1)(1+t^{-k})}.
\end{align*}
This implies that

\begin{align*}
\int_0^{\infty}\frac{dx}{(1+x^2)(1+x^k)}&=\int_0^1\frac{dx}{(1+x^2)(1+x^k)}+\int_0^1\frac{dx}{(1+x^2)(1+x^{-k})}\\
&=\int_0^1\frac{1}{1+x^2}\left(\frac{1}{1+x^k}+\frac{1}{1+x^{-k}}\right)\,dx\\
&=\int_0^1\frac{1}{1+x^2}\left(\frac{1}{1+x^k}+\frac{x^k}{x^k+1}\right)\,dx\\
&=\int_0^1\frac{1}{1+x^2}\cdot\frac{1+x^k}{1+x^k}\,dx=\int_0^1\frac{dx}{1+x^2}\\
&=\arctan(x)\bigg|_0^1=\frac{1}{4}\pi.
\end{align*}
(c) Similarly, we consider

$$
\int_0^{\infty}\frac{dx}{(1+x^2)(1+x^{-k})}=\int_0^1\frac{dx}{(1+x^2)(1+x^{-k})}+\int_1^{\infty}\frac{dx}{(1+x^2)(1+x^{-k})}
$$

for $k\in\{1,2,3,\dots\}$ and use the substitution $x=\dfrac{1}{t}$ again to find that

\begin{align*}
\int_1^{\infty}\frac{dx}{(1+x^2)(1+x^{-k})}&=\int_1^0\frac{1}{(1+t^{-2})(1+t^k)}\left(-\frac{1}{t^2}\right)\,dt\\
&=\int_0^1\frac{dt}{(t^2+1)(1+t^k)}.
\end{align*}
Hence, for $k\in\{1,2,3,\ldots\}$ we have

\begin{align*}
\int_0^{\infty}\frac{dx}{(1+x^2)(1+x^{-k})}&=\int_0^1\frac{dx}{(1+x^2)(1+x^{-k})}+\int_0^1\frac{dx}{(1+x^2)(1+x^k)}\\
&=\int_0^1\frac{1}{1+x^2}\left(\frac{1}{1+x^{-k}}+\frac{1}{1+x^k}\right)\,dx\\
&=\int_0^1\frac{1}{1+x^2}\left(\frac{x^k}{x^k+1}+\frac{1}{1+x^k}\right)\,dx\\
&=\int_0^1\frac{1}{1+x^2}\cdot\frac{x^k+1}{x^k+1}\,dx=\int_0^1\frac{dx}{1+x^2}\\
&=\arctan(x)\bigg|_0^1=\frac{1}{4}\pi.
\end{align*}
:::

::::{exercise}
:label: Exc:Integration:ImproperIntegralsComparisonExercise1
Evaluate $\displaystyle\int_0^{\infty}\frac{x}{1+x^3}\,dx$ exactly. 
::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsComparisonExercise1`
:class: solution, dropdown
:name: Solution:Integration:ImproperIntegralsComparisonExercise1

Note that $1+x^3=(1+x)(1-x+x^2)$ and therefore

\begin{align*}
\frac{x}{1+x^3}&=\frac{x}{(1+x)(1-x+x^2)}=\frac{A}{1+x}+\frac{Bx+C}{1-x+x^2}\\
&=\frac{A(1-x+x^2)+Bx(1+x)+C(1+x)}{(1+x)(1-x+x^2)}.
\end{align*}
Comparing the numerators, we obtain

\begin{align*}
&x=(A+B)x^2+(-A+B+C)x+A+C\\
&\quad\Longrightarrow\quad A=-\frac{1}{3}\quad\text{and}\quad B=C=\frac{1}{3}.
\end{align*}
Hence, we have

\begin{align*}
\int\frac{x}{1+x^3}\,dx&=\frac{1}{3}\int\left(-\frac{1}{1+x}+\frac{x+1}{x^2-x+1}\right)\,dx\\
&=\frac{1}{3}\int\left(-\frac{1}{1+x}+\frac{1}{2}\frac{2x-1}{x^2-x+1}+\frac{3}{2}\frac{1}{x^2-x+1}\right)\,dx.
\end{align*}
Now we have

$$
\int\left(-\frac{1}{1+x}+\frac{1}{2}\frac{2x-1}{x^2-x+1}\right)\,dx=\ln\left(\frac{\sqrt{x^2-x+1}}{1+x}\right)+C
$$

and

\begin{align*}
\int\frac{dx}{x^2-x+1}&=\int\frac{dx}{(x-\frac{1}{2})^2+\frac{3}{4}}=\frac{4}{3}\int\frac{dx}{\left(\frac{2x-1}{\sqrt{3}}\right)^2+1}\\
&=\frac{2}{\sqrt{3}}\arctan\left(\frac{2x-1}{\sqrt{3}}\right)+C
\end{align*}
Since $\displaystyle\lim\limits_{x\to\infty}\frac{\sqrt{x^2-x+1}}{1+x}=1$, we obtain using $\displaystyle\lim_{x\to\infty}\arctan(x)=\tfrac{1}{2}\pi$ and $\arctan\left(\frac{1}{\sqrt{3}}\right)=\frac{1}{6}\pi$

\begin{align*}
\int_0^{\infty}\frac{x}{1+x^3}\,dx&=\bigg[\frac{1}{3}\ln\left(\frac{\sqrt{x^2-x+1}}{1+x}\right)+\frac{1}{\sqrt{3}}\arctan\left(\frac{2x-1}{\sqrt{3}}\right)\bigg]_0^{\infty}\\
&=\frac{1}{\sqrt{3}}\left(\frac{1}{2}\pi+\frac{1}{6}\pi\right)=\frac{2}{3}\pi\sqrt{3}\approx1.2092.
\end{align*}
:::

::::{exercise}
:label: Exc:Integration:ImproperIntegralsComparisonExercise2
Determine whether the integral $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{\sqrt{x}}\,dx$ is convergent or divergent.
::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsComparisonExercise2`
:class: solution, dropdown
:name: Solution:Integration:ImproperIntegralsComparisonExercise2

Note that for all $x\geq1$ we have $\frac{1}{4}\pi\leq\arctan(x)<\frac{1}{2}\pi$. Hence we have
$\displaystyle\frac{\arctan(x)}{\sqrt{x}}\geq\frac{1}{4}\pi\cdot\frac{1}{\sqrt{x}}$ and
$$
\int_1^{\infty}\frac{dx}{\sqrt{x}}=2\sqrt{x}\bigg|_1^{\infty}=\infty.
$$

We conclude that $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{\sqrt{x}}\,dx$ is divergent.
:::

::::{exercise}
:label: Exc:Integration:ImproperIntegralsComparisonExercise3
Determine whether the integral $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{x\sqrt{x}}\,dx$ is convergent or divergent.
::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsComparisonExercise3`
:class: solution, dropdown
:name: Solution:Integration:ImproperIntegralsComparisonExercise3

Note that for all $x\geq1$ we have $\frac{1}{4}\pi\leq\arctan(x)<\frac{1}{2}\pi$. Further we have

$$
\int_1^{\infty}\frac{dx}{x\sqrt{x}}=-\frac{2}{\sqrt{x}}\bigg|_1^{\infty}=2.
$$

We conclude that $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{x\sqrt{x}}\,dx$ is convergent and that

$$
\frac{1}{2}\pi\leq\int_1^{\infty}\frac{\arctan(x)}{x\sqrt{x}}<\pi.
$$

:::


## Grasple exercises

