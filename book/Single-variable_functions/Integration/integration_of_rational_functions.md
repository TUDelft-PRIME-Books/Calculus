# Integration of rational functions

In this section we cover the integration of rational functions with:

- Unique linear factors
- Repeated linear factors
- Irreducible quadratic factors
- Repeated irreducible quadratic factors

In this section we consider integrals of rational functions. A **rational function** is a function of the form $f(x)=\dfrac{P(x)}{Q(x)}$ with $P(x)$ and $Q(x)$ polynomials and $Q(x)\neq0$.

If the degree of $P(x)$ is greater than or equal to the degree of $Q(x)$, we first perform a long division such that

$$
f(x)=\frac{P(x)}{Q(x)}=S(x)+\frac{R(x)}{Q(x)}
$$

with $R(x)$ and $S(x)$ polynomials with the degree of the remainder $R(x)$ less than the degree of $Q(x)$.

The integral of the polynomial $S(x)$ can be evaluated directly using the fundamental theorem of calculus. The quotient $\dfrac{R(x)}{Q(x)}$ can be split into a sum of simpler quotients of which the integral is easier to evaluate.

This **partial fraction decomposition** is based on the fundamental theorem of algebra: if $Q(x)$ is a polynomial of degree $n\geq1$, then

$$
Q(x)=k_n(x-x_1)(x-x_2)\cdots(x-x_n)
$$

with $x_i\in\mathbb{C}$ for $i=1,2,3,\ldots,n$. Since $Q(x)$ is a real polynomial, the zeros are either real or appear in complex conjugate pairs. This implies that $Q(x)$ can be written as a product of linear factors $x+a$ and factors of the form $(x+b)^2+c^2$ with $a,b,c\in\mathbb{R}$.

This implies that the quotient $\dfrac{R(x)}{Q(x)}$ can be written as a sum of *partial fractions* of the form

$$
\frac{A}{(x+a)^k}\quad\text{and}\quad\frac{Bx+C}{((x+b)^2+c)^m}\quad\text{with $k$ and $m$ positive integers}.
$$

We distinguish four different cases.

## $Q(x)$ only has distinct linear factors

In the section on the fundamental theorem we have seen that

$$
\int\frac{dx}{x+\alpha}=\ln|x+\alpha|+C,\quad\alpha\in\mathbb{R}.
$$

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample1
Evaluate $\displaystyle\int\frac{x^3}{x^2+5x+6}\,dx$.

Solution. We start with a long division

$$
\frac{x^3}{x^2+5x+6}=x-5+\frac{19x+30}{x^2+5x+6}.
$$

Then we factor the denomerator $x^2+5x+6$ into $(x+2)(x+3)$ and write

$$
\frac{19x+30}{x^2+5x+6}=\frac{19x+30}{(x+2)(x+3)}=\frac{A}{x+2}+\frac{B}{x+3}.
$$

Now we add the last two fractions to find that

$$
\frac{A}{x+2}+\frac{B}{x+3}=\frac{A(x+3)+B(x+2)}{(x+2)(x+3)}
$$

and compare this with the fraction $\dfrac{19x+30}{(x+2)(x+3)}$. This implies that

$$
19x+30=A(x+3)+B(x+2)=(A+B)x+3A+2B.
$$

This implies that 

$$
\begin{cases}A+B&=19\\3A+2B&=30\end{cases}\quad\Longrightarrow\quad A=-8\quad\text{and}\quad B=27.
$$

Hence, we have

$$
\begin{align*}
\int\frac{x^3}{x^2+5x+6}\,dx&=\int\left(x-5-\frac{8}{x+2}+\frac{27}{x+3}\right)\,dx\\
&=\frac{1}{2}x^2-5x-8\ln|x+2|+27\ln|x+3|+C.
\end{align*}
$$

*Remark*: in order to avoid problems the zeros $-2$ and $-3$ of the denominator of the integrand should not be in the interval of integration. See the section on improper integrals for more details.
::::::

::::::{note}
There is another way to find the coefficients $A$ and $B$ in

$$
19x+30=A(x+3)+B(x+2).
$$

Although the zeros $-2$ and $-3$ should not be in the interval of integration, the polynomials on the left-hand side and on the right-hand side of the equation should coincide at all points of the interval of integration (an infinite number of points). Hence, since polynomials are continuous for all values of $x\in\mathbb{R}$, the polynomials should coincide for all values of $x\in\mathbb{R}$. Even for $x=-2$ and $x=-3$. If we substitute these values, we obtain

$$
19(-2)+30=A(-2+3)+B(-2+2)\quad\Longleftrightarrow\quad-8=A
$$

and

$$
19(-3)+30=A(-3+3)+B(-3+2)\quad\Longleftrightarrow\quad-27=-B.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample2
Evaluate $\displaystyle\int\frac{6x^2-4x-1}{2x^3+x^2-x}\,dx$.

Solution. Note that $2x^3+x^2-x=x(2x-1)(x+1)$ and therefore

$$
\frac{6x^2-4x-1}{2x^3+x^2-x}=\frac{A}{x}+\frac{B}{2x-1}+\frac{C}{x+1}.
$$

This leads to

$$
6x^2-4x-1=A(2x-1)(x+1)+Bx(x+1)+Cx(2x-1).
$$

Substituting $x=0$, $x=\frac{1}{2}$ and $x=-1$ we obtain: $A=1$, $B=-2$ and $C=3$.

Hence, we have

$$
\int\frac{6x^2-4x-1}{2x^3+x^2-x}\,dx=\int\left(\frac{1}{x}-\frac{2}{2x-1}+\frac{3}{x+1}\right)\,dx=\ln|x|-\ln|x-\tfrac{1}{2}|+3\ln|x+1|+C.
$$

Note that $\ln|2x-1|=\ln|2(x-\frac{1}{2})|=\ln(2)+\ln|x-\frac{1}{2}|$. This implies that the answer can also be written as (with a different  constant of integration)

$$
\int\frac{6x^2-4x-1}{2x^3+x^2-x}\,dx=\ln|x|-\ln|2x-1|+3\ln|x+1|+C.
$$

*Remark*: Instead of substituting the zeros of the denominator, we could have used

$$
6x^2-4x-1=(2A+B+2C)x^2+(A+B-C)x-A,
$$

which leads to $A=1$ and 

$$
\begin{cases}B-C=-5\\B+2C=4\end{cases}\quad\Longrightarrow\quad\begin{cases}B=-2\\C=3.\end{cases}
$$

::::::

::::{exercise}
:label: Exc:Integration:RationalFunctionsExercise1
Prove that $\displaystyle\int\frac{dx}{x^2-\alpha^2}=\frac{1}{2\alpha}\ln\left|\frac{x-\alpha}{x+\alpha}\right|+C$ for $\alpha\neq0$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:RationalFunctionsExercise1`
:class: solution, dropdown
Note that $x^2-\alpha^2=(x-\alpha)(x+\alpha)$ and

$$
\frac{1}{x^2-\alpha^2}=\frac{A}{x-\alpha}+\frac{B}{x+\alpha}=\frac{A(x+\alpha)+B(x-\alpha)}{(x-\alpha)(x+\alpha)}
$$

with $A=\dfrac{1}{2\alpha}$ and $B=-\dfrac{1}{2\alpha}$. Hence, we have

$$
\begin{align*}
\int\frac{dx}{x^2-\alpha^2}&=\frac{1}{2\alpha}\int\left(\frac{1}{x-\alpha}-\frac{1}{x+\alpha}\right)\,dx=\frac{1}{2\alpha}\left(\ln|x-\alpha|-\ln|x+\alpha|\right)+C\\
&=\frac{1}{2\alpha}\ln\left|\frac{x-\alpha}{x+\alpha}\right|+C.
\end{align*}
$$

:::

## $Q(x)$ contains repeated linear factors

For $k\in\{2,3,4,\ldots\}$ we have

$$
\int\frac{dx}{(x+\alpha)^k}=-\frac{1}{k-1}\cdot\frac{1}{(x+\alpha)^{k-1}}+C,\quad\alpha\in\mathbb{R}.
$$

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample3
Evaluate $\displaystyle\int\frac{x^2}{x^2+2x+1}\,dx$.

Solution. We have

$$
\frac{x^2}{x^2+2x+1}=1-\frac{2x+1}{x^2+2x+1}=1-\frac{2x+1}{(x+1)^2}.
$$

In this case we obtain

$$
\frac{2x+1}{(x+1)^2}=\frac{A(x+1)+B}{(x+1)^2}=\frac{A}{x+1}+\frac{B}{(x+1)^2}
$$

with $A=2$ and $B=-1$. Hence we have

$$
\int\frac{x^2}{x^2+2x+1}\,dx=\int\left(1-\frac{2}{x+1}+\frac{1}{(x+1)^2}\right)\,dx=x-2\ln|x+1|-\frac{1}{x+1}+C.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample4
Evaluate $\displaystyle\int\frac{x(3x+5)}{(x+1)^3}\,dx$.

Solution. Note that

$$
\frac{x(3x+5)}{(x+1)^3}=\frac{A(x+1)^2+B(x+1)+C}{(x+1)^2}=\frac{A}{x+1}+\frac{B}{(x+1)^2}+\frac{C}{(x+1)^3},
$$

which leads to

$$
x(3x+5)=A(x+1)^2+B(x+1)+C=Ax^2+(2A+B)x+A+B+C.
$$

Hence: $A=3$, $B=-1$ and $C=-2$. We conclude that

$$
\begin{align*}
\int\frac{x(3x+5)}{(x+1)^3}\,dx&=\int\left(\frac{3}{x+1}-\frac{1}{(x+1)^2}-\frac{2}{(x+1)^3}\right)\,dx\\
&=3\ln|x+1|+\frac{1}{x+1}+\frac{1}{(x+1)^2}+C.
\end{align*}
$$

::::::

## $Q(x)$ contains irreducible quadratic factors

In the section on substitution we obtained

$$
\int\frac{dx}{x^2+\alpha^2}=\frac{1}{\alpha}\arctan\left(\frac{x}{\alpha}\right)+C,\quad\alpha\in\mathbb{R}\setminus\{0\}
$$

and

$$
\int\frac{x}{x^2+\alpha^2}\,dx=\frac{1}{2}\ln(x^2+\alpha^2)+C,\quad\alpha\in\mathbb{R}.
$$

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample5
Evaluate $\displaystyle\int\frac{6x^3-7x^2+12x-4}{x^4+5x^2+4}\,dx$.

Solution. We have

$$
\frac{6x^3-7x^2+12x-4}{x^4+5x^2+4}=\frac{6x^3-7x^2+12x-4}{(x^2+1)(x^2+4)}=\frac{Ax+B}{x^2+1}+\frac{Cx+D}{x^2+4},
$$

which implies that

$$
\begin{align*}
6x^3-7x^2+12x-4&=(Ax+B)(x^2+4)+(Cx+D)(x^2+1)\\
&=(A+C)x^3+(B+D)x^2+(4A+C)x+4B+D.
\end{align*}
$$

Hence we have

$$
\begin{cases}A+C=6\\B+D=-7\\4A+C=12\\4B+D=-4\end{cases}\quad\Longleftrightarrow\quad\begin{cases}A+C=6\\4A+C=12\end{cases}\quad\text{and}\quad\begin{cases}B+D=-7\\4B+D=-4,\end{cases}
$$

which lead to $A=2$ and $C=4$ and to $B=1$ and $D=-8$. We conclude that

$$
\begin{align*}
\int\frac{6x^3-7x^2+12x-4}{x^4+5x^2+4}\,dx&=\int\left(\frac{2x+1}{x^2+1}+\frac{4x-8}{x^2+4}\right)\,dx\\
&=\ln(x^2+1)+\arctan(x)+2\ln(x^2+4)-4\arctan(\tfrac{1}{2}x)+C.
\end{align*}
$$

::::::

Sometimes we need a substitution:

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample6
Evaluate $\displaystyle\int\frac{2x+5}{x^2+4x+8}\,dx$.

Solution. Note that $x^2+4x+8=(x+2)^2+4$. Hence, using the substitution $u=x+2$, we have

$$
\begin{align*}
\int\frac{2x+5}{x^2+4x+8}\,dx&=\int\frac{2(x+2)+1}{(x+2)^2+4}\,d(x+2)=\int\frac{2u+1}{u^2+4}\,du\\
&=\ln(u^2+4)+\frac{1}{2}\arctan\left(\frac{u}{2}\right)+C\\
&=\ln((x+2)^2+4)+\frac{1}{2}\arctan\left(\frac{x+2}{2}\right)+C\\
&=\ln(x^2+4x+8)+\frac{1}{2}\arctan\left(\frac{x+2}{2}\right)+C.
\end{align*}
$$

::::::

## $Q(x)$ contains repeated irreducible quadratic factors

For integrals of the form $\displaystyle\int\frac{x}{(x^2+\alpha^2)^m}\,dx$ with $m\in\{2,3,4,\ldots\}$ and $\alpha\neq0$ we have

$$
\int\frac{x}{(x^2+\alpha^2)^m}\,dx=-\frac{1}{2(m-1)}\cdot\frac{1}{(x^2+\alpha^2)^{m-1}}+C.
$$

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsExample7
Evaluate $\displaystyle\int\frac{2x^7+x^6+12x^5+5x^4+16x^3+8x^2+4x+4}{(x^2+1)^2(x^2+2)^2}\,dx$.

Solution. We have

$$
\frac{2x^7+x^6+12x^5+5x^4+16x^3+8x^2+4x+4}{(x^2+1)^2(x^2+2)^2}=\frac{Ax+B}{x^2+1}+\frac{Cx+D}{(x^2+1)^2}+\frac{Ex+F}{x^2+2}+\frac{Gx+H}{(x^2+2)^2}.
$$
 
In order to find the coefficients we set $2x^7+x^6+12x^5+5x^4+16x^3+8x^2+4x+4$ equal to

$$
\begin{align*}
&(Ax+B)(x^2+1)(x^2+2)^2+(Cx+D)(x^2+2)^2\\
&{}\quad\quad{}+(Ex+F)(x^2+2)(x^2+1)^2+(Gx+H)(x^2+1)^2\\
&{}=(A+E)x^7+(B+F)x^6+(5A+C+4E+G)x^5+(5B+D+4F+H)x^4\\
&{}\quad\quad{}+(8A+4C+5E+2G)x^3+(8B+4D+5F+2H)x^2\\
&{}\quad\quad\quad\quad\quad{}+(4A+4C+2E+G)x+4B+4D+2F+H
\end{align*}
$$

We skip the tedious computations, which could be done using a computer, that lead to $A=2$, $B=1$, $C=-2$, $D=0$, $E=0$, $F=0$, $G=4$ and $H=0$. Hence we have

$$
\begin{align*}
&\int\frac{2x^7+x^6+12x^5+5x^4+16x^3+8x^2+4x+4}{(x^2+1)^2(x^2+2)^2}\,dx\\
&{}\quad\quad{}=\int\left(\frac{2x+1}{x^2+1}-\frac{2x}{(x^2+1)^2}+\frac{4x}{(x^2+2)^2}\right)\,dx\\
&{}\quad\quad{}=\ln(x^2+1)+\arctan(x)+\frac{1}{2(x^2+1)^2}-\frac{1}{(x^2+2)^2}+C.
\end{align*}
$$

::::::

Note that we were lucky that $D=0$ and $H=0$ in this example. Otherwise, we had to deal with the integrals 

$$
\int\frac{dx}{(x^2+1)^2}\quad\text{and}\quad\int\frac{dx}{(x^2+2)^2}.
$$ 

For integrals of the form $\displaystyle\int\frac{dx}{(x^2+\alpha^2)^m}$ with $m\in\{2,3,4,\ldots\}$ and $\alpha\neq0$ we use the substitution $x=\alpha\tan(t)$ (compare with the trigonometric substitutions) with $dx=\alpha(1+\tan^2(t))\,dt$. Then we obtain

$$
\frac{dx}{(x^2+\alpha^2)^m}=\frac{\alpha(1+\tan^2(t))}{\alpha^2(1+\tan^2(t))^m}\,dt=\frac{1}{\alpha}\frac{dt}{(1+\tan^2(t))^{m-1}}=\frac{1}{\alpha}\cos^{2m-2}(t)\,dt.
$$

Hence we have: $\displaystyle\int\frac{dx}{(x^2+\alpha^2)^m}=\frac{1}{\alpha}\int\cos^{2m-2}(t)\,dt$. In the next section we will consider trigonometric integrals in more details. Here we only give two examples.

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsRepeatedExample1
Evaluate $\displaystyle\int_0^1\frac{dx}{(1+x^2)^2}$.

Solution. Let $x=\tan(t)$, then we have $dx=(1+\tan^2(t))\,dt$ and therefore

$$
\int_0^1\frac{dx}{(1+x^2)^2}=\int_0^{\frac{1}{4}\pi}\frac{1+\tan^2(t)}{(1+\tan^2(t))^2}\,dt=\int_0^{\frac{1}{4}\pi}\frac{dt}{1+\tan^2(t)}=\int_0^{\frac{1}{4}\pi}\cos^2(t)\,dt.
$$

Now we use $\cos^2(t)=\frac{1}{2}(1+\cos(2t))$ to find that

$$
\int_0^1\frac{dx}{(1+x^2)^2}=\int_0^{\frac{1}{4}\pi}\cos^2(t)\,dt=\frac{1}{2}\int_0^{\frac{1}{4}\pi}(1+\cos(2t))\,dt=\bigg[\frac{1}{2}t+\frac{1}{4}\sin(2t)\bigg]_0^{\frac{1}{4}\pi}=\frac{1}{8}\pi+\frac{1}{4}.
$$

::::::

::::::{prf:Example}
:label: Ex:Integration:RationalFunctionsRepeatedExample2
Evaluate $\displaystyle\int_0^1\frac{dx}{(1+x^2)^3}$.

Solution. Let $x=\tan(t)$, then we have $dx=(1+\tan^2(t))\,dt$ and therefore

$$
\int_0^1\frac{dx}{(1+x^2)^3}=\int_0^{\frac{1}{4}\pi}\frac{1+\tan^2(t)}{(1+\tan^2(t))^3}\,dt=\int_0^{\frac{1}{4}\pi}\frac{dt}{(1+\tan^2(t))^2}=\int_0^{\frac{1}{4}\pi}\cos^4(t)\,dt.
$$

Now we use $\cos^2(t)=\frac{1}{2}(1+\cos(2t))$ to find that

$$
\cos^4(t)=\frac{1}{4}(1+\cos(2t))^2=\frac{1}{4}(1+2\cos(2t)+\cos^2(2t))=\frac{1}{4}+\frac{1}{2}\cos(2t)+\frac{1}{2}\cos^2(2t).
$$

Finally, using $\cos^2(2t)=\frac{1}{2}(1+\cos(4t))$, we obtain

$$
\cos^4(t)=\frac{1}{4}+\frac{1}{2}\cos(2t)+\frac{1}{8}+\frac{1}{8}\cos^2(4t)=\frac{3}{8}+\frac{1}{2}\cos(2t)+\frac{1}{8}\cos(4t).
$$

Hence, we have

$$
\begin{align*}
\int_0^1\frac{dx}{(1+x^2)^3}&=\int_0^{\frac{1}{4}\pi}\cos^4(t)\,dt=\int_0^{\frac{1}{4}\pi}\left(\frac{3}{8}+\frac{1}{2}\cos(2t)+\frac{1}{8}\cos(4t)\right)\,dt\\
&=\bigg[\frac{3}{8}t+\frac{1}{4}\sin(2t)+\frac{1}{32}\sin(4t)\bigg]_0^{\frac{1}{4}\pi}=\frac{3}{32}\pi+\frac{1}{4}.
\end{align*}
$$

::::::

## Grasple exercises
