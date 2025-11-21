# Improper integrals

In this section we cover

- Integrals with infinite limits
- Integrals over intervals that contain a point where the function is discontinuous (infinite or jump discontinuity)
- Combinations of the above
- Comparison theorem

Note: do not use the term "Type I/1" and "Type II/2" improper integrals.

We have defined an integral $\displaystyle\int_a^bf(x)\,dx$, where the integrand $f$ is *continuous* on the *closed* and *finite* interval $[a,b]$. Such a function is *bounded*, which implies that the integral is a finite number. Such integrals are called **proper integrals**.

Now we will extend the concept of integration to the following two cases:

(I): the interval of integration is infinite ($(-\infty,b]$, $[a,\infty)$ or $(-\infty,\infty)$).

(II): the integrand $f$ may be unbounded as $x$ approaches $a$ or $b$ or both.

Integrals satisfying (I) and/or (II) are called **improper integrals**. These kinds of integrals will be defined as a limit which may exist or not.

::::::{prf:Definition} Improper integrals with infinite interval of integration
:label: Def:Integration:ImproperIntegralInfiniteInterval
If $f$ is continuous on $[a,\infty)$, then

$$
\int_a^{\infty}f(x)\,dx:=\lim_{R\to\infty}\int_a^Rf(x)\,dx.
$$

If $f$ is continuous on $(-\infty,b]$, then

$$
\int_{-\infty}^bf(x)\,dx:=\lim_{R\to-\infty}\int_R^bf(x)\,dx.
$$

In either case, if the limit exists (is a finite number), the improper integral is called **convergent**. If the limit does not exist, the improper integral is called **divergent**.

If the limit is $\infty$ or $-\infty$, we say the improper integral **diverges to infinity** or **diverges to negative infinity**.

Furthermore, if $f$ is continuous on $\mathbb{R}$, then

$$
\int_{-\infty}^{\infty}f(x)\,dx:=\int_{-\infty}^cf(x)\,dx+\int_c^{\infty}f(x)\,dx
$$

for any $c\in\mathbb{R}$. The integral on the left converges if and only if both integrals on the right converge.
::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample1
Consider $\displaystyle\int_1^{\infty}\frac{dx}{x\sqrt{x}}$.
```{figure} Images/improper1.png
---
width: 50%
name: improper integral
align: center
---
The integral $\displaystyle\int_1^{\infty}\frac{dx}{x\sqrt{x}}$
```

$$
\int_1^{\infty}\frac{dx}{x\sqrt{x}}=\lim_{R\to\infty}\int_1^R\frac{dx}{x\sqrt{x}}=\lim_{R\to\infty}\bigg[-\frac{2}{\sqrt{x}}\bigg]_1^R=\lim_{R\to\infty}\left(2-\frac{2}{\sqrt{R}}\right)=2.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample2
Consider $\displaystyle\int_1^{\infty}\frac{dx}{\sqrt{x}}$.
```{figure} Images/improper2.png
---
width: 50%
name: improper integral
align: center
---
The integral $\displaystyle\int_1^{\infty}\frac{dx}{\sqrt{x}}$
```

$$
\int_1^{\infty}\frac{dx}{\sqrt{x}}=\lim_{R\to\infty}\int_1^R\frac{dx}{\sqrt{x}}=\lim_{R\to\infty}\bigg[2\sqrt{x}\bigg]_1^R=\lim_{R\to\infty}\left(2\sqrt{R}-2\right)=\infty.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample3
Consider $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$.
```{figure} Images/improper3.png
---
width: 50%
name: improper integral
align: center
---
The integral $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$
```

$$
\int_{-\infty}^{\infty}\frac{dx}{1+x^2}=\int_{-\infty}^0\frac{dx}{1+x^2}+\int_0^{\infty}\frac{dx}{1+x^2}.
$$

Now we have

$$
\begin{align*}
\int_0^{\infty}\frac{dx}{1+x^2}&=\lim_{R\to\infty}\int_0^R\frac{dx}{1+x^2}=\lim_{R\to\infty}\bigg[\arctan(x)\bigg]_0^R\\
&=\lim_{R\to\infty}\arctan(R)=\frac{1}{2}\pi
\end{align*}
$$

and

$$
\begin{align*}
\int_{-\infty}^0\frac{dx}{1+x^2}&=\lim_{R\to-\infty}\int_R^0\frac{dx}{1+x^2}=\lim_{R\to-\infty}\bigg[\arctan(x)\bigg]_R^0\\
&=\lim_{R\to-\infty}\left(-\arctan(R)\right)=\frac{1}{2}\pi.
\end{align*}
$$

Hence, we have

$$
\int_{-\infty}^{\infty}\frac{dx}{1+x^2}=\int_{-\infty}^0\frac{dx}{1+x^2}+\int_0^{\infty}\frac{dx}{1+x^2}=\frac{1}{2}\pi+\frac{1}{2}\pi=\pi.
$$

::::::

::::::{note}

```{figure} Images/cauchy.png
---
width: 50%
name: the Cauchy distribution
align: center
---
The Cauchy distribution $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}=\pi$
```
In probability and statistics this denotes the (total) **Cauchy distribution**, named after the French mathematician [Augustin-Louis Cauchy (1789-1857)](https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy).
::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsInfiniteIntervalExample4
Consider $\displaystyle\int_0^{\infty}\cos(x)\,dx$.
```{figure} Images/improper4.png
---
width: 50%
name: improper integral
align: center
---
The integral $\displaystyle\int_0^{\infty}\cos(x)\,dx$
```

$$\int_0^{\infty}\cos(x)\,dx=\lim_{R\to\infty}\int_0^R\cos(x)\,dx=\lim_{R\to\infty}\bigg[\sin(x)\bigg]_0^R=\lim_{R\to\infty}\sin(R).
$$

This limit does not exist and is not $\infty$ or $-\infty$. In this case we can only say that the integral diverges.
::::::

::::{exercise}
:label: Exc:Integration:ImproperIntegralsExercise1
Determine whether $\displaystyle\int\frac{dx}{x^2}$ is convergent or divergent. 
::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsExercise1`
:class: solution, dropdown

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

$$
\int_1^{\infty}\frac{dx}{x}=\lim_{R\to\infty}\int_1^R\frac{dx}{x}=\lim_{R\to\infty}\bigg[\ln(x)\bigg]_1^R=\lim_{R\to\infty}\ln(R)=\infty.
$$

So, $\displaystyle\int_1^{\infty}\frac{dx}{x}$ is divergent.
:::

::::::{prf:Definition} Improper integrals with discontinuous integrand
:label: Def:Integration:ImproperIntegralDiscontinuousIntegrand
If $f$ is continuous on $(a,b]$ and possibly unbounded near $a$, then

$$
\int_a^bf(x)\,dx=\lim_{c\downarrow a}\int_c^bf(x)\,dx.
$$

If $f$ is continuous on $[a,b)$ and possibly unbounded near $b$, then

$$
\int_a^bf(x)\,dx=\lim_{c\uparrow b}\int_a^cf(x)\,dx.
$$

::::::

::::::{note}
These improper integrals may converge, diverge, diverge to infinity, or diverge to negative infinity.
::::::

::::::{warning}
$$
\int_{-1}^1\frac{dx}{x^2}=-\frac{1}{x}\bigg|_{-1}^1=-1-1=-2
$$

is clearly wrong! Note that the integrand is positive on $[-1,1]$. The evaluation is incorrect because the integrand is not continuous at $x=0$. So, the fundamental theorem of calculus cannot be applied.
::::::

If the discontinuity of the integrand appears not at a boundary point of the interval of integration, we need to split up this interval such that the discontinuity is at a boundary point and then apply {prf:ref}`Def:Integration:ImproperIntegralDiscontinuousIntegrand`.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsDiscontinuousIntegrandExample1
```{figure} Images/improper5.png
---
width: 50%
name: improper integral
align: center
---
The integral $\displaystyle\int_{-1}^1\frac{dx}{x^2}$
```

$$
\int_{-1}^1\frac{dx}{x^2}=\int_{-1}^0\frac{dx}{x^2}+\int_0^1\frac{dx}{x^2}.
$$

Now we have

$$
\int_0^1\frac{dx}{x^2}=\lim_{c\downarrow0}\int_c^1\frac{dx}{x^2}=\lim_{c\downarrow0}\bigg[-\frac{1}{x}\bigg]_c^1=\lim_{c\downarrow0}\left(-1+\frac{1}{c}\right)=\infty
$$

and

$$
\int_{-1}^0\frac{dx}{x^2}=\lim_{c\uparrow0}\int_{-1}^c\frac{dx}{x^2}=\lim_{c\uparrow0}\bigg[-\frac{1}{x}\bigg]_{-1}^c=\lim_{c\uparrow0}\left(-\frac{1}{c}+1\right)=\infty.
$$

Hence, we have

$$
\int_{-1}^1\frac{dx}{x^2}=\int_{-1}^0\frac{dx}{x^2}+\int_0^1\frac{dx}{x^2}=\infty+\infty=\infty.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsDiscontinuousIntegrandExample2
Since $\dfrac{1}{x-1}$ is continuous for all $x\in\mathbb{R}$ except at $x=1$, we have
```{figure} Images/improper6.png
---
width: 50%
name: improper integral
align: center
---
The integral $\displaystyle\int_0^3\frac{dx}{x-1}$
```

$$
\int_0^3\frac{dx}{x-1}=\int_0^1\frac{dx}{x-1}+\int_1^3\frac{dx}{x-1}
$$

with

$$
\begin{align*}
\int_1^3\frac{dx}{x-1}&=\lim_{c\downarrow1}\int_c^3\frac{dx}{x-1}=\lim_{c\downarrow1}\bigg[\ln|x-1|\bigg]_c^3\\
&=\lim_{c\downarrow1}\left(\ln(2)-\ln|c-1|\right)=\infty
\end{align*}
$$

and

$$
\int_0^1\frac{dx}{x-1}=\lim_{c\uparrow1}\int_0^c\frac{dx}{x-1}=\lim_{c\uparrow1}\bigg[\ln|x-1|\bigg]_0^c=\lim_{c\uparrow1}\ln|c-1|=-\infty.
$$

::::::

::::::{warning}
It would be wrong to conclude that $\displaystyle\int_0^3\frac{dx}{x-1}=\infty-\infty=0$ and it is also incorrect to state that

$$
\int_0^3\frac{dx}{x-1}=\ln|x-1|\bigg|_0^3=\ln(2)-\ln(1)=\ln(2).
$$

Since the integrand is discontinuous at $x=1$ the fundamental theorem cannot be applied in this way.
::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsDiscontinuousIntegrandExample3
Consider $\displaystyle\int_0^1\ln(x)\,dx$. 
```{figure} Images/improper7.png
---
width: 50%
name: improper integral
align: center
---
The integral $\displaystyle\int_0^1\ln(x)\,dx$
```
Using integration by parts, we have

$$
\int\ln(x)\,dx=x\ln(x)-\int\ln x\cdot\frac{1}{x}\,dx=x\ln(x)-x+C.
$$

Hence, we have

$$
\int_0^1\ln(x)\,dx=\lim_{c\downarrow0}\bigg[x\ln(x)-x\bigg]_c^1=\lim_{c\downarrow0}\left(-1-c\ln(c)+c\right).
$$

Using l'Hospital's rule we obtain

$$
\lim_{c\downarrow0}c\ln(c)=\lim_{c\downarrow0}\frac{\ln(c)}{\frac{1}{c}}=\lim_{c\downarrow0}\frac{\frac{1}{c}}{-\frac{1}{c^2}}=\lim_{c\downarrow0}\left(-c\right)=0.
$$

We conclude that

$$
\int_0^1\ln(x)\,dx=\lim_{c\downarrow0}\left(-1-c\ln(c)+c\right)=-1-0+0=-1.
$$

::::::

::::{exercise}
:label: Exc:Integration:ImproperIntegralsExercise3
The integral $\displaystyle\int_0^{\infty}\frac{dx}{(1+x)\sqrt{x}}$ is improper both because of the infinite interval of integration and the discontinuous integrand at $x=0$. Evaluate the integral by splitting it into

$$
\int_0^{\infty}\frac{dx}{(1+x)\sqrt{x}}=\int_0^1\frac{dx}{(1+x)\sqrt{x}}+\int_1^{\infty}\frac{dx}{(1+x)\sqrt{x}}.
$$

::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsExercise3`
:class: solution, dropdown
Using the substitution $\sqrt{x}=t$ or $x=t^2$, we have $dx=2t\,dt$ and therefore

$$
\begin{align*}
\int\frac{dx}{(1+x)\sqrt{x}}&=\int\frac{2t\,dt}{(1+t^2)t}=\int\frac{2}{1+t^2}\,dt=2\arctan(t)+C\\
&=2\arctan\left(\sqrt{x}\right)+C.
\end{align*}
$$

Now we obtain

$$
\begin{align*}
\int_0^1\frac{dx}{(1+x)\sqrt{x}}&=\lim_{c\downarrow0}\int_c^1\frac{dx}{(1+x)\sqrt{x}}=\lim_{c\downarrow0}\bigg[2\arctan\left(\sqrt{x}\right)\bigg]_c^1\\
&=2\arctan(1)=\frac{1}{2}\pi
\end{align*}
$$

and

$$
\begin{align*}
\int_1^{\infty}\frac{dx}{(1+x)\sqrt{x}}&=\lim_{R\to\infty}\int_1^R\frac{dx}{(1+x)\sqrt{x}}=\lim_{R\to\infty}\bigg[2\arctan\left(\sqrt{x}\right)\bigg]_1^R\\
&=\pi-\frac{1}{2}\pi=\frac{1}{2}\pi.
\end{align*}
$$

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
Use the substitution $x=\dfrac{1}{t}$ and therefore $dx=-\dfrac{dt}{t^2}$ to find that

$$
\int_1^{\infty}\frac{\ln(x)}{1+x^2}\,dx=-\int_1^0\frac{\ln\left(\frac{1}{t}\right)}{1+\dfrac{1}{t^2}}\cdot\frac{dt}{t^2}=\int_0^1\frac{-\ln(t)}{t^2+1}\,dt=-\int_0^1\frac{\ln(t)}{1+t^2}\,dt.
$$

We conclude that $\displaystyle\int_0^{\infty}\frac{\ln(x)}{1+x^2}\,dx=0$.
:::

::::::{note}
Here we showed that $\displaystyle\int_0^1\frac{\ln(x)}{1+x^2}\,dx=\int_1^{\infty}\frac{\ln(x)}{1+x^2}\,dx$ without evaluating the integrals. Later we will see that the value is equal to *Catalan's constant*.
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
(a) For $k=0$ we obtain: $\displaystyle\int_0^{\infty}\frac{dx}{(1+x^2)(1+x^0)}=\frac{1}{2}\int_0^{\infty}\frac{dx}{1+x^2}=\frac{1}{2}\arctan(x)\bigg|_0^{\infty}=\frac{1}{4}\pi$.

(b) For $k\in\{1,2,3,\ldots\}$ we use the substitution $x=\dfrac{1}{t}$ and therefore $dx=-\dfrac{dt}{t^2}$ to find that

$$
\begin{align*}
\int_1^{\infty}\frac{dx}{(1+x^2)(1+x^k)}&=\int_1^0\frac{1}{(1+t^{-2})(1+t^{-k})}\left(-\frac{1}{t^2}\right)\,dt\\
&=\int_0^1\frac{dt}{(t^2+1)(1+t^{-k})}.
\end{align*}
$$

This implies that

$$
\begin{align*}
\int_0^{\infty}\frac{dx}{(1+x^2)(1+x^k)}&=\int_0^1\frac{dx}{(1+x^2)(1+x^k)}+\int_0^1\frac{dx}{(1+x^2)(1+x^{-k})}\\
&=\int_0^1\frac{1}{1+x^2}\left(\frac{1}{1+x^k}+\frac{1}{1+x^{-k}}\right)\,dx\\
&=\int_0^1\frac{1}{1+x^2}\left(\frac{1}{1+x^k}+\frac{x^k}{x^k+1}\right)\,dx\\
&=\int_0^1\frac{1}{1+x^2}\cdot\frac{1+x^k}{1+x^k}\,dx=\int_0^1\frac{dx}{1+x^2}\\
&=\arctan(x)\bigg|_0^1=\frac{1}{4}\pi.
\end{align*}
$$

(c) Similarly, we consider

$$
\int_0^{\infty}\frac{dx}{(1+x^2)(1+x^{-k})}=\int_0^1\frac{dx}{(1+x^2)(1+x^{-k})}+\int_1^{\infty}\frac{dx}{(1+x^2)(1+x^{-k})}
$$

for $k\in\{1,2,3,\dots\}$ and use the substitution $x=\dfrac{1}{t}$ again to find that

$$
\begin{align*}
\int_1^{\infty}\frac{dx}{(1+x^2)(1+x^{-k})}&=\int_1^0\frac{1}{(1+t^{-2})(1+t^k)}\left(-\frac{1}{t^2}\right)\,dt\\
&=\int_0^1\frac{dt}{(t^2+1)(1+t^k)}.
\end{align*}
$$

Hence, for $k\in\{1,2,3,\ldots\}$ we have

$$
\begin{align*}
\int_0^{\infty}\frac{dx}{(1+x^2)(1+x^{-k})}&=\int_0^1\frac{dx}{(1+x^2)(1+x^{-k})}+\int_0^1\frac{dx}{(1+x^2)(1+x^k)}\\
&=\int_0^1\frac{1}{1+x^2}\left(\frac{1}{1+x^{-k}}+\frac{1}{1+x^k}\right)\,dx\\
&=\int_0^1\frac{1}{1+x^2}\left(\frac{x^k}{x^k+1}+\frac{1}{1+x^k}\right)\,dx\\
&=\int_0^1\frac{1}{1+x^2}\cdot\frac{x^k+1}{x^k+1}\,dx=\int_0^1\frac{dx}{1+x^2}\\
&=\arctan(x)\bigg|_0^1=\frac{1}{4}\pi.
\end{align*}
$$

:::

::::::{prf:Theorem} $p$-integrals
:label: Thm:Integration:ImproperIntegralsPintegrals
For $0<a<\infty$ we have

(a) $\displaystyle\int_a^{\infty}\frac{dx}{x^p}=\begin{cases}\dfrac{a^{1-p}}{p-1}, &p>1\\\infty, &p\leq1.\end{cases}$

(b) $\displaystyle\int_0^a\frac{dx}{x^p}=\begin{cases}\dfrac{a^{1-p}}{1-p}, &p<1\\\infty, &p\geq1.\end{cases}$
::::::

::::::{prf:Proof}

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

Sometimes integrals are not easy to evaluate. However, in many cases evaluation is not necessary as long as we can find out whether the integral is convergent or divergent. In case of convergence we might able to find a lower and upper bound for the integral. The following theorem might be helpful.

::::::{prf:Theorem} A comparison theorem for improper integrals
:label: Thm:Integration:ImproperIntegralsComparison
If $f$ and $g$ are continuous on $(a,b)$ with $-\infty\leq a<b\leq\infty$ and $0\leq f(x)\leq g(x)$, then:

(a) If $\displaystyle\int_a^bg(x)\,dx$ is convergent, then $\displaystyle\int_a^bf(x)\,dx$ is convergent.

(b) If $\displaystyle\int_a^bf(x)\,dx$ is divergent, then $\displaystyle\int_a^bg(x)\,dx$ is divergent.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsComparisonExample1
Without evaluating the integral, determine whether $\displaystyle\int_0^{\infty}\frac{x}{1+x^3}\,dx$ is convergent or divergent.

First, let $\displaystyle\int_0^{\infty}\frac{x}{1+x^3}\,dx=\int_0^1\frac{x}{1+x^3}\,dx+\int_1^{\infty}\frac{x}{1+x^3}\,dx$.

The first integral involves a continuous function on a finite interval, which is convergent. 

Since $0<\dfrac{x}{1+x^3}<\dfrac{1}{1+x^3}<1$ we have

$$
0<\int_0^1\frac{x}{1+x^3}\,dx<1.
$$

Note that $0\leq\dfrac{x}{1+x^3}\leq\dfrac{1}{x^2}$ for $x\geq1$ and since

$$
\int_1^{\infty}\frac{dx}{x^2}=\bigg[-\frac{1}{x}\bigg]_1^{\infty}=1,
$$

we conclude that the second integral is convergent as well and that 

$$
0<\int_1^{\infty}\frac{x}{1+x^3}\,dx<1.
$$

We conclude that $\displaystyle\int_0^{\infty}\frac{x}{1+x^3}\,dx$ is convergent and that

$$
0<\int_0^{\infty}\frac{x}{1+x^3}\,dx<2.
$$

::::::

::::::{note}
We will often use the short notation $\displaystyle\int_1^{\infty}\frac{dx}{x^2}=\bigg[-\frac{1}{x}\bigg]_1^{\infty}=1$ instead of

$$
\int_1^{\infty}\frac{dx}{x^2}=\lim_{R\to\infty}\bigg[-\frac{1}{x}\bigg]_1^R=\lim_{R\to\infty}\left(1-\frac{1}{R}\right)=1.
$$

::::::

::::{exercise}
:label: Exc:Integration:ImproperIntegralsComparisonExercise1
Evaluate $\displaystyle\int_0^{\infty}\frac{x}{1+x^3}\,dx$ exactly. 
::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsComparisonExercise1`
:class: solution, dropdown
Note that $1+x^3=(1+x)(1-x+x^2)$ and therefore

$$
\begin{align*}
\frac{x}{1+x^3}&=\frac{x}{(1+x)(1-x+x^2)}=\frac{A}{1+x}+\frac{Bx+C}{1-x+x^2}\\
&=\frac{A(1-x+x^2)+Bx(1+x)+C(1+x)}{(1+x)(1-x+x^2)}.
\end{align*}
$$

Comparing the numerators, we obtain

$$
\begin{align*}
&x=(A+B)x^2+(-A+B+C)x+A+C\\
&\quad\Longrightarrow\quad A=-\frac{1}{3}\quad\text{and}\quad B=C=\frac{1}{3}.
\end{align*}
$$

Hence, we have

$$
\begin{align*}
\int\frac{x}{1+x^3}\,dx&=\frac{1}{3}\int\left(-\frac{1}{1+x}+\frac{x+1}{x^2-x+1}\right)\,dx\\
&=\frac{1}{3}\int\left(-\frac{1}{1+x}+\frac{1}{2}\frac{2x-1}{x^2-x+1}+\frac{3}{2}\frac{1}{x^2-x+1}\right)\,dx.
\end{align*}
$$

Now we have

$$
\int\left(-\frac{1}{1+x}+\frac{1}{2}\frac{2x-1}{x^2-x+1}\right)\,dx=\ln\left(\frac{\sqrt{x^2-x+1}}{1+x}\right)+C
$$

and

$$
\begin{align*}
\int\frac{dx}{x^2-x+1}&=\int\frac{dx}{(x-\frac{1}{2})^2+\frac{3}{4}}=\frac{4}{3}\int\frac{dx}{\left(\frac{2x-1}{\sqrt{3}}\right)^2+1}\\
&=\frac{2}{\sqrt{3}}\arctan\left(\frac{2x-1}{\sqrt{3}}\right)+C
\end{align*}
$$

Since $\displaystyle\lim\limits_{x\to\infty}\frac{\sqrt{x^2-x+1}}{1+x}=1$, we obtain using $\displaystyle\lim_{x\to\infty}\arctan(x)=\tfrac{1}{2}\pi$ and $\arctan\left(\frac{1}{\sqrt{3}}\right)=\frac{1}{6}\pi$

$$
\begin{align*}
\int_0^{\infty}\frac{x}{1+x^3}\,dx&=\bigg[\frac{1}{3}\ln\left(\frac{\sqrt{x^2-x+1}}{1+x}\right)+\frac{1}{\sqrt{3}}\arctan\left(\frac{2x-1}{\sqrt{3}}\right)\bigg]_0^{\infty}\\
&=\frac{1}{\sqrt{3}}\left(\frac{1}{2}\pi+\frac{1}{6}\pi\right)=\frac{2}{3}\pi\sqrt{3}\approx1.2092.
\end{align*}
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
Later we will see that $\displaystyle\int_0^{\infty}e^{-x^2}\,dx=\tfrac{1}{2}\sqrt{\pi}\approx0.88623$.

By symmetry, we also have: $\displaystyle\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt{\pi}$, which is called the **Gaussian integral**, named after the German mathematician [Johann Carl Friedrich Gauss (1777-1855)](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss).
```{figure} Images/normal.png
---
width: 50%
name: the normal distribution
align: center
---
The normal distribution $\displaystyle\int_{-\infty}^{\infty}e^{-x^2}=\sqrt{\pi}$
```
In probability and statistics this is known as the (standard) **normal distribution** or **Gaussian distribution**. The curve is sometimes referred to as the **bell curve**.
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

::::{exercise}
:label: Exc:Integration:ImproperIntegralsComparisonExercise1
Determine whether the integral $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{\sqrt{x}}\,dx$ is convergent or divergent.
::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsComparisonExercise1`
:class: solution, dropdown
Note that for all $x\geq1$ we have $\frac{1}{4}\pi\leq\arctan(x)<\frac{1}{2}\pi$. Hence we have
$\displaystyle\frac{\arctan(x)}{\sqrt{x}}\geq\frac{1}{4}\pi\cdot\frac{1}{\sqrt{x}}$ and
$$
\int_1^{\infty}\frac{dx}{\sqrt{x}}=2\sqrt{x}\bigg|_1^{\infty}=\infty.
$$

We conclude that $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{\sqrt{x}}\,dx$ is divergent.
:::

::::{exercise}
:label: Exc:Integration:ImproperIntegralsComparisonExercise2
Determine whether the integral $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{x\sqrt{x}}\,dx$ is convergent or divergent.
::::

:::{admonition} Solution of {numref}`Exc:Integration:ImproperIntegralsComparisonExercise2`
:class: solution, dropdown
Note that for all $x\geq1$ we have $\frac{1}{4}\pi\leq\arctan(x)<\frac{1}{2}\pi$. Further we have

$$
\int_1^{\infty}\frac{dx}{x\sqrt{x}}=-\frac{2}{\sqrt{x}}\bigg|_1^{\infty}=2.
$$

We conclude that $\displaystyle\int_1^{\infty}\frac{\arctan(x)}{x\sqrt{x}}\,dx$ is convergent and that

$$
\frac{1}{2}\pi\leq\int_1^{\infty}\frac{\arctan(x)}{x\sqrt{x}}<\pi.
$$

:::

## The gamma function

The **gamma function** $\Gamma(x)$ is defined by the improper integral

$$
\Gamma(x):=\int_0^{\infty}t^{x-1}e^{-t}\,dt,\quad x>0.
$$

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

$$
\begin{align*}
\Gamma(x+1)&=\int_0^{\infty}t^xe^{-t}\,dt=-\int_0^{\infty}t^x\,de^{-t}=-t^xe^{-t}\bigg|_0^{\infty}+\int_0^{\infty}e^{-t}\,dt^x\\
&=0+x\int_0^{\infty}t^{x-1}e^{-t}\,dt=x\Gamma(x).
\end{align*}
$$

This implies that $\Gamma(n+1)=n!$ for $n=0,1,2,\ldots$. So, the gamma function can be seen as a generalization of the factorial.

Furthermore, using the substitution $t=x^2$ we have

$$
\Gamma(\tfrac{1}{2})=\int_0^{\infty}t^{-\frac{1}{2}}e^{-t}\,dt=\int_0^{\infty}x^{-1}e^{-x^2}\cdot2x\,dx=2\int_0^{\infty}e^{-x^2}\,dx.
$$
 
Later we will prove that $\displaystyle\int_0^{\infty}e^{-x^2}\,dx=\tfrac{1}{2}\sqrt{\pi}$. This implies that $\Gamma(\frac{1}{2})=\sqrt{\pi}$.

## The Feynman method

Sometimes an integral is easier to evaluate if we modify the integrand using a parameter such that a specific value of this parameter leads to the original integral. This trick was developed by the American theoretical physicist [Richard Phillips Feynman (1918-1988)](https://en.wikipedia.org/wiki/Richard_Feynman) and is based on the following theorem.

::::::{prf:Theorem} The Feyman method
:label: Thm:Integration:ImproperIntegralsFeynmanMethod
If $f(x,t)$ and $\displaystyle\frac{\partial}{\partial t}f(x,t)$ are both continuous for all $x\in[a,b]$, then

$$
\frac{d}{dt}\int_a^bf(x,t)\,dx=\int_a^b\frac{\partial}{\partial t}f(x,t)\,dx.
$$

::::::

::::::{note}
The notation $\dfrac{\partial}{\partial t}$ denotes the derivative with respect to $t$ and will be explained in the section on partial derivatives.
::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsFeynmanExample1
Consider the improper integral $\displaystyle\int_0^1\frac{x-1}{\ln(x)}\,dx$, which is extremely difficult to evaluate.

Define $I(t)=\displaystyle\int_0^1\frac{x^t-1}{\ln(x)}\,dx$ for $t\geq0$, then we have $I(0)=0$ and

$$
I'(t)=\int_0^1\frac{\partial}{\partial t}\frac{x^t-1}{\ln(x)}\,dx=\int_0^1x^t\,dx=\frac{x^{t+1}}{t+1}\bigg|_0^1=\frac{1}{t+1}.
$$

This implies that $I(t)=\ln|t+1|+C$ with $C=I(0)=0$. Hence: $\displaystyle I(t)=\int_0^1\frac{x^t-1}{\ln(x)}\,dx=\ln(t+1)$ for $t\geq0$. We conclude that

$$
\int_0^1\frac{x-1}{\ln(x)}\,dx=\ln(2).
$$

Similarly, we find that $\displaystyle\int_0^1\frac{x^2-1}{\ln(x)}\,dx=\ln(3)$ and $\displaystyle\int_0^1\frac{\sqrt{x}-1}{\ln(x)}\,dx=\ln\left(\tfrac{3}{2}\right)$, for instance.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsFeynmanExample2
Consider the integral $\displaystyle\int_0^1\frac{\sin(\ln(x))}{\ln(x)}\,dx$.

Let $I(t)=\displaystyle\int_0^1\frac{\sin(t\ln(x))}{\ln(x)}\,dx$, then we have $I(0)=0$ and using the substitution $\ln(x)=y$ or $x=e^y$

$$
I'(t)=\int_0^1\cos(t\ln(x))\,dx=\int_{-\infty}^0\cos(ty)e^y\,dy=\int_0^{\infty}e^{-y}\cos(ty)\,dy.
$$

Now we have using integration by parts

$$
\begin{align*}
\int_0^{\infty}e^{-y}\cos(ty)\,dy&=-e^{-y}\cos(ty)\bigg|_0^{\infty}-t\int_0^{\infty}e^{-y}\sin(ty)\,dy\\
&=1+te^{-y}\sin(ty)\bigg|_0^{\infty}-t^2\int_0^{\infty}e^{-y}\cos(ty)\,dy\\
&=1-t^2\int_0^{\infty}e^{-y}\cos(ty)\,dy.
\end{align*}
$$

Hence: $I'(t)=\displaystyle\int_0^{\infty}e^{-y}\cos(ty)\,dy=\frac{1}{1+t^2}$. Since $I(0)=0$ this implies that $I(t)=\arctan(t)$.

Hence: $\displaystyle\int_0^1\frac{\sin(\ln(x))}{\ln(x)}\,dx=I(1)=\arctan(1)=\tfrac{1}{4}\pi$.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsFeynmanExample3
Consider the integral $I(t)=\displaystyle\int_0^{\infty}\frac{e^{-\alpha x}\sin(xt)}{x}\,dx$ for $\alpha>0$ and $t\geq0$. Since $\displaystyle\lim\limits_{x\downarrow0}\frac{\sin(xt)}{x}=t$, the integral is convergent. Then we have $I(0)=0$ and using integration by parts

$$
\begin{align*}
I'(t)&=\int_0^{\infty}e^{-\alpha x}\cos(xt)\,dx\\
&=\left[\frac{t}{\alpha^2+t^2}e^{-\alpha x}\sin(xt)-\frac{\alpha}{\alpha^2+t^2}e^{-\alpha x}\cos(xt)\right]_0^{\infty}\\
&=\frac{\alpha}{\alpha^2+t^2}.
\end{align*}
$$

This implies that $I(t)=\displaystyle\arctan\left(\frac{t}{\alpha}\right)$.

For instance, this implies that $\displaystyle\int_0^{\infty}\frac{e^{-\alpha x}\sin(\alpha x)}{x}\,dx=\arctan(1)=\tfrac{1}{4}\pi$ for all $\alpha>0$. Furthermore, we have

$$
\int_0^{\infty}\frac{e^{-x\sqrt{3}}\sin(x)}{x}\,dx=\arctan\left(\frac{1}{\sqrt{3}}\right)=\frac{1}{6}\pi
$$

and

$$
\int_0^{\infty}\frac{e^{-x}\sin(x\sqrt{3})}{x}\,dx=\arctan(\sqrt{3})=\frac{1}{3}\pi.
$$

::::::

::::::{prf:Theorem} The Dirichlet integral
:label: Thm:Integration:ImproperIntegralsDirichletIntegral
$\displaystyle\int_0^{\infty}\frac{\sin(x)}{x}\,dx=\frac{1}{2}\pi$.

This integral is named after the German mathematician [Johann Peter Gustav Lejeune Dirichlet (1805-1859)](https://en.wikipedia.org/wiki/Peter_Gustav_Lejeune_Dirichlet).
::::::

::::::{prf:Proof}
Since $\displaystyle\lim\limits_{x\downarrow0}\frac{\sin(x)}{x}=1$, the integrand is continuous and the integral is convergent. 

Now let: $I(t)=\displaystyle\int_0^{\infty}e^{-xt}\frac{\sin(x)}{x}\,dx$. Then we have

$$
\begin{align*}
I'(t)&=-\int_0^{\infty}e^{-xt}\sin(x)\,dx=\int_0^{\infty}e^{-xt}\,d\cos(x)\\
&=e^{-xt}\cos(x)\bigg|_0^{\infty}-\int_0^{\infty}\cos(x)\,de^{-xt}\\
&=-1+t\int_0^{\infty}e^{-xt}\cos(x)\,dx=-1+t\int_0^{\infty}e^{-xt}\,d\sin(x)\\
&=-1+te^{-xt}\sin(x)\bigg|_0^{\infty}-t\int_0^{\infty}\sin(x)\,de^{-xt}\\
&=-1+t^2\int_0^{\infty}e^{-xt}\sin(x)\,dt.
\end{align*}
$$

This implies that $\displaystyle\int_0^{\infty}e^{-xt}\sin(x)\,dx=\frac{1}{1+t^2}$ and therefore $I'(t)=-\dfrac{1}{1+t^2}$. Hence: $I(t)=-\arctan(t)+C$. Note that $0=\displaystyle\lim\limits_{t\to\infty}I(t)=-\tfrac{1}{2}\pi+C$, which implies that $C=\tfrac{1}{2}\pi$. We conclude that: $I(t)=-\arctan(t)+\frac{1}{2}\pi$. Hence: $\displaystyle\int_0^{\infty}\frac{\sin(x)}{x}\,dx=I(0)=\tfrac{1}{2}\pi$.

::::::

## (Grasple) exercises
