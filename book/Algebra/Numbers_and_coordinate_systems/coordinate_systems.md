(Sec:CoordinateSystems)=
# Coordinate systems

- Cartesian coordinates in $\mathbb{R}^2$ and $\mathbb{R}^3$
- Polar coordinates in $\mathbb{R}^2$
- Cylindrical coordinates in $\mathbb{R}^3$:
  - Not only discuss with $z$ as height, but also $x$ or $y$ as height of the cylinder.
- Spherical coordinates in $\mathbb{R}^3$
- General coordinate systems in $\mathbb{R}^2$ and $\mathbb{R}^3$

## Cartesian coordinates in $\mathbb{R}^2$ and $\mathbb{R}^3$

(Sec:CoordinateSystems:PolarCoordinates)=
## Polar coordinates in $\mathbb{R}^2$

Instead of using the Cartesian coordinates $x$ and $y$ to denote a point $(x,y)$ in $\mathbb{R^2}$, there are more ways to fix a point in $\mathbb{R}^2$. One way is to use **polar coordinates**.

Note that a point $P=(x,y)\neq(0,0)$ can be fixed by its distance $r$ to the origin and the angle $\theta$ of the line through $P$ and the origin and the positive $x$-axis. See Figure....

Using the {prf:ref}`Pythagorean theorem <Thm:Trigonometry:Pythagoras>` we obtain that

$$
r=\sqrt{x^2+y^2}.
$$

Furtermore, we find that

$$
x=r\cos(\theta)\quad\text{and}\quad y=r\sin(\theta).
$$

(Sec:CoordinateSystems:CylindricalCoordinates)=
## Cylindrical coordinates in $\mathbb{R}^3$

Polar coordinates in $\mathbb{R}^3$ are usually called **cylindrical coordinates**. If one of the Cartesian coordinates is unchanged, we might apply *polar coordinates* to the other two. For instance, we have

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

(Sec:CoordinateSystems:SphericalCoordinates)=
## Spherical coordinates in $\mathbb{R}^3$

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

## General coordinate systems in $\mathbb{R}^2$ and $\mathbb{R}^3$
