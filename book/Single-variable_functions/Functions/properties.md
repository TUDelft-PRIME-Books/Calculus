(Section:PropertiesFunctions)=
# Properties of functions

(Subsec:PropertiesFunctionsIntro)=
## Introduction

In {numref}`Section:FunctionsIntro` we encountered several types of functions that we called standard functions (for instance, polynomial functions, trigonometric functions and exponential functions). In this section, we combine these standard functions to obtain other, perhaps more complicated functions. In addition, we saw that these standard functions have some very different qualitative behaviour. For instance, exponential functions either always grow or always decay, while the sine and the cosine show periodic behaviour. We will, therefore, also use this section to define various classes of functions and we will try to find out which standard functions fall in which class.

(Subsec:PropertiesFunctionsCombinations)=
## Combining functions

There are many ways to combine functions into a new function. We start with an example to showcase one possibility.

::::::{prf:example} Sum of two functions
:label: Ex:PropertiesFunctions:Sum
The most straightforward way to combine functions is to use arithmetic operations such as addition and multiplication. For instance, consider the function $f(x)=\sin(x)+\frac{x}{2}$. We observe that this function is some sort of combination of the functions $g(x)=\sin(x)$ and $h(x)=\frac{x}{2}$. Indeed, for each value of $x$ we have

$$
 f(x)=\sin(x)+\frac{x}{2}=g(x)+h(x),
$$

so that the function value $f(x)$ is the sum of the function values $g(x)$ and $h(x)$. As such, we say that the function $f$ is the **sum** of the functions $g$ and $h$, and we write $f=g+h$. 

So what does the graph of $f$ look like in terms of the graphs of $g$ and $h$? For each value of $x$, we know that $f(x)=g(x)+h(x)$, so $f(x)$ is $h(x)$ higher than $g(x)$. That means that if we start from the graph of $g$, we obtain the graph of $f$ by rising the function value $\sin(x)$ by $\frac{x}{2}$ for each value of $x$. This can be seen in the figure below. We can also think of this as the graph of $g$ being stacked on top of the graph of $f$. 

```{figure} Images/Fig-PropertiesFunctions-Sum.png
---
width: 100%
name: Fig:PropertiesFunctions:Sum
class: dark-light
---

An illustration of the sum of two functions.

```

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:Sum` with an applet. Important: the functions in this example have changed, but the png picture still uses the old functions. The applet should use the new functions.
:::

::::::

In the previous example we saw that we can take two functions and create a new function by adding the two functions. In general, we can perform arithmetic operations to functions just like with numbers. 

::::::{prf:definition} Arithmetic with functions
:label: Def:PropertiesFunctions:Arithmetic

Let $f$ and $g$ be functions. Then we can define the following functions.

- The **sum function** $f+g$ is defined by $(f+g)(x)=f(x)+g(x)$.
- The **difference function** $f-g$ is defined by $(f-g)(x)=f(x)-g(x)$.
- The **product function** $fg$ is defined by $(fg)(x)=f(x)g(x)$.
- The **quotient function** $\frac{f}{g}$ is defined by $\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}$.
- If $c$ is a real number, then the **scalar multiple function** $cf$ is defined by $(cf)(x)=cf(x)$.
- If $c$ and $d$ are real numbers, then the **linear combination** $h=cf+dg$ is defined by $h(x)=cf(x)+dg(x)$.

::::::

Notice that each of these functions is found by applying the corresponding operation pointwise. That means that, for instance, we define the product function $fg$ by specifying that at each point $x$, we evaluate the function value of $fg$ at $x$ by computing the product of the real numbers $f(x)$ and $g(x)$. 

Recall that we made the convention that, unless specified otherwise, the domain of a function is its maximal domain. So what does this tell us about the domains of functions like $f+g$ or $\frac{f}{g}$? For $f+g$, we defined $(f+g)(x)=f(x)+g(x)$, so whenever $f(x)$ and $g(x)$ both exist, we can define their sum and, with that, we can define $(f+g)(x)$. As such, the domain of $f+g$ consists of precisely those $x$ that are both in the domain of $f$ and the domain of $g$. That is, the domain of $f+g$ is the intersection of the domains of $f$ and $g$. Writing this formally, we have

$$
 D_{f+g}=D_f\cap D_g.
$$

For $h=\frac{f}{g}$, things are a bit more complicated. Indeed, we defined $h(x)=\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}$, so in order for $h(x)$ to exist, both $f(x)$ and $g(x)$ certainly need to exist. However, if $g(x)=0$ for some $x$, then $\frac{f(x)}{g(x)}$ in undefined because we cannot divide by $0$. As such, the domain of $h=\frac{f}{g}$ consists of those values of $x$ that are both in the domain of $f$ and the domain of $g$ **and** have $g(x)\neq 0$. Writing this formally, we have

$$
 D_{h}=\left(D_f\cap D_g\right)\setminus\left\{x\,\middle|\,g(x)=0\right\}.
$$



::::::{prf:example} 
:label: Ex:PropertiesFunctions:ProductsAndDomains

Consider the functions $r(t)=t^3$ and $s(t)=\frac{1}{t}$. Then their product function $rs$ is defined by $(rs)(t)=t^3\frac{1}{t}$. For example, for $t=2$ we have $r(2)=2^3=8$ and $s(2)=\frac{1}{2}$, which gives $(rs)(2)=r(2)s(2)=8\cdot\frac{1}{2}=4$.  For $t\neq 0$, we can simplify this expression to

$$
 (rs)(t)=t^3\frac{1}{t}=t^2.
$$

So what is the domain of the product function? You might be tempted to think that the domain is the set of all real numbers $\mathbb{R}$, since $t^2$ is defined for all values of $t$. However, $(rs)(t)$ is only equal to $t^2$ when $t\neq 0$. If $t=0$, the function value $s(0)$ is not defined as we cannot divide by $0$. As such, $0$ cannot be in the domain of $rs$. So the domain of $rs$ is the set of real numbers $\mathbb{R}$ without the point $0$, i.e. it is $\mathbb{R}\setminus\{0\}$.

:::{figure} Images/Fig-PropertiesFunctions-ProductsAndDomains.png
:name: Fig:PropertiesFunctions:ProductsAndDomains

The graphs of the functions $r$, $s$ and $rs$. The function $r$ is defined in $0$, but $s$ and $rs$ are not.

:::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:ProductsAndDomains` with an applet. Try to make sure that it is clearly visible that $r$ is defined in $0$, but $s$ and $rs$ are not.
:::

::::::



::::::{prf:example} 
:label: Ex:PropertiesFunctions:Composition

Another way of combining two functions is to use the output of one as the input of the other. For instance, consider the function $f(x)=e^{\sin(x)}$. This function is somehow obtained from the functions $g(x)=e^x$ and $h(x)=\sin(x)$, but how? It is not one of the way described in {prf:ref}`Def:PropertiesFunctions:Arithmetic`. Instead, you should think how we could end up with something like $e^{\sin(x)}$. The answer is the following: we are used to plugging $x$ into the formula describing a function, but we could also plug in something else. Indeed, we could plug in $\sin(x)$ into the function $g$ and obtain $g(\sin(x))=e^{\sin(x)}$. Since $\sin(x)=h(x)$, we can write this as

$$
 g(h(x))=g(\sin(x))=e^{\sin(x)}=f(x).
$$

As such we notice that for each value of $x$ we have $f(x)=g(h(x))$. We say that $f$ is the **composition** of $g$ with $h$ and we write $f=g\circ h$. We can think of the composition $g\circ h$ as first applying $h$ and then plugging the resulting number into $g$.

Notice that $g\circ h$ is **not** the same as $h\circ g$. Indeed, for any value of $x$ we can compute

$$
 (h\circ g)(x)=h(g(x))=h\left(e^x\right)=\sin\left(e^x\right).
$$

Since $e^{\sin(x)}$ and $\sin\left(e^x\right)$ typically are not equal, the functions $h\circ g$ and $g\circ h$ are not equal.

::::::

We can generalise this concept as follows. 

::::::{prf:definition} 
:label: Def:PropertiesFunctions:Composition

Let $f$ and $g$ be functions. Then the **composition** of $f$ with $g$, denoted by $f\circ g$ (this notation is pronounced as "$f$ after $g$"), is defined by

$$
 (f\circ g)(x)=f(g(x)).
$$

::::::

::::::{warning} 
:name: Warning:PropertiesFunctions:Composition

The compositions $f\circ g$ and $g\circ f$ are typically not the same function. If they are the same, we say that the functions $f$ and $g$ **commute**.
::::::

What can we say about the domain of the composition $f\circ g$? Since $(f\circ g)(x)=f(g(x))$, at the very least we need to be able to compute $g(x)$, since otherwise we could never plug it into $f$. So for $x$ to be in the domain of $f\circ g$, $x$ needs to be in the domain of $g$. We also need to be able to plug $g(x)$ into $f$, so $g(x)$ should be in the domain of $f$. Since these are the only restrictions, the domain of $f\circ g$ consists precisely of those values of $x$ in the domain of $g$ for which $g(x)$ is in the domain of $f$. Notice that this does not mean that $x$ in the domain of $f\circ g$ is also in the domain of $f$: only $g(x)$ needs to be in the domain of $f$. Writing this formally, we have

$$
 D_{f\circ g}=\left\{x\in D_g\,\middle|\,g(x)\in D_f\right\}.
$$

::::{question}
:type: multiple-choice
:variant: single-select
:admonition:
:class: question
:showanswer:
:columns: 1
Let $f$ and $g$ be functions for which $f\circ g$ exists.
Which of the following statements is true?
---
[ ] The range of $f\circ g$ is equal to the range of $f$.
> For $x$ in the domain of $f\circ g$, we have $(f\circ g)(x)=f(g(x))$. Since $g(x)$ is in the domain of $f$, $f(g(x))$ is in the range of $f$. However, not every element in the range of $f$ needs to be reached. For instance, consider $f(x)=x$ and $g(x)=\sqrt{x}$. Then the range of $f$ is $\mathbb{R}$. On the other hand, we have $(f\circ g)(x)=\sqrt{x}$, so the range of $f\circ g$ is $[0,\infty)$.

[x] The range of $f\circ g$ is a subset of the range of $f$, but is not necessarily the same.
> For $x$ in the domain of $f\circ g$, we have $(f\circ g)(x)=f(g(x))$. Since $g(x)$ is in the domain of $f$, $f(g(x))$ is in the range of $f$. However, not every element in the range of $f$ needs to be reached. For instance, consider $f(x)=x$ and $g(x)=\sqrt{x}$. Then the range of $f$ is $\mathbb{R}$. On the other hand, we have $(f\circ g)(x)=\sqrt{x}$, so the range of $f\circ g$ is $[0,\infty)$.
[ ] The range of $f\circ g$ is equal to the range of $g$.
> For $x$ in the domain of $f\circ g$, we have $(f\circ g)(x)=f(g(x))$. Since $g(x)$ is in the domain of $f$, $f(g(x))$ is in the range of $f$ and not necessarily in the range of $g$. For instance consider $f(x)=-x$ and $g(x)=\dfrac{1}{x^2}$. Then for $x\neq 0$ we have $(f\circ g)(x)=-\dfrac{1}{x^2}$. So the range of $g$ is $(0,\infty)$, while the range of $f\circ g$ is $(-\infty,0)$. So in this case, the ranges of $f\circ g$ has no overlap at all with the range of $g$.
[ ] The range of $f\circ g$ is a subset of the range of $g$, but is not necessarily the same.
> For $x$ in the domain of $f\circ g$, we have $(f\circ g)(x)=f(g(x))$. Since $g(x)$ is in the domain of $f$, $f(g(x))$ is in the range of $f$ and not necessarily in the range of $g$. For instance consider $f(x)=-x$ and $g(x)=\dfrac{1}{x^2}$. Then for $x\neq 0$ we have $(f\circ g)(x)=-\dfrac{1}{x^2}$. So the range of $g$ is $(0,\infty)$, while the range of $f\circ g$ is $(-\infty,0)$. So in this case, the ranges of $f\circ g$ has no overlap at all with the range of $g$.
[ ] The range of $f\circ g$ is not necessarily a subset of either of the ranges of $f$ and $g$.
> or $x$ in the domain of $f\circ g$, we have $(f\circ g)(x)=f(g(x))$. Since $g(x)$ is in the domain of $f$, $f(g(x))$ is in the range of $f$. Does it necessarily cover the entire range of $f$?
---
::::

A logical follow-up question could be what happens if we take the composition of three (or even more) functions. So say, we have functions $f$, $g$ and $h$, what do we mean by $f\circ g\circ h$? Since we know what the composition of two functions is, we could try to construct the composition of three function as repeatedly composing two functions, but we run into an issue: there are two logical ways to make this construction. We could either compose $f$ and $g\circ h$, i.e. we could look at $f\circ(g\circ h)$, or, we could compose $f\circ g$ with $h$, i.e. we could look at $(f\circ g)\circ h$. Fortunately, it does not matter which of these we choose, as the resulting function is the same. This important property of composing functions is known as **associativity**.

::::::{prf:theorem} Associativity of function composition
:label: Thm:PropertiesFunctions:Associativity

Let $f$, $g$ and $h$ be three functions. Then we have

$$
 f\circ(g\circ h)=(f\circ g)\circ h.
$$

As a consequence, we write $f\circ g\circ h$, when we mean one of these functions.

::::::

:::{admonition} Proof of {prf:ref}`Thm:PropertiesFunctions:Associativity`
:class: tudproof, dropdown
For any $x$ we have

$$
 (f\circ(g\circ h))(x)=f((g\circ h)(x))=f(g(h(x)))=(f\circ g)(h(x))=((f\circ g)\circ h)(x),
$$

provided this expression exists. In addition, $(f\circ(g\circ h))(x)$ exists precisely when $(g\circ h)(x)=g(h(x))$ exists and is in the domain of $f$, which happens precisely when $x$ is in the domain of $h$, $h(x)$ is in the domain of $g$ and $g(h(x))$ is in the domain of $f$. Following a similar reasoning, this is the same condition as the existence of $((f\circ g)\circ h)(x)$. This means that the functions $f\circ(g\circ h)$ and $(f\circ g)\circ h$ are the same.
:::

In {prf:ref}`Ex:PropertiesFunctions:Sum` we saw that we can obtain the graph of $f+g$ from the graphs of $f$ and $g$ by stacking one on top of the other. For other combinations of functions like the product $fg$ or the composition $f\circ g$, this is usually a bit trickier. However, we can also reverse questions like these. For instance, if we take the graph of a function $f$ and shift every point $1$ to the right we obtain the graph of a different function (indeed, the result of shifting the graph to the right is a curve in $\mathbb{R}^2$ that still passes the vertical line test ({prf:ref}`Thm:Functions1var:VerticalLineTest`)). The main question now is: which function gives this graph? Let us call this new function $g$. Since we obtained the graph of $g$ by shifting the graph of $f$ $1$ to the right, a point $(x,y)$ lies on the graph of $g$ precisely when $(x-1,y)$ lies on the graph of $f$. Since $(x,y)$ lies on the graph of $g$ precisely when $g(x)=y$, while $(x-1,y)$ lies on the graph of $f$ precisely when $f(x-1)=y$, we find that $g(x)=f(x-1)$. We say that we performed a **horizontal shift** of $1$ to the right to obtain $g$ from $f$.

Similarly, we can perform a **vertical shift** of $2$ downwards to the graph of $f$ to obtain the graph of a new function $h$. Since $(x,y)$ is on the graph of $h$ precisely when $(x,y+2)$ on the graph of $f$, we find that $h(x)=f(x)-2$.

We can generalize these considerations as follows.

::::::{prf:theorem} 
:label: Thm:PropertiesFunctions:Shifts

Let $f$ be a function and $a>0$ be a positive real number. Then we can perform to the graph of $f$

- a **horizontal shift to the right** of size $a$ to obtain the graph of the function $g(x)=f(x-a)$;
- a **horizontal shift to the left** of size $a$ to obtain the graph of the function $g(x)=f(x+a)$;
- a **vertical shift upwards** of size $a$ to obtain the graph of the function $g(x)=f(x)+a$;
- a **vertical shift downwards** of size $a$ to obtain the graph of the function $g(x)=f(x)-a$.

::::::

Recall that for a function $f$ and a real number $c$ we defined the scalar multiple function $cf$ by $(cf)(x)$. What is the consequence of applying such a multiplication by a scalar to the graph of the function $f$? For that, we need to make a distinction between the cases where $c>0$, $c=0$ and $c<0$. 

Let us first consider the case $c>0$. In that case, $(x,y)$ is on the graph of $f$ precisely when $(x,cy)$ is on the graph of $cf$. In terms of the graph, this means that the graph of $f$ is stretched in the $y$-direction with a factor $c$ (for $0<c<1$ this stretching is actually more akin to a compression, but we will call it stretching nonetheless). If $c=0$, then $(cf)(x)=0\cdot f(x)=0$ for all $x$, so then the graph is flattened onto the $x$-axis. Finally, we consider the case $c<0$. For convenience, we first let $c=-1$. In that case $(x,y)$ is on the graph of $f$ precisely when $(x,-y)$ is on the graph of $-f$. This means that we obtain the graph of $-f$ by reflecting the graph of $f$ in the $x$-axis. Now if $c<0$ is any negative scalar, then we notice that $c=-|c|$ so that $cf=-(|c|f)$. This means that we obtain the graph of $cf$ by first stretching it in the $y$ direction with a factor $|c|$ and then reflecting it across the $x$-axis.

So going from $f$ to $cf$ corresponds to vertical stretching and/or reflecting. So what would correspond to horizontal stretching and/or reflecting? For this, let us first consider the function $h$ of which the graph is obtained by reflecting the graph of $f$ in the $y$-axis. That means that $(x,y)$ is on the graph of $h$ precisely when $(-x,y)$ is on the graph of $f$. As such, we must have $h(x)=f(-x)$. Similarly, if we obtain $h$ by stretching the graph of $f$ by a factor $c$ (with $c>0$) in the $x$-direction, then $(x,y)$ is on the graph of $f$ precisely when $(cx,y)$ is on the graph of $h$. Hence, we must have $h(cx)=f(x)$, which we can rewrite to $h(x)=f\left(\frac{x}{c}\right)$. Combining these two ideas, gives that for $c<0$ the function $h(x)=f\left(\frac{x}{c}\right)=f\left(-\frac{x}{|c|}\right)$ is obtained by first stretching in the $x$-direction with a factor $|c|$ and then reflecting it across the $y$-axis.

We combine these results as follows.

::::::{prf:theorem} 
:label: Thm:PropertiesFunctions:ReflectionStretching

Let $f$ be a function and $c\neq 0$ a real number. Consider the functions $g(x)=cf(x)$ and $h(x)=f\left(\frac{x}{c}\right)$. Then, if $c>0$,

- the graph of $g$ is obtained from the graph of $f$ by **vertically stretching** it by a factor $c$;
- the graph of $h$ is obtained from the graph of $f$ by **horizontally stretching** it by a factor $c$.

In addition, if $c=-1$,

- the graph of $g(x)=-f(x)$ is obtained from the graph of $f$ by **reflecting** it across the $x$-axis;
- the graph of $h(x)=f(-x)$ is obtained from the graph of $f$ by **reflecting** it across the $y$-axis.

::::::

::::::{prf:example} 
:label: Ex:PropertiesFunctions:ReflectionStretching

Consider the function $f(x)=-3\sin(2x-2)+4$. How is the graph of $f$ related to the graph of the 'basic' sine function? For this, it turns out to be convenient to write

$$
 f(x)=-3\sin(2x-2)+4=-3\sin(2(x-1))+4.
$$

Starting with the graph of the sine function, which is given $y=\sin(x)$, we first perform a horizontal stretching by a factor $\frac{1}{2}$ to obtain the graph given by $y=\sin(2x)$. Then we perform a horizontal shift of $1$ to the right to obtain the graph given by $y=\sin(2(x-1))$. Subsequently, we perform a reflection across the $x$-axis to obtain the graph given by $y=-\sin(2(x-1))$. Then we perform a vertical stretching by a factor $3$ to obtain the graph given by $y=-3\sin(2(x-1))$. Finally, we perform a vertical shift of $4$ upwards to obtain the graph given by $y=-3\sin(2(x-1))+4$, i.e. the graph of $f$.

:::{figure} Images/Fig-PropertiesFunctions-ReflectionStretching.png
:name: Fig:PropertiesFunctions:ReflectionStretching

The five steps to obtain the graph of $f$ from the graph of $\sin(x)$ visualised.
:::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:ReflectionStretching` with an applet.
Current graphs seem incorrect (and one step has been split up in 2). Correct order should be $y=\sin(x)$, $y=\sin(2x)$, $y=\sin(2(x-1))$, $y=-\sin(2(x-1))$, $y=-3\sin(2(x-1))$, $y=-3\sin(2(x-1))+4$.
:::

Notice that if we performed these five operations in a different order, we might obtain a different function (but not necessarily so). Indeed, if we start with the graph given by $y=\sin(x)$ and perform the vertical shift of $4$ upwards first, we obtain the graph given by $y=\sin(x)+4$. If we then perform the reflection in the $x$-axis we obtain the graph $y=-\left(\sin(x)+4\right)=-\sin(x)-4$. From the vertical stretching by a factor $3$ we obtain the graph given by $y=3\left(-\sin(x)-4\right)=-3\sin(x)-12$. If we then perform the horizontal shift of $1$ to the right we obtain the graph given by $y=-3\sin(x-1)-12$. Finally, if we then perform the horizontal stretching by a factor $\frac{1}{2}$ we obtain the graph given by $y=-3\sin(2x-1)-12$. This function is very different from $f$, as can be seen from the graphs shown below.

:::{figure} Images/Fig-PropertiesFunctions-ReflectionStretching2.png
:name: Fig:PropertiesFunctions:ReflectionStretching2

The result of performing the five steps in a different order visualised.
:::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:ReflectionStretching2` with an applet. Graphs no longer match the story. Correct order: $y=\sin(x)+4$, $y=-3\sin(x)-4$, $y=-3\sin(x)-12$, $y=-3\sin(x-1)-12$ and $y=-3\sin(2x-1)-12$.
:::

::::::

(Subsec:PropertiesFunctionsincreasingdecreasing)=

## Increasing and decreasing functions

[^FootnoteNondecr]: Or perhaps it is better to say that a function nonincreases when the graph does not go down, and it nondecreases when the graph does not go up.

When analysing the graph of a function, one of the most eye-catching properties is where the graph goes up and where it goes down. In more mathematical terms, we say that the function nonincreases when the graph goes up and the function nondecreases when the graph goes down. [^FootnoteNondecr]

::::::{prf:definition} 
:label: Def:PropertiesFunctions:increasingdecreasing

Let $f$ be a function and $I\subset D_f$ be an interval. Then we say that $f$ is **nondecreasing** on $I$ whenever for each two points $x_1<x_2$ in $I$ we have $f(x_1)\leq f(x_2)$. Similarly, we say that $f$ is **nonincreasing** on the interval $I$ whenever for each two points $x_1<x_2$ in $I$ we have $f(x_1)\geq f(x_2)$.

A function that is either nondecreasing or nonincreasing on an interval, is called **monotonic** on that interval.
::::::

::::::{prf:example} 
:label: Ex:PropertiesFunctions:increasingdecreasing


A function can be nondecreasing on some parts on its domain, while it is nonincreasing on other parts of its domain. For instance, consider the function $f(x)=x^2$, of which the graph is shown below.

:::{figure} Images/Fig-PropertiesFunctions-increasingdecreasing.png
:name: Fig:PropertiesFunctions:increasingdecreasing

The graph of the function $f(x)=x^2$.
:::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:increasingdecreasing` with an applet.
:::

The graph suggests that the function nondecreases on the interval $(0,\infty)$. Indeed, if we have $0<x_1<x_2$ then we have $f(x_1)=x_1^2<x_2^2=f(x_2)$. 

Similarly, on the interval $(-\infty,0)$ the function is nonincreasing. Indeed, if we have $x_1<x_2<0$ then we have $0<-x_2<-x_1$, so we obtain $f(x_1)=x_1^2=(-x_1)^2> (-x_2)^2=x_2^2=f(x_2)$.

However, on the interval $(-2,2)$ the function is neither nondecreasing, nor nonincreasing. Indeed, we have $-1$ and $0$ are numbers in this interval with $-1<0$ and we have $f(-1)=1>0=f(0)$, so $f$ is not nondecreasing on this interval. On the other hand, $0$ and $1$ are also numbers in this interval which have $0<1$ and $f(0)=0<1=f(1)$, so $f$ is not nonincreasing on this interval.

::::::

::::::{prf:example} 
:label: Ex:PropertiesFunctions:increasingdecreasingFlat

Consider the piecewise defined function

$$
k(t)=\left\{\begin{array}{ll}t-3,\quad&\text{if }t<0,\\ 2,\quad&\text{if }0\leq t\leq 1,\\ t+4,\quad&\text{if }t>1.\end{array}\right.
$$

The graph of this function is shown below.

:::{figure} Images/Fig-PropertiesFunctions-increasingdecreasingFlat.png
:name: Fig:PropertiesFunctions:increasingdecreasingFlat

The graph of the function $k$.
:::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:increasingdecreasingFlat` with an applet.
:::

From the graph of the function, we see that the function is definitely nondecreasing on the intervals $(-\infty,0)$ and $(1,\infty)$, but what about the interval $[0,1]$? The graph of the function is horizontal there, so it does not seem to "grow" on this interval. Still, according to the definition that we used, the function is nondecreasing on this interval. Indeed, for any $0<t_1<t_2<1$ we have $k(t_1)=2\leq 2=k(t_2)$. We conclude that the function is indeed nondecreasing on this interval. Moreover, it is also nonincreasing on the same interval as for any $0<t_1<t_2<1$ we have $k(t_1)=2\geq 2=k(t_2)$. In general, a function is both nondecreasing and nonincreasing on a certain interval precisely when it is constant on that interval.

In fact, the function is nondecreasing on its entire domain. Indeed, we already know that it is nondecreasing on each of the intervals $(-\infty,0)$, $[0,1]$ and $(1,\infty)$. So we only need to consider what happens if we have two values of $t$ that are in different intervals. First consider $t_1$ in $(-\infty,0)$ and $t_2$ in $[0,1]$. Then $t_1<0$, so $k(t_1)=t-3\leq -3<2=k(t_2)$. Similarly if $t_1$ is in $[0,1]$ and $t_2$ is in $(1,\infty)$ then $t_2>1$, so we find $k(t_2)=t+4>5>2=k(t_1)$. Finally, if $t_1$ is in $(-\infty,0)$ and $t_2$ is in $(1,\infty)$, then $t_1<t_2$, so we must have $k(t_1)=t_1-3<t_2-3<t_2+4=k(t_2)$. We find that $k$ is nondecreasing on its entire domain.

::::::

In {prf:ref}`Ex:PropertiesFunctions:increasingdecreasingFlat` we saw that a constant function is both nondecreasing and nonincreasing. Sometimes, we want to specifically look at functions that actually grow or decay. For this, we adopt some new terminology.

::::::{prf:definition} 
:label: Def:PropertiesFunctions:Strictlyincreasingdecreasing

Let $f$ be a function and $I\subset D_f$ be an interval. Then we say that $f$ is **strictly increasing** on $I$ if for each two points $x_1<x_2$ in $I$ we have $f(x_1)< f(x_2)$. 

Similarly, we say that $f$ is **strictly decreasing** on $I$ if for each two points $x_1<x_2$ in $I$ we have $f(x_1)> f(x_2)$.

A function that is either strictly increasing or strictly decreasing on an interval, is called **strictly monotonic** on that interval.
::::::

In particular, constant functions are nondecreasing and nonincreasing, but neither strictly increasing nor strictly decreasing.

::::::{warning} 
:name: Warning:PropertiesFunctions:Strictlyincreasingdecreasing

In some literature, the terminology increasing and decreasing is used for what we call strictly increasing and strictly decreasing (so in those texts, constant functions are neither increasing nor decreasing). In other literature, the terminology increasing and decreasing is used for what we call nondecreasing and nonincreasing. This makes the terms increasing and decreasing ambiguous, and we will not use these terms. Be aware of this when you read other literature.
::::::

Showing that a function is nondecreasing or nonincreasing can be tricky in practice. In {numref}`Section:GraphsDerivatives` we will learn an efficient way to determine this. For future reference, we already show that exponential functions are either always strictly increasing or always strictly decreasing or constant.

::::::{prf:theorem} 
:label: Thm:PropertiesFunctions:Expnondecreasenonincrease

Let $a>0$ and consider the exponential function $f(x)=a^x$. If $0<a<1$, the function $f$ is strictly decreasing on $\mathbb{R}$. If $a>1$, the function $f$ is strictly increasing on $\mathbb{R}$. If $a=1$, the function $f$ is constant, and, therefore, both nondecreasing and nonincreasing on $\mathbb{R}$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:PropertiesFunctions:Expnondecreasenonincrease`
:class: tudproof
This follows directly from {prf:ref}`Thm:RealNumbers:ExpCalcReal`.
:::

Similarly, we can show that power functions are always strictly increasing or always strictly decreasing or constant on the interval $(0,\infty)$.

::::::{prf:theorem} 
:label: Thm:PropertiesFunctions:Powernondecreasenonincrease

Let $r$ in $\mathbb{R}$ and consider the power function $f(x)=x^r$. If $r>0$, the function $f$ is strictly increasing on $[0,\infty)$. Moreover, if $r=\dfrac{p}{q}$ for integers $p>0$ and $q>0$ with $q$ odd, then $f$ is strictly increasing on $\mathbb{R}$. If $r<0$, the function $f$ is strictly decreasing on $(0,\infty)$. If $r=1$, the function $f$ is constant, and, therefore, both nondecreasing and nonincreasing on $\mathbb{R}$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:PropertiesFunctions:Powernondecreasenonincrease`
:class: tudproof
This follows directly from {prf:ref}`Thm:RealNumbers:ExpCalcReal`.
:::

::::::{prf:example} 
:label: Ex:PropertiesFunctions:Expnondecreasenonincrease

Consider the function $f(x)=e^{-\sqrt{x}}$. We will show that it is strictly decreasing on $[0,\infty)$. For this, we let $x_1<x_2$ in $[0,\infty)$. Then we obtain

$$
 \sqrt{x_1}<\sqrt{x_2}.
$$

Multiplying this equation by $-1$ flips the inequality sign and we obtain

$$
 -\sqrt{x_1}>-\sqrt{x_2}.
$$

Since the exponential function is strictly increasing by {prf:ref}`Thm:PropertiesFunctions:Expnondecreasenonincrease`, we obtain

$$
 f\left(x_1\right)=e^{-\sqrt{x_1}}>e^{-\sqrt{x_2}}=f\left(x_2\right).
$$

This shows that the function $f$ is strictly decreasing on $[0,\infty)$.

:::{todo}
Make an applet with the graph of $f$.
:::
::::::

(Subsec:PropertiesFunctionsEvenOdd)=
## Even and odd functions

The graph of a function can possess many different symmetries. In this section, we consider the two most important ones.

First, let $f$ be a function of which the graph is symmetric with respect to the $y$-axis. That is, a point $(x,y)$ lies on the graph of $f$ precisely when $(-x,y)$ lies on the graph of $f$. Since $(x,y)$ lies on the graph of $f$ precisely when $f(x)=y$, we find that we must have $f(-x)=f(x)$ for each $x$ in the domain of $f$. As we saw in {prf:ref}`Ex:Functions1var:CubicAndHigher` functions of the form $f(x)=x^n$ with $n$ even have this property. Indeed, for such a function we have

$$
 f(-x)=(-x)^n=(-1)^nx^n=1\cdot x^n=x^n=f(x).
$$

As such, we will call such a function **even**. Other examples of even functions include $f(x)=|x|$ and $f(x)=\cos(x)$. 

In the same example, we saw that functions of the form $f(x)=x^n$ with $n$ odd also possess a certain symmetry. Indeed, for such a function we have

$$
 f(-x)=(-x)^n=(-1)^nx^n=(-1)\cdot x^n=-x^n=-f(x).
$$

So we find that for these functions the point $(x,y)$ lies on the graph of $f$ precisely when $(-x,-y)$ lies on the graph of $f$. This means that the graph of the function is point symmetric with resepect to the origin. Such a function will be called **odd**. Other examples of odd functions include $f(x)=\sin(x)$ and $f(x)=\tan(x)$ (the latter only when restricted to the interval $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$).

::::::{prf:definition} 
:label: Def:PropertiesFunctions:EvenOdd

Let $f$ be a function and $I$ an interval. Then $f$ is called **even** on $I$ if for all $x$ in $I$ with $x\geq 0$ we have $-x$ in $I$ and $f(-x)=f(x)$. In addition, $f$ is called **odd** on $I$ if for all $x$ in $I$ with $x\geq 0$ we have $-x$ in $I$ and $f(-x)=-f(x)$.

::::::

:::{note}
A function can only be even and/or odd on an interval that is symmetric with respect to $0$.
:::

::::{figure} Images/Fig-PropertiesFunctions-Even.png
:name: Fig:PropertiesFunctions:Even
:class: dark-light

The graph of an even function is symmetric with respect to the $y$-axis.

::::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:Even` with an applet.
:::

::::{figure} Images/Fig-PropertiesFunctions-Odd.png
:name: Fig:PropertiesFunctions:Odd
:class: dark-light

The graph of an odd function is point symmetric with respect to the origin.

::::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:Odd` with an applet.
:::

::::{question}
:type: multiple-choice
:variant: multiple-select
:admonition:
:class: question
:showanswer:
:columns: 1
Let $f$ be even on $[-1,1]$ and $g$ be odd on $[-1,1]$.
Select all statements that are true.
---
[ ] We must have $f(0)=0$.
> The defining property of even functions gives that $f(-0)=f(0)$ which is true no matter what the value of $f(0)$ is.

[x] We must have $g(0)=0$.
> The defining property of odd functions gives that $g(-0)=-g(0)$. Since $g(-0)=g(0)$ this means that $g(0)=-g(0)$. The only real number which is minus itself is $0$, so we must have $g(0)=0$.
---
::::

::::::{prf:example} 
:label: Ex:PropertiesFunctions:EvenOdd

Consider the function $f(x)=|x|\sin(x)$. Then for any $x$ we have

$$
 f(-x)=|-x|\sin(-x)=|x|\sin(-x)=|x|\left(-\sin(x)\right)=-|x|\sin(x)=-f(x).
$$

As such, the function $f$ is odd. Note that $f=gh$ with $g(x)=|x|$ and $h(x)=\sin(x)$. By inspecting the computation above, you can see that $g(-x)=g(x)$ and $h(-x)=-h(x)$. So $g$ is even, while $h$ is odd. It is true, in general, that the product of an even and an odd function is odd again. You could make a list of whether a sum or product of any combination of even and odd functions is even again, but in practice, it is usually quicker to just plug $-x$ into your function and see where you end up.

:::{figure} Images/Fig-PropertiesFunctions-EvenOdd.png
:name: Fig:PropertiesFunctions:EvenOdd

The graph of the function $f(x)=|x|\sin(x)$. Note that the graph is symmetric in the origin, which is a consequence of the fact that $f$ is odd.
:::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:EvenOdd` with an applet.
:::

::::::

::::{question}
:type: multiple-choice
:variant: multiple-select
:admonition:
:class: question
:showanswer:
:columns: 1
Let $f$ be even on $\mathbb{R}$ and $g$ be odd on $\mathbb{R}$.
Select all statements that are true.
---
[ ] $fg$ is even on $\mathbb{R}$.
> For $x\geq 0$ we have

$$
 (fg)(-x)=f(-x)g(-x)=f(x)\left(-g(x)\right)=-f(x)g(x)=-(fg)(x).
$$

This means that in most cases $fg$ is not even on $\mathbb{R}$.

[x] $fg$ is odd on $\mathbb{R}$.
> For $x\geq 0$ we have

$$
 (fg)(-x)=f(-x)g(-x)=f(x)\left(-g(x)\right)=-f(x)g(x)=-(fg)(x).
$$

This means that $fg$ is odd on $\mathbb{R}$.

[x] $f\circ g$ is even on $\mathbb{R}$.
> For $x\geq 0$ we have

$$
 (f\circ g)(-x)=f(g(-x))=f(-g(x))=f(g(x))=(f\circ g)(x).
$$

This means that $f\circ g$ is even on $\mathbb{R}$.

[ ] $f\circ g$ is odd on $\mathbb{R}$.
> For $x\geq 0$ we have

$$
 (f\circ g)(-x)=f(g(-x))=f(-g(x))=f(g(x))=(f\circ g)(x).
$$

This means that in most cases $f\circ g$ is not odd on $\mathbb{R}$.

[x] $g\circ f$ is even on $\mathbb{R}$.
> For $x\geq 0$ we have

$$
 (g\circ f)(-x)=g(f(-x))=g(f(x))=(g\circ f)(x).
$$

This means that $g\circ f$ is even on $\mathbb{R}$.

[ ] $g\circ f$ is odd on $\mathbb{R}$.
> For $x\geq 0$ we have

$$
 (g\circ f)(-x)=g(f(-x))=g(f(x))=(g\circ f)(x).
$$

This means that in most cases $g\circ f$ is not odd on $\mathbb{R}$.
---
::::

::::::{prf:example} 
:label: Ex:PropertiesFunctions:NotEvenOdd

Consider the function $f(x)=x^2+x$. Then $f=g+h$ with $g(x)=x^2$ and $h(x)=x$, so $f$ is the sum of an even and an odd function. However, $f$ itself is neither even nor odd. Indeed, for any $x$ we have

$$
 f(-x)=(-x)^2+(-x)=x^2-x
$$

and this is not (necessarily) equal to $f(x)$ or to $-f(x)$. Indeed, we find $f(2)=6$, while $f(-2)=2$ which is neither $f(2)$ nor $-f(2)$. So in general, the sum of an even and an odd function will be neither even nor odd, though exceptions exist. Can you come up with one?

:::{figure} Images/Fig-PropertiesFunctions-NotEvenOdd.png
:name: Fig:PropertiesFunctions:NotEvenOdd

The graph of the function $f(x)=x^2+x$. Note that the graph is not symmetric with respect to the $y$-axis, nor is it point symmetric with respect to the origin, which is a consequence of the fact that $f$ is neither even nor odd.
:::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:NotEvenOdd` with an applet.
:::

::::::

If a function is only defined on an interval of the form $(0,a)$ it is possible to extend it to a function that is even or odd on the symmetric interval $(-a,a)$. This is an important concept when studying Fourier sine and cosine series, see {numref}`Section:Fourier`.

::::::{prf:theorem} Odd and even extensions
:label: Thm:PropertiesFunctions:EvenOddExtension
Let $a>0$ or $a=\infty$ and let $f$ be a function that is defined on the interval $(0,a)$. Then the function 

$$
 f_{\mathrm{odd}}(x)=\left\{\begin{array}{l}f(x),\quad&\mathrm{if}\,x\in(0,a)\\ 0,\quad &\mathrm{if}\,x=0\\ -f(-x),\quad&\mathrm{if}\,x\in(-a,0)\end{array}\right.
$$

is odd on $(-a,a)$. It is called the **odd extension of $f$** to $(-a,a)$.

Similarly, if $f$ is defined on the interval $[0,a)$, then the function 

$$
 f_{\mathrm{even}}(x)=\left\{\begin{array}{l}f(x),\quad&\mathrm{if}\,x\in[0,a)\\  f(-x),\quad&\mathrm{if}\,x\in(-a,0)\end{array}\right.
$$

is even on $(-a,a)$. It is called the **even extension of $f$** to $(-a,a)$..
::::::

:::{admonition} Proof of {prf:ref}`Thm:PropertiesFunctions:EvenOddExtension`
:class: tudproof, dropdown
For $x\in(0,a)$ we have $-x\in(-a,0)$ so we have

$$
 f_{\mathrm{odd}}(-x)=-f_{\mathrm{odd}}(-(-x))=-f_{\mathrm{odd}}(x)
$$

and

$$
 f_{\mathrm{even}}(-x)=f_{\mathrm{even}}(-(-x))=f_{\mathrm{even}}(x).
$$ 

Finally, for $x=0$, we have $f_{\mathrm{odd}}(0)=0=-f_{\mathrm{odd}}(-0)$. This means that $f_{\mathrm{odd}}$ is odd on $(-a,a)$ and $f_{\mathrm{even}}$ is even on $(-a,a)$.
:::


:::{todo}
Make an applet that allows students to either draw a graph on $\mathbb{R}^2$ with $x>0$ and sketch the even and odd extensions, or plug in a formula and draw the graphs of the even and odd extensions.
:::

Sometimes, it turns out to be convenient to write a function as the sum of an even and an odd function. The following theorem shows how we can construct these new functions.

::::::{prf:theorem} Even and odd parts
:label: Thm:PropertiesFunctions:EvenOddParts

Let $f$ be a function that is defined on a symmetric interval of the form $(-a,a)$ for some $a>0$. On this interval, $f$ can uniquely be written as $f=f_e+f_o$ with $f_e$ an even function and $f_o$ an odd function. The function $f_e$ is called the **even part** of $f$ and is given by $f_e(x)=\frac{f(x)+f(-x)}{2}$, while the function $f_o$ is called the **odd part** of $f$ and is given by $f_o(x)=\frac{f(x)-f(-x)}{2}$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:PropertiesFunctions:EvenOddParts`
:class: tudproof, dropdown
We consider the functions given by $f_e(x)=\frac{f(x)+f(-x)}{2}$ and $f_o(x)=\frac{f(x)-f(-x)}{2}$. We first note that for any $x$ we have

$$
 f_e(-x)=\frac{f(-x)+f(-(-x))}{2}=\frac{f(-x)+f(x)}{2}=f_e(x),
$$

while

$$
 f_o(-x)=\frac{f(-x)-f(-(-x))}{2}=\frac{f(-x)-f(x)}{2}=-\frac{f(x)-f(-x)}{2}=-f_o(x).
$$

Moreover, we find that

\begin{align*}
 f_e(x)+f_o(x) &= \frac{f(x)+f(-x)}{2}+\frac{f(x)-f(-x)}{2} \\
 &= \frac{f(x)+f(-x)+f(x)-f(-x)}{2} \\
 &= \frac{2f(x)}{2} \\
 &= f(x).
\end{align*}

So we obtain that $f=f_e+f_o$ and that $f_e$ is even and $f_o$ is odd.

Now we show that this decomposition is unique, so we write $f=g+h$ with $g$ even and $h$ odd and aim to show that $g=f_e$ and $h=f_o$. Then we find

\begin{align*}
2f_e(x) &= f(x)+f(-x) \\
&= \left(g(x)+h(x)\right)+\left(g(-x)+h(-x)\right) \\
&= \left(g(x)+h(x)\right)+\left(g(x)-h(x)\right) \\
&= 2g(x)
\end{align*}
and

\begin{align*}
 2f_o(x) &= f(x)-f(-x) \\
 &= \left(g(x)+h(x)\right)-\left(g(-x)+h(-x)\right) \\
 &= \left(g(x)+h(x)\right)-\left(g(x)-h(x)\right) \\
 &= 2h(x).
\end{align*}

Hence, we must have $g=f_e$ and $h=f_o$, as desired.
:::

:::{todo}
Make applet that lets student enter a function and it plots the function and the even and odd parts.
:::

The even and odd parts of the exponential function are so common that they have their own names.

::::::{prf:definition} 
:label: Def:PropertiesFunctions:Hyperbolic


The **hyperbolic cosine function**, denoted by $\cosh$, is the even part of the exponential function. That is, we have $\cosh(x)=\frac{e^x+e^{-x}}{2}$.

The **hyperbolic sine function**, denoted by $\sinh$, is the odd part of the exponential function. That is, we have $\sinh(x)=\frac{e^x-e^{-x}}{2}$.

Finally, the **hyperbolic tangent function** is defined by $\tanh(x)=\dfrac{\sinh(x)}{\cosh(x)}$.

::::::

:::{figure} Images/Fig-PropertiesFunctions-Hyperbolic.png
:name: Fig:PropertiesFunctions:Hyperbolic

The graphs of the hyperbolic cosine, sine and tangent functions.
:::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:Hyperbolic` with an applet.
:::

::::::{prf:notation} Powers of hyperbolic functions
:label: Not:PropertiesFunctions:Hyperbolic

$$
\cosh^n(x)=(\cosh(x))^n,
$$

$$
\sinh^n(x)=(\sinh(x))^n,
$$

$$
\tanh^n(x)=(\tanh(x))^n.
$$

::::::

The naming of these functions suggests some sort of connection to the trigonometric functions. Indeed, the hyperbolic sine and cosine have an interpretation similar to the regular sine and cosine when using [hyperbolic angles](https://en.wikipedia.org/wiki/Hyperbolic_angle) instead of regular angles. They can also be used to parameterise a hyperbola, see {numref}`Subsec:CurvesHyperbola`. Moreover, the derivatives (see {numref}`Chapter:Differentiation`) of the hyperbolic functions follow a similar, though slightly different, pattern to those of the trigonometric functions. Finally, the sine and the hyperbolic sine, the tangent and the hyperbolic tangent are all odd functions (the regular tangent only on $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$), while the cosine and the hyperbolic cosine are both even functions.

::::::{prf:theorem} 
:label: Thm:PropertiesFunctions:HyperbolicProperties

- The function $\cosh(x)$ is even, while the functions $\sinh(x)$ and $\tanh(x)$ are odd. 
- The function $\cosh(x)$ is strictly decreasing on the interval $(-\infty,0)$ and strictly increasing on the interval $(0,\infty)$.
- The functions $\sinh(x)$ and $\tanh(x)$ are strictly increasing on $\mathbb{R}$.
- For any $x$ we have $\cosh^2(x)-\sinh^2(x)=1$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:PropertiesFunctions:HyperbolicProperties`
:class: tudproof, dropdown
That the hyperbolic cosine is even and the hyperbolic sine is even follows directly from their definitions as the even and odd parts respectively of the exponential function. As such, for any $x$ we have

$$
 \tanh(-x)=\frac{\cosh(-x)}{\sinh(-x)}=\frac{\cosh(x)}{-\sinh(x)}=-\tanh(x),
$$

which means that the hyperbolic tangent is odd.

We cannot prove yet on which intervals the hyperbolic cosine and hyperbolic tangent are nondecreasing and nonincreasing. This we will do in {numref}`Section:GraphsDerivatives`.

By {prf:ref}`Thm:PropertiesFunctions:Expnondecreasenonincrease`, the function $x\mapsto e^x$ is strictly increasing on $\mathbb{R}$, while $x\mapsto e^{-x}=\left(\frac{1}{e}\right)^{x}$ is strictly decreasing on $\mathbb{R}$. Moreover, $e^{-x}>0$ for all $x$, so the function $x\mapsto -e^{-x}$ must be strictly increasing on $\mathbb{R}$. As such, the function $\sinh(x)=\frac{1}{2}e^{x}+\frac{1}{2}\left(-e^{-x}\right)$ is the sum of two strictly increasing functions, which means that it must be strictly increasing itself. 

The final property follows from the definition of the hyperbolic cosine and sine functions, which gives that

\begin{align*}
 \cosh^2(x)-\sinh^2(x) &= \left(\frac{e^x+e^{-x}}{2}\right)^2-\left(\frac{e^x-e^{-x}}{2}\right)^2 \\
 &= \frac{e^{2x}+2+e^{-2x}}{4}-\frac{e^{2x}-2+e^{-2x}}{4} \\
 &= \frac{4}{4} \\
 &= 1.
\end{align*}

:::



(Subsec:PropertiesFunctionsPeriodic)=
## Periodic functions

In {prf:ref}`Ex:Functions1var:Trigonometry` we saw that the trigonometric functions $\cos(\theta)$, $\sin(\theta)$ and $\tan(\theta)$ show periodic behaviour: the cosine and sine repeat themselves after every cycle of length $2\pi$, while the tangent repeats itself after every cycle of length $\pi$. We can denote this by writing, for instance, $\cos(\theta+2\pi)=\cos(\theta)$ for each value of $\theta$. 

::::::{prf:definition} 
:label: Def:PropertiesFunctions:Periodic

A function $f$ is **periodic** if there exists a $T>0$ such that $f(x+T)=f(x)$ for all $x$. $T$ is called a **period** of the function $f$. If there is a smallest value of $T$ with this property, it is called the **fundamental period** of $f$.

::::::

::::{figure} Images/Fig-PropertiesFunctions-Periodic.png
:name: Fig:PropertiesFunctions:Periodic
:class: dark-light

The graph of function with fundamental period $T$.

::::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:Periodic` with an applet.
:::

Periodic functions play an important role in many fields of science and engineering, for instance in signal processing and astronomy. In addition, periodic functions are precisely the functions that can be described by a Fourier series, see {numref}`Section:Fourier`.

Notice that if $T$ is a period of a periodic function $f$, then any number of the form $nT$ with $n\geq 1$ a nonzero natural number is again a period of $f$. For instance, for $n=3$ we have for all $x$ that

$$
 f(x+3T)=f((x+2T)+T)=f(x+2T)=f((x+T)+T)=f(x+T)=f(x).
$$

In fact, any other period of a periodic function must be an integer multiple of the fundamental period.

::::::{prf:theorem} 
:label: Thm:PropertiesFunctions:Fundperiod

Let $f$ be a periodic function which has a fundamental period $T_0$. If $T$ is a period of $f$, then $T=nT_0$ for some integer $n\geq 1$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:PropertiesFunctions:Fundperiod`
:class: tudproof
Since $T_0$ is the fundamental period, we must have $T\geq T_0$. Using long division we can write $T=nT_0+r$ for some integer $n\geq 1$ and some $0\leq r<T_0$. Then we have for any $x$

$$
 f(x+r)=f(x+T-nT_0)=f(x-nT_0)=f(x),
$$

where the second equality sign follows since $T$ is a period of $f$ and the third one since $nT_0$ is a period of $f$. This means that either $r=0$ or that $r$ is a period of $f$. Since $r<T_0$ and $T_0$ is the fundamental period of $f$ the latter is impossible, so we must have $r=0$. As such, we obtain $T=nT_0$, as desired.
:::

As a small technicality: not all periodic functions have a fundamental period. For instance, a constant function $f(x)=c$ is periodic and any number $T>0$ is a period. Indeed, for any $T>0$ and any $x$ we have

$$
 f(x+T)=c=f(x).
$$

As such, the constant function does not have a smallest positive period (in more mathematical terms: the infimum of the set of all periods of $f$ is $0$). In practice, however, most periodic functions you will encounter will have a definable fundamental period.

::::::{prf:theorem} 
:label: Thm:PropertiesFunctions:TrigPeriodic

The functions $f(x)=\cos(x)$, $g(x)=\sin(x)$ and $h(x)=\tan(x)$ are all periodic. The fundamental period of $f$ and $g$ is $2\pi$, while the fundamental period of $h$ is $\pi$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:PropertiesFunctions:TrigPeriodic`
:class: tudproof
This follows directly from {prf:ref}`Thm:Trigonometry:Periodicity`.
:::

::::::{prf:example} 
:label: Ex:PropertiesFunctions:PeriodicCombining

Consider the functions $f(x)=\cos(4x)$, $g(x)=\sin(6x)$ and $h(x)=(f+g)(x)=\cos(4x)+\sin(6x)$. The graphs of these functions are shown below.

:::{figure} Images/Fig-PropertiesFunctions-PeriodicCombining.png
:name: Fig:PropertiesFunctions:PeriodicCombining

The graph of the functions $f(x)=\cos(4x)$, $g(x)=\sin(6x)$ and $h(x)=(f+g)(x)=\cos(4x)+\sin(6x)$.
:::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:PeriodicCombining` with an applet.
:::

As we can see in the graph, all of these functions are periodic. Since the sine and cosine have fundamental period $2\pi$, we might expect these functions to have this period as well. So let us find out if that is indeed the case. For any $x$ we can compute

$$
 f(x+2\pi)=\cos(4(x+2\pi))=\cos(4x+8\pi)=\cos(4x)=f(x)
$$

and

$$
 g(x+2\pi)=\sin(6(x+2\pi))=\sin(6x+12\pi)=\sin(6x)=g(x).
$$

Here we used that any integer multiple of a period is also a period. Finally, we also note that

$$
 h(x+2\pi)=f(x+2\pi)+g(x+2\pi)=f(x)+g(x)=h(x).
$$

So indeed, all of the functions $f$, $g$ and $h$ are periodic with period $2\pi$. However, if we look back at the graphs of these functions, their fundamental periods seem to be smaller. From {prf:ref}`Thm:PropertiesFunctions:ReflectionStretching` we obtain that the graph of $f$ is obtained from the graph of the regular cosine by stretching it by a factor $\frac{1}{4}$, i.e. compressing it by a factor $4$, in the horizontal direction. Since the regular cosine repeats itself after $2\pi$, $f$ must already do so after $\frac{2\pi}{4}=\frac{\pi}{2}$. Indeed, for any $x$ we have

$$
 f\left(x+\frac{\pi}{2}\right)=\cos\left(4\left(x+\frac{\pi}{2}\right)\right)=\cos(4x+2\pi)=\cos(4x).
$$

So the fundamental period of $f$ is actually $\frac{\pi}{2}$. Similarly, the fundamental period of $g$ is $\frac{2\pi}{6}=\frac{\pi}{3}$. So what is the fundamental period of $h=f+g$? For this, we notice that $h$ has completed a full period whenever $f$ and $g$ have completed a whole number of periods at the same time. Since the fundamental periods of $f$ and $g$ are $\frac{\pi}{2}$ and $\frac{\pi}{3}$ respectively, this happens the first time after a period of $T=\pi$ (when $f$ has completed $2$ periods and $g$ has completed $3$ periods). So the fundamental period of $h$ is $\pi$.
::::::

::::::{prf:example} 
:label: Ex:PropertiesFunctions:PeriodicCombining2

Consider the functions $f(x)=\cos(2x)$, $g(x)=\sin(\pi x)$ and $h(x)=(f+g)(x)=\cos(2x)+\sin(\pi x)$. The graph of these functions is shown below.

:::{figure} Images/Fig-PropertiesFunctions-PeriodicCombining2.png
:name: Fig:PropertiesFunctions:PeriodicCombining2

The graph of the functions $f(x)=\cos(2x)$, $g(x)=\sin(\pi x)$ and $h(x)=(f+g)(x)=\cos(2x)+\sin(\pi x)$.
:::

:::{todo}
Replace {numref}`Fig:PropertiesFunctions:PeriodicCombining2` with an applet.
:::

Following a similar reasoning to {prf:ref}`Ex:PropertiesFunctions:PeriodicCombining` the functions $f$ and $g$ are periodic with fundamental periods $\frac{2\pi}{2}=\pi$ and $\frac{2\pi}{\pi}=2$ respectively. So is the function $h$ periodic here as well and if so, what is its period? In order for $h$ to complete a full period, $f$ and $g$ would need to complete a number of periods at the same time. So a period $T$ of $h$ should be of the form $T=2m+\pi n$ for some integers $m,n\geq 1$. However, since $\pi$ is irrational, no such numbers $m$ and $n$ exist (otherwise, we would be able to write $\pi$ as a fraction). As such, the function $h$ is not periodic in this case. This can also be seen from the graph of $h$.
::::::

We summarize the observations about the periodicity of the sum of periodic function from the preceding examples in the following result.

::::::{prf:theorem}
:label: Thm:PropertiesFunctions:Sumperiodic
Let $f$ and $g$ be periodic functions with periods $T_1$ and $T_2$ respectively. If $\dfrac{T_1}{T_2}$ is a rational number, i.e. if there are nonzero positive integers $p$ and $q$ with $pT_1=qT_2$, the sum function $f+g$ is periodic with period $T=pT_1=qT_2$.  
::::::

:::{admonition} Proof of {prf:ref}`Thm:PropertiesFunctions:Sumperiodic`
:class: tudproof, dropdown
Suppose that $T=pT_1=qT_2$. Then $pT_1$ is a period of $f$ and $qT_2$ is a period of $g$, so for any $x$ we have

$$
 (f+g)(x+T)=f(x+T)+g(x+T)=f(x+pT_1)+g(x+qT_2)=f(x)+g(x)=(f+g)(x).
$$

So $f+g$ is periodic with period $T$.



:::

::::{note}
It might be tempting to think that {prf:ref}`Thm:PropertiesFunctions:Sumperiodic` also works the other way around in the sense that the quotient of the fundamental periods of two period functions being irrational would mean that the sum function is not periodic, but this is not the case in general. However, counterexamples are way beyond the scope of this book. If you are interested, you can find a counterexample in [this article](https://www.jstor.org/stable/2690095?seq=2).
::::




If a function is only defined on an interval of the form $[a,b)$ it is possible to extend it to a function that is periodic. This is an important concept when studying Fourier series, see {numref}`Section:Fourier`, especially when combining it with the even and odd extensions from {prf:ref}`Thm:PropertiesFunctions:EvenOddExtension`.

::::::{prf:theorem} Periodic extension
:label: Thm:PropertiesFunctions:PeriodicExtension
Let $a<b$, let $f$ be a function that is defined on $[a,b)$ and write $\ell=b-a$. Then the function 

$$
 f_{\mathrm{ext}}(x+n\ell)=f(x)
$$

for $x$ in $[a,b)$ and an integer $n$ is a periodic function with period $\ell$. It is called the **periodic extension of $f$**.
::::::

:::{admonition} Proof of {prf:ref}`Thm:PropertiesFunctions:PeriodicExtension`
:class: tudproof, dropdown
This follows directly from the construction of the periodic extension.
:::

::::::{prf:example} 
:label: Ex:PropertiesFunctions:PeriodicCombining3
Consider the functions 

$$
 f(x)=\left\{\begin{array}{l}1,\quad&\mathrm{if}\,0\leq x<1\\ 0,\quad &\mathrm{if}\,1\leq x<4\end{array}\right.,\qquad g(x)=\left\{\begin{array}{l}1,\quad&\mathrm{if}\,2\leq x<3\\ 0,\quad &\mathrm{if}\,3\leq x<6\end{array}\right.
$$

and let $f_{\mathrm{ext}}$ and $g_{\mathrm{ext}}$ denote their periodic extensions. Then both $f_{\mathrm{ext}}$ and $g_{\mathrm{ext}}$ have fundamental period. According to {prf:ref}`Thm:PropertiesFunctions:Sumperiodic`, $f_{\mathrm{ext}}+g_{\mathrm{ext}}$ is periodic with period $4$. It is very tempting to think that the fundamental period of $f+g$ is also $4$, but this is not the case. Indeed, we note that $(f_{\mathrm{ext}}+g_{\mathrm{ext}})(x)=1$ for $x$ in intervals of the form $[n,n+1)$ with $n$ even (since $f_{\mathrm{ext}}$ is $1$ and $g_{\mathrm{ext}}$ is $0$ on this interval if $n$ is divisible by $4$ and the other way around if $n$ is not divisible by $4$), while $(f_{\mathrm{ext}}+g_{\mathrm{ext}})(x)=0$ for $x$ in intervals of the form $[n,n+1)$ with $n$ odd (since $f_{\mathrm{ext}}$ and $g_{\mathrm{ext}}$ are both $0$ on these intervals). As such, we see that $f_{\mathrm{ext}}+g_{\mathrm{ext}}$ has fundamental period $2$. This example shows that there is no general way to find the fundamental period of the sum of two periodic functions.
::::::

::::::{prf:definition} Odd and even periodic extensions
:label: Def:PropertiesFunctions:OddEvenPeriodicExtension
If $f$ is defined on the interval $(0,a)$, then the periodic extension of the odd extension of $f$ is called the **odd periodic extension of $f$**.

Similarly, if $f$ is defined on the interval $[0,a)$, then the periodic extension of the even extension of $f$ is called the **even periodic extension of $f$**.
::::::

:::{note}
The symmetries of the odd and even extensions of $f$ carry over to the odd and even periodic extensions. If the original function was defined on $(0,a)$ then the odd and even periodic extensions have period $2a$, since they are periodic extensions of functions that are defined on the interval $(-a,a)$, which has length $2a$.
:::


:::{todo}
Make an applet that allows students to either draw a graph on $\mathbb{R}^2$ with $x>0$ and sketch the even and odd periodic extensions, or plug in a formula and draw the graphs of the even and odd periodic extensions.
:::

## Grasple exercises

### Exercises on combining and manipulating functions

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e5683704-3cac-4cb6-8535-bc4ba03deb4b?id=70802
:label: Grasple:70802
:dropdown:
:description: Maximal domain of product of two functions.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/de942950-9ffb-4c19-93f9-994c6ee3df8d?id=70803
:label: Grasple:70803
:dropdown:
:description: Maximal domain of product of two functions.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fd5d41c4-6c51-4e67-8b4b-28a410348c66?id=70805
:label: Grasple:70805
:dropdown:
:description: Maximal domain of composition of two functions.

::::

### Exercises on even and odd functions and hyperbolic functions



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fae93512-dad5-40c4-bd28-aa3e78083fdd?id=63037
:label: Grasple:63037
:dropdown:
:description: Determining whether a function is even and/or odd.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/eee3b148-0dca-4a4a-ae13-102d20789966?id=63040
:label: Grasple:63040
:dropdown:
:description: Determining whether a function is even and/or odd.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bddbac7c-3de8-4262-ba87-f99db3420348?id=63042
:label: Grasple:63042
:dropdown:
:description: Determining whether a function is even and/or odd.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e58f9eda-50a9-4e4d-9b3f-0ac06f81b27e?id=73779
:label: Grasple:73779
:dropdown:
:description: Establishing an identity for a hyperbolic function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/16d69364-6a37-4000-a52d-157e30f36013?id=78666
:label: Grasple:78666
:dropdown:
:description: Relating two hyperbolic functions.

::::


### Exercises on periodic functions

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/37c44a1b-96e8-4f88-af3c-bb9988fabf26?id=79437
:label: Grasple:79437
:dropdown:
:description: Which of these functions are periodic?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/abaf8f66-d36c-475d-b7ec-887387cdff8b?id=79439
:label: Grasple:79439
:dropdown:
:description: Dissecting a trigonometric function.

::::