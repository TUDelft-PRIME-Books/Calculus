(Section:Curves3d)=
# Curves in $\mathbb{R}^3$

- What is a parametrisation?
- Standard examples
- No implicit equations

In this section we cover:

- Curves in $\mathbb{R}^3$
- Parametrisation of curves
- Orientation of curves
- Closed curves
- Curvature
- Normal/binormal vector
- Torsion
- Fresnet-Serret formulas

## Introduction

In an area control center (ACC), controllers need to keep track of aircraft flying in the airspace of a certain region. For each aircraft, they need to keep track of the $3$-dimensional position of the aircraft in order to avoid collisions. The position of an aircraft at a certain time $t$ can be modelled as a $3$-dimensional vector

$$
 \mathbf{r}(t)=\begin{pmatrix}x(t)\\ y(t)\\ z(t)\end{pmatrix},
$$

where $x(t)$, $y(t)$ and $z(t)$ describe the three coordinates of the aircraft at time $t$. The trajectory of the aircraft can then be visualised as a **curve** in $\mathbb{R}^3$. We will call the vector function $\mathbf{r}(t)$ a **parametrisation** of the curve, and $t$ the **parameter**. For the aircraft, not only position but also quantities like velocity and acceleration need to be modelled as $3$-dimensional vectors that are a function of time. 

In {numref}`Section:Curves` we have studied curves in $\mathbb{R}^2$. Of course, curves play an equally important role in $\mathbb{R}^3$. In this section, we will study parameterised curves in $\mathbb{R}^3$. Several concepts can be lifted directly to the three-dimensional setting. Since having a third dimension available gives more possibilities for the direction of a curve, we will also introduce concepts such as the torsion to help us understand these possibilities.

## Curves and parametrisations

We often think of curves as lines that are not necessarily straight. In order to turn this into a more mathematical definition, we will define curves in termes of the parametrisations that describe them.

::::::{prf:definition} 
:label: Def:Curves3d:ParamCurve

A **parametric curve**, or simply **curve**, $\mathcal{C}$ in $\mathbb{R}^3$ is a set of points $(x,y,z)$ whose coordinates are given by **parametric equations** 

$$
 \begin{cases}x&=f(t),\\ y&=g(t)\\ z&=h(t)\end{cases}
$$

for $t$ in some set $I\subset\mathbb{R}$, where $f$, $g$ and $h$ are given single-variable functions called the **component functions**. Here $t$ is called a **parameter**. The vector function

$$
 \mathbf{r}(t)=\begin{pmatrix}f(t)\\ g(t)\\ h(t)\end{pmatrix},\qquad t\in I
$$

is called a **parametrisation** or **position vector** of the curve.

If $I$ is the closed interval $[a,b]$, then the point $(x,y,z)=(f(a),g(a),h(a))$ is called the **start point** or **initial point** of $\mathcal{C}$, while the point $(x,y,z)=(f(b),g(b),h(b))$ is called the **end point** or **terminal point** of $\mathcal{C}$. Whenever the start point and the end point of the curve coincide, we say that the curve is **closed**.

::::::

:::{note}
A curve in $\mathbb{R}^3$ is also known as a **space curve**, while a curve in $\mathbb{R}^2$ is known as a **planar curve**.
:::


:::{note}
A curve is the range of its parametrisation.
:::

:::{note}
A curve in $\mathbb{R}^3$ can have many different parametrisations.
:::

:::{important}
When writing down a parametrisation of a curve, you should always explicitly write down for which values of the parameter the parametric equations hold, i.e. a parametrisation can be of the form $\mathbf{r}(t)$ for $a\leq t\leq b$, but only writing $\mathbf{r}(t)$ is not enough.
:::

Unlike planar curves, space curves can typically not be described by an (implicit) equation, because a single equation usually describes a surface instead of a curve. Instead, curves can arise naturally when intersection two surfaces. We will consider this in more detail in {numref}`Section:SurfacesR3`. 

::::::{prf:example} 
:label: Ex:Curves3d:Helix
Consider the space curve $\mathcal{C}$ with parametrisation $\mathbf{r}(t)=\begin{pmatrix}4\cos(2t)\\ 4\sin(2t)\\ t\end{pmatrix}$ for $0\leq t\leq 3\pi$. We note that for $0\leq t\leq 3\pi$ we have

$$
 x(t)^2+y(t)^2=\left(4\cos(2t)\right)^2+\left(4\sin(2t)\right)^2=16\left(\cos^2(2t)+\sin^2(2t)\right)=16.
$$

[^FootnoteProj]: You can visualise a projection onto the $xy$-plane of a curve by imagining looking at the curve from above so that differences in $z$-coordinate are not visible, or by "squashing" the curve onto the $xy$-plane.

So when we project the curve onto the $xy$-plane[^FootnoteProj] we see a circle with radius $4$. According to {prf:ref}`Thm:Curves:EllipseParam`, this circle is traversed three times in counterclockwise direction, when viewed from above. In particular, the curve $\mathcal{C}$ lies on the cylinder $x^2+y^2=16$, i.e. the cylinder of which the axis is the $z$-axis and which has radius $4$. Of course, we are not only interested in what happens with $x$ and $y$, as $z$ plays an equally important role. We observe that $z$ grows linearly as a function of $t$. At $t=\pi$, $t=2\pi$ and $t=3\pi$ the position vector $\mathbf{r}(t)$ is right above the initial point $\mathbf{r}(0)$. We conclude that the curve is a *circular helix*,  that goes around the cylinder $x^2+y^2=16$ three times.

:::{todo}
Include an applet of the curve.
:::
::::::

::::::{prf:example} 
:label: Ex:Curves3d:Line
In {numref}`Sec:LinesAndPlanes` we have defined lines using a parametric vector equation. It should not come as a surprise that these lines are also curves in the sense of {prf:ref}`Def:Curves3d:ParamCurve`. For instance, we can consider the line $\mathcal{L}$ that contains the points $P=(1,2,4)$ and $Q=(5,3,1)$. In {prf:ref}`Ex:LinesAndPlanes:ParametricVectorEquationLineR3` we saw that the equation

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}=\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}+r\begin{pmatrix} 4 \\ 1 \\ -3 \end{pmatrix} \qquad \text{$r$ in $\mathbb{R}$}
$$

is a parametric vector equation of $\mathcal{L}$. This means that the equation

$$
 \mathbf{r}(r)=\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}+r\begin{pmatrix} 4 \\ 1 \\ -3 \end{pmatrix} \qquad \text{$r$ in $\mathbb{R}$}
$$

is a parametrisation of $\mathcal{L}$, which means that $\mathcal{L}$ is a space curve.
::::::

::::::{prf:example} 
:label: Ex:Curves3d:IntersectionSurface
Consider the cylinder $S$ in $\mathbb{R}^3$ given by the equation

$$
 x^2+z^2=9.
$$

This is a cylinder of radius $2$ of which the axis is the $y$-axis. In addition, we consider the plane $P$ give by the equation

$$
 2x+3y+4z=3.
$$

The intersection $\mathcal{C}$ of $S$ and $P$ is a curve in $\mathbb{R}^3$ so we let us try to find a parametrisation of $\mathcal{C}$. Inspired by the standard parametrisation for a circle (see {prf:ref}`Thm:Curves:EllipseParam`) we choose

$$
 x(t)=3\cos(t),\qquad z(t)=3\sin(t)
$$

for $0\leq t\leq 2\pi$. This way, we have 

$$
 \left(x(t)\right)^2+\left(z(t)\right)^2=9
$$

for $0\leq t\leq 2\pi$, so now matter what we choose as $y(t)$, the curve will lie on the cylinder $S$. In order to ensure that it also lies on the plane $P$, we plug in our chosen expressions for $x(t)$ and $y(t)$ to obtain

$$
 6\cos(t)+3y+12\sin(t)=3.
$$

We can then solve for $y$ to find

$$
 y=1-2\cos(t)-4\sin(t).
$$

As such, we find that $\mathbf{r}(t)=\begin{pmatrix}3\cos(t)\\ 1-2\cos(t)-4\sin(t)\\ 3\sin(t)\end{pmatrix}$ for $0\leq t\leq 2\pi$ is a parametristion of the curve of intersection $\mathcal{C}$. Of course, there are many other parametrisations possible for this curve.

:::{todo}
Include an applet showing $S$, $P$ and $\mathcal{C}$, preferable with a slider (or something) moving $t$ along the curve.
::::::

We like to think of curves as lines that are not necessarily straight. However, more sets are curves than you might think initially. For instance, there exist closed planar curves, with a continuous parametrisation, which fill up the entire filled square $\left\{(x,y)\in\mathbb{R}^2\middle|0\leq x\leq 1,0\leq y\leq 1\right\}$. Such a curve is known as a [space-filling curve](https://en.wikipedia.org/wiki/Space-filling_curve). We will not delve deeper into these space-filling curves, but it is useful to realise that they exist.


