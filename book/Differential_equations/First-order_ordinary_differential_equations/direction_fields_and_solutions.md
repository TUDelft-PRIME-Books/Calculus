# Slope fields

## Introduction

For certain classes of first-order differential equations, such as separable (see {numref}`Sec:ODE1:Separable`), linear (see {numref}`Sec:ODE1:Linear`) or exact (see {numref}`Sec:ODE1:Exact`) differential equations, there are general techniques to solve these equations. Still, for specific differential equations, performing these techniques might not always be easy, or even possible, for instance because we might encounter integrals that we cannot evaluate by hand. Or even worse, we might encounter a differential equation that is not of one of the mentioned types. In those cases it may be impossible to find the solution analytically.

However, in practice it is often sufficient to only know the **qualitative** behaviour of the solution, instead of having a **quantitative** expression for the solution. In this section, we introduce a common way to obtain this qualitative behaviour without solving the differential equation (or before solving it, if that is possible).
 
## Slope fields

[^Footnoteform]: Not all first-order differential equations are of this form, but for those that are not of this form it is usually not possible to draw a slope field.

We consider a first-order differential equation of the form[^Footnoteform] 

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

:::{note}
In some cases, especially when we want to draw a lot of directions in a slope field, it is more convenient to draw line segments instead of arrows. In that case, we can draw a line segment with slope $F(t,y)$ at each point $(t,y)$ in the grid.
:::

If we have sketched a direction field on a sufficiently fine grid (or better, let a computer do this for us), we can use this to sketch graphs of solutions. Indeed, the arrows should be tangent to the graph of the solution that goes through the point. So if we follow the arrows, we obtain a sketch of the graph of a solution.

::::::{prf:example}
:label: Ex:ODE1Slope:DF1
Consider the differential equation $\dfrac{dy}{dt}=t+2y$. We want to sketch a slope field for this differential equation. For this, we first choose any point, say the point $(t,y)=(0,1)$. This means that our technique will approximate the solution with initial condition $y(0)=1$. Then we compute that the slope of the solution at that point should be

$$
 \left.\frac{dy}{dt}\right|_{(t,y)=(0,1)}=0+2\cdot1=2.
$$

We draw a short arrow with slope $2$ at the point $(0,1)$. This gives the figure in {numref}`Fig:ODE1Slope:DF1` below.

:::{applet}
:url: calculus/slope_fields/building_a_slope_field
:name: Fig:ODE1Slope:DF1
:class: dark-light

This figure shows the following stages of the construction of a slope field for the differential equation $\dfrac{dy}{dt}=t+2y$: \
(1) (_initial_) An initial arrow at the point $(0,1)$. \
(2) An additional arrow at the point $(0,2)$. \
(3) Several more arrows along the $y$-axis. \
(4) Several more arrows along the vertical line $t=1$. \
(5) (_final_) The complete slope field.
:::

Just one arrow, of course, not enough to determine the qualitative behaviour of solutions of this differential equation. So we repeat this procedure on a grid of points to obtain a complete slope field:

1. We first add an arrow at the point $(t,y)=(0,2)$, which has slope $4$.
2. Then arrows at several more points along the $y$-axis, such as $(0,3)$ with slope $6$, $(0,4)$ with slope $8$, etc.
3. Then we add arrows at several points along the vertical line $t=1$, such as $(1,0)$ with slope $1$, $(1,1)$ with slope $3$, $(1,2)$ with slope $5$, etc.
4. We continue this procedure for several more vertical lines, until we have a complete slope field.

In {numref}`Fig:ODE1Slope:DF1` you can use the buttons to see the construction of the slope field step by step. This finally results in the complete slope field for the differential equation $\dfrac{dy}{dt}=t+2y$ shown in {numref}`Fig:ODE1Slope:DF1final` below.

:::{applet}
:url: calculus/slope_fields/a_slope_field
:name: Fig:ODE1Slope:DF1final
:class: dark-light

A slope field for the differential equation $\dfrac{dy}{dt}=t+2y$.
:::

We can now try to sketch the graph of the solution that satisfies the initial condition $y(0)=1$, i.e. the solution that goes through the point $(t,y)=(0,1)$. For this, we follow the direction in the slope field, first forward and then backward, see {numref}`Fig:ODE1Slope:DF1sol`.

:::{applet}
:url: calculus/slope_fields/sketching_in_a_slope_field
:name: Fig:ODE1Slope:DF1sol
:class: dark-light

This figure shows the following stages of the sketching a solution in a slope field for the differential equation $\dfrac{dy}{dt}=t+2y$: \
(1) (_initial_) The initial point $(0,y(0))$. \
(2) The sketch of the solution curve for $t\geq0$. \
(3) (_final_) The sketch of the solution curve for all $t$. \
You can also drag the initial point to see how the solution changes.
:::

In {numref}`Sec:ODE1:Linear` we will see a technique that allows us to obtain the exact solution 

$$
 y(t)=\dfrac{5}{4}e^{2t}-\frac{t}{2}-\frac{1}{4}
$$

of this initial-value problem. You can see that we found the linearly decreasing behaviour for negative $t$ (the exponential is very small for negative $t$ compared to the linear term), and the exponentially increasing behaviour for positive $t$, just by a careful sketch of the slope field.

::::::

::::::{prf:remark}
The idea of sketching solutions of differential equations by following the arrows in a slope field forms the basis of the technique called the Forward Euler method, which is used to approximate solutions of differential equations. We will study this technique in {numref}`Sec:DE:Num`.
::::::

::::::{prf:example}
:label: Ex:ODE1Slope:DF2

Consider the differential equation $\dfrac{dy}{dx}=4x^3-y^3-3$. Then we can find its slope field by taking a grid of points and for each point $(x,y)$ on the grid, computing the slope $\dfrac{dy}{dx}$ as $4x^3-y^3-3$. For instance, at the point $(x,y)=(0,2)$ we have the slope

$$
 \left.\frac{dy}{dx}\right|_{(x,y)=(0,2)}=4\cdot 0^3-2^3-3=-11.
$$

This gives the following slope field in {numref}`Fig:ODE1Slope:DF2sol` below. We also added the graph of the solution with initial condition $y(0)=0$ to this slope field. Investigate how the solution changes when you change the initial condition $y(0)=k$ by dragging the point to change $k$ in $[-2,2]$ in steps of $0.1$.

:::{applet}
:url: calculus/slope_fields/solutions_in_a_slope_field
:name: Fig:ODE1Slope:DF2sol
:class: dark-light

A slope field for the differential equation $\dfrac{dy}{dx}=4x^3-y^3-3$ with the graphs of the solutions with $y(0)=k$ with $k=0$ initially. You can drag the point to change the initial condition with $k$ in $[-2,2]$ in steps of $0.1$.
:::

::::::

## Equilibrium solutions

In {numref}`Sec:DE:Intro` we introduced the concept of an **equilibrium solution** of a differential equation, i.e. a constant solution $y=c$. We saw how we can find equilibrium solutions, but can we also recognise them in a slope field? Fortunately, this is not very hard. Indeed, if $y(t)=k$ is an equilibrium solution of the first-order differential equation, then for all $t$ we have 

$$
 \left.\frac{dy}{dt}\right|_{(t,y)=(t,k)}=0.
$$

So in a slope field, we would draw a line segment with slope $0$, i.e. a horizontal line segment. In particular, an equilibrium solution always gives a horizontal line of horizontal arrows. And reversely, a horizontal line of horizontal arrows must always correspond to an equilibrium solution.

::::::{prf:example}
:label: Ex:ODE1Slope:DF3

Consider a first-order differential equation with the slope field shown in {numref}`Fig:ODE1Slope:DF3sol`. Can you identify the equilibrium solutions in this slope field?

:::{applet}
:url: calculus/slope_fields/equilibrium_solutions_in_a_slope_field
:name: Fig:ODE1Slope:DF3sol
:class: dark-light

A slope field for a differential equation with the graphs of the solutions with $y(0)=k$ with $k=0$ initially. You can drag the point to change the initial condition with $k$ in $[-2,2]$ in steps of $0.1$.
:::

Since equilibrium solutions correspond to horizontal lines of horizontal arrows, we conclude that $y=-1$ and $y=2$ must be equilibrium solutions. Note that there are other arrows that are horizontal, such as at $(t,y)=(0,1)$, but since other arrows on the horizontal line through this arrow are not horizontal, this does not correspond to an equilibrium solution. It merely tells us that the graph of the solution that goes through $(t,y)=(0,1)$ has a horizontal tangent line at that point.
::::::

::::::{prf:example} Population growth
:label: Ex:ODE1Slope:population
In {prf:ref}`Ex:Diffclass:population` we studied the logistic equation

$$
 \frac{dP}{dt}=kP\left(1-\frac{P}{M}\right).
$$

Let us draw the slope field and see if we can find (and interpret) the equilibrium solutions.

:::{todo} Include the slope field here, preferrably with draggable k,M.
:::

Since equilibrium solutions correspond to horizontal lines of horizontal arrows, we conclude that $P=0$ and $P=M$ must be equilibrium solutions. We recall that $P(t)$ represents the size of the poluation at time $t$. As such, the equilibrium solution $P=0$ corresponds to extinction of the species: if we start off with no popuation, we will never have any population. The other equilibrium at $P=M$ represents the maximal population size that the enviornment can sustain. In this state, the birth and death rates will cancel out each other.
::::::

## Grasple exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2e5c4c1c-bbc7-4661-bf38-a8de2ddaa7b9?id=122356
:label: Grasple:122356
:dropdown:
:description: Match the differential equation with its slope field.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/70155ec5-7a46-4ec6-9a5c-e6de23aa60c8?id=63841
:label: Grasple:63841
:dropdown:
:description: Match the differential equation with its slope field.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fcc2d727-b755-400b-a653-a37faa84a18f?id=122357
:label: Grasple:122357
:dropdown:
:description: Match the differential equation with its slope field.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2edfedd7-b232-4359-af53-d296885d282d?id=122358
:label: Grasple:122358
:dropdown:
:description: Match the differential equation with its slope field.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/91a1abec-3a93-496e-9493-39a6dede34f6?id=122359
:label: Grasple:122359
:dropdown:
:description: Match the differential equation with its slope field.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a810fa0b-7227-4fc0-9c6a-958a94931f8c?id=122360
:label: Grasple:122360
:dropdown:
:description: Match the differential equation with its slope field.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f0d7f9b3-9f25-44cf-ac27-17aeda047d6d?id=122361
:label: Grasple:122361
:dropdown:
:description: Match the differential equation with its slope field.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/35da40cc-8c12-4fec-97e7-85d2129bd92a?id=122362
:label: Grasple:122362
:dropdown:
:description: Match the differential equation with its slope field.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a9633335-5d34-4a01-865f-9107dd2352a0?id=122363
:label: Grasple:122363
:dropdown:
:description: Match the differential equation with its slope field.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8990dee9-f2fb-43d9-95bd-c6684181a9a1?id=63822
:label: Grasple:63822
:dropdown:
:description: Match the slope field with its differential equation.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2d2ce4f3-9f93-4be8-b5c6-a5bc13e1104f?id=116693
:label: Grasple:116693
:dropdown:
:description: Match the slope field with its differential equation.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4c063499-111c-47c3-8160-4ee7d7684b8e?id=78809
:label: Grasple:78809
:dropdown:
:description: Match the slope field with its differential equation.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/17f0e668-9463-48e4-b954-472a49480220?id=78811
:label: Grasple:78811
:dropdown:
:description: Finding tangent line to a solution.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b416b50f-04d5-42f2-9e32-291a4d3d59ec?id=63827
:label: Grasple:63827
:dropdown:
:description: Defining and finding an isocline.
::::::

