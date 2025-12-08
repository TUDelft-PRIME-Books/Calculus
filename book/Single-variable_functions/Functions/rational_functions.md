```{admonition} Attribution
:class: attribution
This page reuses content from {cite:t}`dekleijn2025longdivision`.
```

(Sec:RationalFunctions)=
# Rational functions

## Introduction

::::{figure} Images/Fig-RationalFunctions-Intro.png
:name: Fig:RationalFunctions:Intro
:class: dark-light
:figclass: margin

Is this proper?

::::
:::::

Rational functions are functions that are formed by the ratio of two polynomials. They are widely used in various fields of mathematics, including calculus, algebra, and real analysis. Rational functions can exhibit interesting behaviors, such as asymptotes and discontinuities, which are treated in sections further on in this chapter.

We start of with some definitions:

::::{prf:definition}
:label: Def:RationalFunctions:Def

A **rational function** $r$ is a function that can be expressed as the ratio of two polynomials:

$$
r(x) = \frac{p(x)}{q(x)},
$$

where $p$ and $q$ are polynomials and $q(x) \neq 0$.

A **proper rational function** is a rational function where the degree of the numerator polynomial $p$ is less than the degree of the denominator polynomial $q$.

An **improper rational function** is a rational function where the degree of the numerator polynomial $p$ is greater than or equal to the degree of the denominator polynomial $q$.

::::

::::{prf:example}
:label: Ex:RationalFunctions:Examples

Consider the following three functions:

\begin{align*}
r_1(x) &= \frac{x^4-4x^3+3x^2+4x-4}{x^3-x^2-8x}, \\
r_2(x) &= 2x^2+1 + \frac{-x^2+4x-2}{x^3-2x+1},
\\
r_3(x) &= \frac{-x^2+4x-2}{x^3-2x+1}.
\end{align*}

The function $r_1$ is a rational function, but not a proper rational function since the degree of the numerator ($4$) is greater than the degree of the denominator ($3$), and can be seen directly from its definition as a ratio of two polynomials.

The function $r_2$ is also a rational function. This can be seen by rewriting it to a single ratio:

\begin{align*}
r_2(x) &= 2x^2+1 + \frac{-x^2+4x-2}{x^3-2x+1} \\
&= \frac{(2x^2+1)(x^3-2x+1) + (-x^2+4x-2)}{x^3-2x+1} \\
&= \frac{2x^5-3x^3+x^2+2x-1}{x^3-2x+1}.
\end{align*}

$r_2$ is again not a proper rational function since the degree of the numerator ($5$) is greater than the degree of the denominator ($3$).

$r_3$ is a proper rational function since the degree of the numerator ($2$) is less than the degree of the denominator ($3$) and is already expressed as a ratio of two polynomials.

::::

The domain of a rational function is all real numbers except where the denominator is zero, or in other words, the rational function $\frac{p(x)}{q(x)}$ is undefined where $q(x) = 0$.

First we will look at how to simplify rational functions by applying polynomial division. After that we will look at how to decompose proper rational functions into simpler fractions using partial fraction decomposition.

## Polynomial division

When dealing with rational functions where the degree of the numerator is greater than or equal to the degree of the denominator, it is often useful to perform polynomial long division. This allows us to express the rational function as a sum of a polynomial and a proper rational function.

In the method of long division of polynomials we consider quotients of polynomials $p$ and $q$, i.e. $\frac{p(x)}{q(x)}$. When the degree of $p$ is higher than the degree of $q$ it is possible that $p(x) = s(x)q(x)$ for $s$ another polynomial. In this case the long division terminates at $0$. It is also possible that the long division terminates at a polynomial $t$ that whose degree is lower than the degree of the polynomial $q$. In that case $p(x) = t(x) + s(x)q(x)$ for some polynomials $s$ and $t$.

The method works by starting with the highest power of $x$. We consider a monomial $a_1x^{k_1}$  such that the highest powers of $a_1x^{k_1}q(x)$ and $p(x)$ match. Then we consider $p_1(x)=p(x)-a_1x^{k_1}q(x)$ whose degree must be lower than the degree of $p$. If it is also lower than the degree of $q$ the long division terminates. Otherwise we continue by repeating the first step again, but now with respect to the polynomial $p_1$ instead of $p$.

Below are two examples, one for factoring out a linear factor of which we know that it is a linear factor (so the method is guaranteed to terminate at $0$) and one where we are writing a rational functions as the sum of a polynomial plus a proper rational function.  In this case the long division does not terminate at $0$.

::::{prf:example}
:label: Ex:RationalFunctions:PolynomialDivision1

In order to simplify the rational function

$$
\frac{x^4-4x^3+3x^2+4x-4}{x^3-2x^2-x+2}
$$

we can apply the technique of _canceling common factors_. Indeed we see that both the numerator and denominator are $0$ at $x=2$. This means both expressions can be written as $x-2$ times some other polynomial. We will show how to obtain this factorisation for the numerator by long division. We start by denoting the polynomial we want to factor out, i.e. by which we want to divide, on the left and the polynomial which we want to factor , i.e. which we want to divide, in the middle as follows:

$$
\begin{array}{rclcl}
x-2 & \Big/ & x^4-4x^3+3x^2+4x-4 & \Big\\ & 
\end{array}
$$

Now we consider by what monomial $ax^n$ we should multiply the left polynomial in order to match the highest order terms with the middle polynomial. In this case we find it should be $x^3$. Then we subtract the obtained polynomial from the middle polynomial as indicated. We write the monomial we had to multiply by on the right:

$$
\begin{array}{rclcl}
x-2 & \Big/ & x^4-4x^3+3x^2+4x-4 & \Big\backslash & x^3 \\
    &       & x^4-2x^3           &        &     \\
&          & \overline{\phantom{x^4}-2x^3+3x^2+4x-4} & \overline{\phantom{x^4}} & \\
\end{array}
$$

Now we repeat this step with the same left polynomial, but the new middle polynomial. For this second step we find that we should multiply by $-2x^2$.

$$
\begin{array}{rclcl}
x-2 & \Big/ & x^4-4x^3+3x^2+4x-4 & \Big\backslash & x^3-2x^2 \\
    &       & x^4-2x^3           &        &     \\
&          & \overline{\phantom{x^4}-2x^3+3x^2+4x-4} & \overline{\phantom{x^4}} & \\
&           & \phantom{x^4}-2x^3+4x^2           &        &     \\
&          & \overline{\phantom{x^4-2x^32}-x^2+4x-4} & \overline{\phantom{x^4}} & \\
\end{array}
$$

We repeat the step again and this time we find $-x$.

$$
\begin{array}{rclcl}
x-2 & \Big/ & x^4-4x^3+3x^2+4x-4 & \Big\backslash & x^3-2x^2-x \\
    &       & x^4-2x^3           &        &     \\
&          & \overline{\phantom{x^4}-2x^3+3x^2+4x-4} & \overline{\phantom{x^4}} & \\
&           & \phantom{x^4}-2x^3+4x^2           &        &     \\
&          & \overline{\phantom{x^4-2x^32}-x^2+4x-4} & \overline{\phantom{x^4}} & \\
&           & \phantom{x^4-2x^32}-x^2+2x           &        &     \\
&          & \overline{\phantom{x^4-2x^3-2x^2+\,}2x-4} & \overline{\phantom{x^4}} & \\
\end{array}
$$

We repeat one more time and this time we find $+2$. Note that the result of subtracting is now of lower degree then the polynomial on the left. This means our long division is done:

$$
\begin{array}{rclcl}
x-2 & \Big/ & x^4-4x^3+3x^2+4x-4 & \Big\backslash & x^3-2x^2-x \\
    &       & x^4-2x^3           &        &     \\
&          & \overline{\phantom{x^4}-2x^3+3x^2+4x-4} & \overline{\phantom{x^4}} & \\
&           & \phantom{x^4}-2x^3+4x^2           &        &     \\
&          & \overline{\phantom{x^4-2x^32}-x^2+4x-4} & \overline{\phantom{x^4}} & \\
&           & \phantom{x^4-2x^32}-x^2+2x           &        &     \\
&          & \overline{\phantom{x^4-2x^3-2x^2+\,}2x-4} & \overline{\phantom{x^4}} & \\
&          & \phantom{x^4-2x^3-2x^2+\,}2x-4 &  & \\
&          & \overline{\phantom{x^4-2x^3-2x^2+\,2x-}\,0} & \overline{\phantom{x^4}} & \\
\end{array}
$$

Since our long division terminates at $0$ this means that indeed the left polynomial is a factor fo the middle polynomial. Indeed the middle polynomial factors as a product of the left and right polynomials, i.e. 

$$
x^4-4x^3+3x^2+4x-4 = (x-2)(x^3-2x^2-x+2).
$$

For the denominator we can apply the same method of polynomial long division to find that

$$
x^3-2x^2-x+2=(x-2)(x^2-1).
$$

In other words, if $x\neq2$, we can simplify the original rational function as follows:

$$
\frac{x^4-4x^3+3x^2+4x-4}{x^3-2x^2-x+2} = \frac{(x-2)(x^3-2x^2-x+2)}{(x-2)(x^2-1)} = \frac{x^3-2x^2-x+2}{x^2-1}.
$$

::::

Not all long divisions will terminate at $0$. In general rational functions are not actually similar to linear functions and so long division will terminate at some non-zero rest term.

::::{prf:example}
:label: Ex:RationalFunctions:PolynomialDivision2

Let's consider the example of the rational function 

$$
\frac{\frac{1}{2}x^3+x^2-\frac{23}{2}x-24}{x^2-25}.
$$

In order to write this as a linear function plus a proper rational function we can apply long division. Again we put the denominator on the left and the numerator in the middle.

$$
\begin{array}{rclcl}
x^2-25 & \Big/ & \frac12x^3+x^2-\frac{23}{2}x-24 & \Big\backslash & \phantom{\frac12x+1} \\
%     &       & \frac12x^3\phantom{+x^2\,\,\,}-\frac{25}{2}x           &        &     \\
% &          & \overline{\phantom{\frac12x^3+\,\,}x^2\phantom{\frac{25}{2}}+x-24} & \overline{\phantom{\frac{5}{2}}} & \\
% &           & \phantom{\frac12x^3+\,\,}x^2\phantom{\frac{25}{2}+x}-25         &        &     \\
% &           & \overline{\phantom{\frac12x^3+\,\,x^2}\phantom{\frac{25}{2}+\,}x\phantom{2}+1}         &    \overline{\phantom{\frac{5}{2}}}    &     \\
\end{array}
$$

This time the first monomial on the right should be $\frac{x}{2}$. 

$$
\begin{array}{rclcl}
x^2-25 & \Big/ & \frac12x^3+x^2-\frac{23}{2}x-24 & \Big\backslash & \frac12x\phantom{+1} \\
    &       & \frac12x^3\phantom{+x^2\,\,\,}-\frac{25}{2}x           &        &     \\
&          & \overline{\phantom{\frac12x^3+\,\,}x^2\phantom{\frac{25}{2}}+x-24} & \overline{\phantom{\frac{5}{2}}} & \\
% &           & \phantom{\frac12x^3+\,\,}x^2\phantom{\frac{25}{2}+x}-25         &        &     \\
% &           & \overline{\phantom{\frac12x^3+\,\,x^2}\phantom{\frac{25}{2}+\,}x\phantom{2}+1}         &    \overline{\phantom{\frac{5}{2}}}    &     \\
\end{array}
$$

Then we proceed with the monomial $+1$. After this the remainder is lower in degree than the polynomial on the left so the long division terminates. 

$$
\begin{array}{rclcl}
x^2-25 & \Big/ & \frac12x^3+x^2-\frac{23}{2}x-24 & \Big\backslash & \frac12x+1 \\
    &       & \frac12x^3\phantom{+x^2\,\,\,}-\frac{25}{2}x           &        &     \\
&          & \overline{\phantom{\frac12x^3+\,\,}x^2\phantom{\frac{25}{2}}+x-24} & \overline{\phantom{\frac{5}{2}}} & \\
&           & \phantom{\frac12x^3+\,\,}x^2\phantom{\frac{25}{2}+x}-25         &        &     \\
&           & \overline{\phantom{\frac12x^3+\,\,x^2}\phantom{\frac{25}{2}+\,}x\phantom{2}+1}         &    \overline{\phantom{\frac{5}{2}}}    &     \\
\end{array}
$$

This means, as in general, that the polynomial in the middle divided by the polynomial on the left is equal to the polynomial on the right plus the remainder (on the bottom) divided by the polynomial on the left, i.e.

$$
\frac{\frac{1}{2}x^3+x^2-\frac{23}{2}x-24}{x^2-25} = \frac{x}{2}+1 + \frac{x+1}{x^2-25}.
$$

::::

In the next example, we will only present you with the final result of the long division. Try and see if you can see how this result was obtained using the method of long division presented above.

::::{prf:example}
:label: Ex:RationalFunctions:PolynomialDivision3

Long division can be applied whenever you have an improper rational function in order to write it as a polynomial plus a proper rational function. For instance suppose we consider the rational function

$$\frac{2x^5-3x^3+x^2+2x-1}{x^3-2x+1}.$$

The long division results in

$$
\begin{array}{rclcl}
x^3-2x+1 & \Big/ & 2x^5-3x^3+\phantom{2}x^2+2x-1 & \Big\backslash & 2x^2+1 \\
    &       & 2x^5-4x^3+2x^2           &        &     \\
    &       & \overline{\phantom{2x^5-4}x^3\phantom{2}-x^2+2x-1} & \overline{\phantom{x^5}} & \\
    &       & \phantom{2x^5-4}x^3\phantom{-2x^2\,\,}-2x+1         &        &     \\
    &       & \overline{\phantom{2x^5-4x^3\,\,}-x^2+4x-2}         & \overline{\phantom{x^5}} &     \\
\end{array}
$$

This means, as in general, that the polynomial in the middle divided by the polynomial on the left is equal to  the polynomial on the right plus the remainder (on the bottom) divided by the polynomial on the left, i.e. 

$$\frac{2x^5-3x^3+x^2+2x-1}{x^3-2x+1} = 2x^2+1 + \frac{-x^2+4x-2}{x^3-2x+1}.$$

::::

We end this section with the general result of polynomial long division in the next theorem.

::::{prf:theorem}
:label: Thm:RationalFunctions:PolynomialLongDivision

Let $r(x) = \frac{p(x)}{q(x)}$ be a rational function where the nominator $p$ has degree $P$ and the denominator $q$ has degree $Q$. If $P \geq Q$, then there exist a polynomial $s$ of degree $S=P-Q$ and a polynomial $t$ of degree $T<Q$ such that

$$
r(x) = s(x) + \frac{t(x)}{q(x)}.
$$

::::

## Partial fraction decomposition

In the previous examples you have seen how you can use polynomial long division to rewrite an improper rational function as a polynomial plus a proper rational function. In this section we will look at how to decompose proper rational functions into simpler fractions. This technique is called _partial fraction decomposition_.

Before we look at a first example, we take a look at regular fractions, such as

$$
\frac{1}{3}\text{ and }\frac{3}{7}.
$$

Normally you would calculate the sum of these fractions by rewriting them with a common denominator:

$$
\frac{1}{3}+\frac{3}{7} = \frac{1}{3}\frac{7}{7}+\frac{3}{7}\frac{3}{3} = \frac{7}{21}+\frac{9}{21} = \frac{16}{21}.
$$

If we would have two (simple) rational functions, we could do the same. For instance consider the next calculation:

\begin{align*}
\frac{1}{x+2}+\frac{3}{x-5} &= \frac{1}{x+2}\frac{x-5}{x-5}+\frac{3}{x-5}\frac{x+2}{x+2} \\
&= \frac{x-5}{(x+2)(x-5)} + \frac{3(x+2)}{(x-5)(x+2)} \\
&= \frac{x-5 + 3(x+2)}{(x+2)(x-5)} \\
&= \frac{4x+1}{x^2-3x-10}.
\end{align*}

This method of rewriting the some of the (simple) rational functions into a single rational function is exactly the opposite of the method of partial fraction decomposition. In partial fraction decomposition we start with a proper rational function, such as $\frac{4x+1}{x^2-3x-10}$ and we want to rewrite it as the sum of simpler rational functions, such as $\frac{1}{x+2}+\frac{3}{x-5}$.

If we look at the previous calculation, we see that the roots of the denominator $x^2-3x-10$ are $x=-2$ and $x=5$. These roots correspond to the denominators of the simpler rational functions $\frac{1}{x+2}$ and $\frac{3}{x-5}$. The entire concept of partial fraction decomposition is based on this observation in combination with the {prf:ref}`Fundamental Theorem of algebra <Thm:ComplexNumbers:fundamental>`.

We will look at several cases where we can apply partial fraction decomposition, starting with the case where the denominator can be factored into distinct linear factors.

::::{prf:example}
:label: Ex:RationalFunctions:PartialFractionDecomposition1

Consider the proper rational function

$$
r(x)  = \frac{p(x)}{q(x)} = \frac{4x+2}{x^2-1}.
$$

The denominator $q(x)=x^2-1$ of this rational function can be factored as $q(x)=(x-1)(x+1)$, i.e. as a product of distinct linear factors. So, based on our previous thinking, let us look for two polynomials $f$ and $g$ such that

:::{math}
:label: Eq:RationalFunctions:PartialFractionDecomposition1
r(x) = \frac{f(x)}{x-1} + \frac{g(x)}{x+1}
:::

holds. Since $r$ remains the same proper rational function, the ratio between the degrees of the nominator $p(x)=4x+2$ and the denominator $q(x)=x^2-1$ should also not change. We start by taking the right-hand side of Equation {eq}`Eq:RationalFunctions:PartialFractionDecomposition1` and rewriting it to a single rational function:

\begin{align*}
\frac{f(x)}{x-1} + \frac{g(x)}{x+1} &= \frac{f(x)(x+1)}{(x-1)(x+1)} + \frac{g(x)(x-1)}{(x+1)(x-1)} \\
&= \frac{f(x)(x+1) + g(x)(x-1)}{(x-1)(x+1)} \\
&= \frac{(f(x)+g(x))x + (f(x)-g(x))}{x^2-1}.
\end{align*}

If we compare the nominator $(f(x)+g(x))x + (f(x)-g(x))$ of this result with the original nominator $p(x)=4x+2$ of $r(x)$ we see that we should have that $f(x)+g(x)=4$ and $f(x)-g(x)=2$. Solving this system of equations results in $f(x)=3$ and $g(x)=1$. This means we have found the partial fraction decomposition of $r$:

$$
r(x) = \frac{3}{x-1} + \frac{1}{x+1}.
$$

::::

As you may notice, the degrees of the polynomials $f$ and $g$ in the numerators of the simpler rational functions are less than the degree of the corresponding denominators. This is always the case in partial fraction decomposition, as we always consider proper rational functions in the decomposition.

This can be summarised by the next theorem.

::::{prf:theorem} Partial fraction decomposition with distinct complex linear factors
:label: Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearFactors

Let $r(x) = \frac{p(x)}{q(x)}$ be a proper rational function where the denominator $q$ can be factored into _distinct linear factors_, i.e.

$$
q(x) = a_n(x-b_1)(x-b_2)\cdots(x-b_n),
$$

where $b_1,b_2,\ldots,b_n$ are _distinct_ complex numbers and $a_n$ is the leading coefficient of $q$.

Then there exist constants $A_1,A_2,\ldots,A_n$ such that

$$
r(x) = \frac{A_1}{x-b_1} + \frac{A_2}{x-b_2} + \cdots + \frac{A_n}{x-b_n}.
$$

::::

Note that in the above theorem we considered complex numbers as roots of the denominator polynomial. This is because, by the {prf:ref}`Fundamental Theorem of algebra <Thm:ComplexNumbers:fundamental>`, every polynomial with complex coefficients can be factored into linear factors over the complex numbers. If you did not yet study complex numbers, see {numref}`Ch:ComplexNumbersCartesian`, you can also consider the theorem only for real numbers as roots of the denominator polynomial. In that case the theorem only holds when the denominator can be factored into distinct linear factors over the real numbers.

First we will take a look at an example where we apply the above theorem where all roots are real numbers.

:::::{prf:example}
:label: Ex:RationalFunctions:PartialFractionDecomposition2

Consider the proper rational function

$$
r(x)  = \frac{15x+3}{x^3-2x^2-3x}.
$$

The denominator $q(x)=x^3-2x^2-3x$ of this rational function can be factored as $q(x)=x(x-3)(x+1)$, i.e. as a product of three distinct linear factors, so

$$
r(x) = \frac{15x+3}{x(x-3)(x+1)}.
$$

Based on our previous thinking, let us look for three numbers $A_1$, $A_2$ and $A_3$ such that

$$
r(x) = \frac{A_1}{x} + \frac{A_2}{x-3} + \frac{A_3}{x+1}.
$$

Or by using the formula for $r$, we want to solve the equation

$$
\frac{15x+3}{x(x-3)(x+1)} = \frac{A_1}{x} + \frac{A_2}{x-3} + \frac{A_3}{x+1}
$$

for $A_1$, $A_2$ and $A_3$. Rewriting the right-hand side to a single rational function results in the equation

$$
\frac{15x+3}{x(x-3)(x+1)} = \frac{A_1(x-3)(x+1) + A_2x(x+1) + A_3x(x-3)}{x(x-3)(x+1)}.
$$

By comparing the nominators on both sides we obtain the equation

:::{math}
:label: Eq:RationalFunctions:PartialFractionDecomposition2

15x+3 = A_1(x-3)(x+1) + A_2x(x+1) + A_3x(x-3).
:::

Collecting terms on the right-hand side results in

$$
15x+3 = (A_1 + A_2 + A_3)x^2 + (-2A_1 +A_2-3A_3)x + (-3A_1).
$$

By comparing coefficients we obtain the system of equations

$$
\left\{\begin{array}{lcr}
\phantom{-3}A_1 + A_2 + A_3 &=& 0,\\
 -2A_1 + A_2 - 3A_3 &=& 15, \\
  -3A_1 &=& 3.
\end{array}\right.
$$

This system can be solved to find $A_1=-1$, $A_2=4$ and $A_3=-3$. This means we have found the partial fraction decomposition of $r$:

$$
r(x) = \frac{-1}{x} + \frac{4}{x-3} + \frac{-3}{x+1}.
$$

:::::

::::{prf:remark}
:label: Rmk:RationalFunctions:DistinctLinearFactors

If the denominator of a proper rational function can be factored into distinct linear factors over the real numbers, there is another way to find the constants $A_1,A_2,\ldots,A_n$ in {prf:ref}`Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearFactors`.

Although the zeros of the denominator are not part of the domain of the rational function, the polynomials on the left-hand side and on the right-hand side of the equation as a result of the comparison of nominators (such as Equation {eq}`Eq:RationalFunctions:PartialFractionDecomposition2` in the previous example) should coincide for all values of $x\in\mathbb{R}$. Even for the roots of the denominator. This means that we can find the constants $A_1,A_2,\ldots,A_n$ by substituting the roots of the denominator into this equation.

For the previous example this would yield the following system of equations:

$$
\left\{\begin{array}{rcl}
3 &=& -3A_1,\\
48 &=& 12A_2, \\
-12 &=& 4A_3.
\end{array}\right.
$$

Solving this system again results in $A_1=-1$, $A_2=4$ and $A_3=-3$.

::::

::::{warning}
The method in {prf:ref}`Rmk:RationalFunctions:DistinctLinearFactors` only works when the denominator can be factored into distinct linear factors over the real numbers. In other cases you will have to solve the system of equations obtained by comparing coefficients.
::::

In the next example we will consider a proper rational function where the denominator has complex roots.Feel free to skip this example for now and return to it after studying complex numbers in {numref}`Ch:ComplexNumbersCartesian`.

::::{prf:example} Partial fraction decomposition with complex linear factors
:label: Ex:RationalFunctions:PartialFractionDecomposition3
:class: dropdown

Consider the proper rational function

$$
r(x)  = \frac{5x^2+24x+7}{2x^3+2x^2-2x+30}.
$$

The denominator $q(x)=2x^3+2x^2-2x+30$ has the roots $b_1=-3$, $b_2= 1-2i$ and $b_3=1+2i$. So $r$ can be factored as 

$$
r(x) = \frac{A_1}{x+3} + \frac{A_2}{x-(1-2i)} + \frac{A_3}{x-(1+2i)}.
$$ 

Rewriting the right-hand side to a single rational function and comparing the nominators results in the equation

$$
\frac52x^2+12x+\frac72 = \left(A_1+A_2+A_3\right)x^2 + \left( -2A_1+(2-2i)A_2+(2+2i)A_3\right)x+\left(5A_1+(-3-6i)A_2+( -3+6i)A_3\right).
$$

Comparing coefficients results in a system of equations that has the solution

$$
\left\{\begin{array}{lcr}
A_1 &=& -\frac12,\\
A_2 &=& \frac32+\frac54i, \\
A_3 &=& \frac32-\frac54i,
\end{array}\right.
$$

and the partial fraction decomposition of $r$ with complex numbers is

$$
r(x) = \frac{-\frac12}{x+3} + \frac{\frac32+\frac54i}{x-(1-2i)} + \frac{\frac32-\frac54i}{x-(1+2i)}.
$$


Finding this partial fraction decomposition requires calculations with complex numbers and often leads to errors. To avoid this, it is often better to find a partial fraction decomposition with real coefficients. This can be done by grouping the complex conjugate factors together in the denominator. To see how this works, we first combine the last two terms of the above partial fraction decomposition into a single rational function:

$$
\frac{\frac32+\frac54i}{x-(1-2i)} + \frac{\frac32-\frac54i}{x-(1+2i)} = \frac{3x+2}{(x-1)^2 + 4}.
$$

This means we can also write the partial fraction decomposition of $r$ with real coefficients as

$$
r(x) = \frac{-\frac12}{x+3} + \frac{3x+2}{(x-1)^2 + 4}.
$$

We could have found this decomposition directly by looking for constants $A_1$, $B_1$ and $C_1$ such that

$$
r(x) = \frac{A_1}{x+3} + \frac{B_1x + C_1}{(x-1)^2 + 4}.
$$

We would have know to use this form, if we had known in advance that the original denominator had complex roots that came in a conjugate pairs.

This is summarised in the next definition and theorem.

::::

To avoid using complex numbers in partial fraction decomposition, we introduce the next definition.

::::{prf:definition}
:label: Def:RationalFunctions:IrreducibleQuadratic

A polynomial $p$ of degree two that cannot be factored into linear factors over the real numbers is called an **irreducible quadratic**.

This means that an irreducible quadratic $p$ is a polynomial $p$ that can be written as

$$
p(x) = (x-c)^2+d^2,
$$

with $c$ and $d$ real numbers and $d\neq0$.

::::

::::{prf:theorem} Partial fraction decomposition with distinct real linear factors and distinct irreducible quadratics
:label: Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearAndIrreducibleQuadratic

Let $r(x) = \frac{p(x)}{q(x)}$ be a proper rational function where the denominator $q$ can be factored into $\ell$ _distinct and real linear factors_ and $m$ _distinct irreducible quadratics_, i.e.

$$
q(x) = a_n(x-b_1)(x-b_2)\cdots(x-b_\ell)( (x-c_1)^2 + d_1^2 )( (x-c_2)^2 + d_2^2 ) \cdots ( (x-c_m)^2 + d_m^2 ),
$$

where $b_1,b_2,\ldots,b_\ell$ are _distinct real numbers_, $(c_1,d_1^2),(c_2,d_2^2),\ldots,(c_m,d_m^2)$ are _distinct real number pairs_ with $d_1,d_2,\ldots,d_m\neq0$, and $a_n$ is the leading coefficient of $q$.

Then there exist real constants $A_1,A_2,\ldots,A_\ell$, $B_1,\ldots,B_m$ and $C_1,\ldots,C_m$ such that

$$
r(x)= \frac{A_1}{x-b_1} + \frac{A_2}{x-b_2} + \cdots + \frac{A_\ell}{x-b_\ell} + \frac{B_1x + C_1}{(x-c_1)^2 + d_1^2} + \cdots + \frac{B_mx + C_m}{(x-c_m)^2 + d_m^2}.
$$

::::

::::{prf:example}
:label: Ex:RationalFunctions:PartialFractionDecomposition4

Consider the proper rational function

$$
r(x)  = \frac{5x^2+24x+7}{2x^3+2x^2-2x+30}.
$$

The denominator $q(x)=2x^3+2x^2-2x+30$ can be factorised as

$$
q(x) = 2(x+3)\left( (x-1)^2 + 4\right).
$$

An partial fraction decomposition of $r$ is therefore of the form

$$
r(x) = \frac{A_1}{x+3} + \frac{B_1x + C_1}{(x-1)^2 + 4}.
$$ 

Rewriting the right-hand side to a single rational function and comparing the nominators results in the equation

$$
\frac52x^2+12x+\frac72 = \left(A_1+B_1\right)x^2 + \left( -2A_1+3B_1+C_1\right)x+\left(5A_1+3C_1\right).
$$

Comparing coefficients results in a system of equations that has the solution

$$
\left\{\begin{array}{lcr}
A_1 &=& -\frac12,\\
B_1 &=& 3, \\
C_1 &=& 2,
\end{array}\right.
$$

and the partial fraction decomposition of $r$ using only real coefficients is

$$
r(x) = \frac{-\frac12}{x+3} + \frac{3x + 2}{(x-1)^2 + 4}.
$$

::::

In all of the above examples we have only considered the case where the denominator can be factored into distinct linear factors and distinct irreducible quadratics. If the denominator has repeated factors and/or repeated quadratics, the partial fraction decomposition becomes slightly more complicated.

Consider the proper rational function

$$
r(x)  = \frac{2x^2+6x+5}{(x+1)^2(x+2)}.
$$

The denominator $q(x)=(x+1)^2(x+2)$ of this rational function has a repeated linear factor $(x+1)$. If we would try to apply the previous theorems directly, we would look for constants $A$ and $B$ such that

$$
r(x) = \frac{A}{x+1} + \frac{B}{x+2}.
$$

If we would rewrite the right-hand side to a single rational function, we obtain

$$
r(x) = \frac{A(x+2) + B(x+1)}{(x+1)(x+2)} = \frac{(A+B)x + (2A+B)}{(x+1)(x+2)}.
$$

The denominator of this expression is not equal to the original denominator of the rational function $r$, so we cannot compare the nominators directly. If we multiply both the denominator and the numerator of the last expression with $x+1$, we obtain

$$
r(x) = \frac{((A+B)x + (2A+B))(x+1)}{(x+1)^2(x+2)} = \frac{(A+B)x^2 + (3A+2B)x + 2A+B}{(x+1)^2(x+2)}.
$$

Now the denominator is equal to the original denominator of $r$ and we can compare the nominators. This results in the system of equations

$$
\left\{\begin{array}{lcr}
A+B &=& 2, \\
3A+2B &=& 6, \\
2A+B &=& 5.
\end{array}\right.
$$

Unluckily this system has no solutions, so our initial assumption about the form of the partial fraction decomposition was incorrect.

If we look at the last system, we see that we have three equations for only two unknowns. This is because we did not take into account that the factor $(x+1)$ in the denominator is repeated, which is also evident from the fact that we had to multiply the numerator and denominator by $x+1$ to be able to compare nominators.

If we would just consider the factor $(x+1)^2$ in the denominator, we would also arrive at an inconsistent linear system in two variables. However, if we would consider both factors $(x+1)$ and $(x+1)^2$ in the denominator separately, we would have three unknowns instead of two. This is similar to how we handled irreducible quadratics in the previous theorem: there we had a linear and a constant term in the numerator for each irreducible quadratic factor in the denominator. We will do something similar here. We do have to also consider cases where a factor is repeated more than two times, but the idea is the same.

It could also be the case that an irreducible quadratic is repeated in the denominator. In that case we will also have to consider multiple terms in the partial fraction decomposition for that irreducible quadratic. The next theorem summarises all of this.

::::{prf:theorem} Partial fraction decomposition with repeated real linear factors and repeated irreducible quadratics
:label: Thm:RationalFunctions:RepeatedLinearAndIrreducibleQuadratic

Let $r(x) = \frac{p(x)}{q(x)}$ be a proper rational function where the denominator $q$ can be factored into $\ell$ _real linear factors_ and $m$ _irreducible quadratics_, i.e.

$$
\begin{split}
q(x) &= a_n(x-b_1)^{m_1}(x-b_2)^{m_2}\cdots(x-b_\ell)^{m_\ell}\\
& \qquad ( (x-c_1)^2 + d_1^2 )^{n_1}( (x-c_2)^2 + d_2^2 )^{n_2} \cdots ( (x-c_m)^2 + d_m^2 )^{n_m},
\end{split}
$$

where $b_1,b_2,\ldots,b_\ell$ are _distinct real numbers_, $s_1,s_2,\ldots,s_\ell$ are positive integers, $(c_1,d_1^2),(c_2,d_2^2),\ldots,(c_m,d_m^2)$ are _distinct real number pairs_ with $d_1,d_2,\ldots,d_m\neq0$, $t_1,t_2,\ldots,t_m$ are positive integers, and $a_n$ is the leading coefficient of $q$.

Then there exist constants $A_{k,j}$, $1\leq j \leq s_k$ for $1\leq k \leq \ell$, and constants $B_{h,j}$ and $C_{h,j}$, $1\leq j \leq t_h$, for $1\leq h \leq m$ such that

$$
r(x)= L_1(x)+L_2(x)+\cdots+L_\ell(x) + Q_1(x) + Q_2(x) + \cdots + Q_m(x),
$$


where for $1\leq k \leq \ell$, $s_k$ is the multiplicity of the linear factor $(x-b_k)$ in the factorisation of $q$ and

$$
L_k(x) = \frac{A_{k,1}}{x-b_k} + \frac{A_{k,2}}{(x-b_k)^2} + \cdots + \frac{A_{k,s_k}}{(x-b_k)^{s_k}}.
$$

Similarly, for $1\leq h \leq m$, $t_h$ is the multiplicity of the irreducible quadratic factor $((x-c_h)^2 + d_h^2)$ in the factorisation of $q$ and

$$
Q_h(x) = \frac{B_{h,1}x + C_{h,1}}{(x-c_h)^2 + d_h^2} + \frac{B_{h,2}x + C_{h,2}}{((x-c_h)^2 + d_h^2)^2} + \cdots + \frac{B_{h,t_h}x + C_{h,t_h}}{((x-c_h)^2 + d_h^2)^{t_h}}.
$$

::::

::::{prf:remark}
:label: Rmk:RationalFunctions:RepeatedLinearAndIrreducibleQuadratic

Because of the generality of {prf:ref}`Thm:RationalFunctions:RepeatedLinearAndIrreducibleQuadratic`, we used constants with multi-level indexing. In practice it is often easier to use different letters for the constants in the numerators of the various terms in the partial fraction decomposition, as we will do in the next example.
::::

::::{prf:example}
:label: Ex:RationalFunctions:PartialFractionDecomposition5

For the proper rational function

$$
R(x)  = \frac{2x^2+6x+5}{(x+1)^2(x+2)},
$$

we now try the following form for the partial fraction decomposition:

$$
R(x) = \frac{A}{x+1} + \frac{B}{(x+1)^2} + \frac{C}{x+2}.
$$

Rewriting the right-hand side to a single rational function and comparing the nominators results in the system of equations

$$
\left\{\begin{array}{lcr}
A+C&=&2, \\
3A+B+2C &=& 6, \\
2A+2B+C &=& 5.
\end{array}\right.
$$

This system has a solution (luckily), which is $A=1$, $B=1$ and $C=1$. This means we have found the partial fraction decomposition of $R$:

$$
R(x) = \frac{1}{x+1} + \frac{1}{(x+1)^2} + \frac{1}{x+2}.
$$

::::

We end this section, before going to the {ref}`Sec:RationalFunctions:GraspleExercises`, with an example that contains everything we have learned so far.

::::{prf:example}
:label: Ex:RationalFunctions:PartialFractionDecomposition6

Consider the proper rational function

$$
R(x)  = \frac{84 + 196 x + 282 x^2 + 230 x^3 + 104 x^4 + 22 x^5 - 9 x^6 - 7 x^7 - 2 x^8)}{(-1 + x) (2 + x)^2 (x^2+3) (2 + 2 x + x^2)^2}
$$

The denominator $Q(x)=(-1 + x) (2 + x)^2 (x^2+3) (2 + 2 x + x^2)^2$ of this rational function has a distinct linear factor $(-1 + x)$, a repeated linear factor $(2 + x)$ with multiplicity $2$, a distinct irreducible quadratic factor $(x^2+3)$ and a repeated irreducible quadratic factor $(2 + 2 x + x^2)$ with multiplicity $2$.

Based on {prf:ref}`Thm:RationalFunctions:RepeatedLinearAndIrreducibleQuadratic`, we try the following form for the partial fraction decomposition:

$$
R(x) = \frac{A}{x-1}+\frac{B}{x+2}+\frac{C}{(x+2)^2}+\frac{Dx + E}{x^2+3}+\frac{Fx + G}{(2 + 2 x + x^2)^2}+\frac{Hx + I}{2 + 2 x + x^2}.
$$

Rewriting the right-hand side to a single rational function and comparing the nominators results in a system of equations with 9 unknowns and 9 equations. Solving such a system can be quite tedious (but can be done!), so we used a computer algebra system to find the solution and substituted the values back into the partial fraction decomposition. The result is:

$$
R(x) = \frac{1}{x-1}+\frac{-2}{x+2}+\frac{3}{(x+2)^2}+\frac{-x}{x^2+3}+\frac{-1}{(x+1)^2+1}+\frac{2x}{((x+1)^2+1)^2}
$$

::::

(Sec:RationalFunctions:GraspleExercises)=
## Grasple exercises