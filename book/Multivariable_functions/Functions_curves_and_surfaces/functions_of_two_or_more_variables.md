(Sec:MultivariableFunctions)=
# Functions of two or more variables

In this section we cover:

- Notation
- Domain, codomain and range
- Graphs of functions of two variables
- Differences and similarities between graphs and surfaces

## Introduction

[^FootnoteMountain]: i.e. not in the Netherlands,

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

## Graphs

Just like with any function, we can consider the **graph** of a multivariable function. From {numref}`Subsec:Functions1dConcepts` we recall that the graph $G$ of a multivariable function $f$ is given by

$$
 G=\left\{(\mathbf{x},f(\mathbf{x}))\,\middle|\,\mathbf{x}\in D_f\right\}.
$$

Since $D_f$ is a subset of $\mathbb{R}^n$, we can view the graph of $f$ as a subset of $\mathbb{R}^{n+1}$, where for each point in this graph the first $n$ entries correspond to the input variables and the final entry corresponds to the output variable. This means that we can visualise graphs of functions of two variables as surfaces in $\mathbb{R}^3$. Drawing these by hand is typically harder than drawing graphs of single-variable functions, but it is often doable and otherwise, computer graphing software can be used to visualise the graph. 

:::{figure} Images/Fig-Functionsmultivar-Graph2d.png
:name: Fig:Graph2d
:class: dark-light

The graph of a function $f$ of two variables.
:::

:::{todo}
Turn {numref}`Fig:Graph2d` into an applet. Make sure to call the domain $D_f$ and the graph $G_f$. And maybe use a different shape for the function as this picture is stolen from Stewart.
:::

However, for functions of three or more variables we run into a major issue: we live in a three-dimensional world, so it is not feasible to visualise a subset of a four- or higher-dimensional space. So while for these functions the graph exists as a mathematical concept, it cannot be used to visualise the behaviour of the function.

Let us return to functions of two variables. We already stated that the graph of such a function is a surface in $\mathbb{R}^3$. We will study surfaces in more depth in {numref}`Section:SurfacesR3`. Just like not every curve in $\mathbb{R}^2$ is the graph of a single-variable function, not every surface in $\mathbb{R}^3$ is the graph of a function of two variables. Recall that the defining property of a function is that for each input $(x,y)$ the function gives a *single* output $f(x,y)$. Just like we did for single-variable functions, we can check whether a surface is the graph of a function by verifying whether each vertical line, which in $\mathbb{R}^3$ takes the form $\begin{cases}x&=a,\\ y&=b,\end{cases}$, intersects the graph at most once. We can formulate this result as follows.

::::::{prf:theorem} Vertical line test 
:label: Thm:Functionsmultivar:VerticalLineTest
A surface in $\mathbb{R}^3$ is the graph of a function of two variables precisely when each vertical line of the form $\begin{cases}x&=a,\\ y&=b,\end{cases}$ for some real numbers $a$ and $b$ intersects the surface at most once.
::::::




