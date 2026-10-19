(Sec:MultivariableFunctions)=
# Functions of two or more variables


## Introduction

[^FootnoteMountain]: a.k.a. not in the Netherlands,

Suppose you live near a mountainous region[^FootnoteMountain] and you want to make a map that depicts the elevation at each point in the region. In that case, you are trying to describe the elevation as a function of position. However, since position consists of **two** coordinates, this function has **two** input values: the $x$- and the $y$-coordinate of the location. Almost all functions that we have encountered so far only had a single output. Still, since for each input $(x,y)$ we obtain a single elevation we are dealing with a function as we defined in {prf:ref}`Def:Functions1var:Function`. Since the function has two input variables, we call such a function a **function of two variables**.

Since we live in a three-dimensional world, it is very natural to consider functions of two, or even three or four, variables. Many physical quantities are functions of location $(x,y)$, three-dimensional position $(x,y,z)$ and sometimes time can also be used as an additional input variable. In this chapter, we will study functions which have two or more input variables, which we will refer to as **multivariable functions**. We will still only consider functions with a single output variable. We will consider functions which also have several output variables in {numref}`Chapter:VectorCalculusIntro`.

## Basic concepts

In {numref}`Subsec:Functions1dConcepts` we defined the most important concepts related to functions in their most general form. We will repeat some of these definitions, in some cases specifically in the context of multivariable functions.

::::::{prf:definition} 
:label: Def:Functionsmultivar:Function

Let $n\geq 2$ be an integer. Then we call a function $f:D\rightarrow \mathbb{R}$ with $D\subset \mathbb{R}^n$ a **function of $n$ variables** or a **multivariable function**.

::::::

::::::{prf:notation} 
:label: Not:Functionsmultivar:Function

Let $f$ be a function of $n$ variables. For $\mathbf{x}=\begin{pmatrix}x_1\\ \vdots\\ x_n\end{pmatrix}$ in the domain of $f$ we write

$$
 f(x_1,...,x_n)=f(\mathbf{x}).
$$

::::::

:::{fetch} {prf:ref}`Notation:Functions1var:Codomain`
:::



::::::{prf:definition} 
:label: Def:Functions1var:Range

Let $f$ be a multivariable function with domain $D$. Then the **range** $R$ of $f$ is the set of all function values of $f$. That is, we have

$$
 R=\left\{y\,\,\text{in}\,\,\mathbb{R}\,\middle|\,\text{There is an }\mathbf{x}\,\text{in}\,D\,\text{with}\,f(\mathbf{x})=y\right\},
$$

which can be written more compactly as

$$
 R=\left\{f(\mathbf{x})\,\middle|\,\mathbf{x}\,\text{in}\,D\right\}.
$$
::::::

::::::{note}
The range is a subset of the codomain, which in the case of a multivariable function is always chosen to be $\mathbb{R}$.
::::::

Just as for single-variable functions, most functions that we will encounter can be described by means of a formula.

:::{fetch} {prf:ref}`Def:Functions1var:MaxDomain`
:::


::::::{important}
Whenever we define a function by means of a formula and we do not specify the domain, we assume that the domain is the maximal domain. 
::::::

::::::{prf:example} 
:label: Ex:FunctionsMultivar:MaxDomRange

Let $f$ be the function of two variables defined by $f(x,y)=\dfrac{\ln(e-y)}{x-y}$. Since we did not specify the domain of this function, we assume its domain is the maximal domain. So how can we find this maximal domain? For this, we need to check for which points $(x,y)$ the given formula produces a real number. In this case we have two restrictions: the input for the logarithm must be strictly positive and we are not allowed to divide by $0$. The first restriction means that we must have

$$
 e-y>0,
$$

which gives

$$
 y<e.
$$

The second restriction tells us that

$$
 x-y\neq 0,
$$

which we can rewrite as

$$
 x\neq y.
$$

We conclude that the maximal domain of $f$ is given by

$$
 \left\{(x,y)\in\mathbb{R}^2\,\middle|\,x\neq y,y<e\right\}.
$$

We can also find the range of this function. First, we note that for points of the form $(x,0)$ with $x\neq 0$ we have

$$
 f(x,0)=\frac{\ln(e-0)}{x-0}=\frac{1}{x}.
$$

The range of the single-variable function $g(x)=\dfrac{1}{x}$ is the union $(-\infty,0)\cup(0,\infty)$, i.e. the set of all real numbers except $0$. This means that the range of $f$ also contains all of these values. So we only need to check whether $0$ is in the range of $f$. This is the case, since, for instance, we have

$$
 f(0,e-1)=\frac{\ln(e-(e-1))}{0-(e-1)}=\frac{\ln(1)}{1-e}=0.
$$

We conclude that the range of $f$ is $\mathbb{R}$.
::::::

::::::{prf:example} 
:label: Ex:Functionsmultivar:NaturalDomain

In {prf:ref}`Ex:Functions1var:NaturalDomain` we considered a container with constant volume $V_0$ full of gas, measured in cubic meters. Now suppose that we let out the gas in an open room. Then the volume is no longer constant and we denote this volume by $V$. The [Ideal Gas Law](https://en.wikipedia.org/wiki/Ideal_gas_law) states that the temperature $T$ of the gas, measured in kelvin, is related to the pressure $P$, measured in pascal, and the volume by 

$$
 PV=nRT.
$$

Here $n$ is the amount of substance of gas, measured in moles, and $R$ is the ideal gas constant. By writing

$$
 T=f(P,V)=\frac{PV}{nR}
$$

we see that we can think of the temperature as a function of both pressure and volume. So what is a natural choice for the domain of this function? Mathematically, the formula $\dfrac{PV}{nR}$ is defined for each value of $P$ and $V$, so the maximal domain would be $\mathbb{R}^2$. However, physically, a negative pressure and a negative volume cannot occur, so we should, at the very least, impose that $P\geq 0$ and $V\geq 0$. So just like we observed in {prf:ref}`Ex:Functions1var:NaturalDomain`, it is important to keep the distinction in mind between the mathematical maximal domain and the physically relevant domain whenever physical quantities are involved.
::::::

For many standard single-variable functions, such as exponential or trigonometric functions, there is no universally accepted multivarible equivalent. For instance, the functions

$$
 f(x,y)=\sin(x+y),\quad g(x,y)=\sin(x)\sin(y),
$$

$$
 h(x,y)=\sin(2x-3y),\quad k(x,y)=\sin(x)
$$

are all functions of two variables involving one or more sines, but there is no function that is known as **the** sine function of two variables. Polynomial functions (and related terms such as linear and quadratic functions) are an exception to this, since for these functions there is a standard terminology. We have seen that in a single-variable context polynomial functions play a very important role and this is no different in the multivariable context. In order to properly define these functions in the multivariable setting, we first need to take a closer look at the concept of the degree.

::::::{prf:definition} 
:label: Def:Functionsmultivar:Monomial
A **monomial** in $n$ variables $x_1,\ldots,x_n$ is an expression of the form

$$
 ax_1^{m_1}x_2^{m_2}\cdot\ldots\cdot x_n^{m_n}
$$

where $a\in\mathbb{R}$ and $m_1\geq 0,\ldots,m_n\geq 0$ are non-negative integers. If $a\neq 0$, the **degree** of the monomial $ax_1^{m_1}x_2^{m_2}\cdot\ldots\cdot x_n^{m_n}$ is defined as the sum

$$
 m_1+\ldots+m_n.
$$

The degree of the monomial $0$ is undefined.

We say that two monomials $ax_1^{k_1}x_2^{k_2}\cdot\ldots\cdot x_n^{k_n}$ and $bx_1^{m_1}x_2^{m_2}\cdot\ldots\cdot x_n^{m_n}$ with $a\neq 0$ and $b\neq 0$ are **like**, when we have $k_1=m_1,\ldots, k_n=m_n$, i.e. when the exponent of each variable is the same in both monomials. Two monomials which are not like are called **unlike**. A set of several monomials is called **unlike** when each two different monomials in this set are unlike.
::::::

::::::{prf:definition} 
:label: Def:Functionsmultivar:Polynonomial
A **polynomial** in $n$ variables $x_1,\ldots,x_n$ is a finite sum of unlike monomials in $n$ variables. If the polynomial is not $0$, the **degree** of the polynomial is the maximum of the degrees of the non-zero monomials that define the polynomial. The degree of the polynomial $0$ is undefined.

A polynomial of degree $0$ is called **constant**, a polynomial of degree $1$ is called **linear**, a polynomial of degree $2$ is called **quadratic** and a polynomial of degree $3$ is called **cubic**.
::::::


::::::{prf:definition} 
:label: Def:Functionsmultivar:Polynonomialfunction
A function $f$ of $n$ variable is called a **polynomial** function if it can be written as $f(x_1,\ldots,x_n)=P$, where $P$ is a polynomial in $x_1,\ldots,x_n$. The function is called a **constant function**, **linear function**, **quadratic function** or **cubic function** when $P$ is a constant polynomial, linear polynomial, quadratic polynomial or cubic polynomial respectively.
::::::

Linear functions are especially important as they are some of the easiest functions to work with. Sometimes, it is convenient to express a linear function in terms of a dot product as that is a more compact way to denote the function. The following theorem shows that this is always possible.

::::::{prf:theorem} 
:label: Thm:Functionsmultivar:Linear
Let $f$ be a linear function of $n$ variables. Then there exist unique $c\in\mathbb{R}$ and $\mathbf{v}\in\mathbb{R}^n$ with $\mathbf{v}\neq \mathbf{0}$ such that for all $\mathbf{x}\in\mathbb{R}^n$ we have

$$
 f(\mathbf{x})=c+\mathbf{v}\cdot\mathbf{x}.
$$
::::::

:::{admonition} Proof of {prf:ref}`Thm:Functionsmultivar:Linear`
:class: tudproof, dropdown

Since $f$ is a linear function, we have $f(\mathbf{x})=P(\mathbf{x})$ where $P$ is a polynomial of degree $1$. By definition, $P$ is a finite sum of unlike monomials with degree at most $1$, of which at least one monomial has degree $1$. The only type of monomial with degree $0$ is a nonzero constant. So if one of the terms of $P$ is a monomial with degree $0$, we take that term as $c$; otherwise, we take $c=0$. Since the degree of a monomial $ax_1^{m_1}x_2^{m_2}\cdot\ldots\cdot x_n^{m_n}$ with $a\neq 1$ equals $m_1+\ldots+m_n$ and $m_1,\ldots,m_n$ are non-negative integers, we see that we only obtain a monomial of degree $1$ if $m_i=1$ for some $1\leq i\leq n$ and $m_j=0$ for $j\neq i$. So we can uniquely write for $\mathbf{x}=\begin{pmatrix}x_1\\ \vdots\\ x_n\end{pmatrix}$

$$
 P(\mathbf{x})=c+v_1x_1+\ldots+v_nx_n
$$

for some real numbers $v_1,\ldots,v_n$. Writing $\mathbf{v}=\begin{pmatrix}v_1\\ \vdots\\ v_n\end{pmatrix}$, we obtain 

$$
 f(\mathbf{x})=c+v_1x_1+\ldots+v_nx_n=c+\mathbf{v}\cdot\mathbf{x}.
$$

Since $P$ has degree $1$, at least one monomial must have degree $1$, so at least one $v_i$ must be non-zero. This means that $\mathbf{v}\neq\mathbf{0}$.


:::

::::::{prf:example} 
:label: Ex:Functionsmultivar:Polynonomial
Consider the functions

$$
 f(x,y)=3-2x+4y,\qquad g(x,y,z)=x^3-2x^2y^2+3z^2.
$$

Both of these functions are polynomial functions. The polynomial $3-2x+4y$ is the sum of three monomials: $3$, with degree $0$, $-2x$, with degree $1$ and $4y$, also with degree $1$. Therefore, $f$ is a linear function.

The polynomial $x^3-2x^2y^2+3z^2$ is the sum of three monomials: $x^3$, with degree $3$, $-2x^2y^2$, with degree $2+2=4$ and $3z^2$, with degree $2$. As such, the polynomial defining $g$ has degree $4$ (even though there is no fourth power of any of the variables).
::::::




## Graphs

Just like with any function, we can consider the **graph** of a multivariable function. From {numref}`Subsec:Functions1dConcepts` we recall that the graph $G$ of a multivariable function $f$ is given by

$$
 G=\left\{(\mathbf{x},f(\mathbf{x}))\,\middle|\,\mathbf{x}\in D_f\right\}.
$$

Since $D_f$ is a subset of $\mathbb{R}^n$, we can view the graph of $f$ as a subset of $\mathbb{R}^{n+1}$, where for each point in this graph the first $n$ entries correspond to the input variables and the final entry corresponds to the output variable. This means that we can visualise graphs of functions of two variables as surfaces in $\mathbb{R}^3$. Drawing these by hand is typically harder than drawing graphs of single-variable functions, but it is often doable and otherwise, computer graphing software can be used to visualise the graph. 

:::{figure} images/Fig-Functionsmultivar-Graph2d.png
:name: Fig:Graph2d
:class: dark-light

The graph of a function $f$ of two variables.
:::

:::{todo}
Turn {numref}`Fig:Graph2d` into an applet. Make sure to call the domain $D_f$ and the graph $G_f$. And maybe use a different shape for the function as this picture is stolen from Stewart.
:::

However, for functions of three or more variables we run into a major issue: we live in a three-dimensional world, so it is not feasible to visualise a subset of a four- or higher-dimensional space. So while for these functions the graph exists as a mathematical concept, it cannot be used to visualise the behaviour of the function. In {numref}`Section:Levelcurves` we will consider an alternative method to visualise the behaviour of functions of two or three variables.

Let us return to functions of two variables. We already stated that the graph of such a function is a surface in $\mathbb{R}^3$. We will study surfaces in more depth in {numref}`Section:SurfacesR3`. Just like not every curve in $\mathbb{R}^2$ is the graph of a single-variable function, not every surface in $\mathbb{R}^3$ is the graph of a function of two variables. Recall that the defining property of a function is that for each input $(x,y)$ the function gives a *single* output $f(x,y)$. Just like we did for single-variable functions, we can check whether a surface is the graph of a function by verifying whether each vertical line, which in $\mathbb{R}^3$ takes the form $\begin{cases}x&=a,\\ y&=b,\end{cases}$, intersects the graph at most once. We can formulate this result as follows.

::::::{prf:theorem} Vertical line test 
:label: Thm:Functionsmultivar:VerticalLineTest
A surface in $\mathbb{R}^3$ is the graph of a function of two variables precisely when each vertical line of the form $\begin{cases}x&=a,\\ y&=b,\end{cases}$ for some real numbers $a$ and $b$ intersects the surface at most once.
::::::

So what is a good way to start when sketching the graph of a function of two variables? Since we already have a good understandig of how to sketch graphs of single-variable functions, it would be very convenient if we can somehow use this. For this we can fix the value of either the first input variable or of the second input variable. Then there is only one input variable remaining, so we have reduced the problem to sketching the graph of a single-variable function. Geometrically speaking, we consider the intersection of the graph of the function with a plane of the form $x=a$ or $y=b$, which, typically, is a curve in $\mathbb{R}^3$. Let us consider an example to see how this works in practice.

::::::{prf:example} 
:label: Ex:Functionsmultivar:Sketching
Consider the function $f(x,y)=3+(x-1)^2-(y-2)^2$. Suppose we want to sketch the graph of this function. To do so, we first try to see what happens if we fix the value of $y$. Setting $y=b$, we find

$$
 f(x,b)=3+(x-1)^2-(b-2)^2.
$$

For any value of $b$, the equation $z=3+(x-1)^2-(b-2)^2$ is a parabola in the $xz$-plane which opens upwards. The vertex of the parabola is at $(x,z)=\left(1,3-(b-2)^2\right)$. So whenever we intersect the graph of $f$ with the plane $y=b$ we should see such a parabola.

:::{todo}
Include an applet where the parabola $z=3+(x-1)^2-(b-2)^2$ is shown, with a slider for $b$ (default value $b=2$).
:::

We can also see what happens if, instead, we fix the value of $x$. Setting $x=a$, we obtain

$$
 f(a,y)=3+(a-1)^2-(y-2)^2.
$$

For any value of $a$, the equation $z=3+(a-1)^2-(y-2)^2$ is a parabola in the $yz$-plane which opens downwards. The vertex of the parabola is at $(y,z)=\left(2,3+(a-1)^2\right)$. So whenever we intersect the graph of $f$ with the plane $x=a$ we should see such a parabola.

:::{todo}
Include an applet where the parabola $z=3+(x-1)^2-(b-2)^2$ is shown, with a slider for $b$ (default value $b=2$).
:::

Since we now know what the graph of $f$ looks like when intersecting it with planes of the form $y=b$ or $x=a$, we have sufficient information to sketch the graph of $f$ itself. The result is shown in {numref}`Fig:Functionsmultivar:Graphquad`.

:::{todo}
Include an applet with the graph for $f$, with a toggle that shows intersection with planes of the form $y=b$ or $x=a$. The label of the applet should be Fig:Functionsmultivar:Graphquad
:::
::::::

For some functions, we can sketch the graph because we can recognise it as a geometrical object. For instance, the graph of a linear function describes a plane in $\mathbb{R}^3$. Other geometrical objects are possible as well, as can be seen in the following example.

::::::{prf:example} 
:label: Ex:Functionsmultivar:SketchingRecog
Consider the function 

$$
 f(x,y)=2-\sqrt{9-(x+1)^2-y^2}.
$$

We note that if $z=f(x,y)$ we can write

$$
 z-2=-\sqrt{9-(x+1)^2-y^2}.
$$

By squaring this equation, we obtain

$$
 (z-2)^2=9-(x+1)^2-y^2,
$$

which gives

$$
 (x+1)^2+y^2+(z-2)^2=9.
$$

This is the equation for a sphere with radius $\sqrt{9}=3$ and center $(-1,0,2)$. It is a common mistake to now think that the graph of $f$ is exactly this sphere. A reason why this is incorrect, is that a sphere can never be the graph of a function, as it fails {prf:ref}`Thm:Functionsmultivar:VerticalLineTest`. For instance, the line $\begin{cases}x=-1\\ y=0\end{cases}$ intersects this sphere twice: at $(-1,0,-1)$ and at $(-1,0,5)$. 

We arrived at the equation for this sphere by squaring the equation

$$
 z-2=-\sqrt{9-(x+1)^2-y^2}.
$$

Whenever you square an equation, you lose information: squaring the equation 

$$
 z-2=\sqrt{9-(x+1)^2-y^2}
$$ 

*also* gives the equation 

$$
 (z-2)^2=9-(x+1)^2-y^2,
$$

while the equations $z-2=-\sqrt{9-(x+1)^2-y^2}$ and $z-2=\sqrt{9-(x+1)^2-y^2}$ are not the same. From the equation 

$$
 z-2=-\sqrt{9-(x+1)^2-y^2}
$$

we can read off that on the graph of $f$ we should have $z-2\leq 0$, i.e. $z\leq 2$. This means that the graph of $f$ is the lower half of the sphere 

$$
 (x+1)^2+y^2+(z-2)^2=9,
$$

which is a surface that does pass the vertical line test. The upper half of the sphere is the graph of the function 

$$
 g(x,y)=2+\sqrt{9-(x+1)^2-y^2}.
$$

:::{todo}
Include an applet with the graph of $f$.
:::

::::::

