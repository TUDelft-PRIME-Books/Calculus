# NOTE: Differential equations and initial-value problems

NOTE: I find it not ideal that these chapters so late. The subjects and techniques used here are much closer to single-variable calculus than to multivariable calculus. Also: it can be useful to use differential equations as examples in the multivariable chapters, for instance when discussing partial derivatives. Proposal: Move these chapters between Integration and Sequences.

In this section we cover:

- Introduction by means of examples
- Definitions of differential equations and of initial-value problems
- Definition (in)dependent variable
- Definition linear/nonlinear
- Definition homogeneous/nonhomogeneous

It can be shown that a first-order differential equation, that satisfies certain conditions, has a general solution with one degree of freedom; somewhere in the process of solving such a differential equation we have to integrate once which gives rise to a so-called arbitrary **integration constant**.

Then this arbitrary constant can be chosen in such a way that the solution also satisfies an initial condition of the form $y(t_0)=y_0$.

::::::{prf:Example}
The differential equation $y'=3x^2$ has the general solution $y(x)=x^3+C$ with $C\in\mathbb{R}$. However, there is only solution that also satisfies the initial condition $y(0)=0$: $y(x)=x^3$, since $y(0)=0$ leads to $0=0^3+C=C$.
::::::

::::::{prf:Example}
The differential equation $y'=2y$ has the general solution $y(x)=Ce^{2x}$ with $C\in\mathbb{R}$. However, there is only one solution that also satisfies the initial condition $y(0)=3$: $y(x)=3e^{2x}$, since $y(0)=3$ leads to $3=Ce^{2\cdot0}=C$.
:::::: 