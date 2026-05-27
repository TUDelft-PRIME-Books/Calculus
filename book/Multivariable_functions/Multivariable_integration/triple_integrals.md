# Triple integrals

In this section we cover:

- Triple integrals (can go quicker): Riemann sums, repeated integrals and Fubini's theorem
- Triple integrals: general regions
- Multiple integrals: basic ideas
- Improper triple integrals (discontinuous integrand)
- Applications: total mass/charge, center of mass, moments of inertia,\ldots
- Applications as motivation and/or illustration of the use of multiple integrals.

## Introduction

Let $\rho(x,y,z)\geq0$ be a *mass density function* defined on a solid $E$ in $\mathbb{R}^3$. Our aim is to define a triple integral

$$
\iiint\limits_E\rho(x,y,z)\,dV,
$$
 
which denotes the *(total) mass* of the solid $E$.

Consider the rectangular box $B$ given by

$$
B=[a,b]\times[c,d]\times[e,f]=\{(x,y,z)\,|\,a\leq x\leq b,\;c\leq y\leq d,\;e\leq z\leq f\}.
$$

The first step is to divide $B$ into sub-boxes. We do this by dividing the interval $[a,b]$ into $\ell$ subintervals $[x_{i-1},x_i]$ of equal width $\Delta x=(b-a)/\ell$, dividing the interval $[c,d]$ into $m$ subintervals $[y_{j-1},y_j]$  of equal width $\Delta y=(d-c)/m$ and dividing the interval $[e,f]$ into $n$ subintervals $[z_{k-1},z_k]$ of equal width $\Delta z=(f-e)/n$.

This divides the rectangular box $B$ into sub-boxes

$$
B_{ijk}=[x_{i-1},x_i]\times[y_{j-1},y_j]\times[z_{k-1},z_k].
$$

Each sub-box $B_{ijk}$ has volume $\Delta V=\Delta x\,\Delta y\,\Delta z$.

Now we form the **triple Riemann sum**

$$
\sum_{i=1}^{\ell}\sum_{j=1}^m\sum_{k=1}^n\rho(x_{ijk}^*,y_{ijk}^*z_{ijk}^*)\,\Delta V,
$$

where the *sample point* $(x_{ijk}^*,y_{ijk}^*,z_{ijk}^*)$ is in $B_{ijk}$. This leads to

:::::{prf:definition}
:label: Def:MultivariableIntegration:TripleIntegral

The **triple integral** of $\rho$ over the rectangular box $B$ is

$$
\iiint\limits_B\rho(x,y,z)\,dV=\lim\limits_{\ell\to\infty}\lim\limits_{m\to\infty}\lim\limits_{n\to\infty}
\sum_{i=1}^{\ell}\sum_{j=1}^m\sum_{k=1}^n\rho(x_{ijk}^*,y_{ijk}^*z_{ijk}^*)\,\Delta V.
$$  
  
The triple integral exists if $\rho$ is continuous. We can choose the sample point to be any point in the sub-box, however if we choose it to be the point $(x_i,y_j,z_k)$ we get a simpler looking expression for the triple integral:

$$
\iiint\limits_B\rho(x,y,z)\,dV=\lim\limits_{\ell\to\infty}\lim\limits_{m\to\infty}\lim\limits_{n\to\infty}
\sum_{i=1}^{\ell}\sum_{j=1}^m\sum_{k=1}^n\rho(x_i,y_j,z_k)\,\Delta V.
$$

:::::

## Fubini's theorem

:::::{prf:theorem} Fubini
:label: Thm:MultivariableIntegration:Fubini

If $\rho$ is continuous on the rectangular box $B=[a,b]\times[c,d]\times[e,f]$, then

$$
\iiint\limits_B\rho(x,y,z)\,dV=\int_e^f\int_c^d\int_a^b\rho(x,y,z)\,dx\,dy\,dz.
$$
 
The iterated integral on the right can be written in six different orders, all with the same value.

:::::

:::{prf:example}
:label: Ex:MultivariableIntegration:Example1

We evaluate the triple integral $\displaystyle\iiint\limits_Bx^2yz\,dV$, where $B$ is the rectangular box given by

$$
B=[0,1]\times[-1,2]\times[0,3]=\{(x,y,z)\,|\,0\leq x\leq1,\;-1\leq y\leq2,\;0\leq z\leq3\}.
$$

Note that

\begin{align*}
\iiint\limits_Bx^2yz\,dV&=\int_0^3\int_{-1}^2\int_0^1x^2yz\,dx\,dy\,dz\\
&=\left(\int_0^1x^2\,dx\right)\left(\int_{-1}^2y\,dy\right)\left(\int_0^3z\,dz\right)\\
&=\bigg[\frac{1}{3}x^3\bigg]_{x=0}^1\bigg[\frac{1}{2}y^2\bigg]_{y=-1}^2\bigg[\frac{1}{2}z^2\bigg]_{z=0}^3\\
&=\frac{1}{3}\cdot\frac{3}{2}\cdot\frac{9}{2}\\
&=\frac{9}{4}.
\end{align*} 	

:::

## General regions

A tripe integral over a general bounded region (a solid) $E$ in $\mathbb{R}^3$ is defined by much the same procedure that we used for double integrals. We enclose $E$ in a rectangular box $B$ and we define a function $\Omega$ so that it agrees with $\rho$ on $E$ and is $0$ for points in $B$ that are outside $E$. Then:

$$
\iiint\limits_E\rho(x,y,z)\,dV=\iiint\limits_B\Omega(x,y,z)\,dV.
$$  
 
This integral exists if $\rho$ is continuous and the boundary of $E$ is "reasonably smooth".
