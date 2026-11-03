(Section:Curves3d)=

# Curves in $\mathbb{R}^3$

In this section we cover:

- Curves in $\mathbb{R}^3$
- Parametrization of curves
- Orientation of curves
- Closed curves
- Curvature
- Normal/binormal vector
- Torsion
- Fresnet-Serret formulas

## Introduction

In an area control center (ACC), controllers need to keep track of aircraft flying in the airspace of a certain region. For each aircraft, they need to keep track of the $3$-dimensional position of the aircraft in order to avoid collisions. The position of an aircraft at a certain time $t$ can be modelled as a $3$-dimensional vector

$$
 \mathbf{r}(t)=\begin{pmatrix}x(t)\\ y(t)\\ z(t)\end{pmatrix},
$$

where $x(t)$, $y(t)$ and $z(t)$ describe the three coordinates of the aircraft at time $t$. The trajectory of the aircraft can then be visualised as a **curve** in $\mathbb{R}^3$. We will call the vector function $\mathbf{r}(t)$ a **parametrisation** of the curve, and $t$ the **parameter**. For the aircraft, not only position but also quantities like velocity and acceleration need to be modelled as $3$-dimensional vectors that are a function of time. 

In {numref}`Section:Curves` we have studied curves in $\mathbb{R}^2$. Of course, curves play an equally important role in $\mathbb{R}^3$. In this section, we will study parameterised curves in $\mathbb{R}^3$. Several concepts can be lifted directly to the three-dimensional setting. Since having a third dimension available gives more possibilities for the direction of a curve, we will also introduce concepts such as the torsion to help us understand these possibilities.

## Curves and parametrisations

We often think of curves as lines that are not necessarily straight. In order to turn this into a more mathematical definition, we will define curves in termes of the parametrisations that describe them.

::::::{prf:definition} 
:label: Def:Curves3d:ParamCurve

A **parametric curve**, or simply **curve**, $\mathcal{C}$ in $\mathbb{R}^3$ is a set of points $(x,y,z)$ whose coordinates are given by **parametric equations** 

$$
 \begin{cases}x&=f(t),\\ y&=g(t)\\ z&=h(t)\end{cases}
$$

for $t$ in some set $I\subset\mathbb{R}$, where $f$, $g$ and $h$ are given single-variable functions called the **component functions**. Here $t$ is called a **parameter**. The vector function

$$
 \mathbf{r}(t)=\begin{pmatrix}x\\ y\\ z\end{pmatrix}
$$

is known as the **position vector** of the curve. The equation

$$
 \mathbf{r}(t)=\begin{pmatrix}f(t)\\ g(t)\\ h(t)\end{pmatrix},\qquad t\in I
$$

is called a **parametrisation** of the curve.

If $I$ is the closed interval $[a,b]$, then the point $(x,y,z)=(f(a),g(a),h(a))$ is called the **start point** or **initial point** of $\mathcal{C}$, while the point $(x,y,z)=(f(b),g(b),h(b))$ is called the **end point** or **terminal point** of $\mathcal{C}$. Whenever the start point and the end point of the curve coincide, we say that the curve is **closed**.

::::::

:::{note}
A curve in $\mathbb{R}^3$ is also known as a **space curve**, while a curve in $\mathbb{R}^2$ is known as a **planar curve**.
:::

:::{note}
A curve in $\mathbb{R}^3$ can have many different parametrisations.
:::

:::{important}
When writing down a parametrisation of a curve, you should always explicitly write down for which values of the parameter the parametric equations hold, i.e. a parametrisation can be of the form $\mathbf{r}(t)$ for $a\leq t\leq b$, but only writing $\mathbf{r}(t)$ is not enough.
:::

Unlike planar curves, space curves can typically not be described by an (implicit) equation, because a single equation usually describes a surface instead of a curve. Instead, curves can arise naturally when intersection two surfaces. We will consider this in more detail in {numref}`Section:SurfacesR3`. 

::::::{prf:example} 
:label: Ex:Curves3d:Helix
Consider the space curve $\mathcal{C}$ with parametrisation $\mathbf{r}(t)=\begin{pmatrix}4\cos(2t)\\ 4\sin(2t)\\ t\end{pmatrix}$ for $0\leq t\leq 3\pi$. We note that for $0\leq t\leq 3\pi$ we have

$$
 x(t)^2+y(t)^2=\left(4\cos(2t)\right)^2+\left(4\sin(2t)\right)^2=16\left(\cos^2(2t)+\sin^2(2t)\right)=16.
$$

[^FootnoteProj]: You can visualise a projection onto the $xy$-plane of a curve by imagining looking at the curve from above so that differences in $z$-coordinate are not visible, or by "squashing" the curve onto the $xy$-plane.

So when we project the curve onto the $xy$-plane[^FootnoteProj] we see a circle with radius $4$. According to {prf:ref}`Thm:Curves:EllipseParam`, this circle is traversed three times in counterclockwise direction, when viewed from above. In particular, the curve $\mathcal{C}$ lies on the cylinder $x^2+y^2=16$, i.e. the cylinder of which the axis is the $z$-axis and which has radius $4$. Of course, we are not only interested in what happens with $x$ and $y$, as $z$ plays an equally important role. We observe that $z$ grows linearly as a function of $t$. At $t=\pi$, $t=2\pi$ and $t=3\pi$ the position vector $\mathbf{r}(t)$ is right above the initial point $\mathbf{r}(0)$. We conclude that the curve is a *circular helix*,  that goes around the cylinder $x^2+y^2=16$ three times.

:::{todo}
Include an applet of the curve.
:::
::::::

::::::{prf:example} 
:label: Ex:Curves3d:Line
In {numref}`Sec:LinesAndPlanes` we have defined lines using a parametric vector equation. It should not come as a surprise that these lines are also curves in the sense of {prf:ref}`Def:Curves3d:ParamCurve`. For instance, we can consider the line $\mathcal{L}$ that contains the points $P=(1,2,4)$ and $Q=(5,3,1)$. In {prf:ref}`Ex:LinesAndPlanes:ParametricVectorEquationLineR3` we saw that the equation

$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix}=\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}+r\begin{pmatrix} 4 \\ 1 \\ -3 \end{pmatrix} \qquad \text{$r$ in $\mathbb{R}$}
$$

is a parametric vector equation of $\mathcal{L}$. This means that the equation

$$
 \mathbf{r}(r)=\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}+r\begin{pmatrix} 4 \\ 1 \\ -3 \end{pmatrix} \qquad \text{$r$ in $\mathbb{R}$}
$$

is a parametrisation of $\mathcal{L}$, which means that $\mathcal{L}$ is a space curve.
::::::

::::::{prf:example} 
:label: Ex:Curves3d:IntersectionSurface
Consider the cylinder $S$ in $\mathbb{R}^3$ given by the equation

$$
 x^2+z^2=9.
$$

This is a cylinder of radius $2$ of which the axis is the $y$-axis. In addition, we consider the plane $P$ give by the equation

$$
 2x+3y+4z=3.
$$

The intersection $\mathcal{C}$ of $S$ and $P$ is a curve in $\mathbb{R}^3$ so we let us try to find a parametrisation of $\mathcal{C}$. Inspired by the standard parametrisation for a circle (see {prf:ref}`Thm:Curves:EllipseParam`) we choose

$$
 x(t)=3\cos(t),\qquad z(t)=3\sin(t)
$$

for $0\leq t\leq 2\pi$. This way, we have 

$$
 \left(x(t)\right)^2+\left(z(t)\right)^2=9
$$

for $0\leq t\leq 2\pi$, so now matter what we choose as $y(t)$, the curve will lie on the cylinder $S$. In order to ensure that it also lies on the plane $P$, we plug in our chosen expressions for $x(t)$ and $y(t)$ to obtain

$$
 6\cos(t)+3y+12\sin(t)=3.
$$

We can then solve for $y$ to find

$$
 y=1-2\cos(t)-4\sin(t).
$$

As such, we find that $\mathbf{r}(t)=\begin{pmatrix}3\cos(t)\\ 1-2\cos(t)-4\sin(t)\\ 3\sin(t)\end{pmatrix}$ for $0\leq t\leq 2\pi$ is a parametristion of the curve of intersection $\mathcal{C}$. Of course, there are many other parametrisations possible for this curve.

:::{todo}
Include an applet showing $S$, $P$ and $\mathcal{C}$, preferable with a slider (or something) moving $t$ along the curve.
::::::



## Vector functions

An essential component of the parametrisation of a curve is the vector function $\mathbf{r}(t)$, so it is important to see what we can do with these functions. Although the focus of this section is mostly on curves in $\mathbb{R}^3$, it takes little effort to study vector function is the more general setting where these functions have $n$ components. Since the component functions of $\mathbf{r}$ are single-variable functions, we know how concepts like limits, derivatives and integrals work for these component functions. In this subsection, we extend these concepts to vector functions. As usual, we start with limits.

::::::{prf:definition} 
:label: Def:Curves3d:Limit
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function such that the domain of $\mathbf{r}$ contains an open interval of the form $\left(c_1,a\right)$ or $\left(a,c_2\right)$. 

Then we say that the **limit** of $\mathbb{R}$ as $t$ approaches $a$ is equal to $\mathbf{v}$, and we write $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{v}$, whenever for each $\varepsilon>0$ there exists a $\delta>0$, such that for all $t$ in the domain of $\mathbf{r}$ with $0<|t-a|<\delta$, we have $\|\mathbf{r}(t)-\mathbf{v}\|<\varepsilon$.
::::::

Evaluating limits using this definitions sounds (and, admittedly, is) rather cumbersome, but fortunately, we can use all the techniques that we learned previously for single-variable functions by using the following result.

::::::{prf:theorem} 
:label: Thm:Curves3d:Limit
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function such that the domain of $\mathbf{r}$ contains an open interval of the form $\left(c_1,a\right)$ or $\left(a,c_2\right)$. Write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$ and $\mathbf{v}=\begin{pmatrix}v_1\\ \vdots\\ v_n\end{pmatrix}$.

Then we have $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{v}$ if, and only if, for all $1\leq k\leq n$ we have $\lim\limits_{t\rightarrow a}x_k(t)=v_k$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves3d:Limit`
:class: tudproof, dropdown
First suppose that $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{v}$ and let $1\leq k\leq n$. Let $\varepsilon>0$ be given and pick $\delta>0$ such that for for all $t$ in the domain of $\mathbf{r}$ with $0<|t-a|<\delta$, we have $\|\mathbf{r}(t)-\mathbf{v}\|<\varepsilon$. Then for such a value of $t$ we have

$$
 |x_k(t)-v_k|\leq \sqrt{(x_1(t)-v_1)^2+\ldots +(x_n(t)-v_n)^2}=\|\mathbf{r}(t)-\mathbf{v}\|<\varepsilon.
$$

By definition, we have $\lim\limits_{t\rightarrow a}x_k(t)=v_k$.

Now suppose that for all $1\leq k\leq n$ we have $\lim\limits_{t\rightarrow a}x_k(t)=v_k$. Note that by construction the component functions $x_1,\ldots,x_n$ have the same domain as $\mathbf{r}$. Let $\varepsilon>0$ be given. For each $1\leq k\leq n$, we pick $\delta>0$ such that for for all $t$ in the domain of $\mathbf{r}$ with $0<|t-a|<\delta_k$, we have $|x_k(t)-v_k|<\dfrac{\varepsilon}{\sqrt{k}}$. Let $\delta=\mathrm{min}\left\{\delta_1,\ldots,\delta_k\right\}$, i.e. $\delta$ is the smallest of each of the $\delta_k$. Then for $t$ in the domain of $\mathbf{r}$ with $0<|t-a|<\delta$ we have

\begin{align*}
 \|\mathbf{r}(t)-\mathbf{v}\|&=\sqrt{(x_1(t)-v_1)^2+\ldots +(x_n(t)-v_n)^2}\\
 &\leq \sqrt{\left(\frac{\varepsilon}{\sqrt{k}}\right)^2+\ldots+\left(\frac{\varepsilon}{\sqrt{k}}\right)^2}\\
 &=\sqrt{k\frac{\varepsilon^2}{k}}\\
 =\varepsilon.
\end{align*}

We conclude that $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{v}$.
:::

For continuity we use a similar setup: we first give the definition in terms of $\delta$s and $\varepsilon$s and then link continuity of vector functions to continuity of the component functions.

::::::{prf:definition} 
:label: Def:Curves3d:Cont
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function and $a$ a point in the domain of $\mathbf{r}$. Then we say that $f$ is **continuous** at $a$ whenever for each $\varepsilon>0$ there exists a $\delta>0$ such that for every $t$ in the domain of $f$ with $|t-a|<\delta$ we have $\|\mathbf{r}(t)-\mathbf{r}(a)\|<\varepsilon$. If $\mathbf{r}$ is not continuous at $a$, we say that it is **discontinuous** at $a$.

If $\mathbf{r}$ is continuous at each point in its domain, we say that $\mathbf{r}$ is **continuous**.
::::::


::::::{prf:theorem} 
:label: Thm:Curves3d:Cont
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function such that the domain of $\mathbf{r}$ contains an open interval of the form $\left(c_1,a\right]$ or $\left[a,c_2\right)$. Write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$.

Then $\mathbf{r}$ is continuous at $a$ if, and only if, for all $1\leq k\leq n$ the function $x_k$ is continuous at $a$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves3d:Cont`
:class: tudproof, dropdown
It follows directly from the definition of a limit that, with these conditions on the domain of $\mathbf{r}$, $\mathbf{r}$ is continuous at $a$ if, and only if, $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{r}(a)$.

First suppose that $\mathbf{r}$ is continuous at $a$ and let $1\leq k\leq n$. Then we have $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{r}(a)$, so by {prf:ref}`Thm:Curves3d:Limit` we have $\lim\limits_{t\rightarrow a}x_k(t)=x_k(a)$. It then follows from {prf:ref}`Theorem:Continuity:EpsilonDelta` that $x_k$ is continuous at $a$.

Now suppose that for all $1\leq k\leq n$ the function $x_k$ is continuous at $a$. By {prf:ref}`Theorem:Continuity:EpsilonDelta` we have $\lim\limits_{t\rightarrow a}x_k(t)=x_k(a)$ for all $1\leq k\leq n$. Then it follows from {prf:ref}`Thm:Curves3d:Limit` that $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{r}(a)$, so $\mathbf{r}$ is continuous at $a$.
:::

::::::{prf:example} 
:label: Ex:Curves3d:LimCont
Consider the vector function

$$
 \mathbf{r}(t)=\begin{pmatrix}\dfrac{t-1}{t^2-1}\\ \dfrac{\ln(t)}{1-\sqrt{t}} \end{pmatrix}.
$$

The domain of this vector function is the union of the intervals $(0,1)$ and $(1,\infty)$, which we can, alternatively, write as $(0,\infty)\setminus\{1\}$. The component functions $\dfrac{t+1}{t^2-1}$ and $\dfrac{\ln(t)}{1-\sqrt{t}}$ are continuous on this domain, so $\mathbf{r}$ is continuous by {prf:ref}`Thm:Curves3d:Cont`. In addition, we note that

$$
 \lim_{t\rightarrow1}\dfrac{t-1}{t^2-1}=\dfrac{1}{2},
$$

either by cancelling the common factor $t-1$ (see {numref}`Subsec:Limitsrules`) or by using l'Hospital's rule (see {prf:ref}`Thm:lHospital:lHospital`). We also obtain

$$
 \lim_{t\rightarrow1}\dfrac{\ln(t)}{1-\sqrt{t}} =-2,
$$

using l'Hospital's rule. Using {prf:ref}`Thm:Curves3d:Limit` we conclude that

$$
 \lim_{t\rightarrow1}\mathbf{r}(t)=\begin{pmatrix}\lim\limits_{t\rightarrow1}\dfrac{t-1}{t^2-1}\\ \lim\limits_{t\rightarrow1}\dfrac{\ln(t)}{1-\sqrt{t}} \end{pmatrix}=\begin{pmatrix}\frac{1}{2}\\ -2\end{pmatrix}.
$$
::::::

The derivative of a vector function is defined very similarly to the derivative of a single-variable function.

::::::{prf:definition} 
:label: Def:Curves3d:Diff
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function and $a$ a point in the domain of $\mathbf{r}$. Then the **derivative** of $\mathbf{r}$ at $a$, denoted by $\mathbf{r}'(a)$ is

$$
 \mathbf{r}'(a)=\lim_{h\rightarrow 0}\frac{1}{h}\left(\mathbf{r}(a+h)-\mathbf{r}(a)\right),
$$

provided this limit exists. If the limit exists, we say that $\mathbf{r}$ is differentiable in $a$. 


If the function $\mathbf{r}$ is differentiable at each point in its domain, we say that $\mathbf{r}$ is **differentiable**. 
::::::

::::::{prf:theorem} 
:label: Thm:Curves3d:Diff
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function and let $a$ be a point in the domain of $\mathbf{r}$. Write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$.

Then $\mathbf{r}$ is differentiable at $a$ if, and only if, for all $1\leq k\leq n$ the function $x_k$ is differentiable at $a$. In that case, we have 

$$
 \mathbf{r}'(a)=\begin{pmatrix}x_1'(a)\\ \vdots\\ x_n'(a)\end{pmatrix}.
$$ 
::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves3d:Diff`
:class: tudproof, dropdown
Note that for $h\neq 0$ we have

$$
 \frac{1}{h}\left(\mathbf{r}(a+h)-\mathbf{r}(a)\right)=\frac{1}{h}\begin{pmatrix}x_1(a+h)-x_1(a)\\ \vdots \\ x_n(a+h)-x_n(a)\end{pmatrix}=\begin{pmatrix}\frac{x_1(a+h)-x_1(a)}{h}\\ \vdots \\ \frac{x_n(a+h)-x_n(a)}{h}\end{pmatrix}.
$$

By {prf:ref}`Thm:Curves3d:Limit` we have that $\lim\limits_{h\rightarrow 0}\frac{1}{h}\left(\mathbf{r}(a+h)-\mathbf{r}(a)\right)$ exists if and only if for all $1\leq k\leq n$ the limit $\lim\limits_{h\rightarrow 0}\dfrac{x_k(a+h)-x_k(a)}{h}$ exists, meaning that $\mathbf{r}$ is differentiable at $a$ if, and only if, for all $1\leq k\leq n$ the function $x_k$ is differentiable at $a$. In addition, we conclude that

$$ 
 \mathbf{r}'(a)=\lim\limits_{h\rightarrow 0}\dfrac{x_k(a+h)-x_k(a)}{h}=\begin{pmatrix}\frac{\lim\limits_{h\rightarrow 0}x_1(a+h)-x_1(a)}{h}\\ \vdots \\ \lim\limits_{h\rightarrow 0}\frac{x_n(a+h)-x_n(a)}{h}\end{pmatrix}=\begin{pmatrix}x_1'(a)\\ \vdots\\ x_n'(a)\end{pmatrix}.
$$
:::

If the vector function $\mathbf{r}(t)$ represent the **position** of some particle, then the derivative $\mathbf{r}'(t)$ represent its **velocity**. Indeed, we should think of velocity as a vector-valued quantity as it has both a direction and a magnitude (the magnitude of the velocity is typically called the **speed**). 

Just like for derivatives of single-variable functions, there are several computation rules for finding derivatives of vector functions. These usually follow from their single-variable equivalents. The most important ones are listed in the theorem below.

::::::{prf:theorem} 
:label: Thm:Curves3d:Basiccomputationrules
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ and $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset\mathbb{R}$ be vector functions. Let $a\in I$ and assume that $\mathbf{r}$ and $\mathbf{s}$ are differentiable at $a$. 

- $(\mathbf{r}+\mathbf{s})$ is differentiable at $a$ and we have $(\mathbf{r}+\mathbf{s})'(a)=\mathbf{r}'(a)+\mathbf{s}'(a)$. (sum rule)
- If $c\in\mathbb{R}$, then $c\mathbf{r}$ is differentiable at $a$ and we have $(c\mathbf{r})'(a)=c\mathbf{r}'(a)$. (scalar multiple rule)
- If $f$ is a single-variable function that is differentiable at $a$ then $(f\mathbf{r})(t)=f(t)\mathbf{r}(t)$ is differentiable at $a$ and we have $(f\mathbf{r})'(a)=f'(a)\mathbf{r}(a)+f(a)\mathbf{r}'(a)$. (product rule)
- If $g$ is a single variable function and $b$ is in the domain of $g$ in such a way that $g(b)=a$ and $g$ is differentiable at $b$, then $\mathbf{r}\circ g$ is differentiable at $b$ and we have $(\mathbf{r}\circ g)'(b)=g'(b)\mathbf{r}'(a)$. (chain rule)
- $\mathbf{r}\cdot\mathbf{s}$ is differentiable at $a$ and we have $(\mathbf{r}\cdot\mathbf{s})(a)=\mathbf{r}'(a)\cdot \mathbf{s}(a)+\mathbf{r}(a)\cdot \mathbf{s}'(a)$. (dot product rule)
- If the codomain of $\mathbf{r}$ and $\mathbf{s}$ is $\mathbb{R}^3$ then $\mathbf{r}\times\mathbf{s}$ is differentialbe at $a$ and we have $\left(\mathbf{r}\times\mathbf{s}\right)(a)=\mathbf{r}'(a)\times\mathbf{s}(a)+\mathbf{r}(a)\times \mathbf{s}'(a)$. (cross product rule)
::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves3d:Basiccomputationrules`
:class: tudproof, dropdown
**Proof of sum rule**. This follows directly from {prf:ref}`Thm:Curves3d:Diff` and {prf:ref}`Thm:Differentiability:Sumscalar`.

**Proof of scalar multiple rule**. This follows directly from {prf:ref}`Thm:Curves3d:Diff` and {prf:ref}`Thm:Differentiability:Sumscalar`.

**Proof of product rule**.  This follows directly from {prf:ref}`Thm:Curves3d:Diff` and {prf:ref}`Thm:Productquotientrule:Productrule`

**Proof of chain rule**. We write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$. Then we have $\left(\mathbf{r}\circ g\right)(t)=\begin{pmatrix}x_1(g(t))\\ \vdots\\ x_n(g(t))\end{pmatrix}$. By {prf:ref}`Thm:Curves3d:Diff` the functions $x_1,\ldots,x_n$ are all differentiable at $a$. So by {prf:ref}`Thm:Chainrule:Chainrule` the functions $(x_1\circ g),\ldots, (x_n\circ g)$ are all differentiable at $b$ and we have for all $1\leq k\leq n$

$$
 (x_k\circ g)'(b)=g'(b)x_k(g(b))=g'(b)x_k(a).
$$

Then by {prf:ref}`Thm:Curves3d:Diff` the composition $\mathbf{r}\circ g$ is differentiable at $b$ and we have

$$
 (\mathbf{r}\circ g)'(b)=\begin{pmatrix}g'(b)x_1'(a)\\ \vdots \\ g'(b)x_n'(a) \end{pmatrix}=g'(b)\mathbf{r}'(a).
$$

**Proof of dot product rule**. We write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$ and $\mathbf{s}(t)=\begin{pmatrix}y_1(t)\\ \vdots\\ y_n(t)\end{pmatrix}$. Then we have

$$
 \mathbf{r}(t)\cdot \mathbf{s}(t)=\sum_{k=1}^n x_k(t)y_k(t).
$$

By {prf:ref}`Thm:Curves3d:Diff` the functions $x_1,\ldots,x_n,y_1,\ldots,y_n$ are all differentiable at $a$. So by {prf:ref}`Thm:Differentiability:Sumscalar` and {prf:ref}`Thm:Productquotientrule:Productrule` the dot product $\mathbf{r}\cdot \mathbf{s}$ is also differentiable at $a$ and we obtain

\begin{align*}
 (\mathbf{r}\cdot\mathbf{s})(a)&=\sum_{k=1}^n \left(x_k'(a)y_k(a)+x_k(a)y_k'(a)\right)\\ &=\sum_{k=1}^n x_k'(a)y_k(a)+\sum_{k=1}^nx_k(a)y_k'(a)\\ &=\mathbf{r}'(a)\cdot \mathbf{s}(a)+\mathbf{r}(a)\cdot \mathbf{s}'(a).
$$

**Proof of cross product rule**. We write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ x_2(t)\\ x_3(t)\end{pmatrix}$ and $\mathbf{s}(t)=\begin{pmatrix}y_1(t)\\ y_2(t)\\ y_3(t)\end{pmatrix}$. Then we have

$$
 (\mathbf{r}\times\mathbf{s})(t)=\begin{pmatrix}x_2(t)y_3(t)-x_3(t)y_2(t)\\ x_3(t)y_1(t)-x_1(t)y_3(t)\\ x_1(t)y_2(t)-x_2(t)y_1(t)\end{pmatrix}.
$$

By {prf:ref}`Thm:Curves3d:Diff` the functions $x_1,x_2,x_3,y_1,y_2,y_3$ are all differentiable at $a$. So by {prf:ref}`Thm:Differentiability:Sumscalar` and {prf:ref}`Thm:Productquotientrule:Productrule` the cross product $\mathbf{r}\times \mathbf{s}$ is also differentiable at $a$ and we obtain

\begin{align*}
 (\mathbf{r}\times\mathbf{s})'(a)&=\begin{pmatrix}x_2'(a)y_3(a)+x_2(a)y_3'(a)-x_3'(a)y_2(a)-x_3(a)y_2'(a)\\ x_3'(a)y_1(a)+x_3(a)y_1'(a)-x_1'(a)y_3(a)-x_1(a)y_3'(a)\\ x_1'(a)y_2(a)+x_1(a)y_2'(a)-x_2'(a)y_1(a)-x_2(a)y_1'(a)\end{pmatrix}\\
 &=\begin{pmatrix}x_2'(a)y_3(a)-x_3'(a)y_2(a)\\ x_3'(a)y_1(a)-x_1'(a)y_3(a)\\ x_1'(a)y_2(a)-x_2'(a)y_1(a)\end{pmatrix}+\begin{pmatrix}x_2(a)y_3'(a)-x_3(a)y_2'(a)\\ x_3(a)y_1'(a)-x_1(a)y_3'(a)\\ x_1(a)y_2'(a)-x_2(a)y_1'(a)\end{pmatrix}\\
 &=\mathbf{r}'(a)\times\mathbf{s}(a)+\mathbf{r}(a)\times \mathbf{s}'(a)
\end{align*}
:::

As a consequence of the dot product rule, we can also find an expression for the derivative of the norm of a vector function.

::::::{prf:theorem} 
:label: Thm:Curves3d:Normvector
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset\mathbb{R}$ be a differentiable vector function. Then the function $\left|\mathbf{r}(t)\right|^2$ is differentiable and we find

$$
 \frac{d}{dt}\left|\mathbf{r}(t)\right|^2=2\mathbf{r}(t)\cdot \mathbf{r}'(t).
$$

In addition, if $\mathbf{r}(t)\neq\mathbf{0}$ we have

$$
 \frac{d}{dt}\left|\mathbf{r}(t)\right|=\frac{\mathbf{r}(t)\cdot \mathbf{r}'(t)}{|\mathbf{r}(t)|}.
$$

As a consequence, if $\left|\mathbf{r}(t)\right|$ is constant on $D$, then the vectors $\mathbf{r}(t)$ and $\mathbf{r}'(t)$ are orthogonal for each $t\in D$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves3d:Normvector`
:class: tudproof, dropdown
We note that

$$
 \left|\mathbf{r}(t)\right|^2=\mathbf{r}(t)\cdot \mathbf{r}(t).
$$

So by the dot product rule from {prf:ref}`Thm:Curves3d:Basiccomputationrules` we find

$$
 \frac{d}{dt}\left|\mathbf{r}(t)\right|^2=\mathbf{r}'(t)\cdot\mathbf{r}(t)+\mathbf{r}(t)\cdot\mathbf{r}'(t)=2\mathbf{r}(t)\cdot \mathbf{r}'(t).
$$

If $\mathbf{r}(t)\neq \mathbf{0}$ we find using the chain rule

\begin{align*}
 \dfrac{d}{dt}\left|\mathbf{r}(t)\right|&=\dfrac{d}{dt}\sqrt{\left|\mathbf{r}(t)\right|^2}\\
 &=\dfrac{1}{2\sqrt{\left|\mathbf{r}(t)\right|^2}}\frac{d}{dt}\left(\left|\mathbf{r}(t)\right|^2\right)\\
 &=\dfrac{1}{2\left|\mathbf{r}(t)\right|}2\left(\mathbf{r}(t)\cdot \mathbf{r}'(t)\right)\\
 &=\dfrac{\mathbf{r}(t)\cdot \mathbf{r}'(t)}{|\mathbf{r}(t)|}
\end{align*}

If $\left|\mathbf{r}(t)\right|$ is constant on $D$, then its derivative must be $0$ for each $t\in D$. We then obtain $\mathbf{r}(t)\cdot \mathbf{r}'(t)=0$, which means that the vectors $\mathbf{r}(t)$ and $\mathbf{r}'(t)$ are orthogonal.
:::

It is also useful to consider higher order derivatives. For instance, if $\mathbf{r}(t)$ represent the position vector of some particle, then its second derivative $\mathbf{r}''(t)$ represents the **acceleration**. For instance, Newton's second law $\mathbf{F}=m\mathbf{a}$ can be represented as $\mathbf{F}=m\mathbf{r}''$. The second derivative will also play an important role later when computing the curvature of a space curve.

::::::{prf:definition} 
:label: Def:Curves3d:HigherDiff
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function and let $a$ be a point in the domain of $\mathbf{r}$ such that $\mathbf{r}$ is differentiable at $a$. If $\mathbf{r}'$ is differentiable at $a$, then its derivative $(\mathbf{r}')'(a)$ is called the **second derivative** of $\mathbf{r}$ at $a$ and is denoted by $\mathbf{r}''(a)$. If the second derivative of $\mathbf{r}$ exists at each point in its domain, we say that $\mathbf{r}$ is **twice differentiable** and we call the vector function $\mathbf{r}''$ the **second derivative** of $\mathbf{r}$.

In general, if $n>0$ is a nonzero natuarly number, then the **$n$th derivative** of $\mathbf{r}$ at $a$ is the derivative of the $(n-1)$th derivative of $\mathbf{r}$ at $a$, provided it exists, and is denoted by $\mathbf{r}^{(n)}(a)$. If the $n$th derivative of $\mathbf{r}$ exists at each point in its domain, we say that $\mathbf{r}$ is **$n$ times differentiable** and we call the vector function $\mathbf{r}^{(n)}$ the **$n$th derivative** of $\mathbf{r}$.
::::::



::::::{prf:example} 
:label: Ex:Curves3d:Deriv
For the vector function

$$
 \mathbf{r}(t)=\begin{pmatrix}t^3\\ \cos(2t)\\ e^{-t}\end{pmatrix},
$$

we find the derivative by differentiating each of the component functions. We obtain

$$
 \mathbf{r}'(t)=\begin{pmatrix}3t^2\\ -2\sin(2t)\\ -e^{-t}\end{pmatrix}.
$$

This vector function is differentiable again, and we find

$$
 \mathbf{r}''(t)=\begin{pmatrix}6t\\ -4\cos(2t)\\ e^{-t}\end{pmatrix}.
$$
::::::



So far, we have defined introduced limits, continuity and derivatives by lifting the single-variable definitions to the vector function setting and then we showed that we can evaluate them component-wise. For (definite) integrals, there is no nice way to lift {prf:ref}`Def:Integration:DefiniteGeneral` to the vector setting. Instead, we will define the integral of a vector function component-wise.

::::::{prf:definition} 
:label: Def:Curves3d:Integral
Let $\mathbf{r}:[a,b]\rightarrow\mathbb{R}^n$ be a vector function. We write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$ and assume that $x_1,\ldots,x_n$ are piecewise-continuous and bounded on $[a,b]$. Then the **definite integral** $\displaystyle \int_a^b\mathbf{r}(t)\,dt$ of $\mathbf{r}$ is defined as

$$
 \int_a^b\mathbf{r}(t)\,dt =\begin{pmatrix}\int\limits_a^b x_1(t)\,dt\\ \vdots \\ \int\limits_a^b x_n(t)\,dt\end{pmatrix}.
$$
::::::

We can evaluate definite integrals of a vector function the same way as we would for a single-variable function: by finding an antiderivative and by using the fundamental theorem of calculus.

::::::{prf:definition} 
:label: Def:Curves3d:Antiderivative
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function. A vector function $\mathbf{R}$ is known as an **antiderivative** of $\mathbf{r}$ on $D$ if it is differentiable and $\mathbf{R}'(t)=\mathbf{r}(t)$ for all $t\in D$.
::::::

::::::{prf:theorem} 
:label: Thm:Curves3d:FundamentalTheorem
Let $\mathbf{r}:[a,b]\rightarrow\mathbb{R}^n$ be a continuous vector function. Then the vector function

$$
 \mathbf{R}(t)=\int_a^t \mathbf{r}(s)\,ds
$$

is an antiderivative of $\mathbf{r}$.

In addition, if $\mathbf{S}$ is any antiderivative of $\mathbf{r}$ on $[a,b]$ then we have

$$
 \int_a^b\mathbf{r}(t)\,dt=\mathbf{S}(b)-\mathbf{S}(a).
$$
::::::

:::{admonition} Proof of {prf:ref}`Thm:Curves3d:FundamentalTheorem`
:class: tudproof, dropdown
Since integration is defined component-wise, these results follow directly from {prf:ref}`Thm:Integration:FundamentalTheoremPart1` and {prf:ref}`Thm:Integration:FundamentalTheoremPart2`.
:::

::::::{prf:example} 
:label: Ex:Curves3d:Int
We again consider the vector function

$$
 \mathbf{r}(t)=\begin{pmatrix}t^3\\ \cos(2t)\\ e^{-t}\end{pmatrix}
$$

from {prf:ref}`Ex:Curves3d:Deriv`. By integrating the three component functions, we see that the vector function

$$
 \mathbf{R}(t)=\begin{pmatrix}\int t^3\,dt\\ \int\cos(2t)\,dt\\ \int e^{-t}\,dt\end{pmatrix}=\begin{pmatrix}\frac{1}{4}t^4\\ \frac{1}{2}\sin(2t)\\ -e^{-t}\end{pmatrix}
$$

is an antiderivative of $\mathbf{r}$. As such, we can evaluate the definite integral

$$
 \int_0^{1}\mathbf{r}(t)\,dt=\mathbf{R}(1)-\mathbf{R}(0)=\begin{pmatrix}\frac{1}{4}\\ \frac{1}{2}\sin(2)\\ -e^{-1}\end{pmatrix}-\begin{pmatrix}0\\ 0\\ -1\end{pmatrix}=\begin{pmatrix}\frac{1}{4}\\ \frac{1}{2}\sin(2)\\ 1-e^{-1}\end{pmatrix}.
$$

::::::

## Orientation and smoothness of curves


For curves in $\mathbb{R}^2$ or $\mathbb{R}^3$ we can obtain a geometric interpretation of the vector $\mathbb{r}'(t)$ by visualising it. Consider a curve $\mathcal{C}$ in $\mathbb{R}^2$ with parametrisation $\begin{pmatrix} x\\ y\end{pmatrix}=\mathbf{r}(t)$ for $t\in I$ and suppose that $\mathbf{r}$ is differentiable. Let $P$ be the point $\mathbf{r}(t)$ and $Q$ the point $\mathbf{r}(t+h)$. Then the vector $\mathbf{r}(t+h)-\mathbf{r}(t)$ represents the vector from $P$ to $Q$. As $h$ goes to $0$, the point $Q$ moves towards $P$ so that the vector $\mathbf{r}(t+h)-\mathbf{r}(t)$ decreases in length. The vector $\dfrac{1}{h}\left(\mathbf{r}(t+h)-\mathbf{r}(t)\right)$ points in the same direction as the vector $\mathbf{r}(t+h)-\mathbf{r}(t)$, but for $0<h<1$ the length increases again. By inspecting {numref}`Fig:Tangentvector` we see that the vector $\mathbf{r}'(t)$ appears to be tangent to the curve. This leads to the following definition.

:::{figure} images/Fig-Curves3d-Tangentvector2d.png
:name: Fig:Tangentvector
:class: dark-light


:::

:::{todo}
Turn {numref}`Fig:Tangentvector` into an applet consisting of a version in $\mathbb{R}^2$ on the left and one in $\mathbb{R}^3$ on the right. It should also show r(t+h) and r(t+h)-r(t) and $\frac{1}{h}(r(t+h)-r(t))$ with a slider for $h$.
:::

::::::{prf:definition} 
:label: Def:Curves3d:Tangent
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ parametrised by a differentiable vector function $\mathbf{r}(t)$ for $t\in I$ and let $t_0\in I$. If $\mathbf{r}'(t_0)\neq\mathbf{0}$, the vector $\mathbf{r}'(t_0)$ is known as the **tangent vector** to the curve $\mathcal{C}$ at the point $\mathbf{r}(t_0)$. In that case, the line through the point $\mathbf{r}(t_0)$ with direction vector $\mathbf{r}'(t_0)$ is known as the **tangent line** to the curve. The unit vector in the direction of the tangent vector is known as the **unit tangent vector** $\mathbf{T}(t_0)$ and is given by

$$
 \mathbf{T}(t_0)=\frac{1}{\|\mathbf{r}'(t_0)\|}\mathbf{r}'(t_0).
$$
::::::




::::::{prf:example} 
:label: Ex:Curves3d:Helixtang

Consider the space curve $\mathcal{C}$ with parametrisation $\mathbf{r}(t)=\begin{pmatrix}4\cos(2t)\\ 4\sin(2t)\\ t\end{pmatrix}$ for $0\leq t\leq 3\pi$ that we studied in {prf:ref}`Ex:Curves3d:Helix`. Then we can evaluate

$$
 \mathbf{r}'(t)=\begin{pmatrix}-8\sin(2t)\\ 8\cos(2t)\\ 1\end{pmatrix}.
$$

This means that at the point $\mathbf{r}(\pi)=\begin{pmatrix}4\\ 0\\ \pi\end{pmatrix}$ the tangent vector is given by

$$ 
 \mathbf{r}'(\pi)=\begin{pmatrix} 0\\ 8\\ 1\end{pmatrix},
$$

which means that the unit tangent vector at this point is given by

$$
 \mathbf{T}(\pi)=\frac{1}{\|\mathbf{r}'(\pi)\|}\mathbf{r}'(\pi)=\frac{1}{65}\begin{pmatrix} 0\\ 8\\ 1\end{pmatrix}.
$$

In addition, the tangent line to $\mathcal{C}$ at this point is given by the parametric vector equations

$$
 \begin{pmatrix} x\\ y\\ z\end{pmatrix}=\begin{pmatrix}4\\ 0\\ \pi\end{pmatrix}+t\begin{pmatrix} 0\\ 8\\ 1\end{pmatrix}
$$

for $t\in\mathbb{R}$.
::::::

::::::{prf:example} 
:label: Ex:Curves3d:Spheretang

Consider any space curve $\mathcal{C}$ with a differentiable parametrisation $\mathbf{r}(t)$ for $t\in I$ that lies on the sphere

$$
 x^2+y^2+z^2=R^2.
$$

Then for any $t\in I$ we have that $\mathbf{r}(t)$ lies on this sphere, so we find $\left|\mathbf{r}(t)\right|=R$. From {prf:ref}`Thm:Curves3d:Normvector` we find that the tangent vector $\mathbf{r}'(t)$ must be orthogonal to the position vector $\mathbf{r}(t)$. This can also be seen in {numref}`Fig:Tangentsphere`.


:::{todo}
Make an applet which shows a curve on a sphere, with a position vector $\mathbf{r}(t)$ and the corresponding tangent vector $\mathbf{r}'(t)$. The applet should have label Fig:Tangentsphere (or change the references).
:::
::::::


Moet nog: voorbeeld met snijden van twee oppervlakken (meer in 8.4), (piecewise) smoothness
