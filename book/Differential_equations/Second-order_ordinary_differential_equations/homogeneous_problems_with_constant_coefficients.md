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

(SubSec:ODE2:Intro)=

## Introduction

We consider a homogeneous first-order linear differential equation with constant coefficients, which is of the form

$$
 ay'+by=0,
$$

where $a\neq 0$ and $b$ are constants. This equation is both separable and linear, so we could use the techniques from {numref}`Sec:ODE1:Separable` or {numref}`Sec:ODE1:Linear` to solve it. However, we can also try to guess what the solution looks like. Indeed, we can rewrite the differential equation into

$$
 y'=-\frac{b}{a}y,
$$

[^FootnoteEx]: We used a similar approach in {prf:ref}`Ex:ClassDiff:Ansatz`. In fact, that example is of the same form as the one we are considering here.

so we are looking for a function of which the derivative is a multiple of the original function. Exponential functions have this property, so we can make the educated guess that a solution is of the form $y(t)=e^{rt}$. Such an educated guess about the shape of a solution is called an **Ansatz**.[^FootnoteEx] Plugging this exponential into the differential equation gives

$$
 re^{rt}=-\frac{b}{a}e^{rt}.
$$

We can divide by $e^{rt}$ and obtain the equation

$$
 r=-\frac{b}{a}.
$$

This means that the function $y(t)=e^{-\frac{b}{a}t}$ is a solution of the differential equation. By {prf:ref}`Thm:DE:GeneralSolutionHomogeneous`, the general solution is given by

$$
y=Ce^{-\frac{b}{a}t}.
$$



The two reasons why the educated guess $y=e^{rt}$ worked is that the equation is homogeneous and that the coefficients $a$ and $b$ are constants. Indeed, whenever the equation would have been of the form

$$
 a(t)y'(t)+b(t)y(t)=c(t)
$$

with either $c(t)\neq 0$, or with $a(t)$ and/or $b(t)$ not constant, it is very unlikely that we could find a solution of the form $y(t)=e^{rt}$. 

In this section we lift this idea to second-order, linear, homogeneous differential equations with *constant coefficients*, i.e. differential equations of the form

$$
 ay''+by'+cy=0,
$$

where $a\neq 0$, $b$ and $c$ are constants. We will see that we can always find at least one (possibly complex) solution of the form $y(t)=e^{rt}$. The correct values of $r$ can be found by finding the roots of a quadratic equation in $r$. The structure of the solution will be different, depending on whether this quadratic equation has two real roots, a single real root or two complex roots, so we will treat these cases separately.

## Solving second-order, linear, homogenous differential equations

We consider the second-order, linear, homogeneous differential equation with *constant coefficients*

$$
 ay''+by'+cy=0,
$$

where $a\neq 0$, $b$ and $c$ are constants. This means that we are looking function $y$ of which a specific linear combination of $y$, $y'$ and $y''$ is $0$. Inspired by the approach from {numref}`SubSec:ODE2:Intro`, we make the educated guess that $y=e^{rt}$ might be a solution for some constant $r$. Then we compute $y'=re^{rt}$ and $y''=r^2e^{rt}$. Plugging these into the differential equation leads to

$$
 ar^2e^{rt}+bre^{rt}+ce^{rt}=0.
$$

We can factor out the exponential to obtain

$$
 e^{rt}(ar^2+br+c)=0.
$$

Since $e^{rt}\neq0$ this leads to the quadratic equation 

$$
 ar^2+br+c=0.
$$

::::::{prf:definition}
:label: Def:ODE2:Chareq
Consider the second-order, linear, homogeneous differential equation with *constant coefficients*

$$
 ay''+by'+cy=0,
$$

where $a\neq 0$, $b$ and $c$ are constants. Then the quadratic equation 

$$
 ar^2+br+c=0
$$

is known as the **characteristic equation** or the **auxiliary equation** for this differential equation.
::::::

Now we consider three possibilities for the **discriminant** $D=b^2-4ac$: $D>0$, $D=0$ and $D<0$.

### Two real roots

If $D>0$ the characteristic equation has two different real solutions, say $r_1$ and $r_2$. Then the functions $y_1(t)=e^{r_1t}$ and $y_2(t)=e^{r_2t}$ are both solutions. Since these functions are linearly independent, we find that the general solution is $y(t)=c_1e^{r_1t}+c_2e^{r_2t}$ with $c_1,c_2\in\mathbb{R}$.

::::::{prf:theorem}
:label: Thm:ODE2:Tworeal
Consider the second-order, linear, homogeneous differential equation with *constant coefficients*

$$
 ay''+by'+cy=0,
$$

where $a\neq 0$, $b$ and $c$ are constants. If the characteristic equation has two distinct real roots $r_1$ and $r_2$, the general solution is given by

$$
 y(t)=c_1e^{r_1t}+c_2e^{r_2t}.
$$
::::::

:::{admonition} Proof of {prf:ref}`Thm:ODE2:Tworeal`
:class: tudproof, dropdown
The functions $y_1(t)=e^{r_1t}$ and $y_2(t)=e^{r_2t}$ are solutions by construction. We need to check that they are linearly independent. Consider $c_1$ and $c_2$ with

$$
 c_1e^{r_1t}+c_2e^{r_2t}=0
$$

for all $t$. For $t=0$, we obtain $c_1+c_2=0$, which gives $c_1=-c_2$. For $t=1$ we obtain $c_1e^{r_1}+c_2e^{r_2}=0$, which becomes $c_1\left(e^{r_1}-e^{r_2}\right)=0$. Since $r_1\neq r_2$ we have $e^{r_1}-e^{r_2}\neq 0$, so we must have $c_1=0$. This gives $c_2=0$ as well. So the functions $y_1$ and $y_2$ are linearly independent. So we have found two linearly independent solutions of a second-order, linear, homogeneous differential equation. By {prf:ref}`Thm:DE:GeneralSolutionHomogeneous` the general solution of this differential equation is given by

$$
 y(t)=c_1e^{r_1t}+c_2e^{r_2t}.
$$

:::

::::::{prf:example}
The differential equation 

$$
 y''-y'-6y=0
$$

has the characteristic equation 

$$
 r^2-r-6=0,
$$

which can be rewritten as 

$$
 (r-3)(r+2)=0.
$$

The roots of this equation are $r_1=3$ and $r_2=-2$. By {prf:ref}`Thm:ODE2:Tworeal`, the general solution of the differential equation is 

$$
 y=c_1e^{3x}+c_2e^{-2x}
$$

with $c_1,c_2\in\mathbb{R}$.
::::::

### Double real root


If $D=0$ the characteristic equation has two equal real solutions $r_1=r_2=r$. So we only obtain one linear independent solution $y_1=e^{rt}$ in that case. So how do we obtain a second, linearly independent solution? It turns out that $y_2=te^{rt}$ is a solution too, as can be seen in the upcoming theorem. Since these two functions are linearly independent, we can use them to find the general solution.

::::::{prf:theorem}
:label: Thm:ODE2:Onereal
Consider the second-order, linear, homogeneous differential equation with *constant coefficients*

$$
 ay''+by'+cy=0,
$$

where $a\neq 0$, $b$ and $c$ are constants. If the characteristic equation has a double (real) root $r$, the general solution is given by

$$
 y(t)=c_1e^{rt}+c_2te^{rt}.
$$
::::::

:::{admonition} Proof of {prf:ref}`Thm:ODE2:Onereal`
:class: tudproof, dropdown
The function $y_1(t)=e^{rt}$ is a solution by construction. We need to check that $y_2(t)=te^{rt}$ is a solution as well. In order to see this, we note that $r$ being a double root means that the discriminant $D=b^2-4ac=0$. Then, we can express $r$ in terms of the coefficients $a$, $b$, and $c$ as

$$
 r=\frac{-b\pm\sqrt{D}}{2a}=\frac{-b}{2a}.
$$

This means that $2ar+b=0$. Moreover, $r$ is a solution of the characteristic equation, so we must have $ar^2+br+c=0$. Then, for $y_2(t)=te^{rt}$ we can compute $y_2'=(rt+1)e^{rt}$ and $y_2''=(r^2t+2r)e^{rt}$. Plugging these into the differential equation gives

$$
\begin{align*}
ay''+by'+cy&=a(r^2t+2r)e^{rt}+b(rt+1)e^{rt}+cte^{rt}\\
&=(ar^2+br+1)te^{rt}+(2ar+b)e^{rt}\\
&=0+0=0.
\end{align*}
$$

So $y_2$ is indeed a solution of the differential equation. 

Finally, we need to show that $y_1$ and $y_2$  are linearly independent. Consider $c_1$ and $c_2$ with

$$
 c_1e^{rt}+c_2te^{rt}=0
$$

for all $t$. For $t=0$, we directly obtain $c_1=0$. For $t=1$ we then obtain $c_2e^{r}=0$, which gives $c_2=0$. Therefore, the functions $y_1$ and $y_2$ are linearly independent. So we have found two linearly independent solutions of a second-order, linear, homogeneous differential equation. By {prf:ref}`Thm:DE:GeneralSolutionHomogeneous` the general solution of this differential equation is given by

$$
 y(t)=c_1e^{rt}+c_2te^{rt}.
$$

:::




::::::{prf:example}
:label: Def:ODE2:Onereal
The differential equation 

$$
 y''-6y'+9y=0
$$ 

has the characteristic equation 

$$
 r^2-6r+9=0,
$$

which can be written to

$$
 (r-3)^2=0.
$$ 

As such, we have a double root $r=3$. By {prf:ref}`Thm:ODE2:Onereal` the general solution is 

$$
 y=c_1e^{3t}+c_2te^{3t}
$$

with $c_1,c_2\in\mathbb{R}$.
::::::

### Complex roots

If $D<0$ the characteristic equation has a complex conjugate pair as solutions, say $r=\alpha\pm i\beta$ with $\beta\neq0$. This implies that the general (complex) solution is a (complex) linear combination of

$$
e^{(\alpha+i\beta)t}=e^{\alpha t}\cdot e^{i\beta t}=e^{\alpha t}(\cos(\beta t)+i\sin(\beta t))
$$

and

$$
e^{(\alpha-i\beta)t}=e^{\alpha t}\cdot e^{-i\beta t}=e^{\alpha t}(\cos(\beta t)-i\sin(\beta t)).
$$

As can be seen in the proof of the upcoming {prf:ref}`Thm:ODE2:Twocomplex`, it is possible to take certain (complex) linear combinations of these two complex exponentials to obtain the (real-valued!) functions

$$
 y_1(t)=e^{\alpha t}\cos(\beta t)
$$ 

and 

$$
 y_2(t)=e^{\alpha t}\sin(\beta t).
$$

Since linear combinations (even complex ones) of linear, homogeneous equations are again solutions, the functions $y_1$ and $y_2$ are solultions of the differential equation. These solutions are real and linearly independent. This implies that the general solution is 

$$
 y=c_1e^{\alpha t}\cos(\beta t)+c_2e^{\alpha t}\sin(\beta t)
$$

with $c_1,c_2\in\mathbb{R}$ in this case.

::::::{prf:theorem}
:label: Thm:ODE2:Twocomplex
Consider the second-order, linear, homogeneous differential equation with *constant coefficients*

$$
 ay''+by'+cy=0,
$$

where $a\neq 0$, $b$ and $c$ are constants. If the characteristic equation has a a conjugate pair of complex roots $r=\alpha+i\beta$ and $r=\alpha-i\beta$ with $\beta\neq 0$, the general solution is given by

$$
 y(t)=c_1e^{\alpha t}\cos(\beta t)+c_2e^{\alpha t}\sin(\beta t).
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:ODE2:Twocomplex`
:class: tudproof, dropdown 
The functions $\tilde{y}_1(t)=e^{(\alpha+i\beta)t}$ and $\tilde{y}_2(t)=e^{(\alpha-i\beta)t}$ are complex solutions of the differential equation by construction. By {prf:ref}`Thm:DE:SuperpositionPrinciple`, the functions

\begin{align*}
 y_1(t)=&\frac{1}{2}\left(\tilde{y}_1(t)+\tilde{y}_2(t)\right)\\
 =&\frac{1}{2}\left(e^{\alpha t}(\cos(\beta t)+i\sin(\beta t))+e^{\alpha t}(\cos(-\beta t)+i\sin(-\beta t))\right)\\
 =&e^{\alpha t}\cos(\beta t)
\end{align*}

and

\begin{align*}
 y_2(t)=&\frac{1}{2i}\left(\tilde{y}_1(t)-\tilde{y}_2(t)\right)\\
 =&\frac{1}{2i}\left(e^{\alpha t}(\cos(\beta t)+i\sin(\beta t))-e^{\alpha t}(\cos(-\beta t)-i\sin(-\beta t))\right)\\
 =&e^{\alpha t}\sin(\beta t)
\end{align*}

are solutions of this differential equation as well. We see that these solutions are both real.

Finally, we need to show that $y_1$ and $y_2$  are linearly independent. Consider $c_1$ and $c_2$ with

$$
 c_1e^{\alpha t}\cos(\beta t)+c_2e^{\alpha t}\sin(\beta t)=0
$$

for all $t$. For $t=0$, we directly obtain $c_1=0$. For $t=\dfrac{\pi}{2\beta}$ we then obtain 

$$
 c_2e^{\frac{\pi\alpha}{2\beta}}\sin\left(\frac{\pi}{2}\right)=0,
$$

which gives $c_2=0$. Therefore, the functions $y_1$ and $y_2$ are linearly independent. So we have found two linearly independent solutions of a second-order, linear, homogeneous differential equation. By {prf:ref}`Thm:DE:GeneralSolutionHomogeneous` the general solution of this differential equation is given by

$$
 y(t)=c_1e^{\alpha t}\cos(\beta t)+c_2e^{\alpha t}\sin(\beta t).
$$

:::

::::::{prf:example}
:label: Ex:ODE2:Twocomplex
The differential equation 

$$
 y''+4y'+13y=0
$$

has characteristic equation 

$$
 r^2+4r+13=0.
$$

This equation can be solved by completing this square, which gives

$$
 (r+2)^2+9=0.
$$

From this, we obtain the nonreal roots $r=-2\pm3i$. By {prf:ref}`Thm:ODE2:Twocomplex`, the general solution is 

$$
 y=c_1e^{-2t}\cos(3t)+c_2e^{-2t}\sin(t)
$$

with $c_1,c_2\in\mathbb{R}$.
::::::

### Initial-value problems

In {numref}`Sec:DE:ExistenceUniqueness` we have seen that an initial-value problem of the form

$$
\begin{cases}ay''+by'+cy=0,\\ \\y(t_0)=y_0,\quad y'(t_0)=y_0'\end{cases}
$$

has a unique solution. Here $a\neq 0$, $b$ and $c$ are constants. In the next example, we will show how to find this specific solution from the general solution.

::::::{prf:example}
:label: Ex:ODE2:IVP
Suppose we want to find the unique solution of the initial-value problem 

$$
 \begin{cases}y''+y'-6y=0\\ \\y(0)=5,\quad y'(0)=0.\end{cases}
$$

Note that the differential equation

$$
 y''+y'-6y=0
$$

has characteristic equation 

$$
 r^2+r-6=0.
$$

We can rewrite this equation into 

$$
 (r+3)(r-2)=0
$$ 

which gives the roots $r_1=2$ and $r_2=-3$. Since we have two distinct real roots, the general solution is

$$
 y=c_1e^{2t}+c_2e^{-3t}
$$

with $c_1,c_2\in\mathbb{R}$. 

In order to take the initial condition into account, we first evaluate

$$
 y'=2c_1e^{2t}-3c_2e^{-3t}.
$$

The initial values

$$
 \begin{cases}y(0)=5,\\ \\y'(0)=0\end{cases}
$$

give the system of linear equation

$$
\begin{cases}c_1+c_2=5,\\ \\2c_1-3c_2=0.\end{cases}
$$

We can solve this system to obtain

$$
 \begin{cases}c_1=3,\\ \\c_2=2.\end{cases}
$$

Hence, $y(t)=3e^{2t}+2e^{-3t}$ is the unique solution of the initial-value problem.
::::::

### Boundary value problems

On the other hand, boundary-value problems do not always have a unique solution, as can be seen from the following example.

::::::{prf:example}
:label: Ex:ODE2:BVP
Suppose we want to find all solutions of the boundary-value problem 

$$
 \begin{cases}y''+4y=0\\ \\y(0)=1,\quad y(\pi)=-1.\end{cases}
$$

Note that the differential equation

$$
 y''+4y=0
$$

has characteristic equation 

$$
 r^2+4=0.
$$

This gives the roots $r_1=2i$ and $r_2=-2i$. Since we have complex roots, the general solution is

$$
 y=c_1\cos(2t)+c_2\sin(2t).
$$

with $c_1,c_2\in\mathbb{R}$. 

The boundary values

$$
 \begin{cases}y(0)=1,\\ \\y(\pi)=-1\end{cases}
$$

give the system of linear equation

$$
\begin{cases}c_1=1,\\ c_1=-1.\end{cases}
$$

Clearly, $c_1$ cannot be two different values at the same time. We conclude that the boundary-value problem has no solutions.
::::::

### Higher-order equations

The techniques from this section can also be applied to higher-order, linear, homogeneous equations of the form

$$
 a_ny^{(n)}(t)+a_{n-1}y^{(n-1)}(t)+...+a_1y'(t)+a_0y(t)=0,
$$

where $a_0,...,a_n$ are constants with $a_n\neq 0$. For such an equation, the educated guess $y(t)=e^{rt}$ gives an $n$th order polynomial equation. Solving these equations by hand is hard (or even impossible), but in some cases it is doable, as can be seen in the following example.

::::::{prf:example}
Consider the differential equation

$$
 y^{(5)}-6y^{(4)}+15y^{(3)}-20y''+14y'-4y=0.
$$

Since this is a linear, homogeneous equation with constant coefficients, we try a solution of the form $y=e^{rt}$. Plugging this into the differential equation gives

$$
 r^5e^{rt}-6r^4e^{rt}+15r^3e^{rt}-20r^2e^{rt}+14re^{rt}-4e^{rt}=0.
$$

Upon dividing by $e^{rt}$ we obtain

$$
 r^5-6r^4+15r^3-20r^2+14r-4=0.
$$

[It can be shown that there is no general method to find roots of a fifth order polynomial equation](https://en.wikipedia.org/wiki/Abel%E2%80%93Ruffini_theorem). Fortunately, we made this example ourselves so we constructed it in such a way that we know the roots. These are $r_1=1$ (with multiplicity $2$), $r_2=2$, $r_3=1+i$ and $r=1-i$. Following the same ideas as earlier in this section, we obtain the $5$ real solutions

$$
 y_1(t)=e^t, \quad y_2(t)=te^t,\quad y_3(t)=e^{2t},\quad y_4(t)=e^t\cos(t),\quad y_5(t)=e^t\sin(t).
$$

Since these solutions are linearly independent, we obtain the general solution

$$
 y(t)=c_1e^t+c_2te^t+c_3e^{2t}+c_4e^t\cos(t)+c_5e^t\sin(t),
$$

where $c_1,c_2,c_3,c_4$ and $c_5$ are real constants.
::::::

## Applications

### The pendulum

```{figure} Images/pendulum.png
---
width: 65%
name: pendulum
align: left
---
The motion of a pendulum
```

The differential equation which represents the motion of a simple pendulum is

$$
\frac{d^2\theta}{dt^2}+\frac{g}{L}\sin(\theta)=0,
$$

where $g$ is the acceleration due to gravity, $L$ is the length of the pendulum, and $\theta$ is
the angular displacement with respect to the equilibrium position at time $t$.

It is quite difficult to solve this differential equation analytically. Instead, we note that the linearization of the function $f(x)=\sin(x)$ at $x=0$ is

$$
L(x)=f(0)+f'(0)(x-0)=x.
$$

This implies that $\sin(x)\approx x$ for $x$ near $0$. It is much easier to solve the differential equation

$$
\frac{d^2\theta}{dt^2}+\frac{g}{L}\theta=0
$$

instead of the one above. In fact, this is a homogeneous second-order linear differential equation with constant coefficients. The characteristic equation is

$$
r^2+\frac{g}{L}=0, 
$$

from which we obtain

$$
 r=\pm i\sqrt{\frac{g}{l}}.
$$ 

From {prf:ref}`Thm:ODE2:Twocomplex` we obtain that the general solution is

$$
\theta(t)=c_1\cos(rt)+c_2\sin(rt)\quad\text{with}\quad r=\sqrt{\frac{g}{L}}\quad\text{and}\quad c_1,c_2\in\mathbb{R}.
$$

So, if (for instance) the starting position of the pundulum is $\theta_0$ and is released with no initial velocity, then this leads to the initial-value problem

$$
\theta''(t)+\frac{g}{L}\theta(t)=0,\quad\theta(0)=\theta_0,\quad\theta'(0)=0
$$

with solution 

$$
 \theta(t)=\theta_0\cos(\sqrt{\frac{g}{L}}t).
$$

Of course, we made an approximation of the original nonlinear differential equation, so this function will **not** be a solution of the original equation. Still, for small values of $\theta$, it is a good approximation of the real solution.

### A mass-spring system

```{figure} Images/mass-spring1.png
---
width: 50%
name: mass-spring
align: center
---
A mass-spring system
```

In {prf:ref}`Ex:Diffclass:massspring` we studied the mass-spring system. For this system, we aim to find the displacement with respect to equilibrium, which we denote by $x(t)$. Using Newton's law $F=m\cdot a$ and Hooke's law $F=-k\cdot x$ and assuming there is no damping, we obtain

$$
m\cdot\frac{d^2x}{dt^2}=-k\cdot x(t).
$$

Here $k$ is a positive constant, called the <em>spring constant</em>.



```{figure} Images/mass-spring2.png
---
width: 50%
name: mass-spring
align: center
---
A mass-spring system
```

::::::{prf:example}
:label: Ex:ODE2:SpringNodamp
A spring with a mass of $5\;\text{kg}$ has natural length $0.5\;\text{m}$. A force of $45\;\text{N}$ is required to maintain it stretched to a length of $0.75\;\text{m}$. Suppose the spring is stretched to a length of $0.75\;\text{m}$ and then released with initial velocity $0$. Let us see how we can find the position of the mass at any time $t$.

From Hooke's law, the force required to stretch the spring is $k\cdot(0.25)=45$, so $k=\dfrac{45}{0.25}=180$. Using this value of the spring constant $k$, together with $m=5$ we have

$$
5\frac{d^2x}{dt^2}+180x(t)=0.
$$

This is a second-order, linear, homogemenous equation with constant coefficients, so we try $x=e^{rt}$. This gives the characteristic equation

$$
 5r^2+180=0
$$

with solutions $r=6i$ and $r=-6i$. By {prf:ref}`Thm:ODE2:Twocomplex`, the general solution is 


$$
 x(t)=c_1\cos(6t)+c_2\sin(6t).
$$

In order to handle the initial condition, we compute

$$
 x'(t)=-6c_1\sin(6t)+6c_2\cos(6t).
$$

The initial conditions are $x(0)=0.25$ and $x'(0)=0$, which lead to $c_1=0.25$ and $c_2=0$. So, the solution is $x(t)=0.25\cos(6t)$.
::::::

```{figure} Images/mass-spring3.png
---
width: 25%
name: mass-spring
align: right
---
A damped mass-spring system
```

<br /><br />

With damping we have the equation 

$$
 mx''(t)+cx'(t)+kx(t)=0,
$$ 

where $c$ is a positive constant, called the <em>damping constant</em>.



::::::{prf:example}
:label: Ex:ODE2:SpringWithdamp
Suppose that the spring with a mass of $5\;\text{kg}$ from {prf:ref}`Ex:ODE2:SpringNodamp` is immersed in a fluid with damping constant $c=65$. How can we find the position of the mass at any time $t$ if it starts from the equilibrium position and is given a push to start it with an initial velocity of $0.5\;\text{m}/\text{s}$?

With $m=5$ and $k=180$ the differential equation becomes

$$
5\frac{d^2x}{dt^2}+65\frac{dx}{dt}+180x(t)=0,
$$

which we can rewrite into

$$
 \frac{d^2x}{dt^2}+13\frac{dx}{dt}+36x(t)=0.
$$

The characteristic equation is 

$$
 r^2+13r+36=0$$

which gives

$$
 (r+4)(r+9)=0.
$$ 

We obtain the roots $r=-4$ and $r=-9$. By {prf:ref}`Thm:ODE2:Tworeal`, the general solution is 

$$
 x(t)=c_1e^{-4t}+c_2e^{-9t}.
$$

In order to handle the initial conditions, we evaluate 

$$
 x'(t)=-4c_1e^{-4t}-9c_2e^{-9t}.
$$

The initial conditions are $x(0)=0$ and $x'(0)=0.5$, which lead to $c_1=0.1$ and $c_2=-0.1$. So, the solution is $x(t)=0.1\left(e^{-4t}-e^{9t}\right)$.
::::::

For the damped mass-spring system, the qualitative behaviour of the solutions depends greatly on the value of the damping constant. Indeed, let us consider a system with $m=1$, $k=25$ and let us see how different values of the damping constant influence the shape of the solution. 

For a large value of $c$, say $c=26$, we obtain the differential equation

$$
 x''+26x'+25x=0
$$

with characteristic equation

$$
 r^2+26r+25=0.
$$

In this case, we obtain two distinct real roots $r_1=-1$ and $r_2=-25$. The general solution becomes

$$
 x(t)=c_1e^{-t}+c_2e^{-25t}.
$$

In this case, the spring does not oscillate and goes back to equilibrium relatively slowly (because of the $e^{-t}$), at least compared to final one of the upcoming cases. Physically, this makes sense: if you put your spring in a material with a high damping coefficient (say, something like honey), it will go back to equilibrium slowly and not oscillate. This case where we have two real roots is, for this reason, known as the **overdamped** case.

Secondly, we consider a small value of $c$, say $c=6$. Then, we obtain the differential equation

$$
 x''+6x'+25x=0
$$

with characteristic equation

$$
 r^2+6r+25=0.
$$

In this case, we obtain two complex roots $r_1=-3+4i$ and $r_2=-3-4i$. The general solution becomes

$$
 x(t)=c_1e^{-3t}\cos(4t)+c_2e^{-3t}\sin(4t).
$$

Because of the cosine and the sine, the solution with keep on oscillating, with decreasing amplitude because of the exponential. Again, this behaviour matches our physical intuition: if the damping coefficient of the medium is low (say, something like air), we expect the solution to keep on oscillating. This case where we have two complex reasons is, as such, known as the **underdamped** case.

Finally, we consider the critical value of the damping constant when we move betwen the overdamped and the overdamped case. Mathematically, this corresponds to the case where we have a double real root. For this system, this happens when $c=10$. Indeed, in that case we have the differential equation

$$
 x''+10x'+25x=0
$$

with characteristic equation

$$
 r^2+10r+25=0.
$$

In this case, we obtain double root $r=5$. The general solution becomes

$$
 x(t)=c_1e^{-5t}+c_2te^{-5t}.
$$

Note that this solution dampes out quicker than both the overdamped case and the underdamped case. Indeed, for the overdamped case the dominant term is $e^{-t}$, for the underdamped case it is $e^{-3t}$, while here it is $te^{-5t}$. For at least some initial conditions, (for instance, when $x(0)=1$ and $x'(0)=-10$) the solution passes through the equilibrium position excatly once, but there is no oscillation involved. Since this case is the transition case between the other cases, it is known as the **critically damped** case.

:::{figure} Images/Fig-ODE2-damping.png
:name: Fig:ODE2:Damping
:class: dark-light

A plot of the solution with $x(0)=1$, $x'(0)=-10$ for the I) overdamped case; II) critically damped case; III) underdamped case.
:::

:::{todo}
Replace {numref}`Fig:ODE2:Damping` with an applet.
:::

### A complicated family of integrals



::::::{prf:example}
For each $t\in\mathbb{R}$, we consider the integral 

$$
 I(t)=\displaystyle\int_0^{\infty}\frac{\cos(xt)}{x^2+\alpha^2}\,dx
$$ 

with $\alpha>0$. It is very hard to solve this integral by hand, but we will show that it satisfies a second-order differential equation.

For at least one value of $t$ it is doable to evaluate this integral by hand, since we have

$$
 I(0)=\displaystyle\int_0^{\infty}\frac{dx}{x^2+\alpha^2}=\frac{1}{\alpha}\arctan\left(\frac{x}{\alpha}\right)\bigg|_0^{\infty}=\frac{\pi}{2\alpha}.
$$

Moreover, since we integrate over $x$ we can differentiate the integral with respect to $t$ and bring this derivative inside to obtain


\begin{align*}
I'(t)&=\frac{d}{dt}\int_0^{\infty}\frac{\cos(xt)}{x^2+\alpha^2}\,dx\\
&=\int_0^{\infty}\frac{d}{dt}\frac{\cos(xt)}{x^2+\alpha^2}\,dx\\
&=-\int_0^{\infty}\frac{x\sin(xt)}{x^2+\alpha^2}\,dx.
\end{align*}


Now we rewrite this integral to obtain

\begin{align*}
I'(t)&=-\int_0^{\infty}\frac{x\sin(xt)}{x^2+\alpha^2}\,dx\\
&=-\int_0^{\infty}\frac{(x^2+\alpha^2-\alpha^2)\sin(xt)}{x(x^2+\alpha^2)}\,dx\\
&=-\int_0^{\infty}\frac{\sin(xt)}{x}\,dx+\alpha^2\int_0^{\infty}\frac{\sin(xt)}{x(x^2+\alpha^2)}\,dx.
\end{align*}

Using the substitution $xt=u$ we can use {prf:ref}`Thm:Integration:ImproperIntegralsDirichletIntegral` to obtain for $t>0$ that 

$$
 \displaystyle\int_0^{\infty}\frac{\sin(xt)}{x}\,dx=\int_0^{\infty}\frac{\sin(u)}{u}\,du=\frac{1}{2}\pi.
$$ 

Hence, we find that

$$
I'(t)=-\frac{1}{2}\pi+\alpha^2\int_0^{\infty}\frac{\sin(xt)}{x(x^2+\alpha^2)}\,dx.
$$

Using this expression we immediately see that $I'(0)=-\dfrac{1}{2}\pi$ and using the same procedure as before we can use this to obtain

$$
 I''(t)=\alpha^2\displaystyle\int_0^{\infty}\frac{\cos(xt)}{x^2+\alpha^2}\,dx=\alpha^2I(t).
$$

This means that $I(t)$ satisfies a second-order, linear, homogeneous differential equation. The characteristic equation is given by

$$
 r^2-\alpha^2=0,
$$

with roots $r_1=\alpha$ and $r_2=-\alpha$. We then obtain using {prf:ref}`Thm:ODE2:Tworeal` that the general solution is given by

$$
 I(t)=c_1e^{\alpha t}+c_2e^{-\alpha t}.
$$

In order to handle the initial conditions, we first evaluate 

$$
 I'(t)=\alpha c_1e^{\alpha t}-\alpha c_2e^{-\alpha t}.
$$

The initial conditions are $I(0)=\dfrac{\pi}{2\alpha}$ and $I'(0)=-\dfrac{1}{2}\pi$. From this we obtain the system of linear equations

$$
 \begin{cases}c_1+c_2=\dfrac{\pi}{2\alpha}\\ c_1-c_2=-\dfrac{\pi}{2\alpha}.\end{cases}
$$

Solving this system gives $c_1=0$ and $c_2=\dfrac{\pi}{2\alpha}$. We conclude that

$$
 I(t)=\dfrac{\pi}{2\alpha}e^{-\alpha t}.
$$
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