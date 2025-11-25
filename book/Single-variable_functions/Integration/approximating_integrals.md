```{admonition} Attribution
:class: attribution
This page is based on {cite:t}`Vuik_2023`.
```

::::{admonition} Figures that should become applets
:class: remark

Each applet always should have interactivity features such as Zoom, Pan, and Fullscreen.

The following figures should become applets with these additional interactivity features:

```{list-table}
:header-rows: 1
:align: center
:class: mid-align

* - Figure
  - Interactivity
  - Implemented
* - {numref}`Fig:NumericalIntegration:riemann`
  - Dragging each point along the curve/axis (within their relevant intervals)

    Increasing/decreasing the number of points
  - 
* - {numref}`Fig:NumericalIntegration:leftRectangle`
  - Dragging $x_L$ along the curve/axis
    
    Dragging $x_R$ along the axis
  - Yes
* - {numref}`Fig:NumericalIntegration:Trapezoidal`
  - Dragging $x_L$ along the curve/axis
    
    Dragging $x_R$ along the curve/axis
  -
* - {numref}`Fig:NumericalIntegration:Simpsons`
  - Dragging $x_L$ along the curve/axis
    
    Dragging $x_M$ along the curve/axis

    Dragging $x_R$ along the curve/axis
  - 
* - {numref}`Fig:NumericalIntegration:composite`
  - Increasing/decreasing the number of points
  - 
* - {numref}`Fig:NumericalIntegration:errors`
  - Enabling/disabling each of the curves
  - 

```

::::

(Sec:ApproximatingIntegrals)=
# Approximating integrals

## Introduction

Determining the physical quantities of a system (for example volume, mass, or length) often involves the integral of a function. In many cases, an analytic evaluation of the integral is not possible. In such cases one has to resort to numerical quadratures.

As an example, we investigate the production of a spoiler that is mounted onto the cabin of a truck ({numref}`Figure %s <Fig:ApproximatingIntegrals:truck>`). The shape of the spoiler is described by a sine function with a $2\pi$ meter period. The aluminium spoiler is made out of a flat plate by extrusion. The manufacturer wants to know the width of the plate such that the horizontal dimension of the spoiler will be 80 cm. The answer to this question is provided by the arc length of the curve (after a conversion to meters)

$$
 \left\{ \begin{array}{cl}
x(t)\hspace{-0.3cm}&=t ,\\
y(t)\hspace{-0.3cm}&=\sin(t), \quad 0 \leq t \leq \frac14\pi.
         \end{array}
 \right.
$$

:::{figure} Images/Fig-NumericalIntegration-truck.svg
:name: Fig:ApproximatingIntegrals:truck
:figwidth: 90%

Truck with spoiler on the cabin. Originally from <a href="https://www.vecteezy.com/free-vector/truck" target="_blank">Truck Vectors by Vecteezy</a>.

:::

To determine the arc length the formula

$$
\ell = \int\limits_{0}^{\frac14\pi} \sqrt{1 + \left(\frac{dy}{dt}\right)^{2}} dt = \int\limits_{0}^{\frac14\pi}\sqrt{1 + \cos^2\left( t\right)} dt
$$

is used. However, this integral cannot be evaluated in a simple way using only elementary functions. In this chapter, numerical integration methods will be investigated in order to approximate integrals such as the one describing the arc length of the spoiler.

## Riemann sums and integrals

A Riemann sum and the corresponding set of intermediate points $T_n$ are shown in {numref}`Figure %s <Fig:ApproximatingIntegrals:riemann>`.

:::{figure} Images/Fig-NumericalIntegration-riemann.svg
:name: Fig:ApproximatingIntegrals:riemann
:figwidth: 90%
:class: dark-light

A Riemann sum and the corresponding set of intermediate points $T_n$.

:::

Riemann sums are usually used to study integrability theoretically, but they are not very useful in practice. _Numerical integration rules_ constitute different ways to approximate definite integrals. Usually, a numerical integration rule, denoted by $I$, has a similar structure to a Riemann sum:

$$
 I = \sum_{k=0}^n w_k f(t_k).
$$

Here, $t_k$ are called the _integration points_, and $w_k$ are the corresponding _weights_. Numerical integration rules are also called _quadrature rules_.

## Simple integration rules

In this section, we consider the integration of a function $f$ over a single interval $[x_L, x_R]$ and we will present several simple integration rules.

**Rectangle rule**

The most simple integration rule is called the _Rectangle rule_. Two different versions exist:

$$
  \int_{x_L}^{x_R} f(x) dx \approx (x_R - x_L) f(x_L), \text{ and } \int_{x_L}^{x_R} f(x) dx \approx (x_R - x_L) f(x_R),
$$
which use the left and the right end point of the interval, respectively.

The left Rectangle rule is depicted in {numref}`Figure %s <Fig:ApproximatingIntegrals:leftRectangle>`.

::::{applet}
:url: calculus/integration/left_rectangle
:name: Fig:ApproximatingIntegrals:leftRectangle
:class: dark-light

An illustration of the left Rectangle rule.
::::

**Trapezoidal rule**

In the _Trapezoidal rule_, the line piece between $x_L$ and $x_R$ is used to approximate the integral of $f \in C[x_L,x_R]$. This polynomial is given by

$$
L_1(x) = \frac{x_R - x}{x_R - x_L} f(x_L) + \frac{x - x_L}{x_R - x_L} f(x_R).
$$

The corresponding approximation of the integral is given by 

:::{math}
:label: Eq:ApproximatingIntegrals:single_trap

\int_{x_L}^{x_R} f(x) dx \approx \int^{x_R}_{x_L} L_1(x) dx = \frac{x_R - x_L}{2}(f(x_L) + f(x_R)).
:::

This approximation is called the _Trapezoidal rule_, since Equation {eq}`Eq:ApproximatingIntegrals:single_trap` equals the area of the trapezium with vertices $(x_L, 0), \; (x_R, 0),\; (x_R, f(x_R))$ and $(x_L, f(x_L))$. The Trapezoidal rule is depicted in {numref}`Figure %s <Fig:ApproximatingIntegrals:Trapezoidal>`.

:::{figure} Images/Fig-NumericalIntegration-Trapezoidal.svg
:name: Fig:ApproximatingIntegrals:Trapezoidal
:figwidth: 90%
:class: dark-light

An illustration of the Trapezoidal rule.

:::

:::{admonition} Two more rules (bonus material)
:class: bonus, dropdown

**Midpoint rule**

The Midpoint rule uses the integration point $x_M = \frac{x_L + x_R}{2}$, which leads to

$$
\int_{x_L}^{x_R} f(x) dx \approx (x_R - x_L)f (x_M).
$$

**Simpson's rule**

Using a quadratic interpolation polynomial with interpolation nodes $x_L$, $x_M = \frac{x_L + x_R}{2}$, and $x_R$, the Simpson's rule can be derived. The integral of $f$ is approximated by

$$
\int_{x_L}^{x_R} f(x) dx \approx \frac{x_R - x_L}{6} (f(x_{L}) + 4 f (x_{M}) + f(x_{R})).
$$

The Simpson's rule is depicted in {numref}`Figure %s <Fig:ApproximatingIntegrals:Simpsons>`.

::::{figure} Images/Fig-NumericalIntegration-Simpsons.svg
:name: Fig:ApproximatingIntegrals:Simpsons
:figwidth: 90%
:class: dark-light

An illustration of the Simpson's rule.

::::

:::

To summarize:

::::{prf:definition}
:label: Def:ApproximatingIntegrals:simple_rules

Assume $f$ is continuous on $[x_L,x_R]$.

We define the following **integration rules**:

```{list-table}
:header-rows: 0
:align: center
:class: mid-align

* - **left Rectangle rule**
  - $\displaystyle\int_{x_L}^{x_R}f(x)dx\approx (x_R-x_L)f(x_L)$
* - **right Rectangle rule**
  - $\displaystyle\int_{x_L}^{x_R}f(x)dx\approx (x_R-x_L)f(x_R)$
* - **Trapezoidal rule**
  - $\displaystyle\int_{x_L}^{x_R}f(x)dx\approx \frac12(x_R-x_L)\left(f(x_L)+f(x_R)\right)$
```

::::

Let us apply these rules methods to the example of the spoiler:

::::{prf:example}
:label: Ex:ApproximatingIntegrals:spoiler_simple

We will approximate the integral

$$
\int\limits_{0}^{\frac14\pi}\sqrt{1 + \cos^2\left( t\right)} dt.
$$

Each of the three rules use the function values in the left point $x_L=0$ and/or the right point $x_R=\frac14\pi$, so let us calculate these to start:

$$
\begin{align*}
\sqrt{1 + \cos^2\left( 0\right)} &=          1.414213\ldots \\
\sqrt{1 + \cos^2\left(\frac14\pi\right)} &= 1.224744\ldots
\end{align*}
$$

Now we can apply each of the three rules (scroll to the right to see the numerical values if they are not shown (completely)):

```{list-table}
:header-rows: 0
:align: center
:class: mid-align

* - left Rectangle rule
  - $\displaystyle\int\limits_{0}^{\frac14\pi}\sqrt{1 + \cos^2\left( t\right)} dt$
  - $\approx$
  - $\displaystyle\left(\frac14\pi-0\right)\cdot\sqrt{1 + \cos^2\left( 0\right)}$
  - $=$
  - $1.11072\ldots$
* - right Rectangle rule
  - $\displaystyle\int\limits_{0}^{\frac14\pi}\sqrt{1 + \cos^2\left( t\right)} dt$
  - $\approx$
  - $\displaystyle\left(\frac14\pi-0\right)\cdot\sqrt{1 + \cos^2\left( \frac14\pi\right)}$
  - $=$
  - $0.96191\ldots$
* - Trapezoidal rule
  - $\displaystyle\int\limits_{0}^{\frac14\pi}\sqrt{1 + \cos^2\left( t\right)} dt$
  - $\approx$
  - $\displaystyle\frac{\frac14\pi-0}{2}\cdot\left(\sqrt{1 + \cos^2\left( 0\right)}+\sqrt{1 + \cos^2\left( \frac14\pi\right)}\right)$
  - $=$
  - $1.03631\ldots$
```

If we would tell you that the exact value of the integral is

$$
\int\limits_{0}^{\frac14\pi}\sqrt{1 + \cos^2\left( t\right)} dt = 1.05809\ldots
$$

what rule performs best?

::::

## Composite rules

The integration rules that we presented in the previous section usually generate errors that are larger than the required accuracy allows, because at most two points are used. In this section, more accurate approximations will be obtained by applying a _composite integration rule_.

The integral of $f \in C[a,b]$ will be approximated using a subdivision $a = x_0 < x_1 < \ldots < x_n = b$, with $x_k = a + kh$, $k = 0,\ldots, n$, and $h = \frac{b-a}{n}$. This means that between each two consecutive points $x_k$ and $x_{k+1}$ a step of size $h$ is made, or in other words, the points are equidistant.

Using that

$$
 \int_a^b f(x) dx = \int_{x_0}^{x_1} f(x) dx + \int_{x_1}^{x_2} f(x) dx  + \cdots + \int_{x_{n-1}}^{x_n} f(x) dx,
$$

the integration rules of the previous section can be applied on each subinterval $[x_{k-1}, x_k]$.If $I_k$ is an approximation of the integral $\int_{x_{k-1}}^{x_k} f(x) dx$, for $k=1,\ldots,n$, with $x_L = x_{k-1}$ and $x_R = x_k$, then the integral over $[a,b]$ can be approximated by

$$
 \int_a^b f(x) dx = \sum_{k=1}^n \int_{x_{k-1}}^{x_k} f(x) dx \approx \sum_{k=1}^n I_k = I.
$$

This is called a _composite integration rule_ and the idea is illustrated in {numref}`Figure %s <Fig:ApproximatingIntegrals:composite>`.

:::{figure} Images/Fig-NumericalIntegration-composite.svg
:name: Fig:ApproximatingIntegrals:composite
:figwidth: 90%
:class: dark-light 

An illustration of the composite left Rectangle rule.

:::

To summarize:

::::{prf:definition}
:label: Def:ApproximatingIntegrals:composite_rules

Assume $f$ is continuous on $[a,b]$, $h=\dfrac{b-a}{n}$ and $x_k=a+kh$ for $k=0,1,\ldots,n$ are given nodes.

If $I_k$ is an integration rule that approximates $\int_{x_{k-1}}^{x_k}f(x)dx$, we can approximate $\int_{a}^{b}f(x)dx$ with the **composite integration rule**

$$
I = \sum_{k=1}^{n}I_k.
$$

::::

**Rectangle rule**

The left and right composite Rectangle rules are given by

$$
\begin{align*}
 I_{L} &=  \sum_{k=0}^{n-1}h f(x_k) = h\left(f(a) + f(a + h) + \ldots + f(b - h)\right), \\
 I_{R} &= \sum_{k=1}^nh f(x_k)= h\left(f(a+h) + f(a + 2h) + \ldots + f(b)\right).
\end{align*}
$$

**Trapezoidal rule**

For the Trapezoidal rule, the composite version is  

$$
 I_T = \frac{h}{2} \sum_{k=1}^n (f(x_{k-1}) + f(x_k)) = h \left( \frac{1}{2} f(a) + f(a+h) + \ldots + f(b-h) + \frac{1}{2} f(b) \right).
$$

:::{admonition} Two more composite rules (bonus material)
:class: bonus, dropdown

**Midpoint rule**

The composite Midpoint rule is given by

$$
I_{M} = h \sum_{k=1}^n f\left(\frac{x_{k-1} + x_k}{2} \right)= h \left( f(a + \frac{1}{2}h) + f(a + \frac{3}{2}h) + \ldots + f(b - \frac{1}{2}h) \right).
$$

**Simpson's rule**

The repeated Simpson's rule is given by

$$
\begin{align*}
  I_S &= \frac{h}{6} \sum_{k=1}^n \left( f(x_{k-1}) + 4 f\left( \frac{x_{k-1} + x_k}{2} \right)  + f(x_k) \right) \\
&= h\left( \frac{1}{6} f(a) + \frac{2}{3} f(a + \frac{1}{2} h) + \frac{1}{3} f(a + h) +  \frac{2}{3} f(a + \frac{3}{2} h) +  \ldots + \frac{1}{3}f(b-h)+\frac{2}{3} f(b - \frac{1}{2} h) + \frac{1}{6} f(b) \right).
\end{align*}
$$

:::

Let us apply one of these composite rules methods to the example of the spoiler:

::::{prf:example}
:label: Ex:ApproximatingIntegrals:spoiler_composite

We will approximate the integral

$$
\mathcal{I}=\int\limits_{0}^{\frac14\pi}\sqrt{1 + \cos^2\left( t\right)} dt,
$$

using the composite right Rectangle rule with $h=\frac18\pi$:

$$
\begin{align*}
\mathcal{I} &\approx I_R \\
&= \tfrac18\pi\left(\sqrt{1 + \cos^2\left(\tfrac18\pi\right)}+\sqrt{1 + \cos^2\left(\tfrac14\pi\right)}\right) \\
&= 1.01559\ldots
\end{align*}
$$

As this is still very far from the exact value (see {prf:ref}`Ex:ApproximatingIntegrals:spoiler_simple`), we also computed the approximation with some smaller values of $h$:

|$h$|$I_R$|$\left\vert\mathcal{I}-I_R\right\vert$
|-|-|-|
|$\tfrac14\pi$|$0.96191\ldots$|$0.0961831\ldots$|
|$\tfrac18\pi$|$1.01559\ldots$|$0.0424980\ldots$|
|$\tfrac1{16}\pi$|$1.03817\ldots$|$0.0199157\ldots$|
|$\tfrac1{32}\pi$|$1.04846\ldots$|$0.0096286\ldots$|
|$\tfrac1{64}\pi$|$1.05336\ldots$|$0.0047322\ldots$|
|$\tfrac1{128}\pi$|$1.05574\ldots$|$0.0023456\ldots$|

Do you notice anything that happens in the last column?

You can see that the error in the approximation _halves_ each time the value of $h$ _halves_. Something similar is true for each of our composite integration rules, which you can see in {numref}`Figure %s <Fig:ApproximatingIntegrals:errors>`.

:::{figure} Images/Fig-NumericalIntegration-errors.svg
:name: Fig:ApproximatingIntegrals:errors
:figwidth: 90%
:class: dark-light 

An illustration of the errors of three composite integration rules.

:::

::::

We can even formulate a theorem that states that the observation in {prf:ref}`Ex:ApproximatingIntegrals:spoiler_composite` is always true:

::::{prf:theorem} Order of a numerical integration rule
:label: Thm:ApproximatingIntegrals:thm

Assume $f$ is continuous on $[a,b]$, $h=\dfrac{b-a}{n}$, $x_k=a+kh$ for $k=0,1,\ldots,n$ are given nodes and that $\mathcal{I}=\int_{a}^{b}f(x)dx$ is approximated with a composite integration rule $I$.

Then there exist a number $C>0$ and an integer $p$ such that

$$
\left|\mathcal{I}-I\right| \approx C(b-a)h^p,
$$

where $p$ is independent of the function $f$ and is called the **order**.

::::

A proof of this theorem is too much for this book, but you can find it in {cite:t}`Vuik_2023`.

::::{caution}

{prf:ref}`Thm:ApproximatingIntegrals:thm` does not give a way to calculate the real error, only gives an indication how to the error is related to the step size $h$. 

::::

From {prf:ref}`Ex:ApproximatingIntegrals:spoiler_composite` we can deduce the next table:

|Composite rule|$p$|
|-|-|
|left Rectangle|$1$|
|right Rectangle|$1$|
|Trapezoidal|$2$|

## Grasple exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/96be8c57-0314-4896-a632-cc3390b5acb4?id=104235
:label: Grasple:ApproximatingIntegrals:sincosleftright
:dropdown:
:description: Approximate an integral using the left and right Rectangle rules.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/52181c0d-e14d-4823-9ae6-2f5504772632?id=78657
:label: Grasple:ApproximatingIntegrals:tabletrapezoidal
:dropdown:
:description: Approximate an integral using the Trapezoidal rule.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5874f680-fc98-4b44-87b6-07c31a1a3847?id=104245
:label: Grasple:ApproximatingIntegrals:leftequalsright
:dropdown:
:description: When do two rules give the same result?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5639f3eb-8d0c-4f2f-b16b-0a182ac3c723?id=78665
:label: Grasple:ApproximatingIntegrals:compositeleft
:dropdown:
:description: Approximate an integral with the composite left Rectangle rule.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6a7584af-09ac-4ccf-9ccc-c89033109f3f?id=78859
:label: Grasple:ApproximatingIntegrals:compositerighttrapezoidal
:dropdown:
:description: Approximate an integral with the composite right Rectangle rule and the Trapezoidal rule.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/72759075-97e9-44fd-8091-5ff1ee43bb6f?id=104303
:label: Grasple:ApproximatingIntegrals:determine_and_predict
:dropdown:
:description: Determine the used composite integration rule and predict the error.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/509288ed-9cd3-4a3b-890a-04baa57ca1ba?id=104264
:label: Grasple:ApproximatingIntegrals:order_and_predict
:dropdown:
:description: Determine the order of a composite integration rule and predict the error.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/958541cf-21e4-4d58-9a17-0dfebf5f357a?id=104296
:label: Grasple:ApproximatingIntegrals:number_of_intervals
:dropdown:
:description: Determine the number of intervals needed to obtain a required accuracy.

::::