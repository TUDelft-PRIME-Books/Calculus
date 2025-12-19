(Sec:Series:TaylorSeries)=

# Taylor series

In this section we cover:

- Taylor and Maclaurin series (including series of exponential, sine, cosine, logarithm, arctangent), including connection with Taylor polynomials
- Analyticity
- Binomial series
- Applications: limits, integrals

## Introduction

In the previous section we have seen some power series representations of certain functions. These were all based on the geometric series $\displaystyle\sum_{n=0}^{\infty}x^n=\frac{1}{1-x}$ for $|x|<1$. We could use substitutions, differentiation and integration to find power series representations of other functions. In this section we will find power series representations of more general functions that are infinitely differentiable. 

Let $f$ be such an infinitely differentiable function and suppose that $f$ can be represented by a power series: 

$$ 
\begin{align*}
f(x)&=c_0+c_1(x-a)+c_2(x-a)^2+c_3(x-a)^3+c_4(x-a)^4+\cdots\\
&=\sum_{n=0}^{\infty}c_n(x-a)^n,\quad|x-a| < R
\end{align*} 
$$ 

with *positive* radius of convergence $R$. Then we have 

$$ 
\begin{align*}
f'(x)&=c_1+2c_2(x-a)+3c_3(x-a)^2+4c_4(x-a)^3+5c_5(x-a)^4+\cdots\\
&=\sum_{n=1}^{\infty}n(x-a)^{n-1},\quad|x-a| < R, 
\end{align*}
$$ 

$$ 
\begin{align*}
f''(x)&=2c_2+2\cdot3c_3(x-a)+3\cdot4c_4(x-a)^2+4\cdot5c_5(x-a)^3+\cdots\\
&=\sum_{n=2}^{\infty}n(n-1)(x-a)^{n-2},\quad|x-a| < R, 
\end{align*}
$$ 

$$ 
\begin{align*}
f^{(3)}(x)&=2\cdot3c_3+2\cdot3\cdot4c_4(x-a)+3\cdot4\cdot5c_5(x-a)^2+4\cdot5\cdot6c_6(x-a)^3+\cdots\\
&=\sum_{n=3}^{\infty}n(n-1)(n-2)(x-a)^{n-3},\quad|x-a| < R, 
\end{align*}
$$ 

and so on. Since all these power series converge at least at $x=a$ 
we substitute $x=a$ to obtain that 

$$ 
\begin{align*}
&f(a)=c_0,\quad f'(a)=c_1,\quad f''(a)=2c_2,\quad f^{(3)}(a)=2\cdot3c_3,\quad\ldots\\
&\quad\Longrightarrow\quad f^{(n)}(a)=1\cdot2\cdot3\cdot4\cdots nc_n=n!c_n,\quad 
n=1,2,3,\ldots. 
\end{align*}
$$ 

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
c_n=\frac{f^{(n)}(a)}{n!},\quad n=0,1,2,\ldots. 
$$ 

:::::: 

::::::{prf:definition} Taylor series 
:label: Def:Series:TaylorSeries 
The series 

$$ 
\begin{align*}
&\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n\\
&\quad{}=f(a)+\frac{f'(a)}{1!}(x-a)+\frac{f''(a)}{2!}(x-a)^2+\frac{f^{(3)}(a)}{3!}(x-a)^3+\cdots
\end{align*}
$$ 

is called the **Taylor series** or the **Taylor expansion** of the function $f$ at $x=a$. This Taylor series is named after the English mathematician [Brook Taylor (1685-1731)](https://en.wikipedia.org/wiki/Brook_Taylor). 

The special case with $a=0$ 

$$ 
\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n=f(0)+\frac{f'(0)}{1!}x+\frac{f''(0)}{2!}x^2+\frac{f^{(3)}(0)}{3!}x^3+\cdots
$$ 

is sometimes (also) called the **Maclaurin series** of $f$, named after the Scottish mathematician [Colin Maclaurin (1698-1746)](https://en.wikipedia.org/wiki/Colin_Maclaurin). 
:::::: 

::::::{note} 
The $n$th partial sum 

$$ 
T_n(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k 
$$ 

is the $n$th-order *Taylor polynomial* of $f$ around $x=a$. 
:::::: 

::::::{prf:example}
For $f(x)=e^x$ we have: $f^{(n)}(x)=e^x$ for $n=0,1,2,\ldots$. Hence: $f^{(n)}(0)=1$ for $n=0,1,2,\ldots$. This implies that

$$
e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!}=1+x+\frac{1}{2}x^2+\frac{1}{6}x^3+\frac{1}{24}x^4+\frac{1}{120}x^5+\cdots.
$$ 

In order to find the radius of convergence, we apply the ratio test: for $x\neq0$ let $a_n=\displaystyle\frac{x^n}{n!}$, then we have

$$ 
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim\limits_{n\to\infty}\left|\frac{x^{n+1}}{(n+1)!}\cdot\frac{n!}{x^n}\right|
=\lim\limits_{n\to\infty}\frac{|x|}{n+1}=0.
$$ 
 
This implies that the Taylor series converges for all $x\in\mathbb{R}$, so the radius of convergence is $R=\infty$.

::::{figure} Images/taylor.png
:name: Fig:Series:Taylor
:align: center

The function $f(x)=e^x$ and its Taylor polynomials $T_1(x)=1+x$, $T_2(x)=1+x+\frac{1}{2}x^2$ and $T_3(x)=1+x+\frac{1}{2}x^2+\frac{1}{6}x^3$.
::::

::::::

In general, $f(x)$ is the sum of its Taylor series if

$$
f(x)=\lim_{n\to\infty}T_n(x).
$$

If we let $R_n(x)=f(x)-T_n(x)$ or $f(x)=T_n(x)+R_n(x)$, then $R_n(x)$ is called the **remainder** of the Taylor series. So, if $\lim\limits_{n\to\infty}R_n(x)=0$, then

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

If we want to show that $\lim\limits_{n\to\infty}R_n(x)=0$ for a specific function $f$, we usually use the following theorem:

::::::{prf:theorem} Taylor's inequality
:label: Thm:Series:TaylorInequality
If $\left|f^{(n+1)}(x)\right|\leq M$ for $|x-a|<R$, then the remainder $R_n(x)$ of the Taylor series satisfies the inequality

$$
|R_n(x)|\leq\frac{M}{(n+1)!}|x-a|^{n+1}\quad\text{for}\quad|x-a|<R.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:TaylorInequality`
:class: solution, dropdown
See {numref}`Sec:Taylor polynomials`.
:::

::::::{prf:remark} Formulas for Taylor's remainder term
Instead of using Taylor's inequality, we may use a formula for the remainder term $R_n(x)$.

If $f^{(n+1)}$ is continuous on an interval $I$ and $x\in I$, then 

$$
R_n(x)=\frac{1}{n!}\int_a^x(x-t)^nf^{(n+1)}(t)\,dt.
$$

This is called the *integral form of the remainder term*. The mean value theorem implies that there exists a number $c$ between $x$ and $a$ such that

$$
R_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}.
$$

This is called *Lagrange's form of the remainder term*, named after the Italian-French mathematician [Joseph-Louis Lagrange (1736-1813)](https://en.wikipedia.org/wiki/Joseph-Louis_Lagrange).
::::::

::::::{prf:example}
For $f(x)=\sin(x)$ we have: $f'(x)=\cos(x)$, $f''(x)=-\sin(x)$, $f^{(3)}(x)=-\cos(x)$, $f^{(4)}(x)=\sin(x)=f(x)$ and so on. Hence: $f(0)=0$, $f'(0)=1$, $f''(0)=0$, $f^{(3)}(0)=-1$, $f^{(4)}(0)=1=f(0)$ and so on. This implies that

$$
\sin(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{2n+1}=x-\frac{1}{6}x^3+\frac{1}{120}x^5-\frac{1}{5040}x^7+\cdots.
$$

In order to find the radius of convergence, we apply the ratio test: for $x\neq0$ let $a_n=\displaystyle\frac{(-1)^n}{(2n+1)!}x^{2n+1}$, then we have

$$
\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|\frac{(-1)^{n+1}x^{2n+3}}{(2n+3)!}\cdot\frac{(2n+1)!}{(-1)^nx^{2n+1}}\right|\\
&=\lim\limits_{n\to\infty}\frac{x^2}{(2n+2)(2n+3)}=0.
\end{align*}
$$

This implies that the Taylor series for $\sin(x)$ converges for all $x\in\mathbb{R}$, so the radius of convergence is $R=\infty$. 

::::::

::::::{prf:example}
Similarly we obtain that

$$
\cos(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n)!}x^{2n}=1-\frac{1}{2}x^2+\frac{1}{24}x^4-\frac{1}{720}x^6+\cdots.
$$

In order to find the radius of convergence, we apply the ratio test: for $x\neq0$ let $a_n=\displaystyle\frac{(-1)^n}{(2n)!}x^{2n}$, then we have

$$
\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|\frac{(-1)^{n+1}x^{2n+2}}{(2n+2)!}\cdot\frac{(2n)!}{(-1)^nx^{2n}}\right|\\
&=\lim\limits_{n\to\infty}\frac{x^2}{(2n+1)(2n+2)}=0.
\end{align*}
$$

This implies that the Taylor series for $\cos(x)$ converges for all $x\in\mathbb{R}$, so the radius of convergence is $R=\infty$.
::::::

## Standard Taylor series

So far, we have obtained the Maclaurin series for the following six standard functions:

```{list-table}
:header-rows: 0
:align: left
:class: mid-align center-align

* - $e^x=\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{n!},\quad x\in\mathbb{R}$
* - $\sin(x)=\displaystyle\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+1}}{(2n+1)!},\quad x\in\mathbb{R}$
* - $\cos(x)=\displaystyle\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n}}{(2n)!},\quad x\in\mathbb{R}$
* - $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n,\quad |x|<1$
* - $\displaystyle\ln(1+x)=\sum_{n=0}^{\infty}(-1)^n\frac{x^{n+1}}{n+1},\quad |x|<1$
* - $\displaystyle\arctan(x)=\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+1}}{2n+1},\quad |x|<1$  
```

It is worthwhile to remember these formulas.

::::::{prf:example} Applications
1) Using $e^x=1+x+\frac{1}{2}x^2+\frac{1}{6}x^3+\cdots$ for all $x\in\mathbb{R}$ we find that

$$
\begin{align*}
\lim\limits_{x\to 0}\frac{e^x-1-x}{x^2}&=\lim\limits_{x\to 0}\frac{1+x+\frac{1}{2}x^2+\frac{1}{6}x^3+\cdots-1-x}{x^2}\\
&=\lim\limits_{x\to 0}\frac{\frac{1}{2}x^2+\frac{1}{6}x^3+\cdots}{x^2}=\lim\limits_{x\to 0}\left(\frac{1}{2}+\frac{1}{6}x+\cdots\right)\\
&=\frac{1}{2}+0+0=\frac{1}{2}.
\end{align*}
$$

2) Using $\cos(x)=1-\frac{1}{2}x^2+\frac{1}{24}x^4-\frac{1}{720}x^6+\cdots$ for all $x\in\mathbb{R}$ we find that

$$
\begin{align*}
\lim\limits_{x\to 0}\frac{\cos(x)-1+\frac{1}{2}x^2}{x^4}&=\lim\limits_{x\to 0}\frac{1-\frac{1}{2}x^2+\frac{1}{24}x^4-\frac{1}{720}x^6+\cdots-1+\frac{1}{2}x^2}{x^4}\\
&=\lim\limits_{x\to 0}\frac{\frac{1}{24}x^4-\frac{1}{720}x^6+\cdots}{x^4}\\
&=\lim\limits_{x\to 0}\left(\frac{1}{24}-\frac{1}{720}x^2+\cdots\right)=\frac{1}{24}-0+0=\frac{1}{24}.
\end{align*}
$$

3) Using $\sin(x)=\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{2n+1}$ for all $x\in\mathbb{R}$ we obtain that

$$
\begin{align*}
\int_0^1x\sin(x^3)\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}\int_0^1x^{6n+4}\,dx=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}\cdot\frac{1}{6n+5}\\
&=\frac{1}{5}-\frac{1}{66}+\frac{1}{2040}-\frac{1}{115920}+\cdots.
\end{align*}
$$

Taking more and more terms this leads to the following approximations:

```{list-table}
:header-rows: 1
:align: center
:class: mid-align center-align

* - $N$ 
  - $\displaystyle\sum_{n=0}^N\frac{(-1)^n}{(2n+1)!}\cdot\frac{1}{6n+5}$
* - $0$
  - $\displaystyle\frac{1}{5}=0.2$
* - $1$
  - $\displaystyle\frac{1}{5}-\frac{1}{66}\approx0.184848$
* - $2$
  - $\displaystyle\frac{1}{5}-\frac{1}{66}+\frac{1}{2040}\approx0.185338$
* - $3$
  - $\displaystyle\frac{1}{5}-\frac{1}{66}+\frac{1}{2040}-\frac{1}{115920}\approx0.185330$  
```

4) Using $e^x=\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{n!}$ for all $x\in\mathbb{R}$ we obtain that

$$
\begin{align*}
\int_0^{\frac{1}{2}}xe^{-x^4}\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}\int_0^{\frac{1}{2}}x^{4n+1}\,dx=\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}\cdot\frac{(\frac{1}{2})^{4n+2}}{4n+2}\\
&=\frac{1}{8}-\frac{1}{384}+\frac{1}{20480}-\frac{1}{1376256}+\cdots.
\end{align*}
$$

Taking more and more terms this leads to the following approximations:

```{list-table}
:header-rows: 1
:align: center
:class: mid-align center-align

* - $N$ 
  - $\displaystyle\sum_{n=0}^N\frac{(-1)^n}{n!}\cdot\frac{(\frac{1}{2})^{4n+2}}{4n+2}$
* - $0$
  - $\displaystyle\frac{1}{8}=0.125$
* - $1$
  - $\displaystyle\frac{1}{8}-\frac{1}{384}\approx0.122396$
* - $2$
  - $\displaystyle\frac{1}{8}-\frac{1}{384}+\frac{1}{20480}\approx0.122445$
* - $3$
  - $\displaystyle\frac{1}{8}-\frac{1}{384}+\frac{1}{20480}-\frac{1}{1376256}\approx0.122444$  
```

::::::

## Catalan's constant

**Catalan's constant** $G$ is defined as the sum of the series $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}$.

Note that this series is absolutely convergent. However, it is not easy to find its sum. We have

$$
G:=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}\approx0.916.
$$

There are several alternative (integral) representations for this constant. Since 

$$
\arctan(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}x^{2n+1}\quad\text{for}\quad |x|<1
$$ 

we have

$$
\begin{align*}
\int_0^1\frac{\arctan(x)}{x}\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}\int_0^1x^{2n}\,dx=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}\cdot\frac{x^{2n+1}}{2n+1}\bigg|_0^1\\
&=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}=G.
\end{align*}
$$

Using $x=e^{-t}$ we obtain

$$
G=\int_0^1\frac{\arctan(x)}{x}\,dx=\int_{\infty}^0\frac{\arctan\left(e^{-t}\right)}{e^{-t}}\,d e^{-t}
=\int_0^{\infty}\arctan\left(e^{-t}\right)\,dt.
$$

The substitution $\arctan{x}=t$ or $x=\tan(t)$ leads to

$$
\begin{align*}
\int_0^1\frac{\arctan(x)}{x}\,dx&=\int_0^{\frac{1}{4}\pi}\frac{t}{\tan(t)}d\tan(t)=\int_0^{\frac{1}{4}\pi}\frac{t}{\tan(t)}\cdot\frac{1}{\cos^2(t)}\,dt\\
&=\int_0^{\frac{1}{4}\pi}\frac{t}{\sin(t)\cos(t)}\,dt.
\end{align*}
$$

This can be rewritten as

$$
G=\int_0^{\frac{1}{4}\pi}\frac{t}{\sin(t)\cos(t)}\,dt=\int_0^{\frac{1}{4}\pi}\frac{2t}{\sin(2t)}\,dt=\frac{1}{2}\int_0^{\frac{1}{2}\pi}\frac{x}{\sin(x)}\,dx.
$$

Using integration by parts we obtain

$$
\begin{align*}
\int_0^1x^n\ln(x)\,dx&=\int_0^1\frac{1}{n+1}\ln(x)\,dx^{n+1}\\
&=\frac{1}{n+1}x^{n+1}\ln(x)\bigg|_0^1-\frac{1}{n+1}\int_0^1x^{n+1}\,d\ln(x)\\
&=0-\frac{1}{n+1}\int_0^1x^n\,dx=-\frac{1}{(n+1)^2}x^{n+1}\bigg|_0^1\\
&=-\frac{1}{(n+1)^2},\quad n=0,1,2,\ldots.
\end{align*}
$$

With $\displaystyle\frac{1}{1+x^2}=\sum_{n=0}^{\infty}(-x^2)^n$ for $|x|<1$ this implies that

$$
\int_0^1\frac{\ln(x)}{1+x^2}\,dx=\sum_{n=0}^{\infty}(-1)^n\int_0^1x^{2n}\ln(x)\,dx=-\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}=-G.
$$

Using the substitution $x=\dfrac{1}{t}$ we obtain

$$
G=-\int_0^1\frac{\ln(x)}{1+x^2}\,dx=-\int_{\infty}^1\frac{\ln\left(\frac{1}{t}\right)}{1+\left(\frac{1}{t}\right)^2}\cdot\left(-\frac{1}{t^2}\right)\,dt=\int_1^{\infty}\frac{\ln(t)}{1+t^2}\,dt.
$$

Alternative forms of these integrals are obtained using certain substitutions.

If we set $t=\tan(\theta)$, then we have $dt=\left(1+\tan^2(\theta)\right)\,d\theta$ and therefore

$$
G=-\int_0^1\frac{\ln(t)}{1+t^2}\,dt=-\int_0^{\frac{1}{4}\pi}\frac{\ln\left(\tan(\theta)\right)}{1+\tan^2(\theta)}\,d\tan(\theta)
=-\int_0^{\frac{1}{4}\pi}\ln\left(\tan(\theta)\right)\,d\theta
$$

or

$$
G=\int_1^{\infty}\frac{\ln(t)}{1+t^2}\,dt=\int_{\frac{1}{4}\pi}^{\frac{1}{2}\pi}\ln\left(\tan(\theta)\right)\,d\theta. 
$$ 
 
Setting $\ln(t)=x$ or $t=e^x$ we obtain

$$ 
\begin{align*}
G&=\int_1^{\infty}\frac{\ln(t)}{1+t^2}\,dt=\int_0^{\infty}\frac{x}{1+e^{2x}}\cdot e^x\,dx=\int_0^{\infty}\frac{x}{e^{-x}+e^x}\,dx\\
&=\frac{1}{2}\int_0^{\infty}\frac{x}{\cosh(x)}\,dx.
\end{align*}
$$ 
 
The relation

$$
\tan^2(\theta)=\frac{\sin^2(\theta)}{\cos^2(\theta)}=\frac{2\sin^2(\theta)}{2\cos^2(\theta)}=\frac{1-\cos(2\theta)}{1+\cos(2\theta)}
$$ 
 
leads to another interesting representation

$$
\begin{align*}
G&=-\int_0^{\frac{1}{4}\pi}\ln\left(\tan(\theta)\right)\,d\theta=-\frac{1}{2}\int_0^{\frac{1}{4}\pi}\ln\left(\tan^2(\theta)\right)\,d\theta\\
&=-\frac{1}{2}\int_0^{\frac{1}{4}\pi}\ln\left(\frac{1-\cos(2\theta)}{1+\cos(2\theta)}\right)\,d\theta,
\end{align*}
$$ 
 
which is equivalent to

$$
G=-\frac{1}{4}\int_0^{\frac{1}{2}\pi}\ln\left(\frac{1-\cos(x)}{1+\cos(x)}\right)\,dx\quad\text{or}\quad
G=\frac{1}{4}\int_0^{\frac{1}{2}\pi}\ln\left(\frac{1+\cos(x)}{1-\cos(x)}\right)\,dx.
$$ 
 
When we studied Serret's integral in {numref}`Sec:Integration:Substitution` we used the fact that 

$$
\int_0^{\frac{1}{4}\pi}\ln\left(\cos(\tfrac{1}{4}\pi-\theta)\right)\,d\theta=\int_0^{\frac{1}{4}\pi}\ln(\cos(t))\,dt.
$$ 

This integral can be evaluated in terms of Catalan's constant. Using the fact that $\cos(x)=\sin(\frac{1}{2}\pi-x)$ we obtain that

$$ 
\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(\sin(\tfrac{1}{2}\pi-x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(\cos(x))\,dx. 
$$ 
 
Note that this implies that

$$ 
\int_0^{\frac{1}{2}\pi}\ln(\tan(x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx-\int_0^{\frac{1}{2}\pi}\ln(\cos(x))\,dx=0. 
$$ 

Earlier we have seen that

$$
\int_0^{\frac{1}{4}\pi}\ln(\tan(x))\,dx=-G\quad\text{and}\quad\int_{\frac{1}{4}\pi}^{\frac{1}{2}\pi}\ln(\tan(x))\,dx=G.
$$ 
 
If we apply the substitution $2x=t$ we find that

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\ln(\sin(2x))\,dx&=\frac{1}{2}\int_0^{\pi}\ln(\sin(t))\,dt\\
&=\frac{1}{2}\int_0^{\frac{1}{2}\pi}\ln(\sin(t))\,dt+\frac{1}{2}\int_{\frac{1}{2}\pi}^{\pi}\ln(\sin(t))\,dt.
\end{align*}
$$ 
 
Then we apply the substitution $t=\pi-x$ to the latter integral to find that

$$ 
\int_{\frac{1}{2}\pi}^{\pi}\ln(\sin(t))\,dt=-\int_{\frac{1}{2}\pi}^0\ln(\sin(\pi-x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx.
$$ 
 
Hence we have $\displaystyle\int_0^{\frac{1}{2}\pi}\ln(\sin(2x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx$. 
 
Finally, we derive for $I=\displaystyle\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(\cos(x))\,dx$ that 

$$
\begin{align*}
I&=\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(\sin(2x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(2\sin(x)\cos(x))\,dx\\
&=\int_0^{\frac{1}{2}\pi}\left(\ln(2)+\ln(\sin(x))+\ln(\cos(x))\right)\,dx\\
&=\int_0^{\frac{1}{2}\pi}\ln(2)\,dx+\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx+\int_0^{\frac{1}{2}\pi}\ln(\cos(x))\,dx=\frac{1}{2}\pi\ln(2)+2I,
\end{align*}
$$
 
which implies that $I=-\frac{1}{2}\pi\ln(2)$. The substitution $x=\frac{1}{2}\pi-t$ now leads to

$$ 
\int_{\frac{1}{4}\pi}^{\frac{1}{2}\pi}\ln(\sin(x))\,dx=-\int_{\frac{1}{4}\pi}^0\ln(\sin(\tfrac{1}{2}\pi-t)\,dt=\int_0^{\frac{1}{4}\pi}\ln(\cos(t))\,dt
$$

and

$$
\int_{\frac{1}{4}\pi}^{\frac{1}{2}\pi}\ln(\cos(x))\,dx=-\int_{\frac{1}{4}\pi}^0\ln(\cos(\tfrac{1}{2}\pi-t)\,dt=\int_0^{\frac{1}{4}\pi}\ln(\sin(t))\,dt.
$$

Hence we have

$$
\begin{align*}
\int_0^{\frac{1}{4}\pi}\ln(\sin(x))\,dx+\int_0^{\frac{1}{4}\pi}\ln(\cos(x))\,dx&=\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx\\
&=\int_0^{\frac{1}{2}\pi}\ln(\cos(x))\,dx=-\frac{1}{2}\pi\ln(2)
\end{align*}
$$

and

$$
\int_0^{\frac{1}{4}\pi}\ln(\sin(x))\,dx-\int_0^{\frac{1}{4}\pi}\ln(\cos(x))\,dx=\int_0^{\frac{1}{4}\pi}\ln(\tan(x))\,dx=-G.
$$

This implies that

$$
\int_0^{\frac{1}{4}\pi}\ln(\sin(x))\,dx=-\frac{1}{2}G-\frac{1}{4}\pi\ln(2)
$$

and

$$
\int_0^{\frac{1}{4}\pi}\ln(\cos(x))\,dx=\frac{1}{2}G-\frac{1}{4}\pi\ln(2).
$$

Note that this implies that

$$
\int_0^{\frac{1}{4}\pi}\ln(2\sin(x))\,dx=-\frac{1}{2}G\quad\text{and}\quad\int_0^{\frac{1}{4}\pi}\ln(2\cos(x))\,dx=\frac{1}{2}G.
$$

## The Riemann zeta function

The **Riemann zeta function** $\zeta(s)$ is defined as: $\displaystyle\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}$ for $\text{Re}(s)>1$.

This function is named after the German mathematician [Georg Friedrich Bernhard Riemann (1826-1866)](https://en.wikipedia.org/wiki/Bernhard_Riemann). 

We will only consider real values of $s$; in that case we know that the series is absolutely convergent if $s>1$. However, in general it is not very easy to find its sum.

Later (see {prf:ref}`Ex:Series:FourierExample3`) we will be able to show that 

$$
\zeta(2)=\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{1}{6}\pi^2\quad\text{and}\quad\zeta(4)=\sum_{n=1}^{\infty}\frac{1}{n^4}=\frac{1}{90}\pi^4.
$$

The value of $\zeta(3)\approx1.202057$ is also known as **Apéry's constant**, named after the Greek-French mathematician [Roger Apéry (1916-1994)](https://en.wikipedia.org/wiki/Roger_Ap%C3%A9ry).

One proof of the first result might be understandable right now. It is based on the Taylor series of $\displaystyle\frac{\sin(x)}{x}$ and an infinite product. For the infinite product we need to know that the (only but all) zeros of $\displaystyle\frac{\sin(x)}{x}$ are $x=\pm n\pi$ with $n\in\{1,2,3,\ldots\}$ and that $\displaystyle\lim\limits_{x\to0}\frac{\sin(x)}{x}=1$. Compare with {prf:ref}`Ex:Integration:IntroductionExamplesProductSine`. Then we have:

$$
\frac{\sin(x)}{x}=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)!}x^{2k}=\prod_{n=1}^{\infty}\left(1-\frac{x}{n\pi}\right)\left(1+\frac{x}{n\pi}\right)
=\prod_{n=1}^{\infty}\left(1-\frac{x^2}{n^2\pi^2}\right).
$$ 
 
Comparing the coefficients of $x^2$ we obtain that

$$
-\frac{1}{3!}=-\frac{1}{\pi^2}\sum_{n=1}^{\infty}\frac{1}{n^2}
\quad\Longrightarrow\quad\zeta(2)=\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{1}{6}\pi^2.
$$
 
Note that

$$
\sum_{n=0}^{\infty}\frac{1}{(2n+1)^s}=\sum_{n=1}^{\infty}\frac{1}{n^s}-\sum_{n=1}^{\infty}\frac{1}{(2n)^s}=\left(1-\frac{1}{2^s}\right)\zeta(s)
$$

and

$$
\begin{align*}
\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^s}&=\sum_{n=0}^{\infty}\frac{1}{(2n+1)^s}-\sum_{n=1}^{\infty}\frac{1}{(2n)^s}=\sum_{n=1}^{\infty}\frac{1}{n^s}-2\sum_{n=1}^{\infty}\frac{1}{(2n)^s}\\
&=\left(1-\frac{1}{2^{s-1}}\right)\zeta(s).
\end{align*}
$$

Using integration by parts we find that

$$
\begin{align*}
\int_0^1x^n\ln(x)\,dx&=\frac{1}{n+1}x^{n+1}\ln(x)\bigg|_0^1-\frac{1}{n+1}\int_0^1x^{n+1}\cdot\frac{1}{x}\,dx\\
&=0-\frac{1}{n+1}\int_0^1x^n\,dx=-\frac{1}{(n+1)^2}x^{n+1}\bigg|_0^1\\
&=-\frac{1}{(n+1)^2},\quad n=0,1,2,\ldots.
\end{align*}
$$ 
 
Now we use the series representation $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ for $|x|<1$ to find that

$$
\begin{align*}
\int_0^1\frac{\ln(x)}{1-x}\,dt&=\sum_{n=0}^{\infty}\int_0^1x^n\ln(x)\,dx=-\sum_{n=0}^{\infty}\frac{1}{(n+1)^2}=-\sum_{n=1}^{\infty}\frac{1}{n^2}\\
&=-\zeta(2)=-\frac{1}{6}\pi^2.
\end{align*}
$$ 
 
Furthermore using integration by parts we find that

$$
\begin{align*}
\int_0^1x^n\left(\ln(x)\right)^2\,dx&=\frac{1}{n+1}x^{n+1}\left(\ln(x)\right)^2\bigg|_0^1-\frac{2}{n+1}\int_0^1x^{n+1}\ln(x)\cdot\frac{1}{x}\,dx\\
&=0-\frac{2}{n+1}\int_0^1x^n\ln(x)\,dx=\frac{2}{(n+1)^3},\quad n=0,1,2,\ldots.
\end{align*}
$$ 
 
Again we use the series representation $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ for $|x|<1$ to find that

$$
\int_0^1\frac{\left(\ln(x)\right)^2}{1-x}\,dx=\sum_{n=0}^{\infty}\int_0^1x^n\left(\ln(x)\right)^2\,dx=2\sum_{n=0}^{\infty}\frac{1}{(n+1)^3}
=2\sum_{n=1}^{\infty}\frac{1}{n^3}=2\zeta(3).
$$

Similarly, we have

$$
\begin{align*}
\int_0^1\frac{\ln(x)}{1+x}\,dx&=\sum_{n=0}^{\infty}(-1)^n\int_0^1x^n\ln(x)\,dx=-\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^2}\\
&=-\left(1-\frac{1}{2}\right)\zeta(2)=-\frac{1}{12}\pi^2
\end{align*}
$$
 
and

$$
\begin{align*}
\int_0^1\frac{\left(\ln(x)\right)^2}{1+x}\,dx&=\sum_{n=0}^{\infty}(-1)^n\int_0^1x^n\left(\ln(x)\right)^2\,dx=2\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^3}\\
&=2\left(1-\frac{1}{4}\right)\zeta(3)=\frac{3}{2}\zeta(3).
\end{align*}
$$ 

Using the Taylor series $\displaystyle\ln(1-x)=-\sum_{n=1}^{\infty}\frac{x^n}{n}$ for $|x|<1$ we find that

$$
\begin{align*}
\int_0^1\frac{\ln(1-x)}{x}\,dx&=-\sum_{n=1}^{\infty}\frac{1}{n}\int_0^1x^{n-1}\,dx=-\sum_{n=1}^{\infty}\frac{1}{n}\cdot\frac{1}{n}x^n\bigg|_0^1=-\sum_{n=1}^{\infty}\frac{1}{n^2}\\
&=-\zeta(2)=-\frac{1}{6}\pi^2,
\end{align*}
$$

$$
\begin{align*}
\int_0^1\ln(x)\ln(1-x)\,dx&=-\sum_{n=1}^{\infty}\frac{1}{n}\int_0^1x^n\ln(x)\,dx=\sum_{n=1}^{\infty}\frac{1}{n}\cdot\frac{1}{(n+1)^2}\\
&=\sum_{n=1}^{\infty}\left(\frac{1}{n}-\frac{1}{n+1}-\frac{1}{(n+1)^2}\right)=1-\sum_{n=1}^{\infty}\frac{1}{(n+1)^2}\\
&=2-\sum_{n=1}^{\infty}\frac{1}{n^2}=2-\zeta(2)=2-\frac{1}{6}\pi^2
\end{align*}
$$

and

$$
\begin{align*}
\int_0^1\frac{\ln(x)\ln(1-x)}{x}\,dx&=-\sum_{n=1}^{\infty}\frac{1}{n}\int_0^1x^{n-1}\ln(x)\,dx=\sum_{n=1}^{\infty}\frac{1}{n}\cdot\frac{1}{n^2}\\
&=\sum_{n=1}^{\infty}\frac{1}{n^3}=\zeta(3).
\end{align*}
$$

By symmetry (or a substitution) we also have $\displaystyle\int_0^1\frac{\ln(x)\ln(1-x)}{1-x}\,dx=\zeta(3)$ and therefore

$$
\int_0^1\frac{\ln(x)\ln(1-x)}{x(1-x)}\,dx=\int_0^1\frac{\ln(x)\ln(1-x)}{x}\,dx+\int_0^1\frac{\ln(x)\ln(1-x)}{1-x}\,dx=2\zeta(3).
$$

Similarly, using $\displaystyle\ln(1+x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}x^{n+1}$ for $|x|<1$ we have

$$
\int_0^1\frac{\ln(1+x)}{x}\,dx=\sum_{n=0}^{\infty}\int_0^1\frac{(-1)^n}{n+1}x^n\,dx=\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^2}=\left(1-\frac{1}{2}\right)\zeta(2)=\frac{1}{12}\pi^2,
$$

$$
\begin{align*}
\int_0^1\ln(x)\ln(1+x)\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}\int_0^1x^{n+1}\ln(x)\,dx=-\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}\cdot\frac{1}{(n+2)^2}\\
&=\sum_{n=0}^{\infty}\left(\frac{(-1)^n}{n+2}-\frac{(-1)^n}{n+1}+\frac{(-1)^n}{(n+2)^2}\right)\\
&=1-2\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}+\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+2)^2}\\
&=1-2\ln(2)+1-\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^2}\\
&=2-2\ln(2)-\left(1-\frac{1}{2}\right)\zeta(2)=2-2\ln(2)-\frac{1}{12}\pi^2
\end{align*}
$$

and

$$
\begin{align*}
\int_0^1\frac{\ln(x)\ln(1+x)}{x}\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}\int_0^1x^n\ln(x)\,dx=-\sum_{n=1}^{\infty}\frac{(-1)^n}{n+1}\cdot\frac{1}{(n+1)^2}\\
&=-\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^3}=-\left(1-\frac{1}{4}\right)\zeta(3)=-\frac{3}{4}\zeta(3).
\end{align*}
$$

## Pascal's triangle and the binomium theorem

If we define *factorials* as $0!=1$ and $n!=n(n-1)!$ for $n=1,2,3,\ldots$, then the **binomial coefficient** $\displaystyle\binom{n}{k}$ (pronounced as "$n$ choose $k$") is defined as

:::{math}
:label: Eq:Series:BinomialCoefficient

\binom{n}{k}=\frac{n!}{k!(n-k)!}.
:::

The binomial coefficient $\displaystyle\binom{n}{k}$ denotes the number of ways to choose $k$ elements from a set of $n$ elements.

::::::{prf:example}
Consider the set $\{a,b,c,d\}$, then choosing two elements leads to six possibilities:

$$
\{a,b\},\quad\{a,c\},\quad\{a,d\},\quad\{b,c\},\quad\{b,d\}\quad\text{and}\quad\{c,d\}.
$$

We have: $\displaystyle\binom{4}{2}=\frac{4!}{2!\,2!}=\frac{3\cdot4}{1\cdot2}=6$.
::::::

**Pascal's triangle**, named after the French mathematician [Blaise Pascal (1623-1662)](https://en.wikipedia.org/wiki/Blaise_Pascal) is a triangular array of *binomial coefficients*:

$$
\begin{array}{ccccccccccccccc}
&&&&&&& 1\\[2.5mm]
&&&&&& 1 && 1\\[2.5mm]
&&&&& 1 && 2 && 1\\[2.5mm]
&&&& 1 && 3 && 3 && 1\\[2.5mm]
&&& 1 && 4 && 6 && 4 && 1\\[2.5mm]
&& 1 && 5 && 10 && 10 && 5 && 1\\[2.5mm]
& 1 && 6 && 15 && 20 && 15 && 6 && 1\\[2.5mm]
1 && 7 && 21 && 35 && 35 && 21 && 7 && 1
\end{array}
$$

In Pascal's triangle, each number is the sum of the two numbers directly above it. The triangle can be extended by adding rows below in the same pattern. In terms of *binomial coefficients* this property can be written as

:::{math}
:label: Eq:Series:Pascal
\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k},\quad k=1,2,3,\ldots,n
:::

for positive integers $n$.

:::{admonition} Proof of {eq}`Eq:Series:Pascal`
:class: solution, dropdown

$$
\begin{align*}
\binom{n-1}{k-1}+\binom{n-1}{k}&=\frac{(n-1)!}{(k-1)!\,(n-k)!}+\frac{(n-1)!}{k!\,(n-k-1)!}\\
&=\frac{(n-1)!}{k!\,(n-k)!}\left[k+(n-k)\right]\\
&=\frac{n\,(n-1)!}{k!\,(n-k)!}=\frac{n!}{k!\,(n-k)!}=\binom{n}{k}.
\end{align*}
$$

:::

Starting at the top, the rows in Pascal's theorem correspond to

$$
\begin{align*}
(a+b)^0&=1,\\[2.5mm]
(a+b)^1&=a+b,\\[2.5mm]
(a+b)^2&=a^2+2ab+b^2,\\[2.5mm]
(a+b)^3&=a^3+3a^2b+3ab^2+b^3,\\[2.5mm]
(a+b)^4&=a^4+4a^3b+6a^2b^2+4ab^3+b^4,\\[2.5mm]
\text{etcetera.}
\end{align*}
$$

The numbers in Pascal's triangle are the coefficients of the terms on the right. This leads to the binomial theorem:

::::::{prf:theorem} Binomial theorem
:label: Thm:Series:BinomialTheorem

$$
(a+b)^n=\sum_{k=0}^n\binom{n}{k}a^{n-k}b^k=\sum_{k=0}^n\binom{n}{k}a^kb^{n-k},\quad n=0,1,2,\ldots.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:BinomialTheorem`
:class: solution, dropdown
By mathematical induction: for $n=0$ it reads $(a+b)^0=1=\displaystyle\binom{0}{0}a^0b^0$ which is true by definition. Suppose that the formula is true for certain value of $n$, then we have:

$$
\begin{align*}
(a+b)^{n+1}&=(a+b)(a+b)^n=(a+b)\sum_{k=0}^n\binom{n}{k}a^{n-k}b^k\\
&=\sum_{k=0}^n\binom{n}{k}a^{n-k+1}b^k+\sum_{k=0}^n\binom{n}{k}a^{n-k}b^{k+1}\\
&=\sum_{k=0}^n\binom{n}{k}a^{n-k+1}b^k+\sum_{k=1}^{n+1}\binom{n}{k-1}a^{n-k+1}b^k\\
&=a^{n+1}+\sum_{k=1}^n\left\{\binom{n}{k}+\binom{n}{k-1}\right\}a^{n-k+1}b^k+b^{n+1}\\
&=a^{n+1}+\sum_{k=1}^n\binom{n+1}{k}a^{n+1-k}b^k+b^{n+1}=\sum_{k=0}^{n+1}\binom{n+1}{k}a^{n+1-k}b^k.
\end{align*}
$$

Since this is exactly the formula with $n$ replaced by $n+1$, this proves the theorem.
:::

::::::{prf:example}

$$
(1+x)^7=1+7x+21x^2+35x^3+35x^4+21x^5+7x^6+x^7.
$$

::::::

The *Fibonacci numbers* appear in Pascal's traingle as follows:

:::{figure} Images/fibonacci.png
:width: 75%
:name: Fibonacci numbers
:align: center

The Fibonacci numbers appearing in Pascal's triangle
:::

This can be written as $F_n=\displaystyle\sum_{k=0}^{\lfloor\frac{n-1}{2}\rfloor}\binom{n-k-1}{k}$  for $n=1,2,3,\ldots$. Here $\lfloor{\alpha}\rfloor$ denotes the greatest integer less than or equal to $\alpha$. This is equivalent to

$$
F_{2n-1}=\sum_{k=0}^{n-1}\binom{2n-k-2}{k}\quad\text{and}\quad F_{2n}=\sum_{k=0}^n\binom{2n-k-1}{k},\quad n=1,2,3,\ldots.
$$

The proof is by mathematical induction. For $n=1$ we have 

$$
F_1=\displaystyle\binom{0}{0}=1\quad\text{and}\quad F_2=\displaystyle\sum_{k=0}^1\binom{1-k}{k}=\binom{1}{0}+\binom{0}{1}=1.
$$

Now we assume that

$$
F_{2n-1}=\displaystyle\sum_{k=0}^{n-1}\binom{2n-k-2}{k}\quad\text{and}\quad F_{2n}=\displaystyle\sum_{k=0}^n\binom{2n-k-1}{k}
$$

for a certain value of $n$, then we have

$$
\begin{align*}
\sum_{k=0}^n\binom{2n-k}{k}&=1+\sum_{k=1}^n\binom{2n-k-1}{k}+\sum_{k=1}^n\binom{2n-k-1}{k-1}\\
&=\sum_{k=0}^n\binom{2n-k-1}{k}+\sum_{k=0}^{n-1}\binom{2n-k-2}{k}=F_{2n}+F_{2n-1}=F_{2n+1}
\end{align*}
$$

and

$$
\begin{align*}
\sum_{k=0}^{n+1}\binom{2n-k+1}{k}&=1+\sum_{k=1}^{n+1}\binom{2n-k}{k}+\sum_{k=1}^{n+1}\binom{2n-k}{k-1}\\
&=\sum_{k=0}^{n+1}\binom{2n-k}{k}+\sum_{k=0}^n\binom{2n-k-1}{k}=F_{2n+1}+F_{2n}=F_{2n+2}.
\end{align*}
$$

For each $m\in\mathbb{N}$ we also have

:::{math}
:label: Eq:Series:Fibonacci
F_{m+2n}=\displaystyle\sum_{k=0}^n\binom{n}{k}F_{m+k},\quad n=1,2,3,\ldots.
:::

:::{admonition} Proof of {eq}`Eq:Series:Fibonacci`
:class: solution, dropdown
The proof is by mathematical induction. For $n=1$ we have: $F_{m+2}=\displaystyle\sum_{k=0}^1\binom{1}{k}F_{m+k}=F_m+F_{m+1}$ which is true. Now we assume that 

$$
F_{m+2n}=\displaystyle\sum_{k=0}^n\binom{n}{k}F_{m+k}
$$

for a certain value of $n$. Then we have

$$
\begin{align*}
\sum_{k=0}^{n+1}\binom{n+1}{k}F_{m+k}&=F_m+\sum_{k=1}^{n+1}\left\{\binom{n}{k}+\binom{n}{k-1}\right\}F_{m+k}\\
&=\sum_{k=0}^n\binom{n}{k}F_{m+k}+\sum_{k=0}^n\binom{n}{k}F_{m+k+1}\\
&=F_{m+2n}+F_{m+2n+1}=F_{m+2n+2}.
\end{align*}
$$

This is the original formula with $n$ replaced by $n+1$, which proves {eq}`Eq:Series:Fibonacci`.
:::

The special case $m=0$ of {eq}`Eq:Series:Fibonacci` reads

$$
F_{2n}=\displaystyle\sum_{k=0}^n\binom{n}{k}F_k,\quad n=1,2,3,\ldots.
$$

## Binomial series

Consider the function $f(x)=(1+x)^{\alpha}$ with $\alpha\in\mathbb{R}$, then we have

$$
\begin{align*}
&f'(x)=\alpha(1+x)^{\alpha-1},\quad f''(x)=\alpha(\alpha-1)(1+x)^{\alpha-2},\\
&\quad f^{(3)}(x)=\alpha(\alpha-1)(\alpha-2)(1+x)^{\alpha-3},\quad\ldots.
\end{align*}
$$

This implies that $f^{(n)}(0)=\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-n+1)$ for $n=1,2,3,\ldots$. So, if we define the **binomial coefficients**

:::{math}
:label: Eq:Series:BinomialCoefficients

\binom{\alpha}{0}=1,\quad\binom{\alpha}{n}=\frac{\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-n+1)}{n!},\quad n=1,2,3,\ldots,
:::

then we have:

::::::{prf:theorem} Binomial series
:label: Thm:Series:BinomialSeries
If $\alpha\in\mathbb{R}$, then we have

$$
\begin{align*}
(1+x)^{\alpha}&=\sum_{n=0}^{\infty}\binom{\alpha}{n}x^n\\
&=1+\frac{\alpha}{1!}x+\frac{\alpha(\alpha-1)}{2!}x^2+\frac{\alpha(\alpha-1)(\alpha-2)}{3!}x^3+\cdots,\quad|x| < 1.
\end{align*}
$$

This series is called a **binomial series**.
::::::

In order to see that the radius of convergence equals $R=1$ we apply the ratio test: for $x\neq0$ let $a_n=\displaystyle\binom{\alpha}{n}x^n$, then we have:

$$
\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|\binom{\alpha}{n+1}x^{n+1}\bigg/\binom{\alpha}{n}x^n\right|\\
&=\lim\limits_{n\to\infty}\left|\frac{\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-n+1)(\alpha-n)}{\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-n+1)}\frac{n!}{(n+1)!}x\right|\\
&=\lim\limits_{n\to\infty}\left|\frac{\alpha-n}{n+1}x\right|=|x|.
\end{align*}
$$

:::{remark}
Note that the binomial coefficients defined in {eq}`Eq:Series:BinomialCoefficients` generalise the binomial coefficients given in {eq}`Eq:Series:BinomialCoefficient`.
:::

::::{prf:example}
Consider $\displaystyle\sqrt{1+x}=(1+x)^{\frac{1}{2}}=\sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}x^n$ for $|x|<1$. Then we have

$$
\begin{align*}
&\binom{\frac{1}{2}}{0}=1,\quad\binom{\frac{1}{2}}{1}=\frac{1}{2},\quad\binom{\frac{1}{2}}{2}=\frac{\frac{1}{2}\left(\frac{1}{2}-1\right)}{2!}=-\frac{1}{8},\\
&\quad\binom{\frac{1}{2}}{3}=\frac{\frac{1}{2}\left(\frac{1}{2}-1\right)\left(\frac{1}{2}-2\right)}{3!}=\frac{1}{16},\\
&\quad\binom{\frac{1}{2}}{4}=\frac{\frac{1}{2}\left(\frac{1}{2}-1\right)\left(\frac{1}{2}-2\right)\left(\frac{1}{2}-3\right)}{4!}=-\frac{5}{128},\quad\ldots
\end{align*}
$$

and therefore

$$
\begin{align*}
\sqrt{1+x}&=(1+x)^{\frac{1}{2}}=\sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}x^n\\
&=1+\frac{1}{2}x-\frac{1}{8}x^2+\frac{1}{16}x^3-\frac{5}{128}x^4+\cdots,\quad |x|<1.
\end{align*}
$$

::::

::::{prf:example}
Consider $\displaystyle\frac{1}{\sqrt{1+x}}=(1+x)^{-\frac{1}{2}}=\sum_{n=0}^{\infty}\binom{-\frac{1}{2}}{n}x^n$ for $|x|<1$. Then we have

$$
\begin{align*}
&\binom{-\frac{1}{2}}{0}=1,\quad\binom{-\frac{1}{2}}{1}=-\frac{1}{2},\quad\binom{-\frac{1}{2}}{2}=\frac{-\frac{1}{2}\left(-\frac{1}{2}-1\right)}{2!}=\frac{3}{8},\\
&\quad\binom{-\frac{1}{2}}{3}=\frac{-\frac{1}{2}\left(-\frac{1}{2}-1\right)\left(-\frac{1}{2}-2\right)}{3!}=\frac{5}{16},\quad\ldots
\end{align*}
$$

and therefore

$$
\begin{align*}
\frac{1}{\sqrt{1+x}}&=(1+x)^{-\frac{1}{2}}=\sum_{n=0}^{\infty}\binom{-\frac{1}{2}}{n}x^n\\
&=1-\frac{1}{2}x+\frac{3}{8}x^2-\frac{5}{16}x^3+\cdots,\quad |x|<1.
\end{align*}
$$

::::

Replacing $x$ by $-x^2$ in the last example implies that 

$$
\frac{1}{\sqrt{1-x^2}}=\sum_{n=0}^{\infty}(-1)^n\binom{-\frac{1}{2}}{n}x^{2n}=1+\frac{1}{2}x+\frac{3}{8}x^2+\frac{5}{16}x^3+\cdots
$$

for $|-x^2| < 1\;\;\Longleftrightarrow\;\;|x| < 1$. Using integration we obtain

$$
\arcsin(x)=\int\frac{1}{\sqrt{1-x^2}}\,dx=C+\sum_{n=0}^{\infty}(-1)^n\binom{-\frac{1}{2}}{n}\frac{x^{2n+1}}{2n+1},\quad|x| < 1
$$ 
 
and since $\arcsin(0)=0$ we conclude that $C=0$. Similarly, we obtain

$$
\arccos(x)=-\int\frac{1}{\sqrt{1-x^2}}\,dx=K-\sum_{n=0}^{\infty}(-1)^n\binom{-\frac{1}{2}}{n}\frac{x^{2n+1}}{2n+1},\quad|x| <1
$$ 
 
and since $\arccos(0)=\frac{1}{2}\pi$ we conclude that $K=\frac{1}{2}\pi$. Hence we have

$$
\arcsin(x)=\sum_{n=0}^{\infty}(-1)^n\binom{-\frac{1}{2}}{n}\frac{x^{2n+1}}{2n+1},\quad|x| < 1
$$

and

$$
\arccos(x)=\frac{1}{2}\pi-\sum_{n=0}^{\infty}(-1)^n\binom{-\frac{1}{2}}{n}\frac{x^{2n+1}}{2n+1},\quad|x| < 1.
$$ 

::::::{prf:example} Applications
1) Using $\displaystyle\sqrt{1+x^2}=\sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}x^{2n}=1+\frac{1}{2}x^2-\frac{1}{8}x^4+\cdots$ for $|x|<1$ we find that

$$
\lim\limits_{x\to 0}\frac{\sqrt{1+x^2}-1-\frac{1}{2}x^2}{x^4}=\lim\limits_{x\to 0}\frac{1+\frac{1}{2}x^2-\frac{1}{8}x^4+\cdots-1-\frac{1}{2}x^2}{x^4}
=-\frac{1}{8}.
$$

2) Using $\displaystyle\sqrt{1+x^3}=\sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}x^{3n}=1+\frac{1}{2}x^3-\frac{1}{8}x^6+\cdots$ for $|x|<1$ we find that

$$
\begin{align*}
\int_0^{\frac{1}{2}}\sqrt{1+x^3}\,dx&=\sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}\int_0^{\frac{1}{2}}x^{3n}\,dx=\sum_{n=0}^{\infty}\binom{\frac{1}{2}}{n}\frac{(\frac{1}{2})^{3n+1}}{3n+1}\\
&=\frac{1}{2}+\frac{1}{64}-\frac{1}{14680064}+\cdots\approx0.515625.
\end{align*}
$$

::::::
