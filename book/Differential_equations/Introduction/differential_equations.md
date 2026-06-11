(Sec:DE:Intro)=
# Classifications and solutions



(Subsec:DiffclassIntro)=

## Introduction

For most equations we have encountered so far, the solution is a set of numbers. In this chapter, we will study an important class of equations, called **differential equations**, of which the solution is a **function**. Loosely speaking, differential equations are equations that feature an unknown function and one or more of its derivatives. For instance, consider the equation

$$
 y'(x)=\cos(x).
$$

This equations should be read as follows: we are looking for a function $y(x)$ of which the derivative is equal to $\cos(x)$. Fortunately, we already know the answer to this equation, as we have

$$
 y(x)=\int \cos(x)\,dx=\sin(x)+C
$$

for some constant $C$. So far so good, but what should we do with the following equation?

$$
 y'(x)=2y(x).
$$

Let us first try to understand what this equation says. It tells us that we are looking for a function $y(x)$ of which the derivative is $2$ times the original function $y(x)$. What could this function be? If this question is asked in class, the first answer that usually comes up is $y(x)=x^2$. Let us check if this answer is correct. For this function, the derivative is given by

$$
 y'(x)=2x,
$$

while $2$ times the function is given by

$$
 2y(x)=2x^2.
$$

These two expression are **not** the same, so $y(x)=x^2$ is **not** a solution of this differential equation. So which function is a solution, if any? For this, we are looking for a function of which the derivative is a multiple of the original function. Fortunately, we know that exponential functions have this property. This suggests that we should consider $y(x)=e^{2x}$. For this function, the derivative is given by

$$
 y'(x)=2e^{2x},
$$

and $2$ times the function is given by

$$
 2y(x)=2e^{2x}.
$$

This is the same expression, so $y(x)=e^{2x}$ is a solution. Is it the only solution? You might be tempted to think that we should add a constant, similarly to adding a constant of integration, so that $y(x)=e^{2x}+C$ would be a solution for any $C$. To see if this idea is correct, we see that the derivative is given by

$$
 y'(x)=2e^{2x}+0=2e^{2x},
$$

and $2$ times the function is given by

$$
 2y(x)=2e^{2x}+2C.
$$

This is not the same expression (unless $C=0$), so adding a constant does not work. It turns out that, instead, we should have multiplied the exponential with a constant, so $y(x)=Ce^{2x}$ for some constant $C$. Then the derivative is given by

$$
 y'(x)=2Ce^{2x},
$$

and $2$ times the function is given by

$$
 2y(x)=2Ce^{2x}.
$$

This is the same expression, so $y(x)=Ce^{2x}$ is also a solution. Later, we will see that any solution is of this form.

You might think that equations like $y'(x)=2y(x)$ are a bit artificial and are made up by mathematicians who take pleasure in making your life miserable by introducing needlessly complicated equations. Nothing could be further from the truth. In science and engineering, differential equations very often arise in modelling. There are many problems where we try to model a quantity and that the laws of physics tell us that its rate of change (so its derivative) is related to its current size. In the remainder of this introduction, we consider two examples: population growth and a mass-spring system.

::::::{prf:example} Population growth
:label: Ex:Diffclass:population

One model for the growth of a population is based on the assumption that the population grows at a rate proportional to the size of the population. This is a reasonable assumption for a population of bacteria or animals under ideal conditions (unlimited environment, adequate nutrition, absence of predators, immunity of disease). If $P(t)$ denotes the number of individuals in a population at time $t$, we can denote this idea more mathematically by writing

$$
 \dfrac{dP}{dt}=kP(t),
$$

where $k$ denotes the growth rate. This equation is a differential equation, as it features an unknown function $P(t)$ and its derivative $\dfrac{dP}{dt}$. This particular equation is known as *exponential growth*, since the general solution is $P(t)=Ce^{kt}$ for some constant $C$.

A more realistic model is 

$$
 \frac{dP}{dt}=kP\left(1-\frac{P}{M}\right).
$$

This is called a *logistic equation*. This differential equation was proposed by the Belgian mathematician [Pierre François Verhulst (1804-1849)](https://en.wikipedia.org/wiki/Pierre_Fran%C3%A7ois_Verhulst) in 1838 as a model for world population growth.

This more realistic model reflects the fact that a given environment has limited resources. Many populations start by increasing in an exponential manner, but the population levels off when it approaches its *carrying capacity* $M$ (or decreases towards $M$ if it ever exceeds $M$).

:::{todo}
Include an applet with a plot of a few solutions to the logistic equation.
:::

::::::

::::::{prf:example} A mass-spring system
:label: Ex:Diffclass:massspring



Consider a mass $m$ attached to a spring as in {numref}`mass-spring1`. Let $x$ denote the distance from the mass to the equilibrium position. This value is positive when the spring is stretched and negative when the spring is compressed. If we, for instance, pull the mass and stretch the spring over a small distance and release it, the mass will move such that the position $x$ will change from positive to negative and the other way around. So, the distance $x=x(t)$ is in fact a function of the time $t$.

```{figure} Images/mass-spring1.png
---
width: 50%
name: mass-spring1
class: dark-light
---
A mass-spring system
```

So which physical laws determine the behaviour of this system? Somehow, one of the first answers that comes up, usually, is gravity. However, gravity does not play a role here: we could observe the behaviour of this system in outer space and not a lot would change. Only the position of equilibrium is determined by gravity, but since we measure the displacement with respect to equilibrium, we do not see this in our calculations.

Instead, since we are dealing with a spring, Hooke's law $F=-k\cdot x$, where $k$ is a positive constant, called the *spring constant*, should of course be involved. And as with many problems that involve forces, Newton's second law $F=m\cdot a$ must play a role as well. Here $a$ is the acceleration, which is $\dfrac{d^2x}{dt^2}$. Without damping, we can combine these laws into the equation

$$
m\cdot\frac{d^2x}{dt^2}=-k\cdot x(t).
$$

We can rewrite this equation into

$$
 mx''(t)+kx(t)=0.
$$

This is a differential equation, as it involves the unknown function $x(t)$ and its second derivative $x''(t)$. 

```{figure} Images/mass-spring2.png
---
width: 50%
name: mass-spring2
align: center
---
A mass-spring system
```

```{figure} Images/mass-spring3.png
---
width: 50%
name: mass-spring3
align: right
---
A mass-spring system
```

<br /><br />

When damping is involved, it is reasonable that the damping force is of the form $F_{\mathrm{damping}}=-c\dfrac{dx}{dt}$, where $c$ is a positive constant, called the *damping constant*. Then Newton's second law gives

$$
m\cdot\frac{d^2x}{dt^2}=-k\cdot x(t)+c\cdot\dfrac{dx}{dt}.
$$

This equation can be rewritten as

$$
 mx''(t)+cx'(t)+kx(t)=0. 
$$


<br /><br /><br /><br /><br />

::::::

## Classifications

::::::{prf:Definition}
A **differential equation** is an equation involving an unknown function and one or more of its derivatives. The order of the highest derivative involved is called the **order** of the differential equation.
::::::

In case of an unknown function of a single variable, the differential equation is called an **ordinary differential equation**. In case of an unknown function of more than one variable, the differential equation is called a **partial differential equation**.

In this book we will mostly consider ordinary differential equations. In {numref}`Sec:PartialDerivatives`, we saw some examples of partial differential equations. We also distinguish differential equations by their order. In this book we mainly focus on first-order ({numref}`Chapter:FirstorderDE`) and second-order ({numref}`Chapter:SecondorderDE`) differential equations.

For the differential equations we studied in {numref}`Subsec:DiffclassIntro`, we note that the logistic equation is a first-order differential equation and the differential equations involved in a mass-spring system are second-order differential equations.

::::::{prf:Definition}
A differential equation in a function $y(x)$ can be written as $F(x,y,y',y'',\ldots,y^{(n)})=0$. The variable $x$ is called an **independent variable**, while $y=y(x)$ is called a **dependent variable**.

A function $f(x)$ is called a **solution** of the differential equation if the equation is satisfied by $y=f(x)$, so if $F(x,f(x),f'(x),f''(x),\ldots,f^{(n)}(x))=0$.

The **general solution** of a differential equation is an expression for all solutions of the differential equation.
::::::

When we are asked to *solve* a differential equation, we are expected to find all possible solutions. However, in general it is not easy to solve a differential equation. There is no systematic approach that enables us to solve differential equations. Only when a differential equation has a specific form, we might have some techniques to find the general solution. Fortunately, checking that a certain function is a solution is much easier: simply plug in this expression into the differential equation and check whether the equation is satisfied.


::::::{prf:example}
:label: Ex:ClassDiff:Ansatz
[^FootnoteAnsatz]: The word Ansatz is the German word for approach.

For some differential equations, it is possible to find the solution by making an educated guess about the shape of the solution. Such a guess is called an **Ansatz**[^FootnoteAnsatz]. Guessing a solution might not sound very systematic to you, but due to the lack of systematic techniques we often have no other choice. And of course, the guess should be educated, since you will not get very far otherwise.

Consider, for instance, the differential equation

$$
 y''(t)=4y(t).
$$

This is an ordinary differential equation, since the unknown function $y$ only depends on $t$. It is a second-order equation, since it contains a second derivative, but no higher order derivatives. In particular, we are looking for a function $y(t)$ of which the second derivative is a multiple of the original function. We know that exponential functions have this property, so we try a function of the form $y(t)=e^{rt}$ for some, as of yet, unkown parameter $r$. Of course, not every exponential function is going to be a solution, so we should try to find out for which parameter $r$ this function is a solution. We substitute this Ansatz into the differential equation to obtain

$$
 r^2e^{rt}=4e^{rt}.
$$

We can divide by the nonzero term $e^{rt}$ to obtain the equation

$$
 r^2=4.
$$

In particular, we have two solutions $r_1=-2$ and $r_2=2$. Hence, we find that the functions $y_1(t)=e^{-2t}$ and $y_2(t)=e^{2t}$ are solutions, while any other exponential function is not a solution. It can be shown that the general solution of this differential equation is given by

$$
 y(t)=c_1e^{-2t}+c_2e^{2t}
$$

for some constants $c_1$ and $c_2$. We will see later how we can verify this.

In any case, this example shows that when we have a general idea of what a solution looks like, we can use this to find its exact shape. 

::::::

A special type of solutions (and, fortunately, the easiest type of solution) of a differential equation are the **equilibrium solutions**.

::::::{prf:definition}
:label: Def:ClassDiff:EqSol
An **equilibrium solution** of a differential equation is a solution that is constant.
::::::

You can find equilibrium solutions of a differential equation for $y(x)$ by first replacing all derivatives by zero and subsquently solving the equation for $y(x)$. Each answer should be of the form $y(x)=C$ for some constant $C$.

::::::{prf:example}
:label: Ex:ClassDiff:EqSol
Consider the differential equation

$$
 y'(t)=(y^2-4)(t+3).
$$

We want to find all equilibrium solutions of this differential equation. Since an equilibrium solution $y(t)$ is constant, it must have $y'(t)=0$ for all $t$. This means that we can find the equilibrium solutions by setting $y'(t)=0$ in the differential equation and by solving for $y$. This gives

$$
 0=(y^2-4)(t+3).
$$

From this we obtain $y^2-4=0$, which gives $y=2$ or $y=-2$. So this differential equation has two equilibrium solutions: $y(t)=2$ and $y(t)=-2$.

But wait, $t=-3$ is also solution of the equation $0=(y^2-4)(t+3)$, right? So why did we ignore this? The answer is that we are solving a differential equation for $y(t)$, so any solution should be of the form $y(t)=...$ Since $t$ is the independent variable, it can never play the role of a solution.
::::::

::::::{warning}
When finding equilibrium solutions of a differential equation for $y(t)$, any answer should be of the form $y(t)=C$ and never of the form $t=C$.
::::::

For some differential equations, it is possible to find an implicit equation for the solution. We sometimes refer to such an equation as an **implicit solution** of the differential equation. In some cases, it is not possible or feasible to obtain an explicit solution from this, as can be seen in the following example.

::::::{prf:example}
:label: Ex:ClassDiff:ImplSol
Consider the differential equation

$$
 \left(6y^5+5y^4+1\right)\frac{dy}{dx}+\cos(x)=0.
$$

Using the technieques from {numref}`Sec:ODE1:Separable` it is possible to show that any solution $y(x)$ satisfies the implicit equation 

$$
 y^6+y^5+y+\sin(x)=0.
$$

This can be verified by applying implicit differentiation (see {numref}`Subsec:ImplicitDiff`) to this implicit equation. Indeed, differentiating this equation implicitly gives

$$
 6y^5\frac{dy}{dx}+5y^4\frac{dy}{dx}+\frac{dy}{dx}+\cos(x)=0,
$$

which is the same equation as we started with. However, there are no techniques to solve the implicit equation $y^6+y^5+y+\sin(x)=0$ for $y$, so it is not possible to write an explicit solution of the form $y(x)=...$.
::::::

Furthermore, we distinguish linear and nonlinear differential equations. A differential equation $F(x,y,y',y'',\ldots,y^{(n)})=0$ is called **linear** if $F$ is a linear function of the variables $y,y',y'',\ldots,y^{(n)}$. Otherwise, the differential equation is called **nonlinear**. We will define and analyse this concept more rigorously in {numref}`Subsec:DiffclassLinear`.

In general, linear differential equations are much easier to solve than nonlinear differential equations. Especially for differential equations of order higher than one there is very limited theory for solving nonlinear differential equations. 

::::::{prf:example} 
:label: Ex:Diffclass:pendulum

An example of a physical problem that leads to a nonlinear differential equation is an oscillating pendulum.

```{figure} Images/pendulum.png
---
width: 65%
name: pendulum
align: left
---
The motion of a pendulum
```

The differential equation which represents the motion of a simple pendulum is

$$
\frac{d^2\theta}{dt^2}+\frac{g}{L}\sin(\theta)=0.
$$

Here $g$ is the acceleration due to gravity, $L$ is the length of the pendulum, and $\theta$ is
the angular displacement with respect to the equilibrium position at time $t$.

It is quite difficult to solve this differential equation. However, the linearization of the function $f(x)=\sin(x)$ at $x=0$ is

$$
L(x)=f(0)+f'(0)(x-0)=x.
$$

This implies that $\sin(x)\approx x$ for $x$ near $0$.

It turns out that it is much easier to solve the differential equation

$$
\frac{d^2\theta}{dt^2}+\frac{g}{L}\theta=0
$$

instead of the one above. In {numref}`Sec:ODE2:Homogeneous` we see how we can solve equations like this one.

::::::

The differential equations involved in a mass-spring system are all linear. These will also be solved in {numref}`Sec:ODE2:Homogeneous`.

For first-order differential equations we distinguish autonomous and nonautonomous differential equations. 

::::::{prf:Definition}
A first-order differential equation is called **autonomous** if it can be written as $F(y,y')=0$, so if the independent variable is not explicitly involved. Otherwise, the differential equation is called **nonautonomous**.
::::::

Note that the *logistic equation* is an example of an autonomous differential equation. This equation will be solved in {numref}`Sec:ODE1:Separable`.

Usually, it is directly visible whether a differential equation is autonomous or not, but it is sometimes useful to use the following criterion.

::::::{prf:theorem}
:label: Thm:ClassDiff:Autonomous
A first-order differential equation $F(x,y,y')=0$ is autonomous precisely when we have

$$
 \frac{\partial}{\partial x}F(x,y_0,y_1)=0.
$$
::::::

:::{admonition} Proof of {prf:ref}`Thm:ClassDiff:Autonomous`
:class: tudproof, dropdown
This follows immediately, since the differential equation $F(x,y,y')=0$ is autonomous precisely when $F$ does not directly depend on $x$, which happens precisely when the partial derivative with respect to $x$ is $0$.
:::

Finally, it is important to note that in many problems in practice, several quantities depend on each other and each other's derivatives. For this type of problems, a single differential equation will not suffice. Instead, you might encounter several coupled differential equations, such as

$$
 \begin{cases}y_1'=&a_1y_1+a_2y_2\\ y_2'=&b_1y_1+b_2y_2.
 \end{cases}
$$ 



This leads to a **system of first-order linear differential equations**. These systems will not be covered in this book. More information on this can be found in the [relevant section of the Open Linear Algebra book](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter9/DynSystContinuous.html) or in more advanced books on differential equations for a more thorough treatment of these systems.

(Subsec:DiffclassLinear)=

## Linear differential equations

::::::{prf:definition}
A differential equation $F(x,y,y',y'',\ldots,y^{(n)})=0$ is called **linear** if it can be written in the form

$$
 a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+...+a_1(x)y'+a_0(x)y=f(x)
$$

for some functions $a_n(x),...,a_0(x)$ and $f(x)$.

The linear differential equation above is called **homogeneous** if $f(x)=0$ for all $x$ and **nonhomogeneous** or **inhomogeneous** otherwise.
::::::


For linear differential equations there exists quite some theory. In {numref}`Sec:ODE1:Linear` we will consider and solve first-order linear differential equations.

For instance, a second-order *linear* differential equation has the form

$$
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)=G(x),
$$

where $P$, $Q$, $R$ and $G$ are continuous functions with $P(x)\neq0$. A homogeneous second-order linear differential equation has the form

$$
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)=0.
$$

We usually check that a differential equation is linear by writing it in the correct form. If you do not see how to this for a certain equation, this might suggest that the equation is nonlinear. If you want to be sure, it is advisable to use the following criterion.

::::::{prf:theorem}
:label: Thm:ClassDiff:Linear
A differential equation $F(x,y,y',y'',\ldots,y^{(n)})=0$ is linear precisely when for all $0\leq i\leq n$ and $0\leq j\leq n$ we have

$$
 \frac{\partial^2}{\partial y_i\partial y_j}F(x,y_0,...,y_n)=0.
$$
::::::

:::{admonition} Proof of {prf:ref}`Thm:ClassDiff:Linear`
:class: tudproof, dropdown
A linear equation can be written as 

$$
 a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+...+a_1(x)y'+a_0(x)y=f(x).
$$

So for this equation, we have

$$
 F(x,y_0,...,y_n)=a_n(x)y_n+a_{n-1}(x)y_{n-1}+...+a_1(x)y_1+a_0(x)y_0-f(x).
$$

Then for $0\leq j\leq n$ we have

$$
 \frac{\partial}{\partial y_j}F(x,y_0,...,y_n)=a_j(x),
$$

which gives for $0\leq i\leq n$ that

$$
 \frac{\partial^2}{\partial y_i\partial y_j}F(x,y_0,...,y_n)=0.
$$

Now suppose that $0\leq i\leq n$ and $0\leq j\leq n$ we have

$$
 \frac{\partial^2}{\partial y_i\partial y_j}F(x,y_0,...,y_n)=0.
$$

This must mean that for each $0\leq j\leq n$ the partial derivative $\dfrac{\partial}{\partial y_j}F(x,y_0,...,y_n)$ only depends on $x$, so we can write

$$
 \frac{\partial}{\partial y_j}F(x,y_0,...,y_n)=a_j(x)
$$

for some function $a_j(x)$. This then gives that

$$
 F(x,y_0,...,y_n)=a_j(x)y_j+G_j(x,y_0,...,y_{j-1},y_{j+1},...,y_n)
$$

for some function $G_j$. Since this holds for all $0\leq j\leq n$, we must have that

$$
 F(x,y_0,...,y_n)=a_n(x)y_n+a_{n-1}(x)y_{n-1}+...+a_1(x)y_1+a_0(x)y_0+g(x)
$$

for some function $g$. As such, the differential equation $F(x,y,y',y'',\ldots,y^{(n)})=0$ is linear, as desired.
:::

Apart from being easier to solve than nonlinear equations, equations that are linear and homogeneous have the important property that different solutions can be combined into a new solutions. This result is given by the following theorem.

::::::{prf:theorem} Superposition principle
:label: Thm:DE:SuperpositionPrinciple
If $y_1(x)$ and $y_2(x)$ are both solutions of a linear, homogeneous differential equation, then $y(x)=c_1y_1(x)+c_2y_2(x)$ is also a solution for each $c_1,c_2\in\mathbb{R}$.

For complex $c_1,c_2\in\mathbb{C}$, the linear combination $y(x)=c_1y_1(x)+c_2y_2(x)$ is a (possibly) complex solution of the differential equation.
::::::


::::::{admonition} Proof of {prf:ref}`Thm:DE:SuperpositionPrinciple`
:class: tudproof, dropdown
Since $y_1(x)$ and $y_2(x)$ are both solutions, we have

$$
a_n(x)y_1^{(n)}(x)+a_{n-1}(x)y_1^{(n-1)}(x)+...+a_1(x)y_1'(x)+a_0(x)y_1(x)=0
$$

and

$$
a_n(x)y_2^{(n)}(x)+a_{n-1}(x)y_2^{(n-1)}(x)+...+a_1(x)y_2'(x)+a_0(x)y_2(x)=0.
$$

Let $y(x)=c_1y_1(x)+c_2y_2(x)$, then we have

$$
\begin{align*}
&a_n(x)y^{(n)}(x)+a_{n-1}(x)y^{(n-1)}(x)+...+a_1(x)y'(x)+a_0(x)y(x)\\
&=a_n(x)\left[c_1y_1^{(n)}(x)+c_2y_2^{(n)}(x)\right]+a_{n-1}(x)\left[c_1y_1^{(n-1)}(x)+c_2y_2^{(n-1)}(x)\right]+...\\
&{}\quad{}+a_1(x)\left[c_1y_1'(x)+c_2y_2'(x)\right]+a_0(x)\left[c_1y_1(x)+c_2y_2(x)\right]\\
&=c_1\left[a_n(x)y_1^{(n)}(x)+a_{n-1}(x)y_1^{(n-1)}(x)+...+a_1(x)y_1'(x)+a_0(x)y_1(x)\right]\\
&{}\quad{}+c_2\left[a_n(x)y_2^{(n)}(x)+a_{n-1}(x)y_2^{(n-1)}(x)+...+a_1(x)y_2'(x)+a_0(x)y_2(x)\right]\\
&=c_1\cdot0+c_2\cdot0=0.
\end{align*}
$$


This proof also holds when $c_1,c_2\in\mathbb{C}$.
::::::

An important question is how we can determine if we have found all solutions of a differential equations. {prf:ref}`Thm:DE:SuperpositionPrinciple` tells us that for linear, homogeneous differential equations we can take linear combinations of solutions to build new solutions, but that still raises the question how many different solutions we need to build the general solution. For this we need the concept of linear independence.

::::::{prf:definition}
:label: Def:DE:LinearIndependent
Two functions $f(x)$ and $g(x)$ are called **linearly independent** on an interval $I$ if 

$$
c_1f(x)+c_2g(x)=0\quad\text{for all}\quad x\in I
$$

implies that $c_1=0$ and $c_2=0$.

More generally, $n$ functions $f_1(x),...,f_n(x)$ are called **linearly independent** on an interval $I$ if 

$$
c_1f_1(x)+c_2f_2(x)+...+f_n(x)=0\quad\text{for all}\quad x\in I
$$

implies that $c_1=c_2=...=c_n=0$.
::::::

Usually, showing linear independence for three or more functions is best done using techniques from linear algebra. As we do not assume a background in this field, we will stick to the linear independence of two functions in our examples.

::::::{prf:example}
:label: Ex:DE:LinearIndependentExample1
We check that the functions $x$ and $x^2$ are linearly independent on the interval $[0,1]$. Suppose that we have

$$
c_1x+c_2x^2=0
$$

for all $x$ in $[0,1]$. Since this equation holds for *all* $x$ in this interval, we are free to choose several values of $x$, which will give rise to different equations. For instance, we obtain $c_1+c_2=0$ if $x=1$ and $\frac{1}{2}c_1+\frac{1}{4}c_2=0$ if $x=\frac{1}{2}$. These two equations can only hold at the same time $c_1=0$ and $c_2=0$. This means that the two functions are linearly independent.
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

::::::{prf:example}
:label: Ex:DE:LinearIndependentExample4
The functions $e^{x-1}$ and $e^{x+1}$ are linearly dependent on $\mathbb{R}$. Indeed, we can rewrite these functions as $e^{x-1}=e^{-1}e^x$ and $e^{x+1}=ee^x$. Hence, the equation

$$
c_1e^{-1}e^x+c_2ee^x=0,\ x\in\mathbb{R}
$$

has solutions apart from $c_1=c_2=0$. Indeed, we note that $c_1=e$ and $c_2=-e^{-1}$ is also a solution for any $x$.
::::::

When we have sufficiently many linearly independent solutions of a linear, homogeneous differential equation, we can build the general solution. 

::::::{prf:theorem}
:label: Thm:DE:GeneralSolutionHomogeneous
Consider the $n$th order, linear, homogeneous differential equation

$$
 a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+...+a_1(x)y'+a_0(x)y=0.
$$

If $y_1(x),...,y_n(x)$ are linearly independent solutions on an interval, and $a_n(x)$ is never $0$
there, then the general solution is given by 

$$
 y(x)=c_1y_1(x)+c_2y_2(x)+...+c_ny_n(x),
$$

where $c_1,c_2,...,c_n$ are arbitrary constants.
::::::

In particular, you need two linearly independent solutions to find the general solution of a second-order linear, homogeneous differential equaiton, three linearly independent solutions for a third-order one, etc. We cannot prove this result yet. We will give the proof in {numref}`Sec:DE:ExistenceUniqueness`.

::::::{prf:example}
:label: Ex:Classdiff:secondordersol

Consider the differential equation

$$
 y''(t)=-y(t).
$$

Because of the second derivative, this is a second order differential equation. It is an ordinary differential equation, since the unknown function $y$ only depends on the variable $t$. In addition, the equation is linear, since it can be written as

$$
 1\cdot y''(t)+0\cdot y'(t)+1\cdot y(t)=0.
$$ 

Because the right-hand side of this equation is $0$, the differential equation is homogeneous.

If we want to find the general solution of this differential equation, we want to find all functions that satisfy this equation. That is, we look for all functions of which the second derivative is equals to minus the original function. In {numref}`Sec:ODE2:Homogeneous` we will see how you can solve this differential equation systematically, but for this particular equation it is possible to guess the solutions. Can you come up with one or more functions that satisfy this equation?

:::{admonition} Click to see the solution
:class: tudproof, dropdown
One example of a function of which the second derivative is minus the original function is $y_1(t)=\sin(t)$. Indeed, for this function we have

$$
 y_1''(t)=-\sin(t)=-y_1(t),
$$

so this function $y_1(t)$ is a solution of the differential equation. Similarly, the function $y_2(t)=\cos(t)$ is a solution, since we have


$$
 y_2''(t)=-\cos(t)=-y_2(t).
$$

By {prf:ref}`Ex:DE:LinearIndependentExample3` the functions $y_1$ and $y_2$ are linearly independent. This means that we have found two linearly independent solutions of a second order, linear, homogeneous differential equation. By {prf:ref}`Thm:DE:GeneralSolutionHomogeneous`, the general solution is given by

$$
 y(t)=c_1y_1(t)+c_2y_2(t)=c_1\sin(t)+c_2\cos(t).
$$
:::
::::::

It turns out that for solving a nonhomogeneous, linear equation, such as the second order one

$$
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)=G(x),
$$

we first need to solve the corresponding homogeneous equation, which in case of the second order equation becomes

$$
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)=0.
$$

Let us first provide some terminology before we can state how we can solve nonhomogeneous, linear differential equations.

::::::{prf:definition}
:label: Def:DE:ComplEq
For a linear, ordinary differential equation 

$$
 a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+...+a_1(x)y'+a_0(x)y=g(x)
$$

the corresponding **complementary equation** is the homogeneous equation

$$
 a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+...+a_1(x)y'+a_0(x)y=0.
$$

::::::


::::::{prf:definition}
:label: Def:DE:PartSol
A **particular solution** of a differential equation is a function without unknown constants that satisfies the differential equation.

::::::

So a particular solution is just any solution of a differential equation.

::::::{prf:theorem}
:label: Thm:DE:GeneralSolutionInhomogeneous
The general solution of the linear, ordinary differential equation 

$$
 a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+...+a_1(x)y'+a_0(x)y=g(x)
$$

can be written as $y(x)=y_c(x)+y_p(x)$, where $y_c(x)$ is the general solution of the complementary equation

$$
 a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+...+a_1(x)y'+a_0(x)y=0
$$

and $y_p(x)$ is a particular solution of the nonhomogeneous equation.

::::::

:::{admonition} Proof of {prf:ref}`Thm:DE:GeneralSolutionInhomogeneous`
:class: tudproof, dropdown
Let $y_1(x)$ be any solution of the nonhomogeneous differential equation

$$
 a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+...+a_1(x)y'+a_0(x)y=g(x).
$$

Consider the function $y_2(x)=y_1(x)-y_p(x)$. Then we evaluate

$$
\begin{align*}
&a_n(x)y_2^{(n)}(x)+a_{n-1}(x)y_2^{(n-1)}(x)+...+a_1(x)y_2'(x)+a_0(x)y_2(x)\\
&=a_n(x)\left[y_1^{(n)}(x)-y_p^{(n)}(x)\right]+a_{n-1}(x)\left[y_1^{(n-1)}(x)-y_p^{(n-1)}(x)\right]+...\\
&{}\quad{}+a_1(x)\left[y_1'(x)-y_p'(x)\right]+a_0(x)\left[y_1(x)-y_p(x)\right]\\
&=\left[a_n(x)y_1^{(n)}(x)+a_{n-1}(x)y_1^{(n-1)}(x)+...+a_1(x)y_1'(x)+a_0(x)y_1(x)\right]\\
&{}\quad{}-\left[a_n(x)y_p^{(n)}(x)+a_{n-1}(x)y_p^{(n-1)}(x)+...+a_1(x)y_p'(x)+a_0(x)y_p(x)\right]\\
&=g(x)-g(x)=0.
\end{align*}
$$

This means that $y_2(x)$ is a solution of the complementary equation. As such, we have $y_1(x)=y_2(x)+y_p(x)$, so $y_1$ is the sum of a solution of the complementary equation and the particular solution $y_p$. This means that $y_1$ is of the desired form.
:::

::::::{prf:example}
:label: Ex:Classdiff:secondordersolnonhom

Consider the differential equation

$$
 y''(t)+y(t)=1.
$$

In {prf:ref}`Ex:Classdiff:secondordersol` we saw that the general solution of the complementary equation

$$
 y''(t)+y(t)=0
$$

is given by

$$
 y_c(t)=c_1\sin(t)+c_2\cos(t).
$$

If we want to find the general solution of the nonhomogeneous equation, we need to find a particular solution. In {numref}`Sec:ODE2:Inhomogeneous`, we will see that we can find one by making the educated guess that the particular solution looks like the nonhomogeneous term $1$. In particular, we try a solution of the form $y(t)=A$ for some constant $A$. Plugging this guess into the differential equation gives

$$
 0+A=1,
$$

which means that $y_p(t)=1$ is a particular solution. By {prf:ref}`Thm:DE:GeneralSolutionInhomogeneous`, the general solution of the nonhomogeneous differential equation is given by

$$
 y(t)=y_c(t)+y_p(t)=c_1\sin(t)+c_2\cos(t)+1.
$$
::::::


## Initial-value problems

In many cases we are not interested in finding all solutions (the *general solution*), but, instead, in finding a specific solution that also satisfies some additional requirement(s). In many physical problems, in case of a first-order differential equation we need to find a particular solution that also satisfies a condition of the form $y(x_0)=y_0$. This is called an **initial condition**. The problem of finding a solution of a first-order differential equation that also satisfies such an initial condition is called an **initial-value problem**.

::::::{prf:definition}
:label: Def:ClassDiff:IVP
Consider a first order ordinary differential equation

$$
 F(x,y,y')=0
$$

and let $x_0$ in the domain of $F$. Then an equation of the form $y(x_0)=y_0$ is called an **initial condition** for the differential equation.

For a second order ordinary differential equation

$$
 F(x,y,y',y'')=0
$$

with $x_0$ in the domain of $F$, an **initial condition** is a set of equations of the form $y(x_0)=y_0$ and $y'(x_0)=y_1$.

In general, for an $n$th order ordinary differential equation

$$
 F(x,y,y',...,y^{(n)})=0
$$

with $x_0$ in the domain of $F$, an **initial condition** is a set of equations of the form 

$$
 y(x_0)=y_0,y'(x_0)=y_1,...,y^{(n-1)}(x_0)=y_{n-1}.
$$

A differential equation combined with an initial condition is called an **initial-value problem**.
::::::

In {numref}`Sec:DE:ExistenceUniqueness` it will be shown that a first-order differential equation, that satisfies certain conditions, has a general solution with one degree of freedom; somewhere in the process of solving such a differential equation we have to integrate once which gives rise to a so-called arbitrary **constant of integration**.

Then this arbitrary constant can be chosen in such a way that the solution also satisfies an initial condition of the form $y(x_0)=y_0$.

::::::{prf:example}
The differential equation $y'=3x^2$ has the general solution $y(x)=x^3+C$ with $C\in\mathbb{R}$. However, there is only one solution that also satisfies the initial condition $y(0)=0$, which is $y(x)=x^3$. This is because $y(0)=0$ leads to $0=0^3+C=C$.
::::::

::::::{prf:example}
The differential equation $y'=2y$ has the general solution $y(x)=Ce^{2x}$ with $C\in\mathbb{R}$. However, there is only one solution that also satisfies the initial condition $y(0)=3$, which is $y(x)=3e^{2x}$. This is because $y(0)=3$ leads to $3=Ce^{2\cdot0}=C$.
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
Consider the second-order linear differential equation

$$
y''+y=0.
$$

In {prf:ref}`Ex:Classdiff:secondordersol` we saw that $y(x)=c_1\sin(x)+c_2\cos(x)$ is the general solution. Now we consider the initial-value problem

$$
y''+y=0,\quad y(0)=\alpha,\quad y'(0)=\beta
$$

for some constants $\alpha$ and $\beta$. For the general solution $y(x)=c_1\sin(x)+c_2\cos(x)$ we have $y'(x)=c_1\cos(x)-c_2\sin(x)$. Then we have:

$$
\begin{cases}y(0)=\alpha\\ \\y'(0)=\beta\end{cases}\quad\Longleftrightarrow\quad\begin{cases}c_2=\alpha\\ \\c_1=\beta.\end{cases}
$$

This means that the solution of the initial-value problem is given by

$$
 y(t)=\beta\sin(x)+\alpha\cos(x).
$$

::::::

## Boundary-value problems

Instead of initial-value problems we might consider boundary-value problems, where we try to fix the solution $y(x)$ defined on some interval $[a,b]$ such that the value at the boundary points $x=a$ and $x=b$ are fixed: $y(a)=\alpha$ and $y(b)=\beta$. We could also try to fix the value of the derivative at the boundary: $y'(a)=\gamma$ and $y'(b)=\delta$, or we can even try combinations of the two.

::::::{prf:definition}
:label: Def:ClassDiff:BVP
Consider an ordinary differential equation for an unknown function $y(x)$ on an open interval $(a,b)$. A **boundary-value problem** is a combination of the differential equation and two **boundary conditions**, one at $x=a$ and $x=b$.

A boundary condition at $x_0=a$ or $x_0=b$ of the form $y(x_0)=\alpha$ is called a **Dirichlet boundary condition**. A boundary condition at $x_0=a$ or $x_0=b$ of the form $y'(x_0)=\alpha$ is called a **Neumann boundary condition**. 
::::::

Dirichlet and Neumann boundary conditions are the most common ones, but others exist. For instance, a **Robin boundary condition** at $x_0$ takes the form $c_1y(x_0)+c_2y'(x_0)=\alpha$.


In case of a first-order differential equation we only have one degree of freedom. In general, it is not possible to choose the constant of integration in such a way that both $y(a)=\alpha$ and $y(b)=\beta$ are satisfied.

::::::{prf:example}
The differential equation $y'=y$ has the general solution $y(x)=Ce^x$ with $C\in\mathbb{R}$. Now, for instance, $y(0)=\alpha$ implies that $C=\alpha$. However, this gives $y(1)=\alpha e$. This implies that the boundary-value problem

$$
y'=y,\quad y(0)=\alpha,\quad y(1)=\beta
$$

only has a (unique) solution if $\beta=\alpha e$. Otherwise, there is no solution.
::::::

Although the general solution of a second-order linear differential equation has two degrees of freedom, a corresponding boundary-value problems might have no solution, a unique solution or even infinitely many solutions. This is because if the general solution is of the form

$$
 y(t)=c_1y_1(t)+c_2y_2(t)
$$

then any combination of two boundary values gives rise to a system of linear equations for the unknown constant $c_1$ and $c_2$. Such a system can have either $0$, $1$ or infinitely many solutions..

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
\begin{cases}y''+2y=0,\quad 0<x<\pi\\ \ \y(0)=\alpha,\quad y(\pi)=\beta\end{cases}
$$

has a unique solution $y(x)=\alpha\cos(x\sqrt{2})+\dfrac{\beta-\alpha\cos(\pi\sqrt{2})}{\sin(\pi\sqrt{2})}\sin(x\sqrt{2})$.
::::::

## Grasple exercises

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
