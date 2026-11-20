(Sec:CurvesR2)=

# Curves in $\mathbb{R}^2$

## Introduction

In {numref}`Section:Curves` we have seen that we can describe the unit circle using the (implicit) equation

$$
 x^2+y^2=1.
$$

We can also take a look at the unit circle from a different perspective. Imagine a particle starting at the point $(1,0)$ and moving around the circle in counterclockwise direction. At time $t$, the particle has a certain position $(x,y)$ on the circle. Since for each $t$, the particle has a unique $x$- and $y$-coordinate, we note that the $x$ and $y$ coordinates of the particle are functions of $t$, so we can write 

$$
 \left\{\begin{array}{lcl}x&=&f(t),\\ y&=&g(t),\end{array}\right.
$$

The equations $x=f(t),y=g(t)$ are called a **parametric equation** for the circle and $t$ is called a **parameter**. Alternatively, we say that we made a **parametrisation** of the circle. So what could these functions $f$ and $g$ be? It turns out that a single curve can have many different parametrisations. This is because the particle can move around the circle at different speeds, or even at a non-constant speed. As such, we have a lot of freedom in choosing our parametrisation. Still, some parametrisations are more useful than others. In order to find one for the circle, we recall from {numref}`Fig:Trigonometry:UnitCircleStandardValues` that each point $(x,y)$ on the unit circle can be represented as $x=\cos(t)$ and $y=\sin(t)$, where $t$ is the angle with respect to the positive $x$-axis. In order to obtain each point on the circle exactly once we should have, for instance, $0\leq t<2\pi$. This means that the equations

$$
 \left\{\begin{array}{lcl}x&=&\cos(t),\\ y&=&\sin(t),\end{array}\right.\qquad 0\leq t<2\pi
$$

are a set of parametric equations for the unit circle. Indeed if $(x,y)=(\cos(t),\sin(t))$, then we find that

$$
 x^2+y^2=\left(\cos(t)\right)^2+\left(\sin(t)\right)^2=1,
$$ 

so that, indeed, the point $(x,y)=(\cos(t),\sin(t))$ lies on the unit circle. 


:::{applet}
:url: calculus/curves_in_R%5E2/parametrisation_of_the_unit_circle
:name: Fig:Curves:CircleParam
:class: dark-light

The parametrisation $x=\cos(t)$ and $y=\sin(t)$ for $0\leq t<2\pi$ describes the unit circle.
:::

In this section, we will study all sorts of curves that can be described by means of a parametrisation. We will also provide parametrisations for the special curves that we studied in {numref}`Section:Curves`: ellipses, hyperbolas and parabolas.

## Curves and paramterisations

Intuitively, a curve is a line that is not necessarily straight. This is also how we used the concept of a curve in {numref}`Section:Curves`. However, turning that definition into something mathematical can be a bit tricky. Instead, we will define a curve in $\mathbb{R}^2$ as a set of points that satisfies a pair of parametric equations. 

::::::{prf:definition} 
:label: Def:Curves2d:ParamCurve

A **parametric curve**, or simply **curve**, $\mathcal{C}$ in $\mathbb{R}^2$ is a set of points $(x,y)$ whose coordinates are given by **parametric equations** 

$$
 \begin{cases}x&=f(t),\\ y&=g(t)\end{cases}
$$

for $t$ in some set $I\subset\mathbb{R}$, where $f$ and $g$ are given single-variable functions called the **component functions**. Here $t$ is called a **parameter**. The vector function

$$
 \mathbf{r}(t)=\begin{pmatrix}f(t)\\ g(t)\end{pmatrix},\qquad t\in I
$$

is called a **parametrisation** or **position vector** of the curve.

If $I$ is the closed interval $[a,b]$, then the point $(x,y)=(f(a),g(a))$ is called the **start point** or **initial point** of $\mathcal{C}$, while the point $(x,y)=(f(b),g(b))$ is called the **end point** or **terminal point** of $\mathcal{C}$. Whenever the start point and the end point of the curve coincide, we say that the curve is **closed**.

::::::

:::{note}
A curve in $\mathbb{R}^2$ is also known as a **planar curve**.
:::


:::{note}
A curve is the range of its parametrisation.
:::


::::::{note}

A curve can have many different parametrisations.

::::::

::::::{note}

A parametrisation is allowed to cover (some parts of) a curve several times. For instance, the parametrisation

$$
 \mathbf{r}(t)=\begin{pmatrix}\cos(t)\\ \sin(t)\end{pmatrix}\qquad 0\leq t<4\pi
$$

covers each point on the unit circle twice. However, there are situations where you want to avoid these type of parametrisations (for instance, when evaluating the arc length of a curve, see {numref}`Section:ArcLength`), so always be careful when using one.

::::::

::::::{important}
:name: Important:Curves:tInterval

When writing down a parametrisation of a curve, you should always explicitly write down for which values of the parameter the parametric equations hold, i.e. a parametrisation can be of the form $\mathbf{r}(t)$ for $a\leq t\leq b$, but only writing $\mathbf{r}(t)$ is not enough.

::::::


We like to think of curves as lines that are not necessarily straight. However, more sets are curves than you might think initially. For instance, there exist closed planar curves, with a continuous parametrisation, which fill up the entire filled square $\left\{(x,y)\in\mathbb{R}^2\middle|0\leq x\leq 1,0\leq y\leq 1\right\}$. Such a curve is known as a [space-filling curve](https://en.wikipedia.org/wiki/Space-filling_curve). We will not delve deeper into these space-filling curves, but it is useful to realise that they exist.


::::::{prf:example} 
:label: Ex:CurvesR2:Curve1

Consider the curve $\mathcal{C}$ that is defined by the parametrisation $\mathbf{r}(t)=\begin{pmatrix} -1+t\\ t^2-3t\end{pmatrix}$ for $0\leq t\leq 1$. In order to determine which curve we are dealing with, we first draw the curve by computing the values of $x$ and $y$ for several values of $t$. This gives the following result.

:::{applet}
:url: calculus/curves_in_R%5E2/parametrisation_of_quadratic_function
:name: Fig:Curves:Curve1
:class: dark-light

The graph of the curve defined by the parametrisation $\mathbf{r}(t)=\begin{pmatrix} -1+t\\ t^2-3t\end{pmatrix}$ for $0\leq t\leq 1$.
:::

Note that in the figure, the parameter $t$ is not directly visible. Indeed, each value of $t$ gives a point $(x,y)=(-1+t,t^2-3t)$ on the curve. The interpretation of this parameter is that we consider a particle that starts at the initial point of the curve and is at position $(x,y)=(-1+t,t^2-3t)$ at time $t$.

This graph suggest that we might be dealing with a part of the graph of a quadratic function, i.e. that $y=ax^2+bx+c$ for some constants $a$, $b$ and $c$. Indeed, we note that $x$ depends linearly on $t$, while $y$ depends quadratically on $t$. We can now try to find the values of these constants $a$, $b$ and $c$ by substituting the expressions $x=-1+t$ and $y=t^2-3t$ into the equation $y=ax^2+bx+c$. This gives

$$
 t^2-3t=y=ax^2+bx+c=a\left(-1+t\right)^2+b\left(-1+t\right)+c=at^2+\left(-2a+b\right)t+a-b+c.
$$

Two quadratic expressions in $t$ can only be equal when the coefficients for $t^2$ are equal in both expressions, and the coefficients for $t$ are equal in both expressions, and the constant terms are equal in both expressions. As such, we find that $a$, $b$ and $c$ need to satisfy the three equations

$$
 \left\{\begin{array}{lcll}1&=&a,\qquad &(\text{coefficients of }t^2),\\ -3&=&-2a+b,\qquad &(\text{coefficients of }t),\\ 0&=&a-b+c,\qquad &(\text{constant terms}).\end{array}\right.
$$

Solving these equations gives $a=1$, $b=-1$ and $c=-2$. As such, the curve describes part of the graph of the function $f(x)=x^2-x-2$. 

Alternatively, we could have found this function by noting that since $x=-1+t$ we must have $t=x+1$. Plugging this into $y=t^2-3t$ would give the same relation between $x$ and $y$.

The start point of the curve can be found by considering the lowest value of $t$. Since we have $0\leq t\leq1$, the start point of the curve is the point $(x,y)=(-1+0,0^2-3\cdot0)=(-1,0)$. Similarly, the end point of the curve is the point $(x,y)=(-1+1,1^2-3\cdot 1)=(0,-2)$.

::::::

::::::{prf:example} 
:label: Ex:CurvesR2:CurveFunction

Consider any function $f$ of one variable. Then any point $(x,y)$ on the graph of $f$ satisfies the equation $y=f(x)$, or $g(x,y)=y-f(x)=0$. This means that we can think of the graph of $f$ as a curve in $\mathbb{R}^2$. So, what would be a parametrisation for this curve? The important thing to notice here is that if we know $x$, we can compute the corresponding value of $y$ by plugging $x$ into the function. As such, it is convenient to choose $x=t$. Then necessarily, we must have $y=f(x)=f(t)$ in order for $(x,y)$ to lie on the curve. Hence, $\mathbf{r}(t)=\begin{pmatrix}t\\ f(t)\end{pmatrix}$ for $t$ in the domain of $f$ is a parametrisation of the graph of $f$.

As a more explicit example, consider the function $f(x)=-\sqrt{4-x^2}$. Note that the domain of this function is given by $-2\leq x\leq 2$, since these are the only values of $x$ for which $4-x^2\geq 0$. By our previous considerations, $\mathbf{r}(t)=\begin{pmatrix}t\\-\sqrt{4-t^2}\end{pmatrix}$ for $-2\leq t\leq 2$ is a parametrisation of the graph of $f$. We can wonder, however, whether this parametrisation is the most convenient one. Indeed, the graph of $f$ is the lower half of the circle $x^2+y^2=4$. For (parts of) circles, it is often more convenient to use sines and or cosines as a parametrisation. Here, we could choose $\mathbf{r}(t)=\begin{pmatrix}2\cos(t)\\ 2\sin(t)\end{pmatrix}$. Indeed, in that case we have

$$
 x^2+y^2=\left(2\cos(t)\right)^2+\left(2\sin(t)\right)^2=4\left(\cos^2(t)+\sin^2(t)\right)=4\cdot 1=4.
$$

In order to ensure that we only parametrise the lower half of the circle, we should **not** use $0\leq t\leq 2\pi$, since that would parametrise the entire circle. Instead, we could either use $-\pi\leq t\leq 0$ or $\pi\leq t\leq 2\pi$ (or something more exotic like $9\pi\leq t\leq 10\pi$). We conclude that 

$$
 \left\{\begin{array}{lcl}x&=&t,\\ y&=&-\sqrt{4-t^2},\end{array}\right.\qquad -2\leq t\leq 2
$$

and

$$
 \left\{\begin{array}{lcl}x&=&2\cos(t),\\ y&=&2\sin(t),\end{array}\right.\qquad \pi\leq t\leq 2\pi
$$

are both valid parametric equations of the same curve, but in computations the latter is often nicer to work with.

::::::


::::::{prf:example} 
:label: Ex:CurvesR2:FoliumDescartes

In {prf:ref}`Ex:Curves:FoliumDescartes` we have studied the Folium of Descartes, which is given by the implicit equation

$$
 x^3+y^3=3xy.
$$

Finding a parametrisation for the folium of Descartes is very tricky, as there is no obvious way to start. It turns out that 

$$
 \mathbf{r}(t)=\begin{pmatrix}\frac{3t}{1+t^3}\\\frac{3t^2}{1+t^3}\end{pmatrix},\qquad -\infty < t < -1,\ -1 < t < \infty
$$

gives a parametrisation of this curve. Indeed, for any $t\neq -1$ we have

$$
\begin{align*}
 x^3+y^3 &= \left(\frac{3t}{1+t^3}\right)^3+\left(\frac{3t^2}{1+t^3}\right)^3 \\
 &= \frac{27t^3}{(1+t^3)^3}+\frac{27t^6}{(1+t^3)^3} \\
 &= \frac{27t^3(1+t^3)}{(1+t^3)^3} \\
 &= \frac{27t^3}{(1+t^3)^2}
\end{align*}
$$

and

$$
 3xy=3\frac{3t}{1+t^3}\frac{3t^2}{1+t^3}=\frac{27t^3}{(1+t^3)^2}.
$$ 

::::::


::::{question}
:type: short-answer
:variant: gaps
:showanswer:
:admonition:
:class: question

For the parametrisation of the folium of Descartes in {prf:ref}`Ex:CurvesR2:FoliumDescartes`, different values of $t$ generate different parts of the curve. Complete the following sentences.
---
DS[{positive};negative;non-positive;non-negative]
DS[positive;{negative};non-positive;non-negative]
DS[above;{below}]
DS[{left};right]
DS[positive;negative;non-positive;{non-negative}]
DS[{asymptote};loop]
^^^
? :::{card}
- For $t<-1$, $x$ is {gap} and $y$ is {gap}, so this part of the curve lies {gap} the $x$-axis.
- For $-1<t<0$, the curve lies to the {gap} of the $y$-axis.
- For $t\geq0$, both $x$ and $y$ are {gap}, giving the {gap} of the curve.
:::
---
::::

## Parametrisations for ellipses

We have studied ellipses in {numref}`Subsec:CurvesEllipses`. Here, we will study paramterisations of ellipses.

::::::{prf:theorem} 
:label: Thm:CurvesR2:EllipseParam

Let $a>0$ and $b>0$ and consider an ellipse of which the vertices and co-vertices are $(x_0+a,y_0)$, $(x_0-a,y_0)$, $(x_0,y_0+b)$ and $(x_0,y_0-b)$ (so that the center of the ellipse is at the point $(x_0,y_0)$ and the axes are the lines $x=x_0$ and $y=y_0$). Then 

$$
 x(t)=x_0+a\cos(t),\qquad y(t)=y_0+b\sin(t),\qquad 0\leq t\leq 2\pi
$$ 

is a parametrisation for the ellipse that traverses the ellipse once in counterclockwise direction for which both the start and endpoint are the (co-)vertex $(x_0+a,y_0)$. 
::::::

::::::{prf:definition} 
:label: Def:Curves:EllipseParam
This parametrisation in {prf:ref}`Thm:CurvesR2:EllipseParam` is called the **standard parametrisation** of the ellipse.

::::::

:::{admonition} Proof of {prf:ref}`Thm:CurvesR2:EllipseParam`
:class: tudproof, dropdown
By {prf:ref}`Cor:CurvesR2:Ellipse` the equation for this ellipse is $\displaystyle \frac{\left(x-x_0\right)^2}{a^2}+\frac{\left(y-y_0\right)^2}{b^2}=1$. Writing $x(t)=x_0+a\cos(t)$ and $y(t)=y_0+b\sin(t)$, we find

$$
 \frac{\left(x(t)-x_0\right)^2}{a^2}+\frac{\left(y(t)-y_0\right)^2}{b^2}=\frac{a^2\cos^2(t)}{a^2}+\frac{b^2\sin^2(t)}{b^2}=\cos^2(t)+\sin^2(t)=1.
$$

As such, any point of the form $(x,y)=(x_0+a\cos(t),y_0+b\sin(t))$ satisfies the equation of the ellipse, so we are indeed dealing with a parametrisation of (possibly a part of) the ellipse. Note that at $t=0$ we have $(x(0),y(0))=(x_0+a\cos(0),y_0+b\sin(0))=(x_0+a,y_0)$ and at $t=2\pi$ we have $(x(2\pi),y(2\pi))=(x_0+a\cos(2\pi),y_0+b\sin(2\pi))=(x_0+a,y_0)$, so that the start and endpoint are, indeed, both the (co-)vertex $(x_0+a,y_0)$. 

Now we show that this parametrisation covers the ellipse exactly once (except the (co-)vertex $(x_0+a,y_0)$, which is both the start and end point). Consider any point $(x,y)$ on the ellipse. We claim that the point $(x',y')\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)$ lies on the unit circle. Indeed, we have

$$
 \left(x'\right)^2+\left(y'\right)^2=\frac{\left(x-x_0\right)^2}{a^2}+\frac{\left(y-y_0\right)^2}{b^2},
$$

since $(x,y)$ lies on the ellipse. As such, the point $\left(x',y'\right)$ satisfies the equation defining the unit circle. From {numref}`Subsec:TrigonRatio` we know that there is exactly one value of $t$ with $0\leq t<2\pi$ for which $\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)=\left(\cos(t),\sin(t)\right)$. For this value of $t$ we find that $x=x_0+a\cos(t)$ and $y=y_0+b\sin(t)$, as desired.

Finally, we notice that for $0<t<\frac{\pi}{2}$ we have $y(t)=y_0+b\sin(t)>y_0$, which means that the we parametrise the circle in counterclockwise direction.

:::

::::::{prf:remark} 
:label: Remark:CurvesR2:EllipseParam

Consider the parametrisation of an ellipse from {prf:ref}`Thm:Curves:EllipseParam`. If the ellipse is actually a circle (i.e. when $a=b$, or, equivalently, $c=0$), the parameter $t$ can be interpreted as the angle between the positive $x$-axis and the line segment from the origin to the point $(x(t),y(t))$ measured counterclockwise, as usual. However, for ellipses that are not circles this is not the case. The French painter and mathematician  [Philippe de La Hire (1640-1718)](https://en.wikipedia.org/wiki/Philippe_de_La_Hire) discovered the following interpretation of the parameter $t$.

See {numref}`Fig:CurvesR2:deLaHire`. In this figure we have drawn everything in the $(x-x_0,y-y_0)$-plane. Consider two circles with the same center as the ellipse with radius $b$ and $a$, respectively. If we draw the line segment which has angle $t$ with the positive $x-x_0$-axis, then this line segment crosses the first circle at the point $B:(x_0+b\cos(t),y_0+b\sin(t))$ and the second circle at the point $A:(x_0+a\cos(t),y_0+a\sin(t))$. Then the point $(x,y)=(x_0+a\cos(t),y_0+b\sin(t))$ on the ellipse is found by intersecting the line through $B$ parallel to the horizontal $x-x_0$-axis of the ellipse with the line through $A$ parallel to the vertical $y-y_0$-axis of the ellipse, see the figure below.

:::{applet}
:url: calculus/curves_in_R%5E2/interpretation_by_de_la_Hire
:name: Fig:CurvesR2:deLaHire
:class: dark-light

Interpretation of the parameter $t$ in the standard parametrisation of an ellipse. The point on the ellipse corresponding to the parameter $t$ is found by intersecting the line through $B$ parallel to the major axis of the ellipse with the line through $A$ parallel to the minor axis of the ellipse.
:::

::::::

::::::{prf:example} 
:label: Example:CurvesR2:Ellipse

We consider the ellipse from {prf:ref}`Example:Curves:Ellipse` which is given by the equation 

$$
 \frac{\left(x+1\right)^2}{4}+\frac{\left(y-5\right)^2}{9}=1.
$$

The standard parametrisation for this ellipse is given by 

$$
 x=-1+2\cos(t),\qquad y=5+3\sin(t),\qquad 0\leq t\leq 2\pi,
$$

which corresponds to traversing the ellipse once in counterclockwise direction, starting and ending at the co-vertex $(1,5)$.

A different parametrisation for this ellipse would be 

$$
 x=-1+2\sin(2t),\qquad y=5+3\cos(2t),\qquad 0\leq t\leq 2\pi.
$$

Note that both at $t=0$ and at $t=2\pi$ we have $(x(t),y(t))=(-1,8)$, so this curve starts and ends at the vertex $(-1,8)$. Moreover, since the fundamental period of the sine and cosine is $2\pi$, the fundamental period of $\sin(2t)$ and $\cos(2t)$ must be $\pi$ (see {numref}`Subsec:PropertiesFunctionsPeriodic`). Hence, the parametrisation covers the ellipse **twice**. Indeed, for any $0\leq t\leq \pi$ we have

$$
\begin{align*}
 (x(t+\pi),y(t+\pi)) &= \left(-1+2\sin(2(t+\pi)),5+3\cos(2(t+\pi))\right) \\
 &= \left(-1+2\sin(2t+2\pi),5+3\cos(2t+2\pi)\right) \\
 &= \left(-1+2\sin(2t),5+3\cos(2t)\right) \\
 &= (x(t),y(t)).
\end{align*}
$$

Finally, we notice that for $0<t<\frac{\pi}{4}$ we have $x(t)>-1=x(0)$, so the parametrisation describes a clockwise traversal of the ellipse.

:::{applet}
:url: calculus/curves_in_R%5E2/two_parametrisations_of_one_ellipse
:name: Fig:CurvesR2:Ellipse3
:class: dark-light

The ellipse with vertices $V_1(-1,2)$ and $V_2(-1,8)$ and co-vertices $W_1(-3,5)$ and $W_2(1,5)$. On the _left_ the standard parametrisation, on the _right_ the alternative parametrisation. Use the play button to see the two parametrisations in action. 
:::

::::::


It is also possible to find parametrisations for ellipses of which the major axis is not a horizontal or vertical line. However, this requires quite some knowledge of linear algebra. More information on this can be found in the relevant section of the [Open Linear Algebra book](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter8/QuadraticForms.html#conic-sections).

## Parametrisations for hyperbolas

A common parametrisation of a hyperbola uses the hyperbolic cosine and sine functions, see {prf:ref}`Def:PropertiesFunctions:Hyperbolic`.

::::::{prf:theorem} 
:label: Thm:Curves:HyperbolaParam

Let $0<a<c$ and consider a hyperbola of which the vertices are $(x_0-a,y_0)$ and $(x_0+a,y_0)$ and the focal points are $(x_0-c,y_0)$ and $(x_0+c,y_0)$ (so that the center of the hyperbola is at the point $(x_0,y_0)$ and the major axis is the line $y=y_0$). Let $b=\sqrt{c^2-a^2}$. Then 

$$
 x(t)=x_0-a\cosh(t),\qquad y(t)=y_0+b\sinh(t),\qquad -\infty<t<\infty
$$ 

is a parametrisation of the part of the hyperbola with $x<x_0$, while

$$
 x(t)=x_0+a\cosh(t),\qquad y(t)=y_0+b\sinh(t),\qquad -\infty<t<\infty
$$ 

is a parametrisation of the part of the hyperbola with $x>x_0$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves:HyperbolaParam`
:class: tudproof, dropdown

By {prf:ref}`Cor:Curves:Hyperbola` the equation for this hyperbola is 

$$
 \displaystyle \frac{\left(x-x_0\right)^2}{a^2}-\frac{\left(y-y_0\right)^2}{b^2}=1.
$$

Writing $x(t)=x_0-a\cosh(t)$ and $y(t)=y_0+b\sinh(t)$, we find

$$
 \frac{\left(x(t)-x_0\right)^2}{a^2}-\frac{\left(y(t)-y_0\right)^2}{b^2}=\frac{a^2\cosh(t)^2}{a^2}-\frac{b^2\sinh(t)^2}{b^2}=\cosh(t)^2-\sinh(t)^2=1.
$$

The final step follows from {prf:ref}`Thm:PropertiesFunctions:HyperbolicProperties`. As such, any point of the form $(x,y)=(x_0-a\cosh(t),y_0+b\sinh(t))$ satisfies the equation of the hyperbola, so we are indeed dealing with a parametrisation of a part of the hyperbola. Note that since $\cosh(t)=\frac{e^t+e^{-t}}{2}> 0$, we have $x(t)=x_0-a\cosh(t)< x_0$ for all values of $t$. So this parametrisation covers only (possibly a part of) the part of the hyperbola with $x<x_0$.

Now we show that this parametrisation covers the left half of the hyperbola exactly once.  From {prf:ref}`Thm:PropertiesFunctions:HyperbolicProperties` we know that the hyperbolic sine is strictly increasing on $\mathbb{R}$, so two different values of $t$ will always give two different values of $y$, so two different points. Moreover, if $t$ becomes very large positive, $\sinh(t)=\frac{1}{2}e^{t}-\frac{1}{2}e^{-t}$ becomes very large positive as well, while if $t$ becomes very large negative, $\sinh(t)=\frac{1}{2}e^{t}-\frac{1}{2}e^{-t}$ becomes very large negative as well (in the terminology of {numref}`Section:LimitInf` we have $\lim\limits_{t\rightarrow\infty}\sinh(t)=\infty$ and $\lim\limits_{t\rightarrow-\infty}\sinh(t)=-\infty$.) Finally, the function $t\mapsto \sinh(t)$ does not make any jumps, so its range is the entire real line (in the terminology of {numref}`Section:Continuity`, the hyperbolic sine is continuous). As such, this parametrisation covers each value of $y$ exactly once. Since on the left half of the hyperbola each value of $y$ occurs exactly once, this means that the parametrisation covers the left half of the hyperbola exactly once.

The proof for the right half of the hyperbola is identical.

:::

::::::{prf:example} 
:label: Ex:CurvesR2:Hyperbola1

We consider the hyperbola from {prf:ref}`Ex:Curves:Hyperbola1`, which is given by the equation

$$
 \frac{(x-2)^2}{4}-\frac{y^2}{5}=1.
$$

{prf:ref}`Thm:Curves:HyperbolaParam` tells us that we can parametrise the left half of the hyperbola by

$$
 x=2-2\cosh(t),\qquad y=\sqrt{5}\sinh(t),\qquad -\infty<t<\infty,
$$

while the right half of the hyperbola can be parametrised by

$$
 x=2+2\cosh(t),\qquad y=\sqrt{5}\sinh(t),\qquad -\infty<t<\infty.
$$

:::{applet}
:url: calculus/curves_in_R%5E2/two_parametrisations_of_one_hyperbola
:name: Fig:CurvesR2:Hyperbola1
:class: dark-light

The hyperbola with vertices $V_1(0,0)$ and $V_2(4,0)$ and focal points $F_1(-1,0)$ and $F_2(5,0)$.
:::

::::::

## Paramterisations for parabolas

Finding a parametrisation for general parabolas is hard, but not so for those with axis parallel to the $y$-axis on account of {prf:ref}`Ex:CurvesR2:CurveFunction`. 

::::::{prf:theorem} 
:label: Thm:Curves:ParabolaParam

Consider the parabola with vertex $(v_1,v_2)$ and focus $(v_1,v_2+f)$, or equivalently directrix $y=v_2-f$ (i.e. a parabola of which the axis is parallel to the $y$-axis).  Then a parametrisation is given by

$$
 x=t,\qquad y=\frac{1}{4f}\left(t-v_1\right)^2+v_2,\qquad -\infty<t<\infty.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves:ParabolaParam`
:class: tudproof, dropdown

By {prf:ref}`Cor:Curves:Parabola` the equation for this parabola is $y=\frac{1}{4f}\left(x-v_1\right)^2+v_2$, which means that the parabola is the graph of a function. The maximal domain of this function is $\mathbb{R}$. As such, we can use {prf:ref}`Ex:CurvesR2:CurveFunction` to conclude that $(x,y)=\left(t,\frac{1}{4f}\left(t-v_1\right)^2+v_2\right)$ for $t$ in $\mathbb{R}$ is a parametrisation for this curve.

:::

::::::{prf:example} 
:label: Ex:Curves:Parabola1

We consider the parabolya given by

$$
 y=-\frac{1}{4}x^2+\frac{1}{2}x+\frac{23}{4}
$$

from {prf:ref}`Ex:Curves:Parabola1`. A straightforward parametrisation of this parabola is given by

$$
 x=t,\qquad y=-\frac{1}{4}t^2+\frac{1}{2}t+\frac{23}{4},\qquad -\infty<t<\infty.
$$

:::{todo}
Include a version of {numref}`Fig:Curves:Parabola1` that shows the parametrisation.
:::

:::{applet}
:url: calculus/curves_in_R%5E2/a_parabola
:name: Fig:Curves:Parabola1
:class: dark-light

The graph of the function $f(x)=-\frac{1}{4}x^2+\frac{1}{2}x+\frac{23}{4}$ is a parabola with axis $x=1$, vertex $\left(1,6\right)$, focus $\left(1,5\right)$ and directrix $y=7$.
:::




::::::