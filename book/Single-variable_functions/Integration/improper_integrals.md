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

But this means that an integral is improper if

- the interval of integration is not closed and/or not finite,

and/or

- the integrand is not continuous.

In the next subsections we will first consider the two cases separately and then the combination of these cases.

## Infinite interval of integration

Let us first consider the case where the interval of integration is *not finite*. This means that the interval of integration is infinite, i.e., it is of the form $[a,\infty)$, $(-\infty,b]$ or $(-\infty,\infty)$. Note that these intervals are all closed.

Improper integrals over such intervals are defined as a (sum of) limit(s) which may or may not exist. We will give a definition for each of the three types of infinite intervals of integration.

::::::{prf:Definition} Improper integrals with right-infinite interval of integration
:label: Def:Integration:ImproperIntegralInfiniteIntervalRight

If $f$ is continuous on the interval $[a,\infty)$, then

$$
\int_a^{\infty}f(x)\,dx=\lim_{R\to\infty}\int_a^Rf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the improper integral $\displaystyle\int_a^{\infty}f(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_a^{\infty}f(x)\,dx$ is **divergent**. If the limit does not exist and equals $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_a^{\infty}f(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::

::::::{prf:Definition} Improper integrals with left-infinite interval of integration
:label: Def:Integration:ImproperIntegralInfiniteIntervalLeft

If $f$ is continuous on the interval $(-\infty,b]$, then

$$
\int_{-\infty}^bf(x)\,dx=\lim_{R\to-\infty}\int_R^bf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the improper integral $\displaystyle\int_{-\infty}^bf(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_{-\infty}^bf(x)\,dx$ is **divergent**. If the limit does not exist and equals $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_{-\infty}^bf(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::

::::::{prf:Definition} Improper integrals with double-infinite interval of integration
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

```{figure} Images/improper1.png
---
width: 50%
name: Fig:Integration:ImproperIntegral1
align: center
---
The function $\displaystyle\frac{1}{x\sqrt{x}}$ on the interval $[1,\infty)$.
```

This function $\displaystyle\frac{1}{x\sqrt{x}}$ is continuous on $[1,\infty)$ and therefore we can define the improper integral $\displaystyle\int_1^{\infty}\frac{dx}{x\sqrt{x}}$ as in {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalRight`. We have

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

This last limit does not exist, and equals $\infty$. In this case we say that the improper integral diverges to infinity.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample3

Now we consider the function $\dfrac{1}{1+x^2}$ that is continuous on $(-\infty,\infty)$ and therefore we can define the improper integral $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$ as in {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalDouble`.

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

In this case we choose the central point $c=0$ but we could have chosen any other value of $c\in\mathbb{R}$ as well. The value of the integral does not depend on the choice of $c$. 

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

$$
\int_{-\infty}^{\infty}\frac{dx}{1+x^2} = \int_{-\infty}^0\frac{dx}{1+x^2}+\int_0^{\infty}\frac{dx}{1+x^2} = \frac{1}{2}\pi+\frac{1}{2}\pi = \pi.
$$

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

\begin{align*}
\int_0^{\infty}\frac{x}{1+x^2}\,dx&=\lim_{R\to\infty}\int_0^R\frac{x}{1+x^2}\,dx\\
&=\lim_{R\to\infty}\left[\frac{1}{2}\ln(1+x^2)\right]_0^R\\
&=\lim_{R\to\infty}\frac{1}{2}\ln(1+R^2)\\
&=\infty.
\end{align*}

This implies that the integral *diverges*. Nevertheless, we also have

\begin{align*}
\int_{-\infty}^0\frac{x}{1+x^2}\,dx&=\lim_{R\to-\infty}\int_R^0\frac{x}{1+x^2}\,dx\\
&=\lim_{R\to-\infty}\left[\frac{1}{2}\ln(1+x^2)\right]_R^0\\
&=\lim_{R\to-\infty}\left(-\frac{1}{2}\ln(1+R^2)\right)\\
&=-\infty.
\end{align*}

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

\begin{align*}
\int_0^{\infty}\frac{x}{1+x^4}\,dx&=\lim_{R\to\infty}\int_0^R\frac{x}{1+x^4}\,dx\\
&=\lim_{R\to\infty}\left[\frac{1}{2}\arctan(x^2)\right]_0^R\\
&=\lim_{R\to\infty}\frac{1}{2}\arctan(R^2)\\
&=\frac{1}{2}\cdot\frac{1}{2}\pi\\
&=\frac{1}{4}\pi
\end{align*}

and

\begin{align*}
\int_{-\infty}^0\frac{x}{1+x^4}\,dx&=\lim_{R\to-\infty}\int_R^0\frac{x}{1+x^4}\,dx\\
&=\lim_{R\to-\infty}\left[\frac{1}{2}\arctan(x^2)\right]_R^0\\
&=\lim_{R\to-\infty}\left(-\frac{1}{2}\arctan(R^2)\right)\\
&=-\frac{1}{2}\cdot\frac{1}{2}\pi\\
&=-\frac{1}{4}\pi.
\end{align*}

Hence, we have

$$
\int_{-\infty}^{\infty}\frac{x}{1+x^4}\,dx=\int_{-\infty}^0\frac{x}{1+x^4}\,dx+\int_0^{\infty}\frac{x}{1+x^4}\,dx=-\frac{1}{4}\pi+\frac{1}{4}\pi=0.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample6

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

::::::{note}
:name: Note:Integration:ImproperIntegralsNotation

We will often use the short notation $\displaystyle\int_1^{\infty}\frac{dx}{x^2}=\bigg[-\frac{1}{x}\bigg]_1^{\infty}=1$. This means

$$
\int_1^{\infty}\frac{dx}{x^2}=\lim_{R\to\infty}\bigg[-\frac{1}{x}\bigg]_1^R=\lim_{R\to\infty}\left(1-\frac{1}{R}\right)=1.
$$

::::::

## Discontinuous integrands

Having discussed the intervals of integration, we now turn our attention to the integrand. For this subsection we assume that the interval of integration is closed and finite, i.e., of the form $[a,b]$.

{numref}`Section:Continuity` discusses what we consider to be continuity with respect to a function. As continuity is a local property, we will discuss three possible cases of discontinuity of the integrand $f$ on the interval $[a,b]$:

- the integrand $f$ is not right-continuous at $x=a$ (i.e. at the left of the interval).
- the integrand $f$ is not left-continuous at $x=b$ (i.e. at the right of the interval).
- the integrand $f$ is discontinuous at some point $c\in(a,b)$ (i.e. in the interior of the interval).

Note that we consider discontinuity (or being not continuous) in general. Examples of discontinuity include jump discontinuity, infinite discontinuity and removable discontinuity.

In particular, we do not require the integrand to be unbounded near the point of discontinuity, but it may be unbounded as well.

In fact, we consider integrands that are discontinuous in a finite number of points, but which are not piecewise continuous. So, at these points at least one-sided limit does not exist.

The way we define improper integrals with a discontinuous integrand is more general than the way it is often defined in other textbooks, where the integrand is required to be unbounded near the point of discontinuity.

For each of the three cases we will define how to handle the improper integral $\displaystyle\int_a^bf(x)\,dx$.

::::::{prf:Definition} Improper integrals with discontinuous integrand at left endpoint
:label: Def:Integration:ImproperIntegralLeftDiscontinuousIntegrand

If $f$ is continuous on the interval $(a,b]$, then

$$
\int_a^bf(x)\,dx=\lim_{t\to a^+}\int_t^bf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ is **divergent**. If the limit does not exist and equals $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::

::::::{prf:Definition} Improper integrals with discontinuous integrand at right endpoint
:label: Def:Integration:ImproperIntegralRightDiscontinuousIntegrand

If $f$ is continuous on the interval $[a,b)$, then

$$
\int_a^bf(x)\,dx=\lim_{t\to b^-}\int_a^tf(x)\,dx,
$$
provided the limit exists.

If the limit exists, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ is **convergent**.

If the limit does not exist, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ is **divergent**. If the limit does not exist and equals $\infty$ or $-\infty$, we say that the improper integral $\displaystyle\int_a^bf(x)\,dx$ **diverges to infinity** or **diverges to negative infinity**, respectively.
::::::

::::::{prf:Definition} Improper integrals with discontinuous integrand at internal point
:label: Def:Integration:ImproperIntegralInternalDiscontinuousIntegrand

If $f$ is discontinuous at some point $c\in(a,b)$, then

$$
\int_a^bf(x)\,dx=\int_a^cf(x)\,dx+\int_c^bf(x)\,dx
$$
provided the two improper integrals on the right converge.

If the two improper integrals on the right converge, we say that the improper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ is **convergent**.

If at least one of the two improper integrals on the right does not converge, we say that the improper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ is **divergent**.

If one of the improper integrals on the right converges and the other one diverges to infinity, or if both improper integrals on the right diverge to infinity, we say that the improper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ **diverges to infinity**. 

If one of the improper integrals on the right converges and the other one diverges to negative infinity, or if both improper integrals on the right diverge to negative infinity, we say that the improper integral $\displaystyle\int_{a}^{b}f(x)\,dx$ **diverges to negative infinity**.

::::::

We start with an example of an improper integral with a discontinuous integrand at an internal point of the interval of integration.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsDiscontinuousIntegrandExample1

We integrate the function $\displaystyle\frac{1}{x^2}$ on the interval $[-1,1]$. 

```{figure} Images/improper5.png
---
width: 50%
name: Fig:Integration:ImproperIntegral5
align: center
figclass: center
---
The function $\displaystyle\frac{1}{x^2}$.
```

This function is continuous on $[-1,0)$ and on $(0,1]$ but is not continuous at $x=0$. Hence, we can define the improper integral $\displaystyle\int_{-1}^1\frac{dx}{x^2}$ as in {prf:ref}`Def:Integration:ImproperIntegralInternalDiscontinuousIntegrand`. We have

$$
\int_{-1}^1\frac{dx}{x^2}=\int_{-1}^0\frac{dx}{x^2}+\int_0^1\frac{dx}{x^2}.
$$

Now we have

\begin{align*}
\int_{-1}^0\frac{dx}{x^2} &= \lim_{t\to 0^-}\int_{-1}^t\frac{dx}{x^2} \\
&= \lim_{t\to0^-}\bigg[-\frac{1}{x}\bigg]_{-1}^t \\
&= \lim_{t\to 0^-}\left(-\frac{1}{t}-1\right) \\
&= \infty.
\end{align*}

At this point we can already conclude that the integral $\displaystyle\int_{-1}^1\frac{dx}{x^2}$ is divergent. Nevertheless, we evaluate the second integral to show that it also diverges to infinity:

\begin{align*}
\int_0^1\frac{dx}{x^2} &= \lim_{t\to 0^+}\int_t^1\frac{dx}{x^2} \\
&= \lim_{t\to 0^+}\bigg[-\frac{1}{x}\bigg]_t^1 \\
&= \lim_{t\to 0^+}\left(-1+\frac{1}{t}\right) \\
&= \infty.
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

is clearly wrong! Note that the integrand is positive on $[-1,1]$. The evaluation is incorrect because the integrand is not continuous at $x=0$. So, the fundamental theorem of calculus does not apply.
::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsDiscontinuousIntegrandExample2

Consider the function $\dfrac{1}{x-1}$ on the interval $[0,3]$.

```{figure} Images/improper6.png
---
width: 50%
name: Fig:Integration:ImproperIntegral6
align: center
figclass: center
---
The function $\displaystyle\frac{1}{x-1}$.
```

Since $\dfrac{1}{x-1}$ is continuous for all $x\in\mathbb{R}$ except at $x=1$, we have

$$
\int_0^3\frac{dx}{x-1}=\int_0^1\frac{dx}{x-1}+\int_1^3\frac{dx}{x-1}
$$

with

\begin{align*}
\int_0^1\frac{dx}{x-1} &= \lim_{c\to 1^-}\int_0^c\frac{dx}{x-1} \\
&= \lim_{c\to 1^-}\bigg[\ln|x-1|\bigg]_0^c \\
&= \lim_{c\to 1^-}\ln|c-1| \\
&= -\infty
\end{align*}

and

\begin{align*}
\int_1^3\frac{dx}{x-1} &= \lim_{c\to1^+}\int_c^3\frac{dx}{x-1} \\
&= \lim_{c\to 1^+}\bigg[\ln|x-1|\bigg]_c^3 \\
&= \lim_{c\to 1^+}\left(\ln(2)-\ln|c-1|\right) \\
&= \infty.
\end{align*}

Because both integrals diverge, we say that the improper integral $\displaystyle\int_0^3\frac{dx}{x-1}$ diverges.

::::::

::::::{warning}
:name: Warning:Integration:ImproperIntegralsDiscontinuousIntegrandWarning2

It would be wrong to conclude that

$$
\int_0^3\frac{dx}{x-1}=-\infty+\infty=0
$$

and it is also incorrect to state that

$$
\int_0^3\frac{dx}{x-1}=\ln|x-1|\bigg|_0^3=\ln(2)-\ln(1)=\ln(2).
$$

Since the integrand is discontinuous at $x=1$ the fundamental theorem does not apply on $[0,3]$.
::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsDiscontinuousIntegrandExample3

Consider $\displaystyle\int_0^1\ln(x)\,dx$. 

```{figure} Images/improper7.png
---
width: 50%
name: Fig:Integration:ImproperIntegral7
align: center
figclass: center
---
The function $\displaystyle\ln(x)$.
```

Using integration by parts, we have

\begin{align*}
\int\ln(x)\,dx &= x\ln(x)-\int x\cdot\frac{1}{x}\,dx \\
&= x\ln(x)-x+C.
\end{align*}

Hence, we have

\begin{align*}
\int_0^1\ln(x)\,dx &= \lim_{t\to o^+}\bigg[x\ln(x)-x\bigg]_t^1 \\
&= \lim_{t\to 0^+}\left(-1-t\ln(t)+t\right).
\end{align*}

Using l'Hospital's rule, we obtain

\begin{align*}
\lim_{t\to 0^+}t\ln(t) &= \lim_{t\to 0^+}\frac{\ln(t)}{1/t} \\
&= \lim_{t\to 0^+}\frac{1/t}{-1/t^2} \\
&= \lim_{t\to 0^+}\left(-t\right) \\
&=0.
\end{align*}

We conclude that

$$
\int_0^1\ln(x)\,dx=\lim_{t\to 0^+}\left(-1-t\ln(t)+t\right)=-1-0+0=-1.
$$

::::::

Finally, we consider an example of both an infinite interval of integration and a discontinuous integrand.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsDiscontinuousIntegrandExample4

Consider $\displaystyle\int_0^{\infty}\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx$.

Using {prf:ref}`Def:Integration:ImproperIntegralInfiniteIntervalRight` and {prf:ref}`Def:Integration:ImproperIntegralLeftDiscontinuousIntegrand` we write

$$
\int_0^{\infty}\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx=\lim_{R\to\infty}\lim_{t\to 0^+}\int_t^R\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx.
$$

For $0<t<x<R$ we apply the substitution $x=u^2$ and therefore $dx=2u\,du$ to obtain

\begin{align*}
\int_t^R\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx&=\int_{\sqrt{t}}^{\sqrt{R}}\frac{e^{-u}}{u}\cdot2u\,du\\
&=\int_{\sqrt{t}}^{\sqrt{R}}2e^{-u}\,dx\\
&=\Big[-2e^{-u}\Big]_{\sqrt{t}}^{\sqrt{R}}\\
&=2e^{-\sqrt{t}}-2e^{-\sqrt{R}}.
\end{align*}

Hence, we have

\begin{align*}
\int_0^{\infty}\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx&=\lim_{R\to\infty}\lim_{t\to 0^+}\int_t^R\frac{e^{-\sqrt{x}}}{\sqrt{x}}\,dx\\
&=\lim_{R\to\infty}\lim_{t\to 0^+}\left(2e^{-\sqrt{t}}-2e^{-\sqrt{R}}\right)\\
&=\lim_{t\to 0^+}2e^{-\sqrt{t}}-\lim_{R\to\infty}2e^{-\sqrt{R}}\\
&=2-0\\
&=2.
\end{align*}

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

::::::{note}
:name: Note:Integration:ImproperIntegralsGaussianIntegral

Later (see: {prf:ref}`Ex:MultivariableIntegration:PolarApplicationsExample2`) we will see that $\displaystyle\int_0^{\infty}e^{-x^2}\,dx=\frac{1}{2}\sqrt{\pi}\approx0.88623$.

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

::::{question} Short-answer blocks
:type: short-answer
:variant: blocks
:columns: 1
:class: question
:admonition:
:showanswer:

Fill in the correct answer in the input fields.

In order to find a better approximation, we want to find another linear function of the form $-x+c$ with $c\in\mathbb{R}$ such that $-x^2\leq-x+c$ for all $x\geq0$.

---
M[\frac{1}{4}] Then the optimal value of $c$ is
= Note that $-x^2\leq-x+c$ is equivalent to $x^2-x+c\geq0$. The discriminant $D$ of $x^2-x+c=0$ is $D=1-4c$ which equals zero if $c=\frac{1}{4}$.
> Consider $x^2-x+c\geq0$ and use the discriminant.

Use this value of $c$ to find an upper bound for $\displaystyle\int_0^{\infty}e^{-x^2}\,dx$:
M[e^{\frac{1}{4}}] $\displaystyle\int_0^{\infty}e^{-x+c}\,dx=$
= Note that $x^2-x+\frac{1}{4}\geq0$ is equivalent to $(x-\frac{1}{2})^2\geq0$. Now $-x^2\leq-x+\frac{1}{4}$ leads to $e^{-x^2}\leq e^{-x+\frac{1}{4}}$ and

$$
\int_0^{\infty}e^{-x+\frac{1}{4}}\,dx=\left[-e^{-x+\frac{1}{4}}\right]_0^{\infty}=e^{\frac{1}{4}}\approx1.28403.
$$

> Evaluate $\displaystyle\int_0^{\infty}e^{-x+\frac{1}{4}}\,dx$.

Replacing the linear function $-x+c$ by a function of the form $-ax+b$, what would be the optimal value of $b$ (in terms of $a$)?
[\frac{1}{4}a^2] $b=$
= Note that $-x^2\leq-ax+b$ is equivalent to $x^2-ax+b\geq0$. The discriminant $D$ of $x^2-ax+b=0$ is $D=a^2-4b$ which equals zero if $b=\frac{1}{4}a^2$.
> Consider $x^2-ax+b\geq0$ and use the discriminant.

In order to find the best approximation, what should be the value of $a$?
[\sqrt{2}] $a=$
= Now we have

$$
\int_0^{\infty}e^{-ax+\frac{1}{4}a^2}\,dx=\left[-\frac{1}{a}e^{-ax+\frac{1}{4}a^2}\right]_{x=0}^{\infty}=\frac{1}{a}e^{\frac{1}{4}a^2}.
$$

Let $f(x)=\dfrac{1}{x}e^{\frac{1}{4}x^2}$, then

$$
f'(x)=\frac{1}{x}e^{\frac{1}{4}x^2}\cdot\frac{1}{2}x-\frac{1}{x^2}e^{\frac{1}{4}x^2}=\left(\frac{1}{2}-\frac{1}{x^2}\right)e^{\frac{1}{4}x^2},
$$

which equals zero if $x=\pm\sqrt{2}$. Since $a$ should be positive, we conclude that $a=\sqrt{2}$.
> Evaluate $\displaystyle\int_0^{\infty}e^{-ax+\frac{1}{4}a^2}\,dx$ and find its minimal value.

Find the least upper bound for this value of $a$.
[\frac{1}{\sqrt{2}}e^{\frac{1}{2}}] $\displaystyle\int_0^{\infty}e^{-x^2}\,dx\leq$
= 

$$
\int_0^{\infty}e^{-\sqrt{2}x+\frac{1}{2}}\,dx=\frac{1}{\sqrt{2}}e^{\frac{1}{2}}\approx1.16582.
$$

> Use $\displaystyle\int_0^{\infty}e^{-ax+\frac{1}{4}a^2}\,dx=\frac{1}{a}e^{\frac{1}{4}a^2}$ for $a=\sqrt{2}$.
---

::::

```{figure} Images/exponential1.png
---
width: 50%
name: exponential1
align: center
---
The graphs of $e^{-x^2}$ and $e^{-x+\frac{1}{4}}$.
```

```{figure} Images/exponential2.png
---
width: 50%
name: exponential2
align: center
---
The graphs of $e^{-x^2}$ and $e^{-x\sqrt{2}+\frac{1}{2}}$.
```

:::{todo}
Can pictures like these be used in the question above?
:::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsComparisonExample3
Consider $\displaystyle\int_1^{\infty}\frac{2+\cos(x)}{x}\,dx$.

Note that $-1\leq\cos(x)\leq1$ and therefore $1\leq2+\cos(x)\leq3$. This implies that

$$
\frac{2+\cos(x)}{x}\geq\frac{1}{x}\quad\text{and}\quad\int_1^{\infty}\frac{dx}{x}=\ln(x)\bigg|_1^{\infty}=\infty.
$$

This implies that $\displaystyle\int_1^{\infty}\frac{2+\cos(x)}{x}\,dx$ is divergent.

```{figure} Images/comparison1.png
---
width: 50%
name: comparison1
align: center
---
The graphs of $\dfrac{2+\cos(x)}{x}$ and $\dfrac{1}{x}$.
```

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsComparisonExample4
Consider $\displaystyle\int_1^{\infty}\frac{1+e^{-x}}{\sqrt{x}}\,dx$.

Note that $1+e^{-x}>1$ and

$$
\int_1^{\infty}\frac{dx}{\sqrt{x}}=2\sqrt{x}\bigg|_1^{\infty}=\infty.
$$

We conclude that $\displaystyle\int_1^{\infty}\frac{1+e^{-x}}{\sqrt{x}}\,dx$ is divergent.

```{figure} Images/comparison2.png
---
width: 50%
name: comparison2
align: center
---
The graphs of $\dfrac{1+e^{-x}}{\sqrt{x}}$ and $\dfrac{1}{\sqrt{x}}$.
```

::::::

(Sec:Integration:Feynman)=

## The Feynman technique

Sometimes an integral is easier to evaluate if we modify the integrand by inserting a parameter such that a specific value of this parameter leads to the original integral. We have already seen an example of this trick in {numref}`Sec:Integration:Parts`. This technique was developed by the American theoretical physicist [Richard Phillips Feynman (1918-1988)](https://en.wikipedia.org/wiki/Richard_Feynman) and is based on the following theorem.

::::::{prf:Theorem}
:label: Thm:Integration:ImproperIntegralsFeynmanTechnique
If $g(x,t)$ and $\displaystyle\frac{\partial}{\partial t}g(x,t)$ are both continuous for all $x\in[a,b]$, then

$$
\frac{d}{dt}\int_a^bg(x,t)\,dx=\int_a^b\frac{\partial}{\partial t}g(x,t)\,dx.
$$

::::::

::::::{note}
:name: Note:Integration:ImproperIntegralsMultivariableFunctionsAndPartialDerivatives

The notation $g(x,t)$ indicates that $g$ is a function of two variables $x$ and $t$, and will be explained in more detail in {numref}`Sec:MultivariableFunctions`. For now, just assume that $g(x,t)$ is a function of two variables and that $g(x,t_0)$ means that you must substitute $t$ with $t_0$ in the function $g$.

The notation $\dfrac{\partial}{\partial t}$ denotes the derivative with respect to $t$ and will be explained in {numref}`Sec:PartialDerivatives`. For now, $\dfrac{\partial}{\partial t}$ means that you must take the derivative of the function with respect to $t$ while treating $x$ as a constant. For example, if $f(x,t)=x^t$, then $\dfrac{\partial}{\partial t}f(x,t)=x^t\ln(x)$.
::::::

The Feynman method itself is most naturally described by the following algorithm:

:::{prf:algorithm} Feynman method
For any definite integral of the form $\displaystyle\int_a^bf(x)\,dx$ perform the following steps:

1. Introduce a parameter-dependent function $g$ based on the integrand $f$ and define $I(t)=\displaystyle\int_a^bg(x,t)\,dx$ such that

    - $I(t_0)=\alpha$ for some value of $t_0$ and some constant $\alpha\in\mathbb{R}$.

    - $g(x,t_1)=f(x)$ for some value of $t_1$. This implies that $I(t_1)=\displaystyle\int_a^bf(x)\,dx$.

3. Find the partial derivative $\displaystyle\frac{\partial}{\partial t}g(x,t)$.

4. Evaluate the integral $I'(t)=\displaystyle\int_a^b\frac{\partial}{\partial t}g(x,t)\,dx$.

5. Integrate $I'(t)$ with respect to $t$ to find $I(t)$ (including a constant of integration).

6. Determine the value of the constant of integration using the value of $I(t_0)=\alpha$.

6. Evaluate $I(t_1)$ to find the value of the original integral $\displaystyle\int_a^bf(x)\,dx$.
:::

Finding a function $g(x,t)$ that works can be very hard. We will give three examples, where this function will be given.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsFeynmanExample1
Consider the improper integral $\displaystyle\int_0^1\frac{x-1}{\ln(x)}\,dx$, which is extremely difficult to evaluate by any other means.

Define $g(x,t)=\dfrac{x^t-1}{\ln(x)}$ and $I(t)=\displaystyle\int_0^1\frac{x^t-1}{\ln(x)}\,dx$ for $t\geq0$, then we have $I(0)=0$,

$$
\frac{\partial}{\partial t}g(x,t)=\frac{x^t\ln(x)}{\ln(x)}=x^t,
$$

and

$$
I'(t)=\int_0^1\frac{\partial}{\partial t}\frac{x^t-1}{\ln(x)}\,dx=\int_0^1x^t\,dx=\frac{x^{t+1}}{t+1}\bigg|_{x=0}^1=\frac{1}{t+1}.
$$

This implies that $I(t)=\ln|t+1|+C$ with $C=I(0)=0$. This gives

$$
I(t)=\int_0^1\frac{x^t-1}{\ln(x)}\,dx=\ln(t+1)
$$

for $t\geq0$. We conclude that

$$
I(1)=\int_0^1\frac{x-1}{\ln(x)}\,dx=\ln(2).
$$

Similarly, we find that 

$$
I(2)=\int_0^1\frac{x^2-1}{\ln(x)}\,dx=\ln(3)
$$ 

and 

$$
I(\tfrac{1}{2})=\int_0^1\frac{\sqrt{x}-1}{\ln(x)}\,dx=\ln\left(\tfrac{3}{2}\right),
$$ 

for instance.

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
&=1+te^{-y}\sin(ty)\bigg|_{y=0}^{\infty}-t^2\int_0^{\infty}e^{-y}\cos(ty)\,dy\\
&=1-t^2\int_0^{\infty}e^{-y}\cos(ty)\,dy.
\end{align*}

Because the integral $I'(t)$ appears on both sides of the equation, we can solve for $I'(t)$ to find that

$$
I'(t)=\int_0^{\infty}e^{-y}\cos(ty)\,dy=\frac{1}{1+t^2}.
$$

Since $I(0)=0$ this implies that $I(t)=\arctan(t)$.

We finally arrive at

$$
\int_0^1\frac{\sin(\ln(x))}{\ln(x)}\,dx=I(1)=\arctan(1)=\frac{1}{4}\pi.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsFeynmanExample3
Consider the integral $I(t)=\displaystyle\int_0^{\infty}\frac{e^{-x}\sin(xt)}{x}\,dx$ for $t\geq0$. Since $\displaystyle\lim\limits_{x\to 0^+}\frac{\sin(xt)}{x}=t$, the integral is convergent. Then we have $I(0)=0$ and using integration by parts

\begin{align*}
I'(t)&=\int_0^{\infty}e^{-x}\cos(xt)\,dx\\
&=-e^{-x}\cos(xt)\bigg|_{x=0}^{\infty}-t\int_0^{\infty}e^{-x}\sin(xt)\,dt\\
&=1+te^{-x}\sin(xt)\bigg|_{x=0}^{\infty}-t^2\int_0^{\infty}e^{-x}\cos(xt)\,dt\\
&=1+0-t^2I'(t),
\end{align*}

and therefore $I'(t)=\dfrac{1}{1+t^2}$. This implies that $I(t)=\displaystyle\arctan(t)$.

For instance, this implies that $\displaystyle\int_0^{\infty}\frac{e^{-x}\sin(x)}{x}\,dx=\arctan(1)=\frac{1}{4}\pi$. Using the substitution $x=\alpha t$ this implies that

$$
\int_0^{\infty}\frac{e^{-\alpha t}\sin(\alpha t)}{t}\,dt=\frac{1}{4}\pi\quad\text{for all}\quad\alpha>0.
$$ 

Furthermore, we have

$$
\int_0^{\infty}\frac{e^{-x}\sin(x\sqrt{3})}{x}\,dx=\arctan\left(\sqrt{3}\right)=\frac{1}{3}\pi
$$

and

$$
\int_0^{\infty}\frac{e^{-t\sqrt{3}}\sin(t)}{t}\,dt=\int_0^{\infty}\frac{e^{-x}\sin\left(\frac{x}{\sqrt{3}}\right)}{x}\,dx=\arctan\left(\tfrac{1}{\sqrt{3}}\right)=\frac{1}{6}\pi.
$$

::::::

## Special improper integrals

There exist many special improper integrals that are often used in various applications. We will discuss some of them here.

### $p$-Integrals

We start with the so-called *$p$-integrals*:

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

(a) For $p\neq1$ we have

$$
\int_a^{\infty}\frac{dx}{x^p}=\lim_{R\to\infty}\int_a^R\frac{dx}{x^p}=\lim_{R\to\infty}\bigg[\frac{x^{1-p}}{1-p}\bigg]_a^R=\lim_{R\to\infty}\left(\frac{R^{1-p}}{1-p}-\frac{a^{1-p}}{1-p}\right).
$$

This limit exists if $1-p<0$ (then: $\displaystyle\lim_{R\to\infty}\frac{R^{1-p}}{1-p}=0$) and $\displaystyle\lim_{R\to\infty}\frac{R^{1-p}}{1-p}$ equals $\infty$ if $1-p>0$. For $p=1$ the integral reads $\displaystyle\int_a^{\infty}\frac{dx}{x}$ which is divergent.

(b) For $p\neq$ we have

$$
\int_0^a\frac{dx}{x^p}=\lim_{c\to 0^+}\int_c^a\frac{dx}{x^p}=\lim_{c\to 0^+}\bigg[\frac{x^{1-p}}{1-p}\bigg]_c^a=\lim_{c\to 0^+}\left(\frac{a^{1-p}}{1-p}-\frac{c^{1-p}}{1-p}\right).
$$

This limit exists if $1-p>0$ (then: $\displaystyle\lim_{c\to 0^+}\frac{c^{1-p}}{1-p}=0$) and $\displaystyle\lim_{c\to 0^+}\frac{c^{1-p}}{1-p}$ equals $-\infty$ if $1-p<0$. For $p=1$ the integral reads $\displaystyle\int_0^a\frac{dx}{x}$ which is divergent.

::::::

:::{todo}
Insert an applet with the graph of $\dfrac{1}{x^p}$ where the value of $p$ can be changed (by a slider?).
:::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsPIntegralsExample1

1) The integral $\displaystyle\int_1^{\infty}\frac{dx}{x^2}$ is convergent since it is a $p$-integral with $p=2>1$. Furthermore, we have $\displaystyle\int_1^{\infty}\frac{dx}{x^2}=1$.

Using the definition, we have

$$
\int_1^{\infty}\frac{dx}{x^2}=\lim_{R\to\infty}\int_1^R\frac{dx}{x^2}=\lim_{R\to\infty}\bigg[-\frac{1}{x}\bigg]_1^R=\lim_{R\to\infty}\left(1-\frac{1}{R}\right)=1.
$$

2) The integral $\displaystyle\int_1^{\infty}\frac{dx}{x}$ is divergent since it is a $p$-integral with $p=1\leq1$. 

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
\Gamma(x)=\int_0^{\infty}t^{x-1}e^{-t}\,dt,\quad x>0.
$$
:::

This gamma function converges for all $x>0$ and has many remarkable properties. We start by showing its convergence and then we will discuss some of its properties.

Let $\displaystyle\int_0^{\infty}t^{x-1}e^{-t}\,dt=\int_0^1t^{x-1}e^{-t}\,dt+\int_1^{\infty}t^{x-1}e^{-t}\,dt$.

For $0\leq t\leq1$ we have $t^{x-1}e^{-1}\leq t^{x-1}e^{-t}\leq t^{x-1}$ and 

$$
\int_0^1t^{x-1}\,dt=\frac{t^x}{x}\bigg|_{t=0}^1=\frac{1}{x},\quad x>0.
$$

For $t\geq1$ we use {prf:ref}`Theorem:LimitAtInfinity:Standardgrowthrates` to conclude that $e^{\frac{1}{2}t}>t^{x-1}$ if $t$ is large enough. Hence there exists an integer $N$ such that for $t\geq N$ we have $e^{\frac{1}{2}t}>t^{x-1}$. Then we have

$$
\int_1^{\infty}e^{-t}t^{x-1}\,dt=\int_1^Ne^{-t}t^{x-1}\,dt+\int_N^{\infty}e^{-t}t^{x-1}\,dt
$$

with

$$
\int_N^{\infty}e^{-t}t^{x-1}\,dt < \int_N^{\infty}e^{-t}e^{\frac{1}{2}t}\,dt
=\int_N^{\infty}e^{-\frac{1}{2}t}\,dt=\left[-2e^{-\frac{1}{2}t}\right]_N^{\infty}=2e^{\frac{1}{2}N}.
$$

We conclude that $\displaystyle\int_0^{\infty}t^{x-1}e^{-t}\,dt$ converges for all $x>0$.

Note that $\Gamma(1)=\displaystyle\int_0^{\infty}e^{-t}\,dt=-e^{-t}\bigg|_0^{\infty}=1$.

Using integration by parts we obtain for $x>0$

\begin{align*}
\Gamma(x+1)&=\int_0^{\infty}t^xe^{-t}\,dt\\
&=-t^xe^{-t}\bigg|_{t=0}^{\infty}+\int_0^{\infty}e^{-t}\,xt^{x-1}\,dt\\
&=0+x\int_0^{\infty}t^{x-1}e^{-t}\,dt\\
&=x\Gamma(x).
\end{align*}

Then we have $\Gamma(2)=1\cdot\Gamma(1)=1$, $\Gamma(3)=2\cdot\Gamma(2)=2\cdot1=2$, $\Gamma(4)=3\cdot\Gamma(3)=3\cdot2=6$, and so on. We conclude that $\Gamma(n+1)=n!$ for $n=0,1,2,\ldots$. So, the gamma function can be seen as a generalisation of the factorial.

Furthermore, using the substitution $t=u^2$ we have

$$
\Gamma(\tfrac{1}{2})=\int_0^{\infty}t^{-\frac{1}{2}}e^{-t}\,dt=\int_0^{\infty}u^{-1}e^{-u^2}\cdot2u\,du=2\int_0^{\infty}e^{-u^2}\,du.
$$
 
Later (see {prf:ref}`Ex:MultivariableIntegration:PolarApplicationsExample2`) we will prove that $\displaystyle\int_0^{\infty}e^{-u^2}\,du=\frac{1}{2}\sqrt{\pi}$. This implies that $\Gamma(\frac{1}{2})=\sqrt{\pi}$.

### The Dirichlet integral

Now we turn our attention to the *Dirichlet integral*:

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

We start by showing that the integral converges. First we write

$$
\int_0^{\infty}\frac{\sin(x)}{x}\,dx=\int_0^1\frac{\sin(x)}{x}\,dx+\int_1^{\infty}\frac{\sin(x)}{x}\,dx.
$$

Since $\displaystyle\lim\limits_{x\to 0^+}\frac{\sin(x)}{x}=1$, the first integral on the right exists. For the second integral on the right we have

$$
\int_1^{\infty}\frac{\sin(x)}{x}\,dx=\lim_{R\to\infty}\int_1^R\frac{\sin(x)}{x}\,dx.
$$

Using integration by parts we obtain

\begin{align*}
\int_1^R\frac{\sin(x)}{x}\,dx&=-\frac{\cos(x)}{x}\bigg|_1^R-\int_1^R\frac{\cos(x)}{x^2}\,dx\\
&=\cos(1)-\frac{\cos(R)}{R}-\int_1^R\frac{\cos(x)}{x^2}\,dx.
\end{align*}

Now we have

$$
\left|\int_1^R\frac{\cos(x)}{x^2}\,dx\right|\leq\int_1^R\left|\frac{\cos(x)}{x^2}\right|\,dx\leq\int_1^R\frac{1}{x^2}\,dx=\left[-\frac{1}{x}\right]_1^R=1-\frac{1}{R}.
$$

Since $\displaystyle\lim_{R\to\infty}\frac{\cos(R)}{R}=0$ and $\displaystyle\lim_{R\to\infty}\frac{1}{R}=0$ we conclude that $\displaystyle\int_1^{\infty}\frac{\sin(x)}{x}\,dx$ converges.

This shows that $\displaystyle\int_0^{\infty}\frac{\sin(x)}{x}\,dx$ is convergent.

Now let: $I(t)=\displaystyle\int_0^{\infty}e^{-xt}\frac{\sin(x)}{x}\,dx$. Then we have

\begin{align*}
I'(t)&=-\int_0^{\infty}e^{-xt}\sin(x)\,dx\\
&=e^{-xt}\cos(x)\bigg|_0^{\infty}-\int_0^{\infty}\cos(x)\,(-t)e^{-xt}\,dx\\
&=-1+t\int_0^{\infty}e^{-xt}\cos(x)\,dx\\
&=-1+te^{-xt}\sin(x)\bigg|_0^{\infty}-t\int_0^{\infty}\sin(x)\,(-t)e^{-xt}\,dx\\
&=-1+t^2\int_0^{\infty}e^{-xt}\sin(x)\,dx.
\end{align*}

This implies that $\displaystyle\int_0^{\infty}e^{-xt}\sin(x)\,dx=\frac{1}{1+t^2}$ and therefore $I'(t)=-\dfrac{1}{1+t^2}$. So

$$
I(t)=-\arctan(t)+C.
$$

Note that $0=\displaystyle\lim\limits_{t\to\infty}I(t)=-\frac{1}{2}\pi+C$, which implies that $C=\dfrac{1}{2}\pi$. We conclude that

$$
I(t)=-\arctan(t)+\frac{1}{2}\pi
$$

and finally that

$$
\int_0^{\infty}\frac{\sin(x)}{x}\,dx=I(0)=\frac{1}{2}\pi.
$$

::::::

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
:description: Use a comparison theorem to determine whether the integrals converge or diverge.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8786072a-eedf-4980-9dbe-fcfab66eb59a?id=78799
:label: Grasple:78799
:dropdown:
:description: Use a comparison theorem to determine whether the integrals converge or diverge.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fdb58ae4-7de8-4ae8-b6aa-0ad84d55b7a6?id=78801
:label: Grasple:78801
:dropdown:
:description: Use a comparison theorem to determine whether the integrals converge or diverge.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/156a7bde-6aa4-468c-b4ed-de7eca985aeb?id=78807
:label: Grasple:78807
:dropdown:
:description: Use a comparison theorem to determine whether the integrals converge or diverge.

::::
