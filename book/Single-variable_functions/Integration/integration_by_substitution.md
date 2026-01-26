(Sec:Integration:Substitution)=

# Integration by substitution

In this section we cover:

- Integration by substitution for indefinite integrals
- Integration by substitution for definite integrals
- Even and odd functions

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
\int f(g(x))g'(x)\,dx=F(g(x))+C\quad\text{with}.
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

The indefinite integral on the right in Equation {eqref}`Eq:Integration:SubstitutionIndefiniteIntegral` must therefore also be expressed in terms of the variable $x$. This is done by substituting back $u=g(x)$ after having worked out the integral on the right.

A more concise notation for writing Equation {eqref}`Eq:Integration:SubstitutionIndefiniteIntegral` is to write

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
Consider $\displaystyle\int\cos(x)e^{\sin(x)}\,dx$. If we look at the integrand, we see that the term $\sin(x)$ is nested inside the exponential function $e^{ldots}$, and that the derivative of $\sin(x)$, which is $\cos(x)$, is also part of the integrand.

If we now set $u=\sin(x)$, we obtain that $du=\cos(x)\,dx$. Hence, we find that

$$
\int\cos(x)e^{\sin(x)}\,dx= \int e^{\sin(x)}\,\cos(x)\,dx =\int e^u\,du=e^u+C=e^{\sin(x)}+C.
$$

::::::

Sometimes we cannot exactly find the derivative of the inner function in the integrand, but a constant multiple of this derivative. In that case we can often factor out this constant multiple from the integral, which is shown in the next example.

::::::{prf:Example}
:label: Ex:Integration:SubstitutionIndefiniteIntegralExample2
Consider $\displaystyle\int\frac{t}{\sqrt{1-t^2}}\,dt$ for $-1<t<1$.

We see that the term $1-t^2$ is nested inside the square root function $\sqrt{ldots}$. The derivative of $1-t^2$ is $-2t$, which we do not see within the integrand. However, we do see the term $t\,dt$ in the integrand, which is equal to $-\dfrac{1}{2}(-2t\,dt)$.

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

Inspection of the integrand does not give an immediate indication of what the inner function could be. To onbtain candidates, we may try to rewrite the integrand. For example, we can write

$$
\int\frac{1}{(1+x)\sqrt{x}}\,dx = \int\frac{1}{\sqrt{x}}\,\frac{1}{1+x}\,dx,
$$

which might indicate that we could pick $g'(x)\,dx=\dfrac{1}{1+x}\,dx$. We could also write

$$
\int\frac{1}{(1+x)\sqrt{x}}\,dx = \int\frac{1}{1+x}\,\frac{1}{\sqrt{x}}\,dx,
$$

which might indicate that we could pick $g'(x)\,dx=\dfrac{1}{\sqrt{x}}\,dx$.

Because we have two options, we will try both options.

If we set $u=\ln(1+x)$, we obtain that $du=\dfrac{1}{1+x}\,dx$, but also $x=e^u-1$. Hence, we find that

\begin{align*}
\int\frac{1}{(1+x)\sqrt{x}}\,dx &= \int\frac{1}{\sqrt{x}}\,\frac{1}{1+x}\,dx \\
&= \int\frac{1}{\sqrt{e^u-1}}\,du.
\end{align*}

This integral is not a standard integral, so processing might be hard. So before continuing, we try the other option.

If we set $u=\sqrt{x}$ (or $x=u^2$), we obtain that $du=\dfrac{1}{2\sqrt{x}}\,dx$ or $\dfrac{1}{\sqrt{x}}\,dx=2\,du$. Hence, we find that

\begin{align*}
\int\frac{1}{(1+x)\sqrt{x}}\,dx &= \int\frac{1}{1+x}\,\frac{1}{\sqrt{x}}\,dx \\
&= \int\frac{2}{1+u^2}\,du \\
&= 2\arctan(u)+C \\
&= 2\arctan(\sqrt{x})+C.
\end{align*}

Because the second option led to a standard integral, we have found the solution and we do not need to revisit the first option.

::::::

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

In the section on definite integrals we have already seen the following intuitively result, which can now be proved using a substitution:

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

## Trigonometric substitutions

For certain integrals involving square roots of the form $\sqrt{a^2-x^2}$, $\sqrt{a^2+x^2}$ or $\sqrt{x^2-a^2}$ we might use a **trigonometric substitution** in order to get rid of the square root. This will lead to integrals involving trigonometric functions, which will be treated in the section on integration of trigonometric functions. However, here we will show how the method of trigonometric substitution works.

Note that $1-\sin^2(x)=\cos^2(x)$. So if we set $x=a\sin(t)$ in $\sqrt{a^2-a^2}$ we obtain 

$$
\sqrt{a^2-a^2\sin^2(t)}=\sqrt{a^2\cos^2(t)}=|a\cos(t)|.
$$

Combined with $dx=a\cos(t)\,dt$ this leads to an integral involving trigonometric functions.

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample1
Evaluate $\displaystyle\int_{-1}^1\sqrt{1-x^2}\,dx$.

Solution. Let $x=\sin(t)$, then we have $dx=\cos(t)\,dt$. Furthermore, if $x=-1$ then $t=-\frac{1}{2}\pi$ and if $x=1$ then $t=\frac{1}{2}\pi$. Hence we find that

$$
\int_{-1}^1\sqrt{1-x^2}\,dx=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}|\cos(t)|\cos(t)\,dt.
$$

Note that $\cos(t)\geq0$ for $-\frac{1}{2}\pi\leq t\leq\frac{1}{2}\pi$. Using $\cos^2(t)=\frac{1}{2}(1+\cos(2t))$ we then obtain

$$
\begin{align*}
\int_{-1}^1\sqrt{1-x^2}\,dx&=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\cos^2(t)\,dt=\frac{1}{2}\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}(1+\cos(2t))\,dt\\
&=\bigg[\frac{1}{2}t+\frac{1}{4}\sin(2t)\bigg]_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}=\frac{1}{2}\pi.
\end{align*}
$$

*Remark*: the integral denotes the area of the upper half of the unit circle.
::::::

Instead of using the substitution $x=a\sin(t)$ we may also use the substitution $x=a\cos(t)$, which leads to $dx=-a\sin(t)\,dt$ and 

$$
\sqrt{a^2-x^2}=\sqrt{a^2-a^2\cos^2(t)}=\sqrt{a^2\sin^2(t)}=|a\sin(t)|.
$$ 

::::{exercise}
:label: Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution1
Evaluate $\displaystyle\int_{-1}^1\sqrt{1-x^2}\,dx$ using the substitution $x=\cos(t)$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution1`
:class: solution, dropdown
Let $x=\cos(t)$, then we have $dx=-\sin(t)\,dt$. Furthermore, if $x=-1$ then $t=\pi$ and if $x=1$ then $t=0$. Hence we find that

$$
\int_{-1}^1\sqrt{1-x^2}\,dx=-\int_{\pi}^0|\sin(t)|\sin(t)\,dt=\int_0^{\pi}|\sin(t)|\sin(t)\,dt.
$$

Note that $\sin(t)\geq0$ for $0\leq t\leq\pi$. Using $\sin^2(t)=\frac{1}{2}(1-\cos(2t))$ we then obtain

$$
\begin{align*}
\int_{-1}^1\sqrt{1-x^2}\,dx&=\int_0^{\pi}\sin^2(t)\,dt=\frac{1}{2}\int_0^{\pi}(1-\cos(2t))\,dt\\
&=\bigg[\frac{1}{2}t-\frac{1}{4}\sin(2t)\bigg]_0^{\pi}=\frac{1}{2}\pi.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution2
Evaluate $\displaystyle\int_{-1}^1x^2\sqrt{1-x^2}\,dx$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution2`
:class: solution, dropdown
Let $x=\sin(t)$, then we have $dx=\cos(t)\,dt$. Furthermore, if $x=-1$ then $t=-\frac{1}{2}\pi$ and if $x=1$ then $t=\frac{1}{2}\pi$. Hence we find that

$$
\int_{-1}^1x^2\sqrt{1-x^2}\,dx=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\sin^2(t)|\cos(t)|\cos(t)\,dt
=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\sin^2(t)\cos^2(t)\,dt.
$$

Now we use $\sin(2t)=2\sin(t)\cos(t)$ to find 

$$
\int_{-1}^1x^2\sqrt{1-x^2}\,dx=\frac{1}{4}\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\sin^2(2t)\,dt.
$$

Finally, we have $\sin^2(2t)=\frac{1}{2}(1-\cos(4t))$ which leads to

$$
\begin{align*}
\int_{-1}^1x^2\sqrt{1-x^2}\,dx&=\frac{1}{8}\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}(1-\cos(4t))\,dt\\
&=\bigg[\frac{1}{8}t-\frac{1}{32}\sin(4t)\bigg]_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}=\frac{1}{8}\pi.
\end{align*}
$$

:::

For $\sqrt{a^2+x^2}$ we use the fact that for $x=a\tan(t)$ we have

$$
\sqrt{a^2+x^2}=\sqrt{a^2(1+\tan^2(x))}=\sqrt{\frac{a^2}{\cos^2(t)}}=\left|\frac{a}{\cos(t)}\right|.
$$

Combined with $dx=\dfrac{a}{\cos^2(t)}\,dt$ this will also give rise to an integral involving trigonometric functions.

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample2
Evaluate $\displaystyle\int_0^1\frac{1}{\sqrt{1+x^2}}\,dx$.

Solution. Let $x=\tan(t)$, then we have $dx=\dfrac{dt}{\cos^2(t)}$. Furthermore, if $x=0$ then $t=0$ and if $x=1$ then $t=\frac{1}{4}\pi$. Hence we find that

$$
\int_0^1\frac{1}{\sqrt{1+x^2}}\,dx=\int_0^{\frac{1}{4}\pi}|\cos(t)|\frac{1}{\cos^2(t)}\,dt.
$$

Note that $\cos(t)\geq0$ for $0\leq t\leq\frac{1}{4}\pi$. Hence we have

$$
\int_0^1\frac{1}{\sqrt{1+x^2}}\,dx=\int_0^{\frac{1}{4}\pi}\frac{dt}{\cos(t)}.
$$

In 1668 the Scottish mathematician [James Gregory (1638-1675)](https://en.wikipedia.org/wiki/James_Gregory_(mathematician)) discovered that

$$
\int\frac{dt}{\cos(t)}=\ln\left|\tan(t)+\frac{1}{\cos(t)}\right|+C.
$$

This can be shown as follows

$$
\int\frac{dt}{\cos(t)}=\int\frac{1}{\cos(t)}\cdot\frac{\tan(t)+\dfrac{1}{\cos(t)}}{\tan(t)+\dfrac{1}{\cos(t)}}\,dt=\int\frac{\dfrac{\tan(t)}{\cos(t)}+\dfrac{1}{\cos^2(t)}}{\tan(t)+\dfrac{1}{\cos(t)}}\,dt.
$$

Now we set $u=\tan(t)+\dfrac{1}{\cos(t)}$ which implies that

$$
\frac{du}{dt}=\frac{1}{\cos^2(t)}-\frac{1}{\cos^2(t)}\cdot(-\sin(t))=\frac{1}{\cos^2(t)}+\frac{\tan(t)}{\cos(t)}.
$$

Hence we have $du=\left(\dfrac{1}{\cos^2(t)}+\dfrac{\tan(t)}{\cos(t)}\right)\,dt$. Thus

$$
\int\frac{dt}{\cos(t)}=\int\frac{du}{u}=\ln|u|+C=\ln\left|\tan(t)+\frac{1}{\cos(t)}\right|+C.
$$

We conclude that

$$
\int_0^{\frac{1}{4}\pi}\frac{1}{\cos(t)}\,dt=\left[\ln\left|\tan(t)+\frac{1}{\cos(t)}\right|\right]_0^{\frac{1}{4}\pi}=\ln(1+\sqrt{2}).
$$

and therefore $\displaystyle\int_0^1\frac{1}{\sqrt{1+x^2}}\,dx=\ln(1+\sqrt{2})$.
::::::

::::{exercise}
:label: Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution3
Evaluate $\displaystyle\int_0^1\frac{1}{1+x^2}\,dx$ using the substitution $x=\tan(t)$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution3`
:class: solution, dropdown
Let $x=\tan(t)$, then we have $dx=\left(1+\tan^2(t)\right)\,dt$. Furthermore, if $x=0$ then $t=0$ and if $x=1$ then $t=\frac{1}{4}\pi$. Hence we find that

$$
\int_0^1\frac{1}{1+x^2}\,dx=\int_0^{\frac{1}{4}\pi}\frac{1}{1+\tan^2(t)}\left(1+\tan^2(t)\right)\,dt=\int_0^{\frac{1}{4}\pi}1\,dt=\frac{1}{4}\pi.
$$

*Remark*: Of course, it is easier to evaluate the integral directly using the fundamental theorem of calculus (see: {prf:ref}`Ex:Integration:FundamentalTheoremPart2Example3`).

:::

In the case of $\sqrt{x^2-a^2}$ we use the substitution $x=\dfrac{a}{\cos(t)}$. Then we have $dx=\dfrac{a\sin(t)}{\cos^2(t)}$ and

$$
\sqrt{x^2-a^2}=\sqrt{\frac{a^2}{\cos^2(t)}-a^2}=\sqrt{\frac{a^2-a^2\cos^2(t)}{\cos^2(t)}}=\sqrt{\frac{a^2\sin^2(t)}{\cos^2(t)}}=|a\tan(t)|.
$$

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample3
Evaluate $\displaystyle\int_0^{\sqrt{2}}\sqrt{x^2-1}\,dx$.

Solution. Let $x=\dfrac{1}{\cos(t)}$, then we have $dx=\dfrac{\sin(t)}{\cos^2(t)}\,dt$. Furthermore, if $x=1$ then $t=0$ and if $x=\sqrt{2}$ then $t=\frac{1}{4}\pi$. Hence we find that

$$
\begin{align*}
\int_0^{\sqrt{2}}\sqrt{x^2-1}\,dx&=\int_0^{\frac{1}{4}\pi}|\tan(t)|\frac{\sin(t)}{\cos^2(t)}\,dt=\int_0^{\frac{1}{4}\pi}\frac{\sin^2(t)}{\cos^3(t)}\,dt\\
&=\int_0^{\frac{1}{4}\pi}\frac{\sin^2(t)}{\cos^4(t)}\cos(t)\,dt.
\end{align*}
$$

Now we use $\cos^2(t)=1-\sin^2(t)$ and the substitution $u=\sin(t)$ to find that

$$
\int_0^{\frac{1}{4}\pi}\frac{\sin^2(t)}{\cos^4(t)}\cos(t)\,dt=\int_0^{\frac{1}{2}\sqrt{2}}\frac{u^2}{(1-u^2)^2}\,du.
$$

Then we use the partial fraction decomposition (see the section on integration of rational functions)

$$
\frac{u^2}{(1-u^2)^2}=\frac{1}{4}\left(-\frac{1}{1-u}+\frac{1}{(1-u)^2}-\frac{1}{1+u}+\frac{1}{(1+u)^2}\right),
$$

to find that

$$
\begin{align*}
&\int_0^{\frac{1}{2}\sqrt{2}}\frac{u^2}{(1-u^2)^2}\,du\\
&=\frac{1}{4}\int_0^{\frac{1}{2}\sqrt{2}}\left(-\frac{1}{1-u}+\frac{1}{(1-u)^2}-\frac{1}{1+u}+\frac{1}{(1+u)^2}\right)\,dt\\
&=\frac{1}{4}\bigg[\ln|1-u|+\frac{1}{1-u}-\ln|1+u|-\frac{1}{1+u}\bigg]_0^{\frac{1}{2}\sqrt{2}}\\
&=\frac{1}{4}\left(\ln(1-\tfrac{1}{2}\sqrt{2})+\frac{1}{1-\frac{1}{2}\sqrt{2}}-\ln(1+\tfrac{1}{2}\sqrt{2})-\frac{1}{1+\frac{1}{2}\sqrt{2}}\right)\\
&=\frac{1}{4}\ln\left(\frac{2-\sqrt{2}}{2+\sqrt{2}}\right)+\frac{1}{2}\sqrt{2}.
\end{align*}
$$

::::::

## The tangent half-angle substitution

The **tangent half-angle substitution**, sometimes called the **Weierstrass substitution**, converts an integral of a rational function of trigonometric functions into an integral of an ordinary rational function. Although integrals of rational functions will be covered later, we can show how it works.

The method is named after the German mathematician [Karl Theodor Wilhelm Weierstrass (1815-1897)](https://en.wikipedia.org/wiki/Karl_Weierstrass).

For $-\pi<x<\pi$ we set $t=\tan(\frac{1}{2}x)$ or $x=2\arctan(t)$. Then we have

::::{math}
:label: Eq:Integration:Weierstrass

\sin(\tfrac{1}{2}x)=\frac{t}{\sqrt{1+t^2}}\quad\text{and}\quad\cos(\tfrac{1}{2}x)=\frac{1}{\sqrt{1+t^2}}.

::::

:::{admonition} Proof of {eq}`Eq:Integration:Weierstrass`
:class: solution, dropdown
For $0<x<\pi$ consider the right-angled triangle with legs $1$ and $t$ and angle $\theta$ such that $\tan(\theta)=t$. Then the hypotenuse equals $\sqrt{1+t^2}$ and

$$
\sin(\theta)=\frac{t}{\sqrt{1+t^2}}\quad\text{and}\quad\cos(\theta)=\frac{1}{\sqrt{1+t^2}}.
$$

This proves the formulas for $0<x<\pi$. For $-\pi<x<0$ we use $\sin(-\theta)=-\sin(\theta)$ and $\cos(-\theta)=\cos(\theta)$. For $x=0$ the formulas (trivially) hold as well.

Alternatively, we have

$$
\cos^2(\tfrac{1}{2}x)=\frac{1}{1+\tan^2(\frac{1}{2}x)}=\frac{1}{1+t^2}\quad\Longrightarrow\quad\cos(\tfrac{1}{2}x)=\pm\frac{1}{\sqrt{1+t^2}}.
$$

Since $\cos(\frac{1}{2}x)>0$ for $-\pi<x<\pi$ we conclude that $\cos(\frac{1}{2}x)=\dfrac{1}{\sqrt{1+t^2}}$. Then we have

$$
\sin^2(\tfrac{1}{2}x)=1-\cos^2(\tfrac{1}{2}x)=1-\frac{1}{1+t^2}=\frac{1+t^2-1}{1+t^2}=\frac{t^2}{1+t^2}.
$$

Hence, we have: $\sin(\frac{1}{2}x)=\pm\dfrac{t}{\sqrt{1+t^2}}$. Since $\sin(\frac{1}{2}x)$ should have the same sign as $t=\tan(\frac{1}{2}x)$ for $-\pi<x<\pi$ we conclude that $\sin(\frac{1}{2}x)=\dfrac{t}{\sqrt{1+t^2}}$.

:::

This leads to

$$
\sin(x)=2\sin(\tfrac{1}{2}x)\cos(\tfrac{1}{2}x)=\frac{2t}{1+t^2}
$$

and

$$
\cos(x)=\cos^2(\tfrac{1}{2}x)-\sin^2(\tfrac{1}{2}x)=\frac{1-t^2}{1+t^2}.
$$

Furthermore, we have $dx=\dfrac{2\,dt}{1+t^2}$.

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionWeierstrassExample1
Evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\sin(x)}$.

Solution. Using $t=\tan(\frac{1}{2}x)$ we obtain

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\sin(x)}&=\int_0^1\frac{1}{1+\dfrac{2t}{1+t^2}}\cdot\frac{2\,dt}{1+t^2}=\int_0^1\frac{2\,dt}{(t+1)^2}\\
&=-\frac{2}{1+t}\bigg|_0^1=-1+2=1.
\end{align*}
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionWeierstrassExample2
Evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\frac{\cos(x)}{1+\cos(x)}\,dx$.

Solution. Using $t=\tan(\frac{1}{2}x)$ we obtain

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\frac{\cos(x)}{1+\cos(x)}\,dx&=\int_0^1\frac{\dfrac{1-t^2}{1+t^2}}{1+\dfrac{1-t^2}{1+t^2}}\cdot\frac{2}{1+t^2}\,dt\\
&=\int_0^1\frac{1-t^2}{1+t^2+1-t^2}\cdot\frac{2}{1+t^2}\,dt\\
&=\int_0^1\frac{1-t^2}{1+t^2}\,dt=\int_0^1\frac{2-(1+t^2)}{1+t^2}\,dt\\
&=\bigg[2\arctan(t)-t\bigg]_0^1=\frac{1}{2}\pi-1.
\end{align*}
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionWeierstrassExample3
Evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\sin(x)+\cos(x)}$.

Solution. Using $t=\tan(\frac{1}{2}x)$ we obtain

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\sin(x)+\cos(x)}&=\int_0^1\frac{1}{1+\dfrac{2t}{1+t^2}+\dfrac{1-t^2}{1+t^2}}\cdot\frac{2\,dt}{1+t^2}\\
&=\int_0^1\frac{dt}{1+t}=\ln(1+t)\bigg|_0^1=\ln(2).
\end{align*}
$$

::::::

In {prf:ref}`Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample2` we obtained that

$$
\int_0^{\frac{1}{4}\pi}\frac{1}{\cos(t)}\,dt=\ln(1+\sqrt{2}).
$$

This can also be done using the tangent half-angle substitution: set $u=\tan(\frac{1}{2}t)$ or $t=2\arctan(u)$. Then $t=0$ implies that $u=0$ and $t=\frac{1}{4}\pi$ implies that $u=\tan(\frac{1}{8}\pi)=\sqrt{2}-1$ (see: {numref}`Exc:Trigonometry:Exercise_10`). With $\cos(t)=\dfrac{1-u^2}{1+u^2}$ and $dt=\dfrac{2\,du}{1+u^2}$ we obtain

$$
\begin{align*}
\int_0^{\frac{1}{4}\pi}\frac{1}{\cos(t)}\,dt&=\int_0^{\sqrt{2}-1}\frac{1}{\dfrac{1-u^2}{1+u^2}}\cdot\frac{2\,du}{1+u^2}=\int_0^{\sqrt{2}-1}\frac{2}{1-u^2}\,du\\
&=\int_0^{\sqrt{2}-1}\left(\frac{1}{1+u}+\frac{1}{1-u}\right)\,du=\bigg[\ln(1+u)-\ln(1-u)\bigg]_0^{\sqrt{2}-1}\\
&=\ln(\sqrt{2})-\ln(2-\sqrt{2})=\ln\left(\frac{\sqrt{2}}{2-\sqrt{2}}\right)\\
&=\ln\left(\frac{\sqrt{2}}{2-\sqrt{2}}\cdot\frac{2+\sqrt{2}}{2+\sqrt{2}}\right)=\ln\left(\frac{2+2\sqrt{2}}{4-2}\right)=\ln(1+\sqrt{2}).
\end{align*}
$$

## A nice formula with interesting applications

Using the substitution $x=a+b-t$ or $t=a+b-x$ we obtain that:

$$
\begin{align*}
\int_a^b\frac{f(x)}{f(x)+f(a+b-x)}\,dx&=-\int_b^a\frac{f(a+b-t)}{f(a+b-t)+f(t)}\,dt\\
&=\int_a^b\frac{f(a+b-t)}{f(a+b-t)+f(t)}\,dt.
\end{align*}
$$

This implies that

$$
I=\int_a^b\frac{f(x)}{f(x)+f(a+b-x)}\,dx=\int_a^b\frac{f(a+b-x)}{f(a+b-x)+f(x)}\,dx.
$$

Hence we have

$$
2I=\int_a^b\frac{f(x)}{f(x)+f(a+b-x)}\,dx+\int_a^b\frac{f(a+b-x)}{f(a+b-x)+f(x)}\,dx=\int_a^b1\,dx=b-a,
$$

which implies that

$$
\int_a^b\frac{f(x)}{f(x)+f(a+b-x)}\,dx=\frac{b-a}{2}.
$$

::::::{prf:Example}
:label: Ex:Integration:SubstitutionNiceFormula1
For $a=0$, $b=1$ and $f(x)=\sqrt{x}$ we obtain

$$
\int_0^1\frac{\sqrt{x}}{\sqrt{x}+\sqrt{1-x}}\,dx=\frac{1-0}{2}=\frac{1}{2}.
$$

::::::

Grasple-opgave met varianten: $\displaystyle\int_a^b\frac{\sqrt{x}}{\sqrt{x}-\sqrt{a+b-x}}\,dx=\frac{b-a}{2}$ met $a\in\{0,1,2,3,4,5,6,7,8\}$ en $b\in\{1,2,3,4,5,6,7,8,9\}$ met $a<b$ (met uitzondering van $a=0$ en $b=1$).

::::::{prf:Example}
:label: Ex:Integration:SubstitutionNiceFormula2
For $a=0$, $b=\frac{1}{2}\pi$ and $f(x)=\sin(x)$ we obtain

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\frac{\sin(x)}{\sin(x)+\cos(x)}\,dx&=\int_0^{\frac{1}{2}\pi}\frac{\sin(x)}{\sin(x)+\sin(\frac{1}{2}\pi-x)}\,dx\\
&=\frac{\frac{1}{2}\pi-0}{2}=\frac{1}{4}\pi.
\end{align*}
$$

::::::

Grasple-opgave met varianten: $\displaystyle\int_0^{\frac{1}{2}\pi}\frac{(\sin(x))^a}{(\sin(x))^a+(\cos(x))^a}\,dx=\frac{\frac{1}{2}\pi-0}{2}=\tfrac{1}{4}\pi$ met $a\in\{1/2,2,3,4,5\}$.

::::{exercise}
:label: Exc:Integration:SubstitutionNiceFormula
Evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\tan(x)}$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionNiceFormula`
:class: solution, dropdown

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\tan(x)}&=\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\dfrac{\sin(x)}{\cos(x)}}=\int_0^{\frac{1}{2}\pi}\frac{\dfrac{1}{\sin(x)}}{\dfrac{1}{\sin(x)}+\dfrac{1}{\cos(x)}}\,dx\\
&=\frac{\frac{1}{2}\pi-0}{2}=\frac{1}{4}\pi.
\end{align*}
$$

:::

## Serret's integral

Consider the integral $\displaystyle\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx$, which is named after the French mathematician [Joseph Alfred Serret (1819-1885)](https://en.wikipedia.org/wiki/Joseph-Alfred_Serret).  One way to evaluate the integral is by using the substitution $x=\tan(\theta)$:

$$
\begin{align*}
\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx&=\int_0^{\frac{1}{4}\pi}\ln\left(1+\tan(\theta)\right)\,d\theta=\int_0^{\frac{1}{4}\pi}\ln\left(\frac{\cos(\theta)+\sin(\theta)}{\cos(\theta)}\right)\,d\theta\\
&=\int_0^{\frac{1}{4}\pi}\left(\ln\left(\cos(\theta)+\sin(\theta)\right)-\ln\left(\cos(\theta)\right)\right)\,d\theta.
\end{align*}
$$

Now we use $\cos(\theta)+\sin(\theta)=\sqrt{2}\cos(\theta-\frac{1}{4}\pi)$ (see exercise 2) to obtain

$$
\begin{align*}
\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx&=\int_0^{\frac{1}{4}\pi}\left(\ln\left(\sqrt{2}\cos(\theta-\tfrac{1}{4}\pi)\right)-\ln\left(\cos(\theta)\right)\right)\,d\theta\\
&=\int_0^{\frac{1}{4}\pi}\left(\ln\left(\sqrt{2}\right)+\ln\left(\cos\left(\theta-\tfrac{1}{4}\pi\right)-\ln\left(\cos(\theta)\right)\right)\right)\,d\theta.
\end{align*}
$$

Finally, the substitution $t=\frac{1}{4}\pi-\theta$ or $\theta=\frac{1}{4}\pi-t$ shows that

$$
\int_0^{\frac{1}{4}\pi}\ln\left(\cos\left(\theta-\tfrac{1}{4}\pi\right)\right)\,d\theta=-\int_{\frac{1}{4}\pi}^0\ln\left(\cos(t)\right)\,dt=\int_0^{\frac{1}{4}\pi}\ln\left(\cos(t)\right)\,dt,
$$

which implies that

$$
\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx=\frac{1}{4}\pi\ln\left(\sqrt{2}\right)=\frac{1}{8}\pi\ln(2).
$$

In this evaluation we obtained that

$$
\begin{align*}
&\int_0^{\frac{1}{4}\pi}\ln\left(\cos\left(\theta-\tfrac{1}{4}\pi\right)\right)\,d\theta=\int_0^{\frac{1}{4}\pi}\ln\left(\cos(t)\right)\,dt\\
&{}\quad\Longrightarrow\quad\int_0^{\frac{1}{4}\pi}\left(\ln\left(\cos\left(\theta-\tfrac{1}{4}\pi\right)-\ln\left(\cos(\theta)\right)\right)\right)\,d\theta=0.
\end{align*}
$$

The value of the integral $\displaystyle\int_0^{\frac{1}{4}\pi}\ln\left(\cos(t)\right)\,dt$ is closely related to *Catalan's constant*, which will be considered later. See: {numref}`Sec:Series:TaylorSeries`. 

::::{exercise}
:label: Exc:Integration:SubstitutionTrigForm
Show that $\cos(\theta)+\sin(\theta)=\sqrt{2}\cos(\theta-\frac{1}{4}\pi)$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionTrigForm`
:class: solution, dropdown
Using $\cos(x-y)=\cos(x)\cos(y)+\sin(x)\sin(y)$ we obtain

$$
\cos(\theta-\tfrac{1}{4}\pi)=\cos(\theta)\cos(\tfrac{1}{4}\pi)+\sin(\theta)\sin(\tfrac{1}{4}\pi)=\tfrac{1}{2}\sqrt{2}\cos(\theta)+\tfrac{1}{2}\sqrt{2}\sin(\theta).
$$

Multiplying by $\sqrt{2}$ we find that

$$
\sqrt{2}\cos(\theta-\tfrac{1}{4}\pi)=\cos(\theta)+\sin(\theta).
$$

:::

## Integrals involving the Lambert $W$ function

The Lambert $W$ function is the inverse of the function $y=xe^x$ with domain $[-1,\infty)$ and range $[-e^{-1},\infty)$. This implies that 

$$
W(x)e^{W(x)}=x.
$$

Using the substitution $t=W(x)$ or equivalently $x=te^t$ and therefore $dx=(t+1)e^t\,dt$ we have for $x>-e^{-1}$:

$$
\int W(x)\,dx=\int t(t+1)e^t\,dt=(t^2-t+1)e^t+C=xW(x)-x+e^{W(x)}+C.
$$

For $x>-e^{-1}$ and $x\neq0$ this can also be written as: 

$$
\int W(x)\,dx=x\left(W(x)-1+\frac{1}{W(x)}\right)+C.
$$

Since $W(0)=0$ and $W(e)=1$ it follows that $\displaystyle\int_0^eW(x)\,dx=e-1$.

Similarly we obtain for $x>-e^{-1}$ and $x\neq0$:

$$
\begin{align*}
\int\frac{W(x)}{x}\,dx&=\int\frac{t}{te^t}(t+1)e^t\,dt=\int(t+1)\,dt=\frac{1}{2}t^2+t+C\\
&=\frac{1}{2}\{W(x)\}^2+W(x)+C.
\end{align*} 
$$

Using $W(x)e^{W(x)}=x$ this can also be obtained in this way:

$$
\begin{align*}
\int\frac{W(x)}{x}\,dx&=\int e^{-W(x)}\,dx=\int e^{-t}(t+1)e^t\,dt=\int(t+1)\,dt\\
&=\frac{1}{2}t^2+t+C=\frac{1}{2}\{W(x)\}^2+W(x)+C.
\end{align*}
$$

Since $W(0)=0$ and $W(e)=1$ it follows that $\displaystyle\int_0^ee^{-W(x)}\,dx=\frac{3}{2}$.

## Grasple exercises

64141, 64618, 64879, 75957, 64878, 64599, 64834, 65945, 64831, 64653, 64660, 64601, 64825, 64652, 64835, 64850, 64648, 64830, 64826, 64832, 64827, 64881, 75951, 64877