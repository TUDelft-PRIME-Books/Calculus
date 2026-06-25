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

Now consider the case that you _really_ need solutions of Equation {eq}`Eq:ComplexNumbers:abc-eq` even if $D$ is negative. This might sound strange, but you will encounter this in many engineering applications, for example in solving second-order linear differential equations (see {numref}`Sec:ODE2:Homogeneous`). It turns out that the solution in Equation {eq}`Eq:ComplexNumbers:abc-sol` is still valid when $D<0$, which means that you need to take the square root of a negative number.

Fortunately, mathematicians have found a way to handle this, namely complex numbers. Before we start treating complex numbers, we first need to introduce the special number $i$. After that, we will introduce the complex numbers and show how we can do computations with them.

## Definition and arithmetics


We start with considering an easier form of Equation {eq}`Eq:ComplexNumbers:abc-eq`, namely

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

The **imaginary unit** $i$ is a mathematical constant that satisfies

$$
 i^2=-1.
$$


::::

:::{note}
Because of historical conventions we call $i$ imaginary, but that does not mean in the slightest that it is fictitious. There are many physical problems where the imaginary unit (and complex numbers in general) arise naturally.
:::

::::::{prf:notation}
In some fields, particularly in electrical engineering, the imaginary unit is sometimes denoted by $j$, to avoid confusion with the current which often uses the symbol $i$. In this book, we will stick to the symbol $i$.
::::::

Now we know what the imaginary unit is, we can define what a complex number is.

::::{prf:definition}
:label: Def:ComplexNumbers:complexnumber

A **complex number** is an expression of the form

$$
a+bi,
$$

where $a\in\mathbb{R}$ and $b\in\mathbb{R}$. The real number $a$ is known as the **real part** of $z$ and is denoted by

$$
\Re{z}=a,
$$

while the real number $b$ is known as the **imaginary part** of $z$ and is denoted by

$$
\Im{z}=b.
$$

The set of all complex numbers is denoted by the symbol $\mathbb{C}$, and is called the **complex plane**.

::::

::::::{warning}
It is a common error to think that the imaginary part of $z=a+bi$ would be $bi$. This is not correct; the imaginary part is $b$. Indeed, we have defined the imaginary part to be the number before the $i$, **excluding** the $i$.
::::::

:::{note}
$z$ is the symbol most commonly used to denote a complex number, followed by $w$. 
:::



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

Just like we can visualise real numbers on a number line, we can visualise complex numbers in the complex plane. One axis indicates the value of the real part of a complex number and one indicates the imaginary part of the same complex number. In {numref}`Figure %s <Fig:ComplexNumbers:complexplane>` you can see this visualisation. By convention, the horizontal axis always indicates the real part, and the vertical axis always represents the imaginary part.

:::{figure} Images/Fig-ComplexNumbers-complexplane.svg
:name: Fig:ComplexNumbers:complexplane
:class: dark-light

Visualisation of the complex plane $\mathbb{C}$.

:::

:::{todo}
Make {numref}`Fig:ComplexNumbers:complexplane` into an applet. The point should be draggable and/or you should be able to enter the point.
:::


To make everything concise, we will view the set of all real numbers $\mathbb{R}$ as a part of the complex numbers $\mathbb{C}$. By this we mean that if $x$ is a real number, we can interpret it as the complex number with $\Re{x}=x$ and $\Im{x}=0$. Conversely, if $z$ is a complex number with $\Im{z}=0$, we interpret it as a real number. If a complex number is not a real number, we refer to it as **non-real**.



The nice thing with real numbers is that you can you can add, subtract, multiply and, in most cases, divide real numbers to obtain other real numbers. With complex numbers we can do the same operations as with real numbers. This is precisely the reason why we call complex numbers 'numbers'. Addition, subtraction and multiplication are performed by simply working out the brackets.

::::{prf:definition} 
:label: Def:ComplexNumbers:Arithmetics
If $z=a+bi$ and $w=c+di$ are complex numbers (with $a,b,c,d\in\mathbb{R}$), then we define the sum $z+w$, the difference $z-w$ and the product $zw$ as the complex numbers

\begin{align*}
z+w &= (a+c)+(b+d)i, \\
z-w &= (a-c)+(b-d)i, \\
zw &= (ac-bd)+(ad+bc)i.
\end{align*}

::::

The standard computation rules that hold for real numbers, hold for complex numbers as well.

::::{prf:theorem} 
:label: Thm:ComplexNumbers:Commassdistr
Let $z_1$, $z_2$ and $z_3$ be complex numbers. Then we have

\begin{align*}
z_1-z_1&=0,&\\
z_1+z_2 &= z_2+z_1,\qquad&\operatorname{commutativity of addition} \\
(z_1+z_2)+z_3 &= z_1+(z_2+z_3),\qquad&\operatorname{associativity of addition} \\
z_1z_2 &= z_2z_1,\qquad&\operatorname{commutativity of multiplication}\\
(z_1z_2)z_3&=z_1(z_2z_3),\qquad&\operatorname{associativity of addition}\\
z_1(z_2+z_3)&=z_1z_2+z_1z_3.\qquad&\operatorname{distributivity}
\end{align*}

::::

:::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:roots`
:class: tudproof, dropdown
All of these rules follow by writing out both sides of the equation using the definition and using the corresponding property of real numbers. 

For instance, if we want to show associativity of multiplication,we write $z_1=a+bi$, $z_2=c+di$ and $z_3=x+yi$ with $a,b,c,d,x,y\in \mathbb{R}$. Then we have

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
:::

:::{note}
The rules from {prf:ref}`Thm:ComplexNumbers:Commassdistr` also show why it make sense to define addition and multiplication like we did. Indeed, if $z=a+bi$ and $w=c+di$ then we can work out the brackets to obtain

\begin{align*}
z+w&= (a+bi) + (c+di) \\
&= a + bi + c + di \\
&= a + c + bi + di \\
&= (a+c)+(b+d)i\\
\end{align*}

and

\begin{align*}
zw&=(a+bi)(c+di)\\
 &= a(c+di)+bi(c+di) \\
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

Now we consider the geometric interpretation of adding complex numbers. If we add $z=a+bi$ and $w=c+di$ the new number is $z+w=(a+c)+(b+d)i$, so we add the real and imaginary parts. This means we add the coordinates of the corresponding points. This works similar to the addition of vectors, see {numref}`Chapter:VectorAlgebra`. Thus, geometrically we can add two complex numbers by following the parallelogram rule. That is, the lines from the origin to the two complex numbers form two sides of a parallelogram with vertices $0$, $z$, $z+w$, and $w$; see {numref}`Figure %s <Fig:ComplexNumbers:complexadd>`.

:::{figure} Images/Fig-ComplexNumbers-complexadd.svg
:name: Fig:ComplexNumbers:complexadd
:class: dark-light

Adding complex numbers follows the parallelogram rule.

:::

:::{todo}
Turn {numref}`Fig:ComplexNumbers:complexadd` into an applet with draggable points.
:::

If we want to interpret the other operations such as multiplication easily, we first need another way of writing complex numbers, which we will study in {numref}`Ch:ComplexNumbersPolar`. 

Before we consider division of complex numbers we will turn our attention first to solving quadratic equations.

### Solving quadratic equations

Now that we know how addition and multiplication of complex numbers works, we can use complex numbers to solve quadratic equations, even those that do not have any real solutions.

::::{prf:theorem}
:label: Thm:ComplexNumbers:roots

Let $a$ be real number. Then the two complex numbers $x_-=-ai$ and $x_+=ai$ are solutions to the equation $x^2=-a^2$ and they are the only complex numbers that are solutions to this equation.

::::

:::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:roots`
:class: tudproof, dropdown

First we consider $x_-=-ai$ and take its square. This gives

$$
x_-^2 = \left(-ai\right)^2 = a^2i^2 = -a^2.
$$

This shows that $x_-=-ai$ is indeed a solution to the equation $x^2=-a^2$.

We repeat the same for $x_+=ai$ to obtain

$$
x_+^2 = \left(ai\right)^2 = a^2i^2 = -a^2.
$$

We also find that $x_+=ai$ is a solution to the equation $x^2=-a^2$.

Suppose $z=c+di$ also satisfies $z^2=-a^2$. Then we obtain

$$
 -a^2=z^2=(c+di)^2=(c+di)(c+di)=c^2-d^2+2cdi.
$$

Since two complex numbers are the same precisely when their real and imaginary parts are the same, we must have

$$
 -a^2=c^2-d^2,\qquad 0=2cd.
$$

The second equation gives either $c=0$ or $d=0$. If $d=0$, we obtain $-a^2=c^2$, which has no solutions if $a\neq 0$, while it has the solution $c=0$ if $a=0$. If $c=0$, we obtain $-a^2=-d^2$, which gives $d=\pm a$. In any case, we find that $z$ must be $x_-$ or $x_+$.

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

In general, you can use the technique of completing the square to write any polynomial $az^2+bz+c$ in the form $a ((z+p)^2+q)$ by first factoring out the $a$, subsequently choosing the $p$ such that the linear term (the term involving $z$) is correct, and letting $q$ be the remainder. Using this form, you can then determine the zeroes of the polynomial. As such, we obtain the following theorem.


::::{prf:theorem}
:label: Thm:ComplexNumbers:rootsquad

Let $a\neq 0$, $b$ and $c$ be real numbers and let $D=b^2-4ac$. Then the equation 

$$
 az^2+bz+c=0
$$

for $z\in\mathbb{C}$ has two real roots if $D>0$, it has a double real root if $D=0$, and it has two non-real roots if $D<0$.

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

This means that, in this case, the equation has two non-real roots.
:::


### Complex conjugates and division

Before we turn to division, we need to introduce one more arithmetic operation.

::::{prf:definition}
:label: Def:ComplexNumbers:conjugate

If $z=a+bi$ is a complex number (with $a,b\in\mathbb{R}$), the **complex conjugate** $\overline{z}$ is defined as

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
Suppose we want to find the complex conjugates of $z=4+3i$ and $w=-1-2i$. This simply means that we should change the sign of the imaginary part of each of the complex numbers, so we obtain

$$
 \overline{z}=4-3i,\qquad \overline{w}=-1-(-2)i=-1+2i.
$$

::::

Now we look at the geometric interpretation of complex conjugation. Recall that the complex conjugate $\bar z$ changes the sign of the imaginary part of the number $z$. That is $\overline{a+bi} = a-bi$. As the imaginary part of a complex number corresponds to the second coordinate of its representation in the complex plane, this implies that the number is reflected in the real axis (the horizontal axis). See {numref}`Figure %s <Fig:ComplexNumbers:complexconj>`.

:::{figure} Images/Fig-ComplexNumbers-complexconj.svg
:name: Fig:ComplexNumbers:complexconj
:class: dark-light

Complex conjugation reflects a number in the real axis.

:::

:::{todo}
Turn {numref}`Fig:ComplexNumbers:complexconj` into an applet. Probably draggable points are better, right?
:::

The following result is the reason why the complex conjugate can be used to simplify the quotient of two complex numbers.

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

Of the arithmetic operations, division is clearly the most complex. The reason for this is that there is no straightforward way to simplify a fraction when the denominator is a sum of two objects. And complex numbers just so happen to be the sum of two objects (the real part and $i$ times the imaginary part). We can circumvent this by multiplying the denominator and numerator by the same complex number in the hope that the resulting denominator is a single real number. {prf:ref}`Thm:ComplexNumbers:ComplConjCompl` tells us which number we should choose: the complex conjugate of the denominator. In general, we obtain the following result.

::::{prf:theorem}
:label: Thm:ComplexNumbers:division

Let $z=a+bi$ be a complex number (with $a,b\in\mathbb{R}$) with $z\neq 0$. Then there is a unique complex number, denoted by $\dfrac{1}{z}$, which satisfies $z\dfrac{1}{z}=1$.

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

::::

::::{prf:example}
:label: Ex:ComplexNumbers:Division


Suppose we want to divide $z=4+3i$ by $w=-1-2i$. Then we should multiply both parts of the fraction by $\overline{w}=-1+2i$. This gives

$$
\frac{z}{w}=\frac{4+3i}{-1-2i}=\frac{4+3i}{-1-2i}\frac{-1+2i}{-1+2i}=\frac{(4+3i)(-1+2i)}{(-1-2i)(-1+2i)}.
$$

We can now work out the brackets in both parts of the fraction to obtain

$$
\frac{z}{w}=\frac{(4+3i)(-1+2i)}{(-1-2i)(-1+2i)}=\frac{-10+5i}{5}.
$$

This fraction can be simplified directly and we obtain

$$
\frac{z}{w}=\frac{-10+5i}{5}=-2+i.
$$
::::




We can combine the complex conjugate with the other four operations, which gives the following theorem.

::::{prf:theorem}
:label: Thm:ComplexNumbers:conjops

If $z$ and $w$ are a complex numbers, then the following identities hold.

\begin{align*}
\overline{\overline{z}} &= z, \\
\overline{z+w} &= \overline{z}+\overline{w}, \\
\overline{z-w} &= \overline{z}-\overline{w}, \\
\overline{zw} &= \overline{z}\,\overline{w}, \\
\overline{\left(\frac{z}{w}\right)} &= \frac{\overline{z}}{\overline{w}}.\quad\text{(Assuming $w\neq0$.)}
\end{align*}

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:conjops`
:class: dropdown, tudproof 
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:conjops` -->

We show each of the identities, one after the other, where we assume $z=a+bi$ and $w=c+di$, $a,b,c,d\in\mathbb{R}$:

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

::::

Even better, we can relate the complex conjugate with the real and imaginary part of a complex number.

::::{prf:theorem}
:label: Thm:ComplexNumbers:conjparts

If $z$ is a complex number, then the following identities hold:

\begin{align*}
\frac{z+\overline{z}}{2} &= \Re{z}, \\
\frac{z-\overline{z}}{2i} &= \Im{z}, \\
z\overline{z} &= \Re{z}^2+\Im{z}^2.
\end{align*}

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:conjparts`
:class: dropdown, tudproof 
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:conjparts` -->

We show each of the identities, one after the other, where we assume $z=a+bi$, $a,b\in\mathbb{R}$:

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

_Conjugation and product_:

\begin{align*}
z\overline{z} &= (a+bi)(a-bi) \\
&= a^2-abi+abi-b^2i^2 \\
&= a^2+b^2 \\
&= \Re{z}^2+\Im{z}^2.
\end{align*}

::::

From the second identity in {prf:ref}`Thm:ComplexNumbers:conjparts` we can even deduce the next theorem.

::::{prf:theorem}
:label: Thm:ComplexNumbers:realz

Assume $z\in\mathbb{C}$. $z\in\mathbb{R}$ if and only if $z=\overline{z}$.

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:realz`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:realz` -->

Assume $z\in\mathbb{C}$.

If $z\in\mathbb{R}$, then $\Im{z}=0$. The second identity of {prf:ref}`Thm:ComplexNumbers:conjparts` then gives $\frac{z-\overline{z}}{2i}=0$, which gives in turn $z=\overline{z}$.

If $z\notin\mathbb{R}$, then $\Im{z}\neq0$. The second identity of {prf:ref}`Thm:ComplexNumbers:conjparts` then gives $\frac{z-\overline{z}}{2i}\neq0$, which gives in turn $z\neq\overline{z}$.

::::






(Sec:ComplexNumbers:SolvingEquations)=
## Solving equations

The reason for introducing complex numbers is to ensure that more equations have solutions, for example $z^2+1=0$. In this section, we consider equations involving complex numbers. This means that the solutions may be complex, but also that the coefficients in the equations can be complex.

We already solved quadratic equations using the technique called _completing the square_ and in this section you will learn more ways to solve equations.

We introduced complex numbers to give the equation $x^2+1 = 0$  a solution.  It appears that something much stronger holds, namely, that every polynomial equation with coefficients in $\mathbb{C}$, for instance  $(1+i)x^4 - 2x^2 + x = 10i$,  has solutions in $\mathbb{C}$. This is the content of the following theorem.

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

Observe that this factorisation means that $b_1, b_2, \ldots, b_n$ are the zeroes (= roots) of the polynomial $p(z)$. It might happen that the $b$'s are complex numbers, even if $a_1, a_2, \ldots, a_n$ are real.

We will not discuss the proof of this theorem, as that requires much more mathematics. However, we will illustrate the theorem using some examples.

::::{prf:example}
:label: Ex:ComplexNumbers:polyreal

Consider $p(z)=z^2+3z+2$. Then we know that we can factor the polynomial as $p(z) = (z+2)(z+1)$ and thus find the zeroes as $-2$ and $-1$.

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polycomplcon

Consider the equation $z^2=-1$. We can always rewrite an equation to an equation where one side is equal to zero by moving everything to one side. Thus this equation corresponds to $z^2+1=0$. We can now factor $z^2+1$ to $(z+i)(z-i)$ and thus find that $i$ and $-i$ are the two solutions to this equation.

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polycompl

While a polynomial of degree $n$ can be factored in $n$ linear terms, and we have $n$ values $b_i$, this does not mean that there are $n$ distinct zeroes. For example $p(z) = z^2+4z+4$ can be factored as $p(z)=(z+2)^2$ and thus only has $z=-2$ as a solution. However, the term $(z+2)$ occurs twice in the factorisation. We therefore say that the multiplicity of the zero $-2$ is equal to two.

::::

In particular, we see that any polynomial of degree $n$ has $n$ complex zeroes _counting multiplicity_.

::::{prf:theorem}
:label: Thm:ComplexNumbers:uniquezeroes

If $\{z_1,z_2,\ldots,z_k\}$ is the set of _unique_ zeroes of a polynomial $p$ of degree $n$ with $p(z)=a_n z^n + a_{n-1} z^{n-1} + \cdots + a_1 z + a_0$, the polynomial $p$ can be written as

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

Assume $\{z_1,z_2,\ldots,z_k\}$ is the set of _unique_ zeroes of a polynomial $p$ of degree $n$. Then following {prf:ref}`Thm:ComplexNumbers:fundamental`, we can write

:::{math}
:label: Eq:ComplexNumbers:factorsb

p(z) = a_n (z-b_1)(z-b_2) \cdots (z-b_n).

:::

for some complex numbers $b_1, b_2, \ldots, b_n$.

Because $p(z_1)=0$ for $j\in\{1,\ldots,k\}$, we must have that $\alpha_1\in\{1,\ldots,n\}$ numbers out of the set $\{b_1, b_2, \ldots, b_n\}$ must equal $z_1$. Without loss of generality we may assume those are $b_1,\ldots,b_{\alpha_1}$. This is also means that Equation {eq}`Eq:ComplexNumbers:factorsb` transforms to

:::{math}
:label: Eq:ComplexNumbers:factorsb1

p(z) = a_n (z-z_1)^{\alpha_1}(z-b_{\alpha_1+1}) \cdots (z-b_n).

:::

We can repeat the above argument for $z_2$: we must have that $\alpha_2\in\{1,\ldots,n-\alpha_1\}$ numbers out of the set $\{b_{\alpha_1+1}, \ldots, b_n\}$ must equal $z_2$. Without loss of generality we may assume those are $b_{\alpha_1+1},\ldots,b_{\alpha_1+\alpha_2}$. This is also means that Equation {eq}`Eq:ComplexNumbers:factorsb1` transforms to

:::{math}
:label: Eq:ComplexNumbers:factorsb2

p(z) = a_n (z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}(z-b_{\alpha_1+\alpha_2+1}) \cdots (z-b_n).

:::

Repeating this argument for $z_3,\ldots,z_k$ leads to desired formulae.

::::

::::{prf:definition}
:label: Def:ComplexNumbers:multiplicity

If $z_j$ is a zero of a polynomial $p$ of degree $n$ with $p(z)=a_n(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}\cdots(z-z_k)^{\alpha_k}$, where $z_1,...,z_k$ are the distinct roots of $p$, the **(algebraic) multiplicity** of $z_j$ is equal to $\alpha_j$.

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polycomplcon2

The third degree polynomial $p(z) = z^3-4z^2$ can be factored as $p(z) = z^2(z-4) = (z-0)^2(z-4)$. Therefore, it has zeroes $4$ and $0$, where the multiplicity of $4$ is equal to one and the multiplicity of $0$ is equal to two. The degree of the polynomial is $3$, which is equal to the sum of the multiplicities of its zeroes ($1+2=3$).

::::

{prf:ref}`Ex:ComplexNumbers:polycomplcon` showed that both $z=i$ and its complex conjugate $\overline{z}=-i$ where roots of the polynomial $p(z)=z^2+1$. One might wonder whether it is always the case that both $z$ and its complex conjugate $\overline{z}$ are both roots of a given polynomial. It can be shown that this is the case if all coefficients are real valued.

::::{prf:theorem}
:label: Thm:ComplexNumbers:realpoly

Let $p$ be a polynomial with _real_ coefficients.
If $p(z)=0$, then $p(\overline{z})=0$ as well, and the algebraic multiplicities of $z$ and $\overline{z}$ are the same.

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:realpoly`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:realpoly` -->

Consider a polynomial $p$ of degree $n$, $\sum_{j=0}^n a_j z^j$, where the coefficients $a_n, a_{n-1}, \ldots, a_0$ are real-valued numbers and $a_n\neq 0$.

First we show that $p(\overline{z})=0$ by writing $\overline{p(z)}$ in two different forms. First we have

$$
\overline{p(z)} = \overline{0} = 0,
$$

but we also have

$$
\begin{align*}
\overline{p(z)} &= \overline{\sum_{j=0}^n a_j z^j} \\
&= \sum_{j=0}^n\overline{a_jz^j} \\
&= \sum_{j=0}^na_j\overline{z^j} \\
&= \sum_{j=0}^na_j\overline{z}^j \\
&= p(\overline{z}).
\end{align*}
$$

Combining these two results gives the desired $p(\overline{z})=0$.

Now we focus on the algebraic multiplicity. {prf:ref}`Thm:ComplexNumbers:realpoly` shows that we can write $p(z)$ as

$$
p(z)=a_n(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}\cdots(z-z_k)^{\alpha_k}
$$

where $\alpha_j,j=1,2,\ldots,k$ are positive integers,

$$
\sum_{j=1}^k\alpha_j=n
$$

and $z_1,z_2,\ldots,z_k$ are the unique zeroes of $p$.

If $p(z)=0$, then $z=z_j$ for some $j\in\{1,2,\ldots,k\}$ and $z\neq z_i$ for $i\in\{1,2,\ldots,k\}\setminus\{j\}$. Without loss of generality we can assume $j=1$.

This means that also $(z-z_1)^{\alpha_1}=0$ and $(z- z_i)^{\alpha_i}\neq0$ for $i\in\{2,\ldots,k\}$, and even more that $\overline{(z-z_1)}^{\alpha_1}=0$ and $\overline{(z- z_i)}^{\alpha_i}\neq0$ for $i\in\{2,\ldots,k\}$.

From the last it even follows that $(\overline{z}-\overline{z_1})^{\alpha_1}=0$ and $(\overline{z}- \overline{z_i})^{\alpha_i}\neq0$ for $i\in\{2,\ldots,k\}$.

Using the previous results, we look at $p(\overline{z})$:
\begin{align*}
p(\overline{z}) &= \overline{p(z)} \\
&= \overline{a_n(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}\cdots(z-z_k)^{\alpha_k}} \\
&= a_n\overline{(z-z_1)^{\alpha_1}}\ \overline{(z-z_2)^{\alpha_2}}\cdots\overline{(z-z_k)^{\alpha_k}} \\
&= a_n\overline{(z-z_1)}^{\alpha_1}\ \overline{(z-z_2)}^{\alpha_2}\cdots\overline{(z-z_k)}^{\alpha_k} \\
&= a_n(\overline{z}-\overline{z_1})^{\alpha_1}\ (\overline{z}-\overline{z_2})^{\alpha_2}\cdots(\overline{z}-\overline{z_k})^{\alpha_k}.
\end{align*}

As all terms except the first term $(\overline{z}-\overline{z_1})^{\alpha_1}$ are non-zero, and the first term is zero, we find that $\overline{z}=\overline{z_1}$, $\alpha_1$ times. In other words, the algebraic multiplicity of $\overline{z}$ is $\alpha_1$.

::::

::::{prf:example}
:label: Ex:ComplexNumbers:realpoly

Consider the fourth degree polynomial 

$$
 p(z)=z^4-4z^3+14z^2-20z+25.
$$

Factoring this polynomial by hand is very hard, but suppose we are given that $z_1=1+2i$ is a root of this polynomial with multiplicity $2$. Since the polynomial has real coefficients, its complex conjugate $z_2=\overline{z_1}=1-2i$ must be a root with multiplicity $2$ as well by {prf:ref}`Thm:ComplexNumbers:realpoly`. Since we have found two roots of the fourth-degree polynomial with multiplicity $2$, we must have found all roots and we can write

$$
 p(z)=(z-(1+2i))^2(z-(1-2i))^2.
$$

::::

::::{prf:example}
:label: Ex:ComplexNumbers:nonrealpoly

Consider the degree polynomial 

$$
 p(z)=z^2-3z+11-3i.
$$

If we are given that $z_1=1-3i$ is a root, it may be very tempting to think that its complex conjugate $1+3i$ is a root as well, but this is not the case. Indeed, we note that

$$
 p(1+3i)=(1+3i)^2-3(1+3i)+11-3i=-6i\neq 0.
$$

So why doesn't this contradict {prf:ref}`Thm:ComplexNumbers:realpoly`? The reason is that this polynomial does not have real coefficients, which means that the theorem does not apply. Instead, we can complete the square to find that the other root is given by $z_2=2+3i$. In particular, we find

$$
 p(z)+(z-(1-3i))(z-(2+3i)).
$$
::::



### Polynomial Division

Next, we consider a method you can use whenever you know one root of a polynomial. The fundamental theorem of Algebra says that if $p(z)$ is a polynomial such that $p(b)=0$ for some $b$, then $p(z) = a_n(z-b)(z-b_2)\cdots (z-b_n) = (z-b) q(z)$ for another polynomial $q(z)=a_n(z-b_2)\cdots  (z-b_n)$.
Thus, we divide the polynomial $p(z)$ by $(z-b)$ in this case and obtain a new polynomial. To find the zeroes of $p$ we now just have to find the zeroes of the quotient $\nicefrac{p(z)}{z-b}$ and add $b$ to this list.

To divide a polynomial by another polynomial you can use a long division, see {numref}`Sec:LongDivision` for the notation we will use. Let us recall how this worked for ordinary fractions.

:::::{prf:example}
:label: Ex:ComplexNumbers:longdivisionnum

Let us calculate $\frac{97813}{382}$ using long division. To the right of the long division you can see the explanation of the steps, on the left you can see the actual long division.

::::{grid} 2 2 2 2

:::{grid-item}

$$
\class{longdivision}{
\begin{array}{rcl}
97813 & / & \uuline{382} \\
\underline{\class{tud-red}{764}}\phantom{00} & | & \class{tud-cyan}{2}\class{tud-green}{5}\class{tud-pink}{6}\\
2141\phantom{0} & | \\
\underline{\class{tud-blue}{1910}}\phantom{0} & | \\
2313 & | \\
\underline{\class{tud-orange}{2292}} & | \\
21 & | \\
\end{array}
}
$$

:::

:::{grid-item}
\begin{align*}
\class{tud-cyan}{2} \,\cdot\,\, \phantom{0}382 &= \phantom{0}\class{tud-red}{764} \\
978 - \phantom{0}\class{tud-red}{764} &= \phantom{0}214 \\
\class{tud-green}{5} \,\cdot\,\, \phantom{0}382 &= \class{tud-blue}{1910} \\
2141 - \phantom{0}\class{tud-blue}{1910} &= \phantom{0}231 \\
\class{tud-pink}{6} \,\cdot\,\, \phantom{0}382 &= \class{tud-orange}{2292} \\
2313 - \class{tud-orange}{2292} &= \phantom{0}\phantom{0}21 \\
\end{align*}
:::

::::

Here, the calculation behind the long division has been written down concisely:

$$
\frac{97813}{382} = 200 + \frac{21413}{382} = 250 + \frac{2313}{382} = 256 + \frac{21}{382}.
$$

You can see this as follows:

- Because $97813$ is a multiple of $10^4$ and $382$ is a multiple of $10^2$, we start with subtracting as many multiples of $\dfrac{10^4}{10^2}\cdot 382=100\cdot 382$ from $97813$ as possible, so that the remainder remains non-negative.

- Next, we subtract as many multiples of $\dfrac{10^3}{10^2}\cdot 382=10\cdot 382$ from the remainder $21413$ as possible, so that the remainder remains non-negative.

- Finally, we subtract as many multiples of $\dfrac{10^2}{10^2}\cdot 382=1\cdot 382$ from the remainder $2313$ as possible, so that the remainder remains non-negative.

:::::

We can do the same thing for polynomials. Details on long division for polynomials can be found in {numref}`Subsec:RationalFunctions:PolynomialDivision`. We illustrate the method with the following example.

:::::{prf:example}
:label: Ex:ComplexNumbers:longdivisionpoly

Consider $p(z) = z^3+3z^2+z-5$. You may notice that $z=1$ is a root, since we have 

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

The calculation behind the long division are

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

Completing the square gives $z^2+4z+5=(z+2)^2+1$, so the zeroes are $z=-2\pm i$. Thus, the roots of $z^3+3z^2+z-5$ are $z=1$ and $z=-2\pm i$.

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
:description: Linear equation of complex numbers

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