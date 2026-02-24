(Section:Fourier)=

# Fourier series

In this section we cover:

- Periodic functions (Willem: already covered in 3.2)
- Fourier series
- Convergence of Fourier series
- Fourier sine and cosine series

## Introduction

We have seen that Taylor polynomials can be used to approximate a function $f(x)$ near a point $x=a$ as closely as is needed by taking the order large enough. However, in many applications it is much more useful to approximate *periodic functions*. For instance, for functions that describe waves, signal processes or heat flows. In these cases it is useful to decompose such functions in standard periodic functions.

::::::{prf:definition}
A function $f\,:\,\mathbb{R}\to\mathbb{R}$ is called periodic with **period** $T$ if

$$
f(x+T)=f(x)\quad\text{for all}\;x\in\mathbb{R}.
$$

The smallest value of $T$ for which this holds is called the **fundamental period** of $f$.
::::::

Consider the functions $\displaystyle\cos\left(\frac{n\pi x}{L}\right)$ and $\displaystyle\sin\left(\frac{n\pi x}{L}\right)$ with $n$ a positive integer. These functions are all periodic with period $2L$. Moreover, they satisfy a remarkable orthogonality property (compare with {numref}`Exc:Integration:TrigFunctionsProductFormulasOrthogonality`):

::::::{prf:theorem} Orthogonality
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

::::::{note}
Define an **inner product**: $\langle f,g\rangle=\displaystyle\int_{\alpha}^{\beta}f(x)g(x)\,dx$ for functions $f$ and $g$ defined on the interval $(\alpha,\beta)$. Then: two functions $f$ and $g$ are called **orthogonal** if $\langle f,g\rangle=0$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:Orthogonality`
:class: solution, dropdown
Using the product formula $\cos(a)\cos(b)=\frac{1}{2}\left(\cos(a-b)+\cos(a+b)\right)$ (see {prf:ref}`Thm:Trigonometry:ProductFormulas`) we obtain

\begin{align*}
&\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\cos\left(\frac{n\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\int_{-L}^L\cos\left(\frac{(m-n)\pi x}{L}\right)\,dx+\frac{1}{2}\int_{-L}^L\cos\left(\frac{(m+n)\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\left[\frac{L}{(m-n)\pi}\sin\left(\frac{(m-n)\pi x}{L}\right)+\frac{L}{(m+n)\pi}\sin\left(\frac{(m+n)\pi x}{L}\right)\right]_{-L}^L\\
&=0,\quad m\neq n
\end{align*}
and for $m=n$ we use $\cos(2a)=2\cos^2(a)-1$ to find that

\begin{align*}
\int_{-L}^L\left\{\cos\left(\frac{n\pi x}{L}\right)\right\}^2\,dx&=\frac{1}{2}\int_{-L}^L\left\{1+\cos\left(\frac{2n\pi x}{L}\right)\right\}\,dx\\
&=\frac{1}{2}\left[x+\frac{L}{2n\pi}\sin\left(\frac{2n\pi x}{L}\right)\right]_{-L}^L=L.
\end{align*}
Using the product formula $\sin(a)\sin(b)=\frac{1}{2}\left(\cos(a-b)-\cos(a+b)\right)$ (see  {prf:ref}`Thm:Trigonometry:ProductFormulas`) we obtain

\begin{align*}
&\int_{-L}^L\sin\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\int_{-L}^L\cos\left(\frac{(m-n)\pi x}{L}\right)\,dx-\frac{1}{2}\int_{-L}^L\cos\left(\frac{(m+n)\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\left[\frac{L}{(m-n)\pi}\sin\left(\frac{(m-n)\pi x}{L}\right)-\frac{L}{(m+n)\pi}\sin\left(\frac{(m+n)\pi x}{L}\right)\right]_{-L}^L\\
&=0,\quad m\neq n
\end{align*}
and for $m=n$ we use $\cos(2a)=1-2\sin^2(a)$ to find that

\begin{align*}
\int_{-L}^L\left\{\sin\left(\frac{n\pi x}{L}\right)\right\}^2\,dx&=\frac{1}{2}\int_{-L}^L\left\{1-\cos\left(\frac{2n\pi x}{L}\right)\right\}\,dx\\
&=\frac{1}{2}\left[x-\frac{L}{2n\pi}\sin\left(\frac{2n\pi x}{L}\right)\right]_{-L}^L=L.
\end{align*}
Finally we use the product formula $\cos(a)\sin(b)=\frac{1}{2}\left(\sin(a+b)-\sin(a-b)\right)$ (see  {prf:ref}`Thm:Trigonometry:ProductFormulas`) to obtain

\begin{align*}
&\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\int_{-L}^L\sin\left(\frac{(m+n)\pi x}{L}\right)\,dx-\frac{1}{2}\int_{-L}^L\sin\left(\frac{(m-n)\pi x}{L}\right)\,dx\\
&=\frac{1}{2}\left[-\frac{L}{(m+n)\pi}\cos\left(\frac{(m+n)\pi x}{L}\right)+\frac{L}{(m-n)\pi}\cos\left(\frac{(m-n)\pi x}{L}\right)\right]_{-L}^L\\
&=0,\quad m\neq n
\end{align*}
and

$$
\int_{-L}^L\cos\left(\frac{n\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx=\frac{1}{2}\int_{-L}^L\sin\left(\frac{2n\pi x}{L}\right)\,dx=0.
$$

:::

## General Fourier series

::::::{prf:definition} Fourier series
:label: Def:Series:FourierSeries
A series of the form

$$
\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos\left(\frac{n\pi x}{L}\right)+b_n\sin\left(\frac{n\pi x}{L}\right)\right)
$$

with $L>0$ is called a **Fourier series**, named after the French mathematician [Jean-Baptiste Joseph Fourier (1768-1830)](https://en.wikipedia.org/wiki/Joseph_Fourier).
::::::

Now, periodic functions can be expanded in terms of a Fourier series:

::::::{prf:theorem} Fourier
:label: Thm:Series:Fourier
If $f$ and $f'$ are piecewise continuous on an interval $[-L,L)$ and $f$ is defined outside that interval so that it is periodic with period $2L$, then we have:

$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos\left(\frac{n\pi x}{L}\right)+b_n\sin\left(\frac{n\pi x}{L}\right)\right)
$$

with $a_0=\displaystyle\frac{1}{L}\int_{-L}^Lf(x)\,dx$ and for $n=1,2,3,\ldots$

$$
a_n=\frac{1}{L}\int_{-L}^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx\quad\text{and}\quad b_n=\frac{1}{L}\int_{-L}^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$

These are called the **Euler-Fourier formulas**, named after the Swiss mathematician [Leonhard Euler (1707-1783)](https://en.wikipedia.org/wiki/Leonhard_Euler) and the French mathematician [Jean-Baptiste Joseph Fourier (1768-1830)](https://en.wikipedia.org/wiki/Joseph_Fourier).
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:Fourier`
:class: solution, dropdown
Let $f(x)=\displaystyle\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos\left(\frac{n\pi x}{L}\right)+b_n\sin\left(\frac{n\pi x}{L}\right)\right)$, then integration gives

\begin{align*}
\int_{-L}^Lf(x)\,dx&=\frac{a_0}{2}\int_{-L}^L\,dx\\
&{}\quad{}+\sum_{n=1}^{\infty}\left(a_n\int_{-L}^L\cos\left(\frac{n\pi x}{L}\right)\,dx+b_n\int_{-L}^L\sin\left(\frac{n\pi x}{L}\right)\,dx\right).
\end{align*}
Note that $\displaystyle\int_{-L}^L\,dx=2L$, $\displaystyle\int_{-L}^L\cos\left(\frac{n\pi x}{L}\right)\,dx=0$ and $\displaystyle\int_{-L}^L\sin\left(\frac{n\pi x}{L}\right)\,dx=0$. Hence we have

$$
\int_{-L}^Lf(x)\,dx=a_0L\quad\Longleftrightarrow\quad a_0=\frac{1}{L}\int_{-L}^Lf(x)\,dx.
$$

If we multiply by $\displaystyle\cos\left(\frac{m\pi x}{L}\right)$ and then integrate, we obtain

\begin{align*}
\int_{-L}^Lf(x)\cos\left(\frac{m\pi x}{L}\right)\,dx&=\frac{a_0}{2}\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\,dx\\
&{}\quad{}+\sum_{n=1}^{\infty}a_n\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\cos\left(\frac{n\pi x}{L}\right)\,dx\\
&{}\quad{}+\sum_{n=1}^{\infty}b_n\int_{-L}^L\cos\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx.
\end{align*}
Then {prf:ref}`Thm:Series:Orthogonality` implies that for $m=1,2,3,\ldots$

$$
\int_{-L}^Lf(x)\cos\left(\frac{m\pi x}{L}\right)\,dx=a_mL\quad\Longleftrightarrow\quad a_m=\frac{1}{L}\int_{-L}^Lf(x)\cos\left(\frac{m\pi x}{L}\right)\,dx.
$$

If we multiply by $\displaystyle\sin\left(\frac{m\pi x}{L}\right)$ and then integrate, we obtain

\begin{align*}
\int_{-L}^Lf(x)\sin\left(\frac{m\pi x}{L}\right)\,dx&=\frac{a_0}{2}\int_{-L}^L\sin\left(\frac{m\pi x}{L}\right)\,dx\\
&{}\quad{}+\sum_{n=1}^{\infty}a_n\int_{-L}^L\sin\left(\frac{m\pi x}{L}\right)\cos\left(\frac{n\pi x}{L}\right)\,dx\\
&{}\quad{}+\sum_{n=1}^{\infty}b_n\int_{-L}^L\sin\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\,dx.
\end{align*}
Then {prf:ref}`Thm:Series:Orthogonality` implies that for $m=1,2,3,\ldots$

$$
\int_{-L}^Lf(x)\sin\left(\frac{m\pi x}{L}\right)\,dx=b_mL\quad\Longleftrightarrow\quad b_m=\frac{1}{L}\int_{-L}^Lf(x)\sin\left(\frac{m\pi x}{L}\right)\,dx.
$$

:::

::::::{prf:theorem} Convergence
:label: Thm:Series:Convergence
The Fourier series given in {prf:ref}`Thm:Series:Fourier` converges at all points $x$ to

$$
\frac{f(x-)+f(x+)}{2},
$$ 

where $f(x-)=\lim\limits_{t\to x^{-}}f(t)$ and $f(x+)=\lim\limits_{t\to x^{+}}f(t)$. At points $x$, where $f$ is continuous, we have: $\lim\limits_{t\to x^{-}}f(t)=f(x)=\lim\limits_{t\to x^{+}}f(t)$ and therefore: $\displaystyle\frac{f(x-)+f(x+)}{2}=f(x)$.
::::::

::::::{prf:theorem} Parseval's identity
:label: Thm:Series:Parseval
For the Fourier series given in {prf:ref}`Thm:Series:Fourier` we also have

$$
\frac{1}{L}\int_{-L}^L\left\{f(x)\right\}^2\,dx=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}\left(a_n^2+b_n^2\right).
$$

This is called **Parseval's identity**, named after the French mathematician [Marc-Antoine Parseval (1755-1836)](https://en.wikipedia.org/wiki/Marc-Antoine_Parseval).
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:Parseval`
:class: solution, dropdown
Let $f(x)=\displaystyle\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos\left(\frac{n\pi x}{L}\right)+b_n\sin\left(\frac{n\pi x}{L}\right)\right)$, then multiplication by $f(x)$ and integration gives

\begin{align*}
\frac{1}{L}\int_{-L}^L\left\{f(x)\right\}^2\,dx&=\frac{a_0}{2}\cdot\frac{1}{L}\int_{-L}^Lf(x)\,dx\\
&{}\quad{}+\sum_{n=1}^{\infty}a_n\cdot\frac{1}{L}\int_{-L}^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx\\
&{}\quad{}+\sum_{n=1}^{\infty}b_n\cdot\frac{1}{L}\int_{-L}^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx\\
&=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}\left(a_n^2+b_n^2\right).
\end{align*}
:::

## Fourier cosine and sine series

In {prf:ref}`Thm:Integration:OddEven` we have seen: let $g$ be a continuous function defined on $[-L,L]$. Then we have

(a) If $g$ is *odd*, id est $g(-x)=-g(x)$ for all $x$, then: $\displaystyle\int_{-L}^Lg(x)\,dx=0$.

(b) If $g$ is *even*, id est $g(-x)=g(x)$ for all $x$, then: $\displaystyle\int_{-L}^Lg(x)\,dx=2\int_0^Lg(x)\,dx$.

Note that this also holds when $g$ is piecewise continuous. Moreover, we have the following rules of calculation:

* If $g$ is even and $h$ is even, then $g\cdot h$ is even;

* If $g$ is even and $h$ is odd, then $g\cdot h$ is odd;

* If $g$ is odd and $h$ is odd, then $g\cdot h$ is even.

Hence, we have: if $f$ is *even*, then we have $\displaystyle\frac{1}{L}\int_{-L}^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx=0$ and

$$
\frac{1}{L}\int_{-L}^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx=\frac{2}{L}\int_0^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx.
$$

And, if $f$ is *odd*, then we have $\displaystyle\frac{1}{L}\int_{-L}^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx=0$ and 

$$
\frac{1}{L}\int_{-L}^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx=\frac{2}{L}\int_0^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$

::::::{prf:theorem} Fourier cosine series
:label: Thm:Series:FourierCosineSeries
If $f$ is an *even* function on $(-L,L)$ and oustide that interval periodic with period $2L$, then we have:

$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos\left(\frac{n\pi x}{L}\right)
$$

with $a_0=\displaystyle\frac{2}{L}\int_0^Lf(x)\,dx$ and $a_n=\displaystyle\frac{2}{L}\int_0^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx$ for $n=1,2,3,\ldots$.
::::::

::::::{prf:theorem} Fourier sine series
:label: Thm:Series:FourierSineSeries
If $f$ is an *odd* function on $(-L,L)$ and oustide that interval periodic with period $2L$, then we have:

$$
f(x)=\sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{L}\right)
$$

with $b_n=\displaystyle\frac{2}{L}\int_0^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx$ for $n=1,2,3,\ldots$.
::::::

In many applications the function $f$ is defined on an interval $[0,L]$ with $L>0$. For instance, when $f$ describes the motion of a vibrating string with length $L$. Then this function can be defined to be *even* on the interval $(-L,L)$ and outside that interval periodically with period $2L$, but it can also be defined to be *odd* on the interval $(-L,L)$ and outside that interval periodically with period $2L$. So, such a function can be written as a Fourier cosine series, but also as a Fourier sine series:

$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos\left(\frac{n\pi x}{L}\right)=\sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{L}\right)
$$

with $a_0=\displaystyle\frac{2}{L}\int_0^Lf(x)\,dx$ and for $n=1,2,3,\ldots$

$$
a_n=\frac{2}{L}\int_0^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\,dx\quad\text{and}\quad b_n=\frac{2}{L}\int_0^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$

::::::{prf:example}
:label: Ex:Series:FourierExample1
Consider $f(x)=\begin{cases}0,&-\pi\leq x < 0\\1,&0\leq x < \pi\end{cases}$ and $f(x+2\pi)=f(x)$.

Then: $L=\pi$ and $a_0=\displaystyle\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\,dx=\frac{1}{\pi}\int_0^{\pi}dx=1$. Further we have for $n=1,2,3,\ldots$

$$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx=\frac{1}{\pi}\int_0^{\pi}\cos(nx)\,dx=\frac{1}{n\pi}\sin(nx)\bigg|_0^{\pi}=0
$$

and

$$\begin{align*}
b_n&=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx=\frac{1}{\pi}\int_0^{\pi}\sin(nx)\,dx=-\frac{1}{n\pi}\cos(nx)\bigg|_0^{\pi}\\
&=\frac{1-\cos(n\pi)}{n\pi}=\frac{1-(-1)^n}{n\pi}.
\end{align*}
Note that $b_{2k}=0$ and $b_{2k-1}=\displaystyle\frac{2}{(2k-1)\pi}$ for $k=1,2,3,\ldots$. Then we have that

$$
f(x)=\frac{1}{2}+\sum_{n=1}^{\infty}\frac{1-(-1)^n}{n\pi}\sin(nx)=\frac{1}{2}+\frac{2}{\pi}\sum_{k=1}^{\infty}\frac{\sin(2k-1)x}{2k-1}.
$$

A plot of some partial sums of this series:

:::{figure} Images/fourier1.png
:name: fourier1
:width: 50%

A square wave.
:::

This is an example of a *square wave*. Around the jump points the **Gibbs phenomenon** (see below) is visible.

For $x=\frac{1}{2}\pi$ Fourier's theorem implies:

\begin{align*}
1=\frac{1}{2}+\frac{2}{\pi}\sum_{k=1}^{\infty}\frac{\sin(k-\frac{1}{2})\pi}{2k-1}&\quad\Longleftrightarrow\quad
\frac{1}{2}=\frac{2}{\pi}\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{2k-1}\\
&\quad\Longleftrightarrow\quad
\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{2k-1}=\frac{1}{4}\pi.
\end{align*}
Using {prf:ref}`Parseval's identity <Thm:Series:Parseval>` we have:

\begin{align*}
&\frac{1}{2}+\frac{4}{\pi^2}\sum_{k=1}^{\infty}\frac{1}{(2k-1)^2}=\frac{1}{\pi}\int_{-\pi}^{\pi}\{f(x)\}^2\,dx=\frac{1}{\pi}\int_0^{\pi}dx=1\\
&{}\quad\Longrightarrow\quad\sum_{k=1}^{\infty}\frac{1}{(2k-1)^2}=\frac{1}{8}\pi^2.
\end{align*}
::::::

::::::{prf:remark} Gibbs phenomenon
Note that all partial sums of a Fourier series (linear combination of cosines and/or sines) are continuous functions. {prf:ref}`Fourier's convergence theorem <Thm:Series:Convergence>` implies that the series converges to $f(x)$ at points $x$ where $f$ is continuous and to

$$
\frac{f(x-)+f(x+)}{2}
$$

at points $x$ where $f$ is discontinuous. Near points with a jump discontinuity we see an oscillatory behavior (some kind of 'overshoot' and 'undershoot'). This **Gibbs phenomenon** is named after the American scientist [Josiah Willard Gibbs (1839-1903)](https://en.wikipedia.org/wiki/Josiah_Willard_Gibbs).
::::::

::::::{prf:example}
:label: Ex:Series:FourierExample2
Consider $f(x)=2x$ for $-1\leq x\leq 1$ and $f(x+2)=f(x)$.

Then: $L=1$ and $f$ is odd, so $a_n=0$ for $n=0,1,2,\ldots$ and

\begin{align*}
b_n&=\frac{1}{1}\int_{-1}^1f(x)\sin(n\pi x)\,dx=\int_{-1}^12x\sin(n\pi x)\,dx\\
&=-\frac{1}{n\pi}\int_{-1}^12x\,d\cos(n\pi x)\\
&=-\frac{2x\cos(n\pi x)}{n\pi}\bigg|_{-1}^1+\frac{2}{n\pi}\int_{-1}^1\cos(n\pi x)\,dx\\
&=-\frac{4\cos(n\pi)}{n\pi}=\frac{4(-1)^{n+1}}{n\pi},\quad n=1,2,3,\ldots.
\end{align*}
Hence: $f(x)=\displaystyle\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(n\pi x)$.

:::{figure} Images/fourier2.png
:name: fourier2
:width: 50%

A sawtooth wave.
:::

This is an example of a *sawtooth wave*. Around the jump points the Gibbs phenomenon is visible.

For $x=\frac{1}{2}\pi$ {prf:ref}`Fourier's convergence theorem <Thm:Series:Convergence>` implies:

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
Consider $f(x)=1-x^2$ for $-1\leq x\leq 1$ and $f(x+2)=f(x)$.

Then: $L=1$ and $f$ is even, so $b_n=0$ for $n=1,2,3,\ldots$. Further we have

$$
a_0=\frac{1}{1}\int_{-1}^1f(x)\,dx
=\int_{_1}^1(1-x^2)\,dx=\left[x-\frac{1}{3}x^3\right]_{-1}^1=\frac{4}{3}
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
Hence: $f(x)=\displaystyle\frac{2}{3}+\frac{4}{\pi^2}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}\cos(n\pi x)$.

:::{figure} Images/fourier3.png
:name: fourier3
:width: 50%

A full-wave rectified sine wave.
:::

Since $f$ is continuous, the Gibbs phenomenon does not occur here.

For $x=0$ {prf:ref}`Fourier's convergence theorem <Thm:Series:Convergence>` implies:

$$
1=\frac{2}{3}+\frac{4}{\pi^2}\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}\quad\Longrightarrow\quad\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}=\frac{1}{12}\pi^2.
$$

For $x=1$ {prf:ref}`Fourier's convergence theorem <Thm:Series:Convergence>` implies:

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

::::::{prf:example}
:label: Ex:Series:FourierExample4
Consider $f(x)=x$ for $0\leq x\leq 1$.

If we define $f$ such that it is odd and periodic, then we have: $L=1$ and

\begin{align*}
b_n&=\frac{2}{1}\int_0^1f(x)\sin(n\pi x)\,dx=2\int_0^1x\sin(n\pi x)\,dx\\
&=-\frac{2}{n\pi}\int_0^1x\,d\cos(n\pi x)\\
&=-\frac{2x\cos(n\pi x)}{n\pi}\bigg|_0^1+\frac{2}{n\pi}\int_0^1\cos(n\pi x)\,dx\\
&=-\frac{2\cos(n\pi)}{n\pi}=\frac{2(-1)^{n+1}}{n\pi},\quad n=1,2,3,\ldots
\end{align*}
and therefore: $f(x)=\displaystyle\frac{2}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(n\pi x)$.

:::{figure} Images/fourier4.png
:name: fourier4
:width: 50%

A sawtooth wave.
:::

This is an example of a sawtooth wave. Around the jump points the Gibbs phenomenon is visible.

If we define $f$ such that it is even and periodic, then we have: $L=1$,

$$
a_0=\frac{2}{1}\int_0^1f(x)\,dx=2\int_0^1x\,dx=x^2\bigg|_0^1=1
$$

and

\begin{align*}
a_n&=\frac{2}{1}\int_0^1f(x)\cos(n\pi x)\,dx=2\int_0^1x\cos(n\pi x)\,dx\\
&=\frac{2}{n\pi}\int_0^1x\,d\sin(n\pi x)\\
&=\frac{2x\sin(n\pi x)}{n\pi}\bigg|_0^1-\frac{2}{n\pi}\int_0^1\sin(n\pi x)\,dx\\
&=\frac{2}{n^2\pi^2}\cos(n\pi x)\bigg|_0^1
=\frac{2\left((-1)^{n}-1\right)}{n^2\pi^2},\quad n=1,2,3,\ldots
\end{align*}
and therefore: $f(x)=\displaystyle\frac{1}{2}+\frac{2}{\pi^2}\sum_{n=1}^{\infty}\frac{(-1)^n-1}{n^2}\cos(n\pi x)$.

:::{figure} Images/fourier5.png
:name: fourier5
:width: 50%

A triangular wave.
:::

This is an example of a *triangular wave*. In this case the function is continuous and Gibbs phenomenon does not occur.

For $x=1$ {prf:ref}`Fourier's convergence theorem <Thm:Series:Convergence>` implies:

\begin{align*}
&1=\frac{1}{2}+\frac{2}{\pi^2}\sum_{n=1}^{\infty}\frac{(-1)^n-1}{n^2}(-1)^n=\frac{1}{2}+\frac{4}{\pi^2}\sum_{k=1}^{\infty}\frac{1}{(2k-1)^2}\\
&{}\quad\Longrightarrow\quad\sum_{k=1}^{\infty}\frac{1}{(2k-1)^2}=\frac{1}{8}\pi^2.
\end{align*}
Using {prf:ref}`Parseval's identity <Thm:Series:Parseval>` we have:

$$
\frac{1}{2}+\frac{16}{\pi^4}\sum_{k=1}^{\infty}\frac{1}{(2k-1)^4}=\frac{1}{1}\int_{-1}^1\{f(x)\}^2\,dx=\int_{-1}^1x^2\,dx
=\frac{1}{3}x^3\bigg|_{-1}^1=\frac{2}{3}
$$

or equivalently

$$
\frac{16}{\pi^4}\sum_{n=1}^{\infty}\frac{1}{(2k-1)^4}=\frac{2}{3}-\frac{1}{2}=\frac{1}{6}\quad\Longrightarrow\quad
\sum_{n=1}^{\infty}\frac{1}{(2k-1)^4}=\frac{1}{96}\pi^4.
$$

::::::
