(Subsec:Invdiff)=

# Derivatives of inverse functions

## Introduction


One important ingredient still missing from our differentiation toolbox is a way to find the derivatives of the standard functions that have not been covered yet: logarithms, inverse trigonometric functions and non-integer powers of $x$. To recall, we have found the derivatives of the other standard functions in {prf:ref}`Thm:Differentiability:Standard1`, {prf:ref}`Thm:Chain rule:Standard2` and {prf:ref}`Thm:Productquotientrule:Standard3`. So without further ado, let us get to work and find these derivatives.


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
  \frac{d}{dx}e^y=\frac{d}{dx}x=1.
$$

In order to find $\frac{d}{dx}e^y$, we remember that $y$ is a function of $x$, so we can use the chain rule to obtain the equation

$$
 e^y\frac{dy}{dx}=1.
$$

This equation can be solved for $\dfrac{dy}{dx}$ and we obtain

$$
 \frac{dy}{dx}=\frac{1}{e^y}.
$$

Now we recall that $e^y=x$, and we conclude that

$$
 \frac{d}{dx}\ln(x)=\frac{dy}{dx}=\frac{1}{e^y}=\frac{1}{x}.
$$

So, perhaps surprisingly, we have found that the derivative of the natural logarithm is the reciprocal function. 

Now that we know what our approach should be, let us determine the derivatives of the remaining standard functions.

::::::{prf:theorem} Standard derivatives, part 4 out of 4
:label: Thm:Diffinverse:Standard4
We have the following standard derivatives:

- $\dfrac{d}{dx}\log_b(x)=\dfrac{1}{\ln(b)x}$ for any $b>0$ with $b\neq 1$; in particular, we have $\dfrac{d}{dx}\ln(x)=\dfrac{1}{x}$;
- $\dfrac{d}{dx}\arcsin(x)=\dfrac{1}{\sqrt{1-x^2}}$;
- $\dfrac{d}{dx}\arccos(x)=\dfrac{-1}{\sqrt{1-x^2}}$;
- $\dfrac{d}{dx}\arctan(x)=\dfrac{1}{1+x^2}$;
- $\dfrac{d}{dx}x^r=rx^{r-1}$ for any real number $r$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Diffinverse:Standard4`
:class: tudproof
**Derivatives of logarithms.** Consider the function $f(x)=\log_b(x)$. Then by {prf:ref}`Thm:Inverse:Logarithmbasechange`, we can write

$$
 f(x)=\log_b(x)=\frac{\ln(x)}{\ln(b)}.
$$

In the discussion preceding this theorem, we already found the derivative of the natural logarithm. Since $f$ is a constant multiple of this function, we find

$$
 f'(x)=\frac{1}{\ln(b)}\frac{d}{dx}\ln(x)=\dfrac{1}{\ln(b)x}.
$$

**Derivatives of inverse trigonometric functions.** Now we turn to the inverse trigonometric functions. For each of these functions, we will use {prf:ref}`Thm:SlopeCurves:IFT` to justify the use of implicit differentiation.

First, we consider the arcsine function. Then its graph is defined by the equation

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
 \frac{d}{dx}\arcsin(x)=\frac{dy}{dx}=\frac{1}{\cos(\arcsin(x))}=\frac{1}{\sqrt{1-x^2}},
$$

as desired. 

Now we the arccosine function. Then the equation

$$
 y=\arccos(x)
$$

is, for the relevant values of $x$ and $y$, equivalent to

$$
 \cos(y)=x.
$$

We again use implicit differentiation to find

$$
 -\sin(y)\frac{dy}{dx}=1.
$$

This gives

$$
 \frac{d}{dx}\arccos(x)=\frac{dy}{dx}=\frac{-1}{\sin(y)}=\frac{-1}{\sin(\arccos(x))}=\frac{-1}{\sqrt{1-x^2}}.
$$

The final identity follows using a similar approach to {prf:ref}`Ex:Inverse:InversetrigSimplify`. 

Finally, we consider the arctangent function. Then the equation

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
 \frac{d}{dx}\arctan(x)=\frac{dy}{dx}=\frac{1}{1+\tan^2(y)}=\frac{1}{1+x^2}.
$$

**Derivatives of powers of $x$**. As a consequence of our newly found derivatives, we can now also find the derivative of the power function $x^r$ for $x>0$ where $r$ is any real number. For this, we note that $x=e^{\ln(x)}$ for any $x>0$. This means that we can write

$$
 x^r=\left(e^{\ln(x)}\right)^r=e^{r\ln(x)}.
$$

Now we can use the chain rule to find the derivative

$$
 \frac{d}{dx}x^r=e^{r\ln(x)}\frac{d}{dx}r\ln(x)=e^{r\ln(x)}\frac{r}{x}.
$$

Now we substitute $e^{r\ln(x)}=x^r$ back in to find

$$
 \frac{d}{dx}x^r=e^{r\ln(x)}\frac{r}{x}=x^r\frac{r}{x}=rx^{r-1}.
$$
:::

:::{note}
We have now found the derivatives of **all** standard functions. This means that we can find the derivative of any function that can be written as a combination of sums, products, quotients and compositions of any number of standard functions. The result will always be a combination of standard functions. Maybe this sounds unimpressive to you, it is a very important result. Indeed, in {numref}`Chapter:Integration` we will study antiderivatives, which is the reverse concept of a derivative. There, we will see that for many functions like $f(x)=\sin\left(x^2\right)$ the antiderivative **cannot** be expressed as such a combination of standard functions.
:::

::::::{prf:example} 
:label: Ex:Diffinverse:Newdiff
Consider the function $f(x)=\dfrac{\log_2(x)}{\sqrt[3]{\arctan(x)}}$. We need all our newly found standard derivatives to differentiate this function. First, we rewrite the function to

$$
 f(x)=\dfrac{\log_2(x)}{\sqrt[3]{\arctan(x)}}=\log_2(x)\left(\arctan(x)\right)^{-\frac{1}{3}}.
$$

Then we use the product rule to express the derivative as

$$
 f'(x)=\frac{1}{\ln(2)x}\left(\arctan(x)\right)^{-\frac{1}{3}}+\log_2(x)\frac{d}{dx}\left(\left(\arctan(x)\right)^{-\frac{1}{3}}\right).
$$

In order to evaluate this final derivative, we use the chain rule and we find

$$
 \begin{array}{lcl}f'(x)&=&\displaystyle\frac{1}{\ln(2)x}\left(\arctan(x)\right)^{-\frac{1}{3}}+\log_2(x)\frac{d}{dx}\left(\left(\arctan(x)\right)^{-\frac{1}{3}}\right)\\[0.1cm]
 &=&\displaystyle\frac{1}{\ln(2)x}\left(\arctan(x)\right)^{-\frac{1}{3}}+\log_2(x)\left(-\frac{1}{3}\right)\left(\arctan(x)\right)^{-\frac{1}{3}-1}\frac{d}{dx}\arctan(x)\\[0.1cm]
 &=&\displaystyle\frac{1}{\ln(2)x}\left(\arctan(x)\right)^{-\frac{1}{3}}-\frac{1}{3}\log_2(x)\left(\arctan(x)\right)^{-\frac{4}{3}}\frac{1}{1+x^2}\\[0.1cm]
 &=&\displaystyle\frac{3\arctan(x)(1+x^2)-\log_2(x)\ln(2)x}{3\ln(2)x(1+x^2)\left(\arctan(x)\right)^{\frac{4}{3}}}\\[0.1cm]
 &=&\displaystyle\frac{3\arctan(x)(1+x^2)-\ln(x)x}{3\ln(2)x(1+x^2)\left(\arctan(x)\right)^{\frac{4}{3}}}.\end{array}
$$
::::::

::::::{prf:example} 
:label: Ex:Diffinverse:Newdiff2
Consider the function $f(x)=x^x$. The way we found the derivative of $x^r$ for any real number $r$ can, in general, be applied when considering exponents that are functions. Indeed, we have for $x> 0$ that $x=e^{\ln(x)}$, so we can write

$$
 f(x)=x^x=\left(e^{\ln(x)}\right)^x=e^{\ln(x)x}.
$$

Then we can use the chain rule and the product rule to evaluate the derivative

$$
 f'(x)=e^{\ln(x)x}\left(\ln(x)\cdot 1+\frac{1}{x}x\right)=e^{\ln(x)x}\left(\ln(x)+1\right)=x^x\left(\ln(x)+1\right).
$$
::::::

For some functions, it is easier to differentiate the logarithm of a function than the function itself. This usually happens when the function is a product of several functions or if powers of functions are involved. This technique, which is called **logarithmic differentiation** relies on the following result.

::::::{prf:theorem} 
:label: Thm:Diffinverse:Logdiff
For any positive, differentiable function $f$ we have

$$
 f'(x)=f(x)\frac{d}{dx}\ln(f(x)).
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Diffinverse:Logdiff`
:class: tudproof

By the chain rule, we have

$$
 \frac{d}{dx}\ln(f(x))=\frac{f'(x)}{f(x)},
$$

from which the desired identity follows directly.
::: 




::::::{prf:example} Logarithmic differentiation
:label: Ex:Diffinverse:Logdiff


To illustrate logarithmic differentiation, we consider the function $f(x)=x^3\left(g(x)\right)^4\left(h(x)\right)^5$ for some positive, differentiable functions $g$ and $h$. To differentiate this function, the product rule can be used, but differentiating the logarithm is quicker.  Using {prf:ref}`Thm:Diffinverse:Logdiff`, we find for $x>0$

$$
 \frac{d}{dx}\left(x^3\left(g(x)\right)^4\left(h(x)\right)^5\right)=x^3\left(g(x)\right)^4\left(h(x)\right)^5\frac{d}{dx}\ln\left(x^3\left(g(x)\right)^4\left(h(x)\right)^5\right).
$$

The reason why the derivative $\displaystyle\frac{d}{dx}\ln\left(x^3\left(g(x)\right)^4\left(h(x)\right)^5\right)$ is easier to evaluate than the original derivative is that we can use the standard computation rule for the logarithm to split the logarithm of a product into the sum of logarithms. In addition, we can take out the powers. We then obtain

\begin{align*}

 \frac{d}{dx}\left(x^3\left(g(x)\right)^4\left(h(x)\right)^5\right)&=x^3\left(g(x)\right)^4\left(h(x)\right)^5\frac{d}{dx}\ln\left(x^3\left(g(x)\right)^4\left(h(x)\right)^5\right)\\
 &=x^3\left(g(x)\right)^4\left(h(x)\right)^5\frac{d}{dx}\left(3\ln(x)+4\ln(g(x))+5\ln(h(x))\right)\\
 &=x^3\left(g(x)\right)^4\left(h(x)\right)^5\left(\frac{3}{x}+\frac{4g'(x)}{g(x)}+\frac{5h'(x)}{h(x)}\right).

\end{align*}

::::::

::::{question}
:type: multiple-choice
:variant: single-select
:admonition:
:class: question
:showanswer:
:columns: 1
Let $f$ be a positive differentiable function and let $g$ be any differentiable function. What is  $\displaystyle \frac{d}{dx}f(x)^{g(x)}$?
---
[ ] $\displaystyle f(x)^{g(x)-1}f'(x)$
> It seems you applied the ordinary power rule and treated the exponent as if it were a constant. However, the exponent $g(x)$ also depends on $x$, so you need to account for how it changes as well.

[ ] $\displaystyle f(x)^{g(x)-1}g'(x)$
> It seems you may have mixed up the roles of the base and the exponent. The factor $f(x)^{g(x)-1}$ comes from differentiating with respect to the base, while $g'(x)$ measures the change in the exponent. Since both depend on $x$, a simple power rule is not sufficient.


[ ] $\displaystyle f(x)^{g(x)}g'(x)$
> It looks like you recognized that the exponent $g(x)$ changes with $x$, but you may not have accounted for the fact that the base $f(x)$ changes as well. Also, differentiating a variable exponent introduces a factor of $\ln(f(x))$.

[x] $\displaystyle f(x)^{g(x)-1}g(x)f'(x)+f(x)^{g(x)}\ln(f(x))g'(x)$
> We use logarithmic differentiation. We can evaluate

\begin{align*}
 \frac{d}{dx}f(x)^{g(x)}&=f(x)^{g(x)}\frac{d}{dx}\ln\left(f(x)^{g(x)}\right)\\
 &=f(x)^{g(x)}\frac{d}{dx}\left(g(x)\ln\left(f(x)\right)\right)\\
 &=f(x)^{g(x)}\left(g(x)\frac{f'(x)}{f(x)}+g'(x)\ln\left(f(x)\right)\right)\\
 &=f(x)^{g(x)-1}g(x)f'(x)+f(x)^{g(x)}\ln(f(x))g'(x).
\end{align*}

In this computation, we used the product rule.
[ ] $\displaystyle f(x)^{g(x)-1}g(x)f'(x)+f(x)^{g(x)}g'(x)$
> It seems you correctly accounted for the changing base in the first term. However, when differentiating the exponent, you may have forgotten the factor $\ln(f(x))$, which appears when using logarithmic differentiation.
---
::::


## The inverse function theorem

In the proof of the previous theorem, we used implicit differentiation to find the derivatives of several functions that are defined as inverse functions. The following theorem, which is known as the inverse function theorem, justifies this approach and gives us a formula for the derivative of an inverse function in terms of the derivative of the original function.

::::::{prf:theorem} Inverse function theorem
:label: Thm:Diffinverse:IFT
Let $f$ be a continuously differentiable function. Consider $a$ in the domain of $f$ with $f'(a)\neq 0$ and write $b=f(a)$.

Then there is an open interval containing $a$ on which $f$ is invertible.

In addition, $f^{-1}$ is continuously differentiable on an open interval that contains $b$ and on this interval we have

$$
 \left(f^{-1}\right)'(b)=\frac{1}{f'(a)}=\frac{1}{f'(f^{-1}(b))}.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Diffinverse:IFT`
:class: tudproof, dropdown
We assume that $f'(a)>0$ (the case where $f'(a)<0$ follows similarly). First, we show that there is an open interval containing $a$ where $f'$ is positive. We let $\varepsilon=\frac{f'(a)}{2}>0$. Since $f'$ is continuous, we can find $\delta>0$ such that the interval $(a-\delta,a+\delta)$ is contained in the domain of $f$ and such that for all $x$ with $0<|x-a|<\delta$ we have 

$$
 |f'(x)-f'(a)|<\varepsilon=\frac{f'(a)}{2}.
$$

Then for any $x$ with $0<|x-a|<\delta$ we have 

$$
 -\frac{f'(a)}{2}< f'(x)-f'(a)<\frac{f'(a)}{2},
$$

which means 

$$
 f'(x)>\frac{f'(a)}{2}>0.
$$

By {prf:ref}`Thm:MinMax:Increasingdecreasing`, the function $f$ is strictly increasing on $(a-\delta,a+\delta)$. So by {prf:ref}`Thm:Inverse:MonotonicOnetoone` the function $f$ must be invertible on this interval. In addition, we claim that $f$ maps the interval $(a-\delta,a+\delta)$ to the interval $(f(a-\delta),f(a+\delta))$. Since $f$ is strictly increasing on $(a-\delta,a+\delta)$, we have for any $a-\delta<x<a+\delta$ that

$$
 f(a-\delta)<f(x)<f(a+\delta).
$$

Now let $y$ in $(f(a-\delta),f(a+\delta))$. Since $f$ continuous on $[a-\delta,a+\delta]$ we can use {prf:ref}`Theorem:Continuity:IVT` to find $c$ in $(a-\delta,a+\delta)$ with $f(c)=y$. As such, $f$ indeed maps the interval $(a-\delta,a+\delta)$ to the interval $(f(a-\delta),f(a+\delta))$.

Now consider any $c$ in $(a-\delta,a+\delta)$ and let $d=f(c)$. We will show that $f^{-1}$ is differentiable at $d$. Since $f'(c)\neq0$, we find

$$
 \frac{1}{f'(c)}=\frac{1}{\lim\limits_{x\rightarrow c}\frac{f(x)-f(c)}{x-c}}=\lim_{x\rightarrow c}\frac{x-c}{f(x)-f(c)}=\lim_{x\rightarrow c}\frac{f^{-1}(f(x))-c}{f(x)-d}.
$$

We let $g(y)=\dfrac{f^{-1}(y)-c}{y-d}$ for $y$ in $(f(a-\delta),f(a+\delta))$ with $y\neq d$. Then we note that $x\rightarrow c$ precisely when $f(x)\rightarrow d$. However, we do not know a priori that $g$ can be defined in such a way at $y=d$ to make it continuous, so we cannot use the regular substitution for limits. Instead, we use {prf:ref}`Theorem:Continuity:SubstitutionAlt` to obtain

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
{prf:ref}`Thm:Diffinverse:IFT` also justifies the differentiability of logarithms and inverse trigonometric functions, which we previously justified using {prf:ref}`Thm:SlopeCurves:IFT`, of which we have not given a proof yet.
:::


Although we know that derivatives of all combinations of standard functions, {prf:ref}`Thm:Diffinverse:IFT` can still save us some work if we only want to find the derivative of an inverse function in one point.

::::::{prf:example} 
:label: Ex:Diffinverse:IFT
Consider the function $f(x)=5\sqrt[5]{31+x^2}$. This function is not invertible on its entire domain, since $f(1)=f(-1)=5\sqrt[5]{32}-8=2$. We will show that it is invertible on an open interval that contains $1$. We can find its derivative by writing $f(x)=5\left(31+x^2\right)^{\frac{1}{5}}-8$ and using the chain rule to evaluate

$$
 f'(x)=\frac{5}{5}\left(31+x^2\right)^{\frac{1}{5}-1}\left(0+2x\right)=2x\left(31+x^2\right)^{-\frac{4}{5}}.
$$

Then we notice that $f'(1)=\displaystyle (2\cdot 1)\cdot 32^{-\frac{4}{5}}=\frac{2}{16}=\frac{1}{8}\neq 0$. So by {prf:ref}`Thm:Diffinverse:IFT`, $f$ is invertible on an open interval that contains $1$ and the inverse function $f^{-1}$ is differentiable on an open interval that contains $f(1)=2$ and we find that

$$
 \left(f^{-1}\right)'(2)=\frac{1}{f'(f^{-1}(2))}=\frac{1}{f'(1)}=\frac{1}{\frac{1}{8}}=8.
$$

In addition, we notice that $f'(-1)=\displaystyle (2\cdot (-1))\cdot 32^{-\frac{4}{5}}=\frac{-2}{16}=\frac{-1}{8}\neq 0$. So $f$ is also invertible on an open interval that contains $-1$. Since $f$ is not invertible on its entire domain, this inverse function will not be the same as the one around $1$. So if we denote the inverse function of $f$ on the open interval around $-1$ by $\tilde{f}^{-1}$, we find that $\tilde{f}^{-1}$ is differentiable on an open interval that contains $f(-1)=2$ and we find that

$$
 \left(\tilde{f}^{-1}\right)'(2)=\frac{1}{f'(\tilde{f}^{-1}(2))}=\frac{1}{f'(-1)}=\frac{1}{\frac{-1}{8}}=-8.
$$

{numref}`Fig:Diffinverse:IFT` shows the graph of the function $f$ and the tangent lines at the points $-1$ and $1$. The slopes of these tangent lines are precisely the values of $f'(-1)$ and $f'(1)$, which we used to find the derivatives of the inverse functions at $2$.

:::{applet}
:url: calculus/derivatives_of_inverse_functions/inverse_function_theorem
:name: Fig:Diffinverse:IFT
:class: dark-light

The graph of the function $f(x)=5\sqrt[5]{31+x^2}-8$ and the tangent lines at the points $-1$ and $1$ are also shown. By dragging the left and/or right point, can you find a point at which {prf:ref}`Thm:Diffinverse:IFT` does not apply? What happens to the slope of the tangent line at that point?
:::

::::::

::::{question}
:type: multiple-choice
:variant: single-select
:admonition:
:class: question
:showanswer:


Let $f(x)=5\sqrt[5]{31+x^2}-8$ as in {prf:ref}`Ex:Diffinverse:IFT`. Restrict $f$ to the open interval containing $1$ on which it is invertible. What is the explicit formula for the inverse function $f^{-1}(x)$? Does the derivative $\left(\tilde{f}^{-1}\right)'(2)$ match the one found in {prf:ref}`Ex:Diffinverse:IFT`?
---
[ ] $f^{-1}(x)=\pm\sqrt{\left(\frac{x+8}{5}\right)^5-31}$
> This expression is not a function because it gives two possible outputs for most inputs.

[x] $f^{-1}(x)=\sqrt{\left(\frac{x+8}{5}\right)^5-31}$
> Correct! Solving $y=5\sqrt[5]{31+x^2}-8$ for $x$ gives $x=\pm\sqrt{\left(\frac{y+8}{5}\right)^5-31}$. Since the inverse is taken on the branch containing $1$, we choose the positive square root. The derivative of this function is given by

$$
 \left(f^{-1}\right)'(x)=\frac{(x+8)^4}{1250\sqrt{\left(\frac{x+8}{5}\right)^5-31}}.
$$

Plugging in $x=2$ gives

$$
 \left(f^{-1}\right)'(2)=\frac{(2+8)^4}{1250\sqrt{\left(\frac{2+8}{5}\right)^5-31}}=8,
$$

which matches the answer from {prf:ref}`Ex:Diffinverse:IFT`.

[ ] $f^{-1}(x)=-\sqrt{\left(\frac{x+8}{5}\right)^5-31}$
> This is the inverse corresponding to the branch containing $-1$, not the interval containing $1$.

[ ] $f^{-1}(x)=\left(\frac{x+8}{5}\right)^5-31$
> Be careful: this expression equals $x^2$, not $x$. You still need to take a square root.
---
::::


::::::{prf:remark}
:label: Rem:Diffinverse:IFT1
The condition in {prf:ref}`Thm:Diffinverse:IFT` that $f'(a)\neq 0$ is necessary, even if we know that the function is invertible. Consider, for instance, $f(x)=(x-1)^3$. Then $f$ is strictly increasing on $\mathbb{R}$, so it is invertible with inverse function $f^{-1}(x)=\sqrt[3]{x}+1$. In addition, $f$ is differentiable on its domain with $f'(x)=3(x-1)^2$. Then we see that $f'(1)=0$. The inverse function is differentiable everywhere except at $x=0$ (for $x\neq 0$ we have $\left(f^{-1}\right)'(x)=\frac{1}{3}x^{-\frac{2}{3}}$, but the function has a vertical tangent line at $x=0$). Since $f(1)=0$, $x=0$ is precisely the value of $x$ in the domain of $f^{-1}$ that corresponds to the value of $x$ in the domain of $f$ where the derivative of $f$ is $0$.

In fact, when $f$ is invertible on an open interval that contains $a$ and $f'(a)=0$, it is impossible for $f^{-1}$ to be differentiable at $a$. Indeed, if it were differentiable, for $x$ close to $a$ we have $(f^{-1}\circ f)(x)=x$, so we would find that

$$
 \left(f^{-1}\circ f\right)'(a)=\left.\frac{d}{dx}x\right|_{x=a}=\left.1\right|_{x=a}=1.
$$

However, with the chain rule, we would obtain

$$
 \left(f^{-1}\circ f\right)(a)=\left(f^{-1}\right)'(f(a))f'(a)=0,
$$

which gives a contradiction. So $f^{-1}$ can never be differentiable at $a$.

:::{applet}
:url: calculus/derivatives_of_inverse_functions/failure_of_inverse_function_theorem
:name: Fig:Diffinverse:verthor
:class: dark-light

If $f$ has a horizontal tangent line at $a$, then $f^{-1}$ has a vertical tangent line at $f(a)$.
:::

::::::


::::::{prf:remark}
:label: Rem:Diffinverse:IFT2
In {prf:ref}`Thm:Diffinverse:IFT`, the condition that the derivative of $f$ is continuous is necessary. Consider the function 

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
 f'(0)=\lim_{h\rightarrow 0}\frac{f(h)-f(0)}{h}=\lim_{h\rightarrow 0}\frac{-h+4h^2\sin\left(\frac{1}{h}\right)}{h}=\lim_{h\rightarrow 0}\left(-1+4h\sin\left(\frac{1}{h}\right)\right).
$$

We can evaluate this limit using the squeeze theorem ({prf:ref}`Theorem:LimitAtPoint:Squeezetheorem`). Indeed, we notice that since the sine is always between $-1$ and $1$, we have

$$
 -1-4|h|\leq -1+4h\sin\left(\frac{1}{h}\right)\leq -1+4|h|
$$

for all values of $h$. Since we have $\displaystyle\lim_{h\rightarrow 0}\left(-1-4|h|\right)=\lim_{h\rightarrow 0}\left(-1+4|h|\right)=-1$, we obtain with the squeeze theorem that

$$
 f'(0)=\lim_{h\rightarrow 0}\left(-1+4h\sin\left(\frac{1}{h}\right)\right)=-1.
$$

Note that the derivative is not continuous in $0$. Indeed, with the squeeze theorem we do have $\displaystyle \lim_{x\rightarrow 0}\left(-1+8x\sin\left(\frac{1}{x}\right)\right)=-1$, but $\displaystyle \lim_{x\rightarrow 0}-4\cos\left(\frac{1}{x}\right)$ does not exist as the cosine keeps oscillating between $-1$ and $1$. 

The function $f$ is also not invertible in any interval that contains $0$. Indeed, the derivative $\displaystyle f'(x)=-1+8x\sin\left(\frac{1}{x}\right)-4\cos\left(\frac{1}{x}\right)$ will take on both positive and negative values on any interval that contains $0$, as $\displaystyle -4\cos\left(\frac{1}{x}\right)$ keeps on oscillating between $-4$ and $4$, while $\displaystyle -1+2x\sin\left(\frac{1}{x}\right)$ approaches $-1$ as $x\rightarrow 0$. So the function $f$ will alternate between strictly increasing and strictly decreasing on any such interval, which means that it cannot be invertible there.

:::{applet}
:url: calculus/derivatives_of_inverse_functions/failure_of_inverse_function_theorem_2
:name: Fig:Diffinverse:IFT2
:class: dark-light

The graph of the function $f$ and its derivative $f'$ from {prf:ref}`Rem:Diffinverse:IFT2`.
:::

::::::

## Grasple exercises


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/79142901-fa54-4bc5-b81d-ca8b884fde0a?id=63418
:label: Grasple:63418
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5d112029-4427-4231-b436-0ad066c52451?id=63434
:label: Grasple:63434
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fc0c7b54-8e58-4445-b714-fcba02547108?id=63426
:label: Grasple:63426
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/516b4eaf-f83e-491f-adbd-d50b17601ac3?id=63424
:label: Grasple:63424
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a1719639-a441-47a9-a648-b84502165ad1?id=63427
:label: Grasple:63427
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1ef694a5-28e8-4324-8d93-f186a0c79689?id=63431
:label: Grasple:63431
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a48a374e-0e7d-40f7-a159-f4530fcdc631?id=63423
:label: Grasple:63423
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d57df9e2-3592-4b25-bf28-e922a4365aa5?id=71396
:label: Grasple:71396
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/81f5b367-145a-4e6f-991e-805b45970b41?id=75355
:label: Grasple:75355
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/46e1acb0-7381-4296-a702-cf4186c7a004?id=75356
:label: Grasple:75356
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/77d668b9-c9db-4e2e-9e85-1a4076031989?id=75357
:label: Grasple:75357
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7407875d-6d46-43b2-8478-31951387cfb1?id=75359
:label: Grasple:75359
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c67c5ab4-a17c-499e-bda6-de7a35cc812f?id=75358
:label: Grasple:75358
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b7d4d8ec-b239-4853-a95c-4323237b952a?id=63425
:label: Grasple:63425
:dropdown:
:description: Find the derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7fab8c83-125e-46b6-8f2d-d35d73be216d?id=63523
:label: Grasple:63523
:dropdown:
:description: Find two derivatives.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0e6d567d-6864-452c-82d7-e18e919a49a3?id=63499
:label: Grasple:63499
:dropdown:
:description: Find two derivatives.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f31e7b5a-eddd-4c5b-9810-89028f25268f?id=116604
:label: Grasple:116604
:dropdown:
:description: Find an equation for the tangent line.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3be5d836-7913-4deb-a69d-7700bb50839d?id=70863
:label: Grasple:70863
:dropdown:
:description: Find an equation for the tangent line.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fb1e22f8-e467-4d58-8f0d-693591f66b9e?id=116603
:label: Grasple:116603
:dropdown:
:description: Find an equation for the tangent line.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6047b2d2-5728-4a90-b72d-d4d205800d83?id=75360
:label: Grasple:75360
:dropdown:
:description: Simplifying an expression with inverse trigonometric functions.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/665beea4-a04e-43b2-936b-11058bea3f4c?id=69707
:label: Grasple:69707
:dropdown:
:description: Evaluating limits by recognising them as derivatives.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d8bc5cfb-cbe3-4a9b-ba66-c1ba8922a285?id=69711
:label: Grasple:69711
:dropdown:
:description: Evaluating limits by recognising them as derivatives.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1da4667f-95a5-4740-a27f-726cf53655b3?id=71390
:label: Grasple:71390
:dropdown:
:description: Determining differentiability.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ce40519e-7e93-4243-9d8d-9b83c5ee718c?id=71391
:label: Grasple:71391
:dropdown:
:description: Determining differentiability.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e9c2623c-678d-4454-ad7e-3f17ca8b1c90?id=63552
:label: Grasple:63552
:dropdown:
:description: Finding derivative of inverse function using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/34dbc780-717e-4e1a-86fb-c8bab327e42b?id=63605
:label: Grasple:63605
:dropdown:
:description: Finding derivative of inverse function using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ec0f5db9-22c4-489c-8c82-831a53f4a4d5?id=63609
:label: Grasple:63609
:dropdown:
:description: Finding derivative of inverse function using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b7717945-c351-4083-bbfe-94da7ac1f8df?id=63611
:label: Grasple:63611
:dropdown:
:description: Using the inverse function theorem.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/eb9ad8a4-10be-4cec-ba9a-d9731f7dc0d5?id=63542
:label: Grasple:63542
:dropdown:
:description: Using the inverse function theorem.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/73fba58a-b366-4c0a-bd31-fdb8a3020bde?id=63543
:label: Grasple:63543
:dropdown:
:description: Using the inverse function theorem.
::::