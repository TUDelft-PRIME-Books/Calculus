(Section:ArcLength)=

# Arc length

- Arc length
- Arc-length parametrisations
- Maybe integrals using arc-length parametrisation



## Arc length

When a curve describes the position of a wire, it is a natural question to want to know the length $L$ of the wire. In the context of parametric curves, this length is known as the **arc length** of the curve. Consider a curve $\mathcal{C}$ with regular parametrisation $\mathbf{r}(t)$ for $a\leq t\leq b$, which is shown in the figure below.

:::{figure} images/Fig_Curves3d-Arclengthstart.png
:name: Fig:ArclengthStart
:class: dark-light

:::

:::{todo}
Turn {numref}`Fig:ArclengthStart` into an applet. 
:::

In order to find the arc length of this curve, we take an approach that closely resembles the construction of a Riemann sum from {numref}`Sec:Integration:DefiniteIntegrals`. Geometrically, we only know how to find lengths of straight-line pieces. As such, we will approximate the length of the curve by the length of a different curve which only consists of straight-line pieces. To do so, we divide the interval $[a,b]$ into $N$ subintervals of equals width $\Delta t=\dfrac{b-a}{N}$. We let $\Delta s_n$ denote the arc length of $\mathcal{C}$ between $\mathbf{r}(t_{n-1})$ and $\mathbf{r}(t_n)$. We approximate $\Delta s_n$ by the length of the straight-line piece between $\mathbf{r}(t_{n-1})$ and $\mathbf{r}(t_n)$, so we have

$$
 \Delta s_n\approx\|\mathbf{r}(t_n)-\mathbf{r}(t_{n-1})\|.
$$

This approximation can be seen in the figure below.

:::{figure} images/Fig_Curves3d-Arclengthapprox.png
:name: Fig:Arclengthapprox
:class: dark-light

:::

:::{todo}
Turn {numref}`Fig:Arclengthapprox` into an applet. Make sure to use subscripts $n$ instead of $i$. It would also be nice if $N$ could be varied.
:::


We can then approximate the total arc length $L$ by

$$
 L=\sum_{n=1}^N \Delta s_i\approx \sum_{n=1}^N\|\mathbf{r}(t_n)-\mathbf{r}(t_{n-1})\|.
$$

For larger values of $N$, this approximation gets better and taking the limit as $N\rightarrow \infty$, we obtain the actual length of the curve. This gives rise to the following definition.


::::::{prf:definition} 
:label: Def:ArcLength:Arclength
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ with a continuous parametrisation $\mathbf{r}(t)$ for $t\in [a,b]$ that covers all except possibly finitely many points on the curve exactly once. Then the **arc length** $L$ of $\mathcal{C}$ is equal to the limit

$$
 L=\lim_{N\rightarrow\infty} \sum_{n=1}^N\|\mathbf{r}(t_n)-\mathbf{r}(t_{n-1})\|,\text{ with }\Delta t=\dfrac{b-a}{N}\text{ and }t_n=a+n\Delta t,
$$

provided that this limit exists.


::::::

The formula that we have used to define the arc length is not useful at all for computing the arc length, so we have to do something smarter. We recall that we divided the interval $[a,b]$ into subintervals with equal width $\Delta t$. As such, we can write

$$
 L=\lim_{N\rightarrow\infty} \sum_{n=1}^N\left\|\mathbf{r}(t_n)-\mathbf{r}(t_{n-1})\right\|=\lim_{N\rightarrow\infty}\sum_{n=1}^N\left\|\dfrac{\mathbf{r}(t_{n})-\mathbf{r}(t_{n-1})}{\Delta t}\right\|\Delta t.
$$

Initially, it might seem that we made this expression needlessly complicated, but, fortunately, this is not the case. We will now assume that the curve is a space curve, though the argument is very similar for planar curves, and we write $\mathbf{r}(t)=\begin{pmatrix}r_1(t)\\ r_2(t)\\ r_3(t)\end{pmatrix}$. For now, we fix $N\geq 1$. Using {prf:ref}`Thm:MinMax:MVT` we can find, for each $1\leq n\leq N$ three numbers $p_n$, $q_n$ and $s_n$ in the interval $[t_{n-1},t_n]$ with

$$
 \dfrac{r_1(t_{n})-r_1(t_{n-1})}{\Delta t}=r_1'(p_n),\quad \dfrac{r_2(t_{n})-r_2(t_{n-1})}{\Delta t}=r_2'(q_n),\quad \dfrac{r_3(t_{n})-r_3(t_{n-1})}{\Delta t}=r_3'(s_n).
$$

As such, we obtain

$$
\begin{align*}
 \sum_{n=1}^N\left\|\dfrac{\mathbf{r}(t_{n})-\mathbf{r}(t_{n-1})}{\Delta t}\right\|\Delta t&=\sum_{n=1}^N\sqrt{\left(\dfrac{r_1(t_{n})-r_1(t_{n-1})}{\Delta t}\right)^2+\left(\dfrac{r_2(t_{n})-r_2(t_{n-1})}{\Delta t}\right)^2+\left(\dfrac{r_3(t_{n})-r_3(t_{n-1})}{\Delta t}\right)^2}\Delta t\\
 &=\sum_{n=1}^N\sqrt{\left(r_1'(p_n)\right)^2+\left(r_2'(q_n)\right)^2+\left(r_3'(s_n)\right)^2}\Delta t.
\end{align*}
$$

This expression very much resembles a Riemann sum for the function

$$
 \sqrt{\left(r_1'\right)^2+\left(r_2'\right)^2+\left(r_3'\right)^2}.
$$

The only reason it is not an actual Riemann sum is because there is no way to guarantee that $p_n=q_n=s_n$. Fortunately, it can be shown that if the derivative $\mathbf{r}'$ is continuous, the difference between this expression and the actual Riemann sum vanishes as $N\rightarrow\infty$, though we will not give a formal proof of this statement. As such, we find that

$$
\begin{align*}
 L&=\lim_{n\rightarrow\infty}\sum_{n=1}^N\sqrt{\left(r_1'(p_n)\right)^2+\left(r_2'(q_n)\right)^2+\left(r_3'(s_n)\right)^2}\Delta t\\
 &=\lim_{n\rightarrow\infty}\sum_{n=1}^N\sqrt{\left(r_1'(p_n)\right)^2+\left(r_2'(p_n)\right)^2+\left(r_3'(p_n)\right)^2}\Delta t\\
 &=\int_a^b \sqrt{\left(r_1'(t)\right)^2+\left(r_2'(t)\right)^2+\left(r_3'(t)\right)^2}\,dt\\
 &=\int_a^b \|\mathbf{r}'(t)\|\,dt.
\end{align*}
$$

Speaking in kinetic terms, we obtain the length of the curve by taking the integral of the speed, which makes sense if you think about the length of the curve as the distance travelled by following the curve. In general, we obtain the following result.

::::::{prf:theorem} 
:label: Thm:ArcLength:ArclengthCompute
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ with a regular parametrisation $\mathbf{r}(t)$ for $t\in [a,b]$ that covers all except possibly finitely many points on the curve exactly once. Then the arc length $L$ of $\mathcal{C}$ can be evaluated as

$$
 L=\int_a^b \|\mathbf{r}'(t)\|\,dt.
$$

::::::

For piecewise regular curves, we can break the curve into regular pieces, evaluate the length of each piece and add them back together.

::::::{prf:theorem} 
:label: Thm:ArcLength:RegularPiecewise
Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$. Suppose that $\mathcal{C}$ can be written as $\mathcal{C}=\mathcal{C}_1\cup\mathcal{C}_2\cup\ldots\cup\mathcal{C}_n$, where each $\mathcal{C}_i$ is a curve with a regular parametrisation $\mathbf{r}_i(t)$ for $a_i\leq t\leq b_i$ in such a way that $\mathbf{r}_i(b_i)=\mathbf{r}_{i+1}(a_i)$ for $1\leq i\leq n-1$, i.e. the end point of $\mathcal{C}_i$ is the start point of $\mathcal{C}_{i+1}$. Then the arc length $L$ of $\mathcal{C}$ is given by

$$
 L=\sum_{i=1}^n \int_{a_i}^{b_i}\|\mathbf{r}_i'(t)\|\,dt.
$$

::::::

In principle, the length of a curve should be a geometrical property of the curve, and should not depend on the chosen parametrisation. Fortunately, this is the case as can be seen from the following result.

::::::{prf:theorem} 
:label: Thm:ArcLength:ArclengthParamChoice

Let $\mathcal{C}$ be a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ and suppose that $\mathbf{r}(t)$ for $t$ in an interval $[a,b]$ and $\mathbf{s}(t)$ for $t$ in an interval $[c,d]$ are two regular parametrisations that both cover all except possibly finitely many points on $\mathcal{C}$ exactly once. Then we have

$$
 \int_{a}^b \|\mathbf{r}'(t)\|\,dt=\int_c^d\|\mathbf{s}'(t)\|\,dt.
$$

::::::

::::{admonition} Proof of {prf:ref}`Thm:ArcLength:ArclengthParamChoice`
:class: tudproof, dropdown
We choose parameter values

$$
 c=t_0<t_1<\ldots<t_n=d
$$


such that for each $t\in (t_{i-1},t_i)$ the point $\mathbf{s}_i(t)$ is covered once by both parametrisations. Let $1\leq i\leq m$. Following the proof of {prf:ref}`Thm:SlopesParamCurves:Orientation` there exists a differentiable, injective function $\phi_i$ with domain $ (t_{i-1},t_i)$ such that

$$
 \mathbf{s}(t)=\mathbf{r}(\phi_i(t))
$$

for each $t\in (t_{i-1},t_i)$. Let $(u_{i_1},u_i)$ donote the range of $\phi_i$. In the proof of {prf:ref}`Thm:SlopesParamCurves:Orientation` we have seen that 

$$
 \mathbf{s}'(t)=\mathbf{r}'(\phi_i(t))\phi_i'(t)
$$

for all $t\in (t_{i-1},t_i)$, and we have seen that either $\phi_i'>0$ on $(t_{i-1},t_i)$ or $\phi_i'<0$ on $(t_{i-1},t_i)$. Then we obtain

$$
 \int_{t_{i-1}}^{t_i}\|\mathbf{s}'(t)\|\,dt=\int_{t_{i-1}}^{t_i}|\phi'(t)|\,\|\mathbf{r}'(\phi_i(t))\|\,dt.
$$

First we assume that $\phi_i'>0$ on $(t_{i-1},t_i)$. Since $\phi$ is bijective from $(t_{i-1},t_i)$ to $(u_{i-1},u_i)$ and since $\mathbf{r}$ and $\mathbf{s}$ are continuous, we can continuously extend $\phi$ to $[t_{i-1},t_i]$ by setting $\phi(t_{i-1})=u_{i-1}$ and $\phi(t_i)=u_i$. Then we can perform the substitution $u=\phi(t)$ to obtain

$$
 \int_{t_{i-1}}^{t_i}|\phi'(t)|\,\|\mathbf{r}'(\phi_i(t))\|\,dt=\int_{\phi(t_{i-1})}^{\phi(t_i)}\|\mathbf{r}'(u)\|\,du=\int_{u_{i-1}}^{u_i}\|\mathbf{r}'(u)\|\,du.
$$

Similarly, we assume that $\phi_i'<0$ on $(t_{i-1},t_i)$. Since $\phi$ is bijective from $(t_{i-1},t_i)$ to $(u_{i-1},u_i)$ and since $\mathbf{r}$ and $\mathbf{s}$ are continuous, we can continuously extend $\phi$ to $[t_{i-1},t_i]$ by setting $\phi(t_{i-1})=u_{i}$ and $\phi(t_i)=u_{i-1}$. Then we can perform the substitution $u=\phi(t)$ to obtain

$$
 \int_{t_{i-1}}^{t_i}|\phi'(t)|\,\|\mathbf{r}'(\phi_i(t))\|\,dt=-\int_{t_{i-1}}^{t_i}\phi'(t)\,\|\mathbf{r}'(\phi_i(t))\|\,dt=-\int_{\phi(t_{i-1})}^{\phi(t_i)}\|\mathbf{r}'(u)\|\,du=-\int_{u_{i}}^{u_{i-1}}\|\mathbf{r}'(u)\|\,du=\int_{u_{i-1}}^{u_i}\|\mathbf{r}'(u)\|\,du.
$$

By assumption, the vectors $\mathbf{r}(u)$ for $u$ in intervals of the form $(u_{i-1},u_i)$ cover all but finitely many points in $(a,b)$. We, therefore, obtain

$$
 \int_{a}^b \|\mathbf{r}'(t)\|\,dt=\sum_{i=1}^n\int_{u_{i-1}}^{u_i}\|\mathbf{r}'(t)\|\,dt=\sum_{i=1}^n\int_{t_{i-1}}^{t_i}\|\mathbf{s}'(t)\|\,dt=\int_c^d \|\mathbf{s}'(t)\|\,dt.
$$

::::


::::::{prf:example} 
:label: Ex:ArcLength:ArclengthHelix

We again consider the space curve $\mathcal{C}$ with parametrisation $\mathbf{r}(t)=\begin{pmatrix}4\cos(2t)\\ 4\sin(2t)\\ t\end{pmatrix}$ for $0\leq t\leq 3\pi$ from {prf:ref}`Ex:Curves3d:Helix`. Then we have

$$
 \mathbf{r}'(t)=\begin{pmatrix}-8\sin(2t)\\ 8\cos(2t)\\ 1\end{pmatrix},
$$

so using {prf:ref}`Thm:ArcLength:ArclengthCompute` the arc length $L$ of this curve can be computed as

$$
\begin{align*}
 L&=\int_{0}^{3\pi}\|\mathbf{r}'(t)\|\,dt\\
 &=\int_0^{3\pi}\sqrt{\left(-8\cos(2t)\right)^2+\left(8\cos(2t)\right)^2+1^2}\,dt\\
 &=\int_0^{3\pi}\sqrt{64\left(\cos^2(2t)+\sin^2(2t)\right)+1}\,dt
 &=\int_0^{3\pi}\sqrt{64+1}\,dt
 &=3\pi\sqrt{65}.
\end{align*}
$$

In this computation, we used the identity

$$
 \cos^2(2t)+\sin^2(2t)=1,
$$

which follows from {prf:ref}`Thm:Trigonometry:UnitCircleIdentity`.

::::::

Since graphs of single-variable functions are curves, we can now also compute their arc lengths.

::::::{prf:theorem} 
:label: Thm:ArcLength:ArclengthFunction1d

Let $f:[a,b]\rightarrow\mathbb{R}$ be a continuously differentiable function. Then the arc length $L$ of the graph of $f$ for $a\leq x\leq b$ is given by

$$
 L=\int_a^b \sqrt{1+\left(f'(x)\right)^2}\,dx.
$$

::::::

::::{admonition} Proof of {prf:ref}`Thm:ArcLength:ArclengthFunction1d`
:class: tudproof, dropdown
A paramterisation for the graph of $f$ is given by

$$
 \mathbf{r}(x)=\begin{pmatrix}x\\ f(x)\end{pmatrix}
$$

for $a\leq x\leq b$, which has

$$
 \mathbf{r}'(x)=\begin{pmatrix}1\\ f'(x)\end{pmatrix}
$$

Since $f$ is continuously differentiable, the parametrisation is regular. So using {prf:ref}`Thm:ArcLength:ArclengthCompute` we find

$$
 L=\int_a^b\|\mathbf{r}'(x)\|\,dx=\int_a^b \sqrt{1^2+\left(f'(x)\right)^2}\,dx.
$$

::::

The major limitation of this rule that that integrals of functions of the form $\sqrt{1+\left(f'(x)\right)^2}$ are often very hard to compute, as can be seen from the following example. 

::::::{prf:example} 
:label: Ex:ArcLength:ArclengthFunction1d

Consider the function $f(x)=\dfrac{1}{2}x^2$ for $1\leq x\leq 2$. Then according to {prf:ref}`Thm:ArcLength:ArclengthFunction1d` the arc length $L$ of the graph of $f$ is given by

$$
 L=\int_1^2 \sqrt{1+\left(f'(x)\right)^2}\,dx=\int_1^2 \sqrt{1+x^2}\,dx.
$$

Using an approach similar to {prf:ref}`Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample2` it can be shown that

$$
 \int \sqrt{1+x^2}\,dx=\frac{1}{2}x\sqrt{x^2+1}+\frac{1}{2}\ln\left(\sqrt{x^2+1}+x\right)+C.
$$

As such, the arc length is given by

$$
\begin{align*}
 L&=\int_1^2 \sqrt{1+x^2}\,dx\\
 &=\left[\frac{1}{2}x\sqrt{x^2+1}+\frac{1}{2}\ln\left(\sqrt{x^2+1}+x\right)\right]_1^2\\
 &=\sqrt{5}+\frac{1}{2}\ln\left(\sqrt{5}+2\right)-\frac{1}{2}\sqrt{2}-\frac{1}{2}\ln\left(\sqrt{2}+1\right)\\
 &=\sqrt{5}-\frac{1}{2}\sqrt{2}+\frac{1}{2}\ln\left(\frac{\sqrt{5}+2}{\sqrt{2}+1}).
\end{align*}
$$

Approximately, we find $L\approx 1.81$. This number makes sense, as the straight line piece from $\left(1,\frac{1}{2}\right)$ to $\left(2,2\right)$ has length $1.75$, which is also the shortest distance between these two points. Since the graph of $f$ is not a straight line, its length should, indeed, be slightly larger than $1.75$.
::::::

## Arc length parametrisation

One major disadvantage of using parametrisations to describe curves, is that when plotting the curve the parameter is no longer visible. If we imagine the parametrisation describing the position of a particle that follows the curve, we cannot "see" in the curve itself where the particle is at which moment in time, nor what its velocity is. In this sense, it would be convenient to have a parametrisation where this is possible. One way to ensure this is to make sure that the particle traverses the curve with constant speed. The so-called **arc length parametrisation** has precisely this property. In order to construct this parametrisation for a given curve, we first need to introduce the arc length function.


VOORBEELD ARCLENGTH FUNCTIE EN TEKST ERVOOR MOET NOG.