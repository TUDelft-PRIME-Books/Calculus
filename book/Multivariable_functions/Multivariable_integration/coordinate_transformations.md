# Coordinate transformations

- Double integral using general coordinate transform
  - Double integral in polar coordinates as an example.
  - Add theorem on Jacobian for polar coordinates.
- Triple integrals using general coordinate transforms
  - Triple integral in cylindrical coordinates as an example.
  - Triple integral in spherical coordinates as an example.
  - Add theorem on Jacobian for cylindrical and spherical coordinates.
  - Short remark on multiple integrals with 4 or more variables.

## Double integrals in polar coordinates

For regions which are part of a disk, we might use polar coordinates: 

$$
\left\{\begin{array}{l}x=r\cos(\theta)\\[2.5mm]y=r\sin(\theta)\end{array}\right.\quad\Longrightarrow\quad x^2+y^2=r^2.
$$

We start with a **polar rectangle**

$$
R=\{(r\cos(\theta),r\sin(\theta))\,|\,a\leq r\leq b,\;\alpha\leq\theta\leq\beta\}\quad\textrm{with}\quad a\geq0\quad\textrm{and}\quad\beta-\alpha\leq2\pi.
$$

```{figure} Images/polar1.png
---
width: 50%
name: polar1
align: center
---

```

In order to evaluate the double integral $\displaystyle\iint\limits_Rf(x,y)\,dA$ over such a polar rectangle $R$, we divide the interval $[a,b]$ into $m$ subintervals $[r_{i-1},r_i]$ with equal width $\Delta r=(b-a)/m$ and we divide the interval $[\alpha,\beta]$ into $n$ subintervals $[\theta_{j-1},\theta_j]$ of equal width $\Delta\theta=(\beta-\alpha)/n$

```{figure} Images/polar2.png
---
width: 50%
name: polar2
align: center
---

```

Now we consider the polar rectangles

$$
R_{ij}=\{(r\cos(\theta),r\sin(\theta))\,|\,r_{i-1}\leq r\leq r_i,\;\theta_{j-1}\leq\theta\leq\theta_j\}
$$

with area (let: $r_i^*=(r_i+r_{i-1})/2$)

$$ 
\begin{align*}
\Delta A_{ij}&=\frac{1}{2}r_i^2\,\Delta\theta-\frac{1}{2}r_{i-1}^2\,\Delta\theta=\frac{1}{2}(r_i^2-r_{i-1}^2)\,\Delta\theta=\frac{1}{2}(r_i+r_{i-1})(r_i-r_{i-1})\,\Delta\theta\\
&=r_i^*\,\Delta r\,\Delta\theta. 
\end{align*}
$$ 
 
Here we have: $\Delta r=r_i-r_{i-1}$ and $\Delta\theta=\theta_j-\theta_{j-1}$.

It is easier to approximate the area of a polar rectangle. Note that the length of an arc of a circle with radius $r$ and difference of angles $\Delta\theta$ equals $r\,\Delta\theta$. This implies that the area of a polar rectangle is approximately equal to the area of a rectangle with sides $\Delta r$ and $r\,\Delta\theta$, which is: $r\,\Delta r\,\Delta\theta$.

:::::{prf:theorem}
:label: Thm:MultipleIntegrals:PolarCoordinatesRectangle 
If $f$ is continuous on a polar rectangle $R$ given by $0\leq a\leq r\leq b$ and $\alpha\leq\theta\leq\beta$ with $\beta-\alpha\leq2\pi$, then

$$
\iint\limits_Rf(x,y)\,dA=\int_{\alpha}^{\beta}\int_a^bf(r\cos(\theta),r\sin(\theta))\,r\,dr\,d\theta.
$$

:::::

In polar coordinates $\left\{\begin{array}{l}x=r\cos(\theta)\\[2.5mm]y=r\sin(\theta)\end{array}\right.$ the area element equals $dA=r\,dr\,d\theta$.

## Examples

:::{prf:example}
Evaluate $\displaystyle\iint\limits_R(3x+4y^2)\,dA$, where $R$ is the region in the upper half-plane bounded by the circles $x^2+y^2=1$ and $x^2+y^2=4$.

```{figure} Images/polarcoord1.png
---
width: 50%
name: polarcoord1
align: center
---

```

Solution. Note that the region $R=\{(x,y)\,|\,y\geq0,\;1\leq x^2+y^2\leq 4\}$ is described in polar coordinates as

$$
R=\{(r\cos(\theta),r\sin(\theta))\,|\,1\leq r\leq 2,\;0\leq\theta\leq\pi\}.
$$

Hence we have using $\cos(2\theta)=1-2\sin^2(\theta)$:

$$ 	
\begin{align*}
\iint\limits_R(3x+4y^2)\,dA&=\int_0^{\pi}\int_1^2\left(3r\cos(\theta)+4r^2\sin^2(\theta)\right)\,r\,dr\,d\theta\\
&=\int_0^{\pi}\bigg[r^3\cos(\theta)+r^4\sin^2(\theta)\bigg]_{r=1}^2\,d\theta\\
&=\int_0^{\pi}\left(7\cos(\theta)+15\sin^2(\theta)\right)\,d\theta\\
&=\int_0^{\pi}\left(7\cos(\theta)+\frac{15}{2}\left(1-\cos(2\theta)\right)\right)\,d\theta\\
&=\bigg[7\sin(\theta)+\frac{15}{2}\theta-\frac{15}{4}\sin(2\theta)\bigg]_{\theta=0}^{\pi}=\frac{15}{2}\pi.
\end{align*}
$$ 
 
:::

:::{prf:example}
Find the volume of the solid bounded by the plane $z=0$ and the paraboloid $z=1-x^2-y^2$.

```{figure} Images/polarcoord2.png
---
width: 50%
name: polarcoord2
align: center
---

```

Solution. Note that the intersection of the paraboloid and the $xy$-plane ($z=0$) is the circle $x^2+y^2=1$. So, the solid lies under the paraboloid and above the circular disk $D$ given by $x^2+y^2\leq1$. In polar coordinates $D$ is given by

$$
D=\{(r\cos(\theta),r\sin(\theta))\,|\,0\leq r\leq1,\;0\leq\theta\leq2\pi\}.
$$

Hence the volume equals

$$
\begin{align*}
V&=\iint\limits_D(1-x^2-y^2)\,dA=\int_0^{2\pi}\int_0^1(1-r^2)\,r\,dr\,d\theta\\
&=\int_0^{2\pi}d\theta\,\int_0^1(r-r^3)\,dr=2\pi\bigg[\frac{1}{2}r^2-\frac{1}{4}r^4\bigg]_{r=0}^1=\frac{1}{2}\pi.
\end{align*}
$$

:::

## More general regions

:::::{prf:theorem}
:label: Thm:MultipleIntegrals:PolarCoordinatesGeneral 
If $f$ is continuous on a polar region of the form

$$
D=\{(r\cos(\theta),r\sin(\theta))\,|\,\alpha\leq\theta\leq\beta,\;h_1(\theta)\leq r\leq h_2(\theta)\}\
$$

with $\beta-\alpha\leq2\pi$, then

$$
\iint\limits_Df(x,y)\,dA=\int_{\alpha}^{\beta}\int_{h_1(\theta)}^{h_2(\theta)}f(r\cos(\theta),r\sin(\theta))\,r\,dr\,d\theta. 
$$

```{figure} Images/polar3.png
---
width: 50%
name: polar3
align: center
---

```

:::::

## Examples

:::{prf:example}
Use a double integral to find the area of the region $D$ enclosed by one loop of the four-leaved rose $r=\cos(2\theta)$.

```{figure} Images/polarcoord3.png
---
width: 50%
name: polarcoord3
align: center
---

```

Solution. Note that the region $D$ in polar coordinates is given by

$$
D=\{(r\cos(\theta),r\sin(\theta))\,|\,-\textstyle\frac{1}{4}\pi\leq\theta\leq\frac{1}{4}\pi,\;0\leq\theta\leq\cos(2\theta)\}.
$$ 
 
Hence we have using $\cos(2x)=2\cos^2(x)-1$:

$$
\begin{align*}
\textrm{area}(D)&=\iint\limits_D1\,dA=\int_{-\frac{1}{4}\pi}^{\frac{1}{4}\pi}\int_0^{\cos(2\theta)}r\,dr\,d\theta=\int_{-\frac{1}{4}\pi}^{\frac{1}{4}\pi}\bigg[\frac{1}{2}r^2\bigg]_{r=0}^{\cos(2\theta)}\,d\theta\\
&=\frac{1}{2}\int_{-\frac{1}{4}\pi}^{\frac{1}{4}\pi}\cos^2(2\theta)\,d\theta=\frac{1}{4}\int_{-\frac{1}{4}\pi}^{\frac{1}{4}\pi}\left(1+\cos(4\theta)\right)\,d\theta\\
&=\frac{1}{4}\bigg[\theta+\frac{1}{4}\sin(4\theta)\bigg]_{\theta=-\frac{1}{4}\pi}^{\frac{1}{4}\pi}=\frac{1}{8}\pi.
\end{align*}
$$

:::

:::{prf:example}
Use a double integral to find the area of the region $D$ enclosed by one loop of the four-leaved rose $r=\cos(2\theta)$.

```{figure} Images/polarcoord4.png
---
width: 50%
name: polarcoord4
align: left
---

```
```{figure} Images/polarcoord5.png
---
width: 50%
name: polarcoord5
align: right
---

```

Solution. The solid lies above the disk $D$ with boundary circle given by $x^2+y^2=2x$ or equivalently, completing the square, by $(x-1)^2+y^2=1$. In polar coordinates we have $x^2+y^2=r^2$ and $x=r\cos(\theta)$, so this boundary circle becomes $r^2=2r\cos(\theta)$ or $r=2\cos(\theta)$. Hence we have:

$$
D=\{(r\cos(\theta),r\sin(\theta))\,|\,-\textstyle\frac{1}{2}\pi\leq\theta\leq\frac{1}{2}\pi,\;0\leq r\leq2\cos(\theta)\}.
$$ 
 
Hence the volume equals using $\cos(2\theta)=2\cos^2(\theta)-1$

$$
\begin{align*}
V&=\iint\limits_D(x^2+y^2)\,dA=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\int_0^{2\cos(\theta)}r^2\,r\,dr\,d\theta=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\bigg[\frac{1}{4}r^4\bigg]_{r=0}^{2\cos(\theta)}\,d\theta\\
&=4\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\cos^4(\theta)\,d\theta=8\int_0^{\frac{1}{2}\pi}\cos^4(\theta)\,d\theta=8\int_0^{\frac{1}{2}\pi}\left(\frac{1+\cos(2\theta)}{2}\right)^2\,d\theta\\
&=2\int_0^{\frac{1}{2}\pi}\left(1+2\cos(2\theta)+\cos^2(2\theta)\right)\,d\theta\\
&=2\int_0^{\frac{1}{2}\pi}\left(1+2\cos(2\theta)+\frac{1}{2}\left(1+\cos(4\theta)\right)\right)\,d\theta\\
&=\bigg[3\theta+2\sin(2\theta)+\frac{1}{2}\sin(4\theta)\bigg]_{\theta=0}^{\frac{1}{2}\pi}=\frac{3}{2}\pi.
\end{align*}
$$

:::

:::{prf:example}
A swimming pool is circular with a diameter of $10$ m. The depth is constant along east-west lines and increases linearly from $1$ m at the south end to $2$ m at the north end. Find the volume of water in the pool.

```{figure} Images/pool.png
---
width: 50%
name: pool
align: center
---

```

Solution. Note that the linear function $f(x)$ such that $f(-5)=1$ and $f(5)=2$ is given by 

$$
f(x)=\displaystyle\frac{1}{10}x+\frac{3}{2}=\frac{x+15}{10}.
$$ 
 
Then the volume is given by 

$$
V=\iint\limits_{x^2+y^2\leq25}\frac{x+15}{10}\,dA.
$$

Using polar coordinates we obtain

$$
\begin{align*}
V&=\int_0^{2\pi}\int_0^5\frac{r\cos(\theta)+15}{10}\,r\,dr\,d\theta
=\int_0^{2\pi}\bigg[\frac{1}{30}r^3\cos(\theta)+\frac{3}{4}r^2\bigg]_{r=0}^5\,d\theta\\
&=\int_0^{2\pi}\left(\frac{25}{6}\cos(\theta)+\frac{75}{4}\right)\,d\theta=0+\frac{75}{4}\cdot2\pi=\frac{75}{2}\pi.
\end{align*}
$$

:::
