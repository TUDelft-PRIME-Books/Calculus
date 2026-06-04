(Section:Extrema1d)=

# Graphs and extreme values

(Subsec:Extrema1dIntro)=

## Introduction

Now that we know the derivatives of most standard functions, we have not really touched upon what should be the most important question: what can we actually do with derivatives? We have seen that we can use them to find tangent lines, but that is about it. For higher order derivatives we have not even seen *any* uses (yet). However, there is much more that derivatives can tell us. In fact, most qualitative behaviour of a function is captured in its derivatives. For instance, we will see that we can use the first derivative to determine whether a function is increasing or decreasing on an interval.

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

So how should we continue from here? In this section, we will see that a function is nondecreasing when the derivative is positive and nonincreasing when it is negative. So we evaluate the derivative of $A$ to obtain

$$
 \frac{dA}{dw}=200-2w.
$$

Then we see that $\frac{dA}{dw}>0$ when $w<100$, while $\frac{dA}{dw}<0$ when $w>100$. So if the width is less than $100$, we should increase the width since that gives a larger area. In addition, if the width is more than $100$, we should decrease the width since we then also obtain a larger area. This suggests that we obtain the largest area whenever $w=100$. In that case, we have $\ell=200-w=100$ as well. Hence, we obtain the largest area whenever the rectangle is a square.

In this section we will show that this idea is valid. We will look at how we can find the largest function values (called **maxima** of the function) and the lowest function value (called **minima** of the function). Maxima and minima are collectively called the **extrema** of a function. For this, we take two different points of view. First, we look at what happens locally. That is, we zoom in near an interesting point and do not care how the functions behaves far away from that point. Then, we look at what happens globally, so when we take the full domain of the function into account. In order to prove most of these results, we will need a very important theorem, called the **mean value theorem**, which we will also establish in this section.

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

We conclude that $f$ has three critical points: $-1$, $0$ and $1$. So how would we find out if $f$ has a local extremum in any of these points? Unfortunately, we have no way (yet) to rigorously determine this. Still, we can read at least plot the graph of the function and read off the behaviour of the function in these points. {numref}`Fig:MinMax:Critical` shows the graph of the function $f$. This graph suggests that $f$ has a local maximum at $-1$ and $1$ and that it has a local minimum at $0$. In {prf:ref}`Ex:MinMax:CriticalPart2` we will find this result analytically.

:::{figure} Images/Fig-MinMax-Critical.png
:name: Fig:MinMax:Critical

The graph of the function $f$ from {prf:ref}`Ex:MinMax:Critical`.
:::

:::{todo}
Turn {numref}`Fig:MinMax:Critical` into an applet.
:::



::::::

In {numref}`Subsec:FirstScndTest` we will establish two methods to help us classify critical points as either a local minimum, local maximum or none of these.

(Subsec:Extrema1dEVT)=

## Global extrema

Recall that local extrema only consider the behaviour of a function near a critical point. However, if a function has a local minimum at a critical point, it might still have function values that are even lower somewhere far away from the critical point, see for example the function shown in {numref}`Fig:MinMax:Critical`.

As such, it is also interesting to consider the highest and lowest values a function can attain without looking only locally, or in other words, to look globally. This leads us to the following definition.

::::::{prf:definition} 
:label: Def:MinMax:GlobExtr
Let $c$ be in the domain of a function $f$.

Then we say that $f$ has a **global maximum** at $c$, or that $f(c)$ is the **global maximum** value of $f$, if $f(c)\geq f(x)$ for all $x$ in the domain of $f$. 

Similarly, we say that $f$ has a **global minimum** at $c$, or that $f(c)$ is the **global minimum** value of $f$, if $f(c)\leq f(x)$ for all $x$ in the domain of $f$.

A **global extremum** or **global extreme value** is a global maximum or a global minimum.
::::::

Global maxima and minima are sometimes called **absolute** maxima and minima. We have opted for the term global maximum and global minimum, since the term absolute can cause confusion with the absolute value function.

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





[^FootnoteCIM]: If the function has infinitely many critical points, then this method may fail to work.

So how do we find the locations of the global maximum and global minimum values of a continuous function on a closed interval $[a,b]$?

If a global extremum is in the open interval $(a,b)$ then we can apply {prf:ref}`Cor:MinMax:Critical` to conclude that the global extremum is attained at a critical point. And if not, then, well, there are not an awful lot of options left, since the only points that we have not considered are the points $a$ and $b$. So this gives us a way to find all *candidate locations* for the global extreme values.

So how do we then determine which of these corresponds to the global maximum and which to the global minimum?

You might expect that we need to perform all sorts of tests, like the ones that will be discussed in {numref}`Subsec:FirstScndTest`, but that is not the case. Indeed, if I know that the global maximum occurs at one of, say, five points[^FootnoteCIM], then I can just evaluate the function at each of these five points. The largest value I obtain this way **must** be the global maximum value, as this value cannot be attained anywhere else. Similarly, the lowest value **must** be the global minimum value.

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









(Subsec:MVT)=

## Mean value theorem

Suppose you are running a marathon and let $f(t)$ describe the distance you travelled at time $t$. Then $f'(t)$ represents your velocity at time $t$. Say it takes you four and a half hours to finish the marathon. Then your average running speed is around $2.6$ meters per second. Likely, you are not running equally fast at each point in time, so for most values of $t$, $f'(t)$ will be unequal to $2.6$. The idea of the mean value theorem is that there must be at least one point in time (but possibly more) where your velocity is exactly equal to the average velocity. Intuitively this makes sense. If you were to run slower than $2.6$ meters per second all the time, or faster than $2.6$ meters per second all the time, your average velocity would be below or higher than $2.6$ meters per second respecitvely. So there must be points in time where you run slower than your average speed and points in time where you run faster than your average speed. Since your speed does not make sudden jumps (that is, your speed is continuous), it has to attain this average speed at some point in time.

With this idea in mind, let us formulate and prove the mean value theorem, which is also known as **Lagrange's mean value theorem**, named after the Italian mathematician and physicist [Joseph-Louis Lagrange (1736-1813)](https://en.wikipedia.org/wiki/Joseph-Louis_Lagrange). However, we will start with a special case of the mean value theorem, called **Rolle's theorem**, named after the French mathematician [Michel Rolle (1652-1719)](https://en.wikipedia.org/wiki/Michel_Rolle). This special case deals with functions $f$ defined on a closed interval $[a,b]$ with $f(a)=f(b)$.

::::::{prf:theorem} Rolle's theorem
:label: Thm:MinMax:Rolle
Let $f$ be a function that is continuous on a closed interval $[a,b]$ and differentiable on the open interval $(a,b)$. Suppose, in addition, that $f(a)=f(b)$. Then there exists a point $c$ in $(a,b)$ with $f'(c)=0.$

::::::

:::{admonition} Proof of {prf:ref}`Thm:MinMax:Rolle`
:class: tudproof, dropdown
First suppose that the function is constant on the interval $[a,b]$. Since the function is constant, we have $f'(c)=0$ for all $c$ in $(a,b)$.

Now suppose that the function is not constant on the interval $[a,b]$. By {prf:ref}`Thm:MinMax:EVT`, $f$ attains both a local maximum and a local minimum on the interval $[a,b]$. Since $f(a)=f(b)$ and $f$ is not constant, at least one of these two must occur at a point $c$ in the open interval $(a,b)$. Indeed, if they were to both occur at the edge values $a$ or $b$, then $f(a)=f(b)$ would both be the highest value and the lowest value of $f$ on $[a,b]$, which would mean that $f$ is constant on $[a,b]$. By {prf:ref}`Thm:MinMax:Fermat` we have that $f'(c)=0$, as desired.
:::

An illustration of Rolle's theorem is shown in {numref}`Fig:MinMax:Rolle`. Note that {prf:ref}`Thm:MinMax:Rolle` also includes the case that there are multiple points where the derivative is equal to $0$, for instance, for the function on the left in {numref}`Fig:MinMax:Rolle` any point will do, and for the right function there are two points where the derivative is equal to $0$.

:::{figure} Images/Fig-Graph1d-Rolle.png
---
width: 100%
name: Fig:MinMax:Rolle
class: dark-light
---
An illustration of Rolle's theorem.
:::

:::{todo}
Replace {numref}`Fig:MinMax:Rolle` with an applet.
:::

:::{note}
Rolle's theorem even applies when the derivative is not continuous (so when $f$ is differentiable, but not continuously differentiable.) Even then, the derivative can never avoid being $0$ at at least one point.
:::

The mean value theorem is in essence an extension of Rolle's theorem, and formalises what we discussed in the introduction of this subsection.

::::::{prf:theorem} The mean value theorem
:label: Thm:MinMax:MVT
Let $f$ be a function that is continuous on a closed interval $[a,b]$ and differentiable on the open interval $(a,b)$. Then there exists a point $c$ in $(a,b)$ with

$$
 f'(c)=\frac{f(b)-f(a)}{b-a}.
$$

::::::



:::{admonition} Proof of {prf:ref}`Thm:MinMax:MVT`
:class: tudproof, dropdown
We want to apply Rolle's theorem, so we need to construct some function $g$, related to $f$, that has $g(a)=g(b)$. In addition, it needs to be possible to lift the information on $g'$ back to to $f'$, so it is convenient if they differ by a constant. As such, we subtract from $f$ the linear function that goes through the points $(a,f(a))$ and $(b,f(b))$. This linear function is given by $L(x)=f(a)+\dfrac{f(b)-f(a)}{b-a}(x-a)$. Note that 

$$
 L(a)=f(a)+\dfrac{f(b)-f(a)}{b-a}(a-a)=f(a)
$$

and

$$
 L(b)=f(a)+\dfrac{f(b)-f(a)}{b-a}(b-a)=f(b),
$$

so the function $L$ indeed goes through the points $(a,f(a))$ and $(b,f(b))$.

Now consider the function

$$
 g(x)=f(x)-L(x)=f(x)-f(a)-\dfrac{f(b)-f(a)}{b-a}(x-a).
$$

This function satisfies $g(a)=f(a)-L(a)=0$ and $g(b)=f(b)-L(b)=0$.

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

The interpretation of this theorem works as follows: $\dfrac{f(b)-f(a)}{b-a}$ represents the **average slope** of the function on the interval $[a,b]$. The theorem states that there must be at least one point where the slope is equal to this average slope. Note that the mean value theorem does not tell you how to find the point. It only states that such a point must exist. An illustration of the theorem is shown in {numref}`Fig:MinMax:MVT`.

:::{figure} Images/Fig-Graph1d-MVT.png
---
width: 100%
name: Fig:MinMax:MVT
class: dark-light
---
An illustration of the mean value theorem. Note that in this case there are multiple points where the derivative is equal to $\dfrac{f(b)-f(a)}{b-a}$. The red line is the graph of the function $L(x)$ from the proof of {prf:ref}`Thm:MinMax:MVT`.
:::

:::{todo}
Replace {numref}`Fig:MinMax:MVT` with an applet.
:::

Let us return to the example from the start of {numref}`Subsec:MVT`. The function $f(t)$ satisfies $f(0)=0$ and $f(16200)=42195$ (since it takes you four and a half hours, which is $16200$ seconds, to finish the $42195$ meter marathon). Assuming that $f$ is differentiable, {prf:ref}`Thm:MinMax:MVT` tells us that there is a point in time $c$ in $(0,16200)$ with where the speed $f'(c)$ is given by

$$
 f'(c)=\frac{f(16200)-f(0)}{16200-0}=\frac{42195}{16200}\approx 2.6.
$$

So at this point in time $c$, the speed equals the average speed of $2.6$ meters per second

There is a more general version of the mean value theorem, called Cauchy's mean value theorem. This result is named after the French mathematician and engineer [Augustin-Louis Cauchy](https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy). This general version is usually a bit overkill when it comes to proving what the derivative says about a function. Still, we will need this general version when proving l'Hospital's rule in {numref}`Section:lHospital`.

::::::{prf:theorem} The Cauchy mean value theorem
:label: Thm:MinMax:MVTCauchy
Let $f$ and $g$ be functions that are continuous on a closed interval $[a,b]$ and differentiable on the open interval $(a,b)$. Then there exists a point $c$ in $(a,b)$ with

$$
 (f(b)-f(a))g'(c)=(g(b)-g(a))f'(c).
$$



::::::

:::{admonition} Proof of {prf:ref}`Thm:MinMax:MVTCauchy`
:class: tudproof, dropdown
The idea in this proof is similar to the one in the proof of {prf:ref}`Thm:MinMax:MVT`. Here, we define the function

$$
 h(x)=(g(b)-g(a))f(x)-(f(b)-f(a))g(x).
$$

This function is a linear combination of two functions that are continuous on $[a,b]$ and differentiable on $(a,b)$, so the new function $h$ has these properties as well. In addition, we see that $h(a)=h(b)$, since

\begin{align*}
 h(a) &= (g(b)-g(a))f(a)-(f(b)-f(a))g(a) \\
 &= g(b)f(a)-f(b)g(a) 
\end{align*}

and

\begin{align*}
 h(b) &= (g(b)-g(a))f(b)-(f(b)-f(a))g(b) \\
 &= g(b)f(a)-f(b)g(a) .
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
We obtain {prf:ref}`Thm:MinMax:MVT` back from {prf:ref}`Thm:MinMax:MVTCauchy` when choosing the function $g$ to be given by $g(x)=x$.
:::

:::{note}
Consider the setting of {prf:ref}`Thm:MinMax:MVTCauchy`. If $g(a)\neq g(b)$ and $g'(c)\neq 0$, the identity

$$
 (f(b)-f(a))g'(c)=(g(b)-g(a))f'(c).
$$

can be rewritten in the form

$$
 \frac{f'(c)}{g'(c)}=\frac{f(b)-f(a)}{g(b)-g(a)},
$$

and if $f(a)\neq f(b)$ and $f'(c)\neq 0$, it can be rewritten in the form

$$
 \frac{g'(c)}{f'(c)}=\frac{g(b)-g(a)}{f(b)-f(a)}.
 $$
:::

:::{figure} Images/Fig-Graph1d-CauchyMVT.png
---
width: 100%
name: Fig:MinMax:CauchyMVT
class: dark-light
---
An illustration of {prf:ref}`Thm:MinMax:MVTCauchy`. We see the curve with parametrisation $(g(x),f(x))$ for $a\leq x\leq b$. The slope of the vector from the start to the end point is $\frac{g(b)-g(a)}{f(b)-f(a)}$. The vector $\begin{pmatrix} g'(c)\\ f'(c)\end{pmatrix}$ is tangent to the curve at the point $c$ (it is the tangent vector, see {numref}`Subsec:Slopeparam`). The slope of this vector is $\frac{g'(c)}{f'(c)}$.
:::

:::{todo}
Replace {numref}`Fig:MinMax:MVT` with an applet.
:::


Let us see how the mean value theorem can be used in practice.

::::::{prf:example}
:label: EX:MinMax:MVT1
Consider the function $f(x)=x^3+3x^2+6x+3$ and suppose we want to find all (real) solutions of the equation $f(x)=0$ between $-1$ and $0$. We notice that $f(-1)=-1<0$, while $f(0)=3>0$, so by {prf:ref}`Cor:Continuity:IVT`, there is at least one $a$ between $-1$ and $0$ with $f(a)=0$. We will use the mean value theorem (or more specifically, Rolle's theorem) to show that this is the only solution. 

Indeed, suppose that there is another solution, say a number $b$ between $-1$ and $0$ with $f(b)=0$. Without loss of generality, we can assume that $a<b$. Then $f$ is continuous on the interval $[a,b]$ and differentiable on $(2,6)$ (since it is a polynomial). In addition, we have $f(a)=f(b)=0$. Then by {prf:ref}`Thm:MinMax:Rolle`, we can find some $c$ in the interval $(a,b)$ with $f'(c)=0$. However, we can evaluate the derivative of $f$ as

$$
 f'(x)=3x^2+6x+6.
$$

The equation $3x^2+6x+6=0$ does not have any real solutions. So our assumption that there would be another solution must be incorrect. Hence, there is exactly one solution between $-1$ and $0$. This is supported by the graph of the function, which is shown in {numref}`Fig:MinMax:MVT1`.


:::{figure} Images/Fig-Graphsderivatives-MVT1.png
:name: Fig:MinMax:MVT1

The graph of the function $f(x)=x^3+3x^2+6x+3$. Note that there is only one solution of the equation $f(x)=0$ between $-1$ and $0$.
:::

:::{todo}
Replace {numref}`Fig:MinMax:MVT1` with an applet.
:::

::::::

Some of the most important consequences of the mean value theorem are the following two results. These results form an essential part of finding antiderivatives, see {numref}`Sec:Integration:IndefiniteIntegrals`. Indeed, these results indicate that any two functions that have the same derivative must differ by a constant.

::::::{prf:corollary} 
:label: Cor:MinMax:Zeroderivative
Let $f$ be a differentiable function such that $f'(x)=0$ for all $x$ in some interval $I$. Then $f$ is constant on that interval.
::::::

:::{admonition} Proof of {prf:ref}`Cor:MinMax:Zeroderivative`
:class: tudproof
Suppose $f'(x)=0$ for all $x$ in $I$, but $f$ is not constant. Then we can find two points $p<q$ in the interval $I$ with $f(p)\neq f(q)$. Then $f$ is continuous on the interval $[p,q]$ and differentiable on the interval $(p,q)$, so by {prf:ref}`Thm:MinMax:MVT` we can find $c$ in $(p,q)$ with

$$
 f'(c)=\frac{f(q)-f(p)}{q-p}.
$$

Since $f(p)\neq f(q)$ we have $f'(c)=\dfrac{f(q)-f(p)}{q-p}\neq 0$. However, this contradicts the assumption that $f'(x)=0$ for all $x$ in $I$. Hence, $f$ must be constant on this interval.
:::

::::::{prf:corollary} 
:label: Cor:MinMax:Samederivative
Let $f$ and $g$ be differentiable functions such that $f'(x)=g'(x)$ for all $x$ in some interval $I$. Then $f=g+C$ for some constant $C$ on this interval.
::::::

:::{admonition} Proof of {prf:ref}`Cor:MinMax:Samederivative`
:class: tudproof
Consider the function $h=f-g$. Then $h$ is differentiable and for $x\in I$ we have $h'(x)=f'(x)-g'(x)=0$, since $f'(x)=g'(x)$. Hence, the function $h$ is constant by {prf:ref}`Cor:MinMax:Zeroderivative`, say $h=C$. Then $f=g+C$ for this same constant $C$.
:::

The mean value theorem can also be used to translate any restriction on the possible values of the derivative into a limitation on the values of the function itself.



::::::{prf:example}
:label: EX:MinMax:MVT2
Suppose, that for some function $f$ we know that

$$
f(2)=5
$$

and that

$$
3\leq f'(x)\leq 7\quad\text{for}\quad2\leq x\leq 6.
$$

What are the smallest and largest possible values of $f(6)$?

Let us first determine the smallest possible value. Since the slope of the function is always at least $3$, intuitively it makes sense that we obtain the lowest value of $f(6)$ whenever $f'(x)=3$ for **all** $2\leq x\leq 6$.

So consider a function $\tilde{f}$ with $\tilde{f}(2)=f(2)=5$ and $\tilde{f}'(x)=3$ for all $2\leq x\leq 6$. Our intuition suggests that $f(6)\geq\tilde{f}(6)$, since the slope of $f$ is always at least as large as the slope of $\tilde{f}$.

The function $\tilde{f}$ has the same derivative as $g(x)=3x$ on the interval $(2,6)$. So by {prf:ref}`Cor:MinMax:Samederivative` we find that $\tilde{f}(x)=g(x)+C$ for some constant $C$. Since $5=\tilde{f}(2)=g(2)+C=6+C$, we must have $C=-1$, so then $\tilde{f}(x)=3x-1$ on this interval. In that case we would have $\tilde{f}(6)=3\cdot 6-1=17$.

So, intuitively at least, we have shown that $f(6)$ must be at least $\tilde{f}(6)=17$ and we know for certain that there is at least one possible formula for $f$ for which the value of $f(6)$ is precisely $17$ (and this is the function $\tilde{f}$). Can we make this a bit more rigorous? Of course we can! By {prf:ref}`Thm:MinMax:MVT`, there is a point $c$ in the interval $(2,6)$ with

$$
 f'(c)=\frac{f(6)-f(2)}{6-2}=\frac{f(6)-5}{4}.
$$

Solving this equation for $f(6)$ gives

$$
 f(6)=4f'(c)+5.
$$

Since $c$ is in the interval $(2,6)$ we know that $f'(c)\geq 3$, so we find that

$$
 f(6)=4f'(c)+5\geq 4\cdot 3+5=17.
$$

So we conclude that, indeed, we must have $f(6)\geq 17$.

Similarly, we can use $f'(c)\leq 7$ to show that

$$
 f(6)=4f'(c)+5\leq 4\cdot 7+5=33.
$$

This value of $f(6)=33$ is obtained when $f'(x)=7$ for all $x$ in the interval $(2,6)$, in which case we would have been dealing with the function $f(x)=7x-9$.

{numref}`Fig:MinMax:MVT2` shows the graph of the function $3x-1$, the graph of the function $7x-9$ and the graph of an example of a function that satisfies the assumptions on $f$. The graph of any function that satisfies the assumptions must lie in between these two graphs, so in particular, the value of $f(6)$ must be in between $17$ and $33$.

:::{figure} Images/Fig-Graphsderivatives-MVT2.png
:name: Fig:MinMax:MVT2

The graph of the function $3x-1$ , the graph of the function $7x-9$ and the graph of an example of a function that satisfies the assumptions on $f$.
:::

:::{todo}
Replace {numref}`Fig:MinMax:MVT2` with an applet. The function that satisfies the assumptions on $f$ is given by

$$
f(x)=\frac{1}{32} (-2 x^3 + 24 x^2 - 72 x + 64 + (x^2 + 4 x + 68) x)
$$
:::

::::::

::::::{prf:example}
:label: EX:MinMax:MVTnmbre
We can even use the mean value theorem to find estimates on (un)known constants. For instance, consider the function $f(x)=e^x$. We apply {prf:ref}`Thm:MinMax:MVT` on the interval $[0,1]$. This gives that there is $c$ in $(0,1)$ with

$$
 e^c=f'(c)=\frac{f(1)-f(0)}{1-0}=\frac{e-1}{1}=e-1.
$$

Now (assuming that we already know that $e>1$), {prf:ref}`Thm:RealNumbers:ExpCalcReal` tells us, since $0<c<1$, that

$$
 e^0=1<e^c<e^1=e.
$$

Since $e^c=e-1$, we then obtain that

$$
 1<e-1<e,
$$

which gives

$$
 2<e<e+1.
$$

In particular, we have proven that $e>2$. If we were to choose another interval on which we can apply the mean value theorem, we would obtain different estimates for the number $e$.
::::::


{prf:ref}`Cor:MinMax:Samederivative` can also be used to establish certain trigonometric identities.

::::::{prf:example}
:label: EX:MinMax:MVTarctan
Let us try to simplify the expression $\arctan(x)+\arctan\left(\frac{1}{x}\right)$ for $x\neq 0$. We have not found the derivative of the arctangent yet, but as a sneak peek, we will use that $\dfrac{d}{dx}\left[\arctan(x)\right]=\dfrac{1}{1+x^2}$ (this identity will be established in {prf:ref}`Thm:Diffinverse:Standard4`). Using the chain rule, we find that

$$
 \dfrac{d}{dx}\left[\arctan(x)+\arctan\left(\frac{1}{x}\right)\right]=\frac{1}{1+x^2}+\frac{1}{1+\left(\frac{1}{x}\right)^2}\frac{-1}{x^2}=\frac{1}{1+x^2}-\frac{1}{x^2+1}=0.
$$

By {prf:ref}`Cor:MinMax:Samederivative`, we obtain that the function $f(x)=\arctan(x)+\arctan\left(\frac{1}{x}\right)$ must be constant on any interval that does not contain $0$. Now in order to establish which constant this is, we use a point in which we can find the exact value of the function. For instance, if $x>0$ we let $[a,b]$ be any interval that contains $1$ and $x$ and does not contain $0$. Then $f$ is constant on this interval and we find

$$
 f(x)=f(1)=\arctan(1)+\arctan\left(\frac{1}{1}\right)=\frac{\pi}{4}+\frac{\pi}{4}=\frac{\pi}{2}.
$$

Hence, we have $\arctan(x)+\arctan\left(\frac{1}{x}\right)=\frac{\pi}{2}$ for $x>0$. However, it is incorrect to conclude that this must be the case for $x<0$ as well. Indeed, for $x<0$ it is impossible to find an interval $[a,b]$ that contains $x$ and $1$, but does not contain $0$. We absolutely need to avoid the point $0$, since the function $f$ is undefined there. Fortunately, we can use another point so that we can avoid $0$. Indeed, we can let $[a,b]$ be an interval that contains $-1$ and $x$ and does not contain $0$. Then $f$ is constant on this interval and we find

$$
 f(x)=f(-1)=\arctan(-1)+\arctan\left(\frac{1}{-1}\right)=-\frac{\pi}{4}-\frac{\pi}{4}=-\frac{\pi}{2}.
$$

We conclude that 

$$
 \arctan(x)+\arctan\left(\frac{1}{x}\right)=\left\{\begin{array}{l}-\dfrac{\pi}{2},\qquad&\mathrm{if}\ x<0,\\[0.2cm]
 \dfrac{\pi}{2},\qquad&\mathrm{if}\ x>0.\end{array}\right.
 
$$

{numref}`Fig:MinMax:MVT3` shows the graph of this special function.

:::{figure} Images/Fig-Graphsderivatives-MVT3.png
:name: Fig:MinMax:MVT3

The graph of the function $f(x)=\arctan(x)+\arctan\left(\frac{1}{x}\right)$.
:::

:::{todo}
Replace {numref}`Fig:MinMax:MVT3` with an applet. Make sure no vertical line element is shown.
:::

::::::

(Subsec:MinMax:Incrdecr)=

## Increasing and decreasing functions

One of the main features of derivatives is that they can be used to establish on which intervals a function is nondecreasing and on which intervals it is nonincreasing. We defined what it means for a function to be nondecreasing or nonincreasing on an interval in {numref}`Subsec:PropertiesFunctionsIncreasingDecreasing`, but we saw there that without derivatives it is very hard to establish these properties. So how can we use the derivative? Intuitively speaking, if a function is nondecreasing on an interval, then at any point on this interval the function values must grow. So if we consider the tangent line at such a point, we would expect a line with a nonnegative slope. Similarly, we would expect a tangent line with a nonpositive slope on an interval where the function is nonincreasing. We can make this precise in the following way.


::::::{prf:theorem} 
:label: Thm:MinMax:Increasingdecreasing
Let $f$ be a differentiable function.

- $f$ is nondecreasing on an interval precisely when $f'(x)\geq 0$ on that interval.
- $f$ is nonincreasing on an interval precisely when $f'(x)\leq 0$ on that interval.
- If $f'(x)> 0$ on an interval, then $f$ is strictly increasing on that interval.
- If $f'(x)< 0$ on an interval, then $f$ is strictly decreasing on that interval.

::::::

:::{admonition} Proof of {prf:ref}`Thm:MinMax:Increasingdecreasing`
:class: tudproof, dropdown
Suppose that $f'(x)\geq 0$ on an interval and let $a<b$ be any two points in that interval. Then by {prf:ref}`Thm:MinMax:MVT`, we can find $c$ in $(a,b)$ with 

$$
 f'(c)=\frac{f(b)-f(a)}{b-a}.
$$

By assumption, we have $f'(c)\geq 0$, so we find that $\dfrac{f(b)-f(a)}{b-a}\geq 0$. Since $a<b$, this can only happen if $f(a)\leq f(b)$. So we find that $f$ is nondecreasing on this interval.

Now suppose that $f$ is nondecreasing on an interval. Consider any point $x$ in that interval. Then for any $h>0$ for which $x+h$ is in the interval we have $f(x+h)\geq f(x)$. As such, we must have

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
Notice that the two first statements in {prf:ref}`Thm:MinMax:Increasingdecreasing` are equivalences ("precisely when" statements), whereas the latter two statements are implications ("if then" statements). Indeed, if $f$ is strictly increasing on an interval, we cannot conclude that $f'(x)>0$ on this interval.

For instance, consider the function $f(x)=x^3$. Then $f'(x)=3x^2$, which is $0$ at $x=0$. Still, this function is strictly increasing on $\mathbb{R}$, since for any $a<b$ we have $a^3<b^3$.
:::

:::{todo}
Make a poll(???) where student needs to figure out where to proof breaks down if we try to prove the other implication.
:::

::::::{prf:example} 
:label: Ex:MinMax:Increasingdecreasing1
Consider the function $f(x)=-2x^3-3x^2+12x+3$ and suppose we want to know on which intervals the function is nondecreasing and on which intervals it is nonincreasing. For this, we evaluate the derivative, which is given by

$$
 f'(x)=-6x^2-6x+12.
$$

In order to establish when we have $f'(x)>0$ and when we have $f'(x)<0$ we first solve $f'(x)=0$, i.e. $-6x^2-6x+12=0$. This is a quadratic equation with solutions $x=1$ and $x=-2$. Since the coefficient of $x^2$ is negative, the graph of $f'$ is a parabola opening downwards. As such, we find that $f'(x)<0$ for $x<-2$ and for $x>1$, while $f'(x)>0$ for $-2<x<1$. We conclude that $f$ is strictly decreasing on the intervals $(-\infty,-2)$ and $(1,\infty)$, while it is strictly increasing on the interval $(-2,1)$. This can also be seen in the graph of the function.

:::{figure} Images/Fig-Graphsderivatives-Increasingdecreasing1.png
:name: Fig:MinMax:Increasingdecreasing1

The graph of the function $f(x)=-2x^3-3x^2+12x+3$.
:::

:::{todo}
Replace {numref}`Fig:MinMax:Increasingdecreasing1` with an applet.
:::

::::::

[^FootnoteSinh]: We did already prove that the hyperbolic sine was strictly increasing by other means, though we could also show it (quicker) using the derivative.

We postponed a small piece of the proof of {prf:ref}`Thm:PropertiesFunctions:HyperbolicProperties`, since it is very convenient to use derivatives to show whether a given function is increasing or decreasing. So let us finish the proof here.[^FootnoteSinh]

:::{admonition} Remainder of proof of {prf:ref}`Thm:PropertiesFunctions:HyperbolicProperties`
:class: tudproof, dropdown
If $f(x)=\cosh(x)$, then we have $f'(x)=\sinh(x)$. Since $f'(x)<0$ when $x<0$, the hyperbolic cosine must be strictly decreasing on $(-\infty,0)$. Similarly, since $f'(x)>0$ when $x>0$, the hyperbolic cosine is strictly increasing on $(0,\infty)$.

If $h(x)=\tanh(x)$, then we have $h'(x)=\dfrac{1}{\cosh(x)^2}$. We see that $h'(x)>0$ for all $x$, so the hyperbolic tangent is strictly increasing on $\mathbb{R}$.
:::

(Subsec:FirstScndTest)=

## First and second derivative test

::::::{prf:example} ({prf:ref}`Ex:MinMax:Critical` continued)
:label: Ex:MinMax:CriticalPart2
We again consider the function $f(x)=2|x|-x^2$. Previously, we obtained that $f$ has three critical points: $-1$, $0$ and $1$. So how would we find out if $f$ has a local extremum in any of these points? One way to do this, is to note that $f'(x)>0$ for $x<-1$, while $f'(x)<0$ for $-1<x<0$. By {prf:ref}`Thm:MinMax:Increasingdecreasing`, this means that the function strictly increases on the interval $(-\infty,-1)$, while it strictly decreases on the interval $(-1,0)$. Since $f$ is continuous in $-1$, this can only happen if $f(-1)\geq f(x)$ for all $x$ in $(-\infty,0)$. So $f$ has a local maximum in $-1$. 

Similarly, we find that $f'(x)>0$ for $0<x<1$ and $f'(x)<0$ for $x>1$. This means that $f$ is strictly increasing on the interval $(0,1)$ and strictly decreasing on $(1,\infty)$. Using a similar reasoning, this means that $f$ has a local minimum in $0$ and a local maximum in $1$.


:::{fetch} {numref}`Fig:MinMax:Critical`
:::

::::::

The reasoning we used in {prf:ref}`Ex:MinMax:CriticalPart2` to determine whether the critical points were local maxima, local minima or neither of these can be applied in general. This result is known as the first derivative test (in contrast to the second derivative test that we will discuss later).

::::::{prf:theorem} First derivative test 
:label: Thm:MinMax:Firstdertest
Let $c$ be a point in the domain of a continuous function $f$.

- If $f'$ changes from negative to positive at $c$, i.e. $f'(x)\leq 0$ for $x<c$ near $c$ and $f'(x)\geq 0$ for $x>c$ near $c$, then $f(c)$ is a local minimum of $f$.
- If $f'$ changes from positive to negative at $c$, i.e. $f'(x)\geq 0$ for $x<c$ near $c$ and $f'(x)\leq 0$ for $x>c$ near $c$, then $f(c)$ is a local maximum of $f$.
- If $f'(x)>0$ for all $x$ near $c$ (excluding $x=c$) or if $f'(x)<0$ for all $x$ near $c$ (excluding $x=c$) then $f(c)$ is neither a local minimum nor a local maximum of $f$.
::::::

Before we turn to the proof of {prf:ref}`Thm:MinMax:Firstdertest`, we illustrate the different cases of this theorem in {numref}`Fig:MinMax:Firstdiv`.

:::{figure} Images/Fig-MinMax-Firstdiv.png
:name: Fig:MinMax:Firstdiv
:class: dark-light

Illustration of {prf:ref}`Thm:MinMax:Firstdertest`.
(a) $f'$ changes from negative to positive at $c$; (b) $f'$ changes from positive to negative at $c$; (c) $f'(x)>0$ for all $x\neq c$; $f'(x)<0$ for all $x\neq c$.
:::

:::{todo}
Turn {numref}`Fig:MinMax:Firstdiv` into an applet.
:::

{numref}`Fig:MinMax:Firstdiv`(a) clearly shows a local minimum at $x=c$. If you drag the point along the graph, you can see that the slope of the tangent line changes from negative to positive at $x=c$. Similarly, {numref}`Fig:MinMax:Firstdiv`(b) clearly shows a local maximum at $c$, and the slope of the tangent line changes from positive to negative at $c$. Finally, {numref}`Fig:MinMax:Firstdiv`(c) and (d) show graphs that neither have a local minimum nor a local maximum, and the slope of the tangent line is either positive or negative on both sides of $c$. These cases illustrate the different cases of {prf:ref}`Thm:MinMax:Firstdertest`.

Now you can read the proof of {prf:ref}`Thm:MinMax:Firstdertest`.

:::{admonition} Proof of {prf:ref}`Thm:MinMax:Firstdertest`
:class: tudproof, dropdown
Let $I=(a,b)$ be an open interval that contains $c$ and suppose $f'(x)\leq 0$ for $x$ in $I$ with $x<c$ and $f'(x)\geq 0$ for $x$ in $I$ with $x>c$. We will show that $f(c)$ is a local minimum of $f$. For this, we first show that $f$ is nonincreasing on $(a,c]$ (so including at the point $c$). On account of {prf:ref}`Thm:MinMax:Increasingdecreasing`, the function $f$ is nonincreasing on $(a,c)$. We argue by contradiction and assume that we can find $d$ in $(a,c)$ with $f(d)<f(c)$. Since $f$ is nonincreasing on $[d,c)$, we must have

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

Now we show that $f$ is nondecreasing on $[c,b)$. {prf:ref}`Thm:MinMax:Increasingdecreasing` gives that the function $f$ is nondecreasing on $(c,b)$. We again argue by contradiction and assume that we can find $d$ in $(c,b)$ with $f(d)<f(c)$. Then $f$ is nondecreasing on $(c,d)$, so we must have

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

Now suppose that $f'(x)>0$ for all $x$ in $I$ with $x\neq c$. By the first part of the proof $f$ is nondecreasing on $(a,c]$, so we have 

$$
 f(x)\leq f(c)
$$

for all $x$ in $I$ with $x\leq c$. Note that it is not possible that there is $d$ in $I$ with $d<c$ and $f(d)=f(c)$, since on account of {prf:ref}`Thm:MinMax:Increasingdecreasing` $f$ must be strictly increasing on the interval $[d,c)$. So we find that

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
A sign chart shows on which intervals the derivative is positive and on which it is negative. Replace the words increasing and decreasing by strictly increasing and strictly decreasing.
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


## Grasple exercises


### Exercises on extreme values

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8581ed8d-aea8-4812-98e5-c5ea5ec84754?id=68844
:label: Grasple:68844
:dropdown:
:description: Definition of global maximum and minimum.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f02248ee-772b-46a1-968f-4be81b233567?id=68839
:label: Grasple:68839
:dropdown:
:description: Reading off maxima and minima from a graph.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/93ea68d6-70a2-4f74-a6ae-9a05152ebd56?id=68847
:label: Grasple:68847
:dropdown:
:description: Reading off maxima and minima from a graph.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d95a1a3b-a338-424a-a640-b56b77bd4961?id=68854
:label: Grasple:68854
:dropdown:
:description: Reading off maxima and minima from a graph.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6625b3f4-3d55-438d-8f5d-6dcefd36897f?id=68869
:label: Grasple:68869
:dropdown:
:description: Reading off maxima and minima from a graph.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e616f859-f2fc-49b0-ba3d-33f16a888e71?id=79423
:label: Grasple:79423
:dropdown:
:description: Finding the global maximum and minimum of a function on a closed interval.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/dc4f4ad0-1cbf-49c8-8067-be3034db2d23?id=71070
:label: Grasple:71070
:dropdown:
:description: A continuous function of which only some function values are given.
::::


### Exercises on the behaviour of a function and the mean value theorem

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/173b11b1-47d4-4393-ab54-75baa7ceefa5?id=63044
:label: Grasple:63044
:dropdown:
:description: Range of two functions.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/245bc0cf-71e6-4915-96c4-c0283f3f78ae?id=79428
:label: Grasple:79428
:dropdown:
:description: Checking where the function is strictly increasing.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2d5402dd-d41d-4967-9f26-87732af8cc5a?id=70266
:label: Grasple:70266
:dropdown:
:description: Recapping and checking the mean value theorem.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d936e89d-928f-4cc0-8003-2e0e35550e30?id=68988
:label: Grasple:68988
:dropdown:
:description: Recapping and checking the mean value theorem.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0e0b0238-ce28-4de6-9b7d-a72a458d5c37?id=69154
:label: Grasple:69154
:dropdown:
:description: Checking the mean value theorem.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7580f32e-c79d-4f28-afff-b9efa2842f98?id=68968
:label: Grasple:68968
:dropdown:
:description: Checking the mean value theorem.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bb00e894-9d17-47e0-ad0d-e5eaea15f32b?id=68960
:label: Grasple:68960
:dropdown:
:description: Finding an interval in which function values lie.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/060678c6-f920-42ee-9262-489bea916269?id=79421
:label: Grasple:79421
:dropdown:
:description: Application: when does total charge increase strictly and where is its maximal value?

::::