(Sec:Integration:Substitution)=

# Integration by substitution

## Introduction

In the previous section we have seen how to determine definite and indefinite integrals of standard functions and linear combinations of these standard functions.

We have also seen how to apply the fundamental theorem of calculus to evaluate definite integrals. However, in many cases it is not possible to directly use these methods to evaluate (in)definite integrals. For example, consider the following indefinite integral:

$$
\displaystyle\int\cos(x)e^{\sin(x)}\,dx.
$$

Although the integrand is composed of three standard functions, we cannot directly apply the formulas from {numref}`Tab:Integration:StandardIndefiniteIntegrals` to evaluate this integral. We can also not use {prf:ref}`Thm:Integration:IndefiniteProperties` to split the integral into simpler integrals, since the integrand is a product of functions instead of a sum of functions and one standard function is nested inside another standard function.

In this section we introduce the method of **integration by substitution**, which is a very powerful method to evaluate integrals such as in the example above.

## Indefinite integrals

The method of **integration by substitution** is based on the {prf:ref}`chain rule <Thm:Chainrule:Chainrule>` for differentiation: if $g$ is differentiable at $x$ and $F$ is differentiable at $g(x)$, then

$$
\frac{d}{dx}F(g(x))=F'(g(x))g'(x).
$$

Now consider the indefinite integral $\displaystyle\int F'(g(x))g'(x)\,dx$:

\begin{align*}
\int F'(g(x))g'(x)\,dx &= \int \frac{d}{dx}F(g(x))\,dx\\
&= F(g(x))+C.
\end{align*}

If we assume that $F'=f$, so $F$ is an antiderivative of $f$, then we have $F'(g(x))=f(g(x))$ and therefore

$$
\int f(g(x))g'(x)\,dx=F(g(x))+C\quad\text{with}\quad C\in\mathbb{R}.
$$

This leads to the following theorem:

::::::{prf:Theorem} Integration by substitution for indefinite integrals
:label: Thm:Integration:SubstitutionIndefiniteIntegral
If $u=g(x)$ is a differentiable function whose range is an interval $I$ and $f$ is integrable on $I$, then

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
&= \left[\int f(u)\,du\right]_{u=g(x)}.
\end{align*}
::::

::::::{prf:notation}
:label: Rm:Integration:SubstitutionNotation

In {prf:ref}`Thm:Integration:SubstitutionIndefiniteIntegral` the indefinite integral on the left in Equation {eq}`Eq:Integration:SubstitutionIndefiniteIntegral` is expressed in terms of the variable $x$, which means that evaluation of the integral on the left gives a function of $x$.

However, the indefinite integral on the right in Equation {eq}`Eq:Integration:SubstitutionIndefiniteIntegral` is expressed in terms of the variable $u$. In order to rewrite this in terms of the variable $x$ we might use the substitution $u=g(x)$ after evaluating the integral on the right.

A more precise notation for writing Equation {eq}`Eq:Integration:SubstitutionIndefiniteIntegral` is

$$
\int f(g(x))g'(x)\,dx=\left[\int f(u)\,du\right]_{u=g(x)}.
$$

However, we will not use this notation in the sequel, and stick to the notation in Equation {eq}`Eq:Integration:SubstitutionIndefiniteIntegral`.
::::::

::::::{prf:remark}
:label: Rm:Integration:SubstitutionDifferential
If $u=g(x)$, we often use that $du=g'(x)\,dx$.

Furthermore, the method of integration by substitution relies on identifying parts of the integrand as $f(g(x))$ and $g'(x)$. In practice, this means that we look for a part of the integrand $g'(x)$:

- That is the derivative of a known function $g(x)$.
- That can be factored out of the integrand.
- For which $g(x)$, up to a multiplicative constant, is present in the other part $f(g(x))$ of the integrand.

::::::

Let us return to the indefinite integral at the start of this section:

::::::{prf:Example}
:label: Ex:Integration:SubstitutionIndefiniteIntegralExample1
Consider $\displaystyle\int\cos(x)e^{\sin(x)}\,dx$. If we look at the integrand, we recognise the simpler part $\cos(x)$ as the derivative of $\sin(x)$, which is present in the more complicated part of the integrand.

If we now set $u=\sin(x)$, we obtain that $du=\cos(x)\,dx$. Hence, we find that

$$
\int\cos(x)e^{\sin(x)}\,dx= \int e^{\sin(x)}\,\cos(x)\,dx =\int e^u\,du=e^u+C=e^{\sin(x)}+C.
$$

::::::

Sometimes we need a constant multiple of the function $g$ of which a derivative $g'$ is present in the integrand. In that case we can factor out this constant multiple from the integral, which is shown in the next examples.

::::::{prf:Example}
:label: Ex:Integration:SubstitutionIndefiniteIntegralExample2
Consider $\displaystyle\int t^2\cos(t^3)\,dt$.

We recognise $t^2$ as the derivative of $\frac{1}{3}t^3$ while $t^3$ is present in the other part of the integrand. The derivative of $t^3$ is $3t^2$, which is a multiple of $t^2$. However, $t^2\,dt$ is equal to $\frac{1}{3}\cdot 3t^2\,dt$.

To use this, we first rewrite the integral as

$$
\int t^2\cos(t^3)\,dt=\int\frac{1}{3}\cos(t^3)\cdot 3t^2\,dt.
$$

If we set $u=t^3$, we obtain that $du=3t^2\,dt$. Hence, we find that

\begin{align*}
\int t^2\cos(t^3)\,dt&= \int\frac{1}{3}\cos(t^3)\cdot 3t^2\,dt\\
&= \int\frac{1}{3}\cos(u)\,du\\
&= \frac{1}{3}\sin(u)+C\\
&= \frac{1}{3}\sin(t^3)+C.
\end{align*}

::::::

Sometimes we have more than one part of the integrand that we recognise as the derivative of a known function. Then we have to make the right choice as is shown in the next examples.

::::::{prf:Example}
:label: Ex:Integration:SubstitutionIndefiniteIntegralExample3
Consider $\displaystyle\int\frac{1}{(1+x)\sqrt{x}}\,dx$ for $x>0$.

Inspection of the integrand shows two possibilities. 

We recognise $\dfrac{1}{1+x}$ as the derivative of $\ln(1+x)$. However, this function is not present in the integrand.

We also recognise $\dfrac{1}{\sqrt{x}}$ as the derivative of $2\sqrt{x}$ and $\sqrt{x}$ is present in the other part of the integrand, since $1+x=1+\left(\sqrt{x}\right)^2$.

If we set $u=\sqrt{x}$, we obtain that $du=\dfrac{1}{2\sqrt{x}}\,dx$ or $\dfrac{1}{\sqrt{x}}\,dx=2\,du$. Hence, we find that

\begin{align*}
\int\frac{1}{(1+x)\sqrt{x}}\,dx &= \int\frac{1}{1+x}\,\frac{1}{\sqrt{x}}\,dx \\
&= \int\frac{1}{1+u^2}\,2\,du \\
&= 2\arctan(u)+C \\
&= 2\arctan(\sqrt{x})+C.
\end{align*}

::::::

::::::{prf:Example}
:label: Ex:Integration:SubstitutionIndefiniteIntegralExample4
Consider $\displaystyle\int\frac{t}{\sqrt{1-t^2}}\,dt$ for $-1<t<1$.

We recognise $\dfrac{1}{\sqrt{1-t^2}}$ as the derivative of either $\arcsin(t)$ or $-\arccos(t)$. However both functions are not present in the other part of the integrand (being $t$).

We recognise $t$ as the derivative of $\frac{1}{2}t^2$, while $1-t^2$ is present in the other part of the integrand. The derivative of $1-t^2$ is $-2t$, which is a multiple of $t$. However, $t\,dt$ is equal to $-\frac{1}{2}\cdot(-2t)\,dt$.

To use this, we first rewrite the integral as

$$
\int\frac{t}{\sqrt{1-t^2}}\,dt=\int-\frac{1}{2}\frac{1}{\sqrt{1-t^2}}\cdot(-2t)\,dt.
$$

If we set $u=1-t^2$, we obtain that $du=-2t\,dt$. Hence, we find that

\begin{align*}
\int\frac{t}{\sqrt{1-t^2}}\,dt &= \int-\frac{1}{2}\frac{1}{\sqrt{1-t^2}}\cdot(-2t)\,dt \\
&= \int-\frac{1}{2}\frac{1}{\sqrt{u}}\,du \\
&= -\sqrt{u}+C \\
&= -\sqrt{1-t^2}+C.
\end{align*}

Another approach would be to use $t^2$ instead of $1-t^2$:

$$
\int\frac{t}{\sqrt{1-t^2}}\,dt=\int\frac{1}{2}\frac{1}{\sqrt{1-t^2}}\cdot2t\,dt.
$$

If we now set $u=t^2$, then we have $du=2t\,dt$ and we obtain

$$
\int\frac{t}{\sqrt{1-t^2}}\,dt=\int\frac{1}{2}\frac{1}{\sqrt{1-t^2}}\cdot2t\,dt
=\int\frac{1}{2}\frac{1}{\sqrt{1-u}}\,du.
$$

Now we use the techniques of the previous section to obtain

\begin{align*}
\int\frac{t}{\sqrt{1-t^2}}\,dt&= \int\frac{1}{2}\frac{1}{\sqrt{1-u}}\,du\\
&= -\sqrt{1-u}+C\\
&= -\sqrt{1-t^2}+C.
\end{align*}

::::::

Although we have not made it explicit in the examples so far, in many cases we used that, if $u=g(x)$, then also $x=g^{-1}(u)$. For each value of $x$ there should be exactly one value for $u$ and vice versa. For example, in {prf:ref}`Ex:Integration:SubstitutionIndefiniteIntegralExample3`, when we set $u=\sqrt{x}$, we also used that $x=u^2$. This is not always necessary, but it can be useful in some cases. If we introduce the notation $h(x)=g^{-1}(x)$, then we have $x=h(u)$ and also $dx=h'(u)\,du$. Using this notation, we can directly replace each $x$ in the integrand with $h(u)$ and $dx$ with $h'(u)\,du$.

We summarise this in the next algorithm:

::::::{prf:algorithm}
:label: Alg:Integration:SubstitutionIndefiniteIntegral

To evaluate an indefinite integral of the form $\displaystyle\int I(x)\,dx$ using the method of integration by substitution, follow these steps:

1. Select a function $g'(x)$ in the integrand $I(x)$ for which we know an antiderivative $g(x)$.
2. Set $u=g(x)$ and define $x=h(u)=g^{-1}(u)$.
3. Compute $dx=h'(u)\,du$,
4. Substitute $u$ for $g(x)$, $h(u)$ for $x$, $h'(u)\,du$ for $dx$ in the integral.
5. Try to evaluate the resulting indefinite integral using standard methods.

::::::

We will apply this algorithm in the next example:

::::::{prf:Example}
:label: Ex:Integration:SubstitutionIndefiniteIntegralExample5

Consider $\displaystyle\int\frac{1}{(1+x)\sqrt{x}}\,dx$ for $x>0$ again.

We applied $u=\sqrt{x}$ previously, which implies that $x=h(u)=u^2$ and therefore $dx=2u\,du$. The five steps of {prf:ref}`Alg:Integration:SubstitutionIndefiniteIntegral` then lead to:

1. We have $g(x)=\sqrt{x}$.
2. We set $u=g(x)=\sqrt{x}$ and define $x=h(u)=u^2$.
3. We compute $dx=2u\,du$.
4. and 5. We substitute in the integral and evaluate:

\begin{align*}
\int\frac{1}{(1+x)\sqrt{x}}\,dx &= \int\frac{1}{(1+u^2)u}\,2u\,du \\
&= \int\frac{1}{1+u^2}\,2\,du \\
&= 2\arctan(u)+C \\
&= 2\arctan(\sqrt{x})+C.
\end{align*}

::::::

We will not explicitly use {prf:ref}`Alg:Integration:SubstitutionIndefiniteIntegral` in the sequel, but the steps of this algorithm will be followed implicitly.

## Definite integrals

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
If $g'$ is continuous on $[a,b]$ and $f$ is integrable on the range of $u=g(x)$, then

$$
\int_a^b f(g(x))g'(x)\,dx=\int_{g(a)}^{g(b)} f(u)\,du.
$$

::::::


:::{prf:remark}
:label: Rm:Integration:NoBacksies

This also means that when we use the method of substitution for definite integrals, we do not need to substitute back to the original variable after having evaluated the integral on the right-hand side.
:::

:::{prf:remark}
:label: Rm:Integration:Limits

Note that the choice $u=g(x)$ leads to new limits of integration: if $x=a$ then $u=g(a)$, and if $x=b$ then $u=g(b)$.

Be very aware that these new limits may be in descending order if $g(a)>g(b)$ even if $a<b$ originally.
:::

{prf:ref}`Alg:Integration:SubstitutionIndefiniteIntegral` can easily be adapted to definite integrals:

::::::{prf:algorithm}
:label: Alg:Integration:SubstitutionDefiniteIntegral

To evaluate a definite integral of the form $\displaystyle\int_a^b I(x)\,dx$ using the method of integration by substitution, follow these steps:

1. Select a function $g'(x)$ in the integrand $I(x)$ for which we know an antiderivative $g(x)$.
2. Set $u=g(x)$ and define $x=h(u)=g^{-1}(u)$.
3. Compute $dx=h'(u)\,du$,
4. Substitute $u$ for $g(x)$, $h(u)$ for $x$, and $h'(u)\,du$ for $dx$ in the integral.
5. Replace the lower limit $a$ by $g(a)$ and the upper limit $b$ by $g(b)$.
6. Try to evaluate the resulting definite integral using standard methods.

::::::


::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralExample1
We want to determine $\displaystyle\int_1^e\frac{\ln(x)}{x}\,dx$.

Inspecting the integrand we recognise $\dfrac{1}{x}$ as the derivative of $\ln(x)$ which is present in the other part of the integrand. Therefore, we pick $g(x)=\ln(x)$.

If we set $u=\ln(x)$, then we have $du=\dfrac{1}{x}\,dx$. Furthermore, we have if $x=1$ then $u=\ln(1)=0$, and if $x=e$ then $u=\ln(e)=1$. Hence, we find that

$$
\int_1^e\frac{\ln(x)}{x}\,dx=\int_0^1u\,du=\frac{1}{2}u^2\bigg|_0^1=\frac{1}{2}.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralExample2
Consider $\displaystyle\int_{\frac{1}{4}}^1\frac{e^{\frac{1}{\sqrt{x}}}}{x\sqrt{x}}\,dx$.

If we set $u=\dfrac{1}{\sqrt{x}}$, then we have $du=-\dfrac{1}{2x\sqrt{x}}\,dx$ or $\dfrac{1}{x\sqrt{x}}\,dx=-2\,du$. Furthermore, we have if $x=\frac{1}{4}$ then $u=\frac{1}{\sqrt{\frac{1}{4}}}=\frac{1}{\frac{1}{2}}=2$, and if $x=1$ then $u=\frac{1}{\sqrt{1}}=1$. Now we find that

\begin{align*}
\int_{\frac{1}{4}}^1\frac{e^{\frac{1}{\sqrt{x}}}}{x\sqrt{x}}\,dx &= \int_2^1 e^u\left(-2\right)\,du \\
&= \int_1^2 2e^u\,du \\
&= 2e^u\bigg|_1^2 \\
&= 2(e^2-e).
\end{align*}

::::::

:::{warning}
We remark that a sign mistake is easily made in this example. Note that the integrand is positive on $[\frac{1}{4},1]$ and $\frac{1}{4}<1$, so the result should be positive.
:::

In {prf:ref}`Thm:Integration:DefinitePropertiesArea` we have already seen the following intuitive result, which can now be proved using a substitution:

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

## Grasple Exercises

### Indefinite integrals

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bb8a5684-e756-4384-ac03-cd548afa4fba?id=133562
:label: Grasple:133562
:dropdown:
:description: Evaluate the integrals $\displaystyle\int\frac{1}{x^2+\alpha^2}\,dx$ and $\displaystyle\int\frac{x}{x^2+\alpha^2}\,dx$.

::::

:::{note}
So we have

$$
\int\frac{1}{x^2+\alpha^2}\,dx=\frac{1}{\alpha}\arctan\left(\frac{x}{\alpha}\right)+C,\quad\alpha\in\mathbb{R}\setminus\{0\}
$$

and

$$
\int\frac{x}{x^2+\alpha^2}\,dx=\frac{1}{2}\ln(x^2+\alpha^2)+C,\quad\alpha\in\mathbb{R}.
$$

These formulas will be used frequently in {numref}`Sec:Integration:RationalFunctions` on integration of rational functions.
:::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b688b29d-a0a1-4bf5-b412-73acec89cf18?id=75957
:label: Grasple:75957
:dropdown:
:description: Evaluate an integral of the form $\displaystyle\int\frac{1}{x^2+ax+b}\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8aca6ab2-3f03-4785-910f-a1e617f21843?id=64878
:label: Grasple:64878
:dropdown:
:description: Evaluate an integral of the form $\displaystyle\int\frac{1}{\sqrt{\alpha-x^2}}\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c3dc9c7e-50b3-4db7-a274-93f8be2bb7ca?id=64599
:label: Grasple:64599
:dropdown:
:description: Evaluate the indefinite integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/584e6a26-ce71-4686-8777-d77b2db3e215?id=64660
:label: Grasple:64660
:dropdown:
:description: Evaluate the indefinite integral $\displaystyle\int\frac{\cos(\sqrt{x})}{\sqrt{x}}\,dx$.

::::

### Definite integrals

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/248020be-9e36-4d8c-b28f-c8bb059debb5?id=74572
:label: Grasple:74572
:dropdown:
:description: Apply the substitution $u=e^x$ to the definite integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7a17bcbf-2012-4ad3-a6e6-8991a474dc07?id=64601
:label: Grasple:64601
:dropdown:
:description: Evaluate the definite integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5f883700-0be1-476c-ba65-425922459c55?id=64830
:label: Grasple:64830
:dropdown:
:description: Evaluate the definite integral.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/50d4a644-16d5-4437-98c6-861cdf679006?id=64617
:label: Grasple:64617
:dropdown:
:description: Given $\displaystyle\int_0^{\alpha^2}f(x)\,dx$, what is $\displaystyle\int_0^{\alpha}xf(x^2)\,dx$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6e6de53b-a27c-497c-8b43-26421a6323e2?id=133564
:label: Grasple:133564
:dropdown:
:description: Evaluate a definite integral of the form $\displaystyle\int_0^{\alpha}\frac{\arcsin(x)}{\sqrt{1-x^2}}\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4fdebb7b-23ca-4f23-9351-3235fc1faaa6?id=133565
:label: Grasple:133565
:dropdown:
:description: Evaluate a definite integral of the form $\displaystyle\int_0^{\alpha}\frac{\arccos(x)}{\sqrt{1-x^2}}\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/dd6c1502-6c41-4245-89fd-50e011f658f3?id=133566
:label: Grasple:133566
:dropdown:
:description: Evaluate a definite integral of the form $\displaystyle\int_0^{\alpha}\frac{\arctan(x)}{1+x^2}\,dx$.

::::
