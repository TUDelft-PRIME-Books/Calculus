```{admonition} Attribution
:class: attribution
This page reuses content from {cite:t}`dekleijn2025longdivision`.
```

# Rational functions

In this section we cover

- Rational functions
- Asymptotes
- Partial fraction decomposition (using complex numbers)

## Introduction

Rational functions are functions that are formed by the ratio of two polynomials. They are widely used in various fields of mathematics, including calculus, algebra, and real analysis. Rational functions can exhibit interesting behaviors, such as asymptotes and discontinuities.

We start of with some definitions:

::::{prf:definition}
:label: Def:RationalFunctions:Def

A **rational function** $r$ is a function that can be expressed as the ratio of two polynomials:

$$
r(x) = \frac{p(x)}{q(x)},
$$

where $p(x)$ and $q(x)$ are polynomials and $q(x) \neq 0$.

A **proper rational function** is a rational function where the degree of the numerator polynomial $p(x)$ is less than the degree of the denominator polynomial $q(x)$.

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
$$
r_2(x) = 2x^2+1 + \frac{-x^2+4x-2}{x^3-2x+1} = \frac{(2x^2+1)(x^3-2x+1) + (-x^2+4x-2)}{x^3-2x+1} = \frac{2x^5-3x^3+x^2+2x-1}{x^3-2x+1}.
$$

$r_2$ is again not a proper rational function since the degree of the numerator ($5$) is greater than the degree of the denominator ($3$).

$r_3$ is a proper rational function since the degree of the numerator ($2$) is less than the degree of the denominator ($3$) and is already expressed as a ratio of two polynomials.

::::

The domain of a rational function is all real numbers except where the denominator is zero, or in other words, the function is undefined where $q(x) = 0$. Before we move on to asymptotes, we will look at how to simplify rational functions by applying polynomial division.

## Polynomial division

When dealing with rational functions where the degree of the numerator is greater than or equal to the degree of the denominator, it is often useful to perform polynomial long division. This allows us to express the rational function as a sum of a polynomial and a proper rational function.

In the method of long division of polynomials we consider quotients of polynomials $p(x)$ and $q(x)$, i.e. $\frac{p(x)}{q(x)}$. When the degree of $p(x)$ is higher than the degree of $q(x)$ it is possible that $p(x) = b(x)q(x)$ for $b(x)$ another polynomial. In this case the long division terminates at $0$. It is also possible that the long division terminates at a polynomial $r(x)$ that whose degree is lower than $q(x)$. In that case $p(x) = r(x) + b(x)q(x)$ for some polynomial $b(x)$. 

The method works by starting with the highest power of $x$. We consider a monomial $a_1x^{k_1}$  such that the highest powers of $a_1x^{k_1}q(x)$ and $p(x)$ match. Then we consider $p_1(x)=p(x)-a_1x^{k_1}q(x)$ whose degree must be lower than the degree of $p(x)$. If it is also lower than the degree of $q(x)$ the long division terminates. Otherwise we continue by repeating the first step again, but now with respect to the polynomial $p_1(x)$ instead of $p(x)$.

Below are two examples, one for factoring out a linear factor of which we know that it is a linear factor (so the method is guaranteed to terminate at $0$) and one where we are writing a rational functions as the sum of a polynomial plus a proper rational function. A proper rational function is a quotient of polynomials such that the degree of the denominator is higher than the degree of the numerator. In this case the long division does not terminate at $0$.

::::{prf:example}
:label: Ex:RationalFunctions:PolynomialDivision1

In order to compute the limit

$$
\lim_{x\to 2} \frac{x^4-4x^3+3x^2+4x-4}{x^3-x^2-8x}
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

We will revisit the limit at the beginning of this example further on in this section.

::::