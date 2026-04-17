(Section:Extrema1d)=

# Extrema of functions

(Subsec:Extrema1dIntro)=

## Introduction

One of the most important applications of differentiation is that it can be used to solve a certain type of optimisation problems. In optimisation problems, you want to either maximise a certain quantity (like profit, or size) or minimise a quantity (like costs, or material usage), sometimes under some additional constraints.

Suppose, for instance, that you have a large piece on land and you have fences with a total length of $400\ m$. You want to build a rectangular region closed off by these fences. What shape would give the largest area? Since the region is rectangular, we let $\ell$ denote its length and $w$ its width (both in meters). Then the area $A$ (in square meters) is given by

$$
 A=w\ell.
$$

The total circumference of the region is $2\ell+2w$. Since we have only $400\ m$ of fence, we obtain the constraint

$$
 2\ell+2w=400.
$$

From this, we can express one of the variables in terms of the other one and we find that

$$
 \ell=200-w.
$$

This means that we can express the area as a function of only the width $w$ and we obtain

$$
 A(w)=w\ell=w\left(200-w\right).
$$

So how should we continue from here? From {prf:ref}`Thm:Graphsderivatives:Increasingdecreasing` we know that a function is increasing when the derivative is positive and decreasing when it is negative. So we evaluate the derivative of $A$ to obtain

$$
 \frac{dA}{dw}=200-2w.
$$

Then we see that $\frac{dA}{dw}>0$ when $w<100$, while $\frac{dA}{dw}<0$ when $w>100$. So if the width is less than $100$, we should increase the width since that gives a larger area. In addition, if the width is more than $100$, we should decrease the width since we then also obtain a larger area. This suggests that we obtain the largest area whenever $w=100$. In that case, we have $\ell=200-w=100$ as well. Hence, we obtain the largest area whenever the rectangle is a square.

In this section we will show that this idea is valid. We will look at how we can find the largest function values (called **maxima** of the function) and the lowest function value (called **minima** of the function). Maxima and minima are collectively called the **extrema** of a function. For this, we take two different points of view. First, we look at what happens locally. That is, we zoom in near an interesting point and do not care how the functions behaves far away from that point. Then, we look at what happens globally, so when we take the full domain of the function into account.

## Local extrema

Since we will be talking a lot about the minima and maxima of a function, let us first define what we mean by these concepts.

::::::{prf:definition} 
:label: Def:MinMax:LocExtr
Suppose that the domain of a function $f$ contains an open interval $I$. Then for $c$ in $I$ we say that $f$ has a **local maximum** at $c$, or that $f(c)$ is a **local maximum** value of $f$, if $f(c)\geq f(x)$ for $x$ in $I$. Similarly, we say that $f$ has a **local minimum** at $c$, or that $f(c)$ is a **local minimum** value of $f$, if $f(c)\leq f(x)$ for $x$ in $I$.

A **local extremum** or **local extreme value** is a local maximum or a local minimum.
::::::

:::{note}
The function value $f(c)$ is the thing that we call a local maximum or minimum, not the input value $c$. This terminology is often mixed up, so you should be careful with this.
:::


That we are only looking whether $f(c)$ is the largest or smallest function value on an interval around $c$ precisely means that we are looking at the local behaviour of the function. What happens far away from $c$ is not important. 

:::{figure} Images/Fig-MinMax-LocExtr.png
---
width: 100%
name: Fig:MinMax:LocExtr
class: dark-light
---
The function attains a local maximum at $b$ and a local minimum at $c$, even though far away from these points there are points with larger and lower function values. The endpoints $a$ and $b$ are not local extrema, since there is no open interval containing either of them.
:::

:::{todo}
Turn {numref}`Fig:MinMax:LocExtr` into an applet.
:::

:::{note}
Suppose $f$ is constant on an open interval $I$ and let $c$ in $I$. Then for any $x$ in $I$ we have $f(x)\geq f(c)$ (since $f(x)=f(c)$), which means that $f(c)$ is a local minimum of $f$. On the other hand, for any $x$ in $I$ we also have $f(x)\leq f(c)$ (since, still, $f(x)=f(c)$), which means that $f(c)$ is a local maximum on $f$.

So if a function is constant on an open interval, then the function attains both a local minimum and a local maximum at each point in that interval.

This also works the other way around: if $f$ attains both a local maximum and a local minimum of $f$, then for $x$ close to $c$ we must both have $f(x)\leq f(c)$ and $f(x)\geq f(c)$, which means that $f(x)=f(c)$ for any $x$ close to $c$. This exactly means that $f$ is constant on an interval containing $c$.
:::

So how do we find the location of the local extrema of a function? In {numref}`Subsec:Extrema1dIntro` we argued that if the function is differentiable, a local extremum can only occur at points where the derivative is $0$. This is true in general, and the result is known as Fermat's theorem, named after the French mathematician [Pierre de Fermat (1601-1665)](https://en.wikipedia.org/wiki/Pierre_de_Fermat). 

::::::{prf:theorem} Fermat's theorem
:label: Thm:MinMax:Fermat
If a function $f$ has a local maximum or local minimum at $c$ and if $f$ is differentiable at $c$, then $f'(c)=0$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:MinMax:Fermat`
:class: tudproof, dropdown
Suppose that $f$ has a local maximum at $c$. Then for $h$ sufficiently close to $0$ we have

$$
 f(c)\geq f(c+h),
$$

which means that

$$
 f(c+h)-f(c)\leq 0.
$$

Now we want to work towards a difference quotient, so we want to divide by $h$. However, we should make a distinction between positive and negative values of $h$, as the inequality sign flips when dividing by a negative number.

For $h>0$ we can divide by $h$ and obtain

$$
 \frac{f(c+h)-f(c)}{h}\leq 0.
$$

Since $f$ is differentiable in $c$ we have

$$
 f'(c)=\lim_{h\rightarrow 0}\frac{f(c+h)-f(c)}{h}.
$$

Since this limit exists, it is equal to the right limit and we find

$$
 f'(c)=\lim_{h\rightarrow 0}\frac{f(c+h)-f(c)}{h}=\lim_{h\rightarrow 0^+}\frac{f(c+h)-f(c)}{h}.
$$

Using {prf:ref}`Theorem:LimitAtPoint:Comparison` we obtain

$$
 f'(c)=\lim_{h\rightarrow 0^+}\frac{f(c+h)-f(c)}{h}\leq \lim_{h\rightarrow 0^+}0=0.
$$

Now for $h<0$ we divide the equation $f(c+h)-f(c)\leq 0$ by $h$ and we obtain

$$
 \frac{f(c+h)-f(c)}{h}\geq 0.
$$

Similarly to the case for positive $h$, we find that

$$
 f'(c)=\lim_{h\rightarrow 0}\frac{f(c+h)-f(c)}{h}=\lim_{h\rightarrow 0^-}\frac{f(c+h)-f(c)}{h}.
$$

Using {prf:ref}`Theorem:LimitAtPoint:Comparison` we obtain

$$
 f'(c)=\lim_{h\rightarrow 0^-}\frac{f(c+h)-f(c)}{h}\geq \lim_{h\rightarrow 0^-}0=0.
$$

So we find that $f'(c)\leq 0$ and $f'(c)\geq 0$, which must mean that $f'(c)=0$.

Now if $f$ has a local minimum at $c$, then $-f$ has a local maximum at $c$. By the first part of this proof, we must have $-f'(c)=0$, since $-f$ is also differentiable at $c$. Then we obtain $f'(c)=0$, as desired.

:::

So is this the only way a function can have a local extremum? The answer to this is no. Consider, for instance, the function $f(x)=|x|$. Then we find that

$$
 f'(x)=\left\{\begin{array}{l}-1,\qquad&\text{if}\ x<0,\\ 1,\qquad &\text{if}\ x>0,\end{array}\right.,
$$

while the function is not differentiable in $x=0$. In particular, the derivative of this function is never $0$. Still, if we consider the graph of this function, it clearly has a local minimum in $0$. This is precisely the point where the function is not differentiable. This is supported by the graph of $|x|$ shown in {numref}`Fig:MinMax:IntroLocExtr`.

:::{figure} Images/Fig-MinMax-IntroLocExtr.png
:name: Fig:MinMax:IntroLocExtr

The graph of the function $f(x)=|x|$ and it's local extremum at $0$.
:::

:::{todo}
Make an applet of {numref}`Fig:MinMax:IntroLocExtr`.
:::


We conclude that functions can also attain local extrema in points where the function is not differentiable. Let us introduce some terminology for this.


::::::{prf:definition} 
:label: Def:MinMax:Critical
Suppose that the domain of a function $f$ contains an open interval $I$. Then $c$ in $I$ is called a **critical point** of $f$ if either $f$ is not differentiable in $c$ or if $f'(c)=0$.
::::::

::::::{prf:corollary}
:label: Cor:MinMax:Critical
If a function $f$ has a local maximum or local minimum at $c$, then $c$ is a critical point of $f$.
::::::

:::{admonition} Proof of {prf:ref}`Cor:MinMax:Critical`
:class: tudproof
If $f$ is not differentiable at $c$, then $c$ is a critical point of $f$ by definition. On the other hand, if $f$ is differentiable at $c$, then we have $f'(c)=0$ on account of {prf:ref}`Thm:MinMax:Fermat`, so then $c$ is a critical point as well.
:::

:::{warning}
The reverse statement of {prf:ref}`Cor:MinMax:Critical` is not true. For instance, the function $f(x)=x^3+1$ has a critical point at $0$, since $f'(0)=0$. However, the function does not have a local extremum there. Indeed, for $x<0$ we have $f(x)=x^3+1<1$, so $f(0)=1$ cannot be a local minimum of $f$. In addition, for $x>0$ we have $f(x)=x^3+1>1$, so $f(0)=1$ cannot be a local maximum of $f$ either.
:::

::::::{prf:example} 
:label: Ex:MinMax:Critical
Consider the function $f(x)=2|x|-x^2$. Let us try to find all critical points of this function. We first note that the function is not differentiable in $0$, so $0$ is a critical point. For $x>0$, we can write $f(x)=2x-x^2$, and we can evaluate the derivative as

$$
 f'(x)=2-2x.
$$

Then we see that $f'(x)=0$ only for $x=1$, so $1$ is a critical point of $f$. 

Similarly, we can write $f(x)=-2x-x^2$ for $x<0$. Then the derivative becomes

$$
 f'(x)=-2-2x.
$$

We find that $f'(x)=0$ only for $x=-1$, so $-1$ is another critical point of $f$.

We conclude that $f$ has three critical points: $-1$, $0$ and $1$. So how would we find out if $f$ has a local extremum in any of these points? One way to do this, is to note that $f'(x)>0$ for $x<-1$, while $f'(x)<0$ for $-1<x<0$. This means that the function increases on the interval $(-\infty,-1)$, while it decreases on the interval $(-1,0)$. Since $f$ is continuous in $-1$, this can only happen if $f(-1)\geq f(x)$ for all $x$ in $(-\infty,0)$. So $f$ has a local maximum in $-1$. 

Similarly, we find that $f'(x)>0$ for $0<x<1$ and $f'(x)<0$ for $x>1$. This means that $f$ is increasing on the interval $(0,1)$ and decreasing on $(1,\infty)$. Using a similar reasoning, this means that $f$ has a local minimum in $0$ and a local maximum in $1$.

{numref}`Fig:MinMax:Critical` shows the graph of the function $f$ and indicates the points where the function has a local extremum.

:::{figure} Images/Fig-MinMax-Critical.png
:name: Fig:MinMax:Critical

The graph of the function $f$ from {prf:ref}`Ex:MinMax:Critical`.
:::

:::{todo}
Turn {numref}`Fig:MinMax:Critical` into an applet.
:::

::::::

The reasoning we used in {prf:ref}`Ex:MinMax:Critical` to determine whether the critical points were local maxima, local minima or neither of these can be applied in general. This result is known as the first derivative test (in contrast to the second derivative test that we will discuss later).

::::::{prf:theorem} First derivative test 
:label: Thm:MinMax:Firstdertest
Let $c$ be a point in the domain of a continuous function $f$.

- If $f'$ changes from negative to positive at $c$, i.e. $f'(x)\leq 0$ for $x<c$ near $c$ and $f'(x)\geq 0$ for $x>c$ near $c$, then $f(c)$ is a local minimum of $f$.
- If $f'$ changes from positive to negative at $c$, i.e. $f'(x)\geq 0$ for $x<c$ near $c$ and $f'(x)\leq 0$ for $x>c$ near $c$, then $f(c)$ is a local maximum of $f$.
- If $f'(x)>0$ for all $x$ near $c$ (excluding $x=c$) or if $f'(x)<0$ for all $x$ near $c$ (excluding $x=c$) then $f(c)$ is neither a local minimum nor a local maximum of $f$.
::::::

Before we turn to the proof of {prf:ref}`Thm:MinMax:Firstdertest`, we illustrate the different cases of this theorem in {numref}`Fig:MinMax:Firstdertest`.

:::{figure} Images/Fig-MinMax-Firstdiv.png
:name: Fig:MinMax:Firstdiv
:class: dark-light

Illustration of {prf:ref}`Thm:MinMax:Firstdiv`.
(a) $f'$ changes from negative to positive at $c$; (b) $f'$ changes from positive to negative at $c$; (c) $f'(x)>0$ for all $x\neq c$; $f'(x)<0$ for all $x\neq c$.
:::

:::{todo}
Turn {numref}`Fig:MinMax:Firstdiv` into an applet.
:::

{numref}`Fig:MinMax:Firstdiv`(a) clearly shows a local minimum at $x=c$. If you drag the point along the graph, you can see that the slope of the tangent line changes from negative to positive at $x=c$. Similarly, {numref}`Fig:MinMax:Firstdiv`(b) clearly shows a local maximum at $c$, and the slope of the tangent line changes from positive to negative at $c$. Finally, {numref}`Fig:MinMax:Firstdiv`(c) and (d) show graphs that neither have a local minimum nor a local maximum, and the slope of the tangent line is either positive or negative on both sides of $c$. These cases illustrate the different cases of {prf:ref}`Thm:MinMax:Firstdertest`.

Now you can read the proof of {prf:ref}`Thm:MinMax:Firstdertest`.

:::{admonition} Proof of {prf:ref}`Thm:MinMax:Firstdertest`
:class: tudproof, dropdown
Let $I=(a,b)$ be an open interval that contains $c$ and suppose $f'(x)\leq 0$ for $x$ in $I$ with $x<c$ and $f'(x)\geq 0$ for $x$ in $I$ with $x>c$. We will show that $f(c)$ is a local minimum of $f$. For this, we first show that $f$ is decreasing on $(a,c]$ (so including at the point $c$). On account of {prf:ref}`Thm:Graphsderivatives:Increasingdecreasing`, the function $f$ is decreasing on $(a,c)$. We argue by contradiction and assume that we can find $d$ in $(a,c)$ with $f(d)<f(c)$. Since $f$ is decreasing on $[d,c)$, we must have

$$
 f(x)\leq f(d)<f(c)
$$

for all $d\leq x<c$. We write $\varepsilon=\dfrac{f(c)-f(d)}{2}>0$. Since $f$ is continuous at $c$, we can find $\delta>0$ such that for all $x$ with $0<|x-c|<\delta$ we have $|f(x)-f(c)|<\varepsilon$, which means that

$$
 -\varepsilon<f(x)-f(c)<\varepsilon.
$$

Then for any value of $x$ with both $d\leq x<c$ and $0<|x-c|<\delta$, we have on the one hand $f(x)<f(c)$, while on the other hand we have

$$
 f(x)>f(c)-\varepsilon=f(c)-\dfrac{f(c)-f(d)}{2}=\frac{f(c)}{2}+\frac{f(d)}{2}>\frac{f(c)}{2}+\frac{f(c)}{2}=f(c).
$$

This gives a contradiction, so we find that 

$$
 f(x)\geq f(c)
$$

for all $x$ in $I$ with $x\leq c$. 

Now we show that $f$ is increasing on $[c,b)$. {prf:ref}`Thm:Graphsderivatives:Increasingdecreasing` gives that the function $f$ is increasing on $(c,b)$. We again argue by contradiction and assume that we can find $d$ in $(c,b)$ with $f(d)<f(c)$. Then $f$ is increasing on $(c,d)$, so we must have

$$
 f(x)\leq f(d)<f(c)
$$

for all $c<x\leq d$. Then with the same choices for $\varepsilon$ and $\delta$ as before, we find for any $x$ with both $c<x\leq d$ and $0<|x-c|<\delta$ that on the hand we have $f(x)<f(x)$, while on the other hand we have

$$
 f(x)>f(c)-\varepsilon=f(c)-\dfrac{f(c)-f(d)}{2}=\frac{f(c)}{2}+\frac{f(d)}{2}>\frac{f(c)}{2}+\frac{f(c)}{2}=f(c).
$$

This again gives a contradiction. So $f(c)$ must be a local minimum of $f$.

Now suppose that $f'$ changes from positive to negative at $c$. Then $-f'$ changes from negative to positive at $c$, so by the first part of this proof we find that $-f$ has a local minimum at $c$. Then for $x$ close to $c$ we have

$$
 -f(x)\geq -f(c).
$$

Multiplying this equation by $-1$ gives 

$$
 f(x)\leq f(c)
$$

for $x$ near $c$. This means that $f(c)$ is a local maximal value of $f$.

Now suppose that $f'(x)>0$ for all $x$ in $I$ with $x\neq c$. By the first part of the proof $f$ is increasing on $(a,c]$, so we have 

$$
 f(x)\leq f(c)
$$

for all $x$ in $I$ with $x\leq c$. Note that it is not possible that there is $d$ in $I$ with $d<c$ and $f(d)=f(c)$, since on account of {prf:ref}`Thm:Graphsderivatives:Increasingdecreasing` $f$ must be strictly increasing on the interval $[d,c)$. So we find that

$$
 f(x)< f(c)
$$

for all $x$ in $I$ with $x< c$. As such, $f$ cannot have a local minimum at $c$. Using a similar reasoning, $f$ must be strictly decreasing on $[c,b)$, so we have 

$$
 f(x)> f(c)
$$

for all $x$ in $I$ with $x> c$. So $f$ cannot have a local maximum at $c$ either. 

Finally, we suppose that $f'(x)<0$ for all $x$ in $I$ with $x\neq c$. Then $-f'(x)>0$ for all $x$ in $I$ with $x\neq c$, so by the previous part, $-f$ cannot have a local minimum or a local maximum at $c$. Then $f$ cannot have a local extremum at $c$ either.
:::

::::{note}

:::{figure} Images/Fig-MinMax-NoteCont.png
:name: Fig:MinMax:NoteCont
:figclass: margin

The graph of the function $f$ from the note. The function is not continuous at $0$, so we cannot apply {prf:ref}`Thm:MinMax:Firstdertest`. Still, the function has a local maximum at $0$.
:::

:::{todo}
Turn {numref}`Fig:MinMax:NoteCont` into an applet.
:::

The continuity of $f$ at the point $c$ is necessary for {prf:ref}`Thm:MinMax:Firstdertest` to work. Indeed, consider the function 

$$
 f(x)=\left\{\begin{array}{l}x^2,\qquad&\text{if}\ x\neq 0\\ 1,\qquad &\text{if}\ x=0.\end{array}\right.
$$

Then we see that $f'(x)=2x<0$ for $x<0$, while $f'(x)=2x>0$ for $x>0$. On account of {prf:ref}`Thm:MinMax:Firstdertest` (which we cannot apply here since $f$ is not continuous at $0$) you would expect $f$ to have a local minimum at $0$. However, the function actually has a local maximum there, since for any $-1<x<1$ with $x\neq 0$ we have

$$
 f(x)=x^2<1=f(0).
$$

The graph of $f$ also supports this conclusion, see {numref}`Fig:MinMax:NoteCont`.

::::

::::::{prf:example} 
:label: Ex:MinMax:Firstdivtest
Consider the function $f(x)=x+\sin(2x)$ on the interval $(0,2\pi)$ and suppose we want to find and classify all critical points of $f$. First we note that $f$ is differentiable on its domain and we have

$$
 f'(x)=1+2\cos(2x).
$$

In order to find the critical points, we solve $f'(x)=0$, which gives

$$
 1+2\cos(2x)=0,\qquad\Longleftrightarrow\qquad \cos(2x)=-\frac{1}{2}.
$$

Using the standard values of the cosine, we find that $2x=\dfrac{2\pi}{3}+k2\pi$ or $2x=-\dfrac{2\pi}{3}+k2\pi$ for any integer $k$. Of these, only the values $x=\dfrac{\pi}{3}$, $x=\dfrac{2\pi}{3}$, $x=\dfrac{4\pi}{3}$ and $x=\dfrac{5\pi}{3}$ are in the interval $(0,2\pi)$, so the function $f$ has $4$ critical points in this interval. In order to use {prf:ref}`Thm:MinMax:Firstdertest`, we need to know where $f'$ is positive and where it is negative. Since $f'$ is continuous, it can only change from positive to negative or vice versa at one of the critical points. So in each of the intervals $\left(0,\dfrac{\pi}{3}\right)$, $\left(\dfrac{\pi}{3},\dfrac{2\pi}{3}\right)$, $\left(\dfrac{2\pi}{3},\dfrac{4\pi}{3}\right)$, $\left(\dfrac{4\pi}{3},\dfrac{5\pi}{3}\right)$ and $\left(\dfrac{5\pi}{3},2\pi\right)$ we can plug in $1$ conveniently chosen point to determine whether the derivative is positive or negative on that interval. For instance, we find

$$
 f'\left(\frac{\pi}{6}\right)=2>0,\qquad f'\left(\frac{\pi}{2}\right)=-1<0, \qquad f'\left(\pi\right)=3>0,
$$

$$
 f'\left(\frac{3\pi}{2}\right)=-1<0,\qquad f'\left(\frac{11\pi}{6}\right)=2>0.
$$

We conclude that $f'>0$ on the intervals $\left(0,\dfrac{\pi}{3}\right)$, $\left(\dfrac{2\pi}{3},\dfrac{4\pi}{3}\right)$ and $\left(\dfrac{5\pi}{3},2\pi\right)$, while $f'<0$ on the intervals $\left(\dfrac{\pi}{3},\dfrac{2\pi}{3}\right)$ and $\left(\dfrac{4\pi}{3},\dfrac{5\pi}{3}\right)$. A convenient way to denote this behaviour is by a **sign chart**, see {numref}`Fig:MinMax:Signchart`.

:::{figure} Images/Fig-MinMax-Signchart.png
---
width: 100%
name: Fig:MinMax:Signchart
class: dark-light
---
A sign chart shows on which intervals the derivative is positive and on which it is negative.
:::

:::{todo}
Turn {numref}`Fig:MinMax:Signchart` into an applet.
:::

According to {prf:ref}`Thm:MinMax:Firstdertest` the function attains a local maximum at $x=\dfrac{\pi}{3}$ and $x=\dfrac{4\pi}{3}$, while it attains a local minimum at $x=\dfrac{2\pi}{3}$ and $x=\dfrac{5\pi}{3}$. This can also be seen in the graph of the function.

:::{figure} Images/Fig-MinMax-Firstdivtest2.png
:name: Fig:MinMax:Firstdivtest2

The graph of the function $f$ from {prf:ref}`Ex:MinMax:Firstdivtest` and its local extrema.
:::

:::{todo}
Convert {numref}`Fig:MinMax:Firstdivtest2` into an applet.
:::

::::::

For some functions, it takes quite some effort to determine where the derivative is positive and where it is negative. Fortunately, there is another test that can be used to classify a critical point of a function. This test is called the **second derivative test** and as the name suggests, it uses the second derivative of the function. 

::::::{prf:theorem} Second derivative test 
:label: Thm:MinMax:Seconddertest
Let $c$ be a point with $f'(c)=0$ and suppose that $f$ is continuous on an open interval containing $c$.

- If $f''(c)<0$, then $f(c)$ is a local minimum of $f$.
- If $f''(c)>0$, then $f(c)$ is a local maximum of $f$.
- If $f''(c)=0$, then the test is inconclusive.
::::::

:::{admonition} Proof of {prf:ref}`Thm:MinMax:Seconddertest`
:class: tudproof, dropdown
Suppose that $f''(c)>0$. Since $f'(c)=0$, we can write

$$
 0<f''(c)=\lim_{h\rightarrow 0}\frac{f'(c+h)-f'(c)}{h}=\lim_{h\rightarrow 0}\frac{f'(c+h)-0}{h}=\lim_{h\rightarrow 0}\frac{f'(c+h)}{h}.
$$

We write $\varepsilon=\frac{f''(c)}{2}>0$. By the definition of a limit, we can find $\delta>0$ such that for all $h$ with $0<|h|<\delta$ we have

$$
 \left|\frac{f'(c+h)}{h}-f''(c)\right|<\varepsilon,
$$

which gives

$$
 \frac{f'(c+h)}{h}>f''(c)-\varepsilon=\frac{f''(c)}{2}>0.
$$

We want to multiply this equation by $h$, but then we have to make a distinction between positive and negative values of $h$, since for negative values of $h$ the inequality sign flips. For $h<0$ we obtain

$$
 f'(c+h)<0,
$$

while for $h>0$ we obtain

$$
 f'(c+h)>0.
$$

This means that $f'$ changes from negative to positive at $c$. So by {prf:ref}`Thm:MinMax:Firstdertest`, the original function $f$ has a local minimum at $c$.

Now suppose that $f''(c)<0$. Then $-f''(c)>0$, while we also have $-f'(c)=0$. By the first part of this proof, $-f$ has a local minimum at $c$, which means that $f$ has a local maximum at $c$.
:::

:::{note}
An advantage the second derivative test has over the first derivative test is that it can be generalised to functions of more than one variable (see {numref}`Section:LocalExtremaMulti`), while that is not the case for the first derivative test. So making sure that you understand the second derivative test now, can help you later when studying these harder functions. 
:::

::::{note}
A major disadvantage of the second derivative test is that it can never be used to show that a critical point is **not** a local extremum. Indeed, anything can happen when the second derivative is $0$ in a critical point. For instance, if we consider the functions $f(x)=x^4$, $g(x)=5x^5$ and $h(x)=-\frac16x^6$, then $0$ is a critical point for each of these and the second derivative of each of these functions is $0$ in $0$. However, using the first derivative test we can show that $f$ has a local minimum in $0$, $g$ does not have a local extremum in $0$, while $h$ has a local maximum in $0$. This can also be seen in the graphs of these functions.


:::{figure} Images/Fig-MinMax-SeconddivNote.png
:name: Fig:MinMax:SeconddivNote

Three functions with a critical point in $0$ and a second derivative of $0$ in $0$. The function $f(x)=x^4$ has a local minimum at $0$, the function $g(x)=5x^5$ does not have a local extremum at $0$, while the function $h(x)=-\frac16x^6$ has a local maximum at $0$.

:::

:::{todo}
Replace {numref}`Fig:MinMax:SeconddivNote` with an applet.
:::

::::

:::{note}
If you have trouble remembering whether, say, a positive value of the second derivative gives a local maximum or a local minimum, it might be worthwhile to consider the functions $f(x)=x^2$ and $g(x)=-x^2$. Both have a critical point at $0$ and finding their second derivatives is easy: we have $f''(x)=2$, which is positive, while $g''(x)=-2$, which is negative. For these function, you already **know** whether they have a local maximum or a local minimum, as their graphs are an upward opening and downward opening parabola respectively. 

:::

::::::{prf:example} 
:label: Ex:MinMax:Seconddiv
Consider the function 

$$ 
 f(x)=x^4+2\cos(x).
$$ 
Then its derivative is given by 

$$
 f'(x)=4x^3-2\sin(x).
$$

We note that $f'(0)=0$, so $0$ is a critical point of $f$. However, for this function it is rather difficult to see where the first derivative is positive and where it is negative. We could try to just plug in points in between the critical points like we did in {prf:ref}`Ex:MinMax:Firstdivtest`, but then we would need to be certain where the other critical points (if any) are, and solving the equation $f'(x)=0$ is hard in this case. 

However, the second derivative test can be applied without worrying about these things. Indeed, we find that

$$
 f''(x)=12x^2-2\cos(x),
$$

which gives

$$
 f''(0)=-2<0.
$$

So according to {prf:ref}`Thm:MinMax:Seconddertest`, $f$ has a local maximum at $0$.

Our conclusion are supported by the graphs of $f$, $f'$ and $f''$ shown in {numref}`Fig:MinMax:SeconddivEx`.

:::{figure} Images/Fig-MinMax-SeconddivEx.png
:name: Fig:MinMax:SeconddivEx

The graph of the function $f$, $f'$ and $f''$ from {prf:ref}`Ex:MinMax:Seconddiv` and the local extrema of $f$.
:::

:::{todo}
Convert {numref}`Fig:MinMax:SeconddivEx` into an applet.
:::
::::::

(Subsec:Extrema1dEVT)=

## Global extrema

Recall that local extrema only consider the behaviour of a function near a critical point. However, if a function has a local maximum at a critical point, it might still have function values that are even larger somewhere far away from the critical point, see for example the function shown in {numref}`Fig:MinMax:SeconddivEx`.

As such, it is also interesting to consider the highest and lowest values a function can attain without looking only locally, or in other words, to look globally. This leads us to the following definition.

::::::{prf:definition} 
:label: Def:MinMax:GlobExtr
Let $c$ be in the domain of a function $f$.

Then we say that $f$ has a **global maximum** at $c$, or that $f(c)$ is the **global maximum** value of $f$, if $f(c)\geq f(x)$ for all $x$ in the domain of $f$. 

Similarly, we say that $f$ has a **global minimum** at $c$, or that $f(c)$ is the **global minimum** value of $f$, if $f(c)\leq f(x)$ for all $x$ in the domain of $f$.

A **global extremum** or **global extreme value** is a global maximum or a global minimum.
::::::

Global maxima and minima are sometimes called **absolute** maxima and minima. We however have opted for the term global maximum and global minimum, since the term absolute can cause confusion with the absolute value function.

{numref}`Fig:MinMax:GlobExtr` shows a graph of a function with some local and global extrema. This function attains its global minimum value in $a$. It does not attain a local minimum there, since $a$ is on the boundary of the domain. It attains its global maximum in $b$, which is also a local maximum. It has a local minimum in $c$. The point $d$ is neither a local nor a global extremum.

:::{figure} Images/Fig-MinMax-GlobExtr.png
:name: Fig:MinMax:GlobExtr
:class: dark-light

A graph to illustrate the difference between local and global extrema.
:::

:::{todo}
Turn {numref}`Fig:MinMax:GlobExtr` into an applet.
:::

:::{note}
A function does not need to have a global maximum value (or a global minimum value). Consider, for instance, the function $f(x)=\dfrac{1}{x}$. This function has a vertical asymptote at $x=0$, and the function values can get arbitrarily large for $x$ close to $0$.
:::

:::{note}
If a function has a global maximum value, there is only $1$ such value. After all, the global maximum value is the highest function value that is attained and there can only be $1$ highest value. Still, this highest value can be attained in multiple points. For instance, consider the function $f(x)=3x^2$ for $-1\leq x\leq 1$. Then the global maximum value is $3$, which is attained at both $x=-1$ and at $x=1$.

:::

Consider a function $f$ that is continuous on a closed interval $[a,b]$. Is it possible for $f$ to have a vertical asymptote on this interval? The answer is no, since if the function has a vertical asymptote at a point $c$, the function values would need to make a jump from very large or very negative values to the value $f(c)$, which is impossible for a continuous function. In principle, continuous functions can have vertical asymptotes. For instance, the function $f(x)=\dfrac{1}{x}$ has a vertical asymptote at $x=0$. However, although this function is continuous on its domain, is not continuous on any closed interval that contains $0$, since it is undefined there. So the fact that we are dealing with a closed interval is essential here.

This idea suggests that continuous functions cannot "blow up" on closed intervals. The precise version of this idea is known as the **boundedness theorem**.


::::::{prf:theorem} Boundedness theorem
:label: Thm:MinMax:Boundedness
Let $f$ be a function that is continuous on $[a,b]$. Then $f$ is bounded on $[a,b]$. That is, there are real numbers $m$ and $M$ with 

$$
 m\leq f(x)\leq M
$$

 for all $x$ in $[a,b]$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:MinMax:Boundedness`
:class: tudproof, dropdown
The proof of this result is a bit beyond the scope of this book as it used the completeness of the real numbers, but we include it for completeness. Feel free to skip the proof.

We let $S$ denote the set of all $s$ in the interval $[a,b]$ such that $f$ is bounded on the closed interval $[a,s]$. $f$ is definitely bounded on the interval $[a,a]$ (which is just the single point $\{a\}$), so $a$ is in $S$. In particular, $S$ is not the empty set.

Now if $s>a$ were another point in $S$, then $f$ is bounded on $[a,s]$. That means that we can find $m$ and $M$ with

$$
 m\leq f(x)\leq M
$$

for all $a\leq x\leq s$. Now for any $a<t<s$ and any $a\leq x\leq t$ we still have $m\leq f(x)\leq M$. That precisely means that $t$ is in $S$ as well. So if $s$ is in $S$, then the entire interval $[a,s]$ a subset of $S$ as well.

Since $f$ is continuous at $a$ (or, at least, right-continuous), we can let $\delta_1>0$ such that for all $x$ in $[a,b]$ with $0<|x-a|<\delta_1$ we have 

$$
 |f(x)-f(a)|<1.
$$

Without loss of generality, we can assume that $a+\frac{\delta_1}{2}\leq b$. Then for $a\leq x\leq a+\frac{\delta_1}{2}$ we have $|f(x)-f(a)|<1$, which means that

$$
 f(a)-1\leq f(x)\leq f(a)+1.
$$

That is, the function values of $f$ are bounded in between $f(a)-1$ and $f(a)+1$ on the interval $\left[a,a+\frac{\delta_1}{2}\right]$. As such, $a+\frac{\delta_1}{2}$ must be in $S$ and by our previous considerations, the entire interval $\left[a,a+\frac{\delta_1}{2}\right]$ is a subset of $S$.

Finally, for any $s$ in $S$, we have $s\leq b$ by definition of the set $S$. So $S$ is bounded above by $b$.

Since $S$ is a nonempty set that is bounded above, it has a supremum (least upper bound) by the completeness of the real numbers. Let us call this supremum $s$. Since $b$ is an upper bound of $S$, we have $s\leq b$. Since $S$ contains the interval $\left[a,a+\frac{\delta_1}{2}\right]$ we also have $s>a$. We will show that $s=b$. Let us argue by contradiction and assume that $s<b$. Since $f$ is continuous at $s$, we can find $\delta_2>0$ such that for all $x$ with $0<|x-s|<\delta_2$ we have

$$
 |f(x)-f(s)|<1.
$$

Just like before, this means that $f$ is bounded on $\left[s-\frac{\delta_2}{2},s+\frac{\delta_2}{2}\right]$. Since $s<b$, we can, without loss of generality assume that $s+\frac{\delta_2}{2}\leq b$. Since $s$ is the supremum of $S$, there must be a point $t$ in $S$ with $s-\frac{\delta_2}{2}\leq t$. Since $t$ is in $S$, $f$ is bounded on $[a,t]$. Then $f$ is bounded on both $[a,t]$ and $\left[s-\frac{\delta_2}{2},s+\frac{\delta_2}{2}\right]$ and since $s-\frac{\delta_2}{2}\leq t$, we find that $f$ is bounded on $\left[a,s+\frac{\delta_2}{2}\right]$. This means that $s+\frac{\delta_2}{2}$ is in $S$, but this is impossible, since $s$ is the supremum of $S$.

So we find that $s=b$. Unfortunately, that still does not automatically mean that $f$ is bounded on $[a,b]$ as $s$ does not necessarily need to be in $S$ ($S$ could, potentially, be the half-open interval $[a,b)$). To show that $f$ is bounded on $[a,b]$ we will use that $f$ is (left)-continuous in $b$. Indeed, we can take $\delta_3>0$ such that for all $x$ in $[a,b]$ with $0<|x-b|<\delta_3$ we have

$$
 |f(x)-f(b)|<1.
$$

Just like earlier, we find that $f$ must be bounded on $\left[b-\frac{\delta_3}{2},b\right]$. Since $b$ is the supremum of $S$, we can find $t$ in $S$ with $b-\frac{\delta_3}{2}\leq t$. Since $t$ is in $S$, $f$ is bounded on $[a,t]$. Then $f$ is bounded on both $[a,t]$ and $\left[b-\frac{\delta_3}{2},b\right]$ and since $b-\frac{\delta_3}{2}\leq t$, we find that $f$ is bounded on $\left[a,b\right]$, as desired.
:::

We can use the fact that continuous functions on closed intervals are bounded to show that these functions must attain their global extreme values. This result is known as the **extreme value theorem** and is considered a very important theorem in calculus.

::::::{prf:theorem} Extreme value theorem
:label: Thm:MinMax:EVT
Let $f$ be a function that is continuous on $[a,b]$. Then there are $c$ and $d$ in $[a,b]$ such that $f(c)$ is the absolute maximum and $f(d)$ is the absolute minimum of $f$ on $[a,b]$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:MinMax:EVT`
:class: tudproof, dropdown
This proof uses the completeness of the real numbers, just like the proof of {prf:ref}`Thm:MinMax:Boundedness`. Feel free to skip the proof.

The range of $f$ on $[a,b]$, i.e. the set 

$$
 R=\{y\in\mathbb{R}\,|\,y=f(x)\ \text{for}\ \text{some}\ x\in[a,b]\},
$$

is a bounded set by {prf:ref}`Thm:MinMax:Boundedness`. In addition, it is nonempty as it contains $f(a)$. By the completeness of the real numbers, the set $R$ has a supremum $M$. We will show that $M$ is the absolute maximum of $f$ on $[a,b]$. We will argue by contradiction, so we assume that $f(x)<M$ for all $x$ in $[a,b]$. Consider the function

$$
 g(x)=\frac{1}{M-f(x)}.
$$

Since $f(x)<M$ for all $x$ in $[a,b]$, $g$ is a continuous function on $[a,b]$. We will show that $g$ is unbounded on this interval, which contradicts {prf:ref}`Thm:MinMax:Boundedness`.

Consider any $N>0$ and write $\varepsilon=\dfrac{1}{N}$. Since $M$ is the supremum of the range $R$, we can find $y$ in $R$ with $y>M-\varepsilon$. That is, we can find $x$ in $[a,b]$ with 

$$
 f(x)>M-\varepsilon,
$$

which means that

$$
 M-f(x)<\varepsilon.
$$

For this value of $x$, we find that 

$$
 g(x)=g(x)=\frac{1}{M-f(x)}>\frac{1}{\varepsilon}=N.
$$

So that means that $N$ is not an upper bound of $g$ on $[a,b]$. Since this holds for any $N>0$, $g$ cannot be bounded on $[a,b]$. This contradicts {prf:ref}`Thm:MinMax:Boundedness`. So there must be some $c$ in $[a,b]$ with $f(c)=M$, as desired.

Since the function $-f$ is continuous, we can find $d$ in $[a,b]$ with $-f(x)\leq -f(d)$ for all $x$ in $[a,b]$. This means that $f(x)\geq f(d)$ for all $x$ in $[a,b]$, so $f$ also attains an absolute minimum on $[a,b]$.
:::

Both conditions that we are working with a continuous function on a closed interval are necessary for the theorem to work, as can be seen in {numref}`Fig:MinMax:EVT`. In (a) the continuous function $f(x)=\dfrac{1}{x}$ does not attain a global maximum on the non-closed interval $(0,1)$. In (b) for the non-continuous function $g(x)=\left\{\begin{array}{l}x,\qquad &\text{if}\ 0\leq x<2,\\ 1,\qquad &\text{if}\ 2\leq x\leq 4\end{array}\right.$ on the closed interval $[0,4]$, the function values can get arbitrarily close to $2$, but they never actually become $2$, so this function does not attain a global maximum. It does attain a global minimum at $0$.

:::{figure} Images/Fig-MinMax-EVT.png
---
width: 100%
name: Fig:MinMax:EVT
class: dark-light
---
(a) The continuous function $f(x)=\dfrac{1}{x}$ on the non-closed interval $(0,1)$.<br>(b) The function $g(x)=\left\{\begin{array}{l}x,\qquad &\text{if}\ 0\leq x<2,\\ 1,\qquad &\text{if}\ 2\leq x\leq 4\end{array}\right.$ on the closed interval $[0,4]$. 
:::

:::{todo}
Turn {numref}`Fig:MinMax:EVT` into an applet.
:::

[^FootnoteWeierstrass]: Looking at you, [Weierstrass function](https://en.wikipedia.org/wiki/Weierstrass_function).

:::{note}
Even though you are reading the chapter on differentiation and we usually like to think of extrema in terms of derivatives, {prf:ref}`Thm:MinMax:EVT` does not use derivatives **in any way**. Indeed, this result also applies to functions that are nowhere differentiable, as long as they are continuous[^FootnoteWeierstrass].

:::

With the {prf:ref}`Thm:MinMax:EVT`, we can now finally prove Rolle's theorem.

:::{admonition} Proof of {prf:ref}`Thm:Graphsderivatives:Rolle`
:class: tudproof, dropdown
First suppose that the function is constant on the interval $[a,b]$. Since the function is constant, we have $f'(c)=0$ for all $c$ in $(a,b)$.

Now suppose that the function is not constant on the interval $[a,b]$. By {prf:ref}`Thm:MinMax:EVT`, $f$ attains both a local maximum and a local minimum on the interval $[a,b]$. Since $f(a)=f(b)$ and $f$ is not constant, at least one of these two must occur at a point $c$ in the open interval $(a,b)$. Indeed, if they were to both occur at the edge values $a$ or $b$, then $f(a)=f(b)$ would both be the highest value and the lowest value of $f$ on $[a,b]$, which would mean that $f$ is constant on $[a,b]$. By {prf:ref}`Thm:MinMax:Fermat` we have that $f'(c)=0$, as desired.
:::

[^FootnoteCIM]: If the function has infinitely many critical points, then this method may fail to work.

So how do we find the locations of the global maximum and global minimum values of a continuous function on a closed interval $[a,b]$?

If a global extremum is in the open interval $(a,b)$ then we can apply {prf:ref}`Cor:MinMax:Critical` to conclude that the global extremum is attained at a critical point. And if not, then, well, there are not an awful lot of options left, since the only points that we have not considered are the points $a$ and $b$. So this gives us a way to find all *candidate locations* for the global extreme values.

So how do we then determine which of these corresponds to the global maximum and which to the global minimum?

You might expect that we need to perform all sorts of tests, like {prf:ref}`Thm:MinMax:Firstdertest` or {prf:ref}`Thm:MinMax:Seconddertest`, but that is not the case. Indeed, if I know that the global maximum occurs at one of, say, five points[^FootnoteCIM], then I can just evaluate the function at each of these five points. The largest value I obtain this way **must** be the global maximum value, as this value cannot be attained anywhere else. Similarly, the lowest value **must** be the global minimum value.

With that, we have motivated the following algorithm, called the **closed interval method** to find the global extrema.

::::::{prf:algorithm} Closed interval method
:label: Alg:MinMax:Globalextrema

Let $f$ be a continuous function on a closed interval $[a,b]$. Then we can find the global extreme values of $f$ as follows:

1. Find all points in $(a,b)$ where $f$ is not differentiable.
2. Find all points $c$ in $(a,b)$ with $f'(c)=0$.
3. Find the function values of $f$ at the critical points found in steps 1. and 2.
4. Find the function values of $f$ at the end points $a$ and $b$ of the interval.
5. The highest value from steps 3. and 4. is the global maximum value; the lowest value is the global minimum value.



::::::

:::{warning}
When performing {prf:ref}`Alg:MinMax:Globalextrema`, there is no need to classify the critical points.
:::

:::{warning}
When performing {prf:ref}`Alg:MinMax:Globalextrema`, make sure to only consider those critical points that lie in the interval $(a,b)$. Any critical point outside of this interval should be ignored.
:::

Let us see how this method works in practice by considering a few examples.

::::::{prf:example} Closed interval method
:label: Ex:MinMax:Globalextrema1
Consider the function $f(x)=2x^3+3x^2-12x-5$ on the closed interval $[-4,2]$. Suppose we want to find the location and the value of the global maximum and the global minimum on this interval. For this, we perform {prf:ref}`Alg:MinMax:Globalextrema`.

1. The function $f$ is differentiable on the entire domain $(-4,2)$, so we do not obtain any new candidate points in this step.
2. In order to find the points where the derivative is $0$, we first evaluate

   $$
   f'(x)=6x^2+6x-12.
   $$

   The equation $f'(x)=0$ becomes $6x^2+6x-12=0$, which is a quadratic equation, so we know how to solve this equation. We obtain the solutions $x=1$ and $x=-2$, which both lie in the interval $(-4,2)$. So these two points are the first two candidate points for the location of the global maximum and the global minimum.

3. We need to evaluate $f$ at the points found in steps 1. and 2. We obtain

   $$
   f(-2)=15,\qquad f(1)=-12.
   $$

4. We know evaluate $f$ at the boundary points, which gives

   $$
   f(-4)=-37,\qquad f(2)=-1.
   $$

5. According to {prf:ref}`Cor:MinMax:Critical`, the location of the global maximum and the location of the global minimum must be one of the points $x=-4$, $x=-2$, $x=1$ and $x=2$. As such, the lowest value that we obtained in steps 3. and 4. must be the global minimum value, which means that $f$ attains its global minimum of $-37$ at the boundary point $x=-4$. Similarly, the highest value is the global maximum value, so $f$ attains its global maximum of $15$ at the critical point $x=-2$.

The graph of the function is shown in {numref}`Fig:MinMax:Globalextrema1`. Do our conclusions match what we see in the graph?

:::{figure} Images/Fig-MinMax-Globalextrema1.png
:name: Fig:MinMax:Globalextrema1

The graph of the function $f$ from {prf:ref}`Ex:MinMax:Globalextrema1` and its local and global extrema.
:::

:::{todo}
Convert {numref}`Fig:MinMax:Globalextrema1` to an applet Make sure to highlight all candidate points and make difference between local and global extrema clear.
:::
::::::

::::::{prf:example} Closed interval method
:label: Ex:MinMax:Globalextrema2
Consider the function $f(x)=\dfrac{|x|}{2}-\cos(x)$ on the closed interval $[-2\pi,2\pi]$ and suppose we want to find the global minimum and global maximum values. We again perform {prf:ref}`Alg:MinMax:Globalextrema`.

1. The function $f$ is not differentiable in $0$ (since $|x|$ is not differentiable there, while the cosine is differentiable), so the point $x=0$ is a candidate location.

2. In order to find the values of $x$ where $f'(x)=0$, we need to separate between the cases $x>0$ and $x<0$. For $x<0$, we have $|x|=-x$, so we obtain

   $$
   f'(x)=-\frac{1}{2}+\sin(x).
   $$

   Setting $f'(x)=0$ gives $\sin(x)=\dfrac{1}{2}$, which means that $x=\dfrac{\pi}{6}+k2\pi$ of $x=\dfrac{5\pi}{6}+k2\pi$ for some integer $k$. Of these values of $x$, we are only interested in those that lie in the interval $[-2\pi,2\pi]$ **and** have $x<0$, so this leaves us with $x=-\dfrac{11\pi}{6}$ and $x=-\dfrac{7\pi}{6}$.

   For $x>0$, we have $|x|=x$, so we obtain 

   $$
   f'(x)=\frac{1}{2}+\sin(x).
   $$

   Setting $f'(x)=0$ gives $\sin(x)=-\dfrac{1}{2}$, which means that $x=\dfrac{7\pi}{6}+k2\pi$ of $x=\dfrac{11\pi}{6}+k2\pi$ for some integer $k$. Of these values of $x$, we are only interested in those that lie in the interval $[-2\pi,2\pi]$ **and** have $x>0$, so this leaves us with $x=\dfrac{7\pi}{6}$ and $x=\dfrac{11\pi}{6}$. With that, we have found all critical points.

3. We evaluate the function on the point we found in the first two steps. This gives.

$$
 f\left(-\dfrac{11\pi}{6}\right)=\frac{11}{12}\pi-\frac{1}{2}\sqrt{3},\quad f\left(-\dfrac{7\pi}{6}\right)=\frac{7}{12}\pi+\frac{1}{2}\sqrt{3},\quad f(0)=-1
$$

$$
 f\left(\dfrac{7\pi}{6}\right)=\frac{7}{12}\pi+\frac{1}{2}\sqrt{3},\qquad f\left(\dfrac{11\pi}{6}\right)=\frac{11}{12}\pi-\frac{1}{2}\sqrt{3}.
$$

4. We evaluate the function on the boundary points to obtain

$$
 f(-2\pi)=\pi-1,\qquad f(2\pi)=\pi-1.
$$

5. The largest value that we found in steps 3. and 4. must be the global maximum value (since this value cannot be attained at any point that we did not check). This highest value is $\dfrac{1}{2}\sqrt{3}+\dfrac{7\pi}{12}$, which is attained at both $x=-\dfrac{7\pi}{6}$ and at $x=\dfrac{7\pi}{6}$. The lowest value is the global minimum value. This lowest value is $-1$, which is attained at $x=0$.

:::{figure} Images/Fig-MinMax-Globalextrema2.png
:name: Fig:MinMax:Globalextrema2

The graph of the function $f$ from {prf:ref}`Ex:MinMax:Globalextrema2` and its local and global extrema.
:::

:::{todo}
Convert {numref}`Fig:MinMax:Globalextrema2` to an applet Make sure to highlight all candidate points and make difference between local and global extrema clear.
:::
::::::