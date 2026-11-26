# Slope


## Introduction

In {numref}`Section:SlopeCurves` we have seen that implicit differentiation can be used to find the slope of a planar curve that is described by an implicit equation. This technique cannot be generalised to space curves. In addition, if you only have a parametrisation of a planar curve, it can be hard, or even impossible, to turn this into an equation. For those types of curves, we could still want to find the slope. And for space curves, it is not even clear what we mean by a slope, since the curve moves in three dimensions. We do have, at least, some intuitive idea of what a tangent line should be to a curve at a certain point: a straight line that goes through the given point and then moves in the same 'direction' as the curve. In this section, we will make these ideas more concrete. We will also discuss what it means to go forwards or backwards on a curve.

## Tangent vector



For curves in $\mathbb{R}^2$ or $\mathbb{R}^3$ we can obtain a geometric interpretation of the vector $\mathbf{r}'(t)$ by visualising it. Consider a curve $\mathcal{C}$ in $\mathbb{R}^2$ with parametrisation $\mathbf{r}(t)$ for $t\in I$ and suppose that $\mathbf{r}$ is differentiable. Let $P$ be the point $\mathbf{r}(t)$ and $Q$ the point $\mathbf{r}(t+h)$. Then the vector $\mathbf{r}(t+h)-\mathbf{r}(t)$ represents the vector from $P$ to $Q$. As $h$ goes to $0$, the point $Q$ moves towards $P$ so that the vector $\mathbf{r}(t+h)-\mathbf{r}(t)$ decreases in length. The vector $\dfrac{1}{h}\left(\mathbf{r}(t+h)-\mathbf{r}(t)\right)$ points in the same direction as the vector $\mathbf{r}(t+h)-\mathbf{r}(t)$, but for $0<h<1$ the length increases again. By inspecting {numref}`Fig:Tangentvector` we see that the vector $\mathbf{r}'(t)$ appears to be tangent to the curve. This leads to the following definition.

:::{figure} images/Fig-Curves3d-Tangentvector2d.png
:name: Fig:Tangentvector
:class: dark-light


:::

:::{todo}
Turn {numref}`Fig:Tangentvector` into an applet consisting of a version in $\mathbb{R}^2$ on the left and one in $\mathbb{R}^3$ on the right. It should also show r(t+h) and r(t+h)-r(t) and $\frac{1}{h}(r(t+h)-r(t))$ with a slider for $h$.
:::

::::::{prf:definition} 
:label: Def:SlopesParamCurves:Tangent
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ parametrised by a differentiable vector function $\mathbf{r}(t)$ for $t\in I$ and let $t_0\in I$. If $\mathbf{r}'(t_0)\neq\mathbf{0}$, the vector $\mathbf{r}'(t_0)$ is known as the **tangent vector** to the curve $\mathcal{C}$ at the point $\mathbf{r}(t_0)$. In that case, the line through the point $\mathbf{r}(t_0)$ with direction vector $\mathbf{r}'(t_0)$ is known as the **tangent line** to the curve. The unit vector in the direction of the tangent vector is known as the **unit tangent vector** $\mathbf{T}(t_0)$ and is given by

$$
 \mathbf{T}(t_0)=\frac{1}{\|\mathbf{r}'(t_0)\|}\mathbf{r}'(t_0).
$$

::::::

For planar curves we can rigorously define the slope.

::::::{prf:definition} 
:label: Def:SlopesParamCurves:Slope
Let $\mathcal{C}$ be a planar parametrised by a differentiable vector function $\mathbf{r}(t)=\begin{pmatrix}x(t)\\ y(t)\end{pmatrix}$ for $t\in I$ and let $t_0\in I$. If $x'(t_0)\neq0$, we call $\dfrac{y'(t_0)}{x'(t_0)}$ the **slope** of $\mathcal{C}$ at $t_0$. We denote this slope by $\dfrac{dy}{dx}$.

::::::

If we imagine a particle following a curve $\mathcal{C}$ defined by the position vector $\mathbf{r}(t)$ then we can think of the tangent vector $\mathbf{r}'(t_0)$ at a certain point $t_0$ in time as the **direction** in which the particle will move next. We will make the concept of a direction more rigorous later on.


::::::{prf:example} 
:label: Ex:SlopesParamCurves:Param
Let $\mathcal{C}$ be the planar curve with parametrisation $\mathbf{r}(t)=\begin{pmatrix}e^{2t}-e^t\\ e^{3t}+4e^{-2t}-3\end{pmatrix}$ for $-\frac12\leq t\leq \frac12$. Suppose we want to find the slope at $t=0$, i.e. at the point $(x,y)=(0,2)$. We find that the vector

$$
 \mathbf{r}'(0)=\begin{pmatrix}-5\\ 1\end{pmatrix}
$$

is a tangent vector to $\mathcal{C}$ at $(0,2)$. This means that the slope is given by

$$
 \dfrac{dy}{dx}=\frac{1}{-5}
$$

and that

$$
 \mathbf{T}(0)=\frac{1}{\|\mathbf{r}'(0)\|}\mathbf{r}'(0)=\begin{pmatrix}\frac{-5}{\sqrt{26}}\\ \frac{1}{\sqrt{26}}\end{pmatrix}
$$

is a unit tangent vector.

:::{applet}
:url: calculus/slopes_of_curves_in_R2/parametric_curve
:name: Fig:SlopeCurve:Param
:class: dark-light

The curve with parametrisation $\mathbf{r}(t)=\begin{pmatrix}e^{2t}-e^t\\ e^{3t}+4e^{-2t}-3\end{pmatrix}$ for $-\frac12\leq t\leq \frac12$ with the tangent line at $t=0$.
:::

::::::

::::::{prf:example} 
:label: Ex:SlopesParamCurves:ParamVert
Let $\mathcal{C}$ be a curve with parametrisation $\mathbf{r}(t)=\begin{pmatrix}t^2+2t\\ t^3\end{pmatrix}$ for $-2\leq t\leq 2$. Suppose we want to find all points on the curve where the tangent line is vertical. A vertical tangent line means that we are dealing with an "infinite slope". For most values of $t$, the slope is given by 

$$
 \frac{dy}{dx}=\frac{\frac{d}{dt}t^3}{\frac{d}{dt}\left(t^2+2t\right)}=\frac{3t^2}{2t+2}.
$$

We see that for $t\neq -1$ this slope is a well-defined number, so there will be no vertical tangent lines for those values of $t$. However, we see that

$$
 \lim_{t\rightarrow -1}\left|\frac{3t^2}{2t+2}\right|=\infty,
$$

since the numerator goes to $3$ while the denominator goes to $0$ as $t\rightarrow -1$. As such, we obtain a vertical tangent line for $t=-1$, which is at the point $(-1,-1)$.

:::{applet}
:url: calculus/slopes_of_curves_in_R2/vertical_tangent_line
:name: Fig:SlopeCurve:ParamVert
:class: dark-light

The curve with parametrisation $\mathbf{r}(t)=\begin{pmatrix}e^{2t}-e^t\\ e^{3t}+4e^{-2t}-3\end{pmatrix}$ for $-2\leq t\leq 2$ with the tangent line at $t=-1$.
:::


::::::



::::::{prf:example} 
:label: Ex:SlopesParamCurves:Helixtang

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
:label: Ex:SlopesParamCurves:Spheretang

Consider any space curve $\mathcal{C}$ with a differentiable parametrisation $\mathbf{r}(t)$ for $t\in I$ that lies on the sphere

$$
 x^2+y^2+z^2=R^2.
$$

Then for any $t\in I$ we have that $\mathbf{r}(t)$ lies on this sphere, so we find $\left|\mathbf{r}(t)\right|=R$. From {prf:ref}`Thm:Vectorfunctions:Normvector` we find that the tangent vector $\mathbf{r}'(t)$ must be orthogonal to the position vector $\mathbf{r}(t)$. This can also be seen in {numref}`Fig:Tangentsphere`.


:::{todo}
Make an applet which shows a curve on a sphere, with a position vector $\mathbf{r}(t)$ and the corresponding tangent vector $\mathbf{r}'(t)$. The applet should have label Fig:Tangentsphere (or change the references).
:::
::::::


## Regularity





If we want to able to define a (unit) tangent vector at each point of a curve defined by the position vector $\mathbf{r}(t)$, the derivative $\mathbf{r}'(t)$ should be nonzero for all relevant values of $t$. This is such an important property that it warrants its own definition.


::::::{prf:definition} 
:label: Def:SlopesParamCurves:Regular
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ parametrised by a differentiable vector function $\mathbf{r}(t)$ for $t\in I$. The paramteric curve $\mathcal{C}$ is **regular** when $\mathbf{r}'$ is continuous and $\mathbf{r}'(t)\neq\mathbf{0}$ for all $t\in I$.

::::::

:::{note}
The regularity of a parametric curve is inherently linked to the parametrisation that is used. As such, some curves have both regular and non-regular parametrisations, see {prf:ref}`Ex:SlopesParamCurves:Regular`.
:::

:::{note}
In some literature, the term smooth curve is used for what we call a regular curve. This is confusing terminology, as it does not match with the definition of smoothness for single-variable function which was given in {prf:ref}`Def:Differentiability:Higherorderderivative` and which is standard terminology. Instead, we will use the term smooth in the context of curves in the same way as we do for single-variable functions, as can be seen from the following definition.
:::

::::::{prf:definition} 
:label: Def:SlopesParamCurves:Smooth
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ parametrised by a differentiable vector function $\mathbf{r}(t)$ for $t\in I$. The paramteric curve $\mathcal{C}$ is **smooth** when the $n$th derivative $\mathbf{r}^{(n)}$ exists for all natural numbers $n$.

::::::


::::::{prf:example} 
:label: Ex:SlopesParamCurves:Regular
Consider the planar curve $\mathcal{C}$ with parametrisation

$$
 \mathbf{r}(t)=\begin{pmatrix} t^3\\ t^6\end{pmatrix}
$$
   
for $-1\leq t\leq 0$, 

$$
 \mathbf{r}(t)=\begin{pmatrix} 0 \\ 0\end{pmatrix}
$$

for $0<t<1$ and 

$$
 \mathbf{r}(t)=\begin{pmatrix} (t-1)^3\\ (t-1)^6\end{pmatrix}
$$

for $1\leq t\leq 2$. Then the vector function $\mathbf{r}$ is differentiable and $\mathbf{r}'$ is continuous. Since $\mathbf{r}'(t)=\mathbf{0}$ for $0\leq t\leq 1$, the curve $\mathcal{C}$ with this parametrisation is not regular.

Note that for each point on the curve we have $(x(t))^2=y(t)$. So the curve is part of the parabola $y=x^2$. As such, a different parametrisation for the same curve would be

$$
 \mathbf{s}(t)=\begin{pmatrix} t\\ t^2\end{pmatrix}
$$

for $-1\leq t\leq 1$. Since $\mathbf{s}'$ is continuous and $\mathbf{s}'(t)\neq \mathbf{0}$ for $-1\leq t\leq 1$ the curve is regular with this parametrisation.

The reason why this first parametrisation is not regular is that if we imagine a particle follows the trajectory prescribed by the position vector $\mathbf{r}(t)$, the particle will rest at the origin for $0\leq t\leq 1$. Since it does not move, it has no direction in which it will go next, so it has no meaningfully defined direction vector. Using the second parametristion, on the other hand, the particle will only be at the origin at $t=0$, which means that it has a meaningful direction.
::::::

::::::{prf:example} 
:label: Ex:SlopesParamCurves:Smooth
To illustrate that regular curves should not be confused with smooth ones, consider the planar curve with parametrisation

$$
 \mathbf{r}(t)=\begin{pmatrix}t^2\\ t^3\end{pmatrix},\qquad -1\leq t\leq 1.
$$

Then the parametrisation is smooth, in the sense that the $n$th derivative $\mathbf{r}^{(n)}$ exists for each natural number $n$. It is not smooth, though, since we note that

$$
 \mathbf{r}'(0)=\begin{pmatrix}0\\ 0\end{pmatrix}.
$$

In addition, we also see the lack of regularity when we plot the curve, since it has a cusp at the origin.

:::{todo}
Inculde an applet with this curve.
:::
::::::


::::::{prf:example} 
:label: Ex:SlopesParamCurves:Sharp
Some curves are not regular, irrespectively of which parametrisation is chosen. Let $\mathcal{C}$ be the planar curve that is the part of the graph of the function 

$$
 y=|x|,\qquad \text{for }-1\leq x\leq 1.
$$

Intuitively, it makes sense that this curve does not have a regular parametrisation: it has a sharp corner at the origin, so there is no way to regularly follow the curve without suddenly changing direction. Let us see if we can make this argument more rigorous.

Consider any parametrisation $\mathbf{r}(t)=\begin{pmatrix} x(t)\\ y(t)\end{pmatrix}$ for $a\leq t\leq b$ and suppose that this parametrisation is regular. Since this curve is the graph of $y=|x|$ we must have $x(t)=y(t)$ when $x(t)\geq 0$ and $x(t)=-y(t)$ when $x(t)<0$. We choose $t_0$ in such a way that $\mathbf{r}(t_0)=\begin{pmatrix}0\\ 0\end{pmatrix}$. Since we assumed that the paramtrisation is regular, we have $\mathbf{r}'(t_0)\neq \mathbf{0}$, so at least one of the two derivatives $x'(t_0)$ and $y'(t_0)$ must be nonzero. Since $x'$ and $y'$ are continuous, the derivative which is nonzero at $t_0$ must be nonzero for $t$ in an open interval $(t_0-\delta,t_0+\delta)$. On this interval, the corresponding function $x(t)$ or $y(t)$ must be strictly monotonic, i.e. either strictly increasing or strictly decreasing. Since $y(t)\geq 0$ for all $t$ and $y(t_0)=0$, $t_0$ must be a local minimum of $y$, so $y$ cannot be strictly monotonic. Hence, $x(t)$ must be strictly monotonic on $(t_0-\delta,t_0+\delta)$.

We now suppose that $x(t)$ is strictly increasing on $(t_0-\delta,t_0+\delta)$. Then for $t<t_0$ we have $x(t)<0$. Since for these values of $t$ we have $y(t)=-x(t)$, $\mathbf{r}'(t)$ must be a constant multiple of $\begin{pmatrix}1\\ -1\end{pmatrix}$. Since $\mathbf{r'}$ is continuous, $\mathbf{r}'(t_0)$ must be a constant multiple of $\begin{pmatrix}1\\ -1\end{pmatrix}$ as well. For $t>t_0$, we have $x(t)>0$, so then we have $y(t)=x(t)$. This means that $\mathbf{r}'(t)$ must be a constant multiple of $\begin{pmatrix}1\\ 1\end{pmatrix}$. By continuity, $\mathbf{r}'(t_0)$ is a constant multiple of $\begin{pmatrix}1\\ 1\end{pmatrix}$. The only vector that is both a constant multiple of $\begin{pmatrix}1\\ -1\end{pmatrix}$ and of $\begin{pmatrix}1\\ 1\end{pmatrix}$ is the zero vector, so $\mathbf{r}'(t_0)=\mathbf{0}$, which gives a contradiction since we assumed that the parametristion is regular. A similar argument holds when $x(t)$ is strictly decreasing.


:::{todo}
Make an applet showing this curve.
:::

::::::

For many curves that we encounter in practice, there are only finitely many points where the parameristation is not differentiable, or where the derivative is either $\mathbf{0}$ or not continuous. Such a curve can be split up into curves that are regular. Let us properly define these curves.

::::::{prf:definition} 
:label: Def:SlopesParamCurves:RegularPiecewise
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ parametrised by a continuous vector function $\mathbf{r}(t)$ for $t\in I$. The paramteric curve $\mathcal{C}$ is **piecewise regular** if there exists a finite set $S$ such that $\mathbf{r}$ is differentiable on $I\setminus S$,  $\mathbf{r}'$ is continuous on $I\setminus S$ and $\mathbf{r}'(t)\neq\mathbf{0}$ for all $t\in I\setminus S$.

::::::


::::::{prf:theorem} 
:label: Thm:SlopesParamCurves:RegularPiecewise
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$. Suppose that $\mathcal{C}$ can be written as $\mathcal{C}=\mathcal{C}_1\cup\mathcal{C}_2\cup\ldots\cup\mathcal{C}_n$, where each $\mathcal{C}_i$ is a curve with a regular parametrisation $\mathbf{r}_i(t)$ for $a_i\leq t\leq b_i$ in such a way that $\mathbf{r}_i(b_i)=\mathbf{r}_{i+1}(a_i)$ for $1\leq i\leq n-1$, i.e. the end point of $\mathcal{C}_i$ is the start point of $\mathcal{C}_{i+1}$. Then $\mathcal{C}$ has a piecewise regular parametristion.

::::::

:::{admonition} Proof of {prf:ref}`Thm:SlopesParamCurves:RegularPiecewise`
:class: tudproof, dropdown
We let $s_1=a_1$ and for $2\leq i\leq n$ we recursively define 

$$
 s_i=s_{i-1}+(b_{i-1}-a_{i-1}).
$$

Then we defined the parametrisation $\mathbf{r}(t)$ for $s_1\leq t\leq s_n+(b_n-a_n)$ 

$$
 \mathbf{r}(t)=\mathbf{r}_i(t-s_i),\qquad\text{when}\ s_i\leq t\leq s_{i+1}.
$$

By construction this vector function is continuous at each point $s_i$, since the end point of the curve $\mathcal{C}_{i-1}$ is the start point of the curve $\mathcal{C}_i$. At all other values of $t$, the parametrisation is differentiable, the derivative is continuous and $\mathbf{r}'(t)\neq\mathbf{0}$, which means that $\mathbf{r}$ is a piecewise regular parametrisation of $\mathcal{C}$.
:::

:::{figure} images/Fig-Curves3d-PiecewiseRegular.png
:name: Fig:PiecewiseRegular
:class: dark-light


:::

:::{todo}
Turn {numref}`Fig:PiecewiseRegular` into an applet. The curve on the right is of course piecewise regular, not piecewise smooth.
:::



::::::{prf:example} 
:label: Ex:SlopesParamCurves:SharpPiecewise
We again consider the curve from {prf:ref}`Ex:SlopesParamCurves:Sharp` that is part of the graph of the function $y=|x|$ for $-1\leq x\leq 1$. We consider the parametrisation

$$
 \mathbf{r}(t)=\begin{pmatrix}t\\ |t|\end{pmatrix}
$$

for $-1\leq t\leq 1$. The vector function $\mathbf{r}$ is continuous and for any $t\neq 0$, it is differentiable and we have $\mathbf{r}'(t)\neq\mathbf{0}$. This means that this parametrised curve is piecewise regular.

We could have also constructed a piecewise regular parametrisation of this curve by making regular parametrisations of the part of the curve with $-1\leq x\leq 0$ and the part with $0\leq x\leq 1$ and by applying  {prf:ref}`Thm:SlopesParamCurves:RegularPiecewise`.
::::::

## Orientation

It is important to note that if $\mathcal{C}$ is a curve defined by the position vector $\mathbf{r}(t)$ and if the tangent vector $\mathbf{r}'$ is nonzero at $\mathbf{r}(a)$ there are *two* vectors of unit length that are tangent to $\mathcal{C}$ at $\mathbf{r}(a)$: the unit tangent vector $\mathbf{T}(a)$ *and* the vector $-\mathbf{T}(a)$, which points in exactly the opposite direction. If you look at the curve from a purely geometrical point of view, there is no reason why we would prefer one of these choices over the other choice. If we have two regular parametrisations of the same curve, then we will see that the unit tangents vectors corresponding to these two parametristions either are the same at each point, or are opposite of each other at each point.

This means that the parametrisation tells us in which **direction** the curve is traversed and that there are two possible choices for this direction. Depending on the curve we are dealing with, we can use terms like "clockwise" or "forward" to describe this direction. 

Let us make these concepts a bit more rigorous. We first cover the case where the curve is not closed, and then the case where the curve is closed.

::::::{prf:theorem} 
:label: Thm:SlopesParamCurves:Orientation
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ and suppose that $\mathbf{r}(t)$ for $t$ in an interval $I_1$ and $\mathbf{s}(t)$ for $t$ in an interval $I_2$ are two regular parametrisations that both cover $\mathcal{C}$ exactly once. Let $\mathbf{T}_r$ and $\mathbf{T}_s$ denote the corresponding unit tangent vectors. Then either for all $s\in I_1$ and $t\in I_2$ with $\mathbf{r}(s)=\mathbf{s}(t)$ we have $\mathbf{T}_r(s)=\mathbf{T}_s$ or for all $s\in I_1$ and $t\in I_2$ with $\mathbf{r}(s)=\mathbf{s}(t)$ we have $\mathbf{T}_r(s)=-\mathbf{T}_s$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:SlopesParamCurves:Orientation`
:class: tudproof, dropdown
By assumption, the function $\mathbf{r}$ is bijective, so it has an inverse function $\mathbf{r}^{-1}:\mathcal{C}\rightarrow I_1$. We define the function

$$
 \phi=\mathbf{r}^{-1}\circ \mathbf{s}.
$$

Note that for each $t\in I_2$ we have

$$
 \left(\mathbf{r}\circ \phi\right)=\mathbf{r}\left(\mathbf{r}^{-1}\mathbf{s}(t)\right)=\mathbf{s}(t),
$$

so we have

$$
 \mathbf{s}=\mathbf{r}\circ \phi.
$$

We will first show that $\phi:I_2\rightarrow I_1$ is differentiable. Choose any $t_0\in I_1$. Since $\mathbf{r}'(t_0)\neq\mathbf{0}$ some component $r_j$ satisfies $r_j'(t_0)\neq 0$. Since $\mathbf{r}'$ is continuous, we can find an interval $I\subset I_1$ with $t_0\in I$ such that $r_j'(t)\neq 0$ for all $t\in I$. By {prf:ref}`Thm:Diffinverse:IFT` the function $r_j:I\rightarrow r_j(I)$ is invertible and $r_j^{-1}:r_j(I)\rightarrow I$ is continuously differentiable. Now for $t\in I$ we write $\mathbf{x}=\mathbf{r}(t)$ and let $x_j$ denote the $j$-th coordinate of $\mathbf{x}$. Then we see that

$$
 \mathbf{r}^{-1}(\mathbf{x})=t=\mathbf{r}_j^{-1}(x_j).
$$

So if $s_j$ denotes the $j$th component of $\mathbf{s}$ we have for $t\in I_2$ with $\mathbf{s}(t)\in \mathbf{r}(I)$ that

$$
 \phi(t)=\mathbf{r}^{-1}(\mathbf{s}(t))=r_j^{-1}(s_j(t)).
$$

Since $\mathbf{s}$ is regular, $s_j$ is differentiable in $t$. Since $r_j^{-1}$ is differentiable at $s_j(t)$, we find that $\phi$ is differentiable at $t$. In particular, $\phi$ is differentiable at $\phi^{-1}(t_0)$. Since $t_0$ was arbitrary and $\phi$ is bijective, $\phi$ is differentiable.

By {prf:ref}`Thm:Vectorfunctions:Basiccomputationrules` we obtain for $t\in I_2$ that

$$
 \mathbf{s}'(t)=\phi'(t)\mathbf{r}'(\phi(t)).
$$

We first show that $\phi'$ is continuous. Fix $t_0\in I_2$. Since $\mathbf{r}$ is regular, we can choose a component $r_j$ of $\mathbf{r}$ such that

$$
 r_j'(\phi(t_0))\neq 0.
$$

Since $r_j'$ and $\phi$ are continuous, we can choose an interval $J\subset I_2$ with $t_0\in J$ such that $r_j'(\phi(t))\neq 0$ for all $t\in J$. Then for $t\in J$, we find

$$
 \phi'(t)=\frac{s_j'(t)}{r_j'(\phi(t))}.
$$

Since both parametrisations are regular, we find that $s_j'$ and $r_j'\circ\phi$ are continuous, so $\phi'$ is continuous.

We now return to the expression

$$
 \mathbf{s}'(t)=\phi'(t)\mathbf{r}'(\phi(t)).
$$

Since both parametrisations are regular, we have $\mathbf{r}'(\phi(t))\neq\mathbf{0}$ and $\mathbf{s}'(t)\neq 0$, so we find $\phi'(t)\neq 0$ for all $t\in I_2$. So we must have either $\phi'(t)>0$ for all $t\in I_2$ or $\phi'(t)<0$ for all $t\in I_2$. Dividing both sides of this expression by their length (which must be the same), we obtain

$$
 \frac{\mathbf{s}'(t)}{\|\mathbf{s}'(t)\|}=\frac{\phi'(t)\mathbf{r}'(\phi(t))}{\|\phi'(t)\mathbf{r}'(\phi(t))\|}=\frac{\phi'(t)}{|\phi'(t)|}\frac{\mathbf{r}'(\phi(t))}{\|\mathbf{r}'(\phi(t))\|}.
$$

In case $\phi'(t)>0$ for all $t\in I_2$ we obtain for all $t\in I_2$ that

$$
 \frac{\mathbf{s}'(t)}{\|\mathbf{s}'(t)\|}=\frac{\mathbf{r}'(\phi(t))}{\|\mathbf{r}'(\phi(t))\|}.
$$

By construction, we have $\mathbf{s}(t)=\mathbf{r}(\phi(t))$, so they describe the same point on the curve $\mathcal{C}$. So in this case, the unit tangent vectors at the curve corresponding to the two different parametrisations are the same at every point. Similarly, in case $\phi'(t)>0$ for all $t\in I_2$ we obtain for all $t\in I_2$ that

$$
 \frac{\mathbf{s}'(t)}{\|\mathbf{s}'(t)\|}=-\frac{\mathbf{r}'(\phi(t))}{\|\mathbf{r}'(\phi(t))\|},
$$

which means that the unit tangent vectors point in opposite directions at every point.

:::

::::::{prf:theorem} 
:label: Thm:SlopesParamCurves:OrientationClosed
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ and suppose that $\mathbf{r}(t)$ for $t$ in an interval $[a,b]$ and $\mathbf{s}(t)$ for $t$ in an interval $[c,d]$ are two regular parametrisations for which the start and endpoint of both paramterisations are the same point $P$, and that both $\mathbf{r}(t)$ for $t\in(a,b)$ and $\mathbf{s}(t)$ for $t\in(c,d)$ cover $\mathcal{C}\setminus\{P\}$ exactly once. Let $\mathbf{T}_r$ and $\mathbf{T}_s$ denote the corresponding unit tangent vectors. Then either for all $s\in (a,b)$ and $t\in (c,d)$ with $\mathbf{r}(s)=\mathbf{s}(t)$ we have $\mathbf{T}_r(s)=\mathbf{T}_s$ or for all $s\in (a,b)$ and $t\in (c,d)$ with $\mathbf{r}(s)=\mathbf{s}(t)$ we have $\mathbf{T}_r(s)=-\mathbf{T}_s$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:SlopesParamCurves:OrientationClosed`
:class: tudproof, dropdown
By assumption, the vector functions $\mathbf{r}$ with domain $(a,b)$ and $\mathbf{s}$ with domain $(c,d)$ are regular parametrisations of the curve $\mathcal{C}\setminus\{P\}$ that both cover this curve exactly once. As such, the result follows directly from  {prf:ref}`Thm:SlopesParamCurves:Orientation`.

:::

::::::{prf:definition} 
:label: Def:SlopesParamCurves:Orientation
Consider the situation of {prf:ref}`Thm:SlopesParamCurves:Orientation` or {prf:ref}`Thm:SlopesParamCurves:OrientationClosed`. If the unit tangent vectors are the same at each point, except possibly at the start/end point in case of a closed curve, we say that the two parametrisations have the **same orientation** and otherwise, we say that they have **opposite orientation**.

A curve $\mathcal{C}$ with a specified orientation is called an **oriented curve**.
::::::

::::::{prf:theorem} 
:label: Thm:SlopesParamCurves:MinC
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ parametrised by a regular parametrisation $\mathbf{r}(t)$ for $t\in [a,b]$. Then the vector function

$$
 \mathbf{s}(t)=\mathbf{r}(a+b-t),\qquad t\in[a,b]
$$

is a regular parametrisation of $\mathcal{C}$ with opposite orientation.


::::::

:::{admonition} Proof of {prf:ref}`Thm:SlopesParamCurves:MinC`
:class: tudproof, dropdown
Note that for each $t\in [a,b]$ we have 

$$
 a+b-t\geq a+b-b=a,\qquad a+b-t\leq a+b-a=b,
$$

so we have $a+b-t\in[a,b]$. This means that $\mathbf{s}(t)$ describes a point on $\mathcal{C}$. Since the function $f(t)=a+b-t$ is bijective and each point on $\mathcal{C}$ is covered by $\mathbf{r}$, each point is also covered by $\mathcal{s}$. So $\mathcal{s}(t)$ for $t\in[a,b]$ is a parametrisation of $\mathcal{C}$. Since $\mathbf{s}=\mathbf{r}\circ f$ for the function $f(t)=a+b-t$, we find with {prf:ref}`Thm:Vectorfunctions:Basiccomputationrules` that $\mathbf{s}$ is differentiable and

$$
 \mathbf{s}'(t)=f'(t)\mathbf{r}'(f(t))=-\mathbf{r}'(a+b-t).
$$

Since $\mathbf{r}$ is regular, $\mathbf{s}'$ is continuous and never $\mathbf{0}$, so $\mathbf{s}$ is regular as well. Finally, the unit tangent vector $\mathbf{T}_s$ for $\mathbf{s}$ can be related to the unit tangent vector $\mathbf{T}_r$ for $\mathbf{r}$ by

$$
 \mathbf{T}_s(t)=\frac{\mathbf{s}'(t)}{\|\mathbf{s}'(t)\|}=\frac{-\mathbf{r}'(a+b-t)}{\|-\mathbf{r}'(a+b-t)\|}=-\mathbf{T}_r(a+b-t).
$$

This means that the two parametrisations correspond to opposite orientations.

:::

::::::{prf:notation} 
:label: Not:SlopesParamCurves:MinC
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ parametrised by a regular parametrisation $\mathbf{r}(t)$ for $t\in [a,b]$. Then the curve $\mathcal{C}$ with the opposite orientation from {prf:ref}`Thm:SlopesParamCurves:MinC` is denoted by $-\mathcal{C}$.


::::::


::::::{prf:example} 
:label: Ex:SlopesParamCurves:Orientation
Let $\mathcal{C}$ be the part of the unit circle

$$
 x^2+y^2=1
$$

with $x<0$. A standard choice for a parametrisation is to consider

$$
 \mathbf{r}(t)=\begin{pmatrix}\cos(t)\\ \sin(t)\end{pmatrix},\qquad \frac{1}{2}\pi\leq t\leq \frac{3}{2}\pi.
$$

A different parametrisation would be to take

$$
 \mathbf{s}(t)=\begin{pmatrix}-\sqrt{1-t^2}\\ t\end{pmatrix},\qquad -1\leq t\leq 1.
$$

Both parametrisations are regular. For the first one, we can find the unit tangent vector

$$
 \mathbf{T}_r(t)=\frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}=\frac{1}{\sqrt{\left(-\sin(t)\right)^2+\left(\cos(t)\right)^2}}\begin{pmatrix}-\sin(t)\\ \cos(t)\end{pmatrix}=\begin{pmatrix}-\sin(t)\\ \cos(t)\end{pmatrix},
$$

while for the second one we obtain

$$
 \mathbf{T}_s(T)=\frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}=\frac{1}{\sqrt{\left(\frac{t}{\sqrt{1-t^2}}\right)^2+1^2}}\begin{pmatrix}\frac{t}{\sqrt{1-t^2}}\\ 1\end{pmatrix}=\begin{pmatrix}t\\ \sqrt{1-t^2}\end{pmatrix}.
$$

We see that for the first parametrisation, the $y$-component of the unit tangent vector is always negative (since we have $\frac{1}{2}\pi\leq t\leq\frac{3}{2}\pi$), while for the second parametrisation, the $y$-component of the unit tangent vector is always positive. This means that the two parametrisations have opposite orientations. 

We can also see this graphically. The first parametrisation starts at $\begin{pmatrix}0\\ 1\end{pmatrix}$ and moves counterclockwise until it hits $\begin{pmatrix} 0\\ -1\end{pmatrix}$. On the other hand, the second parametrisation starts at $\begin{pmatrix}0\\ -1\end{pmatrix}$ and moves counterclockwise until it hits $\begin{pmatrix} 0\\ 1\end{pmatrix}$. As such, we say that the first parametrisation is a **counterclockwise parametrisation**, while the second one is a **clockwise parametrisation**.

:::{todo}
Include an applet where the curve is visible, as well as the two unit tangent vectors which should be draggable across the curve.
:::

::::::

::::::{prf:example} 
:label: Ex:SlopesParamCurves:OrientationClosedCounterEx

In {prf:ref}`Thm:SlopesParamCurves:OrientationClosed` we specifically did not say that there are only two possibilities for the unit tangent vector at the start/end point of a closed curve with a regular parametrisation. In some cases, there are more options. Consider the planar curve $\mathcal{C}$ with the parametrisation

$$
 \mathbf{r}(t)=\begin{cases} \begin{pmatrix} t\\ t\end{pmatrix},\qquad &0\leq t\leq 1,\\
 \begin{pmatrix}\frac{3}{2}-\frac{1}{2}(t-2)^2\\ (t-2)^3-2(t-2)\end{pmatrix},\qquad &1<t<4, \\
 \begin{pmatrix}4-t\\ t-4\end{pmatrix},\qquad &3\leq t\leq 4.\end{cases}
$$


The formula for $1<t<3$ is chosen in such a way that $\mathbf{r}$ and $\mathbf{r}'$ are continuous. We have

$$
 \mathbf{r}'(t)=\begin{cases}\begin{pmatrix}1\\ 1\end{pmatrix},\qquad &0\leq t\leq 1,\\
 \begin{pmatrix}-(t-2)\\ 3(t-2)^2-2\end{pmatrix} \qquad &1<t<3, \\
 \begin{pmatrix}-1\\ 1\end{pmatrix},\qquad &3\leq t\leq 4.\end{cases}
$$

Then we can directly see that $\mathbf{r}$ and $\mathbf{r}'$ are indeed continuous. We observe that $\mathbf{r}'(t)\neq \mathbf{0}$ for all $0\leq t\leq 4$, so the parametrisation is regular. The curve is closed, since $\mathbf{r}(0)=\mathbf{r}(4)=\begin{pmatrix}0\\ 0\end{pmatrix}$. The unit tangent vector at $t=0$ is given by

$$
 \mathbf{T}(0)=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ 1\end{pmatrix},
$$

while the one at $t=1$ is given by

$$
 \mathbf{T}(4)=\frac{1}{\sqrt{2}}\begin{pmatrix}-1\\ 1\end{pmatrix}.
$$

Note that $\mathbf{T}(4)$ is neither $\mathbf{T}(0)$ nor $-\mathbf{T}(0)$. By alternatively considering the curve $-\mathcal{C}$ given by {prf:ref}`Thm:SlopesParamCurves:MinC` we see that this curve has (at least) four possible unit tangent vectors at the origin: $\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ 1\end{pmatrix}$, $\frac{1}{\sqrt{2}}\begin{pmatrix}-1\\ 1\end{pmatrix}$, $\frac{1}{\sqrt{2}}\begin{pmatrix}-1\\ -1\end{pmatrix}$ and $\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ -1\end{pmatrix}$.

The reason for this is because the curve has a sharp corner at the origin. Since the origin is the start and end point of the curve, this does not directly reflect back in the regularity of the parametrisation. It does mean that the curve has several different tangent directions at the origin.

:::{todo}
Include an applet showing the curve.
:::
::::::