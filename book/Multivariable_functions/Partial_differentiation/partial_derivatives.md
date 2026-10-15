(Sec:PartialDerivatives)=
# Partial derivatives

In this section we cover:

- Partial derivatives for functions of two variables
- Partial derivatives for functions of three or more variables
- Notation
- Higher order partial derivatives, including Clairaut's theorem
- Chain rule
- Implicit function theorem
- Application: partial differential equations, only introduction of the topic and showing a function is a solution. Not solving PDEs.
- Feynman’s integration trick 

(Sec:Integration:Feynman)=

## Feynman’s integration trick

Sometimes an integral is easier to evaluate if we modify the integrand by inserting a parameter such that a specific value of this parameter leads to the original integral. This technique was developed by the American theoretical physicist [Richard Phillips Feynman (1918-1988)](https://en.wikipedia.org/wiki/Richard_Feynman) and is based on the following theorem.

::::::{prf:Theorem}
:label: Thm:Integration:ImproperIntegralsFeynmanTechnique
If $g(x,t)$ and $\displaystyle\frac{\partial}{\partial t}g(x,t)$ are both continuous for all $x\in[a,b]$, then

$$
\frac{d}{dt}\int_a^bg(x,t)\,dx=\int_a^b\frac{\partial}{\partial t}g(x,t)\,dx.
$$

::::::

Feynman’s integration trick itself is most naturally described by the following algorithm:

:::{prf:algorithm} Feynman’s integration trick
For any definite integral of the form $\displaystyle\int_a^bf(x)\,dx$ perform the following steps:

1. Introduce a parameter-dependent function $g$ based on the integrand $f$ and define $I(t)=\displaystyle\int_a^bg(x,t)\,dx$ such that

    - $I(t_0)=\alpha$ for some value of $t_0$ and some constant $\alpha\in\mathbb{R}$.

    - $g(x,t_1)=f(x)$ for some value of $t_1$. This implies that $I(t_1)=\displaystyle\int_a^bf(x)\,dx$.

3. Find the partial derivative $\displaystyle\frac{\partial}{\partial t}g(x,t)$.

4. Evaluate the integral $I'(t)=\displaystyle\int_a^b\frac{\partial}{\partial t}g(x,t)\,dx$.

5. Integrate $I'(t)$ with respect to $t$ to find $I(t)$ (including a constant of integration).

6. Determine the value of the constant of integration using the value of $I(t_0)=\alpha$.

6. Evaluate $I(t_1)$ to find the value of the original integral $\displaystyle\int_a^bf(x)\,dx$.
:::

Finding a function $g(x,t)$ that works can be very hard. We will give three examples, where this function will be given.

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsFeynmanExample1
Consider the improper integral $\displaystyle\int_0^1\frac{x-1}{\ln(x)}\,dx$, which is extremely difficult to evaluate by any other means.

Define $g(x,t)=\dfrac{x^t-1}{\ln(x)}$ and $I(t)=\displaystyle\int_0^1\frac{x^t-1}{\ln(x)}\,dx$ for $t\geq0$, then we have $I(0)=0$,

$$
\frac{\partial}{\partial t}g(x,t)=\frac{x^t\ln(x)}{\ln(x)}=x^t,
$$

and

$$
I'(t)=\int_0^1\frac{\partial}{\partial t}\frac{x^t-1}{\ln(x)}\,dx=\int_0^1x^t\,dx=\frac{x^{t+1}}{t+1}\bigg|_{x=0}^1=\frac{1}{t+1}.
$$

This implies that $I(t)=\ln|t+1|+C$ with $C=I(0)=0$. This gives

$$
I(t)=\int_0^1\frac{x^t-1}{\ln(x)}\,dx=\ln(t+1)
$$

for $t\geq0$. We conclude that

$$
I(1)=\int_0^1\frac{x-1}{\ln(x)}\,dx=\ln(2).
$$

Similarly, we find that 

$$
I(2)=\int_0^1\frac{x^2-1}{\ln(x)}\,dx=\ln(3)
$$ 

and 

$$
I(\tfrac{1}{2})=\int_0^1\frac{\sqrt{x}-1}{\ln(x)}\,dx=\ln\left(\tfrac{3}{2}\right),
$$ 

for instance.

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsFeynmanExample2
Consider the integral $\displaystyle\int_0^1\frac{\sin(\ln(x))}{\ln(x)}\,dx$.

Let $I(t)=\displaystyle\int_0^1\frac{\sin(t\ln(x))}{\ln(x)}\,dx$, then we have $I(0)=0$ and using the substitution $\ln(x)=y$ or $x=e^y$

$$
I'(t)=\int_0^1\cos(t\ln(x))\,dx=\int_{-\infty}^0\cos(ty)e^y\,dy=\int_0^{\infty}e^{-y}\cos(ty)\,dy.
$$

Now we have using integration by parts

\begin{align*}
\int_0^{\infty}e^{-y}\cos(ty)\,dy&=-e^{-y}\cos(ty)\bigg|_0^{\infty}-t\int_0^{\infty}e^{-y}\sin(ty)\,dy\\
&=1+te^{-y}\sin(ty)\bigg|_{y=0}^{\infty}-t^2\int_0^{\infty}e^{-y}\cos(ty)\,dy\\
&=1-t^2\int_0^{\infty}e^{-y}\cos(ty)\,dy.
\end{align*}

Because the integral $I'(t)$ appears on both sides of the equation, we can solve for $I'(t)$ to find that

$$
I'(t)=\int_0^{\infty}e^{-y}\cos(ty)\,dy=\frac{1}{1+t^2}.
$$

Since $I(0)=0$ this implies that $I(t)=\arctan(t)$.

We finally arrive at

$$
\int_0^1\frac{\sin(\ln(x))}{\ln(x)}\,dx=I(1)=\arctan(1)=\frac{1}{4}\pi.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:ImproperIntegralsFeynmanExample3
Consider the integral $I(t)=\displaystyle\int_0^{\infty}\frac{e^{-x}\sin(xt)}{x}\,dx$ for $t\geq0$. Since $\displaystyle\lim\limits_{x\to 0^+}\frac{\sin(xt)}{x}=t$, the integral is convergent. Then we have $I(0)=0$ and using integration by parts

\begin{align*}
I'(t)&=\int_0^{\infty}e^{-x}\cos(xt)\,dx\\
&=-e^{-x}\cos(xt)\bigg|_{x=0}^{\infty}-t\int_0^{\infty}e^{-x}\sin(xt)\,dt\\
&=1+te^{-x}\sin(xt)\bigg|_{x=0}^{\infty}-t^2\int_0^{\infty}e^{-x}\cos(xt)\,dt\\
&=1+0-t^2I'(t),
\end{align*}

and therefore $I'(t)=\dfrac{1}{1+t^2}$. This implies that $I(t)=\displaystyle\arctan(t)$.

For instance, this implies that $\displaystyle\int_0^{\infty}\frac{e^{-x}\sin(x)}{x}\,dx=\arctan(1)=\frac{1}{4}\pi$. Using the substitution $x=\alpha t$ this implies that

$$
\int_0^{\infty}\frac{e^{-\alpha t}\sin(\alpha t)}{t}\,dt=\frac{1}{4}\pi\quad\text{for all}\quad\alpha>0.
$$ 

Furthermore, we have

$$
\int_0^{\infty}\frac{e^{-x}\sin(x\sqrt{3})}{x}\,dx=\arctan\left(\sqrt{3}\right)=\frac{1}{3}\pi
$$

and

$$
\int_0^{\infty}\frac{e^{-t\sqrt{3}}\sin(t)}{t}\,dt=\int_0^{\infty}\frac{e^{-x}\sin\left(\frac{x}{\sqrt{3}}\right)}{x}\,dx=\arctan\left(\tfrac{1}{\sqrt{3}}\right)=\frac{1}{6}\pi.
$$

::::::

Now we turn our attention to the *Dirichlet integral*:

:::{prf:definition} The Dirichlet integral
:label: Def:Integration:ImproperIntegralsDirichletIntegral

The **Dirichlet integral** is defined by the improper integral

$$
\int_0^{\infty}\frac{\sin(x)}{x}\,dx.
$$

:::

This integral is named after the German mathematician [Johann Peter Gustav Lejeune Dirichlet (1805-1859)](https://en.wikipedia.org/wiki/Peter_Gustav_Lejeune_Dirichlet).

This special integral can be evaluated using Feynman's integration trick, which leads to the following result.

::::::{prf:Theorem} The Dirichlet integral
:label: Thm:Integration:ImproperIntegralsDirichletIntegral

$$
\int_0^{\infty}\frac{\sin(x)}{x}\,dx=\frac{1}{2}\pi.
$$

::::::

::::::{admonition} Proof of {prf:ref}`Thm:Integration:ImproperIntegralsDirichletIntegral`
:class: tudproof, dropdown
:name: Proof:Integration:ImproperIntegralsDirichletIntegral

We start by showing that the integral converges. First we write

$$
\int_0^{\infty}\frac{\sin(x)}{x}\,dx=\int_0^1\frac{\sin(x)}{x}\,dx+\int_1^{\infty}\frac{\sin(x)}{x}\,dx.
$$

The first integral on the right exists, because $\dfrac{\sin(x)}{x}\leq 1$ for $0\leq x\leq1$ and thus

$$
\int_0^1\frac{\sin(x)}{x}\,dx \leq \int_0^11\,dx = 1.
$$

For the second integral on the right we have

$$
\int_1^{\infty}\frac{\sin(x)}{x}\,dx=\lim_{R\to\infty}\int_1^R\frac{\sin(x)}{x}\,dx.
$$

Using integration by parts we obtain

\begin{align*}
\int_1^R\frac{\sin(x)}{x}\,dx&=\bigg[-\frac{\cos(x)}{x}\bigg]_1^R-\int_1^R\frac{\cos(x)}{x^2}\,dx\\
&=\cos(1)-\frac{\cos(R)}{R}-\int_1^R\frac{\cos(x)}{x^2}\,dx.
\end{align*}

Now we have

$$
\left|\int_1^R\frac{\cos(x)}{x^2}\,dx\right|\leq\int_1^R\left|\frac{\cos(x)}{x^2}\right|\,dx\leq\int_1^R\frac{1}{x^2}\,dx=\left[-\frac{1}{x}\right]_1^R=1-\frac{1}{R}.
$$

Since $\displaystyle\lim_{R\to\infty}\frac{\cos(R)}{R}=0$ and $\displaystyle\lim_{R\to\infty}\frac{1}{R}=0$ we conclude that $\displaystyle\int_1^{\infty}\frac{\sin(x)}{x}\,dx$ converges.

This shows that $\displaystyle\int_0^{\infty}\frac{\sin(x)}{x}\,dx$ is convergent.

Now let

$$
I(t)=\int_0^{\infty}e^{-xt}\frac{\sin(x)}{x}\,dx.
$$

Then we have

\begin{align*}
I'(t)&=\int_0^{\infty}\frac{\partial}{\partial t}\left(e^{-xt}\frac{\sin(x)}{x}\right)\,dx\\
&=\int_0^{\infty}-e^{-xt}\sin(x)\,dx\\
&=\bigg[e^{-xt}\cos(x)\bigg]_0^{\infty}+\int_0^{\infty}t\cos(x)e^{-xt}\,dx\\
&=-1+\int_0^{\infty}te^{-xt}\cos(x)\,dx\\
&=-1+\bigg[te^{-xt}\sin(x)\bigg]_0^{\infty}+\int_0^{\infty}t^2\sin(x)e^{-xt}\,dx\\
&=-1+t^2\int_0^{\infty}e^{-xt}\sin(x)\,dx \\
&= -1-t^2I'(t)
\end{align*}

This implies that $I'(t)=\displaystyle\int_0^{\infty}e^{-xt}\sin(x)\,dx=\dfrac{-1}{1+t^2}$ and therefore $I'(t)=\dfrac{-1}{1+t^2}$. So

$$
I(t)=-\arctan(t)+C.
$$

Note that $0=\displaystyle\lim\limits_{t\to\infty}I(t)=-\frac{1}{2}\pi+C$, which implies that $C=\dfrac{1}{2}\pi$. We conclude that

$$
I(t)=-\arctan(t)+\frac{1}{2}\pi
$$

and finally that

$$
\int_0^{\infty}\frac{\sin(x)}{x}\,dx=I(0)=\frac{1}{2}\pi.
$$

::::::