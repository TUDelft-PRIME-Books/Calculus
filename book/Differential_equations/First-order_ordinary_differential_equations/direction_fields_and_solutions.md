# Slope fields

## Introduction

For certain classes of first-order differential equations, such as separable (see {numref}`Sec:ODE1:Separable`), linear (see {numref}`Sec:ODE1:Linear`) or exact (see {numref}`Sec:ODE1:Exact`) differential equations, there are general techniques to solve these equations. Still, performing these techniques might not always be easy, or even possible, for specific differential equations, for instance because we might encounter integrals that we cannot evaluate by hand. Or even worse, we might enounter a differential equation that is not of one of the mentioned types. In those cases it may be impossible to find the solution analytically.

However, in practice it is often sufficient to only know the **qualitative** behaviour of the solution, instead of having a **quantitative** expression for the solution. In this section, we introduce a common way to obtain this qualitative behaviour without solving the differential equation.
 
## Slope fields

We consider a first-order differential equation of the form 

$$
 y'(t)=F(t,y).
$$

If $(t_0,y_0)$ is a point in the domain of $F$, we can evaluate $F(t_0,y_0)$. Let $y_*$ be the solution of the differential equation that satisfies $y_*(t_0)=y_0$. The fact that $y_*$ is a solution of the differential equation means that we must have

$$
 y_*'(t_0)=F(t_0,y_0).
$$

This means that we know that the **slope** $y_*'$ of $y_*$ at this point equals $F(t_0,y_0)$, without knowing what the graph of the solution $y_*$ itself looks like. 

So how can we use this to sketch the qualitative behaviour of solutions of the differential equation? A common way is to draw a very short arrow or a line segment at the point $(t_0,y_0)$ with slope $F(t_0,y_0)$. This arrow or line segment will then be tangent to the graph of the actual solution $y_*$ at that point. If we do this at a grid of points, we get a good idea of how the solutions behave qualitatively. This gives rise to the following definition.

::::::{prf:definition}
:label: Def:ODE1SF:SF
A **slope field** (or **direction field**) of a first-order differential equation of the form $y'=F(t,y)$ is a grid of points with arrows in the direction

$$
 \begin{pmatrix} 1\\ F(t,y)\end{pmatrix}.
$$

At each point $(t,y(t))$ on the graph of a solution $y(t)$ of the differential equation, these arrows are tangent to the graph of $y(t)$.
::::::

If we have sketched a direction field on a sufficiently fine grid (or better, let a computer do this for us), we can use this to sketch graphs of solutions. Indeed, the arrows should be tangent to the graph of the solution that goes through the point. So if we follow the arrows, we obtain a sketch of the graph of a solution.

::::::{prf:example}
Consider the differential equation $\dfrac{dy}{dt}=t+y$. We want to sketch a slope field for this differential equation. For this, we first choose any point, say the point $(t,y)=(0,1)$. Then we compute that the slope of the solution at that point should be

$$
 \left.\frac{dy}{dt}\right|_{(t,y)=(0,1)}=0+1=1.
$$

We draw a short line segment with slope $1$ at the point $(0,1)$. This gives the following figure.

:::{todo}
Include a version of {numref}`Fig:ODE1Slope:DF1` with only the line segment through $(0,1)$. The horizontal axis should be $t$ instead of $x$. Maybe arrows instead of line segments? Should also be adjusted in the text in that case.
:::

Just one line segment is, of course, not enough to determine the qualitative behaviour of solutions of this differential equation. So we repeat this procedure on a grid of points to obtain the following slope field.


:::{figure} Images/direction1.png
:name: Fig:ODE1Slope:DF1
:class: dark-light

A slope field for the differential equation $\dfrac{dy}{dt}=t+y$. 
:::

:::{todo}
Turn {numref}`Fig:ODE1Slope:DF1` into an applet. Make sure the horizontal axis is labeled $t$ instead of $x$. Maybe arrows instead of line segments? Should also be adjusted in the text in that case.
:::

We can now try to sketch the graph of the solution that satisfies the initial condition $y(0)=1$, i.e. the solution that goes through the point $(t,y)=(0,1)$. For this, we follow the direction in the slope field, both forward and backward. This gives the following sketch of the graph of the solution.


:::{figure} Images/direction2.png
:name: Fig:ODE1Slope:DF1sol
:class: dark-light

A slope field for the differential equation $\dfrac{dy}{dt}=t+y$ with the graph of the solution with $y(0)=1$ sketched in the slope field.
:::

:::{todo}
Turn {numref}`Fig:ODE1Slope:DF1sol` into an applet. Make sure the horizontal axis is labeled $t$ instead of $x$. Maybe arrows instead of line segments? Should also be adjusted in the text in that case.
:::
::::::

::::::{prf:example}
Consider the differential equation $\dfrac{dy}{dx}=x^2+y^2-1$. Then we can find its slope field by taking a grid of points and for each point $(x,y)$ on the grid, computing the slope $\dfrac{dy}{dx}$ as $x^2+y^2-1$. For instance, at the point $(x,y)=(0,2)$ we have the slope

$$
 \left.\frac{dy}{dx}\right|_{(x,y)=(0,2)}=0^2+2^2-1=3.
$$

This gives the following slope field.

:::{figure} Images/direction6.png
:name: Fig:ODE1Slope:DF2sol
:class: dark-light

A slope field for the differential equation $\dfrac{dy}{dx}=x^2+y^2-1$ with the graphs of the solutions with $y(0)=k$ for $k$ in $\{-2,-1,0,1,2\}$ sketched in the slope field.
:::

:::{todo}
Turn {numref}`Fig:ODE1Slope:DF2sol` into an applet. Maybe arrows instead of line segments? 
:::
::::::

In {numref}`Sec:DE:Intro` we introduced the concept of an **equilibrium solution** of a differential equation, i.e. a constant solution. We saw how we can find equilibrium solutions, but can we also recognise them in a slope field? Fortunately, this is not very hard. Indeed, if $y(t)=k$ is an equilibrium solution of the first-order differential equation, then for all $t$ we have 

$$
 \left.\frac{dy}{dt}\right|_{(t,y)=(t,k)}=0.
$$

So in a slope field, we would draw a line segment with slope $0$, i.e. a horizontal line segment. In particular, an equilibrium solution always gives a horizontal line of horizontal arrows. And reversely, a horizontal line of horizontal arrows must always correspond to an equilibrium solution.

::::::{prf:example}
Consider a first-order differential equation with the following slope field.

:::{todo}
Include the slope field of $y'=(y+1)(y-2)(y+t-1)$. Do not state the differential equation. Include a toggle that when clicked, shows the equilibrium solutions $y=-1$ and $y=2$.
:::

Can we identify the equilibrium solutions in this slope field? Since equilibrium solutions correspond to horizontal lines of horizontal arrows, we conclude that $y=-1$ and $y=2$ must be equilibrium solutions. Note that there are other arrows that are horizontal, such as at $(t,y)=(0,1)$, but since other arrows on the horizontal line through this arrow are not horizontal, this does not correspond to an equilibrium solution.
::::::


