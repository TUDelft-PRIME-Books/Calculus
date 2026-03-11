# Double integrals

In this section we cover:

- Double integrals
- Riemann sums
- Repeated integral and Fubini's theorem
- Rules of calculation
- Improper double integrals (discontinuous integrand)
- General regions
- Changing order of integration

## Volumes

In {numref}`Sec:Integration:DefiniteIntegrals` we introduced single integrals by considering the area between the $x$-axis and the graph of a positive function. See {prf:ref}`Def:Integration:DefiniteIntegral`.

Similarly, consider a function $f$ of two variables defined on a closed rectangle

$$
R=[a,b]\times[c,d]=\{(x,y)\,|\,a\leq x\leq b,\;c\leq y\leq d\}
$$

and first suppose that $f(x,y)\geq0$. The graph of $f$ is a surface with equation $z=f(x,y)$.

Let $S$ be the solid that lies above $R$ and under the graph of $f$, that is

$$
S=\{(x,y,z)\in\mathbb{R}^3\,|\,0\leq z\leq f(x,y),\;(x,y)\in R\}.
$$

Now we want to find the volume of $S$.

The first step is to divide the rectangle $R$ into subrectangles. This is accomplished by dividing the interval $[a,b]$ into subintervals $[x_{i-1},x_i]$ of equal width $\Delta x=(b-a)/m$ and dividing the interval $[c,d]$ into subintervals $[y_{j-1},y_j]$ of equal width $\Delta y=(d-c)/n$.

```{figure} Images/rectangle.png
---
width: 75%
name: rectangle
align: center
---
The division of the rectangle $[a,b]\times[c,d]$ into subrectangles.
```

Consider the subrectangles

$$
R_{ij}=[x_{i-1},x_i]\times[y_{j-1},y_j]=\{(x,y)\,|\,x_{i-1}\leq x\leq x_i,\;y_{j-1}\leq y\leq y_j\},
$$

```{figure} Images/riemann1.png
---
width: 50%
name: riemann1
align: right
---
A double Riemann sum.
```

each with area $\Delta A=\Delta x\,\Delta y$. If we choose a *sample point* $(x_{ij}^*,y_{ij}^*)$ in each subrectangle $R_{ij}$, then the volume of $S$ can be approximated by the sum of the volumes of rectangular boxes with height $f(x_{ij}^*,y_{ij}^*)$:

$$
\sum_{i=1}^m\sum_{j=1}^nf(x_{ij}^*,y_{ij}^*)\Delta A.
$$ 
 
This is called a **double Riemann sum**.

:::::{prf:definition}
:label: Def:MultivariableIntegration:DoubleIntegral
The **double integral** of $f$ over the rectangle $R$ is

$$
\iint\limits_Rf(x,y)\,dA=\lim\limits_{m\to\infty}\lim\limits_{n\to\infty}\sum_{i=1}^m\sum_{j=1}^nf(x_{ij}^*,y_{ij}^*)\Delta A.
$$

:::::

```{figure} Images/riemann2.png
---
width: 75%
name: riemann2
align: center
---
The limit of a double Riemann sum.
```

## Fubini's theorem

:::::{prf:theorem}
:label: Thm:MultivariableIntegration:Fubini
If $f$ is continuous on the rectangle

$$
R=[a,b]\times[c,d]=\{(x,y)\,|\,a\leq x\leq b,\;c\leq y\leq d\},
$$

then we have:

$$
\iint\limits_Rf(x,y)\,dA=\int_a^b\int_c^df(x,y)\,dy\,dx=\int_c^d\int_a^bf(x,y)\,dx\,dy.
$$
 
More generally, this is true if we assume that $f$ is bounded on $R$, $f$ is discontinuous only on a finite number of smooth curves, and the iterated integrals exist.
:::::

:::::{prf:example}
Evaluate $\displaystyle\iint\limits_R(x-3y^2)\,dA$, where $R=[0,2]\times[1,2]$.

Solution. We have

$$
\begin{align*}
\iint\limits_R(x-3y^2)\,dA&=\int_0^2\int_1^2(x-3y^2)\,dy\,dx=\int_0^2\bigg[xy-y^3\bigg]_{y=1}^2\,dx\\
&=\int_0^2(x-7)\,dx=\bigg[\frac{1}{2}x^2-7x\bigg]_{x=0}^2=-12
\end{align*}
$$

and

$$
\begin{align*}
\iint\limits_R(x-3y^2)\,dA&=\int_1^2\int_0^2(x-3y^2)\,dx\,dy=\int_1^2\bigg[\frac{1}{2}x^2-3xy^2\bigg]_{x=0}^2\,dy\\
&=\int_1^2\left(2-6y^2\right)\,dy=\bigg[2y-2y^3\bigg]_{y=1}^2=-12.
\end{align*}
$$

:::::

:::::{prf:example}
Evaluate $\displaystyle\iint\limits_Ry\sin(xy)\,dA$, where $R=[1,2]\times[0,\pi]$.

Solution. We have

$$
\begin{align*}
\iint\limits_Ry\sin(xy)\,dA&=\int_0^{\pi}\int_1^2y\sin(xy)\,dx\,dy=\int_0^{\pi}\bigg[-\cos(xy)\bigg]_{x=1}^2\,dy\\
&=\int_0^{\pi}\left(\cos(x)-\cos(2x)\right)\,dx=\bigg[\sin(x)-\frac{1}{2}\sin(2x)\bigg]_{x=0}^{\pi}\\
&=0.
\end{align*}
$$

Here the other order is much more difficult. Using integration by parts we have

$$ 
\begin{align*}
\int y\sin(xy)\,dy&=-\frac{1}{x}\int y\,d\cos(xy)=-\frac{y}{x}\cos(xy)+\frac{1}{x}\int\cos(xy)\,dy\\
&=-\frac{y}{x}\cos(xy)+\frac{1}{x^2}\sin(xy)+C.
\end{align*}
$$ 
 
Hence we have:

$$ 
\begin{align*}
\iint\limits_Ry\sin(xy)\,dA&=\int_1^2\int_0^{\pi}y\sin(xy)\,dy\,dx\\
&=\int_1^2\bigg[-\frac{y}{x}\cos(xy)+\frac{1}{x^2}\sin(xy)\bigg]_{y=0}^{\pi}\\
&=\int_1^2\left(-\frac{\pi}{x}\cos(\pi x)+\frac{1}{x^2}\sin(\pi x)\right)\,dx.
\end{align*}
$$ 
 
Note that $-\displaystyle\frac{1}{x}\sin(\pi x)$ is an antiderivative, since using the chain rule we have: 
 
$$
\displaystyle\frac{d}{dx}\left(-\frac{1}{x}\sin(\pi x)\right)=-\frac{\pi}{x}\cos(\pi x)+\frac{1}{x^2}\sin(\pi x).
$$ 
 
Hence:

$$
\begin{align*}
\iint\limits_Ry\sin(xy)\,dA&=\int_1^2\int_0^{\pi}y\sin(xy)\,dy\,dx\\
&=\int_1^2\left(-\frac{\pi}{x}\cos(\pi x)+\frac{1}{x^2}\sin(\pi x)\right)\,dx\\
&=\bigg[-\frac{1}{x}\sin(\pi x)\bigg]_{x=1}^2=\sin(\pi)-\frac{1}{2}\sin(2\pi)=0.
\end{align*}
$$

:::::

## Average value

The average value of a function $f$ of one variable defined on an interval $[a,b]$ is

$$
\frac{1}{b-a}\int_a^bf(x)\,dx.
$$

Similarly, we have: the average value of a function $f$ of two variables defined on a rectangle $R$ is 

$$
\frac{1}{\text{area}(R)}\iint\limits_Rf(x,y)\,dA.
$$

## Catalan's constant

Earlier we considered Catalan's constant $G$ which is defined as the sum of the series 

$$
\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}.
$$

We obtained several (integral) representations for $G$, such as: $\displaystyle\int_0^1\frac{\arctan(x)}{x}\,dx=G$.

Now this can be used to prove a nice representation as a "double integral": 

$$
\int_0^1\int_0^1\frac{dx\,dy}{1+x^2y^2}=G.
$$ 

The proof is straightforward:

$$
\begin{align*}
\int_0^1\int_0^1\frac{dx\,dy}{1+x^2y^2}&=\int_0^1\int_0^1\frac{dy\,dx}{1+x^2y^2}=\int_0^1\bigg[\frac{\arctan(xy)}{x}\bigg]_{y=0}^1\,dx\\
&=\int_0^1\frac{\arctan(x)}{x}\,dx=G.
\end{align*}
$$ 
 
Alternatively, we might use $\displaystyle\frac{1}{1-t}=\sum_{n=0}^{\infty}t^n$ for $|t|<1$ to find that

$$
\begin{align*}
\int_0^1\int_0^1\frac{dx\,dy}{1+x^2y^2}&=\sum_{n=0}^{\infty}(-1)^n\int_0^1\int_0^1(xy)^{2n}\,dx\,dy
=\sum_{n=0}^{\infty}(-1)^n\left(\int_0^1t^{2n}\,dt\right)^2\\
&=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}=G.
\end{align*}
$$ 

## Double integrals over general regions

Suppose that $D$ is a bounded region, which can be enclosed in a rectangular region $R$:

```{figure} Images/region.png
---
width: 75%
name: region
align: center
---
A general region in $\mathbb{R}^2$.
```

Now we define a new function $F$ with domain $R$ by:

$$
F(x,y)=\left\{\begin{array}{ll}f(x,y),&(x,y)\in D\\[2.5mm]0,&(x,y)\notin D.\end{array}\right.
$$
 
If $f$ is integrable over $R$, then we define the integral of $f$ over $D$ by:

$$
\iint\limits_Df(x,y)\,dA=\iint\limits_RF(x,y)\,dA.
$$  
 
```{figure} Images/graph1.png
---
width: 25%
name: graph
align: left
---
The graph of $f$.
```

```{figure} Images/graph2.png
---
width: 25%
name: graph
align: right
---
The graph of $F$.
```

## $x$-simple regions

A region $D$ in $\mathbb{R}^2$ is called **$x$-simple** if it lies between the graphs of two continuous functions of $x$, that is:

$$
D=\{(x,y)\,|\,a\leq x\leq b,\;g_1(x)\leq y\leq g_2(x)\},
$$

where $g_1$ and $g_2$ are continuous functions on the interval $[a,b]$.

```{figure} Images/region1a.png
---
width: 25%
name: region1a
align: left
---

```

```{figure} Images/region1b.png
---
width: 25%
name: region1b
align: center
---

```

```{figure} Images/region1c.png
---
width: 25%
name: region1c
align: right
---

```

```{figure} Images/region1d.png
---
width: 25%
name: region1d
align: right
---

```

If $f$ is continuous on a *$x$-simple* region $D$, that is

$$
D=\{(x,y)\,|\,a\leq x\leq b,\;g_1(x)\leq y\leq g_2(x)\},
$$

then

$$
\iint\limits_Df(x,y)\,dA=\int_a^b\int_{g_1(x)}^{g_2(x)}f(x,y)\,dy\,dx.
$$ 

## $y$-simple regions

```{figure} Images/region2a.png
---
width: 25%
name: region2a
align: left
---

```

```{figure} Images/region2b.png
---
width: 25%
name: region2b
align: left
---

```

A region $D$ in $\mathbb{R}^2$ is called **$y$-simple** if it lies between the graphs of two continuous functions of $y$, that is:

$$
D=\{(x,y)\,|\,c\leq y\leq d,\;h_1(y)\leq x\leq h_2(y)\},
$$

where $h_1$ and $h_2$ are continuous functions on the interval $[c,d]$.

If $f$ is continuous on a *$y$-simple* region $D$, that is

$$
D=\{(x,y)\,|\,c\leq y\leq d,\;h_1(y)\leq x\leq h_2(y)\},
$$

then

$$
\iint\limits_Df(x,y)\,dA=\int_c^d\int_{h_1(y)}^{h_2(y)}f(x,y)\,dx\,dy.
$$

## More general regions

```{figure} Images/region3a.png
---
width: 50%
name: region3a
align: left
---

```

If $D=D_1\cup D_2$, then

$$
\iint\limits_Df(x,y)\,dA=\iint\limits_{D_1}f(x,y)\,dA+\iint\limits_{D_2}f(x,y)\,dA.
$$

If $D$ is neither $x$-simple nor $y$-simple:

```{figure} Images/region3b.png
---
width: 50%
name: region3b
align: center
---

```

$D=D_1\cup D_2$, where $D_1$ is $x$-simple and $D_2$ is $y$-simple.

## Examples

:::{prf:example}
Evaluate $\displaystyle\iint_D(x+2y)\,dA$, where $D$ is the region bounded by the parabolas $y=3x^2$ and $y=1+2x^2$.

```{figure} Images/example1.png
---
width: 50%
name: example1
align: center
---

```

Solution. The parabolas intersect when $3x^2=1+2x^2$ or equivalently $x^2=1$, so when $x=\pm1$. Note that the region $D$ is $x$-simple and not $y$-simple:

$$
D=\{(x,y)\,|\,-1\leq x\leq 1,\;3x^2\leq y\leq 1+2x^2\}.
$$

Hence we have

$$
\begin{align*}
\iint\limits_D(x+2y)\,dA&=\int_{-1}^1\int_{3x^2}^{1+2x^2}(x+2y)\,dy\,dx=\int_{-1}^1\bigg[xy+y^2\bigg]_{y=3x^2}^{1+2x^2}\,dx\\
&=\int_{-1}^1\left(x(1+2x^2)+(1+2x^2)^2-x\cdot3x^2-(3x^2)^2\right)\,dx\\
&=\int_{-1}^1\left(1+x+4x^2-x^3-5x^4\right)\,dx\\
&=\bigg[x+\frac{1}{2}x^2+\frac{4}{3}x^3-\frac{1}{4}x^4-x^5\bigg]_{-1}^1
=2\cdot\frac{4}{3}=\frac{8}{3}.
\end{align*}
$$

:::

:::{prf:example}
Find the volume of the solid that lies under the paraboloid $z=x^2+y^2$ and above the region $D$ in the $xy$-plane bounded by the line $y=x$ and the parabola $y=x^2$.

```{figure} Images/example2.png
---
width: 50%
name: example2
align: center
---

```

Solution. Note that the region $D$ is both $x$-simple and $y$-simple. As an $x$-simple region we have:

$$
D=\{(x,y)\,|\,0\leq x\leq 1,\;x^2\leq y\leq x\}.
$$

Therefore the volume under $z=x^2+y^2$ and above $D$ is

$$
\begin{align*}
V&=\iint\limits_D(x^2+y^2)\,dA=\int_0^1\int_{x^2}^x(x^2+y^2)\,dy\,dx=\int_0^1\bigg[x^2y+\frac{1}{3}y^3\bigg]_{y=x^2}^x\,dx\\
&=\int_0^1\left(x^2\cdot x+\frac{1}{3}x^3-x^2\cdot x^2-\frac{1}{3}(x^2)^3\right)\,dx\\
&=\int_0^1\left(\frac{4}{3}x^3-x^4-\frac{1}{3}x^6\right)\,dx=\bigg[\frac{1}{3}x^4-\frac{1}{5}x^5-\frac{1}{21}x^7\bigg]_{x=0}^1\\
&=\frac{1}{3}-\frac{1}{5}-\frac{1}{21}=\frac{35-21-5}{105}=\frac{9}{105}=\frac{3}{35}.
\end{align*}
$$ 
 
As a $y$-simple region we have:

$$
D=\{(x,y)\,|\,0\leq y\leq 1,\;y\leq x\leq\sqrt{y}\}.
$$
 
Therefore the volume can also be obtained as

$$
\begin{align*}
V&=\iint\limits_D(x^2+y^2)\,dA=\int_0^1\int_{y}^{\sqrt{y}}(x^2+y^2)\,dx\,dy=\int_0^1\bigg[\frac{1}{3}x^3+xy^2\bigg]_{x=y}^{\sqrt{y}}\,dy\\
&=\int_0^1\left(\frac{1}{3}(\sqrt{y})^3+y^2\sqrt{y}-\frac{1}{3}y^3-y^3\right)\,dy\\
&=\int_0^1\left(\frac{1}{3}y\sqrt{y}+y^2\sqrt{y}-\frac{4}{3}y^3\right)\,dy=\bigg[\frac{2}{15}y^2\sqrt{y}+\frac{2}{7}y^3\sqrt{y}-\frac{1}{3}y^4\bigg]_{y=0}^1\\
&=\frac{2}{15}+\frac{2}{7}-\frac{1}{3}=\frac{14+30-35}{105}=\frac{9}{105}=\frac{3}{35}.
\end{align*}
$$

:::

:::{prf:example}
Evaluate $\displaystyle\iint\limits_Dxy\,dA$, where $D$ is the region bounded by the line $y=x-1$ and the parabola $y^2=x+5$.

```{figure} Images/example3.png
---
width: 50%
name: example3
align: center
---

```

Solution. Again the region $D$ is both $x$-simple and $y$-simple. As an $x$-simple region we have to split the integral into two parts:

$$
\iint\limits_Dxy\,dA=\int_{-5}^{-1}\int_{-\sqrt{x+5}}^{\sqrt{x+5}}xy\,dy\,dx+\int_{-1}^4\int_{x-1}^{\sqrt{x+5}}xy\,dy\,dx.
$$
 
As a $y$-simple region it is much easier:

$$
D=\{(x,y)\,|\,-2\leq y\leq 3,\;y^2-5\leq x\leq y+1\}.
$$
 
Therefore we obtain

$$
\begin{align*}
\iint\limits_Dxy\,dA&=\int_{-2}^3\int_{y^2-5}^{y+1}xy\,dx\,dy=\int_{-2}^3\bigg[\frac{1}{2}x^2y\bigg]_{x=y^2-5}^{y+1}\,dy\\
&=\frac{1}{2}\int_{-2}^3y\left((y+1)^2-\left(y^2-5\right)^2\right)\,dy\\
&=\frac{1}{2}\int_{-2}^3\left(-24y+2y^2+11y^3-y^5\right)\,dy\\
&=\frac{1}{2}\bigg[-12y^2+\frac{2}{3}y^3+\frac{11}{4}y^4-\frac{1}{6}y^6\bigg]_{y=-2}^3\\
&=\frac{1}{2}\left(-108+18+\frac{891}{4}-\frac{243}{2}+48+\frac{16}{3}-44+\frac{32}{3}\right)\\
&=\frac{1}{2}\left(-70+\frac{891}{4}-\frac{243}{2}\right)=\frac{-280+891-486}{8}=\frac{125}{8}.
\end{align*}
$$

:::

:::{prf:example}
Find the volume of the tetrahedron bounded by the planes $2x+y+z=2$, $y=2x$, $y=0$ and $z=0$.

```{figure} Images/example4.png
---
width: 50%
name: example4
align: center
---

```

Solution. Note that, since the plane $2x+y+z=2$ intersects the $xy$-plane ($z=0$) in the line $2x+y=2$, the volume of the tetrahedron $T$ is the volume under the graph of the function $z=2-2x-y$ above the triangular region $D$ given by

$$
D=\{(x,y)\,|\,0\leq x\leq \tfrac{1}{2},\;2x\leq y\leq2-2x\}.
$$ 
 
Therefore the volume equals

$$
\begin{align*}
V&=\iint\limits_D(2-2x-y)\,dA=\int_0^{\frac{1}{2}}\int_{2x}^{2-2x}(2-2x-y)\,dy\,dx\\
&=\int_0^{\frac{1}{2}}\bigg[2y-2xy-\frac{1}{2}y^2\bigg]_{y=2x}^{2-2x}\,dx
=\int_0^{\frac{1}{2}}\bigg[(2-2x)y-\frac{1}{2}y^2\bigg]_{y=2x}^{2-2x}\,dx\\
&=\int_0^{\frac{1}{2}}\left(\frac{1}{2}(2-2x)^2-(2-2x)\cdot2x+\frac{1}{2}(2x)^2\right)\,dx\\
&=\int_0^{\frac{1}{2}}(2-8x+8x^2)\,dx=\bigg[2x-4x^2+\frac{8}{3}x^3\bigg]_0^{\frac{1}{2}}=\frac{1}{3}.
\end{align*}
$$

:::

:::{prf:example}
Evaluate the iterated integral $\displaystyle\int_0^1\int_x^1\cos(y^2)\,dy\,dx$.

```{figure} Images/example5.png
---
width: 50%
name: example5
align: center
---

```

Solution. The inner integral $\displaystyle\int\cos(y^2)\,dy$ cannot be evaluated in terms of elementary functions. However, note that

$$
\int_0^1\int_x^1\sin(y^2)\,dy\,dx=\iint\limits_D\sin(y^2)\,dA,
$$
 
where

$$
D=\{(x,y)\,|\,0\leq x\leq 1,\;x\leq y\leq 1\}.
$$

This region $D$ is both $x$-simple and $y$-simple. As a $y$-simple region it is given by

$$
D=\{(x,y)\,|\,0\leq y\leq 1,\;0\leq x\leq y\}.
$$

Hence we have

$$
\begin{align*}
\int_0^1\int_x^1\cos(y^2)\,dy\,dx&=\iint\limits_D\cos(y^2)\,dA=\int_0^1\int_0^y\cos(y^2)\,dx\,dy\\
&=\int_0^1y\cos(y^2)\,dy=\bigg[\frac{1}{2}\sin(y^2)\bigg]_{y=0}^1=\frac{1}{2}\sin(1).
\end{align*}
$$

:::

## The area of a region

If we integrate the constant function $f(x,y)=1$ over a region $D$, we get the area of $D$:

$$
\text{area}(D)=\iint\limits_D1\,dA.
$$

:::::{prf:corollorary}
:label: Cor:MultivariableIntegration:Area
If $m\leq f(x,y)\leq M$ for all $(x,y)\in D$, then:

$$
m\cdot\text{area}(D)\leq\iint\limits_Df(x,y)\,dA\leq M\cdot\text{area}(D).
$$

:::::

:::{prf:example}
```{figure} Images/area.png
---
width: 50%
name: area
align: right
---

```

Consider the region $D$ in $\mathbb{R}^2$ bounded by the graphs of $y=x^2$ and $y=\sqrt{x}$.

Then we have:

$$
\textrm{area}(D)=\iint\limits_D1\,dA=\int_0^1\int_{x^2}^{\sqrt{x}}1\,dy\,dx=\int_0^1\left(\sqrt{x}-x^2\right)\,dx
=\bigg[\frac{2}{3}x\sqrt{x}-\frac{1}{3}x^3\bigg]_{x=0}^1=\frac{1}{3}.
$$

:::
