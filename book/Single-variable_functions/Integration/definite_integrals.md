(Sec:Integration:DefiniteIntegrals)=

# Definite integrals

## Introduction

In {numref}`Chapter:FunctionsAndCurves` we have seen that a function $f$ assigns to each number $x$ in its domain a unique number $f(x)$ in its range. In {numref}`Chapter:Differentiation` we have learned about the derivatives of a function and how to calculate them. In this chapter we introduce the concept of **integration** which can be seen as the *inverse* operation of differentiation.

If we take a visual approach, a derivative of a function at a certain point on the graph of that function gives us the *slope* of the graph of a function at that point. Integration, on the other hand, can be used to calculate the *area* between the graph of a function and the horizontal axis.

We start with the definition of the **definite integral** of a function on an interval $[a,b]$.

## Definite integrals as areas

::::::{prf:definition}
:label: Def:Integration:DefiniteIntegral
For a *positive* and *continuous* function $f$ defined on an interval $[a,b]$ the **definite integral of a positive and continuous function**

$$
\int_a^bf(x)\,dx
$$

is the **area** between the graph of $f$ and the $x$-axis between $a$ and $b$:

```{figure} Images/integral1.png
---
width: 50%
name: Fig:Integration:DefiniteIntegral
align: center
---
The integral $\displaystyle\int_a^bf(x)\,dx$.
```

The numbers $a$ and $b$ are called the **limits of integration**, where $a$ is called the **lower limit** and $b$ the **upper limit**.

The function $f$ is called the **integrand** and $x$ is the **variable of integration**. 

::::::

In many cases we need to use special techniques to calculate the area under a curve, however for some simple positive and continuous functions we can calculate the area by using basic geometric shapes such as rectangles and triangles, as shown in the following example.

::::{prf:example}
:label: Ex:Integration:DefiniteSimple

We calculate the integral $\displaystyle\int_0^3(2x+1)\,dx$ by using {prf:ref}`Def:Integration:DefiniteIntegral`. First we sketch the graph of the function $f(x)=2x+1$ on the interval $[0,3]$.

```{figure} Images/Fig-DefiniteIntegrals-LinearFunction.png
---
width: 50%
name: Fig:DefiniteIntegrals:LinearFunction
align: center
---

The graph of the function $f(x)=2x+1$ on the interval $[0,3]$.
```

We can see that the area under the graph consists of a rectangle and a triangle. The area of the rectangle equals base times height: $3\cdot1=3$. The area of the triangle equals one half times base times height: $\frac{1}{2}\cdot3\cdot(7-1)=9$. Hence the total area equals $3+9=12$ and we conclude that

$$
\int_0^3(2x+1)\,dx=12.
$$

::::

Of course we do not only have positive and continuous functions, but also many more. First, we extend the concept of the definite integral to positive piecewise-continuous functions. Then we will see how to deal with negative functions and functions that take on both positive and negative values.

::::{prf:definition}
:label: Def:Integration:DefinitePositivePiecewise

For a *positive* and *piecewise continuous* function $f$ defined on an interval $[a,b]$ the **definite integral of a positive piecewise-continuous function**

$$
\int_a^bf(x)\,dx
$$

is the **area** between the graph of $f$ and the $x$-axis between $a$ and $b$.

::::

As you can see, the definition is the same as for positive continuous functions. The reason is that we can consider each piece of the positive piecewise-continuous function separately as a positive function on each corresponding subinterval and add the areas together.

:::{prf:theorem}
:label: Th:Integration:DefinitePositivePiecewise

For a *positive* and *piecewise continuous* function $f$ defined on an interval $[a,b]$ that is made up of $n$ continuous pieces on the subintervals $[x_0,x_1]$, $[x_1,x_2]$, $\ldots$, $[x_{n-1},x_n]$ with $a=x_0<x_1<\ldots<x_n=b$, the definite integral equals the sum of the integrals on each subinterval:

$$
\int_a^bf(x)\,dx=\sum_{k=1}^n\int_{x_{k-1}}^{x_k}f(x)\,dx.
$$

::::

The next example illustrates this theorem.

::::::{prf:Example}
:label: Ex:Integration:DefinitePiecewise
Consider the function $f:[0,3]\to\mathbb{R}$ given by $f(x)=\left\{\begin{array}{ll}x, & 0\leq x<1,\\2, & 1\leq x\leq 2,\\x-1, & 2<x\leq 3\end{array}\right.$.

The graph of this piecewise continuous function is shown below.

```{figure} Images/piecewise.png
---
width: 50%
name: Fig:Integration:DefinitePiecewise
align: center
---
The graph of a piecewise continuous function.
```

The definite integral of $f$ over the interval $[0,3]$ can be calculated as the sum of three areas:

$$
\int_0^3f(x)\,dx=\int_0^1x\,dx+\int_1^22\,dx+\int_2^3(x-1)\,dx=\frac{1}{2}+2+\frac{3}{2}=4.
$$

::::::

Now we know how to handle the definite integral of positive piecewise-continuous functions, we are going to extend {prf:ref}`Def:Integration:DefiniteIntegral` to negative piecewise-continuous functions and after that to piecewise-continuous functions that take on both positive and negative values.

::::::{prf:definition}
:label: Def:Integration:DefiniteNegative

For a *negative* and *piecewise continuous* function $f$ defined on an interval $[a,b]$ the **definite integral of a negative and piecewise-continuous function**

$$
\int_a^bf(x)\,dx
$$

is *minus* the **area** between the graph of $f$ and the $x$-axis between $a$ and $b$.
::::::

Note that this means that we assume that area is always a positive quantity. Hence, for negative piecewise-continuous functions the definite integral will be a negative number.

But what if the function takes on both positive and negative values? Well, in that case we split the interval into several subintervals such that on each subinterval the function is either positive or negative. Then we calculate the area on each subinterval and add them together, taking into account the sign of the function on each subinterval. Or in other words: If $f$ takes on both positive and negative values the integral equals the total area above the $x$-axis minus the total area below the $x$-axis, as illustrated in the following figure.

```{figure} Images/integral3.png
---
width: 50%
name: Fig:Integration:DefiniteBoth
align: center
---

The integral $\displaystyle\int_a^bf(x)\,dx$ for a function that takes on both positive and negative values.
```

Although the above image contains a continuous function, the same idea applies to piecewise-continuous functions. This leads us to the following final definition of a definite integral.

::::::{prf:definition}
:label: Def:Integration:DefiniteGeneral
For a *piecewise continuous* function $f$ defined on an interval $[a,b]$ the **definite integral of a piecewise-continuous function**

$$
\int_a^bf(x)\,dx
$$

is the **area** between the graph of $f$ and the $x$-axis between $a$ and $b$, taking into account the sign of the function on each subinterval:

- If the function is completely positive on a subinterval, the area on that subinterval is added.
- If the function is completely negative on a subinterval, the area on that subinterval is subtracted.
- If the function takes on both positive and negative values on a subinterval, the area above the $x$-axis is added and the area below the $x$-axis is subtracted.

::::::

We end this subsection with an example.

::::::{prf:example}
:label: Ex:Integration:DefiniteBoth

Consider the function $f:[-2,5]\to\mathbb{R}$ given by $f(x)=\left\{\begin{array}{ll}1, &-2\leq x<0\\2x-4, & 0\leq x<2,\\-x+4, & 2\leq x\leq 5\end{array}\right.$, of which you can find the graph below.

```{figure} Images/Fig-Integration-DefiniteBoth.png
---
width: 50%
name: Fig:Integration:DefiniteBoth
align: center
---

The graph of a piecewise continuous function that takes on both positive and negative values.
```

The integral $\displaystyle\int_{-2}^5f(x)\,dx$ can be calculated as follows:

\begin{align*}
\int_{-2}^{5}f(x)\,dx &= \int_{-2}^{0}1\,dx+\int_{0}^{2}2x-4\,dx+\int_{2}^{5}(-x+4)\,dx\\
&= \int_{-2}^{0}1\,dx+\int_{0}^{2}2x-4\,dx+\int_{2}^{5}(-x+4)\,dx+\int_{4}^{5}(-x+4)\,dx \\
&= 2 \cdot 1-\frac12\cdot2\cdot4+\frac12\cdot2\cdot2-\frac12\cdot1\cdot1 \\
&= 2 - 4 + 2 - \frac12 \\
&= \frac12.
\end{align*}

In the second step we have split the last integral into two parts: one part from $2$ to $4$ where the function is positive and one part from $4$ to $5$ where the function is negative. After that we used the formulas for the areas of rectangles and triangles to calculate the areas and introduced the appropriate signs.

::::::

Now we have {prf:ref}`Def:Integration:DefiniteGeneral`, we can start looking at how to calculate definite integrals for functions that are not so easy to handle geometrically. For this we introduce the concept of Riemann sums.

## Riemann sums

Consider the function shown in the figure below with the indicated area between the graph of the function and the $x$-axis that we want to calculate.

```{figure} Images/Fig-DefiniteIntegrals-General.png
---
width: 50%
name: Fig:DefiniteIntegrals:General
align: center
---

A general function with area to be calculated.
```

Even though the function is continuous on the interval $[a,b]$, it is not composed of a simple geometric shape such as a rectangle or a triangle. Hence we cannot calculate the area directly. In order to find this area, we start with an approximation: we divide the interval $[a,b]$ into subintervals and consider the sum of the areas of the indicated rectangles:

```{figure} Images/integral2.png
---
width: 50%
name: Fig:Integration:SumRectangles
align: center
---

Sum of area of rectangles.
```

The height of each rectangle is taken to be the value of the function $f$ at an arbitrary point $x_k^*$ in the corresponding subinterval. This point $x_k^*$ is called a **sample point** and might be the left point, the right point or the middle point of the subinterval, for instance. Then we take the sum of the areas of all rectangles.

In fact, let us divide the interval $[a,b]$ into $n$ subintervals of equal width $(b-a)/n$:

$$
a=x_0 < x_1 < x_2 < \ldots < x_{n-1} < x_n=b.
$$

```{figure} Images/riemann.png
---
width: 50%
name: Fig:Integration:RiemannSum
align: center
---
Building a Riemann sum.
```

Choose a sample point $x_k^*$ in each subinterval $[x_{k-1},x_k]$, then the area equals

$$
\sum_{k=1}^nf(x_k^*)\Delta x\quad\text{with}\quad\Delta x=x_k-x_{k-1}=\frac{b-a}{n}.
$$

The sum $\displaystyle\sum_{k=1}^nf(x_k^*)(x_k-x_{k-1})$ is called a **Riemann sum**, named after the German mathematician [Georg Friedrich Bernhard Riemann (1826-1866)](https://en.wikipedia.org/wiki/Bernhard_Riemann):

:::::{prf:definition}
:label: Def:Integration:RiemannSum

The **Riemann sum** of a function $f$ on the interval $[a,b]$ for a given partition $P=\{x_0,x_1,\ldots,x_n\}$ with **sample points** $x_k^*$ in each subinterval $[x_{k-1},x_k]$ is defined as

$$
\sum_{k=1}^nf(x_k^*)(x_k-x_{k-1}).
$$

:::::

If we let the number of subintervals $n$ go to infinity, the width of each subinterval $\Delta x$ goes to zero and the Riemann sum approaches the exact area between the graph of the function and the $x$-axis. This leads us to the following theorem for the definite integral in terms of Riemann sums.

::::::{prf:theorem}
:label: Thm:Integration:DefiniteRiemann

The **definite integral of a piecewise continuous function** $f$ on the interval $[a,b]$ is equal to the limit of the Riemann sums as the number of subintervals $n$ approaches infinity

$$
\int_a^bf(x)\,dx=\lim_{n\to\infty}\sum_{k=1}^nf(x_k^*)\Delta x\quad\text{with}\quad\Delta x=\frac{b-a}{n}\quad\text{and}\quad x_k=a+k\Delta x,
$$

provided that this limit exists and is the same for *every* choice of sample points $x_k^*$ in each subinterval $[x_{k-1},x_k]$.
::::::

::::{prf:remark}
:label: Remark:Integration:RiemannSum

We have chosen to divide the interval $[a,b]$ into $n$ subintervals of *equal width* $\Delta x=(b-a)/n$, which is not really necessary but makes the theorem a bit more manageable.
::::

The integral sign $\displaystyle\int$ was introduced by the German mathematician [Gottfried Wilhelm Leibniz (1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) and has the form of an elongated (stretched) $S$ which indicates the *limit* of (Riemann) sums.

Because the limit of the Riemann sums might not always exist, we introduce the term **integrable** to indicate that the integral exists:

::::{prf:definition}
:label: Def:Integration:Integrable

A function for which the limit of the Riemann sums exists is called **integrable**.
::::

Luckily, but without giving a formal proof here, we have the following important result:

::::{prf:theorem}
:label: Th:Integration:IntegrablePiecewise

Every *piecewise continuous* function on an interval $[a,b]$ is integrable.
::::

Before we continue to properties of definite integrals, we show one example of calculating a definite integral using Riemann sums.

::::::{prf:example}
:label: Ex:Integration:RiemannSum

Consider the function $f$ on the interval $[0,1]$ given by $f(x)=x^2$. We want to calculate the integral $\displaystyle\int_0^1x^2\,dx$ using Riemann sums.

We divide the interval $[0,1]$ into $n>0$ subintervals of equal width $\Delta x=\frac{1-0}{n}=\frac{1}{n}$. The endpoints of the subintervals are given by $x_k=0+k\cdot\frac{1}{n}=\frac{k}{n}$ for $k=0,1,2,\ldots,n$.

As sample points we choose the right endpoints of each subinterval, $x_k^*=\frac{k}{n}$ for $k=1,2,\ldots,n$, which gives the function values $f(x_k^*)=\left(\frac{k}{n}\right)^2=\frac{k^2}{n^2}$.

Then the Riemann sum $R$ equals,

\begin{align*}
R &= \sum_{k=1}^nf(x_k^*)\Delta x \\
&= \sum_{k=1}^n\frac{k^2}{n^2}\cdot\frac{1}{n}=\frac{1}{n^3}\sum_{k=1}^nk^2 \\
&= \frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6} \\
&= \frac{2n^3+3n^2+n}{6n^3} \\
&= \frac{2n^2+3n+1}{6n^2}.
\end{align*}

Using techniques from {numref}`Section:Limitinf` we find that

$$
\lim_{n\rightarrow\infty}R=\lim_{n\rightarrow\infty}\frac{2n^2+3n+1}{6n^2}=\frac{2}{6}=\frac{1}{3}.
$$

Because the limit of the Riemann sums exists, we conclude that our function $f$ is integrable on the interval $[0,1]$ and that

$$
\int_0^1x^2\,dx=\frac{1}{3}.
$$

::::::

Calculating definite integrals using Riemann sums can be quite laborious. In the next sections we will see other techniques to calculate definite integrals more easily. But first we state some important properties of definite integrals.

## Properties of definite integrals

Using {prf:ref}`Def:Integration:DefiniteGeneral` we can derive several useful properties of definite integrals.

::::{prf:theorem}
:label: Th:Integration:DefinitePropertiesArea

- $\displaystyle\int_a^af(x)\,dx=0$ with $a$ any real number and $f$ defined at $a$;

- $\displaystyle\int_a^bc\,dx=c(b-a)$ with $a$, $b$ and $c$ any real numbers;

- $\displaystyle\int_a^bf(x)\,dx=\int_a^rf(x)\,dx+\int_r^bf(x)\,dx$ for any $r$ in $[a,b]$ and $f$ piecewise continuous on $[a,b]$.

- $\displaystyle\int_{-a}^af(x)\,dx=0$ with $a$ any real number and $f$ *odd* and piecewise continuous on $[-a,a]$.

- $\displaystyle\int_{-a}^af(x)\,dx=2\int_0^af(x)\,dx$ with $a$ any real number and $f$ *even* and piecewise continuous on $[-a,a]$.

::::

The above theorem can be shown by considering the areas involved according to {prf:ref}`Def:Integration:DefiniteGeneral`. We will not give the full proofs here, but illustrate the last two properties with examples.

::::::{prf:Example}
:label: Ex:Integration:DefiniteOdd

The sine function $\sin(x)$ is an odd function on the interval $\left[-\frac{1}{2}\pi,\frac{1}{2}\pi\right]$, as shown below.

```{figure} Images/sine_odd.png
---
width: 50%
name: Fig:Integration:DefiniteOdd
align: center
---
The graph of the sine function.
```

Inspection of the graph shows that the area below the $x$-axis and to the left of the $y$-axis equals the area above the $x$-axis and right of the $y$-axis. But because the area below the $x$-axis is taken with a negative sign in {prf:ref}`Def:Integration:DefiniteGeneral`, these two areas cancel each other out, and we find

$$
\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\sin(x)\,dx=0.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:DefiniteEven

The absolute value function $|x|$ is an even function on the interval $\left[-1,1\right]$, as shown below.

```{figure} Images/absolute.png
---
width: 50%
name: Fig:Integration:DefiniteEven
align: center
---
The integral of an even function
```

Inspection of the graph shows that the area above the $x$-axis and to the left of the $y$-axis equals the area above the $x$-axis and right of the $y$-axis. Because both areas are taken with a positive sign in {prf:ref}`Def:Integration:DefiniteGeneral`, we find

$$
\int_{-1}^1|x|\,dx=2\int_0^1|x|\,dx=2\cdot\frac{1}{2}=1.
$$

::::::

The next theorem states that the choice of the variable of integration does not matter.

::::{prf:theorem}
:label: Th:Integration:VariableOfIntegration

For a integrable function $f$ on the interval $[a,b]$, the choice of the variable of integration does not change the value of the integral:

$$
\int_a^bf(x)\,dx=\int_a^bf(t)\,dt=\int_a^bf(u)\,du=\int_a^bf(\square)\,d\square=\int_a^bf(\triangle)\,d\triangle.
$$

::::

A rigorous proof of this theorem can be given using Riemann sums, but we will not give it here. You can however convince yourself that this is true by considering the definition of the definite integral in {prf:ref}`Def:Integration:DefiniteGeneral`. If you would draw the graph of the function $f$ and shade the area between the graph and the $x$-axis between $a$ and $b$, you would see that the area does not depend on the name of the variable of integration.

Finally, we state some more properties of definite integrals. Proving these properties requires something called the *Fundamental theorem of calculus*, which we will introduce in {numref}`Sec:Integration:FundamentalTheorem`. For now, we just state the properties.

::::{prf:theorem}
:label: Th:Integration:DefinitePropertiesFundamental

- $\displaystyle\int_b^af(x)\,dx=-\int_a^bf(x)\,dx$ for any real numbers $a$ and $b$ and $f$ piecewise continuous on $[a,b]$.

- $\displaystyle\int_a^b\left(f(x)+g(x)\right)\,dx=\int_a^bf(x)\,dx+\int_a^bg(x)\,dx$ for any real numbers $a$ and $b$ and $f$ and $g$ piecewise continuous on $[a,b]$.

- $\displaystyle\int_a^b cf(x)\,dx=c\int_a^bf(x)\,dx$ for any real numbers $a$, $b$ and $c$ and $f$ piecewise continuous on $[a,b]$.

::::

Finally, we state some important comparison properties of definite integrals. These can be used to estimate the value of definite integrals, as we will do in {prf:ref}`Ex:Integration:DefiniteApproximation`.

::::{prf:theorem}
:label: Th:Integration:DefiniteComparison

- If $f(x)\geq0$ for $a\leq x\leq b$ and $f$ is piecewise continuous on $[a,b]$, then $\displaystyle\int_a^bf(x)\,dx\geq0$.

- If $f(x)\geq g(x)$ for $a\leq x\leq b$ and $f$ and $g$ are piecewise continuous on $[a,b]$, then $\displaystyle\int_a^bf(x)\,dx\geq\int_a^bg(x)\,dx$.

- If $m\leq f(x)\leq M$ for $a\leq x\leq b$ and $f$ is piecewise continuous on $[a,b]$, then $m(b-a)\leq\displaystyle\int_a^bf(x)\,dx\leq M(b-a)$.
::::


::::::{prf:Example}
:label: Ex:Integration:DefiniteApproximation

In order to find estimate the value of $\displaystyle\int_0^1e^{-x^2}\,dx$, we note that the integrand $f(x)=e^{-x^2}$ is a decreasing function on $[0,1]$. Its absolute maximum value is $M=f(0)=1$ and its absolute minimum value is $m=f(1)=e^{-1}$. Hence we have

$$
e^{-1}=e^{-1}(1-0)\leq\int_0^1e^{-x^2}\,dx\leq1(1-0)=1.
$$

Since $e^{-1}\approx0.3679$ we conclude that $0.367\leq\displaystyle\int_0^1e^{-x^2}\,dx\leq1$.
::::::

## Interpretation of definite integrals

Although {prf:ref}`Def:Integration:DefiniteGeneral` defines the definite integral as an area, this area is only an area in the most general sense of the word. In fact, definite integrals can be used in many different contexts and the units of the definite integral depend on the context as well.

If, for example, the function $f$ represents the height of a fence in meters above the ground along a straight path of length $b-a$ meters, then the definite integral $\displaystyle\int_a^bf(x)\,dx$ truly represents the *area* of the fence in square meters.

If, however, the function $f$ represents the *speed* at which an object is moving in meters per second over a time interval $[a,b]$ in seconds then the definite integral $\displaystyle\int_a^bf(t)\,dt$ represents the *distance* traveled by the object in that same time interval, measured in meters. The next examples illustrates this interpretation.

::::::{prf:example}

:::{figure} Images/filip-mroz-XCkRGOX2VgM-unsplash.jpg
:width: 75%
:name: Fig:DefiniteIntegrals:Athlete
:align: center
:figclass: margin
:author: <a href="https://unsplash.com/@mroz?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Filip Mroz</a>
:placement: caption
:license: Unsplash License
:source: [Unsplash](https://unsplash.com/photos/woman-running-wearing-armband-XCkRGOX2VgM?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText")
:date: 2016-11-16

An athlete during an interval training.

:::

Consider an athlete during an interval training. She starts walking at a speed of $5$ km/h during $5$ minutes. Then she runs at a speed of $15$ km/h during $2$ minutes, followed by a period of $4$ minutes walking at a speed of $6$ km/h. Then she runs at a speed of $20$ km/h during $3$ minutes, followed by $6$ minutes walking at a speed of $4$ km/h.

What is the distance traveled by the athlete?

:::{figure} Images/distance.png
:width: 75%
:name: Fig:DefiniteIntegrals:Distance
:align: center

The speed $v$ at which the athlete is moving during the interval training. On the horizontal axis the time $t$ is shown in minutes.
:::

In order to get the correct units, we change the minutes into hours ($5$ minutes is $\frac{1}{12}$ hour for instance) and add the five different areas:

$$
\int_{0}^{\frac1{3}}v(t)\,dt = \tfrac{1}{12}\cdot5+\tfrac{1}{30}\cdot15+\tfrac{1}{15}\cdot5+\tfrac{1}{20}\cdot20+\tfrac{1}{15}\cdot6=\tfrac{25+30+20+60+24}{60}=\tfrac{159}{60}.
$$

This means that the athlete has traveled a distance of $\frac{159}{60}$ km $\approx2.65$ km during her interval training.

We could also have changed the speed into meters per second and the time into seconds. Then the definite integral would have given the same distance, but now measured in meters.

::::::

Note that speed in general cannot change suddenly. In fact, velocity should be a continuous function. Then the distance equals the area between the graph of the velocity and the horizontal axis. Before you learn how to calculate this area exactly, we need to discuss another type of integral in {numref}`Sec:Integration:IndefiniteIntegrals`.

To conclude this section, we give a general theorem about the unit of definite integral.

::::{prf:theorem}
:label: theorem:Integration:Units
If $f$ is a piecewise-continuous function defined on an interval $[a,b]$ and if the units of $f(x)$ are $U_f$ and the units of $x$ are $U_x$, then the units of the definite integral $\displaystyle\int_a^bf(x)\,dx$ are given by the product $U_f\cdot U_x$.

::::

## Grasple exercises

75563, 75363, 75209, 75366, 63602, 63606, 63599