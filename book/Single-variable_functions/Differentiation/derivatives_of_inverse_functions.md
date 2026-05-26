(Subsec:Invdiff)=

# Derivatives of inverse functions

## Introduction

[^FootnoteDiffInv]: Maybe apart from world peace.

The one major thing missing in our lives right know[^FootnoteDiffInv] is a way to find the derivatives of the remaining standard functions. To recall, we have found the derivatives of the other standard functions in {prf:ref}`Thm:Differentiability:Standard1`, {prf:ref}`Thm:Chain rule:Standard2` and {prf:ref}`Thm:Productquotientrule:Standard3`. The ones that are missing are the derivatives of logarithms, inverse trigonometric functions and non-integer powers of $x$, as we promised in {prf:ref}`Remark:Differentiability:Powerfunctions`. So without further ado, let us get to work and find these derivatives.


## Derivatives of logarithms and inverse trigonometric functions

In {numref}`Subsec:ImplicitDiff` we studied the technique of implicit differentiation. It is perhaps surprising that we can use this technique to find derivatives of explicitly defined functions like logarithms and inverse trigonometric functions.

Let us use the natural logarithm as a showcase. Consider the function $f(x)=\ln(x)$. Then the graph of the function $f$ is defined by the equation

$$
 y=\ln(x).
$$

Since the natural logarithm is the inverse function of the exponential function, this equation is equivalent to 

$$
 e^y=x.
$$

In this new equation, $y$ is implicitly defined as a differentiable function of $x$ on account of {prf:ref}`Thm:SlopeCurves:IFT`. We know how to make it explicit (that is the equation that we started with), but working with the implicit equation allows us to use the derivatives that we already know. We will now apply implicit differentiation. For this, we take the derivative with respect to $x$ on both sides of this equation to obtain

$$
  \frac{d}{dx}\left[e^y\right]=\frac{d}{dx}[x]=1.
$$

In order to find $\frac{d}{dx}\left[e^y\right]$, we remember that $y$ is a function of $x$, so we can use the chain rule to obtain the equation

$$
 e^y\frac{dy}{dx}=1.
$$

This equation can be solved for $\dfrac{dy}{dx}$ and we obtain

$$
 \frac{dy}{dx}=\frac{1}{e^y}.
$$

Now we recall that $e^y=x$, and we conclude that

$$
 f'(x)=\frac{dy}{dx}=\frac{1}{e^y}=\frac{1}{x}.
$$

So, perhaps surprisingly, we have found that the derivative of the natural logarithm is $\frac{1}{x}$. 

Now that we know what our approach should be, let us find the derivatives of all remaining standard derivatives.

::::::{prf:theorem} Standard derivatives, part 4 out of 4
:label: Thm:Diffinverse:Standard4
We have the following standard derivatives:

- We have $\dfrac{d}{dx}\left[\log_b(x)\right]=\dfrac{1}{\ln(b)x}$ for any $b>0$. In particular, we have $\dfrac{d}{dx}\left[\ln(x)\right]=\dfrac{1}{x}$.
- We have $\dfrac{d}{dx}\left[\arcsin(x)\right]=\dfrac{1}{\sqrt{1-x^2}}.$
- We have $\dfrac{d}{dx}\left[\arccos(x)\right]=\dfrac{-1}{\sqrt{1-x^2}}.$
- We have $\dfrac{d}{dx}\left[\arctan(x)\right]=\dfrac{1}{1+x^2}.$
- We have $\dfrac{d}{dx}\left[x^r\right]=rx^{r-1}$ for any real number $r$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Diffinverse:Standard4`
:class: tudproof
**Derivatives of logarithms.** Consider the function $f(x)=\log_b(x)$. Then by {prf:ref}`Thm:Inverse:Logarithmbasechange`, we can write

$$
 f(x)=\log_b(x)=\frac{\ln(x)}{\ln(b)}.
$$

In the discussion preceding this theorem, we already found the derivative of the natural logarithm. Since $f$ is a constant multiple of this function, we find

$$
 f'(x)=\frac{1}{\ln(b)}\frac{d}{dx}[\ln(x)]=\dfrac{1}{\ln(b)x}.
$$

**Derivatives of inverse trigonometric functions.** Now we turn to the inverse trigonometric functions. For each of these functions, we will use {prf:ref}`Thm:SlopeCurves:IFT` to justify the use of implicit differentiation.

First consider the function $f(x)=\arcsin(x)$. Then the graph of $f$ is defined by the equation

$$
 y=\arcsin(x),
$$

which, for the relevant values of $x$ and $y$, is equivalent to

$$
 \sin(y)=x.
$$

We apply implicit differentiation to this equation and find

$$
 \cos(y)\frac{dy}{dx}=1.
$$

This gives

$$
 \frac{dy}{dx}=\frac{1}{\cos(y)}=\frac{1}{\cos(\arcsin(x))}.
$$

From {prf:ref}`Ex:Inverse:InversetrigSimplify` we know that we can simplify this expression to

$$
 f'(x)=\frac{dy}{dx}=\frac{1}{\cos(\arcsin(x))}=\frac{1}{\sqrt{1-x^2}},
$$

as desired. Now we consider $g(x)=\arccos(x)$. Then the equation

$$
 y=\arccos(x)
$$

is, for the relevant values of $x$ and $y$, equivalent to

$$
 \cos(y)=x.
$$

We use implicit differentiation to find

$$
 -\sin(y)\frac{dy}{dx}=1.
$$

This gives

$$
 \frac{dy}{dx}=\frac{-1}{\sin(y)}=\frac{-1}{\sin(\arccos(x))}=\frac{-1}{\sqrt{1-x^2}}.
$$

The final identity follows using a similar approach to {prf:ref}`Ex:Inverse:InversetrigSimplify`. Finally, we consider $h(x)=\arctan(x)$. Then the equation

$$
 y=\arctan(x)
$$

is, for the relevant values of $x$ and $y$, equivalent to

$$
 \tan(y)=x.
$$

We use implicit differentiation to find

$$
 \left(1+\tan^2(y)\right)\frac{dy}{dx}=1.
$$

This gives

$$
 \frac{dy}{dx}=\frac{1}{1+\tan^2(y)}=\frac{1}{1+x^2}.
$$

**Derivatives of powers of $x$**. As a consequence of our newly found derivatives, we can now also find the derivative of $f(x)=x^r$ where $r$ is any real number. For this, we note that $x=e^{\ln(x)}$ for any $x>0$. This means that we can write

$$
 x^r=\left(e^{\ln(x)}\right)^r=e^{r\ln(x)}.
$$

Now we can use the chain rule to find the derivative

$$
 f'(x)=e^{r\ln(x)}\frac{d}{dx}\left[r\ln(x)\right]=e^{r\ln(x)}\frac{r}{x}.
$$

Now we substitute back in $e^{r\ln(x)}=x^r$ to find

$$
 f'(x)=e^{r\ln(x)}\frac{r}{x}=x^r\frac{r}{x}=rx^{r-1}.
$$
:::

:::{note}
We have now found the derivatives of **all** standard functions. This means that we can find the derivative of any function that can be written as a combination of sums, products, quotients and compositions of any number of standard functions. The result will always be a combination of standard functions. Maybe this sounds unimpressive to you, but it actually is very impressive. Indeed, in {numref}`Chapter:Integration` we will study antiderivatives, which is the reverse concept of a derivative. There, we will see that for many functions like $f(x)=\sin\left(x^2\right)$ the antiderivative **cannot** be expressed as such a combination of standard functions.
:::

::::::{prf:example} 
:label: Ex:Diffinverse:Newdiff
Consider the function $f(x)=\dfrac{\log_2(x)}{\sqrt[3]{\arctan(x)}}$. We need all our newly found standard derivatives to find differentiate this function. First, we rewrite the function to

$$
 f(x)=\dfrac{\log_2(x)}{\sqrt[3]{\arctan(x)}}=\log_2(x)\left(\arctan(x)\right)^{-\frac{1}{3}}.
$$

Then we use the product rule to express the derivative as

$$
 f'(x)=\frac{1}{\ln(2)x}\left(\arctan(x)\right)^{-\frac{1}{3}}+\log_2(x)\frac{d}{dx}\left[\left(\arctan(x)\right)^{-\frac{1}{3}}\right].
$$

In order to evaluate this final derivative, we use the chain rule and we find

$$
 \begin{array}{lcl}f'(x)&=&\frac{1}{\ln(2)x}\left(\arctan(x)\right)^{-\frac{1}{3}}+\log_2(x)\frac{d}{dx}\left[\left(\arctan(x)\right)^{-\frac{1}{3}}\right]\\
 &=&\frac{1}{\ln(2)x}\left(\arctan(x)\right)^{-\frac{1}{3}}+\log_2(x)\left(-\frac{1}{3}\right)\left(\arctan(x)\right)^{-\frac{1}{3}-1}\frac{d}{dx}\left[\arctan(x)\right]\\
 &=&\frac{1}{\ln(2)x}\left(\arctan(x)\right)^{-\frac{1}{3}}-\frac{1}{3}\log_2(x)\left(\arctan(x)\right)^{-\frac{4}{3}}\frac{1}{1+x^2}\\
 &=&\frac{3\arctan(x)(1+x^2)-\log_2(x)\ln(2)x}{\ln(2)x(1+x^2)\left(\arctan(x)\right)^{\frac{4}{3}}}.\end{array}
$$
::::::

::::::{prf:example} 
:label: Ex:Diffinverse:Newdiff2
Consider the function $f(x)=x^x$. The way we found the derivative of $x^r$ for any real number $r$ can, in general, be applied when considering 'weird' powers of $x$. Indeed, we have for $x> 0$ that $x=e^{\ln(x)}$, so we can write

$$
 f(x)=x^x=\left(e^{\ln(x)}\right)^x=e^{\ln(x)x}.
$$

Then we can use the chain rule and the product rule to evaluate the derivative

$$
 f'(x)=e^{\ln(x)x}\left(\ln(x)\cdot 1+\frac{1}{x}x\right)=e^{\ln(x)x}\left(\ln(x)+1\right)=x^x\left(\ln(x)+1\right).
$$
::::::


## The inverse function theorem

In the proof of the previous theorem, we used implicit differentiation to find the derivatives of several functions that are defined as inverse functions. The following theorem, which is known as the inverse function theorem, justifies this approach and gives us a formula for the derivative of an inverse function in terms of the derivative of the original function.

::::::{prf:theorem} Inverse function theorem
:label: Thm:Diffinverse:IFT
Let $f$ be a continuously differentiable function. Let $a$ with $f'(a)\neq 0$ and write $b=f(a)$.

Then $f$ is invertible on an interval that contains $a$.

In addition, $f^{-1}$ is continuously differentiable on an interval that contains $b$ and we have

$$
 \left(f^{-1}\right)'(b)=\frac{1}{f'(a)}=\frac{1}{f'(f^{-1}(b))}.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Diffinverse:IFT`
:class: tudproof, dropdown
We assume that $f'(a)>0$ (the case where $f'(a)<0$ follows similarly). We write $\varepsilon=\frac{f'(a)}{2}>0$. Since $f'$ is continuous, we can find $\delta>0$ such that for the interval $(a-\delta,a+\delta)$ is contained in the domain of $f$ and such that for all $x$ with $0<|x-a|<\delta$ we have 

$$
 |f'(x)-f(a)|<\varepsilon=\frac{f'(a)}{2}.
$$

Then for any $x$ with $0<|x-a|<\delta$ we have 

$$
 -\frac{f'(a)}{2}< f'(x)-f(a)<\frac{f'(a)}{2},
$$

which means 

$$
 f'(x)>\frac{f'(a)}{2}>0.
$$

By {prf:ref}`Thm:Graphsderivatives:Increasingdecreasing`, the function $f$ is strictly increasing on $(a-\delta,a+\delta)$. So by {prf:ref}`Thm:Inverse:MonotonicOnetoone` the function $f$ must be invertible on this interval. In addition, we claim that $f$ maps the interval $(a-\delta,a+\delta)$ to the interval $(f(a-\delta),f(a+\delta))$. Since $f$ is strictly increasing on $(a-\delta,a+\delta)$, we have for any $a-\delta<x<a+\delta$ that

$$
 f(a-\delta)<f(x)<f(a+\delta).
$$

Now let $y$ in $(f(a-\delta),f(a+\delta))$. Since $f$ continuous on $[a-\delta,a+\delta]$ we can use {prf:ref}`Theorem:Continuity:IVT` to find $c$ in $(a-\delta,a+\delta)$ with $f(c)=y$. As such, $f$ indeed maps the interval $(a-\delta,a+\delta)$ to the interval $(f(a-\delta),f(a+\delta))$.

Now consider any $c$ in $(a-\delta,a+\delta)$ and let $d=f(c)$. We will show that $f^{-1}$ is differentiable in $d$. For this we first write

$$
 \frac{1}{f'(c)}=\frac{1}{\lim_{x\rightarrow c}\frac{f(x)-f(c)}{x-c}}=\lim_{x\rightarrow c}\frac{x-c}{f(x)-f(c)}=\lim_{x\rightarrow c}\frac{f^{-1}(f(x))-c}{f(x)-d}.
$$

We let $g(y)=\dfrac{f^{-1}(y)-c}{y-d}$. Then we note that $x\rightarrow c$ precisely when $f(x)\rightarrow d$. However, we do not know a priori that $g$ can be defined in such a way in $y=d$ to make it continuous, so we cannot use the regular substitution for limits. Instead, we use {prf:ref}`Theorem:Continuity:SubstitutionAlt` to obtain

\begin{align*}
 \frac{1}{f'(c)} &= \lim_{x\rightarrow c}\frac{f^{-1}(f(x))-c}{f(x)-d} \\
 &= \lim_{x\rightarrow c}g(f(x)) \\
 &= \lim_{y\rightarrow d}g(y) \\
 &= \lim_{y\rightarrow d}\frac{f^{-1}(y)-c}{y-d} \\
 &= \lim_{y\rightarrow d}\frac{f^{-1}(y)-f^{-1}(d)}{y-d} \\
 &= (f^{-1})'(d).
\end{align*}

So $f^{-1}$ is differentiable in $d$. Moreover, since $f'$ is continuous we see that $(f^{-1})'$ is continuous. In particular, when $c=a$ we have $d=b$ and we have

$$
 \left(f^{-1}\right)'(b)=\frac{1}{f'(a)}=\frac{1}{f'(f^{-1}(b))}.
$$

:::

:::{note}
{prf:ref}`Thm:Diffinverse:IFT` also justifies the differentiability of logarithms and inverse trigonometric functions, which we previously justified using {prf:ref}`Thm:SlopeCurves:IFT`, of which we have not given a proof of yet.
:::


Although we know that derivatives of all combinations of standard functions, {prf:ref}`Thm:Diffinverse:IFT` can still save us some work if we only want to find the derivative of an inverse function in one point.

::::::{prf:example} 
:label: Ex:Diffinverse:IFT
Consider the function $f(x)=\sqrt[5]{31+x^2}$. This function is not invertible on its entire domain, for instance, since $f(1)=f(-1)=\sqrt[5]{32}=2$. We can find its derivative by writing $f(x)=\left(31+x^2\right)^{\frac{1}{5}}$ and using the chain rule to evaluate

$$
 f'(x)=\frac{1}{5}\left(31+x^2\right)^{\frac{1}{5}-1}\left(0+2x\right)=\frac{2x}{5}\left(31+x^2\right)^{-\frac{4}{5}}.
$$

Then we notice that $f'(1)=\displaystyle \frac{2\cdot 1}{5}\cdot 32^{-\frac{4}{5}}=\frac{2}{5}\frac{1}{16}=\frac{1}{40}\neq 0$. So by {prf:ref}`Thm:Diffinverse:IFT`, $f$ is invertible on an open interval that contains $1$ and the inverse function $f^{-1}$ is differentiable on an open interval that contains $f(1)=2$ and we find that

$$
 \left(f^{-1}\right)'(2)=\frac{1}{f'(f^{-1}(2))}=\frac{1}{f'(1)}=\frac{1}{\frac{1}{40}}=40.
$$

::::::


::::::{prf:remark}
:label: Rem:Diffinverse:IFT1
The condition in {prf:ref}`Thm:Diffinverse:IFT` that $f'(a)\neq 0$ is necessary, even if we know that the function is invertible. Consider, for instance, $f(x)=(x-1)^3$. Then $f$ is strictly increasing on $\mathbb{R}$, so it is invertible with inverse function $f^{-1}(x)=\sqrt[3]{x}+1$. In addition, $f$ is differentiable on its domain with $f'(x)=3(x-1)^2$. Then we see that $f'(1)=0$. The inverse function is differentiable everywhere except in $x=0$ (for $x\neq 0$ we have $\left(f^{-1}\right)'(x)=\frac{1}{3}x^{-\frac{2}{3}}$, but the function has a vertical tangent in $x=0$). Since $f(1)=0$, $x=0$ is precisely the value of $x$ in the domain of $f^{-1}$ that corresponds to the value of $x$ in the domain of $f$ where the derivative of $f$ is $0$.

In fact, when $f$ is invertible on an open interval that contains $a$ and $f'(a)=0$, it is impossible for $f^{-1}$ to be differentiable in $a$. Indeed, if it were differentiable, for $x$ close to $a$ we have $(f^{-1}\circ f)(x)=x$, so we would find that

$$
 \left(f^{-1}\circ f\right)'(a)=\left.\frac{d}{dx}[x]\right|_{x=a}=\left.1\right|_{x=a}=1.
$$

However, with the chain rule, we would obtain

$$
 \left(f^{-1}\circ f\right)(a)=\left(f^{-1}\right)'(f(a))f'(a)=0,
$$

which gives a contradiction. So $f^{-1}$ can never be invertible in $a$.


::::::


::::::{prf:remark}
:label: Rem:Diffinverse:IFT2
The condition in {prf:ref}`Thm:Diffinverse:IFT` that the derivative of $f$ is continuous is also necessary. Consider the function 

$$
 f(x)=\left\{\begin{array}{l}-x+4x^2\sin\left(\frac{1}{x}\right),\qquad&\text{if}\ x\neq 0\\
 0,&\text{if}\ x=0.\end{array}\right.
$$

Then for $x\neq 0$, we can use the product rule and the chain rule to find

$$
 f'(x)=-1+8x\sin\left(\frac{1}{x}\right)+4x^2\cos\left(\frac{1}{x}\right)\frac{-1}{x^2}=-1+8x\sin\left(\frac{1}{x}\right)-4\cos\left(\frac{1}{x}\right).
$$

For $x=0$, we use the limit definition of the derivative to find

$$
 f'(0)=\lim_{h\rightarrow 0}\frac{f(h)-f(0)}{h}=\lim_{h\rightarrow 0}\frac{-h+4h^2\sin\left(\frac{1}{h}\right)}{h}=\lim_{h\rightarrow 0}-1+4h\sin\left(\frac{1}{h}\right).
$$

We can evaluate this limit using the squeeze theorem ({prf:ref}`Theorem:LimitAtPoint:Squeezetheorem`). Indeed, we notice that since the sine is always in between $-1$ and $1$, we have

$$
 -1-4|h|\leq -1+4h\sin\left(\frac{1}{h}\right)\leq -1+4|h|
$$

for all values of $h$. Since we have $\displaystyle\lim_{h\rightarrow 0}-1-4|h|=\lim_{h\rightarrow 0}-1+4|h|=-1$, we obtain with the squeeze theorem that

$$
 f'(0)=\lim_{h\rightarrow 0}-1+4h\sin\left(\frac{1}{h}\right)=-1.
$$

Note that the derivative is not continuous in $0$. Indeed, with the squeeze theorem we do have $\displaystyle \lim_{x\rightarrow 0}-1+8x\sin\left(\frac{1}{x}\right)=-1$, but the limit $\displaystyle \lim_{x\rightarrow 0}-4\cos\left(\frac{1}{x}\right)$ does not exist as the cosine keeps oscillating between $-4$ and $4$. 

The function $f$ is also not invertible in any interval that contains $0$. Indeed, the derivative $f'(x)=-1+2x\sin\left(\frac{1}{x}\right)-4\cos\left(\frac{1}{x}\right)$ will both take on positive and negative values on any interval that contains $0$, as $-4\cos\left(\frac{1}{x}\right)$ keeps on oscillating between $-4$ and $4$, while $-1+2x\sin\left(\frac{1}{x}\right)$ approaches $-1$ as $x\rightarrow 0$. So the function $f$ will alternate between strictly increasing and strictly decreasing on any such interval, which means that it cannot be invertible there.

:::{figure} Images/Fig-Diffinverse-IFT2.png
:name: Fig:Diffinverse:IFT2

The graph of the function $f$ from {prf:ref}`Rem:Diffinverse:IFT2`.
:::

:::{todo}
Replace the graph in {numref}`Fig:Diffinverse:IFT2` with an applet.
:::
:::

::::

## Grasple exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/665beea4-a04e-43b2-936b-11058bea3f4c?id=69707
:label: Grasple:69707
:dropdown:
:description: Evaluating limits by recognising them as derivatives

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d8bc5cfb-cbe3-4a9b-ba66-c1ba8922a285?id=69711
:label: Grasple:69711
:dropdown:
:description: Evaluating limits by recognising them as derivatives

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1da4667f-95a5-4740-a27f-726cf53655b3?id=71390
:label: Grasple:71390
:dropdown:
:description: Determining differentiability

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ce40519e-7e93-4243-9d8d-9b83c5ee718c?id=71391
:label: Grasple:71391
:dropdown:
:description: Determining differentiability

