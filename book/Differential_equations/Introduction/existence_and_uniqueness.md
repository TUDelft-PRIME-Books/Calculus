(Sec:DE:ExistenceUniqueness)=

# Existence and uniqueness of solutions

In this section we discuss under which conditions a differential equation has a solution, and whether this solution is unique.

- Domain of a DE
- E&E for linear any-order DEs
- E&E for nonlinear first-order DEs (Picard-Lindelöf theorem)
- E&E for IVPs & BVPs
- Navier-Stokes existence and uniqueness problem (mention as open problem)

::::::{prf:theorem} 
:label: Thm:DE:ExistenceUniquenessODE1Linear
If the functions $p$ and $g$ are continuous on an open interval $I=(a,b)$ containing the point $t_0$, then there exists a unique function $y=f(t)$ that satisfies the differential equation

$$
y'+p(t)y=g(t)
$$

for each $t$ in $I$, and that also satisfies the initial condition

$$
y(t_0)=y_0,
$$

where $y_0$ is an arbitrary prescribed initial value.
::::::

::::::{prf:theorem} 
:label: Thm:DE:ExistenceUniquenessODE1Nonlinear
Let the functions $y$ and $\partial f/\partial y$ be continuous in some rectangle $\alpha<t<\beta$ and $\gamma<y<\delta$ containing the point $(t_0,y_0)$. Then, in some interval $(t_0-h,t_0+h)$ contained in $(\alpha,\beta)$ there exists a unique solution $y=f(t)$ of the initial-value problem

$$
y'=f(t,y),\quad y(t_0)=y_0.
$$

::::::

::::::{prf:theorem} 
:label: Thm:DE:ExistenceUniquenessODE2Linear
Consider the initial-value problem

$$
y''+p(t)y'+q(t)y=g(t),\quad y(t_0)=y_0,\quad y'(t_0)=y_0',
$$

where $p$, $q$ and $g$ are continuous functions on an open interval $I$ that contains the point $t_0$. This problem has exactly one solution $y=f(t)$, and the solution exists throughout the interval $I$.
::::::
