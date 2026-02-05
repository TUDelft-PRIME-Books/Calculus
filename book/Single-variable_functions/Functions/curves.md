(Section:Curves)=

# Curves in $\mathbb{R}^2$

(Subsec:Curvesintro)=

## Introduction

In {numref}`Subsec:Functions1dGraphs` we saw that the circle with radius $1$, centered around the origin, i.e. the unit circle, cannot be the graph of a function. Indeed, the circle fails the vertical line test ({prf:ref}`Thm:Functions1var:Verticallinetest`). Still, it is useful to find an equation discribing the circle. Because the unit circle is not the graph of a function, this equation can never be of the form $y=f(x)$, but maybe some other type of equation will do. The ciricle is defined as all points $(x,y)$ which have distance $1$ (the radius of the circle) to the origin (the center of the circle). The distance of any point $(x,y)$ to $(0,0)$ can, using the Pythagorean theorem ({prf:ref}`Thm:Trigonometry:Pythagoras`), be computed as $\sqrt{x^2+y^2}$. So all points on the circle must satisfy the equation $\sqrt{x^2+y^2}=1$, which we can simplify, by squaring, to the equation $x^2+y^2=1^2=1$. Reversely, any point $(x,y)$ that satisfies $x^2+y^2=1$ has distance $1$ to the origin, so it must lie on the circle. As such, the equation $x^2+y^2=1$ gives a precise description of the circle. We call such an equation an **implicit equation** for $x$ and $y$. It is called implicit, because knowing the value of, say, $x$ does not allow us to directly find the corresponding value(s) of $y$ or vice-versa. By contrast, an **explicit equation** is an equation of the form $y=f(x)$ or $x=g(y)$, where knowing the value of one variable directly determines the value of the other variable (though not necessarily the other way around). The equation $x^2+y^2=1$ can be turned into the explicit equations $y=\sqrt{1-x^2}$ and $y=-\sqrt{1-x^2}$, which describe, respectively, the upper and lower halves of the unit circle.

```{figure} Images/circle.png
---
width: 100%
name: Fig:Curves:Circle
class: dark-light
---
Hier een mooiere versie van dit plaatje.
The unit circle fails the vertical line test. In addition, any point $(a,b)$ on the circle satisfies $a^2+b^2=1$.
```
Hier ook nog een plaatje van de grafielen van $y=\sqrt{1-x^2}$ en $y=-\sqrt{1-x^2}$ (of misschien liever 2 losse plaatjes naast elkaar)

We can also take a look at the unit circle from a different perspective. Imagine a particle starting at the point $(1,0)$ and moving around the circle in counterclockwise direction. At time $t$, the particle has a certain position $(x,y)$ on the cirle. Since for each $t$, the particle has a unique $x$- and $y$-coordinate, we note that the $x$ and $y$ coordinates of the particle are functions of $t$, so we can write 

$$
 x=f(t), \qquad y=g(t).
$$

The equations $x=f(t),y=g(t)$ are called a **parametric equation** for the circle and $t$ is called a **parameter**. Alternatively, we say that we made a **parametrisation** of the circle. So what could these functions $f$ and $g$ be? It turns out that a single curve can have many different parametrisations. This is because the particle that moves around the circle at different speeds, possibly not even having a constant speed. As such, we have a lot of freedom in choosing out parametrisation. Still, some parametrisations are more useful than others. In order to find one for the circle, we recall from {numref}`Fig:Trigonometry:UnitCircleStandardValues` that each point $(x,y)$ on the unit circle can be represented as $x=\cos(t)$ and $y=\sin(t)$, where $t$ is the angle with respect to the positive $x$-axis. In order to obtain each point on the circle exactly once we should have, for instance, $0\leq t<2\pi$. This means that the equations

$$
 x=\cos(t),\qquad y=\sin(t),\qquad 0\leq t<2\pi
$$

are parametric equations for the unit circle. Indeed if $(x,y)=(\cos(t),\sin(t))$, then we find that

$$
 x^2+y^2=\left(\cos(t)\right)^2+\left(\sin(t)\right)^2=1,
$$ 

so that, indeed, the point $(x,y)=(\cos(t),\sin(t))$ lies on the unit circle. 


```{figure} Images/circleparam.png
---
width: 100%
name: Fig:Curves:Circleparam
class: dark-light
---
Hier een mooiere versie van dit plaatje.
The parametrisaton $x=\cos(t)$ and $y=\sin(t)$ for $0\leq t<2\pi$ describes the unit circle.
```

In this section, we will take a look at more general curves and their parametrisations. Moreover, we will consider some important classes of curves, which describe well-known geometrical objects such as ellipses and parabolas.


(Subsec:CurvesParam)=

## Curves and parametrisations

Intuitively, a curve is a line that is not necessarily straight. However, turning that definition into something mathematical can be a bit tricky. Instead, we will define a curve as a set of points that is given by some parametric equations. 

::::::{prf:definition} 
:label: Def:Curves:Paramcurve

A **parametric curve**, or simply **curve**, $\mathcal{C}$ in $\mathbb{R}^2$ is a set of points $(x,y)$ whose positions are given by **parametric equations** $x=f(t)$ and $y=g(t)$ for $t$ in some interval $I$. Here $t$ is called a **parameter**.

If $I$ is the closed interval $[a,b]$, then the point $(x,y)=(f(a),g(a))$ is called the **start point** or **initial point** of $\mathcal{C}$, while the point $(x,y)=(f(b),g(b))$ is called the **end point** or **terminal point** of $\mathcal{C}$. Whenever the start point and the end point of the curve coincide, we say that the curve is **closed**.

::::::

::::::{note}
:name: Note:Curves:Multipleparam

A curve can have many different parametrisations.

::::::

::::::{important}
:name: Important:Curves:tinterval

When writing down a parametrisation of a curve, you should always explicitly write down for which values of the parameter the parametric equations hold, i.e. a parametrisation can be of the form $x=f(t)$, $y=g(t)$ for $a\leq t\leq b$, but only writing $x=f(t)$, $y=g(t)$ is not enough.

::::::

Recall that the unit circle can also represented as the set of all points $(x,y)$ satisfying the implicit equation $x^2+y^2=1$. Alternatively, we can write this equation as $x^2+y^2-1=0$. In order to generalise this concept to other curves, we first need to define what we mean by a function of two variables.


::::::{prf:definition} 
:label: Def:Curves:Function2var

A **function of two variables** $f$ is a function of which the domain is a subset of $\mathbb{R}^2$ and the codomain is $\mathbb{R}$. For a point $(x,y)$ in the domain of $f$, we write $f(x,y)$ for the image of $(x,y)$ under $f$.

::::::

::::::{prf:definition} 
:label: Def:Curves:Implicitequation

Let $\mathcal{C}$ be a curve. Then we call an equation of the form $f(x,y)=0$ an **implicit equation**, or simply **equation**, for $\mathcal{C}$ when every point on $\mathcal{C}$ satisfies this equation, while any point not on $\mathcal{C}$ does not satisfy the equation.

::::::

::::::{prf:example} 
:label: Ex:Curves:Curve1

Consider the curve $\mathcal{C}$ that is defined by the parametric equations $x=-1+t$ and $y=t^2-3t$ for $0\leq t\leq 1$. In order to determine which curve we are dealing with, we first sketch the curve by computing the values of $x$ and $y$ for several values of $t$. This gives the following result.

Hier de plot van de kromme, nog geen vergelijking voor de kromme geven hier. Het zou misschien leuk zijn als wanneer je over de grafiek hovert je de bijbehorende waarden van $x$, $y$ en vooral ook $t$ te zien krijgt.

Note that in the sketch, the parameter $t$ is not visible directly. Indeed, each value of $t$ gives a point $(x,y)=(-1+t,t^2-3t)$ on the curve. The interpretation of this parameter is that we consider a particle that starts at the initial point of the curve and at time $t$ is at position $(x,y)=(-1+t,t^2-3t)$.

This sketch suggest that we might be dealing with a part of the graph of a quadratic function, i.e. that $y=ax^2+bx+c$ for some constants $a$, $b$ and $c$. Indeed, we note that $x$ depends linearly on $t$, while $y$ depends quadratically on $t$. We can now try to find the values of these constants $a$, $b$ and $c$ by substituting the expressions $x=-1+t$ and $y=t^2-3t$ into the equation $y=ax^2+bx+c$. This gives

$$
 t^2-3t=y=ax^2+bx+c=a\left(-1+t\right)^2+b\left(-1+t\right)+c=at^2+\left(-2a+b\right)t+a-b+c.
$$

Two quadratic expressions in $t$ can only be equal when the coefficients for $t^2$ are equal in both expressions, and the coefficients for $t$ are equal in both expressions, and the constant terms are equal in both expressions. As such, we find that $a$, $b$ and $c$ need to satisfy the three equations

$$
 \left\{\begin{array}{lcll}1&=&a,\qquad &(\text{coefficients of }t^2,)\\ -3&=&-2a+b,\qquad &(\text{coefficients of }t,)\\ 0&=&a-b+c,\qquad &(\text{constant terms.})\end{array}\right.
$$

Solving these equations gives $a=1$, $b=-1$ and $c=-2$. As such, the curve describes part of the graph of the function $f(x)=x^2-x-2$. 

The start point of the curve can be found by considering the lowest value of $t$. Since we have $0\leq t\leq1$, the start point of the curve is the point $(x,y)=(-1+0,0^2-3\cdot0)=(-1,0)$. Similarly, the end point of the curve is the point $(x,y)=(-1+1,1^2-3\cdot 1)$.

::::::

::::::{prf:example} 
:label: Ex:Curves:Curvefunction

Consider any function $f$ of one variable. Then any point $(x,y)$ on the graph satisfies the equation $y=f(x)$, or $y-f(x)=0$. As such, we can think of the graph of $f$ as a curve in $\mathbb{R}^2$. So, what would be a parametrisation for this curve? Since a curve can have many different parametrisations, we have at least some freedom in how we choose our parametrisation. The important thing to notice here is that if we know what $x$, we can compute what the corresponding value of $y$ is by plugging $x$ into the function. As such, it is convenient to choose $x=t$. Then necessarily, we must have $y=f(x)=f(t)$ in order for $(x,y)$ to lie on the curve. As such, $x=t$ and $y=f(t)$ for $t$ in the domain of $f$ is a parametrisation of the graph of $f$.

As a more explicit example, consider the function $f(x)=-\sqrt{4-x^2}$. Note that the domain of this function is given by $-2\leq x\leq 2$, since these are the only values of $x$ for which $4-x^2\geq 0$. By our previous considerations, $x=t$ and $y=-\sqrt{4-t^2}$ for $-2\leq t\leq 2$ is a parametrisation of the graph of $f$. We can wonder however, whether in this specific case this parametrisation is the most convenient one. Indeed, note that the graph of $f$ is the lower half of the circle $x^2+y^2=4$. For (parts of) circles, it is often more convenient to use sines and or cosines as a parametrisation. Here, we could choose $x=2\cos(t)$ and $y=2\sin(t)$. Indeed, in that case we have

$$
 x^2+y^2=\left(2\cos(t)\right)^2+\left(2\sin(t)\right)^2=4\left(\cos^2(t)+\sin^2(t)\right)=4\cdot 1=4.
$$

In order to ensure that we only parametrise the lower half of the circle, we should **not** use $0\leq t\leq 2\pi$, since that would paremetrise the entire circle. Instead, we could either use $-\pi\leq t\leq 0$ or $\pi\leq t\leq 2\pi$ (or something more exotic like $9\pi\leq t\leq 10\pi$). We conclude that $x=t$ and $y=-\sqrt{4-t^2}$ for $-2\leq t\leq 2$ and $x=2\cos(t)$ and $y=2\sin(t)$ for $\pi\leq t\leq 2\pi$ are both valid parametrisations of the same curve, but in computations the latter one is often the nicer one to work with.

::::::

::::::{prf:example} 
:label: Ex:Curves:FoliumDescartes

One of the most famous examples of curves defined by an implicit equation is the **folium of Descartes**. It is named after the French philosopher and mathematician [René Descartes (1596-1650)](https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes). One version of this curve, is the one given by the equation $x^3+y^3=3xy$. A plot of this curve is shown below.

Hier plot van deze versie van folium.

As we can see in the plot, the curve fails the vertical line test, so it cannot be the graph of a function. However, when we cut up the curve in several parts in the right way, we can obtain curves that are the graphs of functions. One such way is shown in the figure below.

```{figure} Images/descartesfolium.png
---
width: 100%
name: Fig:Curves:Descartesfoliumcut
class: dark-light
---
Hier een mooiere versie van dit plaatje.
The curve has been cut up in $3$ pieces, all of which are the graph of a function.
```

It is very hard to find an explicit expression for one of these functions. Still, if $f$ is one of these functions, we necessarilly must have that

$$
 x^3+\left(f(x)\right)^3=3xf(x)
$$

for each $x$ in the domain of $f$, since the graph of $f$ is part of the curve $x^3+y^3=3xy$. 

Finding a parametrisation for the folium of Descartes is very tricky, as there is no obvious way to start. It turns out that $x=\frac{3t}{1+t^3}$ and $y=\frac{3t^2}{1+t^3}$ for $-\infty<t<-1$ and $-1<t<\infty$ gives a parametrisation of this curve. Indeed, for any $t\neq -1$ we have

$$
 x^3+y^3=\left(\frac{3t}{1+t^3}\right)^3+\left(\frac{3t^2}{1+t^3}\right)^3=\frac{27t^3}{(1+t^3)^3}+\frac{27t^6}{(1+t^3)^3}=\frac{27t^3(1+t^3)}{(1+t^3)^3}=\frac{27t^3}{(1+t^3)^2}
$$

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

```{figure} Images/ellipse.png
---
width: 100%
name: Fig:Curves:Ellipse
class: dark-light
---
Hier een mooiere versie van dit plaatje.
An ellipse with focal points $F_1$ and $F_2$ such that for each point $A$ on the ellipse the sum of the distances to $F_1$ and $F_2$ is $2a$. The center $C$ and the distance $c$ between the center and any focal point are also shown, as are the vertices $V_1$ and $V_2$ and the co-vertices $W_1$ and $W_2$ of the ellipse.
```

In order to find an equation for an ellipse, we will, for convenience, first assume that the center of the ellipse is the origin and that the major axis is either the $x$-axis or $y$-axis. In that case we obtain the following result.

::::::{prf:theorem} 
:label: Thm:Curves:Ellipse

Let $a>0$ and $b>0$ and consider an ellipse with of which the vertices and covertices are $(a,0)$, $(-a,0)$, $(0,b)$ and $(0,-b)$ (so that the center of the ellipse is at the origin and the major axis is either the $x$-axis (when $a\geq b$) or the $y$-axis (when $a\leq b$)). Then the ellipse is described by the equation

$$
 \frac{x^2}{a^2}+\frac{y^2}{b^2}=1.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves:Ellipse`
:class: tudproof, dropdown
For convenience, we assume that the major axis of the ellipse is the $x$-axis. In that case, the focal points are $(c,0)$ and $(-c,0)$ for some $0\leq c<a$. Since the sum of the distances from $(a,0)$ to $(c,0)$ and to $(-c,0)$ is $(a-c)+(a-(-c))=2a$, we find that the ellipse consists of all points of which the sum of the distances to $(c,0)$ and $(-c,0)$ is $2a$. By symmetry the distance from $(0,b)$ to $(c,0)$ and to $(-c,0)$ must be equal, so both distances must be $a$ (as their sum should be $2a$ since $(0,b)$ is on the ellipse). By considering the triangle in {numref}`Fig:Curves:Ellipse2` and using the Pythagorean theorem ({prf:ref}`Thm:Trigonometry:Pythagoras`), we find that $b^2+c^2=a^2$, which we will use later in the proof.

```{figure} Images/ellipse2.png
---
width: 100%
name: Fig:Curves:Ellipse2
class: dark-light
---
Hier een mooiere versie van dit plaatje.
Illustration of the ellipse used in this proof.
```

For any point $(x,y)$ on the ellipse, the distance to $(c,0)$ is $\sqrt{(x-c)^2+(y-0)^2}=\sqrt{(x-c)^2+y^2}$, while the distance to $(-c,0)$ is $\sqrt{(x-(-c))^2+(y-0)^2}=\sqrt{(x+c)^2+y^2}$. Hence, $(x,y)$ is on the ellipse precisely when

$$
 \sqrt{(x-c)^2+y^2}+\sqrt{(x+c)^2+y^2}=2a.
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
:::

::::::{prf:corollary} 
:label: Cor:Curves:Ellipse

Let $a>0$ and $b>0$ and consider an ellipse with of which the vertices and covertices are $(x_0+a,y_0)$, $(x_0-a,y_0)$, $(x_0+b,y_0)$ and $(x_0-b,y_0)$ (so that the center of the ellipse is at the point $(x_0,y_0)$ and the axes are the lines $x=x_0$ and $y=y_0$). Then the ellipse is described by the equation

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
:label: Thm:Curves:Ellipseparam

LLet $a>0$ and $b>0$ and consider an ellipse with of which the vertices and covertices are $(x_0+a,y_0)$, $(x_0-a,y_0)$, $(x_0+b,y_0)$ and $(x_0-b,y_0)$ (so that the center of the ellipse is at the point $(x_0,y_0)$ and the axes are the lines $x=x_0$ and $y=y_0$). Then 

$$
 x(t)=x_0+a\cos(t),\qquad y(t)=y_0+b\sin(t),\qquad 0\leq t\leq 2\pi
$$ 

is a parametrisation for the ellipse that traverses the ellipse once in counterclockwise direction for which the start and endpoint are both the (co-)vertex $(x_0+a,y_0)$. 

This parametrisation is called the **standard parametrisation** of the ellipse.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves:Ellipseparam`
:class: tudproof, dropdown
By {prf:ref}`Cor:Curves:Ellipse` the equation for this ellipse is $\displaystyle \frac{\left(x-x_0\right)^2}{a^2}+\frac{\left(y-y_0\right)^2}{b^2}=1$. Writing $x(t)=x_0+a\cos(t)$ and $y(t)=y_0+b\sin(t)$, we find

$$
 \frac{\left(x(t)-x_0)^2}{a^2}+\frac{\left(y(t)-y_0\right)^2}{b^2}=\frac{a^2\cos^2(t)}{a^2}+\frac{b^2\sin^2(t)}{b^2}=\cos^2(t)+\sin^2(t)=1.
$$

As such, any point of the form $(x,y)=(x_0+a\cos(t),y_0+b\sin(t))$ satisfies the equation of the ellipse, so we are indeed dealing with a parametrisation of (possibly a part of) the ellipse. Note that $t=0$ we have $(x(0),y(0))=(x_0+a\cos(0),y_0+b\sin(0))=(x_0+a,y_0)$ and at $t=2\pi$ we have $(x(2\pi),y(2\pi))=(x_0+a\cos(2\pi),y_0+b\sin(2\pi))=(x_0+a,y_0)$, so that the start and endpoint are, indeed, both the (co-)vertex $(x_0+a,y_0)$. 

Now we show that this parametrisation covers the ellips exactly once (except the (co-)vertex $(x_0+a,y_0)$, which is both the start and end point). Consider any point $(x,y)$ on the ellipse. We claim that the point $\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)$ lies on the unit circle. Indeed, we have

$$
 \left(\frac{x-x_0}{a}\right)+\left(\frac{y-y_0}{b}\right)=\frac{\left(x-x_0\right)^2}{a^2}+\frac{\left(y-y_0\right)^2}{b^2}=1,
$$

since $(x,y)$ lies on the ellipse. As such, the point $\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)$ satisfies the equation defining the unit circle. From {numref}`Subsec:TrigonRatio` we know that there is exactly one value of $t$ with $0\leq t<2\pi$ for which $\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)=\left(\cos(t),\sin(t)\right)$. For this value of $t$ we find that $x=x_0+a\cos(t)$ and $y=y_0+b\sin(t)$, as desired.

Finally, we notice that for $0<t<\frac{\pi}{2}$ we have $y(t)=y_0+b\sin(t)>0$, which must mean that the we parametrise the circle in counterclockwise direction.

:::

::::::{prf:remark} 
:label: Remark:Curves:Ellipseparam

Consider the parametrisation of an ellipse from {prf:ref}`Thm:Curves:Ellipseparam`. If the ellipse is actually a circle (so when $a=b$, or, equivalently, $c=0$), the parameter $t$ has the interpretation as the angle between the positive $x$-axis and the line segement from the origin to the point $(x(t),y(t))$ measured counterclockwise, as usual. However, for ellipses that are not circles this is not the case. The French painter and mathematician  [Philippe de la Hire (1640-1718)](https://en.wikipedia.org/wiki/Philippe_de_La_Hire) discovered the following interpretation of the parameter $t$. Consider two circles with the same center as the ellipse with radius $b$ and $a$ respectively. If we draw the line segement which has angle $t$ with the positive $x$-axis, then this line segment crosses the first circle at the point $B:(x_0+b\cos(t),y_0+b\sin(t))$ and the second circle at the point $A:(x_0+a\cos(t),y_0+b\sin(t))$. Then the point $(x,y)=(x_0+a\cos(t),y_0+b\sin(t))$ on the ellipse is found by intersecting the line through $B$ parallel to the major axis of the ellipse with the line through $A$ parallel to the minor axis of the ellipse, see the figure below.

```{figure} Images/delaHire.png
---
width: 100%
name: Fig:Curves:delaHire
class: dark-light
---
Plaatje gejat van wikipedia dus moet ofwel nagemaakt ofwel verwezen. Er staat op wikipedia ook een animatie hiervan, dat is misschien ook nuttig om zoiets erbij te doen (https://en.wikipedia.org/wiki/File:Parametric_ellipse.gif)
```
::::::


::::::{prf:example} 
:label: Example:Curves:Ellipse

Consider the ellipse with vertices $(-1,2)$ and $(-1,8)$ and co-vertices $(-3,5)$ and $(1,5)$. Then the major axis of the ellipse is the line $x=-1$, while the minor axis is the line $y=5$. As such, the center of the ellipse is the intersection of these axes, which is the point $(-1,5)$. The distance from the center to the vertices is $3$, while the distance from the center to the covertices is $2$. According to {prf:ref}`Cor:Curves:Ellipse`, the ellipse is defined by the equation

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

Note that both at $t=0$ and at $t=2\pi$ we have $(x(t),y(t))=(-1,8)$, so this curve starts and ends at the vertex $(-1,8)$. Moreover, since the fundamental period of the sine and cosine is $2\pi$, the fudamental period of $\sin(2t)$ and $\cos(2t)$ must be $\pi$ (see {numref}`Subsec:PropertisfunctionsPeriodic`). So the parametrisation covers the ellipse **twice**. Indeed, for any $0\leq t\leq \pi$ we have

$$
 (x(t+\pi),y(t+\pi))=\left(-1+2\sin(2(t+\pi)),5+3\cos(2(t+\pi))\right)=\left(-1+2\sin(2t+2\pi),5+3\cos(2t+2\pi)\right)=\left(-1+2\sin(2t),5+3\cos(2t)\right)=(x(t),y(t)).
$$

Finally, we notice that for $0<t<\frac{\pi}{4}$ we have $x(t)>-1=x(0)$, so the parametrisation describes a clockwise traversion of the ellipse.

Hier nog een plaatje van de ellips in kwestie.
::::::

It is also possible to find equations and parametrisations for ellipses of which the major axis is not a horizontal or vertical line. However, this requires quite some knowledge of linear algebra. More information on this can be found in the relevant section of the [Open Linear Algebra book](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter8/QuadraticForms.html#conic-sections).

(Subsec:CurvesHyperbola)=

## Hyperbolas

Hyperbolas are another common type of curves that are (often) not the graph of a function. Hyperbola share quite some similarities with ellipses in terms of the definition and the equations describing them, though they look very differently geometrically. As such, we will mainly follow the same structure as in the previous section.


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
Hier een mooiere versie van dit plaatje.
A hyperbola with focal points $F_1$ and $F_2$ such that for each point $A$ on the hyperbola the sum of the distances to $F_1$ and $F_2$ is $2a$. The center $C$ and the vertices $V_1$ and $V_2$ and of the hyperbola are also shown.
```

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

Consider any point $(x,y)$ on the hyperbola. Assume, for convenience, that the point $(-c,0)$ is the point closes to $(x,y)$. Then the distance to $(c,0)$ is $\sqrt{(x-c)^2+(y-0)^2}=\sqrt{(x-c)^2+y^2}$, while the distance to $(-c,0)$ is $\sqrt{(x-(-c))^2+(y-0)^2}=\sqrt{(x+c)^2+y^2}$. Hence, $(x,y)$ is on the hyperbola precisely when

$$
 \left|\sqrt{(x-c)^2+y^2}-\sqrt{(x+c)^2+y^2}\right|=2a.
$$

Since we assumed that $(-c,0)$ is the closest point to $(x,y)$, we can ignore the absoute value. We bring $\sqrt{(x+c)^2+y^2}$ to the other side of the equation and take the square of both sides of the equation to obtain

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

We first consdier the hyperbola of which the vertices are $(x_0-a,y_0)$ and $(x_0+a,y_0)$ and the focal points are $(x_0-c,y_0)$ and $(x_0+c,y_0)$. Writing $p=x-x_0$ and $q=y-y_0$, we note that in the $pq$-plane, the curve becomes a hyperbola with vertices $(-a,0)$ and $(a,0)$ and focal points $(-c,0)$ and $(c,0)$. By {prf:ref}`Thm:Curves:Hyperbola`, the equation for this hyperbola is

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

A common parametrisation of an hyperbola uses the hyperbolic cosine and sine functions, see {prf:ref}`Def:Propertiesfunctions:Hyperbolic`.

::::::{prf:theorem} 
:label: Thm:Curves:Hyperbolaparam

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

:::{admonition} Proof of {prf:ref}`Thm:Curves:Hyperbolaparam`
:class: tudproof, dropdown


TOT HIER!

By {prf:ref}`Cor:Curves:Hyperbola` the equation for this hyperbola is $\displaystyle \frac{\left(x-x_0\right)^2}{a^2}+\frac{\left(y-y_0\right)^2}{b^2}=1$. Writing $x(t)=x_0+a\cos(t)$ and $y(t)=y_0+b\sin(t)$, we find

$$
 \frac{\left(x(t)-x_0)^2}{a^2}+\frac{\left(y(t)-y_0\right)^2}{b^2}=\frac{a^2\cos^2(t)}{a^2}+\frac{b^2\sin^2(t)}{b^2}=\cos^2(t)+\sin^2(t)=1.
$$

As such, any point of the form $(x,y)=(x_0+a\cos(t),y_0+b\sin(t))$ satisfies the equation of the ellipse, so we are indeed dealing with a parametrisation of (possibly a part of) the ellipse. Note that $t=0$ we have $(x(0),y(0))=(x_0+a\cos(0),y_0+b\sin(0))=(x_0+a,y_0)$ and at $t=2\pi$ we have $(x(2\pi),y(2\pi))=(x_0+a\cos(2\pi),y_0+b\sin(2\pi))=(x_0+a,y_0)$, so that the start and endpoint are, indeed, both the (co-)vertex $(x_0+a,y_0)$. 

Now we show that this parametrisation covers the ellips exactly once (except the (co-)vertex $(x_0+a,y_0)$, which is both the start and end point). Consider any point $(x,y)$ on the ellipse. We claim that the point $\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)$ lies on the unit circle. Indeed, we have

$$
 \left(\frac{x-x_0}{a}\right)+\left(\frac{y-y_0}{b}\right)=\frac{\left(x-x_0\right)^2}{a^2}+\frac{\left(y-y_0\right)^2}{b^2}=1,
$$

since $(x,y)$ lies on the ellipse. As such, the point $\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)$ satisfies the equation defining the unit circle. From {numref}`Subsec:TrigonRatio` we know that there is exactly one value of $t$ with $0\leq t<2\pi$ for which $\left(\frac{x-x_0}{a},\frac{y-y_0}{b}\right)=\left(\cos(t),\sin(t)\right)$. For this value of $t$ we find that $x=x_0+a\cos(t)$ and $y=y_0+b\sin(t)$, as desired.

Finally, we notice that for $0<t<\frac{\pi}{2}$ we have $y(t)=y_0+b\sin(t)>0$, which must mean that the we parametrise the circle in counterclockwise direction.

:::

- Ellipse
- Hyperbola
- Parabola
- Lines
- Parametrization of curves
