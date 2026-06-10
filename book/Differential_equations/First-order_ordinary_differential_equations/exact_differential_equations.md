(Sec:ODE1:Exact)=

# Exact differential equations 

In this section we cover:
- exact equations
- mention full/total differentials
- solving exact equations

Another specific form of a differential equation that can be solved is a so-called *exact* differential equation. Consider a differential equation of the form

$$
M(x,y)+N(x,y)\frac{dy}{dx}=0.
$$

Suppose that we can identify a function $\Phi(x,y)$ such that

$$
\frac{\partial}{\partial x}\Phi(x,y)=M(x,y)\quad\text{and}\quad\frac{\partial}{\partial y}\Phi(x,y)=N(x,y).
$$

Then we have

$$
M(x,y)+N(x,y)\frac{dy}{dx}=0\quad\Longleftrightarrow\quad\frac{\partial\Phi}{\partial x}+\frac{\partial\Phi}{\partial y}\frac{dy}{dx}=0\quad\Longleftrightarrow\quad\frac{d}{dx}\Phi(x,y)=0.
$$

This implies that $\Phi(x,y)=C$ with $C$ an arbitrary constant is an *implicit form* of the general solution.

::::::{prf:Definition}
A first-order differential equation is called **exact** if it can be written in the form:

$$
M(x,y)+N(x,y)\frac{dy}{dx}=0,
$$

where $M(x,y)$, $N(x,y)$, $M_y(x,y)$ and $N_x(x,y)$ are continuous functions with

$$
\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}\quad\text{or}\quad M_y(x,y)=N_x(x,y).
$$

::::::

::::::{prf:example}
Consider the differential equation $2x+y^2+2xy\dfrac{dy}{dx}=0$.

Then: $M(x,y)=2x+y^2$ and $N(x,y)=2xy$, which implies that

$$
\frac{\partial}{\partial y}M(x,y)=2y=\frac{\partial}{\partial x}N(x,y).
$$

This implies that there exists a function $\Phi(x,y)$ such that $\dfrac{\partial\Phi}{\partial x}=M$ and $\dfrac{\partial\Phi}{\partial y}=N$. Note that

$$
\Phi_x(x,y)=M(x,y)=2x+y^2\quad\Longrightarrow\quad\Phi(x,y)=x^2+xy^2+f(y),
$$

where $f(y)$ is an arbitrary function of $y$ only, and

$$
\Phi_y(x,y)=N(x,y)=2xy\quad\Longrightarrow\quad\Phi(x,y)=xy^2+g(x),
$$

where $g(x)$ is an arbitrary function of $x$ only.

Combining the latter two equations we conclude that $\Phi(x,y)=x^2+xy^2+k$ with $k$ an arbitrary constant. We conclude that

$$
x^2+xy^2=C,\quad C\in\mathbb{R}
$$

is the general implicit solution of the differential equation.
::::::

Note that we did not need the general solution for $\Phi(x,y)$ above. Only one particular solution for $\Phi(x,y)$ suffices to find the general implicit solution of the differential equation: $\Phi(x,y)=c$ with $c\in\mathbb{R}$.

::::::{prf:example}
Consider the differential equation 

$$
y^2\cos(x)+2xe^y-1+\left(2y\sin(x)+x^2e^y\right)\frac{dy}{dx}=0.
$$

Then: $M(x,y)=y^2\cos(x)+2xe^y-1$ and $N(x,y)=2y\sin(x)+x^2e^y$, which implies that

$$
\frac{\partial}{\partial y}M(x,y)=2y\cos(x)+2xe^y=\frac{\partial}{\partial x}N(x,y).
$$

This implies that there exists a function $\Phi(x,y)$ such that $\dfrac{\partial\Phi}{\partial x}=M$ and $\dfrac{\partial\Phi}{\partial y}=N$. Note that

$$
\begin{align*}
&\Phi_x(x,y)=M(x,y)=y^2\cos(x)+2xe^y-1\\
&{}\quad\Longrightarrow\quad\Phi(x,y)=y^2\sin(x)+x^2e^y-x+f(y)
\end{align*}
$$

and

$$
\begin{align*}
&\Phi_y(x,y)=N(x,y)=2y\sin(x)+x^2e^y\\
&{}\quad\Longrightarrow\quad\Phi(x,y)=y^2\sin(x)+x^2e^y+g(x).
\end{align*}
$$

Combining the latter two equations we conclude that we might choose $\Phi(x,y)=y^2\sin(x)+x^2e^y-x$. We conclude that

$$
y^2\sin(x)+x^2e^y-x=C,\quad C\in\mathbb{R}
$$

is the general implicit solution of the differential equation.
::::::

**Integrating factors**

Sometimes it is possible to convert a differential equation that is not exact into an exact differential equation by multiplying the equation by a suitable integrating factor. Compare with the method that we have seen in {numref}`Sec:ODE1:Linear`.

Consider a differential equation of the form

:::{math}
:label: Eq:ODE1:NotExact
M(x,y)+N(x,y)\frac{dy}{dx}=0
:::

and multiply by a factor $\mu(x,y)$:

:::{math}
:label: Eq:ODE1:Exact
\mu(x,y)M(x,y)+\mu(x,y)N(x,y)\frac{dy}{dx}=0.
:::

This differential equation is *exact* if and only if

$$
(\mu M)_y=(\mu N)_x.
$$

This implies that $\mu(x,y)$ should satisfy

:::{math}
:label: Eq:ODE1:ExactIntegrating
M\mu_y-N\mu_x+(M_y-N_x)\mu=0.
:::

If such a function $\mu(x,y)$ can be found, the general implicit solution can be found by solving the exact differential equation {eq}`Eq:ODE1:Exact`, which has the same solutions as the original differential equation {eq}`Eq:ODE1:NotExact`.

Although we only need one particular solution of {eq}`Eq:ODE1:ExactIntegrating`, which might have several solutions, it is not easy to solve this partial differential equation. However, in some special cases, where $\mu(x,y)$ is a function of $x$ only or a function of $y$ only, it is sometimes possible to find a solution.

When $\mu(x,y)=\mu(x)$ is a function of $x$ only, then $\mu_y=0$ and {eq}`Eq:ODE1:ExactIntegrating` implies that

$$
\frac{d\mu}{dx}=\frac{M_y-N_x}{N}\mu.
$$

If $\dfrac{M_y-N_x}{N}$ is a function of $x$ only, this differential equation is both separable and linear and can be solved to find a particular solution $\mu(x)$.

When $\mu(x,y)=\mu(y)$ is a function of $y$ only, then $\mu_x=0$ and {eq}`Eq:ODE1:ExactIntegrating` implies that

$$
\frac{d\mu}{dy}=\frac{N_x-M_y}{M}\mu.
$$

If $\dfrac{N_x-M_y}{M}$ is a function of $y$ only, this differential equation is both separable and linear and can be solved to find a particular solution $\mu(y)$.

::::::{prf:example}
Consider the differential equation $3xy+2y^2+(x^2+2xy)\dfrac{dy}{dx}=0$.

This differential equation is not exact since

$$
\frac{\partial}{\partial y}\left(3xy+2y^2\right)=3x+4y\neq2x+2y=\frac{\partial}{\partial x}\left(x^2+xy\right).
$$

Let $M(x,y)=3xy+2y^2$ and $N(x,y)=x^2+2xy$, then

$$
\frac{N_x-M_y}{M}=\frac{2x+2y-3x-4y}{3xy+2y^2}=-\frac{x+y}{y(3x+2y)}
$$

is not a function of $y$ only. However, for $x+2y\neq0$,

$$
\frac{M_y-N_x}{N}=\frac{3x+4y-2x-2y}{x^2+2xy}=\frac{x+2y}{x(x+2y)}=\frac{1}{x}
$$

is a function of $x$ only. Then we have

$$
\frac{d\mu}{dx}=\frac{M_y-N_x}{N}\mu\quad\Longrightarrow\quad\frac{d\mu}{dx}=\frac{\mu}{x}
$$

for which $\mu(x)=x$ is a solution. Multiplying by this integrating factor we obtain the exact differential equation

$$
3x^2y+2xy^2+(x^3+2x^2y)\frac{dy}{dx}=0.
$$

Then we obtain

$$
\Phi_x(x,y)=3x^2y+2xy^2\quad\Longrightarrow\quad\Phi(x,y)=x^3+x^2y^2+f(y)
$$

and

$$
\Phi_y(x,y)=x^3+2x^2y\quad\Longrightarrow\quad\Phi(x,y)=x^3y+x^2y^2+g(x).
$$

We conclude that we might choose $\Phi(x,y)=x^3y+x^2y^2$ and that

$$
x^3y+x^2y^2=C,\quad C\in\mathbb{R}
$$

is the general implicit solution of the differential equation.
::::::

::::::{prf:example}
Consider the differential equation $9x^2y+2y^2+(9x^3+8xy)\dfrac{dy}{dx}=0$.

This differential equation is not exact since

$$
\frac{\partial}{\partial y}\left(9x^2y+2y^2\right)=9x^2+4y\neq27x^2+8y=\frac{\partial}{\partial x}\left(9x^3+8xy\right).
$$

Let $M(x,y)=9x^2y+2y^2$ and $N(x,y)=9x^3+8xy$, then

$$
\frac{M_y-N_x}{N}=\frac{9x^2+4y-27x^2-8y}{9x^3+8xy}=-\frac{18x^2+4y}{x(9x^2+8y)}
$$

is not a function of $x$ only. However, for $9x^2+2y\neq0$, 

$$
\frac{N_x-M_y}{M}=\frac{27x^2+8y-9x^2-4y}{9x^2y+2y^2}=\frac{18x^2+4y}{y(9x^2+2y)}=\frac{2}{y}
$$

is a function of $y$ only.

Then we have

$$
\frac{d\mu}{dy}=\frac{N_x-M_y}{M}\mu\quad\Longrightarrow\quad\frac{d\mu}{dy}=\frac{2\mu}{y}
$$

for which $\mu(y)=y^2$ is a solution. Multiplying by this integrating factor we obtain the exact differential equation

$$
9x^2y^3+2y^4+(9x^3y^2+8xy^3)\frac{dy}{dx}=0.
$$

Then we obtain

$$
\Phi_x(x,y)=9x^2y^3+2y^4\quad\Longrightarrow\quad\Phi(x,y)=3x^3y^3+2xy^4+f(y)
$$

and

$$
\Phi_y(x,y)=9x^3y^2+8xy^3\quad\Longrightarrow\quad\Phi(x,y)=3x^3y^3+2xy^4+g(x).
$$

We conclude that we might choose $\Phi(x,y)=3x^3y^3+2xy^4$ and that

$$
3x^3y^3+2xy^4=C,\quad C\in\mathbb{R}
$$

is the general implicit solution of the differential equation.
::::::
