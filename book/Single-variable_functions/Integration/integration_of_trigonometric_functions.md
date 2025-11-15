# Integration of trigonometric functions

In this section we cover the integration of trigonometric functions with:

- Basic trigonometric identities
- Products of trigonometric functions
- Powers of sine and cosine
- Powers of tangent
- Using complex exponentials
- Tangent half-angle substitution (do not call it the Weierstrass substitution, see https://en.wikipedia.org/wiki/Tangent_half-angle_substitution)

## Basic trigonometric identities

Using the fundamental theorem of calculus we have already seen that

$$
\int\sin(x)\,dx=-\cos(x)+C\quad\text{and}\quad\int\cos(x)\,dx=\sin(x)+C.
$$

For the tangent we use the substitution $u=\cos(x)$ and therefore $du=-\sin(x)\,dx$ to obtain

$$
\int\tan(x)\,dx=\int\frac{\sin(x)}{\cos(x)}\,dx=-\int\frac{du}{u}=-\ln|u|+C=-\ln|\cos(x)|+C.
$$

Similarly, the substitution $u=\sin(x)$ and therefore $du=\cos(x)\,dx$ leads to

$$
\int\frac{\cos(x)}{\sin(x)}\,dx=\int\frac{du}{u}=\ln|u|+C=\ln|\sin(x)|+C.
$$

For the square of the sine or the cosine we use the half-angle formulas (see: {prf:ref}`Thm:Trigonometry:HalfAngleFormulas`):

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

::::{exercise}
:label: Exc:Integration:TrigFunctionsExerciseSinDouble
Consider the integral $\displaystyle\int\sin(2x)\,dx$.

(a) Use the substitution $t=2x$ to evaluate the integral.

(b) Use $\sin(2x)=2\sin(x)\cos(x)$ and the substitution $t=\sin(x)$ to evaluate the integral.

(c) Use $\sin(2x)=2\sin(x)\cos(x)$ and the substitution $t=\cos(x)$ to evaluate the integral.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsExerciseSinDouble`
:class: solution, dropdown
(a) The substitution $t=2x$ implies that $dt=2\,dx$ and therefore

$$
\int\sin(2x)\,dx==\frac{1}{2}\int\sin(t)\,dt=-\frac{1}{2}\cos(t)+C=-\frac{1}{2}\cos(2x)+C.
$$

(b) The substitution $t=\sin(x)$ implies that $dt=\cos(x)\,dx$ and therefore

$$
\int\sin(2x)\,dx=2\int\sin(x)\cos(x)\,dx=2\int t\,dt=t^2+C=\sin^2(x)+C.
$$

(c) The substitution $t=\cos(x)$ implies that $dt=-\sin(x)\,dx$ and therefore

$$
\int\sin(2x)\,dx=2\int\sin(x)\cos(x)\,dx=-2\int t\,dt=-t^2+C=-\cos^2(x)+C.
$$

This implies that the functions $-\frac{1}{2}\cos(2x)$, $\sin^2(x)$ and $-\cos^2(x)$ should differ by a constant, which is true since {prf:ref}`Thm:Trigonometry:DoubleAngleFormulas` implies that

$$
-\frac{1}{2}+\sin^2(x)=-\frac{1}{2}\cos(2x)=\frac{1}{2}-\cos^2(x).
$$

:::

Using $\displaystyle\frac{d}{dx}\tan(x)=\frac{d}{dx}\left(\frac{\sin(x)}{\cos(x)}\right)=\frac{\cos^2(x)+\sin^2(x)}{\cos^2(x)}=\frac{1}{\cos^2(x)}$ we have

$$
\int\frac{dx}{\cos^2(x)}=\tan(x)+C.
$$

Similarly, we have $\displaystyle\frac{d}{dx}\left(\frac{\cos(x)}{\sin(x)}\right)=\frac{-\sin^2(x)-\cos^2(x)}{\sin^2(x)}=-\frac{1}{\sin^2(x)}$ and therefore

$$
\int\frac{dx}{\sin^2(x)}=-\frac{\cos(x)}{\sin(x)}+C.
$$

In {prf:ref}`Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample2` we have seen that

$$
\int\frac{dx}{\cos(x)}=\ln\left|\tan(x)+\frac{1}{\cos(x)}\right|+C.
$$

This formula was discovered in 1668 by the Scottish mathematician [James Gregory (1638-1675)](https://en.wikipedia.org/wiki/James_Gregory_(mathematician)). Similarly, we have

$$
\int\frac{dx}{\sin(x)}=-\ln\left|\frac{\cos(x)}{\sin(x)}+\frac{1}{\sin(x)}\right|+C.
$$

The proof is also similar:

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

These formulas can also be written as:

$$
\int\frac{dx}{\cos(x)}=\ln\left|\frac{1+\sin(x)}{\cos(x)}\right|+C=-\ln\left|\frac{1-\sin(x)}{\cos(x)}\right|+C
$$

and

$$
\int\frac{dx}{\sin(x)}=-\ln\left|\frac{1+\cos(x)}{\sin(x)}\right|+C=\ln\left|\frac{1-\cos(x)}{\sin(x)}\right|+C.
$$

::::{exercise}
:label: Exc:Integration:TrigFunctionsCos
(a) Show that $\displaystyle\ln\left|\frac{1+\sin(x)}{\cos(x)}\right|=-\ln\left|\frac{1-\sin(x)}{\cos(x)}\right|$.

(b) Show that $\displaystyle\frac{d}{dx}\left(\ln\left|\frac{1+\sin(x)}{\cos(x)}\right|\right)=\frac{1}{\cos(x)}$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsCos`
:class: solution, dropdown
(a)

$$
\begin{align*}
\ln\left|\frac{1+\sin(x)}{\cos(x)}\right|&=\ln\left|\frac{1+\sin(x)}{\cos(x)}\cdot\frac{1-\sin(x)}{1-\sin(x)}\right|=\ln\left|\frac{1-\sin^2(x)}{\cos(x)(1-\sin(x))}\right|\\
&=\ln\left|\frac{\cos(x)}{1-\sin(x)}\right|=-\ln\left|\frac{1-\sin(x)}{\cos(x)}\right|.
\end{align*}
$$

(b)

$$
\frac{d}{dx}\left(\ln\left|\frac{1+\sin(x)}{\cos(x)}\right|\right)=\frac{\cos(x)}{1+\sin(x)}\cdot\frac{\cos^2(x)+\sin(x)+\sin^2(x)}{\cos^2(x)}=\frac{1}{\cos(x)}.
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsSin
(a) Show that $\displaystyle-\ln\left|\frac{1+\cos(x)}{\sin(x)}\right|=\ln\left|\frac{1-\cos(x)}{\sin(x)}\right|$.

(b) Show that $\displaystyle\frac{d}{dx}\left(\ln\left|\frac{1-\cos(x)}{\sin(x)}\right|\right)=\frac{1}{\sin(x)}$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsSin`
:class: solution, dropdown
(a)

$$
\begin{align*}
-\ln\left|\frac{1+\cos(x)}{\sin(x)}\right|&=-\ln\left|\frac{1+\cos(x)}{\sin(x)}\cdot\frac{1-\cos(x)}{1-\cos(x)}\right|=-\ln\left|\frac{1-\cos^2(x)}{\sin(x)(1-\cos(x))}\right|\\
&=-\ln\left|\frac{\sin(x)}{1-\cos(x)}\right|=\ln\left|\frac{1-\cos(x)}{\sin(x)}\right|.
\end{align*}
$$

(b)

$$
\frac{d}{dx}\left(\ln\left|\frac{1-\cos(x)}{\sin(x)}\right|\right)=\frac{\sin(x)}{1-\cos(x)}\cdot\frac{\sin^2(x)-\cos(x)+\cos^2(x)}{\sin^2(x)}=\frac{1}{\sin(x)}.
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsCosSubstitution
Use $\displaystyle\frac{1}{\cos(x)}=\frac{\cos(x)}{\cos^2(x)}$ and the substitution $u=\sin(x)$ to evaluate $\displaystyle\int\frac{dx}{\cos(x)}$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsCosSubstitution`
:class: solution, dropdown

$$
\begin{align*}
\int\frac{dx}{\cos(x)}&=\int\frac{\cos(x)}{\cos^2(x)}\,dx=\int\frac{d\sin(x)}{1-\sin^2(x)}=\int\frac{du}{1-u^2}=\frac{1}{2}\int\left(\frac{1}{1+u}+\frac{1}{1-u}\right)\,du\\
&=\frac{1}{2}\left(\ln|1+u|-\ln|1-u|\right)+C=\frac{1}{2}\ln\left|\frac{1+u}{1-u}\right|+C=\frac{1}{2}\ln\left|\frac{1+\sin(x)}{1-\sin(x)}\right|+C.
\end{align*}
$$

Note that

$$
\frac{1+\sin(x)}{1-\sin(x)}=\frac{1+\sin(x)}{1-\sin(x)}\cdot\frac{1+\sin(x)}{1+\sin(x)}=\frac{(1+\sin(x))^2}{1-\sin^2(x)}=\frac{(1+\sin(x))^2}{\cos^2(x)}.
$$

Hence, we have

$$
\int\frac{dx}{\cos(x)}=\ln\left|\frac{1+\sin(x)}{\cos(x)}\right|+C.
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsSinSubstitution
Use $\displaystyle\frac{1}{\sin(x)}=\frac{\sin(x)}{\sin^2(x)}$ and the substitution $u=\cos(x)$ to evaluate $\displaystyle\int\frac{dx}{\sin(x)}$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsSinSubstitution`
:class: solution, dropdown

$$
\begin{align*}
\int\frac{dx}{\sin(x)}&=\int\frac{\sin(x)}{\sin^2(x)}\,dx=-\int\frac{d\,\cos(x)}{1-\cos^2(x)}=-\int\frac{du}{1-u^2}=-\frac{1}{2}\int\left(\frac{1}{1+u}+\frac{1}{1-u}\right)\,du\\
&=-\frac{1}{2}\left(\ln|1+u|-\ln|1-u|\right)+C=-\frac{1}{2}\ln\left|\frac{1+u}{1-u}\right|+C=-\frac{1}{2}\ln\left|\frac{1+\cos(x)}{1-\cos(x)}\right|+C.
\end{align*}
$$

Note that

$$
\frac{1+\cos(x)}{1-\cos(x)}=\frac{1+\cos(x)}{1-\cos(x)}\cdot\frac{1+\cos(x)}{1+\cos(x)}=\frac{(1+\cos(x))^2}{1-\cos^2(x)}=\frac{(1+\cos(x))^2}{\sin^2(x)}.
$$

Hence, we have

$$
\int\frac{dx}{\sin(x)}=-\ln\left|\frac{1+\cos(x)}{\sin(x)}\right|+C.
$$

:::

Using the Weierstrass substitution or the tangent half-angle substitution we will derive yet other forms for these integrals.

## Products of trigonometric functions

We consider integrals of the form $\displaystyle\int\sin^m(x)\cos^n(x)\,dx$ for integer values of $m$ and $n$. If (at least) one of these integers is odd, we can use a substitution and the Pythagorean identity {prf:ref}`Thm:Trigonometry:UnitCircleIdentity`.

If $m=2k+1$ with $k\in\{0,1,2,\ldots\}$, then we have using the substitution $u=\cos(x)$

$$
\begin{align*}
\int\sin^{2k+1}(x)\cos^n(x)\,dx&=-\int\sin^{2k}(x)\cos^n(x)\,d\cos(x)=-\int\left(1-\cos^2(x)\right)^k\cos^n(x)\,d\cos(x)\\
&=-\int\left(1-u^2\right)^ku^n\,du.
\end{align*}
$$

If $n=2k+1$ with $k\in\{0,1,2,\ldots\}$, then we have using the substitution $u=\sin(x)$

$$
\begin{align*}
\int\sin^m(x)\cos^{2k+1}(x)\,dx&=\int\sin^m(x)\cos^{2k}(x)\,d\sin(x)=\int\sin^m(x)\left(1-\sin^2(x)\right)^k\,d\sin(x)\\
&=\int u^m\left(1-u^2\right)^k\,du.
\end{align*}
$$

In both cases we end up with an integral of a polynomial, which can be directly evaluated using the fundamental theorem of calculus.

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerOddSinEvenCos
Evaluate $\displaystyle\int\sin^3(x)\cos^2(x)\,dx$.

Solution. Using $u=\cos(x)$ we obtain

$$
\begin{align*}
\int\sin^3(x)\cos^2(x)\,dx&=-\int\sin^2(x)\cos^2(x)\,d\cos(x)=-\int\left(1-\cos^2(x)\right)\cos^2(x)\,d\cos(x)\\
&=-\int(1-u^2)u^2\,du=-\int\left(u^2-u^4\right)\,du=-\frac{1}{3}u^3+\frac{1}{5}u^5+C\\
&=-\frac{1}{3}\cos^3(x)+\frac{1}{5}\cos^5(x)+C.
\end{align*}
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerEvenSinOddCos
Evaluate $\displaystyle\int\sin^4(x)\cos^3(x)\,dx$.

Solution. Using $u=\sin(x)$ we obtain

$$
\begin{align*}
\int\sin^4(x)\cos^3(x)\,dx&=\int\sin^4(x)\cos^2(x)\,d\sin(x)=\int\sin^4(x)\left(1-\sin^2(x)\right)\,d\sin(x)\\
&=\int u^4(1-u^2)\,du=\int\left(u^4-u^6\right)\,du=\frac{1}{5}u^5-\frac{1}{7}u^7+C\\
&=\frac{1}{5}\sin^5(x)-\frac{1}{7}\sin^7(x)+C.
\end{align*}
$$

::::::

If both powers are odd, both methods work.

::::{exercise}
:label: Exc:Integration:TrigFunctionsPowerOddSinOddCos
Consider $\displaystyle\int\sin^3(x)\cos^5(x)\,dx$.

(a) Evaluate the integral using the substitution $u=\cos(x)$.

(b) Evaluate the integral using the substitution $u=\sin(x)$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsPowerOddSinOddCos`
:class: solution, dropdown

(a) Using $=\cos(x)$ we have

$$
\begin{align*}
\int\sin^3(x)\cos^5(x)\,dx&=-\int\sin^2(x)\cos^5(x)\,d\cos(x)=-\int\left(1-\cos^2(x)\right)\cos^5(x)\,d\cos(x)\\
&=-\int(1-u^2)u^5\,du=-\int(u^5-u^7)\,du=-\frac{1}{6}u^6+\frac{1}{8}u^8+C\\
&=-\frac{1}{6}\cos^6(x)+\frac{1}{8}\cos^8(x)+C.
\end{align*}
$$

(b) Using $=\sin(x)$ we have

$$
\begin{align*}
\int\sin^3(x)\cos^5(x)\,dx&=\int\sin^3(x)\cos^4(x)\,d\sin(x)=\int\sin^3(x)\left(1-\sin^2(x)\right)^2\,d\sin(x)\\
&=\int u^3\left(1-u^2\right)^2\,du=\int u^3\left(1-2u^2+u^4\right)\,du=\int\left(u^3-2u^5+u^7\right)\,du\\
&=\frac{1}{4}u^4-\frac{1}{3}u^6+\frac{1}{8}u^8+C=\frac{1}{4}\sin^4(x)-\frac{1}{3}\sin^6(x)+\frac{1}{8}\sin^8(x)+C.
\end{align*}
$$

:::

If both powers are even, it is more difficult. We may use the half-angle formulas (see: {prf:ref}`Thm:Trigonometry:HalfAngleFormulas`) and sometimes $\sin(x)\cos(x)=\frac{1}{2}\sin(2x)$ might help.

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerEvenSinOddCos
Evaluate $\displaystyle\int\sin^2(x)\cos^4(x)\,dx$.

Solution. Using $\sin(x)\cos(x)=\frac{1}{2}\sin(2x)$ and $\cos^2(x)=\frac{1}{2}(1+\cos(2x))$ we have

$$
\begin{align*}
\int\sin^2(x)\cos^4(x)\,dx&=\frac{1}{8}\int\sin^2(2x)(1+\cos(2x))\,dx\\
&=\frac{1}{8}\int\sin^2(2x)\,dx+\frac{1}{8}\int\sin^2(2x)\cos(2x)\,dx.
\end{align*}
$$

Now we might use $\sin^2(2x)=\frac{1}{2}(1-\cos(4x))$ to obtain

$$
\int\sin^2(2x)\,dx=\frac{1}{2}\int(1-\cos(4x))\,dx=\frac{1}{2}x-\frac{1}{8}\sin(2x)+C_1.
$$

Using the substitution $u=\sin(2x)$ we find that

$$
\int\sin^2(2x)\cos(2x)\,dx=\frac{1}{2}\int\sin^2(2x)\,d\sin(2x)=\frac{1}{2}\int u^2\,du=\frac{1}{6}u^3+C_2=\frac{1}{6}\sin^2(2x)+C_2.
$$

Finally, we conclude that

$$
\int\sin^2(x)\cos^4(x)\,dx=\frac{1}{16}x-\frac{1}{64}\sin(2x)+\frac{1}{48}\sin^2(2x)+C.
$$

::::::

Sometimes, these techniques also work in case of quotients instead of products.

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerNegative1
Evaluate $\displaystyle\int\frac{\cos(x)}{\sin^2(x)}\,dx$.

Solution. Using $u=\sin(x)$ we obtain

$$
\int\frac{\cos(x)}{\sin^2(x)}\,dx=\int\frac{d\sin(x)}{\sin^2(x)}=\int\frac{du}{u^2}=-\frac{1}{u}+C=-\frac{1}{\sin(x)}+C.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerNegative2
Evaluate $\displaystyle\int\frac{\sin^3(x)}{\cos^4(x)}\,dx$.

Solution. Using $u=\cos(x)$ we obtain

$$
\begin{align*}
\int\frac{\sin^3(x)}{\cos^4(x)}\,dx&=-\int\frac{1-\cos^2(x)}{\cos^4(x)}\,d\cos(x)=-\int\frac{1-u^2}{u^4}\,du=-\int\left(\frac{1}{u^4}-\frac{1}{u^2}\right)\,du\\
&=\frac{1}{3u^3}-\frac{1}{u}+C=\frac{1}{3\cos^3(x)}-\frac{1}{\cos(x)}+C.
\end{align*}
$$

::::::

Again, when both powers are even it is more difficult. However, there are some exceptions such as in the following examples.

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerNegative3
Evaluate $\displaystyle\int\frac{\sin^2(x)}{\cos^4(x)}\,dx$.

Solution. Since $\displaystyle\frac{d}{dx}\tan(x)=\frac{1}{\cos^2(x)}$ we use $u=\tan(x)$ to obtain

$$
\int\frac{\sin^2(x)}{\cos^4(x)}\,dx=\int\tan^2(x)\,d\tan(x)=\int u^2\,du=\frac{1}{3}u^3+C=\frac{1}{3}\tan^3(x)+C.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerNegative4
Evaluate $\displaystyle\int\frac{\cos^2(x)}{\sin^4(x)}\,dx$.

Solution. Since $\displaystyle\frac{d}{dx}\left(\frac{\cos(x)}{\sin(x)}\right)=-\frac{1}{\sin^2(x)}$ we use $u=\dfrac{\cos(x)}{\sin(x)}$ to obtain

$$
\int\frac{\cos^2(x)}{\sin^4(x)}\,dx=-\int\frac{\cos^2(x)}{\sin^2(x)}\,d\left(\frac{\cos(x)}{\sin(x)}\right)=-\int u^2\,du=-\frac{1}{3}u^3+C=-\frac{1}{3}\frac{\cos^3(x)}{\sin^3(x)}+C.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerNegative5
Evaluate $\displaystyle\int\frac{\sin^2(x)}{\cos^6(x)}\,dx$.

Solution. Since $\displaystyle\frac{d}{dx}\tan(x)=\frac{1}{\cos^2(x)}=1+\tan^2(x)$ we use $u=\tan(x)$ to obtain

$$
\begin{align*}
\int\frac{\sin^2(x)}{\cos^6(x)}\,dx&=\int\tan^2(x)(1+\tan^2(x))\,d\tan(x)=\int u^2(1+u^2)\,du=\frac{1}{3}u^3+\frac{1}{5}u^5+C\\
&=\frac{1}{3}\tan^3(x)+\frac{1}{5}\tan^5(x)+C.
\end{align*}
$$

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
Evaluate $\displaystyle\int\sin(5x)\cos(3x)\,dx$.

Solution.

$$
\int\sin(5x)\cos(3x)\,dx=\frac{1}{2}\int(\sin(2x)+\sin(8x))\,dx=-\frac{1}{4}\cos(2x)-\frac{1}{16}\cos(8x)+C.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsProductFormulas2
Evaluate $\displaystyle\int\sin(2x)\cos(5x)\,dx$.

Solution.

$$
\int\sin(2x)\cos(5x)\,dx=\frac{1}{2}\int(-\sin(3x)+\sin(7x))\,dx=\frac{1}{6}\cos(3x)-\frac{1}{14}\cos(7x)+C.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsProductFormulas3
Evaluate $\displaystyle\int\cos(4x)\cos(2x)\,dx$.

Solution.

$$
\int\cos(4x)\cos(2x)\,dx=\frac{1}{2}\int(\cos(2x)+\cos(6x))\,dx=\frac{1}{4}\sin(2x)+\frac{1}{12}\sin(6x)+C.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsProductFormulas4
Evaluate $\displaystyle\int\sin(x)\sin(3x)\,dx$.

Solution.

$$
\int\sin(x)\sin(3x)\,dx=\frac{1}{2}\int(\cos(2x)-\cos(4x))\,dx=\frac{1}{4}\sin(2x)-\frac{1}{8}\sin(4x)+C.
$$

::::::

::::{exercise}
:label: Exc:Integration:TrigFunctionsProductFormulasOrthogonality
Show that for $m,n\in\mathbb{N}$ we have

(a) $\displaystyle\int_{-\pi}^{\pi}\cos(mx)\cos(nx)\,dx=\begin{cases}0, &m\neq n\\\pi, &m=n,\end{cases}$

(b) $\displaystyle\int_{-\pi}^{\pi}\sin(mx)\sin(nx)\,dx=\begin{cases}0, &m\neq n\\\pi, &m=n,\end{cases}$

and

(c) $\displaystyle\int_{-\pi}^{\pi}\sin(mx)\cos(nx)\,dx=0$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsProductFormulasOrthogonality`
:class: solution, dropdown
(a) For $m\neq n$ we have

$$
\begin{align*}
\int_{-\pi}^{\pi}\cos(mx)\cos(nx)\,dx&=\frac{1}{2}\int_{-\pi}^{\pi}\left(\cos((m-n)x)+\cos((m+n)x)\right)\,dx\\
&=\bigg[\frac{1}{2(m-n)}\sin((m-n)x)+\frac{1}{2(m+n)}\sin((m+n)x)\bigg]_{-\pi}^{\pi}=0.
\end{align*}
$$

For $m=n$ we use a half-angle formula to obtain

$$
\int_{-\pi}^{\pi}\cos^2(nx)\,dx=\frac{1}{2}\int_{-\pi}^{\pi}(1+\cos(2nx))\,dx=\frac{1}{2}\bigg[x+\frac{1}{2n}\sin(2nx)\bigg]_{-\pi}^{\pi}=\pi.
$$

(b) For $m\neq n$ we have

$$
\begin{align*}
\int_{-\pi}^{\pi}\sin(mx)\sin(nx)\,dx&=\frac{1}{2}\int_{-\pi}^{\pi}\left(\cos((m-n)x)-\cos((m+n)x)\right)\,dx\\
&=\bigg[\frac{1}{2(m-n)}\sin((m-n)x)-\frac{1}{2(m+n)}\sin((m+n)x)\bigg]_{-\pi}^{\pi}=0.
\end{align*}
$$

For $m=n$ we use a half-angle formula to obtain

$$
\int_{-\pi}^{\pi}\sin^2(nx)\,dx=\frac{1}{2}\int_{-\pi}^{\pi}(1-\cos(2nx))\,dx=\frac{1}{2}\bigg[x-\frac{1}{2n}\sin(2nx)\bigg]_{-\pi}^{\pi}=\pi.
$$

(c) For $m\neq n$ we obtain

$$
\begin{align*}
\int_{-\pi}^{\pi}\sin(mx)\cos(nx)\,dx&=\frac{1}{2}\int_{-\pi}^{\pi}\left(\sin((m-n)x)+\sin((m+n)x)\right)\,dx\\
&=\bigg[-\frac{1}{2(m-n)}\cos((m-n)x)-\frac{1}{2(m+n)}\cos((m+n)x)\bigg]_{-\pi}^{\pi}=0.
\end{align*}
$$

Moreover, if $m=n$ we also have

$$
\int_{-\pi}^{\pi}\sin(nx)\cos(nx)\,dx=\frac{1}{2}\int_{-\pi}^{\pi}\sin(2nx)\,dx=-\frac{1}{4n}\cos(2nx)\bigg|_{-\pi}^{\pi}=0,\quad n\neq0
$$

and this integral trivially vanishes when $n=0$.

:::

## Powers of sine and cosine

We have seen that $\displaystyle\int\sin(x)\,dx=-\cos(x)+C$ and $\displaystyle\int\cos(x)\,dx=\sin(x)+C$. Furthermore

$$
\int\sin^2(x)\,dx=\frac{1}{2}x-\frac{1}{4}\sin(2x)+C\quad\text{and}\quad\int\cos^2(x)\,dx=\frac{1}{2}x+\frac{1}{4}\sin(2x)+C.
$$

Now we consider higher powers of the sine and the cosine. 

For odd powers we use the same method as in the previous subsection. In fact, we deal with special cases of $\displaystyle\sin^m(x)\cos^n(x)\,dx$ with either $m=0$ or $n=0$. For $k\in\{1,2,3,\ldots\}$ we obtain

$$
\int\sin^{2k+1}(x)\,dx=-\int\sin^{2k}(x)\,d\cos(x)=-\int\left(1-\cos^2(x)\right)^k\,d\cos(x)=-\int\left(1-u^2\right)^k\,du
$$

and

$$
\int\cos^{2k+1}(x)\,dx=\int\cos^{2k}(x)\,d\sin(x)=\int\left(1-\sin^2(x)\right)^k\,d\sin(x)=\int\left(1-u^2\right)^k\,du.
$$

In both cases we end up with an integral of a polynomial, which can be directly evaluated using the fundamental theorem of calculus.

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerOddSin
Evaluate $\displaystyle\int\sin^5(x)\,dx$.

Solution. Using the substitution $u=\cos(x)$ we obtain

$$
\begin{align*}
\int\sin^5(x)\,dx&=-\int\sin^4(x)\,d\cos(x)=-\int(1-\cos^2(x))^2\,d\cos(x)=-\int\left(1-u^2\right)^2\,du\\
&=-\int(1-2u^2+u^4)\,du=-\left(u-\frac{2}{3}u^3+\frac{1}{5}u^5\right)+C\\
&=-\cos(x)+\frac{2}{3}\cos^3(x)-\frac{1}{5}\cos^5(x)+C.
\end{align*}
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerOddCos
Evaluate $\displaystyle\int\cos^3(x)\,dx$.

Solution. Using the substitution $u=\sin(x)$ we obtain

$$
\begin{align*}
\int\cos^3(x)\,dx&=\int\cos^2(x)\,d\sin(x)=\int(1-\sin^2(x))\,d\sin(x)=\int(1-u^2)\,du\\
&=u-\frac{1}{3}u^3+C=\sin(x)-\frac{1}{3}\sin^3(x)+C.
\end{align*}
$$

::::::

For even powers we use the half-angle formulas (see: {prf:ref}`Thm:Trigonometry:HalfAngleFormulas`):

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsPowerEvenSin
Evaluate $\displaystyle\int\sin^4(x)\,dx$.

Solution. Using $\sin^2(x)=\dfrac{1}{2}(1-\cos(2x))$ we obtain

$$
\int\sin^4(x)\,dx=\frac{1}{4}\int\left(1-\cos(2x)\right)^2\,dx=\frac{1}{4}\int\left(1-2\cos(2x)+\cos^2(2x)\right)\,dx.
$$

Now we use $\cos^2(2x)=\dfrac{1}{2}(1+\cos(4x))$ to find that

$$
\begin{align*}
\int\sin^4(x)\,dx&=\frac{1}{4}\int\left(1-2\cos(2x)+\frac{1}{2}+\frac{1}{2}\cos(4x)\right)\,dx\\
&=\int\left(\frac{3}{8}-\frac{1}{2}\cos(2x)+\frac{1}{8}\cos(4x)\right)\,dx\\
&=\frac{3}{8}x-\frac{1}{4}\sin(2x)+\frac{1}{32}\sin(4x)+C.
\end{align*}
$$

::::::

## Powers of tangent

We have seen that $\displaystyle\int\tan(x)\,dx=-\ln|\cos(x)|+C$.

Since $\displaystyle\frac{d}{dx}\tan(x)=1+\tan^2(x)$ we have

$$
\int\tan^2(x)\,dx=\int\left(1+\tan^2(x)-1\right)\,dx=\int\left(1+\tan^2(x)\right)\,dx-\int1\,dx=\tan(x)-x+C.
$$

For higher powers we use a reduction formula for $k\in\{2,3,4,\ldots\}$

$$
\begin{align*}
\int\tan^k(x)\,dx&=\int\tan^{k-2}(x)\left(1+\tan^2(x)-1\right)\,dx=\int\tan^{k-2}(x)\,d\tan(x)-\int\tan^{k-2}(x)\,dx\\
&=\frac{1}{k-1}\tan^{k-1}(x)-\int\tan^{k-2}(x)\,dx.
\end{align*}
$$

For $k=2$ this reads: $\displaystyle\int\tan^2(x)\,dx=\tan(x)-\int1\,dx=\tan(x)-x+C$. 

For $k=3$ we have

$$
\int\tan^3(x)\,dx=\frac{1}{2}\tan^2(x)-\int\tan(x)\,dx=\frac{1}{2}\tan^2(x)+\ln|\cos(x)|+C.
$$

For $k=4$ we obtain

$$
\int\tan^4(x)\,dx=\frac{1}{3}\tan^3(x)-\int\tan^2(x)\,dx=\frac{1}{3}\tan^3(x)-\tan(x)+x+C.
$$

For $k=5$ we have

$$
\int\tan^5(x)\,dx=\frac{1}{4}\tan^2(x)-\int\tan^3(x)\,dx=\frac{1}{4}\tan^4(x)-\frac{1}{2}\tan^2(x)-\ln|\cos(x)|+C.
$$

::::{exercise}
:label: Exc:Integration:TrigFunctionsPowerTanEven
Find a general formula for $\displaystyle\int\tan^{2k}(x)\,dx$ for $k=1,2,3,\ldots$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsPowerTanEven`
:class: solution, dropdown
For $k=1,2,3,\ldots$ we have

$$
\begin{align*}
\int\tan^{2k}(x)\,dx&=\frac{1}{2k-1}\tan^{2k-1}(x)-\frac{1}{2k-3}\tan^{2k-3}(x)+\frac{1}{2k-5}\tan^{2k-5}(x)+\ldots\\
&{}\quad\quad\quad{}\ldots+(-1)^{k-2}\frac{1}{3}\tan^3(x)+(-1)^{k-1}\tan(x)+(-1)^kx+C.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsPowerTanOdd
Find a general formula for $\displaystyle\int\tan^{2k+1}(x)\,dx$ for $k=1,2,3,\ldots$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsPowerTanOdd`
:class: solution, dropdown
For $k=1,2,3,\ldots$ we have

$$
\begin{align*}
\int\tan^{2k+1}(x)\,dx&=\frac{1}{2k}\tan^{2k}(x)-\frac{1}{2k-2}\tan^{2k-2}(x)+\frac{1}{2k-4}\tan^{2k-4}(x)+\ldots\\
&{}\quad\quad\quad{}\ldots+(-1)^{k-2}\frac{1}{4}\tan^4(x)+(-1)^{k-1}\frac{1}{2}\tan^2(x)+(-1)^{k-1}\ln|\cos(x)|+C.
\end{align*}
$$

:::

## The Weierstrass substitution

In the section on integration by substitution we have already seen the **Weierstrass substitution** or the **tangent half-angle substitution**, which converts an integral of a rational function of trigonometric functions into an integral of an ordinary rational function.

The method is named after the German mathematician [Karl Theodor Wilhelm Weierstrass (1815-1897)](https://en.wikipedia.org/wiki/Karl_Weierstrass).

For $-\pi<x<\pi$ we set $t=\tan(\frac{1}{2}x)$ or $x=2\arctan(t)$. Then we have (see {eq}`Eq:Integration:Weierstrass`)

$$
\sin(\tfrac{1}{2}x)=\frac{t}{\sqrt{1+t^2}}\quad\text{and}\quad\cos(\tfrac{1}{2}x)=\frac{1}{\sqrt{1+t^2}}.
$$

This leads to

$$\sin(x)=2\sin(\tfrac{1}{2}x)\cos(\tfrac{1}{2}x)=\frac{2t}{1+t^2}\quad\text{and}\quad\cos(x)=\cos^2(\tfrac{1}{2}x)-\sin^2(\tfrac{1}{2}x)=\frac{1-t^2}{1+t^2}.
$$

Furthermore, we have $dx=\dfrac{2\,dt}{1+t^2}$.

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsWeierstrassExample
Evaluate $\displaystyle\int\frac{dx}{1+\cos(x)}$.

Solution. Let $t=\tan(\frac{1}{2}x)$, then we have $\cos(x)=\dfrac{1-t^2}{1+t^2}$ and $dx=\dfrac{2\,dt}{1+t^2}$. Hence

$$
\int\frac{dx}{1+\cos(x)}=\int\frac{1}{1+\dfrac{1-t^2}{1+t^2}}\cdot\frac{2\,dt}{1+t^2}=\int1\,dt=t+C=\tan(\tfrac{1}{2}x)+C.
$$

::::::

::::{exercise}
:label: Exc:Integration:TrigFunctionsWeierstrassExample
Show that $\displaystyle\frac{d}{dx}\left(\tan(\tfrac{1}{2}x)\right)=\frac{1}{1+\cos(x)}$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsWeierstrassExample`
:class: solution, dropdown
 
$$
\frac{d}{dx}\left(\tan(\tfrac{1}{2}x)\right)=\frac{1}{2\cos^2(\frac{1}{2}x)}=\frac{1}{1+\cos(x)}.
$$

or

$$
\frac{d}{dx}\left(\tan(\tfrac{1}{2}x)\right)=\frac{d}{dx}\left(\frac{\sin(\tfrac{1}{2}x)}{\cos(\frac{1}{2}x)}\right)=\frac{\frac{1}{2}\cos^2(\frac{1}{2})+\frac{1}{2}\sin^2(\frac{1}{2}x)}{\cos^2(\frac{1}{2}x)}=\frac{1}{2\cos^2(\frac{1}{2}x)}=\frac{1}{1+\cos(x)}.
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsWeierstrassOnePlusSin
Evaluate $\displaystyle\int\frac{dx}{1+\sin(x)}$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsWeierstrassOnePlusSin`
:class: solution, dropdown
Let $t=\tan(\frac{1}{2}x)$, then we have $\sin(x)=\dfrac{2t}{1+t^2}$ and $dx=\dfrac{2\,dt}{1+t^2}$. Hence

$$
\begin{align*}
\int\frac{dx}{1+\sin(x)}&=\int\frac{1}{1+\dfrac{2t}{1+t^2}}\cdot\frac{2\,dt}{1+t^2}=\int\frac{2}{(1+t)^2}\,dt=-\frac{2}{1+t}+C\\
&=-\frac{2}{1+\tan(\tfrac{1}{2}x)}+C=-\frac{2\cos(\frac{1}{2}x)}{\cos(\frac{1}{2}x)+\sin(\frac{1}{2}x)}+C.
\end{align*}
$$

Note that, since $-2\cos(\frac{1}{2}x)=-2\cos(\frac{1}{2}x)-2\sin(\frac{1}{2}x)+2\sin(\frac{1}{2}x)$, we have

$$
-\frac{2\cos(\frac{1}{2}x)}{\cos(\frac{1}{2}x)+\sin(\frac{1}{2}x)}=-2+\frac{2\sin(\frac{1}{2}x)}{\sin(\frac{1}{2}x)+\cos(\frac{1}{2}x)}.
$$

This implies that we can also write (with a different constant of integration)

$$
\int\frac{dx}{1+\sin(x)}=\frac{2\sin(\frac{1}{2}x)}{\sin(\frac{1}{2}x)+\cos(\frac{1}{2}x)}+C.
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsWeierstrassSinOnePlusSin
Evaluate $\displaystyle\int\frac{\sin(x)}{1+\sin(x)}\,dx$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsWeierstrassSinOnePlusSin`
:class: solution, dropdown
Let $t=\tan(\frac{1}{2}x)$, then we have $\sin(x)=\dfrac{2t}{1+t^2}$ and $dx=\dfrac{2\,dt}{1+t^2}$. Hence

$$
\int\frac{\sin(x)}{1+\sin(x)}\,dx=\int\frac{\dfrac{2t}{1+t^2}}{1+\dfrac{2t}{1+t^2}}\cdot\frac{2\,dt}{1+t^2}=\int\frac{4t}{(1+t)^2(1+t^2)}\,dt.
$$

Using partial fractions, we obtain

$$
\frac{4t}{(1+t)^2(1+t^2)}=\frac{A(1+t)+B}{(1+t)^2}+\frac{Ct+D}{1+t^2}=\frac{A}{1+t}+\frac{B}{(1+t)^2}+\frac{Ct+D}{1+t^2}
$$

and therefore

$$
\begin{align*}
4t&=A(1+t)(1+t^2)+B(1+t^2)+Ct(1+t)^2+D(1+t)^2\\
&=(A+C)t^3+(A+B+2C+D)t^2+(A+C+2D)t+A+B+D.
\end{align*}
$$

This implies that $A=0$, $B=-2$, $C=0$ and $D=2$. Hence we have

$$
\begin{align*}
\int\frac{\sin(x)}{1+\sin(x)}\,dx&=\int\left(\frac{2}{1+t^2}-\frac{2}{(1+t)^2}\right)\,dt=2\arctan(t)+\frac{2}{1+t}+C\\
&=x+\frac{2}{1+\tan(\frac{1}{2}x)}+C=x+\frac{2\cos(\frac{1}{2}x)}{\cos(\frac{1}{2}x)+\sin(\frac{1}{2}x)}+C.
\end{align*}
$$

Note that, since $2\cos(\frac{1}{2}x)=2\cos(\frac{1}{2}x)+2\sin(\frac{1}{2}x)-2\sin(\frac{1}{2}x)$, we have

$$
\frac{2\cos(\frac{1}{2}x)}{\cos(\frac{1}{2}x)+\sin(\frac{1}{2}x)}=2-\frac{2\sin(\frac{1}{2}x)}{\sin(\frac{1}{2}x)+\cos(\frac{1}{2}x)}.
$$

This implies that we can also write (with a different constant of integration)

$$
\int\frac{\sin(x)}{1+\sin(x)}\,dx=x-\frac{2\sin(\frac{1}{2}x)}{\sin(\frac{1}{2}x)+\cos(\frac{1}{2}x)}+C.
$$

:::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsWeierstrassTan
Evaluate $\displaystyle\int\tan(x)\,dx$ using the Weierstrass substitution.

Solution. Let $t=\tan(\frac{1}{2}x)$, then we have $\tan(x)=\dfrac{2t}{1-t^2}$ and $dx=\dfrac{2\,dt}{1+t^2}$. Hence

$$
\begin{align*}
\int\tan(x)\,dx&=\int\frac{2t}{1-t^2}\cdot\frac{2\,dt}{1+t^2}=\int\left(\frac{2t}{1-t^2}+\frac{2t}{1+t^2}\right)\,dt=\ln|1+t^2|-\ln|1-t^2|+C\\
&=\ln\left|\frac{1+t^2}{1-t^2}\right|+C=\ln\left|\frac{1+\tan^2(\frac{1}{2}x)}{1-\tan^2(\frac{1}{2}x)}\right|+C=\ln\left|\frac{\cos^2(\frac{1}{2}x)+\sin^2(\frac{1}{2}x)}{\cos^2(\frac{1}{2}x)-\sin^2(\frac{1}{2}x)}\right|+C\\
&=\ln\left|\frac{1}{\cos(x)}\right|+C=-\ln|\cos(x)|+C.
\end{align*}
$$

::::::

Let us apply the Weierstrass substitution to the integrals $\displaystyle\int\frac{dx}{\sin(x)}$ and $\displaystyle\int\frac{dx}{\cos(x)}$:

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsWeierstrassSin
Evaluate $\displaystyle\int\frac{dx}{\sin(x)}$ using the Weierstrass substitution.

Solution. Let $t=\tan(\frac{1}{2}x)$, then we have $\sin(x)=\dfrac{2t}{1+t^2}$ and $dx=\dfrac{2\,dt}{1+t^2}$ and thus

$$
\begin{align*}
\int\frac{dx}{\sin(x)}&=\int\frac{1}{\dfrac{2t}{1+t^2}}\cdot\frac{2\,dt}{1+t^2}=\int\frac{dt}{t}=\ln|t|+C=\ln\left|\tan(\tfrac{1}{2}x)\right|+C.
\end{align*}
$$

::::::

::::{exercise}
:label: Exc:Integration:TrigFunctionsWeierstrassSin
Show that $\displaystyle\frac{d}{dx}\left(\ln\left|\tan(\tfrac{1}{2}x)\right|\right)=\frac{1}{\sin(x)}$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsWeierstrassSin`
:class: solution, dropdown

$$
\frac{d}{dx}\left(\ln\left|\tan(\tfrac{1}{2}x)\right|\right)=\frac{1}{\tan(\frac{1}{2}x)}\cdot\frac{1}{\cos^2(\frac{1}{2}x)}\cdot\frac{1}{2}=\frac{1}{2\sin(\frac{1}{2}x)\cos(\frac{1}{2}x)}=\frac{1}{\sin(x)}.
$$

:::

::::::{prf:Example}
:label: Ex:Integration:TrigFunctionsWeierstrassCos
Evaluate $\displaystyle\int\frac{dx}{\cos(x)}$ using the Weierstrass substitution.

Solution. Let $t=\tan(\frac{1}{2}x)$, then we have $\cos(x)=\dfrac{1-t^2}{1+t^2}$ and $dx=\dfrac{2\,dt}{1+t^2}$ and thus

$$
\begin{align*}
\int\frac{dx}{\cos(x)}&=\int\frac{1}{\dfrac{1-t^2}{1+t^2}}\cdot\frac{2\,dt}{1+t^2}=\int\frac{2\,dt}{1-t^2}=\int\left(\frac{1}{1+t}+\frac{1}{1-t}\right)\,dt\\
&=\ln|1+t|-\ln|1-t|+C=\ln\left|\frac{1+t}{1-t}\right|+C=\ln\left|\frac{1+\tan(\frac{1}{2}x)}{1-\tan(\frac{1}{2}x)}\right|+C.
\end{align*}
$$

::::::

::::{exercise}
:label: Exc:Integration:TrigFunctionsWeierstrassCos
Show that $\displaystyle\frac{d}{dx}\left(\ln\left|\frac{1+\tan(\frac{1}{2}x)}{1-\tan(\frac{1}{2}x)}\right|\right)=\frac{1}{\cos(x)}$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsWeierstrassSin`
:class: solution, dropdown

$$
\begin{align*}
\frac{d}{dx}\left(\ln\left|\frac{1+\tan(\frac{1}{2}x)}{1-\tan(\frac{1}{2}x)}\right|\right)&=\frac{1-\tan(\frac{1}{2}x)}{1+\tan(\frac{1}{2}x)}\cdot\frac{\dfrac{1}{2\cos^2(\frac{1}{2}x)}(1-\tan(\frac{1}{2}x))+\dfrac{1}{2\cos^2(\frac{1}{2}x)}(1+\tan(\frac{1}{2}x))}{(1-\tan(\frac{1}{2}x))^2}\\
&=\frac{1}{2\cos^2(\frac{1}{2}x)}\cdot\frac{2}{1-\tan^2(\frac{1}{2}x)}=\frac{1}{\cos^2(\frac{1}{2}x)-\sin^2(\frac{1}{2}x)}=\frac{1}{\cos(x)}.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsWeierstrassSinCos
Evaluate $\displaystyle\int\frac{dx}{3\sin(x)+4\cos(x)}$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsWeierstrassSinCos`
:class: solution, dropdown
Using the Weierstrass substitution $t=\tan(\frac{1}{2}x)$, we have

$$
\sin(x)=\frac{2t}{1+t^2},\quad\cos(x)=\frac{1-t^2}{1+t^2}\quad\text{and}\quad dx=\frac{2\,dt}{1+t^2}.
$$

Hence we have

$$
\begin{align*}
\int\frac{dx}{3\sin(x)+4\cos(x)}&=\int\frac{1}{\dfrac{6t}{1+t^2}+\dfrac{4-4t^2}{1+t^2}}\cdot\frac{2\,dt}{1+t^2}=\int\frac{2}{6t+4-4t^2}\,dt\\
&=\int\frac{dt}{2+3t-2t^2}=\int\frac{dt}{(2-t)(1+2t)}=\frac{1}{5}\int\left(\frac{2}{1+2t}+\frac{1}{2-t}\right)\,dt\\
&=\frac{1}{5}\left(\ln|2t+1|-\ln|2-t|\right)+C=\frac{1}{5}\ln\left|\frac{2t+1}{2-t}\right|+C\\
&=\frac{1}{5}\ln\left|\frac{2\tan(\frac{1}{2}x)+1}{2-\tan(\frac{1}{2}x)}\right|+C=\frac{1}{5}\ln\left|\frac{2\sin(\frac{1}{2}x)+\cos(\frac{1}{2}x)}{2\cos(\frac{1}{2}x)-\sin(\frac{1}{2}x)}\right|+C.
\end{align*}
$$

:::

## (Grasple) exercises

::::{exercise}
:label: Exc:Integration:TrigFunctionsExercise1
Use $\cos(2\theta)=2\cos^2(\theta)-1$ to evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\sqrt{1+\cos(x)}\,dx$. 
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsExercise1`
:class: solution, dropdown
Since $1+\cos(x)=2\cos^2(\frac{1}{2}x)$ we obtain

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\sqrt{1+\cos(x)}\,dx&=\int_0^{\frac{1}{2}\pi}\sqrt{2\cos^2(\tfrac{1}{2}x)}\,dx=\sqrt{2}\int_0^{\frac{1}{2}\pi}\left|\cos(\tfrac{1}{2}x)\right|\,dx=\sqrt{2}\int_0^{\frac{1}{2}\pi}\cos(\tfrac{1}{2}x)\,dx\\
&=2\sqrt{2}\sin(\tfrac{1}{2}x)\bigg|_0^{\frac{1}{2}\pi}=2\sqrt{2}\cdot\tfrac{1}{2}\sqrt{2}=2.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsExercise2
Use $\cos(2\theta)=1-2\sin^2(\theta)$ to evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\sqrt{1-\cos(x)}\,dx$. 
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsExercise2`
:class: solution, dropdown
Since $1-\cos(x)=2\sin^2(\frac{1}{2}x)$ we obtain

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\sqrt{1-\cos(x)}\,dx&=\int_0^{\frac{1}{2}\pi}\sqrt{2\sin^2(\tfrac{1}{2}x)}\,dx=\sqrt{2}\int_0^{\frac{1}{2}\pi}\left|\sin(\tfrac{1}{2}x)\right|\,dx=\sqrt{2}\int_0^{\frac{1}{2}\pi}\sin(\tfrac{1}{2}x)\,dx\\
&=-2\sqrt{2}\cos(\tfrac{1}{2}x)\bigg|_0^{\frac{1}{2}\pi}=-2\sqrt{2}\cdot\tfrac{1}{2}\sqrt{2}+2\sqrt{2}=2\sqrt{2}-2.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsExercise3
Use $1=\sin^2(\theta)+\cos^2(\theta)$ and $\sin(2\theta)=2\sin(\theta)\cos(\theta)$ to evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\sqrt{1-\sin(x)}\,dx$. 
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsExercise3`
:class: solution, dropdown
Since $1-\sin(x)=\sin^2(\frac{1}{2}x)+\cos^2(\frac{1}{2}x)-2\sin(\frac{1}{2}x)\cos(\frac{1}{2}x)$ we find

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\sqrt{1-\sin(x)}\,dx&=\int_0^{\frac{1}{2}\pi}\sqrt{\sin^2(\tfrac{1}{2}x)-2\sin(\tfrac{1}{2}x)\cos(\tfrac{1}{2}x)+\cos^2(\tfrac{1}{2}x)}\,dx\\
&=\int_0^{\frac{1}{2}\pi}\sqrt{\left(\sin(\tfrac{1}{2}x)-\cos(\tfrac{1}{2}x)\right)^2}\,dx=\int_0^{\frac{1}{2}\pi}\left|\sin(\tfrac{1}{2}x)-\cos(\tfrac{1}{2}x)\right|\,dx.
\end{align*}
$$

Note that $\sin(\frac{1}{2}x)\leq\cos(\frac{1}{2}x)$ for $0\leq x\leq\tfrac{1}{2}\pi$. Hence we have

$$
\int_0^{\frac{1}{2}\pi}\sqrt{1-\sin(x)}\,dx=\int_0^{\frac{1}{2}\pi}\left(\cos(\tfrac{1}{2}x)-\sin(\tfrac{1}{2}x)\right)\,dx=\bigg[2\sin(\tfrac{1}{2}x)+2\cos(\tfrac{1}{2}x)\bigg]_0^{\frac{1}{2}\pi}=2\sqrt{2}-2.
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsExercise4
Use $1=\sin^2(\theta)+\cos^2(\theta)$ and $\sin(2\theta)=2\sin(\theta)\cos(\theta)$ to evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\sqrt{1+\sin(x)}\,dx$. 
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsExercise4`
:class: solution, dropdown
Since $1+\sin(x)=\sin^2(\frac{1}{2}x)+\cos^2(\frac{1}{2}x)+2\sin(\frac{1}{2}x)\cos(\frac{1}{2}x)$ we find

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\sqrt{1+\sin(x)}\,dx&=\int_0^{\frac{1}{2}\pi}\sqrt{\sin^2(\tfrac{1}{2}x)+2\sin(\tfrac{1}{2}x)\cos(\tfrac{1}{2}x)+\cos^2(\tfrac{1}{2}x)}\,dx\\
&=\int_0^{\frac{1}{2}\pi}\sqrt{\left(\sin(\tfrac{1}{2}x)+\cos(\tfrac{1}{2}x)\right)^2}\,dx=\int_0^{\frac{1}{2}\pi}\left|\sin(\tfrac{1}{2}x)+\cos(\tfrac{1}{2}x)\right|\,dx.
\end{align*}
$$

Note that $\sin(\frac{1}{2}x)+\cos(\frac{1}{2}x)\geq0$ for $0\leq x\leq\tfrac{1}{2}\pi$. Hence we have

$$
\int_0^{\frac{1}{2}\pi}\sqrt{1+\sin(x)}\,dx=\int_0^{\frac{1}{2}\pi}\left(\cos(\tfrac{1}{2}x)+\sin(\tfrac{1}{2}x)\right)\,dx=\bigg[2\sin(\tfrac{1}{2}x)-2\cos(\tfrac{1}{2}x)\bigg]_0^{\frac{1}{2}\pi}=2.
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsExercise5
Evaluate $\displaystyle\int\cos(x)\cos(2x)\cos(3x)\,dx$. 
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsExercise5`
:class: solution, dropdown
Note that $\cos(x)\cos(2x)=\frac{1}{2}\left(\cos(x)+\cos(3x)\right)$ and therefore

$$
\begin{align*}
\cos(x)\cos(2x)\cos(3x)&=\frac{1}{2}\cos(x)\cos(3x)+\frac{1}{2}\cos(3x)\cos(3x)\\
&=\frac{1}{4}\cos(2x)+\frac{1}{4}\cos(4x)+\frac{1}{4}+\frac{1}{4}\cos(6x).
\end{align*}
$$

Hence, we have

$$
\begin{align*}
\int\cos(x)\cos(2x)\cos(3x)\,dx&=\frac{1}{4}\int\left(1+\cos(2x)+\cos(4x)+\cos(6x)\right)\,dx\\
&=\frac{1}{4}x+\frac{1}{8}\sin(2x)+\frac{1}{16}\sin(4x)+\frac{1}{24}\sin(6x)+C.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:Integration:TrigFunctionsExercise6
Evaluate $\displaystyle\int\sin(x)\sin(2x)\sin(3x)\,dx$. 
::::

:::{admonition} Solution of {numref}`Exc:Integration:TrigFunctionsExercise6`
:class: solution, dropdown
Note that $\sin(x)\sin(2x)=\frac{1}{2}\left(\cos(x)-\cos(3x)\right)$ and therefore

$$
\begin{align*}
\sin(x)\sin(2x)\sin(3x)&=\frac{1}{2}\cos(x)\sin(3x)-\frac{1}{2}\cos(3x)\sin(3x)\\
&=\frac{1}{4}\sin(2x)+\frac{1}{4}\sin(4x)-\frac{1}{4}\sin(6x).
\end{align*}
$$

Hence, we have

$$
\begin{align*}
\int\sin(x)\sin(2x)\sin(3x)\,dx&=\frac{1}{4}\int\left(\sin(2x)+\sin(4x)-\sin(6x)\right)\,dx\\
&=-\frac{1}{8}\cos(2x)-\frac{1}{16}\cos(4x)+\frac{1}{24}\cos(6x)+C.
\end{align*}
$$

:::
