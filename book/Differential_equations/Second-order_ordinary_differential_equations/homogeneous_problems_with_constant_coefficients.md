(Sec:ODE2:Homogeneous)=

# Homogeneous problems with constant coefficients

In this section we cover:

- Ansatz method: three cases (two distinct real, single real, complex)
  - Be careful with using thew word Ansatz.
- Application examples:
  - Mass-spring
  - RLC electrical circuits 
- Mention third and higher order.
  - Example with fifth order to indicate that it is possible (example with 5th order with 1 double real root, 1 single real root, 1 pair of complex conjugate roots).
- Include IVPs and BVPs examples.

A homogeneous first-order linear differential equation with constant coefficients

$$
ay'+by=0,\quad a\neq0
$$

has the general solution $y=Ce^{rx}$ with $r=-\dfrac{b}{a}$.

In the case of a homogeneous second-order linear differential equation with *constant coefficients*

$$
ay''+by'+cy=0,\quad a,b,c\in\mathbb{R},\quad a\neq0
$$

we try $y=e^{rx}$ as a solution. Then $y'=re^{rx}$ and $y''=r^2e^{rx}$, and substitution leads to

$$
ar^2e^{rx}+bre^{rx}+ce^{rx}=0\quad\Longleftrightarrow\quad e^{rx}(ar^2+br+c)=0.
$$

Since $e^{rx}\neq0$ this leads to the **characteristic equation** (or **auxiliary equation**)

$$
ar^2+br+c=0,\quad a,b,c\in\mathbb{R},\quad a\neq0.
$$

Now we consider three possibilities for the **discriminant** $D=b^2-4ac$: $D>0$, $D=0$ and $D<0$.

If $D>0$ the characteristic equation has two different real solutions, say $r_1$ and $r_2$. Then the general solution is $y(x)=c_1e^{r_1x}+c_2e^{r_2x}$ with $c_1,c_2\in\mathbb{R}$.

::::::{prf:example}
The differential equation $y''-y'-6y=0$ has the characteristic equation $r^2-r-6=0\;\Longleftrightarrow\;(r-3)(r+2)=0$ with roots $r_1=3$ and $r_2=-2$. Hence, the general solution is $y=c_1e^{3x}+c_2e^{-2x}$ with $c_1,c_2\in\mathbb{R}$.
::::::

If $D=0$ the characteristic equation has two equal real solutions $r_1=r_2=r$. So we only have one linear independent solution $y=e^{rx}$ in that case. However, then $y=xe^{rx}$ is a solution too. In order to see this, we note that both $ar^2+br+c=0$ and $2ar+b=0$. Then, if a substitute $y=xe^{rx}$, $y'=(rx+1)e^{rx}$ and $y''=(r^2x+2r)e^{rx}$, we find that

$$
\begin{align*}
ay''+by'+cy&=a(r^2x+2r)e^{rx}+b(rx+1)e^{rx}+cxe^{rx}\\
&=(ar^2+br+1)xe^{rx}+(2ar+b)e^{rx}=0+0=0.
\end{align*}
$$

Since $y_1=e^{rx}$ and $y_2=xe^{rx}$ are linear independent, the general solution is $y=c_1e^{rx}+c_2xe^{rx}$ with $c_1,c_2\in\mathbb{R}$.

::::::{prf:example}
The differential equation $y''-6y'+9y=0$ has the characteristic equation $r^2-6r+9=0\;\Longleftrightarrow\;(r-3)^2=0$ with 'double' root $r=3$. Hence, the general solution is $y=c_1e^{3x}+c_2xe^{3x}$ with $c_1,c_2\in\mathbb{R}$.
::::::

If $D<0$ the characteristic equation has a complex conjugate pair as solutions, say $r=\alpha\pm i\beta$ with $\beta\neq0$. This implies that the general (complex) solution is a (complex) linear combination of

$$
e^{(\alpha+i\beta)x}=e^{\alpha x}\cdot e^{i\beta x}=e^{\alpha x}(\cos(\beta x)+i\sin(\beta x))
$$

and

$$
e^{(\alpha-i\beta)x}=e^{\alpha x}\cdot e^{-i\beta x}=e^{\alpha x}(\cos(\beta x)-i\sin(\beta x)).
$$

Note that it is possible to take certain (complex) linear combinations such that $e^{\alpha x}\cos(\beta x)$ and $e^{\alpha x}\sin(\beta x)$ are solutions. These solutions are real and linearly independent. This implies that the general solution is $y=c_1e^{\alpha x}\cos(\beta x)+c_2e^{\alpha x}\sin(\beta x)$ with $c_1,c_2\in\mathbb{R}$ in this case.

::::::{prf:example}
The differential equation $y''+4y'+13y=0$ has the characteristic equation $r^2+4r+13=0\;\Longleftrightarrow\;(r+2)^2+9=0$ with nonreal roots $r=-2\pm3i$. Hence, the general solution is $y=c_1e^{-2x}\cos(3x)+c_2e^{-2x}\sin(x)$ with $c_1,c_2\in\mathbb{R}$.
::::::

**Initial-value problems**

In {numref}`Sec:DE:ExistenceUniqueness` we have seen that an initial-value problem of the form

$$
\begin{cases}ay''+by'+cy=0,\quad a,b,c\in\mathbb{R},\quad a\neq0\\ \\y(t_0)=y_0,\quad y'(t_0)=y_0'\end{cases}
$$

has a unique solution.

::::::{prf:example}
Find the unique solution of the initial-value problem $\begin{cases}y''+y'-6y=0\\ \\y(0)=5,\quad y'(0)=0.\end{cases}$

Note that $y''+y'-6y=0$ has characteristic equation $r^2+r-6=0\;\Longleftrightarrow\;(r+3)(r-2)=0$ with solutions $r_1=2$ and $r_2=-3$. Hence, the general solution is $y=c_1e^{2x}+c_2e^{-3x}$ with $c_1,c_2\in\mathbb{R}$. This implies that $y'=2c_1e^{2x}-3c_2e^{-3x}$. Hence we have

$$
\begin{cases}y(0)=5\\ \\y'(0)=0\end{cases}\quad\Longleftrightarrow\quad\begin{cases}c_1+c_2=5\\ \\2c_1-3c_2=0\end{cases}\quad\Longleftrightarrow\quad\begin{cases}c_1=3\\ \\c_2=2.\end{cases}
$$

Hence, $y(x)=3e^{2x}+2e^{-3x}$ is the unique solution of the initial-value problem.
::::::

## Applications

**The pendulum**

```{figure} Images/pendulum.png
---
width: 65%
name: pendulum
align: left
---
The motion of a pendulum
```

The differential equation which represents the motion of a simple pendulum is:

$$
\frac{d^2\theta}{dt^2}+\frac{g}{L}\sin(\theta)=0,
$$

where $g$ is the acceleration due to gravity, $L$ is the length of the pendulum, and $\theta$ is
the angular displacement with respect to the equilibrium position at time $t$.

It is quite difficult to solve this differential equation.

However, the linearization of the function $f(x)=\sin(x)$ at $x=0$ is

$$
L(x)=f(0)+f'(0)(x-0)=x.
$$

This implies that $\sin(x)\approx x$ for $x$ near $0$.

Note that it is much easier to solve the differential equation

$$
\frac{d^2\theta}{dt^2}+\frac{g}{L}\theta=0
$$

instead of the one above. In fact, this is a homogeneous second-order linear differential equation with constant coefficients. The auxiliary or characteristic equation is

$$
r^2+\frac{g}{L}=0\quad\Longrightarrow\quad r=\pm i\sqrt{\frac{g}{l}}.
$$

This implies that the general solution is

$$
\theta(t)=c_1\cos(rt)+c_2\sin(rt)\quad\text{with}\quad r=\sqrt{\frac{g}{L}}\quad\text{and}\quad c_1,c_2\in\mathbb{R}.
$$

So, if (for instance) the starting position of the pundulum is $\theta_0$ and is released with no initial velocity, then this leads to the initial-value problem

$$
\theta''(t)+\frac{g}{L}\theta(t)=0,\quad\theta(0)=\theta_0,\quad\theta'(0)=0
$$

with solution $\theta(t)=\theta_0\cos(\sqrt{\frac{g}{L}}t)$.

**A mass-spring system**

```{figure} Images/mass-spring1.png
---
width: 50%
name: mass-spring
align: center
---
A mass-spring system
```

Using Newton's law $F=m\cdot a$ and Hooke's law $F=-k\cdot x$, we obtain

$$
m\cdot\frac{d^2x}{dt^2}=-k\cdot x(t),
$$

where $k$ is a positive constant, called the <em>spring constant</em>.

Without damping we have: $mx''(t)+kx(t)=0$.

```{figure} Images/mass-spring2.png
---
width: 50%
name: mass-spring
align: center
---
A mass-spring system
```

::::::{prf:example}
A spring with a mass of $5\;\text{kg}$ has natural length $0.5\;\text{m}$. A force of $45\;\text{N}$ is required to maintain it stretched to a length of $0.75\;\text{m}$. If the spring is stretched to a length of $0.75\;\text{m}$ and then released with initial velocity $0$, find the position of the mass at any time $t$.
::::::

::::::{admonition} Solution
From Hooke's law, the force required to stretch the spring is $k\cdot(0.25)=45$, so $k=\dfrac{45}{0.25}=180$. Using this value of the spring constant $k$, together with $m=5$ we have

$$
5\frac{d^2x}{dt^2}+180x(t)=0.
$$

The general solution is $x(t)=c_1\cos(6t)+c_2\sin(6t)$ which implies that $x'(t)=-6c_1\sin(6t)+6c_2\cos(6t)$. The initial conditions are $x(0)=0.25$ and $x'(0)=0$, which lead to $c_1=0.25$ and $c_2=0$. So, the solution is $x(t)=0.25\cos(6t)$.
::::::

```{figure} Images/mass-spring3.png
---
width: 50%
name: mass-spring
align: right
---
A mass-spring system
```

<br /><br />

With damping we have: $mx''(t)+cx'(t)+kx(t)=0$. 

Here $c$ is a positive constant, called the <em>damping constant</em>.

::::::{prf:example}
Suppose that the same spring with a mass of $5\;\text{kg}$ as above is immersed in a fluid with damping constant $c=65$. Find the position of the mass at any time $t$ if it starts from the equilibrium position and is given a push to start it with an initial velocity of $0.5\;\text{m}/\text{s}$.
::::::

::::::{admonition} Solution
With $m=5$ and $k=180$ the differential equation becomes

$$
5\frac{d^2x}{dt^2}+65\frac{dx}{dt}+180x(t)=0\quad\Longleftrightarrow\quad\frac{d^2x}{dt^2}+13\frac{dx}{dt}+36x(t)=0.
$$

The characteristic or auxillary equation is $r^2+13r+36=0\;\Longleftrightarrow\;(r+4)(r+9)=0$ with roots $r=-4$ and $r=-9$. So, the general solution is $x(t)=c_1e^{-4t}+c_2e^{-9t}$ which implies that $x'(t)=-4c_1e^{-4t}-9c_2e^{-9t}$. The initial conditions are $x(0)=0$ and $x'(0)=0.5$, which lead to $c_1=0.1$ and $c_2=-0.1$. So, the solution is $x(t)=0.1\left(e^{-4t}-e^{9t}\right)$.
::::::

::::::{prf:example}
Consider the integral $I(t)=\displaystyle\int_0^{\infty}\frac{\cos(xt)}{x^2+\alpha^2}\,dx$ with $\alpha>0$. 

Then we have: $I(0)=\displaystyle\int_0^{\infty}\frac{dx}{x^2+\alpha^2}=\frac{1}{\alpha}\arctan\left(\frac{x}{\alpha}\right)\bigg|_0^{\infty}=\frac{\pi}{2\alpha}$ and

$$
\begin{align*}
I'(t)&=-\int_0^{\infty}\frac{x\sin(xt)}{x^2+\alpha^2}\,dx=-\int_0^{\infty}\frac{(x^2+\alpha^2-\alpha^2)\sin(xt)}{x(x^2+\alpha^2)}\,dx\\
&=-\int_0^{\infty}\frac{\sin(xt)}{x}\,dx+\alpha^2\int_0^{\infty}\frac{\sin(xt)}{x(x^2+\alpha^2)}\,dx.
\end{align*}
$$

Using the substitution $xt=u$ we obtain for $t>0$ that $\displaystyle\int_0^{\infty}\frac{\sin(xt)}{x}\,dx=\int_0^{\infty}\frac{\sin(u)}{u}\,du=\frac{1}{2}\pi$ (see: the Dirichlet integral). Hence

$$
I'(t)=-\frac{1}{2}\pi+\alpha^2\int_0^{\infty}\frac{\sin(xt)}{x(x^2+\alpha^2)}\,dx.
$$

Now we have: $I'(0)=-\dfrac{1}{2}\pi$ and $I''(t)=\alpha^2\displaystyle\int_0^{\infty}\frac{\cos(xt)}{x^2+\alpha^2}\,dx=\alpha^2I(t)$.

Hence: $I(t)=c_1e^{\alpha t}+c_2e^{-\alpha t}$ and $I'(t)=\alpha c_1e^{\alpha t}-\alpha c_2e^{-\alpha t}$ with $I(0)=\dfrac{\pi}{2\alpha}$ and $I'(0)=-\dfrac{1}{2}\pi$.

This implies: $c_1+c_2=\dfrac{\pi}{2\alpha}$ and $c_1-c_2=-\dfrac{\pi}{2\alpha}$. Hence: $c_1=0$ and $c_2=\dfrac{\pi}{2\alpha}$.

Conclusion: $I(t)=\dfrac{\pi}{2\alpha}e^{-\alpha t}$ for $\alpha>0$ and $t>0$.
::::::

## (Grasple) exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/00da73f8-266e-4fdf-aa13-09c66804d8d3?id=76568
:label: grasple_exercise_13_1_1
:dropdown:
:description: Find the general solution.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/96b7c05c-56c7-4a02-875f-e4ce8668dfad?id=76567
:label: grasple_exercise_13_1_2
:dropdown:
:description: Find the general solution.
::::::