(Sec:Taylor polynomials)=
# Approximating functions

## Introduction

Additions and multiplications are easy to compute by hand, but if you had to determine the value of $\sqrt[3]{9}$ you would probably need a calculator. The function $\sqrt[3]{x}$, however, can be approximated by polynomials. Polynomials are functions that can be written as sums of multiples of powers of $x$. The functions $1+x-3x^4$ and $-2-5x^2+2x^6-x^7$ are examples of polynomials.

Function values of polynomials are easy to find since you only need to be able to add and multiply numbers. This means that we can use these polynomials to obtain a good guess of what $\sqrt[3]{9}$ should more or less be equal to. In this text we will show you how you can approximate functions by polynomials and apply them to solve various problems.

## Linearisation

We already saw in {numref}`Section:Differentiability` how we can construct a tangent line to a function at a certain point. An equation for the tangent line was

$$
y = f(a) + f'(a)(x-a),
$$

and this line touches the graph of the function $f$ at the point $(a,f(a))$ and has the same slope in that point. The tangent is the graph of the following linear function:

$$L(x)=f(a)+f'(a)(x-a).$$

Near the point $(a,f(a))$, the graph of the function and the tangent line are very close to each other, and the tangent line can therefore be used to approximate the graph of the function near that point. In other words, we can approximate the function $f$ by the linear function $L$ when we are close to the value $a$. This leads to the following definition and properties:

::::{prf:definition}
:label: Def:ApproximatingFunctions:Linearisation

The **linearisation** of a function $f$ at a point $(a,f(a))$ is given by

$$L(x)=f(a)+f'(a)(x-a).$$
::::

::::{prf:property}
:label: Prop:ApproximatingFunctions:Linearisation

Assume $L$ is the linearisation of a function $f$ at the point $(a,f(a))$. Then:
- $L$ is the linear function that best approximates $f$ near $a$.
- The graph of $L$ is the line tangent to the graph of $f$ at  $(a, f(a))$.
- $L$ is the unique linear function such that $L(a)=f(a)$ and $L'(a)=f'(a)$. 

::::

::::{prf:example}
:label: Ex:ApproximatingFunctions:cuberoot

Let's use the function $f(x)=\sqrt[3] x$ as an example and say that $a=8$. Since $f(8)=2$ and $f'(8)  =  \frac{1}{12}$, we have

$$
L(x) \ = \ 2+\frac{1}{12}(x-8).
$$

This leads to the approximation

$$
\sqrt[3] x \ \approx \  2+\frac{1}{12}(x-8).
$$

{numref}`Figure %s <Fig:ApproximatingFunctions:cuberoot>` shows the graph of $\sqrt[3]{x}$ and the linearisation $L(x)$.

:::{figure} Images/Fig-TaylorPolynomials-cuberoot.svg
:name: Fig:ApproximatingFunctions:cuberoot
:class: dark-light

The function $\sqrt[3]{x}$ and the linearisation $ L(x)$.

:::

You can clearly see that for any $x$ close to $8$ the values of $f(x)$ and $L(x)$ are very close to each other.

Let us use this observation to _approximate_ $\sqrt[3]{9}$:

$$
\sqrt[3]{9} = f(9) \approx L(9) = 2+\frac{1}{12}(9-8) = 2+\frac{1}{12} = \frac{25}{12} = 2.08\overline{33}.
$$

::::

Another way to look at linearisation is to use it to approximate changes in function values. If we want to approximate the change in the value of a function $f$ when we change the input from $a$ to $a+h$, we can use the linearisation $L(x)$ of $f$ at $x=a$. The real change in the function value is given by

$$
\Delta f = f(a+h)-f(a). 
$$

Using the linearisation, we can approximate this change by performing the following calculation:

$$
\begin{align*}
\Delta f &= f(a+h)-f(a) \\
& \approx L(a+h)-f(a) \\
& = \left( f(a) + f'(a)(a+h-a) \right) -f(a) \\
& = f'(a) \cdot h.
\end{align*}
$$

In other words, we have the following property:

::::{prf:property}
:label: Prop:ApproximatingFunctions:LinearisationChange

Assume $L$ is the linearisation of a function $f$ at the point $(a,f(a))$. Then the change in the value of $f$ when we change the input from $a$ to $a+h$ can be approximated by
$$
\Delta f = f(a+h)-f(a) \approx f'(a) \cdot h.
$$
::::

The next example shows how we can use this property to investigate function value changes.

:::::{margin}
:::{figure} Images/Construction.png
:name: Fig:ApproximatingFunctions:Construction
:class: dark-light

A set of cylindrical steel beams.

:::
:::::

:::::{prf:example}
:label: Ex:ApproximatingFunctions:ApproxChange

A company constructs cylindrical steel beams with a length of $8$ meter. The diameter of each beam is equal to $0.6$ meter. We wonder how much the volume of a beam approximately would increase if, because of a construction error, the diameter would increase by $0.01$ meter.

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
\frac{\Delta V}{V(0.6)} \approx \frac{2\cdot0.01}{0.06} \approx 0.0333.
$$

which means that the volume increases by approximately $3.33\%$ while the diameter increases by approximately $1.67\%$.

:::::

## Taylor polynomials

You can check yourself that a linearisation $L(x)$ is a polynomial of degree one that has, at the point $a$, the same value and the same derivative as $f(x)$. From now on, we will also refer to the linearisation $L(x)$ of $f$ at $x=a$ as the Taylor polynomial $T_1(x)$ of degree one of $f$ centered at $x=a$. By definition, the graph of $T_1$ is the tangent line to the graph of $f$ at the point $(a,f(a))$, so it makes sense to state that $f(x)\approx T_1(x)$ for all $x$ that are close to $a$. By the expression $f(x)\approx T_1(x)$, we mean that $T_1(x)$ is an approximation of $f(x)$.

**Approximation by a quadratic function**

We can now ask ourselves whether is possible to find a _quadratic function_ $T_2$ such that $T_2(a)=f(a)$, $T_2'(a)=f'(a)$ and $T_2''(a)=f''(a)$, in other words $T_2^{(k)}(a)=f^{(k)}(a)$ for $k=0,1,2$. A straightforward verification shows that these requirements are met by the function

$$
T_2(x)=f(a)+f'(a)(x-a)+\frac 12 f''(a)(x-a)^2.
$$

This function will be called the _Taylor polynomial of order 2 centered at_ $x=a$.

::::{prf:example}
:label: Ex:ApproximatingFunctions:cuberoot-quad

Let's see how this works out for our function $f(x)=\sqrt[3] x$ when $a=8$. Since $f(8)=2$, $f'(8)=\dfrac{1}{12}$ and $f''(8)=-\dfrac{1}{144}$, we have

$$
T_2(x) \ = \ 2+\frac 1{12}(x-8)-\frac 1{288}(x-8)^2.
$$

This leads to the approximation

$$
\sqrt[3] x \ \approx \ 2+\frac 1{12}(x-8)-\frac 1{288}(x-8)^2.
$$

In {numref}`Figure %s <Fig:ApproximatingFunctions:cuberootquad>` you can see that this quadratic polynomial is indeed a better approximation than the linearisation. 

:::{figure} Images/Fig-TaylorPolynomials-cuberoot-quad.svg
:name: Fig:ApproximatingFunctions:cuberootquad
:class: dark-light

The function $\sqrt[3]{x}$ and the Taylor polynomials $T_1(x)$ and $T_2(x)$.

:::

Let us use this observation to _approximate_ $\sqrt[3]{9}$:

$$
\sqrt[3]{9} = f(9) \approx T_2(9) = 2+\frac{1}{12}(9-8)-\frac 1{288}(9-8)^2 = 2+\frac{1}{12}-\frac 1{288} = \frac{599}{288} = 2.07986\overline{11}.
$$

::::

Now, we can generalize this idea to Taylor polynomials of order $n$.

**Higher order approximations**

Continuing this process, we define the Taylor polynomial of order three as

$$
T_3(x) \ = \ f(a)+f'(a)(x-a)+\frac 12f''(a)(x-a)^2+\frac 16f'''(a)(x-a)^3.
$$

The Taylor polynomial $T_n(x)$ of degree $n$ of a function $f(x)$ centered at $a$ will be defined as

::::{prf:definition} 

The **$n$th-order Taylor polynomial $T_n$ of $f$ with center $a$** is given by 

:::{math} 
:label: Eq:ApproximatingFunctions:Tn

T_n(x)= f(a)+f'(a)(x-a)+\frac {f''(a)}{2} (x-a)^2+\frac {f'''(a)}{3!} (x-a)^3+ \ \cdots \ +\dfrac {f^{(n)}(a)}{n!}(x-a)^n,

:::

where

$$
k! = 1 \cdot 2 \cdot 3 \cdot \ldots \cdot k
$$

for integers $k\geq1$ and $0!=1$.

::::

These polynomials are named after the mathematician [Brook Taylor (1685-1731)](https://en.wikipedia.org/wiki/Brook_Taylor), who introduced them in 1715.

Using the summation sign notation, Equation {eq}`Eq:ApproximatingFunctions:Tn` can be written as follows:

$$
T_n(x)=\sum_{k=0}^n \frac{f^{(k)}(a)}{k!}(x-a)^k.
$$

These functions can be used to approximate $f(x)$ if $x$ is not too far from $a$.

::::{prf:example}
:label: Ex:ApproximatingFunctions:exp

Taylor polynomials of $e^x$ centered at $0$ are easy to compute since this function is its own derivative. This implies that if $f(x)=e^x$, then $f^{(n)}(0)$ is equal to $1$ for each $n$. If we plug this into the formula for $T_3(x)$, then we find the following polynomial:

$$
1+x+\frac{1}{2}x^2+\frac{1}{6}x^3.
$$

In fact, the Taylor polynomial of order $n$ centered at $0$ of the function $e^x$ is equal to

$$
1+x+\frac{1}{2}x^2+\frac{1}{6}x^3+ \cdots +\frac{1}{n!}x^n.
$$

::::

::::{prf:example}
:label: Ex:ApproximatingFunctions:cos

Computing Taylor polynomials of $\cos(x)$ requires a little bit more work. Let's start with an approximation by a second-order Taylor polynomial centered at 0. The derivative of $\cos(x)$ is $-\sin(x)$ and the second derivative is equal to $-\cos(x)$. For $f(x)=\cos(x)$ we therefore have $f(0)=1$, $f'(0)=0$ and $f''(0)=-1$. The Taylor polynomial $T_2(x)$ is equal to

$$
1-\frac{1}{2}x^2.
$$

If we want to find $T_3(x)$ we also need the third derivative of $\cos(x)$, which is equal to $\sin(x)$. Because $\sin(0)=0$, we do not get an extra term of degree three in the Taylor polynomial $T_3(x)$. This means $T_3(x)$ is equal to $T_2(x)$. We do get an extra term if we compute the Taylor polynomial of order $4$. We have $f^{(4)}(0)=\cos(0)=1$, so

$$
T_4(x)=1-\frac{1}{2}x^2+\frac{1}{24}x^4.
$$

::::

## Taylor's inequality

So far we have been saying that Taylor polynomials provide us with a way to approximate functions, but how good are these approximations? Is $2$ a good approximation of the number $\sqrt[3]{9}$ or is $2.0801$?

::::{prf:example}
:label: Ex:TaylorPolynomialsAdd:cuberoot

Let's use the Taylor polynomials of the function $f(x)=\sqrt[3]{x}$ that we already computed to find an approximation of $\sqrt[3]{9}$. The first order Taylor polynomial centred at $8$ is equal to

$$
T_1(x)=2+\frac{1}{12}(x-8).
$$

What do we obtain when we use it to approximate $\sqrt[3]{9}$?

$$
\sqrt[3]{\class{red}{9}} = f(\class{red}{9}) \ \approx T_1(\class{red}{9}) =  \ 2+\frac{1}{12}(\class{red}{9}-8) \ = \ \frac{25}{12} \ = \ 2.0833\ldots.
$$

How accurate is this approximation? The actual value of $\sqrt[3]{9}$ is $2.0801\ldots$. This means that the approximation error is in this case equal to:

$$
|f(9) - T_1(9)| = |\sqrt[3]{9}-\frac{25}{12}| =|2.0801\ldots - 2.0833\ldots|= 0.0032\ldots.
$$

If we use a second-order Taylor polynomial we will get a better approximation. Remember that the second-order Taylor polynomial of $\sqrt[3]{x}$ centered at $x=8$ is equal to

$$
T_2(x)=2+\frac{1}{12}(x-8)-\frac{1}{288}(x-8)^2.
$$

This gives us the following approximation of $\sqrt[3]{9}$:

$$
T_2(\class{red}{9}) = 2+\frac{1}{12}(\class{red}{9}-8)-\frac{1}{288}(\class{red}{9}-8)^2 \ = \  \frac{599}{288} \ = \ 2.0798\ldots.
$$

For this approximation the error is equal to

$$
|f(9) - T_2(9)| = |\sqrt[3]{9}-\frac{599}{288}| =|2.0801\ldots - 2.0798|\ldots= 0.0003\ldots.
$$

Next we will show how you can determine an upper bound for these approximation errors.

::::

We would like to be able to have an upper bound for the difference between the approximation of a certain value and the actual value. To do so, we first give two examples.

::::{prf:example}
:label: Ex:TaylorPolynomialsIneq:speed1

Consider we have a scooter:

:::{figure} Images/scooter.jpg
:name: Fig:ApproximatingFunctions:cuberoot-quad
:figwidth: 50%

A scooter. <a href="https://www.vecteezy.com/free-vector/scooter">Scooter Vectors by Vecteezy</a>

:::

Let's assume that this scooter has

- position $x(0)=5\,\mathrm{m}$ at $t=0\,\mathrm{s}$;

- velocity $v(t)=10\,\dfrac{\mathrm{m}}{\mathrm{s}}$ for all $t$.

Using this information we can determine the position of the scooter after $10$ seconds, as in $10$ seconds the scooter will have traveled $10\,\mathrm{s}\cdot10\,\dfrac{\mathrm{m}}{\mathrm{s}}=100\,\mathrm{m}$, so $x(10)=x(0)+100\,\mathrm{m}=105\,\mathrm{m}$.

::::

::::{prf:example}
:label: Ex:TaylorPolynomialsIneq:speed2

Consider we have the same scooter, but now assume that this scooter has

- position $x(0)=5\,\mathrm{m}$ at $t=0\,\mathrm{s}$;

- velocity $v(0)=10\,\dfrac{\mathrm{m}}{\mathrm{s}}$  at $t=0\,\mathrm{s}$;

- acceleration $a(t)$ with $0\,\dfrac{\mathrm{m}}{\mathrm{s}^2}\leq a(t)\leq 0.1\,\dfrac{\mathrm{m}}{\mathrm{s}^2}$ for all $t$.

Using this information we cannot determine the position of the scooter after $10$ seconds _exactly_, as we do not know the _exact_ velocity of the scooter in those 10 seconds.

What we can do, is _estimate_ the position after $10$ seconds.

To do this, we consider the information we have on the acceleration: it is at _minimum_ $0\,\dfrac{\mathrm{m}}{\mathrm{s}^2}$ during those 10 seconds. If we assume the acceleration equals $0\,\dfrac{\mathrm{m}}{\mathrm{s}^2}$ during those 10 seconds, the velocity will be the lowest during the time frame, which also indicates the least distance traveled by the scooter. So in this case, the velocity will remain $10\,\dfrac{\mathrm{m}}{\mathrm{s}}$ and the distance traveled will be again $100\,\mathrm{m}$. So at _minimum_ the scooter will have position $105\,\mathrm{m}$, or in symbols:

$$
x(10) \ge 105.
$$

Now we focus on the _maximum_ acceleration, which is $0.1\,\dfrac{\mathrm{m}}{\mathrm{s}^2}$. If we assume the acceleration equals $0.1\,\dfrac{\mathrm{m}}{\mathrm{s}^2}$ during those 10 seconds, the velocity will be the highest during the time frame, which also indicates the most distance traveled by the scooter. In this case this means that the velocity increases linearly from $10\,\dfrac{\mathrm{m}}{\mathrm{s}}$ to $10\,\dfrac{\mathrm{m}}{\mathrm{s}}+0.1\,\dfrac{\mathrm{m}}{\mathrm{s}^2}\cdot10\,\mathrm{s}=11\,\dfrac{\mathrm{m}}{\mathrm{s}^2}$ in $10$ seconds. In formula form:

$$
v(t)=10+0.1\cdot t.
$$

Now we know this, we can also estimate the _maximum_ position after $10$ seconds:

$$
x(10) \leq x(0) + \int_{0}^{10}v(t)\,dt = 5 + \int_0^{10}10+0.1\cdot t\,dt = 5 + \left[5\left(10+0.1\cdot t\right)^2\right]_{t=0}^{10} = 5 + \left(605 - 500\right) = 110.
$$

In conclusion, we found that the position of the scooter after $10$ seconds satisfies

$$
105 \le x(10) \le 110,
$$

where we used information about the velocity, i.e. the _first derivative_ of the position, at one time moment and bounds for the acceleration, i.e. the _second derivative_ of the position.

::::

In the above example we could say that we approximated the position after $10$ seconds using a _first order_ Taylor polynomial $T_1(x)=x(0)+v(0)\cdot t$ and that we found an interval for the exact value using bounds on  the _second derivative_.

The next theorem generalises the above examples and gives us the tools to always find an upper bound for the difference between the _exact_ value and an _approximation_ using Taylor polynomials:

::::{prf:theorem}

Define $D$ as an interval that contains the point $a$, $T_n$ as the $n$<sup>th</sup> order Taylor polynomial of $f$ around $a$ and $M$ as an upper bound for $|f^{(n+1)}(x)|$ on the interval $D$. Then

:::{math}
:label: Ex:TaylorPolynomialsAdd:TaylorIneq

|f(x)-T_n(x)|\leq \dfrac{M |x-a|^{n+1}}{(n+1)!}

:::

for all $x$ in $D$.

::::

This theorem can be visualised as in {numref}`Figure %s <Fig:ApproximatingFunctions:error>`, where we use $n=1$.

:::{figure} Images/Fig-TaylorPolynomials-error.svg
:name: Fig:ApproximatingFunctions:error
:figwidth: 50%
:class: dark-light

Suppose $|f''(x)|\leq M$ for all $x$, then $T_1(x)-\frac{M}{2}x^2\leq f(x)\leq T_1(x)+\frac{M}{2}x^2$.

:::


To make talking about these formulae a little easier, we name parts of it:

::::{prf:definition}

The Inequality {eq}`Ex:TaylorPolynomialsAdd:TaylorIneq` is called **Taylor's inequality**.

The expression $f(x)-T_n(x)$ is called the **remainder** $R_n(x)$.

The absolute value of the remainder, $E_n=|R_n(x)|=|f(x)-T_n(x)|$ is the **approximation error**.

::::

The next example shows how you can determine an upper bound for the approximation error.

::::{prf:example}
:label: Ex:TaylorPolynomialsAdd:cos4

Let's construct an approximation of $\cos(0.5)$ by using the fourth-order Taylor polynomial $T_4$ of the cosine function $f(x)=\cos(x)$ centered at $x=0$:

$$
T_4(x) \ = \ 1-\frac{1}{2}x^2+\frac{1}{24}x^4.
$$

The approximation that we find is

$$\cos(\class{red}{0.5})=f(\class{red}{0.5}) \ \approx T_4(\class{red}{0.5}) \ 1-\frac{1}{2}\left(\class{red}{0.5}\right)^2+\frac{1}{24}\left(\class{red}{0.5}\right)^4 \ = \ 0.877604\ldots.$$

In order to find an upper bound for the approximation error we will need to find an $M$ such that the fifth derivative $f^{(5)}$ of the cosine function is smaller than $M$ for all numbers $x$ in the interval $[0, 0.5]$. The fifth derivative of $f(x)=\cos(x)$ is equal to $f^{(5)}(x)=-\sin(x)$. We know that $|-\sin(x)|\leq 1$ for all values of $x$, so we can choose $M$ to be equal to $1$. We get the following upper bound for the remainder:

$$
\begin{align*}
\left|R_4\left(\class{red}{0.5}\right)\right| &= |f(\class{red}{0.5})-T_4(\class{red}{0.5})| \\
&\leq \frac{1\cdot |\class{red}{0.5}-0|^{4+1}}{(4+1)!} \\
&= \frac{(0.5)^{5}}{5!} \\
&= \frac{0.03125}{120} \\
&= 0.00026\ldots.
\end{align*}
$$

Thus, the approximation error is at most $0.00027$, as we must round up to ensure a proper upper bound.

Now we have an upper bound for the _absolute_ value of the error, we can even find an interval in between the _exact_ value of $\cos(0.5)$ lies:

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

Suppose that we want to find an approximation of $\sin(0.8)$ such that the difference between the approximation and the actual value is at most $0.0001$. We will use a Taylor polynomial of the function $f(x)=\sin(x)$ and evaluate it in $x=0.8$. What order Taylor polynomial do we need to use?

The derivatives of the sine function $f(x)=\sin(x)$ are all equal to either $\cos(x)$, $-\sin(x)$, $-\cos(x)$ or $\sin(x)$. This means that for each $n$ and for each $x$ we have $|f^{(n+1)}(x)|\leq 1$. Therefore we know that

$$
\left|R_n\left(0.8\right)\right|\leq \frac{(0.8)^{n+1}}{(n+1)!}.
$$

Using this formula, we can make a table with in each row a different value of $n$ and the corresponding upper bound:

|$n$|$\|R_n(0.8)\|\leq$|
|-|-|
|$0$|$0.8$|
|$1$|$0.32$|
|$2$|$0.085\overline{33}$|
|$3$|$0.0170\overline{66}$|
|$4$|$0.002730\overline{66}$|
|$5$|$0.0003640\overline{88}$|
|$6$|$0.00004161\overline{015873}$|
|$7$|$0.000004161\overline{015873}$|

For $n=3$ the right-hand side of the inequality is $0.0170\overline{66}$. This value is not smaller than 0.0001 and thus a Taylor polynomial of order three may not be sufficient to give us an approximation that is good enough. If $n$  is equal to 4 we obtain that the approximation error is smaller than $0.002730\overline{66}$. After a little trial and error we find that for $n=6$ the error is smaller than $0.00004161\overline{015873}$ and therefore also smaller than $0.0001$. A Taylor polynomial of order 6 will give us the approximation that we want. For the sine function this polynomial is equal to

$$
T_6(x)=x-\frac{1}{6}x^3+\frac{1}{120}x^5.
$$

There is no term of degree six since the sixth derivative of $\sin(x)$ is zero in $x=0$. The approximation that we find is

$$
T_6\left( \class{red}{0.8} \right) \ = \ \class{red}{0.8}-\frac{1}{6}\left( \class{red}{0.8} \right)^3+\frac{1}{120}\left( \class{red}{0.8} \right)^5 \ = \ 0.717397\ldots.
$$

Since the error is smaller than 0.0001 this means that the actual value of $\sin(0.8)$ lies in between $0.7172$ and $0.7175$.

::::

## Grasple exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2286a124-b092-4a23-b292-79c0a03c70b4?id=63715
:label: Grasple:ApproximatingFunctions:LinArctan
:dropdown:
:description: Linearisation of $\arctan(x)$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/21d38731-0b57-4fc5-af15-936ef3a414fc?id=63728
:label: Grasple:ApproximatingFunctions:LinPower
:dropdown:
:description: Linearisation of a power of $x$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b36e91ec-7f75-4bd8-9669-e40968b9f15c?id=78767
:label: Grasple:ApproximatingFunctions:LinApprox
:dropdown:
:description: Approximate a function value using a linearisation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7d9a7257-7c30-4be4-8277-6b57eb17e2c0?id=127213
:label: Grasple:ApproximatingFunctions:LinChange
:dropdown:
:description: Approximate change in function value using a linearisation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8cd84d06-42ea-4ff2-8a3f-86fe5ac45bd9?id=75827
:label: Grasple:ApproximatingFunctions:LinRelative
:dropdown:
:description: Relative errors.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/282946e0-2d88-41b6-970c-55c26d28d714?id=64606
:label: Grasple:ApproximatingFunctions:T2Sine
:dropdown:
:description: Finding $T_2$ for a sine function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0d05a9a9-8d42-4ee3-ac40-706b7ac4844f?id=64953
:label: Grasple:ApproximatingFunctions:T2PolyExp
:dropdown:
:description: Finding $T_2$ for a polynomial times an exponential function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/523a3822-e8b6-4c85-923f-d8c73dcffee1?id=64629
:label: Grasple:ApproximatingFunctions:T3Reciprocal
:dropdown:
:description: Finding $T_3$ of a reciprocal function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4bec421b-5b79-4159-85c8-e6cfdc203606?id=105586
:label: Grasple:ApproximatingFunctions:T1Error
:dropdown:
:description: Using Taylor's inequality for $T_1$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4d3f51de-2210-4f7d-985a-edddfb121b4f?id=104206
:label: Grasple:ApproximatingFunctions:T3Error
:dropdown:
:description: Using Taylor's inequality for $T_3$.

::::