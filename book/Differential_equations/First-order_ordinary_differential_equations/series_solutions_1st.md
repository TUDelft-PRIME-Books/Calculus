(Sec:ODE1:Series)=

# Series solutions

In this section we cover:

- Ordinary and singular points
- Power series solutions around ordinary points, including Taylor series

:::{prf:remark}
Restrict to first-order differential equations.
:::

A first-order linear differential equation has the form

$$
P(x)y'(x)+Q(x)y(x)=G(x),
$$

where $P$, $Q$ and $G$ are continuous functions with $P(x)\neq0$.

Sometimes these differential equations can't be solved explicitly in terms of finite combinations of simple familiar functions.

In the case of linear differential equations it is sometimes possible to find a solution in terms of power series. The method is to substitute such a power series into the differential equation and try to determine the values of the coefficients. We first illustrate the method by solving the differential equation $y'=y$ for which we already know the general solution: $y(x)=Ce^x$ with $C\in\mathbb{R}$.

::::::{prf:example}
Use power series to solve the differential equation $y'=y$.

Solution. We assume that there is a solution of the form $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$. Then we have: $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$. Substitution leads to

$$
\sum_{n=1}^{\infty}nc_nx^{n-1}=\sum_{n=0}^{\infty}c_nx^n\quad\Longleftrightarrow\quad\sum_{n=0}^{\infty}(n+1)c_{n+1}x^n=\sum_{n=0}^{\infty}c_nx^n.
$$

This implies that $(n+1)c_{n+1}=c_n$ for $n=0,1,2,\ldots$ or equivalently $nc_n=c_{n-1}$ for $n=1,2,3,\ldots$. This leads to

$$
c_n=\frac{1}{n}c_{n-1}=\frac{1}{n}\cdot\frac{1}{n-1}c_{n-2}=\ldots=\frac{1}{n}\cdot\frac{1}{n-1}\cdot\cdots\cdot\frac{1}{1}c_0=\frac{1}{n!}c_0
$$

for $n=1,2,3,\ldots$. Hence we have

$$
y(x)=\sum_{n=0}^{\infty}c_nx^n=c_0\sum_{n=0}^{\infty}\frac{1}{n!}x^n=c_0e^x.
$$

::::::
