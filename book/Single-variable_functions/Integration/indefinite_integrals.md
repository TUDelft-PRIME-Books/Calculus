(Sec:Integration:IndefiniteIntegrals)=

# Indefinite integrals

In {numref}`Chapter:Differentiation` we saw the concept of the derivative of a function. It turns out that there is a reverse operation, called *integration*, which allows us to find a function if we know its derivative. In this section we introduce the concepts of *antiderivatives* and *indefinite integrals* as the reverse operation of differentiation.

## Antiderivatives

We start with the following definition:

::::{prf:definition}
:label: Def:Integration:Antiderivative
Let $f$ be a function defined on some open (possibly infinite) interval $I$. A function $F$ defined on $I$ is called an **antiderivative** of $f$ if

$$
F'(x)=f(x)\quad\text{for all}\quad x\in I.
$$

Other common names for the term *antiderivative* are **primitive function** or **primitive** of $f$.

:::::

Note that an antiderivative $F$ of a function $f$ is not a unique function, as the following theorem states:

::::::{prf:Theorem}
:label: Th:Integration:AntiderivativeConstant

If $F$ is an antiderivative of a function $f$ on an open interval $I$ and $C$ is an arbitrary real constant, then the function $G$ defined by

$$
G(x) =F(x)+C\quad\text{for all}\quad x\in I,
$$

is also an antiderivative of $f$ on $I$.
::::::

::::::{admonition} Proof of {prf:ref}`Th:Integration:AntiderivativeConstant`
:class: tudproof

Because $F$ is an antiderivative of $f$ on $I$ we have $F'(x)=f(x)$ for all $x\in I$.

Because $C$ is an arbitrary real constant we have $\dfrac{d}{dx}\left[C\right] = 0$.

Combining these two results we find that

$$
G'(x)=\frac{d}{dx}\left[F(x)+C\right]=F'(x)+0=f(x)\quad\text{for all}\quad x\in I,
$$

showing that $G$ is also an antiderivative of $f$ on $I$.
::::::

Because of the close relation between derivates and antiderivatives we have the following important observation:

::::::{prf:observation}
:label: Obs:Integration:AntiderivativeConstant

In many cases an antiderivative $F$ of a function $f$ is easily checked by differentiation. The derivative $F'$ should be equal to the function $f$.
::::::

For many (standard) functions we are familiar with their derivatives. The other way around these derivatives give rise to antiderivatives in terms of these (standard) functions:

```{table} Standard functions and their antiderivatives.
:widths: auto
:align: center
:class: mid-align center-align
:name: Tab:Integration:StandardAntiderivatives

| Standard function | An antiderivative | Remark |
|---|---|---|
| $\displaystyle e^x$ | $\displaystyle e^x$ |  |
| $\displaystyle x^{\alpha}$ | $\displaystyle \frac{1}{\alpha+1}x^{\alpha+1}$ | $\alpha\neq-1$ |
| $\displaystyle\cos(x)$ | $\displaystyle \sin(x)$| |
| $\displaystyle\sin(x)$ | $\displaystyle -\cos(x)$ | |
| $\displaystyle\frac{1}{\cos^2(x)}$ | $\displaystyle \tan(x)$| |
| $\displaystyle\frac{1}{x}$ | $\displaystyle \ln\lvert x\rvert$ | $x>0$ |
| $\displaystyle\cosh(x)$ | $\displaystyle \sinh(x)$ | |
| $\displaystyle\sinh(x)$ | $\displaystyle \cosh(x)$ | |
| $\displaystyle\frac{1}{\sqrt{1-x^2}}$ | $\displaystyle \arcsin(x)$ | $-1<x<1$ |
| $\displaystyle\frac{1}{1+x^2}$ | $\displaystyle \arctan(x)$ | |

```

Just like with derivatives we would like to have a notation for antiderivatives. This leads us to the concept of *indefinite integrals*.

## Indefinite integrals

::::::{prf:Definition}
:label: Def:Integration:IndefiniteIntegral
Let $f$ be a *continuous* function defined on some open (possibly infinite) interval $I$. Then the **indefinite integral** of $f$ is the set of all its *antiderivatives*, and is denoted by:

$$
\int f(x)\,dx=F(x)+C\quad\text{on}\quad I,
$$

where $F$ is *any* antiderivative of $f$ on $I$ and $C\in\mathbb{R}$ is an arbitrary constant.

The arbitrary constant $C\in\mathbb{R}$ is called the **constant of integration**.
::::::

::::::{note}
In the sequel we frequently use a capital $C$ for the constant of integration without mentioning that it is an arbitrary real constant.
::::::

We can transform {numref}`Tab:Integration:StandardAntiderivatives` into a table with formulas for indefinite integrals:

```{table} Indefinite integrals of standard functions.
:widths: auto
:align: center
:class: mid-align center-align
:name: Tab:Integration:StandardIndefiniteIntegrals

| Indefinite integral | Remark |
|---|---|
| $\displaystyle \int e^x \,dx= e^x+C$ |  |
| $\displaystyle \int x^{\alpha} \,dx= \frac{1}{\alpha+1}x^{\alpha+1}+C$ | $\alpha\neq-1$ |
| $\displaystyle \int \cos(x) \,dx= \sin(x)+C$| |
| $\displaystyle \int \sin(x) \,dx= -\cos(x)+C$ | |
| $\displaystyle \int \frac{1}{\cos^2(x)} \,dx= \tan(x)+C$| |
| $\displaystyle \int \frac{1}{x} \,dx= \ln\lvert x\rvert+C$ | $x>0$ |
| $\displaystyle \int \cosh(x) \,dx= \sinh(x)+C$ | |
| $\displaystyle \int \sinh(x) \,dx= \cosh(x)+C$ | |
| $\displaystyle \int \frac{1}{\sqrt{1-x^2}} \,dx= \arcsin(x)+C$ | $-1<x<1$ |
| $\displaystyle \int \frac{1}{1+x^2} \,dx= \arctan(x)+C$ | |
```

::::::{prf:Remark}
Note that we also have $\displaystyle\int\frac{1}{\sqrt{1-x^2}}\,dx=-\arccos(x)+C$.
::::::

::::::{prf:Notation}
Sometimes we combine the differential $dx$ with the numerator of the integrand, such as

$$
\int\frac{dx}{\cos^2(x)},\quad\int\frac{dx}{x},\quad\int\frac{dx}{\sqrt{1-x^2}},\quad\int\frac{dx}{1+x^2}\quad\text{and}\quad\int\frac{2\,dx}{(1+x)\sqrt{x}}.
$$

::::::

## Properties of indefinite integrals

Just like definite integrals have several properties, indefinite integrals also have some useful properties:

::::{prf:theorem}
:label: Th:Integration:IndefiniteProperties

- $\displaystyle\int\left(f(x)+g(x)\right)\,dx=\int f(x)\,dx+\int g(x)\,dx$ for $f$ and $g$ continuous on some open interval $I$.

- $\displaystyle\int cf(x)\,dx=c\int f(x)\,dx$ for any real number $c$ and $f$ continuous on some open interval $I$.

::::

Using these so-called linear properties we can also determine indefinite integrals of linear combinations of functions. Two examples are given below.

::::::{prf:Example}
:label: Ex:Integration:IndefiniteExample1

Indefinite integrals of polynomials are found using the linear properties of indefinite integrals and the power rule from {numref}`Tab:Integration:StandardIndefiniteIntegrals`. For example:

\begin{align*}
\int(x^3-2x+5)\,dx&=\int x^3\,dx-2\int x\,dx+\int 5\,dx\\
&=\frac{1}{4}x^4-2\cdot\frac{1}{2}x^2+5x+C\\
&=\frac{1}{4}x^4 - x^2 + 5x + C.
\end{align*}
::::::

::::::{prf:Example}
:label: Ex:Integration:IndefiniteExample2

But why restrict ourselves to polynomials? We can use the same approach for more complicated functions as well. Assume $x>0$ in the following example:

\begin{align*}
\int\frac{\sqrt{x}-2+3x\sqrt{x}}{x}\,dx &= \int\left(\frac{1}{\sqrt{x}}-\frac{2}{x}+3\sqrt{x}\right)\,dx \\
&= \int x^{-\frac{1}{2}}\,dx - 2\int x^{-1}\,dx + 3\int x^{\frac{1}{2}}\,dx \\
&= 2\sqrt{x}-2\ln|x|+2x\sqrt{x}+C.
\end{align*}

::::::

In {numref}`Sec:Differentiation:ChainRule` we saw the chain rule for derivatives. This rule can also be used to determine some indefinite integrals, which will be explained in more detail in {numref}`Sec:Integration:Substitution`. For now we just state the following important, but *intermediate*, result:

:::{prf:theorem}
:label: Th:Integration:IndefiniteLinearSubstitution
Let $f$ be a continuous function on some open interval $I$, and let $\alpha,\beta\in\mathbb{R}$ with $\alpha\neq0$ such that the linear function $g(x)=\alpha x+\beta$ has its image in $I$. Then

$$
\int f(\alpha x+\beta)\,dx=\frac{1}{\alpha}F(\alpha x+\beta)+C,
$$`

where $F$ is any antiderivative of $f$ on $I$ and $C\in\mathbb{R}$ is an arbitrary constant.
:::

::::::{prf:Remark}
In the section on integration of rational functions we will frequently use that

$$
\int\frac{1}{x+\alpha}\,dx=\ln|x+\alpha|+C,\quad\alpha\in\mathbb{R}.
$$

::::::

In the next section we will explain the relation between definite and indefinite integrals.

## Grasple exercises

66937, 64404, 66936, 63716, 64405, 64407, 66933, 64408, 64596, 66011, 66935, 64128