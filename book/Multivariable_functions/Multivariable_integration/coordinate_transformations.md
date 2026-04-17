# Coordinate transformations in $\mathbb{R}^2$

- Double integral using general coordinate transform
  - Double integral in polar coordinates as an example.
  - Add theorem on Jacobian for polar coordinates.

## Polar coordinates

For regions which are part of a disk, we might use **polar coordinates**: 

$$
\left\{\begin{array}{l}x=r\cos(\theta)\\y=r\sin(\theta)\end{array}\right.\quad\Longrightarrow\quad x^2+y^2=r^2.
$$

We start with a **polar rectangle**

$$
R=\{(r\cos(\theta),r\sin(\theta))\,|\,a\leq r\leq b,\;\alpha\leq\theta\leq\beta\}\;\textrm{with}\; a\geq0\;\textrm{and}\;\beta-\alpha\leq2\pi.
$$

```{figure} Images/polar1.png
---
width: 50%
name: polar1
align: center
---
The polar rectangle $R$.
```

In order to find the double integral $\displaystyle\iint\limits_Rf(x,y)\,dA$ over such a polar rectangle $R$, we divide the interval $[a,b]$ into $m$ subintervals $[r_{i-1},r_i]$ with equal width $\Delta r=(b-a)/m$ and we divide the interval $[\alpha,\beta]$ into $n$ subintervals $[\theta_{j-1},\theta_j]$ of equal width $\Delta\theta=(\beta-\alpha)/n$.

```{figure} Images/polar2.png
---
width: 50%
name: polar2
align: center
---
The division of the polar rectangle $R$ into smaller polar rectangles $R_{ij}$.
```

Now we consider the polar rectangles

$$
R_{ij}=\{(r\cos(\theta),r\sin(\theta))\,|\,r_{i-1}\leq r\leq r_i,\;\theta_{j-1}\leq\theta\leq\theta_j\}
$$

with area (let: $r_i^*=(r_i+r_{i-1})/2$)

\begin{align*}
\Delta A_{ij}&=\frac{1}{2}r_i^2\,\Delta\theta-\frac{1}{2}r_{i-1}^2\,\Delta\theta\\
&=\frac{1}{2}(r_i^2-r_{i-1}^2)\,\Delta\theta\\
&=\frac{1}{2}(r_i+r_{i-1})(r_i-r_{i-1})\,\Delta\theta\\
&=r_i^*\,\Delta r\,\Delta\theta. 
\end{align*}
 
Here we have: $\Delta r=r_i-r_{i-1}$ and $\Delta\theta=\theta_j-\theta_{j-1}$.

It is easier to *approximate* the area of a polar rectangle. Note that the length of an arc of a circle with radius $r$ and difference of angles $\Delta\theta$ equals $r\,\Delta\theta$. This implies that the area of a polar rectangle is approximately equal to the area of a rectangle with sides $\Delta r$ and $r\,\Delta\theta$, which is: $r\,\Delta r\,\Delta\theta$.

:::::{prf:theorem}
:label: Thm:MultivariableIntegration:PolarRectangle
If $f$ is continuous on a polar rectangle $R$ given by $0\leq a\leq r\leq b$ and $\alpha\leq\theta\leq\beta$ with $\beta-\alpha\leq2\pi$, then

$$
\iint\limits_Rf(x,y)\,dA=\int_{\alpha}^{\beta}\int_a^bf(r\cos(\theta),r\sin(\theta))\,r\,dr\,d\theta.
$$

In polar coordinates $\left\{\begin{array}{l}x=r\cos(\theta)\\y=r\sin(\theta)\end{array}\right.$  the area element equals $dA=r\,dr\,d\theta$.
:::::

:::::{prf:example}
:label: Ex:MultivariableIntegration:PolarRectangleExample1

We evaluate $\displaystyle\iint\limits_R(3x+4y^2)\,dA$, where $R$ is the region in the upper half-plane bounded by the circles $x^2+y^2=1$ and $x^2+y^2=4$.

```{figure} Images/polarcoord1.png
---
width: 50%
name: polarcoord1
align: center
---
The region $R=\{(x,y)\,|\,y\geq0,\;1\leq x^2+y^2\leq 4\}$.
```

Note that the region $R=\{(x,y)\,|\,y\geq0,\;1\leq x^2+y^2\leq 4\}$ is described in polar coordinates as

$$
R=\{(r\cos(\theta),r\sin(\theta))\,|\,1\leq r\leq 2,\;0\leq\theta\leq\pi\}.
$$

Hence we have using $\cos(2\theta)=1-2\sin^2(\theta)$:

\begin{align*}
\iint\limits_R(3x+4y^2)\,dA&=\int_0^{\pi}\int_1^2\left(3r\cos(\theta)+4r^2\sin^2(\theta)\right)\,r\,dr\,d\theta\\
&=\int_0^{\pi}\bigg[r^3\cos(\theta)+r^4\sin^2(\theta)\bigg]_{r=1}^2\,d\theta\\
&=\int_0^{\pi}\left(7\cos(\theta)+15\sin^2(\theta)\right)\,d\theta\\
&=\int_0^{\pi}\left(7\cos(\theta)+\frac{15}{2}\left(1-\cos(2\theta)\right)\right)\,d\theta\\
&=\bigg[7\sin(\theta)+\frac{15}{2}\theta-\frac{15}{4}\sin(2\theta)\bigg]_{\theta=0}^{\pi}\\
&=\frac{15}{2}\pi.
\end{align*}

:::::

:::::{prf:example}
:label: Ex:MultivariableIntegration:PolarRectangleExample2

Let us find the volume of the solid bounded by the plane $z=0$ and the paraboloid $z=1-x^2-y^2$.

```{figure} Images/polarcoord2.png
---
width: 50%
name: polarcoord2
align: center
---
The solid bounded by the plane $z=0$ and the paraboloid $z=1-x^2-y^2$.
```

Note that the intersection of the paraboloid and the $xy$-plane ($z=0$) is the circle $x^2+y^2=1$. So, the solid lies under the paraboloid and above the circular disk $D$ given by $x^2+y^2\leq1$. In polar coordinates $D$ is given by

$$
D=\{(r\cos(\theta),r\sin(\theta))\,|\,0\leq r\leq1,\;0\leq\theta\leq2\pi\}.
$$

Hence the volume equals

\begin{align*}
V&=\iint\limits_D(1-x^2-y^2)\,dA\\
&=\int_0^{2\pi}\int_0^2(1-r^2)\,r\,dr\,d\theta\\
&=\int_0^{2\pi}d\theta\,\int_0^1(r-r^3)\,dr\\
&=2\pi\bigg[\frac{1}{2}r^2-\frac{1}{4}r^4\bigg]_{r=0}^1\\
&=\frac{1}{2}\pi.
\end{align*}

:::::

## More general regions

:::::{prf:theorem}
:label: Thm:MultivariableIntegration:PolarGeneral
If $f$ is continuous on a polar region of the form

$$
D=\{(r\cos(\theta),r\sin(\theta))\,|\,\alpha\leq\theta\leq\beta,\;h_1(\theta)\leq r\leq h_2(\theta)\}\;\textrm{with}\;\beta-\alpha\leq2\pi,
$$

then

$$
\iint\limits_Df(x,y)\,dA=\int_{\alpha}^{\beta}\int_{h_1(\theta)}^{h_2(\theta)}f(r\cos(\theta),r\sin(\theta))\,r\,dr\,d\theta.
$$

```{figure} Images/polar3.png
---
width: 50%
name: polar3
align: center
---
The polar region $D$.
```

:::::

:::::{prf:example}
:label: Ex:MultivariableIntegration:PolarGeneralExample1

We want to find the area of the region $D$ enclosed by one loop of the four-leaved rose $r=\cos(2\theta)$.

```{figure} Images/polarcoord3.png
---
width: 50%
name: polarcoord3
align: center
---
The region $D$ enclosed by one loop of the four-leaved rose $r=\cos(2\theta)$.
```

Note that the region $D$ in polar coordinates is given by

$$
D=\{(r\cos(\theta),r\sin(\theta))\,|\,-\textstyle\frac{1}{4}\pi\leq\theta\leq\frac{1}{4}\pi,\;0\leq\theta\leq\cos(2\theta)\}.
$$ 
 
Hence we have using $\cos(2x)=2\cos^2(x)-1$:

\begin{align*}
\textrm{area}(D)&=\iint\limits_D1\,dA\\
&=\int_{-\frac{1}{4}\pi}^{\frac{1}{4}\pi}\int_0^{\cos(2\theta)}r\,dr\,d\theta\\
&=\int_{-\frac{1}{4}\pi}^{\frac{1}{4}\pi}\bigg[\frac{1}{2}r^2\bigg]_{r=0}^{\cos(2\theta)}\,d\theta\\
&=\frac{1}{2}\int_{-\frac{1}{4}\pi}^{\frac{1}{4}\pi}\cos^2(2\theta)\,d\theta\\
&=\frac{1}{4}\int_{-\frac{1}{4}\pi}^{\frac{1}{4}\pi}\left(1+\cos(4\theta)\right)\,d\theta\\
&=\frac{1}{4}\bigg[\theta+\frac{1}{4}\sin(4\theta)\bigg]_{\theta=-\frac{1}{4}\pi}^{\frac{1}{4}\pi}\\
&=\frac{1}{8}\pi.
\end{align*} 

:::::

:::::{prf:example}
:label: Ex:MultivariableIntegration:PolarGeneralExample2

We want to find the volume of the solid that lies under the paraboloid $z=x^2+y^2$, above the $xy$-plane and inside the cylinder $x^2+y^2=2x$.

```{figure} Images/polarcoord4.png
---
width: 50%
name: polarcoord4
align: left
---
The disk $D$ with boundary circle given by $x^2+y^2=2x$
```

```{figure} Images/polarcoord5.png
---
width: 50%
name: polarcoord5
align: right
---
The solid under the paraboloid $z=x^2+y^2$, above the $xy$-plane and inside the cylinder $x^2+y^2=2x$.
```

The solid lies above the disk $D$ with boundary circle given by $x^2+y^2=2x$ or equivalently, completing the square, by $(x-1)^2+y^2=1$. In polar coordinates we have $x^2+y^2=r^2$ and $x=r\cos(\theta)$, so this boundary circle becomes $r^2=2r\cos(\theta)$ or $r=2\cos(\theta)$. Hence we have:

$$
D=\{(r\cos(\theta),r\sin(\theta))\,|\,-\textstyle\frac{1}{2}\pi\leq\theta\leq\frac{1}{2}\pi,\;0\leq r\leq2\cos(\theta)\}.
$$ 
 
Hence the volume equals using $\cos(2\theta)=2\cos^2(\theta)-1$

\begin{align*}
V&=\iint\limits_D(x^2+y^2)\,dA\\
&=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\int_0^{2\cos(\theta)}r^2\,r\,dr\,d\theta\\
&=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\bigg[\frac{1}{4}r^4\bigg]_{r=0}^{2\cos(\theta)}\,d\theta\\
&=4\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\cos^4(\theta)\,d\theta=8\int_0^{\frac{1}{2}\pi}\cos^4(\theta)\,d\theta\\
&=8\int_0^{\frac{1}{2}\pi}\left(\frac{1+\cos(2\theta)}{2}\right)^2\,d\theta\\
&=2\int_0^{\frac{1}{2}\pi}\left(1+2\cos(2\theta)+\cos^2(2\theta)\right)\,d\theta\\
&=2\int_0^{\frac{1}{2}\pi}\left(1+2\cos(2\theta)+\frac{1}{2}\left(1+\cos(4\theta)\right)\right)\,d\theta\\
&=\bigg[3\theta+2\sin(2\theta)+\frac{1}{2}\sin(4\theta)\bigg]_{\theta=0}^{\frac{1}{2}\pi}\\
&=\frac{3}{2}\pi.
\end{align*}

:::::

## Applications

:::::{prf:example}
:label: Ex:MultivariableIntegration:PolarApplicationsExample1

A swimming pool is circular with a diameter of $10\,\text{m}$. The depth is constant along east-west lines and increases linearly from $1\,\text{m}$ at the south end to $2\,\text{m}$ at the north end. We want to find the volume of water in the pool.

```{figure} Images/pool.png
---
width: 75%
name: pool
align: center
---
A circular pool.
```

Note that the linear function $f(x)$ such that $f(-5)=1$ and $f(5)=2$ is given by 
 
$$
f(x)=\frac{1}{10}x+\frac{3}{2}=\frac{x+15}{10}.
$$ 
 
Then the volume is given by $V=\displaystyle\iint\limits_{x^2+y^2\leq25}\frac{x+15}{10}\,dA$. 

Using polar coordinates we obtain

\begin{align*}
V&=\int_0^{2\pi}\int_0^5\frac{r\cos(\theta)+15}{10}\,r\,dr\,d\theta\\
&=\int_0^{2\pi}\bigg[\frac{1}{30}r^3\cos(\theta)+\frac{3}{4}r^2\bigg]_{r=0}^5\,d\theta\\
&=\int_0^{2\pi}\left(\frac{25}{6}\cos(\theta)+\frac{75}{4}\right)\,d\theta\\
&=0+\frac{75}{4}\cdot2\pi\\
&=\frac{75}{2}\pi.
\end{align*}

:::::

:::::{prf:example}
:label: Ex:MultivariableIntegration:PolarApplicationsExample2

Earlier we have seen that the *Gaussian integral* is: $\displaystyle\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt{\pi}$. 

Now we are able to prove this result.

We start with $\displaystyle\int_{-\infty}^{\infty}e^{-x^2}\,dx=2\int_0^{\infty}e^{-x^2}\,dx$ and 

$$
\int_0^{\infty}e^{-x^2}\,dx=\lim\limits_{R\to\infty}\int_0^Re^{-x^2}\,dx.
$$ 

Now we have

$$
\left(\int_0^Re^{-x^2}\,dx\right)^2=\left(\int_0^Re^{-x^2}\,dx\right)\left(\int_0^Re^{-y^2}\,dy\right)=\iint\limits_{[0,R]\times[0,R]}e^{-x^2-y^2}\,dA.
$$
 
Note that

$$
\iint\limits_{C_1}e^{-x^2-y^2}\,dA\leq\iint\limits_{[0,R]\times[0,R]}e^{-x^2-y^2}\,dA\leq\iint\limits_{C_2}e^{-x^2-y^2}\,dA 
$$  
 
with 

$$
C_1=\{(x,y)\,|\,x\geq0,\;y\geq0,\;x^2+y^2\leq R^2\}
$$ 

and 

$$
C_2=\{(x,y)\,|\,x\geq0,\;y\geq0,\;x^2+y^2\leq 2R^2\}.
$$

```{figure} Images/improper.png
---
width: 50%
name: improper
align: center
---
The region $[0,R]\times[0,R]$ and the quarter circles $C_1$ and $C_2$.
```

Now we use polar coordinates to obtain

\begin{align*}
\iint\limits_{C_1}e^{-x^2-y^2}\,dA&=\int_0^{\frac{1}{2}\pi}\int_0^Re^{-r^2}\,r\,dr\,d\theta\\
&=\frac{1}{2}\pi\bigg[-\frac{1}{2}e^{-r^2}\bigg]_{r=0}^R\\
&=\frac{1}{4}\pi\left(1-e^{-R^2}\right) 
\end{align*}
 
and

\begin{align*}
\iint\limits_{C_2}e^{-x^2-y^2}\,dA&=\int_0^{\frac{1}{2}\pi}\int_0^{R\sqrt{2}}e^{-r^2}\,r\,dr\,d\theta\\
&=\frac{1}{2}\pi\bigg[-\frac{1}{2}e^{-r^2}\bigg]_{r=0}^{R\sqrt{2}}\\
&=\frac{1}{4}\pi\left(1-e^{-2R^2}\right).
\end{align*}
 
Finally we take the limit $R\to\infty$ and use the squeeze theorem to obtain that 

$$
\lim\limits_{R\to\infty}\iint\limits_{[0,R]\times[0,R]}e^{-x^2-y^2}\,dA=\frac{1}{4}\pi.
$$ 

Hence we have

$$
\left(\int_0^{\infty}e^{-x^2}\,dx\right)^2=\lim\limits_{R\to\infty}\left(\int_0^Re^{-x^2}\,dx\right)^2=\frac{1}{4}\pi,
$$ 
 
which implies that $\displaystyle\int_0^{\infty}e^{-x^2}\,dx=\tfrac{1}{2}\sqrt{\pi}$. This proves that $\displaystyle\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt{\pi}$.
:::::

## General coordinate transformations

We consider one-to-one transformations

$$
T(u,v)=(x,y):\quad\left\{\begin{array}{l}x=g(u,v)\\y=h(u,v)\end{array}\right.\quad\longleftrightarrow\quad
T^{-1}(x,y)=(u,v):\quad\left\{\begin{array}{l}u=G(x,y)\\v=H(x,y).\end{array}\right.
$$

```{figure} Images/transformation1.png
---
width: 75%
name: transformation1
align: center
---
A one-to-one transformation.
```

:::::{prf:example}
:label: Ex:MultivariableIntegration:GeneralTransformationsExample1

Consider the transformation given by $\left\{\begin{array}{l}x=u^2-v^2\\y=2uv.\end{array}\right.$

```{figure} Images/transformation2.png
---
width: 50%
name: transformation2
align: left
---
The image of the square $[0,1]\times[0,1]$.
```

We study the image of the square $S=[0,1]\times[0,1]=\{(u,v)\,|\,0\leq u\leq1,\;0\leq v\leq1\}$.

We start by considering the sides $S_1$, $S_2$, $S_3$ and $S_4$ of the square $S$.

$S_1:\;0\leq u\leq 1,\;v=0$. This implies that $x=u^2$ and $y=0$. So this corresponds to the line segment $0\leq x\leq1$ and $y=0$.

$S_2:\;u=1,\;0\leq v\leq1$. This implies that $x=1-v^2$ and $y=2v$. So this corresponds to $x=1-\frac{1}{4}y^2$ and $0\leq x\leq1$.

$S_3:\;0\leq u\leq1,\;v=1$. This implies that $x=u^2-1$ and $y=2u$. So this corresponds to $x=\frac{1}{4}y^2-1$ and $-1\leq x\leq0$.

$S_4:\;u-0,\;0\leq v\leq1$. This implies that $x=-v^2$ and $y=0$. So this corresponds to the line segment $-1\leq x\leq0$ and $y=0$.

This leads to the picture at the left.
:::::

Consider the one-to-one transformation

$$
T(u,v)=(x,y):\quad\left\{\begin{array}{l}x=g(u,v)\\y=h(u,v)\end{array}\right.\quad\longleftrightarrow\quad
\mathbf{r}(u,v)=g(u,v)\,\mathbf{i}+h(u,v)\,\mathbf{j}:\quad
\left\{\begin{array}{l}\displaystyle\mathbf{r}_u=\frac{\partial x}{\partial u}\,\mathbf{i}+\frac{\partial y}{\partial u}\,\mathbf{j}\\
\displaystyle\mathbf{r}_v=\frac{\partial x}{\partial v}\,\mathbf{i}+\frac{\partial y}{\partial v}\,\mathbf{j}.\end{array}\right.
$$

```{figure} Images/transformation3.png
---
width: 75%
name: transformation3
align: center
---
A one-to-one transformation.
```

We can approximate the image region $R=T(S)$ by a parallelogram determined by the secant vectors

$$
\mathbf{r}(u_0+\Delta u,v_0)-\mathbf{r}(u_0,v_0)\quad\textrm{and}\quad\mathbf{r}(u_0,v_0+\Delta v)-\mathbf{r}(u_0,v_0).
$$

However, we have

$$
\mathbf{r}_u=\lim\limits_{\Delta u\to 0}\frac{\mathbf{r}(u_0+\Delta u,v_0)-\mathbf{r}(u_0,v_0)}{\Delta u},
$$ 
 
which implies that

$$
\mathbf{r}(u_0+\Delta u,v_0)-\mathbf{r}(u_0,v_0)\approx\Delta u\,\mathbf{r}_u.
$$

Similarly, we have

$$
\mathbf{r}(u_0,v_0+\Delta v)-\mathbf{r}(u_0,v_0)\approx\Delta v\,\mathbf{r}_v.
$$

This means that we can approximate $R$ by a parallelogram determined by the vectors $\Delta u\,\mathbf{r}_u$ and $\Delta v\,\mathbf{r}_v$. Therefore we can approximate the area of $R$ by the area of this parallelogram, which is

$$
\left|(\Delta u\,\mathbf{r}_u)\times(\Delta v\,\mathbf{r}_v)\right|=\left|\mathbf{r}_u\times\mathbf{r}_v\right|\,\Delta u\,\Delta v.
$$

Now, if $\mathbf{r}_u=\langle\displaystyle\frac{\partial x}{\partial u},\frac{\partial y}{\partial u},0\rangle$ and $\mathbf{r}_v=\langle\displaystyle\frac{\partial x}{\partial v},\frac{\partial y}{\partial v},0\rangle$, then

$$
\mathbf{r}_u\times\mathbf{r}_v=\langle0,0,\begin{vmatrix}\displaystyle\frac{\partial x}{\partial u} & \displaystyle\frac{\partial y}{\partial u}\\
\displaystyle\frac{\partial x}{\partial v} & \displaystyle\frac{\partial y}{\partial v}\end{vmatrix}\rangle
=\langle0,0,\begin{vmatrix}\displaystyle\frac{\partial x}{\partial u} & \displaystyle\frac{\partial x}{\partial v}\\
\displaystyle\frac{\partial y}{\partial u} & \displaystyle\frac{\partial y}{\partial v}\end{vmatrix}\rangle.
$$

So, $\|\mathbf{r}_u\times\mathbf{r}_v\|$ equals the *absolute value* of the *determinant*.

:::::{prf:definition}
:label: Def:MultivariableIntegration:JacobianR2

The **Jacobian** of the transformation $T$ given by 

$$
T(u,v)=(x,y):\quad\left\{\begin{array}{l}x=g(u,v)\\y=h(u,v)\end{array}\right.
$$

is

$$
\frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}\displaystyle\frac{\partial x}{\partial u} & \displaystyle\frac{\partial x}{\partial v}\\
\displaystyle\frac{\partial y}{\partial u} & \displaystyle\frac{\partial y}{\partial v}\end{vmatrix}=\frac{\partial x}{\partial u}\,\frac{\partial y}{\partial v}-\frac{\partial x}{\partial v}\frac{\partial y}{\partial u}.
$$ 

::::: 
 
:::{note} 
An approximation of the area $\Delta A$ of $R$ now is: $\displaystyle\Delta A\approx\left|\frac{\partial(x,y)}{\partial(u,v)}\right|\,\Delta u\,\Delta v$.
:::

:::::{prf:theorem}
:label: Thm:MultivariableIntegration:GeneralTransformation

Suppose that $T$ is a one-to-one transformation whose Jacobian is nonzero and that $T$ maps a region $S$ in the $uv$-plane onto a region $R$ in the $xy$-plane. Suppose that $f$ is continuous on 
$R$ and that $R$ and $S$ are plane regions that are either $x$-simple or $y$-simple. Then:

$$
\iint\limits_Rf(x,y)\,dA=\iint\limits_Sf(x(u,v),y(u,v))\left|\frac{\partial(x,y)}{\partial(u,v)}\right|\,du\,dv.
$$

:::::

:::::{example}
:label: Ex:MultivariableIntegration:GeneralTransformationsExample2

We use that change of variables $\left\{\begin{array}{l}x=u^2-v^2\\y=2uv\end{array}\right.$ to evaluate the integral $\displaystyle\iint\limits_Ry\,dA$, where $R$ is the region bounded by the 
$x$-axis and the parabolas $y^2=4-4x$ and $y^2=4+4x$ with $y\geq0$.

```{figure} Images/transformation2.png
---
width: 50%
name: transformation2
align: right
---
The image of the square $[0,1]\times[0,1]$.
```

We have seen that $R=T(S)$, where $S=[0,1]\times[0,1]$ in the $uv$-plane. Now we have

$$
\frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}\displaystyle\frac{\partial x}{\partial u} & \displaystyle\frac{\partial x}{\partial v}\\
\displaystyle\frac{\partial y}{\partial u} & \displaystyle\frac{\partial y}{\partial v}\end{vmatrix}
=\begin{vmatrix}2u & -2v\\2v & 2u\end{vmatrix}=4(u^2+v^2).
$$

Hence we have

\begin{align*}
\iint\limits_Ry\,dA&=\iint\limits_S2uv\left|\frac{\partial(x,y)}{\partial(u,v)}\right|\,du\,dv
=\int_0^1\int_0^12uv\cdot4(u^2+v^2)\,du\,dv\\
&=8\int_0^1\int_0^1(u^3v+uv^3)\,du\,dv=8\int_0^1\bigg[\frac{1}{4}u^4v+\frac{1}{2}u^2v^3\bigg]_{u=0}^1\,dv\\
&=\int_0^1\left(2v+4v^3\right)\,dv=\bigg[v^2+v^4\bigg]_{v=0}^1=2.
\end{align*}

:::::

:::::{example}
:label: Ex:MultivariableIntegration:GeneralTransformationsExample3

```{figure} Images/transformation4.png
---
width: 50%
name: transformation4
align: left
---
The region $S$ in the $uv$-plane and the region $R$ in the $xy$-plane.
```

We evaluate the integral $\displaystyle\iint\limits_Re^{(x+y)/(x-y)}\,dA$, where $R$ is the trapezoidal region with vertices $(1,0)$, $(2,0)$, $(0,-2)$ and $(0,-1)$.

Consider the change of variables $u=x+y$ and $v=x-y$, which implies that $x=\frac{1}{2}(u+v)$ and $y=\frac{1}{2}(u-v)$. Then the Jacobian is

$$
\frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}\displaystyle\frac{\partial x}{\partial u} & \displaystyle\frac{\partial x}{\partial v}\\
\displaystyle\frac{\partial y}{\partial u} & \displaystyle\frac{\partial y}{\partial v}\end{vmatrix}
=\begin{vmatrix}\frac{1}{2} & \frac{1}{2}\\\frac{1}{2} & -\frac{1}{2}\end{vmatrix}=-\frac{1}{2}.
$$

Note that

$$
\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}\displaystyle\frac{\partial u}{\partial x} & \displaystyle\frac{\partial u}{\partial y}\\
\displaystyle\frac{\partial v}{\partial x} & \displaystyle\frac{\partial v}{\partial y}\end{vmatrix}
=\begin{vmatrix}1 & 1\\1 & -1\end{vmatrix}=-2
$$

which implies that

$$
\frac{\partial(x,y)}{\partial(u,v)}=\frac{1}{\displaystyle\frac{\partial(u,v)}{\partial(x,y)}}=-\frac{1}{2}.
$$

To find the region $S$ in the $uv$-plane corresponding to $R$, we note that the sides of $R$ lie on the lines $y=0$, $x-y=2$, $x=0$ and $x-y=1$. These lines correspond to $u=v$, $v=2$, $u=-v$ and $v=1$ respectively. This implies that $S$ is the trapezoidal region with vertices $(1,1)$, $(2,2)$, $(-2,2)$ and $(-1,1)$:

$$
S=\{(u,v)\,|\,1\leq v\leq2,\;-v\leq u\leq v\}.
$$

Hence we have

\begin{align*}
\iint\limits_Re^{(x+y)/(x-y)}\,dA&=\iint\limits_Se^{u/v}\left|\frac{\partial(x,y)}{\partial(u,v)}\right|\,du\,dv
=\int_1^2\int_{-v}^ve^{u/v}\cdot\frac{1}{2}\,du\,dv=\frac{1}{2}\int_1^2\bigg[ve^{u/v}\bigg]_{u=-v}^v\,dv\\
&=\frac{1}{2}\int_1^2\left(e-e^{-1}\right)v\,dv
=\frac{1}{2}\left(e-e^{-1}\right)\bigg[\frac{1}{2}v^2\bigg]_{v=1}^2=\frac{3}{4}\left(e-e^{-1}\right).
\end{align*}

:::::

## Jacobian for polar coordinates

```{figure} Images/transformation5.png
---
width: 50%
name: transformation5
align: right
---
Polar coordinates.
```

In the case of polar coordinates we have: $\displaystyle T(r,\theta)=(x,y):\quad\left\{\begin{array}{l}x=r\cos(\theta)\\
y=r\sin(\theta).\end{array}\right.$ 
 

The Jacobian of $T$ is

$$ 
\frac{\partial(x,y)}{\partial(r,\theta)}=\begin{vmatrix}\displaystyle\frac{\partial x}{\partial r} & \displaystyle\frac{\partial x}{\partial\theta}\\
\displaystyle\frac{\partial y}{\partial r} & \displaystyle\frac{\partial y}{\partial\theta}\end{vmatrix}
=\left|\begin{array}{cc}\cos(\theta) & -\sin(\theta)\\r\sin(\theta) & r\cos(\theta)\end{array}\right|=r>0. 
$$ 
 
Note that the rectangle

$$
S=\{(r,\theta)\,|\,a\leq r\leq b,\;\alpha\leq\theta\leq\beta\}
$$

in the $r\theta$-plane corresponds to the polar rectangle

$$
R=\{(r\cos(\theta),r\sin(\theta))\,|\,a\leq r\leq b,\;\alpha\leq\theta\leq\beta\}
$$

in the $xy$-plane. Hence we have

\begin{align*}
\iint\limits_Rf(x,y)\,dA&=\iint\limits_Sf(r\cos(\theta),r\sin(\theta))\left|\frac{\partial(x,y)}{\partial(r,\theta)}\right|\,dr\,d\theta\\
&=\int_{\alpha}^{\beta}\int_a^bf(r\cos(\theta),r\sin(\theta))\,r\,dr\,d\theta.
\end{align*} 	 
 