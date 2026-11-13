(Sec:Integration:ImproperIntegrals)=

# Improper integrals

## Introduction

In {numref}`Sec:Integration:DefiniteIntegrals` we defined a definite integral $\displaystyle\int_a^bf(x)\,dx$, where the integrand $f$ is a *piecewise-continuous and bounded function* on a *closed* and *finite* interval $[a,b]$.

In this section we will extend the concept of definite integrals to more general functions and intervals.

## Proper and improper

First of all we need the following definition to distinguish between the integrals we have defined so far and the more general integrals we will define in this section:

::::{prf:definition}
:label: Def:Integration:ProperIntegrals

A **proper integral** is a definite integral $\displaystyle\int_a^bf(x)\,dx$ where $f$ is a *continuous function* on the *finite interval* $[a,b]$.

Any other definite integral $\displaystyle\int_a^bf(x)\,dx$ is called an **improper integral**.
::::

Note that $[a,b]$ is always considered closed for all definite integrals from now on, so we will not explicitly mention that anymore.

This means that an integral is improper if

- the interval of integration is _not finite_,

and/or

- the integrand is _not continuous_.

In the next subsections we will first consider the two cases separately and then the combination of these cases.

:::{prf:remark}
:label: Rem:Integration:NotContinuous
Note that we use the term _not continuous_ and similar terms, as this is more general than the term _discontinuous_, as the latter implies that the point where continuity fails is part of the domain, where the former does not.
:::

## Not-finite interval of integration

Let us first consider the case where the interval of integration is *not finite*. This means that the interval of integration is infinite, i.e., it is of the form $[a,\infty)$, $(-\infty,b]$ or $(-\infty,\infty)$. Note that these intervals are all closed.

Improper integrals over such intervals are defined as a (sum of) limit(s) which may or may not exist. We will give a definition for each of the three types of infinite intervals of integration.

::::::{prf:Definition} Improper integral with right-infinite interval of integration
:label: Def:Integration:ImproperIntegralInfiniteIntervalRight

If $f$ is continuous on the interval $[a,\infty)$, then

$$
\int_a^{\infty}f(x)\,dx=\lim_{R\to\infty}\int_a^Rf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the improper integral $\displaystyle\int_a^{\infty}f(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_a^{\infty}f(x)\,dx$ is **divergent**. If the limit does not exist and equals $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_a^{\infty}f(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::

::::::{prf:Definition} Improper integral with left-infinite interval of integration
:label: Def:Integration:ImproperIntegralInfiniteIntervalLeft

If $f$ is continuous on the interval $(-\infty,b]$, then

$$
\int_{-\infty}^bf(x)\,dx=\lim_{R\to-\infty}\int_R^bf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the improper integral $\displaystyle\int_{-\infty}^bf(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_{-\infty}^bf(x)\,dx$ is **divergent**. If the limit does not exist and equals $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_{-\infty}^bf(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::

::::::{prf:Definition} Improper integral with double-infinite interval of integration
:label: Def:Integration:ImproperIntegralInfiniteIntervalDouble

If $f$ is continuous on the interval $(-\infty,\infty)$, then

$$
\int_{-\infty}^{\infty}f(x)\,dx=\int_{-\infty}^cf(x)\,dx+\int_c^{\infty}f(x)\,dx
$$
provided the two improper integrals on the right converge for some value of $c\in\mathbb{R}$.

If the two improper integrals on the right converge, we say that the improper integral $\displaystyle\int_{-\infty}^{\infty}f(x)\,dx$ is **convergent**.

If at least one of the two improper integrals on the right does not converge, we say that the improper integral $\displaystyle\int_{-\infty}^{\infty}f(x)\,dx$ is **divergent**.

If one of the improper integrals on the right converges and the other one diverges to infinity, or both improper integrals on the right diverge to infinity, we say that the improper integral $\displaystyle\int_{-\infty}^{\infty}f(x)\,dx$ **diverges to infinity**. 

If one of the improper integrals on the right converges and the other one diverges to negative infinity, or both improper integrals on the right diverge to negative infinity, we say that the improper integral $\displaystyle\int_{-\infty}^{\infty}f(x)\,dx$ **diverges to negative infinity**.

::::::

So how do we evaluate an improper integral? We will see that in some cases we can evaluate the limit(s) and therefore the improper integral. In other cases we cannot evaluate the limit(s) but we can still determine whether the improper integral is convergent or divergent. In yet other cases we cannot even determine whether the improper integral is convergent or divergent.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample1

Consider the function $\displaystyle\frac{1}{x\sqrt{x}}$ on the interval $[1,\infty)$:

:::{applet}
:url: calculus/improper_integrals/improper_integral_with_right-infinite_interval_of_integration
:name: Fig:Integration:ImproperIntegral1
:class: dark-light

The function $\displaystyle\frac{1}{x\sqrt{x}}$ on the interval $[1,\infty)$.
:::

This function $\displaystyle\frac{1}{x\sqrt{x}}$ is continuous on $[1,\infty)$ and therefore we can define the improper integral $\displaystyle\int_1^{\infty}\frac{dx}{x\sqrt{x}}$ as in {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalRight`. We have

$$
\begin{align*}
\int_1^{\infty}\frac{dx}{x\sqrt{x}} &= \lim_{R\to\infty}\int_1^R\frac{dx}{x\sqrt{x}} \\
&= \lim_{R\to\infty}\bigg[-\frac{2}{\sqrt{x}}\bigg]_1^R \\
&= \lim_{R\to\infty}\left(2-\frac{2}{\sqrt{R}}\right) \\
&= 2.
\end{align*}
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample2
Now consider the function $\displaystyle\frac{1}{\sqrt{x}}$ on the same interval $[1,\infty)$:

:::{applet}
:url: calculus/improper_integrals/improper_integral_with_right-infinite_interval_of_integration_2
:name: Fig:Integration:ImproperIntegral2
:class: dark-light

The function $\displaystyle\frac{1}{\sqrt{x}}$ on the interval $[1,\infty)$.
:::

In this case we have another function that is continuous on $[1,\infty)$ and therefore we can define the improper integral $\displaystyle\int_1^{\infty}\frac{dx}{\sqrt{x}}$ as in {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalRight`. We have 

$$
\begin{align*}
\int_1^{\infty}\frac{dx}{\sqrt{x}} &= \lim_{R\to\infty}\int_1^R\frac{dx}{\sqrt{x}} \\
&= \lim_{R\to\infty}\bigg[2\sqrt{x}\bigg]_1^R \\
&= \lim_{R\to\infty}\left(2\sqrt{R}-2\right) \\
\end{align*}
$$

This last limit does not exist, and equals $\infty$. In this case we say that the improper integral diverges to infinity.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample3

Now we consider the function $\dfrac{1}{1+x^2}$ that is continuous on $(-\infty,\infty)$ and therefore we can define the improper integral $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$ as in {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalDouble`.

:::{applet}
:url: calculus/improper_integrals/improper_integral_with_double-infinite_interval_of_integration
:name: Fig:Integration:ImproperIntegral3
:class: dark-light

The function $\displaystyle\frac{1}{1+x^2}$ on the interval $(-\infty,\infty)$.
:::

We start by splitting the integral into two integrals as in {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalDouble`:

$$
\int_{-\infty}^{\infty}\frac{dx}{1+x^2}=\int_{-\infty}^0\frac{dx}{1+x^2}+\int_0^{\infty}\frac{dx}{1+x^2}.
$$

In this case we choose the central point $c=0$ but we could have chosen any other value of $c\in\mathbb{R}$ as well. The value of the integral does not depend on the choice of $c$. 

Now we have for the first integral

$$
\begin{align*}
\int_{-\infty}^0\frac{dx}{1+x^2} &= \lim_{R\to-\infty}\int_R^0\frac{dx}{1+x^2} \\
&= \lim_{R\to-\infty}\bigg[\arctan(x)\bigg]_R^0\\
&= \lim_{R\to-\infty}\left(-\arctan(R)\right) \\
&=\frac{1}{2}\pi
\end{align*}
$$

and for the second integral

$$
\begin{align*}
\int_0^{\infty}\frac{dx}{1+x^2}&=\lim_{R\to\infty}\int_0^R\frac{dx}{1+x^2}\\
&=\lim_{R\to\infty}\bigg[\arctan(x)\bigg]_0^R\\
&=\lim_{R\to\infty}\arctan(R)\\
&=\frac{1}{2}\pi.
\end{align*}
$$

Hence, we have

$$
\int_{-\infty}^{\infty}\frac{dx}{1+x^2} = \int_{-\infty}^0\frac{dx}{1+x^2}+\int_0^{\infty}\frac{dx}{1+x^2} = \frac{1}{2}\pi+\frac{1}{2}\pi = \pi.
$$

::::::

::::::{note}
:name: Note:Integration:ImproperIntegralsInfiniteIntervalExample3

:::{applet}
:url: calculus/improper_integrals/standard_Cauchy_distribution
:name: Fig:Integration:CauchyDistribution
:class: dark-light

The probability density function of the standard Cauchy distribution.
:::

In probability and statistics the function $\displaystyle\frac{1}{\pi}\cdot\frac{1}{1+x^2}$ is the probability density function of the standard Cauchy distribution, which is named after the French mathematician [Augustin-Louis Cauchy (1789-1857)](https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy).

In {prf:ref}`Ex:Integration:ImproperIntegralsInfiniteIntervalExample3` it is shown that the integral $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$ is convergent and equal to $\pi$. Hence, the total area under the curve of the probability density function of the standard Cauchy distribution is equal to $1$, which is an essential property of a probability density function.

::::::

One should be careful with bounded and odd functions on $\mathbb{R}$ as the following examples show.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample4

Consider

$$
\int_{-\infty}^{\infty}\frac{x}{1+x^2}\,dx=\int_{-\infty}^0\frac{x}{1+x^2}\,dx+\int_0^{\infty}\frac{x}{1+x^2}\,dx.
$$

Then we have

$$
\begin{align*}
\int_0^{\infty}\frac{x}{1+x^2}\,dx&=\lim_{R\to\infty}\int_0^R\frac{x}{1+x^2}\,dx\\
&=\lim_{R\to\infty}\left[\frac{1}{2}\ln(1+x^2)\right]_0^R\\
&=\lim_{R\to\infty}\frac{1}{2}\ln(1+R^2)\\
&=\infty.
\end{align*}
$$

This implies that the integral *diverges*. Nevertheless, we also have

$$
\begin{align*}
\int_{-\infty}^0\frac{x}{1+x^2}\,dx&=\lim_{R\to-\infty}\int_R^0\frac{x}{1+x^2}\,dx\\
&=\lim_{R\to-\infty}\left[\frac{1}{2}\ln(1+x^2)\right]_R^0\\
&=\lim_{R\to-\infty}\left(-\frac{1}{2}\ln(1+R^2)\right)\\
&=-\infty.
\end{align*}
$$

We *cannot* conclude that 

$$
\int_{-\infty}^{\infty}\frac{x}{1+x^2}\,dx=\int_{-\infty}^0\frac{x}{1+x^2}\,dx+\int_0^{\infty}\frac{x}{1+x^2}\,dx=-\infty+\infty=0
$$

since $\infty$ is not a real number.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample5

Consider

$$
\int_{-\infty}^{\infty}\frac{x}{1+x^4}\,dx=\int_{-\infty}^0\frac{x}{1+x^4}\,dx+\int_0^{\infty}\frac{x}{1+x^4}\,dx.
$$

Then we have

$$
\begin{align*}
\int_0^{\infty}\frac{x}{1+x^4}\,dx&=\lim_{R\to\infty}\int_0^R\frac{x}{1+x^4}\,dx\\
&=\lim_{R\to\infty}\left[\frac{1}{2}\arctan(x^2)\right]_0^R\\
&=\lim_{R\to\infty}\frac{1}{2}\arctan(R^2)\\
&=\frac{1}{2}\cdot\frac{1}{2}\pi\\
&=\frac{1}{4}\pi
\end{align*}
$$

and

$$
\begin{align*}
\int_{-\infty}^0\frac{x}{1+x^4}\,dx&=\lim_{R\to-\infty}\int_R^0\frac{x}{1+x^4}\,dx\\
&=\lim_{R\to-\infty}\left[\frac{1}{2}\arctan(x^2)\right]_R^0\\
&=\lim_{R\to-\infty}\left(-\frac{1}{2}\arctan(R^2)\right)\\
&=-\frac{1}{2}\cdot\frac{1}{2}\pi\\
&=-\frac{1}{4}\pi.
\end{align*}
$$

Hence, we have

$$
\int_{-\infty}^{\infty}\frac{x}{1+x^4}\,dx=\int_{-\infty}^0\frac{x}{1+x^4}\,dx+\int_0^{\infty}\frac{x}{1+x^4}\,dx=-\frac{1}{4}\pi+\frac{1}{4}\pi=0.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample6

We can also attempt to integrate trigonometric functions over infinite intervals, for example the cosine function over the interval $[0,\infty)$:

:::{applet}
:url: calculus/improper_integrals/improper_integral_with_right-infinite_interval_of_integration_3
:name: Fig:Integration:ImproperIntegral4
:class: dark-light

The function $\displaystyle\cos(x)$ on the interval $[0,\infty)$.
:::


$$
\begin{align*}
\int_0^{\infty}\cos(x)\,dx &= \lim_{R\to\infty}\int_0^R\cos(x)\,dx \\
&= \lim_{R\to\infty}\bigg[\sin(x)\bigg]_0^R \\
&=\lim_{R\to\infty}\sin(R).
\end{align*}
$$

This limit does not exist and is neither $\infty$ nor $-\infty$. In this case we can only say that the integral diverges.

::::::

::::::{note}
:name: Note:Integration:ImproperIntegralsNotation

We will often use the short notation $\displaystyle\int_1^{\infty}\frac{dx}{x^2}=\bigg[-\frac{1}{x}\bigg]_1^{\infty}=1$. This means

$$
\int_1^{\infty}\frac{dx}{x^2}=\lim_{R\to\infty}\bigg[-\frac{1}{x}\bigg]_1^R=\lim_{R\to\infty}\left(1-\frac{1}{R}\right)=1.
$$

::::::

## Not-continuous integrands

Having discussed the intervals of integration, we now turn our attention to the integrand. For this subsection we assume that the interval of integration is closed and finite, i.e., of the form $[a,b]$.

{numref}`Section:Continuity` discusses what we consider to be continuity with respect to a function. As continuity is a local property, we will discuss three possible cases of where the continuity of the integrand $f$ fails on the interval $[a,b]$:

- the integrand $f$ is not right-continuous at $x=a$ (i.e. at the left of the interval).
- the integrand $f$ is not left-continuous at $x=b$ (i.e. at the right of the interval).
- the integrand $f$ is not continuous at some point $c\in(a,b)$ (i.e. in the interior of the interval).

In particular, we do not require the integrand to be unbounded near the point of failing continuity, but it may be unbounded as well.

The way we define improper integrals with an integrand that is not continuous is more general than the way it is often defined in other textbooks, where the integrand is required to be unbounded near the point of where continuity fails.

For each of the three cases we will define how to handle the improper integral $\displaystyle\int_a^bf(x)\,dx$.

::::::{prf:Definition} Improper integral with not-continuous integrand at left endpoint
:label: Def:Integration:ImproperIntegralLeftNotContinuousIntegrand

If $f$ is continuous on the interval $(a,b]$, then

$$
\int_a^bf(x)\,dx=\lim_{t\to a^+}\int_t^bf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ is **divergent**. If the limit does not exist and equals $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::

::::::{prf:Definition} Improper integral with not-continuous integrand at right endpoint
:label: Def:Integration:ImproperIntegralRightNotContinuousIntegrand

If $f$ is continuous on the interval $[a,b)$, then

$$
\int_a^bf(x)\,dx=\lim_{t\to b^-}\int_a^tf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ is **divergent**. If the limit does not exist and equals $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::

::::::{prf:Definition} Improper integral with not-continuous integrand at internal point
:label: Def:Integration:ImproperIntegralInternalNotContinuousIntegrand

If $f$ is not continuous at some point $c\in(a,b)$, then

$$
\int_a^bf(x)\,dx=\int_a^cf(x)\,dx+\int_c^bf(x)\,dx
$$
provided the two improper integrals on the right converge.

If the two improper integrals on the right converge, we say that the improper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ is **convergent**.

If at least one of the two improper integrals on the right does not converge, we say that the improper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ is **divergent**.

If one of the improper integrals on the right converges and the other one diverges to infinity, or if both improper integrals on the right diverge to infinity, we say that the improper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ **diverges to infinity**. 

If one of the improper integrals on the right converges and the other one diverges to negative infinity, or if both improper integrals on the right diverge to negative infinity, we say that the improper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ **diverges to negative infinity**.

::::::

We start with an example of an improper integral with an integrand that is not continuous at an internal point of the interval of integration.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsNotContinuousIntegrandExample1

We integrate the function $\displaystyle\frac{1}{x^2}$ on the interval $[-1,1]$. 

:::{applet}
:url: calculus/improper_integrals/improper_integral_with_not-continuous_integrand_at_internal_point
:name: Fig:Integration:ImproperIntegral5
:class: dark-light

The function $\displaystyle\frac{1}{x^2}$ on the interval $[-1,1]$.
:::

This function is continuous on $[-1,0)$ and on $(0,1]$ but is not continuous at $x=0$. Hence, we can define the improper integral $\displaystyle\int_{-1}^1\frac{dx}{x^2}$ as in {prf:ref}`Def:Integration:ImproperIntegralInternalNotContinuousIntegrand`. We have

$$
\int_{-1}^1\frac{dx}{x^2}=\int_{-1}^0\frac{dx}{x^2}+\int_0^1\frac{dx}{x^2}.
$$

Now we have

$$
\begin{align*}
\int_{-1}^0\frac{dx}{x^2} &= \lim_{t\to 0^-}\int_{-1}^t\frac{dx}{x^2} \\
&= \lim_{t\to0^-}\bigg[-\frac{1}{x}\bigg]_{-1}^t \\
&= \lim_{t\to 0^-}\left(-\frac{1}{t}-1\right) \\
&= \infty.
\end{align*}
$$

At this point we can already conclude that the integral $\displaystyle\int_{-1}^1\frac{dx}{x^2}$ is divergent. Nevertheless, we evaluate the second integral to show that it also diverges to infinity:

$$
\begin{align*}
\int_0^1\frac{dx}{x^2} &= \lim_{t\to 0^+}\int_t^1\frac{dx}{x^2} \\
&= \lim_{t\to 0^+}\bigg[-\frac{1}{x}\bigg]_t^1 \\
&= \lim_{t\to 0^+}\left(-1+\frac{1}{t}\right) \\
&= \infty.
\end{align*}
$$

Because both integrals diverge to infinity, we say that the improper integral $\displaystyle\int_{-1}^1\frac{dx}{x^2}$ diverges to infinity, which we can write (informally) as

$$
\int_{-1}^1\frac{dx}{x^2}=\infty.
$$

::::::

::::::{warning}
:name: Warning:Integration:ImproperIntegralsNotContinuousIntegrandWarning1

The calculation

$$
\int_{-1}^1\frac{dx}{x^2}=-\frac{1}{x}\bigg|_{-1}^1=-1-1=-2
$$

is clearly wrong! Note that the integrand is positive on $[-1,1]$. The evaluation is incorrect because the integrand is not continuous at $x=0$. So, the fundamental theorem of calculus does not apply.
::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsNotContinuousIntegrandExample2

Consider the function $\dfrac{1}{x-1}$ on the interval $[0,3]$.

:::{applet}
:url: calculus/improper_integrals/improper_integral_with_not-continuous_integrand_at_internal_point_2
:name: Fig:Integration:ImproperIntegral6
:class: dark-light

The function $\displaystyle\frac{1}{x-1}$ on the interval $[0,3]$.
:::

Since $\dfrac{1}{x-1}$ is continuous for all $x\in\mathbb{R}$ except at $x=1$, we have

$$
\int_0^3\frac{dx}{x-1}=\int_0^1\frac{dx}{x-1}+\int_1^3\frac{dx}{x-1}
$$

with

$$
\begin{align*}
\int_0^1\frac{dx}{x-1} &= \lim_{c\to 1^-}\int_0^c\frac{dx}{x-1} \\
&= \lim_{c\to 1^-}\bigg[\ln|x-1|\bigg]_0^c \\
&= \lim_{c\to 1^-}\ln|c-1| \\
&= -\infty
\end{align*}
$$

and

$$
\begin{align*}
\int_1^3\frac{dx}{x-1} &= \lim_{c\to1^+}\int_c^3\frac{dx}{x-1} \\
&= \lim_{c\to 1^+}\bigg[\ln|x-1|\bigg]_c^3 \\
&= \lim_{c\to 1^+}\left(\ln(2)-\ln|c-1|\right) \\
&= \infty.
\end{align*}
$$

Because both integrals diverge, we say that the improper integral $\displaystyle\int_0^3\frac{dx}{x-1}$ diverges.

::::::

::::::{warning}
:name: Warning:Integration:ImproperIntegralsNotContinuousIntegrandWarning2

It would be wrong to conclude that

$$
\int_0^3\frac{dx}{x-1}=-\infty+\infty=0
$$

and it is also incorrect to state that

$$
\int_0^3\frac{dx}{x-1}=\ln|x-1|\bigg|_0^3=\ln(2)-\ln(1)=\ln(2).
$$

Since the integrand is not continuous at $x=1$ the fundamental theorem does not apply on $[0,3]$.
::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsNotContinuousIntegrandExample3

Consider $\displaystyle\int_0^1\ln(x)\,dx$. 

:::{applet}
:url: calculus/improper_integrals/improper_integral_with_not-continuous_integrand_at_left_endpoint
:name: Fig:Integration:ImproperIntegral7
:class: dark-light

The function $\displaystyle\ln(x)$ on the interval $[0,1]$.
:::

Using integration by parts, we have

$$
\begin{align*}
\int\ln(x)\,dx &= x\ln(x)-\int x\cdot\frac{1}{x}\,dx \\
&= x\ln(x)-x+C.
\end{align*}
$$

Hence, we have

$$
\begin{align*}
\int_0^1\ln(x)\,dx &= \lim_{t\to o^+}\bigg[x\ln(x)-x\bigg]_t^1 \\
&= \lim_{t\to 0^+}\left(-1-t\ln(t)+t\right).
\end{align*}
$$

Using l'Hospital's rule, we obtain

$$
\begin{align*}
\lim_{t\to 0^+}t\ln(t) &= \lim_{t\to 0^+}\frac{\ln(t)}{1/t} \\
&= \lim_{t\to 0^+}\frac{1/t}{-1/t^2} \\
&= \lim_{t\to 0^+}\left(-t\right) \\
&=0.
\end{align*}
$$

We conclude that

$$
\int_0^1\ln(x)\,dx=\lim_{t\to 0^+}\left(-1-t\ln(t)+t\right)=-1-0+0=-1.
$$

::::::


It may happen that a definite integral $\displaystyle\int_a^bf(x)\,dx$ is improper because $f$ is not continuous in more than one point in the interval $[a,b]$. If that happens, you can repeatedly apply {prf:ref}`Def:Integration:ImproperIntegralLeftNotContinuousIntegrand`, {prf:ref}`Def:Integration:ImproperIntegralRightNotContinuousIntegrand` and {prf:ref}`Def:Integration:ImproperIntegralInternalNotContinuousIntegrand`.

## Combinations of improperness

If the integrand $f$ is not continuous on the interval of integration and the interval of integration is infinite, we repeatedly apply the definitions {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalRight` until {prf:ref}`Def:Integration:ImproperIntegralInternalNotContinuousIntegrand` from the previous two subsections, which we showcase in the next example.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsNotContinuousIntegrandExample4

Consider $\displaystyle\int_0^{\infty}\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx$.

This integral is improper, because the integrand is not continuous in $0$ and because the interval of integration is infinite.

Using {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalRight` we write

$$
\int_0^{\infty}\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx = \lim_{R\rightarrow\infty}\int_0^{R}\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx.
$$

To evaluate the limit, we must first evaluate the new integral, which using {prf:ref}`Def:Integration:ImproperIntegralLeftNotContinuousIntegrand` becomes

$$
\int_0^{R}\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx = \lim_{t\rightarrow0^{+}}\int_t^{R}\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx.
$$

For $0<t<x<R$ we apply the substitution $x=u^2$ and therefore $dx=2u\,du$ to obtain

$$
\begin{align*}
\int_t^R\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx&=\int_{\sqrt{t}}^{\sqrt{R}}\frac{e^{-u}}{u}\cdot2u\,du\\
&=\int_{\sqrt{t}}^{\sqrt{R}}2e^{-u}\,dx\\
&=\Big[-2e^{-u}\Big]_{\sqrt{t}}^{\sqrt{R}}\\
&=2e^{-\sqrt{t}}-2e^{-\sqrt{R}}.
\end{align*}
$$

Hence, we have

$$
\begin{align*}
\int_0^{\infty}\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx&=\lim_{R\to\infty}\lim_{t\to 0^+}\int_t^R\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx\\
&=\lim_{R\to\infty}\lim_{t\to 0^+}\left(2e^{-\sqrt{t}}-2e^{-\sqrt{R}}\right)\\
&=\lim_{t\to 0^+}2e^{-\sqrt{t}}-\lim_{R\to\infty}2e^{-\sqrt{R}}\\
&=2-0\\
&=2.
\end{align*}
$$

Note that the order in which we apply {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalRight` and {prf:ref}`Def:Integration:ImproperIntegralLeftNotContinuousIntegrand` can be switched without changing the result. 

::::::

## Comparison test for improper integrals

Some improper integrals are difficult to evaluate explicitly. However, in many cases evaluation is not necessary as long as we can find out whether the integral is convergent or divergent. In case of convergence we might be able to find a lower and an upper bound for the integral. The following theorem might be helpful.

::::::{prf:Theorem} Comparison test for improper integrals
:label: Thm:Integration:ImproperIntegralsComparison
Assume $f$ and $g$ are continuous on $(a,b)$ with $-\infty\leq a<b\leq\infty$ and $0\leq f(x)\leq g(x)$. Then the following implications hold:

(a) If $\displaystyle\int_a^bg(x)\,dx$ is convergent, then $\displaystyle\int_a^bf(x)\,dx$ is convergent.

(b) If $\displaystyle\int_a^bf(x)\,dx$ is divergent, then $\displaystyle\int_a^bg(x)\,dx$ is divergent.

::::::

Note that this means that if the area below the graph of $g$ is finite, then so is the area below the graph of $f$ since $f\leq g$. On the other hand, if the area below the graph of $f$ is infinite, then so is the area below the graph of $g$ since $f\leq g$.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsComparisonExample1
Without evaluating the integral explicitly, we determine whether $\displaystyle\int_0^{\infty}\frac{x}{1+x^3}\,dx$ is convergent or divergent and give an interval containing its value.

Note that the inequality $\displaystyle\frac{x}{1+x^3}\leq\frac{x}{x^3}=\frac{1}{x^2}$ does not hold for $x=0$. Therefore, first we write 

$$
\int_0^{\infty}\frac{x}{1+x^3}\,dx=\int_0^1\frac{x}{1+x^3}\,dx+\int_1^{\infty}\frac{x}{1+x^3}\,dx.
$$

The first integral on the right is *proper* and thus exists. 

For $0\leq x\leq 1$ we have $0\leq\dfrac{x}{1+x^3}\leq x$, and therefore

$$
0 \leq \int_0^1\frac{x}{1+x^3}\,dx \leq \int_0^1x\,dx=\frac{1}{2}.
$$

For $x\geq1$ we have $0\leq\dfrac{x}{1+x^3}\leq\dfrac{x}{x^3}=\dfrac{1}{x^2}$, and since

$$
\int_1^{\infty}\frac{dx}{x^2}=\bigg[-\frac{1}{x}\bigg]_1^{\infty}=1,
$$

we obtain that the second integral is *convergent* and that 

$$
0 \leq \int_1^{\infty}\frac{x}{1+x^3}\,dx\le 1.
$$

We conclude that $\displaystyle\int_0^{\infty}\frac{x}{1+x^3}\,dx$ is convergent and that

$$
0 \leq \int_0^{\infty}\frac{x}{1+x^3}\,dx=\int_0^1\frac{x}{1+x^3}\,dx+\int_1^{\infty}\frac{x}{1+x^3}\,dx < \frac{1}{2}+1 = \frac{3}{2}.
$$

::::::

:::{note}
In {numref}`Grasple:133527` we will see that 

$$
\int_0^{\infty}\frac{x}{1+x^3}\,dx=\frac{2\pi}{3\sqrt{3}}\approx1.2092.
$$

:::

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


::::{question}
:type: short-answer
:variant: blocks
:columns: 1
:class: question
:admonition:
:showanswer:

In {prf:ref}`Ex:Integration:ImproperIntegralsComparisonExample2` we used the inequality $e^{-x^2}\leq e^{-x}$ for the comparison test for improper integrals, which also resulted in an approximation for the integral $\displaystyle\int_{0}^{\infty}e^{-x^2}\,dx$.

In order to find another approximation and not wanting to split the integral in two parts, we want to find a $c\in\mathbb{R}$ such that

- $e^{-x^2}\leq e^{-x+c}$ for all $x\geq0$;

- The resulting approximation of $\displaystyle\int_{0}^{\infty}e^{-x^2}\,dx$ using $\displaystyle\int_{0}^{\infty}e^{-x+c}\,dx$ is as good as possible.

Use {numref}`Fig:IntegrationImproperIntegralsComparisonQuestion` to find the optimal value of $c$, and then calculate $\displaystyle\int_{0}^{\infty}e^{-x+c}\,dx$.

---
M[\frac{1}{4}] The optimal value of $c$ is
= Using the graph, we find that for $c\geq\dfrac14$ we have $e^{-x^2}\leq e^{-x+c}$ for all $x\geq0$. If we increase the value of $c$ past $\dfrac14$, the area below $\displaystyle\int_{0}^{\infty}e^{-x+c}\,dx$ increases more and more, indicating that $c=\dfrac14$ is the optimal value of $c$.

Alternatively, we can do this algebraically. The optimal $c$ would be the value of $c$ for which the graph of $e^{-x^2}$ and $e^{-x+c}$ only intersect once, which can only occur if the equation

$$
-x^2 = -x +c
$$

has one solution. The discriminant $1-4c$ of the equivalent equation $x^2-x+c=0$ is zero when $c=\dfrac14$.

> The optimal $c$ would be the value of $c$ for which the graph of $e^{-x^2}$ and $e^{-x+c}$ only intersect once. Can you find this value?

M[e^{\frac{1}{4}}] With the optimal value for $c$, $\displaystyle\int_0^{\infty}e^{-x+c}\,dx=$
= $$
\int_0^{\infty}e^{-x+\frac{1}{4}}\,dx=\left[-e^{-x+\frac{1}{4}}\right]_0^{\infty}=e^{\frac{1}{4}}\approx1.28403.
$$

> Hint: The optimal value for $c$ is $\dfrac14$.
---

:::{applet}
:url: calculus/improper_integrals/comparing_improper_integrals
:name: Fig:IntegrationImproperIntegralsComparisonQuestion
:class: dark-light

The functions $e^{-x^2}$ and $e^{-x+c}$, with the value of $c$ changeable with the slider, on the interval $[0,\infty)$. 
:::

::::

::::{prf:example}
:label: Ex:Integration:ImproperIntegralsComparisonExample2Continued

Instead of using a function of the form $e^{-x+c}$ to use in the comparison with $e^{-x^2}$ to get an upper bound for $\displaystyle\int_{0}^{\infty}e^{-x^2}\,dx$, we can take it one step further and use a function of the form $e^{bx+c}$.

Similar to the question above, we want $b$ and $c$ such that the equation $-x^2=bx+c$ has one solution for $x$. This only occurs if the discriminant $b^2-4c$ of the equivalent equation $x^2+bx+c=0$ equals zero. Solving for $b$ gives the relation

$$
c = \frac14b^2,
$$

Using this relation to find an upper bound for $\displaystyle\int_{0}^{\infty}e^{-x^2}\,dx$ gives:

$$
\begin{align*}
\int_{0}^{\infty}e^{-x^2}\,dx &\leq \int_{0}^{\infty}e^{bx+c}\,dx \\
&= \bigg[\frac{1}{\sqrt{b}}e^{bx+\frac14b^2}\bigg]_{0}^{\infty}
&= \left\{\begin{array}{rcl}
-\frac{1}{b}e^{\frac14b^2} & \text{for} & b<0, \\
\infty & \text{for} & b\geq0, \\
\end{array}\right.
\end{align*}
$$

Note that if $b<0$, the approximation becomes positive, as we should expect.

Now we can determine the value of $b$ for which the upper bound is as small as possible. To this end, define

$$
I(b) = -\frac{1}{b}e^{\frac14b^2}.
$$

We differentiate with respect to $b$ and equate to zero to find the equation

$$
\frac{2 - b^2}{2b^2} e^{\frac14b^2}=0.
$$

The only viable solution of this equation is $b=-\sqrt{2}$, as $b$ should be negative, and gives the upper bound:

$$
\int_{0}^{\infty}e^{-x^2}\,dx \leq I(\sqrt{2}) = \frac{\sqrt{e}}{\sqrt{2}}.
$$

{numref}`Fig:IntegrationImproperIntegralsComparisonB` shows the both the original function and our new approximation.

:::{applet}
:url: calculus/improper_integrals/comparing_improper_integrals_2
:name: Fig:IntegrationImproperIntegralsComparisonB
:class: dark-light

The functions $e^{-x^2}$ and $e^{-bx+\frac14b^2}$, with the value of $b$ changeable with the slider, on the interval $[0,\infty)$. 
:::

::::

::::::{prf:remark}
:label: Note:Integration:ImproperIntegralsGaussianIntegral

Later (see: {prf:ref}`Ex:MultivariableIntegration:PolarApplicationsExample2`) we will see that $\displaystyle\int_0^{\infty}e^{-x^2}\,dx=\frac{1}{2}\sqrt{\pi}\approx0.88623$.

By symmetry, we also have: $\displaystyle\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt{\pi}$, which is called the **Gaussian integral**, named after the German mathematician [Johann Carl Friedrich Gauss (1777-1855)](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss).

:::{applet}
:url: calculus/improper_integrals/standard_normal_distribution
:name: Fig:Integration:NormalDistribution
:class: dark-light

The probability density function of the standard normal distribution.
:::

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

:::{applet}
:url: calculus/improper_integrals/comparing_improper_integrals_3
:name: Fig:Integration:ImproperIntegralsComparisonExample3
:class: dark-light

The graphs of $\dfrac{2+\cos(x)}{x}$ and $\dfrac{1}{x}$ on the interval $[1,\infty)$.
:::

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsComparisonExample4
Consider $\displaystyle\int_1^{\infty}\frac{1+e^{-x}}{\sqrt{x}}\,dx$.

Note that $1+e^{-x}>1$ and

$$
\int_1^{\infty}\frac{dx}{\sqrt{x}}=2\sqrt{x}\bigg|_1^{\infty}=\infty.
$$

We conclude that $\displaystyle\int_1^{\infty}\frac{1+e^{-x}}{\sqrt{x}}\,dx$ is divergent.

:::{applet}
:url: calculus/improper_integrals/comparing_improper_integrals_4
:name: Fig:Integration:ImproperIntegralsComparisonExample4
:class: dark-light

The graphs of $\dfrac{1+e^{-x}}{\sqrt{x}}$ and $\dfrac{1}{\sqrt{x}}$ on the interval $[1,\infty)$.
:::

::::::

## Special improper integrals

There exist many special improper integrals that are often used in various applications. We will discuss two of them here.

### $p$-integrals

We start with the so-called *$p$-integrals*:

:::{prf:definition} $p$-integrals
:label: Def:Integration:ImproperIntegralsPIntegrals
An integral of the form $\displaystyle\int_a^{\infty}\frac{dx}{x^p}$ or $\displaystyle\int_0^a\frac{dx}{x^p}$ for some $a>0$ and $p\in\mathbb{R}$ is called a **$p$-integral**.
:::

$p$-integrals can easily be analysed using the next theorem.

::::::{prf:Theorem}
:label: Thm:Integration:ImproperIntegralsPIntegrals
For $0<a<\infty$ we have

1. $\displaystyle\int_a^{\infty}\frac{dx}{x^p}=\begin{cases}\dfrac{a^{1-p}}{p-1}, &p>1\\\infty, &p\leq1.\end{cases}$

1. $\displaystyle\int_0^a\frac{dx}{x^p}=\begin{cases}\dfrac{a^{1-p}}{1-p}, &p<1\\\infty, &p\geq1.\end{cases}$
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Integration:ImproperIntegralsPIntegrals`
:class: tudproof, dropdown
:name: Proof:Integration:ImproperIntegralsPIntegrals

1. For $p\neq1$ we have

   $$
   \int_a^{\infty}\frac{dx}{x^p}=\lim_{R\to\infty}\int_a^R\frac{dx}{x^p}=\lim_{R\to\infty}\bigg[\frac{x^{1-p}}{1-p}\bigg]_a^R=\lim_{R\to\infty}\left(\frac{R^{1-p}}{1-p}-\frac{a^{1-p}}{1-p}\right).
   $$

   This limit exists if $1-p<0$ (then: $\displaystyle\lim_{R\to\infty}\frac{R^{1-p}}{1-p}=0$) and $\displaystyle\lim_{R\to\infty}\frac{R^{1-p}}{1-p}$ equals $\infty$ if $1-p>0$.
   
   For $p=1$ the integral reads
   
   $$
   \int_a^{\infty}\frac{dx}{x},
   $$
   
   which is divergent.

1. For $p\neq1$ we have
   
   $$
   \int_0^a\frac{dx}{x^p}=\lim_{c\to 0^+}\int_c^a\frac{dx}{x^p}=\lim_{c\to 0^+}\bigg[\frac{x^{1-p}}{1-p}\bigg]_c^a=\lim_{c\to 0^+}\left(\frac{a^{1-p}}{1-p}-\frac{c^{1-p}}{1-p}\right).
   $$

   This limit exists if $1-p>0$ (then: $\displaystyle\lim_{c\to 0^+}\frac{c^{1-p}}{1-p}=0$) and $\displaystyle\lim_{c\to 0^+}\frac{c^{1-p}}{1-p}$ equals $-\infty$ if $1-p<0$.
   
   For $p=1$ the integral reads
   
   $$
   \int_0^a\frac{dx}{x},
   $$
   
   which is divergent.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsPIntegralsExample1

1. The integral $\displaystyle\int_1^{\infty}\frac{dx}{x^2}$ is convergent since it is a $p$-integral with $p=2>1$. Furthermore, we have $\displaystyle\int_1^{\infty}\frac{dx}{x^2}=1$.
   
   Using the definition, we have
   
   $$
   \int_1^{\infty}\frac{dx}{x^2}=\lim_{R\to\infty}\int_1^R\frac{dx}{x^2}=\lim_{R\to\infty}\bigg[-\frac{1}{x}\bigg]_1^R=\lim_{R\to\infty}\left(1-\frac{1}{R}\right)=1.
   $$

2. The integral $\displaystyle\int_1^{\infty}\frac{dx}{x}$ is divergent since it is a $p$-integral with $p=1\leq1$.
   
   Using the definition, we have

   $$
   \int_1^{\infty}\frac{dx}{x}=\lim_{R\to\infty}\int_1^R\frac{dx}{x}=\lim_{R\to\infty}\bigg[\ln(x)\bigg]_1^R=\lim_{R\to\infty}\ln(R)=\infty.
   $$

::::::

These $p$-integrals are often used in the {prf:ref}`comparison test for improper integrals <Thm:Integration:ImproperIntegralsComparison>` as we have seen in {prf:ref}`Ex:Integration:ImproperIntegralsComparisonExample1`. Here is another example:

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsPIntegralsExample2

Consider the integrals $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{\sqrt{x}}\,dx$ and $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{x\sqrt{x}}\,dx$.

For $x\geq1$ we have $\frac{1}{4}\pi\leq\arctan(x)<\frac{1}{2}\pi$. Hence we have

$$
\frac{\arctan(x)}{\sqrt{x}}\geq\frac{1}{4}\pi\cdot\frac{1}{\sqrt{x}}\quad\text{and}\quad\frac{\arctan(x)}{x\sqrt{x}}\leq\frac{1}{2}\pi\cdot\frac{1}{x\sqrt{x}}.
$$

Now, $\displaystyle\int_1^{\infty}\frac{dx}{\sqrt{x}}$ is a $p$-integral with $p=\frac{1}{2}\leq1$ which diverges and $\displaystyle\int_1^{\infty}\frac{dx}{x\sqrt{x}}$ is a $p$-integral with $p=\frac{3}{2}>1$ which converges.

We conclude that $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{\sqrt{x}}\,dx$ is divergent and that $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{x\sqrt{x}}\,dx$ is convergent.

::::::

### The gamma function

Next up is the *gamma function*:

:::{prf:definition} The gamma function
:label: Def:Integration:ImproperIntegralsGammaFunction

The **gamma function** $\Gamma(x)$ is defined by the improper integral

$$
\Gamma(x)=\int_0^{\infty}t^{x-1}e^{-t}\,dt.
$$
:::

The domain of the gamma function is $(0,\infty)$ and has many remarkable properties. We start by showing its domain, for which the proof uses the theory from this section, and then we will discuss some of its properties.

:::{prf:theorem}
:label: Thm:Integration:GammaFunctionDomain

The maximal domain $D_\Gamma$ of the gamma function is $D_\Gamma=(0,\infty)$.
:::

::::::{admonition} Proof of {prf:ref}`Thm:Integration:GammaFunctionDomain`
:class: tudproof, dropdown

The maximal domain $D_\Gamma$ of the gamma function

$$
\Gamma(x)=\int_0^{\infty}t^{x-1}e^{-t}\,dt,
$$

is precisely the values of $x$ for which the improper integral converges.

We investigate the convergence of the integral by splitting the integral in two parts:

$$
\int_0^{\infty}t^{x-1}e^{-t}\,dt=\int_0^1t^{x-1}e^{-t}\,dt+\int_1^{\infty}t^{x-1}e^{-t}\,dt.
$$

We first investigate the first part $\displaystyle\int_0^1t^{x-1}e^{-t}\,dt$. Note that for $0\leq t\leq 1$

$$
t^{x-1}e^{-1} \leq t^{x-1}e^{-t} \leq t^{x-1}.
$$

We consider four cases:

1. If $x<0$, we have $x-1<0$ and as such the function $t^{x-1}$ is not continuous at $t=0$, and we find
   
$$
\begin{align*}
   \int_0^1t^{x-1}e^{-t}\,dt &\geq \int_0^1t^{x-1}e^{-1}\,dt \\
   &= \lim_{s\rightarrow0^+}\bigg[\frac{t^{x}}{x}e^{-1}\bigg]_s^1 \\
   &= \lim_{s\rightarrow0^+}\frac{1}{x}e^{-1}\bigg(1- s^{x}\bigg)\\
   &= \infty.
   \end{align*}
$$

   So for $x<0$ the integral $\displaystyle\int_0^1t^{x-1}e^{-t}\,dt$ diverges and thus is $(-\infty,0)$ not part of $D_\Gamma$.

1. If $x=0$, we find 
   
$$
\begin{align*}
   \int_0^1t^{-1}e^{-t}\,dt &\geq \int_0^1t^{-1}e^{-1}\,dt \\
   &= \lim_{s\rightarrow0^+}\bigg[\ln(t)e^{-1}\bigg]_s^1 \\
   &= \lim_{s\rightarrow0^+}e^{-1}\bigg(0- \ln(s)\bigg)\\
   &= \infty.
   \end{align*}
$$

   So for $x=0$ the integral $\displaystyle\int_0^1t^{x-1}e^{-t}\,dt$ diverges and thus is ${0}$ not part of $D_\Gamma$.

1. If $0<x<1$, we have $-1<x-1<0$ and and find
   
$$
\begin{align*}
   \int_0^1t^{x-1}e^{-t}\,dt &\leq \int_0^1t^{x-1}\,dt \\
   &= \lim_{s\rightarrow0^+}\bigg[\frac{t^{x}}{x}e^{-1}\bigg]_s^1 \\
   &= \lim_{s\rightarrow0^+}e^{-1}\bigg(1- s^{x}\bigg)\\
   &= e{-1}.
   \end{align*}
$$

   So for $0<x<1$ the integral $\displaystyle\int_0^1t^{x-1}e^{-t}\,dt$ converges and thus $(0,1)$ can still be part of $D_\Gamma$.

1. If $x\geq1$ the calculations become
   
$$
\begin{align*}
   \int_0^1t^{x-1}e^{-t}\,dt &\leq \int_0^1t^{x-1}\,dt \\
   &= \bigg[\frac{t^{x}}{x}e^{-1}\bigg]_0^1 \\
   &= e^{-1}\bigg(1- 0\bigg)\\
   &= e{-1}.
   \end{align*}
$$

   So for $x\geq1$ the integral $\displaystyle\int_0^1t^{x-1}e^{-t}\,dt$ exists and thus $[1,\infty)$ can still be part $D_\Gamma$.

From the above we find that $D_\Gamma\subseteq(0,\infty)$.

Now we turn to the second part $\displaystyle\int_1^\infty t^{x-1}e^{-t}\,dt$ and show this improper integral converges. We consider two cases:

1. If $0<x<1$, we have the comparison
   
   $$
   t^{x-1}\leq 1,
   $$

   which gives the calculations

$$
\begin{align*}
   \int_1^\infty t^{x-1}e^{-t}\,dt &\leq \int_1^\infty e^{-t}\,dt \\
   &= \lim_{R\rightarrow\infty}\bigg[-e^{-t}\bigg]_0^R \\
   &= \lim_{s\rightarrow0^+}1-e^{-R}\\
   &= 1.
   \end{align*}
$$

   So for $0<x<1$ the integral $\displaystyle\int_0^1t^{x-1}e^{-t}\,dt$ converges and thus $(0,1)$ is part of $D_\Gamma$.

1. If $x\geq1$, the above comparison does not work, but we can use {prf:ref}`Theorem:LimitAtInfinity:Standardgrowthrates`. This theorem gives that the function $t^{x-1}$ grows slower than any function of the form $e^{ax}$ with $a>0$.

   This means that for every $a>0$ there is some value $N\geq1$ so that
 
   $$
   t^{x-1} \leq e^{at}.
   $$

   We can use this as follows by writing, for any $a>0$,
   
   $$
   \int_1^\infty t^{x-1}e^{-t}\,dt = \int_1^N t^{x-1}e^{-t}\,dt + \int_N^\infty t^{x-1}e^{-t}\,dt.
   $$

   The first integral is proper, so gives a finite value as a result. The second integral can be investigated as follows:

$$
\begin{align*}
   \int_N^\infty t^{x-1}e^{-t}\,dt &\leq \int_N^\infty e^{at}e^{-t}\,dt \\
   &= \lim_{R\rightarrow\infty}\int_N^R e^{(a-1)t}\,dt \\
   &= \lim_{R\rightarrow\infty}\bigg[\frac{1}{a-1}e^{(a-1)t}\bigg]_N^R \\
   &= \lim_{R\rightarrow\infty}\frac{1}{a-1}\bigg(e^{(a-1)R}-e^{(a-1)N}\bigg).
   \end{align*}
$$

   This last limit exists when $a<1$. As the above held for any $a>0$, and we only need one, we pick $a=\dfrac12$.
   
   We find that $\displaystyle\int_1^\infty t^{x-1}e^{-t}\,dt$ converges for $x\geq1$ and and thus $[1,\infty)$ is part of $D_\Gamma$.
  
In conclusion, the maximal domain $D_\Gamma$ is $(0,1)\cup[1,\infty)=(0,\infty)$.

::::::

In {numref}`Fig:Integration:GammaFunction` you can see the gamma function. We have alo added several circles at positions of the form $(n,n!)$, where $n!$ is the factorial of a non-negative integer $n$, see {prf:ref}`Def:SumsAndProducts:Factorial`.

:::{applet}
:url: calculus/improper_integrals/gamma_function
:name: Fig:Integration:GammaFunction
:class: dark-light

The gamma function $\Gamma$ on its maximal domain $D_\Gamma=(0,\infty)$.\
The vertical axis uses a logarithmic scale, so the horizontal axis represents $y=1$.
:::


Note that the gamma function seems to be increasing as fast as the factorials, but with a slight delay. The next theorem gives the direct relation between the gamma function and the factorial.

:::{prf:theorem}
:label: Thm:Integration:GammaFunctionFactorial

For any $x>0$

$$
\Gamma(x+1) = x\Gamma(x),
$$

and for any integer $n\geq0$

$$
\Gamma(n+1)=n!.
$$
:::

::::::{admonition} Proof of {prf:ref}`Thm:Integration:GammaFunctionFactorial`
:class: tudproof

Note that $\Gamma(1)=\displaystyle\int_0^{\infty}e^{-t}\,dt=-e^{-t}\bigg|_0^{\infty}=1$.

Using integration by parts we obtain for $x>0$

$$
\begin{align*}
\Gamma(x+1)&=\int_0^{\infty}t^xe^{-t}\,dt\\
&=\bigg[-t^xe^{-t}\bigg]_{t=0}^{\infty}+\int_0^{\infty}e^{-t}\,xt^{x-1}\,dt\\
&=0+x\int_0^{\infty}t^{x-1}e^{-t}\,dt\\
&=x\Gamma(x).
\end{align*}
$$

Then we have $\Gamma(2)=1\cdot\Gamma(1)=1$, $\Gamma(3)=2\cdot\Gamma(2)=2\cdot1=2$, $\Gamma(4)=3\cdot\Gamma(3)=3\cdot2=6$, and so on.

We conclude that $\Gamma(n+1)=n!$ for $n=0,1,2,\ldots$.

::::::

So, the gamma function can be seen as a generalisation of the factorial. You can investigate this relation using the toggle in {numref}`Fig:Integration:GammaFunction`.

Furthermore, using the substitution $t=u^2$ we have

$$
\Gamma(\tfrac{1}{2})=\int_0^{\infty}t^{-\frac{1}{2}}e^{-t}\,dt=\int_0^{\infty}u^{-1}e^{-u^2}\cdot2u\,du=2\int_0^{\infty}e^{-u^2}\,du.
$$
 
Later (see {prf:ref}`Ex:MultivariableIntegration:PolarApplicationsExample2`) we will prove that $\displaystyle\int_0^{\infty}e^{-u^2}\,du=\frac{1}{2}\sqrt{\pi}$. This implies that $\Gamma(\frac{1}{2})=\sqrt{\pi}$.



## Grasple exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4bc56611-e3cb-4f5a-b99e-96a54f7a6f63?id=133534
:label: Grasple:133534
:dropdown:
:description: Evaluate the integral if possible.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/908b4739-bd46-4030-a584-613f5e5132e0?id=133535
:label: Grasple:133535
:dropdown:
:description: Evaluate the integral if possible.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/50d7af4a-e5d5-429b-80af-548619f6de3b?id=133537
:label: Grasple:133537
:dropdown:
:description: Evaluate the integral if possible.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/419e3b07-2e9f-42a4-ae53-3684a413fcd1?id=133538
:label: Grasple:133538
:dropdown:
:description: Evaluate the integral if possible.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/766f1dc7-f1df-4723-bd3f-ef267f8c6482?id=133539
:label: Grasple:133539
:dropdown:
:description: Evaluate the integral if possible.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2b020706-0274-4fbb-a65d-5c74eb9f31fa?id=133540
:label: Grasple:133540
:dropdown:
:description: Evaluate the integral if possible.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d31cf77b-bf5f-415a-99b7-9cd6d26dbbbe?id=133527
:label: Grasple:133527
:dropdown:
:description: Evaluate $\displaystyle\int_0^{\infty}\frac{x}{1+x^3}\,dx$ exactly.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/89200258-8d20-4fbb-ac52-f94e7de3ed38?id=133530
:label: Grasple:133530
:dropdown:
:description: Evaluate $\displaystyle\int_0^{\infty}\frac{\ln(x)}{1+x^2}\,dx$.

::::

::::::{note}
:name: Note:Integration:CatalansConstant

Here we showed that $\displaystyle-\int_0^1\frac{\ln(x)}{1+x^2}\,dx=\int_1^{\infty}\frac{\ln(x)}{1+x^2}\,dx$ without evaluating the integrals. Later we will see that the value is equal to *Catalan's constant*. See: {numref}`sec:CatalansConstant`.
::::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3073ee80-954c-4db4-b43d-eac5c09b8716?id=133528
:label: Grasple:133528
:dropdown:
:description: Evaluate $\displaystyle\int_0^{\infty}\frac{dx}{(1+x)\sqrt{x}}\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/838fbda7-e1e8-483a-a5cb-6cd47aacd69d?id=133531
:label: Grasple:133531
:dropdown:
:description: A remarkable class of integrals.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ba0412df-e79f-486b-bd82-26cdfedf09a6?id=133541
:label: Grasple:133541
:dropdown:
:description: Use a comparison theorem to determine whether the integrals converge or diverge.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/df409f93-7f92-45f3-b8aa-4b297d8712d5?id=78797
:label: Grasple:78797
:dropdown:
:description: Use a comparison theorem to determine whether the integral converges or diverges.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8786072a-eedf-4980-9dbe-fcfab66eb59a?id=78799
:label: Grasple:78799
:dropdown:
:description: Use a comparison theorem to determine whether the integral converges or diverges.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fdb58ae4-7de8-4ae8-b6aa-0ad84d55b7a6?id=78801
:label: Grasple:78801
:dropdown:
:description: Use a comparison theorem to determine whether the integral converges or diverges.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/156a7bde-6aa4-468c-b4ed-de7eca985aeb?id=78807
:label: Grasple:78807
:dropdown:
:description: Use a comparison theorem to determine whether the integral converges or diverges.

::::
