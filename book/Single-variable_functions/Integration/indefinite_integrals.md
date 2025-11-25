# Indefinite integrals

In this section we cover

- Indefinite integrals
- Antiderivatives
- Basic rules of calculation (e.g. sums and scalars)

::::::{prf:Definition}
:label: Def:Integration:IndefiniteIntegral
Let $f$ be a *continuous* function defined on some open (possible infinite) interval $I$. Then the **indefinite integral** of $f$ is the set of all its **antiderivatives** or **primitive functions**:

$$
\int f(x)\,dx=F(x)+C\quad\text{on}\quad I,
$$

where $F'(x)=f(x)$ for all $x\in I$ and $C\in\mathbb{R}$ is an arbitrary constant.
::::::

The arbitrary constant $C\in\mathbb{R}$ is called the **constant of integration**.

::::::{note}
In the sequel we frequently use a capital $C$ for the constant of integration without mentioning that it is an arbitrary real constant.
::::::

For many (standard) functions we are familiar with their derivatives. The other way around these derivatives give rise to antiderivatives in terms of these (standard) functions:

|   |   |
|---|---|
| $\displaystyle\int e^x\,dx=e^x+C$  | $\displaystyle\int x^{\alpha}\,dx=\frac{1}{\alpha+1}x^{\alpha+1}+C,\quad\alpha\neq-1$ |
| $\displaystyle\int\cos(x)\,dx=\sin(x)+C$ | $\displaystyle\int\sin(x)\,dx=-\cos(x)+C$ |
| $\displaystyle\int\frac{1}{\cos^2(x)}\,dx=\tan(x)+C$ | $\displaystyle\int\frac{1}{x}\,dx=\ln(x)+C,\quad x>0$ |
| $\displaystyle\int\cosh(x)\,dx=\sinh(x)+C$ | $\displaystyle\int\sinh(x)\,dx=\cosh(x)+C$ |
| $\displaystyle\int\frac{1}{\sqrt{1-x^2}}\,dx=\arcsin(x)+C,\quad -1<x<1$ | $\displaystyle\int\frac{1}{1+x^2}\,dx=\arctan(x)+C$ |

Het lukt me niet om de absolute waarde in de tabel te krijgen.

::::::{prf:Remark}
Note that we also have $\displaystyle\int\frac{1}{\sqrt{1-x^2}}\,dx=-\arccos(x)+C$.
::::::

::::::{prf:Notation}
Sometimes we combine the differential $dx$ with the numerator of the integrand, such as

$$
\int\frac{dx}{\cos^2(x)},\quad\int\frac{dx}{x},\quad\int\frac{dx}{\sqrt{1-x^2}},\quad\int\frac{dx}{1+x^2}\quad\text{and}\quad\int\frac{2\,dx}{(1+x)\sqrt{x}}.
$$

::::::

Using the chain rule we can also deduce more general formulas:

::::::{prf:Example}
:label: Ex:Integration:IndefiniteExamples
* $\displaystyle\int e^{3x}\,dx=\frac{1}{3}e^{3x}+C$;
* $\displaystyle\int(\cos(2x)-\sin(5x))\,dx=\frac{1}{2}\sin(2x)+\frac{1}{5}\cos(5x)+C$;
* $\displaystyle\int(x^3-2x+5)\,dx=\frac{1}{4}x^4-x^2+5x+C$;
* $\displaystyle\int\frac{\sqrt{x}-2+3x\sqrt{x}}{x}\,dx=\int\left(\frac{1}{\sqrt{x}}-\frac{2}{x}+3\sqrt{x}\right)\,dx=2\sqrt{x}-2\ln|x|+2x\sqrt{x}+C,\quad x>0$.
::::::

::::::{note}
In many cases an antiderivative $F$ of a function $f$ is easily checked by differentiation. The derivative $F'$ should be equal to the function $f$.
::::::

::::::{prf:Remark}
In the section on integration of rational functions we will frequently use that

$$
\int\frac{1}{x+\alpha}\,dx=\ln|x+\alpha|+C,\quad\alpha\in\mathbb{R}.
$$

::::::

In the next section we will explain the relation between definite and indefinite integrals.

## Grasple exercises

66937, 64404, 66936, 63716, 64405, 64407, 66933, 64408, 64596, 66011, 66935, 64128