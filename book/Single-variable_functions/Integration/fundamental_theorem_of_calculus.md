(Sec:Integration:FundamentalTheorem)=

# Fundamental theorem of calculus

## Introduction

In this section we will explain the relation between definite and indefinite integrals. The connection is given by the *fundamental theorem of calculus*.

In {numref}`Sec:Integration:IndefiniteIntegrals` we introduced the concept of the indefinite integral $\displaystyle \int f(x)\,dx$ of a function $f$ on an open interval $I$ and made a relation between indefinite integrals and derivatives.

Such a relation also exists between definite integrals and derivatives, which is the subject of the fundamental theorem of calculus. This theorem consists of two parts.

## Part 1 of the fundamental theorem of calculus

Without further ado we state the first part of the fundamental theorem of calculus:

::::::{prf:Theorem} The fundamental theorem of calculus, part 1
:label: Thm:Integration:FundamentalTheoremPart1
If $f$ is continuous on the interval $[a,b]$, then the function $F(x)$ defined by

$$
F(x)=\int_a^xf(t)\,dt,\quad a\leq x\leq b
$$

is continuous on $[a,b]$ and differentiable on $(a,b)$, and $F'(x)=f(x)$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Integration:FundamentalTheoremPart1`
:class: tudproof, dropdown
:name: Prf:Integration:FundamentalTheoremPart1

```{figure} Images/FundamentalTheorem.png
---
width: 50%
name: FundamentalTheorem
class: dark-light
---

The fundamental theorem of calculus.
```

Using the third rule of {prf:ref}`Thm:Integration:DefinitePropertiesArea` and {prf:ref}`Def:Differentiability:Derivative`, we obtain

\begin{align*}
F'(x)&=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}\\
&=\lim_{h\to 0}\frac{1}{h}\left(\int_a^{x+h}f(t)\,dt-\int_a^xf(t)\,dt\right)\\
&=\lim_{h\to 0}\frac{1}{h}\left(\int_a^{x}f(t)\,dt+\int_x^{x+h}f(t)\,dt-\int_a^xf(t)\,dt\right)\\
&=\lim_{h\to 0}\frac{1}{h}\int_x^{x+h}f(t)\,dt.
\end{align*}

Because $f$ is continuous on $[a,b]$, we can use the third rule of {prf:ref}`Thm:Integration:DefiniteComparison` to conclude that there exist values $c$ and $d$ between $x$ and $x+h$ such that $f(c)\leq f(t)\leq f(d)$ for all $t$ between $x$ and $x+h$ and that we have

$$
\int_x^{x+h}f(t)\,dt\geq\int_x^{x+h}f(c)\,dt=f(c)\cdot ((x+h)-x)=hf(c).
$$

and

$$
\int_x^{x+h}f(t)\,dt\leq\int_x^{x+h}f(d)\,dt=f(d)\cdot ((x+h)-x)=hf(d).
$$

Note that if $h\rightarrow0$, then both $c$ and $d$ approach $x$ and $f(c)$ and $f(d)$ approach $f(x)$ by continuity. Hence, we can use {prf:ref}`Theorem:LimitAtPoint:Squeezetheorem` to conclude that because

$$
f(c)\leq \frac{1}{h}\int_x^{x+h}f(t)\,dt\leq f(d),
$$

we have

$$
F'(x)=\lim_{h\to 0}\frac{1}{h}\int_x^{x+h}f(t)\,dt = f(x).
$$

This proves that $F$ is differentiable on $(a,b)$ and that $F'(x)=f(x)$.

Because $f$ is continuous on $[a,b]$, it follows from {prf:ref}`Thm:Integration:IntegrablePiecewise` that $F(b)$ exists and $F(a)=0$. Therefore, $F$ is also continuous on $[a,b]$.

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart1Example1

We take $F(x)=\displaystyle\int_0^xe^{t^2}\,dt$ and want to determine $F'(x)$.

We not need to evaluate the integral, which would be impossible in terms of elementary functions. However, application of the fundamental theorem of calculus leads to the immediate solution 

$$
F'(x)=\frac{d}{dx}\int_0^xe^{t^2}\,dt=e^{x^2}.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart1Example2
Let $G(x)=\displaystyle\int_0^{\sqrt{x}}\cos(t^2)\,dt$ for $x>0$. We want to determine $G'(x)$.

Setting $u=\sqrt{x}$ we have $G(x)=\displaystyle\int_0^{u}\cos(t^2)\,dt=H(u)$ with $H'(u)=\cos(u^2)$ by the fundamental theorem of calculus.

Now we apply the chain rule: $G'(x)=H'(u)\dfrac{du}{dx}$. This reads

$$
G'(x)=\cos\left((\sqrt{x})^2\right)\cdot\frac{d}{dx}(\sqrt{x})=\cos(x)\cdot\frac{1}{2\sqrt{x}}=\frac{\cos(x)}{2\sqrt{x}}.
$$

::::::

Before we do a final example for part 1 of the fundamental theorem of calculus, we note that the theorem can also be used if the lower limit of integration is $x$:

::::{prf:corollary}
:label: Cor:Integration:FundamentalTheoremPart1LowerLimit

If $f$ is continuous on the interval $[a,b]$, then the function $G(x)$ defined by

$$
G(x)=\int_x^bf(t)\,dt,\quad a\leq x\leq b
$$

is continuous on $[a,b]$ and differentiable on $(a,b)$, and $G'(x)=-f(x)$.
::::

::::{admonition} Proof of {prf:ref}`Cor:Integration:FundamentalTheoremPart1LowerLimit`
:class: tudproof, dropdown
:name: Prf:Integration:FundamentalTheoremPart1LowerLimit

Using the second rule of {prf:ref}`Thm:Integration:DefinitePropertiesFundamental` we have:

$$
G(x) = \int_x^bf(t)\,dt = - \int_b^xf(t)\,dt.
$$

Differentiating both sides we get:

$$
G'(x) = - f(x).
$$

Using the same arguments as in the proof of {prf:ref}`Thm:Integration:FundamentalTheoremPart1`, we can also show that $G$ is continuous on $[a,b]$ and differentiable on $(a,b)$.

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

::::{question} Short-answer blocks
:type: short-answer
:variant: blocks
:columns: 2
:class: question
:admonition:
:showanswer:

Fill in the correct answer in the input fields.
---
M[\sin(x^2)] $\displaystyle\frac{d}{dx}\int_0^x\sin(t^2)\,dt=$
= Apply the fundamental theorem of calculus to find that 

$$
\frac{d}{dx}\int_0^x\sin(t^2)\,dt=\sin(x^2).
$$
> Apply the fundamental theorem of calculus.

M[0] $\displaystyle\frac{d}{dx}\int_0^y\sin(t^2)\,dt=$
= Note that $\displaystyle\int_0^y\sin(t^2)\,dt$ is a function of $y$, independent of $x$. So, the derivative with respect equals zero.
> Note that $\displaystyle\int_0^y\sin(t^2)\,dt$ does not depend on $x$.

M[2xy\cos(x^2)] $\displaystyle\frac{d}{dx}\int_0^y\sin(x^2)\,dt=$
= Note that $\sin(x^2)$ does not depend on $t$, the variable of integration. So, $\displaystyle\int_0^y\sin(x^2)\,dt=y\sin(x^2)$ and the derivative with respect to $x$ equals $2xy\cos(x^2)$ (since $y$ is just a constant).
> Note that $\sin(x^2)$ does not depend on $t$, the variable of integration.

M[\sin(t^2)] $\displaystyle\frac{d}{dx}\int_0^x\sin(t^2)\,dy=$
= Note that $\sin(t^2)$ does not depend on $y$, the variable of integration. So, $\displaystyle\int_0^x\sin(t^2)\,dy=x\sin(t^2)$ and the derivative with respect to $x$ equals $\sin(t^2)$.
> Note that $\sin(t^2)$ does not depend on $y$, the variable of integration.

---

::::

## Part 2 of the fundamental theorem of calculus

Now that we have finished the first part of the fundamental theorem of calculus, we can state the second part, which finally gives us a way to really calculate definite integrals:

::::::{prf:Theorem} The fundamental theorem of calculus, part 2
:label: Thm:Integration:FundamentalTheoremPart2
If $f$ is continuous on the interval $[a,b]$, then

$$
\int_a^bf(x)\,dx=F(b)-F(a),
$$

where $F$ is any antiderivative of $f$, that is, a function such that $F'=f$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Integration:FundamentalTheoremPart2`
:class: tudproof, dropdown
:name: Prf:Integration:FundamentalTheoremPart2

Let $G(x)=\displaystyle\int_a^xf(t)\,dt$. Then {prf:ref}`Thm:Integration:FundamentalTheoremPart1` implies that $G'(x)=f(x)$. Hence, $G$ is an antiderivative of $f$.

So, if $F$ is any antiderivative of $f$ we have:

$$
F(x)=G(x)+C\quad\text{for}\quad a<x<b.
$$

However, since $F$ and $G$ are both continuous on $[a,b]$ we conclude that $F(x)=G(x)+C$ for all $x$ in $[a,b]$.

First note that

$$
G(a) = \int_a^af(t)\,dt = 0.
$$

This means that:

\begin{align*}
\int_a^bf(x)\,dx &= G(b) \\
&= G(b)-G(a) \\
&= \left(F(b)-C\right) - \left(F(a)-C\right) \\
&= F(b)-F(a),
\end{align*}

which completes the proof.

::::::

::::::{prf:Notation}
:label: Not:Integration:FundamentalTheoremPart2Notation

During evaluations of integrals we often use the notation

$$
\int_a^bf(x)\,dx=\Big[F(x)\Big]_a^b=F(b)-F(a)
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

:::{todo}
Replace {numref}`Fig:Integration:SineArea` with an applet.
:::

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

Integration of the function $\displaystyle f(x)=\frac{1}{1+x^2}$ from $0$ to $1$ gives:

$$
\int_0^1\frac{1}{1+x^2}\,dx=\arctan(x)\bigg|_0^1=\arctan(1)-\arctan(0)=\frac{1}{4}\pi-0=\frac{1}{4}\pi.
$$

::::::

So, in order to evaluate a definite integral we just need to find any antiderivative of the integrand. However, it is not always easy to find such an antiderivative. In the next sections we will cover some methods which can be used to evaluate integrals of certain types.

## Applications of the fundamental theorem of calculus

In some applications functions appear, which are defined in terms of an integral that cannot be evaluated. Even though the integrand is continuous and an antiderivative exists, it is sometimes impossible to write this in terms of standard functions. In the examples below we deal with some of these functions. Although the integral cannot be evaluated, the fundamental theorem of calculus can be used to find properties of the function.

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

:::{todo}
Replace {numref}`Fig:Integration:ErrorFunction` with an applet.
:::

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

:::{todo}
Replace {numref}`Fig:Integration:FresnelFunctions` with an applet.
:::

::::::

## The mean value theorem

In {prf:ref}`Thm:MinMax:MVT` we have seen the mean value theorem that states that the derivative of a continuous and differentiable function on a finite interval equals its average slope somewhere in the interval.

For integrals we have the following version.

```{figure} Images/MeanValueTheoremIntegrals.png
---
width: 50%
name: MeanValueTheoremIntegrals
class: dark-light
---

The mean value theorem for integrals.
```

:::::{prf:theorem} Mean value theorem for integrals
:label: Thm:Integration:MeanValueTheorem

For a continuous function $f$ on the interval $[a,b]$ there exists at least one $c\in(a,b)$ such that

$$
f(c)=\frac{1}{b-a}\int_a^bf(x)\,dx.
$$

Here $\displaystyle\frac{1}{b-a}\int_a^bf(x)\,dx$ denotes the **mean value** of $f$ over the interval $[a,b]$.
:::::

:::::{admonition} Proof of {prf:ref}`Thm:Integration:MeanValueTheorem`
:class: tudproof
:name: Prf:Integration:MeanValueTheorem

Let $F(x)$ be an antiderivative of $f$, such that $F'(x)=f(x)$. Since $f$ is continuous, $F$ is continuous on $[a,b]$ and differentiable on $(a,b)$. Then {prf:ref}`Thm:MinMax:MVT`
implies that there exists at least one $c\in(a,b)$ such that

$$
F'(c)=\frac{F(b)-F(a)}{b-a}.
$$

Now we use that $F'(c)=f(c)$ and $\displaystyle F(b)-F(a)=\int_a^bf(x)\,dx$ to conclude that

$$
f(c)=\frac{1}{b-a}\int_a^bf(x)\,dx.
$$

This proves the theorem.
:::::

## Exercises

::::{exercise}
:label: Exc:Integration:FundamentalTheoremTrigIntegrals
Consider the integrals $\displaystyle\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx$ and $\displaystyle\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx$.

(a) Use the double-angle formula $\cos(2x)=\cos^2(x)-\sin^2(x)$ to show that both integrals are equal.

(b) Use the {prf:ref}`Pythagorean identity <Thm:Trigonometry:UnitCircleIdentity>` $\sin^2(x)+\cos^2(x)=1$ to prove that

$$
\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx=\frac{1}{4}\pi=\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx.
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

(b) Using $\sin^2(x)+\cos^2(x)=1$ we find that

$$
\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx+\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx=\int_0^{\frac{1}{2}\pi}1\,dx=\frac{1}{2}\pi.
$$

Now we use (a) to conclude that

$$
\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx=\frac{1}{4}\pi=\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx.
$$

:::

## Grasple exercises

### Part 1 of the fundamental theorem of calculus

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/166b642b-e1df-42f1-875e-235655f4f856?id=76778
:label: Grasple:76778
:dropdown:
:description: Does this function have an antiderivative?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fdb224fd-fb1e-4a30-b7d3-a03b1484a26b?id=76789
:label: Grasple:76789
:dropdown:
:description: Where is the function $f(x)$ positive?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/760ff5f4-90fd-4d52-bfe8-9682b6c0fc0b?id=63708
:label: Grasple:63708
:dropdown:
:description: Determine the derivative.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/84163d6e-7675-46ca-b1f5-3f385d824040?id=76773
:label: Grasple:76773
:dropdown:
:description: Determine the derivative.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/88a928d5-9312-4916-bada-cbd37d5fb9f3?id=75374
:label: Grasple:75374
:dropdown:
:description: Determine the derivative.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b6b5b1bd-b545-4a31-9d2f-84ac510f0594?id=63704
:label: Grasple:63704
:dropdown:
:description: Determine the derivative.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/988fb5b3-53c9-4232-8d43-c7da4bb9ba19?id=76779
:label: Grasple:76779
:dropdown:
:description: Determine the derivative.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cefa8b9f-4333-4f08-aeaf-ee9020bae1e4?id=71414
:label: Grasple:71414
:dropdown:
:description: Determine the derivative.

::::

### Part 2 of the fundamental theorem of calculus

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cbf86abb-d106-41e9-b83d-6cf329dce134?id=67079
:label: Grasple:67079
:dropdown:
:description: Evaluate the integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bdfaea6b-5c3e-4ce5-8da8-8221383439a7?id=67073
:label: Grasple:67073
:dropdown:
:description: Evaluate the integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/477b2643-6b24-40ad-94f4-298d1c926351?id=67075
:label: Grasple:67075
:dropdown:
:description: Evaluate the integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cd63181e-873c-464d-aaf3-4d56c8b8a7f7?id=67078
:label: Grasple:67078
:dropdown:
:description: Evaluate the integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d40cfb5b-f656-4753-9577-96225af1fda7?id=66942
:label: Grasple:66942
:dropdown:
:description: Evaluate the integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/18c4fc13-db18-432f-ab59-188edc3e4992?id=66940
:label: Grasple:66940
:dropdown:
:description: Evaluate the integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cbf57048-948b-46cf-b23c-7f2652984085?id=67072
:label: Grasple:67072
:dropdown:
:description: Evaluate the integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d812df75-a285-475b-9e19-53e924fd1292?id=67076
:label: Grasple:67076
:dropdown:
:description: Evaluate the integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bba93713-04db-4e3e-bc33-90bcd06a1816?id=67081
:label: Grasple:67081
:dropdown:
:description: Evaluate the integral.

::::

### Applications of the fundamental theorem of calculus

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/54781abc-83a4-4f98-b475-211a05645f58?id=76787
:label: Grasple:76787
:dropdown:
:description: Find the smallest $x>0$ for which the function $\text{Si}(x)$ has a local maximum.

::::
