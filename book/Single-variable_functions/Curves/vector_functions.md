# Vector functions

## Introduction

As we will see in the upcoming sections, an essential component of the description of a curve in $\mathbb{R}^2$ or $\mathbb{R}^3$ is the position function $\mathbf{r}(t)$, which is a function of which the domain is a subset of $\mathbb{R}$ and the codomain is $\mathbb{R}^2$ or $\mathbb{R}^3$. Such a function is known as a **vector function**. Although the focus of this chapter is mostly on curves in $\mathbb{R}^2$ or $\mathbb{R}^3$, it takes little effort to study vector function is the more general setting where these functions have $n$ components. Since the component functions of $\mathbf{r}$ are single-variable functions, we know how concepts like limits, derivatives and integrals work for these component functions. In this section, we extend these concepts to vector functions. 

## Basic concepts

In {numref}`Subsec:Functions1dConcepts` we defined the most important concepts related to functions in their most general form. We will repeat some of these definitions, in some cases specifically in the context of vector functions.

::::::{prf:definition} 
:label: Def:Vectorfunctions:Function

Let $n\geq 2$ be an integer. Then we call a function $\mathbf{r}:D\rightarrow \mathbb{R}^n$ with $D\subset \mathbb{R}$ a **vector function** or a **vector-valued function**.

If we want to emphasize that the codomain of $\mathbf{r}$ is $\mathbb{R}^n$, we call $\mathbf{r}$ an **$\mathbb{R}^n$-valued vector function** or a **vector function with values in $\mathbb{R}^n$**.

For $t\in D$ we write $\mathbf{r}(t)=\begin{pmatrix}r_1(t)\\ \vdots \\ r_n(t)\end{pmatrix}$. Then for $1\leq i\leq n$ the single-variable function $t\mapsto r_i(t)$ is called the **$i$th component function** of $\mathbf{r}(t)$. 

::::::



::::::{prf:notation} 
:label: Notation:Vectorfunctions:Codomain

If we do not explicitly specify the domain and/or codomain of a vector function $\mathbf{r}$, we use the symbols $D_{\mathbf{r}}$ for the domain of $\mathbf{r}$ and $C_{\mathbf{r}}$ for the codomain of $\mathbf{r}$.
::::::


:::{note}
In the most common applications of vector functions (especially those with values in $\mathbb{R}^3$), the output, which describes for instance position or velocity, is a function of time $t$. As such, it is customary, though by no means necessary, to use the symbol $t$ for the input variable.
:::

::::::{prf:definition} 
:label: Def:Vectorfunctions:Range

Let $\mathbf{r}$ be a $\mathbb{R}^n$-valued vector function with domain $D$. Then the **range** $R$, sometimes also called the **trajectory**, of $\mathbf{r}$ is the set of all function values of $\mathbf{r}$. That is, we have

$$
 R=\left\{\mathbf{v}\,\,\text{in}\,\,\mathbb{R}^n\,\middle|\,\text{There is an }t\,\text{in}\,D\,\text{with}\,\mathbf{r}(t)=\mathbf{v}\right\},
$$

which can be written more compactly as

$$
 R=\left\{\mathbf{r}(t)\,\middle|\,t\,\text{in}\,D\right\}.
$$
::::::



Since the component functions of a vector function are single-variable functions, most of these component functions that we will encounter are described by a formula. 

::::::{prf:definition} 
:label: Def:Vectorfunctions:MaxDomain

Let $\mathbf{r}$ be a vector function with component functions $r_1,\ldots,r_n$ and suppose that each of these component functions is defined by a formula. Then the **maximal domain** of $\mathbf{r}$ is the intersection of the maximal domains of the component functions $r_1,\ldots,r_n$. That is, it consists of those $t$ for which the formulas for $r_1,\ldots,r_n$ all produce a real number for this $t$.

::::::


::::::{important}
Whenever we define a vector function by means of a formula for each component function and we do not specify the domain, we assume that the domain is the maximal domain. 
::::::


Just like with any function, we can consider the **graph** of a vector function. From {numref}`Subsec:Functions1dConcepts` we recall that the graph $G$ of a vector function $\mathbf{r}$ is given by

$$
 G=\left\{(t,\mathbf{r}(t))\,\middle|\,t\in D_f\right\}.
$$

[^FootnoteGraph]: The graph of an $\mathbb{R}^2$-valued vector function is a subset of $\mathbb{R}\times \mathbb{R}^2$, which we can identify with $\mathbb{R}^3$. We could use one axis for the input variable and the other two for the two output variables.
[^FootnoteParam]: Later, we will call these different parametrisations of the same curve.

However, for $\mathbb{R}^2$-valued vector functions it is possible to plot the graph[^FootnoteGraph], this is not the customary way to graphically represent vector functions. Instead, we usually simply plot the **range** of the vector function. In this context, we often refer to the range as the trajectory of the vector function. Here we already see a preview of the connection with curves that we will establish later: for many $\mathbb{R}^2$-valued vector functions the range looks like a line in $\mathbb{R}^2$ that is not necessarily straight. Similarly, the range of an $\mathbb{R}^3$-valued vector function often looks like a line in $\mathbb{R}^3$ that is not necessarily straight. Of course, this presents us with one major disadvantage: it is not possible to retrace which input value(s) correspond to a given point on this trajectory. On the upside: this does allow us to identify different vector functions that have the same range[^FootnoteParam].

::::::{prf:example} 
:label: Ex:Vectorfunctions:BasicCircle
We consider the vector function $\mathbf{r}:[0,2\pi)\rightarrow\mathbf{R}^2$ given by $\mathbf{r}(t)=\begin{pmatrix} \cos(t)\\ \sin(t)\end{pmatrix}$. The component functions $r_1$ and $r_2$ of this vector function are given by

$$
 r_1(t)=\cos(t),\qquad r_2(t)=\sin(t).
$$

If we write $x=\cos(t)$ and $y=\sin(t)$, then we find that 


$$
 x^2+y^2=\left(\cos(t)\right)^2+\left(\sin(t)\right)^2=1,
$$ 

so that the point $(x,y)=(\cos(t),\sin(t))$ lies on the unit circle. In fact, if we interpret $t$ as the angle of the arc between the origin and a point $(x,y)$ with the positive axis, measured counter-clockwise, then each point $(x,y)$ on the unit circle can be represented uniquely as $(x,y)=(\cos(t),\sin(t))$ for some $0\leq t<2\pi$. In particular, the range of $\mathbf{r}$ is the unit circle. In {numref}`Sec:CurvesR2` we will interpret the vector function $\mathbf{r}$ as a parametrisation of the unit circle.


:::{applet}
:url: calculus/curves_in_R%5E2/parametrisation_of_the_unit_circle
:name: Fig:Vectorfunctions:BasicCircle
:class: dark-light

The range of the vector function $\mathbf{r}(t)$ is the unit circle.
:::
::::::


## Limits and continuity

In order to generalise concepts such as limits, derivatives and integrals to vector functions, we start, as usual, with limits.

::::::{prf:definition} 
:label: Def:Vectorfunctions:Limit
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function such that the domain of $\mathbf{r}$ contains an open interval of the form $\left(c_1,a\right)$ or $\left(a,c_2\right)$. 

Then we say that the **limit** of $\mathbb{R}$ as $t$ approaches $a$ is equal to $\mathbf{v}$, and we write $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{v}$, whenever for each $\varepsilon>0$ there exists a $\delta>0$, such that for all $t$ in the domain of $\mathbf{r}$ with $0<|t-a|<\delta$, we have $\|\mathbf{r}(t)-\mathbf{v}\|<\varepsilon$.
::::::

Evaluating limits using this definitions sounds (and, admittedly, is) rather cumbersome, but fortunately, we can use all the techniques that we learned previously for single-variable functions by using the following result.

::::::{prf:theorem} 
:label: Thm:Vectorfunctions:Limit
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function such that the domain of $\mathbf{r}$ contains an open interval of the form $\left(c_1,a\right)$ or $\left(a,c_2\right)$. Write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$ and $\mathbf{v}=\begin{pmatrix}v_1\\ \vdots\\ v_n\end{pmatrix}$.

Then we have $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{v}$ if, and only if, for all $1\leq k\leq n$ we have $\lim\limits_{t\rightarrow a}x_k(t)=v_k$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Vectorfunctions:Limit`
:class: tudproof, dropdown
First suppose that $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{v}$ and let $1\leq k\leq n$. Let $\varepsilon>0$ be given and pick $\delta>0$ such that for for all $t$ in the domain of $\mathbf{r}$ with $0<|t-a|<\delta$, we have $\|\mathbf{r}(t)-\mathbf{v}\|<\varepsilon$. Then for such a value of $t$ we have

$$
 |x_k(t)-v_k|\leq \sqrt{(x_1(t)-v_1)^2+\ldots +(x_n(t)-v_n)^2}=\|\mathbf{r}(t)-\mathbf{v}\|<\varepsilon.
$$

By definition, we have $\lim\limits_{t\rightarrow a}x_k(t)=v_k$.

Now suppose that for all $1\leq k\leq n$ we have $\lim\limits_{t\rightarrow a}x_k(t)=v_k$. Note that by construction the component functions $x_1,\ldots,x_n$ have the same domain as $\mathbf{r}$. Let $\varepsilon>0$ be given. For each $1\leq k\leq n$, we pick $\delta>0$ such that for for all $t$ in the domain of $\mathbf{r}$ with $0<|t-a|<\delta_k$, we have $|x_k(t)-v_k|<\dfrac{\varepsilon}{\sqrt{k}}$. Let $\delta=\mathrm{min}\left\{\delta_1,\ldots,\delta_k\right\}$, i.e. $\delta$ is the smallest of each of the $\delta_k$. Then for $t$ in the domain of $\mathbf{r}$ with $0<|t-a|<\delta$ we have

$$
\begin{align*}
 \|\mathbf{r}(t)-\mathbf{v}\|&=\sqrt{(x_1(t)-v_1)^2+\ldots +(x_n(t)-v_n)^2}\\
 &\leq \sqrt{\left(\frac{\varepsilon}{\sqrt{k}}\right)^2+\ldots+\left(\frac{\varepsilon}{\sqrt{k}}\right)^2}\\
 &=\sqrt{k\frac{\varepsilon^2}{k}}\\
 =\varepsilon.
\end{align*}
$$

We conclude that $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{v}$.
:::

For continuity we use a similar setup: we first give the definition in terms of $\delta$s and $\varepsilon$s and then link continuity of vector functions to continuity of the component functions.

::::::{prf:definition} 
:label: Def:Vectorfunctions:Cont
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function and $a$ a point in the domain of $\mathbf{r}$. Then we say that $f$ is **continuous** at $a$ whenever for each $\varepsilon>0$ there exists a $\delta>0$ such that for every $t$ in the domain of $f$ with $|t-a|<\delta$ we have $\|\mathbf{r}(t)-\mathbf{r}(a)\|<\varepsilon$. If $\mathbf{r}$ is not continuous at $a$, we say that it is **discontinuous** at $a$.

If $\mathbf{r}$ is continuous at each point in its domain, we say that $\mathbf{r}$ is **continuous**.
::::::


::::::{prf:theorem} 
:label: Thm:Vectorfunctions:Cont
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function such that the domain of $\mathbf{r}$ contains an open interval of the form $\left(c_1,a\right]$ or $\left[a,c_2\right)$. Write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$.

Then $\mathbf{r}$ is continuous at $a$ if, and only if, for all $1\leq k\leq n$ the function $x_k$ is continuous at $a$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Vectorfunctions:Cont`
:class: tudproof, dropdown
It follows directly from the definition of a limit that, with these conditions on the domain of $\mathbf{r}$, $\mathbf{r}$ is continuous at $a$ if, and only if, $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{r}(a)$.

First suppose that $\mathbf{r}$ is continuous at $a$ and let $1\leq k\leq n$. Then we have $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{r}(a)$, so by {prf:ref}`Thm:Vectorfunctions:Limit` we have $\lim\limits_{t\rightarrow a}x_k(t)=x_k(a)$. It then follows from {prf:ref}`Theorem:Continuity:EpsilonDelta` that $x_k$ is continuous at $a$.

Now suppose that for all $1\leq k\leq n$ the function $x_k$ is continuous at $a$. By {prf:ref}`Theorem:Continuity:EpsilonDelta` we have $\lim\limits_{t\rightarrow a}x_k(t)=x_k(a)$ for all $1\leq k\leq n$. Then it follows from {prf:ref}`Thm:Vectorfunctions:Limit` that $\lim\limits_{t\rightarrow a}\mathbf{r}(t)=\mathbf{r}(a)$, so $\mathbf{r}$ is continuous at $a$.
:::

::::::{prf:example} 
:label: Ex:Vectorfunctions:LimCont
Consider the vector function

$$
 \mathbf{r}(t)=\begin{pmatrix}\dfrac{t-1}{t^2-1}\\ \dfrac{\ln(t)}{1-\sqrt{t}} \end{pmatrix}.
$$

The domain of this vector function is the union of the intervals $(0,1)$ and $(1,\infty)$, which we can, alternatively, write as $(0,\infty)\setminus\{1\}$. The component functions $\dfrac{t+1}{t^2-1}$ and $\dfrac{\ln(t)}{1-\sqrt{t}}$ are continuous on this domain, so $\mathbf{r}$ is continuous by {prf:ref}`Thm:Vectorfunctions:Cont`. In addition, we note that

$$
 \lim_{t\rightarrow1}\dfrac{t-1}{t^2-1}=\dfrac{1}{2},
$$

either by cancelling the common factor $t-1$ (see {numref}`Subsec:Limitsrules`) or by using l'Hospital's rule (see {prf:ref}`Thm:lHospital:lHospital`). We also obtain

$$
 \lim_{t\rightarrow1}\dfrac{\ln(t)}{1-\sqrt{t}} =-2,
$$

using l'Hospital's rule. Using {prf:ref}`Thm:Vectorfunctions:Limit` we conclude that

$$
 \lim_{t\rightarrow1}\mathbf{r}(t)=\begin{pmatrix}\lim\limits_{t\rightarrow1}\dfrac{t-1}{t^2-1}\\ \lim\limits_{t\rightarrow1}\dfrac{\ln(t)}{1-\sqrt{t}} \end{pmatrix}=\begin{pmatrix}\frac{1}{2}\\ -2\end{pmatrix}.
$$
::::::

## Differentiation

The derivative of a vector function is defined very similarly to the derivative of a single-variable function.

::::::{prf:definition} 
:label: Def:Vectorfunctions:Diff
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function and $a$ a point in the domain of $\mathbf{r}$. Then the **derivative** of $\mathbf{r}$ at $a$, denoted by $\mathbf{r}'(a)$ is

$$
 \mathbf{r}'(a)=\lim_{h\rightarrow 0}\frac{1}{h}\left(\mathbf{r}(a+h)-\mathbf{r}(a)\right),
$$

provided this limit exists. If the limit exists, we say that $\mathbf{r}$ is differentiable in $a$. 


If the function $\mathbf{r}$ is differentiable at each point in its domain, we say that $\mathbf{r}$ is **differentiable**. 
::::::

::::::{prf:theorem} 
:label: Thm:Vectorfunctions:Diff
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function and let $a$ be a point in the domain of $\mathbf{r}$. Write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$.

Then $\mathbf{r}$ is differentiable at $a$ if, and only if, for all $1\leq k\leq n$ the function $x_k$ is differentiable at $a$. In that case, we have 

$$
 \mathbf{r}'(a)=\begin{pmatrix}x_1'(a)\\ \vdots\\ x_n'(a)\end{pmatrix}.
$$ 
::::::

:::{admonition} Proof of {prf:ref}`Thm:Vectorfunctions:Diff`
:class: tudproof, dropdown
Note that for $h\neq 0$ we have

$$
 \frac{1}{h}\left(\mathbf{r}(a+h)-\mathbf{r}(a)\right)=\frac{1}{h}\begin{pmatrix}x_1(a+h)-x_1(a)\\ \vdots \\ x_n(a+h)-x_n(a)\end{pmatrix}=\begin{pmatrix}\frac{x_1(a+h)-x_1(a)}{h}\\ \vdots \\ \frac{x_n(a+h)-x_n(a)}{h}\end{pmatrix}.
$$

By {prf:ref}`Thm:Vectorfunctions:Limit` we have that $\lim\limits_{h\rightarrow 0}\frac{1}{h}\left(\mathbf{r}(a+h)-\mathbf{r}(a)\right)$ exists if and only if for all $1\leq k\leq n$ the limit $\lim\limits_{h\rightarrow 0}\dfrac{x_k(a+h)-x_k(a)}{h}$ exists, meaning that $\mathbf{r}$ is differentiable at $a$ if, and only if, for all $1\leq k\leq n$ the function $x_k$ is differentiable at $a$. In addition, we conclude that

$$ 
 \mathbf{r}'(a)=\lim\limits_{h\rightarrow 0}\dfrac{x_k(a+h)-x_k(a)}{h}=\begin{pmatrix}\frac{\lim\limits_{h\rightarrow 0}x_1(a+h)-x_1(a)}{h}\\ \vdots \\ \lim\limits_{h\rightarrow 0}\frac{x_n(a+h)-x_n(a)}{h}\end{pmatrix}=\begin{pmatrix}x_1'(a)\\ \vdots\\ x_n'(a)\end{pmatrix}.
$$

:::

If the vector function $\mathbf{r}(t)$ represent the **position** of some particle, then the derivative $\mathbf{r}'(t)$ represent its **velocity**. Indeed, we should think of velocity as a vector-valued quantity as it has both a direction and a magnitude (the magnitude of the velocity is typically called the **speed**). 

Just like for derivatives of single-variable functions, there are several computation rules for finding derivatives of vector functions. These usually follow from their single-variable equivalents. The most important ones are listed in the theorem below.

::::::{prf:theorem} 
:label: Thm:Vectorfunctions:Basiccomputationrules
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ and $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset\mathbb{R}$ be vector functions. Let $a\in I$ and assume that $\mathbf{r}$ and $\mathbf{s}$ are differentiable at $a$. 

- **Sum rule**: $(\mathbf{r}+\mathbf{s})$ is differentiable at $a$ and we have 

$$
 (\mathbf{r}+\mathbf{s})'(a)=\mathbf{r}'(a)+\mathbf{s}'(a).
$$


- **Scalar multiple rule**: If $c\in\mathbb{R}$, then $c\mathbf{r}$ is differentiable at $a$ and we have 

$$
 (c\mathbf{r})'(a)=c\mathbf{r}'(a).
$$

- **Product rule**: If $f$ is a single-variable function that is differentiable at $a$ then $(f\mathbf{r})(t)=f(t)\mathbf{r}(t)$ is differentiable at $a$ and we have

$$
 (f\mathbf{r})'(a)=f'(a)\mathbf{r}(a)+f(a)\mathbf{r}'(a).
$$

- **Chain rule**: If $g$ is a single-variable function and $b$ is in the domain of $g$ in such a way that $g(b)=a$ and $g$ is differentiable at $b$, then $\mathbf{r}\circ g$ is differentiable at $b$ and we have 

$$
 (\mathbf{r}\circ g)'(b)=g'(b)\mathbf{r}'(a).
$$

- **Dot product rule**: $\mathbf{r}\cdot\mathbf{s}$ is differentiable at $a$ and we have 

$$
 (\mathbf{r}\cdot\mathbf{s})(a)=\mathbf{r}'(a)\cdot \mathbf{s}(a)+\mathbf{r}(a)\cdot \mathbf{s}'(a).
$$

- **Cross product rule**: If the codomain of $\mathbf{r}$ and $\mathbf{s}$ is $\mathbb{R}^3$ then $\mathbf{r}\times\mathbf{s}$ is differentiable at $a$ and we have 

$$
 \left(\mathbf{r}\times\mathbf{s}\right)(a)=\mathbf{r}'(a)\times\mathbf{s}(a)+\mathbf{r}(a)\times \mathbf{s}'(a).
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Vectorfunctions:Basiccomputationrules`
:class: tudproof, dropdown
**Proof of sum rule**. This follows directly from {prf:ref}`Thm:Vectorfunctions:Diff` and {prf:ref}`Thm:Differentiability:Sumscalar`.

**Proof of scalar multiple rule**. This follows directly from {prf:ref}`Thm:Vectorfunctions:Diff` and {prf:ref}`Thm:Differentiability:Sumscalar`.

**Proof of product rule**.  This follows directly from {prf:ref}`Thm:Vectorfunctions:Diff` and {prf:ref}`Thm:Productquotientrule:Productrule`

**Proof of chain rule**. We write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$. Then we have $\left(\mathbf{r}\circ g\right)(t)=\begin{pmatrix}x_1(g(t))\\ \vdots\\ x_n(g(t))\end{pmatrix}$. By {prf:ref}`Thm:Vectorfunctions:Diff` the functions $x_1,\ldots,x_n$ are all differentiable at $a$. So by {prf:ref}`Thm:Chainrule:Chainrule` the functions $(x_1\circ g),\ldots, (x_n\circ g)$ are all differentiable at $b$ and we have for all $1\leq k\leq n$

$$
 (x_k\circ g)'(b)=g'(b)x_k(g(b))=g'(b)x_k(a).
$$

Then by {prf:ref}`Thm:Vectorfunctions:Diff` the composition $\mathbf{r}\circ g$ is differentiable at $b$ and we have

$$
 (\mathbf{r}\circ g)'(b)=\begin{pmatrix}g'(b)x_1'(a)\\ \vdots \\ g'(b)x_n'(a) \end{pmatrix}=g'(b)\mathbf{r}'(a).
$$

**Proof of dot product rule**. We write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$ and $\mathbf{s}(t)=\begin{pmatrix}y_1(t)\\ \vdots\\ y_n(t)\end{pmatrix}$. Then we have

$$
 \mathbf{r}(t)\cdot \mathbf{s}(t)=\sum_{k=1}^n x_k(t)y_k(t).
$$

By {prf:ref}`Thm:Vectorfunctions:Diff` the functions $x_1,\ldots,x_n,y_1,\ldots,y_n$ are all differentiable at $a$. So by {prf:ref}`Thm:Differentiability:Sumscalar` and {prf:ref}`Thm:Productquotientrule:Productrule` the dot product $\mathbf{r}\cdot \mathbf{s}$ is also differentiable at $a$ and we obtain

$$
\begin{align*}
 (\mathbf{r}\cdot\mathbf{s})(a)&=\sum_{k=1}^n \left(x_k'(a)y_k(a)+x_k(a)y_k'(a)\right)\\ &=\sum_{k=1}^n x_k'(a)y_k(a)+\sum_{k=1}^nx_k(a)y_k'(a)\\ &=\mathbf{r}'(a)\cdot \mathbf{s}(a)+\mathbf{r}(a)\cdot \mathbf{s}'(a).
\end{align*}
$$

**Proof of cross product rule**. We write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ x_2(t)\\ x_3(t)\end{pmatrix}$ and $\mathbf{s}(t)=\begin{pmatrix}y_1(t)\\ y_2(t)\\ y_3(t)\end{pmatrix}$. Then we have

$$
 (\mathbf{r}\times\mathbf{s})(t)=\begin{pmatrix}x_2(t)y_3(t)-x_3(t)y_2(t)\\ x_3(t)y_1(t)-x_1(t)y_3(t)\\ x_1(t)y_2(t)-x_2(t)y_1(t)\end{pmatrix}.
$$

By {prf:ref}`Thm:Vectorfunctions:Diff` the functions $x_1,x_2,x_3,y_1,y_2,y_3$ are all differentiable at $a$. So by {prf:ref}`Thm:Differentiability:Sumscalar` and {prf:ref}`Thm:Productquotientrule:Productrule` the cross product $\mathbf{r}\times \mathbf{s}$ is also differentiable at $a$ and we obtain

$$
\begin{align*}
 (\mathbf{r}\times\mathbf{s})'(a)&=\begin{pmatrix}x_2'(a)y_3(a)+x_2(a)y_3'(a)-x_3'(a)y_2(a)-x_3(a)y_2'(a)\\ x_3'(a)y_1(a)+x_3(a)y_1'(a)-x_1'(a)y_3(a)-x_1(a)y_3'(a)\\ x_1'(a)y_2(a)+x_1(a)y_2'(a)-x_2'(a)y_1(a)-x_2(a)y_1'(a)\end{pmatrix}\\
 &=\begin{pmatrix}x_2'(a)y_3(a)-x_3'(a)y_2(a)\\ x_3'(a)y_1(a)-x_1'(a)y_3(a)\\ x_1'(a)y_2(a)-x_2'(a)y_1(a)\end{pmatrix}+\begin{pmatrix}x_2(a)y_3'(a)-x_3(a)y_2'(a)\\ x_3(a)y_1'(a)-x_1(a)y_3'(a)\\ x_1(a)y_2'(a)-x_2(a)y_1'(a)\end{pmatrix}\\
 &=\mathbf{r}'(a)\times\mathbf{s}(a)+\mathbf{r}(a)\times \mathbf{s}'(a)
\end{align*}
$$

:::

:::{note}
The three rules called the product rule, dot product rule and cross product rule all resemble the product rule for single-variable functions ({prf:ref}`Thm:Productquotientrule:Productrule`). It is important to note that for the cross product rule, the vector functions $\mathbf{r}\times \mathbf{s}$ and $\mathbf{s}\times \mathbf{r}$ are, typically, not the same, so their derivatives are different as well. Similarly, we also have to pay attention to the order of the terms in the derivative.
:::

As a consequence of the dot product rule, we can also find an expression for the derivative of the norm of a vector function.

::::::{prf:theorem} 
:label: Thm:Vectorfunctions:Normvector
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset\mathbb{R}$ be a differentiable vector function. Then the function $\left|\mathbf{r}(t)\right|^2$ is differentiable and we find

$$
 \frac{d}{dt}\left|\mathbf{r}(t)\right|^2=2\mathbf{r}(t)\cdot \mathbf{r}'(t).
$$

In addition, if $\mathbf{r}(t)\neq\mathbf{0}$ we have

$$
 \frac{d}{dt}\left|\mathbf{r}(t)\right|=\frac{\mathbf{r}(t)\cdot \mathbf{r}'(t)}{|\mathbf{r}(t)|}.
$$
::::::

:::{admonition} Proof of {prf:ref}`Thm:Vectorfunctions:Normvector`
:class: tudproof, dropdown
We note that

$$
 \left|\mathbf{r}(t)\right|^2=\mathbf{r}(t)\cdot \mathbf{r}(t).
$$

So by the dot product rule from {prf:ref}`Thm:Vectorfunctions:Basiccomputationrules` we find

$$
 \frac{d}{dt}\left|\mathbf{r}(t)\right|^2=\mathbf{r}'(t)\cdot\mathbf{r}(t)+\mathbf{r}(t)\cdot\mathbf{r}'(t)=2\mathbf{r}(t)\cdot \mathbf{r}'(t).
$$

If $\mathbf{r}(t)\neq \mathbf{0}$ we find using the chain rule

$$
\begin{align*}
 \dfrac{d}{dt}\left|\mathbf{r}(t)\right|&=\dfrac{d}{dt}\sqrt{\left|\mathbf{r}(t)\right|^2}\\
 &=\dfrac{1}{2\sqrt{\left|\mathbf{r}(t)\right|^2}}\frac{d}{dt}\left(\left|\mathbf{r}(t)\right|^2\right)\\
 &=\dfrac{1}{2\left|\mathbf{r}(t)\right|}2\left(\mathbf{r}(t)\cdot \mathbf{r}'(t)\right)\\
 &=\dfrac{\mathbf{r}(t)\cdot \mathbf{r}'(t)}{|\mathbf{r}(t)|}
\end{align*}
$$

:::

::::::{prf:corollary} 
:label: Cor:Vectorfunctions:Normvectorconst
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset\mathbb{R}$ be a differentiable vector function. If $\left|\mathbf{r}(t)\right|$ is constant on $D$, then the vectors $\mathbf{r}(t)$ and $\mathbf{r}'(t)$ are orthogonal for each $t\in D$.
::::::

:::{admonition} Proof of {prf:ref}`Cor:Vectorfunctions:Normvectorconst`
:class: tudproof, dropdown
If $\left|\mathbf{r}(t)\right|$ is constant on $D$, then its derivative must be $0$ for each $t\in D$. From {prf:ref}`Thm:Vectorfunctions:Normvector` we obtain $\mathbf{r}(t)\cdot \mathbf{r}'(t)=0$, which means that the vectors $\mathbf{r}(t)$ and $\mathbf{r}'(t)$ are orthogonal.
:::

It is also useful to consider higher order derivatives. For instance, if $\mathbf{r}(t)$ represent the position vector of some particle, then its second derivative $\mathbf{r}''(t)$ represents the **acceleration**. For instance, Newton's second law $\mathbf{F}=m\mathbf{a}$ can be represented as $\mathbf{F}=m\mathbf{r}''$. The second derivative will also play an important role later when computing the curvature of a space curve.

::::::{prf:definition} 
:label: Def:Vectorfunctions:HigherDiff
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function and let $a$ be a point in the domain of $\mathbf{r}$ such that $\mathbf{r}$ is differentiable at $a$. If $\mathbf{r}'$ is differentiable at $a$, then its derivative $(\mathbf{r}')'(a)$ is called the **second derivative** of $\mathbf{r}$ at $a$ and is denoted by $\mathbf{r}''(a)$. If the second derivative of $\mathbf{r}$ exists at each point in its domain, we say that $\mathbf{r}$ is **twice differentiable** and we call the vector function $\mathbf{r}''$ the **second derivative** of $\mathbf{r}$.

In general, if $n>0$ is a nonzero natural number, then the **$n$th derivative** of $\mathbf{r}$ at $a$ is the derivative of the $(n-1)$th derivative of $\mathbf{r}$ at $a$, provided it exists, and is denoted by $\mathbf{r}^{(n)}(a)$. If the $n$th derivative of $\mathbf{r}$ exists at each point in its domain, we say that $\mathbf{r}$ is **$n$ times differentiable** and we call the vector function $\mathbf{r}^{(n)}$ the **$n$th derivative** of $\mathbf{r}$.
::::::



::::::{prf:example} 
:label: Ex:Vectorfunctions:Deriv
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

## Integration

So far, we have defined introduced limits, continuity and derivatives by lifting the single-variable definitions to the vector function setting and then we showed that we can evaluate them component-wise. For (definite) integrals, there is no nice way to lift {prf:ref}`Def:Integration:DefiniteGeneral` to the vector setting. Instead, we will define the integral of a vector function component-wise.

::::::{prf:definition} 
:label: Def:Vectorfunctions:Integral
Let $\mathbf{r}:[a,b]\rightarrow\mathbb{R}^n$ be a vector function. We write $\mathbf{r}(t)=\begin{pmatrix}x_1(t)\\ \vdots\\ x_n(t)\end{pmatrix}$ and assume that $x_1,\ldots,x_n$ are piecewise-continuous and bounded on $[a,b]$. Then the **definite integral** $\displaystyle \int_a^b\mathbf{r}(t)\,dt$ of $\mathbf{r}$ is defined as

$$
 \int_a^b\mathbf{r}(t)\,dt =\begin{pmatrix}\int\limits_a^b x_1(t)\,dt\\ \vdots \\ \int\limits_a^b x_n(t)\,dt\end{pmatrix}.
$$
::::::

We can evaluate definite integrals of a vector function the same way as we would for a single-variable function: by finding an antiderivative and by using the fundamental theorem of calculus.

::::::{prf:definition} 
:label: Def:Vectorfunctions:Antiderivative
Let $\mathbf{r}:D\rightarrow\mathbb{R}^n$ with $D\subset \mathbb{R}$ be a vector function. A vector function $\mathbf{R}$ is known as an **antiderivative** of $\mathbf{r}$ on $D$ if it is differentiable and $\mathbf{R}'(t)=\mathbf{r}(t)$ for all $t\in D$.
::::::

::::::{prf:theorem} 
:label: Thm:Vectorfunctions:FundamentalTheorem
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

:::{admonition} Proof of {prf:ref}`Thm:Vectorfunctions:FundamentalTheorem`
:class: tudproof, dropdown
Since integration is defined component-wise, these results follow directly from {prf:ref}`Thm:Integration:FundamentalTheoremPart1` and {prf:ref}`Thm:Integration:FundamentalTheoremPart2`.
:::

::::::{prf:example} 
:label: Ex:Vectorfunctions:Int
We again consider the vector function

$$
 \mathbf{r}(t)=\begin{pmatrix}t^3\\ \cos(2t)\\ e^{-t}\end{pmatrix}
$$

from {prf:ref}`Ex:Vectorfunctions:Deriv`. By integrating the three component functions, we see that the vector function

$$
 \mathbf{R}(t)=\begin{pmatrix}\int t^3\,dt\\ \int\cos(2t)\,dt\\ \int e^{-t}\,dt\end{pmatrix}=\begin{pmatrix}\frac{1}{4}t^4\\ \frac{1}{2}\sin(2t)\\ -e^{-t}\end{pmatrix}
$$

is an antiderivative of $\mathbf{r}$. As such, we can evaluate the definite integral

$$
 \int_0^{1}\mathbf{r}(t)\,dt=\mathbf{R}(1)-\mathbf{R}(0)=\begin{pmatrix}\frac{1}{4}\\ \frac{1}{2}\sin(2)\\ -e^{-1}\end{pmatrix}-\begin{pmatrix}0\\ 0\\ -1\end{pmatrix}=\begin{pmatrix}\frac{1}{4}\\ \frac{1}{2}\sin(2)\\ 1-e^{-1}\end{pmatrix}.
$$

The indefinite integral of $\mathbf{r}$ takes the form

$$
 \int\mathbf{r}(t)\,dt=\mathbf{R}(t)+\mathbf{C},
$$

where $\mathbf{C}$ is a vector of integration constants, i.e. $\mathbf{C}=\begin{pmatrix} C_1\\ C_2\\ C_3\end{pmatrix}$.

::::::