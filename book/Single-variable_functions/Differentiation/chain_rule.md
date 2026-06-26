(Sec:Differentiation:ChainRule)=

# Chain rule

(Sec:ChainruleIntro)=

## Introduction

Consider a diver who descends into the sea. Let $z$ be the depth (measured in meters) and $p(z)$ the pressure at that depth $z$ (measured in pascals). Also, the depth is a function of time $t$ (measured in seconds), i.e., we have $z=z(t)$. To avoid decompression sickness, the diver should not go to the surface too fast. The main issue is not the change in height, but the change in pressure. So the quantity that should be restricted here is the rate of change of the pressure with respect to time, i.e. $\frac{dp}{dt}$. However, $p$ is a function of $z$, and not directly of $t$, so how should we interpret this? Fortunately, $z$ is a function of $t$, so, indirectly, $p$ is a function of time and we can write $p=p(z(t))$. 

So how would we evaluate $\frac{dp}{dt}$? In a very short period of time $\Delta t$, the change in pressure $\Delta p$ equals the change in pressure per meter, which is $\frac{\Delta p}{\Delta z}$, times the change in depth $\Delta z$ in this short period of time. Written differently, we have

$$
 \frac{\Delta p}{\Delta t}=\Delta p\cdot\frac{1}{\Delta t}=\frac{\Delta p}{\Delta z}\cdot\Delta z\cdot\frac{1}{\Delta t}=\frac{\Delta p}{\Delta z}\frac{\Delta z}{\Delta t}.
$$

Taking the limit as $\Delta t\rightarrow 0$ of this expression, we obtain the expression

$$
 \frac{d p}{d t}=\frac{d p}{d z}\frac{d z}{d t},
$$

as long as the derivatives in this expression exist. Here we used that if $\Delta t\rightarrow 0$, we must have $\Delta z\rightarrow 0$ as well. So the rate of change of the pressure with respect to time is the product of the rate of change of pressure with respect to depth with the velocity at which the depth changes. This makes sense intuitively: if we move twice as fast, we would expect the pressure to change twice as fast as well, and if the pressure decreases three times as fast with respect to depth, it will also change three times as fast with respect to time.

To make things more concrete, suppose now that

$$
 p(z)=10000z
$$

and that the safe decompression rate is given by

$$
 \frac{dp}{dt}=1700\,\frac{\mathrm{Pa}}{\mathrm{s}}.
$$

If we want to find the largest speed to avoid decompression sickness, we should use our previously found expression relating the various derivatives. This gives

$$
 \frac{d z}{d t}=\frac{\frac{d p}{d t}}{\frac{d p}{d z}}=\frac{1700}{10000}\,\frac{\mathrm{m}}{\mathrm{s}}=\frac{17}{100}\,\frac{\mathrm{m}}{\mathrm{s}}.
$$

So in order to avoid decompression sickness, the diver should not move faster than $\displaystyle \frac{17}{100}\,\frac{\mathrm{m}}{\mathrm{s}}$.

The general version of the technique we used to find $\dfrac{d p}{d t}$ is known as the **chain rule**. It is used to find derivatives of compositions of functions. It is a very important and commonly used tool for finding derivatives. In this section, we will state and prove the chain rule and show how it is used. We will also use the chain rule to find the derivative of functions of the form $f(x)=b^x$ for $b>0$.

(Subsec:ChainruleIntro)=

## The chain rule

::::::{prf:theorem} The chain rule
:label: Thm:Chainrule:Chainrule
Let $f$ and $g$ be functions such that the composition $h=f\circ g$ exists. Let $a$ be in the domain of $h$. Assume that $g$ is differentiable at $a$ and that $f$ is differentiable at $g(a)$. Then $h$ is differentiable at $a$ and the derivative $h'(a)$ is given by

$$
 h'(a)=(f\circ g)'(a)=f'(g(a))\cdot g'(a).
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Chainrule:Chainrule`
:class: tudproof, dropdown
For any $x$ with $g(x)\neq g(a)$, we can write

$$
 \frac{f(g(x))-f(g(a))}{x-a}=\frac{f(g(x))-f(g(a))}{g(x)-g(a)}\cdot\frac{g(x)-g(a)}{x-a}.
$$

If there is some interval $(a-\delta,a+\delta)$ such that for each $x$ in $(a-\delta,a+\delta)$ we have $g(x)\neq g(a)$, then we can directly evaluate the limit as $x$ approaches $a$ as

\begin{align*}
 \lim_{x\rightarrow a}\frac{h(x)-h(a)}{x-a} &= \lim_{x\rightarrow a}\frac{f(g(x))-f(g(a))}{x-a} \\
 &= \lim_{x\rightarrow a}\frac{f(g(x))-f(g(a))}{g(x)-g(a)}\cdot\frac{g(x)-g(a)}{x-a} \\
 &= \lim_{x\rightarrow a}\frac{f(g(x))-f(g(a))}{g(x)-g(a)}\cdot\lim_{x\rightarrow a}\frac{g(x)-g(a)}{x-a} \\
 &= f'(g(a))\cdot g'(a)
\end{align*}

using {prf:ref}`Thm:Differentiability:Derivativealt`. In that case, we directly obtain $h'(a)=f'(g(a))\cdot g'(a)$.

However, we cannot make the assumption that there is such an interval $(a-\delta,a+\delta)$, in general. And if we cannot make this assumption, the preceding computation does not work as we are committing the sin of dividing by $0$. So to avoid this, we define a real function $k$ that is given by

$$
 k(u)=\left\{\begin{array}{ll}\dfrac{f(u)-f(g(a))}{u-g(a)},&\text{if}\quad u\neq g(a),\\
 f'(g(a)),&\text{if}\quad u=g(a).\end{array}\right.
$$

Then we have, since $f$ is differentiable at $g(a)$,

$$
 \lim_{u\rightarrow g(a)}k(u)=\lim_{u\rightarrow g(a)}\frac{f(u)-f(g(a))}{u-g(a)}=f'(g(a))=k(g(a)),
$$

so we have constructed $k$ in such a way that $k$ is continuous at $g(a)$. According to {prf:ref}`Thm:Differentiability:Diffimpliescont`, $g$ is continuous at $a$, since it is differentiable at $a$. So by {prf:ref}`Theorem:Continuity:Composition`, $k\circ g$ is continuous at $a$. 

Now for any $x$ for which $g(x)\neq g(a)$ we have

$$
 k(g(x))\frac{g(x)-g(a)}{x-a}=\frac{f(g(x))-f(g(a))}{g(x)-g(a)}\frac{g(x)-g(a)}{x-a}=\frac{f(g(x))-f(g(a))}{x-a}.
$$

In addition, for any $x\neq a$ with $g(x)=g(a)$, we have $f(g(x))=f(g(a))$ as well, so we find that

$$
 k(g(x))\frac{g(x)-g(a)}{x-a}=0=\frac{f(g(x))-f(g(a))}{x-a}.
$$

So the identity $\displaystyle k(g(x))\frac{g(x)-g(a)}{x-a}=\frac{f(g(x))-f(g(a))}{x-a}$ holds for all $x\neq a$. Then, we find that

\begin{align*}
 \lim_{x\rightarrow a}\frac{h(x)-h(a)}{x-a} &= \lim_{x\rightarrow a}\frac{f(g(x))-f(g(a))}{x-a} \\
 &= \lim_{x\rightarrow a}k(g(x))\frac{g(x)-g(a)}{x-a} \\
 &= \lim_{x\rightarrow a}k(g(x))\cdot \lim_{x\rightarrow a}\frac{g(x)-g(a)}{x-a}.
\end{align*}

Now since $k\circ g$ is continuous at $a$, we obtain

$$
 \lim_{x\rightarrow a}\frac{h(x)-h(a)}{x-a}=\lim_{x\rightarrow a}k(g(x))\cdot \lim_{x\rightarrow a}\frac{g(x)-g(a)}{x-a}=k(g(a))\cdot g'(a)=f'(g(a))\cdot g'(a).
$$

This establishes the chain rule in the general setting.

:::

::::{caution}
:name: Caution:Chainrule:Commonerrors

There are two common errors when using the chain rule to find the derivative $(f\circ g)'(x)$. The first is that, instead of evaluating $f'$ at $g(x)$, $f'$ is evaluated at $x$, i.e.,

$$
 (f\circ g)'(x)=f'(x)g'(x)\qquad\qquad \left(\textbf{INCORRECT}\right).
$$

The most common error, however, is forgetting to multiply by $g'(x)$. In that case, the incorrect expression would become

$$
 (f\circ g)'(x)=f'(g(x))\qquad\qquad \left(\textbf{INCORRECT}\right).
$$

Make sure to avoid both errors and use the chain rule as stated.
::::

::::{prf:notation}
:label: Thm:Chainrule:Notation

A useful notation that might help you remember the chain rule is to view $f$ as a function of a variable $u$ and $g$ as a function of a different variable $x$. Then

$$
(f\circ g)(x) = \Bigg[ f(u) \Bigg]_{u=g(x)}.
$$

Using this notation, the chain rule can be remembered by writing it in Leibniz notation as

$$
 \frac{df}{dx}=\frac{df}{du}\frac{du}{dx},
$$

by which we mean

$$
(f\circ g)'(x) = \Bigg[ f'(u) \Bigg]_{u=g(x)} g'(x) = \left[ \dfrac{df}{du} \right]_{u=g(x)} \dfrac{dg}{dx}.
$$


::::

Let us see how we can use the chain rule in practice, by considering a few examples.

::::::{prf:example} 
:label: Thm:Chainrule:Example1
Consider the function $h(x)=\sin\left(x^3\right)$. Then we note that $h=f\circ g$ with $f(u)=\sin(u)$ and $g(x)=x^3$. That means that $h$ is the composition of two functions of which we know the derivative. As such, we can use the chain rule to find the derivative. Indeed, we have $f'(u)=\cos(u)$ and $g'(x)=3x^{3-1}=3x^2$, so we obtain

$$
 h'(x)=f'(g(x))g'(x)=\cos\left(x^3\right)3x^2.
$$

In practice, it suffices to write

$$
 \frac{d}{dx}\sin\left(x^3\right)=\cos\left(x^3\right)\frac{dx^3}{dx}=\cos\left(x^3\right)3x^2.
$$

::::::

::::::{prf:example} 
:label: Thm:Chainrule:Example2
Consider the function $f(t)=e^{3\cos(t)}$. Again, this function can be written as the composition of two other functions of which we know the derivative. Indeed, we have $f=g\circ h$ with $g(u)=e^{u}$ and $h(t)=3\cos(t)$. We know that $g'(u)=e^{u}$ and $h'(t)=-3\sin(t)$. Then, with the chain rule, we obtain

$$
 f'(t)=g'(h(t))h'(t)=e^{3\cos(t)}(-3\sin(t))=-3\sin(t)e^{3\cos(t)}.
$$

::::::




::::::{prf:example} 
:label: Thm:Chainrule:Highpower
Suppose we want to evaluate the derivative of the function $p(t)=\left(t^2+1\right)^{10}$. We could try to work out the brackets, but then we get quite a large number of terms. It is also not necessary to do so. Instead, we can use the chain rule. Indeed, we note that $p=r\circ s$ with $r(u)=u^{10}$ and $s(t)=t^2+1$. We know the derivatives of both of these functions, since we have $r'(u)=10u^{9}$ and $s'(t)=2t$, so we obtain

$$
 p'(t)=r'(s(t))s'(t)=10\left(t^2+1\right)^92t=20t\left(t^2+1\right)^9.
$$

In general, if $n$ is a natural number, the chain rule can be used to find the derivative of functions of the form $p(t)=\left(q(t)\right)^n$ and that derivative becomes $p'(t)=n\left(q(t)\right)^{n-1}q'(t)$.
::::::

## Standard derivatives

::::::{prf:example} 
:label: Thm:Chainrule:Introbtox
Now consider the function $f(x)=2^x$. In {numref}`Section:Differentiability` we saw how we can differentiate the exponential function with base $e$, but not with any other base. Fortunately, the chain rule allows us to do just that. For this, we first rewrite the function $f$ in terms of functions of which we know the derivative. In this case, the important thing to use is that $2=e^{\ln(2)}$, since the natural logarithm is the inverse of the exponential function. This means that for any $x$ we have

$$
 f(x)=2^x=\left(e^{\ln(2)}\right)^x=e^{\ln(2)x}.
$$

Now, the function $f$ is written as the composition $f=g\circ h$ with $g(u)=e^u$ and $h(x)=\ln(2)x$ and of both these functions we know the derivative (note that $\ln(2)$ is just a number, so $h$ is a linear function). Then the chain rule gives

$$
 \frac{d}{dx}\left(2^x\right)=\frac{d}{dx}\left(e^{\ln(2)x}\right)=g'(h(x))h'(x)=e^{\ln(2)x}\ln(2)=\ln(2)2^x.
$$

::::::

[^FootnoteCosSinhyp]: As we noted already in {numref}`Subsec:PropertiesFunctionsEvenOdd`, one of the reasons why the hyperbolic sine and cosine are named that way, is that their derivatives follow a similar (though not exactly the same) pattern as the derivatives of the regular sine and cosine.

{prf:ref}`Thm:Chainrule:Introbtox` shows that we can use the chain rule to find the derivative of exponential functions with base different from $e$. In addition, we can use the chain rule to find the derivative of the hyperbolic functions (see {prf:ref}`Def:PropertiesFunctions:Hyperbolic`).[^FootnoteCosSinhyp]

::::::{prf:theorem} Standard derivatives, part 2 out of 4
:label: Thm:Chain rule:Standard2
We have the following standard derivatives.

- If $a>0$ is a real number, then we have $\dfrac{d}{dx}a^x=\ln(a)a^x$.
- We have $\dfrac{d}{dx}\sinh(x)=\cosh(x)$.
- We have $\dfrac{d}{dx}\cosh(x)=\sinh(x)$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Chain rule:Standard2`
:class: tudproof, dropdown
Let $a>0$ be a real number and consider the function $f(x)=a^x$. Since $a=e^{\ln(a)}$, we have

$$
 f(x)=a^x=\left(e^{\ln(a)}\right)^x=e^{\ln(a)x}.
$$

As such, we have $f=g\circ h$ with $g(u)=e^{u}$ and $h(x)=\ln(a)x$. Then $g'(u)=e^{u}$ and $h'(x)=\ln(a)$ (recall that $\ln(a)$ is simply a number), so with the chain rule we find

$$
 f'(x)=g'(h(x))h'(x)=e^{\ln(a)x}\ln(a)=\ln(a)a^x.
$$

Now consider the function $f(x)=\sinh(x)=\dfrac{e^{x}-e^{-x}}{2}$. We will use the chain rule to find the derivative $\dfrac{d}{dx}e^{-x}$. Indeed, if $p(x)=e^{-x}$ then $p=s\circ t$ with $s(u)=e^u$ and $t(x)=-x$. Then we obtain with the chain rule that

$$
 p'(x)=s'(t(x))t'(x)=e^{-x}(-1)=-e^{-x}.
$$

As such, we find that

$$
 \frac{d}{dx}\sinh(x)=\frac{d}{dx}\dfrac{e^{x}-e^{-x}}{2}=\dfrac{e^{x}-\left(-e^{-x}\right)}{2}=\dfrac{e^x+e^{-x}}{2}=\cosh(x).
$$

Similarly, we find

$$
 \frac{d}{dx}\cosh(x)=\frac{d}{dx}\dfrac{e^{x}+e^{-x}}{2}=\dfrac{e^{x}+\left(-e^{-x}\right)}{2}=\dfrac{e^x-e^{-x}}{2}=\sinh(x).
$$

:::

## Longer chains of functions

So why is the chain rule called the chain rule? This becomes clear when we note that we can use it as well to differentiate a chain of functions of the form $f\circ g\circ h$ (or even longer expressions). Indeed, if we have $z=z(y)$, $y=y(x)$ and $x=x(t)$, then the chain rule gives (in Leibniz notation)

$$
 \frac{dz}{dt}=\frac{dz}{dy}\frac{dy}{dx}\frac{dx}{dt}.
$$

If we were to think (incorrectly!) of expressions like $dz$ as numbers, then the equation above is just a matter of simplifying a product of fractions. Of course, an expression of the form $\dfrac{dz}{dy}$ is not an actual fraction, but simply a notation for the derivative. Still, we can use this to remember what the chain rule looks like for longer chains of functions.

{prf:ref}`Ex:Chainrule:chain` shows how we can find the derivative of a chain of functions in practice.

::::::{prf:example} 
:label: Ex:Chainrule:chain
Consider the function $f(x)=\sin\left(3^{x^2+1}\right)$. Using the chain rule we find

$$
 \frac{df}{dx}=\cos\left(3^{x^2+1}\right)\frac{d}{dx}\left(3^{x^2+1}\right).
$$

Now we can use the chain rule again to find the derivative of  $3^{x^2+1}$. This gives

\begin{align*}
 f'(x) &= \cos\left(3^{x^2+1}\right)\frac{d}{dx}\left(3^{x^2+1}\right) \\
 \cos\left(3^{x^2+1}\right)\ln(3)3^{x^2+1}\left(2x+1\right).
\end{align*}

::::::

::::::{prf:example} 
:label: Ex:Chainrule:chainabstract
Consider the function $f(x)=\sin\left(3^{k(x)}\right)$ for some (unknown), differentiable function $k$. Compared to {prf:ref}`Ex:Chainrule:chain`, it is a bit harder to see what happens here because of this unknown function. We note that $f=g\circ(h\circ k)$ with $g(w)=\sin(w)$ and $h(u)=3^u$. We first apply the chain rule to $f=g\circ (h\circ k)$ to obtain

$$
 f'(x)=g'((h\circ k)(x))(h\circ k)'(x)=g'(h(k(x)))(h\circ k)'(x).
$$

Now we can use the chain rule again to find the derivative $(h\circ k)'(x)$. This gives

\begin{align*}
 f'(x) &= g'(h(k(x)))(h\circ k)'(x) \\
 &= g'(h(k(x)))h'(k(x))k'(x) \\
&= \cos\left(3^{k(x)}\right)\ln(3)3^{k(x)}k'(x).
\end{align*}

::::::

The basic rule you need to remember is that if you have a chain of functions, you can apply the chain rule repeatedly to find the derivative of that entire chain. To do so, you work from the outside in.

A concise, but a little hard to read theorem that summarises this is the following.

::::{prf:corollary}
Let $f_1,f_2,\ldots,f_n$ be functions such that the composition $h=f_1\circ f_{2}\circ \cdots \circ f_n$ exists. Let $a$ be in the domain of $h$. Assume that for each $i=1,2,\ldots,n-1$, the function $f_i$ is differentiable at $(f_{i+1}\circ f_{i+2}\circ\cdots\circ f_n)(a)$ and that $f_n$ is differentiable at $a$. Then the $h$ is differentiable at $a$ and we have

$$
h'(a)=f_1'\Big(\left(f_2\circ f_3\circ\cdots\circ f_n\right)(a)\Big)f_2'\Big(\left(f_3\circ f_4\circ\cdots\circ f_n\right)(a)\Big)\cdots f_{n-1}'(f_n(a))f_n'(a).
$$

::::

If we define

$$
h_i = f_i\circ f_{i+1}\circ\cdots\circ f_n,
$$

for each $i=1,2,\ldots,n$, then the expression for $h'(a)$ in the corollary above can be written more compactly as

$$
h'(a) = \prod_{i=1}^n f_{i}'\left(h_{i+1}(a)\right),
$$

where $h_{n+1}(a) = a$.

We omit the proof of this corollary, since it is just a matter of applying the chain rule repeatedly. The main thing to remember is that if you have a chain of functions, you can apply the chain rule repeatedly to find the derivative of that entire chain.

## Grasple exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/45245d2e-3cd9-4926-b0ab-8b870cc704d2?id=63436
:label: Grasple:63436
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e3d52bed-69d5-4e3f-96ae-97f21cc5b3f8?id=63445
:label: Grasple:63445
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a0e39e7f-7f94-4122-8510-964d348ee5f2?id=63493
:label: Grasple:63493
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4800351f-cd91-4506-a93d-21e4f628dd17?id=63444
:label: Grasple:63444
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/49b611ec-a218-492f-bd9a-b3aeec98402d?id=63525
:label: Grasple:63525
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9f445188-faa5-4a42-a79c-12f7cd3dd271?id=63522
:label: Grasple:63522
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f97dfe6f-5b06-4a04-b2a5-ecdd927fd6fc?id=63419
:label: Grasple:63419
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9508a2aa-1265-4fb8-95d7-7acdf9178a2e?id=63526
:label: Grasple:63526
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ab6a1a77-b42a-479e-bcc9-1e8a4aa830cb?id=71398
:label: Grasple:71398
:dropdown:
:description: Find a derivative.
::::