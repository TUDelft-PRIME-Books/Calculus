(Section:DiffProdQuot)=

# Product and quotient rule

## Introduction

:::::{margin}
:::{figure} Images/Fig-ProductQuotient-Pyramid.png
---
width: 100%
name: Fig:ProductQuotient:Pyramid
class: dark-light
---
A pyramid with rectangular cross section at position $x$.
:::
:::::

:::{todo}
Replace {numref}`Fig:ProductQuotient:Pyramid` with an applet.
:::

Consider a pyramid with a rectangular base. Suppose we take a cross section at distance $x$ from the top of the pyramid. Then we obtain a rectangle with width $w(x)$ and length $\ell(x)$, see {numref}`Fig:ProductQuotient:Pyramid`. What is the area $A$ of this rectangle? You do not need advanced calculus for this to know that the answer is 


$$
 A(x)=w(x)\ell(x).
$$



What happens now if we go a little bit further, say that we take a step of size $\Delta x$? Then the width changes from $w(x)$ to $w(x+\Delta x)$. If $\Delta x$ is sufficiently small, this difference $\Delta w=w(x+\Delta x)-w(x)$ is very close to $w'(x)\Delta x$ (in the sense that $\lim\limits_{\Delta x\rightarrow 0}\dfrac{w(x+\Delta x)-w(x)}{\Delta x}=w'(x)$). Similarly, the change in length $\Delta \ell=\ell(x+\Delta x)-\ell(x)$ is approximately equal to $\ell'(x)\Delta x$. So what happens with the area? Intuitively, we might expect the rate of change of this area to be $w'(x)\ell'(x)$, but this is not correct as we will see soon. For this, we take a look at the sketch of the cross section at distance $x+\Delta x$ from the top, see {numref}`Fig:ProductQuotient:Crosssection`.


:::{figure} Images/Fig-ProductQuotient-Crosssection.png
---
width: 100%
name: Fig:ProductQuotient:Crosssection
class: dark-light
---
The cross section of the pyramid in {numref}`Fig:ProductQuotient:Pyramid` at position $x+\Delta x$.
:::


:::{todo}
Replace {numref}`Fig:ProductQuotient:Crosssection` with an applet.
:::

We see that we have obtained a rectangle with width $w(x)+\Delta w$ and length $\ell(x)+\Delta \ell$. The new area is, therefore, given by

$$
 A(x+\Delta x)=\left(w(x)+\Delta w\right)\left(\ell(x)+\Delta \ell\right).
$$

Now we can plug in the approximations for $\Delta w$ and $\Delta \ell$ in terms of the derivatives to find

\begin{align*}
 A(x+\Delta x) &\approx \left(w(x)+w'(x)\Delta x\right)\left(\ell(x)+\ell'(x)\Delta x\right) \\
 &= w(x)\ell(x)+w(x)\ell'(x)\Delta x+\ell(x) w'(x)\Delta x+w'(x)\ell'(x)\left(\Delta x\right)^2.
\end{align*}

The term $w(x)\ell(x)$ is simply the old area $A(x)$. As such, the new area is the old area plus three new terms, of which one, the one with $\left(\Delta x\right)^2$, is way smaller than the other two. So we find that the change in area divided by $\Delta x$ is approximately

$$
 \frac{A(x+\Delta x)-A(x)}{\Delta x}\approx w(x)\ell'(x)+\ell(x)w'(x)+w'(x)\ell'(x)\Delta x.
$$

Taking the limit as $\Delta x\rightarrow 0$, we obtain an expression for the rate of change of the area:

\begin{align*}
 A'(x) &= \lim_{\Delta x\rightarrow 0}\frac{A(x+\Delta x)-A(x)}{\Delta x} \\
 &\approx \lim_{\Delta x\rightarrow 0} w(x)\ell'(x)+\ell(x)w'(x)+w'(x)\ell'(x)\Delta x \\
 &= w(x)\ell'(x)+\ell(x)w'(x).
\end{align*}

It turns out that because $\dfrac{\Delta w}{\Delta x}\rightarrow w'(x)$ and $\dfrac{\Delta \ell}{\Delta x}\rightarrow \ell'(x)$ as $\Delta x\rightarrow 0$, this expression is in fact exact, so we have found

$$
A'(x)=w(x)\ell'(x)+\ell(x)w'(x)
$$

So we conclude that the small area with the $\left(\Delta x\right)^2$ term had no influence on the rate of change of the area, but both other areas did. As such, the rate of change of the area is the sum of the two terms $w(x)\ell'(x)$ and $\ell(x)w'(x)$ (and in particular, it is **not** equal to $w'(x)\ell'(x)$). 

The general version of this rule is called the **product rule**, or sometimes the **Leibniz rule**. The product rule and the chain rule (which has been discussed in {numref}`Sec:Differentiation:ChainRule`) are the most important rules that we can use to find derivatives of complicated functions. In this section, we will state and prove the product rule and show how it is used. We will also consider another rule, called the **quotient rule**, which is a combination of the product and chain rules. We will use these rules to find yet another standard two derivatives, the ones of the tangent and the hyperbolic tangent.


## The product rule

::::::{prf:theorem} The product rule
:label: Thm:Productquotientrule:Productrule
Let $f$ and $g$ be functions and consider the product function $p=fg$. Let $a$ be in the domain of $p$. Assume that $f$ and $g$ are both differentiable at $a$. Then $p$ is differentiable at $a$ and the derivative $p'(a)$ is given by

$$
 p'(a)=f'(a)g(a)+f(a)g'(a).
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Productquotientrule:Productrule`
:class: tudproof, dropdown

The derivative $p'(a)$, if it exists, is given by the limit

$$
 p'(a)=\lim_{h\rightarrow 0}\frac{p(a+h)-p(a)}{h}=\lim_{h\rightarrow 0}\frac{f(a+h)g(a+h)-f(a)g(a)}{h}.
$$

Now we add the term $-f(a+h)g(a)+f(a+h)g(a)$, which is just a very fancy way of writing $0$, to the numerator of this expression. Then we can split the limit in two parts and we obtain

\begin{align*}
 p'(a) &= \lim_{h\rightarrow 0}\frac{f(a+h)g(a+h)-f(a)g(a)}{h} \\
 &= \lim_{h\rightarrow 0}\frac{f(a+h)g(a+h)-f(a+h)g(a)+f(a+h)g(a)-f(a)g(a)}{h} \\
 &= \lim_{h\rightarrow 0}\frac{f(a+h)g(a+h)-f(a+h)g(a)}{h}+\lim_{h\rightarrow 0}\frac{f(a+h)g(a)-f(a)g(a)}{h}.
\end{align*}

Now we can write both of these limits as a product of two limits to obtain

\begin{align*}
 p'(a) &= \lim_{h\rightarrow 0}\frac{f(a+h)g(a+h)-f(a+h)g(a)}{h}+\lim_{h\rightarrow 0}\frac{f(a+h)g(a)-f(a)g(a)}{h} \\
 &= \lim_{h\rightarrow 0}f(a+h)\lim_{h\rightarrow 0}\frac{g(a+h)-g(a)}{h}+\lim_{h\rightarrow 0}g(a)\lim_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h}.
\end{align*}

Note that since $f$ is differentiable at $a$, it must be continuous at $a$ as well, see {prf:ref}`Thm:Differentiability:Diffimpliescont`, so we must have $\displaystyle \lim_{h\rightarrow 0}f(a+h)=f(a)$. Then we use that $f$ and $g$ are differentiable at $h$ to obtain

\begin{align*}
 p'(a) &= \lim_{h\rightarrow 0}f(a+h)\lim_{h\rightarrow 0}\frac{g(a+h)-g(a)}{h}+\lim_{h\rightarrow 0}g(a)\lim_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h} \\
 &= f(a)g'(a)+g(a)f'(a),
\end{align*}

as desired.

:::

::::{caution}
:name: Caution:Productquotientrule:Commonerrors

The most common error when trying to use the product rule is take the product of the two derivatives. In that case, the incorrect expression would become

$$
 (f g)'(x)=f'(x)g'(x)\qquad\qquad \left(\textbf{INCORRECT}\right).
$$

Make sure to avoid this error and to use the product rule as stated.

::::

Let us see how we can use the product rule in practice, by considering a few examples.

::::::{prf:example} 
:label: Ex:Productquotientrule:Example1
Consider the function $h(x)=x^2\cos(x)$. Then $h$ is the product of the two functions $f(x)=x^2$ and $g(x)=\cos(x)$, both of which we know the derivative of. As such, we can use the product rule to obtain

$$
 h'(x)=f'(x)g(x)+f(x)g'(x)=(2x)\cos(x)+x^2\left(-\sin(x)\right)=2x\cos(x)-x^2\sin(x).
$$

::::::

::::::{prf:example} 
:label: Ex:Productquotientrule:Example2
Consider the function $r(t)=2^t\sinh(t)$. Then $r$ is the product of the two functions $p(t)=2^t$ and $q(t)=\sinh(t)$. In {numref}`Sec:Differentiation:ChainRule` we obtained the derivatives of these functions. As such, we can use the product rule to obtain

$$
 r'(t)=p'(t)q(t)+p(t)q'(t)=\left(\ln(2)2^t\right)\sinh(t)+2^t\cosh(t).
$$

::::::

We can also use the product rule to differentiate functions that are the product of three (or more) functions.

::::::{prf:example} 
:label: Ex:Productquotientrule:Exampletripleproduct
Consider the function $f(x)=x^4\sin(x)\cos(x)$. Then $f$ is the product of three functions, so what should be our approach here? It turns out to be a good idea to first write it as a product of two functions. In this case, we can write $f=gh$ with $g(x)=x^4$ and $h(x)=\sin(x)\cos(x)$. Then the product rule gives

$$
 f'(x)=g'(x)h(x)+g(x)h'(x)=4x^3\sin(x)\cos(x)+x^4h'(x).
$$

To fully work out this derivative, we would need to know $h'(x)$, so how do we find that derivative? Well, $h$ is a product of two functions, so we can use the product rule again. Indeed, we can write $h=pq$ with $p(x)=\sin(x)$ and $q(x)=\cos(x)$. Then the product rule gives

$$
 h'(x)=p'(x)q(x)+p(x)q'(x)=\cos(x)\cos(x)+\sin(x)\left(-\sin(x)\right)=\cos^2(x)-\sin^2(x).
$$

Combining this with the previous equation, we obtain

$$
 f'(x)=4x^3\sin(x)\cos(x)+x^4h'(x)=4x^3\sin(x)\cos(x)+x^4\left(\cos^2(x)-\sin^2(x)\right).
$$

::::::

Finally, we can combine the product and chain rules to find the derivatives of complicated functions.

::::::{prf:example} 
:label: Ex:Productquotientrule:Exampleproductchain
Consider the function $f(x)=x^2\sin\left(x^3+2x+1\right)$. Then $f$ can be written as the product $f=gh$ with $g(x)=x^2$ and $h(x)=\sin\left(x^3+2x+1\right)$. Using the product rule, we find

$$
 f'(x)=g'(x)h(x)+g(x)h'(x)=2x\sin\left(x^3+2x+1\right)+x^2h'(x).
$$

Then in order to find the derivative $h'(x)$ we need the chain rule. Indeed, we can write $h(x)=p\circ q$ with $p(u)=\sin(u)$ and $q(x)=x^3+2x+1$. With the chain rule we obtain

$$
 h'(x)=p'(q(x))q'(x)=\cos\left(x^3+2x+1\right)\left(3x^2+2\right).
$$

Combining these equations gives

\begin{align*}
 f'(x) &=2x\sin\left(x^3+2x+1\right)+x^2h'(x) \\
 &=2x\sin\left(x^3+2x+1\right)+x^2\cos\left(x^3+2x+1\right)\left(3x^2+2\right) \\
 &=2x\sin\left(x^3+2x+1\right)+\left(3x^4+2x^2\right)\cos\left(x^3+2x+1\right).
\end{align*}

::::::

(Subsec:Quotientrule)=

## The quotient rule

The product and chain rules are the most important tools for finding derivatives of complicated functions. There is actually a third rule, called the quotient rule, which is also used often. However, it technically is not a new rule as it follows from the product and chain rules. As the name suggests, the quotient rule is used most often when finding derivatives of quotients of functions, for instance of rational functions.

::::::{prf:theorem} The quotient rule 
:label: Thm:Productquotientrule:Quotientrule

Let $f$ and $g$ be functions and consider the quotient function $q=\frac{f}{g}$. Let $a$ be in the domain of $q$ (so, at least, we should have $g(a)\neq 0$). Assume that $f$ and $g$ are both differentiable at $a$. Then $q$ is differentiable at $a$ and the derivative $q'(a)$ is given by

$$
 q'(a)=\frac{g(a)f'(a)-f(a)g'(a)}{g(a)^2}.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Productquotientrule:Quotientrule`
:class: tudproof, dropdown
We write $q=f\frac{1}{g}$. Then we use the product rule to evaluate

$$
 q'(a)=f'(a)\frac{1}{g(a)}+f(a)\left(\frac{1}{g}\right)(a).
$$

In order to find the derivative of $\frac{1}{g}$, we note that $\frac{1}{g}=h\circ g$ with $h(u)=\frac{1}{u}$. We know that $h'(u)=\frac{-1}{u^2}$. So we can use the chain rule to find

$$
 \left(\frac{1}{g}\right)(a)=h'(g(a))g'(a)=\frac{-1}{g(a)^2}g'(a).
$$

Combining these identities gives

$$
 q'(a)=f'(a)\frac{1}{g(a)}+f(a)\frac{-1}{g(a)^2}g'(a)=\frac{f'(a)g(a)-g'(a)f(a)}{g(a)^2}.
$$

So $q$ is differentiable in $a$ and $\displaystyle q'(a)=\frac{f'(a)g(a)-g'(a)f(a)}{g(a)^2}$.
:::

With the quotient rule in hand, we can find another two standard derivatives.

::::::{prf:theorem} Standard derivatives, part 3 out of 4
:label: Thm:Productquotientrule:Standard3
We have the following standard derivatives.

- We have $\dfrac{d}{dx}\left[\tan(x)\right]=\dfrac{1}{\cos^2(x)}=1+\tan^2(x).$
- We have $\dfrac{d}{dx}\left[\tanh(x)\right]=\dfrac{1}{\cosh^2(x)}=1-\tanh^2(x).$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Productquotientrule:Standard3`
:class: tudproof, dropdown
We know that $\tan(x)=\dfrac{\sin(x)}{\cos(x)}$, so we can use the quotient rule to evaluate

\begin{align*}
 \dfrac{d}{dx}\left[\tan(x)\right] &= \frac{\cos(x)\frac{d}{dx}[\sin(x)]-\sin(x)\frac{d}{dx}[\cos(x)]}{\cos(x)^2} \\
 &= \frac{\cos(x)\cos(x)-\sin(x)(-\sin(x))}{\cos^2(x)} \\
 &= \frac{\cos^2(x)+\sin^2(x)}{\cos^2(x)} \\
 &= \frac{1}{\cos^2(x)}.
\end{align*}

Alternatively, we can rewrite this expression to

\begin{align*}
 \dfrac{d}{dx}\left[\tan(x)\right] &= \frac{\cos^2(x)+\sin^2(x)}{\cos^2(x)} \\
 &= \frac{\cos^2(x)}{\cos^2(x)}+\frac{\sin^2(x)}{\cos^2(x)} \\
 &= 1+\left(\frac{\sin(x)}{\cos(x)}\right)^2 \\
 &= 1+\tan^2(x).
\end{align*}

Similarly, we know that that $\tanh(x)=\dfrac{\sinh(x)}{\cosh(x)}$, so we can use the quotient rule to evaluate

\begin{align*}
 \dfrac{d}{dx}\left[\tanh(x)\right] &= \frac{\cosh(x)\frac{d}{dx}[\sinh(x)]-\sinh(x)\frac{d}{dx}[\cosh(x)]}{\cosh(x)^2} \\
 &= \frac{\cosh(x)\cosh(x)-\sinh(x)\sinh(x)}{\cosh^2(x)} \\
 &= \frac{\cosh^2(x)-\sinh^2(x)}{\cosh^2(x)} \\
 &= \frac{1}{\cosh^2(x)}.
\end{align*}

Alternatively, we can rewrite this expression to

\begin{align*}
 \dfrac{d}{dx}\left[\tanh(x)\right] &= \frac{\cosh^2(x)-\sinh^2(x)}{\cosh^2(x)} \\
 &= \frac{\cosh^2(x)}{\cosh^2(x)}-\frac{\sinh^2(x)}{\cosh^2(x)} \\
 &= 1-\left(\frac{\sinh(x)}{\cosh(x)}\right)^2 \\
 &= 1-\tanh^2(x).
\end{align*}
:::

::::::{prf:example} 
:label: Ex:Productquotientrule:QuotExample1
Consider the function $f(x)=\dfrac{x^2+2x-3}{x^3+x}$. Then $f$ is the quotient of two functions (in fact, it is a rational function), since we can write $f=\dfrac{g}{h}$ with $g(x)=x^2+2x-3$ and $h(x)=x^3-x$. Hence, we can use the quotient rule to evaluate

\begin{align*}
 f'(x) &= \frac{h(x)g'(x)-g(x)h'(x)}{h(x)^2} \\
 &= \frac{(x^3-x)(2x+2)-(x^2+2x-3)(3x^2-1)}{(x^3-x)^2} \\
 &= \frac{-x^4 - 4 x^3 + 8 x^2 - 3}{(x^3-x)^2}.
\end{align*}

In fact, this expression can be simplified a little further and we have

$$
 f'(x)=\frac{-x^4 - 4 x^3 + 8 x^2 - 3}{(x^3-x)^2}=\frac{-x^2-6x-3}{x^2(x+1)^2}.
$$

::::::

::::::{prf:example} 
:label: Ex:Productquotientrule:QuotExample2
:class: full-width

Consider the (admittedly, rather nasty looking) function $p(\theta)=\dfrac{\tan(\theta)e^{2\theta}}{\left(1+\cos(\theta)\right)^3}$. In order to find the derivative of $p$, we are going to need all three of the product, chain and quotient rules. First, we use the quotient rule to write

$$
 p'(\theta)=\frac{\left(1+\cos(\theta)\right)^3\left(\tan(\theta)e^{2\theta}\right)'-\left(\tan(\theta)e^{2\theta}\right)\left(\left(1+\cos(\theta)\right)^3\right)'}{\left(\left(1+\cos(\theta)\right)^3\right)^2}.
$$

Now we need the product rule and the chain rule to find $\left(\tan(\theta)e^{2\theta}\right)'$. This gives

$$
 \left(\tan(\theta)e^{2\theta}\right)'=(\tan(\theta))'e^{2\theta}+\tan(\theta)\left(e^{2\theta}\right)'=\left(1+\tan^2(\theta)\right)e^{2\theta}+\tan(\theta)2e^{2\theta}.
$$

Finally, in order to evaluate $\left(1+\cos(\theta)\right)^3$ we need to use the chain rule. This gives

$$
 \left(1+\cos(\theta)\right)^3=3\left(1+\cos(\theta)\right)^2\left(1+\cos(\theta)\right)'=3\left(1+\cos(\theta)\right)^2\left(-\sin(\theta)\right).
$$

Combining these gives

$$
 p'(\theta)=\frac{\left(1+\cos(\theta)\right)^3\left(\left(1+\tan^2(\theta)\right)e^{2\theta}+\tan(\theta)2e^{2\theta}\right)-\left(\tan(\theta)e^{2\theta}\right)3\left(\left(1+\cos(\theta)\right)^2\left(-\sin(\theta)\right)\right)}{\left(1+\cos(\theta)\right)^6}.
$$

This expression can be simplified a bit further (though not much) and we find

$$
 p'(\theta)=\frac{e^{2 \theta} (\cos(\theta) + 1)^2 (\cos(\theta) + (\tan(\theta) + 1)^2 + \sin(\theta) (4 \tan(\theta) + 2))}{\left(1+\cos(\theta)\right)^6}.
$$
::::::

::::::{prf:example} Function that is differentiable, but not continuously differentiable
:label: Ex:Productquotientrule:Contdiff
:class: full-width

In {numref}`Subsec:Derivativestangent` we claimed that there are functions that are differentiable everywhere, but not continuously differentiable, i.e. its derivative is not continuous. Now we finally have the tools to show an example of such a function. Consider the piecewise defined function

$$
 f(x)=\begin{cases}x^2 \sin\left(\frac{1}{x}\right), & \mathrm{if}\,x \neq 0, \\ 0 & \mathrm{if}\,x = 0. \end{cases}
$$

For $x\neq 0$, the function is differentiable, since it can be written as $f(x)=g(x)h(k(x))$ with $g(x)=x^2$, $h(x)=\sin(x)$ and $k(x)=\dfrac{1}{x}$ and these functions are all differentiable on their maximal domain. Using the product and the chain rule, the derivative is given by

\begin{align*}
 f'(x)=&g(x)h'\left(k(x)\right)k'(x)+g'(x)h(k(x))\\ 
 =&x^2\cos\left(\frac{1}{x}\right)\left(-\frac{1}{x^2}\right)+2x\sin\left(\frac{1}{x}\right)\\
 =&-\cos\left(\frac{1}{x}\right)+2x\sin\left(\frac{1}{x}\right).
\end{align*}

For $x=0$, we evaluate the derivative using the limit definition

$$
 f'(0)=\lim_{h\rightarrow 0}\frac{f(h)-f(0)}{h}=\lim_{h\rightarrow 0}\frac{h^2\sin\left(\frac{1}{h}\right)}{h}=0,
$$

where the final equality follows from {prf:ref}`Ex:LimitAtPoint:SqueezeTheorem`. This means that

$$
 f'(x)=\begin{cases}-\cos\left(\frac{1}{x}\right)+2x\sin\left(\frac{1}{x}\right), & \mathrm{if}\,x \neq 0, \\ 0 & \mathrm{if}\,x = 0, \end{cases}
$$

so $f$ is differentiable everywhere. Using a reasoning similar to {prf:ref}`Ex:LimitAtPoint:SqueezeTheorem`, we see that

$$
 \lim_{x\rightarrow 0}2x\sin\left(\frac{1}{x}\right)=0.
$$

However, using a similar reasoning to {prf:ref}`Ex:LimitAtPoint:Limitsinoneoverx`, the limit 

$$
 \lim_{x\rightarrow 0}-\cos\left(\frac{1}{x}\right)
$$

does not exist. This means that the limit

$$
 \lim_{x\rightarrow 0}f'(x)=\lim_{x\rightarrow 0}-\cos\left(\frac{1}{x}\right)+2x\sin\left(\frac{1}{x}\right)
$$

does not exist. In particular, $f'$ is not continuous at $0$, so $f$ is not continuously differentiable.

:::{todo}
Make an applet with the graph of the function $f$ (left) and of its derivative $f'$ (right)
:::
::::::

## Grasple exercises



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/94a77cde-9af2-47d9-bb60-528d0a65a7bc?id=71399
:label: Grasple:71399
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/94a77cde-9af2-47d9-bb60-528d0a65a7bc?id=71399
:label: Grasple:71399
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a0730d24-9a8f-4b97-8c42-2e0395fb2b14?id=63497
:label: Grasple:63497
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/78f4d4aa-4ade-4948-b2da-74cfad5334a9?id=63494
:label: Grasple:63494
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c5a57f85-3b86-46ad-89cc-f52754cd598e?id=63495
:label: Grasple:63495
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b7d4d8ec-b239-4853-a95c-4323237b952a?id=63425
:label: Grasple:63425
:dropdown:
:description: Find a derivative.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c041c550-e344-4d1b-9568-94552c0aa713?id=63438
:label: Grasple:63438
:dropdown:
:description: Find two derivatives.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9566fa38-7659-415b-892d-6ba5c8ef63d0?id=63534
:label: Grasple:63534
:dropdown:
:description: Derivatives involving hyperbolic functions.
::::
