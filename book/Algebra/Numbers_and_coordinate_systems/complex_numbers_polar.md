(Ch:ComplexNumbersPolar)=
# Polar form of complex numbers

## Introduction

To consider the multiplication of complex numbers, it is best to first consider the polar coordinates of a complex number. Polar coordinates is a concept that works for points in a plane. The idea is that instead of looking at the $x$ and $y$ coordinates of a point, we describe the point by the distance to the origin and the direction from the origin.

## Modulus and argument

::::::{prf:definition}
Let $z$ be a complex number, The **modulus** of $z$, denoted by $|z|$, is the distance from zero to the point in the complex plane.

An **argument** of $z$, denoted by $\arg(z)$, is an angle in the complex plane measured from the positive real axis in counterclockwise direction towards the ray from $0$ through $z$.
::::::

By using the {prf:ref}`Pythagorean theorem <Thm:Trigonometry:Pythagoras>` and with $z=a+bi$, it holds that 

$$
 |z|=\sqrt{a^2+b^2}.
$$

By {prf:ref}`Thm:ComplexNumbers:ComplConjCompl` we can, equivalently, write

$$
 |z|=\sqrt{z\overline{z}}.
$$

We often denote the modulus by the symbol $r$, so $r=|z|$. 

The argument uses the convention similar to the unit circle: the direction straight the right corresponds to $0$ radians, up corresponds to $\frac{1}{2}\pi$ radians, to the left to $\pi$ radians and down to $\frac{3}{2}\pi$ radians. We often denote the argument by the symbol $\theta$, so $\theta=\arg(z)$.

:::{figure} Images/Fig-ComplexNumbers-modarg.svg
:name: Fig:ComplexNumbers:modarg
:class: dark-light

The polar coordinates of a point in the complex plane $\C$ are the distance $r=|z|$ from zero to the point and the angle $\theta=\arg(z)$ measured from the positive real axis in a anticlockwise direction towards the ray from zero through the point.

:::

:::{todo}
Turn {numref}`Fig:ComplexNumbers:modarg` into an applet.
:::

Notice that the argument is not uniquely defined, as you can always go a full circle extra and add $2\pi$ radians to the angle. For example, the number $1$ has argument $0$ (as it is on the positive real axis), but also $2\pi$, $4\pi$, and $-2\pi$ (etc.). In order to make a uniform choice, we sometimes work with the principal value of the argument, which is by definition the unique value of the argument between $-\pi$ and $\pi$.
We write the principal value using a capital A. Thus we have $-\pi < \mathrm{Arg}(z) \leq \pi$.

::::{prf:example}
:label: Ex:ComplexNumbers:polarex1

Suppose $z=3+3i$. We find by using the Pythagorean theorem that the modulus (the distance to the origin) equals 

$$
 |z|=\sqrt{3^2+3^2}=3\sqrt{2}.
$$

The argument, the corresponding angle, equals $\frac14\pi$ as you can see in {numref}`Figure %s <Fig:ComplexNumbers:polarex1>`.

:::{figure} Images/Fig-ComplexNumbers-polarex1.svg
:name: Fig:ComplexNumbers:polarex1
:class: dark-light

The complex number $3+3i$.

:::

:::{todo}
Turn {numref}`Fig:ComplexNumbers:polarex1` into an applet.
:::

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polarex2

Suppose $w=2+3i$. We can still use Pythagoras for the modulus and obtain 

$$
 |w|=\sqrt{2^2+3^2} = \sqrt{13}.
$$

The argument can't be deduced immediately from a picture, see {numref}`Figure %s <Fig:ComplexNumbers:polarex2>`, but we do see that

$$
\tan(\arg(w)) = \frac{\text{opposite}}{\text{adjacent}} = \frac{\text{imaginary part}}{\text{real part}} = \frac{3}{2}.
$$

Unfortunately, there are no 'pretty' angles of which the tangent is $\frac{3}{2}$. Since $\tan(1)\approx 1.557$, the argument of $w$ is going to be close to $1$. Either by making a good sketch (such as the one in {numref}`Fig:ComplexNumbers:polarex2`) and measuring the angle, or by simply trying some angles close to $1$, we find that an even better approximation would be $\arg(w)\approx 0.98$, since $\tan(0.98)\approx 1.49$.

In fact, if you are familiar with the arctangent, which we will cover in {numref}`Section:Inverse`, you can obtain the exact expression $\arg(w) = \arctan\left(\frac32\right) \approx 0.982794$.

:::{figure} Images/Fig-ComplexNumbers-polarex2.svg
:name: Fig:ComplexNumbers:polarex2
:class: dark-light

The complex number $2+3i$.
:::

:::{todo}
Turn {numref}`Fig:ComplexNumbers:polarex2` into an applet. Write $\arg(w)=\arctan(\frac{3}{2})\approx 0.98$ instead of $\arctan(\frac{3}{2})$.
:::

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polarex3

As a final example we consider $v=-1+2i$. Using Pythagoras theorem once again, we find that 

$$
 |v|=\sqrt{(-1)^2+2^2} = \sqrt{5}.
$$

For the argument, we obtain that, just as in the previous example, 

$$
 \tan(\arg(v)) = \frac{2}{-1}=-2.
$$

Again, there is no 'pretty' angle of which the tangent is $-2$. By making a good sketch (such as the one in {numref}`Figure %s <Fig:ComplexNumbers:polarex3>`) and measuring the angle, or by simply trying some angles, we find that an approximation would be $\arg(v)\approx 2.03$, since $\tan(2.03)\approx -2.02$.

If we were to use the arctangent (see {numref}`Section:Inverse`) to find an exact expression for the angle, we would expect that $\arg(v) = \arctan( -2) \approx -1.10715$. But this answer is negative, while we can see in {numref}`Figure %s <Fig:ComplexNumbers:polarex3>` that the true argument is something between $\frac12\pi$ and $\pi$. Thus, this argument cannot be correct. If we multiply both the real and imaginary parts of a complex number by $-1$, then the quotient stays the same. In this case the arctangent gives the argument of $1-2i$ instead. Fortunately, we can easily find the correct argument as it is exactly $\pi$ higher. We find $\arg(v) = \arctan(-2) + \pi \approx 2.03444$.

:::{figure} Images/Fig-ComplexNumbers-polarex3.svg
:name: Fig:ComplexNumbers:polarex3
:class: dark-light

The complex number $-1+2i$.

:::

:::{todo}
Turn {numref}`Fig:ComplexNumbers:polarex3` into an applet. Write $\arg(v)=\arctan(-2)+\pi\approx -2.03$ instead of $\arctan(-2)+\pi$.
:::

::::

:::{warning}
If $z=a+bi$ with $a\neq 0$ we have $\tan\left(\arg(z)\right)=\dfrac{b}{a}$. If you are familiar with the arctangent (see {numref}`Section:Inverse`), you can try to use this arctangent to obtain an exact expression for $\arg(z)$. However, you always have to check whether the value you find with the arctangent gives the correct angle. As the range of the arctangent is $\left(-\frac12\pi,\frac12\pi\right)$ you can only find the correct argument if the complex number is to the right of the imaginary axis, that is, if the real part is positive.

If the real part is negative, the argument is between $\frac12\pi$ and $\frac32\pi$ (or between $-\frac12\pi$ and $-\frac32\pi$ depending on which direction you want to consider) and outside the range of the arctangent. To get the correct value for the argument in these cases, you have to add or subtract $\pi$ from the arctangent. In particular, we have

$$
 \arg(z)\begin{cases}\arctan\left(\frac{b}{a}\right),&\operatorname{if}\ a>0,\\ \arctan\left(\frac{b}{a}\right)+\pi,&\operatorname{if}\ a<0.\end{cases}
$$


:::

Let us summarise the relations between the modulus and the argument on the one hand, and the real and imaginary part on the other hand.

::::::{prf:theorem}
:label: Thm:ComplexNumbers:ChangeCoor
Let $z$ be a complex number and write $z=a+bi$ and $r=|z|$ and $\theta=\arg(z)$. Then we have the following formulas for calculating $a$ and $b$ from $r$ and $\theta$:

$$
a=r\cos(\theta), \qquad b=r\sin(\theta).
$$

For calculating $r$ and $\theta$ from $a$ and $b$ we can use

$$
r= \sqrt{a^2+b^2}, \qquad \tan(\theta)=\frac{b}{a}.
$$



::::::

In particular, we see that the complex number with modulus $r$ and argument $\theta$ equals $r\bigl(\cos(\theta) + i\sin(\theta)\bigr)$ and vice versa. The form $r\cos(\theta) + ir\sin(\theta)$ is called the _polar form_ of the complex number:

::::{prf:definition}
:label: Def:ComplexNumbers:polarform

The **polar form** of a complex number $z=a+bi$ is defined as

$$
z = r\bigl(\cos(\theta)+i\sin(\theta)),
$$

where $r=|z|$ is the modulus of $z$ and $\theta=\arg(z)$ is an argument of $z$.

::::

::::{prf:example} {prf:ref}`Ex:ComplexNumbers:polarex1` continued
:label: Ex:ComplexNumbers:polarex1

For $z=3+3i$, we obtained that

$$
 |z|=\sqrt{3^2+3^2}=3\sqrt{2},\quad\arg(z)=\frac{\pi}{4}.
$$

This means that the polar form of $z$ is given by

$$
 z=3\sqrt{2}\left(\cos\left(\frac{\pi}{4}\right)+i\sin\left(\frac{\pi}{4}\right)\right).
$$

::::

## Geometric interpretation of multiplication

The polar form of a complex number can very conveniently be used to give a geometric interpretation of the multiplication of two complex numbers. First we investigate what the impact is of complex conjugation on the polar form. Suppose $z$ is the complex number with modulus $|z|=r$ and argument $\arg(z)=\theta$. Hence, we have $z=r\cos(\theta) + i r\sin(\theta)$ and $\overline{z}=r\cos(\theta) - i r\sin(\theta)$. This second equation we can rewrite into

:::{math}
:label: Eq:ComplexNumbers:calcconj

\begin{align*}
\overline{z} &= r\cos(\theta) - i r\sin(\theta) \\
&= r\cos(\theta) + i r\sin(-\theta) \\
&= r\cos(-\theta) + i r\sin(-\theta).
\end{align*}

:::

From the last line we see that conjugating a complex number means negating the argument of that complex number.

We can now see what happens to the product of two complex numbers. Suppose we have the complex number $z$ with modulus $|z|=r$ and argument $\arg(z)=\theta$, i.e. $z=r\cos(\theta) + i r\sin(\theta)$. The second complex number we consider is $w$ with modulus $|w|=s$ and argument $\arg(w) = \phi$, i.e. $w=s\cos(\phi) + i s \sin(\phi)$. We can then calculate the product using the addition formulas for cosine and sine ({prf:ref}`Thm:Trigonometry:AdditionSubtractionFormulas`). This gives

:::{math}
:label: Eq:ComplexNumbers:calcproduct

\begin{align*}
zw &= (r\cos(\theta) + i r \sin(\theta)) (s\cos(\phi) + is \sin(\phi))
\\&= rs \cos(\theta) \cos(\phi) + irs \cos(\theta) \sin(\phi) + irs \sin(\theta) \cos(\phi) + i^2 rs \sin(\theta) \sin(\phi)
\\&= rs( \cos(\theta) \cos(\phi) - \sin(\theta) \sin(\phi)) + irs (\cos(\theta) \sin(\phi) + \sin(\theta) \cos(\phi))
\\&= rs \cos(\theta + \phi) + irs \sin(\theta+\phi).
\end{align*}

:::

We recognize this product as the complex number with modulus $|zw|=rs$ and argument $\arg(zw) = \theta+\phi$. In particular we obtain the following theorem.

::::{prf:theorem}
:label: Thm:ComplexNumbers:polarmultdiv

If you take the complex conjugate of a complex number $z$, the modulus remains the same and the argument is negated:

<ul>
<li>

$|\overline{z}| = |z|$,

</li>

<li>

$\arg(\overline{z}) = -\arg(z)$.

</li>
</ul>

If you multiply two complex numbers $z$ and $w$, you multiply the moduli and add the arguments:

<ul>
<li>

$|zw| = |z| \cdot |w|$,

</li>

<li>

$\arg(zw) = \arg(z) + \arg(w)$.

</li>
</ul>

If you divide the complex number $z$ by the complex number $w\neq0$ you divide the modulus of $z$ by the modulus of $w$ and subtract the argument of $w$ from the argument of $z$:

<ul>
<li>

$\left|\frac{z}{w}\right| = \frac{|z|}{|w|}$,

</li>

<li>

$\arg\left(\frac{z}{w}\right) = \arg(z) - \arg(w)$.

</li>
</ul>

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:polarmultdiv`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:polarmultdiv` -->

_Proof for conjugation_

With $|z|=r$ and $\arg{z}=\theta$, Equation {eq}`Eq:ComplexNumbers:calcconj` shows that $|\overline{z}|=|z|$ and $\arg(\overline{z})=-\arg(z)$.

_Proof for multiplication_

With $|z|=r$, $|w|=s$, $\arg{z}=\theta$ and $\arg{w}=\phi$, Equation {eq}`Eq:ComplexNumbers:calcproduct` shows that $|zw| = |z| \cdot |w|$ and $\arg(zw) = \arg(z) + \arg(w)$.

_Proof for division_

For division (assuming $w\neq0$) we obtain

\begin{align*}
\frac{z}{w} &= \frac{z\overline{w}}{w\overline{w}} \\
&= \frac{rs\left(\cos(\theta-\phi)+i\sin(\theta-\phi)\right)}{s^2} \\
&= \frac{r}{s}\left(\cos(\theta-\phi)+i\sin(\theta-\phi)\right),
\end{align*}
where the last line shows that $\left|\frac{z}{w}\right| = \frac{|z|}{|w|}$ and $\arg\left(\frac{z}{w}\right) = \arg(z) - \arg(w)$.

::::

You can see each of these operations illustrated in {numref}`Figures %s <Fig:ComplexNumbers:conjugation>`, {numref}`%s <Fig:ComplexNumbers:multiplication>` and {numref}`%s <Fig:ComplexNumbers:division>`.

:::{figure} Images/Fig-ComplexNumbers-conjugation.svg
:name: Fig:ComplexNumbers:conjugation
:class: dark-light

Conjugating a complex number means negating the argument and keeping the modulus the same.

:::

:::{figure} Images/Fig-ComplexNumbers-multiplication.svg
:name: Fig:ComplexNumbers:multiplication
:class: dark-light

Multiplying complex numbers means adding the arguments and multiplying the moduli.

:::

:::{figure} Images/Fig-ComplexNumbers-division.svg
:name: Fig:ComplexNumbers:division
:class: dark-light

Dividig complex numbers means substracting the arguments and dividing the moduli.

:::

:::{todo}
Turn {numref}`Figures %s <Fig:ComplexNumbers:conjugation>`, {numref}`%s <Fig:ComplexNumbers:multiplication>` and {numref}`%s <Fig:ComplexNumbers:division>` into applets.
:::

## Euler's formula

Given that the polar coordinates of a complex number are so convenient and that the polar form $r\left(\cos(\theta) + i\sin(\theta)\right)$ is such a long expression to write down, we would like to have a simple way of representing the complex number with given modulus $r$ and argument $\theta$.

Therefore we introduce the following identity:

::::{prf:definition}
:label: Dfn:ComplexNumbers:EulersFormule

Let $\theta$ in $\mathbb{R}$. Then we introduce the symbol $e^{i\theta}$ as

$$
e^{i\theta} = \cos(\theta) + i\sin(\theta).
$$

This is known as **Euler's formula**.

::::

Using this definition we see that we can express any complex number in terms of an expression of the form $e^{i\theta}$.

::::{prf:theorem}
:label: Thm:ComplexNumbers:re

Let $z=a+bi$ with $a,b\in\mathbb{R}$ and define $r=|z|$ and $\theta=\arg{z}$. Then we have

$$
z = re^{i\theta}.
$$

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:re`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:re` -->

Using {prf:ref}`Thm:ComplexNumbers:ChangeCoor`, we can directly write

$$
z = a+bi = r\left(\cos(\theta)+i\sin(\theta)\right) = re^{i\theta}.
$$

::::



You might think it is strange to use the number $e$ and superscripts which would suggest some sort of power of $e$. It turns out this is very convenient as this expression satisfies the rules of calculation for exponentials. Indeed the calculation in Equation {eq}`Eq:ComplexNumbers:calcproduct` shows that

$$
(re^{i\theta}) (se^{i\phi} )= rse^{i(\theta+\phi)}.
$$

This corresponds precisely with the rules for multiplying exponentials. As such, you can calculate with this strange notation $re^{i\theta}$ for complex numbers just as you would if you were indeed taking imaginary powers of $e$ ($=2.71828\ldots$). Some deep mathematics show that the definition given here is the only reasonable way to define taking imaginary exponents. Hence, we call an expression of the form $e^{i\theta}$ a **complex exponential**.

In fact, we can use the idea that a complex exponential should satisfy the rules of calculation for the regular exponential to define the complex exponential for any complex number. Indeed, for a complex number $z=a+bi$ with $a,b\in\mathbb{R}$, we define the complex exponential $e^{a+bi}$ as

$$
 e^{a+bi}=e^ae^{bi}=e^a\left(\cos(b)+i\sin(b)\right).
$$

:::::::::{admonition} Bonus: derivative of the complex exponential
:class: bonus, dropdown

If you already know about functions, you can think of the expression $f(\theta)= e^{i\theta}$ as a complex-valued function. A complex-valued function $f$ can be written as $f=g+ih$, where $g$ and $h$ are real-valued functions. When $g$ and $h$ are differentiable, we can define the derivative of $f$ as 

$$
 f'=g+ih'.
$$

We can even show that the complex exponential function behaves exactly like the real exponential function in terms of its derivative.

::::{prf:theorem}
:label: Thm:ComplexNumbers:re_diff

Let $\theta\in\mathbb{R}$. Then

$$
\frac{d}{d\theta}\left(e^{i\theta}\right) = ie^{i\theta}.
$$

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:re_diff`
:class: dropdown, tudproof

The proof is again straight forward:

\begin{align*}
\frac{d}{d\theta}\left(e^{i\theta}\right) &= \frac{d}{d\theta}\left(\cos(\theta)+i\sin(\theta)\right) \\
&= \frac{d}{d\theta}\left(\cos(\theta)\right)+i\frac{d}{d\theta}\left(\sin(\theta)\right) \\
&= -\sin(\theta)+i\cos(\theta) \\
&= i^2\sin(\theta)+i\cos(\theta) \\
&= i\cos(\theta)+i^2\sin(\theta) \\
&= i\left(\cos(\theta)+i\sin(\theta)\right) \\
&= ie^{i\theta}.
\end{align*}

::::

:::::::::

In practice, the polar notation of complex numbers is convenient to use when you take products or powers, whereas the $a+bi$ notation is more convenient when you have to add complex numbers.

::::{prf:example}
:label: Ex:ComplexNumbers:highpower

Let us calculate $(1+i)^6$. As this is a high power of a complex number, we use Euler's formula for the polar form. First, we compute 

$$
 |1+i|=\sqrt{2},\qquad \arg(1+i)=\frac{\pi}{4},
$$

which allows us to write 

$$
 1+i=\sqrt{2} e^{i \frac{\pi}{4}}.
$$ 

Therefore, we have

$$
(1+i)^6 = (\sqrt{2} e^{i\frac{\pi}{4}})^6 = \sqrt{2}^6 e^{i6\frac{\pi}{4}} = 8 e^{i \frac{3\pi}{2}} = -8i.
$$

::::

::::{prf:example}
:label: Ex:ComplexNumbers:threesolutions

Let us calculate $\dfrac{(1-\sqrt{3}i)^3}{(2+2i)^6}$. We have 

$$
 \left|1-\sqrt{3}i\right|=2,\quad\arg\left(1-\sqrt{3}i\right)=-\frac{\pi}{3}
$$

and

$$
 \left|2+2i\right|=2\sqrt{2},\quad\arg\left(2+2i\right)=\frac{\pi}{4},
$$

so we can write

$$
 1-\sqrt{3}i=2e^{-i\frac{\pi}{3}},\qquad 2+2i=2\sqrt{2} e^{i\frac{\pi}{4}}.
$$

Then, we obtain

$$
\frac{(1-\sqrt{3}i)^3}{(2+2i)^6} = \frac{(2e^{-i\frac{\pi}{3}})^3}{(2\sqrt{2} e^{i\frac{\pi}{4}})^6}
= \frac{8e^{-\pi i}}{512 e^{i\frac{3\pi}{2}}} = \frac{1}{64} e^{-i\frac{5\pi}{2}} = -\frac{1}{64} i.
$$

::::

## De Moivre and other trigonometric identities

The notation invented by Euler of $e^{i\theta} = \cos(\theta) + i\sin(\theta)$ allows us to quickly derive trigonometric identities. The most famous one is De Moivre's identity $e^{in\theta} = (e^{i\theta})^n$, which seems obvious now, but was discovered by De Moivre decades before the exponential notation was introduced and is a lot more impressive in the form

$$
\cos(n\theta) + i \sin(n\theta) = \big(\cos(\theta) + i \sin(\theta)\big)^n.
$$

::::{prf:example}
:label: Ex:ComplexNumbers:DeMoivre

De Moivre's identity allows us to find an expression for $\cos(3\theta)$ in terms of $\cos(\theta)$ and $\sin(\theta)$. Indeed, expanding the right-hand side of the identity we have

\begin{align*}
\cos(3\theta) + i\sin(3\theta) &= \cos(\theta)^3 + 3i\cos(\theta)^2 \sin(\theta) + 3i^2 \cos(\theta) \sin(\theta)^2 + i^3 \sin(\theta)^3
\\&= \cos(\theta)^3 - 3\cos(\theta) \sin(\theta)^2 + i \big(3\cos(\theta)^2\sin(\theta) -\sin(\theta)^3\big).
\end{align*}

Comparing the real and imaginary parts on both sides of this equation we find

\begin{align*}
\cos(3\theta) &= \cos(\theta)^3-3\cos(\theta)\sin(\theta)^2, \\
\sin(3\theta) &= 3\cos(\theta)^2 \sin(\theta) - \sin(\theta)^3.
\end{align*}

::::

You can also derive other formulas.

::::{prf:example}
:label: Ex:ComplexNumbers:cos_sin_sum

Formulas for $\cos(\theta+\phi)$ and $\sin(\theta+\phi)$ are often used in calculus courses. These formulas can be derived using De Moivre's identity.

\begin{align*}
\cos(\theta+\phi) + i \sin(\theta +\phi) &= e^{i(\theta+ \phi)} \\
&= e^{i\theta} e^{i\phi} \\
&= \big(\cos(\theta) + i \sin(\theta)\big) \big(\cos(\phi) + i \sin(\phi)\big)
\\&= \cos(\theta) \cos(\phi) + i \cos(\theta) \sin(\phi) + i \sin(\theta) \cos(\phi) + i^2 \sin(\theta) \sin(\phi)
\\&=\cos(\theta) \cos(\phi) - \sin(\theta) \sin(\phi) + i \big(\sin(\theta) \cos(\phi) +\cos(\theta) \sin(\phi)\big)
\end{align*}

Thus $\cos(\theta+\phi) = \cos(\theta) \cos(\phi) - \sin(\theta) \sin(\phi)$ and $\sin(\theta +\phi)=\sin(\theta) \cos(\phi) +\cos(\theta) \sin(\phi)$.

::::

## Solving $z^n=w$

We can use complex exponential to solve equations of the form $z^n=w$ for a given complex number $w$, where $z$ is the variable we want to solve for. Let us consider an example.

::::{prf:example}
:label: Ex:ComplexNumbers:threesolutions2

Consider the equation $z^3=-16+16i$. We know it has $3$ complex solutions, as it is a third degree polynomial equation (see {prf:ref}`Thm:ComplexNumbers:fundamental`). If we write $z=a+bi$ and expand to find $a$ and $b$, we get a very large expression which is not easy to work with.

If we write $z=re^{i\phi}$ in polar coordinates instead, we can easily express $z^3=r^3e^{3i\phi}$. We also have to express the right-hand side in polar coordinates: $-16+16i=16\sqrt{2} e^{\frac34 \pi i}$. In particular, the equation in polar coordinates becomes

$$
 r^3e^{3i\phi}=16\sqrt{2} e^{\frac34 \pi i}.
$$

Comparing the modulus and argument of these two expressions, we find

\begin{align*}
r^3&=|z^3|= |-16+16i| = 16\sqrt{2},\\
3\phi &= \arg(z^3) = \arg(-16+16i) = \frac34\pi.
\end{align*}

Taking a cube root of the equation $r^3=16\sqrt{2}$, we find $r=2\sqrt{2}$. Note that $r\geq 0$ is real, so here we need to consider only the single positive real solution; we do not want to find the complex solutions.

In addition, we have $3\phi = \frac34\pi$, so $\phi = \frac14\pi$. This gives the solution $z=2\sqrt{2} e^{\frac14 \pi i}$. But this is just one solution and there ought to be two more by {prf:ref}`Thm:ComplexNumbers:fundamental`. So what are the remaining two?

As we have seen, the argument is only defined up to a multiple of $2\pi$. Thus, when we get the equation 

$$
 3\phi = \frac34\pi,
$$

we should actually write 

$$
 3\phi = \frac34\pi + 2\pi k
$$

for some integer $k$. Dividing this by $3$ gives 

$$
 \phi = \frac14\pi + \frac23 \pi k.
$$

We see that different values of $k$ give different values of $\phi$. For $k=0$, we obtain 

$$
 \phi=\frac14\pi
$$

as before. For $k=1$, we obtain 

$$
 \phi = \frac14\pi + \frac23\pi = \frac{11}{12}\pi.
$$

For $k=2$, we have 

$$
 \phi = \frac14\pi + \frac43\pi = \frac{19}{12}\pi.
$$

For $k=3$, we obtain 

$$
 \phi = \frac14\pi + 2\pi.
$$

This gives the same complex number as $\phi=\frac14\pi$, as the argument is shifted by one full period. Indeed, if we add a multiple of $3$ to $k$, the argument of $\phi$ is shifted by a multiple of $2\pi$ and thus the corresponding solution $z$ does not change. Therefore, only the cases $k=0$, $k=1$, and $k=2$ suffice to obtain all solutions.

The three solutions, $z_0$, $z_1$ and $z_2$, to the equation $z^3=-16+16i$ thus are

$$
\begin{array}{lllllllll}
z_0&=&2\sqrt{2} e^{\frac14\pi i} &=&  2\sqrt{2}\left( \cos\left(\frac14\pi\right) +  i\sin\left(\frac14\pi\right) \right) & = & 2+2i, \\
z_1&=& 2\sqrt{2} e^{\frac{11}{12}\pi i} &=& 2\sqrt{2} \left(\cos\left(\frac{11}{12}\pi\right) + i\sin\left(\frac{11}{12}\pi\right)\right) & = & (-1-\sqrt{3})+(-1+\sqrt{3})i, \\
z_2&=& 2\sqrt{2} e^{\frac{19}{12}\pi i} &=& 2\sqrt{2}\left(\cos\left(\frac{19}{12}\pi\right) +i\sin\left(\frac{19}{12}\pi\right)\right) &=& (-1+\sqrt{3})+(-1-\sqrt{3})i.
\end{array}
$$

You can find a visualisation of these three solutions in {numref}`Figure %s <Fig:ComplexNumbers:threesolfig>`.

```{applet}
:url: appendix/complex_numbers
:fig: Images/Fig-ComplexNumbers-threesolfig.svg
:name: Fig:ComplexNumbers:threesolfig
:status: approved
:class: dark-light

The three solutions from {prf:ref}`Ex:ComplexNumbers:threesolutions2`, as well as solutions for similar equation for higher powers of $z$.
```

::::

We can generalise the method for solving $z^n=w$ from the example above:

```{prf:algorithm} Solving $z^n=w$

<ol>
<li>

Write $z=re^{i\phi}$ (for unknown $r$ and $\phi$) and express the right-hand side $w$ in polar coordinates.

</li>
<li>

Obtain equations for the modulus $r$ and argument $\phi$ by equating the modulus and argument on both sides of this equation.

</li>
<li>

Solve for $r$ (you only need the single positive real solution).

</li>

<li>

Solve for $\phi$, remembering to add $+2\pi k$ first to the right-hand side.

</li>

<li>

You obtain all solutions to the equation by taking $n$ (the degree of the equation) subsequent values of $k$ in your expression of $\phi$.

</li>

<li>

Combine the solution for $r$ and the $n$ values for $\phi$ to obtain the $n$ solutions.

</li>

</ol>

```

## Adding trigonometric functions

Quite often, you come across expressions where a cosine and a sine of identical frequency are added. If you plot a function of the form $f(t)=b\cos(\omega t) + c\sin(\omega t)$, you notice that it becomes a new single wave. You can use complex numbers in a smart way to rewrite $f(t)$ to the form $A \cos(\omega t -\phi)$ as a single cosine with shifted argument. The variable $A$ gives the amplitude of the combined wave and the variable $\phi$ gives the phase-shift.

::::{prf:example}
:label: Ex:ComplexNumbers:sinusoid

Take $f(t) = \cos(2t) + \sqrt{3} \sin(2t)$. If you plot the graph of this function (see {numref}`Figure %s <Fig:ComplexNumbers:sinusoid>`), you notice it is a single wave.

Indeed, we have

\begin{align*}
f(t) &= \cos(2t) + \sqrt{3} \sin(2t) \\& = \Re{e^{2it}} + \Re{-i\sqrt{3} e^{2it}}
\\&= \Re{ e^{2it} -i\sqrt{3} e^{2it}} \\&= \Re{(1-i\sqrt{3}) e^{2it}}
\\&= \Re{ 2 e^{-\frac13 \pi i} e^{2it}} \\&= \Re{2 e^{i(2t-\frac13\pi)}} \\&= 2\cos\left(2t-\frac13 \pi\right).
\end{align*}

We first wrote both the cosine as the sine as real parts of complex exponentials. For the sine, we use that $-ie^{i\theta} = -i\cos(\theta) + \sin(\theta)$, so $\Re{-ie^{i\theta}} = \sin(\theta)$. Subsequently, we can take out the common factor $e^{2it}$; it is a common factor as the periods of both the cosine and sine are identical. Next, we rewrite $1-i\sqrt{3}$ in polar coordinates and work out what the result is.

:::{figure} Images/Fig-ComplexNumbers-sinusoid.svg
:name: Fig:ComplexNumbers:sinusoid
:class: dark-light

The graph of the sum of a cosine and a sine of identical period is a sinusoid as well.
:::

:::{todo}
Turn {numref}`Fig:ComplexNumbers:sinusoid` into an applet.
:::

::::

::::{prf:example}
:label: Ex:ComplexNumbers:cos_sin_shift

In the same way you can add two cosines (or sines) with shifted arguments.

\begin{align*}
\cos\left(t+\frac13\pi\right) + \cos\left(t-\frac13\pi\right) &= \Re{e^{i\left(t+\frac13\pi\right)}} + \Re{e^{i\left(t-\frac13\pi\right)}}
\\&= \Re{\left(e^{\frac13 \pi i} +e^{-\frac13\pi i}\right) e^{it}}
\\&= \Re{ \left( \left( \frac12+\frac12\sqrt{3} i\right) + \left(\frac12 -\frac12\sqrt{3}i\right)\right)e^{it}}
\\&= \Re{ e^{it}}\\&= \cos(t).  
\end{align*}

::::

## Derivations of Euler's formula

We used Euler's formula 

$$
 e^{i\theta}=\cos(\theta)+i\sin(\theta)
$$

as the definition of $e^{i\theta}$. There are several reasons why it is a logical choice to call this expression $e^{i\theta}$, all of which show that the complex exponential behaves similarly to the real exponential. Here, we consider two of of these reasons, both of which talk about concepts that will be defined later in this book.

**Using a scalar initial value problem**

To find Euler's formula, consider the initial value problem (see {numref}`Chapter:IntroDE`)

:::{math}
:label: Eq:ComplexNumbers:exp_de

\left\{\begin{array}{rcl}
\dfrac{dy}{d\theta} & = & iy,\\
y(0) & = & 1.
\end{array}\right.

:::

Because we assumed that $i$ behaves like any other number, we can solve this initial value problem, which leads to the solution

:::{math}
:label: Eq:ComplexNumbers:exp_sol

y(\theta) = e^{i\theta}.

:::

Now we have a solution, we put it aside and focus on another function $q$, which we define as

:::{math}
:label: Eq:ComplexNumbers:exp_sol_alt

q(\theta) = \cos(\theta)+i\sin(\theta).

:::

Let us calculate first the value of $q$ in $\theta=0$:

\begin{align*}
q(0) &= \cos(0)+i\sin(0) \\
&= 1-0i \\
&= 1.
\end{align*}

This indicates that $q$ satisfies the same initial condition from Equation {eq}`Eq:ComplexNumbers:exp_de` as the function $y$ from Equation {eq}`Eq:ComplexNumbers:exp_sol`. Could it also be that $q$ is a solution to the differential equation from Equation {eq}`Eq:ComplexNumbers:exp_de`? Let us investigate by looking at the first derivative of $q$:

\begin{align*}
\frac{dq}{d\theta} &= \frac{d}{d\theta}\Bigl[\cos(\theta)+i\sin(\theta)\Bigr] \\
&= -\sin(\theta)+i\cos(\theta) \\
&= i^2\sin(\theta)+i\cos(\theta) \\
&= i\bigr(i\sin(\theta)+\cos(\theta)\bigr) \\
&= i\bigr(\cos(\theta)+i\sin(\theta)\bigr) \\
&= iq(\theta).
\end{align*}

So we found that our function $q$ from Equation {eq}`Eq:ComplexNumbers:exp_sol_alt` is also a solution to initial value problem from Equation {eq}`Eq:ComplexNumbers:exp_de`.

But because this initial value problem can only have one unique solution, the function $q$ from Equation {eq}`Eq:ComplexNumbers:exp_sol_alt` must be the same function as the first solution $y$ in Equation {eq}`Eq:ComplexNumbers:exp_sol`. This means that we found Euler's formula:

$$
e^{i\theta} = \cos(\theta) + i\sin(\theta).
$$

**Using series**

Euler's formula can also be derived using series. You may already be familiar with the following three power series (see {numref}`Chapter:Series`)

\begin{align*}
e^x &= \sum_{n=0}^\infty\frac{x^n}{n!}, \\
\cos(x) &= \sum_{k=0}^\infty(-1)^k\frac{x^{2k}}{(2k)!}, \\
\sin(x) &= \sum_{l=0}^\infty(-1)^l\frac{x^{2l+1}}{(2l+1)!}.
\end{align*}

We can use these series to derive Euler's formula.

First consider the following $12$ powers of the complex number $\theta i$ with $\theta\in\mathbb{R}$:

\begin{align*}
(\theta i)^0 &= 1 & (\theta i)^4 &= \theta^4 & (\theta i)^8 &= \theta^8 \\
(\theta i)^1 &= \theta i & (\theta i)^5 &= \theta^5 i & (\theta i)^9 &= \theta^9 i \\
(\theta i)^2 &= -\theta^2 & (\theta i)^6 &= -\theta^6 & (\theta i)^{10} &= -\theta^{10}i \\
(\theta i)^3 &= -\theta^3 i & (\theta i)^7 &= -\theta^7 i & (\theta i)^{11} &= -\theta^{11}i \\
\end{align*}

Do you notice the pattern that _even_ powers give _real_ numbers and _odd_ powers give _complex_ numbers with zero real part? And also that for the list of even powers the sign flips each time? And the same for the odd powers?

Now let us consider $e^{\theta i}$ and expand the series of the exponential function using these patterns:

$$
\begin{align*}
e^{\theta i} &= \sum_{n=0}^\infty\frac{(\theta i)^n}{n!} & &\text{Using the series of $e^x$} \\
&= \sum_{\substack{n=0\\n~{\rm even}}}^\infty\frac{(\theta i)^n}{n!}+\sum_{\substack{n=0\\n~{\rm odd}}}^\infty\frac{(\theta i)^n}{n!} & &\text{Using the odd/even pattern seen above.} \\
&= \sum_{k=0}^\infty\frac{(\theta i)^{2k}}{(2k)!}+\sum_{l=0}^\infty\frac{(\theta i)^{2l+1}}{(2l+1)!} & &\text{Changing the indices using $n=2k$ and $n=2l+1$.} \\
&= \sum_{k=0}^\infty(-1)^{k}\frac{\theta^{2k}}{(2k)!}+\sum_{l=0}^\infty(-1)^l\frac{\theta^{2l+1}i}{(2l+1)!} & &\text{Using the alternating patterns seen above.} \\
&= \sum_{k=0}^\infty(-1)^{k}\frac{\theta^{2k}}{(2k)!}+i\sum_{l=0}^\infty(-1)^l\frac{\theta^{2l+1}}{(2l+1)!} & &\text{Taking $i$ out of the second series.} \\
&= \cos(\theta)+i\sin(\theta). & &\text{Using the series of $\cos(x)$ and $\sin(x)$.}
\end{align*}
$$

As you can see we have arrived at Euler's formula.

## Grasple exercises

### Switching between forms

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/39598c29-5794-403c-bb1b-710a1eef2940?id=64489
:label: Grasple:64489
:dropdown:
:description: From polar form to Cartesian form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/74a651ef-b1ca-493f-a322-73209db3b8d3?id=75402
:label: Grasple:75402
:dropdown:
:description: From polar form to Cartesian form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fe1f71f4-f24c-429b-b133-8f0c22552a61?id=75403
:label: Grasple:75403
:dropdown:
:description: From polar form to Cartesian form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9355ef66-3857-4962-903b-8b19a48861f7?id=64302
:label: Grasple:64302
:dropdown:
:description: From polar form to Cartesian form. Note: this question assumes a knowledge of (real) logarithms.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f19c76de-b7d6-4982-ba28-c1e1dc369ca2?id=64490
:label: Grasple:64490
:dropdown:
:description: From Cartesian form to polar form.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b3b63554-7f34-40e7-a171-ae1c6304ec26?id=68529
:label: Grasple:68529
:dropdown:
:description: From Cartesian form to polar form.

::::

### Arithmetics with the polar form.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7e24de61-8035-45ae-ab02-f10f77356548?id=75406
:label: Grasple:75406
:dropdown:
:description: Real and imaginary parts of polar form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0f03a208-8574-4d62-a224-4d1e5905db63?id=65976
:label: Grasple:65976
:dropdown:
:description: Real and imaginary parts of polar form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e7be5e2d-ac50-4ed6-b8e4-b8fbabc335c0?id=65991
:label: Grasple:65991
:dropdown:
:description: $\overline{z}$ in polar form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ba5fad60-c032-4076-b9ee-a14dad2f778e?id=75404
:label: Grasple:75404
:dropdown:
:description: $-z$ in polar form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/43e571e7-b948-4de8-9067-1f322166dfa8?id=75405
:label: Grasple:75405
:dropdown:
:description: $\frac{1}{z}$ in polar form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/634f8dfc-5ba3-48e0-9699-eb6c91d08bfb?id=65955
:label: Grasple:65955
:dropdown:
:description: Indicating three points in the complex plane.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/613cc600-8341-4e43-a00d-362ec19d8a72?id=71501
:label: Grasple:71501
:dropdown:
:description: Indicating three points in the complex plane.

::::

### Powers of complex numbers

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e4d5b5cc-07b0-4a72-aff1-91a5c617b73a?id=64320
:label: Grasple:75405
:dropdown:
:description: Powers of complex numbers

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/50b70591-2823-4f37-8416-b7d25e76e729?id=64336
:label: Grasple:64336
:dropdown:
:description: Powers of complex numbers

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bf12984b-1cf9-4b92-8a25-02c556194754?id=64337
:label: Grasple:64337
:dropdown:
:description: Powers of complex numbers

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ec9efcd8-cb51-45b9-b520-9ddbb1637f7d?id=68385
:label: Grasple:68385
:dropdown:
:description: Powers of complex numbers

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d5d0a636-177a-42e4-bdce-b8ab7bbfd5b3?id=68466
:label: Grasple:68466
:dropdown:
:description: Powers of complex numbers

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/93ae8521-9cf2-472b-9803-1b6e3ccbcee1?id=68467
:label: Grasple:68467
:dropdown:
:description: Powers of complex numbers

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/323cd6e4-29d2-40cd-8441-aab7c4d060bf?id=65978
:label: Grasple:65978
:dropdown:
:description: Multiplication of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2454beeb-5531-4fa7-893f-768a4f7cbebd?id=68469
:label: Grasple:68469
:dropdown:
:description: Multiplication of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b5a92d7b-abf6-4953-bfd1-d33a503617b4?id=68470
:label: Grasple:68470
:dropdown:
:description: Multiplication of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/078ced36-8705-484e-942c-942ca4c5e61e?id=68471
:label: Grasple:68471
:dropdown:
:description: Multiplication of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ba26c917-b32e-4a48-b653-b87c65071ac0?id=64323
:label: Grasple:64323
:dropdown:
:description: Division of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/65f6ad34-12a4-4ac5-b5cf-d83352d97179?id=64328
:label: Grasple:64328
:dropdown:
:description: Division of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/410c0d7b-1ac3-4700-a73e-89ceca2ae090?id=65964
:label: Grasple:65964
:dropdown:
:description: Division of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c2050eca-ad0a-4f07-8dd0-4c2b5a448e96?id=68472
:label: Grasple:68472
:dropdown:
:description: Division of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3b4052a5-96f4-4a73-bbe7-52cd82648bea?id=68473
:label: Grasple:68473
:dropdown:
:description: Division of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/79261de4-02a6-4e54-8a59-86edcb35f6c4?id=68474
:label: Grasple:68474
:dropdown:
:description: Division of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/80fb5b22-7704-44aa-8079-3be6583d047b?id=68475
:label: Grasple:68475
:dropdown:
:description: Division of powers of complex numbers.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ea0f9473-8735-4a5b-a366-022f8b1b96ec?id=64305
:label: Grasple:64305
:dropdown:
:description: Several manipulations of complex numbers in polar form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/88112a1a-65a8-4f0c-a803-ac7366e4288a?id=68532
:label: Grasple:68532
:dropdown:
:description: Using de Moivre's theorem.

::::

### Equations in the complex plane

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cc37cf9e-2d36-4684-b026-cbd155fbcb16?id=66094
:label: Grasple:66094
:dropdown:
:description: Equations in the complex plane.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fb70bccf-55b1-4094-bc05-097ce1d7667e?id=66007
:label: Grasple:66007
:dropdown:
:description: Equations in the complex plane.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ae68727e-7f7e-4f34-b97a-911b13bade6d?id=66096
:label: Grasple:66096
:dropdown:
:description: Equations in the complex plane.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a3ecb15d-b531-43d6-8831-087bcf7f16c2?id=65968
:label: Grasple:65968
:dropdown:
:description: Equations and inequalities in the complex plane.

::::



### Proving statements with complex numbers

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e92ddb17-1998-4bdc-a1d2-8ac1a89bfef3?id=68530
:label: Grasple:68530
:dropdown:
:description: Expressing trigonometric function in terms of complex exponentials.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7b35642e-b5fc-49eb-b5dc-c6a97ab46087?id=64295
:label: Grasple:64295
:dropdown:
:description: Proving three statements about the polar form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/83ac8f61-4120-429d-af9c-f63271b8427f?id=64298
:label: Grasple:64298
:dropdown:
:description: Proving three statements about the polar form.

::::

### Solving $z^n=w$


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1dff6977-41ec-407d-b334-9fdda04eba53?id=68320
:label: Grasple:68320
:dropdown:
:description: Square roots of a complex number.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ed3ab811-1e8c-4355-bc23-ab8e60681b45?id=71521
:label: Grasple:71521
:dropdown:
:description: Visualising cube roots of a complex number

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c3a3f892-0b78-47db-b5a2-0d57c399d893?id=68316
:label: Grasple:68316
:dropdown:
:description: Cubic roots of a complex number.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7363eaa1-d67a-4b16-a956-afcb0b3a184c?id=68315
:label: Grasple:68315
:dropdown:
:description: Cubic roots of a complex number.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/159060ea-2b4e-4d9d-a1bc-96b000cd0714?id=68317
:label: Grasple:68317
:dropdown:
:description: Fourth roots of a complex number.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/90784279-7cd1-46f0-8f22-b14078b5a3d7?id=65998
:label: Grasple:65998
:dropdown:
:description: A slightly different square root question.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ed4dfebb-908e-4a58-8c72-ffafd093a639?id=68321
:label: Grasple:68321
:dropdown:
:description: A slightly different square root question.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a0e8243a-9fde-464e-8f1e-fdb34c817013?id=68318
:label: Grasple:68318
:dropdown:
:description: A slightly different cubic root question.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9502b908-2018-4eb2-9bc5-988231292a7f?id=71504
:label: Grasple:71504
:dropdown:
:description: Adding and multiplying roots of unity.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ea9ebfd4-46b7-4a1e-896c-f040957fe683?id=71523
:label: Grasple:71523
:dropdown:
:description: Finding solutions to $e^z=w$. Note: this question assumes a knowledge of (real) logarithms.

::::

### Adding trigonometric functions

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5639d60a-2dee-425d-a50c-ee65f7b02880?id=70354
:label: Grasple:70354
:dropdown:
:description: Adding trigonometric functions.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8ac53b59-8db5-4776-8991-7cdf9b033da2?id=79436
:label: Grasple:79436
:dropdown:
:description: Adding trigonometric functions.

::::

### Applications

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3969255c-e2c4-4f2e-ad49-0340013e396e?id=65974
:label: Grasple:65974
:dropdown:
:description: Application: Complex wave function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1e2b0586-fa6e-47c6-ade6-da26072ae518?id=79435
:label: Grasple:79435
:dropdown:
:description: Application: Adding two voltages.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/684c0c67-60fc-436f-9e8e-3d4d7d031f97?id=64334
:label: Grasple:64334
:dropdown:
:description: Derivative of a complex exponential. Note: this question assumes a knowledge of differentiation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/310fc72e-0f50-4423-bedc-fd581af52b9e?id=65966
:label: Grasple:65966
:dropdown:
:description: Application: Waves and vibrations. Note: this question assumes a knowledge of differentiation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cb6f9262-11bb-4029-9775-ee625b0e7670?id=79413
:label: Grasple:79413
:dropdown:
:description: Application: Electrical circuits. Note: this question assumes a knowledge of integration.

::::