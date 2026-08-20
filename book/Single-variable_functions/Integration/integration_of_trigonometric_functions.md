(Sec:Integration:TrigonometricFunctions)=

# Integration of trigonometric functions

## Introduction

In this section we will see how to evaluate integrals, both definite and indefinite, for which the integrand consists of trigonometric functions only (except possibly for an additive constant). We will start with integrating the trigonometric functions and then we will use these integrals to evaluate more complicated integrals.

## Integrals of simple trigonometric functions

In {numref}`Sec:Integration:IndefiniteIntegrals`, and more specifically in {numref}`Tab:Integration:StandardIndefiniteIntegrals`, we already encountered some indefinite integrals involving trigonometric functions.

We have already seen that

$$
\int\sin(x)\,dx=-\cos(x)+C\quad\text{and}\quad\int\cos(x)\,dx=\sin(x)+C.
$$

For the tangent we use the substitution $u=\cos(x)$ and therefore $du=-\sin(x)\,dx$ to obtain

$$
\int\tan(x)\,dx=\int\frac{\sin(x)}{\cos(x)}\,dx=-\int\frac{du}{u}=-\ln|u|+C=-\ln|\cos(x)|+C.
$$

Similarly, the substitution $u=\sin(x)$ and therefore $du=\cos(x)\,dx$ leads to

$$
\int\frac{1}{\tan(x)}\,dx=\int\frac{\cos(x)}{\sin(x)}\,dx=\int\frac{du}{u}=\ln|u|+C=\ln|\sin(x)|+C.
$$

We can also integrate the reciprocal of the sine. For this we need the {prf:ref}`Pythagorean identity <Thm:Trigonometry:UnitCircleIdentity>` $\sin^2(x)+\cos^2(x)=1$ and the substitution $u=\cos(x)$:

\begin{align*}
\int\frac{1}{\sin(x)}\,dx &= \int\frac{\sin(x)}{\sin^2(x)}\,dx \\
&= \int\frac{\sin(x)}{1-\cos^2(x)}\,dx \\
&= \int\frac{1}{u^2-1}\,du \\
&= \int\frac{1}{(u-1)(u+1)}\,du \\
&= \int\left(\frac12\frac1{u-1}-\frac12\frac{1}{u+1}\right)\,du \\
&= \frac{1}{2}\ln|u-1|-\frac{1}{2}\ln|u+1|+C \\
&= \frac{1}{2}\ln\left|\frac{u-1}{u+1}\right|+C \\
&= \frac{1}{2}\ln\left|\frac{\cos(x)-1}{\cos(x)+1}\right|+C.
\end{align*}

Similarly, we can integrate the reciprocal of the cosine. Using the substitution $u=\sin(x)$ we find that

$$
\int\frac{1}{\cos(x)}\,dx = \frac{1}{2}\ln\left|\frac{1+\sin(x)}{1-\sin(x)}\right|+C.
$$

Instead of integrating the (reciprocals of the) sine, cosine and tangent, we can also differentiate them and using the concept of antiderivatives from {numref}`Sec:Integration:IndefiniteIntegrals` we can evaluate the integrals. For example, since $\displaystyle\frac{d}{dx}\tan(x)=\frac{1}{\cos^2(x)}=1+\tan^2(x)$ we have

$$
\int\frac{1}{\cos^2(x)}\,dx=\int\left(1+\tan^2(x)\right)\,dx=\tan(x)+C.
$$

The sine and cosine do not really give new results, but the reciprocal of the sine, cosine and tangent do, for which you can find the result (and all others until now) in {numref}`Tab:Integration:TrigonometricIndefiniteIntegrals`.

```{table} Indefinite integrals involving (reciprocal) trigonometric functions.
:widths: auto
:align: center
:class: mid-align center-align
:name: Tab:Integration:TrigonometricIndefiniteIntegrals

| Indefinite integral | Remark |
|---|---|
| $\displaystyle \int \sin(x) \,dx= -\cos(x)+C$| |
| $\displaystyle \int \cos(x) \,dx= \sin(x)+C$ | |
| $\displaystyle \int \tan(x) \,dx= -\ln\lvert\cos(x)\rvert+C$ | |
| $\displaystyle \int \frac{1}{\sin(x)} \,dx= \frac{1}{2}\ln\left\lvert\frac{\cos(x)-1}{\cos(x)+1}\right\rvert+C$ | |
| $\displaystyle \int \frac{1}{\cos(x)} \,dx= \frac{1}{2}\ln\left\lvert\frac{1+\sin(x)}{1-\sin(x)}\right\rvert+C$ | |
| $\displaystyle \int \frac{1}{\tan(x)} \,dx= \ln\lvert\sin(x)\rvert+C$ | |
| $\displaystyle \int \frac{1}{\cos^2(x)} \,dx= \tan(x)+C$| $\displaystyle \frac{1}{\cos^2(x)}=1+\tan^2(x)$ |
| $\displaystyle \int \frac{1}{\sin(x)\tan(x)} \,dx= \frac{1}{\sin(x)}+C$ | $\displaystyle\frac{1}{\sin(x)\tan(x)}=\frac{\cos(x)}{\sin^2(x)}$ |
| $\displaystyle \int \frac{\tan(x)}{\cos(x)} \,dx= \frac{1}{\cos(x)}+C$ | $\displaystyle\frac{\tan(x)}{\cos(x)}=\frac{\sin(x)}{\cos^2(x)}$ |
| $\displaystyle \int \frac{-1}{\sin^2(x)} \,dx= \frac{1}{\tan(x)}+C$ | $\displaystyle\frac{-1}{\sin^2(x)}=-1-\frac{1}{\tan^2(x)}$ |

```

In {prf:ref}`Thm:Integration:GregoryIntegralCos` we have seen that

$$
\int\frac{dx}{\cos(x)}=\ln\left|\tan(x)+\frac{1}{\cos(x)}\right|+C.
$$

This formula was discovered in 1668 by the Scottish mathematician [James Gregory (1638-1675)](https://en.wikipedia.org/wiki/James_Gregory_(mathematician)). Similarly, we have


:::{prf:theorem}
:label: Thm:Integration:GregoryIntegralSin

$$
\int\frac{dx}{\sin(x)}=-\ln\left|\frac{\cos(x)}{\sin(x)}+\frac{1}{\sin(x)}\right|+C.
$$

:::

The proof is also similar:

:::{admonition} Proof of {prf:ref}`Thm:Integration:GregoryIntegralSin`
:class: dropdown, tudproof

$$
\int\frac{dx}{\sin(x)}=\int\frac{1}{\sin(x)}\cdot\frac{\dfrac{\cos(x)}{\sin(x)}+\dfrac{1}{\sin(x)}}{\dfrac{\cos(x)}{\sin(x)}+\dfrac{1}{\sin(x)}}\,dx=\int\frac{\dfrac{\cos(x)}{\sin^2(x)}+\dfrac{1}{\sin^2(x)}}{\dfrac{\cos(x)}{\sin(x)}+\dfrac{1}{\sin(x)}}\,dx.
$$

Now we set $u=\dfrac{\cos(x)}{\sin(x)}+\dfrac{1}{\sin(x)}$ which implies that

$$
\frac{du}{dx}=\frac{-\sin^2(x)-\cos^2(x)}{\sin^2(x)}-\frac{1}{\sin^2(x)}\cdot\cos(x)=-\frac{1}{\sin^2(x)}-\frac{\cos(x)}{\sin^2(x)}.
$$

Hence we have $du=-\left(\dfrac{1}{\sin^2(x)}+\dfrac{\cos(x)}{\sin^2(x)}\right)\,dx$. Thus

$$
\int\frac{dx}{\sin(x)}=-\int\frac{du}{u}=-\ln|u|+C=-\ln\left|\frac{\cos(x)}{\sin(x)}+\frac{1}{\sin(x)}\right|+C.
$$

Note that this can also be written as:

$$
\int\frac{dx}{\sin(x)}=-\ln\left|\frac{1+\cos(x)}{\sin(x)}\right|+C=\ln\left|\frac{1-\cos(x)}{\sin(x)}\right|+C.
$$

:::

As you may notice, the definite integral of a reciprocal of the (co)sine has several different forms. We want to stress that each of these forms are mathematically correct and that they are all equivalent. Using the tangent half-angle substitution in {numref}`sec:Integration:HalfAngle` we will derive yet other forms for these integrals.

## Products of trigonometric functions

We consider integrals of the form $\displaystyle\int\sin^m(x)\cos^n(x)\,dx$ for integer values of $m$ and $n$. If (at least) one of these integers is odd, we can use a substitution and the {prf:ref}`Pythagorean identity <Thm:Trigonometry:UnitCircleIdentity>`.

If $m=2k+1$ with $k\in\{0,1,2,\ldots\}$, so $m$ is odd, then we have using the substitution $u=\cos(x)$

\begin{align*}
\int\sin^{2k+1}(x)\cos^n(x)\,dx &= \int\left(\sin^{2}(x)\right)^k\cos^n(x)\sin(x)\,dx \\
&= \int\left(1-\cos^{2}(x)\right)^k\cos^n(x)\sin(x)\,dx \\
&= -\int\left(1-u^2\right)^ku^n\,du.
\end{align*}

If $n=2k+1$ with $k\in\{0,1,2,\ldots\}$, so $n$ is odd, then we have using the substitution $u=\sin(x)$

\begin{align*}
\int\sin^m(x)\cos^{2k+1}(x)\,dx &= \int \sin^m(x)\left(\cos^{2}(x)\right)^k\cos(x)\,dx \\
&= \int \sin^m(x)\left(1-\sin^{2}(x)\right)^k\cos(x)\,dx \\
&= \int u^m\left(1-u^2\right)^k\,du.
\end{align*}

In both cases we end up with an integral of a polynomial, which can be directly evaluated. If both powers are odd, both methods will work.

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerOddSinEvenCos
Consider $\displaystyle\int\sin^3(x)\cos^2(x)\,dx$.

Using $u=\cos(x)$ we obtain

\begin{align*}
\int\sin^3(x)\cos^2(x)\,dx &=-\int(1-u^2)u^2\,du \\
&=-\int\left(u^2-u^4\right)\,du\\
&=-\frac{1}{3}u^3+\frac{1}{5}u^5+C\\
&=-\frac{1}{3}\cos^3(x)+\frac{1}{5}\cos^5(x)+C.
\end{align*}

::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerEvenSinOddCos
Let us evaluate $\displaystyle\int\sin^4(x)\cos^3(x)\,dx$.

Using $u=\sin(x)$ we obtain

\begin{align*}
\int\sin^4(x)\cos^3(x)\,dx 
&=\int u^4(1-u^2)\,du \\
&=\int\left(u^4-u^6\right)\,du\\
&=\frac{1}{5}u^5-\frac{1}{7}u^7+C\\
&=\frac{1}{5}\sin^5(x)-\frac{1}{7}\sin^7(x)+C.
\end{align*}

::::::

If both powers are even, it is more difficult. We may use the half-angle formulas (see: {prf:ref}`Thm:Trigonometry:HalfAngleFormulas`) and sometimes $\sin(x)\cos(x)=\frac{1}{2}\sin(2x)$ might help.

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerEvenSinOddCos2
Consider $\displaystyle\int\sin^2(x)\cos^4(x)\,dx$.

Using $\sin(x)\cos(x)=\frac{1}{2}\sin(2x)$ and $\cos^2(x)=\frac{1}{2}(1+\cos(2x))$ we have

\begin{align*}
\int\sin^2(x)\cos^4(x)\,dx&=\frac{1}{8}\int\sin^2(2x)(1+\cos(2x))\,dx\\
&=\frac{1}{8}\int\sin^2(2x)\,dx+\frac{1}{8}\int\sin^2(2x)\cos(2x)\,dx.
\end{align*}

Now we might use $\sin^2(2x)=\frac{1}{2}(1-\cos(4x))$ to obtain

$$
\int\sin^2(2x)\,dx=\frac{1}{2}\int(1-\cos(4x))\,dx=\frac{1}{2}x-\frac{1}{8}\sin(2x)+C_1.
$$

Using the substitution $u=\sin(2x)$ we find that

\begin{align*}
\int\sin^2(2x)\cos(2x)\,dx &= \frac{1}{2}\int u^2\,du\\
&=\frac{1}{6}u^3+C_2\\
&=\frac{1}{6}\sin^3(2x)+C_2.
\end{align*}

Finally, we conclude that

$$
\int\sin^2(x)\cos^4(x)\,dx=\frac{1}{16}x-\frac{1}{64}\sin(2x)+\frac{1}{48}\sin^3(2x)+C.
$$

::::::

Sometimes, these techniques also work in case of quotients instead of products.

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerNegative1
We evaluate the indefinite integral of $\displaystyle\frac{\cos(x)}{\sin^2(x)}$.

Using $u=\sin(x)$ we obtain

$$
\int\frac{\cos(x)}{\sin^2(x)}\,dx=\int\frac{du}{u^2}=-\frac{1}{u}+C=-\frac{1}{\sin(x)}+C.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerNegative2
Another indefinite integral with a fraction we can do is $\displaystyle\int\frac{\sin^3(x)}{\cos^4(x)}\,dx$.

Using $u=\cos(x)$ we obtain

\begin{align*}
\int\frac{\sin^3(x)}{\cos^4(x)}\,dx&=-\int\frac{1-u^2}{u^4}\,du\\
&=-\int\left(\frac{1}{u^4}-\frac{1}{u^2}\right)\,du \\
&=\frac{1}{3u^3}-\frac{1}{u}+C\\
&=\frac{1}{3\cos^3(x)}-\frac{1}{\cos(x)}+C.
\end{align*}
::::::

Again, when both powers are even it is more difficult. However, there are some exceptions such as in the following examples.

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerNegative3
Consider $\displaystyle\int\frac{\sin^2(x)}{\cos^4(x)}\,dx$.

Since $\displaystyle\frac{d}{dx}\tan(x)=\frac{1}{\cos^2(x)}$ we use $u=\tan(x)$ to obtain

\begin{align*}
\int\frac{\sin^2(x)}{\cos^4(x)}\,dx &= \int\frac{\sin^2(x)}{\cos^2(x)}\frac{1}{\cos^2(x)}\,dx \\
&=\int\tan^2(x)\frac{1}{\cos^2(x)}\,dx \\
&=\int u^2\,du\\
&=\frac{1}{3}u^3+C\\
&=\frac{1}{3}\tan^3(x)+C.
\end{align*}
::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerNegative4
We evaluate $\displaystyle\int\frac{\cos^2(x)}{\sin^4(x)}\,dx$.

Since $\displaystyle\frac{d}{dx}\left(\frac{1}{\tan(x)}\right)=-\frac{1}{\sin^2(x)}$ we use $u=\dfrac{1}{\tan(x)}$ to obtain

\begin{align*}
\int\frac{\cos^2(x)}{\sin^4(x)}\,dx &= \int\frac{\cos^2(x)}{\sin^2(x)}\frac{1}{\sin^2(x)}\,dx \\
&= \int\frac{1}{\tan^2(x)}\frac{1}{\sin^2(x)}\,dx \\
&=-\int u^2\,du\\
&=-\frac{1}{3}u^3+C \\
&=-\frac{1}{3}\frac{\cos^3(x)}{\sin^3(x)}+C.
\end{align*}
::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerNegative5
We now evaluate $\displaystyle\int\frac{\sin^2(x)}{\cos^6(x)}\,dx$.

Since $\displaystyle\frac{d}{dx}\tan(x)=\frac{1}{\cos^2(x)}=1+\tan^2(x)$ we use $u=\tan(x)$ to obtain

\begin{align*}
\int\frac{\sin^2(x)}{\cos^6(x)}\,dx &= \int\frac{\sin^2(x)}{\cos^2(x)}\frac{1}{\cos^2(x)}\frac{1}{\cos^2(x)}\,dx \\
&= \int\tan^2(x)\left(1+\tan^2(x)\right)\frac{1}{\cos^2(x)}\,dx \\
&=\int u^2(1+u^2)\,du\\
&=\frac{1}{3}u^3+\frac{1}{5}u^5+C \\
&=\frac{1}{3}\tan^3(x)+\frac{1}{5}\tan^5(x)+C.
\end{align*}
::::::

For integrals of the form $\displaystyle\int\sin(ax)\cos(bx)\,dx$, $\displaystyle\int\cos(ax)\cos(bx)\,dx$ and $\displaystyle\int\sin(ax)\sin(bx)\,dx$ we use the product formulas (see: {prf:ref}`Thm:Trigonometry:ProductFormulas`) to find

$$
\int\sin(ax)\cos(bx)\,dx=\frac{1}{2}\int(\sin((a-b)x)+\sin(a+b)x)\,dx,
$$

$$
\int\cos(ax)\cos(bx)\,dx=\frac{1}{2}\int(\cos((a-b)x)+\cos((a+b)x))\,dx
$$

and

$$
\int\sin(ax)\sin(bx)=\frac{1}{2}\int(\cos((a-b)x)-\cos((a+b)x))\,dx.
$$

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsProductFormulas1
We integrate $\displaystyle\sin(5x)\cos(3x)$:

\begin{align*}
\int\sin(5x)\cos(3x)\,dx&=\frac{1}{2}\int(\sin(2x)+\sin(8x))\,dx\\
&=-\frac{1}{4}\cos(2x)-\frac{1}{16}\cos(8x)+C.
\end{align*}
::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsProductFormulas2
We evaluate $\displaystyle\int\sin(2x)\cos(5x)\,dx$:

\begin{align*}
\int\sin(2x)\cos(5x)\,dx&=\frac{1}{2}\int(-\sin(3x)+\sin(7x))\,dx\\
&=\frac{1}{6}\cos(3x)-\frac{1}{14}\cos(7x)+C.
\end{align*}
::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsProductFormulas3
For $\displaystyle\int\cos(4x)\cos(2x)\,dx$ we find

\begin{align*}
\int\cos(4x)\cos(2x)\,dx&=\frac{1}{2}\int(\cos(2x)+\cos(6x))\,dx\\
&=\frac{1}{4}\sin(2x)+\frac{1}{12}\sin(6x)+C.
\end{align*}
::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsProductFormulas4
$\displaystyle\int\sin(x)\sin(3x)\,dx$ is an indefinite integral of the product of two sine functions. Using the product formula we have

\begin{align*}
\int\sin(x)\sin(3x)\,dx&=\frac{1}{2}\int(\cos(2x)-\cos(4x))\,dx\\
&=\frac{1}{4}\sin(2x)-\frac{1}{8}\sin(4x)+C.
\end{align*}
::::::

## Powers of sine and cosine

For the square of the sine or the cosine we can use the half-angle formulas (see: {prf:ref}`Thm:Trigonometry:HalfAngleFormulas`):

$$
\int\sin^2(x)\,dx=\frac{1}{2}\int(1-\cos(2x))\,dx=\frac{1}{2}x-\frac{1}{4}\sin(2x)+C
$$

and

$$
\int\cos^2(x)\,dx=\frac{1}{2}\int(1+\cos(2x))\,dx=\frac{1}{2}x+\frac{1}{4}\sin(2x)+C.
$$

Note that, using $\cos(2x)=\cos^2(x)-\sin^2(x)$, this implies that

$$
\int\cos(2x)\,dx=\int\left(\cos^2(x)-\sin^2(x)\right)\,dx=\frac{1}{2}\sin(2x)+C,
$$

which also follows from the substitution $t=2x$ and therefore $dt=2\,dx$:

$$
\int\cos(2x)\,dx=\frac{1}{2}\int\cos(t)\,dt=\frac{1}{2}\sin(t)+C=\frac{1}{2}\sin(2x)+C.
$$

Now we consider higher powers of the sine and the cosine.

For odd powers we use the same method as in the previous subsection. In fact, we deal with special cases of $\displaystyle\sin^m(x)\cos^n(x)\,dx$ with either $m=0$ or $n=0$. For $k\in\{1,2,3,\ldots\}$ we obtain

\begin{align*}
\int\sin^{2k+1}(x)\,dx&=-\int\left(1-u^2\right)^k\,du & \text{using }u=\cos(x)
\end{align*}
and

\begin{align*}
\int\cos^{2k+1}(x)\,dx&=\int\left(1-u^2\right)^k\,du & \text{using }u=\cos(x).
\end{align*}

In both cases we end up with an integral of a polynomial, which can be evaluated directly.

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerOddSin
$\displaystyle\int\sin^5(x)\,dx$ can be evaluated using the substitution $u=\cos(x)$ and we obtain

\begin{align*}
\int\sin^5(x)\,dx&=-\int\left(1-u^2\right)^2\,du \\
&=-\int(1-2u^2+u^4)\,du\\
&=-\left(u-\frac{2}{3}u^3+\frac{1}{5}u^5\right)+C\\
&=-\cos(x)+\frac{2}{3}\cos^3(x)-\frac{1}{5}\cos^5(x)+C.
\end{align*}
::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerOddCos
The integral $\displaystyle\int\cos^3(x)\,dx$ can be evaluated using the substitution $u=\sin(x)$ and we find that

\begin{align*}
\int\cos^3(x)\,dx &=\int(1-u^2)\,du \\
&=u-\frac{1}{3}u^3+C \\
&=\sin(x)-\frac{1}{3}\sin^3(x)+C.
\end{align*}
::::::

For even powers we use the half-angle formulas (see: {prf:ref}`Thm:Trigonometry:HalfAngleFormulas`), similar as for the square of the sine and the cosine:

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerEvenSin

Using $\sin^2(x)=\dfrac{1}{2}(1-\cos(2x))$ the indefinite integral of $\sin^4(x)$ becomes

\begin{align*}
\int\sin^4(x)\,dx&=\frac{1}{4}\int\left(1-\cos(2x)\right)^2\,dx\\
&=\frac{1}{4}\int\left(1-2\cos(2x)+\cos^2(2x)\right)\,dx.
\end{align*}

Now we use $\cos^2(2x)=\dfrac{1}{2}(1+\cos(4x))$ to find that

\begin{align*}
\int\sin^4(x)\,dx&=\frac{1}{4}\int\left(1-2\cos(2x)+\frac{1}{2}+\frac{1}{2}\cos(4x)\right)\,dx\\
&=\int\left(\frac{3}{8}-\frac{1}{2}\cos(2x)+\frac{1}{8}\cos(4x)\right)\,dx\\
&=\frac{3}{8}x-\frac{1}{4}\sin(2x)+\frac{1}{32}\sin(4x)+C.
\end{align*}
::::::

Another option for powers of sine, is to use integration by parts to find a reduction formula:

::::::{prf:Example}
:label: Ex:Integration:PartsReductionSin
We will show that
 
$$
\int\sin^n(x)\,dx=-\frac{1}{n}\cos(x)\sin^{n-1}(x)+\frac{n-1}{n}\int\sin^{n-2}(x)\,dx, \quad n=2,3,4,\ldots
$$ 

For $n=2,3,4,\ldots$ we obtain

\begin{align*}
\int\sin^n(x)\,dx&=-\int\sin^{n-1}(x)\,\cos(x)\\
&=-\cos(x)\sin^{n-1}(x)+\int\cos(x)\,d\sin^{n-1}(x)\\
&=-\cos(x)\sin^{n-1}(x)+(n-1)\int\cos(x)\sin^{n-2}(x)\cos(x)\,dx\\
&=-\cos(x)\sin^{n-1}(x)+(n-1)\int\sin^{n-2}(x)\cos^2(x)\,dx.
\end{align*}

Now we use $\cos^2(x)=1-\sin^2(x)$ to find

\begin{align*}
&\int\sin^n(x)\,dx\\
&=-\cos(x)\sin^{n-1}(x)+(n-1)\int\sin^{n-2}(x)\left(1-\sin^2(x)\right)\,dx\\
&=-\cos(x)\sin^{n-1}(x)+(n-1)\int\sin^{n-2}(x)\,dx-(n-1)\int\sin^n(x)\,dx.
\end{align*}
This implies that

$$
n\int\sin^n(x)\,dx=-\cos(x)\sin^{n-1}(x)+(n-1)\int\sin^{n-2}(x)\,dx
$$

and therefore

$$
\int\sin^n(x)\,dx=-\frac{1}{n}\cos(x)\sin^{n-1}(x)+\frac{n-1}{n}\int\sin^{n-2}(x)\,dx.
$$

::::::

## Powers of tangent

We have seen that $\displaystyle\int\tan(x)\,dx=-\ln|\cos(x)|+C$.

Since $\displaystyle\frac{d}{dx}\tan(x)=1+\tan^2(x)$ we have

\begin{align*}
\int\tan^2(x)\,dx&=\int\left(1+\tan^2(x)-1\right)\,dx\\
&=\int\left(1+\tan^2(x)\right)\,dx-\int1\,dx\\
&=\tan(x)-x+C.
\end{align*}

For higher powers we use a reduction formula for $k\in\{2,3,4,\ldots\}$

\begin{align*}
\int\tan^k(x)\,dx &= \int\tan^{k-2}(x)\tan^2(x)\,dx \\
&=\int\tan^{k-2}(x)\left(1+\tan^2(x)-1\right)\,dx\\
&=\int\tan^{k-2}(x)\,d\tan(x)-\int\tan^{k-2}(x)\,dx\\
&=\frac{1}{k-1}\tan^{k-1}(x)-\int\tan^{k-2}(x)\,dx.
\end{align*}

For $k=2$ this gives the same result as before:

$$
\int\tan^2(x)\,dx=\tan(x)-\int1\,dx=\tan(x)-x+C.
$$ 

For $k=3$ we have

$$
\int\tan^3(x)\,dx=\frac{1}{2}\tan^2(x)-\int\tan(x)\,dx=\frac{1}{2}\tan^2(x)+\ln|\cos(x)|+C.
$$

For $k=4$ we obtain

$$
\int\tan^4(x)\,dx=\frac{1}{3}\tan^3(x)-\int\tan^2(x)\,dx=\frac{1}{3}\tan^3(x)-\tan(x)+x+C.
$$

For $k=5$ we have

\begin{align*}
\int\tan^5(x)\,dx&=\frac{1}{4}\tan^2(x)-\int\tan^3(x)\,dx\\
&=\frac{1}{4}\tan^4(x)-\frac{1}{2}\tan^2(x)-\ln|\cos(x)|+C.
\end{align*}

(Sec:Integration:HalfAngle)=
## The tangent half-angle substitution

The **tangent half-angle substitution**, sometimes (misattributed[^misattributed]) as the **Weierstrass substitution**, converts an integral of a rational function of trigonometric functions into an integral of an ordinary rational function. Although integrals of rational functions will be covered in {numref}`Sec:Integration:RationalFunctions`, we will show how the substitution works.

[^misattributed]: See for an explanation [Note 7](https://en.wikipedia.org/wiki/Tangent_half-angle_substitution#cite_note-weierstrass-7) in [Tangent half-angle substitution](https://en.wikipedia.org/wiki/Tangent_half-angle_substitution).

We start with the definition of the tangent half-angle substitution:

:::{prf:definition} Tangent half-angle substitution
:label: Def:Integration:TangentHalfAngleSubstitution
The **tangent half-angle substitution** is the substitution

$$
t=\tan(\tfrac{1}{2}x)\quad\text{for}\quad-\pi<x<\pi
$$

or equivalently

$$
x=2\arctan(t)\quad\text{for}\quad t\in\mathbb{R}.
$$

:::

If we use this substitution, we also have $dx=\dfrac{2\,dt}{1+t^2}$.

The relation between $t$ and the sine and cosine is given by the following theorem:

:::::{prf:theorem}
:label: Thm:Integration:TangentHalfAngleSubstitution
For $-\pi<x<\pi$ we have

$$
\sin(\tfrac{1}{2}x)=\frac{t}{\sqrt{1+t^2}}\quad\text{and}\quad\cos(\tfrac{1}{2}x)=\frac{1}{\sqrt{1+t^2}}.
$$

and

$$
\sin(x)=\frac{2t}{1+t^2},\quad\cos(x)=\frac{1-t^2}{1+t^2}\quad\text{and}\quad\tan(x)=\frac{2t}{1-t^2}.
$$

:::::

:::{admonition} Proof of {prf:ref}`Thm:Integration:TangentHalfAngleSubstitution`
:class: tudproof

For $0<x<\pi$ consider the right-angled triangle with legs $1$ and $t$ and angle $\theta$ such that $\tan(\theta)=t$. Then the hypotenuse equals $\sqrt{1+t^2}$ and

$$
\sin(\theta)=\frac{t}{\sqrt{1+t^2}}\quad\text{and}\quad\cos(\theta)=\frac{1}{\sqrt{1+t^2}}.
$$

This proves the formulas for $0<x<\pi$. For $-\pi<x<0$ we use $\sin(-\theta)=-\sin(\theta)$ and $\cos(-\theta)=\cos(\theta)$. For $x=0$ the formulas (trivially) hold as well.

Alternatively, we have

$$
\cos^2(\tfrac{1}{2}x)=\frac{1}{1+\tan^2(\frac{1}{2}x)}=\frac{1}{1+t^2}\quad\Longrightarrow\quad\cos(\tfrac{1}{2}x)=\pm\frac{1}{\sqrt{1+t^2}}.
$$

Since $\cos(\frac{1}{2}x)>0$ for $-\pi<x<\pi$ we conclude that $\cos(\frac{1}{2}x)=\dfrac{1}{\sqrt{1+t^2}}$. Then we have

$$
\sin^2(\tfrac{1}{2}x)=1-\cos^2(\tfrac{1}{2}x)=1-\frac{1}{1+t^2}=\frac{1+t^2-1}{1+t^2}=\frac{t^2}{1+t^2}.
$$

Hence, we have: $\sin(\frac{1}{2}x)=\pm\dfrac{t}{\sqrt{1+t^2}}$. Since $\sin(\frac{1}{2}x)$ should have the same sign as $t=\tan(\frac{1}{2}x)$ for $-\pi<x<\pi$ we conclude that $\sin(\frac{1}{2}x)=\dfrac{t}{\sqrt{1+t^2}}$.

This leads to

$$
\sin(x)=2\sin(\tfrac{1}{2}x)\cos(\tfrac{1}{2}x)=\frac{2t}{1+t^2},
$$

$$
\cos(x)=\cos^2(\tfrac{1}{2}x)-\sin^2(\tfrac{1}{2}x)=\frac{1-t^2}{1+t^2}
$$

and

$$
\tan(x)=\frac{\sin(x)}{\cos(x)}=\frac{2t}{1+t^2}\cdot\frac{1+t^2}{1-t^2}=\frac{2t}{1-t^2}.
$$

:::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsTangentHalfAngleExample
Let us start with applying the tangent half-angle substitution to $\displaystyle\int\frac{dx}{1+\cos(x)}$.

Let $t=\tan(\frac{1}{2}x)$, then we have $\cos(x)=\dfrac{1-t^2}{1+t^2}$ and $dx=\dfrac{2\,dt}{1+t^2}$. Hence

\begin{align*}
\int\frac{dx}{1+\cos(x)} &= \int\frac{1}{1+\dfrac{1-t^2}{1+t^2}}\cdot\frac{2\,dt}{1+t^2} \\
&= \int\frac{2}{(1+t^2)+(1-t^2)}\,dt \\
&=\int1\,dt \\
&= t+C \\
&= \tan(\tfrac{1}{2}x)+C.
\end{align*}

::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsTangentHalfAngleTan
We evaluate $\displaystyle\int\tan(x)\,dx$ using the tangent half-angle substitution.

Let $t=\tan(\frac{1}{2}x)$, then we have $\tan(x)=\dfrac{2t}{1-t^2}$ and $dx=\dfrac{2\,dt}{1+t^2}$. Hence

\begin{align*}
\int\tan(x)\,dx &= \int\frac{2t}{1-t^2}\cdot\frac{2\,dt}{1+t^2} \\
&= \int\left(\frac{2t}{1-t^2}+\frac{2t}{1+t^2}\right)\,dt\\
&=\ln|1+t^2|-\ln|1-t^2|+C \\
&=\ln\left|\frac{1+t^2}{1-t^2}\right|+C\\
&=\ln\left|\frac{1+\tan^2(\frac{1}{2}x)}{1-\tan^2(\frac{1}{2}x)}\right|+C \\
&=\ln\left|\frac{\cos^2(\frac{1}{2}x)+\sin^2(\frac{1}{2}x)}{\cos^2(\frac{1}{2}x)-\sin^2(\frac{1}{2}x)}\right|+C\\
&=\ln\left|\frac{1}{\cos(x)}\right|+C \\
&=-\ln|\cos(x)|+C.
\end{align*}

In the second step, directly after the substitution, we have used a partial fraction decomposition, which you can read all about in {numref}`sec:PartialFractionDecomposition`. In a later step we have used $\cos(x)=\cos^2(\frac{1}{2}x)-\sin^2(\frac{1}{2}x)$.

::::::

Let us apply the tangent half-angle substitution to the integrals $\displaystyle\int\frac{dx}{\sin(x)}$ and $\displaystyle\int\frac{dx}{\cos(x)}$:

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsTangentHalfAngleSin
Let $t=\tan(\frac{1}{2}x)$, then we have $\sin(x)=\dfrac{2t}{1+t^2}$ and $dx=\dfrac{2\,dt}{1+t^2}$ and thus

\begin{align*}
\int\frac{dx}{\sin(x)} &= \int\frac{1}{\dfrac{2t}{1+t^2}}\cdot\frac{2\,dt}{1+t^2} \\
&= \int\frac{dt}{t} \\
&=\ln|t|+C \\
&=\ln\left|\tan(\tfrac{1}{2}x)\right|+C.
\end{align*}
::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsTangentHalfAngleCos

Let $t=\tan(\frac{1}{2}x)$, then we have $\cos(x)=\dfrac{1-t^2}{1+t^2}$ and $dx=\dfrac{2\,dt}{1+t^2}$ and thus

\begin{align*}
\int\frac{dx}{\cos(x)}&=\int\frac{1}{\dfrac{1-t^2}{1+t^2}}\cdot\frac{2\,dt}{1+t^2} \\
&=\int\frac{2\,dt}{1-t^2} \\
&=\int\left(\frac{1}{1+t}+\frac{1}{1-t}\right)\,dt\\
&=\ln|1+t|-\ln|1-t|+C\\
&=\ln\left|\frac{1+t}{1-t}\right|+C\\
&=\ln\left|\frac{1+\tan(\frac{1}{2}x)}{1-\tan(\frac{1}{2}x)}\right|+C.
\end{align*}

Here again we used a partial fraction decomposition in the third step, which you can read all about in {numref}`sec:PartialFractionDecomposition`. 

::::::

We give some more examples of how you can use the tangent half-angle substitution in definite integrals:

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionTangentHalfAngleExample1
The definite integral $\displaystyle\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\sin(x)}$ can be evaluated by using $t=\tan(\frac{1}{2}x)$:

\begin{align*}
\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\sin(x)} &= \int_0^1\frac{1}{1+\dfrac{2t}{1+t^2}}\cdot\frac{2\,dt}{1+t^2} \\
&= \int_0^1\frac{2}{\dfrac{1+t^2+2t}{1+t^2}}\,dt \\
&= \int_0^1\frac{2\,dt}{(t+1)^2}\\
&=-\frac{2}{1+t}\bigg|_0^1 \\
&=-1+2 \\
&=1.
\end{align*}
::::::

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionTangentHalfAngleExample2
$\displaystyle\int_0^{\frac{1}{2}\pi}\frac{\cos(x)}{1+\cos(x)}\,dx$, using $t=\tan(\frac{1}{2}x)$, becomes

\begin{align*}
\int_0^{\frac{1}{2}\pi}\frac{\cos(x)}{1+\cos(x)}\,dx &= \int_0^1\frac{\dfrac{1-t^2}{1+t^2}}{1+\dfrac{1-t^2}{1+t^2}}\cdot\frac{2}{1+t^2}\,dt\\
&= \int_0^1\frac{1-t^2}{1+t^2+1-t^2}\cdot\frac{2}{1+t^2}\,dt\\
&= \int_0^1\frac{1-t^2}{1+t^2}\,dt \\
&= \int_0^1\frac{2-(1+t^2)}{1+t^2}\,dt\\
&=\bigg[2\arctan(t)-t\bigg]_0^1 \\
&=\frac{1}{2}\pi-1.
\end{align*}

::::::

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionTangentHalfAngleExample3
We evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\sin(x)+\cos(x)}$.

Using $t=\tan(\frac{1}{2}x)$ we obtain

\begin{align*}
\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\sin(x)+\cos(x)} &= \int_0^1\frac{1}{1+\dfrac{2t}{1+t^2}+\dfrac{1-t^2}{1+t^2}}\cdot\frac{2\,dt}{1+t^2}\\
&= \int_0^1\frac{2}{1+t^2+2t+1-t^2}\,dt\\
&= \int_0^1\frac{2}{2+2t}\,dt\\
&= \int_0^1\frac{dt}{1+t} \\
&= \ln(1+t)\bigg|_0^1\\
&=\ln(2).
\end{align*}
::::::

In {prf:ref}`Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample2` we obtained that

$$
\int_0^{\frac{1}{4}\pi}\frac{1}{\cos(t)}\,dt=\ln(1+\sqrt{2}).
$$

This can also be done using the tangent half-angle substitution: set $u=\tan(\frac{1}{2}t)$ or $t=2\arctan(u)$. Then $t=0$ implies that $u=0$ and $t=\frac{1}{4}\pi$ implies that $u=\tan(\frac{1}{8}\pi)=\sqrt{2}-1$ (see {numref}`Grasple:131804`). With $\cos(t)=\dfrac{1-u^2}{1+u^2}$ and $dt=\dfrac{2\,du}{1+u^2}$ we obtain

\begin{align*}
\int_0^{\frac{1}{4}\pi}\frac{1}{\cos(t)}\,dt&=\int_0^{\sqrt{2}-1}\frac{1}{\dfrac{1-u^2}{1+u^2}}\cdot\frac{2\,du}{1+u^2}=\int_0^{\sqrt{2}-1}\frac{2}{1-u^2}\,du\\
&=\int_0^{\sqrt{2}-1}\left(\frac{1}{1+u}+\frac{1}{1-u}\right)\,du=\bigg[\ln(1+u)-\ln(1-u)\bigg]_0^{\sqrt{2}-1}\\
&=\ln(\sqrt{2})-\ln(2-\sqrt{2})=\ln\left(\frac{\sqrt{2}}{2-\sqrt{2}}\right)\\
&=\ln\left(\frac{\sqrt{2}}{2-\sqrt{2}}\cdot\frac{2+\sqrt{2}}{2+\sqrt{2}}\right)=\ln\left(\frac{2+2\sqrt{2}}{4-2}\right)=\ln(1+\sqrt{2}).
\end{align*}

## Using symmetry

In {numref}`Sec:Integration:Substitution` we have seen that a clever substitution might give rise to a certain symmetry which makes it easier to evaluate an integral. For some trigonometric functions something like this might work. In the next example we use the substitution $x=\frac{1}{2}\pi-t$ and symmetry to evaluate the integral.

::::::{prf:Example}
:label: Ex:Integration:SubstitutionSymmetry2
Using the substitution $x=\frac{1}{2}\pi-t$ and therefore $dx=-\,dt$ we obtain

\begin{align*}
I&=\int_0^{\frac{1}{2}\pi}\frac{\sin(x)}{\sin(x)+\cos(x)}\,dx\\
&=-\int_{\frac{1}{2}\pi}^0\frac{\sin(\frac{1}{2}\pi-t)}{\sin(\frac{1}{2}\pi-t)+\cos(\frac{1}{2}\pi-t)}\,dt\\
&=\int_0^{\frac{1}{2}\pi}\frac{\sin(\frac{1}{2}\pi-x)}{\sin(\frac{1}{2}\pi-x)+\cos(\frac{1}{2}\pi-x)}\,dx.
\end{align*}

Now we use (see: {prf:ref}`Thm:Trigonometry:ComplementaryAngles`)

$$
\sin(\tfrac{1}{2}\pi-x)=\cos(x)\quad\text{and}\quad\cos(\tfrac{1}{2}\pi-x)=\sin(x)
$$

to find that

$$
I=\int_0^{\frac{1}{2}\pi}\frac{\sin(x)}{\sin(x)+\cos(x)}\,dx=\int_0^{\frac{1}{2}\pi}\frac{\cos(x)}{\cos(x)+\sin(x)}\,dx.
$$

Hence we have

$$
2I=\int_0^{\frac{1}{2}\pi}\frac{\sin(x)}{\sin(x)+\cos(x)}\,dx+\int_0^{\frac{1}{2}\pi}\frac{\cos(x)}{\sin(x)+\cos(x)}\,dx,
$$

which leads to

$$
2I=\int_0^{\frac{1}{2}\pi}\frac{\sin(x)+\cos(x)}{\sin(x)+\cos(x)}\,dx=\int_0^{\frac{1}{2}\pi}1\,dx=\frac{1}{2}\pi.
$$

We conclude that 

$$
I=\displaystyle\int_0^{\frac{1}{2}\pi}\frac{\sin(x)}{\sin(x)+\cos(x)}\,dx=\frac{1}{4}\pi=\int_0^{\frac{1}{2}\pi}\frac{\cos(x)}{\sin(x)+\cos(x)}\,dx.
$$

::::::

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c30e011a-a7a3-4ecb-8f85-6aa83a81064a?id=134447
:label: Grasple:134447
:dropdown:
:description: Find different forms of an antiderivative of $\sin(2x)$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f2cd0fe8-e133-4577-a63d-984c18adfbe0?id=134471
:label: Grasple:134471
:dropdown:
:description: Find different forms of an antiderivative of $\displaystyle\frac{1}{\cos(x)}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c1394e54-c98e-4c42-9b41-c80bb38762cb?id=134477
:label: Grasple:134477
:dropdown:
:description: Find different forms of an antiderivative of $\displaystyle\frac{1}{\sin(x)}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e651d29c-60cc-4473-90bb-61f51ec56171?id=134492
:label: Grasple:134492
:dropdown:
:description: Evaluate $\displaystyle\int\sin^3(x)\cos^5(x)\,dx$ in two ways.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d2b68986-b3f1-4d2a-ac73-4f42156192f7?id=134494
:label: Grasple:134494
:dropdown:
:description: Prove orthogonality relations for the sine and cosine.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/91b68fbd-1567-4ccb-9726-7eac80cec1dd?id=134500
:label: Grasple:134500
:dropdown:
:description: Show that $\displaystyle\frac{d}{dx}\left(\tan(\tfrac{1}{2}x)\right)=\frac{1}{1+\cos(x)}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b1366d57-4b98-4602-8cbf-0a0442c915aa?id=134504
:label: Grasple:134504
:dropdown:
:description: Show that $\displaystyle\frac{d}{dx}\left(\ln\left|\tan(\tfrac{1}{2}x)\right|\right)=\frac{1}{\sin(x)}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f3edb317-cdad-44b7-bc6a-bedba3b64988?id=134506
:label: Grasple:134506
:dropdown:
:description: Show that $\displaystyle\frac{d}{dx}\left(\ln\left|\frac{1+\tan(\frac{1}{2}x)}{1-\tan(\frac{1}{2}x)}\right|\right)=\frac{1}{\cos(x)}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/99d7f2aa-55ae-4555-9995-7d4b67a1c634?id=134514
:label: Grasple:134514
:dropdown:
:description: Evaluate $\displaystyle\int\frac{dx}{1+\sin(x)}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f6833eca-3d62-4869-b1d7-83b00a6c3688?id=134515
:label: Grasple:134515
:dropdown:
:description: Evaluate $\displaystyle\int\frac{\sin(x)}{1+\sin(x)}\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/083e0b2f-5ba6-492a-a144-c432cea9a4c3?id=134517
:label: Grasple:134517
:dropdown:
:description: Evaluate an integral of the form $\displaystyle\int\frac{dx}{a\sin(x)+b\cos(x)}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5968d74d-2311-4ced-9a88-170b9be9c851?id=134538
:label: Grasple:134538
:dropdown:
:description: Use $\cos(2\theta)=2\cos^2(\theta)-1$ to evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\sqrt{1+\cos(x)}\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9b626623-a38f-4f8d-9b94-cead08ca89c7?id=134539
:label: Grasple:134539
:dropdown:
:description: Use $\cos(2\theta)=1-2\sin^2(\theta)$ to evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\sqrt{1-\cos(x)}\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8a741095-13ce-4faf-9117-c5126e179d28?id=134540
:label: Grasple:134540
:dropdown:
:description: Use $1=\sin^2(\theta)+\cos^2(\theta)$ and $\sin(2\theta)=2\sin(\theta)\cos(\theta)$ to evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\sqrt{1+\sin(x)}\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/57cfd0bd-6050-41e4-bdfa-4e1dc8d09098?id=134541
:label: Grasple:134541
:dropdown:
:description: Use $1=\sin^2(\theta)+\cos^2(\theta)$ and $\sin(2\theta)=2\sin(\theta)\cos(\theta)$ to evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\sqrt{1-\sin(x)}\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fd57615b-4560-4504-9f98-358be11e8ffd?id=134542
:label: Grasple:134542
:dropdown:
:description: Evaluate $\displaystyle\int\cos(x)\cos(2x)\cos(3x)\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/241b0599-4749-436d-859e-f3677fbe71d1?id=134543
:label: Grasple:134543
:dropdown:
:description: Evaluate $\displaystyle\int\sin(x)\sin(2x)\sin(3x)\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e032d14c-df4c-4572-a8ae-d909827a0e71?id=133604
:label: Grasple:134604
:dropdown:
:description: Find a reduction formula for $\displaystyle\int\cos^n(x)\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2a806dac-fad6-45c4-a66b-4c56af966471?id=134651
:label: Grasple:134651
:dropdown:
:description: Find closed formulas for $\displaystyle\int_0^{\frac{1}{2}\pi}\sin^{2n+1}(x)\,dx$ and $\displaystyle\int_0^{\frac{1}{2}\pi}\sin^{2n}(x)\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5f998152-3f25-4845-a2f3-fef08cc73ddf?id=134657
:label: Grasple:134657
:dropdown:
:description: Proof of the Wallis product.

::::

:::{note}
The result of {numref}`Grasple:134657` 

$$
\lim_{n\to\infty}\frac{(2\cdot4\cdot6\cdots2n)^2}{1\cdot(3\cdot5\cdot7\cdots(2n-1))^2\cdot(2n+1)}=\frac{\pi}{2}
$$

can also be written as

$$
\lim_{n\to\infty}\frac{2}{1}\frac{2}{3}\frac{4}{3}\frac{4}{5}\frac{6}{5}\frac{6}{7}\cdots\frac{2n}{2n-1}\frac{2n}{2n+1}=\frac{\pi}{2}.
$$

This result is sometimes written as an infinite product

$$
\prod_{n=1}^{\infty}\frac{2n}{2n-1}\frac{2n}{2n+1}=\frac{\pi}{2},
$$

which is called the *Wallis product*. This formula is named after the English mathematician [John Wallis (1616-1703)](https://en.wikipedia.org/wiki/John_Wallis).
:::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/60d93c06-c902-4e62-a79a-e345ab8c7a7b?id=132747
:label: Grasple:132747
:dropdown:
:description: Evaluate an integral of the form $\displaystyle\int_0^{\frac{1}{2}\pi}\frac{(\sin(x))^a}{(\sin(x))^a+(\cos(x))^a}\,dx$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/606aaccc-19e9-47e9-8805-1d128f9dd576?id=134400
:label: Grasple:134400
:dropdown:
:description: Evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\tan(x)}$.

::::
