# Special constants and functions

## Introduction

Series can be used to define special constants and functions. In this section we will consider Catalan's constant and the Riemann zeta function.

(sec:CatalansConstant)=
## Catalan's constant

**Catalan's constant** $G$ is defined as the sum of the series $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}$.

Note that this series is absolutely convergent. However, it is not easy to find its sum. We have

$$
G=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}\approx0.916.
$$

There are several alternative (integral) representations for this constant. Since 

$$
\arctan(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}x^{2n+1}\quad\text{for}\quad |x|<1
$$ 

we have

\begin{align*}
\int_0^1\frac{\arctan(x)}{x}\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}\int_0^1x^{2n}\,dx=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}\cdot\frac{x^{2n+1}}{2n+1}\bigg|_0^1\\
&=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}=G.
\end{align*}
Using $x=e^{-t}$ we obtain

$$
G=\int_0^1\frac{\arctan(x)}{x}\,dx=\int_{\infty}^0\frac{\arctan\left(e^{-t}\right)}{e^{-t}}\,d e^{-t}
=\int_0^{\infty}\arctan\left(e^{-t}\right)\,dt.
$$

The substitution $\arctan{x}=t$ or $x=\tan(t)$ leads to

\begin{align*}
\int_0^1\frac{\arctan(x)}{x}\,dx&=\int_0^{\frac{1}{4}\pi}\frac{t}{\tan(t)}d\tan(t)=\int_0^{\frac{1}{4}\pi}\frac{t}{\tan(t)}\cdot\frac{1}{\cos^2(t)}\,dt\\
&=\int_0^{\frac{1}{4}\pi}\frac{t}{\sin(t)\cos(t)}\,dt.
\end{align*}
This can be rewritten as

$$
G=\int_0^{\frac{1}{4}\pi}\frac{t}{\sin(t)\cos(t)}\,dt=\int_0^{\frac{1}{4}\pi}\frac{2t}{\sin(2t)}\,dt=\frac{1}{2}\int_0^{\frac{1}{2}\pi}\frac{x}{\sin(x)}\,dx.
$$

Using integration by parts we obtain

\begin{align*}
\int_0^1x^n\ln(x)\,dx&=\int_0^1\frac{1}{n+1}\ln(x)\,dx^{n+1}\\
&=\frac{1}{n+1}x^{n+1}\ln(x)\bigg|_0^1-\frac{1}{n+1}\int_0^1x^{n+1}\,d\ln(x)\\
&=0-\frac{1}{n+1}\int_0^1x^n\,dx=-\frac{1}{(n+1)^2}x^{n+1}\bigg|_0^1\\
&=-\frac{1}{(n+1)^2},\quad n=0,1,2,\ldots.
\end{align*}
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

\begin{align*}
G&=\int_1^{\infty}\frac{\ln(t)}{1+t^2}\,dt=\int_0^{\infty}\frac{x}{1+e^{2x}}\cdot e^x\,dx=\int_0^{\infty}\frac{x}{e^{-x}+e^x}\,dx\\
&=\frac{1}{2}\int_0^{\infty}\frac{x}{\cosh(x)}\,dx.
\end{align*}
The relation

$$
\tan^2(\theta)=\frac{\sin^2(\theta)}{\cos^2(\theta)}=\frac{2\sin^2(\theta)}{2\cos^2(\theta)}=\frac{1-\cos(2\theta)}{1+\cos(2\theta)}
$$ 
 
leads to another interesting representation

\begin{align*}
G&=-\int_0^{\frac{1}{4}\pi}\ln\left(\tan(\theta)\right)\,d\theta=-\frac{1}{2}\int_0^{\frac{1}{4}\pi}\ln\left(\tan^2(\theta)\right)\,d\theta\\
&=-\frac{1}{2}\int_0^{\frac{1}{4}\pi}\ln\left(\frac{1-\cos(2\theta)}{1+\cos(2\theta)}\right)\,d\theta,
\end{align*}
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

\begin{align*}
\int_0^{\frac{1}{2}\pi}\ln(\sin(2x))\,dx&=\frac{1}{2}\int_0^{\pi}\ln(\sin(t))\,dt\\
&=\frac{1}{2}\int_0^{\frac{1}{2}\pi}\ln(\sin(t))\,dt+\frac{1}{2}\int_{\frac{1}{2}\pi}^{\pi}\ln(\sin(t))\,dt.
\end{align*}
Then we apply the substitution $t=\pi-x$ to the latter integral to find that

$$ 
\int_{\frac{1}{2}\pi}^{\pi}\ln(\sin(t))\,dt=-\int_{\frac{1}{2}\pi}^0\ln(\sin(\pi-x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx.
$$ 
 
Hence we have $\displaystyle\int_0^{\frac{1}{2}\pi}\ln(\sin(2x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx$. 
 
Finally, we derive for $I=\displaystyle\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(\cos(x))\,dx$ that 

\begin{align*}
I&=\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(\sin(2x))\,dx=\int_0^{\frac{1}{2}\pi}\ln(2\sin(x)\cos(x))\,dx\\
&=\int_0^{\frac{1}{2}\pi}\left(\ln(2)+\ln(\sin(x))+\ln(\cos(x))\right)\,dx\\
&=\int_0^{\frac{1}{2}\pi}\ln(2)\,dx+\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx+\int_0^{\frac{1}{2}\pi}\ln(\cos(x))\,dx=\frac{1}{2}\pi\ln(2)+2I,
\end{align*}
which implies that $I=-\frac{1}{2}\pi\ln(2)$. The substitution $x=\frac{1}{2}\pi-t$ now leads to

$$ 
\int_{\frac{1}{4}\pi}^{\frac{1}{2}\pi}\ln(\sin(x))\,dx=-\int_{\frac{1}{4}\pi}^0\ln(\sin(\tfrac{1}{2}\pi-t)\,dt=\int_0^{\frac{1}{4}\pi}\ln(\cos(t))\,dt
$$

and

$$
\int_{\frac{1}{4}\pi}^{\frac{1}{2}\pi}\ln(\cos(x))\,dx=-\int_{\frac{1}{4}\pi}^0\ln(\cos(\tfrac{1}{2}\pi-t)\,dt=\int_0^{\frac{1}{4}\pi}\ln(\sin(t))\,dt.
$$

Hence we have

\begin{align*}
\int_0^{\frac{1}{4}\pi}\ln(\sin(x))\,dx+\int_0^{\frac{1}{4}\pi}\ln(\cos(x))\,dx&=\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx\\
&=\int_0^{\frac{1}{2}\pi}\ln(\cos(x))\,dx=-\frac{1}{2}\pi\ln(2)
\end{align*}
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

\begin{align*}
\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^s}&=\sum_{n=0}^{\infty}\frac{1}{(2n+1)^s}-\sum_{n=1}^{\infty}\frac{1}{(2n)^s}=\sum_{n=1}^{\infty}\frac{1}{n^s}-2\sum_{n=1}^{\infty}\frac{1}{(2n)^s}\\
&=\left(1-\frac{1}{2^{s-1}}\right)\zeta(s).
\end{align*}
Using integration by parts we find that

\begin{align*}
\int_0^1x^n\ln(x)\,dx&=\frac{1}{n+1}x^{n+1}\ln(x)\bigg|_0^1-\frac{1}{n+1}\int_0^1x^{n+1}\cdot\frac{1}{x}\,dx\\
&=0-\frac{1}{n+1}\int_0^1x^n\,dx=-\frac{1}{(n+1)^2}x^{n+1}\bigg|_0^1\\
&=-\frac{1}{(n+1)^2},\quad n=0,1,2,\ldots.
\end{align*}
Now we use the series representation $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ for $|x|<1$ to find that

\begin{align*}
\int_0^1\frac{\ln(x)}{1-x}\,dt&=\sum_{n=0}^{\infty}\int_0^1x^n\ln(x)\,dx=-\sum_{n=0}^{\infty}\frac{1}{(n+1)^2}=-\sum_{n=1}^{\infty}\frac{1}{n^2}\\
&=-\zeta(2)=-\frac{1}{6}\pi^2.
\end{align*}
Furthermore using integration by parts we find that

\begin{align*}
\int_0^1x^n\left(\ln(x)\right)^2\,dx&=\frac{1}{n+1}x^{n+1}\left(\ln(x)\right)^2\bigg|_0^1-\frac{2}{n+1}\int_0^1x^{n+1}\ln(x)\cdot\frac{1}{x}\,dx\\
&=0-\frac{2}{n+1}\int_0^1x^n\ln(x)\,dx=\frac{2}{(n+1)^3},\quad n=0,1,2,\ldots.
\end{align*}
Again we use the series representation $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ for $|x|<1$ to find that

$$
\int_0^1\frac{\left(\ln(x)\right)^2}{1-x}\,dx=\sum_{n=0}^{\infty}\int_0^1x^n\left(\ln(x)\right)^2\,dx=2\sum_{n=0}^{\infty}\frac{1}{(n+1)^3}
=2\sum_{n=1}^{\infty}\frac{1}{n^3}=2\zeta(3).
$$

Similarly, we have

\begin{align*}
\int_0^1\frac{\ln(x)}{1+x}\,dx&=\sum_{n=0}^{\infty}(-1)^n\int_0^1x^n\ln(x)\,dx=-\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^2}\\
&=-\left(1-\frac{1}{2}\right)\zeta(2)=-\frac{1}{12}\pi^2
\end{align*}
and

\begin{align*}
\int_0^1\frac{\left(\ln(x)\right)^2}{1+x}\,dx&=\sum_{n=0}^{\infty}(-1)^n\int_0^1x^n\left(\ln(x)\right)^2\,dx=2\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^3}\\
&=2\left(1-\frac{1}{4}\right)\zeta(3)=\frac{3}{2}\zeta(3).
\end{align*}
Using the Taylor series $\displaystyle\ln(1-x)=-\sum_{n=1}^{\infty}\frac{x^n}{n}$ for $|x|<1$ we find that

\begin{align*}
\int_0^1\frac{\ln(1-x)}{x}\,dx&=-\sum_{n=1}^{\infty}\frac{1}{n}\int_0^1x^{n-1}\,dx=-\sum_{n=1}^{\infty}\frac{1}{n}\cdot\frac{1}{n}x^n\bigg|_0^1=-\sum_{n=1}^{\infty}\frac{1}{n^2}\\
&=-\zeta(2)=-\frac{1}{6}\pi^2,
\end{align*}
\begin{align*}
\int_0^1\ln(x)\ln(1-x)\,dx&=-\sum_{n=1}^{\infty}\frac{1}{n}\int_0^1x^n\ln(x)\,dx=\sum_{n=1}^{\infty}\frac{1}{n}\cdot\frac{1}{(n+1)^2}\\
&=\sum_{n=1}^{\infty}\left(\frac{1}{n}-\frac{1}{n+1}-\frac{1}{(n+1)^2}\right)=1-\sum_{n=1}^{\infty}\frac{1}{(n+1)^2}\\
&=2-\sum_{n=1}^{\infty}\frac{1}{n^2}=2-\zeta(2)=2-\frac{1}{6}\pi^2
\end{align*}
and

\begin{align*}
\int_0^1\frac{\ln(x)\ln(1-x)}{x}\,dx&=-\sum_{n=1}^{\infty}\frac{1}{n}\int_0^1x^{n-1}\ln(x)\,dx=\sum_{n=1}^{\infty}\frac{1}{n}\cdot\frac{1}{n^2}\\
&=\sum_{n=1}^{\infty}\frac{1}{n^3}=\zeta(3).
\end{align*}
By symmetry (or a substitution) we also have $\displaystyle\int_0^1\frac{\ln(x)\ln(1-x)}{1-x}\,dx=\zeta(3)$ and therefore

$$
\int_0^1\frac{\ln(x)\ln(1-x)}{x(1-x)}\,dx=\int_0^1\frac{\ln(x)\ln(1-x)}{x}\,dx+\int_0^1\frac{\ln(x)\ln(1-x)}{1-x}\,dx=2\zeta(3).
$$

Similarly, using $\displaystyle\ln(1+x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}x^{n+1}$ for $|x|<1$ we have

$$
\int_0^1\frac{\ln(1+x)}{x}\,dx=\sum_{n=0}^{\infty}\int_0^1\frac{(-1)^n}{n+1}x^n\,dx=\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^2}=\left(1-\frac{1}{2}\right)\zeta(2)=\frac{1}{12}\pi^2,
$$

\begin{align*}
\int_0^1\ln(x)\ln(1+x)\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}\int_0^1x^{n+1}\ln(x)\,dx=-\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}\cdot\frac{1}{(n+2)^2}\\
&=\sum_{n=0}^{\infty}\left(\frac{(-1)^n}{n+2}-\frac{(-1)^n}{n+1}+\frac{(-1)^n}{(n+2)^2}\right)\\
&=1-2\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}+\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+2)^2}\\
&=1-2\ln(2)+1-\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^2}\\
&=2-2\ln(2)-\left(1-\frac{1}{2}\right)\zeta(2)=2-2\ln(2)-\frac{1}{12}\pi^2
\end{align*}
and

\begin{align*}
\int_0^1\frac{\ln(x)\ln(1+x)}{x}\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}\int_0^1x^n\ln(x)\,dx=-\sum_{n=1}^{\infty}\frac{(-1)^n}{n+1}\cdot\frac{1}{(n+1)^2}\\
&=-\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^3}=-\left(1-\frac{1}{4}\right)\zeta(3)=-\frac{3}{4}\zeta(3).
\end{align*}