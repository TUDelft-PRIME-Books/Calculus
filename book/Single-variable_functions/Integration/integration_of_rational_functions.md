(Sec:Integration:RationalFunctions)=

# Integration of rational functions

## Introduction

In {numref}`Sec:RationalFunctions` we covered rational functions and more specifically polynomial division and partial fraction decomposition. In this section we will use these techniques to evaluate integrals of rational functions.

In {numref}`Sec:PartialFractionDecomposition` we encountered in {prf:ref}`Thm:RationalFunctions:RepeatedLinearAndIrreducibleQuadratic` that any _proper_ rational function can be written as a sum of partial fractions, where each is one of the following general forms:

- $\displaystyle\frac{A}{(x-a)^k}$ with $A,a\in\mathbb{R}$ and $k\in\{1,2,3,\ldots\}$.
- $\displaystyle\frac{Bx+C}{((x-b)^2+c^2)^m}$ with $B,C,b,c\in\mathbb{R}$ and $m\in\{1,2,3,\ldots\}$.

## Indefinite integrals of six cases

To evaluate integrals containing one of the above general forms, we need to be able to integrate six specific cases:

1. $\displaystyle\frac{1}{x-a}$ with $a\in\mathbb{R}$.
2. $\displaystyle\frac{1}{(x-a)^k}$ with $a\in\mathbb{R}$ and $k\in\{2,3,\ldots\}$.
3. $\displaystyle\frac{x-b}{(x-b)^2+c^2}$ with $b,c\in\mathbb{R}$, $c\neq0$.
4. $\displaystyle\frac{1}{(x-b)^2+c^2}$ with $b,c\in\mathbb{R}$, $c\neq0$.
5. $\displaystyle\frac{x-b}{((x-b)^2+c^2)^m}$ with $b,c\in\mathbb{R}$, $c\neq0$ and $m\in\{2,3,\ldots\}$.
6. $\displaystyle\frac{1}{((x-b)^2+c^2)^m}$ with $b,c\in\mathbb{R}$, $c\neq0$ and $m\in\{2,3,\ldots\}$.

The six cases can be integrated using the following theorem:

::::::{prf:theorem}
:label: Thm:RationalFunctions:Cases

Let $a,b,c\in\mathbb{R}$, $c\neq0$ and $k,m\in\{2,3,\ldots\}$. Then we have

1. $\displaystyle\int\frac{1}{x-a}\,dx = \ln|x-a|+C$ with $C\in\mathbb{R}$.<br><br>
2. $\displaystyle\int\frac{1}{(x-a)^k}\,dx = \frac{-1}{k-1}\cdot\frac{1}{(x-a)^{k-1}}+C$ with $C\in\mathbb{R}$.<br><br>
3. $\displaystyle\int\frac{x-b}{(x-b)^2+c^2}\,dx = \frac{1}{2}\ln((x-b)^2+c^2)+C$ with $C\in\mathbb{R}$.<br><br>
4. $\displaystyle\int\frac{1}{(x-b)^2+c^2}\,dx = \frac{1}{c}\arctan\left(\frac{x-b}{c}\right)+C$ with $C\in\mathbb{R}$.<br><br>
5. $\displaystyle\int\frac{x-b}{((x-b)^2+c^2)^m}\,dx = \frac{-1}{2(m-1)}\cdot\frac{1}{((x-b)^2+c^2)^{m-1}}+C$ with $C\in\mathbb{R}$.<br><br>
6. $\displaystyle\int\frac{1}{((x-b)^2+c^2)^m}\,dx = \int\frac{1}{c}\cos^{2m-2}(t)\,dt$ with $x=b+c\tan(t)$ and $C\in\mathbb{R}$.

::::::

The last integrand in the sixth case can be evaluated using the techniques for trigonometric integrals, which is covered in {numref}`sec:Integration:TrigFunctions`.

::::{admonition} Proof of {prf:ref}`Thm:RationalFunctions:Cases`
:class: tudproof

Cases 1 and 2 follow from the substitution $u=x-a$ and {numref}`Tab:Integration:StandardIndefiniteIntegrals`.

Cases 3 and 5 follow from the substitution $u=(x-b)^2+c^2$ and {numref}`Tab:Integration:StandardIndefiniteIntegrals`.

Case 4 follows from the substitution $u=\frac{x-b}{c}$ and {numref}`Tab:Integration:StandardIndefiniteIntegrals`.

Finally, case 6 follows from the substitution $x=b+c\tan(t)$, which leads to $dx=c(1+\tan^2(t))\,dt$ and therefore

\begin{align*}
\int\frac{1}{((x-b)^2+c^2)^m}\,dx&=\int\frac{c(1+\tan^2(t))}{(c^2(1+\tan^2(t)))^m}\,dt\\
&= \int\frac{1}{c}\cdot\frac{1}{(1+\tan^2(t))^{m-1}}\,dt\\
&=\int\frac{1}{c}\cos^{2m-2}(t)\,dt,
\end{align*}

where in the last step we used the identity $1+\tan^2(t)=\dfrac{1}{\cos^2(t)}$.

::::

Now we have all the tools to evaluate integrals of rational functions.

## Algorithm

Integrating a rational function always consists of the same steps, which means we can capture it in a general algorithm:

::::::{prf:algorithm}
:label: Alg:RationalFunctions:IntegrationAlgorithm

Assume $f$ is a rational function. Then we can evaluate $\displaystyle\int f(x)\,dx$ as follows:

1. Determine polynomials $P$ and $Q$ such that $f(x)=\frac{P(x)}{Q(x)}$ for all $x\in\mathbb{R}$ with $Q(x)\neq0$.
2. Perform a long division to find polynomials $S$ and $R$ with $\deg(R)<\deg(Q)$ such that $f(x)=S(x)+\frac{R(x)}{Q(x)}$.
3. Perform a partial fraction decomposition to write $\frac{R(x)}{Q(x)}$ as a sum of partial fractions.
4. Split each of the partial fractions into multiples of the six cases in {prf:ref}`Thm:RationalFunctions:Cases`.
5. Integrate each of the separate terms (remember to also integrate the polynomial $S$).
6. Add the results together and add a constant of integration.

::::::

In the next sections we will apply this algorithm to various examples.

:::{prf:remark}
:label: Rmk:RationalFunctions:IntegrationAlgorithm

{prf:ref}`Alg:RationalFunctions:IntegrationAlgorithm` can be used to evaluate definite integrals of rational functions as well. However, in order to avoid problems the zeros of the denominator of the integrand should not be in the interval of integration. See {numref}`Sec:Integration:ImproperIntegrals` for more details.

:::

## Unrepeated linear factors

If the partial fraction decomposition of a proper rational function only contains unrepeated linear factors, then we can directly apply the first case of {prf:ref}`Thm:RationalFunctions:Cases` to find the answer. We give two examples.

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample1
We will evaluate $\displaystyle\int\frac{x^3}{x^2+5x+6}\,dx$.

We start with a long division

$$
\frac{x^3}{x^2+5x+6}=x-5+\frac{19x+30}{x^2+5x+6}.
$$

Then we factor the denominator $x^2+5x+6$ into $(x+2)(x+3)$ and find the partial fraction decomposition:

$$
\frac{19x+30}{x^2+5x+6}=-\frac{8}{x+2}+\frac{27}{x+3}.
$$

Hence, we have

\begin{align*}
\int\frac{x^3}{x^2+5x+6}\,dx&=\int\left(x-5-\frac{8}{x+2}+\frac{27}{x+3}\right)\,dx\\
&=\frac{1}{2}x^2-5x-8\ln|x+2|+27\ln|x+3|+C.
\end{align*}

::::::

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample2
Now we take a look at $\displaystyle\int\frac{6x^2-4x-1}{2x^3+x^2-x}\,dx$.

Note that the integrand is a proper rational function since the degree of the numerator is less than the degree of the denominator, and $2x^3+x^2-x=2x(x-\frac12)(x+1)$ and therefore

\begin{align*}
\frac{6x^2-4x-1}{2x^3+x^2-x} &= \frac{6x^2-4x-1}{2x(x-\frac12)(x+1)} \\
&= \frac{3x^2-2x-\frac12}{x(x-\frac12)(x+1)} \\
&= \frac{1}{x}-\frac{1}{x-\frac12}+\frac{3}{x+1}.
\end{align*}

This leads to

\begin{align*}
\int\frac{6x^2-4x-1}{2x^3+x^2-x}\,dx&=\int\left(\frac{1}{x}-\frac{1}{x-\frac12}+\frac{3}{x+1}\right)\,dx\\
&=\ln|x|-\ln|x-\tfrac{1}{2}|+3\ln|x+1|+C.
\end{align*}

Note that $\ln|x-\tfrac12|=\ln|\frac12(2x-1)|=\ln(\tfrac12)+\ln|2x-1|$. This implies that the answer can also be written as (with a different  constant of integration)

$$
\int\frac{6x^2-4x-1}{2x^3+x^2-x}\,dx=\ln|x|-\ln|2x-1|+3\ln|x+1|+C.
$$

::::::

::::{exercise}
:label: Exc:Integration:RationalFunctionsExercise1
Prove that $\displaystyle\int\frac{dx}{x^2-\alpha^2}=\frac{1}{2\alpha}\ln\left|\frac{x-\alpha}{x+\alpha}\right|+C$ for $\alpha\neq0$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:RationalFunctionsExercise1`
:class: solution, dropdown
Note that $x^2-\alpha^2=(x-\alpha)(x+\alpha)$ and

$$
\frac{1}{x^2-\alpha^2}=\frac{A}{x-\alpha}+\frac{B}{x+\alpha}=\frac{A(x+\alpha)+B(x-\alpha)}{(x-\alpha)(x+\alpha)}
$$

with $A=\dfrac{1}{2\alpha}$ and $B=-\dfrac{1}{2\alpha}$. Hence, we have

\begin{align*}
\int\frac{dx}{x^2-\alpha^2}&=\frac{1}{2\alpha}\int\left(\frac{1}{x-\alpha}-\frac{1}{x+\alpha}\right)\,dx\\
&=\frac{1}{2\alpha}\left(\ln|x-\alpha|-\ln|x+\alpha|\right)+C\\
&=\frac{1}{2\alpha}\ln\left|\frac{x-\alpha}{x+\alpha}\right|+C.
\end{align*}
:::

## Repeated linear factors

If the partial fraction decomposition of a proper rational function contains repeated linear factors, then we can directly apply the second case of {prf:ref}`Thm:RationalFunctions:Cases` to find the answer. We give two examples.

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample3
Consider $\displaystyle\int\frac{x^2}{x^2+2x+1}\,dx$.

We have

$$
\frac{x^2}{x^2+2x+1}=1-\frac{2x+1}{x^2+2x+1}=1-\frac{2x+1}{(x+1)^2}.
$$

In this case we obtain

$$
\frac{2x+1}{(x+1)^2}=-\frac{2}{x+1}+\frac{1}{(x+1)^2}.
$$

Hence we have

\begin{align*}
\int\frac{x^2}{x^2+2x+1}\,dx&=\int\left(1-\frac{2}{x+1}+\frac{1}{(x+1)^2}\right)\,dx\\
&=x-2\ln|x+1|-\frac{1}{x+1}+C.
\end{align*}
::::::

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample4
We will evaluate $\displaystyle\int\frac{x(3x+5)}{(x+1)^3}\,dx$.

Note that the integrand is a proper rational function and

$$
\frac{x(3x+5)}{(x+1)^3}=\frac{3}{x+1}-\frac{1}{(x+1)^2}-\frac{2}{(x+1)^3}.
$$

We conclude that

\begin{align*}
\int\frac{x(3x+5)}{(x+1)^3}\,dx&=\int\left(\frac{3}{x+1}-\frac{1}{(x+1)^2}-\frac{2}{(x+1)^3}\right)\,dx\\
&=3\ln|x+1|+\frac{1}{x+1}+\frac{1}{(x+1)^2}+C.
\end{align*}
::::::

## Unrepeated irreducible quadratic factors

If the partial fraction decomposition of a proper rational function contains unrepeated irreducible quadratic factors, then we can directly apply the third and fourth case of {prf:ref}`Thm:RationalFunctions:Cases` to find the answer. We give two examples.

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample5

We will compute the indefinite integral of the rational function $\dfrac{6x^3-7x^2+12x-4}{x^4+5x^2+4}$.

We have

$$
\frac{6x^3-7x^2+12x-4}{x^4+5x^2+4}=\frac{6x^3-7x^2+12x-4}{(x^2+1)(x^2+4)}=\frac{2x+1}{x^2+1}+\frac{4x-8}{x^2+4},
$$

which implies that

\begin{align*}
\int\frac{6x^3-7x^2+12x-4}{x^4+5x^2+4}\,dx&=\int\left(\frac{2x+1}{x^2+1}+\frac{4x-8}{x^2+4}\right)\,dx\\
&= \int\left(\frac{2x}{x^2+1}+\frac{1}{x^2+1}+\frac{4x}{x^2+4}-\frac{8}{x^2+4}\right)\,dx \\
&=\ln(x^2+1)+\arctan(x)+2\ln(x^2+4)-4\arctan(\tfrac{1}{2}x)+C.
\end{align*}

::::::

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample6
We evaluate $\displaystyle\int\frac{2x+5}{x^2+4x+8}\,dx$.

Note that $x^2+4x+8=(x+2)^2+4$ and with that the integrand already becomes a partial fraction decomposition. Hence, we have

\begin{align*}
\int\frac{2x+5}{x^2+4x+8}\,dx&=\int\frac{2(x+2)+1}{(x+2)^2+4}\,dx\\
&=\int\frac{2(x+2)}{(x+2)^2+4}+\frac{1}{(x+2)^2+4}\,dx\\
&= \ln\left((x+2)^2+4\right)+\frac{1}{2}\arctan\left(\frac{x+2}{2}\right)+C \\
&= \ln(x^2+4x+8)+\frac{1}{2}\arctan\left(\frac{x+2}{2}\right)+C.
\end{align*}

Note that in this case we also could have used the substitution $u=x+2$ to find the answer:

\begin{align*}
\int\frac{2x+5}{x^2+4x+8}\,dx&=\int\frac{2u+1}{u^2+4}\,du\\
&=\ln(u^2+4)+\frac{1}{2}\arctan\left(\frac{u}{2}\right)+C\\
&=\ln((x+2)^2+4)+\frac{1}{2}\arctan\left(\frac{x+2}{2}\right)+C\\
&=\ln(x^2+4x+8)+\frac{1}{2}\arctan\left(\frac{x+2}{2}\right)+C.
\end{align*}

::::::

## Repeated irreducible quadratic factors

If the partial fraction decomposition of a proper rational function contains repeated irreducible quadratic factors, then we can directly apply the fifth and sixth case of {prf:ref}`Thm:RationalFunctions:Cases` to find the answer. We give several examples.

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample7
Consider $\displaystyle\int\frac{2x^7+x^6+12x^5+5x^4+16x^3+8x^2+4x+4}{(x^2+1)^2(x^2+2)^2}\,dx$.

We have, using some tedious computations, that the partial fraction decomposition of the integrand is

$$
\frac{2x^7+x^6+12x^5+5x^4+16x^3+8x^2+4x+4}{(x^2+1)^2(x^2+2)^2} = \frac{2x+1}{x^2+1}-\frac{2x}{(x^2+1)^2}+\frac{4x}{(x^2+2)^2}.
$$

Hence we have

\begin{align*}
&\int\frac{2x^7+x^6+12x^5+5x^4+16x^3+8x^2+4x+4}{(x^2+1)^2(x^2+2)^2}\,dx\\
&{}\quad\quad{}=\int\left(\frac{2x+1}{x^2+1}-\frac{2x}{(x^2+1)^2}+\frac{4x}{(x^2+2)^2}\right)\,dx\\
&{}\quad\quad{}=\ln(x^2+1)+\arctan(x)+\frac{1}{2(x^2+1)^2}-\frac{1}{(x^2+2)^2}+C.
\end{align*}
::::::

Note that we were lucky that the partial fraction decomposition did not contain terms for the sixth case in {prf:ref}`Thm:RationalFunctions:Cases`. Otherwise, we had to deal with multiples of the integrals 

$$
\int\frac{dx}{(x^2+1)^2}\quad\text{and}\quad\int\frac{dx}{(x^2+2)^2}.
$$ 

To show you how to handle these integrals, we give two short examples next. For more details we refer to {numref}`sec:Integration:TrigFunctions`.

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsRepeatedExample1
We integrate $\dfrac{1}{(1+x^2)^2}$ over the interval $[0,1]$.

Using the substitution $x=\tan(t)$ from case 6 in {prf:ref}`Thm:RationalFunctions:Cases`, we find that $t=0$ if $x=0$ and $t=\frac{1}{4}\pi$ if $x=1$. Hence, we have

$$
\int_0^1\frac{1}{(1+x^2)^2}\,dx=\int_0^{\frac{1}{4}\pi}\cos^2(t)\,dt.
$$

Now we use $\cos^2(t)=\frac{1}{2}(1+\cos(2t))$ to find that

\begin{align*}
\int_0^1\frac{1}{(1+x^2)^2}\,dx&=\int_0^{\frac{1}{4}\pi}\cos^2(t)\,dt \\
&=\frac{1}{2}\int_0^{\frac{1}{4}\pi}(1+\cos(2t))\,dt\\
&=\bigg[\frac{1}{2}t+\frac{1}{4}\sin(2t)\bigg]_0^{\frac{1}{4}\pi}=\frac{1}{8}\pi+\frac{1}{4}.
\end{align*}
::::::

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsRepeatedExample2
We determine $\displaystyle\int_{1}^{\sqrt{3}}\frac{dx}{(1+x^2)^3}$.

Again we use $x=\tan(t)$ and therefore

$$
\int_1^{\sqrt{3}}\frac{dx}{(1+x^2)^3}=\int_{\frac{\pi}{4}}^{\frac{\pi}{3}}\cos^4(t)\,dt.
$$

Now we use $\cos^2(t)=\frac{1}{2}(1+\cos(2t))$ to find that

\begin{align*}
\cos^4(t)&=\frac{1}{4}(1+\cos(2t))^2=\frac{1}{4}(1+2\cos(2t)+\cos^2(2t))\\
&=\frac{1}{4}+\frac{1}{2}\cos(2t)+\frac{1}{2}\cos^2(2t).
\end{align*}
Finally, using $\cos^2(2t)=\frac{1}{2}(1+\cos(4t))$, we obtain

$$
\cos^4(t)=\frac{1}{4}+\frac{1}{2}\cos(2t)+\frac{1}{8}+\frac{1}{8}\cos^2(4t)=\frac{3}{8}+\frac{1}{2}\cos(2t)+\frac{1}{8}\cos(4t).
$$

Hence, we have

\begin{align*}
\int_1^{\sqrt{3}}\frac{dx}{(1+x^2)^3}&=\int_{\frac{\pi}{4}}^{\frac{\pi}{3}}\cos^4(t)\,dt=\int_{\frac{\pi}{4}}^{\frac{\pi}{3}}\left(\frac{3}{8}+\frac{1}{2}\cos(2t)+\frac{1}{8}\cos(4t)\right)\,dt\\
&=\bigg[\frac{3}{8}t+\frac{1}{4}\sin(2t)+\frac{1}{32}\sin(4t)\bigg]_{\frac{\pi}{4}}^{\frac{\pi}{3}}
&= \frac{\pi}{32} + \frac{7\sqrt{3} - 16}{64}.
\end{align*}
::::::

## Grasple exercises
