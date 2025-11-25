```{admonition} Attribution
:class: attribution
This page reuses content from {cite:t}`dekleijn2025longdivision`.
```

# Rational functions

## Introduction

Rational functions are functions that are formed by the ratio of two polynomials. They are widely used in various fields of mathematics, including calculus, algebra, and real analysis. Rational functions can exhibit interesting behaviors, such as asymptotes and discontinuities, which are treated in sections further on in this chapter.

We start of with some definitions:

::::{prf:definition}
:label: Def:RationalFunctions:Def

A **rational function** $r$ is a function that can be expressed as the ratio of two polynomials:

$$
r(x) = \frac{p(x)}{q(x)},
$$

where $p(x)$ and $q(x)$ are polynomials and $q(x) \neq 0$.

A **proper rational function** is a rational function where the degree of the numerator polynomial $p(x)$ is less than the degree of the denominator polynomial $q(x)$.

An **improper rational function** is a rational function where the degree of the numerator polynomial $p(x)$ is greater than or equal to the degree of the denominator polynomial $q(x)$.

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

The domain of a rational function is all real numbers except where the denominator is zero, or in other words, the function is undefined where $q(x) = 0$.

First we will look at how to simplify rational functions by applying polynomial division. After that we will look at how to decompose proper rational functions into simpler fractions using partial fraction decomposition.

## Polynomial division

When dealing with rational functions where the degree of the numerator is greater than or equal to the degree of the denominator, it is often useful to perform polynomial long division. This allows us to express the rational function as a sum of a polynomial and a proper rational function.

In the method of long division of polynomials we consider quotients of polynomials $p(x)$ and $q(x)$, i.e. $\frac{p(x)}{q(x)}$. When the degree of $p(x)$ is higher than the degree of $q(x)$ it is possible that $p(x) = b(x)q(x)$ for $b(x)$ another polynomial. In this case the long division terminates at $0$. It is also possible that the long division terminates at a polynomial $r(x)$ that whose degree is lower than $q(x)$. In that case $p(x) = r(x) + b(x)q(x)$ for some polynomial $b(x)$. 

The method works by starting with the highest power of $x$. We consider a monomial $a_1x^{k_1}$  such that the highest powers of $a_1x^{k_1}q(x)$ and $p(x)$ match. Then we consider $p_1(x)=p(x)-a_1x^{k_1}q(x)$ whose degree must be lower than the degree of $p(x)$. If it is also lower than the degree of $q(x)$ the long division terminates. Otherwise we continue by repeating the first step again, but now with respect to the polynomial $p_1(x)$ instead of $p(x)$.

Below are two examples, one for factoring out a linear factor of which we know that it is a linear factor (so the method is guaranteed to terminate at $0$) and one where we are writing a rational functions as the sum of a polynomial plus a proper rational function. A proper rational function is a quotient of polynomials such that the degree of the denominator is higher than the degree of the numerator. In this case the long division does not terminate at $0$.

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
R(x)  = \frac{P(x)}{Q(x)} = \frac{4x+2}{x^2-1}.
$$

The denominator $Q(x)=x^2-1$ of this rational function can be factored as $Q(x)=(x-1)(x+1)$, i.e. as a product of distinct linear factors. So, based on our previous thinking, let us look for two polynomials $f(x)$ and $g(x)$ such that

:::{math}
:label: Eq:RationalFunctions:PartialFractionDecomposition1
R(x) = \frac{f(x)}{x-1} + \frac{g(x)}{x+1}
:::

holds. Since $R$ remains the same proper rational function, the ratio between the degrees of the nominator $P(x)=4x+2$ and the denominator $Q(x)=x^2-1$ should also not change. We start by taking the right-hand side of Equation {eq}`Eq:RationalFunctions:PartialFractionDecomposition1` and rewriting it to a single rational function:

\begin{align*}
\frac{f(x)}{x-1} + \frac{g(x)}{x+1} &= \frac{f(x)(x+1)}{(x-1)(x+1)} + \frac{g(x)(x-1)}{(x+1)(x-1)} \\
&= \frac{f(x)(x+1) + g(x)(x-1)}{(x-1)(x+1)} \\
&= \frac{(f(x)+g(x))x + (f(x)-g(x))}{x^2-1}.
\end{align*}

If we compare the nominator $(f(x)+g(x))x + (f(x)-g(x))$ of this result with the original nominator $P(x)=4x+2$ of $R(x)$ we see that we should have that $f(x)+g(x)=4$ and $f(x)-g(x)=2$. Solving this system of equations results in $f(x)=3$ and $g(x)=1$. This means we have found the partial fraction decomposition of $R(x)$:

$$
R(x) = \frac{3}{x-1} + \frac{1}{x+1}.
$$

::::

As you may notice, the degrees of the polynomials $f(x)$ and $g(x)$ in the numerators of the simpler rational functions are less than the degree of the corresponding denominators. This is always the case in partial fraction decomposition, as we always consider proper rational functions in the decomposition.

This can be summarised by the next theorem.

::::{prf:theorem}
:label: Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearFactors

Let $R(x) = \frac{P(x)}{Q(x)}$ be a proper rational function where the denominator $Q(x)$ can be factored into _distinct linear factors_, i.e.

$$
Q(x) = a_n(x-b_1)(x-b_2)\cdots(x-b_n),
$$

where $b_1,b_2,\ldots,b_n$ are _distinct_ complex numbers and $a_n$ is the leading coefficient of $Q(x)$.

Then there exist constants $A_1,A_2,\ldots,A_n$ such that

$$
R(x) = a_n\left(\frac{A_1}{x-b_1} + \frac{A_2}{x-b_2} + \cdots + \frac{A_n}{x-b_n}\right).
$$

::::

Note that in the above theorem we considered complex numbers as roots of the denominator polynomial. This is because, by the {prf:ref}`Fundamental Theorem of algebra <Thm:ComplexNumbers:fundamental>`, every polynomial with complex coefficients can be factored into linear factors over the complex numbers.

First we will take a look at an example where we apply the above theorem where all roots are real numbers. Next we will consider an example where some of the roots are complex numbers, but luckily come in a conjugate pair.

:::::{prf:example}
:label: Ex:RationalFunctions:PartialFractionDecomposition2

Consider the proper rational function

$$
R(x)  = \frac{15x+3}{x^3-2x^2-3x}.
$$

The denominator $Q(x)=x^3-2x^2-3x$ of this rational function can be factored as $Q(x)=x(x-3)(x+1)$, i.e. as a product of three distinct linear factors, so

$$
R(x) = \frac{15x+3}{x(x-3)(x+1)}.
$$

Based on our previous thinking, let us look for three numbers $A_1$, $A_2$ and $A_3$ such that

$$
R(x) = \frac{A_1}{x} + \frac{A_2}{x-3} + \frac{A_3}{x+1}.
$$

Or by using the formula for $R(x)$, we want to solve the equation

$$
\frac{15x+3}{x(x-3)(x+1)} = \frac{A_1}{x} + \frac{A_2}{x-3} + \frac{A_3}{x+1}
$$

for $A_1$, $A_2$ and $A_3$. Rewriting the right-hand side to a single rational function results in the equation

$$
\frac{15x+3}{x(x-3)(x+1)} = \frac{A_1(x-3)(x+1) + A_2x(x+1) + A_3x(x-3)}{x(x-3)(x+1)}.
$$

::::