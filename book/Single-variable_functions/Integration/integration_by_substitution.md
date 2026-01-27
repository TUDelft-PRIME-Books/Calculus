(Sec:Integration:Substitution)=

# Integration by substitution

## Introduction

In the previous section we have seen how to determine definite and indefinite integrals of standard functions and linear combinations of these standard functions.

We have also seen how to apply the fundamental theorem of calculus to evaluate definite integrals. However, in many cases it is not possible to directly use these methods to evaluate (in)definite integrals. For example, consider the following indefinite integral:

$$
\displaystyle\int\cos(x)e^{\sin(x)}\,dx.
$$

Although the integrand is composed of three standard functions, we cannot directly apply the formulas from {numref}`Tab:Integration:StandardIndefiniteIntegrals` to evaluate this integral. We can also not use {prf:ref}`Th:Integration:IndefiniteProperties` to split the integral into simpler integrals, since the integrand is a product of functions instead of a sum of functions ánd one standard function is nested inside another standard function.

In this section we introduce the method of **integration by substitution**, which is a very powerful method to evaluate integral such as in the example above.

## Substitution for indefinite integrals

The method of **integration by substitution** is based on the chain rule for differentiation: if $g$ is differentiable at $x$ and $F$ is differentiable at $g(x)$, then

$$
\frac{d}{dx}F(g(x))=F'(g(x))g'(x).
$$

Now consider the indefinite integral $\displaystyle\int F'(g(x))g'(x)\,dx$:

\begin{align*}
\int F'(g(x))g'(x)\,dx &= \int \frac{d}{dx}F(g(x))\,dx\\
&= F(g(x))+C.
\end{align*}

If we would assume that $F'=f$, so $F$ is an antiderivative of $f$, then we have $F'(g(x))=f(g(x))$ and therefore

$$
\int f(g(x))g'(x)\,dx=F(g(x))+C\quad\text{with}\quad C\in\mathbb{R}.
$$

This leads to the following theorem:

::::::{prf:Theorem} Integration by substitution for indefinite integrals
:label: Thm:Integration:SubstitutionIndefiniteIntegral
If $u=g(x)$ is a differentiable function whose range is an interval $I$ and $f$ is continuous on $I$, then

:::{math}
:label: Eq:Integration:SubstitutionIndefiniteIntegral

\int f(g(x))g'(x)\,dx=\int f(u)\,du.
:::

::::::

::::{admonition} Proof of {prf:ref}`Thm:Integration:SubstitutionIndefiniteIntegral`
:class: tudproof, dropdown
Let $F$ be an antiderivative of $f$ on $I$, so $F'=f$. Then:

\begin{align*}
\int f(g(x))g'(x)\,dx &= \int F'(g(x))g'(x)\,dx\\
&= \int \frac{d}{dx}F(g(x))\,dx\\
&= F(g(x))+C \\
&= \left[F(u)+C\right]_{u=g(x)}\\
&= \left[\int f(u)\,du\right]_{u=g(x)} \\
&= \int f(u)\,du.
\end{align*}
::::

::::::{prf:notation}
:label: Rm:Integration:SubstitutionNotation

In {prf:ref}`Thm:Integration:SubstitutionIndefiniteIntegral` the indefinite integral on the left in Equation {eq}`Eq:Integration:SubstitutionIndefiniteIntegral` is expressed in terms of the variable $x$, which means that working out the integral on the left gives a function of $x$.

The indefinite integral on the right in Equation {eq}`Eq:Integration:SubstitutionIndefiniteIntegral` must therefore also be expressed in terms of the variable $x$. This is done by substituting back $u=g(x)$ after having worked out the integral on the right.

A more concise notation for writing Equation {eq}`Eq:Integration:SubstitutionIndefiniteIntegral` is to write

$$
\int f(g(x))g'(x)\,dx=\left[\int f(u)\,du\right]_{u=g(x)}.
$$

We however will not use this notation in the sequel, and stick to the notation in Equation {eq}`Eq:Integration:SubstitutionIndefiniteIntegral`.
::::::

::::::{prf:remark}
:label: Rm:Integration:SubstitutionDifferential
If $u=g(x)$, we often use that $du=g'(x)\,dx$.

Furthermore, the method of integration by substitution rests on identifying parts of the integrand as $f(g(\ldots))$ and $g'(\ldots)$. In practice, this means that we look for a part of the integrand:

- that is nested inside another function.
- whose derivative is also part of the integrand and is multiplied by a differential $d\ldots$ (which depends on the variable of integration).

::::::

Let us return to the indefinite integral at the start of this section:

::::::{prf:Example}
:label: Ex:Integration:SubstitutionIndefiniteIntegralExample1
Consider $\displaystyle\int\cos(x)e^{\sin(x)}\,dx$. If we look at the integrand, we see that the term $\sin(x)$ is nested inside the exponential function $e^{\ldots}$, and that the derivative of $\sin(x)$, which is $\cos(x)$, is also part of the integrand.

If we now set $u=\sin(x)$, we obtain that $du=\cos(x)\,dx$. Hence, we find that

$$
\int\cos(x)e^{\sin(x)}\,dx= \int e^{\sin(x)}\,\cos(x)\,dx =\int e^u\,du=e^u+C=e^{\sin(x)}+C.
$$

::::::

Sometimes we cannot exactly find the derivative of the inner function in the integrand, but a constant multiple of this derivative. In that case we can often factor out this constant multiple from the integral, which is shown in the next example.

::::::{prf:Example}
:label: Ex:Integration:SubstitutionIndefiniteIntegralExample2
Consider $\displaystyle\int\frac{t}{\sqrt{1-t^2}}\,dt$ for $-1<t<1$.

We see that the term $1-t^2$ is nested inside the square root function $\sqrt{\ldots}$. The derivative of $1-t^2$ is $-2t$, which we do not see within the integrand. However, we do see the term $t\,dt$ in the integrand, which is equal to $-\dfrac{1}{2}(-2t\,dt)$.

To use this, we first rewrite the integral as

$$
\int\frac{t}{\sqrt{1-t^2}}\,dt=\int-\dfrac{1}{2}\frac{1}{\sqrt{1-t^2}}\,(-2t)\,dt.
$$

If we set $u=1-t^2$, we obtain that $du=-2t\,dt$. Hence, we find that

\begin{align*}
\int\frac{t}{\sqrt{1-t^2}}\,dt &= \int-\dfrac{1}{2}\frac{1}{\sqrt{1-t^2}}\,(-2t)\,dt \\
&=\int-\frac{1}{2}\frac{1}{\sqrt{u}}\,du \\
&=-\sqrt{u}+C \\
&=-\sqrt{1-t^2}+C.
\end{align*}

::::::

The method of integration by substitution can also be used to evaluate integrals where identifying the inner function is not immediately obvious, as shown in the next example.

::::::{prf:Example}
:label: Ex:Integration:SubstitutionIndefiniteIntegralExample3
Consider $\displaystyle\int\frac{1}{(1+x)\sqrt{x}}\,dx$ for $x>0$.

Inspection of the integrand does not give an immediate indication of what the inner function could be. To obtain candidates, we may try to rewrite the integrand. For example, we can write

$$
\int\frac{1}{(1+x)\sqrt{x}}\,dx = \int\frac{1}{\sqrt{x}}\,\frac{1}{1+x}\,dx,
$$

which might indicate that we could pick $g'(x)\,dx=\dfrac{1}{1+x}\,dx$. We could also write

$$
\int\frac{1}{(1+x)\sqrt{x}}\,dx = \int\frac{1}{1+x}\,\frac{1}{\sqrt{x}}\,dx,
$$

which might indicate that we could pick $g'(x)\,dx=\dfrac{1}{\sqrt{x}}\,dx$.

Because we have two options, we will try both options.

If we set $u=\ln(1+x)$, we obtain that $du=\dfrac{1}{1+x}\,dx$. Hence, we find that

\begin{align*}
\int\frac{1}{(1+x)\sqrt{x}}\,dx &= \int\frac{1}{\sqrt{x}}\,\frac{1}{1+x}\,dx \\
&= \int\frac{1}{\sqrt{e^u-1}}\,du.
\end{align*}

This integral is not a standard integral, so processing might be hard. So before continuing, we try the other option.

If we set $u=\sqrt{x}$, we obtain that $du=\dfrac{1}{2\sqrt{x}}\,dx$ or $\dfrac{1}{\sqrt{x}}\,dx=2\,du$. Hence, we find that

\begin{align*}
\int\frac{1}{(1+x)\sqrt{x}}\,dx &= \int\frac{1}{1+x}\,\frac{1}{\sqrt{x}}\,dx \\
&= \int\frac{2}{1+u^2}\,du \\
&= 2\arctan(u)+C \\
&= 2\arctan(\sqrt{x})+C.
\end{align*}

Because the second option led to a standard integral, we have found the solution and we do not need to revisit the first option.

::::::

Although we have not made it explicit in the examples so far, in many case we used, if $u=g(x)$, that also $x=g^{-1}(u)$. For example, in {prf:ref}`Ex:Integration:SubstitutionIndefiniteIntegralExample3`, when we set $u=\sqrt{x}$, we also used that $x=u^2$, and with the first option $u=\ln(1+x)$ we used $x=e^u-1$. This is not always necessary, but it can be useful in some cases. If we introduce the notation $h(x)=g^{-1}(x)$, then we have $x=h(u)$ and also $dx=h'(u)\,du$. Using this notation, we can directly replace each $x$ in the integrand with $h(u)$ and $dx$ with $h'(u)\,du$.

We summarise this in the next algorithm:

::::::{prf:algorithm}
:label: Alg:Integration:SubstitutionIndefiniteIntegral

To evaluate an indefinite integral of the form $\displaystyle\int I(x)\,dx$ using the method of integration by substitution, follow these steps:

1. Select the inner function $g(x)$ in the integrand $I(x)$.
2. Set $u=g(x)$ and define $h(u)=g^{-1}(u)$.
3. Compute $dx=h'(u)\,du$,
4. Substitute $g(x)$ with $u$, $x$ with $h(u)$, and $dx$ with $h'(u)\,du$ in the integral.
5. Evaluate the resulting indefinite integral using standard methods.

::::::

We will apply this algorithm in the next example:

::::::{prf:Example}
:label: Ex:Integration:SubstitutionIndefiniteIntegralExample4

Consider $\displaystyle\int\frac{1}{(1+x)\sqrt{x}}\,dx$ for $x>0$ again.

We selected $u=\sqrt{x}$ previously as the inner function, which implies that $x=h(u)=u^2$ and therefore $dx=2u\,du$. The five steps of {prf:ref}`Alg:Integration:SubstitutionIndefiniteIntegral` then lead to:

1. We have $g(x)=\sqrt{x}$.
2. We set $u=\sqrt{x}$ and define $h(u)=u^2$.
3. We compute $dx=2u\,du$.
4. and 5. We substitute in the integral and evaluate:

\begin{align*}
\int\frac{1}{(1+x)\sqrt{x}}\,dx &= \int\frac{1}{(1+u^2)u}\,2u\,du \\
&= \int\frac{2}{1+u^2}\,du \\
&= 2\arctan(u)+C \\
&= 2\arctan(\sqrt{x})+C.
\end{align*}

::::::

We will not explicitly use {prf:ref}`Alg:Integration:SubstitutionIndefiniteIntegral` in the sequel, but the steps of this algorithm will be followed implicitly.

::::{exercise}
:label: Exc:Integration:SubstitutionIndefiniteIntegralRationalFunctions
Prove that for $\alpha\in\mathbb{R}\setminus\{0\}$ we have

$$
\int\frac{1}{x^2+\alpha^2}\,dx=\frac{1}{\alpha}\arctan\left(\frac{x}{\alpha}\right)+C
$$

and

$$
\int\frac{x}{x^2+\alpha^2}\,dx=\frac{1}{2}\ln(x^2+\alpha^2)+C.
$$

These formulas will be used frequently in the section on integration of rational functions.
::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionIndefiniteIntegralRationalFunctions`
:class: solution, dropdown
Using the substitution $\dfrac{x}{\alpha}=t$ or $x=\alpha t$, which implies that $dx=\alpha\,dt$, we find that

$$
\int\frac{1}{x^2+\alpha^2}\,dx=\frac{1}{\alpha^2}\int\frac{1}{\left(\frac{x}{\alpha}\right)^2+1}\,dx=\frac{1}{\alpha^2}\int\frac{1}{t^2+1}\alpha\,dt=\frac{1}{\alpha}\arctan(t)+C=\frac{1}{\alpha}\arctan\left(\frac{x}{\alpha}\right)+C
$$

and

$$
\begin{align*}
\int\frac{x}{x^2+\alpha^2}\,dx&=\frac{1}{\alpha^2}\int\frac{x}{\left(\frac{x}{\alpha}\right)^2+1}\,dx=\frac{1}{\alpha^2}\int\frac{\alpha t}{t^2+1}\alpha\,dt=\int\frac{t}{t^2+1}\,dt\\
&=\frac{1}{2}\ln(t^2+1)+C=\frac{1}{2}\ln\left(\left(\frac{x}{\alpha}\right)^2+1\right)+C\\
&=\frac{1}{2}\ln\left(\frac{x^2+\alpha^2}{\alpha^2}\right)+C=\frac{1}{2}\ln(x^2+\alpha^2)-\frac{1}{2}\ln(\alpha^2)+C.
\end{align*}
$$

Note that $-\frac{1}{2}\ln(\alpha^2)$ is a constant. So $-\frac{1}{2}\ln(\alpha^2)+C$ can be replaced by another arbitrary constant of integration.

Note that $\frac{1}{2}\ln(x^2+\alpha^2)$ can also be written as $\ln\sqrt{x^2+\alpha^2}$.

Note that the second formula also holds for $\alpha=0$.
:::

## Substitution for definite integrals

Now we have some experience with the method of integration by substitution for indefinite integrals, we can also apply this method to definite integrals.

Consider the definite integral $\displaystyle\int_a^b f(g(x))g'(x)\,dx$ and assume $f$, $g$, $a$ and $b$ are such that the indefinite integral $\displaystyle\int f(g(x))g'(x)\,dx$ can be evaluated using {prf:ref}`Thm:Integration:SubstitutionIndefiniteIntegral`. Also assume that $F$ is an antiderivative of $f$. Then we have:

\begin{align*}
\int f(g(x))g'(x)\,dx &= \int f(u)\,du \\
&= F(u)+C \\
&= F(g(x))+C.
\end{align*}

For the definite integral we then find that

\begin{align*}
\int_a^b f(g(x))g'(x)\,dx &= \Big[F(g(x))\Big]_a^b \\
&= F(g(b))-F(g(a)) \\
&= \Big[F(u)\Big]_{u=g(a)}^{u=g(b)} \\
&= \int_{g(a)}^{g(b)} f(u)\,du.
\end{align*}

But this means that we have proved the following theorem:

::::::{prf:Theorem} Substitution for definite integrals
:label: Thm:Integration:SubstitutionDefiniteIntegral
If $g'$ is continuous on $[a,b]$ and $f$ is continuous on the range of $u=g(x)$, then

$$
\int_a^b f(g(x))g'(x)\,dx=\int_{g(a)}^{g(b)} f(u)\,du.
$$

::::::


:::{prf:remark}
:label: Rm:Integration:NoBacksies

This also means that when we use the method of substitution for definite integrals, we do not need to substitute back to the original variable after having worked out the integral on the right-hand side.
:::

:::{prf:remark}
:label: Rm:Integration:Limits

Note that the choice $u=g(x)$ leads to new limits of integration: if $x=a$ then $u=g(a)$, and if $x=b$ then $u=g(b)$.

Be very aware that these new limits may be in descending order if $g(a)>g(b)$ eval if $a>b$ originally.
:::

{prf:ref}`Alg:Integration:SubstitutionIndefiniteIntegral` can easily be adapted to definite integrals:

::::::{prf:algorithm}
:label: Alg:Integration:SubstitutionDefiniteIntegral

To evaluate a definite integral of the form $\displaystyle\int_a^b I(x)\,dx$ using the method of integration by substitution, follow these steps:

1. Select the inner function $g(x)$ in the integrand $I(x)$.
2. Set $u=g(x)$ and define $h(u)=g^{-1}(u)$.
3. Compute $dx=h'(u)\,du$,
4. Substitute $g(x)$ with $u$, $x$ with $h(u)$, $dx$ with $h'(u)\,du$, $a$ with $g(a)$, and $b$ with $g(b)$ in the integral.
5. Evaluate the resulting definite integral using standard methods.

::::::


::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralExample1
We want to determine $\displaystyle\int_1^e\frac{\ln(x)}{x}\,dx$.

Inspection of the integrand shows two option for the inner function: we could pick either $g(x)=\ln(x)$ or $g(x)=x$. If we would use $g(x)=x$, we would end up with the exact same integral on the right-hand side, so this is not useful. Therefore, we pick $g(x)=\ln(x)$.

If we set $u=\ln(x)$, then we have $du=\dfrac{1}{x}\,dx$. Furthermore, we have if $x=1$ then $u=\ln(1)=0$, and if $x=e$ then $u=\ln(e)=1$. Hence, we find that

$$
\int_1^e\frac{\ln(x)}{x}\,dx=\int_0^1u\,du=\frac{1}{2}u^2\bigg|_0^1=\frac{1}{2}.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralExample2
Let us evaluate $\displaystyle\int_0^{\frac{1}{2}}\frac{\arcsin(x)}{\sqrt{1-x^2}}\,dx$.

If we set $u=\arcsin(x)$, then we have $du=\dfrac{1}{\sqrt{1-x^2}}\,dx$. Furthermore, we have if $x=0$ then $u=\arcsin(0)=0$, and if $x=\frac{1}{2}$ then $u=\arcsin(\frac{1}{2})=\frac{1}{6}\pi$. Hence, we find that

$$
\int_0^{\frac{1}{2}}\frac{\arcsin(x)}{\sqrt{1-x^2}}\,dx=\int_0^{\frac{1}{6}\pi}u\,du=\frac{1}{2}u^2\bigg|_0^{\frac{1}{6}\pi}=\frac{1}{2}\cdot\frac{1}{36}\pi^2=\frac{1}{72}\pi^2.
$$

Note that we did not select $u=\sqrt{1-x^2}$, because this would have led to a more complicated integral. Also, we recognised that $\dfrac{1}{\sqrt{1-x^2}}$ is the derivative of $\arcsin(x)$, which led us to the correct choice for the inner function.

::::::

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralExample3
We are going to calculate $\displaystyle\int_{\frac{1}{4}}^1\frac{e^{\frac{1}{\sqrt{x}}}}{x\sqrt{x}}\,dx$.

If we set $u=\frac{1}{\sqrt{x}}$, then we have $du=-\dfrac{1}{2x\sqrt{x}}\,dx$ or $\dfrac{1}{x\sqrt{x}}\,dx=-2\,du$. Furthermore, we have if $x=\frac{1}{4}$ then $u=\frac{1}{\sqrt{\frac{1}{4}}}=\frac{1}{\frac{1}{2}}=2$, and if $x=1$ then $u=\dfrac{1}{\sqrt{1}}=1$. Now we find that

\begin{align*}
\int_{\frac{1}{4}}^1\frac{e^{\frac{1}{\sqrt{x}}}}{x\sqrt{x}}\,dx &= \int_2^1 e^u\left(-2\right)\,du \\
&= \int_1^2 2e^u\,du \\
&= 2e^u\bigg|_1^2 \\
&= 2(e^2-e).
\end{align*}

::::::

In the section on definite integrals, in {prf:ref}`Th:Integration:DefinitePropertiesArea` we have already seen the following intuitively result, which can now be proved using a substitution:

::::::{prf:Theorem}
:label: Thm:Integration:OddEven
Let $f$ be a continuous function defined on $[-a,a]$. Then we have

(a) If $f$ is *odd*, so $f(-x)=-f(x)$ for all $x$, then $\displaystyle\int_{-a}^af(x)\,dx=0$.

(b) If $f$ is *even*, so $f(-x)=f(x)$ for all $x$, then $\displaystyle\int_{-a}^af(x)\,dx=2\int_0^af(x)\,dx$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Integration:OddEven`
:class: tudproof, dropdown
In both cases we use the substitution $x=-t$ with $dx=-dt$:

$$
\int_{-a}^0f(x)\,dx=-\int_a^0f(-t)\,dt=\int_0^af(-t)\,dt=\int_0^af(-x)\,dx.
$$

(a) If $f(-x)=-f(x)$ for all $x$, we have $\displaystyle\int_{-a}^0f(x)\,dx=-\int_0^af(x)\,dx$, which implies that 

$$
\int_{-a}^af(x)\,dx=\int_{-a}^0f(x)\,dx+\int_0^af(x)\,dx=0.
$$

(b) If $f(-x)=f(x)$ for all $x$, we have $\displaystyle\int_{-a}^0f(x)\,dx=\int_0^af(x)\,dx$, which implies that 

$$
\int_{-a}^af(x)\,dx=\int_{-a}^0f(x)\,dx+\int_0^af(x)\,dx=2\int_0^af(x)\,dx.
$$

::::::

::::{exercise}
:label: Exc:Integration:SubstitutionCos
Consider the integral $\displaystyle\int_{\frac{1}{2}}^2\cos\left(x-\frac{1}{x}\right)\,dx$.

(a) Use the substitution $x=\dfrac{1}{t}$ to show that

$$
\int_{\frac{1}{2}}^2\cos\left(x-\frac{1}{x}\right)\,dx=\int_{\frac{1}{2}}^2\frac{1}{t^2}\cos\left(t-\frac{1}{t}\right)\,dt.
$$

(b) Add both forms of the integral and use the substitution $u=x-\dfrac{1}{x}$ to evaluate the integral.

::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionCos`
:class: solution, dropdown

(a) Using the substitution $x=\dfrac{1}{t}$ we obtain:

$$
\int_{\frac{1}{2}}^2\cos\left(x-\frac{1}{x}\right)\,dx=\int_2^{\frac{1}{2}}\cos\left(\frac{1}{t}-t\right)\left(-\frac{1}{t^2}\right)\,dt
=\int_{\frac{1}{2}}^2\frac{1}{t^2}\cos\left(t-\frac{1}{t}\right)\,dt.
$$

(b) This implies that

$$
2\int_{\frac{1}{2}}^2\cos\left(x-\frac{1}{x}\right)\,dx=\int_{\frac{1}{2}}^2\left(1+\frac{1}{x^2}\right)\cos\left(x-\frac{1}{x}\right)\,dx.
$$

Now we apply the substitution $u=x-\dfrac{1}{x}$ and therefore $du=\left(1+\dfrac{1}{x^2}\right)\,dx$:

$$
\int_{\frac{1}{2}}^2\cos\left(x-\frac{1}{x}\right)\,dx=\frac{1}{2}\int_{-\frac{3}{2}}^{\frac{3}{2}}\cos(u)\,du
=\frac{1}{2}\bigg[\sin(u)\bigg]_{-\frac{3}{2}}^{\frac{3}{2}}=\sin\left(\tfrac{3}{2}\right).
$$

:::

## Grasple exercises

64141, 64618, 64879, 75957, 64878, 64599, 64834, 65945, 64831, 64653, 64660, 64601, 64825, 64652, 64835, 64850, 64648, 64830, 64826, 64832, 64827, 64881, 75951, 64877