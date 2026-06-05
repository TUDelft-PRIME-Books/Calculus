(Sec:MultivariableIntegration:TransformationsR3)=

# Coordinate transformations in $\mathbb{R}^3$

- Triple integrals using general coordinate transforms
  - Triple integral in cylindrical coordinates as an example.
  - Triple integral in spherical coordinates as an example.
  - Add theorem on Jacobian for cylindrical and spherical coordinates.

In {numref}`Sec:MultivariableIntegration:TransformationsR2` we have seen the polar coordinates, which are helpful in evaluating double integrals over (parts of ) circular regions. In triple integrals these are usual called _cylindrical coordinates_.

## Cylindrical coordinates

For instance, consider

$$
\left\{\begin{array}{l}x=r\cos(\theta)\\y=r\sin(\theta)\\z=z\end{array}\right.\quad\Longrightarrow\quad r^2=x^2+y^2\quad\textrm{and}\quad\tan(\theta)=\frac{y}{x}.
$$

```{figure} Images/cylindrical.png
---
width: 50%
name: cylindrical
align: center
---
Cylindrical coordinates.
```

The volume element equals the area of the polar rectangle multiplied by the height: $dV=r\,dz\,dr\,d\theta$.

```{figure} Images/volume1.png
---
width: 50%
name: volume1
align: center
---
The volume of a cylindrical box.
```

Suppose that $E$ is a $z$-simple region whose projection $D$ onto the $xy$-plane is conveniently described in polar coordinates. In particular, suppose that $f$ is continuous and

$$
E=\{(x,y,z)\,|\,(x,y)\in D,\;u_1(x,y)\leq z\leq u_2(x,y)\},
$$

where $D$ is given in polar coordinates by

$$
D=\{(r\cos(\theta),r\sin(\theta))\,|\,\alpha\leq\theta\leq\beta,\;h_1(\theta)\leq r\leq h_2(\theta)\}.
$$

Then we have

$$
\iiint\limits_Ef(x,y,z)\,dV=\int_{\alpha}^{\beta}\int_{h_1(\theta)}^{h_2(\theta)}\int_{u_1(r\cos(\theta),r\sin(\theta))}^{u_2(r\cos(\theta),r\sin(\theta))}
f(r\cos(\theta),r\sin(\theta),z)\,r\,dz\,dr\,d\theta.
$$

## Spherical coordinates

$$
\left\{\begin{array}{l}x=\rho\sin(\phi)\cos(\theta)\\y=\rho\sin(\phi)\sin(\theta)\\z=\rho\cos(\phi)\end{array}\right.\quad\Longrightarrow\quad \rho^2=x^2+y^2+z^2.
$$

```{figure} Images/spherical.png
---
width: 50%
name: spherical
align: center
---
Spherical coordinates.
```

The volume element equals: $dV=\rho^2\sin(\phi)\,d\rho\,d\phi\,d\theta$.

```{figure} Images/volume2.png
---
width: 50%
name: volume2
align: center
---
The volume of a spherical wedge.
```

The counterpart of a rectangular box in spherical coordinates is a spherical wedge given by $a\leq\rho\leq b$, $\alpha\leq\theta\leq\beta$ and $\gamma\leq\phi\leq\delta$, where $a\geq0$, $\beta-\alpha\leq2\pi$ and $\delta-\gamma\leq\pi$. The volume of such a wedge is approximately equal to that of a box with sides of length $d\rho$, $\rho\,d\phi$ and $r\,d\theta$, where $r=\rho\sin(\phi)$ denotes the distance to the $z$-axis, which is $d\rho\cdot\rho\,d\phi\cdot\rho\sin(\phi)\,d\theta=\rho^2\sin(\phi)\,d\rho\,d\phi\,d\theta$.

Suppose that

$$
E=\{(\rho\sin(\phi)\cos(\theta),\rho\sin(\phi)\sin(\theta),\rho\cos(\phi)\,|\,\alpha\leq\theta\leq\beta,\;\gamma\leq\phi\leq\delta,\;u_1(\phi,\theta))\leq\rho\leq u_2(\phi,\theta)\},
$$

then we have:

$$
\iiint\limits_Ef(x,y,z)\,dV=\int_{\alpha}^{\beta}\int_{\gamma}^{\delta}\int_{u_1(\phi,\theta)}^{u_2(\phi,\theta)}
f(\rho\sin(\phi)\cos(\theta),\rho\sin(\phi)\sin(\theta),\rho\cos(\phi))\,\rho^2\sin(\phi)\,d\rho\,d\phi\,d\theta.
$$

## General coordinate transformations

Similar to the case of double integrals we define the **Jacobian** of the transformation $T$ given by

$$
T(u,v,w)=(x,y,z):\quad\left\{\begin{array}{l}x=g(u,v,w)\\y=h(u,v,w)\\z=k(u,v,w)\end{array}\right.
$$

by

$$
\frac{\partial(x,y,z)}{\partial(u,v,w)}=\begin{vmatrix}\displaystyle\frac{\partial x}{\partial u} & \displaystyle\frac{\partial x}{\partial v} & \displaystyle\frac{\partial x}{\partial w}\\
\displaystyle\frac{\partial y}{\partial u} & \displaystyle\frac{\partial y}{\partial v} & \displaystyle\frac{\partial y}{\partial w}\\
\displaystyle\frac{\partial z}{\partial u} & \displaystyle\frac{\partial z}{\partial v} & \displaystyle\frac{\partial z}{\partial w}\end{vmatrix}.
$$

Such a determinant is defined as a scalar triple product (see also the course on Linear Algebra for more details):

$$
\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix}
=\begin{vmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{vmatrix}
=\det(\mathbf{a},\mathbf{b},\mathbf{c})=\mathbf{a}\cdot\left(\mathbf{b}\times\mathbf{c}\right).
$$ 
 
Then we have

$$
\iiint\limits_Rf(x,y,z)\,dV=\iiint\limits_Sf(x(u,v,w),y(u,v,w),z(u,v,w))\left|\frac{\partial(x,y,z)}{\partial(u,v,w)}\right|\,du\,dv\,dw.
$$

### Cylindrical coordinates

In the case of cylindrical coordinates we have: $\displaystyle T(r,\theta,z)=(x,y,z):\quad
\left\{\begin{array}{l}x=r\cos(\theta)\\y=r\sin(\theta)\\z=z.\end{array}\right.$

The Jacobian of $T$ is (see the course on Linear Algebra for details about the computation)

\begin{align*}
\frac{\partial(x,y,z)}{\partial(r,\theta,z)}&=\begin{vmatrix}\displaystyle\frac{\partial x}{\partial r} & \displaystyle\frac{\partial x}{\partial\theta} & \displaystyle\frac{\partial x}{\partial z}\\
\displaystyle\frac{\partial y}{\partial r} & \displaystyle\frac{\partial y}{\partial\theta} & \displaystyle\frac{\partial y}{\partial z}\\
\displaystyle\frac{\partial z}{\partial r} & \displaystyle\frac{\partial z}{\partial\theta} & \displaystyle\frac{\partial z}{\partial z}\end{vmatrix}\\
&=\begin{vmatrix}\cos(\theta) & -\sin(\theta) & 0\\r\sin(\theta) & r\cos(\theta) & 0\\0 & 0 & 1\end{vmatrix}\\
&=\begin{vmatrix}\cos(\theta) & -\sin(\theta)\\r\sin(\theta) & r\cos(\theta)\end{vmatrix}=r>0.
\end{align*}

### Spherical coordinates

In the case of spherical coordinates we have: $\displaystyle T(\rho,\phi,\theta)=(x,y,z):\quad
\left\{\begin{array}{l}x=\rho\sin(\phi)\cos(\theta)\\y=\rho\sin(\phi)\sin(\theta)\\z=\rho\cos(\phi).\end{array}\right.$ 

The Jacobian of $T$ is (see the course on Linear Algebra for details about the computation)

\begin{align*}
\frac{\partial(x,y,z)}{\partial(\rho,\phi,\theta)}&=\begin{vmatrix}\displaystyle\frac{\partial x}{\partial\rho} & \displaystyle\frac{\partial x}{\partial\phi} & \displaystyle\frac{\partial x}{\partial\theta}\\
\displaystyle\frac{\partial y}{\partial\rho} & \displaystyle\frac{\partial y}{\partial\phi} & \displaystyle\frac{\partial y}{\partial\theta}\\
\displaystyle\frac{\partial z}{\partial\rho} & \displaystyle\frac{\partial z}{\partial\phi} & \displaystyle\frac{\partial z}{\partial\theta}\end{vmatrix}\\
&=\begin{vmatrix}\sin(\phi)\cos(\theta) & \rho\cos(\phi)\cos(\theta) & -\rho\sin(\phi)\sin(\theta)\\
\sin(\phi)\sin(\theta) & \rho\cos(\phi)\sin(\theta) & \rho\sin(\phi)\cos(\theta)\\\cos(\phi) & -\rho\sin(\phi) & 0\end{vmatrix}\\
&=\cos(\phi)\begin{vmatrix}\rho\cos(\phi)\cos(\theta) & -\rho\sin(\phi)\sin(\theta)\\
\rho\cos(\phi)\sin(\theta) & \rho\sin(\phi)\cos(\theta)\end{vmatrix}\\
&{}\quad{}+\rho\sin(\phi)\begin{vmatrix}\sin(\phi)\cos(\theta) & -\rho\sin(\phi)\sin(\theta)\\
\sin(\phi)\sin(\theta) & \rho\sin(\phi)\cos(\theta)\end{vmatrix}\\
&=\cos(\phi)\left(\rho^2\sin(\phi)\cos(\phi)\cos^2(\theta)+\rho^2\sin(\phi)\cos(\phi)\sin^2(\theta)\right)\\
&{}\quad{}+\rho\sin(\phi)\left(\rho\sin^2(\phi)\cos^2(\theta)+\rho\sin^2(\phi)\sin^2(\theta)\right)\\
&=\cos(\phi)\cdot\rho^2\sin(\phi)\cos(\phi)+\rho\sin(\phi)\cdot\rho\sin^2(\phi)\\
&=\rho^2\sin(\phi)\left(\cos^2(\phi)+\sin^2(\phi)\right)\\
&=\rho^2\sin(\phi)>0.
\end{align*}
