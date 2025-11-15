# Definite integrals

In this section we cover

- Riemann sums
- Definite integrals
- Basic rules of calculation (e.g. sums and scalars)
- Comparison rules (for definite integrals)
- Integrals of piecewise-defined continuous functions

**Areas**

::::::{prf:Definition}
:label: Def:Integration:DefiniteIntegral
For a *positive* and *continuous* function $f$ defined on an interval $[a,b]$ the **definite integral**

$$
\int_a^bf(x)\,dx
$$

is the **area** between the graph of $f$ and the $x$-axis between $a$ and $b$:

```{figure} Images/integral1.png
---
width: 50%
name: integral
align: center
---
The integral $\displaystyle\int_a^bf(x)\,dx$
```
::::::

In order to find this area, we start with an approximation: divide the interval $[a,b]$ into subintervals and consider the sum of the areas of the indicated rectangles:

```{figure} Images/integral2.png
---
width: 50%
name: integral
align: center
---
Sum of area of rectangles
```

The height of each rectangle is taken to be the value of the function $f$ at an arbitrary point $x_i^*$ in the corresponding subinterval. This point $x_i^*$ is called a **sample point** and might be the left point, the right point or the middle point of the subinterval, for instance. Then we take the sum of the areas of all rectangles.

In fact, let us divide the interval $[a,b]$ into $n$ subintervals of equal width $(b-a)/n$:

$$
a=x_0 < x_1 < x_2 < \ldots < x_{n-1} < x_n=b.
$$

```{figure} Images/riemann.png
---
width: 50%
name: integral
align: center
---
Building a Riemann sum
```

Choose a sample point $x_i^*$ in each subinterval $[x_{i-1},x_i]$, then the area equals

$$
\int_a^bf(x)\,dx:=\lim_{n\to\infty}\,\sum_{i=1}^nf(x_i^*)\Delta x\quad\text{with}\quad\Delta x=x_i-x_{i-1}=\frac{b-a}{n}.
$$

The sum $\displaystyle\sum_{i=1}^nf(x_i^*)(x_i-x_{i-1})$ is called a **Riemann sum**, named after the German mathematician [Georg Friedrich Bernhard Riemann (1826-1866)](https://en.wikipedia.org/wiki/Bernhard_Riemann).

**Remarks**

- The integral sign $\displaystyle\int$ was introduced by the German mathematician [Gottfried Wilhelm Leibniz (1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) and has the form of an elongated (stretched) $S$ which indicates the *limit* of (Riemann) sums.

- $a$ and $b$ are called the **limits of integration**; $a$ is called the **lower limit** and $b$ the **upper limit**.

- The function $f$ is called the **integrand** and $x$ is the **variable of integration**. Another choice of this variable does not change the integral:

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

- $\displaystyle\int_b^af(x)\,dx=-\int_a^bf(x)\,dx$;

- $\displaystyle\int_a^af(x)\,dx=0$;

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

## Grasple exercises

75563, 75363, 75209, 75366, 63602, 63606, 63599