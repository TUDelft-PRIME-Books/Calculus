(Ch:ComplexNumbersCartesian)=
# Complex numbers

## Introduction

Consider the equation

:::{math}
:label: Eq:ComplexNumbers:abc-eq
ax^2+bx+c=0,

:::

where $a\neq0$. In {numref}`Subsec:R:IneqAbs` we have seen that Equation {eq}`Eq:ComplexNumbers:abc-eq` only has solutions when $D=b^2-4ac$ is non-negative and in that case we obtain the two solutions

:::{math}
:label: Eq:ComplexNumbers:abc-sol
x_{1,2}=\frac{-b\pm\sqrt{D}}{2a}.

:::

In many engineering applications, for example in solving second-order linear differential equations (see {numref}`Sec:ODE2:Homogeneous`), you need solutions of Equation {eq}`Eq:ComplexNumbers:abc-eq` even if $D$ is negative. Plugging Equation {eq}`Eq:ComplexNumbers:abc-sol` into Equation {eq}`Eq:ComplexNumbers:abc-eq` still gives a valid equation when $D<0$, but we need to make sense of taking the square root of a negative number. To handle this, we need so-called complex numbers.

## Definition and arithmetics


We start by considering an easier form of Equation {eq}`Eq:ComplexNumbers:abc-eq`, namely

:::{math}
:label: Eq:ComplexNumbers:abc-eq-simple
x^2+1=0,
:::

which we can rewrite into

$$
x^2=-1.
$$

There is no real number of which the square is $-1$, so this seems like a problem. However, mathematicians would not be mathematicians if they could not define their way out of a problem like this.

::::{prf:definition}
:label: Def:ComplexNumbers:i

The **imaginary unit** $i$ is a mathematical constant that satisfies, by definition,

$$
 i^2=-1.
$$


::::

:::{note}
Because of historical conventions we call $i$ imaginary, but that does not mean in the slightest that it is fictitious. There are many physical problems where the imaginary unit (and complex numbers in general) arise naturally.
:::

::::::{prf:notation}
In some fields, particularly in electrical engineering, the imaginary unit is sometimes denoted by $j$ to avoid confusion with the quantity current which often uses the symbol $i$. In this book, we will stick to the symbol $i$.

In some other areas, for example in programming languages, the imaginary unit is sometimes denoted by $I$, but we will also not use this notation in this book.
::::::

We can now define what a complex number is.

::::{prf:definition}
:label: Def:ComplexNumbers:complexnumber

A **complex number** $z$ is an expression of the form

$$
z=a+bi,
$$

where $a\in\mathbb{R}$ and $b\in\mathbb{R}$. The real number $a$ is known as the **real part** of $z$ and is denoted by

$$
\Re{z}=a,
$$

while the real number $b$ is known as the **imaginary part** of $z$ and is denoted by

$$
\Im{z}=b.
$$

The set of all complex numbers is denoted by the symbol $\mathbb{C}$ and is called the **complex plane**.

::::

::::::{warning}
It is a common error to think that the imaginary part of $z=a+bi$ would be $bi$. This is not correct; the imaginary part is $b$. Indeed, we have defined the imaginary part to be the number before the $i$, **excluding** the $i$.
::::::




::::{prf:example}
:label: Ex:ComplexNumbers:realimaginary

We consider the complex number $z=-1+2i$. Then it is in the form $z=a+bi$ with $a=-1\in\mathbb{R}$ and $b=2\in\mathbb{R}$. As such, we find that

$$
\Re{z}=-1,
$$

and 

$$
\Im{z}=2.
$$



::::

Just like we can visualise real numbers on a number line, we can visualise complex numbers in the complex plane. By convention, the horizontal axis indicates the value of the real part of a complex number and the vertical axis indicates the imaginary part of the same complex number. In {numref}`Figure %s <Fig:ComplexNumbers:complexplane>` you can see this visualisation. 

:::{applet}
:url: calculus/complex_numbers/visualisation_of_the_complex_plane
:name: Fig:ComplexNumbers:complexplane
:class: dark-light

Visualisation of the complex plane $\mathbb{C}$.

:::

We will view the set of all real numbers $\mathbb{R}$ as a part of the complex numbers $\mathbb{C}$. By this we mean that if $x$ is a real number, we can interpret it as the complex number with $\Re{x}=x$ and $\Im{x}=0$. Conversely, if $z$ is a complex number with $\Im{z}=0$, we interpret it as a real number. If a complex number is not a real number, we refer to it as **non-real**.



You can add, subtract, multiply and, in most cases, divide real numbers to obtain other real numbers. With complex numbers we can perform the same operations as with real numbers. This is precisely the reason why we call complex numbers 'numbers'. Addition, subtraction and multiplication are performed by simply working out the brackets.

::::{prf:definition} 
:label: Def:ComplexNumbers:Arithmetics
If $z=a+bi$ and $w=c+di$ are complex numbers (with $a,b,c,d\in\mathbb{R}$), then we define the **sum** $z+w$, the **difference** $z-w$ and the **product** $zw$, as well as the complex number $-z$ (which is called the **additive inverse** of $z$, or simply **minus $z$**), as the complex numbers

\begin{align*}
z+w &= (a+c)+(b+d)i, \\
z-w &= (a-c)+(b-d)i, \\
zw &= (ac-bd)+(ad+bc)i,\\
-z&=-a+(-b)i.
\end{align*}

In addition, if $n\in\mathbb{Z}$ with $n\geq 1$, we define the $n$th **power** of $z$ as

$$
z^n=\underbrace{z\cdot z\cdot\cdots\cdot z}_{n\text{ times}}.
$$

Finally, we define $z^0=1$.
::::

The standard computation rules that hold for real numbers, hold for complex numbers as well.

::::{prf:theorem} 
:label: Thm:ComplexNumbers:Commassdistr
Let $z_1$, $z_2$ and $z_3$ be complex numbers. Then we have

\begin{align*}
z_1-z_1&=0,&\\
z_1+z_2 &= z_2+z_1,\qquad&\text{commutativity of addition} \\
(z_1+z_2)+z_3 &= z_1+(z_2+z_3),\qquad&\text{associativity of addition} \\
z_1z_2 &= z_2z_1,\qquad&\text{commutativity of multiplication}\\
(z_1z_2)z_3&=z_1(z_2z_3),\qquad&\text{associativity of multiplication}\\
z_1(z_2+z_3)&=z_1z_2+z_1z_3,\qquad&\text{distributivity}\\
z_1+0&=0+z_1=z_1,\qquad&0\text{ is the neutral element for addition}\\
1z_1&=z_11=z_1.\qquad&1\text{ is the neutral element for multiplication}\\
\end{align*}

Finally, if $z_1z_2=0$ then we must have $z_1=0$ or $z_2=0$.
::::


::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:Commassdistr`
:class: tudproof, dropdown
All of these rules follow by writing out both sides of the equation using the definition and using the corresponding property of real numbers. 

For instance, if we want to show associativity of multiplication, we write $z_1=a+bi$, $z_2=c+di$ and $z_3=x+yi$ with $a,b,c,d,x,y\in \mathbb{R}$. Then we have

\begin{align*}
(z_1z_2)z_3&=((ac-bd)+(ad+bc)i)(x+yi)\\
&=\left((ac-bd)x-(ad+bc)y\right)+\left((ac-bd)y+(ad+bc)x\right)i\\
&=\left(acx-bdx-ady-bcy\right)+\left(acy-bdy+adx+bcx\right)i,
\end{align*}

and

\begin{align*}
z_1(z_2z_3)&=(a+bi)((cx-dy)+(cy+dx)i)\\
&=\left(a(cx-dy)-b(cy+dx)\right)+\left(a(cy+dx)+b(cx-dy)\right)i\\
&=\left(acx-ady-bcy-bdx\right)+\left(acy+adx+bcx-bdy\right)\\
&=\left(acx-bdx-ady-bcy\right)+\left(acy-bdy+adx+bcx\right)i.
\end{align*}

We conclude that $(z_1z_2)z_3=z_1(z_2z_3)$.

To check the final statement, we suppose that $z_1z_2=0$. We write $z_1=a+bi$ and $z_2=c+di$. Then we have

$$
 0=z_1z_2=(ac-bd)+(ad+bc)i,
$$

which gives the system of equations

:::{math}
:label: Eq:ComplexNumbers:zerodivisor
 \begin{cases}0=ac-bd,\\ 0=d+bc,\end{cases}
:::

since a complex number can only be $0$ if both its real and imaginary parts are $0$.

If $z=0$ we are done, so we assume that $z\neq 0$. In that case at least one of the real numbers $a$ and $b$ must be non-zero, which means that $a^2+b^2>0$. We now first multiply the first equation of {eq}`Eq:ComplexNumbers:zerodivisor` by $a$ and the second equation by $b$ and add these to obtain

$$
 0=a(ac-bd)+b(ad+bc)=\left(a^2+b^2\right)c.
$$

Since $a^2+b^2>0$ and $c$ is real, we must have $c=0$. Similarly, we multiply the first equation of {eq}`Eq:ComplexNumbers:zerodivisor` by $-b$ and the second one by $a$ and add them to obtain

$$
 0=-b(ac-bd)+a(ad+bc)=\left(a^2+b^2\right)d.
$$

Again, since $a^2+b^2>0$ and $d$ is real, we must have $d=0$. We then find $z_2=c+di=0$, as desired.
::::

:::{note}
The rules from {prf:ref}`Thm:ComplexNumbers:Commassdistr` also show why it make sense to define addition and multiplication like we did. Indeed, if $z=a+bi$ and $w=c+di$ then we can work out the brackets to obtain

\begin{align*}
(a+bi) + (c+di)
&= a + bi + c + di \\
&= a + c + bi + di \\
&= (a+c)+(b+d)i\\
&=z+w
\end{align*}

and

\begin{align*}
(a+bi)(c+di)&= a(c+di)+bi(c+di) \\
&= ac+adi+bci+bdi^2 \\
&= ac+adi+bci-bd \\
&= ac-bd+adi+bci \\
&= (ac-bd)+(ad+bc)i\\
&=zw.
\end{align*}

:::

:::{important}
In practice, you add, subtract and multiply complex numbers by working out the brackets and not by learning the defining properties from {prf:ref}`Def:ComplexNumbers:Arithmetics` by heart.
:::

::::{prf:example} Addition and subtraction
:label: Ex:ComplexNumbers:Addition
Addition of complex numbers is very straightforward. Indeed, suppose we have $z=4+3i$ and $w=-1-2i$. Then we can compute

\begin{align*}
z+w &= (4+3i)+(-1-2i) \\
&= 4+3i+(-1)-2i \\
&= 4+(-1)+3i-2i \\
&= 3+i.
\end{align*}

Similarly, subtraction is done by subtracting the real parts and subtracting the imaginary parts. In this case, we obtain

\begin{align*}
z-w &= (4+3i)-(-1-2i) \\
&= 4+3i-(-1)-(-2i) \\
&= 4+1+3i+2i \\
&= 5+5i.
\end{align*}

::::

::::{prf:example} Multiplication
:label: Ex:ComplexNumbers:Multiplication
Suppose we want to multiply $z=4+3i$ and $w=-1-2i$. Then we can expand the brackets to obtain

\begin{align*}
zw &= (4+3i)(-1-2i) \\
&= 4(-1-2i)+3i(-1-2i) \\
&= 4\cdot(-1)+4\cdot (-2i)-3i+3\cdot (-2)i^2 \\
&= -4-8i-3i-6 \cdot(-1)\\
&= 2-11i.
\end{align*}

::::

Now we consider the geometric interpretation of adding complex numbers. If we add $z=a+bi$ and $w=c+di$, we add the real and imaginary parts to obtain $z+w=(a+c)+(b+d)i$. This means we add the coordinates of the corresponding points. This works similar to the addition of vectors, see {numref}`Chapter:VectorAlgebra`. Thus, geometrically we can add two complex numbers by following the parallelogram rule. That is, the lines from the origin to the two complex numbers form two sides of a parallelogram with vertices $0$, $z$, $z+w$, and $w$; see {numref}`Figure %s <Fig:ComplexNumbers:complexadd>`.

:::{applet}
:url: calculus/complex_numbers/adding_complex_numbers
:name: Fig:ComplexNumbers:complexadd
:class: dark-light

Adding complex numbers follows the parallelogram rule.

:::


If we want to interpret the other operations such as multiplication easily, we first need another way of writing complex numbers, which we will study in {numref}`Ch:ComplexNumbersPolar`. 

Before we consider division of complex numbers we will turn our attention first to solving quadratic equations.

### Solving quadratic equations

Now that we know how addition and multiplication of complex numbers work, we can use complex numbers to solve quadratic equations, even those that do not have real solutions.

::::{prf:theorem}
:label: Thm:ComplexNumbers:roots

Let $a$ be a real number. Then the two complex numbers $-ai$ and $ai$ are solutions to the equation $x^2=-a^2$ and they are the only complex numbers that are solutions to this equation.

::::

:::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:roots`
:class: tudproof, dropdown

First we consider $x=-ai$ and take its square. This gives

$$
\left(-ai\right)^2 = a^2i^2 = -a^2.
$$

This shows that $x=-ai$ is indeed a solution of the equation $x^2=-a^2$.

For $x=ai$ we obtain

$$
 \left(ai\right)^2 = a^2i^2 = -a^2.
$$

We find that $x=ai$ also is a solution of the equation $x^2=-a^2$.

Suppose $z=c+di$ also satisfies $z^2=-a^2$. Then we obtain

$$
 -a^2=z^2=(c+di)^2=(c+di)(c+di)=c^2-d^2+2cdi.
$$

Since two complex numbers are the same precisely when their real and imaginary parts are the same, we must have

$$
 -a^2=c^2-d^2,\qquad 0=2cd.
$$

The second equation gives either $c=0$ or $d=0$. If $d=0$, we obtain $-a^2=c^2$, which has no solutions if $a\neq 0$, while it has the solution $c=0$ if $a=0$. If $c=0$, we obtain $-a^2=-d^2$, which gives $d=\pm a$. In any case, we find that $z$ must be $-ai$ or $ai$.

:::


In particular, the only solutions to Equation {eq}`Eq:ComplexNumbers:abc-eq-simple` are $z=i$ and $z=-i$.

We can revisit the general case given in Equation {eq}`Eq:ComplexNumbers:abc-eq`. Let us start with an example.

::::{prf:example}
:label: Ex:ComplexNumbers:compsquare

Consider the second degree polynomial $p(z) =z^2+2z+5$. We want to solve the equation $p(z)=0$.

We are going to do this by completing the square. This means that we rewrite $p$ in the form $p(z) = (z+q)^2+r$ for some numbers  $q$ and $r$.

Expanding the brackets gives that we want 

$$
 z^2+2z+5=z^2+2qz + (q^2+r).
$$

This means that $2=2q$ and $5=q^2+r$. The first equation gives us $q=1$. Plugging this into the second equation, we obtain $5=1+r$, so $r=4$. Therefore, we obtain

$$
 z^2+2z+5=(z+1)^2+4.
$$

To solve $z^2+2z+5=0$, we can now write

\begin{align*}
&z^2+2z+5 =0 \\
\Longleftrightarrow\qquad&(z+1)^2+4=0 \\
\Longleftrightarrow\qquad&(z+1)^2 =-4 \\
\Longleftrightarrow\qquad & z+1 = \pm 2i \\
\Longleftrightarrow\qquad &z = -1 \pm 2i.
\end{align*}

Here we used {prf:ref}`Thm:ComplexNumbers:roots`.

In addition to helping us find roots of the polynomial, writing it as $z^2+2z+5=(z+1)^2+4$ has another advantage: we can use it to immediately read off that $4$ is the minimal value of the parabola

$$
 y=z^2+2z+5=(z+1)^2+4,
$$

when only considering real values of $z$. Indeed, we have $(z+1)^2\geq 0$ for all real $z$, so we obtain the minimal value when $z=-1$.
::::

In general, you can use the technique of completing the square to write any polynomial $az^2+bz+c$ in the form $a ((z+p)^2+q)$ by first factoring out the $a$, subsequently choosing the $p$ such that the linear term (the term involving $z$) is correct, and letting $q$ be the remainder. Using this form, you can then determine the zeros of the polynomial. As such, we obtain the following theorem.


::::{prf:theorem}
:label: Thm:ComplexNumbers:rootsquad

Let $a\neq 0$, $b$ and $c$ be real numbers and let $D=b^2-4ac$. Then the equation 

$$
 az^2+bz+c=0
$$

for $z\in\mathbb{C}$ has two real roots if $D>0$, it has a double real root if $D=0$, and it has two non-real roots if $D<0$.

If $D<0$, these roots are given by

$$
 z=-\frac{b}{2a}\pm\sqrt{-\frac{b^2-4ac}{4a^2}}i.
$$

::::

:::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:rootsquad`
:class: tudproof, dropdown
The cases $D>0$ and $D=0$ have been discussed in {numref}`Subsec:R:IneqAbs`. Now suppose $D<0$. Completing the square, we can rewrite $az^2+bz+c=0$ into

$$
 a\left(z+\frac{b}{2a}\right)^2-\frac{b^2}{4a}+c=0,
$$

which can be written as

$$
 \left(z+\frac{b}{2a}\right)^2=\frac{b^2}{4a^2}-\frac{c}{a}=\frac{b^2-4ac}{4a^2}.
$$

By assumption, we have $\dfrac{b^2-4ac}{4a^2}<0$. So using {prf:ref}`Thm:ComplexNumbers:roots` we find

$$
 z+\frac{b}{2a}=\pm\sqrt{-\frac{b^2-4ac}{4a^2}}i,
$$

which gives

$$
 z=-\frac{b}{2a}\pm\sqrt{-\frac{b^2-4ac}{4a^2}}i.
$$

So the equation has two non-real roots.
:::


### Complex conjugates and division

Before we turn to division, we introduce one more arithmetic operation.

::::{prf:definition}
:label: Def:ComplexNumbers:conjugate

If $z=a+bi$ is a complex number (with $a,b\in\mathbb{R}$), the **complex conjugate** or **conjugate** $\overline{z}$ is defined as

$$
\overline{z}=a-bi,
$$

which is also a complex number.

::::

::::::{prf:notation}
In some texts, the complex conjugate of a complex number is denoted by $z^*$ instead of $\overline{z}$.
::::::

::::{prf:example} Complex conjugation
:label: Ex:ComplexNumbers:ComplConj
Suppose we want to find the complex conjugates of $z=4+3i$, $w=-1-2i$ and $v=5(=5+0i)$. This simply means that we should change the sign of the imaginary part of each of the complex numbers, so we obtain

$$
 \overline{z}=4-3i,\qquad \overline{w}=-1-(-2)i=-1+2i,\qquad \overline{v}=5-0i=5.
$$

::::

In {prf:ref}`Ex:ComplexNumbers:ComplConj` we saw that the complex conjugate of the real number $v=3$ is equal to $v$ itself. This is true for all real numbers, as can be seen from the following theorem.

::::{prf:theorem}
:label: Thm:ComplexNumbers:realz

Assume $z\in\mathbb{C}$. Then we have $z\in\mathbb{R}$ if and only if $z=\overline{z}$.

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:realz`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:realz` -->

Assume $z\in\mathbb{C}$ and write $z=a+bi$ with $a,b\in\mathbb{R}$.

If $z\in\mathbb{R}$, then $\Im{z}=b=0$. By definition, we find

$$
 \overline{z}=a-bi=a-0i=a=z.
$$

Now suppose that $z=\overline{z}$. This means that

$$
 a+bi=a-bi.
$$

Simplifying this equation gives

$$
 2bi=0.
$$

By {prf:ref}`Thm:ComplexNumbers:Commassdistr` we must have $b=0$, which gives $z\in\mathbb{R}$.

::::

Now we look at the geometric interpretation of complex conjugation. The complex conjugate $\bar z$ changes the sign of the imaginary part of the number $z$, that is $\overline{a+bi} = a-bi$. As the imaginary part of a complex number corresponds to the second coordinate of its representation in the complex plane, taking the complex conjugate of a complex number reflects it across the real axis (the horizontal axis). See {numref}`Figure %s <Fig:ComplexNumbers:complexconj>`.

:::{applet}
:url: calculus/complex_numbers/complex_conjugation
:name: Fig:ComplexNumbers:complexconj
:class: dark-light

Complex conjugation reflects a number in the real axis.

:::

The following result will turn out to be the reason why the complex conjugate can be used to simplify the quotient of two complex numbers.

::::{prf:theorem} 
:label: Thm:ComplexNumbers:ComplConjCompl
If $z=a+bi$ is a complex number with $a,b\in\mathbb{R}$, then 

$$
 z\overline{z}=a^2+b^2
$$

is a non-negative real number.

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:ComplConjCompl`
:class: dropdown, tudproof 
We have $\overline{z}=a-bi$, so we can work out the product $z\overline{z}$ as

\begin{align*}
z\overline{z} &= (a+bi)(a-bi) \\
&= a(a-bi)+bi(a-bi) \\
&= a^2+a(-b)i+bai+b(-b)i^2 \\
&= a^2-abi+bai-b^2\cdot(-1) \\
&= a^2+b^2.
\end{align*}

Since $a$ and $b$ are real numbers, $a^2+b^2$ is a non-negative real number.
::::



Of the arithmetic operations, division is the most complicated. The reason for this is that there is no straightforward way to simplify a fraction when the denominator is a sum of two objects. And complex numbers just so happen to be the sum of two objects (the real part and $i$ times the imaginary part). We can circumvent this by multiplying the denominator and numerator by the same complex number in the hope that the resulting denominator is a single real number. {prf:ref}`Thm:ComplexNumbers:ComplConjCompl` tells us which number we should choose: the complex conjugate of the denominator. In general, we obtain the following result.

::::{prf:theorem}
:label: Thm:ComplexNumbers:division

Let $z=a+bi$ be a complex number (with $a,b\in\mathbb{R}$) with $z\neq 0$. Then there is a unique complex number, denoted by $\dfrac{1}{z}$ or $z^{-1}$, which satisfies $z\dfrac{1}{z}=1$, namely 

$$
 \frac{1}{z}=\frac{a}{a^2+b^2}-\frac{b}{a^2+b^2}i.
$$

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:division`
:class: dropdown, tudproof 
We try to solve the equation

$$
zw=1
$$

for $w$. For this, we write $w=c+di$ and work out the product $zw$ to obtain

$$
 (ac-bd)+(ad+bc)i=1.
$$

Since two complex numbers are equal precisely when their real and imaginary parts are equal, we find

$$
 ac-bd=1,\qquad ad+bc=0.
$$

We first consider the case $a\neq 0$. Then we obtain 

$$
 d=-\frac{b}{a}c.
$$

We substitute this in the the equation $ac-bd=1$ to obtain

$$
 ac-b\left(-\frac{b}{a}c\right)=1,
$$

which simplifies into

$$
 ac+\frac{b^2}{a}c=1.
$$

Multiplying by $a$ and factoring gives

$$
 (a^2+b^2)c=a,
$$

which gives

$$
 c=\frac{a}{a^2+b^2}.
$$

Substituting this back into $d=-\dfrac{b}{a}c$ gives

$$
 d=-\frac{b}{a}\frac{a}{a^2+b^2}=-\frac{b}{a^2+b^2}.
$$

In this case, we obtain the unique solution

$$
 w=c+di=\frac{a}{a^2+b^2}-\frac{b}{a^2+b^2}i.
$$

Now in the special case $a=0$, we must have $b\neq 0$, since otherwise we would have $z=0$. In that case, the equations become

$$
 -bd=1,\qquad bc=0.
$$

Since $b\neq0$, we obtain the unique solution $d=-\frac{1}{b}$ and $c=0$, so we find

$$
 w=-\frac{1}{b}i.
$$

Note that this is the same formula as the case for $a\neq 0$, since we can write

$$
 w=-\frac{1}{b}i=\frac{0}{0^2+b^2}-\frac{b}{0^2+b^2}i=\frac{a}{a^2+b^2}-\frac{b}{a^2+b^2}i.
$$

::::


::::{prf:definition}
:label: Def:ComplexNumbers:Division
Let $z$ and $w$ in $\mathbb{C}$ with $w\neq 0$. Then we define the **quotient** $\dfrac{z}{w}$ as

$$
\dfrac{z}{w}=z\frac{1}{w}.
$$

In addition, if $n\in\mathbb{Z}$ with $n\geq 1$, we define a **negative power** of $z\neq 0$ as

$$
z^{-n}=\frac{1}{z^n}
$$

::::

::::{prf:example}
:label: Ex:ComplexNumbers:Division


Suppose we want to divide $z=4+3i$ by $w=-1-2i$. Then we should multiply both parts of the fraction by $\overline{w}=-1+2i$. This gives

$$
\frac{z}{w}=\frac{z}{w}\frac{\overline{w}}{\overline{w}}=\frac{z\overline{w}}{w\overline{w}}=\frac{(4+3i)(-1+2i)}{(-1-2i)(-1+2i)}=\frac{-10+5i}{5}.
$$

This fraction can be simplified directly and we obtain

$$
\frac{z}{w}=\frac{-10+5i}{5}=-2+i.
$$
::::




We can combine the complex conjugate with the other four operations, which gives the following theorem.

::::{prf:theorem}
:label: Thm:ComplexNumbers:conjops

If $z$ and $w$ are complex numbers, then the following identities hold.

\begin{align*}
\overline{\overline{z}} &= z, \\
\overline{z+w} &= \overline{z}+\overline{w}, \\
\overline{z-w} &= \overline{z}-\overline{w}, \\
\overline{zw} &= \overline{z}\,\overline{w}, \\
\overline{\left(\frac{z}{w}\right)} &= \frac{\overline{z}}{\overline{w}}, & (\text{assuming}\ w\neq0).
\end{align*}

In addition, if $n\in\mathbb{Z}$ we have the identity

$$
 \overline{z^n}=\overline{z}^n,\qquad \left(\text{assuming}\ z\neq0\ \text{if}\ n<0\right).
$$
::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:conjops`
:class: dropdown, tudproof 
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:conjops` -->

We assume $z=a+bi$ and $w=c+di$, $a,b,c,d\in\mathbb{R}$. Then we obtain each of the identities as follows.

_Double conjugation_:

\begin{align*}
\overline{\overline{z}} &= \overline{\overline{a+bi}} \\
&= \overline{a-bi} \\
&= a+bi \\
&= z.
\end{align*}

_Addition and conjugation_:

\begin{align*}
\overline{z+w} &= \overline{(a+c)+(b+d)i} \\
&= (a+c)-(b+d)i \\
&= (a-bi)+(c-di) \\
&= \overline{z}+\overline{w}.
\end{align*}

_Subtraction and conjugation_:

\begin{align*}
\overline{z-w} &= \overline{(a-c)+(b-d)i} \\
&= (a-c)-(b-d)i \\
&= (a-bi)-(c+di) \\
&= \overline{z}-\overline{w}.
\end{align*}

_Multiplication and conjugation_:

\begin{align*}
\overline{zw} &= \overline{(ac-bd)+(ad+bc)i} \\
&= (ac-bd)-(ad+bc)i \\
&= (ac-adi)-(bd+bci) \\
&= a(c-di)-b(d+ci) \\
&= a(c-di)-b(ci-di^2) \\
&= a(c-di)-bi(c-di) \\
&= (a-bi)(c-di) \\
&= \overline{z}\overline{w}.
\end{align*}

_Division and conjugation_:

\begin{align*}
\overline{\left(\frac{z}{w}\right)} &= \overline{\frac{ac+bd}{c^2+d^2}+\frac{bc-ad}{c^2+d^2}i} \\
&= \frac{ac+bd}{c^2+d^2}-\frac{bc-ad}{c^2+d^2}i \\
&= \frac{ac+bd-(bc-ad)i}{c^2+d^2} \\
&= \frac{(a-bi)(c+di)}{(c-di)(c+di)} \\
&= \frac{a-bi}{c-di}\frac{c+di}{c+di} \\
&= \frac{\overline{z}}{\overline{w}}.
\end{align*}

_Powers and conjugation_:

If $n>0$ we have, using the multiplicative property,

\begin{align*}
\overline{z^n}&=\overline{\underbrace{z\cdot\cdots\cdot z}_{n\text{ times}}}\\
&=\underbrace{\overline{z}\cdot\cdots\cdot\overline{z}}_{n\text{ times}}\\
&=\overline{z}^n.
\end{align*}

For $n=0$, we find

$$
\overline{z^0}=\overline{1}=1=\overline{z}^0.
$$

Finally, for $n<0$, we find, using the other properties and using that $-n>0$

\begin{align*}
\overline{z^n}&=\overline{\frac{1}{z^{-n}}}\\
&=\frac{\overline{1}}{\overline{z^{-n}}}\\
&=\frac{1}{\overline{z}^{-n}}\\
&=\overline{z}^n.
\end{align*}

::::


Even better, we can relate the complex conjugate to the real and imaginary part of a complex number.

::::{prf:theorem}
:label: Thm:ComplexNumbers:conjparts

If $z$ is a complex number, then the following identities hold:

\begin{align*}
\frac{z+\overline{z}}{2} &= \Re{z}, \\
\frac{z-\overline{z}}{2i} &= \Im{z}.
\end{align*}

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:conjparts`
:class: dropdown, tudproof 
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:conjparts` -->

We assume $z=a+bi$, $a,b\in\mathbb{R}$. Then we find

_Conjugation and real part_:

\begin{align*}
\frac{z+\overline{z}}{2} &= \frac{(a+bi)+(a-bi)}{2} \\
&= \frac{2a}{2} \\
&= a \\
&= \Re{z}.
\end{align*}

_Conjugation and imaginary part_:

\begin{align*}
\frac{z-\overline{z}}{2i} &= \frac{(a+bi)-(a-bi)}{2i} \\
&= \frac{2bi}{2i} \\
&= b \\
&= \Im{z}.
\end{align*}


::::







(Sec:ComplexNumbers:SolvingEquations)=
## Solving equations

The reason for introducing complex numbers is to ensure that more equations have solutions, for example $z^2+1=0$. In this section, we consider equations involving complex numbers. This means that not only the solutions may be complex, but also that the coefficients in the equations can be complex.


We already saw in {prf:ref}`Thm:ComplexNumbers:rootsquad` that every quadratic equation with real coefficients has a solution in $\mathbb{C}$.  It turns out that something much stronger holds, namely, that every (non-constant) polynomial equation with coefficients in $\mathbb{C}$, for instance  $(1+i)x^4 - 2x^2 + x = 10i$,  has solutions in $\mathbb{C}$. This is the content of the following theorem.

::::{prf:theorem} Fundamental Theorem of algebra
:label: Thm:ComplexNumbers:fundamental

Consider a polynomial $p(z)$ of degree $n$,

$$
p(z) = a_n z^n + a_{n-1} z^{n-1} + \cdots + a_1 z + a_0,
$$

where the coefficients $a_n, a_{n-1}, \ldots, a_0$ are complex numbers and $a_n\neq 0$. Then you can factor the polynomial in linear terms, that is

$$
p(z) = a_n (z-b_1)(z-b_2) \cdots (z-b_n)
$$

for some complex numbers $b_1, b_2, \ldots, b_n$.

::::

Observe that this factorisation means that $b_1, b_2, \ldots, b_n$ are the zeros (= roots) of the polynomial $p(z)$. It might happen that the $b$'s are complex numbers, even if $a_1, a_2, \ldots, a_n$ are real. It is also important to note that some of the zeros $b_1, b_2, \ldots, b_n$ may coincide. 

As far as the authors of this book are aware, there is no elementary proof of this theorem. We will provide one proof that uses techniques from later chapters.

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:fundamental`
:class: dropdown, tudproof
We will consider the modulus $|p(z)|$ of $p(z)$, see {numref}`Ch:ComplexNumbersPolar`. Using the reverse triangle inequality form {prf:ref}`Thm:ComplexNumbers:complextriangle` we have

\begin{align*}
 |p(z)|&=\left|a_nz^n+\left(a_{n-1} z^{n-1} + \cdots + a_1 z + a_0\right)\right|\\
 &\geq \left|\left|a_nz^n\right|-\left|a_{n-1} z^{n-1} + \cdots + a_1 z + a_0\right|\right|\\
 &\geq \left|a_nz^n\right|-\left|a_{n-1} z^{n-1} + \cdots + a_1 z + a_0\right|
\end{align*}

Now we use the triangle inequality from {prf:ref}`Thm:ComplexNumbers:complextriangle` and {prf:ref}`Thm:ComplexNumbers:polarmultdiv` we obtain

\begin{align*}
 |p(z)|&\geq \left|a_nz^n\right|-\left|a_{n-1} z^{n-1} + \cdots + a_1 z + a_0\right|\\
 &\geq \left|a_nz^n\right|-\left(\left|a_{n-1}z^{n-1}\right|+\cdots+\left|a_1z\right|+\left|a_0\right|\right)\\
 &=\left|a_n\right||z|^n-\left|a_{n-1}\right||z|^{n-1}-....-\left|a_1\right||z|-\left|a_0\right|.
\end{align*}

Since $a_n\neq 0$, we see that the righthand-side of this inequality tends to $\infty$ as $|z|\rightarrow \infty$ (see {numref}`Section:Limitinf`). As such, there must exist some $R>0$ such that for all $z\in\mathbb{C}$ with $|z|\geq R$ we have

$$
|p(z)|> |p(0)|.
$$

On the other hand, the disk 

$$
 D=\left\{z\in\mathbb{C}\,\middle| \,|z|\leq R\right\}
$$

is closed and bounded. In addition, the real valued function of two variable

$$
 f(x,y)=|p(x+iy)|
$$ 

is continuous (see {numref}`Section:LimContnd`). By {prf:ref}`Thm:GlobExtrnd:EVT` we can find $z_0$ in $D$ such that

$$
 \left|p\left(z_0\right)\right|\leq \left|p(z)\right|
$$

for $z$ in $D$. Since for $z\in\mathbb{C}$ with $|z|\geq R$ we have

$$
 |p(z)|>|p(0)|\geq \left|p\left(z_0\right)\right|,
$$

we find that

$$
 \left|p\left(z_0\right)\right|\leq \left|p(z)\right|
$$

for all $z\in\mathbb{C}$. We will show that $p\left(z_0\right)=0$.


We argue by contradiction and we assume that $p(z_0)\neq 0$. We consider the polynomial

$$
 q(z)=\frac{p(z+z_0)}{p(z_0)}.
$$

We first note that

$$
 q(0)=\frac{p(0+z_0)}{p(z_0)}=1.
$$

In addition, since $\left|p\left(z_0\right)\right|\leq \left|p(z)\right|$ for all $z\in\mathbb{C}$, we have

$$
 \left|q(z)\right|=\left|\frac{p(z+z_0)}{p(z_0)}\right|=\left|p(z+z_0)\right|\frac{1}{|p(z_0)|}\geq |p(z_0)|\frac{1}{|p(z_0)|}=1
$$

for all $z\in\mathbb{C}$. Since $p$ is of degree $n$, $q$ must be of degree $n$ as well. Since $q$ is a polynomial with $q(0)=1$, we can write

$$
 q(z)=1+b_mz^m+b_{m+1}z^{m+1}+\cdots +b_nz^n,
$$

where $b_m\neq 0$. This means that $b_mz^m$ is the first non-zero term in $q$ apart from the constant term $1$. Using this way of expressing $q$, we can more compactly write

$$
 q(z)=1+b_mz^m+z^{m+1}r(z),
$$

where $r(z)$ is a polynomial.

According to {prf:ref}`Thm:ComplexNumbers:rootsunity` we can pick a complex number $w$ with

$$
 w^m=\frac{-1}{b_m},
$$

which gives

$$
 w^mb_m=-1.
$$

We will look for a complex number $z=tw$, where $t$ is a positive real number, which has $|q(z)|<1$, which then gives a contradiction. For complex numbers of this form we can write

$$
q(z)=q(tw)=1+t^mw^mb_m+t^{m+1}w^{m+1}r(tw)=1-t^m+t^{m+1}w^{m+1}r(tw).
$$ 

We denote this final term by

$$
 E(t)=t^{m+1}w^{m+1}r(tw).
$$

Since $r$ is a polynomial, which is continuous, we can take the limit as $t\rightarrow 0$ (see {numref}`Section:LimitPoint`)

$$
 \lim_{t\rightarrow 0}\frac{|E(t)|}{t^m}=\lim_{t\rightarrow 0}tw^{m+1}r(tw)=0\cdot w^{m+1}r(0)=0.
$$

This means that we can pick $0<\delta<1$ such that for all $t$ with $0<t<\delta$ we have

$$
\frac{|E(t)|}{t^m}<\frac{1}{2},
$$

which gives

$$
|E(t)<\frac{1}{2}t^m.
$$

For these values of $t$, we obtain using the triangle inequality from {prf:ref}`Thm:ComplexNumbers:complextriangle`

$$
 |q(tw)|=\left|1-t^m+E(t)\right|\leq|1-t^m|+|E(t)|.
$$

Since $0<t<\delta<1$, we have $1-t^m>0$, which gives

$$
|q(tw)|=\left|1-t^m+E(t)\right|\leq|1-t^m|+|E(t)|\leq 1-t^m+\frac{1}{2}t^m=1-\frac{1}{2}t^m<1.
$$

This contradicts the previously established result that $|q(z)|\geq 1$ for all $z\in\mathbb{C}$. This can only mean that our assumption that $p(z_0)\neq 0$ is false, which means that

$$
 p(z_0)=0.
$$

Now in oder to establish the factorisation in linear factors, we consider the expression

$$
 \frac{p(z)}{z-z_0}.
$$

According to {prf:ref}`Thm:RationalFunctions:PolynomialLongDivision` we can find polynomials $r$ and $s$, where the degree of $s$ is $n-1$ and the degree of $r$ is $0$ (as it should be strictly less than $1$) with

$$
 \frac{p(z)}{z-z_0}=s(z)+\frac{r(z)}{z-z_0}.
$$

Since $r$ has degree $0$, it is constant, so we can write $r(z)=A$ for some $A\in\mathbb{C}$. We can rewrite the equation above into

$$
 p(z)=s(z)(z-z_0)+A.
$$

Since $p(z_0)=0$, we find that

$$
 0=p(z_0)=s(z_0)(z_0-z_0)+A=A,
$$

so $A=0$. This means that

$$
 p(z)=s(z)(z-z_0).
$$

Now $s$ is a polynomial. If $s$ is not constant, we can use the first part of the theorem to find a complex number $z_1$ with $s(z_1)=0$. Then we can write 

$$
 p(z)=t(z)(z-z_0)(z-z_1)
$$

where $t(z)$ is a polynomial of degree $n-2$. We can repeat this process, until we find that

$$
 p(z)=B(z-z_0)(z-z_1)\cdots(z-z_{n-1})
$$

for some complex numbers $B,z_2,\cdots,z_{n-1}$. If we write out the product on the right-hand side of the equation, we see that $B$ is the coefficient of $z^n$. This means that $B=a_n$, which gives the factorisation from the theorem.
::::

We will illustrate the theorem using some examples.

::::{prf:example}
:label: Ex:ComplexNumbers:polyreal

Consider $p(z)=z^2+3z+2$. Using the techniques from {numref}`Subsec:R:IneqAbs`, we can factor the polynomial as $p(z) = (z+2)(z+1)$ and thus find the zeros as $-2$ and $-1$.

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polycomplcon

Consider the equation $z^2=-1$, which is equivalent to $z^2+1=0$. We can now factor $z^2+1$ to $(z+i)(z-i)$ and thus find that $i$ and $-i$ are the two solutions of this equation.

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polycompl

While a polynomial of degree $n$ can be factored in $n$ linear terms, and we have $n$ values $b_i$, this does not mean that there are $n$ distinct zeros. For example $p(z) = z^2+4z+4$ can be factored as $p(z)=(z+2)^2$ and thus only has $z=-2$ as a solution. However, the term $(z+2)$ occurs twice in the factorisation. We therefore say that the multiplicity of the zero $-2$ is equal to two.

::::

In particular, we see that any polynomial of degree $n$ has $n$ complex zeros _counting multiplicities_.

::::{prf:theorem}
:label: Thm:ComplexNumbers:uniquezeroes

Let $\{z_1,z_2,\ldots,z_k\}$ be the set of _distinct_ zeros of a polynomial $p$ of degree $n$ with $p(z)=a_n z^n + a_{n-1} z^{n-1} + \cdots + a_1 z + a_0$, that is, $z_j\neq z_k$ when $j\neq k$. Then the polynomial $p$ can be written as

$$
p(z)=a_n(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}\cdots(z-z_k)^{\alpha_k}
$$

where $\alpha_j,j=1,2,\ldots,k$ are positive integers and

$$
\sum_{j=1}^k\alpha_j=n.
$$

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:uniquezeroes`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:uniquezeroes` -->

Assume $\{z_1,z_2,\ldots,z_k\}$ is the set of _distinct_ zeros of a polynomial $p$ of degree $n$. Then following {prf:ref}`Thm:ComplexNumbers:fundamental`, we can write

:::{math}
:label: Eq:ComplexNumbers:factorsb

p(z) = a_n (z-b_1)(z-b_2) \cdots (z-b_n).

:::

for some complex numbers $b_1, b_2, \ldots, b_n$.

Because $p(z_1)=0$, we must have that some non-zero number of elements of the set $\{b_1, b_2, \ldots, b_n\}$ must equal $z_1$. Without loss of generality we may assume those are $b_1,\ldots,b_{\alpha_1}$. This is also means that Equation {eq}`Eq:ComplexNumbers:factorsb` transforms to

:::{math}
:label: Eq:ComplexNumbers:factorsb1

p(z) = a_n (z-z_1)^{\alpha_1}(z-b_{\alpha_1+1}) \cdots (z-b_n).

:::

We can repeat the above argument for $z_2$: we must have that some non-zero number of elements of the set $\{b_{\alpha_1+1}, \ldots, b_n\}$ must equal $z_2$. Without loss of generality we may assume those are $b_{\alpha_1+1},\ldots,b_{\alpha_1+\alpha_2}$. This is also means that Equation {eq}`Eq:ComplexNumbers:factorsb1` transforms to

:::{math}
:label: Eq:ComplexNumbers:factorsb2

p(z) = a_n (z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}(z-b_{\alpha_1+\alpha_2+1}) \cdots (z-b_n).

:::

We can directly repeat this argument for $z_3,\ldots,z_{k-1}$. For $z_k$, we have seen that the set $\{b_1,\ldots,b_{a\alpha_1+\alpha_2+\dots+\alpha_{k-1}}\}$ is equal to the set $\{z_1,...,z_{k-1}\}$, while the remaining roots $b_{\alpha_1+\alpha_2+\dots+\alpha_{k-1}+1},\ldots,b_n$ are unequal to $z_j$ for $1\leq j\leq k-1$. Necessarily, all of these $n-\alpha_1-\alpha_2-....-\alpha_{k-1}$ remaining roots must be equal to $z_k$. Hence, we find

$$
p(z)=a_n(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}\cdots(z-z_k)^{\alpha_k}
$$

where $\alpha_k=n-\alpha_1-\alpha_2-....-\alpha_{k-1}$. This also establishes

$$
\sum_{j=1}^k\alpha_j=n.
$$

::::

::::{prf:definition}
:label: Def:ComplexNumbers:multiplicity

If $z_j$ is a zero of a polynomial $p$ of degree $n$ with $p(z)=a_n(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}\cdots(z-z_k)^{\alpha_k}$, where $z_1,...,z_k$ are the distinct roots of $p$, $\alpha_j$ is called the **(algebraic) multiplicity** of $z_j$.

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polycomplcon2

The third degree polynomial $p(z) = z^3-4z^2$ can be factored as $p(z) = z^2(z-4) = (z-0)^2(z-4)$. Therefore, it has zeros $4$ and $0$, where the multiplicity of $4$ is equal to one and the multiplicity of $0$ is equal to two. The degree of the polynomial is $3$, which is equal to the sum of the multiplicities of its zeros ($1+2=3$).

::::

In {prf:ref}`Thm:ComplexNumbers:rootsquad` we saw that if a quadratic polynomial with real coefficients has non-real roots, these two roots are complex conjugates of each other. One might wonder whether it is always the case that both $z$ and its complex conjugate $\overline{z}$ are both roots of a given polynomial. It can be shown that this is the case if all coefficients are real valued.

::::{prf:theorem}
:label: Thm:ComplexNumbers:realpoly

Let $p$ be a polynomial with _real_ coefficients.
If $p(z_0)=0$, then $p(\overline{z_0})=0$ as well, and the algebraic multiplicities of $z_0$ and $\overline{z_0}$ are the same.

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:realpoly`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:realpoly` -->

Consider a polynomial $p$ of degree $n$, which we can write as 

$$
 p(z)=a_nz^n+a_{n-1}z^{n-1}+\cdots a_1z+a_0=\sum_{j=0}^na_jz^j,
$$

where the coefficients $a_n, a_{n-1}, \ldots, a_0$ are real numbers and $a_n\neq 0$. Let $z_0\in\mathbb{C}$ with $p(z_0)=0$.

First we show that $p(\overline{z_0})=0$. Note that

$$
\overline{p(z_0)} = \overline{0} = 0,
$$

but we also have

$$
\begin{align*}
\overline{p(z_0)} &= \overline{\sum_{j=0}^n a_j z_0^j} \\
&= \sum_{j=0}^n\overline{a_jz_0^j} \\
&= \sum_{j=0}^na_j\overline{z_0^j}\qquad (\text{since}\ a_j\in\mathbb{R}\ \text{for}\ 0\leq j\leq n) \\
&= \sum_{j=0}^na_j\overline{z_0}^j \\
&= p(\overline{z_0}).
\end{align*}
$$

Combining these two results gives the desired $p(\overline{z_0})=0$.

Now we focus on the algebraic multiplicity. If $z_0\in\mathbb{R}$, then $z_0$ and $\overline{z_0}$ are the same number, so they must have the same algebraic multiplicity. 

We now assume that $z_0\notin\mathbb{R}$, so that $\overline{z_0}\neq z_0$. {prf:ref}`Thm:ComplexNumbers:uniquezeroes` shows that we can write $p(z)$ as

$$
p(z)=a_n(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}\cdots(z-z_k)^{\alpha_k}
$$

where $\alpha_j,j=1,2,\ldots,k$ are positive integers that satisfy

$$
\sum_{j=1}^k\alpha_j=n
$$

and $z_1,z_2,\ldots,z_k$ are the unique zeros of $p$.

If $p(z_0)=0$, then $z_0=z_j$ for some $j\in\{1,2,\ldots,k\}$ and $z_0\neq z_l$ for $l\in\{1,2,\ldots,k\}\setminus\{j\}$. Without loss of generality we can assume $j=1$. Similarly, $\overline{z_0}=z_{\tilde{j}}$ for some $\tilde{j}\in\{2,\ldots,k\}$ and $\overline{z_0}\neq z_i$ for $i\in\{1,2,\ldots,k\}\setminus\{\tilde{j}\}$. Without loss of generality we can assume $\tilde{j}=2$.

We first note that

$$
 (z-z_1)(z-z_2)=(z-z_0)(z-\overline{z_0})=z^2-(z_0+\overline{z_0})z+z_0\overline{z_0}.
$$

According to {prf:ref}`Thm:ComplexNumbers:conjparts` and {prf:ref}`Thm:ComplexNumbers:ComplConjCompl`, $-(z_0+\overline{z_0})$ and $z_0\overline{z_0}$ are both real numbers, so $(z-z_1)(z-z_2)$ has real coefficients. According to {prf:ref}`Thm:RationalFunctions:PolynomialLongDivision`, we must have that

$$
 q(z)=\frac{p(z)}{(z-z_1)(z-z_2)}=a_n(z-z_1)^{\alpha_1-1}(z-z_2)^{\alpha_2-1}\cdots(z-z_k)^{\alpha_k}
$$

is a polynomial with real coefficients. If $\alpha_1-1>0$, we see that $q(z_0)=q(z_1)=0$. Since $q$ has real coefficients, we obtain from the first part of this proof that $q(\overline{z}_0)=q(z_2)=0$ as well. In particular, we must have $\alpha_2-1>0$. As such, we can divide $q$ by the polynomial $(z-z_1)(z-z_2)$ to obtain another polynomial with real coefficients. Continuing like this, we see that

$$
 r(z)=\frac{p(z)}{(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}}=a_n(z-z_2)^{\alpha_2-\alpha_1}\cdots(z-z_k)^{\alpha_k}
$$

is a polynomial with real coefficients. From this, we immediately obtain $\alpha_2-\alpha_1\geq 0$.

Suppose $z_0$ and $\overline{z}_0$ have different algebraic multiplicities. Then we must have $\alpha_2-\alpha_1>0$. Then we find that

$$
 r(z_2)=a_n(z_2-z_2)^{\alpha_2-\alpha_1}\cdots(z_2-z_k)^{\alpha_k}=0,
$$

which means that $\overline{z_0}=z_2$ is a root of the polynomial $r$. Since $r$ has real coefficients, we find that $\overline{\overline{z_0}}=z_0$ must be a root of $r$ as well by the first part of this proof. However, we have

$$
 r(z_0)=a_n(z_0-z_2)^{\alpha_2-\alpha_1}\cdots(z_0-z_k)^{\alpha_k}\neq 0
$$

since $z_0\neq z_l$ for $l\in\{2,...,k\}$. This gives a contradiction, so we must have $\alpha_1=\alpha_2$. As such, $z_0$ and $\overline{z_0}$ have the same algebraic multiplicity.




::::

::::{prf:example}
:label: Ex:ComplexNumbers:realpoly

Consider the fourth-degree polynomial 

$$
 p(z)=z^4-4z^3+14z^2-20z+25.
$$

Factoring this polynomial by hand is very hard, but not if we are given that $z_1=1+2i$ is a root of this polynomial with multiplicity $2$. Since the polynomial has real coefficients, $z_2=\overline{z_1}=1-2i$ must also be a root with multiplicity $2$ by {prf:ref}`Thm:ComplexNumbers:realpoly`. Since we have found two roots of the fourth-degree polynomial with multiplicity $2$, we must have found all roots and we can write

$$
 p(z)=(z-(1+2i))^2(z-(1-2i))^2.
$$

::::

::::{prf:example}
:label: Ex:ComplexNumbers:nonrealpoly

Consider the second-degree polynomial 

$$
 p(z)=z^2-3z+11-3i.
$$

If we are given that $z_1=1-3i$ is a root, it may be tempting to think that $\overline{z_1}=1+3i$ is a root as well, but this is not the case. Indeed, we note that

$$
 p(1+3i)=(1+3i)^2-3(1+3i)+11-3i=-6i\neq 0.
$$

So why doesn't this contradict {prf:ref}`Thm:ComplexNumbers:realpoly`? The reason is that this polynomial does not have real coefficients, which means that the theorem does not apply. 


Instead, we can complete the square to find that the other root is given by $z_2=2+3i$. In particular, we find

$$
 p(z)+(z-(1-3i))(z-(2+3i)).
$$
::::



### Polynomial Division

The fundamental theorem of Algebra says that if $p(z)$ is a polynomial such that $p(b)=0$ for some $b$, then $p(z) = a_n(z-b)(z-b_2)\cdots (z-b_n) = (z-b) q(z)$ for another polynomial $q(z)=a_n(z-b_2)\cdots  (z-b_n)$.
We can interpret this as dividing the polynomial $p(z)$ by $(z-b)$ to obtain a new polynomial. To find the zeros of $p$ we now just have to find the zeros of $q(z)$ and add $b$ to this list.

To find $q(z)=\dfrac{p(z)}{z-b}$ you can use a long division, see {numref}`Sec:LongDivision` for the notation we will use. Let us recall from {numref}`Section:RealNumbers` how this works for ordinary fractions.

:::{fetch} {prf:ref}`Ex:RealNumbers:longdivisionnum`
:::

We can do the same thing for polynomials. Details on long division for polynomials can be found in {numref}`Subsec:RationalFunctions:PolynomialDivision`. We illustrate the method with the following example.

:::::{prf:example}
:label: Ex:ComplexNumbers:longdivisionpoly

Consider $p(z) = z^3+3z^2+z-5$. We note that $z_1=1$ is a root, since we have 

$$
 p(1)=1^3+3\cdot 1^2+1-5=0.
$$

Therefore, $z-1$ must be a factor. If we calculate this division we obtain

$$
\class{longdivision}{
\begin{array}{rcl}
z^3 + 3z^2 + \phantom{4}z - 5 & / & {z-1} \\
\underline{\class{tud-red}{z^3 - \!\phantom{3}z^2}} \hspace0.45em\phantom{+ 4z - 0} & | & \ooline{\class{tud-cyan}{z^2}+\class{tud-green}{4z}+\class{tud-pink}{5}} \\
4z^2 + \phantom{4}z - 5 & | \\
\underline{\class{tud-blue}{4z^2 - 4z}} \hspace0.45em\phantom{-5} & | \\
5z-5 & | \\
\underline{\class{tud-orange}{5z-5}} & | \\
0 & |
\end{array}
}
$$

The calculations behind the long division are

\begin{align*}
\class{tud-cyan}{z^2} \cdot (z-1) &= \class{tud-red}{z^3 - z^2} \\
(z^3 + 3z^2 + z - 5) - (\class{tud-red}{z^3 - z^2}) &= 4z^2 + z - 5 \\
\class{tud-green}{4z} \cdot (z-1) &= \class{tud-blue}{4z^2 - 4z} \\
(4z^2 + z - 5) - (\class{tud-blue}{4z^2 - 4z}) &= 5z - 5 \\
\class{tud-pink}{5} \cdot (z-1) &= \class{tud-orange}{5z - 5} \\
(5z - 5) - (\class{tud-orange}{5z - 5}) &= 0
\end{align*}

Note that the remainder is zero, as we should have expected.

Here, we essentially calculate

$$
\frac{z^3+3z^2+z-5}{z-1} = z^2 + \frac{4z^2+z-5}{z-1} = z^2+4z+\frac{5z-5}{z-1} = z^2+4z+5.
$$

You can see this as follows.

- Because $z^3$ is a multiple of $z^3$ and $z$ is a multiple of $z$, we start with subtracting as many multiples of $\dfrac{z^3}{z}\cdot (z-1)=z^2\cdot (z-1)=z^3-z^2$ from $z^3+3z^2+z-5$ as possible so that the $z^3$ term is eliminated.

- Next, we subtract as many multiples of $\dfrac{z^2}{z}\cdot (z-1)=z\cdot (z-1)=z^2-z$ from the remainder $4z^2 + z - 5$ as possible so that the $z^2$ term is eliminated

- Finally, we subtract as many multiples of $\dfrac{z}{z}\cdot (z-1)=1\cdot (z-1)=z-1$ from the remainder $5z - 5$ as possible.

As a consequence, we see that $z^3+3z^2+z-5=(z-1)(z^2+4z+5)$, so it equals $0$ if either $z-1=0$ or $z^2+4z+5=0$.

Completing the square gives $z^2+4z+5=(z+2)^2+1$, so the zeros are $z=-2\pm i$. Thus, the roots of $z^3+3z^2+z-5$ are $z=1$ and $z=-2\pm i$.

:::::

## Grasple exercises

### Exercises on operations with complex numbers

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/adb8493e-88f8-462d-b069-f6192060f0a1?id=75397
:label: Grasple:75397
:dropdown:
:description: Real part of a complex number.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/95288a05-3c20-4a1e-b9c6-04de1a8af535?id=75398
:label: Grasple:75398
:dropdown:
:description: Imaginary part of a complex number.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2daad980-d96a-46ba-a3aa-ae18686532e2?id=75394
:label: Grasple:75394
:dropdown:
:description: Adding two complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c9dd1334-3902-43cb-ba40-5a31f1e8ca27?id=75395
:label: Grasple:75395
:dropdown:
:description: Subtracting two complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0a153784-60f8-4bc7-bc28-dea031bc3d22?id=75396
:label: Grasple:75396
:dropdown:
:description: Multiplying two complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0d7b1ba0-a763-4c49-a38c-4b3330f32ba9?id=75417
:label: Grasple:75417
:dropdown:
:description: Dividing two complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8ca4a847-bc4e-4227-ae2d-189ba1530451?id=75399
:label: Grasple:75399
:dropdown:
:description: Dividing two complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f9375305-f2ae-4a2e-93f7-6988923f488f?id=65961
:label: Grasple:65961
:dropdown:
:description: Complex conjugate of a complex number.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4fcf5b83-042c-4154-a85f-c2a857f9f363?id=75400
:label: Grasple:75400
:dropdown:
:description: Multiplying a complex number with it's complex conjugate.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f5b4d636-b98f-49e6-a706-5ab23ac4dd55?id=75416
:label: Grasple:75416
:dropdown:
:description: Complex conjugate of a quotient of complex numbers.

::::

### Exercises on solving equations

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/284d7804-e09e-429c-a595-397f58c19e3a?id=75401
:label: Grasple:75401
:dropdown:
:description: Linear equation of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a0af469e-5580-419f-83ff-cabc8ae8a75a?id=66105
:label: Grasple:66105
:dropdown:
:description: Completing the square with real coefficients.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ad1b8dc9-1909-4729-8cd1-d8b285b63602?id=65992
:label: Grasple:65992
:dropdown:
:description: Completing the square with real coefficients.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bf1837c9-59c1-4389-9e38-93f116000d34?id=66106
:label: Grasple:66106
:dropdown:
:description: Completing the square with complex coefficients.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f5426424-0d72-484c-a547-154ab867089a?id=66107
:label: Grasple:66107
:dropdown:
:description: Completing the square with complex coefficients.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e90df85b-35b4-4145-8a7d-fbb1d15d69d5?id=66006
:label: Grasple:66006
:dropdown:
:description: Completing the square with complex coefficients.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/eb0d0a6f-403a-4581-acf9-7ff821835695?id=122754
:label: Grasple:122754
:dropdown:
:description: Polynomial long division.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fd1ba3d4-3cc1-417e-9e0a-0d33b3f808ee?id=122756
:label: Grasple:122756
:dropdown:
:description: Polynomial long division.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d231f221-3d67-4360-b1c2-59432d6f1f61?id=68322
:label: Grasple:68322
:dropdown:
:description: Counting solutions of a polynomial equation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3737e7f3-2e03-4d0a-af25-a3ee4d809b1c?id=66004
:label: Grasple:66004
:dropdown:
:description: On the relation between roots of polynomials.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7594cf18-983a-4761-81f0-7245aa4bb314?id=68310
:label: Grasple:68310
:dropdown:
:description: Solving a cubic equation given a root.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d789c363-0f03-4190-a1cd-6471d01f9f74?id=66114
:label: Grasple:66114
:dropdown:
:description: Solving a cubic equation given a root.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f7d1e049-692a-4eb3-8c02-67f56c915c76?id=68311
:label: Grasple:68311
:dropdown:
:description: Solving a quartic equation given two roots.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4630b883-b306-44c8-86a9-8ab8d35f5036?id=68312
:label: Grasple:68312
:dropdown:
:description: Solving a quartic equation given one root.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cf88dffc-02f8-4ddc-8351-575379ba5713?id=71519
:label: Grasple:71519
:dropdown:
:description: Solving a quartic equation given one root.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a09d0b97-def4-4a8f-a133-86f1c7141b60?id=68314
:label: Grasple:68314
:dropdown:
:description: Solving a quartic equation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7a6cb0d1-6a30-451a-a8d2-213a4e7a0917?id=68313
:label: Grasple:68313
:dropdown:
:description: Solving a quartic equation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7c6c944c-937a-43f2-8b9f-ed99ddda3ab4?id=68323
:label: Grasple:68323
:dropdown:
:description: Finding the multiplicity of a root of a polynomial.

::::