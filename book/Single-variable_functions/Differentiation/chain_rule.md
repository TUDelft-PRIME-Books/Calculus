(Sec:Differentiation:ChainRule)=

# Chain rule

(Subsec:ChainruleIntro)=

## Introduction

Consider a diver who is diviving in the sea. Let $x$ be the depth (measured in meters) and $p(x)$ the pressure at that depth $x$ (measured in pascals). In addition, the depth is a function of time $t$ (measured in seconds), i.e., we have $x=x(t)$. To avoid decompression sickness, the diver should not go to the surface too fast. The main issue at hand here is not the change in height, but the change in pressure. So the main quantity that should be restricted here is the rate of change of the pressure with respect to time, i.e. $\frac{dp}{dt}$. However, $p$ is a function of $x$, and not of $t$, so how should we interpret this? Fortunately, $x$ is a function of $t$, so, indirectly, $p$ is a function of time and we can write $p=p(x(t))$. 

So how would we then evalute $\frac{dp}{dt}$? In a very short period of time $\Delta t$, the change in pressure $\Delta p$ equals the change in pressure per meter, which is $\frac{\Delta p}{\Delta x}$, times the change in depth $\Delta x$ in this short period of time. Written differently, we have

$$
 \frac{\Delta p}{\Delta t}=\frac{\Delta p}{\Delta x}\frac{\Delta x}{\Delta t}.
$$

Taking the limit as $\Delta t$ approaches $0$ of this expression, we obtain the expression

$$
 \frac{d p}{d t}=\frac{d p}{d x}\frac{d x}{d t}.
$$

Here we used that if $\Delta t\rightarrow 0$ we have $\Delta x\rightarrow 0$ as well. So the rate of change of the pressure with respect to time is the product of the rate of change of pressure with respect to depth times the velocity at which the depth changes. This makes sense intuitively: if we move twice as fast, we would expect the pressure to change twice as fast as well, and if the pressure decreases three times as fast with respect to depth, it will also change three times as fast with respect to time.

The general version of this result is known as the **chain rule**. It is used to find derivatives of compositions of functions. It is a very important and commonly used tool when finding derivatives. In this section, we will state and prove the chain rule and show how it is used. We will also use the chain rule to find the derivative of functions of the form $f(x)=b^x$ for $b>0$.

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

If there is some interval $(a-h,a+h)$ such that for each $x$ in $(a-h,a+h)$ we have $g(x)\neq g(a)$, then we can directly evalute the limit as $x$ approaches $a$ as

$$
 \lim_{x\rightarrow a}\frac{h(x)-h(a)}{x-a}=\lim_{x\rightarrow a}\frac{f(g(x))-f(g(a))}{x-a}=\lim_{x\rightarrow a}\frac{f(g(x))-f(g(a))}{g(x)-g(a)}\cdot\frac{g(x)-g(a)}{x-a}=\lim_{x\rightarrow a}\frac{f(g(x))-f(g(a))}{g(x)-g(a)}\cdot\lim_{x\rightarrow a}\frac{g(x)-g(a)}{x-a}=f'(g(a))\cdot g'(a)
$$

using {prf:ref}`Thm:Differentiability:Derivativealt`. In that case, we would directly obtain $h'(a)=f'(g(a))\cdot g'(a)$.

However, we cannot make the assumption that there is such an interval $(a-h,a+h)$, in general. And if we cannot make this assumption, the preceding computation does not work as we are committing the sin of dividing by $0$. So to avoid this, we define a real function $k$ that is given by

$$
 k(x)=\left\{\begin{array}{l}\frac{f(x)-f(g(a))}{x-g(a)},\qquad&\text{if}\ x\neq g(a),\\
 f'(g(a)),\qquad&\text{if}\ x=g(a)\end{array}\right.
$$

Then we have, since $f$ is differentiable at $g(a)$,

$$
 \lim_{x\rightarrow g(a)}k(x)=\lim_{x\rightarrow g(a)}\frac{f(x)-f(g(a))}{x-g(a)}=f'(g(a))=k(a),
$$

so we have constructed $k$ in such a way that $k$ is continuous at $g(a)$. According to {prf:ref}`Thm:Differentiability:Diffimpliescont`, $g$ is continuous at $a$, since it is differentiable at $a$. So by {prf:ref}`Theorem:Continuity:Composition`, $\phi\circ g$ is continuous at $a$. 

Now for any $x$ for which $g(x)\neq g(a)$ we have

$$
 k(g(x))\frac{g(x)-g(a)}{x-a}=\frac{f(g(x))-f(g(a))}{g(x)-g(a)}\frac{g(x)-g(a)}{x-a}=\frac{f(g(x))-f(g(a))}{x-a}.
$$

In addition, for any $x\neq a$ with $g(x)=g(a)$, we have $f(g(x))=f(g(a))$ as well, so we find that

$$
 k(g(x))\frac{g(x)-g(a)}{x-a}=0=\frac{f(g(x))-f(g(a))}{x-a}.
$$

So the identity $\displaystyle k(g(x))\frac{g(x)-g(a)}{x-a}=\frac{f(g(x))-f(g(a))}{x-a}$ holds for all $x\neq a$. Then, we find that

$$
 \lim_{x\rightarrow a}\frac{h(x)-h(a)}{x-a}=\lim_{x\rightarrow a}\frac{f(g(x))-f(g(a))}{x-a}=\lim_{x\rightarrow a}k(g(x))\frac{g(x)-g(a)}{x-a}=\lim_{x\rightarrow a}k(g(x))\cdot \lim_{x\rightarrow a}\frac{g(x)-g(a)}{x-a}.
$$

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

Let us see how we can use the chain rule in practice, by considering a few examples.

::::::{prf:example} 
:label: Thm:Chainrule:Example1
Consider the function $h(x)=\sin\left(x^3\right)$. Then we note that $h=f\circ g$ with $f(x)=\sin(x)$ and $g(x)=x^3$. That means that $h$ is the composition of two functions of which we know the derivative. As such, we can use the chain rule to find the derivative. Indeed, we have $f'(x)=\cos(x)$ and $g'(x)=3x^{3-2}=3x^2$, so we obtain

$$
 h'(x)=f'(g(x))g'(x)=\cos\left(x^3\right)3x^2.
$$

::::::

::::::{prf:example} 
:label: Thm:Chainrule:Example2
Consider the function $f(t)=e^{3\cos(t)}$. Again, this function can be written as the composition of two other functions of which we know the derivative. Indeed, we have $f=g\circ h$ with $g(t)=e^{t}$ and $h(t)=3\cos(t)$. We know that $g'(t)=e^t$ and $h'(t)=-3\sin(t)$. Then, with the chain rule, we obtain

$$
 f'(t)=g'(h(t))h'(t)=e^{3\cos(t)}(-3\sin(t))=-3\sin(t)e^{3\cos(t)}.
$$

::::::




::::::{prf:example} 
:label: Thm:Chainrule:Highpower
Suppose we want to know the derivative of the function $p(t)=\left(t^2+1\right)^{10}$. We could try to work out the brackets, but then we get quite a large number of terms. It is also not necessary to do so. Instead, we can use the chain rule. Indeed, we note that $p=r\circ s$ with $r(t)=t^{10}$ and $s(t)=t^2+1$. We know the derivatives of both of these functions, since we have $r'(t)=10t^{10-1}=10t^9$ and $s'(t)=2t^{2-1}+0=2t$, so we obtain

$$
 p'(t)=r'(s(t))s'(t)=10\left(t^2+1\right)^92t=20t\left(t^2+1\right)^9.
$$

In general, if $n$ is a natural number, the chain rule can be used to find the derivative of functions of the form $p(t)=\left(q(t)\right)^n$ and that derivative becomes $p'(t)=n\left(q(t)\right)^{n-1}q'(t)$.
::::::

::::::{prf:example} 
:label: Thm:Chainrule:Introbtox
Now consider the function $f(x)=2^x$. In {numref}`Section:Differentiability` we saw how we can differentiate the exponential function with base $e$, but not with any other base. Fortunately, the chain rule allows us to do just that. For this, we first want to rewrite the function $f$ in terms of functions of which we know the derivative. In this case, the important thing to use is that $2=e^{\ln(2)}$, since the natural logarithm is the inverse of the exponential function. This means that for any $x$ we have

$$
 f(x)=2^x=\left(e^{\ln(2)}\right)^x=e^{\ln(2)x}.
$$

Now, the function $f$ is written as the composition $f=g\circ h$ with $g(x)=e^x$ and $h(x)=\ln(2)x$ and of both these functions we know the derivative (note that $\ln(2)$ is just a number, so $h$ is a linear function). Then the chain rule gives

$$
 \frac{d}{dx}2^x=\frac{d}{dx}e^{\ln(2)x}=g'(h(x))h'(x)=e^{\ln(2)x}\ln(2)=\ln(2)2^x.
$$

::::::

{prf:ref}`Thm:Chainrule:Introbtox` suggests that we can use the chain rule to find the derivative of exponential functions with base different from $e$. In addition, we can use the chain rule to find the derivative of the hyperbolic functions (see {prf:ref}`Def:PropertiesFunctions:Hyperbolic`)

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

As such, we have $f=g\circ h$ with $g(x)=e^{x}$ and $h(x)=\ln(a)x$. Then $g'(x)=e^x$ and $h'(x)=\ln(a)$ (recall that $\ln(a)$ is simply a number), so with the chain rule we find

$$
 f'(x)=g'(h(x))h'(x)=e^{\ln(a)x}\ln(a)=\ln(a)a^x.
$$

Now consider the function $f(x)=\sinh(x)=\dfrac{e^{x}-e^{-x}}{2}$. We will use the chain rule to find the derivative $\dfrac{d}{dx}e^{-x}$. Indeed, we, if $p(x)=e^{-x}$ then $p=s\circ t$ with $s(x)=e^x$ and $t(x)=-x$. Then we obtain with the chain rule that

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

So why is the chain rule called the chain rule? This becomes clear when we note that we can use it as well to differentiate a chain of functions of the form $f\circ g\circ h$ (or even longer expressions). Indeed, if we have $z=z(y)$, $y=y(x)$ and $x=x(t)$, then the chain rule gives (in Leibniz notation)

$$
 \frac{dz}{dt}=\frac{dz}{dy}\frac{dy}{dx}\frac{dx}{dt}.
$$

If we were to think (incorrectly!) of expressions like $dz$ as numbers, then the equation above is just a matter of simplifying a product of fractions. Of course, an expression of the form $\dfrac{dz}{dy}$ is not an actual fraction, but simply a notation for the derivative. Still, we can use this to remember what the chain rule looks like for longer chains of functions.

{prf:ref}`Thm:Chainrule:chain` how we can find the derivative of a chain of functions in practice.

::::::{prf:example} 
:label: Thm:Chainrule:chain
Consider the function $f(x)=\sin\left(3^{x^2+1}\right)$. Then we note that $f=g\circ h\circ k$ with $g(x)=\sin(x)$, $h(x)=3^x$ and $k(x)=x^2+1$. We first apply the chain rule to $f=g\circ (h\circ k)$ to obtain

$$
 f'(x)=f'((g\circ h)(x))(g\circ h)'(x)=f'(g(h(x)))(g\circ h)'(x).
$$

Now we can use the chain rule again to find the derivative $(g\circ h)'(x)$. This gives

$$
 f'(x)=f'(g(h(x)))(g\circ h)'(x)=f'(g(h(x)))g'(h(x))h'(x)=\cos\left(3^{x^2+1}\right)\ln(3)3^{x^2+1}\left(2x+1\right).
$$


::::::