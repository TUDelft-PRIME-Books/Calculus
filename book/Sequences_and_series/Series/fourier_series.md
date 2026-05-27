(Section:Fourier)=

# Fourier series

## Introduction

We have seen that Taylor polynomials, the partial sums of Taylor series, can be used to approximate a function $f(x)$ near a point $x=a$ as closely as is needed by taking the order large enough, provided we stay within the interval of convergence.

If the function $f$ is however periodic, then approximating $f$ by (Taylor) polynomials might not be the best approach, since the Taylor polynomials are not periodic. Examples where periodic functions appear are abundant in physics and engineering, for instance in the description of waves, signal processes or heat flows. In these cases it is useful to decompose such functions in standard periodic functions.

We first focus on an important property of trigonometric functions, the orthogonality, and then we use this property to decompose periodic functions in so-called Fourier series.

## Orthogonality of trigonometric functions

We repeat the definition of periodic functions from {numref}`Subsec:PropertiesFunctionsPeriodic`: 

:::{fetch} {prf:ref}`Def:PropertiesFunctions:Periodic`
:::

Now consider the functions $\displaystyle\cos\left(\frac{n\pi x}{L}\right)$ and $\displaystyle\sin\left(\frac{n\pi x}{L}\right)$ with $n$ a positive integer. These functions are all periodic with period $2L$. Moreover, they satisfy a remarkable property (compare with {numref}`Exc:Integration:TrigFunctionsProductFormulasOrthogonality`):

::::::{prf:theorem}
:label: Thm:Series:Orthogonality
For $m,n\in\{1,2,3,\ldots\}$ we have

$$
\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\cos\left(\frac{n\pi x}{L}\right)\,dx=\left\{\begin{array}{ll}0,&m\neq n\\L,&m=n,\end{array}\right.
$$

$$
\int_{-L}^L\sin\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx=\left\{\begin{array}{ll}0,&m\neq n\\L,&m=n\end{array}\right.
$$

and

$$
\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx=0.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:Orthogonality`
:class: tudproof, dropdown
Using the product formula $\cos(a)\cos(b)=\frac{1}{2}\left(\cos(a-b)+\cos(a+b)\right)$ (see {prf:ref}`Thm:Trigonometry:ProductFormulas`) we obtain for $m\neq n$

\begin{align*}
&\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\cos\left(\frac{n\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\int_{-L}^L\cos\left(\frac{(m-n)\pi x}{L}\right)\,dx+\frac{1}{2}\int_{-L}^L\cos\left(\frac{(m+n)\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\left[\frac{L}{(m-n)\pi}\sin\left(\frac{(m-n)\pi x}{L}\right)+\frac{L}{(m+n)\pi}\sin\left(\frac{(m+n)\pi x}{L}\right)\right]_{-L}^L\\
&=0,
\end{align*}

and for $m=n$ we use $\cos(2a)=2\cos^2(a)-1$ to find that

\begin{align*}
\int_{-L}^L\left\{\cos\left(\frac{n\pi x}{L}\right)\right\}^2\,dx&=\frac{1}{2}\int_{-L}^L\left\{1+\cos\left(\frac{2n\pi x}{L}\right)\right\}\,dx\\
&=\frac{1}{2}\left[x+\frac{L}{2n\pi}\sin\left(\frac{2n\pi x}{L}\right)\right]_{-L}^L \\
&=L.
\end{align*}

Using the product formula $\sin(a)\sin(b)=\frac{1}{2}\left(\cos(a-b)-\cos(a+b)\right)$ (see  {prf:ref}`Thm:Trigonometry:ProductFormulas`) we obtain for $m\neq n$

\begin{align*}
&\int_{-L}^L\sin\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\int_{-L}^L\cos\left(\frac{(m-n)\pi x}{L}\right)\,dx-\frac{1}{2}\int_{-L}^L\cos\left(\frac{(m+n)\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\left[\frac{L}{(m-n)\pi}\sin\left(\frac{(m-n)\pi x}{L}\right)-\frac{L}{(m+n)\pi}\sin\left(\frac{(m+n)\pi x}{L}\right)\right]_{-L}^L\\
&=0,
\end{align*}
and for $m=n$ we use $\cos(2a)=1-2\sin^2(a)$ to find that

\begin{align*}
\int_{-L}^L\left\{\sin\left(\frac{n\pi x}{L}\right)\right\}^2\,dx&=\frac{1}{2}\int_{-L}^L\left\{1-\cos\left(\frac{2n\pi x}{L}\right)\right\}\,dx\\
&=\frac{1}{2}\left[x-\frac{L}{2n\pi}\sin\left(\frac{2n\pi x}{L}\right)\right]_{-L}^L \\
&=L.
\end{align*}

Finally we use the product formula $\cos(a)\sin(b)=\frac{1}{2}\left(\sin(a+b)-\sin(a-b)\right)$ (see  {prf:ref}`Thm:Trigonometry:ProductFormulas`) to obtain for $m\neq n$

\begin{align*}
&\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\int_{-L}^L\sin\left(\frac{(m+n)\pi x}{L}\right)\,dx-\frac{1}{2}\int_{-L}^L\sin\left(\frac{(m-n)\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\left[-\frac{L}{(m+n)\pi}\cos\left(\frac{(m+n)\pi x}{L}\right)+\frac{L}{(m-n)\pi}\cos\left(\frac{(m-n)\pi x}{L}\right)\right]_{-L}^L\\
&=0,
\end{align*}

and for $m=n$ we use $\sin(2a)=2\sin(a)\cos(a)$ to find that

$$
\int_{-L}^L\cos\left(\frac{n\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx=\frac{1}{2}\int_{-L}^L\sin\left(\frac{2n\pi x}{L}\right)\,dx=0.
$$

:::

The property that the integrals of the products of these functions are zero when $m\neq n$ and are positive when $m=n$ is called the **orthogonality** of these functions. This is a very important property, which allows us to decompose periodic functions in terms of these trigonometric functions.

The formal definition of orthogonality for arbitrary functions is as follows:

::::::{prf:definition}
:label: Def:Series:Orthogonality

Let $f$ and $g$ be functions defined on an interval $(\alpha,\beta)$. The inner product of $f$ and $g$, denoted by $\langle f,g\rangle$, is defined as

$$
\langle f,g\rangle=\displaystyle\int_{\alpha}^{\beta}f(x)g(x)\,dx.
$$

If $\langle f,g\rangle=0$, then $f$ and $g$ are called **orthogonal**.
::::::

So how can we use this orthogonality of the sine and cosine functions of {prf:ref}`Thm:Series:Orthogonality` to decompose periodic functions in terms of these functions? And which of these sine and cosine functions functions do we need?

To introduce the answer to that question, first note that we already have a cosine function or a sine function, or for that matter any linear combination of these functions with the same period, the decomposition is already given by the function itself, similar to how a Taylor series of a polynomial is already given by the polynomial itself.

Things become harder when we add a constant to such a function. This is investigated in the following example.

::::{prf:example}
:label: Ex:Series:IntroConstant

Consider the function $f(x)=7+\frac12\cos\left(\frac{\pi x}{3}\right)$, which is a function that is periodic with fundamental period $6$. You can confirm this by taking a look at {numref}`Fig:Series:IntroConstant`.

:::{figure} Images/Fig-Series-IntroConstant.png
:name: Fig:Series:IntroConstant

Graph of the function $f(x)=7+\frac12\cos\left(\frac{\pi x}{3}\right)$.
:::

Because of the constant term $7$ in the definition of $f$, $f$ oscillates around $7$ and not around $0$. This means that if we define the function $g$ by

$$
g(x)=f(x)-7=\frac12\cos\left(\frac{\pi x}{3}\right),
$$

then $g$ is a function that oscillates around $0$. Even better: $g$ is one of the functions of the form $\displaystyle\cos\left(\frac{n\pi x}{L}\right)$ with $n=1$ and $L=3$. But this also means that _if_ we would multiply $g$ by $\displaystyle\cos\left(\frac{n\pi x}{L}\right)$ and then integrate from $-3$ to $3$, we would get zero for all $n$ except for $n=1$ and $L=3$. Integrating $g$ gives in that case:

\begin{align*}
\int_{-3}^3g(x)\cos\left(\frac{\pi x}{3}\right)\,dx&=\int_{-3}^3\frac12\cos\left(\frac{\pi x}{3}\right)\cos\left(\frac{\pi x}{3}\right)\,dx\\
&=\frac12\int_{-3}^3\cos^2\left(\frac{\pi x}{3}\right)\,dx \\
&=\frac12\cdot3.
\end{align*}

But this also means that 

$$
\frac{1}{3}\int_{-3}^3g(x)\cos\left(\frac{\pi x}{3}\right)\,dx=\frac{1}{3}\cdot\frac{1}{2}\cdot3=\frac{1}{2},
$$

which is exactly the coefficient of $\displaystyle\cos\left(\frac{\pi x}{3}\right)$ in the definition of $g$. If we replace $g$ by $f$, then we find

\begin{align*}
\frac{1}{3}\int_{-3}^3f(x)\cos\left(\frac{\pi x}{3}\right)\,dx &= \frac{1}{3}\int_{-3}^3(g(x)+7)\cos\left(\frac{\pi x}{3}\right)\,dx \\
&= \frac{1}{3}\int_{-3}^3g(x)\cos\left(\frac{\pi x}{3}\right)+7\cos\left(\frac{\pi x}{3}\right)\,dx \\
&= \frac{1}{3}\int_{-3}^3g(x)\cos\left(\frac{\pi x}{3}\right)\,dx + \frac{1}{3}\int_{-3}^37\cos\left(\frac{\pi x}{3}\right)\,dx \\
&= \frac{1}{2} + 0 \\
&= \frac{1}{2},
\end{align*}

which is exactly the coefficient of $\displaystyle\cos\left(\frac{\pi x}{3}\right)$ in the definition of $f$.

Now, instead of substituting multiplying $g$ by a cosine function, we can also just integrate $f$ from $-3$ to $3$ and then divide by $3$. This gives:

$$
\frac{1}{3}\int_{-3}^3f(x)\,dx=\frac{1}{3}\int_{-3}^3\left(7+\frac12\cos\left(\frac{\pi x}{3}\right)\right)\,dx=\frac{1}{3}\int_{-3}^37\,dx=\frac{1}{3}\cdot(6\cdot7)=2\cdot7.
$$

This last results is exactly two times the constant term $7$ in the definition of $f$.

In  other words and symbols, we have found the following decomposition of $f$:

$$
f(x) = \frac{a_0}{2} + a_1\cos\left(\frac{\pi x}{3}\right),
$$

where

\begin{align*}
a_0 &= \frac{1}{3}\int_{-3}^3f(x)\,dx\quad(=2\cdot7), \\
a_1 &= \frac{1}{3}\int_{-3}^3f(x)\cos\left(\frac{\pi x}{3}\right)\,dx\quad(= \frac{1}{2}).
\end{align*}

::::

The idea of writing a function as a linear combination of trigonometric functions, where we exploit the orthogonality of these functions to find the coefficients of this linear combination, is the basis of the next section. Because we might not now _a priori_ which trigonometric functions we need, we will have to consider all of them. This is what we do in the next section and leads to an infinite linear combination of trigonometric functions, which is called a Fourier series.

## Definition of Fourier series

We start with giving a formal definition of Fourier series:

::::::{prf:definition} Fourier series
:label: Def:Series:FourierSeries
A series of the form

$$
\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos\left(\frac{n\pi x}{L}\right)+b_n\sin\left(\frac{n\pi x}{L}\right)\right)
$$

with $L>0$ is called a **Fourier series**.
::::::

Fourier series are named after the French mathematician [Jean-Baptiste Joseph Fourier (1768-1830)](https://en.wikipedia.org/wiki/Joseph_Fourier), who introduced this type of series in his work on the theory of heat.

Before we can use Fourier series to decompose periodic functions, we need to introduce the concept of bounded variation, which is a technical condition on the function $f$ that we want to decompose. We will not go into the details of this concept, but it is sufficient to know that piecewise continuous functions are of bounded variation.

:::{prf:definition}
A function $f$ is called of **bounded variation** on an interval $[a,b]$ if there exists a number $M\geq 0$ such that for every partition $P=\{x_0,x_1,\ldots,x_n\}$ of the interval $[a,b]$ we have

$$
\sum_{i=1}^n|f(x_i)-f(x_{i-1})|\leq M.
$$

::::::

This concept of bounded variation is important for the convergence of Fourier series, as we will see in {prf:ref}`Thm:Series:FourierConvergence`, and guarantees that our functions do not have too many oscillations and large jumps. For a special set of functions, bounded variation can be determined by checking a few conditions, as the following theorem states.

::::::{prf:theorem}
:label: Thm:Series:BoundedVariation
If

- $f$ is a piecewise continuous function on an interval $[a,b]$;

- $f'$ only has discontinuities on $(a,b)$ on a finite set of points $J=\{x_1,x_2,\ldots,x_m\}$ for some integer $m\geq0$;

- $f'$ is piecewise continuous on $(a,b)\setminus J$;

- $\displaystyle\int_a^b|f'(x)|\,dx$ is finite;

then $f$ is of bounded variation on $[a,b]$.
::::::

The next example applies this theorem.

::::{prf:example}
:label: Ex:Series:BoundedVariation

Consider the function $f$ defined by

$$
f(x) = \begin{cases}
f(x+4), & \text{if } x \leq -2, \\
0, & \text{if } -2 < x \leq 0, \\
x, & \text{if } 0 < x \leq 2, \\
f(x-4), & \text{if } x > 2.
\end{cases}
$$

You can see the graph of this function in {numref}`Fig:Series:BoundedVariation`. We have also shown the graph of the derivative of this function, including the integral mentioned in {prf:ref}`Thm:Series:BoundedVariation`.

:::{figure} Images/Fig-Series-BoundedVariation.png
:name: Fig:Series:BoundedVariation

The graph of the function $f$ and it's derivative $f'$ from {prf:ref}`Ex:Series:BoundedVariation`.
:::

:::{todo}
Replace {numref}`Fig:Series:BoundedVariation` with an applet. Note that in the current image the function is incorrect, only the shape is correct.
:::

The function $f$ is piecewise continuous on $[-2,2]$ and it is periodic with period $4$. The derivative of $f$ is piecewise continuous on $(-2,2)$ and has only one discontinuity at $x=0$. Moreover, we have 

$$
\int_{-2}^2 |f'(x)| \, dx = \int_{-2}^0 |0| \, dx + \int_0^2 |1| \, dx = 0 + 2 = 2.
$$

$f$ therefore satisfies the conditions of {prf:ref}`Thm:Series:BoundedVariation` and is of bounded variation on $[-2,2]$.

::::

In this section we will only consider functions that satisfy the conditions of this theorem, so all functions are of bounded variation. 

With this in mind, we can now give the main result of this section:

::::::{prf:definition}
:label: Def:Series:FourierFormula

If $f$ is piecewise continuous function on an interval $[-L,L)$ and $f$ is defined outside that interval so that it is periodic with period $2L$, then the **Fourier series** $g$ of $f$ is defined by

$$
g(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos\left(\frac{n\pi x}{L}\right)+b_n\sin\left(\frac{n\pi x}{L}\right)\right),
$$

where 

$$
a_0=\frac{1}{L}\int_{-L}^Lf(x)\,dx,
$$

and for $n=1,2,3,\ldots$ 

\begin{align*}
a_n &= \frac{1}{L}\int_{-L}^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx, \\
b_n &= \frac{1}{L}\int_{-L}^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
\end{align*}

The formulas for $a_n$, $n=0,1,2,3,\ldots$ and $b_n$, $n=1,2,3,\ldots$ are called the **Euler-Fourier formulas**, named after the Swiss mathematician [Leonhard Euler (1707-1783)](https://en.wikipedia.org/wiki/Leonhard_Euler) and the French mathematician [Jean-Baptiste Joseph Fourier (1768-1830)](https://en.wikipedia.org/wiki/Joseph_Fourier).
::::::

:::{admonition} Derivation of {prf:ref}`Def:Series:FourierFormula`
:class: derivation, dropdown

Ideally, we would like that $f$ and $g$ are the same function, so assume we could write $f$ as

$$
f(x)=\displaystyle\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos\left(\frac{n\pi x}{L}\right)+b_n\sin\left(\frac{n\pi x}{L}\right)\right)
$$

Then integration gives

\begin{align*}
\int_{-L}^Lf(x)\,dx&=\frac{a_0}{2}\int_{-L}^L\,dx\\
&{}\quad\quad{}+\sum_{n=1}^{\infty}\left(a_n\int_{-L}^L\cos\left(\frac{n\pi x}{L}\right)\,dx+b_n\int_{-L}^L\sin\left(\frac{n\pi x}{L}\right)\,dx\right).
\end{align*}
Note that $\displaystyle\int_{-L}^L\,dx=2L$, $\displaystyle\int_{-L}^L\cos\left(\frac{n\pi x}{L}\right)\,dx=0$ and $\displaystyle\int_{-L}^L\sin\left(\frac{n\pi x}{L}\right)\,dx=0$. Hence we have

$$
\int_{-L}^Lf(x)\,dx=a_0L\quad\Longleftrightarrow\quad a_0=\frac{1}{L}\int_{-L}^Lf(x)\,dx.
$$

If we multiply by $\displaystyle\cos\left(\frac{m\pi x}{L}\right)$ and then integrate, we obtain

\begin{align*}
\int_{-L}^Lf(x)\cos\left(\frac{m\pi x}{L}\right)\,dx&=\frac{a_0}{2}\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\,dx\\
&{}\quad\quad{}+\sum_{n=1}^{\infty}a_n\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\cos\left(\frac{n\pi x}{L}\right)\,dx\\
&{}\quad\quad{}+\sum_{n=1}^{\infty}b_n\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx.
\end{align*}

Then {prf:ref}`Thm:Series:Orthogonality` implies that for $m=1,2,3,\ldots$

$$
\int_{-L}^Lf(x)\cos\left(\frac{m\pi x}{L}\right)\,dx=a_mL\quad\Longleftrightarrow\quad a_m=\frac{1}{L}\int_{-L}^Lf(x)\cos\left(\frac{m\pi x}{L}\right)\,dx.
$$

If we multiply by $\displaystyle\sin\left(\frac{m\pi x}{L}\right)$ and then integrate, we obtain

\begin{align*}
\int_{-L}^Lf(x)\sin\left(\frac{m\pi x}{L}\right)\,dx&=\frac{a_0}{2}\int_{-L}^L\sin\left(\frac{m\pi x}{L}\right)\,dx\\
&{}\quad\quad{}+\sum_{n=1}^{\infty}a_n\int_{-L}^L\sin\left(\frac{m\pi x}{L}\right)\cos\left(\frac{n\pi x}{L}\right)\,dx\\
&{}\quad\quad{}+\sum_{n=1}^{\infty}b_n\int_{-L}^L\sin\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx.
\end{align*}
Then {prf:ref}`Thm:Series:Orthogonality` implies that for $m=1,2,3,\ldots$

$$
\int_{-L}^Lf(x)\sin\left(\frac{m\pi x}{L}\right)\,dx=b_mL\quad\Longleftrightarrow\quad b_m=\frac{1}{L}\int_{-L}^Lf(x)\sin\left(\frac{m\pi x}{L}\right)\,dx.
$$



:::

::::::{prf:theorem} Convergence
:label: Thm:Series:FourierConvergence

If $f$ is a piecewise continuous function of bounded variation on an interval $[-L,L)$ and $f$ is defined outside that interval so that it is periodic with period $2L$, then the Fourier series $g$ given in {prf:ref}`Def:Series:FourierFormula` converges at all points $x$ to

$$
g(x)=\frac{f(x^-)+f(x^+)}{2},
$$ 

where $f(x^-)=\lim\limits_{t\to x^{-}}f(t)$ and $f(x^+)=\lim\limits_{t\to x^{+}}f(t)$.

At points $x$ where $f$ is continuous, we have $\lim\limits_{t\to x^{-}}f(t)=f(x)=\lim\limits_{t\to x^{+}}f(t)$, and therefore $g(x) = \displaystyle\frac{f(x^-)+f(x^+)}{2}=f(x)$.
::::::

We omit a proof of this theorem, as this is beyond the scope of this course. 

We do however use the consequences of this theorem in the remainder of this section, starting with the following important example.

::::{prf:example}
:label: Ex:Series:Fourier1

We revisit the function $f$ from {prf:ref}`Ex:Series:BoundedVariation`, which was defined by

$$
f(x) = \begin{cases}
f(x+4), & \text{if } x \leq -2, \\
0, & \text{if } -2 < x \leq 0, \\
x, & \text{if } 0 < x \leq 2, \\
f(x-4), & \text{if } x > 2.
\end{cases}
$$

We start with calculating the Fourier coefficients of $f$. Using $L=2$, we have

\begin{align*}
a_0 &= \frac{1}{2}\int_{-2}^2f(x)\,dx \\
&= \frac{1}{2}\int_{-2}^0 0 \, dx + \frac{1}{2}\int_0^2 x \, dx \\
&= \frac{1}{2}\cdot\frac{4}{2} \\
&= 1, \\
a_n &= \frac{1}{2}\int_{-2}^2f(x)\cos\left(\frac{n\pi x}{2}\right)\,dx \\
&= \frac{1}{2}\int_0^2 x\cos\left(\frac{n\pi x}{2}\right)\,dx \\
&= \frac{2}{n^2\pi^2}\left(n\pi\sin(n\pi)+\cos(n\pi)-1\right) \\
&= \frac{2}{n^2\pi^2}\left(0+(-1)^n-1\right) \\
&= \begin{cases}
0, & \text{if } n \text{ is even}, \\
\frac{-4}{n^2\pi^2}, & \text{if } n \text{ is odd},
\end{cases} \\
b_n &= \frac{1}{2}\int_{-2}^2f(x)\sin\left(\frac{n\pi x}{2}\right)\,dx \\
&= \frac{1}{2}\int_0^2 x\sin\left(\frac{n\pi x}{2}\right)\,dx \\
&= \frac{2}{n^2\pi^2}\left(\sin(n\pi)-n\pi\cos(n\pi)\right) \\
&= \frac{2}{n^2\pi^2}\left(0-n\pi(-1)^n\right) \\
&= \frac{2(-1)^{n+1}}{n\pi}.
\end{align*}

The entire Fourier series $g$ of $f$ is therefore given by

$$
g(x) = \frac{1}{2} + \sum_{k=1}^{\infty}\frac{-4}{(2k-1)^2\pi^2}\cos\left(\frac{(2k-1)\pi x}{2}\right)+\sum_{n=1}^{\infty}\frac{2(-1)^{n+1}}{n\pi}\sin\left(\frac{n\pi x}{2}\right).
$$

Because $f$ is continuous at all points $x$ except for points of the form $x=2+4k$ for some integer $k$, {prf:ref}`Thm:Series:FourierConvergence` gives that $g(x)=f(x)$ for all points $x$ except for points of the form $x=2+4k$ for some integer $k$. At these points we have

$$
g(x) = \frac{f(x^-)+f(x^+)}{2} = \frac{0+2}{2} = 1.
$$

This means that the Fourier series $g$ of $f$ converges to $f$ at all points except for points of the form $x=2+4k$ for some integer $k$, where it converges to $1$ instead of $0$ or $2$.

This result can also be visualised by plotting the Fourier series $g$ of $f$ together with the function $f$ itself. The Fourier series $g$ is an infinite series, so we cannot plot it directly. However, we can plot the Fourier series truncated at some finite number of terms, which gives us an approximation of $g$, which we did in {numref}`Fig:Series:Fourier1`. You can decrease or increase the number of terms in the series to see how the approximation changes by changing the value of $N$.

:::{figure} Images/Fig-Series-Fourier1.png
:name: Fig:Series:Fourier1

The graph of the function $f$ from {prf:ref}`Ex:Series:BoundedVariation` together with the Fourier series of $f$ truncated at $N=5$ (initially).
:::

:::{todo}
Replace {numref}`Fig:Series:Fourier1` with an applet, where you can change the value of $N$ to see how the approximation changes.

:::

Note that for larger $N$ the Fourier series $g$ of $f$ converges to $f$ at all points except for points of the form $x=2+4k$ for some integer $k$, where it converges to $1$ instead of $0$ or $2$. In particular, near these points you can see that the Fourier series $g$ of $f$ oscillates around the value of  $f$ with increasing amplitude.

::::

::::::{prf:definition} Gibbs phenomenon

The phenomenon that the truncated Fourier series of a function with a jump discontinuity oscillates around the value of the function near the point of discontinuity with increasing amplitude for increasing number of terms is called the **Gibbs phenomenon**.
::::::

This _Gibbs phenomenon_ is named after the American scientist [Josiah Willard Gibbs (1839-1903)](https://en.wikipedia.org/wiki/Josiah_Willard_Gibbs).

::::{prf:example}
:label: Ex:Series:GibbsFourier

We turn our attention to the function $f$ we have seen in {prf:ref}`Ex:Series:Fourier1`.

To investigate the Gibbs phenomenon for this function, we make a graph of the difference between the truncated Fourier series $g$ of $f$ and the function $f$ itself, which is shown in {numref}`Fig:Series:GibbsFourier`. You can change the value of $N$ to see how the approximation changes.

:::{figure} Images/Fig-Series-GibbsFourier.png
:name: Fig:Series:GibbsFourier

The graph of the difference between the truncated Fourier series $g$ of $f$ from {prf:ref}`Ex:Series:Fourier1` and the function $f$ itself.
:::

:::{todo}
Replace {numref}`Fig:Series:GibbsFourier` with an applet, where you can change the value of $N$ to see how the approximation changes.
:::

If you increase $N$ you should see that the truncated Fourier series $g$ of $f$ minus the function $f$ itself oscillates around the value of $0$ near the points of discontinuity of $f$ with increasing amplitude for increasing number of terms. This is the Gibbs phenomenon in action. Observe also that the width of these oscillations decreases for increasing number of terms, which is also part of the Gibbs phenomenon. In particular, the truncated Fourier series $g$ of $f$ minus the function $f$ itself converges to $0$ at all points except for points of the form $x=2+4k$ for some integer $k$, where it converges to $1$ instead of $0$ or $2=0$.

::::

If a Fourier series converges to a function for all $x$, then we have the following important identity, which is a consequence of the orthogonality of the sine and cosine functions.

::::::{prf:theorem} Parseval's identity
:label: Thm:Series:Parseval
For a Fourier series given as in {prf:ref}`Def:Series:FourierFormula` that converge for all $x$ in $[-L,L]$ to $f(x)$ where $f$ is continuous, we also have

$$
\frac{1}{L}\int_{-L}^L\left\{f(x)\right\}^2\,dx=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}\left(a_n^2+b_n^2\right).
$$

This is called **Parseval's identity**, named after the French mathematician [Marc-Antoine Parseval (1755-1836)](https://en.wikipedia.org/wiki/Marc-Antoine_Parseval).
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:Parseval`
:class: tudproof, dropdown

Because the Fourier series converges to $f$ for all $x$ in $[-L,L]$ where $f$ is continuous, we have


$$
f(x)=\displaystyle\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos\left(\frac{n\pi x}{L}\right)+b_n\sin\left(\frac{n\pi x}{L}\right)\right),
$$

for all $x$ in $[-L,L]$ where $f$ is continuous.

Multiplication of this expression by $f(x)$ and integration over $[-L,L]$ then gives

\begin{align*}
\frac{1}{L}\int_{-L}^L\left\{f(x)\right\}^2\,dx&=\frac{a_0}{2}\cdot\frac{1}{L}\int_{-L}^Lf(x)\,dx\\
&{}\quad\quad{}+\sum_{n=1}^{\infty}a_n\cdot\frac{1}{L}\int_{-L}^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx\\
&{}\quad\quad{}+\sum_{n=1}^{\infty}b_n\cdot\frac{1}{L}\int_{-L}^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx\\
&=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}\left(a_n^2+b_n^2\right).
\end{align*}

Note that we assume here that the locations where $f$ is not continuous do not contribute to the value of the integral.
:::

Let us do one more example that touches all subjects we explored in this section, including the Fourier series, the convergence of Fourier series and Parseval's identity.

::::::{prf:example}
:label: Ex:Series:FourierExample1
Consider the function $f$ defined as

$$
f(x)=\begin{cases}
f(x+2\pi), & x < -\pi, \\
0,&-\pi\leq x < 0, \\
1,&0\leq x < \pi, \\
f(x-2\pi), & x \geq \pi.
\end{cases}
$$

This function is an example of a square wave, which is a function that jumps between two values, in this case $0$ and $1$.

Then $L=\pi$ and

$$
a_0=\displaystyle\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\,dx=\frac{1}{\pi}\int_0^{\pi}dx=1.
$$

Further we have for $n=1,2,3,\ldots$

$$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx=\frac{1}{\pi}\int_0^{\pi}\cos(nx)\,dx=\frac{1}{n\pi}\sin(nx)\bigg|_0^{\pi}=0
$$

and

\begin{align*}
b_n&=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx=\frac{1}{\pi}\int_0^{\pi}\sin(nx)\,dx=-\frac{1}{n\pi}\cos(nx)\bigg|_0^{\pi}\\
&=\frac{1-\cos(n\pi)}{n\pi}=\frac{1-(-1)^n}{n\pi}.
\end{align*}

Note that $b_{2k}=0$ and $b_{2k-1}=\displaystyle\frac{2}{(2k-1)\pi}$ for $k=1,2,3,\ldots$. Then we have that the fourier series $g$ of $f$ is given by

$$
g(x)=\frac{1}{2}+\sum_{n=1}^{\infty}\frac{1-(-1)^n}{n\pi}\sin(nx)=\frac{1}{2}+\frac{2}{\pi}\sum_{k=1}^{\infty}\frac{\sin(2k-1)x}{2k-1}.
$$

A plot of some partial sums of this series can be found in {numref}`Fig:Series:SquareWaveFourier`.

:::{figure} Images/fourier1.png
:name: Fig:Series:SquareWaveFourier
:width: 50%

A square wave and a partial sum of its Fourier series.
:::

:::{todo}
Replace {numref}`Fig:Series:SquareWaveFourier` with an applet, where you can change the value of $N$ to see how the approximation changes.
:::

Notice that around the jump points the _Gibbs phenomenon_ is visible.

At $x=\frac{1}{2}\pi$ the function $f$ is continuous, so the Fourier series $g$ converges to $f(x)$, which implies:

\begin{align*}
1=\frac{1}{2}+\frac{2}{\pi}\sum_{k=1}^{\infty}\frac{\sin(k-\frac{1}{2})\pi}{2k-1}&\quad\Longleftrightarrow\quad
\frac{1}{2}=\frac{2}{\pi}\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{2k-1}\\
&\quad\Longleftrightarrow\quad
\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{2k-1}=\frac{1}{4}\pi.
\end{align*}

Using {prf:ref}`Parseval's identity <Thm:Series:Parseval>` we can also find that

\begin{align*}
&\frac{1}{2}+\frac{4}{\pi^2}\sum_{k=1}^{\infty}\frac{1}{(2k-1)^2}=\frac{1}{\pi}\int_{-\pi}^{\pi}\{f(x)\}^2\,dx=\frac{1}{\pi}\int_0^{\pi}dx=1\\
&{}\quad\Longrightarrow\quad\sum_{k=1}^{\infty}\frac{1}{(2k-1)^2}=\frac{1}{8}\pi^2.
\end{align*}

::::::

## Fourier cosine and sine series

In the last example we have seen that the cosine part of the Fourier series of the square wave disappeared. This can be explained by the behavior of odd and even functions.

The definition of _odd_ and _even_ was given as:

:::{fetch} {prf:ref}`Def:PropertiesFunctions:EvenOdd`
:::

Moreover, we have the following rules of calculation:

* If $g$ is even and $h$ is even, then $g\cdot h$ is even;

* If $g$ is even and $h$ is odd, then $g\cdot h$ is odd;

* If $g$ is odd and $h$ is odd, then $g\cdot h$ is even.

In {numref}`Sec:Integration:Substitution` we have seen:

:::{fetch} {prf:ref}`Thm:Integration:OddEven`
:::

Note that this also holds when $g$ is piecewise continuous.

Hence, we have, if $f$ is *even* on $(-L,L)$, that

$$
\frac{1}{L}\int_{-L}^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx=0
$$

and

$$
\frac{1}{L}\int_{-L}^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx=\frac{2}{L}\int_0^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx.
$$

And, if $f$ is *odd* on $(-L,L)$, then we have

$$
\frac{1}{L}\int_{-L}^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx=0
$$

and

$$
\frac{1}{L}\int_{-L}^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx=\frac{2}{L}\int_0^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$


The above shows that if $f$ is periodic with period $2L$ and even on $(-L,L)$, in the Fourier series of $f$ the sine part disappears, and if $f$ is periodic with period $2L$ and odd on $(-L,L)$, in the Fourier series of $f$ the cosine part disappears. This gives us the following two special cases of Fourier series, which are called **Fourier cosine series** and **Fourier sine series**.

::::::{prf:theorem} Fourier cosine series
:label: Thm:Series:FourierCosineSeries
If $f$ is an *even* function on $(-L,L)$ and periodic with period $2L$, then the Fourier series $g$ of $f$ is given by

$$
g(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos\left(\frac{n\pi x}{L}\right)
$$

with $a_0=\displaystyle\frac{2}{L}\int_0^Lf(x)\,dx$ and $a_n=\displaystyle\frac{2}{L}\int_0^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx$ for $n=1,2,3,\ldots$.
::::::

::::::{prf:theorem} Fourier sine series
:label: Thm:Series:FourierSineSeries
If $f$ is an *odd* function on $(-L,L)$ and periodic with period $2L$, then the Fourier series $g$ of $f$ is given by

$$
g(x)=\sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{L}\right)
$$

with $b_n=\displaystyle\frac{2}{L}\int_0^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx$ for $n=1,2,3,\ldots$.
::::::



If $f$ is neither even nor odd, but $g(x)=f(x)-\bar{f}$ is odd, with $\bar{f}=\displaystyle\frac{1}{2L}\int_{-L}^Lf(x)\,dx$, then we can write $f$ as a Fourier sine series plus $\bar{f}$. This is exactly what happened in {prf:ref}`Ex:Series:FourierExample1`, where the Fourier series $g$ of $f$ was given by

$$
g(x)=\frac{1}{2}+\frac{2}{\pi}\sum_{k=1}^{\infty}\frac{\sin(2k-1)x}{2k-1}.
$$

The constant term $\frac{1}{2}$ is the average value of $f$ over $[-\pi,\pi]$, i.e., $\bar{f}$, and the rest of the Fourier series is a Fourier sine series. To see that the rest of the Fourier series is a Fourier sine series, we can investigate whether the function $h$ defined by

$$
h(x) = f(x) - \bar{f} = f(x) - \frac{1}{2} = 
\begin{cases}
f(x+2\pi)-\frac12, & x < -\pi, \\
-\frac12,&-\pi\leq x < 0, \\
\frac12,&0\leq x < \pi, \\
f(x-2\pi)-\frac12, & x \geq \pi.
\end{cases}
$$

is indeed odd on $(-\pi,\pi)$. We have for $x\in(0,\pi)$ that

$$
h(x) = \frac12,\quad\text{and}\quad h(-x) = -\frac12 = -h(x).
$$

This shows that $h$ is odd on $(-\pi,\pi)$, and therefore the Fourier series $g$ of $f$ can be written as a Fourier sine series plus $\bar{f}$.

Let us investigate some other functions and their Fourier series.



::::::{prf:example}
:label: Ex:Series:FourierExample2
Consider the function $f$ defined by

$$
f(x) = \begin{cases}
f(x+2), & x < -1, \\
2x, & -1 \leq x \leq 1, \\
f(x-2), & x > 1.
\end{cases}
$$

Then $L=1$ and $f$ is odd on $(-1,1)$. This means that the Fourier series of $f$ is a Fourier sine series, and we only have to calculate the Fourier sine coefficients $b_n$ for $n=1,2,3,\ldots$:

\begin{align*}
b_n&=\frac{1}{1}\int_{-1}^1f(x)\sin(n\pi x)\,dx=\int_{-1}^12x\sin(n\pi x)\,dx\\
&=-\frac{1}{n\pi}\int_{-1}^12x\,d\cos(n\pi x)\\
&=-\frac{2x\cos(n\pi x)}{n\pi}\bigg|_{-1}^1+\frac{2}{n\pi}\int_{-1}^1\cos(n\pi x)\,dx\\
&=-\frac{4\cos(n\pi)}{n\pi}=\frac{4(-1)^{n+1}}{n\pi}.
\end{align*}

Hence the Fourier series $g$ of $f$ is given by

:::{math}
:name: Eq:Series:SawToothFourier
g(x)=\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(n\pi x).
:::

In {numref}`Fig:Series:SawToothFourier` you can see a plot of some partial sums of this Fourier series together with the function $f$ itself. You can change the value of $N$ to see how the approximation changes.

The function $f$ is an example of a sawtooth wave, which is a function that changes linearly and then jumps down/up.

:::{figure} Images/fourier2.png
:name: Fig:Series:SawToothFourier
:width: 50%

A sawtooth wave.
:::

:::{todo}
Replace {numref}`Fig:Series:SawToothFourier` with an applet, where you can change the value of $N$ to see how the approximation changes.
:::

Around the jump points the Gibbs phenomenon is visible.

For $x=\frac{1}{2}$ the function {prf:ref}`Fourier's convergence theorem <Thm:Series:FourierConvergence>` implies:

\begin{align*}
&1=\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin\left(\frac{n\pi}{2}\right)=\frac{4}{\pi}\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{2k-1}\\
&{}\quad\Longrightarrow\quad\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{2k-1}=\frac{1}{4}\pi.
\end{align*}

Using {prf:ref}`Parseval's identity <Thm:Series:Parseval>` we have:

\begin{align*}
&\frac{16}{\pi^2}\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{1}{1}\int_{-1}^1\{f(x)\}^2\,dx=\int_{-1}^14x^2\,dx=\frac{4}{3}x^3\bigg|_{-1}^1=\frac{8}{3}\\
&{}\quad\Longrightarrow\quad\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{1}{6}\pi^2.
\end{align*}
::::::

::::::{prf:example}
:label: Ex:Series:FourierExample3
Consider the function $f$ defined by

$$
f(x) = \begin{cases}
f(x+2), & x < -1, \\
1-x^2, & -1 \leq x \leq 1, \\
f(x-2), & x > 1.
\end{cases}
$$

Then $f$ is even on $(-1,1)$ and periodic with period $2$, so $L=1$. Using {prf:ref}`Thm:Series:FourierCosineSeries` we have that the Fourier series $g$ of $f$ is a Fourier cosine series, so we only calculate the Fourier cosine coefficients $a_n$ for $n=0,1,2,3,\ldots$ and find

$$
a_0=\frac{1}{1}\int_{-1}^1f(x)\,dx
=\int_{-1}^1(1-x^2)\,dx=\left[x-\frac{1}{3}x^3\right]_{-1}^1=\frac{4}{3}
$$

and

\begin{align*}
a_n&=\frac{1}{1}\int_{-1}^1f(x)\cos(n\pi x)\,dx=\int_{-1}^1(1-x^2)\cos(n\pi x)\,dx\\
&=\frac{1}{n\pi}\int_{-1}^1(1-x^2)\,d\sin(n\pi x)\\
&=\frac{(1-x^2)\sin(n\pi x)}{n\pi}\bigg|_{-1}^1+\frac{1}{n\pi}\int_{-1}^12x\sin(n\pi x)\,dx\\
&=-\frac{1}{n^2\pi^2}\int_{-1}^12x\,d\cos(n\pi x)\\
&=-\frac{2x\cos(n\pi x)}{n^2\pi^2}+\frac{2}{n^2\pi^2}\int_{-1}^1\cos(n\pi x)\,dx\\
&=-\frac{4\cos(n\pi)}{n^2\pi^2}=\frac{4(-1)^{n+1}}{n^2\pi^2},\quad n=1,2,3,\ldots.
\end{align*}

This means that the Fourier series $g$ of $f$ is given by

$$
g(x)=\frac{2}{3}+\frac{4}{\pi^2}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}\cos(n\pi x).
$$

The function $f$ is an example of a full-wave rectified sine wave, which is a function that looks like the absolute value of a sine wave. Even better, because the function $f$ is continuous on $\mathbb{R}$, the Gibbs phenomenon should not occur here and we can state that $f(x)=g(x)$ for all $x \in \mathbb{R}$.

As you can see in {numref}`Fig:Series:RectifiedSineFourier`, where we have plotted some partial sums of the Fourier series $g$ of $f$ together with the function $f$ itself, the function $f$ is continuous and the Gibbs phenomenon does not occur.

:::{figure} Images/fourier3.png
:name: Fig:Series:RectifiedSineFourier
:width: 50%

A full-wave rectified sine wave.
:::

:::{todo}
Replace {numref}`Fig:Series:RectifiedSineFourier` with an applet, where you can change the value of $N$ to see how the approximation changes.
:::

For $x=0$ {prf:ref}`Fourier's convergence theorem <Thm:Series:FourierConvergence>` implies:

$$
1=\frac{2}{3}+\frac{4}{\pi^2}\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}\quad\Longrightarrow\quad\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}=\frac{1}{12}\pi^2.
$$

For $x=1$ {prf:ref}`Fourier's convergence theorem <Thm:Series:FourierConvergence>` implies:

$$
0=\frac{2}{3}+\frac{4}{\pi^2}\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}(-1)^n\quad\Longrightarrow\quad\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{1}{6}\pi^2.
$$

Using {prf:ref}`Parseval's identity <Thm:Series:Parseval>` we have:

\begin{align*}
\frac{8}{9}+\frac{16}{\pi^4}\sum_{n=1}^{\infty}\frac{1}{n^4}&=\frac{1}{1}\int_{-1}^1\{f(x)\}^2\,dx=\int_{-1}^1(1-x^2)^2\,dx\\
&=\int_{-1}^1(1-2x^2+x^4)\,dx=\left[x-\frac{2}{3}x^3+\frac{1}{5}x^5\right]_{-1}^1=\frac{16}{15}
\end{align*}
or equivalently

$$
\frac{16}{\pi^4}\sum_{n=1}^{\infty}\frac{1}{n^4}=\frac{16}{15}-\frac{8}{9}=\frac{8}{45}\quad\Longrightarrow\quad
\sum_{n=1}^{\infty}\frac{1}{n^4}=\frac{1}{90}\pi^4.
$$

::::::

## Fourier series of arbitrary functions

On inspection of {prf:ref}`Def:Series:FourierFormula`, we see that to construct a Fourier series of a function $f$, it must have at least the following properties:

* $f$ must be defined on an interval $[-L,L]$ for some $L>0$;
* $f$ must be periodic with period $2L$;
* $f$ must be piecewise continuous on $[-L,L]$.

However, in many applications the function $f$ might only be defined on an interval $[0,L]$ with $L>0$. An example is when $f$ describes the motion of a vibrating string with length $L$. In most of those case the function $f$ is also piecewise continuous on $[0,L]$, but it might not be periodic with period $2L$. This means that we cannot directly apply {prf:ref}`Def:Series:FourierFormula` to find the Fourier series of $f$.

If we do want to do this, we must perform two steps. First, we must extend the function $f$ to a function defined on $[-L,L]$. Second, we must extend this function to a function defined on $\mathbb{R}$ that is periodic with period $2L$.

Let us focus on the first step, for which we can use the next theorem from {numref}`Section:PropertiesFunctions`:

:::{fetch} {prf:ref}`Thm:PropertiesFunctions:EvenOddExtension`
:::

Note that the extension of $f$ to a function defined on $[-L,L]$ is not unique, and the choice of the extension will determine the Fourier series of $f$. Note that if we choose to extend $f$ to an _odd_ function on $(-L,L)$, the value of the extension at $0$ becomes $0$, irrespective of the value of $f$ at $0$.

Next up, making the function periodic with period $2L$. Here {numref}`Section:PropertiesFunctions` comes to the rescue again with the next theorem:

:::{fetch} {prf:ref}`Thm:PropertiesFunctions:PeriodicExtension`
:::

Another, but equivalent, way to define the periodic extension of $f$ to a function defined on $[a,b)$ that is periodic with period $\ell=b-a$ is to define it as

$$
f_{\mathrm{ext}} =
\begin{cases}
f_{\mathrm{ext}}(x+\ell), & x < a, \\
f(x), & a \leq x < b, \\
f_{\mathrm{ext}}(x-\ell), & x \geq b.
\end{cases}
$$

Now we have discussed the two steps to extend a function $f$ defined on $[0,L]$ to a function defined on $\mathbb{R}$ that is periodic with period $2L$ and is either odd or even, we can apply {prf:ref}`Def:Series:FourierFormula` to find the Fourier series of $f$. If we choose to extend $f$ to an odd function on $(-L,L)$, then the Fourier series of $f$ will be a Fourier sine series, and if we choose to extend $f$ to an even function on $(-L,L)$, then the Fourier series of $f$ is a Fourier cosine series.

Let us do an example to see how this works in practice.

::::::{prf:example}
:label: Ex:Series:FourierExample4

Consider $f(x)=2x$ for $0\leq x\leq 1$, so $L=2$ in this case. We want to find a Fourier series of $f$.

If we define $f_{\mathrm{odd}}$ as the odd periodic extension of $f$ to $\mathbb{R}$ with period $2L=2$, we find that $f_{\mathrm{odd}}$ is given by

\begin{align*}
f_{\mathrm{odd}}(x) &= \begin{cases}
f_{\mathrm{odd}}(x+2), & x \leq -1, \\
-f(-x), & -1 < x < 0, \\
0, & x=0, \\
f(x), & 0 < x \leq 1, \\
f_{\mathrm{odd}}(x-2), & x > 1,
\end{cases}
\\ &=
\begin{cases}
f_{\mathrm{odd}}(x+2), & x \leq -1, \\
-2(-x), & -1 < x < 0, \\
0, & x=0, \\
2x, & 0 < x \leq 1, \\
f_{\mathrm{odd}}(x-2), & x > 1,
\end{cases}
\\ &=
\begin{cases}
f_{\mathrm{odd}}(x+2), & x \leq -1, \\
2x, & -1 < x \leq 1, \\
f_{\mathrm{odd}}(x-2), & x > 1.
\end{cases}
\end{align*}

Note that to avoid defining the value of $f_{\mathrm{odd}}$ at $-1+2n$ for any integer $n$ twice, we have defined $f_{\mathrm{odd}}$ at those points as $f_{\mathrm{odd}}(x+2)$ for $x \leq -1$ and as $f_{\mathrm{odd}}(x-2)$ for $x > 1$. This is just a technicality to avoid defining the value of $f_{\mathrm{odd}}$ at those points twice, and it does not change the function $f$ itself on the interval $(0,1]$.

The function $f_{\mathrm{odd}}$ turns out to be exactly the function $f$ defined in {prf:ref}`Ex:Series:FourierExample2`, which was a sawtooth wave. The Fourier sine series $g$ of $f_{\mathrm{odd}}$ is given by Equation {eq}`Eq:Series:SawToothFourier` and a visualization of the Fourier sine series $g$ of $f_{\mathrm{odd}}$ can be found in {numref}`Fig:Series:SawToothFourier`.

If we define $f_{\mathrm{even}}$ as the even periodic extension of $f$ to $\mathbb{R}$ with period $2L=2$, we find that $f_{\mathrm{even}}$ is given by

\begin{align*}
f_{\mathrm{even}}(x) &= \begin{cases}
f_{\mathrm{even}}(x+2), & x \leq -1, \\
f(-x), & -1 < x < 0, \\
f(x), & 0 \leq x \leq 1, \\
f_{\mathrm{even}}(x-2), & x > 1,
\end{cases}
\\ &=
\begin{cases}
f_{\mathrm{even}}(x+2), & x \leq -1, \\
f(-x), & -1 < x < 0, \\
f(x), & 0 \leq x \leq 1, \\
f_{\mathrm{even}}(x-2), & x > 1,
\end{cases}
\\ &=
\begin{cases}
f_{\mathrm{even}}(x+2), & x \leq -1, \\
-2x, & -1 < x < 0, \\
2x, & -1 < x \leq 1, \\
f_{\mathrm{even}}(x-2), & x > 1.
\end{cases}
\end{align*}

Again, we avoid double values at $x=-1+2n$ for any integer $n$ by defining $f_{\mathrm{even}}$ at those points as $f_{\mathrm{even}}(x+2)$ for $x \leq -1$ and as $f_{\mathrm{even}}(x-2)$ for $x > 1$.

Now we have an even periodic extension $f_{\mathrm{even}}$ of $f$ to $\mathbb{R}$ with period $2L=2$, so we can apply {prf:ref}`Thm:Series:FourierCosineSeries` to find the Fourier cosine series $h$ of $f_{\mathrm{even}}$. We have for that

$$
a_0=\frac{2}{1}\int_0^1f(x)\,dx=2\int_0^12x\,dx=2x^2\bigg|_0^1=2,
$$

and for $n=0,1,2,3,\ldots$

\begin{align*}
a_n&=\frac{2}{1}\int_0^1f(x)\cos(n\pi x)\,dx \\
&=2\int_0^12x\cos(n\pi x)\,dx\\
&=\frac{4x\sin(n\pi x)}{n\pi}\bigg|_0^1-\frac{4}{n\pi}\int_0^1\sin(n\pi x)\,dx\\
&=\frac{4}{n^2\pi^2}\cos(n\pi x)\bigg|_0^1 \\
&=\frac{4\left((-1)^{n}-1\right)}{n^2\pi^2},
\end{align*}

and therefore

$$
h(x)=1+\frac{4}{\pi^2}\sum_{n=1}^{\infty}\frac{(-1)^n-1}{n^2}\cos(n\pi x).
$$

Because our function $f_{\mathrm{even}}$ is continuous on $\mathbb{R}$, the Gibbs phenomenon does not occur and we have that $h(x)=f_{\mathrm{even}}(x)$ for all $x \in \mathbb{R}$.

{numref}`Fig:Series:TriangularWave` shows a plot of the partial sum of the Fourier cosine series $h$ of $f_{\mathrm{even}}$ together with the function $f_{\mathrm{even}}$ itself. We also included the partial sum of the Fourier sine series $g$ of $f_{\mathrm{odd}}$ in the plot to show the difference between the two extensions.
You can change the value of $N$ to see how the approximation changes.

:::{figure} Images/fourier5.png
:name: Fig:Series:TriangularWave
:width: 50%

Truncated Fourier series of the even and odd periodic extensions of $f(x)=2x$ on $[0,1]$.
:::

:::{todo}
Replace {numref}`Fig:Series:TriangularWave` with an applet, where you can change the value of $N$ to see how the approximation changes.
:::

The even periodic extension $f_{\mathrm{even}}$ is an example of a *triangular wave*.

::::::

The last example shows that if we want to avoid the Gibbs phenomenon, we should extend $f$ to a function that is continuous on $\mathbb{R}$, if possible. In the example we have seen that the odd periodic extension $f_{\mathrm{odd}}$ of $f$ is not continuous on $\mathbb{R}$, and therefore the Gibbs phenomenon occurs in the Fourier sine series $g$ of $f_{\mathrm{odd}}$. On the other hand, the even periodic extension $f_{\mathrm{even}}$ of $f$ is continuous on $\mathbb{R}$, and therefore the Gibbs phenomenon does not occur in the Fourier cosine series $h$ of $f_{\mathrm{even}}$.

In practice using an even periodic extension is more common than using an odd periodic extension of $f$, as the even periodic extension of a function $f$ that is continuous on $[0,L]$ is also continuous on $\mathbb{R}$, while the odd periodic extension of a function $f$ that is continuous on $[0,L]$ can only be continuous on $\mathbb{R}$ if $f(0)=0=f(L)$.