(Sec:ODE2:Series)=

# Series solutions

In this section we cover:

- Ordinary and singular points
- Power series solutions around ordinary points, including Taylor series
- Bessel functions

:::{prf:remark}
Restrict to second-order differential equations.
:::

A homogeneous second-order linear differential equation has the form

:::{math}
:label: Eq:ODE2:Hom
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)=0,
:::

where $P$, $Q$ and $R$ are continuous functions with $P(x)\neq0$.

Many of these differential equations can't be solved explicitly in terms of finite combinations of simple familiar functions. This is true even for simple looking equations like

$$
xy''+y'+xy=0\quad\text{or}\quad y''-2xy'+4y=0.
$$

In the case of linear differential equations it is sometimes possible to find solutions in terms of power series. The method is to substitute such a power series into the differential equation and try to determine the values of the coefficients. We first illustrate the method by solving the differential equation $y''+y=0$ for which we already know the general solution: $y(x)=c_0\cos(x)+c_1\sin(x)$ with $c_0,c_1\in\mathbb{R}$.

::::::{prf:example}
Use power series to solve the differential equation $y''+y=0$.

Solution. We assume that there is a solution of the form $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$. Then we have: $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$. Substitution leads to

$$
\begin{align*}
&\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}+\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n+\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This implies that

$$
\begin{align*}
&\sum_{n=0}^{\infty}\left[(n+2)(n+1)c_{n+2}+c_n\right]x^n=0\\
&{}\quad\Longrightarrow\quad(n+2)(n+1)c_{n+2}+c_n=0,\quad n=0,1,2,\ldots.
\end{align*}
$$

This is a *recursion relation* for the coefficients:

$$
c_{n+2}=-\frac{c_n}{(n+1)(n+2)},\quad n=0,1,2,\ldots.
$$

If $c_0$ and $c_1$ are known, this equation allows us to determine the remaining coefficients recursively by putting $n=0,1,2,\ldots$ in succession:

$$
\begin{array}{llll}
n=0: & c_2=-\displaystyle\frac{c_0}{1\cdot2}=-\frac{c_0}{2!} &{}\hspace{10mm}n=1: & c_3=-\displaystyle\frac{c_1}{2\cdot3}=-\frac{c_1}{3!}\\[5mm]
n=2: & c_4=-\displaystyle\frac{c_2}{3\cdot4}=\frac{c_0}{1\cdot2\cdot3\cdot4}=\frac{c_0}{4!} &{}\hspace{10mm}n=3: & c_5=-\displaystyle\frac{c_3}{4\cdot5}=\frac{c_1}{2\cdot3\cdot4\cdot5}=\frac{c_1}{5!}\\[5mm]
n=4: & c_6=-\displaystyle\frac{c_4}{5\cdot6}=-\frac{c_0}{4!\cdot5\cdot6}=-\frac{c_0}{6!} &{}\hspace{10mm}n=5: & c_7=-\displaystyle\frac{c_5}{6\cdot7}=-\frac{c_1}{5!\cdot6\cdot7}=-\frac{c_1}{7!}
\end{array}
$$

and so on. We see the pattern: $c_{2n}=\displaystyle\frac{(-1)^n}{(2n)!}c_0$ and $c_{2n+1}=\displaystyle\frac{(-1)^n}{(2n+1)!}c_1$ for $n=1,2,3,\ldots$. This leads to the (general) solution

$$
\begin{align*}
y&=\sum_{n=0}^{\infty}c_nx^n=\sum_{n=0}^{\infty}c_{2n}x^{2n}+\sum_{n=0}^{\infty}c_{2n+1}x^{2n+1}\\
&=c_0\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n)!}x^{2n}+c_1\sum_{n=1}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{2n+1}\\
&=c_0\cos(x)+c_1\sin(x),\quad c_0,c_1\in\mathbb{R}.
\end{align*}
$$

:::::: 

It is not always possible to find all solutions or the general solution:

::::::{prf:example}
Find a solution of $xy''+y'+xy=0$.

Solution. Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&x\sum_{n=0}^{\infty}n(n-1)c_nx^{n-2}+\sum_{n=1}^{\infty}nc_nx^{n-1}+x\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=2}^{\infty}n(n-1)c_nx^{n-1}+\sum_{n=1}^{\infty}nc_nx^{n-1}+\sum_{n=0}^{\infty}c_nx^{n+1}=0.
\end{align*}
$$

In order to find the coefficients we rewrite the last series:

$$
\begin{align*}
&\sum_{n=2}^{\infty}n(n-1)c_nx^{n-1}+\sum_{n=1}^{\infty}nc_nx^{n-1}+\sum_{n=2}^{\infty}c_{n-2}x^{n-1}=0\\
&\quad\Longrightarrow\quad
c_1=0\;\;\text{and}\;\;\sum_{n=2}^{\infty}\left[n(n-1)c_n+nc_n+c_{n-2}\right]x^{n-1}=0.
\end{align*}
$$

So we conclude that $c_1=0$ and $c_n=-\displaystyle\frac{c_{n-2}}{n^2}$ for $n=2,3,4,\ldots$. This implies that $c_{2n+1}=0$ for $n=1,2,3,\ldots$ and

$$
\begin{align*}
c_{2n}&=-\frac{c_{2n-2}}{(2n)^2}=\frac{c_{2n-4}}{(2n)^2(2n-2)^2}=\cdots=\frac{(-1)^n}{(2n)^2(2n-2)^2\cdots2^2}c_0\\
&=\frac{(-1)^n}{2^{2n}(n!)^2}c_0,\quad n=1,2,3,\ldots.
\end{align*}
$$

This leads to the solution $y=c_0\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{2^{2n}(n!)^2}x^{2n}=c_0J_0(x)$, where $J_0(x)$ denotes the Bessel function of the first kind of order $0$. Compare with {prf:ref}`Ex:Series:Bessel`.

```{figure} Images/besselzero.png
---
width: 75%
name: The Bessel function of the first kind of order $0$
align: center
---
The Bessel function of the first kind of order $0$
```

::::::

Here $x=0$ is a so-called *singular point* of the differential equation. In this case a second linear independent solution cannot be written as a power series. We refer to more advanced texts on differential equations for the second solution $Y_0(x)$, which is called the Bessel function of the second kind of order $0$.

Sometimes it is even impossible to find power series solutions. As an example we mention the Bessel differential equation of order $\pm\frac{1}{2}$.

:::::{admonition} The Bessel differential equation of order $\pm\frac{1}{2}$ (bonus material)
:class: solution, dropdown
The Bessel differential equation of order $\pm\frac{1}{2}$ reads

:::{math}
:label: Eq:ODE2:BesselOrderHalf
x^2y''+xy'+\left(x^2-\frac{1}{4}\right)y=0,\quad x>0.
:::

There exist no solutions in the form of a power series. However, the substitution $y(x)=\dfrac{u(x)}{\sqrt{x}}$ leads to the general solution. Note that

$$
y'(x)=\frac{u'(x)\sqrt{x}-\dfrac{u(x)}{2\sqrt{x}}}{x}=\frac{u'(x)}{\sqrt{x}}-\frac{u(x)}{2x\sqrt{x}}
$$

and

$$
\begin{align*}
y''(x)&=\frac{u''(x)\sqrt{x}-\dfrac{u'(x)}{2\sqrt{x}}}{x}-\frac{u'(x)2x\sqrt{x}-u(x)3\sqrt{x}}{4x^3}\\
&=\frac{u''(x)}{\sqrt{x}}-\frac{u'(x)}{x\sqrt{x}}+\frac{3u(x)}{4x^2\sqrt{x}}.
\end{align*}
$$

Substitution into {eq}`Eq:ODE2:BesselOrderHalf` leads to

$$u''(x)x\sqrt{x}-u'(x)\sqrt{x}+\frac{3u(x)}{4\sqrt{x}}+u'(x)\sqrt{x}-\frac{u(x)}{2\sqrt{x}}+u(x)x\sqrt{x}-\frac{u(x)}{4\sqrt{x}}=0.
$$

Simplifying we end up with $\left(u''(x)+u(x)\right)x\sqrt{x}=0$. Since $x>0$ we conclude that

$$
u''(x)+u(x)=0
$$

which has the general solution $u(x)=c_1\cos(x)+c_2\sin(x)$ with $c_1,c_2\in\mathbb{R}$. This leads to the general solution

$$
y(x)=c_1\frac{\cos(x)}{\sqrt{x}}+c_2\frac{\sin(x)}{\sqrt{x}},\quad c_1,c_2\in\mathbb{R}
$$

of the Bessel differential equation {eq}`Eq:ODE2:BesselOrderHalf`.

The function $J_{1/2}(x)=\displaystyle\sqrt{\frac{2}{\pi\,x}}\sin(x)$ for $x>0$ is called the Bessel function of the first kind of order $\frac{1}{2}$ and the function $J_{-1/2}(x)=\displaystyle\sqrt{\frac{2}{\pi\,x}}\cos(x)$ for $x>0$ is called the Bessel function of the first kind of order $-\frac{1}{2}$.

```{figure} Images/besselhalf.png
---
width: 75%
name: The Bessel functions of the first kind of order $\pm\frac{1}{2}$
align: center
---
The Bessel functions of the first kind of order $\pm\frac{1}{2}$
```

:::::

In cases like this we need so-called generalized power series to find the general solution. This method, named after the German mathematician [Ferdinand Georg Frobenius (1849-1917)](https://en.wikipedia.org/wiki/Ferdinand_Georg_Frobenius), does not fit in the scope of this book. We refer to more advanced text on differential equation for this.

::::::{prf:definition} Ordinary and singular points (1)
A point $x_0$ is called an **ordinary point** or **regular point** of the differential equation {eq}`Eq:ODE2:Hom` if $P(x_0)\neq0$. Otherwise, so if $P(x_0)=0$, it is called a **singular point**.
::::::

Suppose that $x_0$ is an ordinary point of the differential equation. Since $P(x)$ is continuous, it follows that there exists an open interval $I$ containing $x_0$ in which $P(x)$ is never zero. In that interval $I$ the differential equation can be divided by $P(x)$ to obtain

:::{math}
:label: Eq:ODE2:HomStandard
y''(x)+p(x)y'(x)+q(x)y(x)=0,
:::

where $p(x)=\displaystyle\frac{Q(x)}{P(x)}$ and $q(x)=\displaystyle\frac{R(x)}{P(x)}$ are continuous functions on $I$. Hence, the existence and uniqueness theorem implies that there exists a unique solution of the differential equation in the interval $I$ that also satisfies the initial conditions $y(x_0)=x_0$ and $y'(x_0)=y_0'$ for arbitrary values of $y_0$ and $y_0'$. In that case the general solution of the differential equation can be written as a power series of the form $y(x)=\displaystyle\sum_{n=0}^{\infty}c_n(x-x_0)^n$ with a positive radius of convergence.

::::::{prf:definition} Ordinary and singular points (2)
A point $x_0$ is called an **ordinary point** or **regular point** of the differential equation {eq}`Eq:ODE2:HomStandard` if both $p(x)$ and $q(x)$ are analytic for $x=x_0$. Otherwise, $x=x_0$ is called a **singular point** of the differential equation.
::::::

::::::{prf:theorem}
:label: Thm:ODE2:OrdinaryPoint
If $x_0$ is an ordinary point of the differential equation

$$
y''(x)+p(x)y'(x)+q(x)y(x)=0,
$$

then both $p(x)$ and $q(x)$ are analytic at $x=x_0$. That means that there exist positive constants $R_1$ and $R_2$ such that

$$
p(x)=\sum_{n=0}^{\infty}p_0(x-x_0)^n,\quad|x-x_0| < R_1
$$

and

$$
q(x)=\sum_{n=0}^{\infty}q_n(x-x_0)^n,\quad|x-x_0| < R_2.
$$

Then there exist solutions $y(x)$ of the differential equation that are analytic at $x=x_0$. In fact, if $R=\min\{R_1,R_2\}$ then the general solution can be written as

$$
y(x)=\sum_{n=0}^{\infty}c_n(x-x_0)^n,\quad|x-x_0| < R.
$$

Moreover $c_0=y(x_0)$ and $c_1=y'(x_0)$ can be chosen arbitrarily and we have that $y(x)=c_0y_1(x)+c_1y_2(x)$ where $y_1(x)$ and $y_2(x)$ are linearly independent solutions.
::::::
 
::::::{prf:example}
Use power series to find a polynomial solution of $y''-2xy'+4y=0$.

Solution. Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-2x\sum_{n=1}^{\infty}nc_nx^{n-1}+4\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n-2\sum_{n=0}^{\infty}nc_nx^n+4\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+2)(n+1)c_{n+2}-(2n-4)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=\frac{2(n-2)}{(n+1)(n+2)}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$
 
Putting $n=0,1,2,\ldots$ successively, we obtain:

$$
\begin{array}{llll}
n=0: & c_2=\displaystyle\frac{-4}{1\cdot2}c_0=-2c_0 &{}\hspace{10mm}n=1: & c_3=\displaystyle\frac{-2}{2\cdot3}c_1=-\frac{1}{3}c_1\\[5mm]
n=2: & c_4=0 &{}\hspace{10mm}n=3: & c_5=\displaystyle\frac{2}{4\cdot5}c_3=\frac{1}{10}c_3=-\frac{1}{30}c_1\\[5mm]
n=4: & c_6=0 &{}\hspace{10mm}n=5: & c_7=\displaystyle\frac{6}{6\cdot7}c_5=\frac{1}{7}c_5=-\frac{1}{210}c_1
\end{array}
$$

and so on. This implies that $c_{2n}=0$ for $n=2,3,4,\ldots$ and therefore we have:

$$
\begin{align*}
y&=\sum_{n=0}^{\infty}c_nx^n=\sum_{n=0}^{\infty}c_{2n}x^{2n}+\sum_{n=0}^{\infty}c_{2n+1}x^{2n+1}\\
&=c_0\left(1-2x^2\right)+c_1\left(x-\frac{1}{3}x^3-\frac{1}{30}x^5-\frac{1}{210}x^7-\cdots\right),\quad c_0,c_1\in\mathbb{R}.
\end{align*}
$$

Note that $p(x)=1-2x^2$ is a polynomial solution. This is easily checked, since: $p'(x)=-4x$ and $p''(x)=-4$. This implies that

$$
p''(x)-2xp'(x)+4p(x)=-4+8x^2+4(1-2x^2)=0.
$$

It is not impossible to find an explicit formula for the coefficients of the second solution:

$$
\begin{align*}
c_{2n+1}&=\frac{2(2n-3)}{2n(2n+1)}c_{2n-1}\\
&=\frac{2n-3}{n(2n+1)}\cdot\frac{2n-5}{(n-1)(2n-1)}\cdots\frac{1}{2\cdot5}\cdot\frac{-1}{1\cdot3}c_1\\
&=\frac{(-1)\cdot1}{n!(2n-1)(2n+1)}c_1=-\frac{1}{(4n^2-1)n!}c_1,\quad n=1,2,3,\ldots.
\end{align*}
$$

This implies that the second solution is $y=x-\displaystyle\sum_{n=1}^{\infty}\frac{x^{2n+1}}{(4n^2-1)n!}$.
::::::

::::{exercise}
:label: Exc:ODE2:HermiteExercise1
Use power series to find a polynomial solution of $y''-2xy'+6y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:HermiteExercise1`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-2x\sum_{n=1}^{\infty}nc_nx^{n-1}+6\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n-2\sum_{n=0}^{\infty}nc_nx^n+6\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+2)(n+1)c_{n+2}-(2n-6)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=\frac{2(n-3)}{(n+1)(n+2)}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$
 
Note that $c_3=-\frac{2}{3}c_1$ and $c_5=0$, which implies that $c_{2n+1}=0$ for $n=2,3,4,\ldots$ and therefore we have:

$$
\sum_{n=0}^{\infty}c_{2n+1}x^{2n+1}=c_1\left(x-\tfrac{2}{3}x^3\right),\quad c_1\in\mathbb{R}.
$$

Hence, $p(x)=x-\frac{2}{3}x^3$ is a polynomial solution. To check this, note that $p'(x)=1-2x^2$ and $p''(x)=-4x$. This implies that

$$
p''(x)-2xp'(x)+6p(x)=-4x-2x+4x^3+6(x-\tfrac{2}{3}x^3)=0.
$$

:::

::::{exercise}
:label: Exc:ODE2:HermiteExercise2
Use power series to find a polynomial solution of $y''-2xy'+8y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:HermiteExercise2`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-2x\sum_{n=1}^{\infty}nc_nx^{n-1}+8\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n-2\sum_{n=0}^{\infty}nc_nx^n+8\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+2)(n+1)c_{n+2}-(2n-8)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=\frac{2(n-4)}{(n+1)(n+2)}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$
 
Note that $c_2=-4c_0$, $c_4=-\frac{1}{3}c_2=\frac{4}{3}c_0$ and $c_6=0$, which implies that $c_{2n}=0$ for $n=3,4,5,\ldots$ and therefore we have:

$$
\sum_{n=0}^{\infty}c_{2n}x^{2n}=c_0\left(1-4x^2+\tfrac{4}{3}x^4\right),\quad c_0\in\mathbb{R}.
$$

Hence, $p(x)=1-4x^2+\frac{4}{3}x^4$ is a polynomial solution. To check this. note that $p'(x)=-8x+\frac{16}{3}x^3$ and $p''(x)=-8+16x^2$. This implies that

$$
\begin{align*}
&p''(x)-2xp'(x)+8p(x)\\
&{}=-8+16x^2-2x(-8x+\tfrac{16}{3}x^3)+8(1-4x^2+\tfrac{4}{3}x^4)=0.
\end{align*}
$$

:::

::::::{prf:example}
Use power series to solve $(1-x^2)y''-4xy'-2y=0$.

Solution. Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&(1-x^2)\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-4x\sum_{n=1}^{\infty}nc_nx^{n-1}-2\sum_{n=0}^{\infty}c_nx^n=0\\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n-\sum_{n=0}^{\infty}\left[n(n-1)+4n+2\right]x^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+2)(n+1)c_{n+2}-(n^2+3n+2)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=\frac{(n+1)(n+2)}{(n+1)(n+2)}c_n=c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$

Hence we have: $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n=c_0\sum_{n=0}^{\infty}x^{2n}+c_1\sum_{n=0}^{\infty}x^{2n+1}$.

For $|x|<1$ we have: $\displaystyle\sum_{n=0}^{\infty}x^{2n}=\frac{1}{1-x^2}$ and $\displaystyle\sum_{n=0}^{\infty}x^{2n+1}=\frac{x}{1-x^2}$.

Direct substitution shows that these solutions $p(x)=\displaystyle\frac{1}{1-x^2}$ and $q(x)=\displaystyle\frac{x}{1-x^2}$ are also valid for $|x|>1$. 

Note that $p'(x)=\displaystyle\frac{2x}{(1-x^2)^2}$ and $p''(x)=\displaystyle\frac{2+6x^2}{(1-x^2)^3}$, which implies that

$$
(1-x^2)p''(x)-4xp'(x)-2p(x)=\frac{2+6x^2}{(1-x^2)^2}-\frac{8x^2}{(1-x^2)^2}-\frac{2}{1-x^2}=0.
$$

Similarly, we have $q'(x)=\displaystyle\frac{1+x^2}{(1-x^2)^2}$ and $q''(x)=\displaystyle\frac{6x+2x^3}{(1-x^2)^3}$ and therefore

$$
(1-x^2)q''(x)-4xq'(x)-2q(x)=\frac{6x+2x^3}{(1-x^2)^2}-\frac{4x+4x^3}{(1-x^2)^2}-\frac{2x}{1-x^2}=0.
$$

::::::

::::{exercise}
:label: Exc:ODE2:SpecialExercise
Use power series to solve $(1-x^2)y''-6xy'-6y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:SpecialExercise`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&(1-x^2)\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-6x\sum_{n=1}^{\infty}nc_nx^{n-1}-6\sum_{n=0}^{\infty}c_nx^n=0\\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n-\sum_{n=0}^{\infty}\left[n(n-1)+6n+6\right]x^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+2)(n+1)c_{n+2}-(n^2+5n+6)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=\frac{(n+2)(n+3)}{(n+1)(n+2)}c_n=\frac{n+3}{n+1}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$

Now we have

$$
c_{2n}=\frac{2n+1}{2n-1}c_{2n-2}=\frac{2n+1}{2n-1}\cdot\frac{2n-1}{2n-3}\cdot\frac{2n-3}{2n-5}\cdots\frac{3}{1}c_0=(2n+1)c_0.
$$

Hence we have a solution $\displaystyle\sum_{n=0}^{\infty}(2n+1)x^{2n}$ of the differential equation. Note that

$$
\begin{align*}
&\sum_{n=0}^{\infty}x^{2n+1}=\frac{x}{1-x^2},\quad|x|<1\\
&{}\quad\Longrightarrow\quad\sum_{n=0}^{\infty}(2n+1)x^{2n}=\frac{d}{dx}\left(\frac{x}{1-x^2}\right),\quad|x|<1.
\end{align*}
$$

Now we have

$$
p(x)=\sum_{n=0}^{\infty}(2n+1)x^{2n}=\frac{d}{dx}\left(\frac{x}{1-x^2}\right)=\frac{1-x^2+2x^2}{(1-x^2)^2}=\frac{1+x^2}{(1-x^2)^2}
$$

is a solution of the differential equation.

Similarly we have

$$
c_{2n+1}=\frac{2n+2}{2n}c_{2n-1}=\frac{2n+2}{2n}\cdot\frac{2n}{2n-2}\cdot\frac{2n-2}{2n-4}\cdots\frac{4}{2}c_1=(n+1)c_1.
$$

Hence we have a solution $\displaystyle\sum_{n=0}^{\infty}(n+1)x^{2n+1}$ of the differential equation. Note that

$$
\begin{align*}
&\sum_{n=0}^{\infty}x^{2n+2}=\frac{x^2}{1-x^2},\quad|x|<1\\
&{}\quad\Longrightarrow\quad\sum_{n=0}^{\infty}(2n+2)x^{2n+1}=\frac{d}{dx}\left(\frac{x^2}{1-x^2}\right),\quad|x|<1.
\end{align*}
$$

Now we have

$$
\begin{align*}
q(x)&=\frac{1}{2}\sum_{n=0}^{\infty}(2n+2)x^{2n+1}=\frac{1}{2}\frac{d}{dx}\left(\frac{x^2}{1-x^2}\right)=\frac{1}{2}\frac{2x(1-x^2)+2x^3}{(1-x^2)^2}\\
&=\frac{x}{(1-x^2)^2}
\end{align*}
$$

is a solution of the differential equation.

Again, direct substitution shows that these solutions $p(x)=\displaystyle\frac{1+x^2}{(1-x^2)^2}$ and $q(x)=\displaystyle\frac{x}{(1-x^2)^2}$are also valid for $|x|>1$.

Note that we have $p'(x)=\displaystyle\frac{6x+2x^3}{(1-x^2)^3}$ and $p''(x)=\displaystyle\frac{6+36x^2+6x^4}{(1-x^2)^4}$, which implies that

$$
\begin{align*}
&(1-x^2)p''(x)-6xp'(x)-6p(x)\\
&{}=\frac{6+36x^2+6x^4}{(1-x^2)^3}-\frac{36x^2+12x^4}{(1-x^2)^3}-\frac{6+6x^2}{(1-x^2)^2}=0.
\end{align*}
$$

Similarly, we have $q'(x)=\displaystyle\frac{1+3x^2}{(1-x^2)^3}$ and $q''(x)=\displaystyle\frac{12x+12x^3}{(1-x^2)^4}$, which implies that

$$
\begin{align*}
&(1-x^2)q''(x)-6xq'(x)-6q(x)\\
&{}=\frac{12x+12x^3}{(1-x^2)^3}-\frac{6x+18x^3}{(1-x^2)^3}-\frac{6x}{(1-x^2)^2}=0.
\end{align*}
$$

:::

## (Grasple) exercises

::::{exercise}
:label: Exc:ODE2:LegendreExercise1
Use power series to find a polynomial solution of $(1-x^2)y''-2xy'+6y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:LegendreExercise1`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&(1-x^2)\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-2x\sum_{n=1}^{\infty}nc_nx^{n-1}+6\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n-\sum_{n=0}^{\infty}n(n-1)c_nx^n\\
&{}\hspace{25mm}{}-2\sum_{n=0}^{\infty}nc_nx^n+6\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+2)(n+1)c_{n+2}-(n^2+n-6)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=\frac{(n+3)(n-2)}{(n+1)(n+2)}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$
 
Note that $c_2=-3c_0$ and $c_4=0$, which implies that $c_{2n}=0$ for $n=2,3,4,\ldots$ and therefore we have:

$$
\sum_{n=0}^{\infty}c_{2n}x^{2n}=c_0\left(1-3x^2\right),\quad c_0\in\mathbb{R}.
$$

Hence, $p(x)=1-3x^2$ is a polynomial solution. To check this, note that $p'(x)=-6x$ and $p''(x)=-6$. This implies that

$$
(1-x^2)p''(x)-2xp'(x)+6p(x)=-6(1-x^2)+12x^2+6(1-3x^2)=0.
$$

:::

::::{exercise}
:label: Exc:ODE2:LegendreExercise2
Use power series to find a polynomial solution of $(1-x^2)y''-2xy'+12y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:LegendreExercise2`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&(1-x^2)\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-2x\sum_{n=1}^{\infty}nc_nx^{n-1}+12\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n-\sum_{n=0}^{\infty}n(n-1)c_nx^n\\
&{}\hspace{25mm}{}-2\sum_{n=0}^{\infty}nc_nx^n+12\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+2)(n+1)c_{n+2}-(n^2+n-12)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=\frac{(n+4)(n-3)}{(n+1)(n+2)}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$
 
Note that $c_3=-\frac{5}{3}c_1$ and $c_5=0$, which implies that $c_{2n+1}=0$ for $n=2,3,4,\ldots$ and therefore we have:

$$
\sum_{n=0}^{\infty}c_{2n+1}x^{2n+1}=c_1\left(x-\tfrac{5}{3}x^3\right),\quad c_1\in\mathbb{R}.
$$

Hence, $p(x)=x-\frac{5}{3}x^3$ is a polynomial solution. To check this, note that $p'(x)=1-5x^2$ and $p''(x)=-10x$. This implies that

$$
\begin{align*}
&(1-x^2)p''(x)-2xp'(x)+12p(x)\\
&{}=-10x(1-x^2)-2x(1-5x^2)+12(x-\tfrac{5}{3}x^3)=0.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:ODE2:ChebyshevExercise1
Use power series to find a polynomial solution of $(1-x^2)y''-xy'+4y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:ChebyshevExercise1`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&(1-x^2)\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-x\sum_{n=1}^{\infty}nc_nx^{n-1}+4\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n-\sum_{n=0}^{\infty}n(n-1)c_nx^n\\
&{}\hspace{25mm}{}-\sum_{n=0}^{\infty}nc_nx^n+4\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+2)(n+1)c_{n+2}-(n^2-4)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=\frac{(n+2)(n-2)}{(n+1)(n+2)}c_n=\frac{n-2}{n+1}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$
 
Note that $c_2=-2c_0$ and $c_4=0$, which implies that $c_{2n}=0$ for $n=2,3,4,\ldots$ and therefore we have:

$$
\sum_{n=0}^{\infty}c_{2n}x^{2n}=c_0\left(1-2x^2\right),\quad c_0\in\mathbb{R}.
$$

Hence, $p(x)=1-2x^2$ is a polynomial solution. To check this, note that $p'(x)=-4x$ and $p''(x)=-4$. This implies that

$$
(1-x^2)p''(x)-xp'(x)+4p(x)=-4(1-x^2)+4x^2+4(1-2x^2)=0.
$$

:::

::::{exercise}
:label: Exc:ODE2:ChebyshevExercise2
Use power series to find a polynomial solution of $(1-x^2)y''-xy'+9y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:ChebyshevExercise2`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&(1-x^2)\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-x\sum_{n=1}^{\infty}nc_nx^{n-1}+9\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n-\sum_{n=0}^{\infty}n(n-1)c_nx^n\\
&{}\hspace{25mm}{}-\sum_{n=0}^{\infty}nc_nx^n+9\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+2)(n+1)c_{n+2}-(n^2-9)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=\frac{(n+3)(n-3)}{(n+1)(n+2)}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$
 
Note that $c_3=-\frac{4}{3}c_1$ and $c_5=0$, which implies that $c_{2n+1}=0$ for $n=2,3,4,\ldots$ and therefore we have:

$$
\sum_{n=0}^{\infty}c_{2n+1}x^{2n+1}=c_1\left(x-\tfrac{4}{3}x^3\right),\quad c_1\in\mathbb{R}.
$$

Hence, $p(x)=x-\frac{4}{3}x^3$ is a polynomial solution. To check this, note that $p'(x)=1-4x^2$ and $p''(x)=-8x$. This implies that

$$
\begin{align*}
&(1-x^2)p''(x)-xp'(x)+9p(x)\\
&{}=-8x(1-x^2)-x(1-4x^2)+9(x-\tfrac{4}{3}x^3)=0.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:ODE2:ChebyshevExercise3
Use power series to find a polynomial solution of $(1-x^2)y''-3xy'+8y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:ChebyshevExercise3`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&(1-x^2)\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-3x\sum_{n=1}^{\infty}nc_nx^{n-1}+8\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n-\sum_{n=0}^{\infty}n(n-1)c_nx^n\\
&{}\hspace{25mm}{}-3\sum_{n=0}^{\infty}nc_nx^n+8\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+2)(n+1)c_{n+2}-(n^2+2n-8)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=\frac{(n+4)(n-2)}{(n+1)(n+2)}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$
 
Note that $c_2=-4c_0$ and $c_4=0$, which implies that $c_{2n}=0$ for $n=2,3,4,\ldots$ and therefore we have:

$$
\sum_{n=0}^{\infty}c_{2n}x^{2n}=c_0\left(1-4x^2\right),\quad c_0\in\mathbb{R}.
$$

Hence, $p(x)=1-4x^2$ is a polynomial solution. To check this, note that $p'(x)=-8x$ and $p''(x)=-8$. This implies that

$$
(1-x^2)p''(x)-3xp'(x)8p(x)=-8(1-x^2)+24x^2+8(1-4x^2)=0.
$$

:::

::::{exercise}
:label: Exc:ODE2:ChebyshevExercise4
Use power series to find a polynomial solution of $(1-x^2)y''-3xy'+15y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:ChebyshevExercise4`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&(1-x^2)\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-3x\sum_{n=1}^{\infty}nc_nx^{n-1}+15\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n-\sum_{n=0}^{\infty}n(n-1)c_nx^n\\
&{}\hspace{25mm}{}-3\sum_{n=0}^{\infty}nc_nx^n+15\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+2)(n+1)c_{n+2}-(n^2+2n-15)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=\frac{(n+5)(n-3)}{(n+1)(n+2)}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$
 
Note that $c_3=-2c_1$ and $c_5=0$, which implies that $c_{2n+1}=0$ for $n=2,3,4,\ldots$ and therefore we have:

$$
\sum_{n=0}^{\infty}c_{2n+1}x^{2n+1}=c_1\left(x-2x^3\right),\quad c_1\in\mathbb{R}.
$$

Hence, $p(x)=x-2x^3$ is a polynomial solution. To check this, note that $p'(x)=1-6x^2$ and $p''(x)=-12x$. This implies that

$$
\begin{align*}
&(1-x^2)p''(x)-3xp'(x)+15p(x)\\
&{}=-12x(1-x^2)-3x(1-6x^2)+15(x-2x^3)=0.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:ODE2:LaguerreExercise1
Use power series to find a polynomial solution of $xy''+(1-x)y'+2y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:LaguerreExercise1`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&x\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}+(1-x)\sum_{n=1}^{\infty}nc_nx^{n-1}+2\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+1)nc_{n+1}x^n+\sum_{n=0}^{\infty}(n+1)c_{n+1}x^n\\
&{}\hspace{25mm}{}-\sum_{n=0}^{\infty}nc_nx^n+2\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+1)(n+1)c_{n+1}-(n-2)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+1}=\frac{n-2}{(n+1)^2}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$
 
Note that $c_1=-2c_0$, $c_2=-\frac{1}{4}c_1=\frac{1}{2}c_0$ and $c_3=0$, which implies that $c_n=0$ for $n=3,4,5,\ldots$ and therefore we have:

$$
\sum_{n=0}^{\infty}c_nx^n=c_0\left(1-2x+\tfrac{1}{2}x^2\right),\quad c_0\in\mathbb{R}.
$$

Hence, $p(x)=1-2x+\frac{1}{2}x^2$ is a polynomial solution. To check this, note that $p'(x)=-2+x$ and $p''(x)=1$. This implies that

$$
\begin{align*}
&xp''(x)+(1-x)p'(x)+2p(x)\\
&{}=x+(1-x)(-2+x)+2(1-2x+\tfrac{1}{2}x^2)=0.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:ODE2:LaguerreExercise2
Use power series to find a polynomial solution of $xy''+(1-x)y'+3y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:LaguerreExercise2`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&x\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}+(1-x)\sum_{n=1}^{\infty}nc_nx^{n-1}+3\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+1)nc_{n+1}x^n+\sum_{n=0}^{\infty}(n+1)c_{n+1}x^n\\
&{}\hspace{25mm}{}-\sum_{n=0}^{\infty}nc_nx^n+3\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recursion relation

$$
\begin{align*}
&(n+1)(n+1)c_{n+1}-(n-3)c_n=0,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+1}=\frac{n-3}{(n+1)^2}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$
 
Note that $c_1=-3c_0$, $c_2=-\frac{1}{2}c_1=\frac{3}{2}c_0$, $c_3=-\frac{1}{9}c_2=-\frac{1}{6}c_0$ and $c_4=0$, which implies that $c_n=0$ for $n=4,5,6,\ldots$ and therefore we have:

$$
\sum_{n=0}^{\infty}c_nx^n=c_0\left(1-3x+\tfrac{3}{2}x^2-\tfrac{1}{6}x^3\right),\quad c_0\in\mathbb{R}.
$$

Hence, $p(x)=1-3x+\frac{3}{2}x^2-\frac{1}{6}x^3$ is a polynomial solution. To check this, note that $p'(x)=-3+3x-\frac{1}{2}x^2$ and $p''(x)=3-x$. This implies that

$$
\begin{align*}
&xp''(x)+(1-x)p'(x)+3p(x)\\
&{}=x(3-x)+(1-x)(-3+3x-\tfrac{1}{2}x^2)+3(1-3x+\tfrac{3}{2}x^2-\tfrac{1}{6}x^3)=0.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:ODE2:PolynomialExercise1
Use power series to find the general solution of $(1+x^2)y''-2xy'+2y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:PolynomialExercise1`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&(1+x^2)\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-2x\sum_{n=1}^{\infty}nc_nx^{n-1}+2\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n\\
&{}\hspace{25mm}{}+\sum_{n=0}^{\infty}n(n-1)c_nx^n-2\sum_{n=0}^{\infty}nc_nx^n+2\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recurrence relation

$$
\begin{align*}
&(n+1)(n+2)c_{n+2}+\left\{n(n-1)-2n+2\right\}c_n,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=-\frac{(n-1)(n-2)}{(n+1)(n+2)}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$

Note that $c_2=-c_0$, $c_3=0$, $c_4=0$, which implies that $c_n=0$ for $n=3,4,5,\ldots$. Hence we have

$$
y(x)=c_0(1-x^2)+c_1x,\quad c_0,c_1\in\mathbb{R}.
$$

:::

::::{exercise}
:label: Exc:ODE2:PolynomialExercise2
Use power series to find the general solution of $(1+x^2)y''-4xy'+6y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:PolynomialExercise2`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&(1+x^2)\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-4x\sum_{n=1}^{\infty}nc_nx^{n-1}+6\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n\\
&{}\hspace{25mm}{}+\sum_{n=0}^{\infty}n(n-1)c_nx^n-4\sum_{n=0}^{\infty}nc_nx^n+6\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recurrence relation

$$
\begin{align*}
&(n+1)(n+2)c_{n+2}+\left\{n(n-1)-4n+6\right\}c_n,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=-\frac{(n-2)(n-3)}{(n+1)(n+2)}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$

Note that $c_2=-3c_0$, $c_3=-\frac{1}{3}c_1$, $c_4=0$, $c_5=0$, which implies that $c_n=0$ for $n=4,5,6,\ldots$. Hence we have

$$
y(x)=c_0(1-3x^2)+c_1(x-\tfrac{1}{3}x^3),\quad c_0,c_1\in\mathbb{R}.
$$

:::

::::{exercise}
:label: Exc:ODE2:PolynomialExercise3
Use power series to find the general solution of $(1+x^2)y''-6xy'+12y=0$.
::::

:::{admonition} Solution of {numref}`Exc:ODE2:PolynomialExercise3`
:class: solution, dropdown
Substitution of $y=\displaystyle\sum_{n=0}^{\infty}c_nx^n$, $y'=\displaystyle\sum_{n=1}^{\infty}nc_nx^{n-1}$ and $y''=\displaystyle\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}$ leads to

$$
\begin{align*}
&(1+x^2)\sum_{n=2}^{\infty}n(n-1)c_nx^{n-2}-6x\sum_{n=1}^{\infty}nc_nx^{n-1}+12\sum_{n=0}^{\infty}c_nx^n=0\\
&{}\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n\\
&{}\hspace{25mm}{}+\sum_{n=0}^{\infty}n(n-1)c_nx^n-6\sum_{n=0}^{\infty}nc_nx^n+12\sum_{n=0}^{\infty}c_nx^n=0.
\end{align*}
$$

This leads to the recurrence relation

$$
\begin{align*}
&(n+1)(n+2)c_{n+2}+\left\{n(n-1)-6n+12\right\}c_n,\quad n=0,1,2,\ldots\\
&{}\quad\Longrightarrow\quad c_{n+2}=-\frac{(n-3)(n-4)}{(n+1)(n+2)}c_n,\quad n=0,1,2,\ldots.
\end{align*}
$$

Note that $c_2=-6c_0$, $c_3=-c_1$, $c_4=-\frac{1}{6}c_2=c_0$, $c_5=0$, $c_6=0$, which implies that $c_n=0$ for $n=5,6,7,\ldots$. Hence we have

$$
y(x)=c_0(1-6x^2+x^4)+c_1(x-x^3),\quad c_0,c_1\in\mathbb{R}.
$$

:::
