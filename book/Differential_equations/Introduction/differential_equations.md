# Differential equations

In this section we cover:

- Introduction by means of examples
- Definitions of differential equation, initial-value problems and boundary-value problems:
  - Mention names of problems
  - Mention names of boundary conditions
- (in)dependent variable
- Classification of differential equations:
  - linear/nonlinear
  - homogeneous/nonhomogeneous
  - order
  - ordinary/partial
  - autonomous/non-autonomous
  - homogeneous/non-homogeneous
  - constant coefficients/variable coefficients
- Definition solution of a DE/IVP/BVP
- Superposition principle for linear differential equations


It can be shown that a first-order differential equation, that satisfies certain conditions, has a general solution with one degree of freedom; somewhere in the process of solving such a differential equation we have to integrate once which gives rise to a so-called arbitrary **constant of integration**.

Then this arbitrary constant can be chosen in such a way that the solution also satisfies an initial condition of the form $y(t_0)=y_0$.

::::::{prf:example}
The differential equation $y'=3x^2$ has the general solution $y(x)=x^3+C$ with $C\in\mathbb{R}$. However, there is only solution that also satisfies the initial condition $y(0)=0$: $y(x)=x^3$, since $y(0)=0$ leads to $0=0^3+C=C$.
::::::

::::::{prf:example}
The differential equation $y'=2y$ has the general solution $y(x)=Ce^{2x}$ with $C\in\mathbb{R}$. However, there is only one solution that also satisfies the initial condition $y(0)=3$: $y(x)=3e^{2x}$, since $y(0)=3$ leads to $3=Ce^{2\cdot0}=C$.
:::::: 