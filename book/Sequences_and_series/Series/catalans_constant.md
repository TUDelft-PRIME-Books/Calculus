# Catalan's constant

## Introduction

Series can be used to define special constants and functions. In this section we will consider Catalan's constant.

(Sec:CatalansConstant)=
## Catalan's constant

**Catalan's constant** $G$, named after the French and Belgian mathematician [Eugène Charles Catalan (1814-1894)](https://en.wikipedia.org/wiki/Eug%C3%A8ne_Charles_Catalan), is defined as the sum of the series $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}$.

Note that this series is absolutely convergent. However, it is not easy to find its sum. We have

$$
G=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}\approx0.91597.
$$

Catalan's constant surprisingly appears in various branches of mathematics, such as number theory, analysis, geometry and combinatorics.

There are several alternative (integral) representations for this constant. Since 

$$
\arctan(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}x^{2n+1}\quad\text{for}\quad |x|<1
$$ 

we have

\begin{align*}
\int_0^1\frac{\arctan(x)}{x}\,dx&=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}\int_0^1x^{2n}\,dx\\
&=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}\cdot\frac{x^{2n+1}}{2n+1}\bigg|_0^1\\
&=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}\\
&=G.
\end{align*}

Using the substitution $x=e^{-t}$ and therefore $dx=-e^{-t}\,dt$ we obtain

$$
G=\int_0^1\frac{\arctan(x)}{x}\,dx=-\int_{\infty}^0\frac{\arctan\left(e^{-t}\right)}{e^{-t}}e^{-t}\,dt=\int_0^{\infty}\arctan\left(e^{-t}\right)\,dt.
$$

The substitution $\arctan(x)=t$ or $x=\tan(t)$ and therefore $dx=\dfrac{1}{\cos^2(t)}\,dt$ leads to

$$
\int_0^1\frac{\arctan(x)}{x}\,dx=\int_0^{\frac{1}{4}\pi}\frac{t}{\tan(t)}\cdot\frac{1}{\cos^2(t)}\,dt=\int_0^{\frac{1}{4}\pi}\frac{t}{\sin(t)\cos(t)}\,dt.
$$

This can be rewritten as

$$
G=\int_0^{\frac{1}{4}\pi}\frac{t}{\sin(t)\cos(t)}\,dt=\int_0^{\frac{1}{4}\pi}\frac{2t}{\sin(2t)}\,dt=\frac{1}{2}\int_0^{\frac{1}{2}\pi}\frac{x}{\sin(x)}\,dx.
$$

Using integration by parts we obtain

\begin{align*}
\int_0^1x^n\ln(x)\,dx&=\frac{1}{n+1}x^{n+1}\ln(x)\bigg|_0^1-\frac{1}{n+1}\int_0^1x^{n+1}\cdot\frac{1}{x}\,dx\\
&=0-\frac{1}{n+1}\int_0^1x^n\,dx\\
&=-\frac{1}{(n+1)^2}x^{n+1}\bigg|_0^1\\
&=-\frac{1}{(n+1)^2},\quad n=0,1,2,\ldots
\end{align*}

With $\displaystyle\frac{1}{1+x^2}=\sum_{n=0}^{\infty}(-x^2)^n=\sum_{n=0}^{\infty}(-1)^nx^{2n}$ for $|x|<1$ this implies that

$$
\int_0^1\frac{\ln(x)}{1+x^2}\,dx=\sum_{n=0}^{\infty}(-1)^n\int_0^1x^{2n}\ln(x)\,dx=-\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}=-G.
$$

Using the substitution $x=\dfrac{1}{t}$ we obtain

$$
G=-\int_0^1\frac{\ln(x)}{1+x^2}\,dx=-\int_{\infty}^1\frac{\ln\left(\frac{1}{t}\right)}{1+\left(\frac{1}{t}\right)^2}\cdot\left(-\frac{1}{t^2}\right)\,dt=\int_1^{\infty}\frac{\ln(t)}{1+t^2}\,dt.
$$

In {numref}`Grasple:133530` we proved that $\displaystyle\int_0^{\infty}\frac{\ln(x)}{1+x^2}\,dx=0$ by showing that

$$
-\int_0^1\frac{\ln(x)}{1+x^2}\,dx=\int_1^{\infty}\frac{\ln(x)}{1+x^2}\,dx.
$$

Now we see that both integrals equal Catalan's constant $G$.

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
 
Setting $\ln(t)=x$ or $t=e^x$ and using {prf:ref}`Def:PropertiesFunctions:Hyperbolic` we obtain

$$
G=\int_1^{\infty}\frac{\ln(t)}{1+t^2}\,dt=\int_0^{\infty}\frac{x}{1+e^{2x}}e^x\,dx=\int_0^{\infty}\frac{x}{e^{-x}+e^x}\,dx=\frac{1}{2}\int_0^{\infty}\frac{x}{\cosh(x)}\,dx.
$$

The relation

$$
\tan^2(\theta)=\frac{\sin^2(\theta)}{\cos^2(\theta)}=\frac{2\sin^2(\theta)}{2\cos^2(\theta)}=\frac{1-\cos(2\theta)}{1+\cos(2\theta)}
$$ 
 
leads to another interesting representation

\begin{align*}
G&=-\int_0^{\frac{1}{4}\pi}\ln\left(\tan(\theta)\right)\,d\theta\\
&=-\frac{1}{2}\int_0^{\frac{1}{4}\pi}\ln\left(\tan^2(\theta)\right)\,d\theta\\
&=-\frac{1}{2}\int_0^{\frac{1}{4}\pi}\ln\left(\frac{1-\cos(2\theta)}{1+\cos(2\theta)}\right)\,d\theta,
\end{align*}

which is equivalent to

$$
G=-\frac{1}{4}\int_0^{\frac{1}{2}\pi}\ln\left(\frac{1-\cos(x)}{1+\cos(x)}\right)\,dx\quad\text{or}\quad
G=\frac{1}{4}\int_0^{\frac{1}{2}\pi}\ln\left(\frac{1+\cos(x)}{1-\cos(x)}\right)\,dx.
$$ 
 
When we studied Serret's integral in {prf:ref}`Ex:Integration:SubstitutionTrigSerretsIntegral` we used the fact that 

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
I&=\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx\\
&=\int_0^{\frac{1}{2}\pi}\ln(\sin(2x))\,dx\\
&=\int_0^{\frac{1}{2}\pi}\ln(2\sin(x)\cos(x))\,dx\\
&=\int_0^{\frac{1}{2}\pi}\left(\ln(2)+\ln(\sin(x))+\ln(\cos(x))\right)\,dx\\
&=\int_0^{\frac{1}{2}\pi}\ln(2)\,dx+\int_0^{\frac{1}{2}\pi}\ln(\sin(x))\,dx+\int_0^{\frac{1}{2}\pi}\ln(\cos(x))\,dx\\
&=\frac{1}{2}\pi\ln(2)+2I,
\end{align*}

which implies that $I=-\dfrac{1}{2}\pi\ln(2)$. The substitution $x=\dfrac{1}{2}\pi-t$ now leads to

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
&=\int_0^{\frac{1}{2}\pi}\ln(\cos(x))\,dx\\
&=-\frac{1}{2}\pi\ln(2)
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

## Connecting to other functions

The **Dirichlet beta function** $\beta(s)$ is defined as $\displaystyle\beta(s)=\sum_{n=0}^{|infty}\frac{(1-1)^n}{(2n+1)^s} for $\text{Re}(s)>0$. This function is closely related to the *Riemann zeta* (see: {numref}`Sec:Series:RiemannZetaFunction`).

This function is named after the German mathematician [Johann Peter Gustav Lejeune Dirichlet (1805-1859)](https://en.wikipedia.org/wiki/Peter_Gustav_Lejeune_Dirichlet).

We will only consider real values of $s$; in that case we know that the series is absolutely convergent if $s>1$. Furthermore, for $0<s\leq1$ it is conditionally convergent because of the alternative series test. However, in general it is not very easy to find its sum.

In {prf:ref}`Ex:Series:Arctan` we have seen the *Leibniz formula* for $\pi$, which reads

$$
\beta(1)=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}=1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\cdots=\frac{1}{4}\pi.
$$

Furthermore, the definition of Catalan's constant implies that $\beta(2)=G$.