(Section:Curves3d)=
# Curves in $\mathbb{R}^3$



## Introduction

In an area control center (ACC), controllers need to keep track of aircraft flying in the airspace of a certain region. For each aircraft, they need to keep track of the $3$-dimensional position of the aircraft in order to avoid collisions. The position of an aircraft at a certain time $t$ can be modelled as a $3$-dimensional vector

$$
 \mathbf{r}(t)=\begin{pmatrix}x(t)\\ y(t)\\ z(t)\end{pmatrix},
$$

where $x(t)$, $y(t)$ and $z(t)$ describe the three coordinates of the aircraft at time $t$. The trajectory of the aircraft can then be visualised as a **curve** in $\mathbb{R}^3$. We will call the vector function $\mathbf{r}(t)$ a **parametrisation** of the curve, and $t$ the **parameter**. For the aircraft, not only position but also quantities like velocity and acceleration need to be modelled as $3$-dimensional vectors that are a function of time. 

In {numref}`Sec:CurvesR2` we have studied curves in $\mathbb{R}^2$. Of course, curves play an equally important role in $\mathbb{R}^3$. In this section, we will study parameterised curves in $\mathbb{R}^3$. Most concepts can be lifted directly from the two-dimensional to the three-dimensional setting. As such, we will strongly use the same set-up as in {numref}`Sec:CurvesR2` here.

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
A curve in $\mathbb{R}^3$ is also known as a **space curve**.
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

::::::{note}

A parametrisation is allowed to cover (some parts of) a curve several times. For instance, the parametrisation

$$
 \mathbf{r}(t)=\begin{pmatrix}\cos(t)\\ \sin(t)\\ 0\end{pmatrix}\qquad 0\leq t<4\pi
$$

covers each point on the circle $x^2+y^2=1,z=0$ twice. However, there are situations where you want to avoid these type of parametrisations (for instance, when evaluating the arc length of a curve, see {numref}`Section:ArcLength`), so always be careful when using one.

::::::


In some cases, it is important to specify that a parametrisation covers each point of the curve exactly once, where an exception is always made for the start and end point of a closed curve. For these cases, we have the following definition.

::::::{prf:definition} 
:label: Def:Curves3d:SelfIntersect
Let $\mathcal{C}$ be a space curve with paramametrisation $\mathbf{r}(t)$ for $t\in I$. 

If $\mathcal{C}$ is not closed, we say that $\mathcal{C}$ is **simple** or **non-self intersecting** when for all $t_1,t_2\in I$ with $t_1\neq t_2$ we have $\mathbf{r}(t_1)\neq\mathbf{r}(t_2)$; otherwise $\mathcal{C}$ **self-intersects**. 

If $I=[a,b]$ and $\mathcal{C}$ is closed, we say that $\mathcal{C}$ is **simple** or **non-self intersecting** when for all $t_1,t_2\in [a,b)$ with $t_1\neq t_2$ we have $\mathbf{r}(t_1)\neq\mathbf{r}(t_2)$; otherwise $\mathcal{C}$ **self-intersects**.
::::::




::::::{prf:example} 
:label: Ex:Curves3d:Helix
Consider the space curve $\mathcal{C}$ with parametrisation $\mathbf{r}(t)=\begin{pmatrix}4\cos(2t)\\ 4\sin(2t)\\ t\end{pmatrix}$ for $0\leq t\leq 3\pi$. We note that for $0\leq t\leq 3\pi$ we have

$$
 x(t)^2+y(t)^2=\left(4\cos(2t)\right)^2+\left(4\sin(2t)\right)^2=16\left(\cos^2(2t)+\sin^2(2t)\right)=16.
$$

[^FootnoteProj]: You can visualise a projection onto the $xy$-plane of a curve by imagining looking at the curve from above so that differences in $z$-coordinate are not visible, or by "squashing" the curve onto the $xy$-plane.

So when we project the curve onto the $xy$-plane[^FootnoteProj] we see a circle with radius $4$. According to {prf:ref}`Thm:CurvesR2:EllipseParam`, this circle is traversed three times in counterclockwise direction, when viewed from above. In particular, the curve $\mathcal{C}$ lies on the cylinder $x^2+y^2=16$, i.e. the cylinder of which the axis is the $z$-axis and which has radius $4$. Of course, we are not only interested in what happens with $x$ and $y$, as $z$ plays an equally important role. We observe that $z$ grows linearly as a function of $t$. At $t=\pi$, $t=2\pi$ and $t=3\pi$ the position vector $\mathbf{r}(t)$ is right above the initial point $\mathbf{r}(0)$. We conclude that the curve is a *circular helix*,  that goes around the cylinder $x^2+y^2=16$ three times. Since each point on the curve is only covered once by the parametrisation, the curve is simple.

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

is a parametric vector equation of $\mathcal{L}$. In the terminology of this section, we have that

$$
 \mathbf{r}(r)=\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}+r\begin{pmatrix} 4 \\ 1 \\ -3 \end{pmatrix} \qquad \text{$r$ in $\mathbb{R}$}
$$

is a parametrisation of $\mathcal{L}$, which means that $\mathcal{L}$ is a space curve.
::::::

Unlike planar curves, space curves can typically not be described by an (implicit) equation, because a single equation usually describes a surface instead of a curve. We will consider this in more detail in {numref}`Section:ImplicitEquationsR3`.  Instead, curves can arise naturally when intersection two surfaces, as can be seen from the following examples. 

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

The intersection $\mathcal{C}$ of $S$ and $P$ is a curve in $\mathbb{R}^3$ so we let us try to find a parametrisation of $\mathcal{C}$. Inspired by the standard parametrisation for a circle (see {prf:ref}`Thm:CurvesR2:EllipseParam`) we choose

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
:::

::::::


::::::{prf:example} 
:label: Ex:Curves3d:IntersectionSurface
We let $\mathcal{C}$ denote the curve of intersection of the two surfaces $S_1$, given by

$$
 3x^3+2y-z=4,
$$

and $S_2$, given by

$$
 4y-xz=3.
$$

It is not immediately obvious how we should paramterise this curve. It pays off to first eliminate one of the variables. Since in both equations, we only see constant multiples of $y$, we can subtract two times the equation for $S_1$ from the one for $S_2$ to obtain the equation

$$
 -6x^3+2z-xz=-5,
$$

which does not feature $y$. In the resulting equation, it is easier to write $z$ as a function of $x$ than the other way around. As such, we choose $x=t$, which then gives

$$
 -6t^3+2z-tz=-5.
$$

We can factor out the $z$ and rewrite to obtain

$$
 z(2-t)=-5+6t^3,
$$

which gives

$$
 z=\frac{-5+6t^3}{2-t}.
$$

As the final step, we plug out expressions for $x$ and $z$ into the equation for $S_2$ to find

$$
 y=\frac{3}{4}+\frac{1}{4}xz=\frac{3}{4}+\frac{-5t+6t^4}{8-4t}.
$$

We then obtain the parametrisation

$$
 \mathbf{r}(t)=\begin{pmatrix}t\\[0.2cm] \dfrac{3}{4}+\dfrac{-5t+6t^4}{8-4t}\\[0.3cm] \dfrac{-5+6t^3}{2-t}\end{pmatrix},
$$

which is defined for $t\neq 2$. This suggests that there is no point on the curve corresponding to $t=2$, i.e. a point with $x=2$.

We should check now this is indeed the case. Substituting $x=2$ in the equation for $S_1$ gives

$$
 24+2y-z=4,
$$

which gives

$$
 z=2y+20.
$$

In the equation for $S_2$ we obtain

$$
 4y-2z=3,
$$

which gives

$$
 z=2y+\frac{3}{2}.
$$

Since the lines $\begin{cases}z&=2y+20\\ x&=2\end{cases}$ and $\begin{cases}z&=2y+\frac{3}{2}\\ x&=2\end{cases}$ have the same direction vector, but do not coincide, they are parallel, so they do not intersect. So there is, indeed, no point on $\mathcal{C}$ with $x=2$.

So the curve $\mathcal{C}$ consists of two branches: one for parameter values $t<2$ and one for parameter values $t>2$. This can also be seen when plotting the curve.

:::{todo}
Include an applet with $S_1$, $S_2$ and $\mathcal{C}$.
:::
::::::


