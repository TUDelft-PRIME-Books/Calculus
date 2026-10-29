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



## Limits, continuity, derivatives and integrals

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

For curves in $\mathbb{R}^2$ or $\mathbb{R}^3$ we can obtain the geometric interpretation of the vector $\mathbb{r}'(t)$ by visualising it. Consider a curve $\mathcal{C}$ in $\mathbb{R}^2$ with parametrisation $\begin{pmatrix} x\\ y\end{pmatrix}=\mathbf{r}(t)$ for $t\in I$ and suppose that $\mathbf{r}$ is differentiable. Let $P$ be the point $\mathbf{r}(t)$ and $Q$ the point $\mathbf{r}(t+h)$. Then the vector $\mathbf{r}(t+h)-\mathbf{r}(t)$ represents the vector from $P$ to $Q$. As $h$ goes to $0$, the point $Q$ moves towards $P$ so that the vector $\mathbf{r}(t+h)-\mathbf{r}(t)$ decreases in length. The vector $\dfrac{1}{h}\left(\mathbf{r}(t+h)-\mathbf{r}(t)\right)$ points in the same direction as the vector $\mathbf{r}(t+h)-\mathbf{r}(t)$, but for $0<h<1$ the length increases again. By inspecting {numref}`Fig:Tangentvector` we see that the vector $\mathbf{r}'(t)$ appears to be tangent to the curve. This leads to the following definition.

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

Moet nog: rekenregels, hogere orde afgeleiden, interpretatie als velocity, integralen
