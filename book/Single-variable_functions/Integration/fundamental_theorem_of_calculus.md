(Sec:Integration:FundamentalTheorem)=

# Fundamental theorem of calculus

## Introduction

In this section we explain the relation between definite and indefinite integrals. The connection is given by the *fundamental theorem of calculus*.

In {numref}`Sec:Integration:IndefiniteIntegrals` we introduced the concept of the indefinite integral $\displaystyle \int f(x)\,dx$ of a function $f$ on an open interval $I$ and made a relation between indefinite integrals and derivatives.

Such a relation als exists between definite integrals and derivatives, which is the subject of the fundamental theorem of calculus. This theorem consists of two parts.

## Part 1 of the fundamental theorem of calculus

Without further ado we state the first part of the fundamental theorem of calculus:

::::::{prf:Theorem} The fundamental theorem of calculus, part 1
:label: Thm:Integration:FundamentalTheoremPart1
If $f$ is continuous on the interval $[a,b]$, then the function $g(x)$ defined by

$$
g(x)=\int_a^xf(t)\,dt,\quad a\leq x\leq b
$$

is continuous on $[a,b]$ and differentiable on $(a,b)$, and $g'(x)=f(x)$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Integration:FundamentalTheoremPart1`
:class: tudproof
:label: Prf:Integration:FundamentalTheoremPart1

Using the definition of the derivative, we obtain

\begin{align*}
g'(x)&=\lim_{h\to 0}\frac{g(x+h)-g(x)}{h}\\
&=\lim_{h\to 0}\frac{1}{h}\left(\int_a^{x+h}f(t)\,dt-\int_a^xf(t)\,dt\right)\\
&=\lim_{h\to 0}\frac{1}{h}\left(\int_a^{x}f(t)\,dt+\int_x^{x+h}f(t)\,dt-\int_a^xf(t)\,dt\right)\\
&=\lim_{h\to 0}\frac{1}{h}\int_x^{x+h}f(t)\,dt.
\end{align*}
Because $f$ is continuous on $[a,b]$, we can use the third comparison test from {prf:ref}`Th:Integration:DefiniteComparison` to conclude that there exists values $c$ and $d$ between $x$ and $x+h$ such that $f(d)\leq f(x)\leq f(c)$ for all $x$ between $x$ and $x+h$ and that we have

$$
\int_x^{x+h}f(t)\,dt\geq\int_x^{x+h}f(d)\,dt=f(d)\cdot ((x+h)-x)=hf(d).
$$

and

$$
\int_x^{x+h}f(t)\,dt\leq\int_x^{x+h}f(c)\,dt=f(c)\cdot ((x+h)-x)=hf(c).
$$

Note that if $h\rightarrow0$, then both $c$ and $d$ approach $x$ and $f(d)$ and $f(c)$ approach $f(x)$. Hence, we can use {prf:ref}`Theorem:LimitAtPoint:Squeezetheorem` to conclude that because

$$
f(d)\leq \frac{1}{h}\int_x^{x+h}f(t)\,dt\leq f(c),
$$

we have

$$
g'(x)=\lim_{h\to 0}\frac{1}{h}\int_x^{x+h}f(t)\,dt = f(x).
$$

This proves that $g$ is differentiable on $(a,b)$ and that $g'(x)=f(x)$.

Because $f$ is continuous on $[a,b]$, it follows from {prf:ref}`Def:Integration:Integrable` that $g(b)$ exists and $g(a)=0$. Therefore, $g$ is also continuous on $[a,b]$.

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart1Example1

We take $g(x)=\displaystyle\int_0^xe^{t^2}\,dt$ and want to determine $g'(x)$.

We need not to evaluate the integral, which would be impossible. However, application of the fundamental theorem of calculus leads to the immediate answer 

$$
g'(x)=\frac{d}{dx}\int_0^xe^{t^2}\,dt=e^{x^2}.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart1Example2
Let us assume $g(x)=\displaystyle\int_0^{\sqrt{x}}\cos(t^2)\,dt$ for $x>0$ and determine $g'(x)$.

If we would have had $h(u)=\displaystyle\int_0^{u}\cos(t^2)\,dt$, we would have had $h'(u)=\cos(u^2)$ by the fundamental theorem of calculus.

However, now we need to also apply the chain rule:

$$
\frac{d}{dx}\int_0^{\sqrt{x}}\cos(t^2)\,dt=\cos\left((\sqrt{x})^2\right)\cdot\frac{d}{dx}(\sqrt{x})=\cos(x)\cdot\frac{1}{2\sqrt{x}}=\frac{\cos(x)}{2\sqrt{x}}.
$$

::::::

Before we do a final example for part 1 of the fundamental theorem of calculus, we note that the theorem can also be used if the upper limit of integration is $x$:

::::{prf:theorem}
:label: Thm:Integration:FundamentalTheoremPart1LowerLimit

If $f$ is continuous on the interval $[a,b]$, then the function $h(x)$ defined by

$$
h(x)=\int_x^bf(t)\,dt,\quad a\leq x\leq b
$$

is continuous on $[a,b]$ and differentiable on $(a,b)$, and $h'(x)=-f(x)$.
::::

::::{admonition} Proof of {prf:ref}`Thm:Integration:FundamentalTheoremPart1LowerLimit`
:class: tudproof
:label: Prf:Integration:FundamentalTheoremPart1LowerLimit

Using the definition of the definite integral we have:

$$
\int_a^bf(t)\,dt=\int_a^xf(t)\,dt+\int_x^bf(t)\,dt = g(x)+h(x),
$$

where $g(x)$ is the function defined in {prf:ref}`Thm:Integration:FundamentalTheoremPart1`. Differentiating both sides gives:

$$
0 = g'(x) + h'(x) = f(x) + h'(x),
$$

which implies that $h'(x) = -f(x)$.

Using the same arguments as in the proof of {prf:ref}`Thm:Integration:FundamentalTheoremPart1`, we can also show that $h$ is continuous on $[a,b]$ and differentiable on $(a,b)$.

::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart1Example3
We want to determine $\displaystyle\frac{d}{dx}\int_x^{x^2}\ln(1+t^2)\,dt$.

Because both limits of integration depend on $x$, we first rewrite the integral as the sum of two integrals with one constant limit:

$$
\int_x^{x^2}\ln(1+t^2)\,dt=\int_x^0\ln(1+t^2)\,dt+\int_0^{x^2}\ln(1+t^2)\,dt.
$$

Note that this even works if $x^2<x$ and if $x>0$. Now we can differentiate both integrals separately using the fundamental theorem of calculus and the chain rule:

\begin{align*}
\frac{d}{dx}\int_x^{x^2}\ln(1+t^2)\,dt&=\frac{d}{dx}\left(\int_x^0\ln(1+t^2)\,dt+\int_0^{x^2}\ln(1+t^2)\,dt\right)\\
&=\frac{d}{dx}\int_x^0\ln(1+t^2)\,dt+\frac{d}{dx}\int_0^{x^2}\ln(1+t^2)\,dt\\
&=-\ln(1+x^2)\cdot\frac{d}{dx}(x)+\ln\left(1+\left(x^2\right)^2\right)\cdot\frac{d}{dx}(x^2)\\
&=-\ln(1+x^2)+2x\ln(1+x^4).
\end{align*}

::::::

## Part 2 of the fundamental theorem of calculus

Now we have finished the first part of the fundamental theorem of calculus, we can state the second part, which finally gives as a way to really calculate definite integrals:

::::::{prf:Theorem} The fundamental theorem of calculus, part 2
:label: Thm:Integration:FundamentalTheoremPart2
If $f$ is continuous on the interval $[a,b]$, then

$$
\int_a^bf(x)\,dx=F(b)-F(a),
$$

where $F$ is any antiderivative of $f$, that is, a function such that $F'=f$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Integration:FundamentalTheoremPart2`
:class: tudproof
:label: Prf:Integration:FundamentalTheoremPart2

Let $g(x)=\displaystyle\int_a^xf(t)\,dt$. Then {prf:ref}`Thm:Integration:FundamentalTheoremPart1` implies that $g'(x)=f(x)$. Hence, $g$ is an antiderivative of $f$.

So, if $F$ is any antiderivative of $f$ we have:

$$
F(x)=g(x)+C\quad\text{for}\quad a<x<b.
$$

However, since $F$ and $g$ are both continuous on $[a,b]$ we conclude that $F(x)=g(x)+C$ for all $x$ in $[a,b]$.

First note that

$$
g(a) = \int_a^af(t)\,dt = 0.
$$

This means that:

\begin{align*}
\int_a^bf(x)\,dx &= g(b) \\
&= g(b)-g(a) \\
&= \left(F(b)+C\right) - \left(F(a)+C\right) \\
&= F(b)-F(a),
\end{align*}

which concludes the proof.

::::::

::::::{prf:Notation}
:label: Not:Integration:FundamentalTheoremPart2Notation

During evaluations of integrals we often use the notation

$$
\int_a^bf(x)\,dx=\bigg[F(x)\bigg]_a^b=F(b)-F(a)
$$

or

$$
\int_a^bf(x)\,dx=F(x)\bigg|_a^b=F(b)-F(a).
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart2Example1

We want to evaluate the integral $\displaystyle\int_0^{\pi}\sin(x)\,dx$.

```{figure} Images/sine_area.png
---
width: 50%
name: Fig:Integration:SineArea
align: center
---
The function $\sin(x)$ on the interval $[0,\pi]$.
```

This is the same as calculating the area under one positive arc of the sine function, which is shown in the figure above, and this area is:

$$
\int_0^{\pi}\sin(x)\,dx=-\cos(x)\bigg|_0^{\pi}=-\cos(\pi)+\cos(0)=-(-1)+1=2.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart2Example2

Another example is the evaluation of the integral $\displaystyle\int_1^e\frac{1}{x}\,dx$:

$$
\int_1^e\frac{1}{x}\,dx=\ln(x)\bigg|_1^e=\ln(e)-\ln(1)=1-0=1.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart2Example3

Integration of the function $\displaystyle f(x)=\frac{1}{1+x^2}$ from $0$ to $\frac{1}{4}\pi$ gives:

$$
\int_0^{\frac{1}{4}\pi}\frac{1}{1+x^2}\,dx=\bigg[\arctan(x)\bigg]_0^{\frac{1}{4}\pi}=\arctan(\tfrac{1}{4}\pi)-\arctan(0)=1-0=1.
$$

::::::

So, in order to evaluate a definite integral we just need to find any antiderivative of the integrand. However, it is not always easy to find such an antiderivative. In the next sections we will cover some methods which can be used to evaluate integrals of certain types.

## Applications of the fundamental theorem of calculus

However, in some applications functions appear, which are defined in terms of an integral that cannot be evaluated. Even though the integrand is continuous and an antiderivative exists, it is sometimes impossible to write this in terms of standard functions. In the examples below we deal with some of these functions. Although the integral cannot be evaluated, the fundamental theorem of calculus can be used to find properties of the function.

::::::{prf:Example} Error function
:label: Ex:Integration:FundamentalTheoremErrorFunction

In probability and statistics the **error function**

$$
\erf(x)=\frac{2}{\sqrt{\pi}}\int_0^xe^{-t^2}\,dt
$$

with $x\geq0$ appears. Although it turns out that it is difficult to evaluate this integral, we have by the fundamental theorem of calculus:

$$
\erf'(x)=\frac{2}{\sqrt{\pi}}e^{-x^2}>0,
$$

which implies that the function is increasing. Furthermore, $\erf(0)=0$ and $\lim\limits_{x\to\infty}\erf'(x)=0$.

Later we will see that $\lim\limits_{x\to\infty}\erf(x)=1$. The graph of $\erf(x)$ for $x\geq0$ is given below:

```{figure} Images/error_function.png
---
width: 50%
name: Fig:Integration:ErrorFunction
align: center
---
Graph of $\erf(x)$ for $x\geq0$.
```
::::::

::::::{prf:Example} Fresnel integrals
:label: Ex:Integration:FundamentalTheoremFresnelIntegrals

In optics the **Fresnel integrals**

$$
C(x)=\int_0^x\cos\left(\frac{1}{2}\pi t^2\right)\,dt
$$

and

$$
S(x)=\int_0^x\sin\left(\frac{1}{2}\pi t^2\right)\,dt
$$

for $x\geq0$ appear, which are also difficult to evaluate. These integrals are named after the French civil engineer and physicist [Augustin Jean Fresnel (1788-1827)](https://en.wikipedia.org/wiki/Augustin-Jean_Fresnel).

However we have $C'(x)=\displaystyle\cos\left(\frac{1}{2}\pi x^2\right)$ and $S'(x)=\displaystyle\sin\left(\frac{1}{2}\pi x^2\right)$ by the fundamental theorem of calculus.

So, for instance, we have: 

$$
C'(x)=0\quad\Longleftrightarrow\quad\frac{1}{2}\pi x^2=\frac{(2k+1)\pi}{2}\quad\text{with}\quad k=0,1,2,\ldots
$$

Hence, $C'(x)=0$ for $x=\sqrt{2k+1}$ with $k=0,1,2,\ldots$

Similarly, we have: 

$$
S'(x)=0\quad\Longleftrightarrow\quad\frac{1}{2}\pi x^2=k\pi\quad\text{with}\quad k=0,1,2,\ldots
$$

Hence, $S'(x)=0$ for $x=\sqrt{2k}$ with $k=0,1,2,\ldots$

The graphs of $C(x)$ and $S(x)$ for $0\leq x\leq4$ are given below:

```{figure} Images/fresnel.png
---
width: 50%
name: Fig:Integration:FresnelFunctions
align: center
---
Graphs of $C(x)$ and $S(x)$ for $0\leq x\leq4$.
```
::::::

## Exercises

::::{exercise}
:label: Exc:Integration:FundamentalTheoremTrigIntegrals
Consider the integrals $\displaystyle\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx$ and $\displaystyle\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx$.

(a) Use the double-angle formula $\cos(2x)=\cos^2(x)-\sin^2(x)$ to show that both integrals are equal.

(b) Use the Pythagorean identity $\cos^2(x)+\sin^2(x)=1$ to prove that

$$
\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx=\tfrac{1}{4}\pi=\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx.
$$

::::

:::{admonition} Solution of {numref}`Exc:Integration:FundamentalTheoremTrigIntegrals`
:class: solution, dropdown
:name: Sol:Integration:FundamentalTheoremTrigIntegrals

(a) Using $\cos(2x)=\cos^2(x)-\sin^2(x)$ we find that

$$
\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx-\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx=\int_0^{\frac{1}{2}\pi}\cos(2x)\,dx=\frac{1}{2}\sin(2x)\bigg|_0^{\frac{1}{2}\pi}=0,
$$

which implies that $\displaystyle\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx=\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx$.

(b) Using $\cos^2(x)+\sin^2(x)=1$ we find that

$$
\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx+\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx=\int_0^{\frac{1}{2}\pi}1\,dx=\tfrac{1}{2}\pi.
$$

We conclude that

$$
\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx=\tfrac{1}{4}\pi=\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx.
$$

:::

## Grasple exercises

66942, 66940, 67076, 67078, 67075, 67081, 67079, 67073, 67072, 63704, 76779, 71414, 76784