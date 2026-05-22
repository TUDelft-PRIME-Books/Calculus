(Sec:Integration:Parts)=

# Integration by parts

## Introduction

In the previous sections we have seen how to evaluate definite and indefinite integrals of standard functions and linear combinations of these standard functions, and also how to apply the method of integration by substitution.

Now consider the following indefinite integral:

$$
\displaystyle\int x\cos(x)\,dx.
$$

Although the integrand is composed of two standard functions, $x$ and $\cos(x)$, we cannot directly apply the formulas from {numref}`Tab:Integration:StandardIndefiniteIntegrals` to evaluate this integral. We can also not use {prf:ref}`Th:Integration:IndefiniteProperties` to split the integral into simpler integrals, since the integrand is a product of functions instead of a sum of functions. Finally, the method of integration by substitution is not useful here either, since antiderivatives of both $x$ and $\cos(x)$ are not present in the integrand.

In this section we introduce the method of **integration by parts**, which is a very powerful method to evaluate integrals such as in the example above.

## Indefinite integrals

The method of **integration by parts** is based on the product rule: if $f$ and $g$ are both differentiable, then

$$
\left(f(x)g(x)\right)'=f(x)g'(x)+g(x)f'(x).
$$

Switching the left-hand and right-hand sides and integrating leads to

$$
\int\left(f(x)g'(x)+g(x)f'(x)\right)\,dx= \int\left(f(x)g(x)\right)'\,dx.
$$

Now, by the {prf:ref}`fundamental theorem of calculus<Thm:Integration:FundamentalTheoremPart1>`, this leads to

$$
\int f(x)g'(x)\,dx+\int g(x)f'(x)\,dx=f(x)g(x).
$$

Hence, we have the following theorem:

::::::{prf:Theorem} Integration by parts for indefinite integrals
:label: Thm:Integration:PartsIndefiniteIntegral
If $f$ and $g$ are differentiable and $f'$ and $g'$ are continuous, then

:::{math}
:label: Eq:Integration:PartsIndefiniteIntegral
\int f(x)g'(x)\,dx=f(x)g(x)-\int g(x)f'(x)\,dx.
:::

::::::

Note that the continuity of $f'$ and $g'$ implies the existence of the integrals. However, it also works under less strict conditions.

:::::{prf:notation}
:label: Not:Integration:PartsIndefiniteIntegral

If $u=f(x)$ then $du=f'(x)\,dx$, and if $v=g(x)$ then $dv=g'(x)\,dx$.

Note that Equation {eq}`Eq:Integration:PartsIndefiniteIntegral` can also be written as

:::{math}
:label: Eq:Integration:PartsIndefiniteIntegralDifferentialNotation
\displaystyle\int u\,dv=uv-\int v\,du
:::

using this differential notation.
:::::

Before we apply the method of integration by parts to the integral $\displaystyle\int x\cos(x)\,dx$, we will give you an algorithm to apply the method:

::::::{prf:algorithm}
:label: Alg:Integration:IntegrationByPartsIndefiniteIntegral

To evaluate an indefinite integral of the form $\displaystyle\int I(x)\,dx$ using the method of integration by parts, follow these steps:

1. Select the function $f(x)$ in the integrand $I(x)$.
2. Determine the function $g'(x)$ such that $I(x)=f(x)g'(x)$.
3. Set $u=f(x)$ and derive $du=f'(x)\,dx$.
4. Set $dv=g'(x)\,dx$ and choose $v=g(x)$.
5. Apply Equation {eq}`Eq:Integration:PartsIndefiniteIntegralDifferentialNotation` to rewrite the integral.
6. Evaluate, after possibly a repetition of the above steps, the remaining indefinite integral using standard methods.

::::::

::::::{prf:Example}
:label: Ex:Integration:PartsPowerCos

Let us revisit the integral $\displaystyle\int x\cos(x)\,dx$ introduced at the beginning of this section.

Taking $u=x$ and $dv=\cos(x)\,dx$, we obtain $du=dx$ and we might choose $v=\sin(x)$. Applying this to Equation {eq}`Eq:Integration:PartsIndefiniteIntegralDifferentialNotation` we obtain

\begin{align*}
\int x\cos(x)\,dx&=x\sin(x)-\int\sin(x)\,dx\\
&=x\sin(x)+\cos(x)+C.
\end{align*}
::::::

Note that the choice $u=x$ and $dv=\cos(x)\,dx$ was crucial. The other choice $u=\cos(x)$ and $dv=x\,dx$ and therefore $du=-\sin(x)\,dx$ and $v=\frac{1}{2}x^2$, for example, leads to a more difficult integral:

$$
\int x\cos(x)\,dx=\frac{1}{2}x^2\cos(x)+\frac{1}{2}\int x^2\sin(x)\,dx.
$$

That $\cos(x)$ in the integrand is replaced by $\sin(x)$ does not make the integral more difficult. However, the raising of the power of $x$ does. 

Sometimes we have to apply the method more than once. This is shown in the next example.

::::::{prf:Example}
:label: Ex:Integration:PartsPowerExp

We start with applying the method of integration by parts to the integral $\displaystyle\int x^2e^{2x}\,dx$. Taking $u=x^2$ and $dv=e^{2x}\,dx$, we obtain $du=2x\,dx$ and choose $v=\dfrac{1}{2}e^{2x}$. Applying this to Equation {eq}`Eq:Integration:PartsIndefiniteIntegralDifferentialNotation` we obtain

\begin{align*}
\int x^2e^{2x}\,dx&=\frac{1}{2}x^2e^{2x}-\int \frac{1}{2}e^{2x}\,2x\,dx\\
&=\frac{1}{2}x^2e^{2x}-\int xe^{2x}\,dx.
\end{align*}

Note that the integral $\displaystyle\int xe^{2x}\,dx$ looks easier to evaluate than the original integral $\displaystyle\int x^2e^{2x}\,dx$. However, we still don't know an antiderivative of the integrand. Using integration by parts once more on the remaining indefinite integral, we obtain, by choosing $u=x$ and $dv=e^{2x}\,dx$ (which implies that $du=dx$ and $v=\dfrac{1}{2}e^{2x}$ for instance):

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

Note that in both {prf:ref}`Ex:Integration:PartsPowerCos` and {prf:ref}`Ex:Integration:PartsPowerExp` the power of $x$ was lowered by $1$ in each step.

If the integrand consists of only one function, we may choose $u$ to be the integrand and $dv=dx$: 

::::::{prf:Example}
:label: Ex:Integration:PartsAntiderivativeArctan
In order to find an antiderivative of $\arctan(x)$ we apply integration by parts using $u=\arctan(x)$ and $dv=dx$:

\begin{align*}
\int\arctan(x)\,dx&=x\arctan(x)-\int x\,\frac{1}{1+x^2}\,dx\\
&=x\arctan(x)-\frac{1}{2}\ln(1+x^2)+C,
\end{align*}

where the substitution $t=1+x^2$ is used to evaluate the final remaining integral.

Note that the result can also be written as 

$$
\int\arctan(x)\,dx=x\arctan(x)-\ln\left(\sqrt{1+x^2}\right)+C.
$$

::::::

If we have a choice, which part of the integrand should be chosen as $u$ and which part as $dv$? 

Note that basic trigonometric functions, sine and cosine, and exponential functions do not become more complicated after integration. In the case of an algebraic function (a power of $x$) we only have a slightly increase of the power of $x$. However, for logarithmic functions or inverse trigonometric functions this leads to much more complicated functions.

We can incorporate these observations in the algorithm {prf:ref}`Alg:Integration:IntegrationByPartsIndefiniteIntegral` as follows:

::::::{prf:algorithm}
:label: Alg:Integration:IntegrationByPartsIndefiniteIntegralLIATE

To evaluate an indefinite integral of the form $\displaystyle\int I(x)\,dx$ using the method of integration by parts, follow these steps:

1. Select the function $f(x)$ in the integrand $I(x)$:
    - If there is a logarithmic function, choose it for $f(x)$.
    - Otherwise, if there is an inverse trigonometric function, choose it for $f(x)$.
    - Otherwise, if there is an algebraic function (a power of $x$), choose it for $f(x)$.
    - Otherwise, if there is a trigonometric function, choose it for $f(x)$.
    - Otherwise, if there is an exponential function, choose it for $f(x)$.
    - Otherwise, choose another part of the integrand for $f(x)$.
2. Determine the function $g'(x)$ such that $I(x)=f(x)g'(x)$.
3. Set $u=f(x)$ and derive $du=f'(x)\,dx$.
4. Set $dv=g'(x)\,dx$ and choose $v=g(x)$.
5. Apply Equation {eq}`Eq:Integration:PartsIndefiniteIntegralDifferentialNotation` to rewrite the integral.
6. Evaluate, possibly after a repetition of the above steps, the remaining indefinite integral using standard methods.

::::::

This is sometimes called the **LIATE rule**. If possible we choose for $u$ a **L**ogarithm, an **I**nverse trigonometric function, an **A**lgebraic function (a power of $x$), a **T**rigonometric function or an **E**xponential function, in that order.

In {prf:ref}`Ex:Integration:PartsPowerCos` and {prf:ref}`Ex:Integration:PartsPowerExp` we chose the algebraic function ($x$ and $x^2$, respectively) for $u$ instead of the trigonometric function ($\cos(x)$) or the exponential function ($e^{2x}$).

::::::{prf:Example}
:label: Ex:Integration:PartsPowerCosWrong
Consider $\displaystyle\int x^3\ln(x)\,dx$ for $x>0$. 

Note that $x^3$ is an algebraic function and $\ln(x)$ is a logarithm. So, if we choose $u=\ln(x)$ and $dv=x^3\,dx$, we obtain that $\displaystyle du=\frac{1}{x}\,dx$ and we might choose $v=\frac14x^4$. We have

\begin{align*}
\int x^3\ln(x)\,dx&=\frac{1}{4}x^4\ln(x)-\int \frac{1}{4}x^4\,\frac{1}{x}\,dx\\
&=\frac{1}{4}x^4\ln(x)-\int \frac{1}{4}x^3\,dx\\
&=\frac{1}{4}x^4\ln(x)-\frac{1}{16}x^4+C.
\end{align*}

::::::

Although the power of $x$ increases the method works in this case since $\ln(x)$ disappears and is replaced by $\dfrac{1}{x}$ which is easily combined with the power of $x$.

Note that this method works for each integral of the form $\displaystyle\int x^{\alpha}\ln(x)\,dx$ for every $\alpha\in\mathbb{R}\setminus\{-1\}$. The case $\alpha=-1$ is treated in the next example.

::::::{prf:Example}
:label: Ex:Integration:PartsLn
The integral $\displaystyle\int\frac{\ln(x)}{x}\,dx$ can be evaluated using the substitution $u=\ln(x)$, which implies that $du=\displaystyle\frac{1}{x}\,dx$, see {prf:ref}`Ex:Integration:SubstitutionDefiniteIntegralExample1`.

However, it can also be done using integration by parts. The LIATE rule suggests to use $u=\ln(x)$ and $dv=\dfrac{1}{x}\,dx$, which implies that $du=\dfrac{1}{x}\,dx$ and $v=\ln(x)$, for instance. We have

\begin{align*}
\int\frac{\ln(x)}{x}\,dx&=\ln(x)\cdot\ln(x)-\int\ln(x)\,\dfrac{1}{x}\,dx\\
&=(\ln(x))^2-\int\frac{\ln(x)}{x}\,dx+C.
\end{align*}
Hence, we have

:::{math}
:label: Eq:Integration:PartsLnIntermediate
\displaystyle 2\int\frac{\ln(x)}{x}\,dx=(\ln(x))^2
:::

and therefore 

$$
\int\frac{\ln(x)}{x}\,dx=\frac{1}{2}(\ln(x))^2+\frac{1}{2}C.
$$

Note that $C$ is an arbitrary constant, then so is $\frac{1}{2}C$. Hence, we may replace $\frac{1}{2}C$ by another arbitrary constant. 

::::::

Sometimes we might have even more possible ways to evaluate an integral:

:::::{prf:example}
:label: Ex:Integration:PartsSineCosine
Consider the integral $I=\displaystyle\int\sin(x)\cos(x)\,dx$. We might choose $u=\sin(x)$ and $dv=\cos(x)\,dx$, which implies that $du=\cos(x)\,dx$ and $v=\sin(x)$, for instance. Then we have

$$
\int\sin(x)\cos(x)\,dx=\sin(x)\cdot\sin(x)-\int\sin(x)\cos(x)\,dx.
$$

Hence, if we have

$$
2I=\sin^2(x)+K\quad\Longrightarrow\quad I=\frac{1}{2}\sin^2(x)+C.
$$

Note that we chose $C=\frac{1}{2}K$.
:::::

::::{question} Short-answer blocks
:type: short-answer
:variant: blocks
:columns: 1
:class: question
:admonition:
:showanswer:

Fill in the correct answer in the input field.

Use a capital $C$ to denote the arbitrary constant of integration.
---
M[-\frac{1}{4}\cos(2x)+C] Using the fact that $\sin(x)\cos(x)=\frac{1}{2}\sin(2x)$ we obtain that $\displaystyle\int\sin(x)\cos(x)\,dx=$
= We have

$$
\int\sin(x)\cos(x)\,dx=\frac{1}{2}\int\sin(2x)\,dx=-\frac{1}{4}\cos(2x)+C.
$$
---

::::

::::{question} Short-answer blocks
:type: short-answer
:variant: blocks
:columns: 1
:class: question
:admonition:
:showanswer:

Fill in the correct answer in the input field.

Use a capital $C$ to denote the arbitrary constant of integration.
---
M[-\frac{1}{2}\cos^2(x)+C] Choosing $u=\cos(x)$ and $dv=\sin(x)\,dx$ we obtain that $I=\displaystyle\int\sin(x)\cos(x)\,dx=$
= Since $du=-\sin(x)\,dx$ and $v=-\cos(x)$ for instance, we have

$$
\int\sin(x)\cos(x)\,dx=-\cos(x)\cdot\cos(x)-\int\cos(x)\sin(x)\,dx.
$$

Hence, we have

$$
2I=-\cos^2(x)+K\quad\Longrightarrow\quad I=-\frac{1}{2}\cos^2(x)+C.
$$

Note that we chose $C=\frac{1}{2}K$.

Using $\cos(2x)=2\cos^2(x)-1=1-2\sin^2(x)$ you may check that all different forms are correct. Compare with {prf:ref}`Ex:Integration:Antiderivatives`.
---

::::

In the next example we deal with a product of a trigonometric function and an exponential function.

::::::{prf:Example}
:label: Ex:Integration:PartsExpCos

For the integral $I=\displaystyle\int e^{-2x}\cos(3x)\,dx$, the LIATE rule suggests to choose the trigonometric function for $u$. So we pick $u=\cos(3x)$ and $dv=e^{-2x}\,dx$, which implies that $du=-3\sin(3x)\,dx$ and that we might choose $v=-\dfrac{1}{2}e^{-2x}$. We have

$$
\int e^{-2x}\cos(3x)\,dx =-\frac{1}{2}e^{-2x}\cos(3x)-\frac{3}{2}\int  e^{-2x}\sin(3x)\,dx
$$

In the new indefinite integral, we again choose the trigonometric function for $u$. So we pick $u=\sin(3x)$ and $dv=e^{-2x}\,dx$, which implies that $du=3\cos(3x)\,dx$ and $v=-\dfrac{1}{2}e^{-2x}$, for instance. We continue:

\begin{align*}
\int e^{-2x}\cos(3x)\,dx &= -\frac{1}{2}e^{-2x}\cos(3x)-\frac{3}{2}\int  e^{-2x}\sin(3x)\,dx \\
&= -\frac{1}{2}e^{-2x}\cos(3x)\\
&{}\hspace{10mm}{}-\frac{3}{2}\left(-\dfrac{1}{2}e^{-2x}\sin(3x)+\dfrac{3}{2}\int e^{-2x}\cos(3x)\,dx \right) \\
&= -\frac{1}{2}e^{-2x}\cos(3x)\\
&{}\hspace{10mm}{}+\frac{3}{4}e^{-2x}\sin(3x)-\dfrac{9}{4}\int e^{-2x}\cos(3x)\,dx.
\end{align*}

Notice that the integral in the final step equals $I$, the integral we would like to evaluate. This means that we have:

\begin{align*}
&~ & I &=-\frac{1}{2}e^{-2x}\cos(3x)+\frac{3}{4}e^{-2x}\sin(3x)-\frac{9}{4}I\\
&\Longrightarrow & \left(1+\frac{9}{4}\right)I &= -\frac{1}{2}e^{-2x}\cos(3x)+\frac{3}{4}e^{-2x}\sin(3x)+K
\end{align*}

with $K\in\mathbb{R}$ arbitrary. Since $1+\dfrac{9}{4}=\dfrac{13}{4}$ we conclude that

$$
I=-\frac{2}{13}e^{-2x}\cos(3x)+\frac{3}{13}e^{-2x}\sin(3x)+C.
$$

Note that we have replaced the arbitrary constant $\dfrac{4}{13}K$ by another arbitrary constant $C\in\mathbb{R}$.
::::::

Here we chose the trigonometric function for $u$ in both the first and the second step. In this case we could have chosen the exponential function instead. See {numref}`Exc:Integration:PartsOtherChoice`. However, it is important to stick to the same choice (trigonometric or exponential function) in the second step. Otherwise, we return to the original integral without any result:

\begin{align*}
\int e^{-2x}\cos(3x)\,dx &=-\frac{1}{2}e^{-2x}\cos(3x)-\frac{3}{2}\int e^{-2x}\sin(3x)\,dx\\
&=-\frac{1}{2}e^{-2x}\cos(3x)+\frac{1}{2}e^{-2x}\cos(3x)+\int e^{-2x}\cos(3x)\,dx.\\
&=\int e^{-2x}\cos(3x)\,dx.
\end{align*}

## Definite integrals

The method of integration by parts can also be applied to definite integrals. We derive the formula starting from the product rule: if $f$ and $g$ are both differentiable, then

$$
\left(f(x)g(x)\right)'=f(x)g'(x)+g(x)f'(x).
$$

Switching the left-hand and right-hand sides and integrating both sides from $a$ to $b$ we get

$$
\int_a^b\left(f(x)g'(x)+g(x)f'(x)\right)\,dx= \int_a^b\left(f(x)g(x)\right)'\,dx.
$$

This implies that

$$
\int_a^b f(x)g'(x)\,dx+\int_a^b g(x)f'(x)\,dx=f(x)g(x)\bigg|_a^b.
$$

In conclusion, we have the following theorem:

::::::{prf:Theorem} Integration by parts for definite integrals
:label: Thm:Integration:PartsDefiniteIntegral

If $f$ and $g$ are continuous on $[a,b]$, integrable and differentiable on $(a,b)$ and $f'$ and $g'$ are continuous on $(a,b)$, then

:::{math}
:label: Eq:Integration:PartsDefiniteIntegralDifferentialNotation
\int_a^bf(x)g'(x)\,dx=f(x)g(x)\bigg|_a^b-\int_a^bg(x)f'(x)\,dx.
:::

::::::

Similar to {prf:ref}`Not:Integration:PartsIndefiniteIntegral`, we can use the differential notation $u=f(x)$, $dv=g'(x)\,dx$, $du=f'(x)\,dx$ and $v=g(x)$.

We use this in an algorithm similar to {prf:ref}`Alg:Integration:IntegrationByPartsIndefiniteIntegralLIATE` to evaluate definite integrals:

::::::{prf:algorithm}
:label: Alg:Integration:IntegrationByPartsDefiniteIntegralLIATE

To evaluate a definite integral of the form $\displaystyle\int_{a}^{b} I(x)\,dx$ using the method of integration by parts, follow these steps:

1. Select the function $f(x)$ in the integrand $I(x)$:
    - If there is a logarithmic function, choose it for $f(x)$.
    - Otherwise, if there is an inverse trigonometric function, choose it for $f(x)$.
    - Otherwise, if there is an algebraic function (a power of $x$), choose it for $f(x)$.
    - Otherwise, if there is a trigonometric function, choose it for $f(x)$.
    - Otherwise, if there is an exponential function, choose it for $f(x)$.
    - Otherwise, choose another part of the integrand for $f(x)$.
2. Determine the function $g'(x)$ such that $I(x)=f(x)g'(x)$.
3. Set $u=f(x)$ and derive $du=f'(x)\,dx$.
4. Set $dv=g'(x)\,dx$ and choose $v=g(x)$.
5. Apply Equation {eq}`Eq:Integration:PartsDefiniteIntegralDifferentialNotation` to rewrite the integral.
6. Evaluate, after possibly a repetition of the above steps, the remaining definite integral using standard methods.

::::::

::::::{prf:Example}
:label: Ex:Integration:PartsDefiniteLn

We apply the method of integration by parts for definite integrals to $\displaystyle\int_1^e\ln(x)\,dx$:

$$
\int_1^e\ln(x)\,dx=x\ln(x)\bigg|_1^e-\int_1^ex\,\frac{1}{x}\,dx=e-\int_1^e1\,dx=e-(e-1)=1.
$$

::::::

Sometimes we need to combine the method of integration by parts and the method of integration by substitution to evaluate an integral as in the next example.

::::::{prf:Example}
:label: Ex:Integration:PartsDefiniteArcsin

Let us try to evaluate the integral $\displaystyle\int_0^{\frac{1}{2}}\arcsin(x)\,dx$. We start with the application of the method of integration by parts:

\begin{align*}
\int_0^{\frac{1}{2}}\arcsin(x)\,dx&=x\arcsin(x)\bigg|_0^{\frac{1}{2}}-\int_0^{\frac{1}{2}}x\,\frac{1}{\sqrt{1-x^2}}\,dx\\
&=\frac{1}{2}\cdot\frac{1}{6}\pi-\int_0^{\frac{1}{2}}\frac{x}{\sqrt{1-x^2}}\,dx.
\end{align*}

For the latter integral we use the substitution $u=1-x^2$ to obtain

\begin{align*}
\int_0^{\frac{1}{2}}\arcsin(x)\,dx&=\frac{1}{12}\pi+\sqrt{1-x^2}\bigg|_0^{\frac{1}{2}}\\
&=\frac{1}{12}\pi+\frac{1}{2}\sqrt{3}-1.
\end{align*}

::::::

Sometimes we should first perform an integration by substitution and then apply integration by parts:

::::::{prf:Example}
:label: Ex:Integration:PartsSubstitution
Let us evaluate $\displaystyle\int_4^9e^{\sqrt{x}}\,dx$.

First apply the substitution $t=\sqrt{x}$ which implies that $dt=\dfrac{1}{2\sqrt{x}}\,dx$ or $dx=2t\,dt$:

$$
\int_4^9e^{\sqrt{x}}\,dx=2\int_2^3te^t\,dt.
$$

Now we use integration by parts, with $u=t$ and $dv=e^t\,dt$ and therefore $du=dt$ and $v=e^t$ for instance, to obtain

\begin{align*}
\int_4^9e^{\sqrt{x}}\,dx&=2\int_2^3te^t\,dt \\
&=2te^t\bigg|_2^3-2\int_2^3e^t\,dt\\
&=6e^3-4e^2-2e^t\bigg|_2^3 \\
&=6e^3-4e^2-2e^3+2e^2\\
&=4e^3-2e^2.
\end{align*}
::::::

In {prf:ref}`Ex:Integration:SubstitutionTrigSerretsIntegral` we have seen that $\displaystyle\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx=\frac{1}{8}\pi\ln(2)$. This result can also be used to evaluate a similar integral involving the inverse tangent function:

:::::{prf:example} Serret's integral revisited
:label: Ex:Integration:IntegrationByPartsSerretsIntegral

Since we recognise $\dfrac{1}{1+x^2}$ as the derivative of $\arctan(x)$, we can use integration by parts to evaluate Serret's integral:

\begin{align*}
\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx&=\ln(1+x)\arctan(x)\bigg|_0^1-\int_0^1\frac{\arctan(x)}{1+x}\,dx\\
&=\frac{1}{4}\pi\ln(2)-\int_0^1\frac{\arctan(x)}{1+x}\,dx.
\end{align*}

Since $\displaystyle\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx=\frac{1}{8}\pi\ln(2)$ this implies that 

$$
\int_0^1\frac{\arctan(x)}{1+x}\,dx=\frac{1}{4}\pi\ln(2)-\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx=\frac{1}{8}\pi\ln(2)
$$

as well. Hence, we have

::::{math}
:label: Eq:Integration:PartsSerret
\int_0^1\frac{\arctan(x)}{1+x}\,dx=\frac{1}{8}\pi\ln(2)=\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx.
::::

:::::

::::{question} Short-answer blocks
:type: short-answer
:variant: blocks
:columns: 1
:class: question
:admonition:
:showanswer:

Fill in the correct answer in the input field.
---
M[0] Let $f$ be a function that satisfies $f(x)\cos(x)=f'(x)\sin(x)$. Then $\displaystyle\int_0^{\pi}f(x)\cos(x)\,dx=$
= Using integration by parts we obtain

\begin{align*}
\int_0^{\pi}f(x)\cos(x)\,dx&=\int_0^{\pi}f'(x)\sin(x)\,dx\\
 &=f(x)\sin(x)\bigg|_0^{\pi}-\int_0^{\pi}f(x)\cos(x)\,dx.
 &=f(x)\sin(x)\bigg|_0^{\pi}-\int_0^{\pi}f(x)\cos(x)\,dx.
\end{align*}

Hence, we have

$$
\int_0^{\pi}f(x)\cos(x)\,dx=\frac{1}{2}f(x)\sin(x)\bigg|_0^{\pi}=0.
$$

---

::::

## Reduction formulas

In {prf:ref}`Ex:Integration:PartsPowerExp` we evaluated the integral $\displaystyle\int x^2e^{2x}\,dx$ using integration by parts twice. What happens if we replace $x^2$ by a higher power of $x$? For instance, consider:

$$
\int x^{10}e^x\,dx=x^{10}e^x-10\int x^9e^x\,dx.
$$

Note that the latter integral has the same form as the original one, where the exponent of $x$ is lowered by one. If we apply the same technique once more to the latter integral we will end up with a similar integral with an exponent of $x$ lowered by one again. We may proceed in this way until the exponent of $x$ equals zero and the integral reads $\displaystyle\int e^x\,dx$, which can be evaluated directly using the fundamental theorem of calculus.

More generally, let $n\in\{1,2,3,\ldots\}$. Then we obtain

$$
\int x^ne^x\,dx=x^ne^x-n\int x^{n-1}e^x\,dx.
$$

So, if we define $I_n=\displaystyle\int x^ne^x\,dx$, then we have: $I_n=x^ne^x-nI_{n-1}$ for $n=1,2,3,\ldots$. Furthermore, we have $I_0=\displaystyle\int e^x\,dx=e^x+C_0$. Hence, we obtain the **reduction formula**

$$
I_n=x^ne^x-nI_{n-1},\quad n=1,2,3,\ldots\quad\text{with}\quad I_0=e^x+C_0.
$$

This implies that 

$$
I_1=xe^x-I_0=xe^x-e^x-C_0=(x-1)e^x+C_1,
$$

$$
I_2=x^2e^x-2I_1=x^2e^x-2xe^x+2e^x-2C_1=(x^2-2x+2)e^x+C_2,
$$

and so on. Note that we can change the constant of integration in each step. Moreover, if we put the factor $e^x$ outside the brackets, we find that, for example,

\begin{align*}
I_{10}&=\left(x^{10}-10x^9+90x^8-720x^7+5040x^6-30240x^5+151200x^4\right.\\
&{}\quad\quad\quad\left.{}-604800x^3+1814400x^2-3628800x+3628800\right)e^x+C_{10}.
\end{align*}

In {prf:ref}`Ex:Integration:PartsPowerCos` we evaluated the integral $\displaystyle\int x\cos(x)\,dx$ using integration by parts. What happens if we replace $x$ by a higher power of $x$?

Let $n\in\{2,3,4,\ldots\}$, then we obtain using integration by parts

$$
\int x^n\cos(x)\,dx = x^n\sin(x)-n\int x^{n-1}\sin(x)\,dx.
$$

Applying integration by parts once more, we find that

\begin{align*}
\int x^n\cos(x)\,dx&=x^n\sin(x)-n\int x^{n-1}\sin(x)\,dx\\
&=x^n\sin(x)+nx^{n-1}\cos(x)-n(n-1)\int x^{n-2}\cos(x)\,dx.
\end{align*}
So, if we define $I_n=\displaystyle\int x^n\cos(x)\,dx$, then we have: 

$$
I_n=x^n\sin(x)+nx^{n-1}\cos(x)-n(n-1)I_{n-2},\quad n=2,3,4,\ldots.
$$

Furthermore, we have $I_0=\displaystyle\int\cos(x)\,dx=\sin(x)+C_0$ and in {prf:ref}`Ex:Integration:PartsPowerCos` we found that $I_1=\displaystyle\int x\cos(x)\,dx=x\sin(x)+\cos(x)+C_1$. This leads to

$$
I_2=x^2\sin(x)+2x\cos(x)-2I_0=x^2\sin(x)+2x\cos(x)-2\sin(x)+C_2,
$$

\begin{align*}
I_3&=x^3\sin(x)+3x^2\cos(x)-6I_1\\
&=x^3\sin(x)+3x^2\cos(x)-6x\sin(x)-6\cos(x)+C_3,
\end{align*}
and so on.

## Grasple exercises

:::{todo}
Add Grasple exercises in {numref}`Sec:Integration:Parts`.
:::

## Exercises

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

\begin{align*}
\int\arcsin(x)\,dx&=x\arcsin(x)-\int x\,\frac{1}{\sqrt{1-x^2}}\,dx\\
&=x\arcsin(x)-\int\frac{x}{\sqrt{1-x^2}}\,dx\\
&=x\arcsin(x)+\sqrt{1-x^2}+C.
\end{align*}
:::

::::{exercise}
:label: Exc:Integration:PartsAntiderivativeOfArccos

Find an antiderivative of $\arccos(x)$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsAntiderivativeOfArccos`
:class: solution, dropdown

\begin{align*}
\int\arccos(x)\,dx&=x\arccos(x)-\int x\,\frac{-1}{\sqrt{1-x^2}}\,dx\\
&=x\arccos(x)+\int\frac{x}{\sqrt{1-x^2}}\,dx\\
&=x\arccos(x)-\sqrt{1-x^2}+C.
\end{align*}

Alternatively, since $\arcsin(x)+\arccos(x)=\frac{1}{2}\pi$ we have by using {numref}`Exc:Integration:PartsAntiderivativeOfArcsin`

\begin{align*}
\int\arccos(x)\,dx&=\int\left(\frac{1}{2}\pi-\arcsin(x)\right)\,dx\\
&=\frac{1}{2}\pi x-x\arcsin(x)-\sqrt{1-x^2}+C\\
&=x\arccos(x)-\sqrt{1-x^2}+C.
\end{align*}

:::

::::{exercise}
:label: Exc:Integration:PartsOtherChoice

Evaluate $\displaystyle\int e^{-2x}\cos(3x)\,dx$ by taking $u=e^{-2x}$ in each step.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsOtherChoice`
:class: solution, dropdown

\begin{align*}
\int e^{-2x}\cos(3x)\,dx &=\frac{1}{3}e^{-2x}\sin(3x)+\frac{2}{3}\int e^{-2x}\sin(3x)\,dx\\
&=\frac{1}{3}e^{-2x}\sin(3x)\\
&{}\hspace{10mm}{}+\frac{2}{3}\left(-\frac{1}{3}e^{-2x}\cos(3x)-\frac{2}{3}\int e^{-2x}\cos(3x)\,dx \right) \\
&=\frac{1}{3}e^{-2x}\sin(3x)\\
&{}\hspace{10mm}{}-\frac{2}{9}e^{-2x}\cos(3x)-\frac{4}{9}\int e^{-2x}\cos(3x)\,dx.
\end{align*}

Let $I=\displaystyle\int e^{-2x}\cos(3x)\,dx$, then we have:

\begin{align*}
&~ & I &= \frac{1}{3}e^{-2x}\sin(3x)-\frac{2}{9}e^{-2x}\cos(3x)-\frac{4}{9}I\\
&\Longrightarrow & \left(1+\frac{4}{9}\right)I &= \frac{1}{3}e^{-2x}\sin(3x)-\frac{2}{9}e^{-2x}\cos(3x)+K
\end{align*}

with $K\in\mathbb{R}$ aribtrary. Since $1+\dfrac{4}{9}=\dfrac{13}{9}$ we can again conclude that

$$
I=\frac{3}{13}e^{-2x}\sin(3x)-\frac{2}{13}e^{-2x}\cos(3x)+C.
$$

:::

::::{exercise}
:label: Exc:Integration:PartsSubstitutionSin

Evaluate $\displaystyle\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^3\sin(t^2)\,dt$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsSubstitutionSin`
:class: solution, dropdown
First apply the substitution $x=t^2$ which implies that $dx=2t\,dt$:

\begin{align*}
\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^3\sin(t^2)\,dt&=\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^2\sin(t^2)t\,dt\\
&=\frac{1}{2}\int_{\pi/2}^{\pi}x\sin(x)\,dx.
\end{align*}

Now we use integration by parts to find that

\begin{align*}
\int_{\sqrt{\pi/2}}^{\sqrt{\pi}}t^3\sin(t^2)\,dt &= \frac{1}{2}\int_{\pi/2}^{\pi}x\sin(x)\,dx \\
&=-\frac{1}{2}u\cos(x)\bigg|_{\pi/2}^{\pi}+\frac{1}{2}\int_{\pi/2}^{\pi}\cos(x)\,dx\\
&=\frac{1}{2}\pi+\frac{1}{2}\sin(x)\bigg|_{\pi/2}^{\pi}\\
&=\frac{1}{2}\pi-\frac{1}{2}.
\end{align*}

:::

::::{exercise}
:label: Exc:Integration:PartsReductionPowerExpNeg

Find a reduction formula for $\displaystyle\int x^ne^{-x}\,dx$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsReductionPowerExpNeg`
:class: solution, dropdown

$$
\int x^ne^{-x}\,dx = -x^ne^{-x}+n\int x^{n-1}e^{-x}\,dx.
$$

Define $I_n=\displaystyle\int x^ne^{-x}\,dx$, then we have

$$
I_n=-x^ne^{-x}+nI_{n-1},\quad n=1,2,3,\ldots.
$$

Furthermore, we have $I_0=\displaystyle\int e^{-x}\,dx=-e^{-x}+C_0$.
:::

::::{exercise}
:label: Exc:Integration:PartsReductionPowerSin

Find a reduction formula for $\displaystyle\int x^n\sin(x)\,dx$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsReductionPowerSin`
:class: solution, dropdown

\begin{align*}
\int x^n\sin(x)\,dx &= -x^n\cos(x)+n\int x^{n-1}\cos(x)\,dx\\
&=-x^n\cos(x)+nx^{n-1}\sin(x)-n(n-1)\int x^{n-2}\sin(x)\,dx.
\end{align*}

Define $I_n=\displaystyle\int x^n\sin(x)\,dx$, then we have

$$
I_n=-x^n\cos(x)+nx^{n-1}\sin(x)-n(n-1)I_{n-2},\quad n=2,3,4,\ldots.
$$

Furthermore, we have $I_0=\displaystyle\int\sin(x)\,dx=-\cos(x)+C_0$ and

\begin{align*}
I_1&= \int x\sin(x)\,dx\\
&=-x\cos(x)+\int\cos(x)\,dx\\
&=-x\cos(x)+\sin(x)+C_1.
\end{align*}

:::

::::{exercise}
:label: Exc:Integration:PartsReductionLn

Find a reduction formula for $\displaystyle\int\left(\ln(x)\right)^n\,dx$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:PartsReductionLn`
:class: solution, dropdown

\begin{align*}
\int\left(\ln(x)\right)^n\,dx&=x\left(\ln(x)\right)^n-n\int x\left(\ln(x)\right)^{n-1}\frac{1}{x}\,dx\\
&=x\left(\ln(x)\right)^n-n\int\left(\ln(x)\right)^{n-1}\,dx.
\end{align*}

Define $I_n=\displaystyle\int\left(\ln(x)\right)^n\,dx$, then we have

$$
I_n=x\left(\ln(x)\right)^n-nI_{n-1},\quad n=1,2,3,\ldots.
$$

Furthermore, we have: $I_0=\displaystyle\int1\,dx=x+C_0$.
:::

## Grasple exercises
