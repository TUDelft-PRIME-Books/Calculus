(Section:Curves)=

# Implicit equations in $\mathbb{R}^2$

(Subsec:CurvesIntro)=

## Introduction

In {numref}`Subsec:Functions1dGraphs` we saw that the circle with radius $1$, centered around the origin, i.e. the unit circle, cannot be the graph of a function. Indeed, the circle fails the vertical line test ({prf:ref}`Thm:Functions1var:VerticalLineTest`). Still, it is useful to find an equation describing the circle. Because the unit circle is not the graph of a function, this equation can never be of the form $y=f(x)$, but maybe some other type of equation will do. The circle is defined as the set of all points $(x,y)$ which have distance $1$ (the radius of the circle) to the origin (the center of the circle). The distance of any point $(x,y)$ to $(0,0)$ can, using the Pythagorean theorem ({prf:ref}`Thm:Trigonometry:Pythagoras`), be computed as $\sqrt{x^2+y^2}$. So all points on the circle must satisfy the equation $\sqrt{x^2+y^2}=1$, which we can simplify, by squaring, to the equation $x^2+y^2=1^2=1$. Conversely, any point $(x,y)$ that satisfies $x^2+y^2=1$ has distance $1$ to the origin, so it must lie on the circle. As such, the equation $x^2+y^2=1$ gives a precise description of the circle. We call such an equation an **implicit equation** for $x$ and $y$. It is called implicit, because knowing the value of, say, $x$ does not allow us to directly find the corresponding value(s) of $y$ or vice-versa. By contrast, an **explicit equation** is an equation of the form $y=f(x)$ or $x=g(y)$, where knowing the value of one variable directly determines the value of the other variable (though not necessarily the other way around). The equation $x^2+y^2=1$ can be turned into the explicit equations $y=\sqrt{1-x^2}$ and $y=-\sqrt{1-x^2}$, which describe, respectively, the upper and lower halves of the unit circle.

:::{applet}
:url: calculus/curves_in_R%5E2/vertical_line_test_for_the_unit_circle
:name: Fig:Curves:Circle
:class: dark-light

The unit circle fails the vertical line test. In addition, any point $(a,b)$ on the circle satisfies $a^2+b^2=1$.
:::

:::{applet}
:url: calculus/curves_in_R%5E2/vertical_line_test_for_two_unit_semi-circles
:name: Fig:Curves:CircleExplicit
:class: dark-light

The two explicit equations $y=\sqrt{1-x^2}$ and $y=-\sqrt{1-x^2}$ describe the upper and lower halves of the unit circle, respectively.
:::



In this section, we will take a look at more general curves that are described by implicit equations. Moreover, we will consider some important classes of curves, which describe well-known geometrical objects such as ellipses, hyperbolas and parabolas.


(Subsec:CurvesParam)=

## Implicit equations

[^FootnoteDef]: In this section, we will not give a formal definition of what we mean by a curve. Instead, we assume that we have some sort of intuitive understandig of what a curve is: a line in $\mathbb{R}^2$ that is not necessarily straight. In \numref{Sec:CurvesR2} we will give a proper definition of a curve.

Recall that the unit circle can represented as the set of all points $(x,y)$ satisfying the implicit equation $x^2+y^2=1$. Alternatively, we can write this equation as $x^2+y^2-1=0$. In order to generalise this concept to other curves[^FootnoteDef], we first need to define what we mean by a function of two variables. These function will be studied in way more depth in {numref}`Sec:MultivariableFunctions`.


::::::{prf:definition} 
:label: Def:Curves:Function2var

A **function of two variables** $f$ is a function of which the domain is a subset of $\mathbb{R}^2$ and the codomain is $\mathbb{R}$. For a point $(x,y)$ in the domain of $f$, we write $f(x,y)$ for the image of $(x,y)$ under $f$.

::::::

::::::{prf:definition} 
:label: Def:Curves:ImplicitEquation

Let $\mathcal{C}$ be a curve. Then we call an equation of the form $f(x,y)=0$ an **implicit equation**, or simply **equation**, for $\mathcal{C}$ when every point on $\mathcal{C}$ satisfies this equation, while any point not on $\mathcal{C}$ does not satisfy the equation.

::::::


::::::{prf:example} 
:label: Ex:Curves:FoliumDescartes

One of the most famous examples of curves defined by an implicit equation is the **folium of Descartes**. It is named after the French philosopher and mathematician [René Descartes (1596-1650)](https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes). One version of this curve is the one given by the equation $x^3+y^3=3xy$. A plot of this curve is shown below.

:::{applet}
:url: calculus/curves_in_R%5E2/folium_of_Descartes
:name: Fig:Curves:FoliumOfDescartes
:class: dark-light

One example of the folium of Descartes is the curve defined by the equation $x^3+y^3=3xy$.
:::

As we can see in the plot, the curve fails the vertical line test, so it cannot be the graph of a function. However, when we cleverly cut up the curve in several parts, we can obtain curves that are the graphs of functions. One possibility is shown in the figure below.

:::{applet}
:url: calculus/curves_in_R%5E2/three_parts_of_the_folium_of_Descartes
:name: Fig:Curves:DescartesFoliumCut
:class: dark-light

The curve in {numref}`Fig:Curves:FoliumOfDescartes` has been cut in three pieces, shown in the _top-left_, _top-right_ and the _bottom-left_, all of which are the graph of a function.
:::

It is very hard to find an explicit expression for one of these functions. Still, if $f$ is one of these functions, we necessarily must have that

$$
 x^3+\left(f(x)\right)^3=3xf(x)
$$

for each $x$ in the domain of $f$, since the graph of $f$ is part of the curve $x^3+y^3=3xy$. 



::::::


(Subsec:CurvesEllipses)=

## Circles and ellipses

A very common type of curves that cannot be described as the graph of some function are ellipses, which includes circles. Before, we give the (rather technical) definition, we first consider an example.

::::::{prf:example} 
:label: Def:Curves:Prelimellipse
Consider the curve given by the equation

$$
 \frac{x^2}{25}+\frac{y^2}{16}=1.
$$

This curve is shown in {numref}`Fig:Curves:Prelimellipse`. You likely already know that we call such a curve an ellipse (or otherwise, it is not an unreasonable guess), but what geometrical properties makes this curve an ellipse? In  {numref}`Fig:Curves:Prelimellipse` we have highlighted the two points $(-3,0)$ and $(3,0)$. These points are called the **focal points** of the ellipse. The defining property of an ellipse is that it is the set of all points $(x,y)$ where the sum of distances to the two focal points is constant. This can be seen in the figure by dragging the pulsing point around the ellipse.

:::{applet}
:url: calculus/curves_in_R%5E2/introduction_to_ellipses
:name: Fig:Curves:Prelimellipse
:class: dark-light

The ellipse defined by $\frac{x^2}{25}+\frac{y^2}{16}=1$.
:::

::::::

Now, we give a geometrical description of these objects and then we try to find useful equations describing them.

::::::{prf:definition} 
:label: Def:Curves:Ellipse

An **ellipse** is a curve in $\mathbb{R}^2$ surrounding two points, called the **focal points** of the ellipse, such that for all points on the curve, the sum of the distances to the two focal points is a constant $2a$ that is greater than the distance between the focal points. A **circle** is an ellipse for which the two focal points coincide.

The midpoint of the line segment joining the two focal points is called the **center** of the ellipse. In case the ellipse is not a circle, the line through the focal points is called the **major axis** of the ellipse, while the line perpendicular to the major axis is called the **minor axis** of the ellipse. The intersection points of the major axis with the ellipse are called the **vertices** of the ellipse, while the intersection points of the minor axis with the ellipse are called the **co-vertices**.

If $c$ denotes the distance from any focal point to the center, the number $e=\frac{c}{a}$ is called the **eccentricity** of the ellipse.
::::::

:::{applet}
:url: calculus/curves_in_R%5E2/definition_of_an_ellipse
:name: Fig:Curves:Ellipse
:class: dark-light

An ellipse with focal points $F_1$ and $F_2$ such that for each point $A$ on the ellipse the sum of the distances to $F_1$ and $F_2$ is $\operatorname{dist}(V_1,V_2)<\operatorname{dist}(F_1,F_2)$. The center $C$ is also shown, as are the vertices $V_1$ and $V_2$ and the co-vertices $W_1$ and $W_2$ of the ellipse.
:::

In order to find an equation for an ellipse, we will, for convenience, first assume that the center of the ellipse is the origin and that the major axis is either the $x$-axis or $y$-axis. In that case we obtain the following result.

::::::{prf:theorem} 
:label: Thm:Curves:Ellipse

Let $a>0$ and $b>0$ and consider an ellipse of which the vertices and co-vertices are $(a,0)$, $(-a,0)$, $(0,b)$ and $(0,-b)$ (so that the center of the ellipse is at the origin). Let $c\geq 0$ be the distance between the focal points.

- If $a>b$, the major axis is the $x$-axis and we have $b^2=a^2-c^2$.
- If $a<b$, the major axis is the $y$-axis and we have $a^2=b^2-c^2$.
- If $a=b$, the ellipse is a circle and we have $c=0$.


In each of these cases, the ellipse is described by the equation

$$
 \frac{x^2}{a^2}+\frac{y^2}{b^2}=1.
$$

::::::

::::{admonition} Proof of {prf:ref}`Thm:Curves:Ellipse`
:class: tudproof, dropdown
For convenience, we assume that the major axis of the ellipse is the $x$-axis. In that case, the focal points are $(c,0)$ and $(-c,0)$ for some $0\leq c<a$. Since the sum of the distances from $(a,0)$ to $(c,0)$ and to $(-c,0)$ is $(a-c)+(a-(-c))=2a$, we find that the ellipse consists of all points of which the sum of the distances to $(c,0)$ and $(-c,0)$ is $2a$. By symmetry the distance from $(0,b)$ to $(c,0)$ and to $(-c,0)$ must be equal, so both distances must be $a$ (as their sum should be $2a$ since $(0,b)$ is on the ellipse). By considering the triangle in the figure below and using the Pythagorean theorem ({prf:ref}`Thm:Trigonometry:Pythagoras`), we find that $b^2+c^2=a^2$, which we will use later in the proof.

:::{applet}
:url: calculus/curves_in_R%5E2/proof_of_equation_of_ellipse
:name: Fig:Curves:Ellipse2
:class: dark-light
:nonumber:

Illustration of the ellipse used in this proof.
:::

For any point $P:(x,y)$ on the ellipse, the distance to $F_1:(c,0)$ is $\sqrt{(x-c)^2+(y-0)^2}=\sqrt{(x-c)^2+y^2}$, while the distance to $F_2:(-c,0)$ is $\sqrt{(x-(-c))^2+(y-0)^2}=\sqrt{(x+c)^2+y^2}$. Hence, $(x,y)$ is on the ellipse precisely when

$$
 \operatorname{dist}(P,F_1)+\operatorname{dist}(P,F_2)=\sqrt{(x-c)^2+y^2}+\sqrt{(x+c)^2+y^2}=2a.
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

Working out the brackets on the left-hand side of the equation and regrouping the terms gives

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

Let $a>0$ and $b>0$ and consider an ellipse of which the vertices and co-vertices are $(x_0+a,y_0)$, $(x_0-a,y_0)$, $(x_0,y_0+b)$ and $(x_0,y_0-b)$ (so that the center of the ellipse is at the point $(x_0,y_0)$ and the axes are the lines $x=x_0$ and $y=y_0$). Then the ellipse is described by the equation

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

::::{question}
:type: multiple-choice
:variant: single-select
:admonition:
:class: question
:showanswer:

What is the eccentricity of a circle with radius $a$?
---
[x] $0$.
> That is correct. A circle is a special case of an ellipse in which the two foci coincide at the centre. Since the distance from the centre to a focus is $c=0$ the eccentricity is $e=\dfrac{c}{a}={0}{a}=0$.
[ ] Undefined.
> Does a circle have foci? And a center? And a (co-)vertices?
[ ] $\infty$.
> You probable used the formula $e=\dfrac{a}{c}$. Is that the correct formula?
[ ] $1$.
> In case of a circle, do the foci lie on the circle, or somewhere else?
---
::::




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

:::{todo}

Make a version of {numref}`Fig:CurvesR2:Ellipse3` that only shows the ellipse, and not the paramterisation (so only 1 figure).
:::

::::::

It is also possible to find equations for ellipses of which the major axis is not a horizontal or vertical line. However, this requires quite some knowledge of linear algebra. More information on this can be found in the relevant section of the [Open Linear Algebra book](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter8/QuadraticForms.html#conic-sections).

(Subsec:CurvesHyperbola)=

## Hyperbolas

Hyperbolas are another common type of curves that are (often) not the graph of a function. Hyperbola share quite some similarities with ellipses in terms of the definition and the equations describing them, though they look very differently geometrically. In fact, both are examples of **conic sections**, see the [Open Linear Algebra book](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter8/QuadraticForms.html#conic-sections). 

Just like for ellipses, we first consider a preliminary example before we introduce the technical definition.

::::::{prf:example} 
:label: Def:Curves:Prelimhyp
Consider the curve given by the equation

$$
 \frac{x^2}{9}-\frac{y^2}{16}=1.
$$

This curve is shown in {numref}`Fig:Curves:Prelimhyp`. As you can reasonably guess, we will call this curve a hyperbola. What geometrical properties make this curve a hyperbola?

:::{applet}
:url: calculus/curves_in_R%5E2/introduction_to_hyperbolas
:name: Fig:Curves:Prelimhyp
:class: dark-light

The hyperbola defined by $\frac{x^2}{9}-\frac{y^2}{16}=1$.
:::

In {numref}`Fig:Curves:Prelimhyp` we have highlighted the two points $(-5,0)$ with a square and $(5,0)$ with a triangle. These points are called the **focal points** of the ellipse. The defining property of an hyperbola is that it is the set of all points $(x,y)$ where the absolute difference of the distances to the two focal points is constant.

This can be seen in the figure by dragging the pulsing diamond around the hyperbola. If the diamond is on the left part of the hyperbola, the distance between the square and diamond minus the distance between the triangle and the diamond stays the same, as indicated by the filled circle around the diamond.

If you drag the diamond to the right part of the hyperbola, the distance between the triangle and diamond minus the distance between the square and the diamond stays the same, as also indicated by the filled circle around the diamond.
::::::


::::::{prf:definition} 
:label: Def:Curves:Hyperbola

A **hyperbola** is a curve in $\mathbb{R}^2$ such that there are two points, called the **focal points** of the hyperbola, such that for all points on the curve, the absolute difference of the distances to the two focal points is a constant $2a$. 

The midpoint of the line segment joining the two focal points is called the **center** of the hyperbola. The line through the focal points is called the **major axis** of the hyperbola. The intersection points of the major axis with the hyperbola are called the **vertices** of the hyperbola. The line through the center perpendicular to the major axis is called the **minor axis** of the hyperbola.

If $c$ denotes the distance from any focal point to the center, the number $e=\frac{c}{a}$ is called the **eccentricity** of the hyperbola.
::::::

:::{applet}
:url: calculus/curves_in_R%5E2/definition_of_a_hyperbola
:name: Fig:Curves:Hyperbola
:class: dark-light

A hyperbola with focal points $F_1$ and $F_2$ such that for each point $A$ on the hyperbola the absolute difference between the distances to $F_1$ and $F_2$ is $\operatorname{dist}(V_1,V_2)>\operatorname{dist}(F_1,F_2)$. The center $C$ and the vertices $V_1$ and $V_2$ of the hyperbola are also shown.
:::

In order to find an equation for a hyperbola, we will first assume, for convenience, that the center of the hyperbola is the origin and that the major axis is the $x$-axis. In that case we obtain the following result.

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

Similarly, the hyperbola of which the vertices are $(x_0,y_0-a)$ and $(x_0,y_0+a)$ and the focal points are $(x_0,y_0-c)$ and $(x_0,y_0+c)$ (so that the center of the hyperbola is at the point $(x_0,y_0)$ and the major axis is the line $x=x_0$) is described by the equation

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



::::::{prf:example} 
:label: Ex:Curves:Hyperbola1

Consider the hyperbola with vertices $(0,0)$ and $(4,0)$ and focal points $(-1,0)$ and $(5,0)$. Since the vertices both lie on the $x$-axis, the $x$-axis is the major axis of this hyperbola. In addition, the center of the hyperbola is the midpoint of the line segment joining the vertices, so the midpoint must be $(2,0)$. The distance from the center to the vertices is $2$ and the distance from the center to the focal points is $3$. As such, according to {prf:ref}`Cor:Curves:Hyperbola` an equation for the hyperbola is given by

$$
 \frac{(x-2)^2}{2^2}-\frac{(y-0)^2}{3^2-2^2}=1,
$$

which we can rewrite to

$$
 \frac{(x-2)^2}{4}-\frac{y^2}{5}=1.
$$

:::{todo} 
Include a version of {numref}`Fig:CurvesR2:Hyperbola1` that does not show the parametrisation.
:::

::::::

::::::{prf:example} 
:label: Ex:Curves:Hyperbola2

Consider the graph of the function $f(x)=\dfrac{1}{x}$. We claim that this is a hyperbola with vertices $V_1:(-1,-1)$ and $V_2:(1,1)$ and focal points $F_1:(-\sqrt{2},-\sqrt{2})$ and $F_2:(\sqrt{2},\sqrt{2})$. This would mean that the major axis of the hyperbola is the line $y=x$.

Pick any point $P:(x,y)$ on the graph of $f$. We want to show that the absolute difference between the distances from $P$ to $F_1$ and to $F_2$ is constant. In that case, we have $y=f(x)=\frac{1}{x}$. The distance from $P$ to $F_1$ is 

$$
\begin{align*}
 \operatorname{dist}(P,F_1) &= \sqrt{\left(x-\left(-\sqrt{2}\right)\right)^2+\left(\frac{1}{x}-\left(-\sqrt{2}\right)\right)^2} \\
 &= \sqrt{x^2+2\sqrt{2}x+2+\frac{1}{x^2}+\frac{2\sqrt{2}}{x}+2} \\
 &= \sqrt{x^2+x^{-2}+2+2\sqrt{2}\left(x+x^{-1}\right)+2},
\end{align*}
$$

while the distance from $P$ to $F_2$ is

$$
\begin{align*}
 \operatorname{dist}(P,F_2) &= \sqrt{\left(x-\sqrt{2}\right)^2+\left(\frac{1}{x}-\sqrt{2}\right)^2} \\
 &= \sqrt{x^2-2\sqrt{2}x+2+\frac{1}{x^2}-\frac{2\sqrt{2}}{x}+2} \\
 &= \sqrt{x^2+x^{-2}+2-2\sqrt{2}\left(x+x^{-1}\right)+2}.
\end{align*}
$$

In order to simplify these distances, we note that

$$
\left(x+x^{-1}\right)^2=x^2+2xx^{-1}+x^{-2}=x^2+2+x^{-2}.
$$

As such, we can write

$$
\begin{align*}
 \sqrt{x^2+x^{-2}+2+2\sqrt{2}\left(x+x^{-1}\right)+2} &= \sqrt{(x+x^{-1})^2+2\sqrt{2}\left(x+x^{-1}\right)+(\sqrt{2})^2} \\
 &= \sqrt{\left(\left(x+x^{-1}\right)+\sqrt{2}\right)^2} \\
 &= \left|\left(x+x^{-1}\right)+\sqrt{2}\right|
\end{align*}
$$

and

$$
\begin{align*}
 \sqrt{x^2+x^{-2}+2-2\sqrt{2}\left(x+x^{-1}\right)+2} &= \sqrt{(x+x^{-1})^2-2\sqrt{2}\left(x+x^{-1}\right)+(-\sqrt{2})^2} \\
 &= \sqrt{\left(\left(x+x^{-1}\right)-\sqrt{2}\right)^2} \\
 &= \left|\left(x+x^{-1}\right)-\sqrt{2}\right|.
\end{align*}
$$

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

$$
\begin{align*}
 \left|\operatorname{dist}(P,F_1)-\operatorname{dist}(P,F_2)\right| &= \left|\left(x+x^{-1}\right)+\sqrt{2}\right|-\left|\left(x+x^{-1}\right)-\sqrt{2}\right| \\
 &= \left(\left(x+x^{-1}\right)+\sqrt{2}\right)-\left(\left(x+x^{-1}\right)-\sqrt{2}\right) \\
 &=2\sqrt{2}.
\end{align*}
$$

Using a similar argument, the absolute difference of the distances between $P$ and the focal points is $2\sqrt{2}$ as well if $x<0$.

We conclude that the graph of the function $f(x)=\frac{1}{x}$ is, indeed, a hyperbola with vertices $V_1:(-1,-1)$ and $V_2:(1,1)$ and focal points $F_1:(-\sqrt{2},-\sqrt{2})$ and $F_2:(\sqrt{2},\sqrt{2})$.

:::{applet}
:url: calculus/curves_in_R%5E2/a_simple_hyperbola
:name: Fig:Curves:Hyperbola1OverX
:class: dark-light

The graph of the function $f(x)=\frac{1}{x}$ is a hyperbola with vertices $V_1(-1,-1)$ and $V_2(1,1)$ and focal points $F_1(-\sqrt{2},-\sqrt{2})$ and $F_2(\sqrt{2},\sqrt{2})$.
:::

:::{todo}
Remove the animation for the parametrisation from {numref}`Fig:Curves:Hyperbola1OverX`.
:::

::::::

In {prf:ref}`Ex:Curves:Hyperbola2` we saw that it can be tricky to describe hyperbolas of which the major axis is not the $x$-axis or $y$-axis. Fortunately, with the aid of linear algebra this is a lot easier. More information on this can be found in the relevant section of the [Open Linear Algebra book](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter8/QuadraticForms.html#conic-sections).

As mentioned earlier, ellipses and hyperbolas are so-called **conic sections**. A conic section is defined as the curve that results from the intersection of a plane in $\mathbb{R}^3$ with a double cone in $\mathbb{R}^3$. {numref}`Fig:Curves:ConicSections` shows a cone, a plane and the intersection between the cone and the plane. You can change the tilt of the plane to see the intersection change shape from ellipse to hyperbola and vice versa.

:::{applet}
:url: calculus/curves_in_R%5E2/conic_sections
:name: Fig:Curves:ConicSections
:class: dark-light

A (double) cone, a plane and the intersection between the cone and the plane, which initially is an ellipse. \
The first slider influences the tilt of the plane. \
The second slider influences the height of the plane.
:::

(Subsec:CurvesParabola)=

## Parabolas

Parabolas are yet another type of _conic sections_. You can see this in {numref}`Fig:Curves:ConicSections` by setting, for example, the tilt of the plane to $2$ and the height of the plane to $5$.

The most common examples are the graphs of quadratic functions, i.e. functions of the form $f(x)=ax^2+bx+c$ with $a\neq 0$, $b$ and $c$ constants. However, these are not the only type of parabolas that can occur. For instance, one could take the graph of $f(x)=x^2$ and rotate it $\frac{\pi}{2}$ radians clockwise. The resulting curve is no longer the graph of a function, but it is still a parabola (with equation $x=y^2$). In this section, we will find a more general equation for a parabola.

:::{applet}
:url: calculus/curves_in_R%5E2/introduction_to_parabolas
:name: Fig:Curves:ParabolaRotate
:class: dark-light

The graph of the function $f(x)=x^2$ has been rotated to give a parabola that is not the graph of a function.
:::

::::::{prf:definition} 
:label: Def:Curves:Parabola

A **parabola** is a curve in $\mathbb{R}^2$ such that there are a point, called the **focal point** of the parabola, and a line that does not contain the focal point, called the **directrix** of the parabola, such that for all points on the curve, the distance to the focal point is equal to the distance to the directrix. 

The point on the parabola where the distance to the focal point (or, equivalently, to the directrix) is minimal is called the **vertex** of the parabola. The distance of the vertex to the focal point is called the **focal length** of the parabola.

The line containing the focal point and the vertex of the parabola is called the **axis** of the parabola.
::::::

:::{applet}
:url: calculus/curves_in_R%5E2/definition_of_a_parabola
:name: Fig:Curves:Parabola
:class: dark-light

A parabola with focal point $F$ such that for each point $P$ on the parabola the distance to $F$ is equal to the distance to the directrix (which is the distance between the point $P$ and the point $D$). The vertex $V$ and the axis of the parabola are also shown.
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
 \operatorname{dist}(P,F)=\sqrt{\left(x_0-p\right)^2+\left(y_0-q\right)^2}.
$$

In order to compute the distance from $P$ to the line, we use some ideas from {numref}`Sec:LinesAndPlanes`. Note that the directrix can be written in vector form as $\begin{pmatrix}a\\ b\end{pmatrix}\cdot\begin{pmatrix}x\\ y\end{pmatrix}=-c$. As such, the line $\begin{pmatrix}a\\ b\end{pmatrix}\cdot\begin{pmatrix}x\\ y\end{pmatrix}=0$ is parallel to the directrix and from this we can read off that the vector $\begin{pmatrix}a\\ b\end{pmatrix}$ is perpendicular to the directrix. Hence, the line $\mathcal{L}$ with parametric vector equation $\begin{pmatrix}x\\ y\end{pmatrix}=\begin{pmatrix}x_0\\ y_0\end{pmatrix}+t\begin{pmatrix} a\\ b\end{pmatrix}$ passes through $(x_0,y_0)$ and is perpendicular to the directrix. This means that the intersection point of this line $\mathcal{L}$ and the directrix will give the point on the directrix closest to $(x_0,y_0)$. Plugging in the parametric vector equation into the equation for the directrix gives

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

$$
\begin{align*}
 \operatorname{dist}(d,P) &= \sqrt{\left(x_0+\frac{-ax_0-by_0-c}{a^2+b^2}a-x_0\right)^2+\left(y_0+\frac{-ax_0-by_0-c}{a^2+b^2}b-y_0\right)^2} \\
 &~ \quad\cdot\sqrt{\left(-ax_0-by_0-c\right)\frac{a^2}{\left(a^2+b^2\right)^2}+\left(-ax_0-by_0-c\right)\frac{b^2}{\left(a^2+b^2\right)^2}} \\
 &= \sqrt{\left(-ax_0-by_0-c\right)^2\frac{a^2+b^2}{\left(a^2+b^2\right)^2}} \\
 &= \sqrt{\left(-ax_0-by_0-c\right)^2\frac{1}{a^2+b^2}} \\
 &= \frac{|-ax_0-by_0-c|}{\sqrt{a^2+b^2}}.
\end{align*}
$$

Since the parabola consists of those points for which $\operatorname{dist}(d,P)=\operatorname{dist}(P,F)$, or equivalently when $\left(\operatorname{dist}(d,P)\right)^2=\left(\operatorname{dist}(P,F)\right)^2$ we find that $(x_0,y_0)$ lies on the parabola precisely when

$$
 \left(x_0-p\right)^2+\left(y_0-q\right)^2=\left(\frac{|-ax_0-by_0-c|}{\sqrt{a^2+b^2}}\right)^2=\frac{\left(ax_0+by_0+c\right)^2}{a^2+b^2},
$$

as desired.

:::{applet}
:url: calculus/curves_in_R%5E2/proof_of_equation_of_parabola
:name: Fig:Curves:DistanceToLine
:class: dark-light
:nonumber:

Illustration of the situation described in this proof. The point $D$ is the point on the directrix that is closest to the point $P$ on the parabola.
:::

::::

::::::{prf:corollary} 
:label: Cor:Curves:Parabola

Consider the parabola with vertex $(v_1,v_2)$ and focus $(v_1,v_2+f)$, or equivalently directrix $y=v_2-f$ (i.e. a parabola of which the axis is parallel to the $y$-axis). Then the parabola is defined by the equation

$$
 y=\frac{1}{4f}\left(x-v_1\right)^2+v_2,
$$

which means that the parabola is the graph of the function $g(x)=\frac{1}{4f}\left(x-v_1\right)^2+v_2$.

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

Consider the graph of the function $g(x)=ax^2+bx+c$ with constants $a\neq 0$, $b$ and $c$. This graph is a parabola with axis $x=-\dfrac{b}{2a}$, vertex $\left(-\dfrac{b}{2a},\dfrac{4ac-b^2}{4a}\right)$, focus $\left(-\dfrac{b}{2a},\dfrac{4ac-b^2+1}{4a}\right)$ and directrix $y=\dfrac{4ac-b^2-1}{4a}$.

::::::

:::{admonition} Proof of {prf:ref}`Cor:Curves:Parabola2`
:class: tudproof, dropdown
By completing the square, we can write the equation $y=ax^2+bx+c$ as

$$
 y=a\left(x+\frac{b}{2a}\right)^2+\frac{4ac-b^2}{4a}.
$$

Comparing this to the equation in {prf:ref}`Cor:Curves:Parabola`, we note that it is of the same form. So the graph of $g$ is a parabola of which the axis is parallel to the $y$-axis. Consider the vertex $(v_1,v_2)$, focus $(v_1,v_2+f)$ and directrix $y=v_2-f$ of this parabola. According to the equation in {prf:ref}`Cor:Curves:Parabola`, we must have

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

:::{applet}
:url: calculus/curves_in_R%5E2/types_of_parabolas
:name: Fig:Curves:Parabola4Types
:class: dark-light

The four different types of parabolas defined in {prf:ref}`Def:Curves:ParabolaUpDownLeftRight`. Note that the names of the different types of parabolas precisely mean what we would expect them to mean.
:::



::::::{prf:example} 
:label: Ex:Curves:Parabola1

Consider the graph of the function $f(x)=-\frac{1}{4}x^2+\frac{1}{2}x+\frac{23}{4}$, see {numref}`Fig:Curves:Parabola1`.

According to {prf:ref}`Cor:Curves:Parabola2`, this graph is a parabola with axis $x=1$, vertex $\left(1,6\right)$, focus $\left(1,5\right)$ and directrix $y=7$. Notice that the focus lies below the vertex, while the directrix lies above the vertex, so the parabola opens downwards. We also note that the graph of the function intersects the $y$-axis, i.e. the line $x=0$, at the point $(0,f(0))=\left(0,\frac{23}{4}\right)$. Finally, upon solving the equation $-\frac{1}{4}x^2+\frac{1}{2}x+\frac{23}{4}=0$ we find that the graph intersects the $x$-axis, i.e. the line $y=0$, at the points $(1-2\sqrt{6},0)$ and $(1+2\sqrt{6},0)$. 

:::{applet}
:url: calculus/curves_in_R%5E2/a_parabola
:name: Fig:Curves:Parabola1
:class: dark-light

The graph of the function $f(x)=-\frac{1}{4}x^2+\frac{1}{2}x+\frac{23}{4}$ is a parabola with axis $x=1$, vertex $\left(1,6\right)$, focus $\left(1,5\right)$ and directrix $y=7$.
:::


::::::

::::::{prf:example} 
:label: Ex:Curves:Parabola2

Consider the parabola with focus $F:(1,4)$ and directrix $y=-x+1$. Since the directrix is not parallel to the $x$- or $y$-axis, we have to use {prf:ref}`Thm:Curves:Parabola` to find an equation for this parabola. Rewriting the directrix to $x+y-1=0$, we obtain the equation

$$
 \frac{\left(x+y-1\right)^2}{2}=(x-1)^2+(y-4)^2.
$$

Now suppose we want to find the axis and vertex of this parabola. As in the proof of {prf:ref}`Thm:Curves:Parabola`, we notice that the directrix is parallel to the line $x+y=0$, which can be written in vector form as $\begin{pmatrix}1\\ 1\end{pmatrix}\cdot\begin{pmatrix}x\\ y\end{pmatrix}=0$. This means that the vector $\begin{pmatrix}1\\ 1\end{pmatrix}$ is perpendicular to the directrix. We consider the line $\mathcal{L}$ written in parametric vector form $\begin{pmatrix}x\\ y\end{pmatrix}=\begin{pmatrix}1\\ 4\end{pmatrix}+t\begin{pmatrix}1\\ 1\end{pmatrix}$. By construction, this line passes through the focal point $(1,4)$ and has direction vector $\begin{pmatrix}1\\ 1\end{pmatrix}$. Since the line is perpendicular to the directrix, it intersects the directrix in the point closest to the focus point. Hence, it intersects the parabola at its vertex. As such, this line $\mathcal{L}$ is actually the axis of the parabola. We substitute $x=1+t$ and $y=4+t$ into the equation for the parabola to obtain

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

