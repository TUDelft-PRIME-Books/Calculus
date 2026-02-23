(Sec:ODE2:Inhomogeneous)=

# Inhomogeneous problems with constant coefficients

In this section we cover:

- Method of undetermined coefficients: basic cases
- Method of undetermined coefficients: advanced cases (sums, products, guess is already solution, etc.)
- Application examples:
  - Mass-spring
  - RLC electrical circuits 
- Include IVPs and BVPs examples.
- Include examples that show when method of undetermined coefficients cannot be used and not always work (e.g. $\ldots=\sqrt{t}$).

We consider inhomogeneous second-order differential equations with *constant coefficients*

$$
ay''+by'+cy=G(x),\quad a,b,c\in\mathbb{R},\quad a\neq0,\quad G(x)\not\equiv0.
$$

The general solution $y_h(x)$ of the corresponding homogeneous differential equation can be found using the method explained in the previous section. So, we only need an arbitrary particular solution $y_p(x)$ of the inhomogeneous equation to find the general solution $y(x)=y_p(x)+y_h(x)$.

<b>The method of undetermined coefficients</b>

In some cases we will be able to find such a particular solution by guessing its form, with one or more coefficients, and then deduce the values of these coefficients by substitution. This is called the **method of undetermined coefficients**.

This method can be applied when the right-hand side $G(x)$ is an exponential function, a polynomial, a sine, a cosine or a combination of these functions.

We start with the situation that the right-hand side $G(x)$ is an exponential function. If this exponential function is not a solution of the corresponding homogeneous differential equation, we might just take a constant times the exponential equation as a 'guess' for a particular solution.

::::::{prf:example}
If $y''-2y'-8y=e^{3x}$, then $y_h(x)=c_1e^{-2x}+c_2e^{4x}$. Now take $y_p(x)=Ae^{3x}$, then we have $y_p'(x)=3Ae^{3x}$ and $y_p''(x)=9Ae^{3x}$. Substitution then gives

$$
9Ae^{3x}-6Ae^{3x}-8Ae^{3x}=e^{3x}\quad\Longleftrightarrow\quad-5Ae^{3x}=e^{3x}\quad\Longleftrightarrow\quad A=-\tfrac{1}{5}.
$$

Hence: $y_p(x)=-\frac{1}{5}e^{3x}$ is a particular solution. Then the general solution is: $y(x)=-\frac{1}{5}e^{3x}+c_1e^{-2x}+c_2e^{4x}$ with $c_1,c_2\in\mathbb{R}$.
::::::

If the exponential function is a solution of the corresponding homogeneous differential equation, this will not work since every constant multiplied by the exponential function will give zero when we substitute this into the left-hand side of the differential equation. Similarly as in the case of 'double' roots of the characteristic equation, we multiply by a factor $x$ (the variable). 

::::::{prf:example}
If $y''-2y'-8y=e^{4x}$, then $y_h(x)=c_1e^{-2x}+c_2e^{4x}$. Now, take $y_p(x)=Axe^{4x}$, then we have $y_p'(x)=A(4x+1)e^{4x}$ and $y_p''(x)=A(16x+8)e^{4x}$. Substitution then gives

$$
\begin{align*}
A(16x+8)e^{4x}-A(8x+2)e^{4x}-8Axe^{4x}=e^{4x}&\quad\Longleftrightarrow\quad6Ae^{4x}=e^{4x}\\
&\quad\Longleftrightarrow\quad A=\tfrac{1}{6}.
\end{align*}
$$

Hence: $y_p(x)=\frac{1}{6}xe^{4x}$ is a particular solution. Then the general solution is: $y(x)=\frac{1}{6}xe^{4x}+c_1e^{-2x}+c_2e^{4x}$ with $c_1,c_2\in\mathbb{R}$.
::::::

Combinations of exponential functions can be treated likewise.

::::::{prf:example}
If $y''-2y'-8y=8e^{2x}-6e^{-2x}$, then $y_h(x)=c_1e^{-2x}+c_2e^{4x}$. Now take $y_p(x)=Ae^{2x}+Bxe^{-2x}$, then we have $y_p'(x)=2Ae^{2x}+B(-2x+1)$ and $y_p''(x)=4Ae^{2x}+B(4x-2)e^{-2x}$. Substitution then gives

$$
\begin{align*}
&4Ae^{2x}+B(4x-2)e^{-2x}-4Ae^{2x}+B(4x-2)e^{-2x}-8Ae^{2x}-8Bxe^{-2x}\\
&\quad{}=8e^{2x}-6e^{-2x}\quad\Longleftrightarrow\quad -8Ae^{2x}-6Be^{-2x}=8e^{2x}-6e^{-2x}\\
&\quad\Longleftrightarrow\quad A=-1\;\text{and}\;B=1.
\end{align*}
$$

Hence: $y_p(x)=xe^{-2x}-e^{2x}$ is a particular solution. Then the general solution is: $y(x)=y_p(x)=xe^{-2x}-e^{2x}+c_1e^{-2x}+c_2e^{4x}$ with $c_1,c_2\in\mathbb{R}$.
::::::

If the exponential function and the multiplication by $x$ (the variable) are both solutions of corresponding homogeneous differential equation, we multiply by an extra factor $x$: 

::::::{prf:example}
If $y''-4y'+4y=e^{2x}$, then $y_h(x)=c_1e^{2x}+c_2xe^{2x}$. Now take $y_p(x)=Ax^2e^{2x}$, then we have $y_p'(x)=A(2x^2+2x)e^{2x}$ and $y_p''(x)=A(4x^2+8x+2)e^{2x}$. Substitution then gives

$$
\begin{align*}
&A(4x^2+8x+2)e^{2x}-A(8x^2+8x)e^{2x}+4Ax^2e^{2x}=e^{2x}\\
&{}\quad\Longleftrightarrow\quad2Ae^{2x}=e^{2x}\quad\Longleftrightarrow\quad A=\tfrac{1}{2}.
\end{align*}
$$

Hence: $y_p(x)=\frac{1}{2}x^2e^{2x}$ is a particular solution. Then the general solution is: $y(x)=\frac{1}{2}x^2e^{2x}+c_1e^{2x}+c_2xe^{2x}$ with $c_1,c_2\in\mathbb{R}$.
::::::

If the exponential function is multiplied by a polynomial, we take the exponential function multiplied by a general polynomial of the same degree.

::::::{prf:example}
If $y''-2y'-8y=5xe^{3x}$, then $y_h(x)=c_1e^{-2x}+c_2e^{4x}$. Now take $y_p(x)=(Ax+B)e^{3x}$, then we have $y_p'(x)=(3Ax+A+3B)e^{3x}$ and $y_p''(x)=(9Ax+6A+9B)e^{3x}$. Substitution then gives

$$
\begin{align*}
&(9Ax+6A+9B-6Ax-2A-6B-8Ax-8B)e^{3x}=5xe^{3x}\\
&{}\quad\Longleftrightarrow\quad(-5Ax+4A-5B)e^{3x}=5xe^{3x}\\
&{}\quad\Longleftrightarrow\quad -5A=5\;\text{and}\;4A-5B=0\quad\Longleftrightarrow\quad A=-1\;\text{and}\;B=-\tfrac{4}{5}.
\end{align*}
$$

Hence: $y_p(x)=-(x+\frac{4}{5})e^{3x}$ is a particular solution. Then the general solution is: $y(x)=-(x+\frac{4}{5})e^{3x}+c_1e^{-2x}+c_2e^{4x}$ with $c_1,c_2\in\mathbb{R}$.
::::::

If the exponential function is a solution of the corresponding homogeneous differential equation, we add an extra factor $x$ (the variable).

::::::{prf:example}
If $y''-2y'-8y=12xe^{4x}$, then $y_h(x)=c_1e^{-2x}+c_2e^{4x}$. Now take $y_p(x)=(Ax^2+Bx)e^{4x}$, then we have $y_p'(x)=(4Ax^2+2Ax+4Bx+B)e^{3x}$ and $y_p''(x)=(16Ax^2+16Ax+16Bx+8B)e^{4x}$. Substitution then gives

$$
\begin{align*}
&(16Ax^2+16Ax+16Bx+8B-8Ax^2-4Ax-8Bx-2B)e^{4x}\\
&\quad{}(-8Ax^2-8Bx)e^{4x}=12xe^{4x}\\
&\quad\Longleftrightarrow\quad(12Ax+2A+6B)e^{4x}=12xe^{4x}\\
&\quad\Longleftrightarrow\quad 12A=12\;\text{and}\;2A+6B=0\quad\Longleftrightarrow\quad A=1\;\text{and}\;B=-\tfrac{1}{3}.
\end{align*}
$$

Hence: $y_p(x)=(x^2-\frac{1}{3}x)e^{4x}$ is a particular solution. Then the general solution is: $y(x)=(x^2-\frac{1}{3}x)e^{4x}+c_1e^{-2x}+c_2e^{4x}$ with $c_1,c_2\in\mathbb{R}$.
::::::

If the right-hand side $G(x)$ is a polynomial, we just take a general polynomial of the same degree. In fact, this is the same situation as above combined with an exponential function $e^{0x}=1$.

::::::{prf:example}
If $y''+3y'+2y=4x$, then $y_h(x)=c_1e^{-x}+c_2e^{-2x}$. Now take $y_p(x)=Ax+B$, then we have $y_p'(x)=A$ and $y_p''(x)=0$. Substitution then gives

$$
\begin{align*}
0+3A+2Ax+2B=4x&\quad\Longleftrightarrow\quad 2A=4\;\text{and}\;3A+2B=0\\
&\quad\Longleftrightarrow\quad A=2\;\text{and}\;B=-3.
\end{align*}
$$

Hence: $y_p(x)=2x-3$ is a particular solution. Then the general solution is: $y(x)=2x-3+c_1e^{-x}+c_2e^{-2x}$ with $c_1,c_2\in\mathbb{R}$.
::::::

::::::{prf:example}
If $y''+4y'+5y=25x^2$, then $y_h(x)=c_1e^{-2x}\cos(x)+c_2e^{-2x}\sin(x)$. Now take $y_p(x)=Ax^2+Bx+C$, then we have $y_p'(x)=2Ax+B$ and $y_p''(x)=2A$. Substitution then gives

$$
\begin{align*}
&2A+8Ax+4B+5Ax^2+5Bx+5C=25x^2\\
&\quad\Longleftrightarrow\quad 5A=25,\;8A+5B=0\;\text{and}\;2A+4B+5C=0.
\end{align*}
$$

This implies that $A=5$, $B=-8$ and $C=\frac{22}{5}$. Hence: $y_p(x)=5x^2-8x+\frac{22}{5}$ is a particular solution. Then the general solution is: $y(x)=5x^2-8x+\frac{22}{5}+c_1e^{-2x}\cos(x)+c_2e^{-2x}\sin(x)$ with $c_1,c_2\in\mathbb{R}$.
::::::

Note that the invisible factor $e^{0x}=1$ corresponds to a root $0$ of the characteristic equation. So, in that case we have to add an extra factor $x$ (the variable).

::::::{prf:example}
If $y''+4y'=8x$, then $y_h(x)=c_1+c_2e^{-4x}$. Now take $y_p(x)=Ax^2+Bx$, then we have $y_p'(x)=2Ax+B$ and $y_p''(x)=2A$. Substitution then gives

$$
\begin{align*}
2A+8Ax+4B=8x&\quad\Longleftrightarrow\quad 8A=8\;\text{and}\;2A+4B=0\\
&\quad\Longleftrightarrow\quad A=1\;\text{and}\;B=-\tfrac{1}{2}.
\end{align*}
$$

Hence: $y_p(x)=x^2-\frac{1}{2}x$ is a particular solution. Then the general solution is: $y(x)=x^2-\frac{1}{2}x+c_1+c_2e^{-4x}$ with $c_1,c_2\in\mathbb{R}$.
::::::

If the right-hand side $G(x)$ is a sine or a cosine, we try a linear combination of the sine and the cosine as a 'guess' for a particular solution. Note that the substitution of a sine or a cosine gives rise to the other one when we differentiate.

::::::{prf:example}
If $y''-3y'+2y=10\cos(x)$, then $y_h(x)=c_1e^x+c_2e^{2x}$. Now take $y_p(x)=A\cos(x)+B\sin(x)$, then we have $y_p'(x)=-A\sin(x)+B\cos(x)$ and $y_p''(x)=-A\cos(x)-B\sin(x)$. Substitution then gives

$$
\begin{align*}
&-A\cos(x)-B\sin(x)+3A\sin(x)-3B\cos(x)\\
&\quad{}+2A\cos(x)+2B\sin(x)=10\cos(x)\\
&\quad\Longleftrightarrow\quad (A-3B)\cos(x)+(3A+B)\sin(x)=10\cos(x)\\
&\quad\Longleftrightarrow\quad A-3B=10\;\text{and}\;3A+B=0.
\end{align*}
$$

This implies that $A=1$ and $B=-3$. Hence: $y_p(x)=\cos(x)-3\sin(x)$ is a particular solution. Then the general solution is: $y(x)=\cos(x)-3\sin(x)+c_1e^x+c_2e^{2x}$ with $c_1,c_2\in\mathbb{R}$.
::::::

::::::{prf:example}
If $y''+2y'+5y=17\sin(x)$, then $y_h(x)=c_1e^{-x}\cos(2x)+c_2e^{-x}\sin(2x)$. Now take $y_p(x)=A\cos(2x)+B\sin(2x)$, then we have $y_p'(x)=-2A\sin(2x)+2B\cos(2x)$ and $y_p''(x)=-4A\cos(2x)-4B\sin(2x)$. Substitution then gives

$$
\begin{align*}
&-4A\cos(2x)-4B\sin(2x)-4A\sin(2x)+4B\cos(2x)\\
&\quad{}+5A\cos(2x)+5B\sin(2x)=17\sin(2x)\\
&\quad\Longleftrightarrow\quad(A+4B)\cos(2x)+(-4A+B)\sin(2x)=17\sin(2x)\\
&\quad\Longleftrightarrow\quad A+4B=0\;\text{and}\;-4A+B=17.
\end{align*}
$$

This implies that $A=-4$ and $B=1$. Hence: $y_p(x)=-4\cos(x)+\sin(x)$ is a particular solution. Then the general solution is: $y(x)=-4\cos(2x)+\sin(2x)+c_1e^{-x}\cos(2x)+c_2e^{-x}\sin(2x)$ with $c_1,c_2\in\mathbb{R}$.
::::::

If the right-hand side is a solution of the corresponding homogeneous differential equation, we add an extra factor $x$ (the variable) again.

::::::{prf:example}
If $y''+9y=6\sin(3x)$, then $y_h(x)=c_1\cos(3x)+c_2\sin(3x)$. Now take $y_p(x)=Ax\cos(3x)+Bx\sin(3x)$, then we have $y_p'(x)=A\left(\cos(3x)-3x\sin(3x)\right)+B\left(\sin(3x)+3x\cos(3x)\right)$ and $y_p''(x)=A\left(-6\sin(3x)-9x\cos(3x)\right)+B\left(6\cos(3x)-9x\sin(3x)\right)$. Substitution then gives

$$
\begin{align*}
&A\left(-6\sin(3x)-9x\cos(3x)\right)+B\left(6\cos(3x)-9x\sin(3x)\right)\\
&\quad{}+9Ax\cos(3x)+9Bx\sin(3x)=6\sin(3x)\\
&\quad\Longleftrightarrow\quad-6A\sin(3x)+6B\cos(3x)=6\sin(3x)\\
&\quad\Longleftrightarrow\quad A=-1\;\text{and}\;B=0.
\end{align*}
$$

Hence: $y_p(x)=-x\cos(3x)$ is a particular solution. Then the general solution is: $y(x)=-x\cos(3x)+c_1\cos(3x)+c_2\sin(3x)$ with $c_1,c_2\in\mathbb{R}$.
::::::

<b>The method of variation of parameters</b>

The method of variation of parameters, which can also be applied in cases were the method of undetermined coefficients will not work, can be found in books about differential equations.

## (Grasple) exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5bb7f21d-6b1f-46e2-9dc0-95f67f889f71?id=77062
:label: grasple_exercise_13_2_1
:dropdown:
:description: Find the general solution.
::::::