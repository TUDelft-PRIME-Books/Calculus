(Sec:DE:Intro)=

# Differential equations and solutions

In this section we cover:

- Introduction by means of examples
- Definitions of differential equation, initial-value problems and boundary-value problems:
  - Mention names of problems
  - Mention names of boundary conditions
- (in)dependent variable
- Classification of differential equations:
  - linear/nonlinear (including algorithmic check)
  - order
  - ordinary/partial
  - autonomous/non-autonomous (including algorithmic check)
- Definition solution of a DE/IVP/BVP
  - general solution
  - particular solution
  - implicit solution
  - equilibrium solution
  - checking solutions
- linear differential equations
  - constant coefficients/variable coefficients
  - Superposition principle for linear differential equations
  - homogeneous/non-homogeneous (including algorithmic check)
  - nonhomogeneous solution = homogeneous solution + particular solution

## Introduction

In science differential equations often arise in modelling. We consider two examples: population growth and a mass-spring system.

**Population growth**

One model for the growth of a population is based on the assumption that the population grows at a rate proportional to the size of the population.

That is a reasonable assumption for a population of bacteria or animals under ideal conditions (unlimited environment, adequate nutrition, absence of predators, immunity of disease).

If $P(t)$ denotes the number of individuals in a population at time $t$, then: $\dfrac{dP}{dt}=kP$, where $k$ denotes the growth rate. This is called *exponential growth*, since the general solution is $P(t)=Ce^{kt}$ with $C\in\mathbb{R}$.

A more realistic model is $\displaystyle\frac{dP}{dt}=kP\left(1-\frac{P}{M}\right)$. This is called a *logistic equation*.

This differential equation was proposed by the Belgian mathematician [Pierre François Verhulst (1804-1849)](https://en.wikipedia.org/wiki/Pierre_Fran%C3%A7ois_Verhulst) in 1838 as a model for world population growth.

This more realistic model reflects the fact that a given environment has limited resources. Many populations start by increasing in an exponential manner, but the population levels off when it approaches its *carrying capacity* $M$ (or decreases toward $M$ if it ever exceeds $M$).

**A mass-spring system**

Consider a mass $m$ attached to a spring as in the picture below. Let $x$ denote the distance from the mass to the equilibrium position. This value is positive when the spring is stretched and negative when the spring is compressed. If we, for instance, pull the mass and stretch the spring over a small distance and release it, the mass will move such that the position $x$ will change from positive to negative and the other way around. So, the distance $x=x(t)$ is in fact a function of the time $t$.

```{figure} Images/mass-spring1.png
---
width: 50%
name: mass-spring
align: center
---
A mass-spring system
```

Using Newton's law $F=m\cdot a$ and Hooke's law $F=-k\cdot x$, we obtain

$$
m\cdot\frac{d^2x}{dt^2}=-k\cdot x(t),
$$

where $k$ is a positive constant, called the *spring constant*.

Without damping we have: $mx''(t)+kx(t)=0$.

```{figure} Images/mass-spring2.png
---
width: 50%
name: mass-spring
align: center
---
A mass-spring system
```

```{figure} Images/mass-spring3.png
---
width: 50%
name: mass-spring
align: right
---
A mass-spring system
```

<br /><br />

With damping we have: $mx''(t)+cx'(t)+kx(t)=0$. 

Here $c$ is a positive constant, called the *damping constant*.

<br /><br /><br /><br /><br />

## Classifications

::::::{prf:Definition}
A **differential equation** is an equation involving an unknown function and one or more of its derivatives. The order of the highest derivative involved is called the **order** of the differential equation.
::::::

In case of an unknown function of a single variable, the differential equation is called an **ordinary differential equation**. In case of an unknown function of more than one variable, the differential equation is called a **partial differential equation**.

In this book we will only consider ordinary differential equations. However, see chapter 9 on partial derivatives for some examples of partial differential equations.

Note that the logistic equation is a first-order differential equation and the differential equations involved in a mass-spring system are second-order differential equations.

A differential equation in a function $y(x)$ can be written as $F(x,y,y',y'',\ldots,y^{(n)})=0$. The variable $x$ is called an **independent variable**, while $y=y(x)$ is called a **dependent variable**.

A function $f(x)$ is called a **solution** of the differential equation if the equation is satisfied by $y=f(x)$, so if $F(x,f(x),f'(x),f''(x),\ldots,f^{(n)}(x))=0$.

When we are asked to *solve* a differential equation, we are expected to find all possible solutions. However, in general it is not easy to solve a differential equation. There is no systematic approach that enables us to solve differential equations. Only when a differential equation has a specific form, we might have some techniques to find the general solution (the set of *all* solutions).

We also distinguish differential equations by their order. In this book we mainly focus on first-order (chapter 13) and second-order (chapter 14) differential equations.

Furthermore, we distinguish linear and nonlinear differential equations. A differential equation $F(x,y,y',y'',\ldots,y^{(n)})=0$ is called **linear** if $F$ is a linear function of the variables $y,y',y'',\ldots,y^{(n)}$. Otherwise, the differential equation is called **nonlinear**.

In general, linear differential equations are much easier to solve than nonlinear differential equations. Especially for differential equations of order higher than one there is very limited theory for nonlinear differential equations.

An example of a physical problem that leads to a nonlinear differential equation is an oscillating pendulum.

```{figure} Images/pendulum.png
---
width: 65%
name: pendulum
align: left
---
The motion of a pendulum
```

The differential equation which represents the motion of a simple pendulum is:

$$
\frac{d^2\theta}{dt^2}+\frac{g}{L}\sin(\theta)=0,
$$

where $g$ is the acceleration due to gravity, $L$ is the length of the pendulum, and $\theta$ is
the angular displacement with respect to the equilibrium position at time $t$.

It is quite difficult to solve this differential equation.

However, the linearization of the function $f(x)=\sin(x)$ at $x=0$ is

$$
L(x)=f(0)+f'(0)(x-0)=x.
$$

This implies that $\sin(x)\approx x$ for $x$ near $0$.

It turns out that it is much easier to solve the differential equation

$$
\frac{d^2\theta}{dt^2}+\frac{g}{L}\theta=0
$$

instead of the one above. See {numref}`Sec:ODE2:Homogeneous`.

The differential equations involved in a mass-spring system are all linear. These will also be solved in {numref}`Sec:ODE2:Homogeneous`.

For first-order differential equations we distinguish autonomous and nonautonomous differential equations. A differential equation is called **autonomous** if it can be written as $F(y,y')=0$. So, if the independent variable is not explicitly involved. Otherwise, the differential equation is called **nonautonomous**.

Note that the *logistic equation* is an example of an autonomous differential equation. This equation will be solved in {numref}`Sec:ODE1:Separable`.

Finally we mention the possibility of more than one unknown function. For each unknown function we might consider a linear differential equation of the form

$$
y_k'(x)=a_1y_1(x)+a_2y_2(x)+\cdots+a_ny_n(x)+g_k(x),\quad k=1,2,3,\ldots,n.
$$

This leads to a **system of first-order linear differential equations**. These systems will not be covered in this book. We refer to the book on Linear algebra for an introduction to homogeneous systems of first-order differential equations and to more advanced books on differential equations for a more thorough treatment of these systems.

## Linear differential equations

A differential equation $F(x,y,y',y'',\ldots,y^{(n)})=0$ is called *linear* if $F$ is a linear function of the variables $y,y',y'',\ldots,y^{(n)}$. For linear differential equations there exists quite some theory. In {numref}`Sec:ODE1:Linear` we will consider and solve first-order linear differential equations.

A second-order *linear* differential equation has the form

$$
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)=G(x),
$$

where $P$, $Q$, $R$ and $G$ are continuous functions with $P(x)\neq0$. Such a differential equation is called **homogeneous** if $G(x)\equiv0$ and **inhomogeneous** if $G(x)\not\equiv0$.

So, a homogeneous second-order linear differential equation has the form

$$
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)=0,
$$

where $P$, $Q$ and $R$ are continuous functions with $P(x)\neq0$. Then we have:

::::::{prf:theorem} Superposition principle
:label: Thm:DE:SuperpositionPrinciple
If $y_1(x)$ and $y_2(x)$ are both solutions, then $y(x)=c_1y_1(x)+c_2y_2(x)$ is also a solution for each $c_1,c_2\in\mathbb{R}$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:DE:SuperpositionPrinciple`
:class: tudproof, dropdown
Since $y_1(x)$ and $y_2(x)$ are both solutions, we have

$$
P(x)y_1''(x)+Q(x)y_1'(x)+R(x)y_1(x)=0
$$

and

$$
P(x)y_2''(x)+Q(x)y_2'(x)+R(x)y_2(x)=0.
$$

Let $y(x)=c_1y_1(x)+c_2y_2(x)$, then we have

$$
\begin{align*}
&P(x)y''(x)+Q(x)y'(x)+R(x)y(x)\\
&=P(x)\left[c_1y_1''(x)+c_2y_2''(x)\right]+Q(x)\left[c_1y_1'(x)+c_2y_2'(x)\right]\\
&{}\quad{}+R(x)\left[c_1y_1(x)+c_2y_2(x)\right]\\
&=c_1\left[P(x)y_1''(x)+Q(x)y_1'(x)+R(x)y_1(x)\right]\\
&{}\quad{}+c_2\left[P(x)y_2''(x)+Q(x)y_2'(x)+R(x)y_2(x)\right]\\
&=c_1\cdot0+c_2\cdot0=0.
\end{align*}
$$

::::::

::::::{prf:definition}
:label: Def:DE:LinearIndependent
Two functions $f(x)$ and $g(x)$ are called **linearly independent** on an interval $I$ if 

$$
c_1f(x)+c_2g(x)=0\quad\text{for all}\quad x\in I
$$

implies that $c_1=0$ and $c_2=0$.
::::::

::::::{prf:example}
:label: Ex:DE:LinearIndependentExample1
The functions $x$ and $x^2$ are linearly independent on the interval $[0,1]$, since

$$
c_1x+c_2x^2=0
$$

leads to $c_1+c_2=0$ if $x=1$ and to $\frac{1}{2}c_1+\frac{1}{4}c_2=0$ if $x=\frac{1}{2}$. This implies that $c_1=0$ and $c_2=0$.
::::::

::::::{prf:example}
:label: Ex:DE:LinearIndependentExample2
The functions $e^{-2x}$ and $e^{3x}$ are linearly independent on $\mathbb{R}$, since

$$
c_1e^{-2x}+c_2e^{3x}=0
$$

leads to $c_1+c_2=0$ if $x=0$ and to $e^{-2}c_1+e^{3}c_2=0$ if $x=1$. This implies that $c_1=0$ and $c_2=0$.
::::::

::::::{prf:example}
:label: Ex:DE:LinearIndependentExample3
The functions $\cos(x)$ and $\sin(x)$ are linearly independent on $\mathbb{R}$, since

$$
c_1\cos(x)+c_2\sin(x)=0
$$

leads to $c_1=0$ if $x=0$ and to $c_2=0$ if $x=\frac{1}{2}\pi$.
::::::

::::::{prf:theorem}
:label: Thm:DE:GeneralSolutionHomogeneous
If $y_1(x)$ and $y_2(x)$ are linearly independent solutions on an interval, and $P(x)$ is never $0$
there, then the general solution is given by $y(x)=c_1y_1(x)+c_2y_2(x)$, where $c_1$ and $c_2$ are arbitrary constants.
::::::

An inhomogeneous second-order linear differential equation has the form

$$
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)=G(x),
$$

where $P$, $Q$, $R$ and $G$ are continuous functions with $P(x)\neq0$ and $G(x)\not\equiv0$. Then we have:

::::::{prf:theorem}
:label: Thm:DE;GeneralSolutionInhomogeneous
If $y_p(x)$ is a particular solution and $y_h(x)$ is the general solution of the corresponding homogeneous (also called: *complementary*) differential equation (with $G(x)$ replaced by $0$), then $y(x)=y_p(x)+y_h(x)$ is the general solution.
::::::

## Initial-value problems

In many cases we are not interested in finding all solutions (the *general solution*) as in finding a specific solution that also satisfies some additional requirement(s). In many physical problems, in case of a first-order differential equation we need to find a particular solution that also satisfies a condition of the form $y(x_0)=y_0$. This is called an **initial condition**. The problem of finding a solution of a first-order differential equation that also satisfies such an initial condition is called an **initial-value problem**.

In {numref}`Sec:DE:ExistenceUniqueness` it will be shown that a first-order differential equation, that satisfies certain conditions, has a general solution with one degree of freedom; somewhere in the process of solving such a differential equation we have to integrate once which gives rise to a so-called arbitrary **constant of integration**.

Then this arbitrary constant can be chosen in such a way that the solution also satisfies an initial condition of the form $y(x_0)=y_0$.

::::::{prf:example}
The differential equation $y'=3x^2$ has the general solution $y(x)=x^3+C$ with $C\in\mathbb{R}$. However, there is only one solution that also satisfies the initial condition $y(0)=0$: $y(x)=x^3$, since $y(0)=0$ leads to $0=0^3+C=C$.
::::::

::::::{prf:example}
The differential equation $y'=2y$ has the general solution $y(x)=Ce^{2x}$ with $C\in\mathbb{R}$. However, there is only one solution that also satisfies the initial condition $y(0)=3$: $y(x)=3e^{2x}$, since $y(0)=3$ leads to $3=Ce^{2\cdot0}=C$.
:::::: 

In {numref}`Sec:DE:ExistenceUniqueness` it will be shown that a second-order linear differential equations of the form

$$
y''+p(t)y'+q(t)y=g(t),
$$

with $p$, $q$ and $g$ continuous functions, has a general solution with two degrees of freedom; it contains two arbitrary constants of integration. These can be chosen such that the solution also satisfies two initial conditions $y(t_0)=y_0$ and $y'(t_0)=y_0'$.

Note that this implies that the solution of the **initial-value problem**

$$
y''+p(t)y'+q(t)y=g(t),\quad y(t_0)=y_0,\quad y'(t_0)=y_0'
$$

*exists* and is *unique*.

::::::{prf:example}
Note that $y_1(x)=\cos(x)$ and $y_2=\sin(x)$ are two linear independent solutions of the second-order linear differential equation

$$
y''+y=0.
$$

This implies that $y(x)=c_1\cos(x)+c_2\sin(x)$ is the general solution. This implies that $y'(x)=-c_1\sin(x)+c_2\cos(x)$. Then we have:

$$
\begin{cases}y(0)=\alpha\\ \\y'(0)=\beta\end{cases}\quad\Longleftrightarrow\quad\begin{cases}c_1=\alpha\\ \\c_2=\beta.\end{cases}
$$

::::::

## Boundary-value problems

Instead of initial-value problems we might consider boundary-value problems, where we try to fix the solution $y(x)$ defined on some interval $[a,b]$ such that the value at the boundary points $x=a$ and $x=b$ are fixed: $y(a)=\alpha$ and $y(b)=\beta$.

In case of a first-order differential equation we only have one degree of freedom. In general, it is not possible to choose the constant of integration in such a way that both $y(a)=\alpha$ and $y(b)=\beta$ are satisfied.

::::::{prf:example}
The differential equation $y'=y$ has the general solution $y(x)=Ce^x$ with $C\in\mathbb{R}$. Now, for instance, $y(0)=\alpha$ implies that $C=\alpha$. However, then $y(1)=\alpha e$. This implies that the boundary-value problem

$$
y'=y,\quad y(0)=\alpha,\quad y(1)=\beta
$$

only has a (unique) solution if $\beta=\alpha e$. Otherwise, there is no solution.
::::::

Although the general solution of a second-order linear differential equation has two degrees of freedom, a corresponding boundary-value problems might have no solution, a unique solution or even infinitely many solutions.

::::::{prf:example}
The general solution of $y''+y=0$ is $y(x)=c_1\cos(x)+c_2\sin(x)$ with $c_1,c_2\in\mathbb{R}$. This implies, for instance, that $y(0)=c_1$ and $y(\pi)=-c_1$. So, the boundary-value problem

$$
\begin{cases}y''+y=0,\quad0<x<\pi\\ \\y(0)=\alpha,\quad y(\pi)=\beta\end{cases}
$$

has no solution if $\beta\neq-\alpha$. Moreover, if $\beta=-\alpha$ the boundary-value problem has infinitely many solutions $y(x)=\alpha\cos(x)+c_2\sin(x)$ with $c_2\in\mathbb{R}$ arbitrary.
::::::

::::::{prf:example}
Check that $y_1(x)=\cos(x\sqrt{2})$ and $\sin(x\sqrt{2})$ are two linear independent solutions of the second-order linear differential equation $y''+2y=0$. Then the boundary-value problem

$$
\begin{cases}y''+2y=0,\quad 0<x<\pi\\ \\y(0)=\alpha,\quad y(\pi)=\beta\end{cases}
$$

has a unique solution $y(x)=\alpha\cos(x\sqrt{2})+\dfrac{\beta-\alpha\cos(\pi\sqrt{2})}{\sin(\pi\sqrt{2})}\sin(x\sqrt{2})$.
::::::

## (Grasple) exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c83c4815-8d8c-4a1d-bade-f720cf165406?id=79453
:label: grasple_exercise_13_0_1
:dropdown:
:description: Are two functions linearly independent?
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fa7c4299-9811-428f-80dc-ee1ad8503e6c?id=79449
:label: grasple_exercise_13_0_2
:dropdown:
:description: Is the differential equation homogeneous or not?
::::::
