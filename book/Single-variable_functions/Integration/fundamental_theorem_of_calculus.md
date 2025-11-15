# Fundamental theorem of calculus

In this section we cover

- Fundamental theorem of calculus

In this section we explain the relation between definite and indefinite integrals. The connection is given by the **fundamental theorem of calculus**, which consists of two parts.

**The fundamental theorem of calculus (part 1)**

::::::{prf:Theorem} The fundamental theorem of calculus, part 1
:label: Thm:Integration:FundamentalTheoremPart1
If $f$ is continuous on the interval $[a,b]$, then the function $g(x)$ defined by

$$
g(x)=\int_a^xf(t)\,dt,\quad a\leq x\leq b
$$

is continuous on $[a,b]$ and differentiable on $(a,b)$, and $g'(x)=f(x)$.
::::::

::::::{prf:Proof}
Using the definition of the derivative, we obtain

$$
\begin{align*}
g'(x)&=\lim_{h\to 0}\frac{g(x+h)-g(x)}{h}=\lim_{h\to 0}\frac{1}{h}\left(\int_a^{x+h}f(t)\,dt-\int_a^xf(t)\,dt\right)\\
&=\lim_{h\to 0}\frac{1}{h}\int_x^{x+h}f(t)\,dt=\lim_{h\to 0}\frac{1}{h}\cdot hf(c)
\end{align*}
$$

for a certain value $c$ between $x$ and $x+h$. Then we have

$$
g'(x)=\lim_{c\to x}f(c)=f(x),
$$

since $f$ is continuous.
::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart1Example1
Find $\displaystyle\frac{d}{dx}\int_0^xe^{t^2}\,dt$.

Solution. We need not to evaluate the integral, which would be impossible. However, application of the fundamental theorem of calculus leads to the immediate answer 

$$
\frac{d}{dx}\int_0^xe^{t^2}\,dt=e^{x^2}.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart1Example2
Find $\displaystyle\frac{d}{dx}\int_0^{\sqrt{x}}\cos(t^2)\,dt$ for $x>0$.

Solution. Now we need to apply the chain rule:

$$
\frac{d}{dx}\int_0^{\sqrt{x}}\cos(t^2)\,dt=\sin\left((\sqrt{x})^2\right)\cdot\frac{d}{dx}(\sqrt{x})=\sin(x)\cdot\frac{1}{2\sqrt{x}}=\frac{\sin(x)}{2\sqrt{x}}.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart1Example3
Find $\displaystyle\frac{d}{dx}\int_x^{x^2}\ln(1+t^2)\,dt$.

Solution. Now we have:

$$
\begin{align*}
\frac{d}{dx}\int_x^{x^2}\ln(1+t^2)\,dt&=\frac{d}{dx}\left(\int_0^{x^2}\ln(1+t^2)\,dt-\int_0^x\ln(1+t^2)\,dt\right)\\
&=\ln\left(1+\left(x^2\right)^2\right)\cdot\frac{d}{dx}(x^2)-\ln(1+x^2)=2x\ln(1+x^4)-\ln(1+x^2).
\end{align*}
$$

::::::

**The fundamental theorem of calculus (part 2)**

::::::{prf:Theorem} The fundamental theorem of calculus, part 2
:label: Thm:Integration:FundamentalTheoremPart2
If $f$ is continuous on the interval $[a,b]$, then

$$
\int_a^bf(x)\,dx=F(b)-F(a),
$$

where $F$ is any antiderivative of $f$, that is, a function such that $F'=f$.
::::::

::::::{prf:Proof}
Let $g(x)=\displaystyle\int_a^xf(t)\,dt$. Then part 1 implies that $g'(x)=f(x)$. Hence, $g$ is an antiderivative of $f$.
So, if $F$ is any antiderivative of $f$ we have: $F(x)=g(x)+C$ for $a<x<b$. However, since $F$ and $g$ are both continuous
on $[a,b]$ we conclude that $F(x)=g(x)+C$ for all $x$ in $[a,b]$.

For $x=a$ we obtain: $g(a)=\displaystyle\int_a^af(t)\,dt=0$ and therefore

$$
F(b)-F(a)=g(b)+C-g(a)-C=g(b)-g(a)=g(b)=\int_a^bf(t)\,dt.
$$

::::::

::::::{prf:Notation}
During evaluations of integrals we often use the notation

$$
\int_a^bf(x)\,dx=\bigg[F(x)\bigg]_a^b=F(b)-F(a)\quad\text{or}\quad\int_a^bf(x)\,dx=F(x)\bigg|_a^b=F(b)-F(a).
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart2Example1
```{figure} Images/sine_area.png
---
width: 50%
name: area under one arc of the sine function
align: center
---
The integral $\displaystyle\int_0^{\pi}\sin(x)\,dx$
```

$$
\int_0^{\pi}\sin(x)\,dx=-\cos(x)\bigg|_0^{\pi}=-\cos(\pi)+\cos(0)=-(-1)+1=2.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart2Example2

$$
\int_1^e\frac{1}{x}\,dx=\ln(x)\bigg|_1^e=\ln(e)-\ln(1)=1-0=1.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremPart2Example3

$$
\int_0^{\frac{1}{4}\pi}\frac{1}{1+x^2}\,dx=\bigg[\arctan(x)\bigg]_0^{\frac{1}{4}\pi}=\arctan(\tfrac{1}{4}\pi)-\arctan(0)=1-0=1.
$$

::::::

So, in order to evaluate a definite integral we just need to find any antiderivative of the integrand. However, it is not always easy to find such an antiderivative. In the next sections we will cover some methods which can be used to evaluate integrals of certain types.

However, in some applications functions appear, which are defined in terms of an integral that cannot be evaluated. Even though the integrand is continuous and an antiderivative exists, it is sometimes impossible to write this in terms of standard functions. In the examples below we deal with some of these functions. Although the integral cannot be evaluated, the fundamental theorem of calculus can be used to find properties of the function.

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremErrorFucntion
In probability and statistics the **error function** $\text{erf}(x)=\displaystyle\frac{2}{\sqrt{\pi}}\int_0^xe^{-t^2}\,dt$ with $x\geq0$ appears. Although it turns out that it is difficult to evaluate this integral, we have: $\text{erf}'(x)=\displaystyle\frac{2}{\sqrt{\pi}}e^{-x^2}>0$, which implies that the function is increasing. Furthermore, $\text{erf}(0)=0$ and $\lim\limits_{x\to\infty}\text{erf}'(x)=0$. Later we will see that $\lim\limits_{x\to\infty}\text{erf}(x)=1$. The graph of $\text{erf}(x)$ for $x\geq0$ is given below:
```{figure} Images/error_function.png
---
width: 50%
name: error function
align: center
---
Graph of $\text{erf}(x)$ for $x\geq0$
```
Dit plaatje vervangen door een plaatje van de grafiek van $\text{erf}(x)$ voor $x\geq0$.
::::::

::::::{prf:Example}
:label: Ex:Integration:FundamentalTheoremFresnelIntegrals
In optics the **Fresnel integrals** $C(x)=\displaystyle\int_0^x\cos\left(\frac{1}{2}\pi t^2\right)\,dt$ and $S(x)=\displaystyle\int_0^x\sin\left(\frac{1}{2}\pi t^2\right)\,dt$ for $x\geq0$ appear, which are also difficult to evaluate. These integrals are named after the French civil engineer and physicist [Augustin Jean Fresnel (1788-1827)](https://en.wikipedia.org/wiki/Augustin-Jean_Fresnel).

However we have: $C'(x)=\displaystyle\cos\left(\frac{1}{2}\pi x^2\right)$ and $S'(x)=\displaystyle\sin\left(\frac{1}{2}\pi x^2\right)$.

So, for instance, we have: 

$$
C'(x)=0\quad\Longleftrightarrow\quad\frac{1}{2}\pi x^2=\frac{(2k+1)\pi}{2}\quad\text{with}\quad k=0,1,2,\ldots.
$$

Hence, $C'(x)=0$ for $x=\sqrt{2k+1}$ with $k=0,1,2,\ldots$.

Similarly, we have: 

$$
S'(x)=0\quad\Longleftrightarrow\quad\frac{1}{2}\pi x^2=k\pi\quad\text{with}\quad k=0,1,2,\ldots.
$$

Hence, $S'(x)=0$ for $x=\sqrt{2k}$ with $k=0,1,2,\ldots$. 
```{figure} Images/fresnel.png
---
width: 50%
name: fresnel functions
align: center
---
Graphs of $C(x)$ and $S(x)$ for $0\leq x\leq4$
```
::::::

::::{exercise}
:label: Exc:Integration:FundamentalTheoremTrigIntegrals
Consider the integrals $\displaystyle\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx$ and $\displaystyle\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx$

(a) Use the double-angle formula $\cos(2x)=\cos^2(x)-\sin^2(x)$ to show that both integrals are equal.

(b) Use the Pythagorean identity $\cos^2(x)+\sin^2(x)=1$ to prove that

$$
\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx=\tfrac{1}{4}\pi=\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx.
$$

::::

:::{admonition} Solution of {numref}`Exc:Integration:FundamentalTheoremTrigIntegrals`
:class: solution, dropdown

(a) Using $\cos(2x)=\cos^2(x)-\sin^2(x)$ we find that

$$
\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx-\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx=\int_0^{\frac{1}{2}\pi}\cos(2x)\,dx=\frac{1}{2}\sin(2x)\bigg|_0^{\frac{1}{2}\pi}=0,
$$

which implies that $\displaystyle\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx=\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx$.

(b) Using $\cos^2(x)+\sin^2(x)=1$ we find that

$$
\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx+\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx=\int_0^{\frac{1}{2}\pi}1\,dx=\tfrac{1}{2}\pi.
$$

We conclude that

$$
\int_0^{\frac{1}{2}\pi}\cos^2(x)\,dx=\tfrac{1}{4}\pi=\int_0^{\frac{1}{2}\pi}\sin^2(x)\,dx.
$$

:::

## Grasple exercises

66942, 66940, 67076, 67078, 67075, 67081, 67079, 67073, 67072, 63704, 76779, 71414, 76784