::::{admonition} Attribution
:class: attribution
This page reuses content from {cite:t}`dekleijn2025longdivision`.
::::

(Sec:RationalFunctions)=
# Rational functions

## Introduction

Rational functions are functions that are defined by the ratio of two polynomials. They are widely used in various fields of mathematics, including calculus, algebra, and real analysis. Rational functions can exhibit interesting behaviours, such as asymptotes and discontinuities, which are treated in sections further on in this chapter.

We start with some definitions:

::::{prf:definition}
:label: Def:RationalFunctions:Def

A **rational function** $f$ is a function that can be expressed as the ratio of two polynomials:

$$
f(x) = \frac{p(x)}{q(x)},
$$

where $p$ and $q$ are polynomials and $q\neq 0$[^notzero].

[^notzero]: The condition $q \neq 0$ means that the function value $q(x)$ is not equal to zero (function) for all $x\in\mathbb{R}$. It is not allowed that $q$ attains the value $0$ at some points in it's domain, as long as it is not zero everywhere.

A **proper rational function** is a rational function where the degree of the numerator polynomial $p$ is less than the degree of the denominator polynomial $q$.

An **improper rational function** is a rational function where the degree of the numerator polynomial $p$ is greater than or equal to the degree of the denominator polynomial $q$.

::::

::::{prf:example}
:label: Ex:RationalFunctions:Examples

Consider the following four functions:

\begin{align*}
f_1(x) &= \frac{x^4-4x^3+3x^2+4x-4}{x^3-x^2-8x}, \\
f_2(x) &= 2x^2+1 + \frac{-x^2+4x-2}{x^3-2x+1},
\\
f_3(x) &= \frac{-x^2+4x-2}{x^3-2x+1}, \\
f_4(x) &= \frac{x+\sqrt{x}+3}{x^2-5}.
\end{align*}

The function $f_1$ is a rational function, as can be seen directly from its definition as a ratio of two polynomials, but it is not a proper rational function since the degree of the numerator ($4$) is greater than the degree of the denominator ($3$).

The function $f_2$ is also a rational function. This can be seen by rewriting it to a single fraction:

\begin{align*}
f_2(x) &= 2x^2+1 + \frac{-x^2+4x-2}{x^3-2x+1} \\
&= \frac{(2x^2+1)(x^3-2x+1) + (-x^2+4x-2)}{x^3-2x+1} \\
&= \frac{2x^5-3x^3+x^2+2x-1}{x^3-2x+1}.
\end{align*}

$f_2$ is again not a proper rational function since the degree of the numerator ($5$) is greater than the degree of the denominator ($3$).

$f_3$ is a proper rational function since the degree of the numerator ($2$) is less than the degree of the denominator ($3$) and is already expressed as a ratio of two polynomials.

$f_4$ is not a rational function since the numerator is not a polynomial. The numerator contains the term $x+\sqrt{x}+3$ which is not a polynomial term since it contains a non-integer power of $x$.

::::

:::{prf:remark}
:label: Rmk:RationalFunctions:Domain
The domain of a rational function is the set of all real numbers except those for which the denominator is zero In other words, the rational function $\frac{p(x)}{q(x)}$ is undefined where $q(x) = 0$.

The co-domain of a rational function is the set of all real numbers. The range of the rational function is the set of all real numbers that are actually attained by the function, i.e. the set of all $y\in\mathbb{R}$ such that there exists an $x\in\mathbb{R}$ with $f(x)=y$.

The range can be the entire set of real numbers, but it can also be a proper subset of the real numbers. 
:::

::::{prf:example}
:label: Ex:RationalFunctions:DomainAndRange1

For instance, the rational function $f(x)=\frac{1}{x^2+1}$ has domain $\mathbb{R}$ since the denominator $x^2+1$ is never zero for any real number $x$.

The range of this function is the range $(0,1]$ since $f(x)$ is always positive and attains it's maximum value $1$ at $x=0$.

{numref}`Fig:RationalFunctions:DomainAndRange1` shows the graph of this function.

:::{applet}
:url: calculus/rational_functions/witch_of_Agnesi
:name: Fig:RationalFunctions:DomainAndRange1
:class: dark-light

The function $f(x)=\frac{1}{x^2+1}$ has domain $\mathbb{R}$ and range $(0,1]$.
:::

This curve has many names, but it sometimes called the _Witch of Agnesi_, named after [Maria Gaetana Agnesi](https://en.wikipedia.org/wiki/Maria_Gaetana_Agnesi).

::::

::::{prf:example}
:label: Ex:RationalFunctions:DomainAndRange2

It is also possible that the range of a rational function is all real numbers except for a single value. For instance, the rational function $f(x)=\frac{1}{x}$ has range $\mathbb{R}\setminus\{0\}$ since $f(x)$ can be any real number except $0$.

{numref}`Fig:RationalFunctions:DomainAndRange2` shows the graph of this function.

:::{applet}
:url: calculus/rational_functions/reciprocal_function
:name: Fig:RationalFunctions:DomainAndRange2
:class: dark-light

The function $f(x)=\frac{1}{x}$ has domain $\mathbb{R}\setminus\{0\}$ and range $\mathbb{R}\setminus\{0\}$.
:::

::::

::::{prf:example}
:label: Ex:RationalFunctions:DomainAndRange3

Consider the rational function $f(x)=\frac{2x^2+7x-15}{2x^2-x-3}$.

The domain of this function is $\mathbb{R}\setminus\{-1, -\frac{3}{2}\}$ since the denominator is zero at $x=-1$ and $x=-\frac{3}{2}$ and so the function is undefined at these points.

The range of this function is $\mathbb{R}\setminus\{1\}$ since $f(x)$ can be any real number except $1$.

{numref}`Fig:RationalFunctions:DomainAndRange3` shows the graph of this function.

:::{applet}
:url: calculus/rational_functions/a_rational_function
:name: Fig:RationalFunctions:DomainAndRange3
:class: dark-light

The function $f(x)=\frac{2x^2+7x-15}{2x^2-x-3}$ has domain $\mathbb{R}\setminus\{-1, -\frac{3}{2}\}$ and range $\mathbb{R}\setminus\{1,\frac{13}{5}\}$.
:::

Note that the graph has a vertical asymptote at $x=-1$ and a perforation at $(x,y)=\left(-\frac{3}{2}, \frac{13}{5}\right)$, which are the points where the function is undefined. The graph also has a horizontal asymptote at $y=1$ which is the value that the function approaches as $x$ goes to positive or negative infinity. The function never attains the value $1$, which is why the range does not include $1$.

::::


In the coming subsections we will first look at how to simplify rational functions by applying polynomial division. After that we will look at how to decompose proper rational functions into simpler fractions using partial fraction decomposition.

(Subsec:RationalFunctions:PolynomialDivision)=

## Polynomial division

When dealing with *improper* rational functions, it is often useful to express the rational function as a sum of a polynomial and a proper rational function. To do so, we perform polynomial long division[^othersection].

[^othersection]: The method of long division of polynomials has been very briefly treated in {prf:ref}`Ex:ComplexNumbers:longdivisionpoly`.

In the method of long division of polynomials we consider quotients of polynomials $p$ and $q$, i.e. $\frac{p(x)}{q(x)}$. When the degree of $p$ is higher than the degree of $q$ it is possible that $p(x) = s(x)q(x)$ for another polynomial $s$. It is also possible that $p(x) = r(x) + s(x)q(x)$ for some polynomials $s$ and $r$.

The method works by starting with the highest power of $x$. We consider a monomial $a_1x^{k_1}$  such that the term with the highest power of $a_1x^{k_1}q(x)$ matches the term with the highest power of $p(x)$. Then we consider $p_1(x)=p(x)-a_1x^{k_1}q(x)$ which has lower degree than  $p$. If the degree of $p_1$ is lower than the degree of $q$ the long division stops. Otherwise we repeat the first step again, but now with respect to the polynomial $p_1$ instead of $p$. We continue this procedure until we have a polynomial $p_n$ whose degree is lower than the degree of $q$. This means that we have found polynomials $s$ and $r$ such that $p(x) = r(x) + s(x)q(x)$, where $s(x)=a_1x^{k_1}+a_2x^{k_2}+\cdots + a_nx^{k_n}$.

This is summarised in the next algorithm.

::::{prf:algorithm}
:label: Alg:RationalFunctions:PolynomialDivision
Assume  $p$ and $q$ are polynomials where the degree of $p$ is greater than or equal to the degree of $q$.

Define $p_0(x)=p(x)$, $s(x)=0$ and $n=0$.

For $n=0,1,2,\ldots$ do the following:

1. Consider a monomial $a_nx^{k_n}$ such that the term with the highest power of $a_nx^{k_n}q(x)$ matches the term with the highest power of $p_n(x)$.

2. Define $p_{n+1}(x)=p_n(x)-a_nx^{k_n}q(x)$ and $s(x)=s(x)+a_nx^{k_n}$.

3. If the degree of $p_{n+1}$ is lower than the degree of $q$, then stop and define $r(x)=p_{n+1}(x)$.

4. Otherwise, continue with the next iteration of the loop.

::::

Below are two examples, one for factoring out a linear factor of which we know that it is a divisor and one where we are writing a rational functions as the sum of a polynomial plus a proper rational function.

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

Now we consider by what monomial $ax^n$ we should multiply the polynomial on the left in order to match the highest order term of the polynomial in the middle. In this case we find it should be $x^3$. We multiply $x^3$ by $x-2$ and subtract the obtained polynomial from the polynomial in the middle as indicated. We write the monomial we had to multiply with on the right:

$$
\begin{array}{rclcl}
x-2 & \Big/ & x^4-4x^3+3x^2+4x-4 & \Big\backslash & x^3 \\
    &       & x^4-2x^3           &        &     \\
&          & \overline{\phantom{x^4}-2x^3+3x^2+4x-4} & \overline{\phantom{x^4}} & \\
\end{array}
$$

Now we repeat this step with the same polynomial on the left, but the new polynomial in the middle. For this second step we find that we should multiply by $-2x^2$.

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

We repeat one more time and this time we find $+2$:

$$
\begin{array}{rclcl}
x-2 & \Big/ & x^4-4x^3+3x^2+4x-4 & \Big\backslash & x^3-2x^2-x+2 \\
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

Note that the result of subtracting is now of lower degree then the polynomial on the left. This means our long division is done.

Since our long division terminates at $0$ this means that the polynomial on the left is indeed a factor for the polynomial in the middle. The polynomial in the middle factors as a product of the left and polynomials on the right, i.e. 

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

Not all long divisions will terminate at $0$, as in general, rational functions are, on their domain, not actually equal to polynomials and so long division will terminate at some non-zero remainder.

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

This time the first monomial on the right should be $\frac{1}{2}x$. 

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

This means that the polynomial in the middle divided by the polynomial on the left is equal to the polynomial on the right plus the remainder (on the bottom) divided by the polynomial on the left, i.e.

$$
\frac{\frac{1}{2}x^3+x^2-\frac{23}{2}x-24}{x^2-25} = \frac{1}{2}x+1 + \frac{x+1}{x^2-25}.
$$

::::

In the next example, we will only present you with the final result of the long division. Try find the same result yourself by applying the method of long division as described in the previous example.

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

This means that the polynomial in the middle divided by the polynomial on the left is equal to  the polynomial on the right plus the remainder (on the bottom) divided by the polynomial on the left, i.e. 

$$\frac{2x^5-3x^3+x^2+2x-1}{x^3-2x+1} = 2x^2+1 + \frac{-x^2+4x-2}{x^3-2x+1}.$$

::::

We end this section with the general result of polynomial long division in the next theorem.

::::{prf:theorem}
:label: Thm:RationalFunctions:PolynomialLongDivision

Let $f(x) = \frac{p(x)}{q(x)}$ be a rational function where the numerator $p$ has degree $P$ and the denominator $q$ has degree $Q$. Then there exist a polynomial $s$ of degree $S=P-Q$ and a polynomial $r$ of degree $R<Q$ such that

$$
f(x) = s(x) + \frac{r(x)}{q(x)}.
$$

::::

::::{admonition} Proof of Theorem {prf:ref}`Thm:RationalFunctions:PolynomialLongDivision`
:class: tudproof, dropdown

Consider {prf:ref}`Alg:RationalFunctions:PolynomialDivision`. If we can prove that the algorithm terminates, then we have found the polynomials $s$ and $r$ such that $p(x) = r(x) + s(x)q(x)$. If we then also can deduce that the degrees are as required, the proof is complete.

If $P<Q$ then we can simply define $s(x)=0$ and $r(x)=p(x)$ and we are done.

In the remainder of this proof we will assume that $P\geq Q$.

In step 1 and 2 of the algorithm the degree of $p_{n+1}$ is strictly lower than the degree of $p_n$ since we are subtracting a monomial $a_nx^{k_n}q(x)$ from $p_n$ where the term with the highest power of $a_nx^{k_n}q(x)$ matches the term with the highest power of $p_n$.

This means that the degree of $p_{n+1}$ is at least one less than the degree of $p_n$. Since the degree of $p_0$ is $P$, this means that after at most $P-Q$ iterations we have a polynomial whose degree is lower than the degree of $q$. This means that the algorithm terminates and we have found polynomials $s$ and $r$ such that $p(x) = r(x) + s(x)q(x)$.

The degree of the polynomial $s$ is $S=P-Q$ since in each iteration we are adding a monomial $a_nx^{k_n}$ to $s$ where the term with the highest power of $a_nx^{k_n}q(x)$ matches the term with the highest power of $p_n$. Since the degree of $p_0$ is $P$, this means that the degree of the first monomial we add to $s$ is $P-Q$. Since in each iteration we are adding a monomial of lower degree, this means that the degree of $s$ is indeed $S=P-Q$.

The degree of the polynomial $r$ is $R<Q$ since the algorithm terminates when we have a polynomial $p_{n+1}$ whose degree is lower than the degree of $q$. Since we define $r(x)=p_{n+1}(x)$, this means that the degree of $r$ is indeed $R<Q$.

::::


::::{question} Multiple-choice Multiple-select
:type: multiple-choice
:variant: multiple-select
:admonition:
:class: question

When applying polynomial long division to divide a polynomial $p$ by a second degree polynomial $q$, what can the remainder $r$ be?

Pick all correct options, then press _Submit answer(s)_.

---
[ ] A second degree polynomial.
> If $q$ is a second degree polynomial, then the degree of the remainder $r$ will be less than $2$. So $r$ can be a first degree polynomial, a non-zero constant or zero, but it cannot be a second degree polynomial.
[x] A first degree polynomial.
> That is correct! The degree of the remainder $r$ will be less than the degree of $q$. Since $q$ is a second degree polynomial, the degree of $r$ must be less than $2$, so it can be a first degree polynomial.
[x] A non-zero constant.
> That is correct! The degree of the remainder $r$ will be less than the degree of $q$. Since $q$ is a second degree polynomial, the degree of $r$ must be less than $2$, so it can be a non-zero constant.
[x] Zero.
> That is correct! The degree of the remainder $r$ will be less than the degree of $q$. Since $q$ is a second degree polynomial, the degree of $r$ must be less than $2$, so it can be zero. In this case, the original polynomial $p$ is a multiple of $q$ and the rational function $\frac{p(x)}{q(x)}$ can be simplified to a polynomial (on the domain where $q(x) \neq 0$).
---

::::

::::{prf:example-start}
:label: Ex:RationalFunctions:LongDivisionCode

Performing long division of polynomials can be a bit tedious, especially when the polynomials are of high degree. Fortunately, there are computer algebra systems that can perform long division for us. Below is an example of how to perform long division of polynomials using the Python. In this example we will perform long division to rewrite the rational function

$$
f(x) = \frac{x^{8} + 2 x^{7} - x^{5} + 4 x^{4} - 3 x^{2} + 10}{x^{3} - 2 x + 1}.
$$

::::


:::{code-cell} ipython3
---
tags: [auto-execute-page]
---
# Import a symbolic mathematics library
import sympy as sp
# import a function to display the result in LaTeX format
from IPython.display import Latex
# Define the variable and the constants
x = sp.symbols('x')
# define the parts of the rational function 
p = (x**8+2*x**7-x**5+4*x**4-3*x**2+10)
q = (x**3-2*x+1)

# perform the long division of the numerator by the denominator
s , r = sp.div(p, q, domain='QQ')

# Display the result
display(Latex("The long division of"))
display(Latex("$$p(x) = "+sp.latex(p)+"$$"))
display(Latex("by"))
display(Latex("$$q(x) = "+sp.latex(q)+"$$"))
display(Latex("gives quotient"))
display(Latex("$$s(x) = "+sp.latex(s)+"$$"))
display(Latex("and remainder"))
display(Latex("$$r(x) = "+sp.latex(r)+".$$"))
display(Latex("""This means that the original rational function $f$
 can be rewritten as"""))
display(Latex("$$f(x) = "+sp.latex(s)+" + \\frac{"+sp.latex(r)+"}{"
    +sp.latex(q)+"}.$$"))
display(Latex("""The entire long division is:"""))
display_string = ["$$",r"\begin{array}{rcrcl}"]
first_line = sp.latex(q)
first_line += r" & \Big/ & "
first_line += sp.latex(p)
first_line += r" & \Big\backslash & "
first_line += sp.latex(s)
first_line += r"\\"
display_string.append(first_line)
# Split in the separate monomials of s
s_monomials = sp.Poly(s).all_terms()
rem = p
for st in s_monomials:
  if st[1] != 0:
    stimesp = st[1]*x**st[0][0]*q
    new_lines = ["&&" + sp.latex(stimesp.expand()) + r"&&\\"]
    rem -= stimesp
    new_lines.extend([r"&&\overline{"+sp.latex(rem.expand())+r"}&\overline{\phantom{x^5}}&\\"])
    display_string.extend(new_lines)

final_lines = [r"\end{array}","$$"]
display_string.extend(final_lines)
display_string = "\n".join(display_string)
display(Latex(display_string))
:::


::::{prf:example-end}
::::


(sec:PartialFractionDecomposition)=
## Partial fraction decomposition

In the previous examples, you have seen how you can use polynomial long division to rewrite an improper rational function as a polynomial plus a proper rational function. In this section we will look at how to decompose proper rational functions into simpler fractions. This technique is called _partial fraction decomposition_.

We often apply the method of partial fraction decomposition in order to be able to determine the antiderivative of a rational function, as the antiderivative of a proper rational function is often easier to determine when the rational function is decomposed into simpler fractions. We will look at the method of partial fraction decomposition in more detail in {numref}`sec:Integration:RationalFunctions`.

Before we look at a first example, we take a look at (proper) regular fractions, such as

$$
\frac{1}{3}\text{ and }\frac{3}{7}.
$$

Normally you would calculate the sum of these fractions by rewriting them with a common denominator:

$$
\frac{1}{3}+\frac{3}{7} = \frac{1}{3}\frac{7}{7}+\frac{3}{7}\frac{3}{3} = \frac{7}{21}+\frac{9}{21} = \frac{16}{21}.
$$

If we have two rational functions, we can do the same. For instance consider the next calculation:

\begin{align*}
\frac{1}{x+2}+\frac{3}{x-5} &= \frac{1}{x+2}\frac{x-5}{x-5}+\frac{3}{x-5}\frac{x+2}{x+2} \\
&= \frac{x-5}{(x+2)(x-5)} + \frac{3(x+2)}{(x-5)(x+2)} \\
&= \frac{x-5 + 3(x+2)}{(x+2)(x-5)} \\
&= \frac{4x+1}{x^2-3x-10}.
\end{align*}

This method of rewriting the sum of rational functions into a single rational function is exactly the opposite of the method of partial fraction decomposition. In partial fraction decomposition we start with a proper rational function, such as $\frac{4x+1}{x^2-3x-10}$ and we want to rewrite it as the sum of simpler rational functions, such as $\frac{1}{x+2}+\frac{3}{x-5}$.

If we look at the previous calculation, we see that the roots of the denominator $x^2-3x-10$ are $x=-2$ and $x=5$. These roots correspond to the denominators of the simpler rational functions $\frac{1}{x+2}$ and $\frac{3}{x-5}$. The entire concept of partial fraction decomposition is based on this observation in combination with the {prf:ref}`Fundamental Theorem of Algebra <Thm:ComplexNumbers:fundamental>`.

We will look at several cases where we can apply partial fraction decomposition, starting with the case where the denominator can be factored into distinct linear factors.

::::{prf:example}
:label: Ex:RationalFunctions:PartialFractionDecomposition1

Consider the proper rational function

$$
r(x)  = \frac{p(x)}{q(x)} = \frac{4x+2}{x^2-1}.
$$

The denominator $q(x)=x^2-1$ of this rational function can be factored as $q(x)=(x-1)(x+1)$, i.e. as a product of distinct linear factors. So, based on our previous thinking, let us look for two constants $A$ and $B$ such that

:::{math}
:label: Eq:RationalFunctions:PartialFractionDecomposition1
r(x) = \frac{A}{x-1} + \frac{B}{x+1}
:::

holds. We start by taking the right-hand side of Equation {eq}`Eq:RationalFunctions:PartialFractionDecomposition1` and rewriting it as a single rational function:

\begin{align*}
\frac{A}{x-1} + \frac{B}{x+1} &= \frac{A(x+1)}{(x-1)(x+1)} + \frac{B(x-1)}{(x+1)(x-1)} \\
&= \frac{A(x+1) + B(x-1)}{(x-1)(x+1)} \\
&= \frac{(A+B)x + (A-B)}{x^2-1}.
\end{align*}

If we compare the numerator $(A+B)x + (A-B)$ of this result with the original numerator $p(x)=4x+2$ of $r(x)$ we see that we should have that $A+B=4$ and $A-B=2$. Solving this system of equations results in $A=3$ and $B=1$. This means we have found the partial fraction decomposition of $r$:

$$
r(x) = \frac{3}{x-1} + \frac{1}{x+1}.
$$

::::

If we consider that the constants $A$ and $B$ in the numerators of the simpler rational functions are in fact also polynomials, then we can see that the degree of the numerator of the simpler rational functions is less than the degree of the denominator. This is not a coincidence, and is always the case in partial fraction decomposition, as we always consider proper rational functions in the decomposition.

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

::::{admonition} Proof of Theorem {prf:ref}`Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearFactors`
:class: tudproof, dropdown

We need to show that there exist constants $A_1,A_2,\ldots,A_n$ such that

:::{math}
:label: Eq:RationalFunctions:ToShow

\frac{A_1}{x-b_1} + \frac{A_2}{x-b_2} + \cdots + \frac{A_n}{x-b_n} = \frac{p(x)}{a_n(x-b_1)(x-b_2)\cdots(x-b_n)}.
:::

First we will multiply both sides of the above equation by $q(x)=a_n(x-b_1)(x-b_2)\cdots(x-b_n)$ to obtain

$$
A_1\frac{q(x)}{x-b_1} + A_2\frac{q(x)}{x-b_2} + \cdots + A_n\frac{q(x)}{x-b_n} = p(x).
$$

On the right-hand side we have a polynomial with degree less than $n$, so the left-hand side should also be a polynomial of degree less than $n$. Each term of the form $A_k\frac{q(x)}{x-b_k}$ in the left-hand side is a rational function, provided the constant $A_k$ exists. As long as $x\neq b_k$, this rational function can be reduced to a polynomial if degree $n-1<n$, because the factor $x-b_k$ in the denominator can be canceled with one of the factors in the numerator. This means that, provided all constant $A_k$, $k=1,2,\ldots,n$, exist, each term of the left-hand side is a polynomial of degree less than $n$ and the entire left-hand side is a sum of polynomials of degree less than $n$ and so is itself a polynomial of degree less than $n$.

So if we can show that each constant $A_k$m $k=1,2,3,\ldots,n$, exist, then we have proven the theorem.

Let $k$ be any integer such that $1\leq k \leq n$. We will show that the constant $A_k$ exist.

We multiply Equation {eq}`Eq:RationalFunctions:ToShow` by $x-b_k$, to obtain

\begin{align*}
\frac{A_1(x-b_k)}{x-b_1} &+ \ldots + \frac{A_{k-1}(x-b_k)}{x-b_{k-1}} + A_k + \frac{A_{k+1}(x-b_k)}{x-b_{k+1}} \cdots + \frac{A_n}{x-b_n} \\
&= \frac{p(x)}{a_n(x-b_1)(x-b_2)\cdots(x-b_{k-1})(x-b_{k+1})\cdots(x-b_n)}.
\end{align*}

Note that we have canceled the common factor $x-b_k$ on both sides of the equation. Now we substitute $x=b_k$ in the above expression to obtain

$$
A_k = \frac{p(b_k)}{a_n(b_k-b_1)(b_k-b_2)\cdots(b_k-b_{k-1})(b_k-b_{k+1})\cdots(b_k-b_n)}.
$$

Because the numbers $b_1,b_2,\ldots,b_n$ are distinct, the denominator of the right-hand side is not zero. This means that the above expression is well-defined.

This shows that $A_k$ exists for all $k=1,2,\ldots,n$. This means that there exist constants $A_1,A_2,\ldots,A_n$ such that Equation {eq}`Eq:RationalFunctions:ToShow` holds. This completes the proof.

::::

Note that in the above theorem we considered complex numbers as roots of the denominator polynomial. This is because, by the {prf:ref}`Fundamental Theorem of Algebra <Thm:ComplexNumbers:fundamental>`, every polynomial with complex coefficients can be factored into linear factors over the complex numbers. If you did not yet study complex numbers, you can study {numref}`Ch:ComplexNumbersCartesian`. You can also consider the theorem only for real numbers as roots of the denominator polynomial. In that case the theorem only holds when the denominator can be factored into distinct linear factors over the real numbers.

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

Let us look for three numbers $A_1$, $A_2$ and $A_3$ such that

$$
r(x) = \frac{A_1}{x} + \frac{A_2}{x-3} + \frac{A_3}{x+1}.
$$

By substituting the formula for $r$ in the left-hand side, we obtain the equation

$$
\frac{15x+3}{x(x-3)(x+1)} = \frac{A_1}{x} + \frac{A_2}{x-3} + \frac{A_3}{x+1}
$$

for $A_1$, $A_2$ and $A_3$. Rewriting the right-hand side to a single rational function results in the equation

$$
\frac{15x+3}{x(x-3)(x+1)} = \frac{A_1(x-3)(x+1) + A_2x(x+1) + A_3x(x-3)}{x(x-3)(x+1)}.
$$

By comparing the numerators on both sides we obtain the equation

:::{math}
:label: Eq:RationalFunctions:PartialFractionDecomposition2

15x+3 = A_1(x-3)(x+1) + A_2x(x+1) + A_3x(x-3).
:::

Collecting terms on the right-hand side results in

$$
15x+3 = (A_1 + A_2 + A_3)x^2 + (-2A_1 +A_2-3A_3)x + (-3A_1).
$$

In the right-hand side we have a polynomial of degree $2$ and in the left-hand side we have a polynomial of degree $1$. To remedy this, we can rewrite the left-hand side as a polynomial of degree $2$ by adding a term with $x^2$ and setting its coefficient to zero:

$$
0x^2+15x+3 = (A_1 + A_2 + A_3)x^2 + (-2A_1 +A_2-3A_3)x + (-3A_1).
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

If the denominator of a proper rational function can be factored into distinct linear factors, there is another way to find the constants $A_1,A_2,\ldots,A_n$ in {prf:ref}`Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearFactors`.

Although the roots of the denominator are not part of the domain of the rational function, the polynomials on the left-hand side and on the right-hand side of the equation as a result of the comparison of numerators (such as Equation {eq}`Eq:RationalFunctions:PartialFractionDecomposition2` in the previous example) should coincide for all values. Even for the roots of the denominator. This means that we can find the constants $A_1,A_2,\ldots,A_n$ by substituting the roots of the denominator into this equation.

For the previous example, substituting the roots $x=0$, $x=3$ and $x=-1$ into Equation {eq}`Eq:RationalFunctions:PartialFractionDecomposition2`, respectively, would yield the following system of equations:

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

To avoid complex numbers in partial fraction decomposition, we will now look at the case where the denominator can be factored into distinct linear factors and distinct irreducible quadratics over the real numbers. Before we do this, we need the definition of an irreducible quadratic:

::::{prf:definition}
:label: Def:RationalFunctions:IrreducibleQuadratic

A polynomial $p$ of degree two that cannot be factored into linear factors over the real numbers is called an **irreducible quadratic**.

::::

To relate this to theory you already may have learned, we have the following theorem:

::::{prf:theorem}
:label: Thm:RationalFunctions:IrreducibleQuadratic

A quadratic polynomial $p(x)=Ax^2+Bx+C$ is irreducible over the real numbers if and only if its discriminant $B^2-4AC$ is negative.

::::

::::{admonition} Proof of Theorem {prf:ref}`Thm:RationalFunctions:IrreducibleQuadratic`
:class: tudproof, dropdown

First we will show that if the discriminant of a quadratic polynomial is negative, then the polynomial is irreducible over the real numbers. Let $p(x)=Ax^2+Bx+C$ be a quadratic polynomial with discriminant $B^2-4AC<0$. This means that if we define $c=-\frac{B}{2A}$ and $d=\frac{\sqrt{4AC-B^2}}{2A}>0$, then we have that

$$
r_1 = c + id \quad\text{and}\quad r_2 = c - id
$$

are the roots of $p$. Since $d>0$, these roots are complex conjugates and not real numbers. This means that $p$ cannot be factored into linear factors over the real numbers, by the Fundamental Theorem of Algebra, so $p$ is irreducible over the real numbers.

If on the other hand $p$ is irreducible over the real numbers, then $p$ cannot be factored into linear factors over the real numbers. This means that the roots of $p$ are not real numbers. Since the roots of a quadratic polynomial are given by the formula

$$
x = \frac{-B \pm \sqrt{B^2-4AC}}{2A},
$$

and these roots must have a non-zero imaginary part, this means that the discriminant $B^2-4AC$ must be negative. This completes the proof.

::::

In the next part we need a special way of writing an irreducible quadratic. We can always rewrite an irreducible quadratic in the form given in the next theorem.

::::{prf:theorem}
:label: Thm:RationalFunctions:IrreducibleQuadraticForm

Let $p$ be an irreducible quadratic polynomial with $p(x)=Ax^2+Bx+C$. Then there exist real numbers $c$ and $d$ such that

$$
p(x) = A\left((x-c)^2+d^2\right).
$$

::::

::::{admonition} Proof of Theorem {prf:ref}`Thm:RationalFunctions:IrreducibleQuadraticForm`
:class: tudproof, dropdown

Let $p(x)=Ax^2+Bx+C$ be an irreducible quadratic polynomial. Since $p$ is irreducible, the discriminant $B^2-4AC$ is negative. This means that if we define $c=-\frac{B}{2A}$ and $d=\frac{\sqrt{4AC-B^2}}{2A}>0$, then we have that

\begin{align*}
-2c &= -2\left(-\frac{B}{2A}\right) = \frac{B}{A}, \\
c^2 &= \left(-\frac{B}{2A}\right)^2 = \frac{B^2}{4A^2}, \\
d^2 &= \left(\frac{\sqrt{4AC-B^2}}{2A}\right)^2 = \frac{4AC-B^2}{4A^2}, \\
c^2 + d^2 &= \frac{B^2}{4A^2} + \frac{4AC-B^2}{4A^2} = \frac{4AC}{4A^2} = \frac{C}{A}.
\end{align*}

This means that we also have that

\begin{align*}
A\left((x-c)^2+d^2\right) &= A\left(x^2-2cx+c^2+d^2\right) \\
&= Ax^2 + A\left(-2c\right)x + A\left(c^2+d^2\right) \\
&= Ax^2 + Bx + C \\
&= p(x).
\end{align*}

This completes the proof.
::::

With this definition and these theorems, we first look at an example of a proper rational function where the denominator can be factored into one distinct linear factor and one distinct irreducible quadratics over the real numbers.

::::{prf:example}
:label: Ex:RationalFunctions:PartialFractionDecomposition4

Consider the proper rational function

$$
r(x)  = \frac{5x^2+24x+7}{2x^3+2x^2-2x+30}.
$$

The denominator $q(x)=2x^3+2x^2-2x+30$ can be factored as

$$
q(x) = 2(x+3)\left( x^2-2x+5\right).
$$

The last term $x^2-2x+5$ is an irreducible quadratic since its discriminant is negative, i.e. $(-2)^2-4\cdot1\cdot5=-16<0$. So the denominator can be factored into one distinct linear factor and one distinct irreducible quadratic over the real numbers.

{prf:ref}`Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearFactors` does not apply to this case if we limit the theorem to real linear factors, since the denominator cannot be factored into distinct real linear factors. However, we can still find a partial fraction decomposition of $r$ by attempting to find something with a similar structure as for the case of distinct linear factors.

In the case of a linear factor, such as $x+3$, we had a constant $A_1$ in the numerator of the corresponding simpler rational function $\frac{A_1}{x+3}$. In other words, the degree of the numerator was zero, which is one less than the degree of the denominator, which is one. This is because we want to have a proper rational function in the decomposition.

If we would apply the same principle as for the linear factor to the irreducible quadratic $x^2-2x+5$, we would want a numerator of degree one, which is one less than the degree of the denominator, which is two. This means that we should have a linear factor in the numerator of the corresponding simpler rational function, which results in the form

$$
\frac{B_1x + C_1}{x^2-2x+5},
$$

where $B_1$ and $C_1$ are constants. So let us try this.

A partial fraction decomposition of $r$ could be of the form

$$
r(x) = \frac{A_1}{x+3} + \frac{B_1x + C_1}{x^2-2x+5}.
$$ 

Rewriting the right-hand side to a single rational function and comparing the numerators results in the equation

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
r(x) = \frac{-\frac12}{x+3} + \frac{3x + 2}{x^2-2x+5}.
$$

::::

As you can see, the choice to use a linear factor in the numerator of the simpler rational function corresponding to the irreducible quadratic in the denominator worked, and we were able to find a partial fraction decomposition of $r$ using only real coefficients.

In the next example we will consider the same proper rational function but now we will use complex numbers. Feel free to skip this example for now and return to it after studying complex numbers in {numref}`Ch:ComplexNumbersCartesian`.

::::{prf:example} Partial fraction decomposition with complex linear factors
:label: Ex:RationalFunctions:PartialFractionDecomposition3
:class: dropdown

Consider the proper rational function

$$
r(x)  = \frac{5x^2+24x+7}{2x^3+2x^2-2x+30}.
$$

The denominator $q(x)=2x^3+2x^2-2x+30$ has the roots $b_1=-3$, $b_2= 1-2i$ and $b_3=1+2i$. So $r$ can be factored by {prf:ref}`Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearFactors` as

$$
r(x) = \frac{A_1}{x+3} + \frac{A_2}{x-(1-2i)} + \frac{A_3}{x-(1+2i)}.
$$ 

Rewriting the right-hand side to a single rational function and comparing the numerators results in the equation

\begin{align*}
\frac52x^2+12x+\frac72 &= \left(A_1+A_2+A_3\right)x^2 \\
&~ \qquad + \left( -2A_1+(2-2i)A_2+(2+2i)A_3\right)x \\
&~ \qquad +\left(5A_1+(-3-6i)A_2+( -3+6i)A_3\right).
\end{align*}

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


If we combine the last two terms of the above expression, we obtain

$$
\frac{\frac32+\frac54i}{x-(1-2i)} + \frac{\frac32-\frac54i}{x-(1+2i)} = \frac{3x+2}{(x-1)^2 + 4}.
$$

This means we can also write the partial fraction decomposition of $r$ with real coefficients as

$$
r(x) = \frac{-\frac12}{x+3} + \frac{3x+2}{(x-1)^2 + 4}.
$$

This is the same partial fraction decomposition as in {prf:ref}`Ex:RationalFunctions:PartialFractionDecomposition4`, which means that we have found the same partial fraction decomposition of $r$ using only real coefficients and using complex numbers. This is not a coincidence, and is always the case when the denominator can be factored into distinct linear factors and distinct irreducible quadratics over the real numbers.

::::

The next theorem states that the idea of {prf:ref}`Ex:RationalFunctions:PartialFractionDecomposition4` can be applied in general when the denominator can be factored into distinct linear factors and distinct irreducible quadratics over the real numbers. 

::::{prf:theorem} Partial fraction decomposition with distinct real linear factors and distinct irreducible quadratics
:label: Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearAndIrreducibleQuadratic

Let $r(x) = \frac{p(x)}{q(x)}$ be a proper rational function where the denominator $q$ can be factored into $\ell$ _distinct and real linear factors_ and $m$ _distinct irreducible quadratics_, i.e.

\begin{align*}
q(x) &= a_n(x-b_1)(x-b_2)\cdots(x-b_\ell) \\
&~ \qquad \cdot ( (x-c_1)^2 + d_1^2 )( (x-c_2)^2 + d_2^2 ) \cdots ( (x-c_m)^2 + d_m^2 ),
\end{align*}

where $b_1,b_2,\ldots,b_\ell$ are _distinct real numbers_, $(c_1,d_1^2),(c_2,d_2^2),\ldots,(c_m,d_m^2)$ are _distinct real number pairs_ with $d_1,d_2,\ldots,d_m\neq0$, and $a_n$ is the leading coefficient of $q$.

Then there exist real constants $A_1,A_2,\ldots,A_\ell$, $B_1,\ldots,B_m$ and $C_1,\ldots,C_m$ such that

\begin{align*}
r(x) &= \frac{A_1}{x-b_1} + \frac{A_2}{x-b_2} + \cdots + \frac{A_\ell}{x-b_\ell} \\
&~ \qquad + \frac{B_1x + C_1}{(x-c_1)^2 + d_1^2} + \cdots + \frac{B_mx + C_m}{(x-c_m)^2 + d_m^2}.
\end{align*}

::::

::::{admonition} Proof of Theorem {prf:ref}`Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearAndIrreducibleQuadratic`
:class: tudproof, dropdown

This proof is similar to the proof of {prf:ref}`Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearFactors`, but now we also have to take into account the irreducible quadratics in the denominator. We will not give a full proof here, but we will give the main ideas and conclusions.

By multiplication of the two representations of $r$ by the denominator $q$, we can show that if the constants $A_1,A_2,\ldots,A_\ell$, $B_1,\ldots,B_m$ and $C_1,\ldots,C_m$ exist, then the right-hand side of the equation in the theorem is a polynomial of degree less than $n$. Since the right-hand side should be equal to the left-hand side, which is also a polynomial of degree less than $n$, this means that if the constants exist, then the equation in the theorem holds.

Next we focus on the linear factors in the denominator. We can use multiplication by $x-b_k$ and subsequent substitution of $x=b_k$as in the proof of {prf:ref}`Thm:RationalFunctions:PartialFractionDecompositionDistinctLinearFactors` to show that the constants $A_1,A_2,\ldots,A_\ell$ exist.

Finally we focus on the irreducible quadratics in the denominator. We can use multiplication by $(x-c_h)^2 + d_h^2$ and subsequent substitution of $x=c_h\pm id_h$to show that the constants $B_1,\ldots,B_m$ and $C_1,\ldots,C_m$ exist.

These three (large) steps show that the theorem holds.

::::

In all of the above examples we have only considered the case where the denominator can be factored into distinct linear factors and distinct irreducible quadratics. If the denominator has repeated factors and/or repeated quadratics, the partial fraction decomposition becomes slightly more complicated.

Consider the proper rational function

$$
r(x)  = \frac{2x^2+6x+5}{(x+1)^2(x+2)}.
$$

The denominator $q(x)=(x+1)^2(x+2)$ of this rational function has a repeated linear factor $(x+1)$. If tried to apply the previous theorems directly, we would look for constants $A$, $B$ and $C$ such that

$$
r(x) = \frac{A}{x+1} + \frac{B}{x+1} + \frac{C}{x+2}.
$$

If we rewrite the right-hand side as a single rational function, we obtain

$$
r(x) = \frac{(A+B)(x+2) + C(x+1)}{(x+1)(x+2)} = \frac{(A+B+C)x + (2A+2B+C)}{(x+1)(x+2)}.
$$

The denominator of this expression is not equal to the original denominator of the rational function $r$, so we cannot compare the numerators directly. If we multiply both the denominator and the numerator of the last expression with $x+1$, we obtain

\begin{align*}
r(x) &= \frac{((A+B+C)x + (2A+2B+C))(x+1)}{(x+1)^2(x+2)} \\
&= \frac{(A+B+C)x^2 + (3A+2B+C)x + (2A+2B+C)}{(x+1)^2(x+2)}.
\end{align*}

Now the denominator is equal to the original denominator of $r$ and we can compare the numerators. This results in the system of equations

$$
\left\{\begin{array}{lcr}
A+B+C &=& 2, \\
3A+3B+2C &=& 6, \\
2A+2B+C &=& 5.
\end{array}\right.
$$

Unfortunately, this system has no solutions, so our initial assumption about the form of the partial fraction decomposition was incorrect.

If we look at the last system, we see that we have three equations for only two unknowns. This is because we did not take into account that the factor $(x+1)$ in the denominator is repeated, which is also evident from the fact that we had to multiply the numerator and denominator by $x+1$ to be able to compare numerators.

If we just consider the factor $(x+1)^2$ in the denominator, we would also arrive at an inconsistent linear system in two variables. However, if we consider both factors $(x+1)$ and $(x+1)^2$ in the denominator separately, we will have three unknowns instead of two. This is similar to how we handled irreducible quadratics in the previous theorem: there we had a linear and a constant term in the numerator for each irreducible quadratic factor in the denominator. We will do something similar here. We also do have to consider cases where a factor is repeated more than two times, but the idea is the same.

It could also be the case that an irreducible quadratic is repeated in the denominator. In that case we will also have to consider multiple terms in the partial fraction decomposition for that irreducible quadratic. The next theorem summarises all of this.

::::{prf:theorem} Partial fraction decomposition with repeated real linear factors and repeated irreducible quadratics
:label: Thm:RationalFunctions:RepeatedLinearAndIrreducibleQuadratic

Let $r(x) = \frac{p(x)}{q(x)}$ be a proper rational function where the denominator $q$ can be factored into $\ell$ _real linear factors_ and $m$ _irreducible quadratics_, i.e.

$$
\begin{split}
q(x) &= a_n(x-b_1)^{s_1}(x-b_2)^{s_2}\cdots(x-b_\ell)^{s_\ell}\\
& \qquad ( (x-c_1)^2 + d_1^2 )^{t_1}( (x-c_2)^2 + d_2^2 )^{t_2} \cdots ( (x-c_m)^2 + d_m^2 )^{t_m},
\end{split}
$$

where $b_1,b_2,\ldots,b_\ell$ are _distinct real numbers_, $s_1,s_2,\ldots,s_\ell$ are positive integers, $(c_1,d_1^2),(c_2,d_2^2),\ldots,(c_m,d_m^2)$ are _distinct real number pairs_ with $d_1,d_2,\ldots,d_m\neq0$, $t_1,t_2,\ldots,t_m$ are positive integers, and $a_n$ is the leading coefficient of $q$.

Then there exist constants $A_{k,j}$, $1\leq j \leq s_k$ for $1\leq k \leq \ell$, and constants $B_{h,j}$ and $C_{h,j}$, $1\leq j \leq t_h$, for $1\leq h \leq m$ such that

$$
r(x)= L_1(x)+L_2(x)+\cdots+L_\ell(x) + Q_1(x) + Q_2(x) + \cdots + Q_m(x),
$$


where for $1\leq k \leq \ell$

$$
L_k(x) = \frac{A_{k,1}}{x-b_k} + \frac{A_{k,2}}{(x-b_k)^2} + \cdots + \frac{A_{k,s_k}}{(x-b_k)^{s_k}}.
$$

and for $1\leq h \leq m$

$$
Q_h(x) = \frac{B_{h,1}x + C_{h,1}}{(x-c_h)^2 + d_h^2} + \frac{B_{h,2}x + C_{h,2}}{((x-c_h)^2 + d_h^2)^2} + \cdots + \frac{B_{h,t_h}x + C_{h,t_h}}{((x-c_h)^2 + d_h^2)^{t_h}}.
$$

::::

We will not give a proof of the above theorem, but the main idea is similar to the proofs of the previous two theorems. The main difference is that we have to take into account the repeated factors in the denominator, which results in more unknowns in the system of equations obtained by comparing coefficients.

::::{prf:remark}
:label: Rmk:RationalFunctions:RepeatedLinearAndIrreducibleQuadratic

Because of the generality of {prf:ref}`Thm:RationalFunctions:RepeatedLinearAndIrreducibleQuadratic`, we used constants with multi-level indexing. In practice it is often easier to use different letters for the constants in the numerators of the various terms in the partial fraction decomposition, as we will do in the next example.
::::

::::{prf:example}
:label: Ex:RationalFunctions:PartialFractionDecomposition5

For the proper rational function

$$
r(x)  = \frac{2x^2+6x+5}{(x+1)^2(x+2)},
$$

we now try the following form for the partial fraction decomposition:

$$
r(x) = \frac{A}{x+1} + \frac{B}{(x+1)^2} + \frac{C}{x+2}.
$$

Rewriting the right-hand side to a single rational function gives:

\begin{align*}
r(x) &= \frac{A(x+1)(x+2) + B(x+2) + C(x+1)^2}{(x+1)^2(x+2)} \\
&= \frac{(A+C)x^2 + (3A+B+2C)x + (2A+2B+C)}{(x+1)^2(x+2)}.
\end{align*}

Comparing the numerators results in the system of equations

$$
\left\{\begin{array}{lcr}
A+C&=&2, \\
3A+B+2C &=& 6, \\
2A+2B+C &=& 5.
\end{array}\right.
$$

This system has a solution (fortunately), which is $A=1$, $B=1$ and $C=1$. This means we have found the partial fraction decomposition of $r$:

$$
r(x) = \frac{1}{x+1} + \frac{1}{(x+1)^2} + \frac{1}{x+2}.
$$

::::

We end this section, before going to the {ref}`Sec:RationalFunctions:GraspleExercises`, with an example that contains everything we have learned so far.

::::{prf:example-start}
:label: Ex:RationalFunctions:PartialFractionDecomposition6

Consider the proper rational function

$$
r(x)  = \frac{ 2 x^8+ 7 x^7+ 9 x^6- 22 x^5 - 104 x^4 - 230 x^3 - 282 x^2 - 196 x -84  }{(x - 1) (x + 2)^2 (x^2+3) (2 + 2 x + x^2)^2}
$$

The denominator $q(x)=(x - 1) (x + 2)^2 (x^2+3) (2 + 2 x + x^2)^2$ of this rational function has a distinct linear factor $(x - 1)$, a repeated linear factor $(x + 2)$ with multiplicity $2$, a distinct irreducible quadratic factor $(x^2+3)$ and a repeated irreducible quadratic factor $(2 + 2 x + x^2)$ with multiplicity $2$.

Based on {prf:ref}`Thm:RationalFunctions:RepeatedLinearAndIrreducibleQuadratic`, we try the following form for the partial fraction decomposition:

$$
r(x) = \frac{A}{x-1}+\frac{B}{x+2}+\frac{C}{(x+2)^2}+\frac{Dx + E}{x^2+3}+\frac{Fx + G}{2 + 2 x + x^2}+\frac{Hx + I}{(2 + 2 x + x^2)^2}.
$$

Rewriting the right-hand side to a single rational function and comparing the numerators results in a system of $9$ equations with $9$ unknowns. Solving such a system can be quite tedious, so we turn to some Python code. Run the code and see what happens.

::::

:::{code-cell} python
# Import a symbolic mathematics library
import sympy as sp
from IPython.display import Latex
# Define the variable and the constants
x = sp.symbols('x')
# define the rational function 
p = (2*x**8 + 7*x**7 + 9*x**6 - 22*x**5 - 104*x**4 \
     - 230*x**3 - 282*x**2 - 196*x -84)
q = ((x - 1) \
     * (x + 2)**2 * (x**2 + 3) * (2 + 2*x + x**2)**2)
r = p / q
# perform the partial fraction decomposition
decomp = sp.apart(r)

# Display the result
display(Latex("A partial fraction decomposition of"))
display(Latex("$$r(x) = "+sp.latex(r)+".$$"))
display(Latex("is"))
display(Latex("$$r(x) = "+sp.latex(decomp)+".$$"))
A, B, C, D, E, F, G, H, I = sp.symbols('A B C D E F G H I')
rform = A/(x - 1) \
+ B/(x + 2) \
+ C/(x + 2)**2 \
+ (D*x + E)/(x**2 + 3) \
+ (F*x + G)/(2 + 2*x + x**2) \
+ (H*x + I)/(2 + 2*x + x**2)**2
num, den = rform.cancel().as_numer_denom()
pterms = sp.Poly(p,x).all_terms()
nterms = sp.Poly(num,x).all_terms()
display(Latex("""The systems of equations that would result in this
 partial fraction decomposition (based on the form above):"""))
eq_str = [r"$$\left\{\begin{array}{rcr}"]
for i in range(len(pterms)):
  if i+1<len(pterms):
    eq_str.append(f"{sp.latex(nterms[i][1])} & = & {pterms[i][1]}, \\\\")
  else:
    eq_str.append(f"{sp.latex(nterms[i][1])} & = & {pterms[i][1]}.")
  

eq_str.append(r"\end{array}\right.$$")
eq_str = "\n".join(eq_str)
display(Latex(eq_str))
:::

::::{prf:example-end}
::::

::::{question} Multiple-choice Single-select
:type: multiple-choice
:variant: single-select
:admonition:
:class: question

A partial fraction decomposition for $f(x)=\dfrac{x^2+4}{x(x-1)^2}$ is asked.

Someone suggests the decomposition $f(x)=\dfrac{A}{x} + \dfrac{Bx+C}{(x-1)^2}$.

Will this suggestion lead to a partial fraction decomposition of $f$?

---
[ ] No, because the proposed decomposition is incorrect.
> Although you are not wrong, nothing is directly wrong with the proposed decomposition, so this is not the best answer.
[ ] No, because we will not find a solution for $A$, $B$ and $C$.
> If you would try to find $A$, $B$ and $C$ by comparing coefficients, you would find that $A$, $B$ and $C$ satisfy the system of equations

$$
\begin{cases}
A + B &= 1, \\
-2A+C &= 0, \\
A &= 4.
\end{cases}
$$

Investigate yourself whether this system has a solution or not.

[ ] No, because we will find infinitely many solutions for $A$, $B$ and $C$.
> If you would try to find $A$, $B$ and $C$ by comparing coefficients, you would find that $A$, $B$ and $C$ satisfy the system of equations

$$
\begin{cases}
A + B &= 1, \\
-2A+C &= 0, \\
A &= 4.
\end{cases}
$$

Investigate yourself whether this system has one or infinitely many solutions or not.

[x] Yes, because we will find a unique solution for $A$, $B$ and $C$.
> Although the suggested decomposition is not a standard partial fraction decomposition, we can show that for this particular rational function, we will find $A=4$, $B=-3$ and $C=8$ as the unique solution for $A$, $B$ and $C$. The notice that

\begin{align*}
\dfrac{Bx+C}{(x-1)^2} &= \dfrac{-3x+8}{(x-1)^2} \\
&=  \dfrac{-3(x-1)+5}{(x-1)^2} \\
&=  \dfrac{-3}{x-1} + \dfrac{5}{(x-1)^2}.
\end{align*}

So after this step, the suggested decomposition can be rewritten to the standard form of a partial fraction decomposition, which turns out to be

$$
f(x) = \dfrac{4}{x} + \dfrac{-3}{x-1} + \dfrac{5}{(x-1)^2}.
$$
---
::::

(Sec:RationalFunctions:GraspleExercises)=
## Grasple exercises

### Domain and range

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/debe9205-dc80-4e2d-88e4-e9a90671b5a5?id=131205
:label: Grasple:131205
:dropdown:
:description: Find the domain of a rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2e95a962-8482-40a6-9c9a-5e2f34adaf5e?id=70778
:label: Grasple:70778
:dropdown:
:description: Find the domain of a rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e5683704-3cac-4cb6-8535-bc4ba03deb4b?id=70802
:label: Grasple:70802
:dropdown:
:description: Find the domain of a rational function.

::::

### Long division

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4700075b-46b4-4872-944e-52abcedd453f?id=131208
:label: Grasple:131208
:dropdown:
:description: Perform long division of polynomials.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/aa4ce0bf-388f-4bd9-b399-547f5caf1dc1?id=131209
:label: Grasple:131209
:dropdown:
:description: Perform long division of polynomials.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c4940371-5342-4c15-b2dd-511806136e45?id=70065
:label: Grasple:
:dropdown:
:description: Perform long division of polynomials.

::::

### Partial fraction decomposition

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7e93a9ec-efc0-41b5-915a-7859bc8ef483?id=76961
:label: Grasple:76961
:dropdown:
:description: Find the form for a partial fraction decomposition of a rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ac5587d0-c069-4b20-9d2a-60a622b0ff53?id=76964
:label: Grasple:76964
:dropdown:
:description: Find the form for a partial fraction decomposition of a rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/51e48a0d-7e14-41ee-9197-1b672d901946?id=76965
:label: Grasple:76965
:dropdown:
:description: Find the form for a partial fraction decomposition of a rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fa880403-1aed-481d-b0fc-f33aff7a5f18?id=76966
:label: Grasple:76966
:dropdown:
:description: Find the form for a partial fraction decomposition of a rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b8410be6-4f2a-4677-8534-76cb52b111ab?id=76967
:label: Grasple:76967
:dropdown:
:description: Find the form for a partial fraction decomposition of a rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a04d2783-b937-4cbd-944d-3010badaf13b?id=64098
:label: Grasple:64098
:dropdown:
:description: Find a partial fraction decomposition of a rational function step-by-step.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/58b43c58-7ec7-471e-a2f1-f45e074cf9dc?id=64101
:label: Grasple:64101
:dropdown:
:description: Find a partial fraction decomposition of a rational function step-by-step.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/509e7e82-2e3c-4fc0-b481-57e6f73335c5?id=64105
:label: Grasple:64105
:dropdown:
:description: Find a partial fraction decomposition of a rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/03079bd7-acfc-4d79-bbbf-51343cce6b40?id=64104
:label: Grasple:64104
:dropdown:
:description: Find a partial fraction decomposition of a rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c956a099-e66d-4aac-8285-7fba11239b8a?id=64242
:label: Grasple:64242
:dropdown:
:description: Find a partial fraction decomposition of a rational function.

::::