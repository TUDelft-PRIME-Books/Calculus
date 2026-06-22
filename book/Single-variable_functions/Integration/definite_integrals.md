(Sec:Integration:DefiniteIntegrals)=

# Definite integrals

## Introduction

In {numref}`Chapter:FunctionsAndCurves` we have seen that a function $f$ assigns to each number $x$ in its domain a unique number $f(x)$ in its range. In {numref}`Chapter:Differentiation` we have learned about the derivatives of a function and how to calculate them. In this chapter we introduce the concept of **integration** which can be seen as the *inverse* operation of differentiation.

If we take a visual approach, a derivative of a function at a certain point on the graph of that function gives us the *slope* of the graph of a function at that point. Integration, on the other hand, can be used to calculate the *area* between the graph of a function and the horizontal axis.

We start with the definition of the **definite integral** of a function on an interval $[a,b]$.

## Definite integrals as areas

::::::{prf:definition}
:label: Def:Integration:DefiniteIntegral
For a *positive* and *continuous* function $f$ defined on an interval $[a,b]\subset D_f$ the **definite integral of a positive[^nonnegative] and continuous function**

[^nonnegative]: In fact, nonnegative would suffice.

$$
\int_a^bf(x)\,dx
$$

is the **area** between the graph of $f$ and the $x$-axis between $a$ and $b$:

:::{applet}
:url: calculus/definite_integrals/positive_continuous_function
:name: Fig:Integration:DefiniteIntegral
:class: dark-light 

The integral $\displaystyle\int_a^bf(x)\,dx$ for a positive and continuous function $f$.
:::

The numbers $a$ and $b$ are called the **limits of integration**, where $a$ is called the **lower limit** and $b$ the **upper limit**.

The function $f$ is called the **integrand** and $x$ is the **variable of integration**. 

::::::

In many cases we need to use special techniques to calculate the area under a curve, however for some simple positive and continuous functions we can calculate the area by using basic geometric shapes such as rectangles and triangles, as shown in the following example.

::::{prf:example}
:label: Ex:Integration:DefiniteSimple

We calculate the integral $\displaystyle\int_0^3(2x+1)\,dx$ by using {prf:ref}`Def:Integration:DefiniteIntegral`. First we sketch the graph of the function $f(x)=2x+1$ on the interval $[0,3]$ and shade the area between the graph and the $x$-axis.

```{applet}
:url: calculus/definite_integrals/linear_function
:name: Fig:DefiniteIntegrals:LinearFunction
:class: dark-light

The graph of the function $f(x)=2x+1$ on the interval $[0,3]$ and the related integral.
```

We can see that the region under the graph is a trapezoid. The area of this trapezoid equals base times the average height: $3\cdot\frac{1+7}{2}=12$. Hence

$$
\int_0^3(2x+1)\,dx=12.
$$

::::

Of course we do not always deal with positive and continuous functions, so we need a generalisation. First, we extend the concept of the definite integral to positive piecewise-continuous functions. Then we will see how to deal with negative functions and functions that take on both positive and negative values.

::::{prf:definition}
:label: Def:Integration:DefinitePositivePiecewise

For a *positive*, *piecewise-continuous* and *bounded* function $f$ defined on an interval $[a,b]\subset D_f$ the **definite integral of a positive, piecewise-continuous and bounded function**

$$
\int_a^bf(x)\,dx
$$

is the **area** between the graph of $f$ and the $x$-axis between $a$ and $b$.

::::

As you can see, the definition is the same as for positive continuous functions. The reason is that we can consider each piece of the positive piecewise-continuous function separately as a positive function on each corresponding subinterval and sum the corresponding areas.

:::{note}
If the function is *unbounded* somewhere on the interval $[a,b]$ the integral is called *improper*. We will consider *improper integrals* in {numref}`Sec:Integration:ImproperIntegrals`.
:::

::::::{prf:Example}
:label: Ex:Integration:DefinitePiecewise
Consider the function $f:[0,3]\to\mathbb{R}$ given by $f(x)=\left\{\begin{array}{ll}x, & 0\leq x<1,\\2, & 1\leq x\leq 2,\\x-1, & 2<x\leq 3.\end{array}\right.$

The graph of this piecewise-continuous function is shown below. We have shaded the area between the graph and the $x$-axis.

```{applet}
:url: calculus/definite_integrals/piecewise_function
:name: Fig:Integration:DefinitePiecewise
:class: dark-light

The graph of a positive piecewise-continuous function and the area between the graph and the $x$-axis.
```

The definite integral of $f$ over the interval $[0,3]$ can be calculated as the sum of three areas:

$$
\int_0^3f(x)\,dx=\int_0^1x\,dx+\int_1^22\,dx+\int_2^3(x-1)\,dx=\frac{1}{2}+2+\frac{3}{2}=4.
$$

::::::

This example illustrates the following theorem.

:::{prf:theorem}
:label: Thm:Integration:DefinitePositivePiecewise

For a *positive*, *piecewise-continuous* and *bounded* function $f$ defined on an interval $[a,b]$ that is made up of $n$ continuous pieces on the subintervals $[x_0,x_1]$, $[x_1,x_2]$, $\ldots$, $[x_{n-1},x_n]$ with $a=x_0<x_1<\ldots<x_n=b$, the definite integral equals the sum of the integrals on each subinterval:

$$
\int_a^bf(x)\,dx=\sum_{k=1}^n\int_{x_{k-1}}^{x_k}f(x)\,dx.
$$

::::

Now we know how to handle the definite integral of a positive piecewise-continuous function, we are going to extend {prf:ref}`Def:Integration:DefiniteIntegral` to negative piecewise-continuous functions and after that to piecewise-continuous functions that take on both positive and negative values.

::::::{prf:definition}
:label: Def:Integration:DefiniteNegative

For a *negative*, *piecewise-continuous* and *bounded* function $f$ defined on an interval $[a,b]$ the **definite integral of a negative, piecewise-continuous and bounded function**

$$
\int_a^bf(x)\,dx
$$

is *minus* the **area** between the graph of $f$ and the $x$-axis between $a$ and $b$.
::::::

Note that this means that we assume that an area is a nonnegative quantity. Hence, for negative piecewise-continuous functions the definite integral will be a negative number.

But what if the function takes on both positive and negative values? Well, in that case we split the interval into several subintervals such that on each subinterval the function is either positive or negative. Then we calculate the area on each subinterval and add them together, taking into account the sign of the function on each subinterval. Or in other words: If $f$ takes on both positive and negative values the integral equals the total area above the $x$-axis minus the total area below the $x$-axis, as illustrated in the following figure.

```{applet}
:url: calculus/definite_integrals/positive_and_negative_values
:name: Fig:Integration:Integral3
:class: dark-light

The integral $\displaystyle\int_a^bf(x)\,dx$ for a function that takes on both positive and negative values.
```

::::{prf:example}
:label: Ex:Integration:IntegralCos

```{applet}
:url: calculus/definite_integrals/cosine_area
:name: Fig:Integration:IntegralCos
:class: dark-light

The integral $\displaystyle\int_0^{2\pi}\cos(x)\,dx$ visualised.
```

\begin{align*}
\int_0^{2\pi}\cos(x)\,dx&=\int_0^{\frac{1}{2}\pi}\cos(x)\,dx+\int_{\frac{1}{2}\pi}^{\pi}\cos(x)\,dx\\
&{}\quad{}+\int_{\pi}^{\frac{3}{2}\pi}\cos(x)\,dx+\int_{\frac{3}{2}\pi}^{2\pi}\cos(x)\,dx=0.
\end{align*}

::::

The same idea applies to piecewise-continuous functions. This leads us to the following final definition of a definite integral.

::::::{prf:definition}
:label: Def:Integration:DefiniteGeneral
For a *piecewise-continuous* and *bounded* function $f$ defined on an interval $[a,b]\subset D_f$ the **definite integral of a piecewise-continuous and bounded function**

$$
\int_a^bf(x)\,dx
$$

is the **area** between the graph of $f$ and the $x$-axis between $a$ and $b$, taking into account the sign of the function on each subinterval: if the function takes on positive values on a subinterval, the area above the $x$-axis is added and if the function takes on negative values the area below the $x$-axis is subtracted. This is sometimes called the **signed area** between the graph of $f$ and the $x$-axis.

::::::

::::{question}
:type: short-answer
:variant: gaps
:admonition:
:class: question
:showanswer:

Fill in the gaps with the correct words:

---
TI[definite]
TI[limit]
TI[lower limit]
TI[integrand]
TI[variable]
^^^
? Consider the {gap} integral $\displaystyle\int_a^bf(x)\,dx$.

The number $b$ is called the upper {gap} and the number $a$ is called the {gap} of the integral.

The function $f$ is called the {gap} and $x$ is the {gap} of integration.
---
::::

We end this subsection with an example. 

::::::{prf:example}
:label: Ex:Integration:DefiniteBoth

Consider the function $f:[-2,5]\to\mathbb{R}$ given by $f(x)=\left\{\begin{array}{rl}1, &-2\leq x<0,\\2x-4, & \phantom{-}0\leq x<2,\\-x+4, & \phantom{-}2\leq x\leq 5,\end{array}\right.$ of which you can find the graph below.

```{applet}
:url: calculus/definite_integrals/piecewise_function_with_negative_and_positive_values
:name: Fig:Integration:DefiniteBoth
:class: dark-light

The graph of a piecewise-continuous function that takes on both positive and negative values.
```

The integral $\displaystyle\int_{-2}^5f(x)\,dx$ can be calculated as follows:

\begin{align*}
\int_{-2}^{5}f(x)\,dx &= \int_{-2}^{0}1\,dx+\int_{0}^{2}(2x-4)\,dx+\int_{2}^{5}(-x+4)\,dx\\
&= \int_{-2}^{0}1\,dx+\int_{0}^{2}(2x-4)\,dx\\
&{}\quad{}+\int_{2}^{4}(-x+4)\,dx+\int_{4}^{5}(-x+4)\,dx \\
&= 2 \cdot 1-\frac12\cdot2\cdot4+\frac12\cdot2\cdot2-\frac12\cdot1\cdot1 \\
&= 2 - 4 + 2 - \frac12 \\
&= -\frac12.
\end{align*}

In the second step we have split the last integral into two parts: one part from $2$ to $4$ where the function is positive and one part from $4$ to $5$ where the function is negative. After that we used the formulas for the areas of rectangles and triangles to calculate the areas and introduced the appropriate signs.

::::::

Now we have {prf:ref}`Def:Integration:DefiniteGeneral`, we can start looking at how to calculate definite integrals for functions that are not so easy to handle geometrically. For this we introduce the concept of Riemann sums.

## Riemann sums

Consider the graph of a function shown in the figure below with the indicated area between the graph of the function and the $x$-axis that we want to calculate.

```{applet}
:url: calculus/definite_integrals/general_function
:name: Fig:DefiniteIntegrals:General
:class: dark-light

A general function with the area to be calculated.
```

Even though the function is continuous on the interval $[a,b]$, it is not composed of a simple geometric shape such as a rectangle or a triangle. Hence we cannot calculate the area directly. In order to find this area, we start with an approximation: we divide the interval $[a,b]$ into subintervals and consider the sum of the areas of the indicated rectangles:

```{applet}
:url: calculus/definite_integrals/sum_of_areas_of_rectangles
:name: Fig:Integration:SumRectangles
:class: dark-light

Sum of areas of rectangles.
```

The height of each rectangle is taken to be the value of the function $f$ at an arbitrary point $x_n^*$ in the corresponding subinterval. This point $x_n^*$ is called a **sample point** and might be any point in the subinterval such as the left point, the right point or the middle point, for instance. The width of each rectangle is $\Delta x_n = x_n - x_{n-1}$. Then we take the sum of the areas of all rectangles.

In fact, let us divide the interval $[a,b]$ into $N$ subintervals of equal width $\Delta x = \dfrac{b-a}{N}$:

$$
a=x_0 < x_1 < x_2 < \ldots < x_{N-1} < x_N=b.
$$

```{applet}
:url: calculus/definite_integrals/building_a_Riemann_sum
:name: Fig:Integration:RiemannSum
:class: dark-light

Building a Riemann sum.
```

If we choose as sample point $x_n^*=x_n$ the right point in each subinterval $[x_{n-1},x_n]$, then the area equals

$$
\sum_{n=1}^Nf(x_n)\Delta x\quad\text{with}\quad x_n=a+n\Delta x\quad\text{and}\quad\Delta x=x_n-x_{n-1}=\frac{b-a}{N}.
$$

The sum $\displaystyle\sum_{n=1}^Nf(x_n)(x_n-x_{n-1})$ is called a **Riemann sum**, named after the German mathematician [Georg Friedrich Bernhard Riemann (1826-1866)](https://en.wikipedia.org/wiki/Bernhard_Riemann):

:::::{prf:definition}
:label: Def:Integration:RiemannSum

The **Riemann sum** $R_N$ of a function $f$ on the interval $[a,b]$ for a given partition $P=\{x_0,x_1,\ldots,x_N\}$ with **sample points** $x_n^*$ in each subinterval $[x_{n-1},x_n]$ is defined as

$$
R_N=\sum_{n=1}^Nf(x_n^*)(x_n-x_{n-1}).
$$

:::::

If we let the number of subintervals $N$ go to infinity, the width of each subinterval $\Delta x$ tends to zero and the Riemann sum approaches the exact area between the graph of the function and the $x$-axis. This leads us to the following theorem for the definite integral in terms of Riemann sums.

::::::{prf:theorem}
:label: Thm:Integration:DefiniteRiemann

The **definite integral of a piecewise-continuous and bounded function** $f$ on the interval $[a,b]\subset D_f$ is equal to the limit of the Riemann sums as the number of subintervals $N$ approaches infinity

$$
\int_a^bf(x)\,dx=\lim_{N\to\infty}\sum_{n=1}^Nf(x_n)\Delta x\;\text{with}\;\Delta x=\frac{b-a}{N}\;\text{and}\;x_n=a+n\Delta x,
$$

provided that this limit exists and is the same for *every* choice of sample points $x_n^*$ in each subinterval $[x_{n-1},x_n]$.
::::::

::::{prf:remark}
:label: Remark:Integration:RiemannSum

We have chosen to divide the interval $[a,b]$ into $N$ subintervals of *equal width* $\Delta x=\dfrac{b-a}{N}$, which is not really necessary but makes the formulas somewhat easier.
::::

The integral sign $\displaystyle\int$ was introduced by the German mathematician [Gottfried Wilhelm Leibniz (1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) and has the form of an elongated (stretched) $S$ which indicates the *limit* of (Riemann) sums.

Because the limit of the Riemann sums might not exist, we introduce the term **integrable** to indicate that the integral exists:

::::{prf:definition}
:label: Def:Integration:Integrable

A function for which the limit of the Riemann sums exists is called **integrable**.
::::

Luckily, but without giving a formal proof here, we have the following important result:

::::{prf:theorem}
:label: Thm:Integration:IntegrablePiecewise

Every *piecewise-continuous* and *bounded* function on an interval $[a,b]$ is integrable.
::::

Before we continue to properties of definite integrals, we show one example of calculating a definite integral using Riemann sums.

::::::{prf:example}
:label: Ex:Integration:RiemannSum

Consider the function $f$ on the interval $[0,1]$ given by $f(x)=x^2$. We want to calculate the integral $\displaystyle\int_0^1x^2\,dx$ using Riemann sums.

We divide the interval $[0,1]$ into $N>0$ subintervals of equal width $\Delta x=\frac{1-0}{N}=\frac{1}{N}$. The endpoints of the subintervals are given by $x_n=0+n\cdot\frac{1}{N}=\frac{n}{N}$ for $n=0,1,2,\ldots,N$.

As sample points we choose the right endpoints of each subinterval, $x_n^*=\frac{n}{N}$ for $n=1,2,\ldots,N$, which gives the function values $f(x_n^*)=\left(\frac{n}{N}\right)^2=\frac{n^2}{N^2}$.

Then the Riemann sum $R_N$ equals,

\begin{align*}
R_N&= \sum_{n=1}^Nf(x_n^*)\Delta x \\
&= \sum_{n=1}^N\frac{n^2}{N^2}\cdot\frac{1}{N} \\
&= \frac{1}{N^3}\sum_{n=1}^Nn^2 \\
&= \frac{1}{N^3}\left(1^2+2^2+3^2+\cdots+N^2\right) \\
&= \frac{1}{N^3}\cdot\frac{N(N+1)(2N+1)}{6} \\
&= \frac{(N+1)(2N+1)}{6N^2} \\
&= \frac{2N^2+3N+1}{6N^2}.
\end{align*}

Here we used the result from {numref}`Exc:SumsAndProducts:SumOfSquares`.

Using techniques from {numref}`Section:Limitinf` we find that

$$
\int_0^1x^2\,dx=\lim_{N\rightarrow\infty}R_N=\lim_{N\rightarrow\infty}\frac{2N^2+3N+1}{6N^2}
=\frac{2}{6}=\frac{1}{3}.
$$

Because the limit of the Riemann sums exists, we conclude that the function $f$ is integrable on the interval $[0,1]$ and that

$$
\int_0^1x^2\,dx=\frac{1}{3}.
$$

::::::

Since the width of each subinterval $[x_{n-1},x_n]$ tends to zero, the choice of the *sample point* $x_n^*$ in $[x_{n-1},x_n]$ is arbitrary. Except for this choice of the sample point, there are other ways to define a definite integral. We chose the definition of a so-called **Riemann integral**. Instead one could take the *lower sum* of all areas with as height the minimum of $f$ in each subinterval and the *upper sum* of all areas with as height the maximum of $f$ in each subinterval. A function $f$ is then called integrable if the *supremum* (the smallest upperbound) of all lower sums equals the *infimum* (the largest lowerbound) of all upper sums, being the value of the integral. This is the definition of a so-called **Darboux integral**, named after the French mathematician [Jean-Gaston Darboux (1842-1917)](https://en.wikipedia.org/wiki/Jean_Gaston_Darboux).

A function $f$ is Darboux integrable if and only if it is Riemann integrable. Moreover, the values of the integrals are the same.

:::{note}
There is a more general way to define definite integrals due to the French mathematician [Henri Léon Lebesgue (1875-1941)](https://en.wikipedia.org/wiki/Henri_Lebesgue). The **Lebesgue integral** is a generalisation of the Riemann integral that extends integration to a broader class of functions by partitioning the range (the $y$-axis) instead of the domain (the $x$-axis). It uses *measure theory* to calculate the "area" under a curve by measuring the size of the set of $x$-values for given $y$-values, rather than summing rectangle areas.

All functions that are Riemann integrable are also Lebesgue integrable. 

In this book we do only use the definition of Riemann integrals.
:::

::::{question}
:type: multiple-choice
:variant: single-select
:admonition:
:class: question
:showanswer:

For some function $f$ on the interval $[a,b]$ we have the Riemann sum

$$
R_N = \sum_{n=1}^N f(x_n)\Delta x = \dfrac{2N^2-3N+4}{3N^2+4N+5}.
$$

Find $\displaystyle\int_a^bf(x)\,dx$.

---
[ ] $\displaystyle\int_a^bf(x)\,dx=\dfrac{4}{5}$.
> You probably chose this answer because these are the constant terms in the numerator and denominator of $R_N$. However, you should do something with the leading terms in the numerator and denominator of $R_N$.
[ ] $\displaystyle\int_a^bf(x)\,dx=\dfrac{1}{4}$.
> You probably chose this answer by summing all terms in the numerator and denominator of $R_N$. However, you should do something with the leading terms in the numerator and denominator of $R_N$.
[ ] $\displaystyle\int_a^bf(x)\,dx=-\dfrac{3}{4}$.
> You probably chose this answer because these are the middle terms in the numerator and denominator of $R_N$. However, you should do something with the leading terms in the numerator and denominator of $R_N$.
[x] $\displaystyle\int_a^bf(x)\,dx=\dfrac{2}{3}$.
> This is the correct answer. To find the value of the integral, we need to calculate the limit of $R_N$ as $N$ approaches infinity. The leading terms in the numerator and denominator of $R_N$ are $2N^2$ and $3N^2$, respectively. As $N$ approaches infinity, the lower order terms become negligible compared to the leading terms, so we can focus on the ratio of the leading terms. Therefore, we have:

$$
\displaystyle\int_a^bf(x)\,dx = \lim_{N \to \infty} R_N = \dfrac{2}{3}.
$$
---
::::

Calculating definite integrals using Riemann sums can be quite laborious. In the next sections we will see other techniques to evaluate definite integrals more easily. But first we state some important properties of definite integrals.

## Properties of definite integrals

Using {prf:ref}`Def:Integration:DefiniteGeneral` we can derive several useful properties of definite integrals.

::::{prf:theorem}
:label: Thm:Integration:DefinitePropertiesArea

- $\displaystyle\int_a^af(x)\,dx=0$ for $a\in D_f$;

- $\displaystyle\int_a^bc\,dx=c(b-a)$ with $a$, $b$ and $c$ any real numbers;

- $\displaystyle\int_a^bf(x)\,dx=\int_a^rf(x)\,dx+\int_r^bf(x)\,dx$ for any $r$ in $[a,b]$ and $f$ piecewise continuous and bounded on $[a,b]$;

- $\displaystyle\int_{-a}^af(x)\,dx=0$ for $a\in D_f$ and $f$ *odd* and piecewise continuous and bounded on $[-a,a]$;

- $\displaystyle\int_{-a}^af(x)\,dx=2\int_0^af(x)\,dx$ for $a\in D_f$ and $f$ *even* and piecewise continuous and bounded on $[-a,a]$.

::::

The above theorem can be proved by considering the areas involved according to {prf:ref}`Def:Integration:DefiniteGeneral`. We will not give the full proofs here, but illustrate the last two properties with examples.

::::::{prf:Example}
:label: Ex:Integration:DefiniteOdd

The sine function $\sin(x)$ is an odd function on the interval $\left[-\frac{1}{2}\pi,\frac{1}{2}\pi\right]$, of which the graph is shown below.

```{applet} 
:url: calculus/definite_integrals/sine_area
:name: Fig:Integration:DefiniteOdd
:class: dark-light

The graph of the sine function and the integral $\displaystyle\int_{-\frac12\pi}^{\frac12\pi}\sin(x)\,dx$.
```

Inspection of the graph shows that the area below the $x$-axis and to the left of the $y$-axis equals the area above the $x$-axis and to the right of the $y$-axis. Since the area below the $x$-axis is taken with a negative sign in {prf:ref}`Def:Integration:DefiniteGeneral`, these two areas cancel, and we find

$$
\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\sin(x)\,dx=0.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:DefiniteEven

The absolute value function $|x|$ is an even function on the interval $\left[-a,a\right]$ with $a>0$ and its graph is shown below.

```{applet}
:url: calculus/definite_integrals/absolute_value
:name: Fig:Integration:DefiniteEven
:class: dark-light

The even function $|x|$ and its integral on $[-a,a]$.
```

Inspection of the graph shows that the area above the $x$-axis and to the left of the $y$-axis equals the area above the $x$-axis and right of the $y$-axis. Because both areas are taken with a positive sign in {prf:ref}`Def:Integration:DefiniteGeneral`, we find

$$
\int_{-a}^a|x|\,dx=2\int_0^ax\,dx=x^2\bigg|_0^a=a^2.
$$

::::::

The next theorem states that the choice of the variable of integration does not matter.

::::{prf:theorem}
:label: Thm:Integration:VariableOfIntegration

For an integrable function $f$ on the interval $[a,b]\subset D_f$, the choice of the variable of integration does not change the value of the integral:

$$
\int_a^bf(x)\,dx=\int_a^bf(t)\,dt=\int_a^bf(u)\,du.
$$

::::

A rigorous proof of this theorem can be given using Riemann sums, but we will not give it here. You can however convince yourself that this is true by considering the definition of the definite integral in {prf:ref}`Def:Integration:DefiniteGeneral`. If you would draw the graph of the function $f$ and shade the area between the graph and the $x$-axis between $a$ and $b$, you would see that the area does not depend on the name of the variable of integration.

Finally, we state some more properties of definite integrals. Proving these properties requires something called the *fundamental theorem of calculus*, which we will introduce in {numref}`Sec:Integration:FundamentalTheorem`. For now, we just state the properties.

::::{prf:theorem}
:label: Thm:Integration:DefinitePropertiesFundamental

- $\displaystyle\int_a^bf(x)\,dx+\int_b^cf(x)\,dx=\int_a^cf(x)\,dx$ for any real numbers $a$, $b$ and $c$ and $f$ piecewise continuous and bounded on $[a,c]$;

- $\displaystyle\int_b^af(x)\,dx=-\int_a^bf(x)\,dx$ for any real numbers $a$ and $b$ and $f$ piecewise continuous and bounded on $[a,b]$;

- $\displaystyle\int_a^b\left(f(x)+g(x)\right)\,dx=\int_a^bf(x)\,dx+\int_a^bg(x)\,dx$ for any real numbers $a$ and $b$ and $f$ and $g$ piecewise continuous and bounded on $[a,b]$;

- $\displaystyle\int_a^b cf(x)\,dx=c\int_a^bf(x)\,dx$ for any real numbers $a$, $b$ and $c$ and $f$ piecewise continuous and bounded on $[a,b]$.

::::

Finally, we state some important comparison properties of definite integrals. These can be used to estimate the value of definite integrals, as we will do in {prf:ref}`Ex:Integration:DefiniteApproximation`.

::::{prf:theorem}
:label: Thm:Integration:DefiniteComparison

- If $f(x)\geq0$ for $a\leq x\leq b$ and $f$ is piecewise continuous and bounded on $[a,b]$, then $\displaystyle\int_a^bf(x)\,dx\geq0$;

- If $f(x)\geq g(x)$ for $a\leq x\leq b$ and $f$ and $g$ are piecewise continuous and bounded on $[a,b]$, then $\displaystyle\int_a^bf(x)\,dx\geq\int_a^bg(x)\,dx$;

- If $m\leq f(x)\leq M$ for $a\leq x\leq b$ and $f$ is piecewise continuous and bounded on $[a,b]$, then $m(b-a)\leq\displaystyle\int_a^bf(x)\,dx\leq M(b-a)$.
::::


::::::{prf:Example}
:label: Ex:Integration:DefiniteApproximation

In order to estimate the value of $\displaystyle\int_0^1e^{-x^2}\,dx$, we note that the integrand $f(x)=e^{-x^2}$ is a decreasing function on $[0,1]$. Its absolute maximum value is $M=f(0)=1$ and its absolute minimum value is $m=f(1)=e^{-1}$. Hence we have

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
:label: Ex:Integration:DefiniteDistance

:::{figure} Images/filip-mroz-XCkRGOX2VgM-unsplash.jpg
:width: 75%
:name: Fig:DefiniteIntegrals:Athlete
:align: center
:figclass: margin
:author: Filip Mroz
:placement: caption
:license: Unsplash License
:source: [Unsplash](https://unsplash.com/photos/woman-running-wearing-armband-XCkRGOX2VgM?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText")
:date: 2016-11-16

An athlete during an interval training.

:::

Consider an athlete during an interval training. She starts walking at a speed of $5$ km/h during $5$ minutes($\frac{1}{12}$ hours). Then she runs at a speed of $15$ km/h during $2$ minutes ($\frac{1}{30}$ hours), followed by a period of $4$ minutes ($\frac{1}{15}$ hours) walking at a speed of $6$ km/h. Then she runs at a speed of $20$ km/h during $3$ minutes ($\frac{1}{20}$ hours), followed by $6$ minutes ($\frac{1}{10}$ hours) walking at a speed of $4$ km/h.

What is the distance traveled by the athlete?

:::{applet}
:url: calculus/definite_integrals/an_interval_training
:name: Fig:DefiniteIntegrals:Distance
:class: dark-light

The speed $v$ at which the athlete is moving during the interval training. On the horizontal axis the time $t$ is shown in minutes. On the vertical axis the speed in kilometers per hour.
:::

Note that the athlete is active for $20$ minutes, which equals $\frac{1}{3}$ hours. In order to find the total distance traveled by the athlete we add the five different areas:

$$
\begin{align*}
\int_0^{\frac{1}{3}}v(t)\,dt &= \frac{1}{12}\cdot5+\frac{1}{30}\cdot15+\frac{1}{15}\cdot5+\frac{1}{20}\cdot20+\frac{1}{15}\cdot6\\
&=\frac{25+30+20+60+24}{60}\\
&=\frac{159}{60}.
\end{align*}
$$

This means that the athlete has traveled a distance of $\frac{159}{60}$ km $\approx2.65$ km during her interval training.

We could also have changed the speed into meters per second and the time into seconds. Then the definite integral would have given the same distance measured in meters.

::::::

Note that the velocity in general cannot change suddenly. In fact, the velocity should be a continuous function. Then the distance equals the area between the graph of the velocity and the horizontal axis. Before you learn how to calculate this area exactly, we need to discuss another type of integral in {numref}`Sec:Integration:IndefiniteIntegrals`.

## Grasple exercises

### Terminology of definite integrals

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/62e814ee-8ef0-4fff-a9ec-5840b2d01720?id=75363
:label: Grasple:75363
:dropdown:
:description: Practicing terminology of definite integrals.

::::

### Definite integrals using areas

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d54d29f0-1b1e-449a-851a-58a88cf86a40?id=132478
:label: Grasple:132478
:dropdown:
:description: The definite integral of a continuous function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b95055c4-d49a-4acb-9314-ccca8a3d972b?id=132479
:label: Grasple:132479
:dropdown:
:description: The definite integral of a discontinuous function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7716710d-1e60-4a38-920a-81081f257611?id=132480
:label: Grasple:132480
:dropdown:
:description: The definite integral of a function with a special square root.

::::

### Riemann sums

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/59fac7ae-702d-44fa-81df-5e936fdec6f9?id=63602
:label: Grasple:63602
:dropdown:
:description: Practicing with Riemann sums.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/765e5797-52a4-47d2-aace-2aa9bd6b9842?id=63606
:label: Grasple:63606
:dropdown:
:description: Practicing with Riemann sums once more.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7e5d0644-606d-4d78-8c70-9051d215b799?id=63599
:label: Grasple:63599
:dropdown:
:description: Identifying the correct integral from a Riemann sum.

::::

### Upper bounds for definite integrals

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d55fa167-c082-491a-9fe2-39f136afa497?id=75209
:label: Grasple:75209
:dropdown:
:description: Calculating an upper bound for a definite integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/933d3d4b-a7fd-423e-a2ce-d64504eaabf8?id=75366
:label: Grasple:75366
:dropdown:
:description: Calculating an upper bound for another definite integral.

::::
