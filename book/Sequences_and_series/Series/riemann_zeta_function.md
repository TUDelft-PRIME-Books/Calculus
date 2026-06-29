# The Riemann zeta function

## Introduction

Series can be used to define special constants and functions. In this section we will consider the Riemann zeta function.

(Sec:Series:RiemannZetaFunction)=
## The Riemann zeta function

The **Riemann zeta function** $\zeta(s)$ is defined as $\displaystyle\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}$ for $\text{Re}(s)>1$.

This function is named after the German mathematician [Georg Friedrich Bernhard Riemann (1826-1866)](https://en.wikipedia.org/wiki/Bernhard_Riemann). 

We will only consider real values of $s$; in that case we know that the series is absolutely convergent if $s>1$. However, in general it is not very easy to find its sum.

In {prf:ref}`Ex:Series:FourierExample3` we have already seen that 

$$
\zeta(2)=\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{1}{6}\pi^2\quad\text{and}\quad\zeta(4)=\sum_{n=1}^{\infty}\frac{1}{n^4}=\frac{1}{90}\pi^4.
$$

The value of $\zeta(3)\approx1.20206$ is also known as **Apéry's constant**, named after the Greek-French mathematician [Roger Apéry (1916-1994)](https://en.wikipedia.org/wiki/Roger_Ap%C3%A9ry).

Note that

$$
\sum_{n=0}^{\infty}\frac{1}{(2n+1)^s}=\sum_{n=1}^{\infty}\frac{1}{n^s}-\sum_{n=1}^{\infty}\frac{1}{(2n)^s}=\left(1-\frac{1}{2^s}\right)\zeta(s)
$$

and

\begin{align*}
\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^s}&=\sum_{n=0}^{\infty}\frac{1}{(2n+1)^s}-\sum_{n=1}^{\infty}\frac{1}{(2n)^s}\\
&=\sum_{n=1}^{\infty}\frac{1}{n^s}-2\sum_{n=1}^{\infty}\frac{1}{(2n)^s}\\
&=\left(1-\frac{1}{2^{s-1}}\right)\zeta(s).
\end{align*}

Using integration by parts we find that

\begin{align*}
\int_0^1x^n\ln(x)\,dx&=\frac{1}{n+1}x^{n+1}\ln(x)\bigg|_0^1-\frac{1}{n+1}\int_0^1x^{n+1}\cdot\frac{1}{x}\,dx\\
&=0-\frac{1}{n+1}\int_0^1x^n\,dx\\
&=-\frac{1}{(n+1)^2}x^{n+1}\bigg|_0^1\\
&=-\frac{1}{(n+1)^2},\quad n=0,1,2,\ldots
\end{align*}

Now we use the series representation $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ for $|x|<1$ to find that

\begin{align*}
\int_0^1\frac{\ln(x)}{1-x}\,dx&=\sum_{n=0}^{\infty}\int_0^1x^n\ln(x)\,dx\\
&=-\sum_{n=0}^{\infty}\frac{1}{(n+1)^2}\\
&=-\sum_{n=1}^{\infty}\frac{1}{n^2}\\
&=-\zeta(2)\\
&=-\frac{1}{6}\pi^2.
\end{align*}

Furthermore using integration by parts we find that

\begin{align*}
\int_0^1x^n\left(\ln(x)\right)^2\,dx&=\frac{1}{n+1}x^{n+1}\left(\ln(x)\right)^2\bigg|_0^1-\frac{2}{n+1}\int_0^1x^{n+1}\ln(x)\cdot\frac{1}{x}\,dx\\
&=0-\frac{2}{n+1}\int_0^1x^n\ln(x)\,dx\\
&=\frac{2}{(n+1)^3},\quad n=0,1,2,\ldots
\end{align*}

Again we use the series representation $\displaystyle\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n$ for $|x|<1$ to find that

$$
\int_0^1\frac{\left(\ln(x)\right)^2}{1-x}\,dx=\sum_{n=0}^{\infty}\int_0^1x^n\left(\ln(x)\right)^2\,dx=2\sum_{n=0}^{\infty}\frac{1}{(n+1)^3}
=2\sum_{n=1}^{\infty}\frac{1}{n^3}=2\zeta(3).
$$

Similarly, we have

\begin{align*}
\int_0^1\frac{\ln(x)}{1+x}\,dx&=\sum_{n=0}^{\infty}(-1)^n\int_0^1x^n\ln(x)\,dx\\
&=-\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^2}\\
&=-\left(1-\frac{1}{2}\right)\zeta(2)\\
&=-\frac{1}{12}\pi^2
\end{align*}

and

\begin{align*}
\int_0^1\frac{\left(\ln(x)\right)^2}{1+x}\,dx&=\sum_{n=0}^{\infty}(-1)^n\int_0^1x^n\left(\ln(x)\right)^2\,dx\\
&=2\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^3}\\
&=2\left(1-\frac{1}{4}\right)\zeta(3)\\
&=\frac{3}{2}\zeta(3).
\end{align*}

Using the Taylor series $\displaystyle\ln(1-x)=-\sum_{n=1}^{\infty}\frac{x^n}{n}$ for $|x|<1$ we find that

\begin{align*}
\int_0^1\frac{\ln(1-x)}{x}\,dx&=-\sum_{n=1}^{\infty}\frac{1}{n}\int_0^1x^{n-1}\,dx\\
&=-\sum_{n=1}^{\infty}\frac{1}{n}\cdot\frac{1}{n}x^n\bigg|_0^1\\
&=-\sum_{n=1}^{\infty}\frac{1}{n^2}\\
&=-\zeta(2)\\
&=-\frac{1}{6}\pi^2,
\end{align*}

\begin{align*}
\int_0^1\ln(x)\ln(1-x)\,dx&=-\sum_{n=1}^{\infty}\frac{1}{n}\int_0^1x^n\ln(x)\,dx\\
&=\sum_{n=1}^{\infty}\frac{1}{n}\cdot\frac{1}{(n+1)^2}\\
&=\sum_{n=1}^{\infty}\left(\frac{1}{n}-\frac{1}{n+1}-\frac{1}{(n+1)^2}\right)\\
&=1-\sum_{n=1}^{\infty}\frac{1}{(n+1)^2}\\
&=2-\sum_{n=1}^{\infty}\frac{1}{n^2}\\
&=2-\zeta(2)\\
&=2-\frac{1}{6}\pi^2
\end{align*}

and

\begin{align*}
\int_0^1\frac{\ln(x)\ln(1-x)}{x}\,dx&=-\sum_{n=1}^{\infty}\frac{1}{n}\int_0^1x^{n-1}\ln(x)\,dx\\
&=\sum_{n=1}^{\infty}\frac{1}{n}\cdot\frac{1}{n^2}\\
&=\sum_{n=1}^{\infty}\frac{1}{n^3}\\
&=\zeta(3).
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
\int_0^1\ln(x)\ln(1+x)\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}\int_0^1x^{n+1}\ln(x)\,dx\\
&=-\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}\cdot\frac{1}{(n+2)^2}\\
&=\sum_{n=0}^{\infty}\left(\frac{(-1)^n}{n+2}-\frac{(-1)^n}{n+1}+\frac{(-1)^n}{(n+2)^2}\right)\\
&=1-2\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}+\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+2)^2}\\
&=1-2\ln(2)+1-\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^2}\\
&=2-2\ln(2)-\left(1-\frac{1}{2}\right)\zeta(2)\\
&=2-2\ln(2)-\frac{1}{12}\pi^2
\end{align*}
and

\begin{align*}
\int_0^1\frac{\ln(x)\ln(1+x)}{x}\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}\int_0^1x^n\ln(x)\,dx\\
&=-\sum_{n=1}^{\infty}\frac{(-1)^n}{n+1}\cdot\frac{1}{(n+1)^2}\\
&=-\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)^3}\\
&=-\left(1-\frac{1}{4}\right)\zeta(3)\\
&=-\frac{3}{4}\zeta(3).
\end{align*}
