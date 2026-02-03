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

If $I$ is the closed interval $[a,b]$, then the point $(x,y)=(f(a),g(a))$ is called the **start point** or **initial point** of $\mathcal{C}$, while the point $(x,y)=(f(b),g(b))$ is called the **end point** or **terminal point** of $\mathcal{C}$.

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



- Ellipse
- Hyperbola
- Parabola
- Lines
- Parametrization of curves
