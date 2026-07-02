(Sec:Series:TaylorSeries)=

# Taylor series

## Introduction

In the previous section we have seen some power series representations of certain functions. These were all based on the geometric series $\displaystyle\sum_{n=0}^{\infty}x^n=\frac{1}{1-x}$ for $|x|<1$. We could use substitutions, differentiation and integration to find power series representations of other functions by using this power series representation of the function $\dfrac{1}{1-x}$.

In this section we will find power series representations of more functions, which are infinitely differentiable.

## Derivation

Let $f$ be such an infinitely differentiable function and suppose that $f$ can be represented by a power series for $|x-a|<R$ for some $R>0$, that is, suppose that: 

\begin{align*}
f(x)&=c_0+c_1(x-a)+c_2(x-a)^2+c_3(x-a)^3+c_4(x-a)^4+\ldots\\
&=\sum_{n=0}^{\infty}c_n(x-a)^n,\quad|x-a| < R.
\end{align*}

Again, $R$ is the radius of convergence of this power series. Since $f$ is infinitely differentiable, we can differentiate the power series term by term to obtain that for $|x-a|<R$ we have

\begin{align*}
f'(x) &=c_1+2c_2(x-a)+3c_3(x-a)^2+4c_4(x-a)^3+5c_5(x-a)^4+\ldots\\
 &=\sum_{n=1}^{\infty}n(x-a)^{n-1}, \\
f''(x)&=2c_2+2\cdot3c_3(x-a)+3\cdot4c_4(x-a)^2+4\cdot5c_5(x-a)^3+\ldots\\
&=\sum_{n=2}^{\infty}n(n-1)(x-a)^{n-2}, \\
f^{(3)}(x)&=2\cdot3c_3+2\cdot3\cdot4c_4(x-a)+3\cdot4\cdot5c_5(x-a)^2+4\cdot5\cdot6c_6(x-a)^3+\ldots\\
&=\sum_{n=3}^{\infty}n(n-1)(n-2)(x-a)^{n-3},
\end{align*}

and so on. Since all these power series converge at least at $x=a$ we substitute $x=a$ to obtain that

\begin{align*}
&~ f(a)=c_0,\quad f'(a)=c_1,\quad f''(a)=2c_2,\quad f^{(3)}(a)=2\cdot3c_3,\quad\ldots\\
&\Longrightarrow f^{(n)}(a)=1\cdot2\cdot3\cdot4\cdots nc_n=n!c_n,\quad 
n=1,2,3,\ldots 
\end{align*}

This leads to the following theorem. 

::::::{prf:theorem} Taylor series 
:label: Thm:Series:TaylorSeries 
If $f$ has a power series representation (expansion) around $x=a$, 
that is, if for some $R>0$ 

$$ 
f(x)=\sum_{n=0}^{\infty}c_n(x-a)^n,\quad|x-a| < R, 
$$ 

then the coefficients are given by the formula 

$$ 
c_n=\frac{f^{(n)}(a)}{n!},\quad n=0,1,2,\ldots 
$$ 

:::::: 

::::::{prf:definition} Taylor series 
:label: Def:Series:TaylorSeries 
The series 

\begin{align*}
&\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n\\
&\quad{}=f(a)+\frac{f'(a)}{1!}(x-a)+\frac{f''(a)}{2!}(x-a)^2+\frac{f^{(3)}(a)}{3!}(x-a)^3+\ldots
\end{align*}

is called the **Taylor series** or the **Taylor expansion** of the function $f$ at $x=a$. 

The special case with $a=0$ 

$$ 
\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n=f(0)+\frac{f'(0)}{1!}x+\frac{f''(0)}{2!}x^2+\frac{f^{(3)}(0)}{3!}x^3+\ldots
$$ 

is sometimes (also) called the **Maclaurin series** of $f$. 
::::::

This Taylor series is named after the English mathematician [Brook Taylor (1685-1731)](https://en.wikipedia.org/wiki/Brook_Taylor) and the Maclaurin series is named after the Scottish mathematician [Colin Maclaurin (1698-1746)](https://en.wikipedia.org/wiki/Colin_Maclaurin).

::::::{note} 
The $n$th partial sum 

$$ 
T_n(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k 
$$ 

is the $n$th-order *Taylor polynomial* of $f$ around $x=a$ and has been studied in {numref}`Sec:TaylorPolynomials`.
:::::: 

Sometimes it is useful for us to refer to functions that have a Taylor series with a positive radius of convergence. This leads to the following definition:

::::::{prf:definition} Analytic functions 
:label: Def:Series:Analytic 
A function is called **analytic** if it has a Taylor series with a positive radius of convergence.
::::::

One of the most simple Taylor series is the Taylor series of the exponential function $f(x)=e^x$ at $x=0$, which we consider in the next example.

::::::{prf:example}
:label: Ex:Series:ExpTaylor

For $f(x)=e^x$ we have

$$
f^{(n)}(x)=e^x\quad\text{for }n=0,1,2,\ldots
$$

Hence:

$$
f^{(n)}(0)=1\quad\text{for }n=0,1,2,\ldots
$$

This implies that the Taylor series of $f$ at $x=0$ is given by

$$
e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!}=1+x+\frac{1}{2}x^2+\frac{1}{6}x^3+\frac{1}{24}x^4+\frac{1}{120}x^5+\ldots
$$ 

In order to find the radius of convergence, we apply the ratio test: for $x\neq0$ let $a_n=\displaystyle\frac{x^n}{n!}$, then we have

$$ 
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim\limits_{n\to\infty}\left|\frac{x^{n+1}}{(n+1)!}\cdot\frac{n!}{x^n}\right|
=\lim\limits_{n\to\infty}\frac{|x|}{n+1}=0.
$$ 
 
This implies that the Taylor series converges for all $x\in\mathbb{R}$, so the radius of convergence is $R=\infty$.

{numref}`Fig:Series:ExpTaylor` showcases the function $f(x)=e^x$ and some of its Taylor polynomials, which are the partial sums of the Taylor series. We can see that these Taylor polynomials are good approximations of the function $f$ around $x=0$ and that they get better and better as we take more and more terms in the Taylor series.

::::{figure} Images/taylor.png
:name: Fig:Series:ExpTaylor
:align: center

The function $f(x)=e^x$ and its Taylor polynomial $T_n$ for variable $n$.
::::

:::{todo}
Replace {numref}`Fig:Series:ExpTaylor` with an applet with $n$ a slider.
:::

::::::

:::{prf:remark}
:label: Rem:Series:ExpMinus1
In {prf:ref}`Ex:Series:ApproximationSum` we obtained an approximation of

$$
\sum_{n=2}^{\infty}\frac{(-1)^n}{n!}=e^{-1}\approx0.36788.
$$

Now we are able to prove this result:

$$
\sum_{n=2}^{\infty}\frac{(-1)^n}{n!}=\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}=e^{-1}.
$$

:::

::::::{prf:example}
:label: Ex:Series:SinTaylor

For $f(x)=\sin(x)$ we have: $f'(x)=\cos(x)$, $f''(x)=-\sin(x)$, $f^{(3)}(x)=-\cos(x)$, $f^{(4)}(x)=\sin(x)=f(x)$ and so on. Hence: $f(0)=0$, $f'(0)=1$, $f''(0)=0$, $f^{(3)}(0)=-1$, $f^{(4)}(0)=1=f(0)$ and so on. This implies that

$$
\sin(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{2n+1}=x-\frac{1}{6}x^3+\frac{1}{120}x^5-\frac{1}{5040}x^7+\ldots
$$

In order to find the radius of convergence, we apply the ratio test: for $x\neq0$ let $a_n=\displaystyle\frac{(-1)^n}{(2n+1)!}x^{2n+1}$, then we have

\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|\frac{(-1)^{n+1}x^{2n+3}}{(2n+3)!}\cdot\frac{(2n+1)!}{(-1)^nx^{2n+1}}\right|\\
&=\lim\limits_{n\to\infty}\frac{x^2}{(2n+2)(2n+3)}=0.
\end{align*}
This implies that the Taylor series for $\sin(x)$ converges for all $x\in\mathbb{R}$, so the radius of convergence is $R=\infty$.

In {numref}`Fig:Series:SinCosTaylor` you can investigate this convergence yourself by increasing the number of terms in the Taylor polynomial that approximate the function.

::::::

:::{figure} Images/Fig-Series-SinCosTaylor.png
:name: Fig:Series:SinCosTaylor

The functions $f(x)=\sin(x)$ and its Taylor polynomial $T_n$ for variable $n$. You can investigate the convergence of the Taylor series for $\sin(x)$ by increasing the number of terms in the Taylor polynomial $T_n$. You can also switch to the function $g(x)=\cos(x)$ and its Taylor polynomials to investigate the convergence of the Taylor series for $\cos(x)$.

:::

:::{todo}
Replace {numref}`Fig:Series:SinCosTaylor` with an applet with $n$ a slider. Make $\sin$ and $\cos$ available in a dropdown.
:::

::::::

::::::{prf:example}
:label: Ex:Series:CosTaylor
Similarly we obtain that

$$
\cos(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n)!}x^{2n}=1-\frac{1}{2}x^2+\frac{1}{24}x^4-\frac{1}{720}x^6+\ldots
$$

In order to find the radius of convergence, we apply the ratio test: for $x\neq0$ let $a_n=\displaystyle\frac{(-1)^n}{(2n)!}x^{2n}$, then we have

\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|\frac{(-1)^{n+1}x^{2n+2}}{(2n+2)!}\cdot\frac{(2n)!}{(-1)^nx^{2n}}\right|\\
&=\lim\limits_{n\to\infty}\frac{x^2}{(2n+1)(2n+2)}=0.
\end{align*}
This implies that the Taylor series for $\cos(x)$ converges for all $x\in\mathbb{R}$, so the radius of convergence is $R=\infty$.

In {numref}`Fig:Series:SinCosTaylor` you can investigate this convergence yourself by increasing the number of terms in the Taylor polynomial that approximate the function.

::::::

As you can see in {numref}`Fig:Series:ExpTaylor` and {numref}`Fig:Series:SinCosTaylor`, the Taylor polynomials of $\sin(x)$ and $\cos(x)$ are good approximations of these functions around $x=0$ and they get better and better as we take more and more terms in the Taylor series. This indicates that the part that is cut off from the Taylor series, gets smaller and smaller as we take more and more terms in the Taylor series. In the next section we will make this precise.

## The remainder

In general, $f(x)$ is the sum of its Taylor series if

$$
f(x)=\lim_{n\to\infty}T_n(x),
$$

for $x$ within the interval of convergence of the Taylor series.


If we let $R_n(x)=f(x)-T_n(x)$ or $f(x)=T_n(x)+R_n(x)$, then $R_n(x)$ is called the **remainder** of the Taylor series, see {prf:ref}`Def:TaylorPolynomials:TaylorIneq`. So, if $\lim\limits_{n\to\infty}R_n(x)=0$, then

$$
\lim_{n\to\infty}T_n(x)=\lim_{n\to\infty}\left(f(x)-R_n(x)\right)=f(x)-\lim_{n\to\infty}R_n(x)=f(x)-0=f(x).
$$

This proves the following theorem:

::::::{prf:theorem}
:label: Thm:Series:TaylorSum
If $f(x)=T_n(x)+R_n(x)$, where $T_n(x)$ is the $n$th-order Taylor polynomial of $f$ at $x=a$ and

$$
\lim_{n\to\infty}R_n(x)=0
$$

for $|x-a|<R$, then $f$ is equal to the sum of its Taylor series for $|x-a|<R$.
::::::

If we want to show that $\lim\limits_{n\to\infty}R_n(x)=0$ for a specific function $f$, we first need a formula for the remainder term $R_n(x)$, which is provided in the next theorem.

:::{prf:theorem}
:label: Thm:Series:TaylorRemainder
If $f^{(n+1)}$ is continuous on an interval $I$ and $x\in I$, then 

$$
R_n(x)=\frac{1}{n!}\int_a^x(x-t)^nf^{(n+1)}(t)\,dt.
$$

This is called the **integral form of the remainder term**. Furthermore, there exists a number $c$ between $a$ and $x$ such that

$$
R_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}.
$$

This is called **Lagrange's form of the remainder term**.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:TaylorRemainder`
:class: tudproof, dropdown

First consider $n=0$:

\begin{align*}
R_0(x) &= f(x) - T_0(x) \\
&= f(x) - f(a) \\
&= \int_a^x f'(t)\,dt \\
&= \frac{1}{0!}\int_a^x(x-t)^0f'(t)\,dt.
\end{align*}

Now assume that the formula holds for a certain value of $n$. Then we have

\begin{align*}
R_{n+1}(x) &= f(x) - T_{n+1}(x) \\
&= f(x) - T_n(x) - \frac{f^{(n+1)}(a)}{(n+1)!}(x-a)^{n+1} \\
&= R_n(x) - \frac{f^{(n+1)}(a)}{(n+1)!}(x-a)^{n+1} \\
&= \frac{1}{n!}\int_a^x(x-t)nf^{(n+1)}(t)\,dt - \frac{f^{(n+1)}(a)}{(n+1)!}(x-a)^{n+1}.
\end{align*}

In the last step we used the induction hypothesis. Now we apply integration by parts to the integral term, using $u=f^{(n+1)}(t)$ and $dv=(x-t)^n\,dt$, which implies that $du=f^{(n+2)}(t)\,dt$ and $v=-\frac{1}{n+1}(x-t)^{n+1}$, to obtain that

\begin{align*}
R_{n+1}(x) &= \frac{1}{n!}\left(\left[-\frac{1}{n+1}(x-t)^{n+1}f^{(n+1)}(t)\right]_{t=a}^{x} + \int_a^x \frac{1}{n+1}(x-t)^{n+1}f^{(n+2)}(t)\,dt \right) \\
&~ \quad\quad- \frac{f^{(n+1)}(a)}{(n+1)!}(x-a)^{n+1} \\
&= \frac{f^{(n+1)}(a)}{(n+1)!}(x-a)^{n+1} + \frac{1}{(n+1)!}\int_a^x(x-t)^{n+1}f^{(n+2)}(t)\,dt \\
&~ \quad\quad- \frac{f^{(n+1)}(a)}{(n+1)!}(x-a)^{n+1} \\
&= \frac{1}{(n+1)!}\int_a^x(x-t)^{n+1}f^{(n+2)}(t)\,dt.
\end{align*}

This proves the first part of the theorem.

For the next part, we use the {prf:ref}`mean value theorem for integrals <Thm:Integration:FundamentalTheorem>`, to obtain that there exists a number $c$ between $a$ and $x$ such that

\begin{align*}
R_n(x) &= \frac{1}{n!}\int_a^x(x-t)^nf^{(n+1)}(t)\,dt \\
&= \frac{f^{(n+1)}(c)}{n!}\int_a^x(x-t)^n\,dt \\
&= \frac{f^{(n+1)}(c)}{n!}\cdot\frac{1}{n+1}(x-a)^{n+1} \\
&= \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}.
\end{align*}

This concludes the proof of the theorem.
:::

The last form in the above theorem is named after the Italian-French mathematician [Joseph-Louis Lagrange (1736-1813)](https://en.wikipedia.org/wiki/Joseph-Louis_Lagrange).

Using this theorem, we can find an upper bound for the remainder term, leading to the following theorem[^other]:

[^other]: This theorem is a reformulation of {prf:ref}`Th:TaylorPolynomialsAdd:TaylorIneq`.

::::::{prf:theorem} Taylor's inequality
:label: Thm:Series:TaylorInequality
If $\left|f^{(n+1)}(x)\right|\leq M$ for $|x-a|<R$, then the remainder $R_n(x)$ of the Taylor series satisfies the inequality

$$
|R_n(x)|\leq\frac{M}{(n+1)!}|x-a|^{n+1}\quad\text{for}\quad|x-a|<R.
$$

Furthermore, $M$ can be taken as any upper bound for $|f^{(n+1)}(x)|$ on an interval $D$ that contains $a$ and $x$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:TaylorInequality`
:class: tudproof, dropdown

We have seen in {prf:ref}`Thm:Series:TaylorRemainder` that there exists a number $c$ between $a$ and $x$ such that

$$
R_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}.
$$

Assume $M$ is an upper bound for $|f^{(n+1)}(x)|$ on an interval $D$ that contains $a$ and $x$, then we have

\begin{align*}
|R_n(x)|&=\left|\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}\right|\\
&=\frac{|f^{(n+1)}(c)|}{(n+1)!}|x-a|^{n+1} \\
&\leq \frac{M}{(n+1)!}|x-a|^{n+1}.
\end{align*}

:::

:::{prf:example}
:label: Ex:Series:TaylorInequality

We want to find an approximation of $\cosh(1)$ exact to three decimal places using Taylor polynomials.

First, we set $f(x)=\cosh(x)$, then we have by {prf:ref}`Thm:Chain rule:Standard2` that

$$
f^{(n)}(x) = \begin{cases}
\sinh(x) & \text{if } n \text{ is odd}, \\
\cosh(x) & \text{if } n \text{ is even}.
\end{cases}
$$

Next to the derivatives of $f$ we also need a centre for our Taylor series. Since we want to find an approximation of $\cosh(1)$, it is natural to choose $a=0$ as the centre of our Taylor series, as the values of $\cosh(x)$ and $\sinh(x)$ at $x=0$ are easy to compute. This implies that

$$
f^{(n)}(0) = \begin{cases}
0 & \text{if } n \text{ is odd}, \\
1 & \text{if } n \text{ is even}.
\end{cases}
$$

This implies that the $n$th term of the Taylor series of $f$ at $x=0$ is given by

$$
\frac{f^{(n)}(0)}{n!}(x-0)^n = \begin{cases}
0 & \text{if } n \text{ is odd}, \\
\frac{1}{n!}x^n & \text{if } n \text{ is even}.
\end{cases}
$$

Therefore, the Taylor series of $f$ at $x=0$ is given by

$$
f(x) = \cosh(x)=\sum_{n=0}^{\infty}\frac{1}{(2n)!}x^{2n}.
$$

Let $a_n=\frac{1}{(2n)!}x^{2n}$, then the ratio test with $x\neq0$ gives us that

\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|\frac{1}{(2n+2)!}x^{2n+2}\cdot\frac{(2n)!}{1}x^{-2n}\right|\\
&=\lim\limits_{n\to\infty}\frac{x^2}{(2n+1)(2n+2)}=0,
\end{align*}

so the radius of convergence is $R=\infty$.

Because the radius of convergence is infinite, we can use Taylor's inequality to find an approximation of $\cosh(1)$ exact to three decimal places. We do have to pick an interval that contains $0$ and $1$ to find an upper bound for $|f^{(n+1)}(x)|$. We choose the interval $[0,\ln(3)]$, as $\cosh(x)$ and $\sinh(x)$ are both positive on this interval and therefore also increasing on this interval. This implies that for $x\in[0,\ln(3)]$ we have

\begin{align*}
|f^{(n+1)}(x)| &= \begin{cases}
\sinh(x) & \text{if } n \text{ is even}, \\
\cosh(x) & \text{if } n \text{ is odd},
\end{cases} \\
&\leq \begin{cases}
\sinh(\ln(3)) & \text{if } n \text{ is even}, \\
\cosh(\ln(3)) & \text{if } n \text{ is odd},
\end{cases} \\
&= \begin{cases}
\frac{4}{3} & \text{if } n \text{ is even}, \\
\frac{5}{3} & \text{if } n \text{ is odd},
\end{cases} \\
&\leq \frac{5}{3}.
\end{align*}

This implies that we can take $M=\frac{5}{3}$ in Taylor's inequality. We want to find an approximation of $\cosh(1)$ exact to three decimal places, so we want to find $n$ such that

$$
|R_n(x)|\leq\frac{M}{(n+1)!}|1-0|^{n+1}=\frac{5}{3(n+1)!}\leq 0.5\cdot10^{-3}.
$$

Solving the last inequality gives us $(n+1)!\geq \dfrac13\cdot10^4 = 3333.\overline{33}$. This implies that we must take $n\geq6$ to find an approximation of $\cosh(1)$ exact to three decimal places. The following table shows the values of $T_n(1)$ for $n=0,2,4,6,8,10$ exact to six decimal places. We skip all odd values of $n$ as the Taylor series of $f$ at $x=0$ only has even terms.

```{list-table} Approximation of $\cosh(1)$ using Taylor polynomials.
:header-rows: 1
:class: mid-align center-align

* - $n$ 
  - $T_n(1)$
* - $0$
  - $1.000000\ldots$
* - $2$
  - $1.500000\ldots$
* - $4$
  - $1.541666\ldots$
* - $6$
  - $1.543055\ldots$
* - $8$
  - $1.543080\ldots$
* - $10$
  - $1.543080\ldots$
```
:::

## Taylor series of standard functions

So far, we have obtained the Taylor series of six standard functions at $x=0$, or in other words, the Maclaurin series. These are:

```{list-table} Maclaurin series of six standard functions.
:header-rows: 1
:align: left
:class: mid-align center-align

* - Function
  - Maclaurin series
  - Interval of convergence
  - Details
* - $e^x$
  - $\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{n!}$
  - $\mathbb{R}$
  - {prf:ref}`Ex:Series:ExpTaylor`
* - $\sin(x)$
  - $\displaystyle\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+1}}{(2n+1)!}$
  - $\mathbb{R}$
  - {prf:ref}`Ex:Series:SinTaylor`
* - $\cos(x)$
  - $\displaystyle\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n}}{(2n)!}$
  - $\mathbb{R}$
  - {prf:ref}`Ex:Series:CosTaylor`
* - $\displaystyle\frac{1}{1-x}$
  - $\sum_{n=0}^{\infty}x^n$
  - $(-1,1)$
  - {prf:ref}`Ex:Series:GeometricSeries`
* - $\displaystyle\ln(1+x)$
  - $\displaystyle\sum_{n=0}^{\infty}(-1)^n\frac{x^{n+1}}{n+1}$
  - $(-1,1]$
  - {prf:ref}`Ex:Series:PowerSeriesExample2`
* - $\displaystyle\arctan(x)$
  - $\displaystyle\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+1}}{2n+1}$
  - $[-1,1]$
  - {prf:ref}`Ex:Series:Arctan`
```

The Taylor series of these functions at $x=0$ can be used in many applications, such as finding limits, approximating functions, and evaluating integrals. We will see some of these applications in the next examples.

::::::{prf:example}
:label: Ex:Series:TaylorLimitExp

Using the Taylor series of $e^x$ at $x=0$ we can find for $x\neq 0$ that:

\begin{align*}
\frac{e^x-1-x}{x^2} &= \frac{\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{n!} - 1 - x}{x^2} \\
&= \frac{\left(1+x + \displaystyle\sum_{n=2}^{\infty}\frac{x^n}{n!}\right) - 1 - x}{x^2} \\
&= \frac{\displaystyle\sum_{n=2}^{\infty}\frac{x^n}{n!}}{x^2} \\
&= \displaystyle\sum_{n=2}^{\infty}\frac{x^{n-2}}{n!} \\
&= \frac{1}{2}+\frac{1}{6}x+\frac{1}{24}x^2+\cdots.
\end{align*}

This means that if we take the limit as $x$ approaches $0$, then we have

\begin{align*}
\lim\limits_{x\to 0}\frac{e^x-1-x}{x^2} &= \lim\limits_{x\to 0}\left(\frac{1}{2}+\frac{1}{6}x+\frac{1}{24}x^2+\cdots\right)\\
&=\frac{1}{2}+0+0+\cdots \\
&=\frac{1}{2}.
\end{align*}

::::::

::::::{prf:example}
:label: Ex:Series:TaylorLimitCos

In a similar fashion as in the previous example, we find that

\begin{align*}
\lim\limits_{x\to 0}\frac{\cos(x)-1+\frac{1}{2}x^2}{x^4}
&= \lim\limits_{x\to 0}\frac{\displaystyle\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n}}{(2n)!}-1+\frac{1}{2}x^2}{x^4} \\
&= \lim\limits_{x\to 0}\frac{\left(1-\frac{1}{2}x^2+\displaystyle\sum_{n=2}^{\infty}(-1)^n\frac{x^{2n}}{(2n)!}\right)-1+\frac{1}{2}x^2}{x^4} \\
&= \lim\limits_{x\to 0}\frac{\displaystyle\sum_{n=2}^{\infty}(-1)^n\frac{x^{2n}}{(2n)!}}{x^4} \\
&= \lim\limits_{x\to 0}\displaystyle\sum_{n=2}^{\infty}(-1)^n\frac{x^{2n-4}}{(2n)!} \\
&= \lim\limits_{x\to 0}\left(-\frac{1}{24}+\frac{1}{720}x^2-\frac{1}{40320}x^4+\cdots\right) \\
&=-\frac{1}{24}+0-0+\cdots \\
&=-\frac{1}{24}.
\end{align*}

::::::

::::::{prf:example}
:label: Ex:Series:TaylorIntegralSin

Using $\sin(x)=\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{2n+1}$ for all $x\in\mathbb{R}$ we obtain that

\begin{align*}
\int_0^1x\sin(x^3)\,dx
&= \int_0^1x\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}(x^3)^{2n+1}\,dx \\
&= \int_0^1x\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{6n+3}\,dx \\
&= \int_0^1\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{6n+4}\,dx \\
&= \displaystyle\sum_{n=0}^{\infty}\int_0^1\frac{(-1)^n}{(2n+1)!}x^{6n+4}\,dx \\
&= \displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}\int_0^1x^{6n+4}\,dx \\
&= \displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}\frac{1}{6n+5} \\
&= \frac{1}{5}-\frac{1}{66}+\frac{1}{2040}-\frac{1}{115920}+\cdots
\end{align*}

We can use this series representation of the definite integral to find an approximation of the value of the integral by truncating the series after a finite number of terms. {numref}`Tab:Series:TaylorIntegralSin` shows the approximations of the value of the integral using one, two, three and four term(s).

```{list-table} Approximations of $\displaystyle\int_0^1x\sin(x^3)\,dx$ using the Taylor series of $\sin(x)$ at $x=0$.
:header-rows: 1
:class: mid-align center-align
:name: Tab:Series:TaylorIntegralSin

* - $n$ 
  - $\displaystyle\sum_{k=0}^n\frac{(-1)^k}{(2k+1)!}\frac{1}{6k+5}$
* - $0$
  - $0.200000\ldots$
* - $1$
  - $0.184848\ldots$
* - $2$
  - $0.185338\ldots$
* - $3$
  - $0.185330\ldots$  
```

Note that with $n=1$ we already have an approximation of the value of the integral that is exact to two decimal places, and with $n=2$ we have an approximation of the value of the integral that is exact to three decimal places.

::::::

::::::{prf:example}
:label: Ex:Series:TaylorIntegralExp

Using $e^x=\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{n!}$ for all $x\in\mathbb{R}$ we obtain that

\begin{align*}
\int_0^{\frac{1}{2}}xe^{-x^4}\,dx
&= \int_0^{\frac{1}{2}}x\displaystyle\sum_{n=0}^{\infty}\frac{(-x^4)^n}{n!}\,dx \\
&= \int_0^{\frac{1}{2}}x\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^nx^{4n}}{n!}\,dx \\
&= \int_0^{\frac{1}{2}}\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^nx^{4n+1}}{n!}\,dx \\
&= \displaystyle\sum_{n=0}^{\infty}\int_0^{\frac{1}{2}}\frac{(-1)^nx^{4n+1}}{n!}\,dx \\
&= \displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}\int_0^{\frac{1}{2}}x^{4n+1}\,dx \\
&= \displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}\frac{1}{4n+2}\left(\frac12\right)^{4n+2}.
\end{align*}

We can use this series representation of the definite integral to find an approximation of the value of the integral by truncating the series after a finite number of terms. {numref}`Tab:Series:TaylorIntegralExp` shows the approximations of the value of the integral using one, two, three and four term(s).

```{list-table} Approximations of $\displaystyle\int_0^{\frac{1}{2}}xe^{-x^4}\,dx$ using the Taylor series of $e^x$ at $x=0$.
:header-rows: 1
:class: mid-align center-align
:name: Tab:Series:TaylorIntegralExp

* - $n$ 
  - $\displaystyle\sum_{k=0}^n\frac{(-1)^k}{k!}\frac{1}{4k+2}\left(\frac12\right)^{4k+2}$
* - $0$
  - $0.125000\ldots$
* - $1$
  - $0.122396\ldots$
* - $2$
  - $0.122445\ldots$
* - $3$
  - $0.122444\ldots$  
```

In this example we have an approximation of the value of the integral that is already exact to three decimal places with $n=1$.

::::::

Before we turn our attention to a special set of functions and their Taylor series in the next section, let's practice with some exercises.

## Grasple exercises

:::{todo}
Add exercises on Taylor series, including finding Taylor series of functions, finding the radius of convergence, and using Taylor's inequality to find approximations of functions in {numref}`Sec:Series:TaylorSeries`.
:::

