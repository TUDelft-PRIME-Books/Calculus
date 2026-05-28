(Sec:TaylorPolynomials)=
# Approximating functions

## Introduction

Additions and multiplications are easy to compute by hand, but if you have to determine the value of $\sqrt[3]{9}$ you would probably need a calculator. The function $\sqrt[3]{x}$, however, can be approximated by polynomials. Recall, polynomials are functions that can be written as sums of multiples of powers of $x$. The functions $1+x-3x^4$ and $-2-5x^2+2x^6-x^7$ are examples of polynomials.

Function values of polynomials are easy to compute since you only need to be able to add and multiply numbers. This means that we can use these polynomials to obtain a guess of what $\sqrt[3]{9}$ should more or less be equal to. In this section you will learn how you can approximate functions by polynomials and use them to solve various problems.

## Linearisation

We already saw in {numref}`Section:Differentiability` how we can construct a tangent line to a function at a certain point. An equation for the tangent line was

$$
y = f(a) + f'(a)(x-a).
$$

The tangent line is the graph of the following linear function:

$$
L(x)=f(a)+f'(a)(x-a).
$$

This function satisfies $L(a)=f(a)$ and $L'(a)=f'(a)$, which means that the function $L$ has the same value and the same derivative as $f$ at the point $a$. Therefore, the tangent line intersect the graph of $f$ at the point $(a,f(a))$ and has the same slope as the graph of $f$ at that point.

Near the point $(a,f(a))$, the graph of the function and the tangent line are very close to each other, and the tangent line can therefore be used to approximate the graph of the function near that point. In other words, we can approximate the function $f$ by the linear function $L$ when we are close to the value $a$. This leads to the following definition and properties:

::::{prf:definition}
:label: Def:ApproximatingFunctions:Linearisation

The **linearisation** of a function $f$ at $x=a$ is given by

$$L(x)=f(a)+f'(a)(x-a).$$
::::

::::{prf:property}
:label: Prop:ApproximatingFunctions:Linearisation

Assume $L$ is the linearisation of a function $f$ at $x=a$. Then:
- The graph of $L$ is the line tangent to the graph of $f$ at  $(a, f(a))$.
- $L$ is the unique linear function such that $L(a)=f(a)$ and $L'(a)=f'(a)$.

::::

::::{prf:example}
:label: Ex:ApproximatingFunctions:cuberoot

Let us use the function $f(x)=\sqrt[3] x$ as an example and say that $a=8$. Since $f(8)=2$ and $f'(8)  =  \frac{1}{12}$, we have

$$
L(x) \ = \ 2+\frac{1}{12}(x-8).
$$

This leads to the approximation

$$
\sqrt[3] x \ \approx \  2+\frac{1}{12}(x-8).
$$

{numref}`Figure %s <Fig:ApproximatingFunctions:cuberoot>` shows the graphs of $\sqrt[3]{x}$ and of the linearisation $L(x)$.

:::{figure} Images/Fig-TaylorPolynomials-cuberoot.svg
:name: Fig:ApproximatingFunctions:cuberoot
:class: dark-light

The function $\sqrt[3]{x}$ and the linearisation $ L(x)$.

:::

:::{todo}
Replace {numref}`Fig:ApproximatingFunctions:cuberoot` with an applet.

Do not use $y=\ldots$, but $L(x)=\ldots$ and $f(x)=\ldots$ in the legend of the graph.
:::

It can be observed that for any $x$ close to $8$ the values of $f(x)$ and $L(x)$ are very close to each other.

Let us use this observation to _approximate_ $\sqrt[3]{9}$:

$$
\sqrt[3]{9} = f(9) \approx L(9) = 2+\frac{1}{12}(9-8) = 2+\frac{1}{12} = \frac{25}{12} = 2.08\overline{33}.
$$

::::

::::{question}
:type: multiple-choice
:variant: single-select
:admonition:
:class: question
:showanswer:

Consider the function

$$
f(x) = 1+2x+3x^2+4x^3+5x^4.
$$

Which of the below answers gives the linearisation $L$ of $f$ at $x=1$?
---
[ ] $\displaystyle 5(8x-5)$
> Remember that you have to be specific in mathematics. What is equal to $5(8x-5)$?
[x] $\displaystyle L(x) = -25 + 40x$
> Well done!
[ ] $\displaystyle y = 5(8x-5)$
> Remember that you have to be specific in mathematics. Is $y$ defined in the question?
[ ] $\displaystyle y = 15 + 40(x-1)$
> Remember that you have to be specific in mathematics. Is $y$ defined in the question?
[x] $\displaystyle L(x) = 15 + 40(x-1)$
> Well done!
[ ] $\displaystyle -25 + 40x$
> Remember that you have to be specific in mathematics. What is equal to $-25 + 40x$?
[x] $\displaystyle L(x) = 5(8x-5)$
> Well done!
[ ] $\displaystyle y = -25 + 40x$
> Remember that you have to be specific in mathematics. Is $y$ defined in the question?
[ ] $\displaystyle 15 + 40(x-1)$
> Remember that you have to be specific in mathematics. What is equal to $15 + 40(x-1)$?
---
::::




Another way to view linearisation, is to use it to approximate changes in function values. If we want to approximate the change in the value of a function $f$ when we change the input from $a$ to $a+h$, we can use the linearisation $L(x)$ of $f$ at $x=a$. The real change in the function value is given by

$$
\Delta f = f(a+h)-f(a). 
$$

Using the linearisation, we can approximate this change by performing the following calculation:

\begin{align*}
\Delta f &= f(a+h)-f(a) \\
& \approx L(a+h)-f(a) \\
& = \left( f(a) + f'(a)(a+h-a) \right) -f(a) \\
& = f'(a) \cdot h.
\end{align*}
In other words, we have the following property:

::::{prf:property}
:label: Prop:ApproximatingFunctions:LinearisationChange

Assume $L$ is the linearisation of a function $f$ at $x=a$. Then the **change in the value of $f$** when we change the input from $a$ to $a+h$ can be approximated by

$$
\Delta f = f(a+h)-f(a) \approx L(a+h)-f(a) = f'(a) \cdot h.
$$

The **relative change in the value of $f$** when we change the input from $a$ to $a+h$ can be approximated by

$$
\frac{\Delta f}{f(a)} = \frac{f(a+h)-f(a)}{f(a)} \approx \frac{L(a+h)-f(a)}{f(a)} = \frac{f'(a) \cdot h}{f(a)}.
$$

::::

The next example shows how we can use this property to investigate changes in function values.

:::::{margin}
:::{figure} Images/Construction.png
:name: Fig:ApproximatingFunctions:Construction
:class: dark-light
:placement: caption
:source: [Pixabay](https://pixabay.com/photos/modern-architecture-roof-construction-100973/)
:license: Pixabay License
:date: 2013-04-07
:author: PixelAnarchy

A set of cylindrical steel beams.

:::
:::::

:::::{prf:example}
:label: Ex:ApproximatingFunctions:ApproxChange

A company constructs cylindrical steel beams with a length of $8$ meter. The diameter of each beam is equal to $0.6$ meter. We wonder how much, approximately, the volume of a beam would increase if, because of a construction error, the diameter increases by $0.01$ meter.

Let $V$ be the volume of the beam and $x$ the diameter, which means

$$
V(x)=8\pi \left(\frac{x}{2} \right)^2 = 2\pi x^2,
$$

and

$$
V'(x)=4\pi x,
$$

and if the diameter increases from $x$ to $x+h$, the change in volume can be approximated by

\begin{align*}
\Delta V &= V(x+h)-V(x) \\
&\approx V'(x) h \\
&= 4\pi x h.
\end{align*}

The relative change in volume with respect to the original volume is approximately equal to

$$
\frac{\Delta V}{V(x)} \approx \frac{4\pi x h}{2\pi x^2} = \frac{2h}{x}.
$$

In our case $x=0.6$ meter and $h=0.01$ meter, so the change in volume is approximately equal to

$$
\Delta V \approx 4\pi \cdot 0.6 \cdot 0.01 \approx 0.0754 {\rm m}^3,
$$

and the relative change in volume with respect to the original volume is approximately equal to

$$
\frac{\Delta V}{V(0.6)} \approx \frac{2\cdot0.01}{0.6} \approx 0.0333,
$$

which means that the volume increases by approximately $3.33\%$ if the diameter increases by approximately $1.67\%$.

:::::


## Taylor polynomials

A linearisation $L(x)$ is a polynomial of degree one that approximates the function $f$ near the point $(a,f(a))$. From now on, we will also refer to the linearisation $L(x)$ of $f$ at $x=a$ as the _Taylor polynomial $T_1(x)$ of order[^orderVsDegree] $1$ of $f$ centred at $x=a$_. By this definition, the graph of $T_1$ is the tangent line to the graph of $f$ at the point $(a,f(a))$, so it makes sense to state that $f(x)\approx T_1(x)$ for all $x$ that are close to $a$. By the expression $f(x)\approx T_1(x)$, we mean that $T_1(x)$ is an approximation of $f(x)$.

[^orderVsDegree]: We use the term _order_ to refer to the number of derivatives that are used in the construction of the Taylor polynomial, and we use the term _degree_ to refer to the highest power of $x$ that appears in the Taylor polynomial.

We can now ask ourselves whether is possible to find a _quadratic function_ $T_2$ such that $T_2(a)=f(a)$, $T_2'(a)=f'(a)$ and $T_2''(a)=f''(a)$, in other words $T_2^{(k)}(a)=f^{(k)}(a)$ for $k=0,1,2$. Geometrically, this means that the graph of $T_2$ should

- intersect the graph of $f$ at the point $(a,f(a))$ (because $T_2(a)=f(a)$);
- have the same slope as the graph of $f$ at that point (because $T_2'(a)=f'(a)$);
- have the same concavity as the graph of $f$ at that point (because $T_2''(a)=f''(a)$).

A quadratic function is the common name for polynomials of degree two, so we are looking for a function of the form

$$
T_2(x)=c_0+c_1(x-a)+c_2(x-a)^2.
$$

The first-order and second-order derivatives of this function are equal to

\begin{align*}
T_2'(x) &= c_1 + 2c_2(x-a), \\
T_2''(x) &= 2c_2.
\end{align*}

If we now use these formulas to write down the requirements that $T_2$ should satisfy, we get

$$
\left\{
\begin{array}{rcl}
c_0 & = & f(a), \\
c_1 & = & f'(a), \\
2c_2 & = & f''(a),
\end{array}
\right.
$$

Note the $2$ appearing in the last equation, which is a consequence of the fact that the second derivative of $T_2$ is equal to $2c_2$. Solving this system of equations gives us the following values for the coefficients $c_0$, $c_1$ and $c_2$:

$$
\left\{
\begin{array}{rcl}
c_0 & = & f(a), \\
c_1 & = & f'(a), \\
c_2 & = & \frac{1}{2}f''(a),
\end{array}
\right.
$$

and finally we find the following formula for the quadratic function $T_2$:

$$
T_2(x)=f(a)+f'(a)(x-a)+\frac 12 f''(a)(x-a)^2.
$$

This function will be called the _Taylor polynomial of order $2$ centred at_ $x=a$. Note that if $f''(a)=0$, then $T_2$ is equal to $T_1$, so the Taylor polynomial of order $2$ is a generalisation of the linearisation. Because this can always happen, we loosen our demand that $T_2$ must be a quadratic function and only demand that it is a polynomial of degree _at most_ $2$.

::::{prf:example}
:label: Ex:ApproximatingFunctions:cuberoot-quad

Let us see how this works out for our function $f(x)=\sqrt[3] x$ when $a=8$. Since $f(8)=2$, $f'(8)=\dfrac{1}{12}$ and $f''(8)=-\dfrac{1}{144}$, we have

$$
T_2(x) \ = \ 2+\frac 1{12}(x-8)-\frac 1{288}(x-8)^2.
$$

This leads to the approximation

$$
\sqrt[3] x \ \approx \ 2+\frac 1{12}(x-8)-\frac 1{288}(x-8)^2.
$$

In {numref}`Figure %s <Fig:ApproximatingFunctions:cuberootquad>` you can see that the graph of this quadratic polynomial $T_2$ follows the curvature of the graph of the function $\sqrt[3]{x}$ more closely than the graph of the linear function $T_1$.

:::{figure} Images/Fig-TaylorPolynomials-cuberoot-quad.svg
:name: Fig:ApproximatingFunctions:cuberootquad
:class: dark-light

The function $\sqrt[3]{x}$ and the Taylor polynomials $T_1(x)$ and $T_2(x)$.

:::

:::{todo}
Replace {numref}`Fig:ApproximatingFunctions:cuberoot` with an applet.

Do not use $y=\ldots$, but $L(x)=\ldots$ and $f(x)=\ldots$ in the legend of the graph.
:::


Let us use this observation to _approximate_ $\sqrt[3]{9}$:

\begin{align*}
\sqrt[3]{9} &= f(9) \\
 &\approx T_2(9) \\
 &= 2+\frac{1}{12}(9-8)-\frac 1{288}(9-8)^2 \\
 &= 2+\frac{1}{12}-\frac 1{288} \\
 &= \frac{599}{288} \\
 &= 2.07986\overline{11}.
\end{align*}

::::

Now, we can generalise this idea to Taylor polynomials of order $n$.

For the Taylor polynomial of order $2$ we set the demands that

- $T_2^{(k)}(a)=f^{(k)}(a)$ for $k=0,1,2$;
- $T_2$ is a polynomial of degree at most $2$.

If we would want to find a Taylor polynomial of order $3$, we would set the demands that

- $T_3^{(k)}(a)=f^{(k)}(a)$ for $k=0,1,2,3$;
- $T_3$ is a polynomial of degree at most $3$.

We can continue this process and find Taylor polynomials of order $n$ for any positive integer $n$, by setting the demands that

- $T_n^{(k)}(a)=f^{(k)}(a)$ for $k=0,1,2,\ldots,n$;
- $T_n$ is a polynomial of degree at most $n$.

As long as all the demanded derivatives of $f$ at $a$ exist, we can find a Taylor polynomial of order $n$ for any positive integer $n$. The next definition gives us a formula for these Taylor polynomials.

::::{prf:definition} 
:label: Def:ApproximatingFunctions:TaylorPolynomials

The **Taylor polynomial $T_n$ of order $n$ of $f$ with center $a$** is given by 

:::{math} 
:label: Eq:ApproximatingFunctions:Tn

\begin{array}{rcl}
T_n(x) &=& f(a)+f'(a)(x-a)+\frac {f''(a)}{2} (x-a)^2 \\
&& \quad\quad+\frac {f'''(a)}{3!} (x-a)^3+ \ \cdots \ +\dfrac {f^{(n)}(a)}{n!}(x-a)^n.
\end{array}
:::

::::

These polynomials are named after the mathematician [Brook Taylor (1685-1731)](https://en.wikipedia.org/wiki/Brook_Taylor), who introduced them in 1715.

The factorial $k!$, see {prf:ref}`Def:SumsAndProducts:Factorial`, appears in the denominator of the coefficients of the Taylor polynomials because the $k$-th derivative of a term of the form $c_k(x-a)^k$ is equal to $c_k\cdot k!$. This means that if we want the $k$-th derivative of $T_n$ at $a$ to be equal to $f^{(k)}(a)$, we need to divide the coefficient of $(x-a)^k$ by $k!$.

Using the summation sign notation, Equation {eq}`Eq:ApproximatingFunctions:Tn` can be written as follows:

$$
T_n(x)=\sum_{k=0}^n \frac{f^{(k)}(a)}{k!}(x-a)^k.
$$

For example, the Taylor polynomial of order $3$ of $f$ with center $a$ is equal to

$$
T_3(x)=\sum_{k=0}^3 \frac{f^{(k)}(a)}{k!}(x-a)^k = f(a)+f'(a)(x-a)+\frac{f''(a)}{2}(x-a)^2+\frac{f^{(3)}(a)}{6}(x-a)^3.
$$

These functions can be used to approximate $f(x)$ if $x$ is not too far from $a$.

::::{prf:example}
:label: Ex:ApproximatingFunctions:exp

Taylor polynomials of $e^x$ centred at $0$ are easy to compute since this function is its own derivative. This implies that if $f(x)=e^x$, then $f^{(k)}(0)$ is equal to $1$ for each $k$. If we plug this into the formula for $T_3(x)$, then we find the following polynomial:

$$
T_3(x)=1+x+\frac{1}{2}x^2+\frac{1}{6}x^3.
$$

In fact, the Taylor polynomial of order $n$ centred at $0$ of the function $e^x$ is equal to

$$
T_n(x)=1+x+\frac{1}{2}x^2+\frac{1}{6}x^3+ \cdots +\frac{1}{n!}x^n.
$$

In {numref}`Fig:ApproximatingFunctions:exp` you can see the graphs of $e^x$ and of the Taylor polynomials $T_{n-2}$, $T_{n-1}$ and $T_{n}$, where $n$ is initially $3$.

:::{figure} Images/Fig-TaylorPolynomials-exp.png
:name: Fig:ApproximatingFunctions:exp
:class: dark-light

The function $e^x$ and the Taylor polynomials $T_{n-2}(x)$, $T_{n-1}(x)$ and $T_n(x)$, where $n$ is initially $3$.
:::

:::{todo}
Replace {numref}`Fig:ApproximatingFunctions:exp` with an applet with variable $n$ slider.
:::

::::

::::{prf:example}
:label: Ex:ApproximatingFunctions:cos

Computing Taylor polynomials of $\cos(x)$ requires a little bit more work. Let us start with an approximation by a Taylor polynomial of order $2$ centred at 0. The derivative of $\cos(x)$ is $-\sin(x)$ and the second derivative is equal to $-\cos(x)$. For $f(x)=\cos(x)$ we therefore have $f(0)=1$, $f'(0)=0$ and $f''(0)=-1$. The Taylor polynomial $T_2(x)$ is equal to

$$
T_2(x) = 1-\frac{1}{2}x^2.
$$

If we want to find $T_3(x)$ we also need the third derivative of $\cos(x)$, which is equal to $\sin(x)$. Since $\sin(0)=0$, we do not get an extra term of degree three in the Taylor polynomial $T_3(x)$. This means $T_3(x)$ is equal to $T_2(x)$, so

$$
T_3(x)=T_2(x)=1-\frac{1}{2}x^2.
$$

We do get an extra term if we compute the Taylor polynomial of order $4$. We have $f^{(4)}(0)=\cos(0)=1$, so

$$
T_4(x)=1-\frac{1}{2}x^2+\frac{1}{24}x^4.
$$

::::

:::{prf:remark}
:label: Rm:OrderVsDegree

Note that we have used the term _order_ to refer to the number of derivatives that are used in the construction of the Taylor polynomial, and we have used the term _degree_ to refer to the highest power of $x$ that appears in the Taylor polynomial. The _degree_ of a Taylor polynomial is always smaller than or equal to its _order_, but it can be strictly smaller.

For example, $T_3(x)$ is a Taylor polynomial of order $3$ and a polynomial of degree $2$ in {prf:ref}`Ex:ApproximatingFunctions:cos`.

For Taylor polynomials of order $n$ with a low value of $n$, we might sometimes also use the following names:
- $T_1$ is called the first-order Taylor polynomial;
- $T_2$ is called the second-order Taylor polynomial;
- $T_3$ is called the third-order Taylor polynomial;
and so on.
:::

::::{question}
:type: multiple-choice
:variant: single-select
:admonition:
:class: question
:showanswer:
:columns: 1 1 1 1

Construct the Taylor polynomial of order $2$, $T_2$, of the function $f(x)=1+2x+3x^2+4x^3+5x^4$ centred at $x=1$.
---
[ ] $\begin{array}{rcl}T_2(x)&=&(1+2x+3x^2+4x^3+5x^4)+(2 + 6 x + 12 x^2 + 20 x^3)(x-1)\\&&\quad+(6 + 24 x + 60 x^2)(x-1)^2\end{array}$
> Remember that you have to substitute the values of $f(1)$, $f'(1)$ and $f''(1)$ in the formula for $T_2$, not just the values of $f(x)$, $f'(x)$ and $f''(x)$.
[x] $T_2(x)=15+40(x-1)+90(x-1)^2$
> Well done!
[ ] $T_2(x)=1+2(x-1)+3(x-1)^2+4(x-1)^3+5(x-1)^4$
> This is a polynomial of degree $4$, so it cannot be the Taylor polynomial of order $2$.
[ ] $T_2(x)=1+2x+3x^2$
> This is indeed a polynomial of degree $2$, but it is not the Taylor polynomial of order $2$ of $f$ centred at $x=1$.
It is the Taylor polynomial of order $2$ of $f$ centred at $x=0$.
---
::::

## Taylor's inequality

So far we have been saying that Taylor polynomials provide us with a way to approximate functions locally, but how good are these approximations? Is $2$ a good approximation of the number $\sqrt[3]{9}$ or is $2.0801$?

::::{prf:example}
:label: Ex:TaylorPolynomialsAdd:cuberoot

Let us use the Taylor polynomials of the function $f(x)=\sqrt[3]{x}$ that we already computed to find an approximation of $\sqrt[3]{9}$. The Taylor polynomial of order $1$ centred at $8$ is equal to

$$
T_1(x)=2+\frac{1}{12}(x-8).
$$

What do we obtain when we use it to approximate $\sqrt[3]{9}$?

$$
\sqrt[3]{\class{red}{9}} = f(\class{red}{9}) \ \approx T_1(\class{red}{9}) =  \ 2+\frac{1}{12}(\class{red}{9}-8) \ = \ \frac{25}{12} \ = \ 2.0833\ldots
$$

How accurate is this approximation? The actual value of $\sqrt[3]{9}$ is $2.0801\ldots$. This means that the approximation error is in this case equal to:

$$
|f(9) - T_1(9)| = |\sqrt[3]{9}-\frac{25}{12}| =|2.0801\ldots - 2.0833\ldots|= 0.0032\ldots
$$

If we use a Taylor polynomial of order $2$ we will get a better approximation. Remember that the Taylor polynomial of order $2$ of $\sqrt[3]{x}$ centred at $x=8$ is equal to

$$
T_2(x)=2+\frac{1}{12}(x-8)-\frac{1}{288}(x-8)^2.
$$

This gives us the following approximation of $\sqrt[3]{9}$:

$$
T_2(\class{red}{9}) = 2+\frac{1}{12}(\class{red}{9}-8)-\frac{1}{288}(\class{red}{9}-8)^2 \ = \  \frac{599}{288} \ = \ 2.0798\ldots
$$

For this approximation the error is equal to

$$
|f(9) - T_2(9)| = |\sqrt[3]{9}-\frac{599}{288}| =|2.0801\ldots - 2.0798|\ldots= 0.0003\ldots
$$

Next we will show how you can determine an upper bound for these approximation errors.

::::

We would like to be able to have an upper bound for the error in our Taylor polynomial approximations. To do so, we first give two examples.

::::{margin}
:::{figure} Images/scooter.jpg
:name: Fig:ApproximatingFunctions:cuberoot-quad
:placement: caption
:source: [Vecteezy](https://www.vecteezy.com/vector-art/1270966-motor-scooter-isolated-on-white-background)
:license: Vecteezy Free License
:author: Timplaru Emil
:date: 2020-09-03

A scooter.
:::
::::

::::{prf:example}
:label: Ex:TaylorPolynomialsIneq:speed1

Consider we have a scooter and that this scooter has at $t=0\,\text{s}$ the position $x(0)=5\,\text{m}$.

Next consider that the velocity of the scooter is constant and equal to $10\,\dfrac{\text{m}}{\text{s}}$ for all $t$.

Using this information we can determine the position of the scooter after $10$ seconds, since in $10$ seconds the scooter will have traveled $10\,\text{s}\cdot10\,\dfrac{\text{m}}{\text{s}}=100\,\text{m}$, so $x(10)=x(0)+100\,\text{m}=105\,\text{m}$.

::::

::::{prf:example}
:label: Ex:TaylorPolynomialsIneq:speed2

Consider we have the same scooter, but now assume that this scooter has at $t=0\,\text{s}$ the position $x(0)=5\,\text{m}$ and the velocity $v(0)=10\,\dfrac{\text{m}}{\text{s}}$ at $t=0\,\text{s}$.

Now the acceleration $a(t)$ varies between $0\,\dfrac{\text{m}}{\text{s}^2}$ and $0.1\,\dfrac{\text{m}}{\text{s}^2}$ for all $t$.

Using this information we cannot determine the position of the scooter after $10$ seconds _exactly_, as we do not know the _exact_ velocity of the scooter in those 10 seconds.

What we can do, is _estimate_ the position after $10$ seconds.

To do this, we consider the information we have on the acceleration: it is at _minimum_ $0\,\dfrac{\text{m}}{\text{s}^2}$ during those 10 seconds. If we assume the acceleration equals $0\,\dfrac{\text{m}}{\text{s}^2}$ during those 10 seconds, the velocity will be the lowest during the time frame, which also indicates the least distance traveled by the scooter. So in this case, the velocity will remain $10\,\dfrac{\text{m}}{\text{s}}$ and the distance traveled will be again $100\,\text{m}$. So at _minimum_ the scooter will have position $105\,\text{m}$, or in symbols:

$$
x(10) \ge 105.
$$

Now we focus on the _maximum_ acceleration, which is $0.1\,\dfrac{\text{m}}{\text{s}^2}$. If we assume the acceleration equals $0.1\,\dfrac{\text{m}}{\text{s}^2}$ during those 10 seconds, the velocity will be the highest during the time frame, which also indicates the most distance traveled by the scooter. In this case this means that the velocity increases linearly from $10\,\dfrac{\text{m}}{\text{s}}$ to $10\,\dfrac{\text{m}}{\text{s}}+0.1\,\dfrac{\text{m}}{\text{s}^2}\cdot10\,\text{s}=11\,\dfrac{\text{m}}{\text{s}^2}$ in $10$ seconds. In formula form:

$$
v(t)=10+0.1\cdot t.
$$

Now we know this, we can also estimate the _maximum_ position after $10$ seconds:

\begin{align*}
x(10) &\leq x(0) + \int_{0}^{10}v(t)\,dt \\
&= 5 + \int_0^{10}\left(10+0.1t\right)\,dt \\
&= 5 + \left[10t+0.05 t^2\right]_{t=0}^{10} \\&
= 5 + \left(605 - 500\right) \\&= 110.
\end{align*}

In conclusion, we found that the position of the scooter after $10$ seconds satisfies

$$
105 \le x(10) \le 110,
$$

where we used information about the position, i.e. the _zeroth derivative_ of the position, and the velocity, i.e. the _first derivative_ of the position, at one time moment, and bounds for the acceleration, i.e. the _second derivative_ of the position.

::::

In the above example we could say that we approximated the position after $10$ seconds using a Taylor polynomial $T_1(t)=x(0)+v(0)\cdot t$ of order $1$ and that we found an interval for the exact value using bounds on the _second derivative_.

The next theorem generalises the above examples and gives us the tools to always find an upper bound for the difference between the _exact_ value and an _approximation_ using Taylor polynomials:

::::{prf:theorem}
:label: Th:TaylorPolynomialsAdd:TaylorIneq

Define $D$ as an interval that contains the point $a$, $T_n$ as the Taylor polynomial of order $n$ of $f$ centred at $a$ and $M$ as an upper bound for $|f^{(n+1)}(x)|$ on the interval $D$. Then

:::{math}
:label: Ex:TaylorPolynomialsAdd:TaylorIneq

|f(x)-T_n(x)|\leq \dfrac{M |x-a|^{n+1}}{(n+1)!}

:::

for all $x$ in $D$.

::::

As this theorem is pretty technical, we will not give a proof of it, but postpone it to {numref}`Sec:Series:TaylorSeries`.

To make talking about these formulae a little easier, we name parts of it:

::::{prf:definition}
:label: Def:TaylorPolynomials:TaylorIneq

The Inequality {eq}`Ex:TaylorPolynomialsAdd:TaylorIneq` is called **Taylor's inequality**.

The expression $f(x)-T_n(x)$ is called the **remainder** $R_n(x)$.

The absolute value of the remainder, $E_n(x)=|R_n(x)|=|f(x)-T_n(x)|$ is the **approximation error**.

::::

The interval $D$ mentioned in the statement of Taylor's inequality is important, as it is the interval on which we can guarantee that the approximation error is smaller than or equal to $\dfrac{M |x-a|^{n+1}}{(n+1)!}$. If we choose a different interval, we might not be able to find an upper bound for $|f^{(n+1)}(x)|$ on that interval, and then we cannot use Taylor's inequality to find an upper bound for the approximation error. Sometimes the interval $D$ can be given, but sometimes we have to choose it ourselves. In the latter case, you often already know a specific value of $x$ for which you want to find an approximation, and then you can choose $D$ to be an interval that contains both $a$ and that specific value of $x$. So if $x>a$, you can choose $D$ to be the interval $[a,x]$, and if $x<a$, you can choose $D$ to be the interval $[x,a]$.

To give an idea what {prf:ref}`Th:TaylorPolynomialsAdd:TaylorIneq` is saying, let us look at an example.

::::{prf:example}
:label: Ex:TaylorPolynomials:Visualise

Consider the function $f(x)=\cos(x)+\sin(x)$. Because of the cyclic nature of the derivates of the sine and cosine functions, $f^{(n)}(0)$ for $n=0,1,2,\ldots$ gives the next sequence:

$$
1, 1, -1, -1, 1, 1, -1, -1, \ldots
$$

We can use this to construct different Taylor polynomials of $f$ centred at $0$. For example, the Taylor polynomial of orders $1$, $2$, and $3$ centred at $0$ are equal to

\begin{align*}
T_1(x) & = 1+x, \\
T_2(x) & = 1+x-\frac{1}{2}x^2, \\
T_3(x) & = 1+x-\frac{1}{2}x^2-\frac{1}{6}x^3.
\end{align*}

Now we turn our attention to the approximation error of these Taylor polynomials on the interval $D=(-\infty,\infty)$. We want to find an upper bound for the error, so we need to find an $M$ such that $|f^{(n+1)}(x)|\leq M$ for all $x$ in some interval $D$ that contains $0$. The $(n+1)$-th derivative of $f$ is equal to $\pm \cos(x)\pm \sin(x)$, so we need to find an upper bound for $|\pm \cos(x)\pm \sin(x)|$. Using the triangle inequality, we have

\begin{align*}
|\pm \cos(x)\pm \sin(x)| &\leq |\cos(x)| + |\sin(x)| \\
&\leq 1+1 = 2,
\end{align*}

as we know that $\cos(x)$ and $\sin(x)$ are both between $-1$ and $1$.

This means that we can choose $M$ to be equal to $2$, as $|\cos(x)+\sin(x)|\leq 2$ for all values of $x$. Using $a=0$ and $M=2$ in Inequality {eq}`Ex:TaylorPolynomialsAdd:TaylorIneq`, we get

$$
|f(x)-T_n(x)|\leq \dfrac{2|x|^{n+1}}{(n+1)!},
$$

or even

$$
T_n(x)-\dfrac{2|x|^{n+1}}{(n+1)!} \leq f(x) \leq T_n(x)+\dfrac{2|x|^{n+1}}{(n+1)!}.
$$

For $n=1$ we get the following inequalities

$$
T_1(x)-\dfrac{2x^{2}}{2!} \leq f(x) \leq T_1(x)+\dfrac{2x^{2}}{2!},
$$

while for $n=2$ we get

$$
T_2(x)-\dfrac{2|x|^{3}}{3!} \leq f(x) \leq T_2(x)+\dfrac{2|x|^{3}}{3!}.
$$

These inequalities can also be visualised as in {numref}`Fig:ApproximatingFunctions:error`, where we used $n=1$ and $M=2$ initially. It can be observed that the graph of $f$ is always between the graphs of $T_n(x)-\dfrac{2|x|^{n+1}}{(n+1)!}$ and $T_n(x)+\dfrac{2|x|^{n+1}}{(n+1)!}$, which is exactly what Taylor's inequality is saying.

:::{figure} Images/Fig-TaylorPolynomials-error.svg
:name: Fig:ApproximatingFunctions:error
:figwidth: 50%
:class: dark-light

Suppose $|f''(x)|\leq M$ for all $x$, then $T_1(x)-\frac{M}{2}x^2\leq f(x)\leq T_1(x)+\frac{M}{2}x^2$.

:::

:::{todo}
Replace {numref}`Fig:ApproximatingFunctions:error` with an applet where $n$ can be varied with a slider and $M$ can be adjusted to the stricter bound.
:::

As a final remark, note that the upper bound we found for the approximation error is not necessarily the best possible upper bound. For example, in the above example we found that $M$ can be equal to $2$, but we could have found a smaller $M$ by using the fact that $\cos(x)+\sin(x)$ is between $\sqrt{2}$ and $-\sqrt{2}$ for all $x$. This would have given us a better upper bound for the approximation error, but it would have also made the calculations more difficult. In practice, it is often good enough to find an upper bound that is not too far from the best possible upper bound, as long as it is easy to compute. If you are interested in the effect of this stronger upper bound of $M=\sqrt{2}$, you visualise it in {numref}`Fig:ApproximatingFunctions:error` by changing the value of $M$ to $\sqrt{2}$. 

::::

We can not only use Taylor's inequality to find an upper bound for the approximation error, but also to find an interval in which the exact value of $f(x)$ lies. The next example shows how we can do this.

::::{prf:example}
:label: Ex:TaylorPolynomialsAdd:cos4

Let us construct an approximation of $\cos(0.5)$ by using the  Taylor polynomial $T_4$ of order $4$ of the cosine function $f(x)=\cos(x)$ centred at $x=0$:

$$
T_4(x) \ = \ 1-\frac{1}{2}x^2+\frac{1}{24}x^4.
$$

The approximation that we find is

$$
\cos(\class{red}{0.5})=f(\class{red}{0.5}) \ \approx T_4(\class{red}{0.5}) = 1-\frac{1}{2}\left(\class{red}{0.5}\right)^2+\frac{1}{24}\left(\class{red}{0.5}\right)^4 \ = \ 0.877604\ldots
$$

In order to find an upper bound for the approximation error we will need to find an $M$ such that the fifth derivative $f^{(5)}$ of the cosine function is smaller than $M$ for all numbers $x$ in the interval $[0, 0.5]$. The fifth derivative of $f(x)=\cos(x)$ is equal to $f^{(5)}(x)=-\sin(x)$. We know that $|-\sin(x)|\leq 1$ for all values of $x$, so we can choose $M$ to be equal to $1$. We get the following upper bound for the remainder:

\begin{align*}
\left|R_4\left(\class{red}{0.5}\right)\right| &= |f(\class{red}{0.5})-T_4(\class{red}{0.5})| \\
&\leq \frac{1\cdot |\class{red}{0.5}-0|^{4+1}}{(4+1)!} \\
&= \frac{(0.5)^{5}}{5!} \\
&= \frac{0.03125}{120} \\
&= 0.00026\ldots
\end{align*}
Thus, the approximation error is at most $0.00027$, as we must round up to ensure a proper upper bound.

Now we have an upper bound for the _absolute_ value of the error, we can even find an interval in which the _exact_ value of $\cos(0.5)$ lies:

$$
\begin{array}{rcl}
& |f({0.5})-T_4({0.5})| & \leq 0.00027 \\
-0.00027 \le  & \cos({0.5})- 0.877604 & \leq 0.00027 \\
0.877604-0.00027 \le & \cos({0.5}) &\leq 0.877604+0.00027 \\
0.877334 \le & \cos({0.5}) &\leq 0.877874 \\
\end{array}
$$

::::

Most of the time when we are looking for an approximation we want to find a value that lies within a given margin of error. The next example shows exactly how we can do that.

::::{prf:example}
:label: Ex:TaylorPolynomialsAdd:sin

Suppose that we want to find an approximation of $\sin(0.8)$ such that the difference between the approximation and the actual value is at most $0.0001$. We will use a Taylor polynomial of the function $f(x)=\sin(x)$ and evaluate it at $x=0.8$. What order Taylor polynomial do we need to use?

The derivatives of the sine function $f(x)=\sin(x)$ are all equal to either $\cos(x)$, $-\sin(x)$, $-\cos(x)$ or $\sin(x)$. This means that for each $n$ and for each $x$ we have $|f^{(n+1)}(x)|\leq 1$. Therefore we know that

$$
\left|R_n\left(0.8\right)\right|\leq \frac{(0.8)^{n+1}}{(n+1)!}.
$$

Using this formula, we can make a table with in each row a different value of $n$ and the corresponding upper bound:

```{table} Upper bounds for the approximation error of $\sin(0.8)$ using Taylor polynomials of different orders.
:widths: auto
:align: center
:name: Tab:ApproximatingFunctions:SinBounds

|$n$|$E_n(0.8)\leq$|
|-|-|
|$0$|$0.8$|
|$1$|$0.32$|
|$2$|$0.085\overline{33}$|
|$3$|$0.0170\overline{66}$|
|$4$|$0.002730\overline{66}$|
|$5$|$0.0003640\overline{88}$|
|$6$|$0.00004161\overline{015873}$|
|$7$|$0.000004161\overline{015873}$|
```

For $n=3$ the right-hand side of the inequality is $0.0170\overline{66}$. This value is not smaller than $0.0001$ and thus a Taylor polynomial of order $3$ may not be sufficient to give us an approximation that is good enough. If $n$  is equal to 4 we obtain that the approximation error is smaller than $0.002730\overline{66}$. After a little trial and error we find that for $n=6$ the error is smaller than $0.00004161\overline{015873}$ and therefore also smaller than $0.0001$. A Taylor polynomial of order $6$ will give us the approximation that we want. For the sine function this polynomial is equal to

$$
T_6(x)=x-\frac{1}{6}x^3+\frac{1}{120}x^5.
$$

There is no term of degree six since the sixth derivative of $\sin(x)$ is zero in $x=0$. The approximation that we find is

$$
T_6\left( \class{red}{0.8} \right) \ = \ \class{red}{0.8}-\frac{1}{6}\left( \class{red}{0.8} \right)^3+\frac{1}{120}\left( \class{red}{0.8} \right)^5 \ = \ 0.717397\ldots
$$

Since the error is smaller than $0.0001$ this means that the actual value of $\sin(0.8)$ lies in between $0.7172$ and $0.7175$.

::::

In {numref}`Tab:ApproximatingFunctions:SinBounds` it can be seen that the upper bound for the approximation error decreases very quickly as we increase $n$. This is a general phenomenon: the approximation error of Taylor polynomials often decreases very quickly as we increase the order of the Taylor polynomial. The theory behind this behavior and much more is the subject of {numref}`Sec:Series:TaylorSeries`, where we will also give a proof of Taylor's inequality.

::::{prf:example-start}
:label: Ex:TaylorPolynomials:Code

As you may have noticed, computing Taylor polynomials and using Taylor's inequality can be quite a bit of work. For harder problems some times it is easier to use a computer to do the calculations. For example, the following Python code:
- computes the Taylor polynomial of order $5$ of the function $f(x)=\sqrt{1+\cos^2(x)}$ centred at $0$;
- approximates $f(0.8)$ by evaluating the Taylor polynomial at $x=0.8$;
- finds an upper bound for the approximation error in this approximation using Taylor's inequality on the interval $[0,0.8]$.
- finds an interval in which the exact value of $f(0.8)$ lies.

::::

:::{code-cell} python
---
tags: [auto-execute-page]
---
# Import a symbolic mathematics library
import sympy as sp
# import a function for optimisation
from scipy.optimize import minimize_scalar
# import a function to display the result in LaTeX format
from IPython.display import Latex
# Define the variable and the constants
x = sp.symbols('x')
# Define the function
f = sp.sqrt(1 + sp.cos(x)**2)
# Set which order Taylor polynomial we want to compute
n = 5
# Set around which point we want to compute the Taylor polynomial
a = 0
# Set at which point we want to evaluate the Taylor polynomial
x_eval = 0.8
# set how many digits should be shown in the display
digits = 6

# Compute the Taylor polynomial
T_n = f.series(x, a,n+1).removeO()
# Compute the value at x_eval
T_n_eval = T_n.subs(x,sp.Rational(str(x_eval))).simplify()
# Find the (n+1)-th derivative of f
f_der = f.diff(x,n+1).simplify()
f_der_numpy = sp.lambdify(x, f_der, modules=['numpy'])
# Determine the maximum of the absolute value on (a,x_eval)
res = minimize_scalar(lambda x: -f_der_numpy(x),
                      bounds=(min([a,x_eval]),max([a,x_eval])),
                      method='bounded')
M = -res.fun
# Apply Taylor's inequality to get the upper bound at x_eval
UB = M*abs(x_eval-a)**(n+1)/sp.factorial(n+1)
# Determine the interval for f(x_eval)
MIN = T_n_eval-UB
MAX = T_n_eval+UB
# Display the results
display(Latex(f"The Taylor polynomial of order ${sp.latex(n)}$ of the "
              f"function $f(x)={sp.latex(f)}$ "
              f"centred at ${sp.latex(a)}$ is"))
display(Latex("$$T_{}(x) = {}.$$".format(n, sp.latex(T_n))))
display(Latex(f"The value $f({sp.latex(x_eval)})$ can be approximated as"))
display(Latex(f"$$T_{sp.latex(n)}({sp.latex(x_eval)})={sp.latex(T_n_eval)}"
             f"\\approx{sp.latex(T_n_eval.evalf(digits))}$$"))
display(Latex(f"The maximum $M$ of the absolute value "
              f"of the ${sp.latex(n+1)}$-th derivative of $f$ "
              f"on the interval $[{sp.latex(sp.Min(a,x_eval))}"
              f",{sp.latex(sp.Max(a,x_eval))}]$ is"))
display(Latex(f"$$M={sp.latex(round(M,digits))}.$$"))
display(Latex(f"Taylor's inequality thus gives"))
display(Latex(f"$$|f({sp.latex(x_eval)})-T_{{{sp.latex(n)}}}"
              f"({sp.latex(x_eval)})|\leq "
              f"{sp.latex(round(UB,digits))}.$$"))
display(Latex(f"The exact value of $f({sp.latex(x_eval)})$ therefore "
              f"satisfies"))
display(Latex(f"$${sp.latex(MIN.evalf(digits))}\leq f({sp.latex(x_eval)}) "
              f"\leq {sp.latex(MAX.evalf(digits))}.$$"))
:::

::::{prf:example-end}
::::

## Grasple exercises

### Linearisations

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2286a124-b092-4a23-b292-79c0a03c70b4?id=63715
:label: Grasple:63715
:dropdown:
:description: Linearisation of the arctangent.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/21d38731-0b57-4fc5-af15-936ef3a414fc?id=63728
:label: Grasple:63728
:dropdown:
:description: Linearisation of a power of $x$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b36e91ec-7f75-4bd8-9669-e40968b9f15c?id=78767
:label: Grasple:78767
:dropdown:
:description: Approximate a function value using a linearisation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7d9a7257-7c30-4be4-8277-6b57eb17e2c0?id=127213
:label: Grasple:127213
:dropdown:
:description: Approximate change in function value using a linearisation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8cd84d06-42ea-4ff2-8a3f-86fe5ac45bd9?id=75827
:label: Grasple:75827
:dropdown:
:description: Relative errors.

::::

### Taylor polynomials

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/282946e0-2d88-41b6-970c-55c26d28d714?id=64606
:label: Grasple:64606
:dropdown:
:description: Finding $T_2$ for a sine function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fe0d364e-9888-4a9d-9e65-08d0e5675c34?id=132982
:label: Grasple:132982
:dropdown:
:description: Finding $T_2$ for a polynomial times an exponential function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/523a3822-e8b6-4c85-923f-d8c73dcffee1?id=64629
:label: Grasple:64629
:dropdown:
:description: Finding $T_3$ of a reciprocal function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4bec421b-5b79-4159-85c8-e6cfdc203606?id=105586
:label: Grasple:105586
:dropdown:
:description: Using Taylor's inequality for $T_1$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4d3f51de-2210-4f7d-985a-edddfb121b4f?id=104206
:label: Grasple:104206
:dropdown:
:description: Using Taylor's inequality for $T_3$.

::::