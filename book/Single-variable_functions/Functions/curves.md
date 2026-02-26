(Section:Curves)=

# Curves in $\mathbb{R}^2$

(Subsec:CurvesIntro)=

## Introduction

In {numref}`Subsec:Functions1dGraphs` we saw that the circle with radius $1$, centered around the origin, i.e. the unit circle, cannot be the graph of a function. Indeed, the circle fails the vertical line test ({prf:ref}`Thm:Functions1var:VerticalLineTest`). Still, it is useful to find an equation describing the circle. Because the unit circle is not the graph of a function, this equation can never be of the form $y=f(x)$, but maybe some other type of equation will do. The circle is defined as all points $(x,y)$ which have distance $1$ (the radius of the circle) to the origin (the center of the circle). The distance of any point $(x,y)$ to $(0,0)$ can, using the Pythagorean theorem ({prf:ref}`Thm:Trigonometry:Pythagoras`), be computed as $\sqrt{x^2+y^2}$. So all points on the circle must satisfy the equation $\sqrt{x^2+y^2}=1$, which we can simplify, by squaring, to the equation $x^2+y^2=1^2=1$. Reversely, any point $(x,y)$ that satisfies $x^2+y^2=1$ has distance $1$ to the origin, so it must lie on the circle. As such, the equation $x^2+y^2=1$ gives a precise description of the circle. We call such an equation an **implicit equation** for $x$ and $y$. It is called implicit, because knowing the value of, say, $x$ does not allow us to directly find the corresponding value(s) of $y$ or vice-versa. By contrast, an **explicit equation** is an equation of the form $y=f(x)$ or $x=g(y)$, where knowing the value of one variable directly determines the value of the other variable (though not necessarily the other way around). The equation $x^2+y^2=1$ can be turned into the explicit equations $y=\sqrt{1-x^2}$ and $y=-\sqrt{1-x^2}$, which describe, respectively, the upper and lower halves of the unit circle.

```{figure} Images/circle.png
---
width: 100%
name: Fig:Curves:Circle
class: dark-light
---
The unit circle fails the vertical line test. In addition, any point $(a,b)$ on the circle satisfies $a^2+b^2=1$.
```

:::{todo}
Replace {numref}`Fig:Curves:Circle` with an applet.
:::

:::{figure} Images/Fig-Curves-CircleExplicit.png
:name: Fig:Curves:CircleExplicit
:class: dark-light

The two explicit equations $y=\sqrt{1-x^2}$ and $y=-\sqrt{1-x^2}$ describe the upper and lower halves of the unit circle, respectively.
:::

:::{todo}
Replace {numref}`Fig:Curves:CircleExplicit` with an applet.

Put the graphs next to each other.
:::


We can also take a look at the unit circle from a different perspective. Imagine a particle starting at the point $(1,0)$ and moving around the circle in counterclockwise direction. At time $t$, the particle has a certain position $(x,y)$ on the circle. Since for each $t$, the particle has a unique $x$- and $y$-coordinate, we note that the $x$ and $y$ coordinates of the particle are functions of $t$, so we can write 

$$
 x=f(t), \qquad y=g(t).
$$

The equations $x=f(t),y=g(t)$ are called a **parametric equation** for the circle and $t$ is called a **parameter**. Alternatively, we say that we made a **parametrisation** of the circle. So what could these functions $f$ and $g$ be? It turns out that a single curve can have many different parametrisations. This is because the particle can moves around the circle at different speeds, possibly not even having a constant speed. As such, we have a lot of freedom in choosing out parametrisation. Still, some parametrisations are more useful than others. In order to find one for the circle, we recall from {numref}`Fig:Trigonometry:UnitCircleStandardValues` that each point $(x,y)$ on the unit circle can be represented as $x=\cos(t)$ and $y=\sin(t)$, where $t$ is the angle with respect to the positive $x$-axis. In order to obtain each point on the circle exactly once we should have, for instance, $0\leq t<2\pi$. This means that the equations

$$
 x=\cos(t),\qquad y=\sin(t),\qquad 0\leq t<2\pi
$$

are parametric equations for the unit circle. Indeed if $(x,y)=(\cos(t),\sin(t))$, then we find that

$$
 x^2+y^2=\left(\cos(t)\right)^2+\left(\sin(t)\right)^2=1,
$$ 

so that, indeed, the point $(x,y)=(\cos(t),\sin(t))$ lies on the unit circle. 


```{figure} Images/CircleParam.png
---
width: 100%
name: Fig:Curves:CircleParam
class: dark-light
---
The parametrisation $x=\cos(t)$ and $y=\sin(t)$ for $0\leq t<2\pi$ describes the unit circle.
```

:::{todo}
Replace {numref}`Fig:Curves:CircleParam` with an applet.
:::

In this section, we will take a look at more general curves and their parametrisations. Moreover, we will consider some important classes of curves, which describe well-known geometrical objects such as ellipses, hyperbolas and parabolas.


(Subsec:CurvesParam)=

## Curves and parametrisations

Intuitively, a curve is a line that is not necessarily straight. However, turning that definition into something mathematical can be a bit tricky. Instead, we will define a curve as a set of points that is given by some parametric equations. 

::::::{prf:definition} 
:label: Def:Curves:ParamCurve

A **parametric curve**, or simply **curve**, $\mathcal{C}$ in $\mathbb{R}^2$ is a set of points $(x,y)$ whose positions are given by **parametric equations** $x=f(t)$ and $y=g(t)$ for $t$ in some interval $I$. Here $t$ is called a **parameter**.

If $I$ is the closed interval $[a,b]$, then the point $(x,y)=(f(a),g(a))$ is called the **start point** or **initial point** of $\mathcal{C}$, while the point $(x,y)=(f(b),g(b))$ is called the **end point** or **terminal point** of $\mathcal{C}$. Whenever the start point and the end point of the curve coincide, we say that the curve is **closed**.

::::::

::::::{note}
:name: Note:Curves:MultipleParam

A curve can have many different parametrisations.

::::::

::::::{important}
:name: Important:Curves:tInterval

When writing down a parametrisation of a curve, you should always explicitly write down for which values of the parameter the parametric equations hold, i.e. a parametrisation can be of the form $x=f(t)$, $y=g(t)$ for $a\leq t\leq b$, but only writing $x=f(t)$, $y=g(t)$ is not enough.

::::::

Recall that the unit circle can also represented as the set of all points $(x,y)$ satisfying the implicit equation $x^2+y^2=1$. Alternatively, we can write this equation as $x^2+y^2-1=0$. In order to generalise this concept to other curves, we first need to define what we mean by a function of two variables. These function will be studied in way more depth in {numref}`Sec:MultivariableFunctions`.


::::::{prf:definition} 
:label: Def:Curves:Function2var

A **function of two variables** $f$ is a function of which the domain is a subset of $\mathbb{R}^2$ and the codomain is $\mathbb{R}$. For a point $(x,y)$ in the domain of $f$, we write $f(x,y)$ for the image of $(x,y)$ under $f$.

::::::

::::::{prf:definition} 
:label: Def:Curves:ImplicitEquation

Let $\mathcal{C}$ be a curve. Then we call an equation of the form $f(x,y)=0$ an **implicit equation**, or simply **equation**, for $\mathcal{C}$ when every point on $\mathcal{C}$ satisfies this equation, while any point not on $\mathcal{C}$ does not satisfy the equation.

::::::

::::::{prf:example} 
:label: Ex:Curves:Curve1

Consider the curve $\mathcal{C}$ that is defined by the parametric equations $x=-1+t$ and $y=t^2-3t$ for $0\leq t\leq 1$. In order to determine which curve we are dealing with, we first draw the curve by computing the values of $x$ and $y$ for several values of $t$. This gives the following result.

:::{figure} Images/Fig-Curves-Curve1.png
:name: Fig:Curves:Curve1
:class: dark-light

The graph of the curve defined by the parametric equations $x=-1+t$ and $y=t^2-3t$ for $0\leq t\leq 1$.
:::

:::{todo}
Replace {numref}`Fig:Curves:Curve1` with an applet.

On hovering over the graph, the corresponding values of $t$, $x$ and $y$ should be shown.
:::

Note that in the draw, the parameter $t$ is not visible directly. Indeed, each value of $t$ gives a point $(x,y)=(-1+t,t^2-3t)$ on the curve. The interpretation of this parameter is that we consider a particle that starts at the initial point of the curve and at time $t$ is at position $(x,y)=(-1+t,t^2-3t)$.

This graph suggest that we might be dealing with a part of the graph of a quadratic function, i.e. that $y=ax^2+bx+c$ for some constants $a$, $b$ and $c$. Indeed, we note that $x$ depends linearly on $t$, while $y$ depends quadratically on $t$. We can now try to find the values of these constants $a$, $b$ and $c$ by substituting the expressions $x=-1+t$ and $y=t^2-3t$ into the equation $y=ax^2+bx+c$. This gives

$$
 t^2-3t=y=ax^2+bx+c=a\left(-1+t\right)^2+b\left(-1+t\right)+c=at^2+\left(-2a+b\right)t+a-b+c.
$$

Two quadratic expressions in $t$ can only be equal when the coefficients for $t^2$ are equal in both expressions, and the coefficients for $t$ are equal in both expressions, and the constant terms are equal in both expressions. As such, we find that $a$, $b$ and $c$ need to satisfy the three equations

$$
 \left\{\begin{array}{lcll}1&=&a,\qquad &(\text{coefficients of }t^2),\\ -3&=&-2a+b,\qquad &(\text{coefficients of }t),\\ 0&=&a-b+c,\qquad &(\text{constant terms}).\end{array}\right.
$$

Solving these equations gives $a=1$, $b=-1$ and $c=-2$. As such, the curve describes part of the graph of the function $f(x)=x^2-x-2$. 

The start point of the curve can be found by considering the lowest value of $t$. Since we have $0\leq t\leq1$, the start point of the curve is the point $(x,y)=(-1+0,0^2-3\cdot0)=(-1,0)$. Similarly, the end point of the curve is the point $(x,y)=(-1+1,1^2-3\cdot 1)$.

::::::

::::::{prf:example} 
:label: Ex:Curves:CurveFunction

Consider any function $f$ of one variable. Then any point $(x,y)$ on the graph satisfies the equation $y=f(x)$, or $y-f(x)=0$. As such, we can think of the graph of $f$ as a curve in $\mathbb{R}^2$. So, what would be a parametrisation for this curve? Since a curve can have many different parametrisations, we have at least some freedom in how we choose our parametrisation. The important thing to notice here is that if we know what $x$, we can compute what the corresponding value of $y$ is by plugging $x$ into the function. As such, it is convenient to choose $x=t$. Then necessarily, we must have $y=f(x)=f(t)$ in order for $(x,y)$ to lie on the curve. As such, $x=t$ and $y=f(t)$ for $t$ in the domain of $f$ is a parametrisation of the graph of $f$.

As a more explicit example, consider the function $f(x)=-\sqrt{4-x^2}$. Note that the domain of this function is given by $-2\leq x\leq 2$, since these are the only values of $x$ for which $4-x^2\geq 0$. By our previous considerations, $x=t$ and $y=-\sqrt{4-t^2}$ for $-2\leq t\leq 2$ is a parametrisation of the graph of $f$. We can wonder however, whether in this specific case this parametrisation is the most convenient one. Indeed, note that the graph of $f$ is the lower half of the circle $x^2+y^2=4$. For (parts of) circles, it is often more convenient to use sines and or cosines as a parametrisation. Here, we could choose $x=2\cos(t)$ and $y=2\sin(t)$. Indeed, in that case we have

$$
 x^2+y^2=\left(2\cos(t)\right)^2+\left(2\sin(t)\right)^2=4\left(\cos^2(t)+\sin^2(t)\right)=4\cdot 1=4.
$$

In order to ensure that we only parametrise the lower half of the circle, we should **not** use $0\leq t\leq 2\pi$, since that would parametrise the entire circle. Instead, we could either use $-\pi\leq t\leq 0$ or $\pi\leq t\leq 2\pi$ (or something more exotic like $9\pi\leq t\leq 10\pi$). We conclude that $x=t$ and $y=-\sqrt{4-t^2}$ for $-2\leq t\leq 2$ and $x=2\cos(t)$ and $y=2\sin(t)$ for $\pi\leq t\leq 2\pi$ are both valid parametrisations of the same curve, but in computations the latter one is often the nicer one to work with.

::::::

::::::{prf:example} 
:label: Ex:Curves:FoliumDescartes

One of the most famous examples of curves defined by an implicit equation is the **folium of Descartes**. It is named after the French philosopher and mathematician [René Descartes (1596-1650)](https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes). One version of this curve, is the one given by the equation $x^3+y^3=3xy$. A plot of this curve is shown below.

:::{figure} Images/Fig-Curves-FoliumOfDescartes.png
:name: Fig:Curves:FoliumOfDescartes
:class: dark-light

One example of the folium of Descartes is the curve defined by the equation $x^3+y^3=3xy$.
:::

:::{todo}
Replace {numref}`Fig:Curves:FoliumOfDescartes` with an applet.

Add the hovering functionality to show the coordinates of the point on the curve.
:::

As we can see in the plot, the curve fails the vertical line test, so it cannot be the graph of a function. However, when we cut up the curve in several parts in the right way, we can obtain curves that are the graphs of functions. One such way is shown in the figure below.

```{figure} Images/Fig-Curves-DescartesFoliumCut.png
---
width: 100%
name: Fig:Curves:DescartesFoliumCut
class: dark-light
---
The curve in {numref}`Fig:Curves:FoliumOfDescartes` has been cut up in $3$ pieces, all of which are the graph of a function.
```

:::{todo}
Replace {numref}`Fig:Curves:DescartesFoliumCut` with an applet.
:::

It is very hard to find an explicit expression for one of these functions. Still, if $f$ is one of these functions, we necessarily must have that

$$
 x^3+\left(f(x)\right)^3=3xf(x)
$$

for each $x$ in the domain of $f$, since the graph of $f$ is part of the curve $x^3+y^3=3xy$. 

Finding a parametrisation for the folium of Descartes is very tricky, as there is no obvious way to start. It turns out that $x=\frac{3t}{1+t^3}$ and $y=\frac{3t^2}{1+t^3}$ for $-\infty<t<-1$ and $-1<t<\infty$ gives a parametrisation of this curve. Indeed, for any $t\neq -1$ we have

\begin{align*}
 x^3+y^3 &= \left(\frac{3t}{1+t^3}\right)^3+\left(\frac{3t^2}{1+t^3}\right)^3 \\
 &= \frac{27t^3}{(1+t^3)^3}+\frac{27t^6}{(1+t^3)^3} \\
 &= \frac{27t^3(1+t^3)}{(1+t^3)^3} \\
 &= \frac{27t^3}{(1+t^3)^2}
\end{align*}

and

$$
 3xy=3\frac{3t}{1+t^3}\frac{3t^2}{1+t^3}=\frac{27t^3}{(1+t^3)^2}.
$$ 

Note that for $t<-1$, $x$ is positive, while $y$ is negative. So these values of $t$ give the part of the curve below the $x$-axis. Similarly, for $-1<t<0$, $x$ is negative and $y$ is positive, so these values give the part of curve to the left of the $y$-axis. Finally, for $t\geq 0$ we have $x\geq 0$ and $y\geq 0$, so these values give the loop in the curve. 
::::::

(Subsec:CurvesEllipses)=

## Circles and ellipses

A very common type of curves that cannot be described as the graph of some function is that of ellipses, which included the circles. First, we give a geometrical description of these objects and then we try to find useful equations and parametrisations describing them.

::::::{prf:definition} 
:label: Def:Curves:Ellipse

An **ellipse** is a curve in $\mathbb{R}^2$ surrounding two points, called the **focal points** of the ellipse, such that for all points on the curve, the sum of the distances to the two focal points is a constant $2a$ that is greater than the distance between the focal points. A **circle** is an ellipse for which the two focal points coincide.

The midpoint of the line segment joining the two focal points is called the **center** of the ellipse. In case the ellipse is not a circle, the line through the focal points is called the **major axis** of the ellipse, while the line perpendicular to the major axis is called the **minor axis** of the ellipse. The intersection points of the major axis with the ellipse are called the **vertices** of the ellipse, while the intersection points of the minor axis with the ellipse are called the **co-vertices**.

If $c$ denotes the distance from any focal point to the center, the number $e=\frac{c}{a}$ is called the **eccentricity** of the ellipse.
::::::

:::{figure} Images/ellipse.png
:width: 100%
:name: Fig:Curves:Ellipse
:class: dark-light

An ellipse with focal points $F_1$ and $F_2$ such that for each point $A$ on the ellipse the sum of the distances to $F_1$ and $F_2$ is $2a$. The center $C$ and the distance $c$ between the center and any focal point are also shown, as are the vertices $V_1$ and $V_2$ and the co-vertices $W_1$ and $W_2$ of the ellipse.
:::

:::{todo}
Replace {numref}`Fig:Curves:Ellipse` with an applet.
:::

In order to find an equation for an ellipse, we will, for convenience, first assume that the center of the ellipse is the origin and that the major axis is either the $x$-axis or $y$-axis. In that case we obtain the following result.

::::::{prf:theorem} 
:label: Thm:Curves:Ellipse

Let $a>0$ and $b>0$ and consider an ellipse with of which the vertices and co-vertices are $(a,0)$, $(-a,0)$, $(0,b)$ and $(0,-b)$ (so that the center of the ellipse is at the origin and the major axis is either the $x$-axis (when $a\geq b$) or the $y$-axis (when $a\leq b$)). Then the ellipse is described by the equation

$$
 \frac{x^2}{a^2}+\frac{y^2}{b^2}=1.
$$

::::::

::::{admonition} Proof of {prf:ref}`Thm:Curves:Ellipse`
:class: tudproof, dropdown
For convenience, we assume that the major axis of the ellipse is the $x$-axis. In that case, the focal points are $(c,0)$ and $(-c,0)$ for some $0\leq c<a$. Since the sum of the distances from $(a,0)$ to $(c,0)$ and to $(-c,0)$ is $(a-c)+(a-(-c))=2a$, we find that the ellipse consists of all points of which the sum of the distances to $(c,0)$ and $(-c,0)$ is $2a$. By symmetry the distance from $(0,b)$ to $(c,0)$ and to $(-c,0)$ must be equal, so both distances must be $a$ (as their sum should be $2a$ since $(0,b)$ is on the ellipse). By considering the triangle in {numref}`Fig:Curves:Ellipse2` and using the Pythagorean theorem ({prf:ref}`Thm:Trigonometry:Pythagoras`), we find that $b^2+c^2=a^2$, which we will use later in the proof.

```{figure} Images/ellipse2.png
---
width: 100%
name: Fig:Curves:Ellipse2
class: dark-light
---
Illustration of the ellipse used in this proof.
```

:::{todo}
Replace {numref}`Fig:Curves:Ellipse2` with an applet.
:::

For any point $P:(x,y)$ on the ellipse, the distance to $F_1:(c,0)$ is $\sqrt{(x-c)^2+(y-0)^2}=\sqrt{(x-c)^2+y^2}$, while the distance to $F_2:(-c,0)$ is $\sqrt{(x-(-c))^2+(y-0)^2}=\sqrt{(x+c)^2+y^2}$. Hence, $(x,y)$ is on the ellipse precisely when

$$
 \mathrm{dist}(P,F_1)+\mathrm{dist}(P,F_2)=\sqrt{(x-c)^2+y^2}+\sqrt{(x+c)^2+y^2}=2a.
$$

We bring $\sqrt{(x+c)^2+y^2}$ to the other side of the equation and take the square of both sides of the equation to obtain

$$
 \begin{array}{lcl}(x-c)^2+y^2&=&\left(2a-\sqrt{(x+c)^2+y^2}\right)^2\\ &=& 4a^2-4a\sqrt{(x+c)^2+y^2}+(x+c)^2+y^2. \end{array}
$$

We work out the brackets on both sides of the equation to obtain 

$$
 x^2-2cx+c^2+y^2=4a^2-4a\sqrt{(x+c)^2+y^2}+x^2+2cx+c^2+y^2.
$$

Several of these terms cancel out, and we are left with

$$
 4a\sqrt{(x+c)^2+y^2}=4a^2+4cx.
$$

Now we divide both sides of the equation by $4a$ and square again to obtain

$$
 (x+c)^2+y^2=\left(a+\frac{c}{a}x\right)^2=a^2+2cx+\frac{c^2}{a^2}x^2.
$$

Working out the brackets on the left-hand side of the equation and bringing several terms to the other side of the equation gives

$$
 x^2\left(1-\frac{c^2}{a^2}\right)+y^2=a^2-c^2.
$$

Note that $1-\frac{c^2}{a^2}=\frac{a^2-c^2}{a^2}$. As such, we can divide the equation by $a^2-c^2$ to obtain

$$
 \frac{x^2}{a^2}+\frac{y^2}{a^2-c^2}=1.
$$

Finally, we recall that $b^2=a^2-c^2$ to obtain the desired formula

$$
 \frac{x^2}{a^2}+\frac{y^2}{b^2}=1.
$$
::::

::::::{prf:corollary} 
:label: Cor:Curves:Ellipse

Let $a>0$ and $b>0$ and consider an ellipse with of which the vertices and co-vertices are $(x_0+a,y_0)$, $(x_0-a,y_0)$, $(x_0+b,y_0)$ and $(x_0-b,y_0)$ (so that the center of the ellipse is at the point $(x_0,y_0)$ and the axes are the lines $x=x_0$ and $y=y_0$). Then the ellipse is described by the equation

$$
 \frac{\left(x-x_0\right)^2}{a^2}+\frac{\left(y-y_0\right)^2}{b^2}=1.
$$

::::::

:::{admonition} Proof of {prf:ref}`Cor:Curves:Ellipse`
:class: tudproof, dropdown

Writing $p=x-x_0$ and $q=y-y_0$, we note that in the $pq$-plane, the curve becomes an ellipse with focal points $(c,0)$ and $(-c,0)$ and vertices $(a,0)$ and $(-a,0)$. By {prf:ref}`Thm:Curves:Ellipse`, the equation for this ellipse is

$$
 \frac{p^2}{a^2}+\frac{q^2}{b^2}=1.
$$

Substituting back in $p=x-x_0$ and $q=y-y_0$, we obtain the desired formula

$$
 \frac{\left(x-x_0\right)^2}{a^2}+\frac{\left(y-y_0\right)^2}{b^2}=1.
$$
:::

::::::{prf:theorem} 
:label: Thm:Curves:EllipseParam

Let $a>0$ and $b>0$ and consider an ellipse with of which the vertices and co-vertices are $(x_0+a,y_0)$, $(x_0-a,y_0)$, $(x_0+b,y_0)$ and $(x_0-b,y_0)$ (so that the center of the ellipse is at the point $(x_0,y_0)$ and the axes are the lines $x=x_0$ and $y=y_0$). Then 

$$
 x(t)=x_0+a\cos(t),\qquad y(t)=y_0+b\sin(t),\qquad 0\leq t\leq 2\pi
$$ 

is a parametrisation for the ellipse that traverses the ellipse once in counterclockwise direction for which the start and endpoint are both the (co-)vertex $(x_0+a,y_0)$. 
::::::

::::::{prf:definition} 
:label: Def:Curves:EllipseParam
This parametrisation in {prf:ref}`Thm:Curves:EllipseParam` is called the **standard parametrisation** of the ellipse.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves:EllipseParam`
:class: tudproof, dropdown
By {prf:ref}`Cor:Curves:Ellipse` the equation for this ellipse is $\displaystyle \frac{\left(x-x_0\right)^2}{a^2}+\frac{\left(y-y_0\right)^2}{b^2}=1$. Writing $x(t)=x_0+a\cos(t)$ and $y(t)=y_0+b\sin(t)$, we find

$$
 \frac{\left(x(t)-x_0\right)^2}{a^2}+\frac{\left(y(t)-y_0\right)^2}{b^2}=\frac{a^2\cos^2(t)}{a^2}+\frac{b^2\sin^2(t)}{b^2}=\cos^2(t)+\sin^2(t)=1.
$$

As such, any point of the form $(x,y)=(x_0+a\cos(t),y_0+b\sin(t))$ satisfies the equation of the ellipse, so we are indeed dealing with a parametrisation of (possibly a part of) the ellipse. Note that $t=0$ we have $(x(0),y(0))=(x_0+a\cos(0),y_0+b\sin(0))=(x_0+a,y_0)$ and at $t=2\pi$ we have $(x(2\pi),y(2\pi))=(x_0+a\cos(2\pi),y_0+b\sin(2\pi))=(x_0+a,y_0)$, so that the start and endpoint are, indeed, both the (co-)vertex $(x_0+a,y_0)$. 

Now we show that this parametrisation covers the ellipse exactly once (except the (co-)vertex $(x_0+a,y_0)$, which is both the start and end point). Consider any point $(x,y)$ on the ellipse. We claim that the point $\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)$ lies on the unit circle. Indeed, we have

$$
 \left(\frac{x-x_0}{a}\right)+\left(\frac{y-y_0}{b}\right)=\frac{\left(x-x_0\right)^2}{a^2}+\frac{\left(y-y_0\right)^2}{b^2}=1,
$$

since $(x,y)$ lies on the ellipse. As such, the point $\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)$ satisfies the equation defining the unit circle. From {numref}`Subsec:TrigonRatio` we know that there is exactly one value of $t$ with $0\leq t<2\pi$ for which $\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)=\left(\cos(t),\sin(t)\right)$. For this value of $t$ we find that $x=x_0+a\cos(t)$ and $y=y_0+b\sin(t)$, as desired.

Finally, we notice that for $0<t<\frac{\pi}{2}$ we have $y(t)=y_0+b\sin(t)>0$, which must mean that the we parametrise the circle in counterclockwise direction.

:::

::::::{prf:remark} 
:label: Remark:Curves:EllipseParam

Consider the parametrisation of an ellipse from {prf:ref}`Thm:Curves:EllipseParam`. If the ellipse is actually a circle (so when $a=b$, or, equivalently, $c=0$), the parameter $t$ has the interpretation as the angle between the positive $x$-axis and the line segment from the origin to the point $(x(t),y(t))$ measured counterclockwise, as usual. However, for ellipses that are not circles this is not the case. The French painter and mathematician  [Philippe de la Hire (1640-1718)](https://en.wikipedia.org/wiki/Philippe_de_La_Hire) discovered the following interpretation of the parameter $t$. Consider two circles with the same center as the ellipse with radius $b$ and $a$ respectively. If we draw the line segment which has angle $t$ with the positive $x$-axis, then this line segment crosses the first circle at the point $B:(x_0+b\cos(t),y_0+b\sin(t))$ and the second circle at the point $A:(x_0+a\cos(t),y_0+b\sin(t))$. Then the point $(x,y)=(x_0+a\cos(t),y_0+b\sin(t))$ on the ellipse is found by intersecting the line through $B$ parallel to the major axis of the ellipse with the line through $A$ parallel to the minor axis of the ellipse, see the figure below.

```{figure} Images/deLaHire.png
---
width: 100%
name: Fig:Curves:deLaHire
class: dark-light
---
Interpretation of the parameter $t$ in the standard parametrisation of an ellipse. The point on the ellipse corresponding to the parameter $t$ is found by intersecting the line through $B$ parallel to the major axis of the ellipse with the line through $A$ parallel to the minor axis of the ellipse.
```

:::{todo}
Replace {numref}`Fig:Curves:deLaHire` with an applet.

Combine the current image with [animation](https://en.wikipedia.org/wiki/File:Parametric_ellipse.gif).
:::
::::::


::::::{prf:example} 
:label: Example:Curves:Ellipse

Consider the ellipse with vertices $(-1,2)$ and $(-1,8)$ and co-vertices $(-3,5)$ and $(1,5)$. Then the major axis of the ellipse is the line $x=-1$, while the minor axis is the line $y=5$. As such, the center of the ellipse is the intersection of these axes, which is the point $(-1,5)$. The distance from the center to the vertices is $3$, while the distance from the center to the co-vertices is $2$. According to {prf:ref}`Cor:Curves:Ellipse`, the ellipse is defined by the equation

$$
 \frac{\left(x-(-1)\right)^2}{2^2}+\frac{\left(y-5\right)^2}{3^2}=1,
$$

which we can rewrite to

$$
 \frac{\left(x+1\right)^2}{4}+\frac{\left(y-5\right)^2}{9}=1.
$$

The standard parametrisation for this ellipse is given by 

$$
 x=-1+2\cos(t),\qquad y=5+3\sin(t),\qquad 0\leq t\leq 2\pi,
$$

which corresponds to traversing the ellipse once in counterclockwise direction, starting and ending at the co-vertex $(1,5)$.

A different parametrisation for this circle would be to have

$$
 x=-1+2\sin(2t),\qquad y=5+3\cos(2t),\qquad 0\leq t\leq 2\pi.
$$

Note that both at $t=0$ and at $t=2\pi$ we have $(x(t),y(t))=(-1,8)$, so this curve starts and ends at the vertex $(-1,8)$. Moreover, since the fundamental period of the sine and cosine is $2\pi$, the fundamental period of $\sin(2t)$ and $\cos(2t)$ must be $\pi$ (see {numref}`Subsec:PropertiesFunctionsPeriodic`). So the parametrisation covers the ellipse **twice**. Indeed, for any $0\leq t\leq \pi$ we have

\begin{align*}
 (x(t+\pi),y(t+\pi)) &= \left(-1+2\sin(2(t+\pi)),5+3\cos(2(t+\pi))\right) \\
 &= \left(-1+2\sin(2t+2\pi),5+3\cos(2t+2\pi)\right) \\
 &= \left(-1+2\sin(2t),5+3\cos(2t)\right) \\
 &= (x(t),y(t)).
\end{align*}

Finally, we notice that for $0<t<\frac{\pi}{4}$ we have $x(t)>-1=x(0)$, so the parametrisation describes a clockwise traversal of the ellipse.

:::{figure} Images/Fig-Curves-Ellipse3.png
:name: Fig:Curves:Ellipse3
:class: dark-light

The ellipse with vertices $(-1,2)$ and $(-1,8)$ and co-vertices $(-3,5)$ and $(1,5)$.
:::

:::{todo}
Replace {numref}`Fig:Curves:Ellipse3` with an applet.

Include an animation of the parametrisation of the ellipse.
:::

::::::

It is also possible to find equations and parametrisations for ellipses of which the major axis is not a horizontal or vertical line. However, this requires quite some knowledge of linear algebra. More information on this can be found in the relevant section of the [Open Linear Algebra book](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter8/QuadraticForms.html#conic-sections).

(Subsec:CurvesHyperbola)=

## Hyperbolas

Hyperbolas are another common type of curves that are (often) not the graph of a function. Hyperbola share quite some similarities with ellipses in terms of the definition and the equations describing them, though they look very differently geometrically. In fact, both are examples of **conic sections**, see the [Open Linear Algebra book](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter8/QuadraticForms.html#conic-sections). As such, we will mainly follow the same structure as in the previous section.


::::::{prf:definition} 
:label: Def:Curves:Hyperbola

A **hyperbola** is a curve in $\mathbb{R}^2$ such that there are two points, called the **focal points** of the hyperbola, such that for all points on the curve, the absolute difference of the distances to the two focal points is a constant $2a$. 

The midpoint of the line segment joining the two focal points is called the **center** of the hyperbola. The line through the focal points is called the **major axis** of the hyperbola. The intersection points of the major axis with the hyperbola are called the **vertices** of the hyperbola.

If $c$ denotes the distance from any focal point to the center, the number $e=\frac{c}{a}$ is called the **eccentricity** of the hyperbola.
::::::

```{figure} Images/hyperbola.png
---
width: 100%
name: Fig:Curves:Hyperbola
class: dark-light
---
A hyperbola with focal points $F_1$ and $F_2$ such that for each point $A$ on the hyperbola the sum of the distances to $F_1$ and $F_2$ is $2a$. The center $C$ and the vertices $V_1$ and $V_2$ of the hyperbola are also shown.
```

:::{todo}
Replace {numref}`Fig:Curves:Hyperbola` with an applet.
:::

In order to find an equation for a hyperbola, we will, for convenience, first assume that the center of the hyperbola is the origin and that the major axis is the $x$-axis. In that case we obtain the following result.

::::::{prf:theorem} 
:label: Thm:Curves:Hyperbola

Let $0<a<c$ and consider a hyperbola of which the vertices are $(a,0)$ and $(-a,0)$ and the focal points are $(c,0)$ and $(-c,0)$ (so that the center of the hyperbola is at the origin and the major axis is the $x$-axis). Then the hyperbola is described by the equation

$$
 \frac{x^2}{a^2}-\frac{y^2}{b^2}=1,
$$

where $b^2=c^2-a^2$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves:Hyperbola`
:class: tudproof, dropdown
Since the absolute difference of the distances from $(a,0)$ to $(c,0)$ and to $(-c,0)$ is $\left|(c-a)-(a-(-c))\right|=2a$, we find that the hyperbola consists of all points of which the absolute difference of the distances to $(c,0)$ and $(-c,0)$ is $2a$. 

Consider any point $(x,y)$. Then the distance to $(c,0)$ is $\sqrt{(x-c)^2+(y-0)^2}=\sqrt{(x-c)^2+y^2}$, while the distance to $(-c,0)$ is $\sqrt{(x-(-c))^2+(y-0)^2}=\sqrt{(x+c)^2+y^2}$. Hence, $(x,y)$ is on the hyperbola precisely when

$$
 \left|\sqrt{(x-c)^2+y^2}-\sqrt{(x+c)^2+y^2}\right|=2a.
$$

Now suppose $(x,y)$ is on the hyperbola and assume, for convenience, that the point $(-c,0)$ is the point closes to $(x,y)$. Then, we can ignore the absolute value. We bring $\sqrt{(x+c)^2+y^2}$ to the other side of the equation and take the square of both sides of the equation to obtain

$$
 \begin{array}{lcl}(x-c)^2+y^2&=&\left(2a+\sqrt{(x+c)^2+y^2}\right)^2\\ &=& 4a^2+4a\sqrt{(x+c)^2+y^2}+(x+c)^2+y^2. \end{array}
$$

We work out the brackets on both sides of the equation to obtain 

$$
 x^2-2cx+c^2+y^2=4a^2+4a\sqrt{(x+c)^2+y^2}+x^2+2cx+c^2+y^2.
$$

Several of these terms cancel out, and we are left with

$$
 -4a\sqrt{(x+c)^2+y^2}=4a^2+4cx.
$$

Now we divide both sides of the equation by $4a$ and square again to obtain

$$
 (x+c)^2+y^2=\left(a+\frac{c}{a}x\right)^2=a^2+2cx+\frac{c^2}{a^2}x^2.
$$

Working out the brackets on the left-hand side of the equation and bringing several terms to the other side of the equation gives

$$
 x^2\left(1-\frac{c^2}{a^2}\right)+y^2=a^2-c^2.
$$

Note that $1-\frac{c^2}{a^2}=\frac{a^2-c^2}{a^2}$. As such, we can divide the equation by $a^2-c^2$ to obtain

$$
 \frac{x^2}{a^2}+\frac{y^2}{a^2-c^2}=1.
$$

Finally, we set $b^2=c^2-a^2$ to obtain the desired formula

$$
 \frac{x^2}{a^2}-\frac{y^2}{b^2}=1.
$$
:::

::::::{prf:corollary} 
:label: Cor:Curves:Hyperbola

Let $0<a<c$ and write $b^2=c^2-a^2$. 

Consider a hyperbola of which the vertices are $(x_0-a,y_0)$ and $(x_0+a,y_0)$ and the focal points are $(x_0-c,y_0)$ and $(x_0+c,y_0)$ (so that the center of the hyperbola is at the point $(x_0,y_0)$ and the major axis is the line $y=y_0$). Then the hyperbola is described by the equation

$$
 \frac{\left(x-x_0\right)^2}{a^2}-\frac{\left(y-y_0\right)^2}{b^2}=1.
$$

Similarly, the hyperbola of which the vertices are $(x_0,y_0-a)$ and $(x_0,y_0+a)$ and the focal points are $(x_0,y_0-c)$ and $(x_0,y_0+c)$ (so that the center of the hyperbola is at the point $(x_0,y_0)$ and the major axis is the line $x=x_0$). Then the hyperbola is described by the equation

$$
 \frac{\left(y-y_0\right)^2}{a^2}-\frac{\left(x-x_0\right)^2}{b^2}=1.
$$

::::::

:::{admonition} Proof of {prf:ref}`Cor:Curves:Hyperbola`
:class: tudproof, dropdown

We first consider the hyperbola of which the vertices are $(x_0-a,y_0)$ and $(x_0+a,y_0)$ and the focal points are $(x_0-c,y_0)$ and $(x_0+c,y_0)$. Writing $p=x-x_0$ and $q=y-y_0$, we note that in the $pq$-plane, the curve becomes a hyperbola with vertices $(-a,0)$ and $(a,0)$ and focal points $(-c,0)$ and $(c,0)$. By {prf:ref}`Thm:Curves:Hyperbola`, the equation for this hyperbola is

$$
 \frac{p^2}{a^2}-\frac{q^2}{b^2}=1.
$$

Substituting back in $p=x-x_0$ and $q=y-y_0$, we obtain the desired formula

$$
 \frac{\left(x-x_0\right)^2}{a^2}-\frac{\left(y-y_0\right)^2}{b^2}=1.
$$

Now we consider the hyperbola of which the vertices are $(x_0,y_0-a)$ and $(x_0,y_0+a)$ and the focal points are $(x_0,y_0-c)$ and $(x_0,y_0+c)$. Writing $r=y$ and $s=x$, we obtain a hyperbola in the $rs$-plane with vertices $(y_0-a,x_0)$ and $(y_0+a,x_0)$ and focal points $(y_0-c,x_0)$ and $(y_0+c,x_0)$. By the first part of this proof, the equation for this hyperbola is

$$
 \frac{\left(r-y_0\right)^2}{a^2}-\frac{\left(s-x_0\right)^2}{b^2}=1.
$$

Substituting back in $r=y$ and $s=x$, we obtain the desired formula

$$
 \frac{\left(y-y_0\right)^2}{a^2}-\frac{\left(x-x_0\right)^2}{b^2}=1.
$$

:::

A common parametrisation of an hyperbola uses the hyperbolic cosine and sine functions, see {prf:ref}`Def:PropertiesFunctions:Hyperbolic`.

::::::{prf:theorem} 
:label: Thm:Curves:HyperbolaParam

Let $0<a<c$ and consider a hyperbola of which the vertices are $(x_0-a,y_0)$ and $(x_0+a,y_0)$ and the focal points are $(x_0-c,y_0)$ and $(x_0+c,y_0)$ (so that the center of the hyperbola is at the point $(x_0,y_0)$ and the major axis is the line $y=y_0$). Then 

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

By {prf:ref}`Cor:Curves:Hyperbola` the equation for this hyperbola is $\displaystyle \frac{\left(x-x_0\right)^2}{a^2}-\frac{\left(y-y_0\right)^2}{b^2}=1$. Writing $x(t)=x_0-a\cosh(t)$ and $y(t)=y_0+b\sinh(t)$, we find

$$
 \frac{\left(x(t)-x_0\right)^2}{a^2}-\frac{\left(y(t)-y_0\right)^2}{b^2}=\frac{a^2\cosh(t)^2}{a^2}+\frac{b^2\sinh(t)^2}{b^2}=\cosh(t)^2-\sinh(t)^2=1.
$$

The final step follows from {prf:ref}`Thm:PropertiesFunctions:HyperbolicProperties`. As such, any point of the form $(x,y)=(x_0-a\cosh(t),y_0+b\sinh(t))$ satisfies the equation of the hyperbola, so we are indeed dealing with a parametrisation of a part of the hyperbola. Note that since $\cosh(t)=\frac{e^t+e^{-t}}{2}\geq 0$, we have $x(t)=x_0-a\cosh(t)\leq x_0$ for all values of $t$. So this parametrisation covers only (possibly a part of) the part of the hyperbola with $x<x_0$.

Now we show that this parametrisation covers the left half of the parabola exactly once.  From {prf:ref}`Thm:PropertiesFunctions:HyperbolicProperties` we know that the hyperbolic sine is strictly increasing on $\mathbb{R}$, so two different values of $t$ will also always give two different values of $y$, so two different points. Moreover, if $t$ becomes very large positive, $\sinh(t)=\frac{1}{2}e^{t}-\frac{1}{2}e^{-t}$ becomes very large positive as well, while if $t$ becomes very large negative, $\sinh(t)=\frac{1}{2}e^{t}-\frac{1}{2}e^{-t}$ becomes very large negative as well (in the terminology of {numref}`Section:LimitInf` we have $\lim\limits_{t\rightarrow\infty}\sinh(t)=\infty$ and $\lim\limits_{t\rightarrow-\infty}\sinh(t)=-\infty$.) Finally, the function $t\mapsto \sinh(t)$ does not make any jumps, so its range is the entire real line (in the terminology of {numref}`Section:Continuity`, the hyperbolic sine is continuous). As such, this parametrisation covers each value of $y$ exactly once. Since on the left half of the hyperbola each value of $y$ occurs exactly once, this means that the parametrisation covers the left half of the parabola exactly once.

The proof for the right half of the parabola is identical.

:::

::::::{prf:example} 
:label: Ex:Curves:Hyperbola1

Consider the hyperbola with vertices $(0,0)$ and $(4,0)$ and focal points $(-1,0)$ and $(5,0)$. Since the vertices both lie on the $x$-axis, the $x$-axis is the major axis of this hyperbola. In addition, the center of the hyperbola is the midpoint of the line segment joining the vertices, so the midpoint must be $(2,0)$. The distance from the center to the vertices is $2$ and the distance from the center to the focal points is $3$. As such, according to {prf:ref}`Cor:Curves:Hyperbola` an equation for the hyperbola is given by

$$
 \frac{(x-2)^2}{2^2}+\frac{(y-0)^2}{2^2-3^2}=1,
$$

which we can rewrite to

$$
 \frac{(x-2)^2}{4}-\frac{y^2}{5}=1.
$$

Moreover, {prf:ref}`Thm:Curves:HyperbolaParam` gives that we can parametrise the left half of the hyperbola by

$$
 x=-2-2\cosh(t),\qquad y=\sqrt{5}\sinh(t),\qquad -\infty<t<\infty,
$$

while the right half of the hyperbola can be parametrised by

$$
 x=-2+2\cosh(t),\qquad y=\sqrt{5}\sinh(t),\qquad -\infty<t<\infty.
$$

:::{figure} Images/Fig-Curves-Hyperbola1.png
:name: Fig:Curves:Hyperbola1
:class: dark-light

The hyperbola with vertices $(0,0)$ and $(4,0)$ and focal points $(-1,0)$ and $(5,0)$.
:::

:::{todo}
Replace {numref}`Fig:Curves:Hyperbola1` with an applet.

Include an animation of the parametrisation of the hyperbola.
:::

::::::

::::::{prf:example} 
:label: Ex:Curves:Hyperbola2

Consider the graph of the function $f(x)=\dfrac{1}{x}$. We claim that this is a hyperbola with vertices $V_1:(-1,-1)$ and $V_2:(1,1)$ and focal points $F_1:(-\sqrt{2},-\sqrt{2})$ and $F_2:(\sqrt{2},\sqrt{2})$. This would mean that the major axis of the hyperbola is the line $y=x$.

We want to show that the absolute difference between the distances to $F_1$ and to $F_2$ is constant. Pick any point $P:(x,y)$ on the graph of $f$. In that case, we have $y=f(x)=\frac{1}{x}$. The distance from $P$ to $F_1$ is 

\begin{align*}
 \operatorname{dist}(P,F_1) &= \sqrt{\left(x-\left(-\sqrt{2}\right)\right)^2+\left(\frac{1}{x}-\left(-\sqrt{2}\right)\right)^2+} \\
 &= \sqrt{x^2+2\sqrt{2}x+2+\frac{1}{x^2}+\frac{2\sqrt{2}}{x}+2} \\
 &= \sqrt{x^2+x^{-2}+2+2\sqrt{2}\left(x+x^{-1}\right)+2},
\end{align*}

while the distance from $P$ to $F_2$ is

\begin{align*}
 \operatorname{dist}(P,F_2) &= \sqrt{\left(x-\sqrt{2}\right)^2+\left(\frac{1}{x}-\sqrt{2}\right)^2} \\
 &= \sqrt{x^2-2\sqrt{2}x+2+\frac{1}{x^2}-\frac{2\sqrt{2}}{x}+2} \\
 &= \sqrt{x^2+x^{-2}+2-2\sqrt{2}\left(x+x^{-1}\right)+2}.
\end{align*}

In order to simplify these distances, we note that

$$
\left(x+x^{-1}\right)^2=x^2+2xx^{-1}+x^{-2}=x^2+2+x^{-2}.
$$

As such, we can write

\begin{align*}
 \sqrt{x^2+x^{-2}+2+2\sqrt{2}\left(x+x^{-1}\right)+2} &= \sqrt{(x+x^{-1})^2+2\sqrt{2}\left(x+x^{-1}\right)+(\sqrt{2})^2} \\
 &= \sqrt{\left(\left(x+x^{-1}\right)+\sqrt{2}\right)^2} \\
 &= \left|\left(x+x^{-1}\right)+\sqrt{2}\right|
\end{align*}

and

\begin{align*}
 \sqrt{x^2+x^{-2}+2-2\sqrt{2}\left(x+x^{-1}\right)+2} &= \sqrt{(x+x^{-1})^2-2\sqrt{2}\left(x+x^{-1}\right)+(-\sqrt{2})^2} \\
 &= \sqrt{\left(\left(x+x^{-1}\right)-\sqrt{2}\right)^2} \\
 &= \left|\left(x+x^{-1}\right)-\sqrt{2}\right|.
\end{align*}

Now we will show that for any $x>0$ we have $x+x^{-1}>\sqrt{2}$. Indeed, for $0<x\leq \frac{1}{2}$ we have

$$
 x+\frac{1}{x}\geq 0+\frac{1}{\frac{1}{2}}=2>\sqrt{2},
$$

for $\frac{1}{2}<x\leq 1$ we have

$$
 x+\frac{1}{x}\geq \frac{1}{2}+\frac{1}{1}=\frac{3}{2}>\sqrt{2},
$$

for $1<x\leq\frac{3}{2}$ we have

$$
 x+\frac{1}{x}\geq 1+\frac{1}{\frac{3}{2}}=\frac{5}{3}>\sqrt{2}
$$

and, finally, for $x>\frac{3}{2}$ we have

$$
 x+\frac{1}{x}>\frac{3}{2}+0>\sqrt{2}.
$$

As such, if $x>0$ the absolute difference of the distances between $P$ and the focal points is

\begin{align*}
 \left|\mathrm{dist}(P,F_1)-\mathrm{dist}(P,F_2)\right| &= \left|\left(x+x^{-1}\right)+\sqrt{2}\right|-\left|\left(x+x^{-1}\right)-\sqrt{2}\right| \\
 &= \left(\left(x+x^{-1}\right)+\sqrt{2}\right)-\left(\left(x+x^{-1}\right)-\sqrt{2}\right) \\
 &=2\sqrt{2}.
\end{align*}

Using a similar argument, the absolute difference of the distances between $P$ and the focal points is $2\sqrt{2}$ as well if $x<0$.

We conclude that the graph of the function $f(x)=\frac{1}{x}$ is, indeed, a hyperbola with vertices $V_1:(-1,-1)$ and $V_2:(1,1)$ and focal points $F_1:(-\sqrt{2},-\sqrt{2})$ and $F_2:(\sqrt{2},\sqrt{2})$.

```{figure} Images/Fig-Curves-Hyperbola1OverX.png
---
width: 100%
name: Fig:Curves:Hyperbola1OverX
class: dark-light
---
The graph of the function $f(x)=\frac{1}{x}$ is a hyperbola with vertices $(-1,-1)$ and $(1,1)$ and focal points $(-\sqrt{2},-\sqrt{2})$ and $(\sqrt{2},\sqrt{2})$.
```

:::{todo}
Replace {numref}`Fig:Curves:Hyperbola1OverX` with an applet.
:::

::::::

In {prf:ref}`Ex:Curves:Hyperbola2` we saw that it can be tricky to describe hyperbolas of which the major axis is not the $x$-axis or $y$-axis. Luckily, with the aid of linear algebra this is a lot easier. More information on this can be found in the relevant section of the [Open Linear Algebra book](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter8/QuadraticForms.html#conic-sections).

(Subsec:CurvesParabola)=

## Parabolas

Parabolas are yet another type of **conic sections**. The most common examples are the graphs of quadratic functions, i.e. functions of the form $f(x)=ax^2+bx+c$ with $a\neq 0$, $b$ and $c$ constants. However, these are not the only type of parabolas that can occur. For instance, one could take the graph of $f(x)=x^2$ and rotate it $\frac{\pi}{2}$ radians to the right. The resulting curve is no longer the graph of a function, but it is still a parabola. In this section, we will find a more general equation for a parabola and we will also see how we can parametrise them.

```{figure} Images/Fig-Curves-ParabolaRotate.png
---
width: 100%
name: Fig:Curves:ParabolaRotate
class: dark-light
---
The graph of the function $f(x)=x^2$ has been rotated to give a parabola that is not the graph of a function.
```

:::{todo}
Replace {numref}`Fig:Curves:ParabolaRotate` with an applet.
:::


::::::{prf:definition} 
:label: Def:Curves:Parabola

A **parabola** is a curve in $\mathbb{R}^2$ such that there are a point, called the **focal point** of the parabola, and a line that does not contain the focal point, called the **directrix** of the parabola, such that for all points on the curve, the distance to the focal point is equal to the distance to the directrix. 

The point on the parabola where the distance to the focal point (or, equivalently, to the directrix) is minimal is called the **vertex** of the parabola. The distance of the vertex to the focal point is called the **focal length** of the parabola.

The line containing the focal point and the vertex of the parabola is called the **axis** of the parabola.
::::::

```{figure} Images/Fig-Curves-Parabola.png
---
width: 100%
name: Fig:Curves:Parabola
class: dark-light
---
A parabola with focal point $F$ such that for each point $P$ on the parabola the distance to $F$ is equal to the distance to the directrix. The vertex $V$ and the axis of the parabola are also shown.
```

:::{todo}
Replace {numref}`Fig:Curves:Parabola` with an applet.
:::

Unlike ellipses and hyperbolas, finding a general equation for a parabola does not require a lot of linear algebra, so we can immediately give the most general result.

::::::{prf:theorem} 
:label: Thm:Curves:Parabola

Let $\mathcal{C}$ be a parabola with focus $F:(p,q)$ and directrix $d$ given by $ax+by+c=0$. Then the parabola is defined by the equation

$$
 \frac{\left(ax+by+c\right)^2}{a^2+b^2}=\left(x-p\right)^2+\left(y-q\right)^2.
$$



::::::

::::{admonition} Proof of {prf:ref}`Thm:Curves:Parabola`
:class: tudproof, dropdown
Consider any point $P:(x_0,y_0)$. Then the distance to the focus point is given by

$$
 \mathrm{dist}(P,F)=\sqrt{\left(x_0-p\right)^2+\left(y_0-q\right)^2}.
$$

In order to compute the distance from $P$ to the line, we use some ideas from {numref}`Sec:LinesAndPlanes`. Note that the directrix can be written in vector form as $\begin{pmatrix}a\\ b\end{pmatrix}\cdot\begin{pmatrix}x\\ y\end{pmatrix}=-c$. As such, the line $\begin{pmatrix}a\\ b\end{pmatrix}\cdot\begin{pmatrix}x\\ y\end{pmatrix}=0$ is parallel to the directrix and from this we can read off that the vector $\begin{pmatrix}a\\ b\end{pmatrix}$ is perpendicular to the directrix. Hence, the line $\mathcal{L}$ with parametric vector equation $\begin{pmatrix}x\\ y\end{pmatrix}=\begin{pmatrix}x_0\\ y_0\end{pmatrix}+t\begin{pmatrix} a\\ b\end{pmatrix}$ passes through $(x_0,y_0)$ and is perpendicular to the directrix. As such, the intersection point of this line $\mathcal{L}$ and the directrix will give the point on the directrix closest to $(x_0,y_0)$. Plugging in the parametric vector equation into the equation for the directrix gives

$$
 a\left(x_0+at\right)+b\left(y_0+bt\right)+c=0,
$$

which gives

$$
 t=\frac{-ax_0-by_0-c}{a^2+b^2}.
$$

As such, the point on the directrix closest to $(x_0,y_0)$ is

$$
(x,y)=\left(x_0+\frac{-ax_0-by_0-c}{a^2+b^2}a,y_0+\frac{-ax_0-by_0-c}{a^2+b^2}b\right),
$$

which gives that the requested distance is

\begin{align*}
 \mathrm{dist}(d,P) &= \sqrt{\left(x_0+\frac{-ax_0-by_0-c}{a^2+b^2}a-x_0\right)^2+\left(y_0+\frac{-ax_0-by_0-c}{a^2+b^2}b-y_0\right)^2} \\
 &~ \quad\cdot\sqrt{\left(-ax_0-by_0-c\right)\frac{a^2}{\left(a^2+b^2\right)^2}+\left(-ax_0-by_0-c\right)\frac{b^2}{\left(a^2+b^2\right)^2}} \\
 &= \sqrt{\left(-ax_0-by_0-c\right)^2\frac{a^2+b^2}{\left(a^2+b^2\right)^2}} \\
 &= \sqrt{\left(-ax_0-by_0-c\right)^2\frac{1}{a^2+b^2}} \\
 &= \frac{|-ax_0-by_0-c|}{\sqrt{a^2+b^2}}.
\end{align*}

Since the parabola consists of those points for which $\mathrm{dist}(d,P)=\mathrm{dist}(P,F)$, or equivalently when $\left(\mathrm{dist}(d,P)\right)^2=\left(\mathrm{dist}(P,F)\right)^2$ we find that $(x_0,y_0)$ lies on the parabola precisely when

$$
 \left(x_0-p\right)^2+\left(y_0-q\right)^2=\left(\frac{|-ax_0-by_0-c}{\sqrt{a^2+b^2}}\right)^2=\frac{\left(ax_0+by_0+c\right)}{a^2+b^2},
$$

as desired.

```{figure} Images/Fig-Curves-DistanceToLine.png
---
width: 100%
name: Fig:Curves:DistanceToLine
class: dark-light
---
Illustration of the situation described in this proof.
```

:::{todo}
Replace {numref}`Fig:Curves:DistanceToLine` with an applet.
:::

::::

::::::{prf:corollary} 
:label: Cor:Curves:Parabola

Consider the parabola with vertex $(v_1,v_2)$ and focus $(v_1,v_2+f)$, or equivalently directrix $y=v_2-f$ (i.e. a parabola of which the axis is parallel to the $y$-axis). Then the parabola is defined by the equation

$$
 y=\frac{1}{4f}\left(x-v_1\right)^2+v_2,
$$

which means that the parabola is the graph of the function $f(x)=\frac{1}{4f}\left(x-v_1\right)^2+v_2$.

Similarly, the parabola with vertex $(v_1,v_2)$ and focus $(v_1+f,v_2)$, or equivalently directrix $x=v_1-f$ (i.e. a parabola of which the axis is parallel to the $x$-axis) is defined by the equation

$$
 x=\frac{1}{4f}\left(y-v_2\right)^2+v_1.
$$


::::::

:::{admonition} Proof of {prf:ref}`Cor:Curves:Parabola`
:class: tudproof, dropdown
Let $\mathcal{C}$ be the parabola with vertex $(v_1,v_2)$, focus $(v_1,v_2+f)$ and directrix $y=v_2-f$ (which we can write as $0\cdot x+1\cdot y-v_2+f=0$). Then by {prf:ref}`Thm:Curves:Parabola`, the parabola is defined by the equation

$$
 \frac{\left(0\cdot x+1\cdot y-v_2+f\right)^2}{0^2+1^2}=\left(x-v_1\right)^2+\left(y-(v_2+f)\right)^2.
$$

We work out some of the brackets and simplify to obtain

$$
 y^2-2v_2y+2fy+v_2^2-2v_2f+f^2=\left(x-v_1\right)^2+y^2-2v_2y-2fy+v_2^2+2v_2f+f^2.
$$

Several terms cancel out and we are left with

$$
 4fy=\left(x-v_1\right)^2+4v_2f.
$$

Upon dividing by $4f$ we obtain the desired result

$$
 y=\frac{1}{4f}\left(x-v_1\right)^2+v_2.
$$

The proof for the parabola with axis parallel to the $x$-axis is similar.



:::

::::::{prf:corollary} 
:label: Cor:Curves:Parabola2

Consider the graph of the function $f(x)=ax^2+bx+c$ with constants $a\neq 0$, $b$ and $c$. This graph is a parabola with axis $x=-\dfrac{b}{2a}$, vertex $\left(-\dfrac{b}{2a},\dfrac{4ac-b^2}{4a}\right)$, focus $\left(-\dfrac{b}{2a},\dfrac{4ac-b^2+1}{4a}\right)$ and directrix $y=\dfrac{4ac-b^2-1}{4a}$.

::::::

:::{admonition} Proof of {prf:ref}`Cor:Curves:Parabola2`
:class: tudproof, dropdown
By completing the square, we can write the equation $y=ax^2+bx+c$ as

$$
 y=a\left(x+\frac{b}{2a}\right)^2+\frac{4ac-b^2}{4a}.
$$

Comparing this to the equation in {prf:ref}`Cor:Curves:Parabola`, we note that it is of the same form. So the graph of $f$ is a parabola of which the axis is parallel to the $y$-axis. Consider the vertex $(v_1,v_2)$, focus $(v_1,v_2+f)$ and directrix $y=v_2-f$ of this parabola. According to the equation in {prf:ref}`Cor:Curves:Parabola`, we must have

$$
 y=a\left(x+\frac{b}{2a}\right)^2+\frac{4ac-b^2}{4a}=\frac{1}{4f}\left(x-v_1\right)^2+v_2.
$$

From this we can immediately read off that $a=\frac{1}{4f}$, or $f=\frac{1}{4a}$. Moreover, we can read off that $v_1=-\frac{b}{2a}$ and $v_2=\frac{4ac-b^2}{4a}$. This immediately gives the desired form of the vertex, focus and directrix of the parabola. Finally, the axis of the parabola is the line through the vertex and the focus, so it must be the line $x=-\dfrac{b}{2a}$.



:::


::::::{prf:definition} 
:label: Def:Curves:ParabolaUpDownLeftRight

Consider the parabola with vertex $(v_1,v_2)$ and focus $(v_1,v_2+f)$, or equivalently directrix $y=v_2-f$ (i.e. a parabola of which the axis is parallel to the $y$-axis). Then we say that the parabola **opens upwards** if $f>0$, while the parabola **opens downwards** if $f<0$.

Similarly, the parabola with vertex $(v_1,v_2)$ and focus $(v_1+f,v_2)$, or equivalently directrix $x=v_1-f$ (i.e. a parabola of which the axis is parallel to the $x$-axis) is **opens to the left** if $f<0$, while it opens **to the right** if $f>0$.

::::::

:::{figure} Images/Fig-Curves-Parabola4Types.png
:name: Fig:Curves:Parabola4Types
:class: dark-light

The four different types of parabolas defined in {prf:ref}`Def:Curves:ParabolaUpDownLeftRight`. Note that the names of the different types of parabolas precisely mean what we would expect them to mean.
:::

:::{todo}
Replace {numref}`Fig:Curves:Parabola4Types` with an applet.

Include names of the different types of parabolas in the applet.
:::

Finding a parametrisation for general parabolas is hard, but not so for those with axis parallel to the $y$-axis on account of {prf:ref}`Ex:Curves:CurveFunction`. 

::::::{prf:theorem} 
:label: Thm:Curves:ParabolaParam

Consider the parabola with vertex $(v_1,v_2)$ and focus $(v_1,v_2+f)$, or equivalently directrix $y=v_2-f$ (i.e. a parabola of which the axis is parallel to the $y$-axis).  Then a parametrisation is given by

$$
 x=t,\qquad y=\frac{1}{4f}\left(t-v_1\right)^2+v_2,\qquad -\infty<t<\infty.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves:ParabolaParam`
:class: tudproof, dropdown

By {prf:ref}`Cor:Curves:Hyperbola` the equation for this parabola is $y=\frac{1}{4f}\left(x-v_1\right)^2+v_2$, which means that the parabola is the graph of a function. The maximal domain of this function is $\mathbb{R}$. As such, we can use {prf:ref}`Ex:Curves:CurveFunction` to conclude that $(x,y)=\left(t,\frac{1}{4f}\left(t-v_1\right)^2+v_2\right)$ for $t$ in $\mathbb{R}$ is a parametrisation for this curve.

:::

::::::{prf:example} 
:label: Ex:Curves:Parabola1

Consider the graph of the function $f(x)=-2x^2+4x+4$. According to {prf:ref}`Cor:Curves:Parabola2`, this graph is a parabola with axis $x=1$, vertex $\left(1,6\right)$, focus $\left(1,\frac{47}{8}\right)$ and directrix $y=\frac{49}{8}$. Notice that the focus lies below the vertex, while the directrix lies above the vertex, so the parabola opens downwards. We also note that the graph of the function intersects the $y$-axis, i.e. the line $x=0$, at the point $(0,f(0))=(0,4)$. Finally, upon solving the equation $f(x)=-2x^2+4x+4=0$ we find that the graph intersects the $x$-axis, i.e. the line $y=0$, at the points $(1-\sqrt{3},0)$ and $(1+\sqrt{3},0)$. 

:::{figure} Images/Fig-Curves-Parabola1.png
:name: Fig:Curves:Parabola1
:class: dark-light

The graph of the function $f(x)=-2x^2+4x+4$ is a parabola with axis $x=1$, vertex $\left(1,6\right)$, focus $\left(1,\frac{47}{8}\right)$ and directrix $y=\frac{49}{8}$.
:::

:::{todo}
Replace {numref}`Fig:Curves:Parabola1` with an applet.
:::

A straightforward parametrisation of this parabola is given by

$$
 x=t,\qquad y=-2t^2+4t+4,\qquad -\infty<t<\infty.
$$
::::::

::::::{prf:example} 
:label: Ex:Curves:Parabola2

Consider the parabola with focus $F:(1,4)$ and directrix $y=-x+1$. Since the directrix is not parallel to the $x$- or $y$-axis, we have to use {prf:ref}`Thm:Curves:Parabola` to find an equation for this parabola. Rewriting the directrix to $x+y-1=0$, we obtain the equation

$$
 \frac{\left(x+y-1\right)^2}{2}=(x-1)^2+(y-4)^2.
$$

Now suppose we want to find the axis and vertex of this parabola. As in the proof of {prf:ref}`Thm:Curves:Parabola`, we notice that the directrix is parallel to the line $x+y=0$, which can be written in vector form as $\begin{pmatrix}1\\ 1\end{pmatrix}\cdot\begin{pmatrix}x\\ y\end{pmatrix}=0$. This means that the vector $\begin{pmatrix}1\\ 1\end{pmatrix}$ is perpendicular to the directrix. We consider the line $\mathcal{L}$ written in parametric vector form $\begin{pmatrix}x\\ y\end{pmatrix}=\begin{pmatrix}1\\ 4\end{pmatrix}+t\begin{pmatrix}1\\ 1\end{pmatrix}$. By construction, this line passes through the focal point $(1,4)$ and moves in the direction $\begin{pmatrix}1\\ 1\end{pmatrix}$. Since the line is perpendicular to the directrix, it intersects the directrix in the point closest to the focus point. Hence, it intersects the parabola at its vertex. As such, this line $\mathcal{L}$ is actually the axis of the parabola. We substitute $x=1+t$ and $y=4+t$ into the equation for the parabola to obtain

$$
 \frac{\left(1+t+4+t-1\right)^2}{2}=(1+t-1)^2+(4+t-4)^2,
$$

which simplifies to

$$
 2t^2+8t+8=2t^2.
$$

Solving this equation yields $t=-1$, so the vertex is the point $(x,y)=(1+(-1),4+(-1))=(0,3)$.

The axis of the parabola is the line $\mathcal{L}$. In order to find an equation for this line, we notice that it passes through the points $(0,3)$ and $(1,4)$. As such, it must be the line $y-x=3$.


::::::

