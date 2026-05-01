(Section:Continuity)=

# Continuity

## Introduction

Almost all functions we have encountered so far have the useful property that it is possible to sketch their graph without lifting your pen, except possibly for skipping over a vertical asymptote. Indeed, polynomials, powers of $x$, rational functions, (inverse) trigonometric functions, exponential functions and logarithms have this property. A function with this property is called **continuous**. Stated differently, a function is continuous whenever small changes in the input give rise to small changes in the output values. 

In science and engineering, most variables depend on each other in a continuous way. However, that does not always need to be the case. Consider, for instance, an electrical circuit, shown in {numref}`Fig:Continuity-Circuit` where a DC voltage source is connected to a resistor and a capacitor. Initially, the voltage source is turned off, but at $t=0$, we turn on the voltage source. Instantly, the current through the capacitor will jump from $0$ to a non-zero value, so a small change in time will give rise to a large change in current. As such, the current as a function of time is not continuous at the moment in time the voltage source is turned on (it is continuous at other points in time).

```{figure} Images/Fig-Continuity-Circuit.png
---
class: dark-light
name: Fig:Continuity-Circuit

placement: caption
---

The circuit described above with a resistor with resistance $R$ and a capacitor with capacitance $C$, where a voltage source of size $V_s$ is turned on at $t=0$. The resulting current $i(t)$ across the capacitor is not continuous at $t=0$.
```

:::{todo}
Make an applet of this figure. 
Hierbij ook nog een schets van de current i(t) (0 voor $t<0$, daarna van de vorm $\frac{V_s}{R}exp(-t)$, maar geef maar geen maatvoering op de assen)
:::

(Subsec:ContProp)=

## Definition and properties



::::::{prf:definition} Continuity
:label: Def:Continuity:ContinuityLimit

Let $f$ be a function and $a$ a point in the domain of $f$. Then we say that $f$ is **continuous** at $a$ whenever for every $\varepsilon>0$ there exists a $\delta>0$ such that for every $x$ in the domain of $f$ with $0<|x-a|<\delta$ we have $|f(x)-f(a)|<\varepsilon$. If $f$ is not continuous at $a$, we say that it is **discontinuous** at $a$.

If a function $f$ is continuous at each points in each point in its domain, we say that $f$ is **continuous**. 
::::::

In most situations, continuity of a function can conveniently be expressed in terms of limits.

::::::{prf:theorem} 
:label: Theorem:Continuity:EpsilonDelta
Suppose that  the domain of $f$ contains an open interval $(b,c)$ and let $a$ in $(b,c)$. Then $f$ is continuous at $a$ precisely when $\lim\limits_{x\rightarrow a}f(x)=f(a)$. 
::::::

:::{admonition} Proof of {prf:ref}`Theorem:Continuity:Composition`
:class: tudproof, dropdown
This follows directly from the precise definition of a limit ({prf:ref}`Def:LimitAtPoint:Precisedef`).
:::

:::{note}
It is clearly the easiest way to think about continuity in terms of limits (epsilons and deltas are never easy to think about). However, if we were to only use the definition in terms of the limit, we would run into a few technical issues. For instance, if $f$ is a function of which the domain is a closed interval $[a,b]$, then $\lim\limits_{x\rightarrow a}f(x)$ and $\lim\limits_{x\rightarrow b}f(x)$ do not exist as the left limit at $a$ and the right limit at $b$ do not exist. If we were to only define continuity in terms of limits, this function could never be continuous at $a$ or $b$, which is not something we want. As such, we have to define continuity in terms of epsilons and deltas, but it is advisable to use limits whenever we are not looking at the boundary of the domain.
::::::


You might be tempted to think that this definition means that a function $f$ is continuous at a point $a$, whenever $\lim\limits_{x\rightarrow a}f(x)$ exists. However, this is not the case. In the definition, it is stated explicitly that this limit should not only exist, but it should also be equal to the function value $f(a)$. For instance, for the function $f$ defined in {prf:ref}`Ex:LimitAtPoint:LimitLeftRightPiecewise`, the limit $\lim\limits_{x\rightarrow 2}f(x)$ exists, but it is unequal to $f(2)$. Hence, this function $f$ is not continuous at the point $2$.


{prf:ref}`Theorem:LimitAtPoint:Directsub` essentially states that most functions that we know (polynomials, rational functions, powers of $x$, (inverse) trigonometric functions, exponential functions and logarithms) are continuous on their domains. However, we never proved this theorem (we will do so in this section), so we cannot make use of this yet. Still, it does give us an idea which functions are going to be continuous. 

::::::{prf:example}
:label: Ex:Continuity:Visual
Consider the function $f$ of which the graph is shown below.

::::{figure} Images/Fig-Continuity-Visual.png
:name: Fig:Continuity:Visual
:class: dark-light

Some function $f$.

::::

::::{todo}
Make this figure into an applet. The part for $x\geq 1$, this should be $3-2(x-1)$. Also make a hold at $x=2$.

Do not mention in the final applet/image which function is shown here.
::::

Can we read off from the graph at which points the function is continuous? Well, for almost all points $a$ there is no problem: the limit $\lim\limits_{x\rightarrow a}f(x)$ always exists and is equal to $f(a)$. Only the points $a=-2$, $a=-1$, $a=1$ and $a=2$ are potentially problematic. 

At $x=-2$ the left and right limits exist, but are unequal, so the limit $\lim\limits_{x\rightarrow -2}f(x)$ does not exist, which means that it can never be equal to $f(-2)$. As such, $f$ is not continuous at $x=-2$.

At $x=-1$, the limit exists, as the left and right limits exist and are equal. However, we read off that $\lim\limits_{x\rightarrow -1}f(x)=1$, while $f(1)=-3$. So at this point, the limit exists, but is unequal to the function value. As such, $f$ is not continuous at $-1$.

At $x=1$ the left and right limit are both equal to $1$ and we see that $f(1)=1$ as well. So the limit exists, and is equal to the function value. Hence, $f$ is continuous at $x=1$. You might notice that the function has a sharp edge, but this does not influence the continuity (it does, on the other hand, influence the differentiability of the function, see {numref}`Section:Differentiability`).

Finally, at $x=2$ the left and right limit exist and are equal, so the limit $\lim\limits_{x\rightarrow 2}f(x)$ exists. However, the point $x=2$ is not in the domain of $f$, so $f$ is neither continuous nor discontinuous at that point. It is simply undefined there.

We conclude that $f$ is continuous at all points except $-2$ and $-1$.

::::::






::::::{prf:example} 
:label: Ex:Continuity:Firstexample

Consider the function $f(x)=x^2$. In {prf:ref}`Ex:LimitAtPoint:Formaldefexists` we showed that $\lim\limits_{x\rightarrow 2}x^2=4$. Since $f(2)=2^2=4$, this means that $\lim\limits_{x\rightarrow 2}x^2=f(2)$. So this function is continuous at $2$. In fact, it is continuous everywhere, as we will show later.
::::::

Before showing that many standard functions are continuous, it pays off to first show that we can combine continuous functions in several ways to obtain new continuous functions. Since we already know several computation rules for limits, and continuity is defined in terms of limits, we can directly lift these results to obtain computation rules for continuity.

::::::{prf:theorem} Basic rules of calculation for continuity
:label: Theorem:Continuity:Basiccomputationrules
Consider two functions $f$ and $g$ and let $a$ be a point that is both in the domain of $f$ and in the domain of $g$. Also let $c$ be a real number. Suppose that both $f$ and $g$ are continuous at $a$. Then the following functions are also continuous at $a$.

- $cf$
- $f+g$
- $fg$
- $\frac{f}{g}$, provided $g(a)\neq 0$.

::::::

:::{admonition} Proof of {prf:ref}`Theorem:Continuity:Basiccomputationrules`
:class: tudproof, dropdown

These statements follow directly from {prf:ref}`Theorem:LimitAtPoint:Basiccomputationrules` in case the domain of the function under consideration contains an open intervals $(b,c)$ with $a\in(b,c)$. Otherwise the proof of {prf:ref}`Theorem:LimitAtPoint:Basiccomputationrules` can be repeated where each of occurence of "for each $x$ with" should be replaced by "for each $x$ in the domain of the function under consideration with".
:::

In addition to the rules above, the composition of two continuous functions is again continuous, as can be seen from the following results.

::::::{prf:theorem} Composition of continuous functions
:label: Theorem:Continuity:Composition
Consider two functions $f$ and $g$. Suppose that $g$ is continuous at $a$ and $f$ is continuous at $g(a)$. Then the composite function $f\circ g$ is continuous at $a$.

::::::

:::{admonition} Proof of {prf:ref}`Theorem:Continuity:Composition`
:class: tudproof, dropdown

[^FootnoteEpsDelta]: So $\delta_1$ takes the role here that $\varepsilon$ usually takes.

Let $\varepsilon>0$ be given. Since $f$ is continuous at $g(a)$, we can pick $\delta_1>0$ in such a way that for each $x$ in the domain of $f$ with $0<|x-g(a)|<\delta_1$ we have $|f(x)-f(g(a))|<\varepsilon$. Since $g$ is continuous at $a$ and $\delta_1>0$, we can find $\delta_2>0$ in such a way that for each $x$ in the domain of $g$ with $0<|x-a|<\delta_2$ we have $|g(x)-g(a)|<\delta_1$[^FootnoteEpsDelta]. Consider any $x$ in the domain of $f\circ g$ with $0<|x-a|<\delta_2$. Then $x$ is also in the domain of $g$ and it satisfies $0<|x-a|<\delta_2$, so we must have $|g(x)-g(a)|<\delta_1$. As such, $g(x)$ is an element of the domain of $f$ with $0<|g(x)-g(a)|<\delta_1$, which means that we must have $|f(g(x))-f(g(a))|<\varepsilon$. This precisely means that $f\circ g$ is continuous at $a$.
:::

::::::{warning} 
:name: Warning:Continuity:Oppositecomposition

The reverse of the statement in {prf:ref}`Theorem:Continuity:Composition` is not true. That is, there are functions $f$ and $g$ for which there is a point $a$, such that either $f$ is discontinuous at $g(a)$ or $g$ is discontinuous at $a$ (or both), but $f\circ g$ is continuous at $a$. For instance, if $f=0$, then $f\circ g=0$ as well (independently of what $g$ is), which is a continuous function even if $g$ is not continuous everywhere.
::::::

We will not show the continuity of standard functions yet, since for several of these we need the upcoming intermediate value theorem. For the purpose of having at least some examples, we will show here that polynomial functions are continuous.

::::::{prf:theorem} Continuity of polynomial functions
:label: Theorem:Continuity:ContPoly
Let $f(x)=a_nx^n+...+a_1x+a_0$ be a polynomial function. Then $f$ is continuous on its maximal domain $\mathbb{R}$.

::::::

:::{admonition} Proof of {prf:ref}`Theorem:Continuity:ContPoly`
:class: tudproof, dropdown
We will first show that the functions $g(x)=1$ and $h(x)=x$ are continuous. Then we will use the previous results to establish the continuity of the polynomial function $f(x)=a_nx^n+...+a_1x+a_0$.

Let $a$ in $\mathbb{R}$ and let $\varepsilon>0$ be given. We want to choose $\delta>0$ in such a way that for each $x$ with $0<|x-a|<\delta$ we have $|g(x)-g(a)|<\varepsilon$. Fortunately, for any $x$ we have $|g(x)-g(a)|=|1-1|=0<\varepsilon$. So we are free to choose $\delta$, independently of $\varepsilon$. So we choose $\delta=1$ and then we find that for each $x$ with $0<|x-a|<\delta$ we have $|g(x)-g(a)|<\varepsilon$. This means that $g$ is continuous at $a$. Since this holds for all $a$, $g$ is continuous on $\mathbb{R}$.

Now we want to choose $\delta>0$ in such a way that for each $x$ with $0<|x-a|<\delta$ we have $|h(x)-h(a)|<\varepsilon$. For any $x$ we have $|h(x)-h(a)|=|x-a|$. So we choose $\delta=\varepsilon$. Then we find that for each $x$ with $0<|x-a|<\delta$ we have 

$$
 |h(x)-h(a)|=|x-a|<\delta=\varepsilon.
$$

This means that $g$ is continuous at $a$. Since this holds for all $a$, $g$ is continuous on $\mathbb{R}$.

Now in order to establish the continuity of $f$, we note that for each $1\leq k\leq n$ the function $x\mapsto x^k=\underbrace{x\cdot x\cdot....\cdot x}_{k\,\mathrm{ times}}$ is the product of $k$ times the continuous function $h$. On account of {prf:ref}`Theorem:Continuity:Basiccomputationrules`, the function $x\mapsto x^k$ is continuous on $\mathbb{R}$. From the same theorem we find that the function $x\mapsto a_kx^k$ is continuous on $\mathbb{R}$. In addition, the function $x\mapsto a_0$ is a scalar mulitple of the continuous function $g$, so this function is continuous on $\mathbb{R}$ too. This means that $f$ is the sum of continuous functions, so by {prf:ref}`Theorem:Continuity:Basiccomputationrules` it must be continuous.
:::

::::::{prf:example} 
:label: Ex:Continuity:ContPoly
Consider the rational function $f(x)=\dfrac{x^2+1}{x^2-1}$. Then we have $f=\dfrac{g}{h}$ with $g(x)=x^2+1$ and $h(x)=x^2-1$. The functions $g$ and $h$ are polynomial functions, so they are continuous on $\mathbb{R}$ by {prf:ref}`Theorem:Continuity:ContPoly`. So by {prf:ref}`Theorem:Continuity:Basiccomputationrules` the function $f$ is continuous at each point $a$ with $h(a)\neq 0$. We see that $h(a)=0$ precisely when $a=1$ or $a=-1$. So $f$ is continuous on its maximal domain, which is the set of all $a$ in $\mathbb{R}$ except $a=1$ and $a=-1$. At these two points, $f$ is undefined, so it neither continuous nor discontinuous.

:::{todo}
Make an applet with the graph of $f$.
:::

::::::

(Subsec:ContIVT)=

## Intermediate value theorem

Recall that we, informally, stated that the graph a continuous function can be drawn without lifting your pen. Specifically, this means that when a continuous function changes from one function value to another, it does not skip over any intermediate values. We make this idea more precise in the following theorem.

::::::{prf:theorem} Intermediate Value Theorem
:label: Theorem:Continuity:IVT

Suppose that $f$ is continuous on the closed interval $[a,b]$. Then for any $d$ in between $f(a)$ and $f(b)$ there exists a number $a\leq c\leq b$ with $f(c)=d$, i.e. $f$ takes on all values in between $f(a)$ and $f(b)$.
::::::

:::{admonition} Proof of {prf:ref}`Theorem:Continuity:IVT`
:class: tudproof, dropdown

The proof is a bit beyond the scope of this book as it uses the completeness of the real numbers, but we include it for completeness (of the book, that is). Feel free to skip the proof.

We assume that $f(a)<f(b)$ (the case where $f(b)<f(a)$ is very similar, so we will omit it). Consider any $d$ with $f(a)<d<f(b)$. Let $S$ be the set of all $x$ in $[a,b]$ that have $f(x)<d$. Then the set $S$ is non-empty, since $a$ is in this set (as $f(a)<d$). Moreover, the set $S$ is bounded, as it is contained in the interval $[a,b]$. As such, the set $S$ has a *supremum* $c$, i.e. $c$ is the smallest number that satisfies $c\geq x$ for all $x$ in $S$. The fact that this supremum exists follows from the completeness of the real numbers. 

We claim that $f(c)=d$. For this, we first prove that $c$ cannot be equal to either $a$ or $b$. Write $\varepsilon_1=d-f(a)>0$. Since $f$ is continuous at $a$, we can find $\delta_1>0$ such that for all $x$ in $[a,b]$ with $|x-a|<\delta_1$ we have $|f(x)-f(a)|<\epsilon_1$. Then we can take any $a<x<b$ with $|x-a|<\delta_1$ and for such $x$ we have $|f(x)-f(a)|<\epsilon_1=d-f(a)$, which means $f(x)<d$ and therefore this $x$ must be in $S$. As such, there are numbers in $S$ larger than $a$, so $a$ cannot be the smallest upper bound of $S$. Hence, we must have $c>a$. 

Similarly, we can write $\varepsilon_2=f(b)-d>0$. Since $f$ is continuous at $b$, we can find $\delta_2>0$ such that for all $x$ with $|x-b|<\delta_2$ we have $|f(x)-f(b)|<\epsilon_2$. Then we can take any $a<x<b$ in $[a,b]$ with $|x-b|<\delta_2$ and for such $x$ we have $|f(b)-f(x)|<\epsilon_2=f(b)-d$, which means $f(x)>d$ and therefore this $x$ cannot be in $S$. Hence, there are numbers below $b$ that are not in $S$, so $b$ cannot be the smallest upper bound of $S$. As such, we must have $c<b$.

Combining the two inequalities, we must have $a<c<b$. As such, we can find $\delta_3>0$ in such a way that $a+\delta_3<c<b-\delta_3$. Now let $\varepsilon>0$ be given. $f$ is continuous at $c$, so we can find $\delta_4>0$ such that for all $x$ with $0<|x-c|<\delta_4$ we have $|f(x)-f(c)|<\varepsilon$, i.e. $f(x)-\varepsilon<f(c)<f(x)+\varepsilon$. We take $\delta=\operatorname{min}\left(\delta_3,\delta_4\right)$, so $\delta$ is the smallest of the values $\delta_3$ and $\delta_4$. Because of how we chose $\delta_3$, each $x$ with $c-\delta<x<c+\delta$ is in the interval $[a,b]$. Since $c$ is the smallest upper bound of the set $S$, there must be a number $p$ with $c-\delta<p<c$ which is in $S$, since otherwise $c-\delta$ would be an even smaller upper bound for $S$. For this number $p$, we have $|p-c|<\delta$ and $p$ is in $S$, i.e. $f(p)<d$, so we find

$$
 f(c)<f(p)+\varepsilon<d+\varepsilon
$$

Since $c$ is an upper bound of $S$, any number $q$ with $c<q<c+\delta$ cannot be in $S$, which means that $f(q)\geq d$. So for any such number $q$ we have $|q-c|<\delta$ and $q$ is not in $S$, so we find

$$
 f(c)>f(q)-\varepsilon\geq d-\varepsilon
$$

We conclude that $d-\varepsilon<f(c)<d+\varepsilon$. Since these inequalities hold for all $\varepsilon>0$, we must have that $f(c)=d$, as desired.

:::

::::{figure} Images/Fig-Continuity-IVT.png
:name: Fig:Continuity:IVT
:class: dark-light

A function $f$ to illustrate {prf:ref}`Theorem:Continuity:IVT`.
::::

::::{note}
:name: Note:Continuity:IVTlabels

In this applet/figure, do not add labels for the function $f$. Label the point $0$ as $a$ and the point $\pi$ as $b$. In both pictures, the lines $y=\frac{1}{2}$ and $y=-\frac{1}{2}$ should be labeled as $f(a)$ and $f(b)$ respectively. In the left picture, the line $y=\frac{1}{4}$, should be labeled as $d$, along with the corresponding vertical line labeled as $c$. In the right picture, the line $y=0.7$, labeled as $d$, along with the two corresponding vertical lines labeled as $c_1$ and $c_2$.
::::

The Intermediate Value Theorem can be used to show that certain equations have a solution, even if finding this solution is very hard, or even impossible.

::::::{prf:example} 
:label: Ex:Continuity:IVT

Suppose we want to show that the equation $x^5-8x^3+2x^2+1=0$ has at least $1$ solution between $0$ and $1$. Unless you are very lucky, it is impossible to find an explicit expression for a root of a polynomial of degree $5$. Here, we can use the Intermediate Value Theorem. Indeed, note that the function $f(x)=x^5-8x^3+2x^2+1$ is continuous on the interval $[0,1]$ as it is a polynomial. Moreover, we can compute that $f(0)=1$ and $f(1)=-4$. By the Intermediate Value Theorem, $f$ must take on any value in between $1$ and $-4$ on the interval $[0,1]$. Since $0$ is in between these values, there must be some $c$ in $[0,1]$ with $f(c)=c^5-8c^3+2c^2+1=0$. As such, the equation $x^5-8x^3+2x^2+1=0$ has at least one solution between $0$ and $1$.

::::{figure} Images/Fig-Continuity-IVTex.png
:name: Fig:Continuity:IVTex
:class: dark-light

The function $f$ with supporting horizontal and vertical lines that we can use with {prf:ref}`Theorem:Continuity:IVT`.
::::


We could even try to find a better approximation for what the value of $c$ is. Indeed, we can divide the interval $[0,1]$ into two pieces $\left[0,\frac{1}{2}\right]$ and $\left[\frac{1}{2},1\right]$. Note that $f\left(\frac{1}{2}\right)=\frac{33}{32}>0$. So on the interval $\left[\frac{1}{2},1\right]$, $f$ changes from positive to negative, which means that on this interval it must be equal to $0$ somewhere. As such, there is a solution to $x^5-8x^3+2x^2+1=0$ in between $\frac{1}{2}$ and $1$. We can continue this process of dividing the interval in two pieces and looking on which of these intervals we can still apply the Intermediate Value Theorem. The longer we continue this process, the closer we will be to the actual value of the solution. However, we cannot use this method to find the exact value of the solution, as we can only perform finitely many computations.
::::::


The reasoning in {prf:ref}`Ex:Continuity:IVT` can be generalized to obtain the following result and is known as the **Intermediate Zero Theorem** or **Bolzano's Theorem**, named after the Bohemian mathematician [Bernardus Placidus Johann Nepomuk Bolzano (1781-1848)](https://en.wikipedia.org/wiki/Bernard_Bolzano). Long before the formal formulation of this theorem, the result was known and used already by the Flemish mathematician [Simon Stevin (1548-1620)](https://en.wikipedia.org/wiki/Simon_Stevin).

::::::{prf:corollary} Bolzano's Theorem
:label: Cor:Continuity:IVT

Suppose that $f$ is continuous on the closed interval $[a,b]$. If $f(a)$ and $f(b)$ have opposite signs (so one of them is positive while the other is negative) then there is a point $c$ in the open interval $(a,b)$ with $f(c)=0$.
::::::

:::{admonition} Proof of {prf:ref}`Cor:Continuity:IVT`
:class: tudproof
Since $f(a)$ and $f(b)$ have opposite signs, the number $0$ must be in between these values. Hence, the result follows directly from {prf:ref}`Theorem:Continuity:IVT`.
:::

:::{prf:remark}
:label: Remark:Continuity:Weierstrass

The name Weierstrass Nullstellensatz, named after the German mathematician [Karl Theodor Wilhelm Weierstrass (1815-1897)](https://en.wikipedia.org/wiki/Karl_Weierstrass) is sometimes used for either {prf:ref}`Theorem:Continuity:IVT` or {prf:ref}`Cor:Continuity:IVT`. Usually, the Weierstrass Nullstellensatz refers to a version of Bolzano's Theorem specifically for polynomials with coefficients in a [real closed field](https://en.wikipedia.org/wiki/Real_closed_field)
:::

:::{todo}
Interactive element: let students enter function plus left and right endpoint plus number of steps. Check if $f(a)f(b)<0$. If so, let students select correct interval $[a,...]$ or $[...,b]$. Then split this new interval up again and same question. After each step, show the graph of $f$ on the chosen interval. Could be either an applet or something in python?
:::

::::::{prf:example} 
:label: Ex:Continuity:IVTnoncont

The assumption that the function $f$ in the Intermediate Value Theorem is continuous is essential. Indeed, consider the function 
$$
 f(x)=\left\{\begin{array}{ll}x+3,&\text{if }\,x\leq 1\\ 2x+4,&\text{if }\,x>1.\end{array}\right.
$$

Then $f$ is not continuous at the point $1$, since the function values jump from $4$ to $6$ there. In addition, even though $f(0)=3$ and $f(2)=8$, there is no value of $x$ with $f(x)=5$.

It is also important that the function is defined in each point of the closed interval $[a,b]$. Indeed, consider the function $g(x)=\frac{1}{x}$. Then $g$ is continuous on its maximal domain (as it is the quotient of two polynomials), which does not include $x=0$. Note that $f(-1)=-1$ and $f(1)=1$. However, there is no $x$ in between $-1$ and $1$ with $f(x)=0$.

::::{figure} Images/Fig-Continuity-IVTnoncont.png
:name: Fig:Continuity:IVTnoncont
:class: dark-light

The function $f$ on the left, the function $g$ on the right.
::::

::::::





## Continuity of standard functions

With the intermediate value theorem in hand, we are almost ready to show the continuity of standard functions. As a final preparation, we can show that inverse functions (if they exist) of continuous functions are continuous. Intuitively, this result makes sense: the graph of the inverse function is obtained by reflecting the graph of the original function in the line $y=x$, so if the first one does not contain any jumps, the second one will not contain any jumps as well. In order to establish this result, we first need the following theorem.


::::::{prf:theorem} 
:label: Thm:Continuity:InverseMonotonic
Let $f$ be an invertible function, defined on an interval $(a,b)$, that is continuous. Then $f$ is either strictly monotonic on the interval $(a,b)$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Continuity:InverseMonotonic`
:class: tudproof, dropdown
Suppose that is $f$ is neither strictly increasing nor strictly decreasing on $(a,b)$. Then there are three points $a<x_1<x_2<x_3<b$ such that $f(x_2)$ does not lie in between $f(x_1)$ and $f(x_3)$. Then either $f(x_1)$ is in between $f(x_2)$ and $f(x_3)$ or $f(x_3)$ is in between $f(x_1)$ and $f(x_2)$.

First suppose that $f(x_1)$ is in between $f(x_2)$ and $f(x_3)$. By the Intermediate Value Theorem, there is a $c$ in between $x_2$ and $x_3$ with $f(c)=f(x_1)$. However, since $x_1<x_2<x_3$ and $c$ is in between $x_2$ and $x_3$, $c$ cannot be equal to $x_1$. Therefore, $c$ and $x_1$ are different numbers with the same function value, which contradicts the invertibility of $f$.

Similarly, suppose that $f(x_3)$ is in between $f(x_1)$ and $f(x_2)$. By the Intermediate Value Theorem, there is a $c$ in between $x_1$ and $x_2$ with $f(c)=f(x_3)$. However, since $x_1<x_2<x_3$ and $c$ is in between $x_1$ and $x_2$, $c$ cannot be equal to $x_3$. Therefore, $c$ and $x_3$ are different numbers with the same function value, which contradicts the invertibility of $f$.
:::




::::::{prf:theorem} Continuity of inverse functions
:label: Theorem:Continuity:Inverse
Let $f$ be one-to-one function, defined on an interval $(a,b)$, that is continuous. Then the inverse function $f^{-1}$ is continuous as well.

::::::

:::{admonition} Proof of {prf:ref}`Theorem:Continuity:Inverse`
:class: tudproof, dropdown
By {prf:ref}`Thm:Continuity:InverseMonotonic` $f$ must be either strictly increasing or strictly decreasing on $(a,b)$. We assume that $f$ is strictly increasing (the case where $f$ is strictly decreasing is similar). Let $d$ be any point in the domain of $f^{-1}$ and write $c=f^{-1}(d)$. Let $\varepsilon>0$ be given. We want to choose $\delta>0$ in such a way that for each $y$ with $0<|y-d|<\delta$ we have $|f^{-1}(y)-f^{-1}(d)|<\varepsilon$, i.e. $c-\varepsilon=f^{-1}(d)-\varepsilon<f^{-1}(y)<f^{-1}(d)+\varepsilon=c+\varepsilon$. If $\varepsilon$ is too large $c-\varepsilon$ and/or $c+\varepsilon$ might be outside of the interval of $(a,b)$, so we assume that $\varepsilon$ is sufficiently small (as we saw earlier, small values of $\varepsilon$ are the most interesting cases anyway). Define $y_1=f(c-\varepsilon)$ and $y_2=f(c+\varepsilon)$. We know that $f$ is strictly increasing, so we must have $y_1<d<y_2$. Now we choose $\delta>0$ in such a way that $y_1\leq d-\delta$ and $d+\delta\leq y_2$.   We know that for any $y$ with $|y-d|<\delta$ we have $y_1\leq d-\delta<y<d+\delta\leq y_2$, which means that $f^{-1}(y_1)<f^{-1}(y)<f^{-1}(y_2)$. Hence, $f^{-1}$ must be strictly increasing as well. Then we obtain

$$
 c-\varepsilon=f^{-1}(y_1)<f^{-1}(y)<f^{-1}(y_2)=c+\varepsilon
$$

This means that $|f^{-1}(y)-c|<\varepsilon$, as desired. Hence, $f^{-1}$ is continuous at $c$. Since $c$ was chosen arbitrary, $f^{-1}$ is continuous on its maximal domain.
:::



::::::{warning} 
:name: Warning:Continuity:Inverse
If $f$ is a one-to-one function, defined on an interval $(a,b)$, that is continuous at a point $c$ in the interval $(a,b)$, you might expect that the inverse function $f^{-1}$ is continuous at $f(c)$ as well, but this is not necessarily the case. However, coming up with an example where this fails, is very hard. We provide one below, but it is very technical, so read it at your own risk.

::::::

:::{prf:example} Example of one-to-one function where continuity at point does not carry over to inverse
:label: Example:Continuity:InverseDiscontinuity
:class: dropdown

Consider the function $f(x)$, defined for $x$ in the interval $(-1,1)$, which has $f\left(\frac{1}{n}\right)=\frac{1}{2n}$ for all integers $n\geq 3$, $f\left(1-\frac{1}{n}\right)=\frac{1}{2n+1}$ for all integers $n\geq 3$ and $f(x)=x$ for all other values of $x$. First, we show that $f$ is one-to-one. Note that the points of the form $\frac{1}{n}$ are mapped to points of the form $\frac{1}{m}$ with $m$ even, while points of the form $1-\frac{1}{n}$ are mapped to points of the form $\frac{1}{m}$ with $m$ odd, so these points are not mapped to the same function values. Moreover, if $x$ is not of one of these forms, then $x$ is mapped to itself, which is not of the form $\frac{1}{m}$ for $m$ either even or odd. So indeed, different points are mapped to different function values, so the function is one-to-one.

Now we claim that $f$ is continuous at $0$. We know $f(0)=0$, so we must show that $\lim\limits_{x\rightarrow 0}f(x)=0$. Let $\varepsilon>0$ be given. We choose $\delta=\mathrm{min}\left\{\varepsilon,\dfrac{1}{2}\right\}$, i.e. $\delta$ is the smallest of the two values $\varepsilon$ and $\dfrac{1}{2}$. Then for $x$ with $|x|<\delta$ we either have $x=\frac{1}{n}$, which means that $|f(x)|=\frac{1}{2n}\leq \frac{1}{n}<\delta=\varepsilon$, or $x$ is not of this form, in which case $|f(x)|=|x|<\delta=\varepsilon$ ($x=1-\frac{1}{n}$ for $n\geq 3$ is not possible since we assumed that $\delta\leq \frac{1}{2}$). As such, we must have $\lim\limits_{x\rightarrow 0}f(x)=0$, so $f$ is continuous at $0$.

[^Footnoteproperty]: In this case, the property is that for all $x$ in the domain of $f^{-1}$ with $0<|x-0|<\delta$ we have $|f^{-1}(x)-f^{-1}(0)|<\varepsilon$.

Finally, we claim that $f^{-1}$ is not continuous at $0$. Note that $f^{-1}(0)=0$, as $f(0)=0$. Since continuity means that for each $\varepsilon>0$ there is a $\delta>0$ with a certain property[^Footnoteproperty], and we want to show that the function is discontinuous, we want to choose $\varepsilon>0$ such that there is no $\delta>0$ with the desired property. Here, we choose $\varepsilon=\frac{1}{4}$. We want to show that no choice of $\delta$ works, so we let $\delta>0$ be given. Then we can choose an integer $n\geq 3$ such that $0<\frac{1}{2n+1}<\delta$. For this $n$, we find that $f^{-1}\left(\frac{1}{2n+1}\right)=1-\frac{1}{n}$, since we know that $f\left(1-\frac{1}{n}\right)=\frac{1}{2n+1}$. Since $n\geq 2$, we have $f^{-1}\left(\frac{1}{2n+1}\right)=1-\frac{1}{n}>\frac{1}{4}=\varepsilon$. So we found a point $x$ with $0<|x|<\delta$ and $|f^{-1}(x)|\geq \varepsilon$. Since $\delta$ was chosen arbitrarily, no $\delta$ is going to work. As such, the function $f^{-1}$ is not continuous at $f^{-1}(0)=0$, even though $f$ was continuous at $0$.

So if a one-to-one function is continuous on an interval, then its inverse is continuous on the corresponding interval as well {prf:ref}`Theorem:Continuity:Inverse`, but this is no longer true when we only look at continuity in a single point.

:::{todo}
Hier ook nog een schets van de functie, met alle discrete waarden als gevulde stippen gehighlight en alle gaten met open stippen.
:::
:::

With all these preparations in hand, we are ready to show that most standard functions are continuous.

::::::{prf:theorem} Continuity of standard functions
:label: Theorem:Continuity:Standardfunctions
The following functions are continuous on their maximal domain.

- $f(x)=x^r$ for any real number $r$
- $f(x)=|x|$
- $f(x)=b^x$ for $b>0$
- $f(x)=\log_b(x)$ for $b>0$ and $b\neq 1$
- $f(x)=\sin(x)$
- $f(x)=\cos(x)$
- $f(x)=\tan(x)$
- $f(x)=\arcsin(x)$
- $f(x)=\arccos(x)$
- $f(x)=\arctan(x)$


::::::

::::::{admonition} Proof of {prf:ref}`Theorem:Continuity:Standardfunctions`
:class: tudproof, dropdown, full-width

[^Footnoterange]: This happens when $a^r-\varepsilon<0$ and $r$ is not of the form $r=\dfrac{p}{q}$ with $p$ and $q>0$ integers with $q$ odd.
[^Footnotesmalleps]: As we saw earlier, small values of $\varepsilon$ are the most interesting cases anyway.

**Continuity of $x^r$:** Let $r>0$ and consider the function $f(x)=x^r$. Let $a\geq 0$ be any point in the domain of $f$ and let $\varepsilon>0$ be given. We want to choose $\delta>0$ in such a way that for each $x$ with $0<|x-a|<\delta$ we have $|x^r-a^r|<\varepsilon$, i.e. $a^r-\varepsilon<x^r<a^r+\varepsilon$. If $a^r-\varepsilon$ is not in the range of $f$[^Footnoterange] the part $a^r-\varepsilon<x^r$ is satisfied automatically, so we can assume that $a^r-\varepsilon$ is in the range of $f$[^Footnotesmalleps]. Define $x_1=\left(a^r-\varepsilon\right)^{\frac{1}{r}}$ and $x_2=\left(a^r+\varepsilon\right)^{\frac{1}{r}}$. From {prf:ref}`Thm:PropertiesFunctions:Powernondecreasenonincrease` we know that the function $x^{\frac{1}{r}}$ is strictly increasing, so we must have $x_1<a<x_2$. Now we choose $\delta>0$ in such a way that $0\leq x_1\leq a-\delta$ and $a+\delta\leq x_2$. Since $f$ is strictly increasing as well by {prf:ref}`Thm:PropertiesFunctions:Powernondecreasenonincrease`, we know that for any $x$ with $|x-a|<\delta$ we have $x_1\leq a-\delta<x<a+\delta\leq x_2$, which means that $f(x_1)<f(x)<f(x_2)$, i.e. 

$$
 a^r-\varepsilon=\left(\left(a^r-\varepsilon\right)^{\frac{1}{r}}\right)^r=f(x_1)<x^r<f(x_2)=\left(\left(a^r+\varepsilon\right)^{\frac{1}{r}}\right)^r=a^r+\varepsilon
$$

This means that $|x^r-a^r|<\varepsilon$, as desired. Hence, $f$ is continuous at $a$. Now suppose that $r=\dfrac{p}{q}$ with $p$ and $q>0$ integers with $q$ odd. Then (and only then) the domain of $f$ also contains the interval $(-\infty,0)$ so we let $a$ in $(-\infty,0)$. Note that for $x<0$ we have if $p$ is odd

$$
 f(x)=x^r=\sqrt[q]{x^p}=-\sqrt[q]{\left(-x\right)^p}=-\left(-x\right)^r=-f(-x)
$$

while if $p$ is even we have

$$
 f(x)=x^r=\sqrt[q]{x^p}=\sqrt[q]{\left(-x\right)^p}=\left(-x\right)^r=f(-x).
$$

Since $f$ is continuous at $-a$, we obtain from {prf:ref}`Theorem:Continuity:Basiccomputationrules` that $f$ is also continuous at $a$. So $f$ is continuous on its maximal domain.

Since $a$ was chosen arbitrary, $f$ is continuous on its maximal domain.

For $r=0$, we have the function $f(x)=x^r=1$. We already saw that this function is continuous in {prf:ref}`Theorem:Continuity:ContPoly`.

Now, finally, we let $r<0$ and consider the function $f(x)=x^r$. Then $f(x)=\frac{1}{x^{-r}}$ and since $-r>0$ the function $x\mapsto x^{-r}$ is continuous on its maximal domain. Then $f$ is continuous on its maximal domain as it is the quotient of two continuous functions.

**Continuity of $|x|$:** Let $f(x)=|x|$. For $a>0$, we have $\lim\limits_{x\rightarrow a}|x|=\lim\limits_{x\rightarrow a}x=a=|a|$, since the function $x$ is continuous at $a$. Similarly, for $a<0$, we have $\lim\limits_{x\rightarrow a}|x|=\lim\limits_{x\rightarrow a}-x=-a=|a|$, since the function $-x$ is continuous at $a$. Finally, we consider $a=0$. Then we have $\lim\limits_{x\rightarrow 0^+}|x|=\lim\limits_{x\rightarrow 0^+}x=0=|0|$, since the function $x$ is continuous at $0$. Similarly, we have $\lim\limits_{x\rightarrow 0^-}|x|=\lim\limits_{x\rightarrow 0^-}-x=-0=|0|$, since the function $-x$ is continuous at $0$. We conclude that $\lim\limits_{x\rightarrow 0}|x|=0=|0|$, so $f$ is continuous at $0$. Hence, $f$ is continuous on its maximal domain.

**Continuity of $b^x$:** Let $b>0$ be given and consider the function $f(x)=b^x$. Recall from {numref}`Subsec:RealnumbersExp` how this function was defined: for a rational number $a=\frac{p}{q}$ (so with $p$ and $q$ integers), we defined $b^a=b^{\frac{p}{q}}=\sqrt[q]{b^p}$. Then for an irrational number $a$ we 'filled in the gap' by approximating $b^a$ from below by a sequence of numbers $b^{x_1},b^{x_2},b^{x_3},\ldots$ and from above by $b^{y_1},b^{y_2},b^{y_3},\ldots$ where $x_1,x_2,x_3,\ldots$ and $y_1,y_2,y_3,\ldots$ are rational and approach the value $a$ (more mathematically: the sequences $\left\{x_n\right\}_{n=1}^\infty$ and $\left\{y_n\right\}_{n=1}^\infty$ converge to $a$, see {numref}`Section:SequenceConvergence`). Stated differently, we constructed $b^a$ in such a way that the function $f$ is continuous at $a$. As such, this function is continuous everywhere.

**Continuity of $\log_b(x)$:** Let $b>0$ with $b\neq 1$ and consider $f(x)=\log_b(x)$. Then $f$ is the inverse function of the continuous function $b^x$. So by {prf:ref}`Theorem:Continuity:Inverse` $f$ is continuous.

**Continuity of $\sin(x)$ and $\cos(x)$:** Now consider the function $f(x)=\sin(x)$. We will first show that $f$ is continuous in $0$ by showing that $\lim\limits_{x\rightarrow 0}\sin(x)=\sin(0)=0$. For this, we will show that $|\sin(x)|\leq |x|$ for all $-\frac{\pi}{2}<x<\frac{\pi}{x}$, which will allow us to use the squeeze theorem. First consider $x$ with $0<x<\frac{\pi}{2}$. We consider a circle with radius $1$, centered around the origin $O$. Then we consider two points $A$ and $B$ on the circle such that the angle between the line pieces $OA$ and $OB$ is exactly $x$, as shown in the figure below.

::::{figure} Images/Fig-Continuity-Standardfunctions.svg
:name: Fig:Continuity:Standardfunctions
:class: dark-light

Circle with centre O and points A and B on its circumference, where A lies on the positive $x$-axis. Triangle AOB is shown with angle $x$ between OA and OB. Point C lies on line OA, directly below B.
::::

Consider the point $C$ that lies on the line piece $OA$ in such a way that the triangle $OCB$ is a right triangle. By the geometric definition of the sine, we have $\sin(x)=\frac{|BC|}{|OB|}=|BC|$, since $B$ lies on the circle with radius $1$ and center $O$. Note that $C$ is the closest point to $B$ on the line through $O$ and $A$, since the line piece $BC$ is orthogonal to the line piece $OA$. As such, we must have $|BC|\leq |BA|$. The length of the part of the circle from $A$ to $B$ is exactly $\frac{x}{2\pi}$ times the total circumference of the circle. Since the circle has radius $1$, this length is $\frac{x}{2\pi}2\pi=x$. Since $|AB|$ is the distance between $A$ and $B$, and $x$ is the length of a different path from $A$ to $B$ (namely the one following the circle), we must have $|AB|\leq x$. Combining the inequalities gives 

$$
 \sin(x)=|BC|\leq |AB|\leq x.
$$ 

Since $\sin(x)$ and $x$ are both positive, we find $|\sin(x)|\leq |x|$. For $-\frac{\pi}{2}<x<0$ we have $0<-x<\frac{\pi}{2}$ and we find

$$
 |\sin(x)|=|-\sin(-x)|=|\sin(-x)|\leq|-x|=|x|,
$$

as desired. So for all $-\frac{\pi}{2}<x<\frac{\pi}{x}$ we have $|\sin(x)|\leq |x|$, i.e. we have $-|x|\leq \sin(x)\leq |x|$. Since $|x|$ and $-|x|$ are continuous, we find $\lim\limits_{x\rightarrow 0}-|x|=-|0|=0$ and $\lim\limits_{x\rightarrow 0}|x|=|0|=0$. By {prf:ref}`Theorem:LimitAtPoint:Squeezetheorem` we find that $\lim\limits_{x\rightarrow 0}\sin(x)=0=\sin(0)$ as well. Hence, the sine is continuous at $0$. 

Before establishing that the sine is continuous at any other point, we will first establish that that $g(x)=\cos(x)$ is continuous in $0$ as well. For this we evaluate

$$
 \lim\limits_{x\rightarrow 0}\cos(x)-1=\lim\limits_{x\rightarrow 0}\left(\cos(x)-1\right)\frac{\cos(x)+1}{\cos(x)+1}=\lim\limits_{x\rightarrow 0}\frac{\cos(x)^2-1}{\cos(x)+1}=\lim\limits_{x\rightarrow 0}\frac{-\sin(x)^2}{\cos(x)+1}
$$

By the geometrical definition of the cosine, we know that the cosine is strictly decreasing on the interval $\left[0,\frac{\pi}{2}\right]$, so we find $0=\cos\left(\frac{\pi}{2}\right)\leq \cos(x)\leq  \cos(0)=1$ for all $0\leq x\leq\frac{\pi}{2}$. Since $\cos(-x)=\cos(x)$, we find that $0\leq \cos(x)\leq1$ and, therefore, $1\leq \cos(x)+1\leq2$ holds for all $-\frac{\pi}{2}\leq x\leq \frac{\pi}{2}$. As such, we find that 

$$
 \frac{-\sin(x)^2}{1}\leq \frac{-\sin(x)^2}{\cos(x)+1}\leq \frac{\sin(x)^2}{1}
$$

for all $-\frac{\pi}{2}\leq x\leq \frac{\pi}{2}$. Since the sine is continuous at $0$, we find that 

$$
 \lim\limits_{x\rightarrow 0}-\sin(x)^2=-\sin(0)^2=0
$$

and

$$
 \lim\limits_{x\rightarrow 0}\sin(x)^2=\sin(0)^2=0.
$$ 

By {prf:ref}`Theorem:LimitAtPoint:Squeezetheorem` we find that 

$$
 \lim\limits_{x\rightarrow 0}\cos(x)-1=\lim\limits_{x\rightarrow 0}\frac{-\sin(x)^2}{\cos(x)+1}=0,
$$

so

$$
 \lim\limits_{x\rightarrow 0}\cos(x)=1=\cos(0).
$$

Hence, the cosine is continuous at $0$.


Now we consider any point $a$ and we will show that the sine is continuous at $a$. For any $x$ we write $\sin(x)=\sin(a+(x-a))=\sin(a)\cos(x-a)+\cos(a)\sin(x-a)$. Let $\varepsilon>0$ be given. Since the cosine is continuous at $0$, we can take $\delta_1>0$ such that for all $x$ with $0<|x|<\delta_1$ we have $|\cos(x)-1|<\frac{\varepsilon}{2}$. Also, since the sine is continuous at $0$, we can take $\delta_2>0$ such that for all $x$ with $0<|x|<\delta_2$ we have $|\sin(x)|<\frac{\varepsilon}{2}$. We let $\delta=\operatorname{min}(\delta_1,\delta_2)$, i.e. $\delta$ is the smallest of $\delta_1$ and $\delta_2$. Then for $x$ with $0<|x-a|<\delta$ we can estimate

$$
 \begin{array}{lcll}|\sin(x)-\sin(a)|&=&|\sin(a)\cos(x-a)+\cos(a)\sin(x-a)-\sin(a)|&\\
 &\leq &|\sin(a)\cos(x-a)-\sin(a)|+|\cos(a)\sin(x-a)|\qquad &\text{using the triangle inequality}\\
 &=&|\sin(a)||\cos(x-a)-1|+|\cos(a)||\sin(x-a)|&\\
 &\leq &|\cos(x-a)-1|+|\sin(x-a)|&\text{since }|\sin(a)|\leq 1\,\text{ and }\,|\cos(a)|\leq 1\\
 &\leq &\frac{\varepsilon}{2}+|\sin(x-a)|&\text{since }\,0<|x-a|<\delta\leq \delta_1\\
 &\leq &\frac{\varepsilon}{2}+\frac{\varepsilon}{2}&\text{since }\,0<|x-a|<\delta\leq \delta_2\\
 &=&\varepsilon&\end{array}
$$

Here we used the triangle inequality {prf:ref}`thm:triangle_inequality_real_numbers`. As such, we have shown that $\lim\limits_{x\rightarrow a}\sin(x)=\sin(a)$. So the sine is continuous everywhere. Note that $\cos(x)=\sin\left(\frac{\pi}{2}-x\right)$, so the cosine is the composition of the continuous functions $\sin(x)$ and $\frac{\pi}{2}-x$, which by {prf:ref}`Theorem:Continuity:Composition` means that the cosine is continuous as well.

**Continuity of $\tan(x)$:** The function $\tan(x)=\frac{\sin(x)}{\cos(x)}$ is the quotient of two continuous functions and is, therefore, itself continuous on its maximal domain. 

**Continuity of $\arcsin(x)$, $\arccos(x)$ and $\arctan(x)$:** Finally, the inverse trigonometric functions $\arcsin(x)$, $\arccos(x)$ and $\arctan(x)$ are inverse functions of continuous functions, so by {prf:ref}`Theorem:Continuity:Inverse` they are continuous as well.
::::::

With these results at hand, we can finally prove the fundamental results from {numref}`Section:LimitPoint` which we used in most computations in that section.

:::{admonition} Proof of {prf:ref}`Theorem:LimitAtPoint:Directsub`
:class: tudproof, dropdown
If $f$ is a polynomial, rational function, power of $x$, (inverse) trigonometric function, exponential function or logarithmic function and $a$ is in the domain of $f$, then $f$ is continuous at $a$ by {prf:ref}`Theorem:Continuity:Standardfunctions`, possibly combined with {prf:ref}`Theorem:Continuity:Basiccomputationrules`. As such, we must have $\lim\limits_{x\rightarrow a}f(x)=f(a)$, as desired.
:::

We can also establish a more general version of {prf:ref}`Theorem:LimitAtPoint:Substitution` and {prf:ref}`Theorem:LimitAtInfinity:Substitution`, which, in turn, we can use to prove these results.

::::::{prf:theorem} Substitution for limit at a point
:label: Theorem:Continuity:Substitution
Let $f$ be a function and suppose that the domain of $f$ contains intervals of the form $(c_1,b)$ and $(b,c_2)$. Suppose that $f$ is continuous at $b$. Moreover, suppose that $\lim\limits_{x\rightarrow a}g(x)=b$. Then $\lim\limits_{x\rightarrow a}f(g(x))=f\left(\lim\limits_{x\rightarrow a}g(x)\right)=f(b)$.
::::::

:::{admonition} Proof of {prf:ref}`Theorem:Continuity:Substitution`
:class: tudproof, dropdown
Consider the function $h(x)=\left\{\begin{array}{ll}g(x)&\text{if }\,x\neq a\\ b&\text{if }\,x=a\end{array}\right.$ Since $\lim\limits_{x\rightarrow a}h(x)=\lim\limits_{x\rightarrow a}g(x)=b=h(a)$, $h$ is continuous at $a$. As such, the function $f\circ h$ is continuous by {prf:ref}`Theorem:Continuity:Composition` at $a$. Note that for $x\neq a$ we have $f(h(x))=f(g(x))$. Then we find

$$
 \lim\limits_{x\rightarrow a}f(g(x))=\lim\limits_{x\rightarrow a}f(h(x))=f(h(a))=f(b)=f\left(\lim\limits_{x\rightarrow a}g(x)\right)
$$
:::

:::{admonition} Proof of {prf:ref}`Theorem:LimitAtPoint:Substitution`
:class: tudproof, dropdown
:name: prf:Continuity:Prooflimitpointsub
If $f$ is a polynomial, rational function, power of $x$, (inverse) trigonometric function, exponential function or logarithmic function and $b$ is in the domain of $f$, then $f$ is continuous at $b$ by {prf:ref}`Theorem:Continuity:Standardfunctions`, possibly combined with {prf:ref}`Theorem:Continuity:Basiccomputationrules`. As such, the result follows from {prf:ref}`Theorem:Continuity:Substitution`


:::

::::::{prf:theorem} Substitution for limit at plus or minus infinity
:label: Theorem:Continuity:SubstitutionInf
Let $f$ be a function and consider $b$ in the domain of $f$. Suppose that $f$ is continuous at $b$. Moreover, suppose that $\lim\limits_{x\rightarrow \infty}g(x)=b$. Then $\lim\limits_{x\rightarrow \infty}f(g(x))=f\left(\lim\limits_{x\rightarrow \infty}g(x)\right)=f(b)$.

A similar result holds for limits at minus infinity.
::::::

:::{admonition} Proof of {prf:ref}`Theorem:Continuity:SubstitutionInf`
:class: tudproof, dropdown

[^Footnoteroleepsdelt]: Hence, $\delta$ takes the rol here that $\varepsilon$ usually takes.

Unfortunately, since we are dealing with a limit at infinity, we cannot refer to {prf:ref}`Theorem:Continuity:Composition`. Instead, we will use the precise definition of a limit at infinity. Let $\varepsilon>0$ be given. Since $f$ is continuous at $b$, we can find $\delta>0$ such that for all $x$ in the domain of $f$ with $0<|x-b|<\delta$ we have $|f(x)-f(b)|<\varepsilon.$ Then, since $\lim\limits_{x\rightarrow \infty}g(x)=b$ we can take $N$ such that for all $x$ with $x>N$ we have $|g(x)-b|<\delta$[^Footnoteroleepsdelt]. Then for $x>N$ we have that $g(x)$ is a number with $|g(x)-b|<\delta$, which means that $|f(g(x))-f(b)|<\varepsilon$. This precisely means that $\lim\limits_{x\rightarrow \infty}f(g(x))=f(b)$, as desired.
:::

:::{admonition} Proof of {prf:ref}`Theorem:LimitAtInfinity:Substitution`
:class: tudproof, dropdown
If $f$ is a polynomial, rational function, power of $x$, (inverse) trigonometric function, exponential function or logarithmic function and that $b$ is in the domain of $f$, then $f$ is continuous at $b$ by {prf:ref}`Theorem:Continuity:Standardfunctions`, possibly combined with {prf:ref}`Theorem:Continuity:Basiccomputationrules`. As such, the result follows from {prf:ref}`Theorem:Continuity:SubstitutionInf`

:::

In case the outer function is not continuous, we need additional assumptions on the inner function to use the substitution rule for limits.

::::::{prf:theorem} Substitution for limit at a point when outer function is not continuous
:label: Theorem:Continuity:SubstitutionAlt
Let $f$ and $g$ be functions such that $g$ is one-to-one and continuous on an open interval $I$ containing a number $a$. Then $\displaystyle\lim_{x\rightarrow a}f(g(x))$ exists precisely when $\displaystyle \lim_{y\rightarrow g(a)}f(y)$ exists. In case these limits exist, they are equal.
::::::

:::{admonition} Proof of {prf:ref}`Theorem:Continuity:SubstitutionAlt`
:class: tudproof, dropdown

Suppose first that $\displaystyle\lim_{x\rightarrow a}f(g(x))=L$. Let $\varepsilon>0$ be given. Then we can find $\delta>0$ such that for all $x$ with $0<|x-a|<\delta$ we have 

$$
 |f(g(x))-L|<\varepsilon$.
$$  

We write $g(I)$ for the set of all values of the form $g(x)$ for $x$ in $I$ and we note that $g(a)$ is in $g(I)$. Since $g$ is one-to-one, the restriction of $g$ from $I$ to $g(I)$ is bijective. Then by {prf:ref}`Theorem:Continuity:Inverse`, the inverse function $g^{-1}$ is continuous on $g(I)$. So we can find $\tilde{\delta}>0$ such that for all $y$ with $0<|y-g(a)|<\tilde{\delta}$ we have 

$$
 |g^{-1}(y)-a|=|g^{-1}(y)-g^{-1}(g(a))|<\delta.
$$

Note that for any $y$ with $0<|y-g(a)|<\tilde{\delta}$ we have $g^{-1}(y)\neq g{^{-1}}(g(a))=a$, so $|g^{-1}(y)-a|\neq 0$, since $g^{-1}$ is one-to-one. This means that for any $y$ with $0<|y-g(a)|<\tilde{\delta}$ we have $0<|g^{-1}(y)-a|<\delta$, from which it follows that

$$
 |f(g(g^{-1}(y)))-L|<\varepsilon.
$$

As such, we find that $\displaystyle \lim_{y\rightarrow g(a)}f(y)=L$.

Now suppose that $\displaystyle \lim_{y\rightarrow g(a)}f(y)=L$. We write $h=f\circ g$. Then we find that $f=f\circ g\circ g^{-1}=h\circ g^{-1}$, so we have

$$
 \lim_{y\rightarrow g(a)}f(y)=\lim_{y\rightarrow g(a)}h(g^{-1}(y)).
$$

In addition, we find that

$$
 \lim_{x\rightarrow a}f(g(x))=\lim_{x\rightarrow a}h(x)=\lim_{x\rightarrow g^{-1}(g(a))}h(x).
$$

Note that $g^{-1}$ is one-to-one and continuous on an interval that contains $g(a)$. So now we can apply the first half of this proof to the function $h$ instead of $f$ and $g^{-1}$ instead of $g$ to conclude that 

$$
 \lim_{x\rightarrow a}f(g(x))=\lim_{x\rightarrow a}h(x)=\lim_{x\rightarrow g^{-1}(g(a))}h(x)=\lim_{y\rightarrow g(a)}h(g^{-1}(y))=\lim_{y\rightarrow g(a)}f(y)=L.
$$

:::


::::::{prf:example} 
:label: Ex:Continuity:Secondexample

Consider the function 
$$
 f(x)=\left\{\begin{array}{ll}2^x+b&\text{if }\,x< 2,\\ 2b+10&\text{ if }\,x=2,\\ x^2-3x&\text{if }\,x>2.\end{array}\right.
$$

We want to find out for which value of $b$, if any, the function is continuous. By {prf:ref}`Theorem:Continuity:Standardfunctions` and {prf:ref}`Theorem:Continuity:Basiccomputationrules` the function $f$ is continuous at each point $a$ except possibly at $a=2$. In order to establish when (if ever) $f$ is continuous at $a=2$, we evaluate

\begin{align*}
 \lim\limits_{x\rightarrow2^-}f(x) &= \lim\limits_{x\rightarrow2^-}2^x+b \\
 &=2^2+b \\
 &=4+b,\\
 \lim\limits_{x\rightarrow2^+}f(x) &= \lim\limits_{x\rightarrow2^+}x^2-3x\\
 &=2^2-3\cdot 2\\
 &=-2,\\
 f(2)&=2b+10.
\end{align*}

So in order for $f$ to be continuous at $2$, we need to have $4+b=-2=2b+10$, i.e. $b=-6$. So $f$ is continuous everywhere if $b=-6$ and otherwise, it is continuous everywhere except at $2$.



::::{figure} Images/Fig-Continuity-Secondexample.png
:name: Fig:Continuity:Secondexample
:class: dark-light

The function $f(x)$ and a slider for the parameter $b$. Can you recreate the result of the example using the slider?

::::
::::::

:::{todo}
Make polling that is variation of the previous example. Or perhaps make only an applet with a slider where the correct value of a parameter needs to be found to make the function continuous.
:::


(Subsec:ContLeftRight)=

## Left and right continuity

Consider the function from {prf:ref}`Ex:Continuity:Visual`. We saw that this function was not continuous at $-2$, since the left and right limit were unequal. However, we can read off from the graph that $\lim\limits_{x\rightarrow 2^-}f(x)=f(-2)$. So if we ignore the part of the function to the right of $-2$, the function is continuous. We say that the function is **left continuous** at $-2$. Although left continuity (and the corresponding **right continuity**) is a bit weaker than regular continuity, it is still a useful concept to consider.

::::::{prf:definition} Left and right continuity
:label: Def:Continuity:Continuityleftright

Let $f$ be a function and $a$ a point in the domain of $f$. Then we say that $f$ is **left continuous** at $a$ if $\lim\limits_{x\rightarrow a^-}f(x)=f(a)$. 

Similarly, we say that $f$ is **right continuous** at $a$ if $\lim\limits_{x\rightarrow a^+}f(x)=f(a)$. 
::::::

::::::{prf:corollary} 
:label: Thm:Continuity:Continuityleftright

Suppose that the domain of $f$ contains an open interval $(b,c)$ and let $a$ in $(b,c)$. Then $f$ is continuous at $a$ precisely when $f$ is both left and right continuous at $a$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Continuity:Continuityleftright`
:class: tudproof
A function is both left and right continuous at $a$, when both identities $\lim\limits_{x\rightarrow a^-}f(x)=f(a)$ and $\lim\limits_{x\rightarrow a^+}f(x)=f(a)$ hold. By {prf:ref}`Theorem:LimitAtPoint:Leftrightequal` this happens precisely when $\lim\limits_{x\rightarrow a}f(x)=f(a)$, i.e. when $f$ is continuous at $a$.
:::

::::::{prf:example} 
:label: Example:Continuity:Continuityleftright

Consider the function $f(x)=\left\{\begin{array}{ll}3x+4,&\text{if }\,x\leq 0\\ \ln(x)+3,&\text{if }\,0<x<1\\ 3-x,&\text{if }\,x\geq 1. \end{array}\right.$
We want to find out at which points $f$ is continuous (either regular, left or right). Since the functions $3x+4$, $\ln(x)+3$ and $3-x$ are continuous on their domains, the only problems can arise at the points where we switch between which formula is used to describe the function values, i.e. at $0$ and $1$. We can evaluate

\begin{align*}
 \lim\limits_{x\rightarrow 0^-}f(x)&=\lim\limits_{x\rightarrow 0^-}3x+4=4,\\
  \lim\limits_{x\rightarrow 0^+}f(x)&=\lim\limits_{x\rightarrow 0^+}\ln(x)+3=-\infty,\\
  f(0)&=4.
\end{align*}

Hence, the limit $\lim\limits_{x\rightarrow 0}f(x)$ does not exist, so the function is not continuous at $0$. However, we do find that $\lim\limits_{x\rightarrow 0^-}f(x)=f(0)$. As such, the function is left continuous at $0$ (but not right continuous).

Similarly, we can evaluate

\begin{align*}
 \lim\limits_{x\rightarrow 1^-}f(x)&=\lim\limits_{x\rightarrow 1^-}\ln(x)+3=3,\\
  \lim\limits_{x\rightarrow 1^+}f(x)&=\lim\limits_{x\rightarrow 1^+}3-x=2,\\
  f(1)&=2.
\end{align*}

Hence, the limit $\lim\limits_{x\rightarrow 1}f(x)$ does not exist, so the function is not continuous at $1$. However, we do find that $\lim\limits_{x\rightarrow 1^+}f(x)=f(1)$. As such, the function is right continuous at $1$ (but not left continuous).

::::{figure} Images/Fig-Continuity-Continuityleftright.png
:name: Fig:Continuity:Continuityleftright
:class: dark-light

The function $f$ as an example for continuity from the right.
::::

::::::

(Subsec:LimitAtInfinityGrasple)=

## Grasple exercises

:::{todo}
Grasple exercises on left- and right continuity
:::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/516eefd5-6e4d-42f0-9cf7-ea54159a3262?id=126101
:label: Grasple:Continuity:Piecewisemakingcont
:dropdown:
:description: Continuity of piecewise defined function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2e8691ba-b5cd-48c7-bbc5-ca6a94481eda?id=126174
:label: Grasple:Continuity:Piecewisenotccontwithlimit
:dropdown:
:description: Continuity of piecewise defined function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/445e61d2-3524-494b-b2de-86e6ce4afdfb?id=71061
:label: Grasple:Continuity:Piecewisenotccontnolimit
:dropdown:
:description: Continuity of piecewise defined function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/720c95b4-58da-476e-a7a6-489a0c11c98e?id=71067
:label: Grasple:Continuity:Piecewisecont
:dropdown:
:description: Continuity of piecewise defined function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1a52582e-aa31-4c85-907e-8f9d2dbfa64a?id=71084
:label: Grasple:Continuity:Rounding
:dropdown:
:description: Continuity of rounding function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7a20b481-0633-4bbe-9ddd-ab543f3a8419?id=71860
:label: Grasple:Continuity:Fractionalpart
:dropdown:
:description: Continuity of fractional part

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c142b871-cbf8-4b80-8d9e-4482a373fed3?id=71152
:label: Grasple:Continuity:Sin1overx
:dropdown:
:description: Continuity of $\sin\left(\frac{1}{x}\right)$

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d41b9b5f-ed30-4ff7-bf03-8fad78f2dc14?id=71154
:label: Grasple:Continuity:xsin1overx
:dropdown:
:description: Continuity of $x\sin\left(\frac{1}{x}\right)$

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/db5adbfb-cc9f-4fdb-9192-204dad31bddd?id=70561
:label: Grasple:Continuity:product
:dropdown:
:description: Continuity of product function

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e5d12e97-b986-442c-9352-e38d034d61c7?id=130757
:label: Grasple:Continuity:leftright1
:dropdown:
:description: Left and right continuity

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8a96a8e7-62aa-40dc-bb17-2b3a76f579cd?id=130761
:label: Grasple:Continuity:leftright2
:dropdown:
:description: Left and right continuity

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/50052d0d-a89a-4096-9d81-72c898a37d50?id=74182
:label: Grasple:Continuity:Inflimitinsidecontsinexp
:dropdown:
:description: Limit at infinity involving sines and exponentials

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/69d04f22-bf0e-4c08-ab3e-3644096d2ffe?id=74229
:label: Grasple:Continuity:Inflimitinsidecontcoslog
:dropdown:
:description: Limit at infinity involving cosines and logarithms
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/99ca75a4-5529-4236-96e4-612120d08955?id=75748
:label: Grasple:Continuity:Inflimitinsidecontcosexp
:dropdown:
:description: Limit at infinity involving cosines and exponentials
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4f72dd27-5d72-47a2-8ef1-f11f6c49ea7a?id=74228
:label: Grasple:Continuity:Inflimitinsidecontratexp
:dropdown:
:description: Limit at infinity involving exponentials
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/987e6761-2501-491b-b264-d649431f68ad?id=75627
:label: Grasple:Continuity:Inflimitinside+squeeze
:dropdown:
:description: Limit at infinity (inverse) trigonometric function
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ed59a9d8-4ba9-4d64-a252-1314e8265571?id=130748
:label: Grasple:Continuity:IVTroot
:dropdown:
:description: Location of root of polynomial
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3e95271d-2875-4061-96e4-53be7714d50b?id=71159
:label: Grasple:Continuity:IVTGamma
:dropdown:
:description: The Gamma function
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/498dd0b8-dee0-4907-978e-ac7abda596a8?id=71156
:label: Grasple:Continuity:IVTtemperature
:dropdown:
:description: Application: temperature on Earth
::::