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

In this section we cover:

- The chain rule
- Derivative of b^x