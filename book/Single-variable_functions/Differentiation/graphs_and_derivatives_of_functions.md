(Section:GraphsDerivatives)=

# Graphs and derivatives of functions

## Introduction

Now that we know the derivatives of most standard functions, we have not really touched upon what should be the most important question: what can we actually do with derivatives? We have seen that we can use them to find tangent lines, but that is about it. For higher order derivatives we have not even seen *any* uses (yet). However, there is much more that derivatives can tell us. In fact, most qualitative behaviour of a function is captured in its derivatives. For instance, we will see that we can use the first derivative to determine whether a function is increasing or decreasing at a point.

In this section, we will specifically see what the first and second derivatives say about the graph of a function. The ideas presented here can be generalized to give interpretations of higher order derivatives, but these are typically less useful in practice. In order to prove most of these results, we will need a very important theorem, called the **mean value theorem**, so let us start there.

## Mean value theorem

Suppose you are running a marathon and you let $f(t)$ describe the distance you travelled at time $t$. Then $f'(t)$ represents your velocity at time $t$. Say it takes you four and a half hours to finish the marathon. Then you average running speed is around $2.6$ meters per second. Likely, you are not running equally fast at each point of time, so for most values of $t$, $f'(t)$ will be unequal to $2.6$. The idea of the mean value theorem is that there must be at least one point in time (but possibly more) where your velocity is exactly equal to the average velocity. Intuitively this makes sense. If you were to run slower than $2.6$ meters per second at all points in time, or faster than $2.6$ meters per second at all points in time, your average velocity can never be $2.6$. So there must be points in time where you run slower than your average speed and points in time where you run faster than your average speed. Since your speed does not make sudden jumps (that is, your speed is continuous), it has to attain this average speed at some point in time.

With this idea in mind, let us formulate and prove the mean value theorem, which is also known as **Lagrange's mean value theorem**, named after the Italian mathematician and physicist [Joseph-Louis Lagrange (1736-1813)](https://en.wikipedia.org/wiki/Joseph-Louis_Lagrange). However, we will start with a special case of the mean value theorem, called **Rolle's theorem**, named after the French mathematician [Michel Rolle (1652-1719)](https://en.wikipedia.org/wiki/Michel_Rolle). This special case deals with functions $f$ defined on a closed interval $[a,b]$ with $f(a)=f(b)$.

::::::{prf:theorem} Rolle's theorem
:label: Thm:Graphsderivatives:Rolle
Let $f$ be a function that is continuous on a closed interval $[a,b]$ and differentiable on the open interval $(a,b)$. Suppose, in addition, that $f(a)=f(b)$. Then there exists a point $c$ in $(a,b)$ with $f'(c)=0.$

::::::

Unfortunately, we cannot prove Rolle's theorem yet, since the proof uses some other results that we have not obtained yet. We will give the proof in {numref}`Subsec:Extrema1dEVT`. An illustration of the theorem is shown in {numref}`Fig:Graphsderivatives:Rolle`. Note that {prf:ref}`Thm:Graphsderivatives:Rolle` also includes the case that there can be multiple points where the derivative is equal to $0$, for instance, for the function on the left in {numref}`Fig:Graphsderivatives:Rolle` any point will do, and for the right function there are two points where the derivative is equal to $0$.

:::{figure} Images/Fig-Graph1d-Rolle.png
---
width: 100%
name: Fig:Graphsderivatives:Rolle
class: dark-light
---
An illustration of Rolle's theorem.
:::

:::{todo}
Replace {numref}`Fig:Graphsderivatives:Rolle` with an applet.
:::

The mean value theorem is in essence an extension of Rolle's theorem, and formalises what we discussed in the introduction of this section.

::::::{prf:theorem} The mean value theorem
:label: Thm:Graphsderivatives:MVT
Let $f$ be a function that is continuous on a closed interval $[a,b]$ and differentiable on the open interval $(a,b)$. Then there exists a point $c$ in $(a,b)$ with

$$
 f'(c)=\frac{f(b)-f(a)}{b-a}.
$$

::::::

[^checkpoints]: Note that $L(a)=f(a)+\dfrac{f(b)-f(a)}{b-a}(a-a)=f(a)$ and $L(b)=f(a)+\dfrac{f(b)-f(a)}{b-a}(b-a)=f(b)$, so the function $L$ indeed goes through the points $(a,f(a))$ and $(b,f(b))$.

:::{admonition} Proof of {prf:ref}`Thm:Graphsderivatives:MVT`
:class: tudproof, dropdown
We want to apply Rolle's theorem, so we need to construct some function $g$, related to $f$, that has $g(a)=g(b)$. As such, we subtract from $f$ the linear function that goes through the points $(a,f(a))$ and $(b,f(b))$. This linear function is given by $L(x)=f(a)+\dfrac{f(b)-f(a)}{b-a}(x-a)$. Note that this function goes through the specified points[^checkpoints].

Now consider the function

$$
 g(x)=f(x)-L(x)=f(x)-f(a)-\dfrac{f(b)-f(a)}{b-a}(x-a).
$$

This function satisfies $g(a)=f(a)-L(a)=f(a)-f(a)=0$ and $g(b)=f(b)-L(b)=f(b)-f(b)=0$.

This function is the difference between two functions that are continuous on $[a,b]$ and differentiable on $(a,b)$, so the new function $g$ has these properties as well. As such, we can use Rolle's theorem to obtain $c$ in $(a,b)$ with $g'(c)=0$ and $g(a)=g(b)=0$. We can evaluate the derivative of $g$ as

$$
 g'(x)=f'(x)-L'(x)=f'(x)-\frac{f(b)-f(a)}{b-a}.
$$

Hence, we find, since $g'(c)=0$, that

$$
 0=g'(c)=f'(c)-\frac{f(b)-f(a)}{b-a},
$$

which gives $f'(c)=\dfrac{f(b)-f(a)}{b-a}$, as desired.
:::

The interpretation of this theorem works as follows: $\dfrac{f(b)-f(a)}{b-a}$ represents the **average slope** of the function on the interval $[a,b]$. The theorem states that there must be at least one point where the slope is equal to this average slope. Note that the mean value theorem does not tell you how to find the point. It only states that such a point must exist. An illustration of the theorem is shown in {numref}`Fig:Graphsderivatives:MVT`.

:::{figure} Images/Fig-Graph1d-MVT.png
---
width: 100%
name: Fig:Graphsderivatives:MVT
class: dark-light
---
An illustration of the mean value theorem. Note that in this case there are multiple points where the derivative is equal to $\dfrac{f(b)-f(a)}{b-a}$.
:::

:::{todo}
Replace {numref}`Fig:Graphsderivatives:MVT` with an applet.
:::

There is a more general version of the mean value theorem, called Cauchy's mean value theorem. This result is named after the French mathematician and engineer [Augustin-Louis Cauchy](https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy). This general version is usually a bit overkill when it comes to proving what the derivative says about a functions. Still, we will need this general version when proving l'Hospital's rule in {numref}`Section:lHospital`.

::::::{prf:theorem} The Cauchy mean value theorem
:label: Thm:Graphsderivatives:MVTCauchy
Let $f$ and $g$ be functions that are continuous on a closed interval $[a,b]$ and differentiable on the open interval $(a,b)$. Then there exists a point $c$ in $(a,b)$ with

$$
 (f(b)-f(a))g'(c)=(g(b)-g(a))f'(c).
$$

If $g(a)\neq g(b)$ and $g'(c)$, this can be rewritten in the form

$$
 \frac{f'(c)}{g'(c)}=\frac{f(b)-f(a)}{g(b)-g(a)},
$$

and if $f(a)\neq f(b)$ and $f'(c)\neq 0$, this can be rewritten in the form

$$
 \frac{g'(c)}{f'(c)}=\frac{g(b)-g(a)}{f(b)-f(a)}.
 $$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Graphsderivatives:MVTCauchy`
:class: tudproof, dropdown
The idea of proving this theorem is similar to the ones used in the proof of {prf:ref}`Thm:Graphsderivatives:MVT`. Here, we define the function

$$
 h(x)=(g(b)-g(a))f(x)-(f(b)-f(a))g(x).
$$

This function is a linear combination of two functions that are continuous on $[a,b]$ and differentiable on $(a,b)$, so the new function $h$ has these properties as well. In addition, we see that

\begin{align*}
 h(a) &= (g(b)-g(a))f(a)-(f(b)-f(a))g(a) \\
 &= g(b)f(a)-f(b)g(a) \\
 &= (g(b)-g(a))f(b)-(f(b)-f(a))g(b) \\
 &= h(b).
\end{align*}

As such, we can use Rolle's theorem to obtain $c$ in $(a,b)$ with $h'(c)=0$. We can evaluate the derivative of $h$ as

$$
 h'(x)=(g(b)-g(a))f'(x)-(f(b)-f(a))g'(x).
$$

Hence, we find, since $h'(c)=0$, that

$$
 0=h'(c)=(g(b)-g(a))f'(c)-(f(b)-f(a))g'(c),
$$

which gives $(f(b)-f(a))g'(c)=(g(b)-g(a))f'(c)$, as desired.
:::

:::{note}
We obtain {prf:ref}`Thm:Graphsderivatives:MVT` back from {prf:ref}`Thm:Graphsderivatives:MVTCauchy` when choosing the function $g$ to be given by $g(x)=x$.
:::


Let us see how the mean value theorem can be used in practice.

::::::{prf:example}
:label: EX:Graphsderivatives:MVT1
Consider the function $f(x)=x^3+3x^2+6x+3$ and suppose we want to find all (real) solutions of the equation $f(x)=0$ in between $-1$ and $0$. We notice that $f(-1)=-1<0$, while $f(0)=3>0$, so by {prf:ref}`Cor:Continuity:IVT`, there is at least one $a$ in between $-1$ and $0$ with $f(a)=0$. We will use the mean value theorem (or more specifically, Rolle's theorem) to show that this is the only solution. 

Indeed, suppose that there would be another solution, say a number $b$ in between $-1$ and $0$ with $f(b)=0$. Without loss of generality, we can assume that $a<b$. Then $f$ is continuous on the interval $[a,b]$ and differentiable on $(a,b)$ (since it is a polynomial). In addition, we have $f(a)=f(b)=0$. Then by {prf:ref}`Thm:Graphsderivatives:Rolle`, we can find some $c$ in the interval $(a,b)$ with $f'(c)=0$. However, we can evaluate the derivative of $f$ as

$$
 f'(x)=3x^2+6x+6.
$$

However, the equation $3x^2+6x+6=0$ does not have any real solutions. So our assumption that there would be another solution must be incorrect. Hence, there is only one solution between $-1$ and $0$. This is supported by the graph of the function, which is shown in {numref}`Fig:Graphsderivatives:MVT1`.


:::{figure} Images/Fig-Graphsderivatives-MVT1.png
:name: Fig:Graphsderivatives:MVT1

The graph of the function $f(x)=x^3+3x^2+6x+3$. Note that there is only one solution of the equation $f(x)=0$ in between $-1$ and $0$.
:::

:::{todo}
Replace {numref}`Fig:Graphsderivatives:MVT1` with an applet.
:::

::::::

One of the most important consequences of the mean value theorem are the following two results. These results form an essential part of finding antiderivatives, see {numref}`Sec:Integration:IndefiniteIntegrals`. Indeed, these results indicate that any two functions that have the same derivative must be different by a constant.

::::::{prf:corollary} 
:label: Cor:Graphsderivatives:Zeroderivative
Let $f$ be a differentiable function such that $f'(x)=0$ for all $x$ in some interval $(a,b)$. Then $f$ is constant on that interval.
::::::

:::{admonition} Proof of {prf:ref}`Cor:Graphsderivatives:Zeroderivative`
:class: tudproof
Suppose $f$ is not constant, but $f'(x)=0$ for all $x$ in $(a,b)$. Then we can find two points $p<q$ in the interval $(a,b)$ with $f(p)\neq f(q)$. Then $f$ is continuous on the interval $[p,q]$ and differentiable on the interval $(p,q)$, so by {prf:ref}`Thm:Graphsderivatives:MVT` we can find $c$ in $(p,q)$ with

$$
 f'(c)=\frac{f(q)-f(p)}{q-p}.
$$

Since $f(p)\neq f(q)$ we have $f'(c)=\dfrac{f(q)-f(p)}{q-p}\neq 0$. However, this contradicts the assumption that $f'(x)=0$ for all $x$ in $(a,b)$. Hence, $f$ must be constant on this interval.
:::

::::::{prf:corollary} 
:label: Cor:Graphsderivatives:Samederivative
Let $f$ and $g$ be differentiable functions such that $f'(x)=g'(x)$ for all $x$ in some interval $(a,b)$. Then $f=g+C$ for some constant $C$ on this interval.
::::::

:::{admonition} Proof of {prf:ref}`Cor:Graphsderivatives:Samederivative`
:class: tudproof
Consider the function $h=f-g$. Then $h$ is differentiable and for $x\in (a,b)$ we have $h'(x)=f'(x)-g'(x)=0$, since $f'(x)=g'(x)$. Hence, the function $h$ is constant by {prf:ref}`Cor:Graphsderivatives:Zeroderivative`, say $h=C$. Then $f=g+C$ for this same constant $C$.
:::

The mean value theorem can also be used to translate any restriction on the possible values of the derivative into a limitation on the values of the function itself.

Suppose, that for some function $f$ we know that

$$
f(2)=5
$$

and that

$$
3\leq f'(x)\leq 7\quad\text{for}\quad2\leq x\leq 6.
$$

 What are the smallest and largest possible values of $f(6)$?

Let us start with the smallest possible value. Since the slope of the function is always at least $3$, intuitively it makes sense that we obtain the lowest value of $f(6)$ whenever $f'(x)=3$ for **all** $2\leq x\leq 6$.

So consider a function $\tilde{f}$ with $\tilde{f}(2)=f(2)=5$ and $\tilde{f}'(x)=3$ for all $2\leq x\leq 6$. Our intuition tells us that then $f(6)\geq\tilde{f}(6)$, since the slope of $f$ is always at least as large as the slope of $\tilde{f}$.

The function $\tilde{f}$ has the same derivative as $g(x)=3x$ on the interval $(2,6)$. So by {prf:ref}`Cor:Graphsderivatives:Samederivative` we find that $\tilde{f}(x)=g(x)+C$ for some constant $C$. Since $5=\tilde{f}(2)=g(2)+C=6+C$, we must have $C=-1$, so then $\tilde{f}(x)=3x-1$ on this interval. In that case we would have $\tilde{f}(6)=3\cdot 6-1=17$.

So, intuitively at least, we have shown that $f(6)$ must be at least $\tilde{f}(6)=17$ and we know for certain that there is at least one possible formula for $f$ for which the value of $f(6)$ is precisely $17$ (and this is the function $\tilde{f}$). Hence, we have found the smallest possible value of $f(6)$, which is $17$.

However, can we make this a bit more rigorous?

Of course we can! The next example shows how to use the mean value theorem to establish that $f(6)\geq 17$ and $f(6)\leq 33$.

::::::{prf:example}
:label: EX:Graphsderivatives:MVT2
Assume we have any function $f$ that satisfies the assumptions

$$
f(2) = 5
$$

and

$$
3\leq f'(x)\leq 7\quad\text{for}\quad2\leq x\leq 6.
$$

Then by {prf:ref}`Thm:Graphsderivatives:MVT`, there would be a $c$ in the interval $[2,6]$ with

$$
 f'(c)=\frac{f(6)-f(2)}{6-2}=\frac{f(6)-5}{4}.
$$

Solving this equation for $f(6)$ gives

$$
 f(6)=4f'(c)+5.
$$

Since $c$ is in the interval $(a,b)$ we know that $f'(c)\geq 3$, so we find that

$$
 f(6)=4f'(c)+5\geq 4\cdot 3+5=17.
$$

So we conclude that, indeed, we must have $f(6)\geq 17$.

Similarly, we can use $f'(c)\leq 7$ to show that

$$
 f(6)=4f'(c)+5\leq 4\cdot 7+5=33.
$$

This value of $f(6)=33$ is obtained when $f'(x)=7$ for all $x$ in the interval $(2,6)$, in which case we would have been dealing with the function $f(x)=7x-9$.

{numref}`Fig:Graphsderivatives:MVT2` shows the graph of the function $3x-1$ , the graph of the function $7x-9$ and the graph of an example of a function that satisfies the assumptions on $f$. The graph of any function that satisfies the assumptions must lie in between these two graphs, so in particular, the value of $f(6)$ must be in between $17$ and $33$.

:::{figure} Images/Fig-Graphsderivatives-MVT2.png
:name: Fig:Graphsderivatives:MVT2

The graph of the function $3x-1$ , the graph of the function $7x-9$ and the graph of an example of a function that satisfies the assumptions on $f$.
:::

:::{todo}
Replace {numref}`Fig:Graphsderivatives:MVT2` with an applet. The function that satisfies the assumptions on $f$ is given by

$$
f(x)=\frac{1}{8}(x-2)^4 - \frac{3}{2}(x-2)^3 + \frac{9}{2}(x-2)^2 + 3(x-2) + 5.
$$
:::

::::::

{prf:ref}`Cor:Graphsderivatives:Samederivative` can also be used to establish certain trigonometric identities.

::::::{prf:example}
:label: EX:Graphsderivatives:MVT2
Let us try to simplify the expression $\arctan(x)+\arctan\left(\frac{1}{x}\right)$ for $x\neq 0$. We have not found the derivative of the arctangent yet, but as a sneak peak, we will use that $\dfrac{d}{dx}\left[\arctan(x)\right]=\dfrac{1}{1+x^2}$ (this identity will be established in {prf:ref}`Thm:Diffinverse:Standard4`). Using the chain rule, we find that

$$
 \dfrac{d}{dx}\left[\arctan(x)+\arctan\left(\frac{1}{x}\right)\right]=\frac{1}{1+x^2}+\frac{1}{1+\left(\frac{1}{x}\right)^2}\frac{-1}{x^2}=\frac{1}{1+x^2}-\frac{1}{x^2+1}=0.
$$

By {prf:ref}`Cor:Graphsderivatives:Samederivative`, we obtain that the function $f(x)=\arctan(x)+\arctan\left(\frac{1}{x}\right)$ must be constant on any closed interval that does not contain $0$. Now in order to establish which constant this is, we use a point in which we can find the exact value of the function. For instance, if $x>0$ we let $[a,b]$ be any interval that contains $1$ and $x$ and does not contain $0$. Then $f$ is constant on this interval and we find

$$
 f(x)=f(1)=\arctan(1)+\arctan\left(\frac{1}{1}\right)=\frac{\pi}{4}+\frac{\pi}{4}=\frac{\pi}{2}.
$$

Hence, we have $\arctan(x)+\arctan\left(\frac{1}{x}\right)=\frac{\pi}{2}$ for $x>0$. However, it is incorrect to conclude that this must be the case for $x<0$ as well. Indeed, for $x<0$ it is impossible to find an interval $[a,b]$ that contains $x$ and $1$, but does not contain $0$. And we absolutely need to avoid the point $0$, since the function $f$ is undefined there. Fortunately, we can use another point so that we can avoid $0$. Indeed, we can let $[a,b]$ be an interval that contains $-1$ and $x$ and does not contain $0$. Then $f$ is constant on this interval and we find

$$
 f(x)=f(-1)=\arctan(-1)+\arctan\left(\frac{1}{-1}\right)=-\frac{\pi}{4}-\frac{\pi}{4}=-\frac{\pi}{2}.
$$

We conclude that $\arctan(x)+\arctan\left(\frac{1}{x}\right)=\frac{\pi}{2}$ for $x>0$, while $\arctan(x)+\arctan\left(\frac{1}{x}\right)=-\frac{\pi}{2}$ for $x<0$. {numref}`Fig:Graphsderivatives:MVT2` shows the graph of this special function.

:::{figure} Images/Fig-Graphsderivatives-MVT3.png
:name: Fig:Graphsderivatives:MVT3

The graph of the function $f(x)=\arctan(x)+\arctan\left(\frac{1}{x}\right)$.
:::

:::{todo}
Replace {numref}`Fig:Graphsderivatives:MVT3` with an applet. Make sure no vertical line element is shown.
:::

::::::

(Subsec:Graphsderivatives:Incrdecr)=

## Increasing and decreasing functions

One of the main features of derivatives is that they can be used to establish on which intervals a function is increasing and on which intervals it is decreasing. We defined what it means for a function to be increasing or decreasing on an interval in {numref}`Subsec:PropertiesFunctionsIncreasingDecreasing`, but we saw there that without derivatives it is very hard to establish these properties. So how can we use the derivative? Intuitively speaking, if a function is increasing on an interval, then at any point on this interval the function values must grow. So if we consider the tangent line at such a point, we would expect a line with a positive slope. Similarly, we would expect a tangent line with a negative slope on an interval where the function is decreasing. We can make this precise in the following way.


::::::{prf:theorem} 
:label: Thm:Graphsderivatives:Increasingdecreasing
Let $f$ be a differentiable function.

- $f$ is increasing on an interval precisely when $f'(x)\geq 0$ on that interval.
- $f$ is decreasing on an interval precisely when $f'(x)\leq 0$ on that interval.
- If $f'(x)> 0$ on an interval, then $f$ is strictly increasing on that interval.
- If $f'(x)< 0$ on an interval, then $f$ is strictly decreasing on that interval.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Graphsderivatives:Increasingdecreasing`
:class: tudproof, dropdown
Suppose that $f'(x)\geq 0$ on an interval and let $a<b$ be any two points in that interval. Then by {prf:ref}`Thm:Graphsderivatives:MVT`, we can find $c$ in $(a,b)$ with 

$$
 f'(c)=\frac{f(b)-f(a)}{b-a}.
$$

By assumption, we have $f'(c)\geq 0$, so we find that $\dfrac{f(b)-f(a)}{b-a}\geq 0$. Since $a<b$, this can only happen if $f(a)\leq f(b)$. So we find that $f$ is increasing on this interval.

Now suppose that $f$ is increasing on an interval. Consider any point $x$ in that interval. Then for any $h>0$ for which $x+h$ is in the interval we have $f(x+h)\geq f(x)$. As such, we must have

$$
 \frac{f(x+h)-f(x)}{h}\geq 0.
$$

Similarly, for any $h<0$ for  which $x+h$ is in the interval we have $f(x+h)\leq f(x)$. Then both $f(x+h)-f(x)$ and $h$ are less than or equal to $0$, so we find that

$$
 \frac{f(x+h)-f(x)}{h}\geq 0.
$$

As such, we must have 

$$
 f'(x)=\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}\geq 0,
$$

as desired.

The other cases follow similarly.
:::

:::{warning}
A function $f$ can be strictly increasing on an interval even if its derivative is $0$ somewhere. For instance, consider the function $f(x)=x^3$. Then $f'(x)=3x^2$, which is $0$ at $x=0$. Still, this function is strictly increasing on $\mathbb{R}$, since for any $a<b$ we have $a^3<b^3$.
:::

::::::{prf:example} 
:label: Ex:Graphsderivatives:Increasingdecreasing1
Consider the function $f(x)=-2x^3-3x^2+12x+3$ and suppose we want to know on which intervals the function is increasing and on which intervals it is decreasing. For this, we evaluate the derivative, which is given by

$$
 f'(x)=-6x^2-6x+12.
$$

In order to establish when we have $f'(x)>0$ and when we have $f'(x)<0$ we first solve $f'(x)=0$, i.e. $-6x^2-6x+12=0$. This is a quadratic equation with solutions $x=1$ and $x=-2$. Since the coefficient of $x^2$ is negative, the graph of $f'$ is a parabola opening downwards. As such, we find that $f'(x)<0$ for $x<-2$ and for $x>1$, while $f'(x)>0$ for $-2<x<1$. We conclude that $f$ is strictly increasing on the intervals $(-\infty,-2)$ and $(1,\infty)$, while it is strictly decreasing on the interval $(-2,1)$. This can also be seen in the graph of the function.

:::{todo}
Here an applet with the graph of the function.
:::

::::::

We postponed a small piece of the proof of {prf:ref}`Thm:PropertiesFunctions:HyperbolicProperties`, since it is very convenient to use derivatives to show whether a given function is increasing or decreasing. So let us finish the proof here.

:::{admonition} Remainder of proof of {prf:ref}`Thm:PropertiesFunctions:HyperbolicProperties`
:class: tudproof, dropdown
If $f(x)=\cosh(x)$, then we have $f'(x)=\sinh(x)$. Since $f'(x)<0$ when $x<0$, the hyperbolic cosine must be strictly decreasing on $(-\infty,0)$. Similarly, since $f'(x)>0$ when $x>0$, the hyperbolic cosine is strictly increasing on $(0,\infty)$.

If $h(x)=\tanh(x)$, then we have $fh'(x)=\dfrac{1}{\cosh(x)^2}$. We see that $h'(x)>0$ for all $x$, so the hyperbolic tangent is strictly increasing on $\mathbb{R}$.
:::

## Convexity, concavity and inflection points

In {numref}`Subsec:Graphsderivatives:Incrdecr` we saw how we can use the first derivative to say something about the graph of a function. In {numref}`Section:Extrema1d` we will see even more uses of the first derivative. However, we have not found any uses for higher order derivatives yet. In this subsection we will focus on the second derivative.

Consider the functions $f(x)=\sin\left(\frac{\pi}{2}x\right)$ and $g(x)=x^2$ on the interval $[0,1]$. Both functions are strictly increasing on this interval, but they still show very different behaviour in their growth. Indeed, the function $f$ first grows quickly and then slows down, while for the function $g$ it is the other way around.

:::{todo}
Here an applet with the graph of these functions, as well as the graphs of their derivatives.
:::

We can see this behaviour back in the derivatives of these functions. If we look at the graphs of the derivatives of these functions, we see that the function $f'$ is decreasing, while the function $g'$ is increasing. This matches the behaviour that we observed in the original function. Indeed, the fact that the function $f'$ is decreasing, means that the slope of the original function get lower so that it grows slower. On the other hand, the function $g'$ is increasing, so the slope of the function $g$ increases as well, which means that the function grows quicker. So how can we establish that $f'$ decreases and $g'$ increases? The same way you would do that for any other function: you take a look whether the derivative is positive or negative. This means that in order to distinguish between the behaviour of the functions $f$ and $g$, we should take a look at the derivatives of their derivatives, so at their second derivatives. 

Let us first give these concepts a name and then we will see how we can use the second derivative to establish the right behaviour.

::::::{prf:definition} 
:label: Def:Graphsderivatives:Concavity
A function $f$ is called **convex** or **concave upwards** on an interval if for any two points $a<b$ in the interval and for all $0\leq t\leq 1$ we have

$$
 f(ta+(1-t)b)\leq tf(a)+(1-t)f(b).
$$ 


A function $f$ is called **concave** or **concave downwards** on an interval if for any two points $a<b$ in the interval and for all $0\leq t\leq 1$ we have

$$
 f(ta+(1-t)b)\leq tf(a)+(1-t)f(b).
$$ 

::::::

Since the line segment between points $(a,f(a))$ and $(b,f(b))$ can be parametrised by $x(t)=ta+(1-t)b$ and $y(t)=tf(a)+(1-t)f(b)$ for $0\leq t\leq 1$, if the line segment between any two distinct points on the graph of $f$ lies above the graph of $f$.

Similarly, $f$ is concave on an interval precisely when for any two points $a<b$ in that interval the line segment between any two distinct points on the graph of $f$ lies below the graph of $f$.




:::{figure} Images/Fig-Graph1d-convexdef.png
---
width: 100%
name: Fig:Graphsderivatives:Convexdef
class: dark-light
---
An illustration of the definition of a convex function (left) and a concave function (right), with the line piece between any two points $a$ and $b$ lying above or below the function respectively.
:::

:::{todo}
Turn {numref}`Fig:Graphsderivatives:Convexdef` into an applet. Maybe nice if you can slide the points $(x(t),f(x(t)))$ and $(x(t),y(t))$.
:::

:::{note}
A function $f$ is convex on an interval precisely when $-f$ is concave on that interval. This follows since $f(ta+(1-t)b)\leq tf(a)+(1-t)f(b)$ precisely when $-f(ta+(1-t)b)\geq -tf(a)-(1-t)f(b)$.
:::

Similarly to strictly increasing and strictly decreasing, we can also define strictly convex and strictly concave functions. 

::::::{prf:definition} 
:label: Def:Graphsderivatives:StrictConcavity
A function $f$ is called **strictly convex** or **strictly concave upwards** on an interval if for any two points $a<b$ in the interval and for all $0\leq t\leq 1$ we have

$$
 f(ta+(1-t)b)< tf(a)+(1-t)f(b).
$$ 


A function $f$ is called **strictly concave** or **strictly concave downwards** on an interval if for any two points $a<b$ in the interval and for all $0\leq t\leq 1$ we have

$$
 f(ta+(1-t)b)> tf(a)+(1-t)f(b).
$$ 

::::::


Before we make a link between convex and concave functions and the second derivative, let us first make a connection with the first derivative.

::::::{prf:theorem} 
:label: Thm:Graphsderivatives:Concavitytangent
A differentiable function $f$ is convex on an interval precisely when $f$ lies above all tangent lines in that interval. That is, $f$ is convex precisely when for any two points $a$ and $b$ in the interval we have $f(b)\geq f(a)+f'(a)(b-a)$.

$f$ is concave on an interval precisely when $f$ lies below all tangent lines in that interval. That is, $f$ is concave precisely when for any two points $a$ and $b$ in the interval we have $f(b)\leq f(a)+f'(a)(b-a)$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Graphsderivatives:Concavitytangent`
:class: tudproof, dropdown
Let $I$ be an interval. 

Suppose first that $f$ is convex on $I$. Let $a<b$ in $I$. Then, since $f$ is convex, we have for any $ 0< t< 1$ that 

$$
 f(ta+(1-t)b)\leq tf(a)+(1-t)f(b).
$$

Then we can subtract $f(a)$ from both sides of the inequality to obtain

$$
 f(ta+(1-t)b)-f(a)\leq tf(a)+(1-t)f(b)-f(a)=(t-1)f(a)+(1-t)f(b)=(1-t)(f(b)-f(a)).
$$

Now we divide this inequality by the positive number $(1-t)(b-a)$ to obtain

$$
 \frac{f(ta+(1-t)b)-f(a)}{(1-t)(b-a)}\leq \frac{f(b)-f(a)}{b-a}.
$$

Note that $(1-t)(b-a)=\left(ta+(1-t)b\right)-a$, so we rewrite the left-hand side of this inequality to obtain

$$
 \frac{f(ta+(1-t)b)-f(a)}{\left(ta+(1-t)b\right)-a}\leq \frac{f(b)-f(a)}{b-a}.
$$

Since $ta+(1-t)b\rightarrow a$ as $t\rightarrow 1$, we find that

$$
 \lim_{t\rightarrow 1}\frac{f(ta+(1-t)b)-f(a)}{\left(ta+(1-t)b\right)-a}=\lim_{s\rightarrow 1}\frac{f(s)-f(a)}{s-a}=f'(a),
$$

so we obtain

$$
 f'(a)\leq \frac{f(b)-f(a)}{b-a}.
$$

Since $b-a>0$ we can multiply both parts of the inequality by $b-a$ to obtain

$$
 f'(a)(b-a)\leq f(b)-f(a),
$$

which gives

$$
 f(b)\geq f(a)+f'(a)(b-a),
$$

as desired. 

Now suppose that for all $x$ and $y$ in the interval we have $f(y)\geq f(x)+f'(x)(y-x)$. Let $a<b$ in $I$ and let $0\leq t\leq 1$. Then we want to show $tf(a)+(1-t)f(b)\geq f(ta+(1-t)b)$, i.e. $tf(a)+(1-t)f(b)- f(ta+(1-t)b)\geq 0$. Then we can write 

$$
 f(ta+(1-t)b)=1\cdot f(ta+(1-t)b)=(t+(1-t))f(ta+(1-t)b)=tf(ta+(1-t)b)+(1-t)f(ta+(1-t)b).
$$

With this, we have 

$$
 tf(a)+(1-t)f(b)-f(ta+(1-t)b)=tf(a)+(1-t)f(b)-\left(tf(ta+(1-t)b)+(1-t)f(ta+(1-t)b)\right)=t\left(f(a)-f(ta+(1-t)b)\right)+(1-t)\left(f(b)-f(ta+(1-t)b)\right).
$$

Since $a$, $b$ and $ta+(1-t)b$ are all points in the interval $I$, we can use our assumption to obtain the estimate

$$
 \begin{array}{lcl}tf(a)+(1-t)f(b)-f(ta+(1-t)b)&=&t\left(f(a)-f(ta+(1-t)b)\right)+(1-t)\left(f(b)-f(ta+(1-t)b)\right)\\ &\geq& t\left(f(a)-\left(f(a)-f'(ta+(1-t)b)(a-(ta+(1-t)b))\right)\right)+(1-t)\left(f(b)-\left(f(b)-f'(ta+(1-t)b)(b-(ta+(1-t)b))\right)\right)\\ &=&tf'(ta+(1-t)b)(a-(ta+(1-t)b))+(1-t)f'(ta+(1-t)b)(b-(ta+(1-t)b))\\ &=&tf'(ta+(1-t)b)((1-t)a-(1-t)b)+(1-t)f'(ta+(1-t)b)(tb-ta)\\ &=&t(1-t)f'(ta+(1-t)b)(a-b)+(1-t)tf'(ta+(1-t)b)(b-a)\\ &=&0.\end{array}
$$

Hence, we must have $tf(a)+(1-t)f(b)\geq f(ta+(1-t)b)$, which means that $f$ is convex.

The results about concavity follow by applying the first part to the function $-f$.
:::

:::{figure} Images/Fig-Graph1d-convextangent.png
---
width: 100%
name: Fig:Graphsderivatives:Convextangent
class: dark-light
---
An illustration of the classification of a convex function (left) and a concave function (right) from {prf:ref}`Thm:Graphsderivatives:Concavitytangent`.
:::

:::{todo}
Turn {numref}`Fig:Graphsderivatives:Convextangent` into an applet. 
:::

For many functions, both the definition and the classification from {prf:ref}`Thm:Graphsderivatives:Concavitytangent` are rather hard to check. Fortunately, for functions that are twice differentiable we have a criterion, similar to {prf:ref}`Thm:Graphsderivatives:Increasingdecreasing`, that is much easier to check.

::::::{prf:theorem} 
:label: Thm:Graphsderivatives:Concaveseconddiv
Let $f$ be a twice differentiable function.

- $f$ is convex on an interval precisely when $f''(x)\geq 0$ on that interval.
- $f$ is concave on an interval precisely when $f''(x)\leq 0$ on that interval.
- If $f''(x)> 0$ on an interval, then $f$ is strictly convex on that interval.
- If $f''(x)< 0$ on an interval, then $f$ is strictly concave on that interval.

::::::


:::{admonition} Proof of {prf:ref}`Thm:Graphsderivatives:Concaveseconddiv`
:class: tudproof, dropdown
Suppose first that $f''(x)\geq 0$ for all $x$ in an interval $I$. Let $a<b$ be two distinct points in $I$. Then by {prf:ref}`Thm:Graphsderivatives:MVT`, we can find $c$ in $(a,b)$ with 

$$
 f'(c)=\frac{f(b)-f(a)}{b-a}.
$$

Since $f''(x)\geq 0$ for all $x$, it follows from {prf:ref}`Thm:Graphsderivatives:Increasingdecreasing` that $f'$ is increasing on $I$. Hence, we find that 

$$
 f'(a)\leq f'(c).
$$ 

Then we multiply both sides of this inequality by  $(b-a)$ (which is positive) and we add $f(a)$ to obtain

$$
 f(a)+f'(a)(b-a)\leq f(a)+f'(c)(b-a).
$$

Now the equation $f'(c)=\frac{f(b)-f(a)}{b-a}$ can be rewritten to $f(a)+f'(c)(b-a)=f(b)$, so we find that

$$
 f(a)+f'(a)(b-a)\leq f(b).
$$

Then we obtain that $f$ must be convex by {prf:ref}`Thm:Graphsderivatives:Concavitytangent`.

Now suppose that $f$ is convex on an interval $I$. We will show that $f''(x)\geq 0$ on $I$ by showing that $f''$ is increasing on $I$ and then using {prf:ref}`Thm:Graphsderivatives:Concavitytangent`. Let $a<b$ be two distinct points in $I$. Consider any point $a<p<b$. Write $t=\frac{b-p}{b-a}$. Since $a<p<b$, we must have $0<t<1$. Note, in addition, that 

$$
 1-t=1-\frac{b-p}{b-a}=\frac{p-a}{b-a}
$$

and that 

$$
 ta+(1-t)b=\frac{b-p}{b-a}a+\frac{p-a}{b-a}b=p.
$$

Then by the definition of convexity, we find that

$$
 f(p)=f\left(ta+(1-t)b\right)\leq tf(a)+(1-t)f(b)=\frac{b-p}{b-a}f(a)+\frac{p-a}{b-a}f(b).
$$

Then we multiply this inequality by the positive term $b-a$, which gives

$$
 (b-a)f(p)\leq (b-p)f(a)+(p-a)f(b).
$$

Now we subtract $(b-a)f(a)$ from both sides of the inequality to obtain

$$
 (b-a)f(p)-(b-a)f(a)\leq (b-p)f(a)+(p-a)f(b)-(b-a)f(a)=(a-p)f(a)+(p-a)f(b)=(p-a)f(b)-(p-a)f(a).
$$

Then we divide both sides of the inequality by the positive term $(b-a)(p-a)$ to obtain

$$
 \frac{f(p)-f(a)}{p-a}\leq \frac{f(b)-f(a)}{b-a}.
$$

Taking the limit $p\rightarrow a^+$ gives

$$
 f'(a)=\lim_{p\rightarrow a^+}\frac{f(p)-f(a)}{p-a}\leq \frac{f(b)-f(a)}{b-a}.
$$

Now we return to a previous inequality: $(b-a)f(p)\leq (b-p)f(a)+(p-a)f(b)$. This time, we first bring a few terms to the other side of the equation, which gives

$$
 -(b-p)f(a)\leq (p-a)f(b)-(b-a)f(p).
$$

Then, we add $(b-p)f(b)$ to both sides of the equation to obtain

$$
 (b-p)f(b)-(b-p)f(a)\leq (p-a)f(b)-(b-a)f(p)+(b-p)f(b)=(b-a)f(b)-(b-a)f(p).
$$

Then we divide both sides of the inequality by the positive term $(b-a)(b-p)$ to obtain

$$
 \frac{f(b)-f(a)}{b-a}\leq \frac{f(b)-f(p)}{b-p}.
$$

Taking the limit $p\rightarrow b^-$ gives

$$
 f'(b)=\lim_{p\rightarrow b^-}\frac{f(b)-f(p)}{b-p}\geq \frac{f(b)-f(a)}{b-a}.
$$

Combining these two inequalities gives

$$
 f'(a)\leq \frac{f(b)-f(a)}{b-a}\leq f'(b).
$$

This means that $f'$ is increasing, so by {prf:ref}`Thm:Graphsderivatives:Concavitytangent` we must have $f''(x)\geq 0$ on $I$, as desired.

The other cases follow similarly.
:::

:::{warning}
A function $f$ can be strictly convex on an interval even if its second derivative is $0$ somewhere. For instance, consider the function $f(x)=x^4$. Then $f''(x)=12x^3$, which is $0$ at $x=0$. Still, this function is strictly convex on $\mathbb{R}$, which can be seen from the graph of the function.
:::

As a consequence, we can also check for convexity by checking whether the derivative is increasing or decreasing. In fact, we already used this in the proof of {prf:ref}`Thm:Graphsderivatives:Concaveseconddiv`.

::::::{prf:theorem} 
:label: Thm:Graphsderivatives:Concaveseconddiv
Let $f$ be a twice differentiable function. 

- $f$ is convex on an interval precisely when $f'$ is increasing on that interval.
- $f$ is concave on an interval precisely when $f'$ is decreasing on that interval.
- If $f'$ is strictly increasing on an interval, then $f$ is strictly convex on that interval.
- If $f'$ is strictly decreasing on an interval, then $f$ is strictly concave on that interval.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Graphsderivatives:Concavitytangent`
:class: tudproof, dropdown

This follows directly from combining {prf:ref}`Thm:Graphsderivatives:Concaveseconddiv` and {prf:ref}`Thm:Graphsderivatives:Increasingdecreasing`.

:::

Before we move on to discussing an example, we need one more definition.

::::::{prf:definition} 
:label: Thm:Graphsderivatives:Inflection
Let $x$ be a point in the domain of a function $f$. Then $x$ is called an **inflection point** if is a point where the function changes from being convex to concave or vice versa.
::::::

For a twice differentiable function $f$, we see from {prf:ref}`Thm:Graphsderivatives:Concaveseconddiv` that an inflection point occurs if the second derivative changes from positive (meaning $f$ is convex) to negative (meaning $f$ is concave). If $f''$ is itself continuous, this can only happen if the second derivative is $0$ at this point. Hence, we obtain the following result.

::::::{prf:theorem} 
:label: Thm:Graphsderivatives:Inflection
Let $f$ be a twice differentiable function such that $f''$ is. If $x$ is an inflection point of $f$ and $f''$ is continuous at $x$, then $f''(x)=0$.

::::::

:::{warning}
{prf:ref}`Thm:Graphsderivatives:Inflection` does not work the other way around. For instance, if we consider $f(x)=x^4$, then we have $f''(0)=0$. However, $0$ is not an inflection point of $f$, since $f''(x)=12x^2>0$ for all $x\neq 0$. So the function does not change from convex to concave or vice versa at $0$, since it is convex on both the intervals $(-\infty,0)$ and $(0,\infty)$.
:::

To conclude, let us see how we determine the convexity of a function in practice. 

::::::{prf:example} 
:label: Ex:Graphsderivatives:Convex
Consider the function $f(x)=x^4+2x^3-36x^2+3x+4$. We want to know on which intervals the function is convex or concave and where the inflection points are. For this, we evaluate its second derivative. We obtain

$$
 f'(x)=4x^3+6x^2-72x+3
$$

and

$$
 f''(x)=12x^2+12x-72.
$$

In order to find out where $f''$ is positive or negative, we first look where it is $0$. Solving $12x^2+12x-72=0$ gives $x=-3$ and $x=2$. Since the graph of $f''$ is a parabola opening upwards, we find that $f''(x)>0$ for $x<-3$ and for $x>2$, while $f''(x)<0$ for $-3<x<2$. By {prf:ref}`Thm:Graphsderivatives:Concaveseconddiv`, the function $f$ is strictly convex on the intervals $(-\infty,-3)$ and $(2,\infty)$, while it is strictly concave on the interval $(-3,2)$. At $x=-3$ the function changes from convex to concave, while at $x=2$ it changes from concave back to convex. So both points are inflection points.

:::{todo}
Applet with the graph of the function.
:::

::::::

