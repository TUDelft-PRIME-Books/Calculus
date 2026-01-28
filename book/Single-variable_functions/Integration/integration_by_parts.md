(Sec:Integration:Parts)=

# Integration by parts

In this section we cover:

- Integration by parts for indefinite integrals
- Integration by parts for definite integrals
- Advanced cases (e.g. x^3*sin(x), arctan(x), e^x*cos(x), combination with substitution)
- Reduction formulas
- LIATE rule for choosing (including exceptions)


## Introduction

In the previous sections we have seen how to determine definite and indefinite integrals of standard functions and linear combinations of these standard functions, and also how to apply the method of integration by substitution.

Now consider the following indefinite integral:

$$
\displaystyle\int x\cos(x)\,dx.
$$

Although the integrand is composed of two standard functions, $x$ and $\cos(x)$, we cannot directly apply the formulas from {numref}`Tab:Integration:StandardIndefiniteIntegrals` to evaluate this integral. We can also not use {prf:ref}`Th:Integration:IndefiniteProperties` to split the integral into simpler integrals, since the integrand is a product of functions instead of a sum of functions ánd one standard function is nested inside another standard function. Finally, the method of integration by substitution is not applicable here either, since there is no part of the integrand that is nested inside another function.

In this section we introduce the method of **integration by parts**, which is a very powerful method to evaluate integral such as in the example above.

## Indefinite integrals

The method **integration by parts** is based on the product rule: if $f$ and $g$ are both differentiable, then

$$
\frac{d}{dx}\left(f(x)g(x)\right)=f(x)g'(x)+g(x)f'(x).
$$

Switching the left-hand and right-hand sides and integrating leads to

$$
\int f(x)g'(x)+g(x)f'(x) \,dx= \int \frac{d}{dx}\left(f(x)g(x)\right) \, dx.
$$

This implies that

$$
\int f(x)g'(x)\,dx+\int g(x)f'(x)\,dx=f(x)g(x).
$$

This leads to the following theorem:

::::::{prf:Theorem} Integration by parts for indefinite integrals
:label: Thm:Integration:PartsIndefiniteIntegral
If $f$ and $g$ are differentiable and $f'$ and $g'$ are continuous, then

:::{math}
:label: eq:Integration:PartsIndefiniteIntegral
\int f(x)g'(x)\,dx=f(x)g(x)-\int g(x)f'(x)\,dx.
:::

::::::


:::{prf:notation}

If $u=f(x)$ then $du=f'(x)\,dx$, and if $v=g(x)$ then $dv=g'(x)\,dx$.

Note that Equation {eq}`eq:Integration:PartsIndefiniteIntegral` can also be written as

:::{math}
:label: eq:Integration:PartsIndefiniteIntegralDifferentialNotation
\displaystyle\int u\,dv=uv-\int v\,du
:::

using this differential notation.
:::

The purpose of the method of integration by parts is that the new integral is not harder to evaluate than the original integral. We explicitly state *not harder* instead of *easier* because sometimes the new integral is equally hard to evaluate as the original integral, but at least we have made some progress.

Before we apply the method of integration by parts to the integral $\displaystyle\int x\cos(x)\,dx$, we will give you an algorithm to apply the method:

::::::{prf:algorithm}
:label: Alg:Integration:IngtegrationByPartsIndefiniteIntegral

To evaluate an indefinite integral of the form $\displaystyle\int I(x)\,dx$ using the method of integration by parts, follow these steps:

1. Select the function $f(x)$ in the integrand $I(x)$.
2. Determine the function $g'(x)$ such that $I(x)=f(x)g'(x)$.
3. Set $u=f(x)$ and compute $du=f'(x)\,dx$.
4. Set $dv=g'(x)\,dx$ and compute $v=g(x)$.
5. Apply Equation {eq}`eq:Integration:PartsIndefiniteIntegralDifferentialNotation` to rewrite the integral.
6. Evaluate the remaining indefinite integral using standard methods.

::::::

::::::{prf:Example}
:label: Ex.Integration:PartsPowerCos

Let us revisit the integral $\displaystyle\int x\cos(x)\,dx$ introduced at the beginning of this section.

Taking $u=x$ and $dv=\cos(x)\,dx$ we obtain $du=dx$ and $v=\sin(x)$. Applying this to Equation {eq}`eq:Integration:PartsIndefiniteIntegralDifferentialNotation` leads to

$$
\begin{align*}
\int x\cos(x)\,dx&=x\sin(x)-\int\sin(x)\,dx\\
&=x\sin(x)+\cos(x)+C.
\end{align*}
$$

::::::

Sometimes we have to apply the method more than once, or more concise: we can apply the method of integration by parts to each new integral we obtain. This is shown in the next example.

::::::{prf:Example}
:label: Ex.Integration:PartsPowerExp

We start with applying the method of integration by parts to the integral $\displaystyle\int x^2e^{2x}\,dx$. Taking $u=x^2$ and $dv=e^{2x}\,dx$ we obtain $du=2x\,dx$ and $v=\dfrac{1}{2}e^{2x}$. Applying this to Equation {eq}`eq:Integration:PartsIndefiniteIntegralDifferentialNotation` leads to

$$
\begin{align*}
\int x^2e^{2x}\,dx&=\frac{1}{2}x^2e^{2x}-\int \frac{1}{2}e^{2x}\,2x\,dx\\
&=\frac{1}{2}x^2e^{2x}-\int xe^{2x}\,dx.
\end{align*}
$$

Note that the integral $\displaystyle\int xe^{2x}\,dx$ looks easier to evaluate than the original integral $\displaystyle\int x^2e^{2x}\,dx$. However, we still don't know an antiderivative of the integrand. Using integration by parts once more on the remaining indefinite integral, we obtain, by choosing $u=x$ and $dv=e^{2x}\,dx$ (which implies that $du=dx$ and $v=\dfrac{1}{2}e^{2x}$):

\begin{align*}
\int xe^{2x}\,dx &= \frac{1}{2}xe^{2x}-\int \frac{1}{2}e^{2x}\,dx \\
&= \frac{1}{2}xe^{2x}-\frac{1}{4}e^{2x}+C.
\end{align*}

We conclude that

\begin{align*}
\int x^2e^{2x}\,dx &= \frac{1}{2}x^2e^{2x}-\left(\frac{1}{2}xe^{2x}-\frac{1}{4}e^{2x}+C\right) \\
&= \frac{1}{2}x^2e^{2x}-\frac{1}{2}xe^{2x}+\frac{1}{4}e^{2x}-C.
\end{align*}

::::::

Note that the choice $u=x$ and $dv=\cos(x)\,dx$ in the first example was crucial. The other choice $u=\cos(x)$ and $dv=x\,dx$ leads to a more difficult integral:

$$
\begin{align*}
\int x\cos(x)\,dx&=\frac{1}{2}\int\cos(x)\,dx^2=\frac{1}{2}x^2\cos(x)-\frac{1}{2}\int x^2\,d\cos(x)\\
&=\frac{1}{2}x^2\cos(x)+\frac{1}{2}\int x^2\sin(x)\,dx.
\end{align*}
$$

That $\cos(x)$ in the integrand is replaced by $\sin(x)$ does not make the integral more difficult. However, the raise of the power of $x$ does. Note that in the first two examples the power of $x$ was lowered by $1$ in each step.

If the integrand does not consist of more than one part, we may choose $u$ to be the integrand and $dv=dx$: 

::::::{prf:Example}
:label: Ex:Integration:PartsAntiderivativeArctan
In order to find an antiderivative of $\arctan(x)$ we apply integration by parts using $u=\arctan(x)$ and $dv=dx$:

$$
\begin{align*}
\int\arctan(x)\,dx&=x\arctan(x)-\int x\,\frac{1}{1+x^2}\,dx\\
&=x\arctan(x)-\int\frac{x}{1+x^2}\,dx\\
&=x\arctan(x)-\frac{1}{2}\ln(1+x^2)+C.
\end{align*}
$$

Note that this can also be written as 

$$
\int\arctan(x)\,dx=x\arctan(x)-\ln(\sqrt{1+x^2})+C.
$$

::::::

::::{exercise}
:label: Exc:Integration:PartsAntiderivativeOfLn
Find an antiderivative of $\ln(x)$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsAntiderivativeOfLn`
:class: solution, dropdown

$$
\int\ln(x)\,dx=x\ln(x)-\int x\,\frac{1}{x}\,dx=x\ln(x)-\int 1\,dx=x\ln(x)-x+C.
$$

:::

::::{exercise}
:label: Exc:Integration:PartsAntiderivativeOfArcsin
Find an antiderivative of $\arcsin(x)$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsAntiderivativeOfArcsin`
:class: solution, dropdown

$$
\begin{align*}
\int\arcsin(x)\,dx&=x\arcsin(x)-\int x\,\frac{1}{\sqrt{1-x^2}}\,dx\\
&=x\arcsin(x)-\int\frac{x}{\sqrt{1-x^2}}\,dx\\
&=x\arcsin(x)+\sqrt{1-x^2}+C.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:Integration:PartsAntiderivativeOfArccos
Find an antiderivative of $\arccos(x)$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsAntiderivativeOfArccos`
:class: solution, dropdown

$$
\begin{align*}
\int\arccos(x)\,dx&=x\arccos(x)-\int x\,\frac{-1}{\sqrt{1-x^2}}\,dx\\
&=x\arccos(x)+\int\frac{x}{\sqrt{1-x^2}}\,dx\\
&=x\arccos(x)-\sqrt{1-x^2}+C.
\end{align*}
$$

:::

<!-- EDITOR: Hier gebleven -->


If we have a choice, which part of the integrand should be chosen as $u$ and which part as $dv$? In many cases the so-called **LIATE rule** will help to make the right choice. If possible we choose for $u$ a **L**ogarithm, an **I**nverse trigonometric function, an **A**lgebraic function (a power of $x$), a **T**rigonometric function or an **E**xponential function, in that order. We can incorporate this rule in our algorithm {prf:ref}`Alg:Integration:IngtegrationByPartsIndefiniteIntegral` as follows:

::::::{prf:algorithm}
:label: Alg:Integration:IngtegrationByPartsIndefiniteIntegralLIATE

To evaluate an indefinite integral of the form $\displaystyle\int I(x)\,dx$ using the method of integration by parts, follow these steps:

1. Select the function $f(x)$ in the integrand $I(x)$:
    - If there is a logarithmic function, choose it for $f(x)$.
    - Otherwise, if there is an inverse trigonometric function, choose it for $f(x)$.
    - Otherwise, if there is an algebraic function (a power of $x$), choose it for $f(x)$.
    - Otherwise, if there is a trigonometric function, choose it for $f(x)$.
    - Otherwise, choose an exponential function for $f(x)$.
    - Otherwise, choose another part of the integrand for $f(x)$.
2. Determine the function $g'(x)$ such that $I(x)=f(x)g'(x)$.
3. Set $u=f(x)$ and compute $du=f'(x)\,dx$.
4. Set $dv=g'(x)\,dx$ and compute $v=g(x)$.
5. Apply Equation {eq}`eq:Integration:PartsIndefiniteIntegralDifferentialNotation` to rewrite the integral.
6. Evaluate the remaining indefinite integral using standard methods.

::::::

In {prf:ref}`Ex.Integration:PartsPowerCos` and {prf:ref}`Ex.Integration:PartsPowerExp` we chose the algebraic function ($x$ and $x^2$) for $u$ instead of the trigonometric function ($\cos(x)$) or the exponential function ($e^{2x}$).

::::::{prf:Example}
:label: Ex:Integration:PartsPowerCosWrong
Consider $\displaystyle\int x^3\ln(x)\,dx$ for $x>0$. If we choose $u=\ln(x)$ and $dv=x^3\,dx$, we obtain that $\displaystyle du=\frac{1}{x}\,dx$ which can easily be combined with any power of $x$, and $v=\frac14x^4$. We have

\begin{align*}
\int x^3\ln(x)\,dx&=\frac{1}{4}x^4\ln(x)-\int \frac{1}{4}x^4\,\frac{1}{x}\,dx\\
&=\frac{1}{4}x^4\ln(x)-\int \frac{1}{4}x^3\,dx\\
&=\frac{1}{4}x^4\ln(x)-\frac{1}{16}x^4+C.
\end{align*}

::::::

Note that this method works for every integral of the form $\displaystyle\int x^{\alpha}\ln(x)\,dx$ for every $\alpha\in\mathbb{R}\setminus\{-1\}$. The case $\alpha=-1$ is treated in the next example.

::::::{prf:Example}
:label: Ex:Integration:PartsLn
The integral $\displaystyle\int\frac{\ln(x)}{x}\,dx$ can be evaluated using the substitution $u=\ln(x)$, which implies that $du=\displaystyle\frac{1}{x}\,dx$, see {prf:ref}`Ex:Integration:SubstitutionDefiniteIntegralExample1`.

However, it can also be done using integration by parts. The LIATE rule suggests to use $u=\ln(x)$ and $dv=\dfrac{1}{x}\,dx$, which implies that $du=\dfrac{1}{x}\,dx$ and $v=\ln(x)$. We have

$$
\begin{align*}
\int\frac{\ln(x)}{x}\,dx&=\ln(x)\cdot\ln(x)-\int\ln(x)\,\dfrac{1}{x}\,dx\\
&=(\ln(x))^2-\int\frac{\ln(x)}{x}\,dx.
\end{align*}
$$

Hence, we have

:::{math}
:label: eq:Integration:PartsLnIntermediate
\displaystyle 2\int\frac{\ln(x)}{x}\,dx=(\ln(x))^2
:::

and therefore 

$$
\int\frac{\ln(x)}{x}\,dx=\frac{1}{2}(\ln(x))^2+C.
$$

Note that in this case, we only include the constant of integration at the end. If you would have included it one step earlier, in Equation {eq}`eq:Integration:PartsLnIntermediate`, you would have ended up with $\frac12C$ instead of $C$ in your answer. This would also have been correct, because if $C$ is an arbitrary constant, then so is $\frac12C$.

::::::

In the next example we deal with a product of a trigonometric function and an exponential function.

::::::{prf:Example}
:label: Ex:Integration:PartsExpCos

For the integral $I=\displaystyle\int e^{-2x}\cos(3x)\,dx$, the LIATE rule suggests to choose the trigonometric function for $u$. So we pick $u=\cos(3x)$ and $dv=e^{-2x}\,dx$, which implies that $du=-3\sin(3x)\,dx$ and $v=-\dfrac{1}{2}e^{-2x}$. We have

$$
\int e^{-2x}\cos(3x)\,dx =-\frac{1}{2}e^{-2x}\cos(3x)-\frac{3}{2}\int  e^{-2x}\sin(3x)\,dx
$$

In the new indefinite integral, which is not harder than the original, we again choose the trigonometric function for $u$. So we pick $u=\sin(3x)$ and $dv=e^{-2x}\,dx$, which implies that $du=3\cos(3x)\,dx$ and $v=-\dfrac{1}{2}e^{-2x}$. We continue:

\begin{align*}
\int e^{-2x}\cos(3x)\,dx &= -\frac{1}{2}e^{-2x}\cos(3x)-\frac{3}{2}\int  e^{-2x}\sin(3x)\,dx \\
&= -\frac{1}{2}e^{-2x}\cos(3x)-\frac{3}{2}\left(-\dfrac{1}{2}e^{-2x}\sin(3x)+\dfrac{3}{2}\int e^{-2x}\cos(3x)\,dx \right) \\
&= -\frac{1}{2}e^{-2x}\cos(3x)+\frac{3}{4}e^{-2x}\sin(3x)-\dfrac{9}{4}\int e^{-2x}\cos(3x)\,dx.
\end{align*}

This means we have:

\begin{align*}
&~ & I &=-\frac{1}{2}e^{-2x}\cos(3x)+\frac{3}{4}e^{-2x}\sin(3x)-\frac{9}{4}I\\
&\Longrightarrow & \left(1+\frac{9}{4}\right)I &= -\frac{1}{2}e^{-2x}\cos(3x)+\frac{3}{4}e^{-2x}\sin(3x).
\end{align*}

Since $1+\dfrac{9}{4}=\dfrac{13}{4}$ we conclude that

$$
I=-\frac{2}{13}e^{-2x}\cos(3x)+\frac{3}{13}e^{-2x}\sin(3x)+C.
$$

Note that we can wait to add the constant of integration till the last step.
::::::

Here we chose the trigonometric function for $u$ in both the first and the second step. In this case we could have chosen the exponential function instead. However, it is important to stick to the same choice (trigonometric or exponential function) in the second step. Otherwise, we return to the original integral without any result:

% EDITOR: Continue here

$$
\begin{align*}
&\int e^{-2x}\cos(3x)\,dx=-\frac{1}{2}\int\cos(3x)\,de^{-2x}\\
&=-\frac{1}{2}e^{-2x}\cos(3x)+\frac{1}{2}\int e^{-2x}\,d\cos(3x)\\
&=-\frac{1}{2}e^{-2x}\cos(3x)-\frac{3}{2}\int e^{-2x}\sin(3x)\,dx\\
&=-\frac{1}{2}e^{-2x}\cos(3x)+\frac{1}{2}\int e^{-2x}\,d\cos(3x)\\
&=-\frac{1}{2}e^{-2x}\cos(3x)+\frac{1}{2}e^{-2x}\cos(3x)-\frac{1}{2}\int\cos(3x)\,de^{-2x}\\
&=\int e^{-2x}\cos(3x)\,dx.
\end{align*}
$$

::::{exercise}
:label: Exc:Integration:PartsOtherChoice
Evaluate $\displaystyle\int e^{-2x}\cos(3x)\,dx$ by taking $u=e^{-2x}$ in each step.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsOtherChoice`
:class: solution, dropdown

$$
\begin{align*}
&\int e^{-2x}\cos(3x)\,dx=\frac{1}{3}\int e^{-2x}\,d\sin(3x)\\
&=\frac{1}{3}e^{-2x}\sin(3x)-\frac{1}{3}\int\sin(3x)\,de^{-2x}\\
&=\frac{1}{3}e^{-2x}\sin(3x)+\frac{2}{3}\int e^{-2x}\sin(3x)\,dx\\
&=\frac{1}{3}e^{-2x}\sin(3x)-\frac{2}{9}\int e^{-2x}\,d\cos(3x)\\
&=\frac{1}{3}e^{-2x}\sin(3x)-\frac{2}{9}e^{-2x}\cos(3x)+\frac{2}{9}\int\cos(3x)\,de^{-2x}\\
&=\frac{1}{3}e^{-2x}\sin(3x)-\frac{2}{9}e^{-2x}\cos(3x)-\frac{4}{9}\int e^{-2x}\cos(3x)\,dx.
\end{align*}
$$

Let $I=\displaystyle\int e^{-2x}\cos(3x)\,dx$, then we have:

$$
\begin{align*}
&I=\frac{1}{3}e^{-2x}\sin(3x)-\frac{2}{9}e^{-2x}\cos(3x)-\frac{4}{9}I\\
&{}\quad\Longrightarrow\quad
\left(1+\frac{4}{9}\right)I=\frac{1}{3}e^{-2x}\sin(3x)-\frac{2}{9}e^{-2x}\cos(3x).
\end{align*}
$$

Since $1+\dfrac{4}{9}=\dfrac{13}{9}$ we conclude that

$$
I=\frac{3}{13}e^{-2x}\sin(3x)-\frac{2}{13}e^{-2x}\cos(3x)+C.
$$

:::

For definite integrals we have:
::::::{prf:Theorem} Integration by parts for definite integrals
:label: Thm:Integration:PartsDefiniteIntegral
If $f$ and $g$ are continuous on $[a,b]$, integrable and differentiable on $(a,b)$ and $f'$ and $g'$ are continuous on $[a,b]$, then

$$
\int_a^bf(x)g'(x)\,dx=f(x)g(x)\bigg|_a^b-\int_a^bg(x)f'(x)\,dx.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:PartsDefiniteLn

$$
\int_1^e\ln(x)\,dx=x\ln(x)\bigg|_1^e-\int_1^ex\,d\ln(x)=e-\int_1^e1\,dx=e-(e-1)=1.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:PartsDefiniteArcsin

$$
\begin{align*}
\int_0^{\frac{1}{2}}\arcsin(x)\,dx&=x\arcsin(x)\bigg|_0^{\frac{1}{2}}-\int_0^{\frac{1}{2}}x\,d\arcsin(x)\\
&=\frac{1}{2}\cdot\frac{1}{6}\pi-\int_0^{\frac{1}{2}}\frac{x}{\sqrt{1-x^2}}\,dx=\frac{1}{12}\pi+\sqrt{1-x^2}\bigg|_0^{\frac{1}{2}}\\
&=\frac{1}{12}\pi+\frac{1}{2}\sqrt{3}-1.
\end{align*}
$$

::::::

Sometimes we might combine the methods of substitution and integration by parts:

::::::{prf:Example}
:label: Ex:Integration:PartsSubstitution
Evaluate $\displaystyle\int_4^9e^{\sqrt{x}}\,dx$.

Solution. First apply the substitution $u=\sqrt{x}$ which implies that $du=\dfrac{1}{2\sqrt{x}}\,dx$ or $dx=2u\,du$:

$$
\int_4^9e^{\sqrt{x}}\,dx=2\int_2^3ue^u\,du.
$$

Now we use integration by parts to obtain

$$
\begin{align*}
\int_4^9e^{\sqrt{x}}\,dx&=2\int_2^3ue^u\,du=2\int_2^3u\,de^u=2ue^u\bigg|_2^3-2\int_2^3e^u\,du\\
&=6e^3-4e^2-2e^u\bigg|_2^3=6e^3-4e^2-2e^3+2e^2=4e^3-2e^2.
\end{align*}
$$

::::::

::::{exercise}
:label: Exc:Integration:PartsSubstitutionCos
Evaluate $\displaystyle\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^3\cos(t^2)\,dt$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsSubstitutionCos`
:class: solution, dropdown
First apply the substitution $u=t^2$ which implies that $du=2t\,dt$:

$$
\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^3\cos(t^2)\,dt=\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^2\cos(t^2)t\,dt=\frac{1}{2}\int_{\pi/2}^{\pi}u\cos(u)\,du.
$$

Now we use integration by parts to find that

$$
\begin{align*}
\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^3\cos(t^2)\,dt&=\frac{1}{2}\int_{\pi/2}^{\pi}u\cos(u)\,du=\frac{1}{2}\int_{\pi/2}^{\pi}u\,d\sin(u)\\
&=\frac{1}{2}u\sin(u)\bigg|_{\pi/2}^{\pi}-\frac{1}{2}\int_{\pi/2}^{\pi}\sin(u)\,du\\
&=-\frac{1}{4}\pi+\frac{1}{2}\cos(u)\bigg|_{\pi/2}^{\pi}=-\frac{1}{4}\pi-\frac{1}{2}.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:Integration:PartsSubstitutionSin
Evaluate $\displaystyle\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^3\sin(t^2)\,dt$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsSubstitutionSin`
:class: solution, dropdown
First apply the substitution $u=t^2$ which implies that $du=2t\,dt$:

$$
\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^3\sin(t^2)\,dt=\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^2\sin(t^2)t\,dt=\frac{1}{2}\int_{\pi/2}^{\pi}u\sin(u)\,du.
$$

Now we use integration by parts to find that

$$
\begin{align*}
\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^3\sin(t^2)\,dt&=\frac{1}{2}\int_{\pi/2}^{\pi}u\sin(u)\,du=-\frac{1}{2}\int_{\pi/2}^{\pi}u\,d\cos(u)\\
&=-\frac{1}{2}u\cos(u)\bigg|_{\pi/2}^{\pi}+\frac{1}{2}\int_{\pi/2}^{\pi}\cos(u)\,du\\
&=\frac{1}{2}\pi+\frac{1}{2}\sin(u)\bigg|_{\pi/2}^{\pi}=\frac{1}{2}\pi-\frac{1}{2}.
\end{align*}
$$

:::

## Reduction formulas

In {prf:ref}`Ex.Integration:PartsPowerExp` we evaluated the integral $\displaystyle\int x^2e^{2x}\,dx$ using integration by parts twice. What happens if we replace $x^2$ by a higher power of $x$? For instance, consider:

$$
\int x^{10}e^x\,dx=\int x^{10}\,de^x=x^{10}e^x-\int e^x\,dx^{10}=x^{10}e^x-10\int x^9e^x\,dx.
$$

Note that the latter integral has the same form as the original one with a power of $x$ one less. If we apply the same technique once more to the latter integral we will end up with a similar integral with a power of $x$ one less again. We may proceed in this way until the power of $x$ equals $x^0=1$ and the integral reads $\displaystyle\int e^x\,dx$, which can be evaluated directly using the fundamental theorem of calculus.

More general, let $n\in\{1,2,3,\ldots\}$. Then we obtain

$$
\int x^ne^x\,dx=\int x^n\,de^x=x^ne^x-\int e^x\,dx^n=x^ne^x-n\int x^{n-1}e^x\,dx.
$$

So, if we define $I_n=\displaystyle\int x^ne^x\,dx$, then we have: $I_n=x^ne^x-nI_{n-1}$ for $n=1,2,3,\ldots$. Furthermore, we have $I_0=\displaystyle\int e^x\,dx=e^x+C$. Hence, we obtained the **reduction formula**

$$
I_n=x^ne^x-nI_{n-1},\quad n=1,2,3,\ldots\quad\text{with}\quad I_0=e^x+C.
$$

This implies that 

$$
I_1=xe^x-I_0=xe^x-e^x-C=(x-1)e^x-C,
$$

$$
I_2=x^2e^x-2I_1=x^2e^x-2xe^x+2e^x+2C=(x^2-2x+2)e^x+2C,
$$

and so on. Note that we might add the constant of integration only in the last step. Moreover, if we put the factor $e^x$ outside the brackets, we find that

$$
\begin{align*}
I_{10}&=\left(x^{10}-10x^9+90x^8-720x^7+5040x^6-30240x^5+151200x^4\right.\\
&{}\quad\quad\quad\left.{}-604800x^3+1814400x^2-3628800x+3628800\right)e^x+C.
\end{align*}
$$

::::{exercise}
:label: Exc:Integration:PartsReductionPowerExpNeg
Find a reduction formula for $\displaystyle\int x^ne^{-x}\,dx$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsReductionPowerExpNeg`
:class: solution, dropdown

$$
\begin{align*}
\int x^ne^{-x}\,dx&=-\int x^n\,de^{-x}=-x^ne^{-x}+\int e^{-x}\,dx^n\\
&=-x^ne^{-x}+n\int x^{n-1}e^{-x}\,dx.
\end{align*}
$$

Define $I_n=\displaystyle\int x^ne^{-x}\,dx$, then we have

$$
I_n=-x^ne^{-x}+nI_{n-1},\quad n=1,2,3,\ldots.
$$

Furthermore, we have $I_0=\displaystyle\int e^{-x}\,dx=-e^{-x}+C$.
:::

In {prf:ref}`Ex.Integration:PartsPowerCos` we evaluated the integral $\displaystyle\int x\cos(x)\,dx$ using integration by parts. What happens if we replace $x$ by a higher power of $x$?

Let $n\in\{2,3,4,\ldots\}$, then we obtain using integration by parts

$$
\begin{align*}
\int x^n\cos(x)\,dx&=\int x^n\,d\sin(x)=x^n\sin(x)-\int\sin(x)\,dx^n\\
&=x^n\sin(x)-n\int x^{n-1}\sin(x)\,dx.
\end{align*}
$$

Applying integration by parts once more, we find that

$$
\begin{align*}
\int x^n\cos(x)\,dx&=x^n\sin(x)+n\int x^{n-1}\,d\cos(x)\\
&=x^n\sin(x)+nx^{n-1}\cos(x)-n\int\cos(x)\,dx^{n-1}\\
&=x^n\sin(x)+nx^{n-1}\cos(x)-n(n-1)\int x^{n-2}\cos(x)\,dx.
\end{align*}
$$

So, if we define $I_n=\displaystyle\int x^n\cos(x)\,dx$, then we have: 

$$
I_n=x^n\sin(x)+nx^{n-1}\cos(x)-n(n-1)I_{n-2},\quad n=2,3,4,\ldots.
$$

Furthermore, we have $I_0=\displaystyle\int\cos(x)\,dx=\sin(x)+C$ and in {prf:ref}`Ex.Integration:PartsPowerCos` we found that $I_1=\displaystyle\int x\cos(x)\,dx=x\sin(x)+\cos(x)+C$. This leads to

$$
I_2=x^2\sin(x)+2x\cos(x)-2I_0=x^2\sin(x)+2x\cos(x)-2\sin(x)+C,
$$

$$
\begin{align*}
I_3&=x^3\sin(x)+3x^2\cos(x)-6I_1\\
&=x^3\sin(x)+3x^2\cos(x)-6x\sin(x)-6\cos(x)+C,
\end{align*}
$$

and so on.

::::{exercise}
:label: Exc:Integration:PartsReductionPowerSin
Find a reduction formula for $\displaystyle\int x^n\sin(x)\,dx$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsReductionPowerSin`
:class: solution, dropdown

$$
\begin{align*}
\int x^n\sin(x)\,dx&=-\int x^n\,d\cos(x)=-x^n\cos(x)+\int\cos(x)\,dx^n\\
&=-x^n\cos(x)+n\int x^{n-1}\cos(x)\,dx\\
&=-x^n\cos(x)+n\int x^{n-1}\,d\sin(x)\\
&=-x^n\cos(x)+nx^{n-1}\sin(x)-n\int\sin(x)\,dx^{n-1}\\
&=-x^n\cos(x)+nx^{n-1}\sin(x)-n(n-1)\int x^{n-2}\sin(x)\,dx.
\end{align*}
$$

Define $I_n=\displaystyle\int x^n\sin(x)\,dx$, then we have

$$
I_n=-x^n\cos(x)+nx^{n-1}\sin(x)-n(n-1)I_{n-2},\quad n=2,3,4,\ldots.
$$

Furthermore, we have $I_0=\displaystyle\int\sin(x)\,dx=-\cos(x)+C$ and

$$
\begin{align*}
I_1:&=\int x\sin(x)\,dx-\int x\,d\cos(x)\\
&=-x\cos(x)+\int\cos(x)\,dx=-x\cos(x)+\sin(x)+C.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:Integration:PartsReductionLn
Find a reduction formula for $\displaystyle\int\left(\ln(x)\right)^n\,dx$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsReductionLn`
:class: solution, dropdown

$$
\begin{align*}
\int\left(\ln(x)\right)^n\,dx&=x\left(\ln(x)\right)^n-\int x\,d\left(\ln(x)\right)^n\\
&=x\left(\ln(x)\right)^n-n\int x\left(\ln(x)\right)^{n-1}\frac{1}{x}\,dx\\
&=x\left(\ln(x)\right)^n-n\int\left(\ln(x)\right)^{n-1}\,dx.
\end{align*}
$$

Define $I_n=\displaystyle\int\left(\ln(x)\right)^n\,dx$, then we have

$$
I_n=x\left(\ln(x)\right)^n-nI_{n-1},\quad n=1,2,3,\ldots.
$$

Furthermore, we have: $I_0=\displaystyle\int1\,dx=x+C$.
:::

::::::{prf:Example}
:label: Ex:Integration:PartsReductionSin
Show that $\displaystyle\int\sin^n(x)\,dx=-\frac{1}{n}\cos(x)\sin^{n-1}(x)+\frac{n-1}{n}\int\sin^{n-2}(x)\,dx$ for $n=2,3,4,\ldots$.

Solution. For $n=2,3,4,\ldots$ we obtain

$$
\begin{align*}
\int\sin^n(x)\,dx&=-\int\sin^{n-1}(x)\,\cos(x)\\
&=-\cos(x)\sin^{n-1}(x)+\int\cos(x)\,d\sin^{n-1}(x)\\
&=-\cos(x)\sin^{n-1}(x)+(n-1)\int\cos(x)\sin^{n-2}(x)\cos(x)\,dx\\
&=-\cos(x)\sin^{n-1}(x)+(n-1)\int\sin^{n-2}(x)\cos^2(x)\,dx.
\end{align*}
$$

Now we use $\cos^2(x)=1-\sin^2(x)$ to find

$$
\begin{align*}
&\int\sin^n(x)\,dx\\
&=-\cos(x)\sin^{n-1}(x)+(n-1)\int\sin^{n-2}(x)\left(1-\sin^2(x)\right)\,dx\\
&=-\cos(x)\sin^{n-1}(x)+(n-1)\int\sin^{n-2}(x)\,dx-(n-1)\int\sin^n(x)\,dx.
\end{align*}
$$

This implies that

$$
n\int\sin^n(x)\,dx=-\cos(x)\sin^{n-1}(x)+(n-1)\int\sin^{n-2}(x)\,dx
$$

and therefore

$$
\int\sin^n(x)\,dx=-\frac{1}{n}\cos(x)\sin^{n-1}(x)+\frac{n-1}{n}\int\sin^{n-2}(x)\,dx.
$$

::::::

::::{exercise}
:label: Exc:Integration:PartsReductionCos
Find a reduction formula for $\displaystyle\int\cos^n(x)\,dx$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsReductionCos`
:class: solution, dropdown
For $n=2,3,4,\ldots$ we obtain

$$
\begin{align*}
\int\cos^n(x)\,dx&=\int\cos^{n-1}(x)\,\sin(x)=\sin(x)\cos^{n-1}(x)-\int\sin(x)\,d\cos^{n-1}(x)\\
&=\sin(x)\cos^{n-1}(x)+(n-1)\int\sin(x)\cos^{n-2}(x)\sin(x)\,dx\\
&=\sin(x)\cos^{n-1}(x)+(n-1)\int\cos^{n-2}(x)\sin^2(x)\,dx.
\end{align*}
$$

Now we use $\sin^2(x)=1-\cos^2(x)$ to find

$$
\begin{align*}
&\int\cos^n(x)\,dx\\
&=\sin(x)\cos^{n-1}(x)+(n-1)\int\cos^{n-2}(x)\left(1-\cos^2(x)\right)\,dx\\
&=\sin(x)\cos^{n-1}(x)+(n-1)\int\cos^{n-2}(x)\,dx-(n-1)\int\cos^n(x)\,dx.
\end{align*}
$$

This implies that

$$
n\int\cos^n(x)\,dx=\sin(x)\cos^{n-1}(x)+(n-1)\int\cos^{n-2}(x)\,dx
$$

and therefore

$$
\int\cos^n(x)\,dx=\frac{1}{n}\sin(x)\cos^{n-1}(x)+\frac{n-1}{n}\int\cos^{n-2}(x)\,dx.
$$

:::

::::{exercise}
:label: Exc:Integration:PartsReductionSinDefinite
Use the reduction formula of {prf:ref}`Ex:Integration:PartsReductionSin` to show that

$$
\int_0^{\frac{1}{2}\pi}\sin^n(x)\,dx=\frac{n-1}{n}\int_0^{\frac{1}{2}\pi}\sin^{n-2}(x)\,dx,\quad n=2,3,4,\ldots.
$$

::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsReductionSinDefinite`
:class: solution, dropdown

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\sin^n(x)\,dx&=-\frac{1}{n}\cos(x)\sin^{n-1}(x)\bigg|_0^{\frac{1}{2}\pi}+\frac{n-1}{n}\int_0^{\frac{1}{2}\pi}\sin^{n-2}(x)\,dx\\
&=\frac{n-1}{n}\int_0^{\frac{1}{2}\pi}\sin^{n-2}(x)\,dx,
\end{align*}
$$

since $\cos(\frac{1}{2}\pi)=0$ and $\sin(0)=0$. Note that $\sin^{n-1}(x)$ contains at least one factor $\sin(x)$ for $n=2,3,4,\ldots$.
:::

::::{exercise}
:label: Exc:Integration:PartsReductionSinDefiniteOdd
Use the reduction formula obtained in {numref}`Exc:Integration:PartsReductionSinDefinite` to show that

$$
\int_0^{\frac{1}{2}\pi}\sin^{2n+1}(x)\,dx=\frac{2\cdot4\cdot6\cdots2n}{3\cdot5\cdot7\cdots(2n+1)},\quad n=1,2,3,\ldots.
$$

::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsReductionSinDefiniteOdd`
:class: solution, dropdown
Replacing $n$ by $2n+1$ in {numref}`Exc:Integration:PartsReductionSinDefinite` we find

$$
\int_0^{\frac{1}{2}\pi}\sin^{2n+1}(x)\,dx=\frac{2n}{2n+1}\int_0^{\frac{1}{2}\pi}\sin^{2n-1}(x)\,dx,\quad n=1,2,3,\ldots.
$$

Iteration now leads to

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\sin^{2n+1}(x)\,dx&=\frac{2n}{2n+1}\cdot\frac{2n-2}{2n-1}\cdot\frac{2n-4}{2n-3}\cdots\frac{2}{3}\int_0^{\frac{1}{2}\pi}\sin(x)\,dx\\
&=\frac{2\cdot4\cdot6\cdots2n}{3\cdot5\cdot7\cdots(2n+1)},
\end{align*}
$$

since $\displaystyle\int_0^{\frac{1}{2}\pi}\sin(x)\,dx=-\cos(x)\bigg|_0^{\frac{1}{2}\pi}=1$. Note that the products in the numerator and the denominator are written in the opposite order.
:::

::::{exercise}
:label: Exc:Integration:PartsReductionSinDefiniteEven
Use the reduction formula obtained in {numref}`Exc:Integration:PartsReductionSinDefinite` to show that

$$
\int_0^{\frac{1}{2}\pi}\sin^{2n}(x)\,dx=\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots2n}\frac{\pi}{2},\quad n=1,2,3,\ldots.
$$

::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsReductionSinDefiniteEven`
:class: solution, dropdown
Replacing $n$ by $2n$ in {numref}`Exc:Integration:PartsReductionSinDefinite` we find

$$
\int_0^{\frac{1}{2}\pi}\sin^{2n}(x)\,dx=\frac{2n-1}{2n}\int_0^{\frac{1}{2}\pi}\sin^{2n-2}(x)\,dx,\quad n=1,2,3,\ldots.
$$

Iteration now leads to

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\sin^{2n}(x)\,dx&=\frac{2n-1}{2n}\cdot\frac{2n-3}{2n-2}\cdot\frac{2n-5}{2n-4}\cdots\frac{1}{2}\int_0^{\frac{1}{2}\pi}1\,dx\\
&=\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots2n}\frac{\pi}{2},
\end{align*}
$$

since $\displaystyle\int_0^{\frac{1}{2}\pi}1\,dx=\frac{\pi}{2}$. Note that the products in the numerator and the denominator are written in the opposite order.
:::

::::{exercise}
:label: Exc:Integration:PartsWallis
Let $I_n=\displaystyle\int_0^{\frac{1}{2}\pi}\sin^n(x)\,dx$.

(a) Show that $I_{2n+2}\leq I_{2n+1}\leq I_{2n}$.

(b) Use the reduction formula obtained in {numref}`Exc:Integration:PartsReductionSinDefiniteEven` to show that

$$
\frac{I_{2n+2}}{I_{2n}}=\frac{2n+1}{2n+2}.
$$

(c) Use parts (a) and (b) to show that

$$
\frac{2n+1}{2n+2}\leq\frac{I_{2n+1}}{I_{2n}}\leq1
$$

and deduce that $\displaystyle\lim_{n\to\infty}\frac{I_{2n+1}}{I_{2n}}=1$.

(d) Use part (c) and {numref}`Exc:Integration:PartsReductionSinDefiniteOdd` and {numref}`Exc:Integration:PartsReductionSinDefiniteEven` to show that

$$
\lim_{n\to\infty}\frac{2}{1}\frac{2}{3}\frac{4}{3}\frac{4}{5}\frac{6}{5}\frac{6}{7}\cdots\frac{2n}{2n-1}\frac{2n}{2n+1}=\frac{\pi}{2}.
$$

This result is sometimes written as an infinite product

$$
\prod_{n=1}^{\infty}\frac{2n}{2n-1}\frac{2n}{2n+1}=\frac{\pi}{2},
$$

which is called the *Wallis product*. This formula is named after the English mathematician [John Wallis (1616-1703)](https://en.wikipedia.org/wiki/John_Wallis).
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsWallis`
:class: solution, dropdown
(a) Note that $0\leq\sin(x)\leq1$ for $x\in[0,\frac{1}{2}\pi]$. Hence we have for $x\in[0,\frac{1}{2}\pi]$:

$$
\sin^{2n+2}(x)\leq\sin^{2n+1}(x)\leq\sin^{2n}(x)\quad\Longrightarrow\quad I_{2n+2}\leq I_{2n+1}\leq I_{2n}.
$$

(b) Using the reduction formula obtained in {numref}`Exc:Integration:PartsReductionSinDefiniteEven` we obtain

$$
\frac{I_{2n+2}}{I_{2n}}=\frac{\dfrac{1\cdot3\cdot5\cdots(2n-1)\cdot(2n+1)}{2\cdot4\cdot6\cdots2n\cdot(2n+2)}\dfrac{\pi}{2}}{\dfrac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots2n}\dfrac{\pi}{2}}=\frac{2n+1}{2n+2}.
$$

(c) Now divide the inequality of part (a) by $I_{2n}$ to find

$$
\frac{I_{2n+2}}{I_{2n}}\leq\frac{I_{2n+1}}{I_{2n}}\leq\frac{I_{2n}}{I_{2n}},
$$

which implies, by using the result of part (b), that

$$
\frac{2n+1}{2n+2}\leq\frac{I_{2n+1}}{I_{2n}}\leq1.
$$

Since $\displaystyle\lim_{n\to\infty}\frac{2n+1}{2n+2}=1$, the squeeze theorm implies that

$$
\lim_{n\to\infty}\frac{I_{2n+1}}{I_{2n}}=1.
$$

(d) Finally, we use the results of {numref}`Exc:Integration:PartsReductionSinDefiniteOdd` and {numref}`Exc:Integration:PartsReductionSinDefiniteEven` to find

$$
\begin{align*}
1=\lim_{n\to\infty}\frac{I_{2n+1}}{I_{2n}}&=\lim_{n\to\infty}\frac{\dfrac{2\cdot4\cdot6\cdots2n}{3\cdot5\cdot7\cdots(2n+1)}}{\dfrac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots2n}\dfrac{\pi}{2}}\\
&=\lim_{n\to\infty}\frac{(2\cdot4\cdot6\cdots2n)^2}{1\cdot(3\cdot5\cdot7\cdots(2n-1))^2\cdot(2n+1)}\frac{2}{\pi}.
\end{align*}
$$

This implies that

$$
\lim_{n\to\infty}\frac{(2\cdot4\cdot6\cdots2n)^2}{1\cdot(3\cdot5\cdot7\cdots(2n-1))^2\cdot(2n+1)}=\frac{\pi}{2},
$$

which proves the Wallis product.
:::

## Serret's integral

In the previous section we have seen that $\displaystyle\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx=\frac{1}{8}\pi\ln(2)$. If we apply integration by parts we obtain

$$
\begin{align*}
\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx&=\int_0^1\ln(1+x)\,d\arctan(x)\\
&=\ln(1+x)\arctan(x)\bigg|_0^1-\int\arctan(x)\,d\ln(1+x)\\
&=\frac{1}{4}\pi\ln(2)-\int_0^1\frac{\arctan(x)}{1+x}\,dx.
\end{align*}
$$

This implies that

::::{math}
:label: Eq:Integration:PartsSerret
\int_0^1\frac{\arctan(x)}{1+x}\,dx=\frac{1}{8}\pi\ln(2)=\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx.
::::

::::::{admonition} A different approach to Serret's integral (bonus material)
:class: solution, dropdown
The results in {eq}`Eq:Integration:PartsSerret` can also be obtained using the Feynman method (see: {numref}`Sec:Integration:ImproperIntegrals` on improper integrals).

Note that Serret's integral is a special case of $I(\alpha)=\displaystyle\int_0^{\alpha}\frac{\ln(1+\alpha x)}{1+x^2}\,dx$.

Differentiation with respect to $\alpha$ leads to 

$$
I'(\alpha)=\displaystyle\frac{\ln(1+\alpha^2)}{1+\alpha^2}+\int_0^{\alpha}\frac{x}{(1+x^2)(1+\alpha x)}\,dx.
$$ 

Now we use (see the section on integration of rational functions for more details) 
 
$$
\frac{x}{(1+x^2)(1+\alpha x)}=\frac{1}{1+\alpha^2}\left(\frac{\alpha+x}{1+x^2}-\frac{\alpha}{1+\alpha x}\right)
$$

to obtain

$$
\begin{align*}
&\int_0^{\alpha}\frac{x}{(1+x^2)(1+\alpha x)}\,dx\\
&=\frac{1}{1+\alpha^2}\int_0^{\alpha}\left(\frac{\alpha+x}{1+x^2}-\frac{\alpha}{1+\alpha x}\right)\,dx\\
&=\frac{1}{1+\alpha^2}\bigg[\alpha\arctan(x)+\frac{1}{2}\ln(1+x)-\ln(1+\alpha x)\bigg]_0^{\alpha}\\
&=\frac{1}{1+\alpha^2}\left(\alpha\arctan(\alpha)+\frac{1}{2}\ln(1+\alpha^2)-\ln(1+\alpha^2)\right)\\
&=\frac{\alpha}{1+\alpha^2}\arctan(\alpha)-\frac{\ln(1+\alpha^2)}{2(1+\alpha^2)}.
\end{align*}
$$ 
 
Hence we have: $I'(\alpha)=\displaystyle\frac{\alpha}{1+\alpha^2}\arctan(\alpha)+\frac{\ln(1+\alpha^2)}{2(1+\alpha^2)}$. Since $I(0)=0$, this implies that

$$
\begin{align*}
I(\alpha)&=\int\frac{\alpha}{1+\alpha^2}\arctan(\alpha)\,d\alpha+\int\frac{\ln(1+\alpha^2)}{2(1+\alpha^2)}\,d\alpha\\
&=\frac{1}{2}\int\arctan(\alpha)\,d\ln(1+\alpha^2)+\int\frac{\ln(1+\alpha^2)}{2(1+\alpha^2)}\,d\alpha\\
&=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2)-\frac{1}{2}\int\ln(1+\alpha^2)\,d\arctan(\alpha)\\
&{}\quad\quad\quad{}+\frac{1}{2}\int\frac{\ln(1+\alpha^2)}{1+\alpha^2}\,d\alpha\\
&=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2)-\frac{1}{2}\int\frac{\ln(1+\alpha^2)}{1+\alpha^2}\,d\alpha\\
&{}\quad\quad\quad{}+\frac{1}{2}\int\frac{\ln(1+\alpha^2)}{1+\alpha^2}\,d\alpha\\
&=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2)+C\quad\Longrightarrow\quad I(\alpha)=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2).
\end{align*}
$$

Hence we have: $\displaystyle\int_0^{\alpha}\frac{\ln(1+\alpha x)}{1+x^2}\,dx=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2)$.

The special case $\alpha=1$ now reads

$$
\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx=\frac{1}{2}\arctan(1)\ln(2)=\frac{1}{2}\cdot\frac{1}{4}\pi\cdot\ln(2)=\frac{1}{8}\pi\ln(2).
$$

Similarly, the integral $\displaystyle\int_0^1\frac{\arctan(x)}{1+x}\,dx$ is a special case of

$$
\begin{align*}
\alpha\int_0^{\alpha}\frac{\arctan(x)}{1+\alpha x}\,dx&=\int_0^{\alpha}\arctan(x)\,d\ln(1+\alpha x)\\
&=\arctan(x)\ln(1+\alpha x)\bigg|_0^{\alpha}-\int_0^{\alpha}\ln(1+\alpha x)\,d\arctan(x)\\
&=\arctan(\alpha)\ln(1+\alpha^2)-\int_0^{\alpha}\frac{\ln(1+\alpha x)}{1+x^2}\,dx.
\end{align*}
$$

This implies that: 

$$
\alpha\int_0^{\alpha}\frac{\arctan(x)}{1+\alpha x}\,dx=\frac{1}{2}\arctan(\alpha)\ln(1+\alpha^2)=\int_0^{\alpha}\frac{\ln(1+\alpha x)}{1+x^2}\,dx.
$$

For $\alpha=1$ this reads {eq}`Eq:Integration:PartsSerret`.

::::::

## Grasple exercises
