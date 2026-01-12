(Sec:Integration:DefiniteIntegrals)=

# Definite integrals

## Introduction

In {numref}`Chapter:FunctionsAndCurves` we have seen that a function $f$ assigns to each number $x$ in its domain a unique number $f(x)$ in its range. In {numref}`Chapter:Differentiation` we have learned about the derivatives of a function and how to calculate them. In this chapter we introduce the concept of **integration** which can be seen as the *inverse* operation of differentiation.

If we take a visual approach, a derivative of a function at a certain point on the graph of that function gives us the *slope* of the graph of a function at that point. Integration, on the other hand, can be used to calculate the *area* between the graph of a function and the horizontal axis.

We start with the definition of the **definite integral** of a function on an interval $[a,b]$.

## Definite integrals as areas

::::::{prf:definition}
:label: Def:Integration:DefiniteIntegral
For a *positive* and *continuous* function $f$ defined on an interval $[a,b]$ the **definite integral of a positive and continuous**

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

<!-- STOP EDIT -->

## Riemann sums

In order to find this area, we start with an approximation: we divide the interval $[a,b]$ into subintervals and consider the sum of the areas of the indicated rectangles:

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
\int_a^bf(x)\,dx=\lim_{n\to\infty}\,\sum_{k=1}^nf(x_k^*)\Delta x\quad\text{with}\quad\Delta x=x_k-x_{k-1}=\frac{b-a}{n}.
$$

The sum $\displaystyle\sum_{k=1}^nf(x_k^*)(x_k-x_{k-1})$ is called a **Riemann sum**, named after the German mathematician [Georg Friedrich Bernhard Riemann (1826-1866)](https://en.wikipedia.org/wiki/Bernhard_Riemann):

:::::{prf:definition}
:label: Def:Integration:RiemannSum

The **Riemann sum** of a function $f$ on the interval $[a,b]$ for a given partition $P=\{x_0,x_1,\ldots,x_n\}$ with sample points $x_k^*$ in each subinterval $[x_{k-1},x_k]$ is defined as

$$
\sum_{k=1}^nf(x_k^*)(x_k-x_{k-1})
$$

:::::

**Remarks**

- The integral sign $\displaystyle\int$ was introduced by the German mathematician [Gottfried Wilhelm Leibniz (1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) and has the form of an elongated (stretched) $S$ which indicates the *limit* of (Riemann) sums.

Another choice of this variable does not change the integral:

$$
\int_a^bf(x)\,dx=\int_a^bf(t)\,dt=\int_a^bf(u)\,du=\int_a^bf(\square)\,d\square=\int_a^bf(\triangle)\,d\triangle.
$$

- The definition of the integral of a positive function holds when the function is *continuous* on the interval $[a,b]$, but can easily be extended to *piecewise continuous* functions.

::::::{prf:Example}
:label: Ex:Integration:DefinitePiecewise
Consider the function $f:[0,3]\to\mathbb{R}$ given by $f(x)=\left\{\begin{array}{ll}x, & 0\leq x<1\\2, & 1\leq x\leq 2\\x-1, & 2<x\leq 3.\end{array}\right.$
```{figure} Images/piecewise.png
---
width: 50%
name: a piecewise continuous function
align: center
---
The integral of a piecewise continuous function
```

$$
\int_0^3f(x)\,dx=\int_0^1x\,dx+\int_1^22\,dx+\int_2^3(x-1)\,dx=\frac{1}{2}+2+\frac{3}{2}=4.
$$

::::::

- We have chosen to divide the interval $[a,b]$ into $n$ subintervals of *equal width* $\Delta x=(b-a)/n$ which is not really necessary.

- For *negative* functions the integral is defined as *minus* the area between the graph of $f$ and the $x$-axis. If $f$ takes on both positive and negative values the integral equals the total area above the $x$-axis minus the total area below the $x$-axis.

```{figure} Images/integral3.png
---
width: 50%
name: integral
align: center
---
Signed areas
```

- A function for which the limit of the Riemann sums exists is called **integrable**; every *piecewise continuous* function on an interval $[a,b]$ is integrable (its integral exists).

**Properties**

- $\displaystyle\int_a^af(x)\,dx=0$;

- $\displaystyle\int_b^af(x)\,dx=-\int_a^bf(x)\,dx$;

- $\displaystyle\int_a^bc\,dx=c(b-a)$ with $c$ a constant;

- $\displaystyle\int_a^b\left(f(x)+g(x)\right)\,dx=\int_a^bf(x)\,dx+\int_a^bg(x)\,dx$;

- $\displaystyle\int_a^b cf(x)\,dx=c\int_a^bf(x)\,dx$ with $c$ a constant;

- If $r$ is some point in $(a,b)$, then: $\displaystyle\int_a^bf(x)\,dx=\int_a^rf(x)\,dx+\int_r^bf(x)\,dx$;

- If $f$ is an *odd* function defined on $[-a,a]$, then: $\displaystyle\int_{-a}^af(x)\,dx=0$;

- If $f$ is an *even* function defined on $[-a,a]$, then: $\displaystyle\int_{-a}^af(x)\,dx=2\int_0^af(x)\,dx$.

::::::{prf:Example}
:label: Ex:Integration:DefiniteOdd
```{figure} Images/sine_odd.png
---
width: 50%
name: odd function
align: center
---
The integral of an odd function
```

$$
\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\sin(x)\,dx=0.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:DefiniteEven
```{figure} Images/absolute.png
---
width: 50%
name: even function
align: center
---
The integral of an even function
```

$$
\int_{-1}^1|x|\,dx=2\int_0^1|x|\,dx=2\cdot\frac{1}{2}=1.
$$

::::::

**Comparison properties**

- If $f(x)\geq0$ for $a\leq x\leq b$, then $\displaystyle\int_a^bf(x)\,dx\geq0$.

- If $f(x)\geq g(x)$ for $a\leq x\leq b$, then $\displaystyle\int_a^bf(x)\geq\int_a^bg(x)\,dx$.

- If $m\leq f(x)\leq M$ for $a\leq x\leq b$, then $m(b-a)\leq\displaystyle\int_a^bf(x)\,dx\leq M(b-a)$.

::::::{prf:Example}
:label: Ex:Integration:DefiniteApproximation
In order to find an estimation of $\displaystyle\int_0^1e^{-x^2}\,dx$, we note that the integrand $f(x)=e^{-x^2}$ is a decreasing function on $[0,1]$. Its absolute maximum value is $M=f(0)=1$ and its absolute minimum value is $m=f(1)=e^{-1}$. Hence we have

$$
e^{-1}=e^{-1}(1-0)\leq\int_0^1e^{-x^2}\,dx\leq1(1-0)=1.
$$

Since $e^{-1}\approx0.3679$ we conclude that $0.3679\leq\displaystyle\int_0^1e^{-x^2}\,dx\leq1$.
::::::

## Distances

Instead of calculating areas, integration can also be used to find *distances*. Let's consider the **distance** problem: find the distance traveled by an object during a certain time period when the velocity of the object is known at all times.

If the velocity remains constant, then the distance problem is easy to solve: the distance is the product of the velocity and the time.

What if the velocity varies?

::::::{prf:example}

:::{figure} Images/filip-mroz-XCkRGOX2VgM-unsplash.jpg
:width: 75%
:name: Fig:DefiniteIntegrals:Athlete
:align: center
:figclass: margin

An athlete during an interval training. Photo by <a href="https://unsplash.com/@mroz?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Filip Mroz</a> on <a href="https://unsplash.com/photos/woman-running-wearing-armband-XCkRGOX2VgM?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
      
:::

Consider an athlete during an interval training. She starts walking at a speed of $5\;\text{km/h}$ during $5$ minutes. Then she runs at a speed of $15\;\text{km/h}$ during $2$ minutes, followed by a period of $4$ minutes walking at a speed of $6\;\text{km/h}$. Then she runs at a speed of $20\;\text{km/h}$ during $3$ minutes, followed by $6$ minutes walking at a speed of $4\;\text{km/h}$.

What is the distance traveled by the athlete?

:::{figure} Images/distance.png
:width: 75%
:name: distance problem
:align: center

The distance traveled by the athlete
:::

In order to get the correct units, we change the minutes into hours ($5$ minuties is $\frac{1}{12}$ hour for instance) and add five different areas:

$$
\tfrac{1}{12}\cdot5+\tfrac{1}{30}\cdot15+\tfrac{1}{15}\cdot5+\tfrac{1}{20}\cdot20+\tfrac{1}{15}\cdot6=\tfrac{25+30+20+60+24}{60}=\tfrac{159}{60}.
$$

::::::

Note that the speed cannot change suddenly. In fact, the velocity is a continuous function. Then the distance equals the area between the graph of the velocity and the horizontal axis.

## Grasple exercises

75563, 75363, 75209, 75366, 63602, 63606, 63599