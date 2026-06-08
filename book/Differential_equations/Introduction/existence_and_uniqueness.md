(Sec:DE:ExistenceUniqueness)=

# Existence and uniqueness of solutions

In this section we discuss under which conditions a differential equation has a solution, and whether this solution is unique.

- Domain of a DE
- E&U for linear any-order DEs
- E&U for nonlinear first-order DEs (Picard-Lindelöf theorem)
- E&U for IVPs & BVPs
- Navier-Stokes existence and uniqueness problem (mention as open problem)

## Introduction

In the previous section we showed that boundary value problems might have no solution, a unique solution or even infinitely many solutions.

Furthermore, we mentioned that a first-order differential equation has a solution with one degree of freedom denoted by an arbitrary constant of integration. This constant can be determined by using an initial value. In this section we prove this, first for linear differential equations and then for more general (not necessary linear) differential equations.

For second-order differential equations we prove an existence and uniqueness theorem for initial-value problems in the case of a linear differential equation.

## First-order differential equations

We start with the case of a linear first-order differential equation and an initial value.

::::::{prf:theorem} 
:label: Thm:DE:ExistenceUniquenessODE1Linear
If the functions $p$ and $g$ are continuous on an open interval $I=(a,b)$ containing the point $t_0$, then there exists a unique function $y=f(t)$ that satisfies the differential equation

:::{math}
:label: Eq:DE:ODE1Linear
y'+p(t)y=g(t)
:::

for each $t$ in $I$, and that also satisfies the initial condition

$$
y(t_0)=y_0,
$$

where $y_0$ is an arbitrary prescribed initial value.
::::::

Note that {prf:ref}`Thm:DE:ExistenceUniquenessODE1Linear` states that the initial-value problem *has* a solution (existence) and furthermore that it has *only one* solution (uniqueness).

::::::{admonition} Proof of {prf:ref}`Thm:DE:ExistenceUniquenessODE1Linear`
:class: tudproof, dropdown
The German mathematicician [Gottfried Wilhelm Leibniz (1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) discovered that if the differential equation is multiplied by a certain function $I(t)$, then the equation {eq}`Eq:DE:ODE1Linear` can be converted into one that can immediately be integrated by using the product rule for derivatives. This function $I(t)$ is called an **integrating factor**.

Since $p(t)$ is continuous, the integral $\displaystyle\int p(t)\,dt$ exists. Note that this denotes the set of all antiderivatives of $p(t)$. Taking just one of these antiderivatives we define

$$
I(t)=e^{\displaystyle\int_{t_0}^t p(s)\,ds}\neq0.
$$

Note that $I(t)$ is continuous and that we have $I'(t)=p(t)I(t)$. Therefore

$$
I(t)y'(t)+I(t)p(t)y(t)=\frac{d}{dt}\left\{I(t)y(t)\right\}.
$$

Hence we have

$$
\frac{d}{dt}\left\{I(t)y(t)\right\}=I(t)g(t)\quad\Longrightarrow\quad I(t)y(t)=\int I(t)g(t)\,dt.
$$

The latter integral exists since $I(t)$ and $g(t)$ are both continuous. Now we may write

$$
I(t)y(t)=\int_{t_0}^tI(s)g(s)\,ds+C,
$$

where $C$ is an arbitrary constant of integration. Since $I(t_0)=e^0=1$ we conclude that

$$
y(t_0)=y_0\quad\Longleftrightarrow\quad C=y_0.
$$

This proves the theorem.
::::::

In the case of first-order differential equations one can also prove a more general result. This is called the Picard-Lindelöf theorem, named after the French mathematician [Charles Émile Picard (1856-1941)](https://en.wikipedia.org/wiki/%C3%89mile_Picard) and the Swedish mathematician [Ernst Leonard Lindelöf (1870-1946)](https://en.wikipedia.org/wiki/Ernst_Leonard_Lindel%C3%B6f).

::::::{prf:theorem} Picard-Lindelöf theorem
:label: Thm:DE:ExistenceUniquenessODE1Nonlinear
Let the functions $f$ and $\partial f/\partial y$ be continuous in some rectangle $\alpha<t<\beta$ and $\gamma<y<\delta$ containing the point $(t_0,y_0)$. Then, in some interval $(t_0-h,t_0+h)$ contained in $(\alpha,\beta)$ there exists a unique solution $y=\phi(t)$ of the initial-value problem

:::{math}
:label: Eq:DE:ODE1NonLinear
y'=f(t,y),\quad y(t_0)=y_0.
:::

::::::

::::::{admonition} Proof of {prf:ref}`Thm:DE:ExistenceUniquenessODE1Nonlinear`
:class: tudproof, dropdown
We just give an outline of the proof.

Integrating {eq}`Eq:DE:ODE1NonLinear` we conclude that it is equivalent to

$$
y(t)=y_0+\int_{t_0}^tf(s,y(s))\,ds.
$$

Now we use the **method of successive approximations** or **Picard's iteration method**, named after the French mathematician [Charles Émile Picard (1856-1941)](https://en.wikipedia.org/wiki/%C3%89mile_Picard). We start with

$$
\phi_0(t)=y_0.
$$

This function satisfies the initial condition $y(t_0)=y_0$. Now we define

$$
\phi_{n+1}(t)=y_0+\int_{t_0}^tf(s,\phi_n(s))\,ds,\quad n=0,1,2,\ldots
$$

Then every function in the sequence $\{\phi_n(t)\}_{n=0}^{\infty}$ satisfies the initial condition $y(t_0)=y_0$. The so-called *Lipschitz condition* $\partial f/\partial y$ implies that the sequence converges to a function $\phi(t)$ that satisfies both the differential equation and the initial condition.

Furthermore, it can be shown that this solution $\phi(t)$ is unique.
::::::

:::{todo}
Include proof of {prf:ref}`Thm:SlopeCurves:IFT`.

:::

## Second-order differential equations

In the case of a linear second-order differential equation we have:

::::::{prf:theorem} 
:label: Thm:DE:ExistenceUniquenessODE2Linear
Consider the initial-value problem

$$ 
y''+p(t)y'+q(t)y=g(t),\quad y(t_0)=y_0,\quad y'(t_0)=y_0',
$$

where $p$, $q$ and $g$ are continuous functions on an open interval $I$ that contains the point $t_0$. This problem has exactly one solution $y=\phi(t)$, and the solution exists throughout the interval $I$.
::::::

Also for second-order differential equations one can prove a more general result:

::::::{prf:theorem}
:label: Thm:DE:ExistenceUniquenessODE2Nonlinear
Let the functions $f$, $\partial f/\partial y$ and $\partial f/\partial y'$ be continuous in some open region containing the point $(t_0,y_0,y_0')$. Then, there exists a unique solution $y=\phi(t)$ of the initial-value problem

:::{math}
:label: Eq:DE:ODE2NonLinear
y''=f(t,y,y'),\quad y(t_0)=y_0,\quad y'(t_0)=y_0'.
:::

::::::

Proof of {prf:ref}`Thm:DE:GeneralSolutionHomogeneous`
