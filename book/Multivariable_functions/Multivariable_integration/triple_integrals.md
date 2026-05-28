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
:label: Ex:MultivariableIntegration:TripleIntegralsExample1

We evaluate the triple integral $\displaystyle\iiint\limits_Bx^2yz\,dV$, where $B$ is the rectangular box given by

\begin{align*}
B&=[0,1]\times[-1,2]\times[0,3]\\
&=\{(x,y,z)\,|\,0\leq x\leq1,\;-1\leq y\leq2,\;0\leq z\leq3\}.
\end{align*}

Note that

\begin{align*}
\iiint\limits_Bx^2yz\,dV&=\int_0^3\int_{-1}^2\int_0^1x^2yz\,dx\,dy\,dz\\
&=\left(\int_0^1x^2\,dx\right)\left(\int_{-1}^2y\,dy\right)\left(\int_0^3z\,dz\right)\\
&=\bigg[\frac{1}{3}x^3\bigg]_{x=0}^1\bigg[\frac{1}{2}y^2\bigg]_{y=-1}^2\bigg[\frac{1}{2}z^2\bigg]_{z=0}^3\\
&=\frac{1}{3}\cdot\frac{3}{2}\cdot\frac{9}{2}\\
&=\frac{9}{4}.
\end{align*} 	

:::

## Average value

The average value of a function $f$ of three variables defined on a rectangular box $B$ is 

$$
\frac{1}{\text{vol}(B)}\iiint\limits_Bf(x,y,z)\,dA.
$$

:::{prf:example}
:label: Ex:MultipleIntegration:TripleIntegralsAverageValue

Consider a metal box $B=[-5,5]\times[-3,3]\times[-1,1]$, where the temperature $T$ (in ${}^{\circ}\text{C}$) in each point $(x,y,z)\in B$ is given by $T(x,y,z)=50-3x^2-3y^2-3z^2$. Then we have: $\text{vol}(B)=10\cdot6\cdot1=60$ and

\begin{align*}
&\iiint_B\left(50-3x^2-3y^2-3z^2\right)\,dV\\
&{}\hspace{10mm}{}=\int_{-5}^5\int_{-3}^3\int_{-1}^1\left(50-3x^2-3y^2-3z^2\right)\,dz\,dy\,dx\\
&{}\hspace{10mm}{}=\int_{-5}^5\int_{-3}^3\bigg[50z-3x^2z-3y^2z-z^3\bigg]_{z=-1}^1\\
&{}\hspace{10mm}{}=\int_{-5}^5\int_{-3}^3 2\cdot\left(50-3x^2-3y^2-1\right)\,dx\\
&{}\hspace{10mm}{}=\int_{-5}^5\bigg[98y-6x^2y-2y^3\bigg]_{y=-3}^3\\
&{}\hspace{10mm}{}=\int_{-5}^5 2\cdot\left(294-18x^2-54\right)\,dx\\
&{}\hspace{10mm}{}=\bigg[480x-12x^3\bigg]_{x=-5}^5\\
&{}\hspace{10mm}{}=2\cdot\left(2400-1500\right)\\
&{}\hspace{10mm}{}=1800.
\end{align*}

Hence, the average temperature in $B$ equals $\dfrac{1800}{60}=30^{\circ}\text{C}$.

:::

## General regions

A tripe integral over a general bounded region (a solid) $E$ in $\mathbb{R}^3$ is defined by much the same procedure that we used for double integrals. We enclose $E$ in a rectangular box $B$ and we define a function $\Omega$ so that it agrees with $\rho$ on $E$ and is $0$ for points in $B$ that are outside $E$. Then:

$$
\iiint\limits_E\rho(x,y,z)\,dV=\iiint\limits_B\Omega(x,y,z)\,dV.
$$  
 
This integral exists if $\rho$ is continuous and the boundary of $E$ is "reasonably smooth".

### $z$-simple regions

```{figure} Images/z-simple.png
---
width: 50%
name: z-simple
align: center
---

```

A solid region $E$ in $\mathbb{R}^3$ is said to be $z$-simple if it lies between the graphs of two continuous functions of $x$ and $y$:

$$
E=\{(x,y,z)\,|\,(x,y)\in D,\;u_1(x,y)\leq z\leq u_2(x,y)\},
$$

where $D$ is the projection of $E$ onto the $xy$-plane. Then:

$$
\iiint\limits_E\rho(x,y,z)\,dV=\iint\limits_D\left(\int_{u_1(x,y)}^{u_2(x,y)}\rho(x,y,z)\,dz\right)\,dA.
$$

### $x$-simple regions

```{figure} Images/x-simple.png
---
width: 50%
name: x-simple
align: center
---

```

A solid region $E$ in $\mathbb{R}^3$ is said to be $x$-simple if it lies between the graphs of two continuous functions of $y$ and $z$:

$$
E=\{(x,y,z)\,|\,(y,z)\in D,\;u_1(y,z)\leq x\leq u_2(y,z)\},
$$

where $D$ is the projection of $E$ onto the $yz$-plane. Then:

$$
\iiint\limits_E\rho(x,y,z)\,dV=\iint\limits_D\left(\int_{u_1(y,z)}^{u_2(y,z)}\rho(x,y,z)\,dx\right)\,dA.
$$

### $y$-simple regions

```{figure} Images/y-simple.png
---
width: 50%
name: y-simple
align: center
---

```

A solid region $E$ in $\mathbb{R}^3$ is said to be $y$-simple if it lies between the graphs of two continuous functions of $x$ and $z$:

$$
E=\{(x,y,z)\,|\,(x,z)\in D,\;u_1(x,z)\leq y\leq u_2(x,z)\},
$$

where $D$ is the projection of $E$ onto the $xz$-plane. Then:

$$
\iiint\limits_E\rho(x,y,z)\,dV=\iint\limits_D\left(\int_{u_1(x,z)}^{u_2(x,z)}\rho(x,y,z)\,dy\right)\,dA.
$$

## Examples

:::{prf:example}
:label: Ex:MultivariableIntegration:TripleIntegralsExample2

We evaluate $\displaystyle\iiint\limits_Ex\,dV$, where $E$ is the solid tetrahedron bounded by the four planes $x=0$, $y=0$, $z=0$ and $x+y+z=1$.

```{figure} Images/triple1a.png
---
width: 50%
name: triple1a
align: left
---

```

```{figure} Images/triple1b.png
---
width: 50%
name: triple1b
align: right
---

```

Note that the projection of $E$ on the $xy$-plane is

$$
D=\{(x,y)\,|\,0\leq x\leq 1,\;0\leq y\leq 1-x\}.
$$

Using the description of $E$ as a $z$-simple region, the tetrahedron is between the planes $z=0$ and $z=1-x-y$, we have:

\begin{align*}
\iiint\limits_Ex\,dV&=\iint\limits_D\left(\int_0^{1-x-y}x\,dz\right)\,dA\\
&=\iint\limits_Dx(1-x-y)\,dA\\
&=\int_0^1\int_0^{1-x}x(1-x-y)\,dy\,dx\\
&=\int_0^1\bigg[x(1-x)y-\frac{1}{2}xy^2\bigg]_0^{1-x}\,dx\\
&=\int_0^1\left(x(1-x)^2-\frac{1}{2}x(1-x)^2\right)\,dx\\
&=\frac{1}{2}\int_0^1x(1-x)^2\,dx\\
&=\frac{1}{2}\int_0^1\left(1-(1-x)\right)(1-x)^2\,dx\\
&=\frac{1}{2}\int_0^1(1-x)^2\,dx-\frac{1}{2}\int_0^1(1-x)^3\,dx\\
&=-\frac{1}{6}\bigg|_0^1+\frac{1}{8}(1-x)^4\bigg|_0^1\\
&=\frac{1}{6}-\frac{1}{8}\\
&=\frac{1}{24}.
\end{align*}

Note that the projection of $E$ on the $yz$-plane is

$$
D=\{(y,z)\,|\,0\leq y\leq 1,\;0\leq z\leq 1-y\}.
$$

Using the description of $E$ as a $x$-simple region, the tetrahedron is between the planes $x=0$ and $x=1-y-z$, we have:

\begin{align*}
\iiint\limits_Ex\,dV&=\iint\limits_D\left(\int_0^{1-y-z}x\,dx\right)\,dA\\
&=\frac{1}{2}\iint\limits_D(1-y-z)^2\,dA\\
&=\frac{1}{2}\int_0^1\int_0^{1-y}(1-y-z)^2\,dz\,dy\\
&=\frac{1}{2}\int_0^1\bigg[-\frac{1}{3}(1-y-z)^3\bigg]_{z=0}^{1-y}\,dy\\
&=\frac{1}{6}\int_0^1(1-y)^3\,dy\\
&=-\frac{1}{24}(1-y)^4\bigg|_0^1\\
&=\frac{1}{24}.
\end{align*}

:::

:::{prf:example}
:label: Ex:MultivariableIntegration:TripleIntegralsExample3

We want to evaluate $\displaystyle\iiint\limits_E\sqrt{x^2+z^2}\,dV$, where $E$ is the region bounded by the paraboloid $y=x^2+z^2$ and the plane $y=4$.

```{figure} Images/triple2a.png
---
width: 50%
name: triple2a
align: left
---

```

```{figure} Images/triple2b.png
---
width: 50%
name: triple2b
align: right
---

```

Note that the projection of $E$ on the $xy$-plane is

$$
D=\{(x,y)\,|\,-2\leq x\leq 2,\;x^2\leq y\leq 4\}.
$$

Therefore, if we consider $E$ as a $z$-simple region, we obtain

$$
\iiint\limits_E\sqrt{x^2+z^2}\,dV=\iint\limits_D\left(\int_{-\sqrt{y-x^2}}^{\sqrt{y-x^2}}\sqrt{x^2+z^2}\,dz\right)\,dA
=\int_{-2}^2\int_{x^2}^4\int_{-\sqrt{y-x^2}}^{\sqrt{y-x^2}}\sqrt{x^2+z^2}\,dz\,dy\,dx,
$$  
 
which is extremely difficult to evaluate.

```{figure} Images/triple2c.png
---
width: 50%
name: triple2c
align: right
---

```

However, if we consider $E$ as a $y$-simple region, the projection of $E$ onto the $xz$-plane is the disk

$$
D=\{(x,z)\,|\,x^2+z^2\leq 4\}.
$$

Then we have:

\begin{align*}
\iiint\limits_E\sqrt{x^2+z^2}\,dV&=\iint\limits_D\left(\int_{x^2+z^2}^4\sqrt{x^2+z^2}\,dy\right)\,dA\\
&=\iint\limits_{D_3}(4-x^2-z^2)\sqrt{x^2+z^2}\,dA.
\end{align*}
 
Using polar coordinates we now obtain

\begin{align*}
\iiint\limits_E\sqrt{x^2+z^2}\,dV&=\iint\limits_{D_3}(4-x^2-z^2)\sqrt{x^2+z^2}\,dA\\
&=\int_0^{2\pi}\int_0^2(4-r^2)\,r\,r\,dr\,d\theta\\
&=\int_0^{2\pi}d\theta\int_0^2(4r^2-r^4)\,dr\\
&=2\pi\bigg[\frac{4}{3}r^3-\frac{1}{5}r^5\bigg]_{r=0}^2\\
&=2\pi\left(\frac{32}{3}-\frac{32}{5}\right)\\
&=2\pi\cdot32\cdot\frac{2}{15}\\
&=\frac{128}{15}\pi.
\end{align*}

:::

## Applications

If $\rho(x,y,z)=1$ for all points $(x,y,z)$ in $E$, then the (total) mass of $E$ equals the **volume** of $E$:

$$
\textrm{vol}(E)=\iiint\limits_E1\,dV.
$$
 
If $\rho(x,y,z)\geq0$ is a mass density function defined on a solid $E$ in $\mathbb{R}^3$, then

$$
m=\iiint\limits_E\rho(x,y,z)\,dV
$$
 
denotes the (total) **mass** of $E$. Then the integrals

$$  
\iiint\limits_Ex\,\rho(x,y,z)\,dV,\quad\iiint\limits_Ey\,\rho(x,y,z)\,dV\quad\textrm{and}\quad\iiint\limits_Ez\,\rho(x,y,z)\,dV
$$  
 
are the **moments** of $E$ about the three coordinate planes $x=0$, $y-0$ and $z=0$, respectively.

The **center of mass** of $E$ is located at the point $(\overline{x},\overline{y},\overline{z})$ with
 
\begin{align*}
&\overline{x}=\frac{1}{m}\iiint\limits_Ex\,\rho(x,y,z)\,dV,\quad\overline{y}=\frac{1}{m}\iiint\limits_Ey\,\rho(x,y,z)\,dV\\
&{}\quad\textrm{and}\quad\overline{z}=\frac{1}{m}\iiint\limits_Ez\,\rho(x,y,z)\,dV,
\end{align*}

where $m=\displaystyle\iiint\limits_E\rho(x,y,z)\,dV$ denotes the (total) mass of  $E$.

If the mass density function $\rho(x,y,z)$ is constant, then the center of mass is called the **centroid** of the solid $E$.

If $\rho(x,y,z)\geq0$ is a mass density function defined on a solid $E$ in $\mathbb{R}^3$, then the integrals

\begin{align*}
&I_x=\iiint\limits_E(y^2+z^2)\rho(x,y,z)\,dV,\quad I_y=\iiint\limits_E(x^2+z^2)\rho(x,y,z)\,dV\\
&{}\quad\textrm{and}\quad I_z=\iiint\limits_E(x^2+y^2)\rho(x,y,z)\,dV  
\end{align*}

are the **moments of inertia** of the solid $E$ about the $x$-axis, the $y$-axis and the $z$-axis, respectively.

In {prf:ref}`Ex:MultivariableIntegration:DirichletIntegral` through {prf:ref}`Ex:MultivariableIntegration:DoubleIntegralsExample3` we used double integrals to evaluate a single integral. In the next example we use a triple integral.

:::::{prf:example}
:label: Ex:MultivariableIntegration:TripleIntegralsExample

For $\alpha>0$ and $\beta>0$ we have

\begin{align*}
\int_0^{\infty}\frac{(1-e^{-\alpha x})(1-e^{-\beta x})}{x^2}\,dx&=\int_0^{\infty}\left(\int_0^{\alpha}e^{-xy}\,dy\right)\left(\int_0^{\beta}e^{-xz}\,dz\right)\,dx\\
&=\int_0^{\alpha}\int_0^{\beta}\left(\int_0^{\infty}e^{-x(y+z)}\,dx\right)\,dz\,dy\\
&=\int_0^{\alpha}\int_0^{\beta}\frac{1}{y+z}\,dz\,dy\\
&=\int_0^{\alpha}\left(\ln(y+\beta)-\ln(y)\right)\,dy\\
&=\bigg[(y+\beta)\ln(y+\beta)-y\ln(y)\bigg]_0^{\alpha}\\
&=(\alpha+\beta)\ln(\alpha+\beta)-\alpha\ln(\alpha)-\beta\ln(\beta).
\end{align*}

:::::
