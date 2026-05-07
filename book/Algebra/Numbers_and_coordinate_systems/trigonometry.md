(Sec:Algebra:Trigonometry)=

# Trigonometry

## Introduction

In this section we will introduce some basic concepts of trigonometry. Trigonometry is the branch of mathematics that studies the relations between the angles and the lengths of the sides of triangles. It has many applications in science and engineering, such as in physics, computer graphics, signal processing and navigation.

## Angles

:::{prf:definition}
:label: Def:Trigonometry:AngleIntuitive

An **angle** is a measure for the amount of space between two half lines.

:::

Angles can be measured in degrees or in radians (abbreviated as $\operatorname{rad}$). The angle given by a complete revolution equals $360^{\circ}$, which is the same as $2\pi$ rad. Therefore:

$$\pi\;\operatorname{rad}=180^{\circ}\quad\Longrightarrow\quad 1\;\operatorname{rad}=\left(\dfrac{180}{\pi}\right)^{\circ}\quad\text{and}\quad 1^{\circ}=\dfrac{\pi}{180}\;\operatorname{rad}.$$ 

In calculus we use radians to measure angles except when otherwise indicated. Moreover, we leave out "$\operatorname{rad}$".

:::{note}
In geography and navigation a degree is divided into $60$ minutes and a minute into $60$ seconds.
This is called the DMS (Degrees, Minutes, Seconds) notation: 

$$
\text{dd}^{\circ}\text{mm}'\text{ss}''.
$$ 

For instance, the location of the statue of Hugo de Groot (or Hugo Grotius) in the centre of Delft in decimal GPS (Global Positioning System) coordinates is $52.01203^{\circ}$ (N) and $4.35982^{\circ}$ (E), which translates into $52^{\circ}00'43.308''$ (N) and $04^{\circ}21'35.352''$ (E) in DMS notation. 
:::

:::{admonition} Converting decimal degrees into DMS notation
:class: bonus, dropdown

Converting $52.01203^{\circ}$ we start with $52^{\circ}$. Then

$$
0.01203\times 60=0.7218\quad\longrightarrow\quad 00'
$$

and

$$
0.7218\times 60=43.308''.
$$

Converting $4.35982^{\circ}$ we start with $4^{\circ}$. Then

$$
0.35982\times 60=21.5892\quad\longrightarrow\quad 21'
$$

and

$$
0.5892\times 60=35.352''.
$$

:::

:::{note}
:name: Note:Trigonometry:HourAngles
In astronomy and celestial navigation also so-called *hour angles* are used. Then a $24$ hour angle corresponds to $360^{\circ}$ or $2\pi$, which implies that $1$ hour equals $15^{\circ}$ or $\frac{1}{12}\pi$.
:::

:::{todo}
Add a reference to the section on triple integrals in spherical coordinates. 
:::

:::{note}
:name: Note:Trigonometry:Gradians
In surveying, mining and geology angles are sometimes measured in *gradians* or *gons*. Then the angle given by a complete revolution equals $400^{g}$, which is the same as $2\pi$ rad. Therefore:

$$\pi\;\operatorname{rad}=200^{\operatorname{g}}\quad\Longrightarrow\quad 1\;\operatorname{rad}=\left(\dfrac{200}{\pi}\right)^{\operatorname{g}}\quad\text{and}\quad 1^{\operatorname{g}}=\dfrac{\pi}{200}\;\operatorname{rad}.$$ 

We will not use these *gradians* or *gons* in this book.
:::

::::::{prf:remark} Angle between two half lines
:label: Rem:Trigonometry:AngleBetweenTwoLines

An angle between two intersecting half lines is always in $[0,\pi]$. An angle of $\frac{1}{2}\pi$ is called a **right angle**. An angle between $0$ and $\frac{1}{2}\pi$ is called **acute** and an angle between $\frac{1}{2}\pi$ and $\pi$ is called **obtuse**. An angle of $\pi$ is called a **stretched angle**.

::::::

::::::{prf:definition}
:label: Def:Trigonometry:Angle

Angles are always measured from an **initial side** to a **terminal side**. The **vertex** of the angle is the common endpoint of the two sides.

The **standard position** of an angle occurs when we place its vertex at the origin of a coordinate system with two variables and its initial side on the positive horizontal axis.

A **positive angle** is obtained by rotating the initial side counterclockwise until it coincides with the terminal side. Likewise, **negative angle**s are obtained by clockwise rotation.

::::::

{numref}`Fig:Trigonometry:Trig` shows an angle $\theta$ in standard position within the $xy$-plane.

```{figure} Images/Fig-Trigonometry-Trig.png
---
width: 65%
name: Fig:Trigonometry:Trig
class: dark-light
---
An angle $\theta$ in the $xy$-plane in standard position.
```
:::{todo}
Convert {numref}`Fig:Trigonometry:Trig` into an applet.
:::

(Subsec:TrigonRatio)=
## Trigonometric ratios

Using angles, we define three trigonometric ratios: the sine, the cosine and the tangent.

We start with a right-angled triangle as shown in {numref}`Fig:Trigonometry:AcuteAngle`. Then for acute angles the trigonometric ratios can be described as ratios of the lengths of the sides of the triangle.

```{figure} Images/Fig-Trigonometry-AcuteAngle.png
---
width: 50%
name: Fig:Trigonometry:AcuteAngle
class: dark-light
---

The trigonometric ratios for an acute angle.
```
:::{todo}
Convert {numref}`Fig:Trigonometry:AcuteAngle` into an applet.
:::

::::::{prf:definition}
:label: Def:Trigonometry:TrigonometricRatiosTriangle

If the sides of a triangle are labelled "opp" for the opposite side and "adj" for the adjacent side of the angle $\theta$ (as shown in {numref}`Fig:Trigonometry:AcuteAngle`) and "hyp" for the hypotenuse of the triangle, then we have:

- $\sin(\theta)=\dfrac{\operatorname{opp}}{\operatorname{hyp}}$;

- $\cos(\theta)=\dfrac{\operatorname{adj}}{\operatorname{hyp}}$;

- $\tan(\theta)=\dfrac{\operatorname{opp}}{\operatorname{adj}}$.

::::::

For general angles this is generalised as follows.

::::::{prf:definition}
:label: Def:Trigonometry:TrigonometricRatios

For a general angle $\theta$ in standard position in the $xy$-plane we let $P(x,y)$ be any point on the terminal side of $\theta$ and we let $r>0$ be the distance between $O$ and $P$, see {numref}`Fig:Trigonometry:Trig`.

Then we define:

- The **sine** of $\theta$ as:
  
  $$
  \sin(\theta)=\dfrac{y}{r}.
  $$
- The **cosine** of $\theta$ as:
  
  $$
  \cos(\theta)=\dfrac{x}{r}.
  $$
- The **tangent** of $\theta$ as:
  
  $$
  \tan(\theta)=\dfrac{\sin(\theta)}{\cos(\theta)}=\dfrac{y}{x},
  $$

  provided that $x\neq0$.

::::::

If we take the point $P(x,y)$ on the **unit circle** (the circle with the origin as center and radius $r=1$, see {numref}`Fig:Trigonometry:UnitCircle`), we have $x=\cos(\theta)$ and $y=\sin(\theta)$.

```{figure} Images/Fig-Trigonometry-UnitCircle.png
---
width: 50%
name: Fig:Trigonometry:UnitCircle
class: dark-light
---
The unit circle.
```
:::{todo}
Convert {numref}`Fig:Trigonometry:UnitCircle` into an applet.
:::

The tangent is shown on the so-called *tangent axis*, the vertical line at $x=1$.

::::::{prf:remark} Additional trigonometric ratios
:label: Rem:Trigonometry:AlternativeTrigonometricRatios

Next to the three trigonometric ratios defined above, there are three more trigonometric ratios, which are defined as follows: 

- The **cosecant** of $\theta$ as:
  
  $$
  \csc(\theta)=\dfrac{r}{y}=\dfrac{1}{\sin(\theta)}.
  $$
- The **secant** of $\theta$ as:
  
  $$
  \sec(\theta)=\dfrac{r}{x}=\dfrac{1}{\cos(\theta)}.
  $$
- The **cotangent** of $\theta$ as:
  
  $$
  \cot(\theta)=\dfrac{\cos(\theta)}{\sin(\theta)}=\dfrac{x}{y},
  $$

  provided that $y\neq0$.

However, in this book we will not use these three trigonometric ratios.

::::::

All six trigonometric ratios can be displayed in one picture:

```{figure} Images/Fig-Trigonometry-TrigRatios.png
---
width: 50%
name: Fig:Trigonometry:TrigRatios
class: dark-light
---
The six trigonometric ratios.
```
:::{todo}
Convert {numref}`Fig:Trigonometry:TrigRatios` into an applet.

In the applet $\sin(\theta)$, $\cos(\theta)$, etc. should be used.
:::

Commonly powers of trigonometric ratios are used, such as $(\sin(\theta))^2$ and $(\cos(\theta))^3$. For brevity we will write these as $\sin^2(\theta)$ and $\cos^3(\theta)$, respectively, or more generally:

::::::{prf:notation} Powers of trigonometric ratios
:label: Not:Trigonometry:Powers

For any positive integer $n$ we use the following notation:

$$
\sin^n(\theta)=(\sin(\theta))^n;
$$

$$
\cos^n(\theta)=(\cos(\theta))^n;
$$

$$
\tan^n(\theta)=(\tan(\theta))^n.
$$
::::::

Before we proceed with properties of the sine, the cosine and the tangent we deal with two ancient theorems named after [Thales of Miletus (c. 624 - c. 545 BC)](https://en.wikipedia.org/wiki/Thales_of_Miletus) and [Pythagoras of Samos (c. 570 - c. 495 BC)](https://en.wikipedia.org/wiki/Pythagoras).

## Thales's theorem

Let $AB$ be any *diameter* of a circle with center $M$, id est, $A$ and $B$ lie on the circle and $M$ lies on the line segment from $A$ to $B$ as shown in {numref}`Fig:Trigonometry:Thales`. Let $C$ be an arbitrary point on the circle not equal to $A$ or $B$.

```{figure} Images/Fig-Trigonometry-Thales.png
---
width: 50%
name: Fig:Trigonometry:Thales
class: dark-light
---
An illustration for Thales's theorem.
```
:::{todo}
Convert {numref}`Fig:Trigonometry:Thales` into an applet.

Ideally, an image with a rotatable line segment $AB$ through the centre and a freely movable point $C$ on one side (the top) along the circle between $A$ and $B$.
:::

In {numref}`Fig:Trigonometry:Thales` you might notice that the angle $\angle ACB$ looks like a right angle. Thales's theorem states that this is indeed the case:

::::::{prf:theorem} Thales's theorem
:label: Thm:Trigonometry:Thales

If $AB$ is a diameter of a circle and $C$ is an arbitrary point on the circle, not equal to $A$ or $B$, then the angle $\angle ACB$ equals $\frac{1}{2}\pi$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Trigonometry:Thales`
:class: tudproof, dropdown

Consider the angles $\alpha$ and $\beta$ as indicated in {numref}`Fig:Trigonometry:Thales`. Since the triangle $\triangle AMC$ is isosceles ($AM$ and $MC$ are both equal to the radius of the circle), we have $\angle ACM=\alpha$. Likewise, the triangle $\triangle BMC$ is isosceles ($BM$ and $MC$ are both equal to the radius of the circle) and therefore $\angle BCM=\beta$. So, we have to prove that $\alpha+\beta$ equals $\frac{1}{2}\pi$.

Because the sum of all angles in a triangle equals $\pi$, we have in triangle $\triangle AMC$ that $\angle AMC=\pi-2\alpha$. Similarly, using triangle $\triangle BMC$ we find $\angle BMC=\pi-2\beta$. Further we have $\angle AMC+\angle BMC=\pi$. Hence

$$
\begin{align*}
&~ & \angle AMC+\angle BMC &= \pi \\
&\Longleftrightarrow & (\pi-2\alpha)+(\pi-2\beta) &= \pi \\
&\Longleftrightarrow & -2\alpha-2\beta &= -\pi \\
&\Longleftrightarrow & \alpha+\beta &= \tfrac{1}{2}\pi.
\end{align*}
$$

::::::

## The Pythagorean theorem

Another very important theorem in trigonometry is the Pythagorean theorem, which is about the relation between the lengths of the sides of a right-angled triangle, such shown in {numref}`Fig:Trigonometry:RightTriangle`.

```{figure} Images/Fig-Trigonometry-RightTriangle.png
---
width: 50%
name: Fig:Trigonometry:RightTriangle
class: dark-light
---

A right-angled triangle, with sides $a$, $b$ and $c$. The right angle is indicated by the small square. $a$ and $b$ are commonly referred to as the *legs* and $c$ as the *hypotenuse* of the triangle.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:RightTriangle` into an applet.
:::

::::::{prf:theorem} Pythagorean theorem
:label: Thm:Trigonometry:Pythagoras

In a right-angled triangle with legs $a$ and $b$ and hypotenuse $c$ we have:

$$
a^2+b^2=c^2.
$$

::::::

::::::{admonition} Proof of {prf:ref}`Thm:Trigonometry:Pythagoras`
:class: tudproof, dropdown

An elegant proof of the Pythagorean theorem is based on the following figure:

```{figure} Images/Fig-Trigonometry-PythagorasProof.png
---
width: 50%
name: Fig:Trigonometry:PythagorasProof
class: dark-light
---

A square within a larger square for the proof of the Pythagorean theorem.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:PythagorasProof` into an applet.
:::

The area of the large square is $(a+b)^2$ and that of the small square is $c^2$.

The area of each of the four triangles is $\frac{1}{2}ab$.

So we have:

$$
\begin{align*}
&~ & (a+b)^2 &= c^2+4\cdot\frac{1}{2}ab \\
&\Longleftrightarrow & a^2+2ab+b^2 &= c^2+2ab \\
&\Longleftrightarrow & a^2+b^2 &= c^2.
\end{align*}
$$

::::::

## The law of cosines

The *law of cosines* is a generalisation of the {prf:ref}`Pythagorean theorem <Thm:Trigonometry:Pythagoras>`, and regards arbitrary triangles as shown in {numref}`Fig:Trigonometry:LawOfCosines`.

```{figure} Images/Fig-Trigonometry-ABCTriangle.png
---
width: 50%
name: Fig:Trigonometry:LawOfCosines
class: dark-light
---

An arbitrary triangle $\triangle ABC$ with sides $a$, $b$ and $c$ opposite to angles $\alpha$, $\beta$ and $\gamma$, respectively.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:LawOfCosines` into an applet.
:::

::::::{prf:theorem} Law of cosines
:label: Thm:Trigonometry:LawOfCosines

In an arbitrary triangle with sides $a$, $b$ and $c$ opposite to angles $\alpha$, $\beta$ and $\gamma$, respectively we have (see {numref}`Fig:Trigonometry:LawOfCosines`):

$$
a^2=b^2+c^2-2bc\cos(\alpha).
$$

::::::

::::::{admonition} Proof of {prf:ref}`Thm:Trigonometry:LawOfCosines`
:class: tudproof, dropdown

Consider the perpendicular from $C$ to the opposite side $AB$, as shown in {numref}`Fig:Trigonometry:LawOfCosinesProof`.

```{figure} Images/Fig-Trigonometry-LawOfCosinesProof.png
---
width: 50%
name: Fig:Trigonometry:LawOfCosinesProof
class: dark-light
---

An illustration for the law of cosines.
``` 

:::{todo}
Convert {numref}`Fig:Trigonometry:LawOfCosinesProof` into an applet.
:::

Then we have according to the Pythagorean theorem:
$h^2=b^2-e^2$ and $h^2=a^2-(c-e)^2$. Hence

$$
b^2-e^2=a^2-c^2+2ce-e^2\quad\Longleftrightarrow\quad b^2=a^2-c^2+2ce.
$$

Now we have $\cos(\alpha)=\dfrac{e}{b}$, which implies that $e=b\cos(\alpha)$. So:

$$
a^2=b^2+c^2-2bc\cos(\alpha).
$$

::::::

::::::{prf:corollary} Law of cosines
:label: Cor:Trigonometry:LawOfCosinesVariants

Note that we also have 

$$
b^2=a^2+c^2-2ac\cos(\beta)
$$ 

and 

$$
c^2=a^2+b^2-2ab\cos(\gamma).
$$

Furthermore, if one of the angles is a right angle the law of cosines using that same angle reduces to the Pythagorean theorem.
::::::

## The law of sines

Further we have the *law of sines*, which relates the lengths of the sides of an arbitrary triangle and the sines of the opposite angles to the radius of the circumscribed circle, as shown in {numref}`Fig:Trigonometry:LawOfSines`.

```{figure} Images/Fig-Trigonometry-ABCTriangle-Circle.png
---
width: 50%
name: Fig:Trigonometry:LawOfSines
class: dark-light
---

An arbitrary triangle $\triangle ABC$ with sides $a$, $b$ and $c$ opposite to angles $\alpha$, $\beta$ and $\gamma$, respectively, and its circumscribed circle.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:LawOfSines` into an applet.
:::

::::::{prf:theorem} Law of sines
:label: Thm:Trigonometry:LawOfSines

In an arbitrary triangle as in {numref}`Fig:Trigonometry:LawOfSines` we have

$$
\frac{a}{\sin(\alpha)}=\frac{b}{\sin(\beta)}=\frac{c}{\sin(\gamma)}=2r
$$

with $r$ the radius of the circumscribed circle of the triangle.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Trigonometry:LawOfSines`
:class: tudproof, dropdown

Consider the perpendicular from $C$ to the opposite side $AB$, as shown in {numref}`Fig:Trigonometry:LawOfCosinesProof`.
 
Then we have $\sin(\alpha)=\dfrac{h}{b}$ and $\sin(\beta)=\dfrac{h}{a}$. Hence $b\sin(\alpha)=h=a\sin(\beta)$ or equivalently 

$$
\frac{a}{\sin(\alpha)}=\frac{b}{\sin(\beta)}.
$$

Similarly, drawing the perpendicular from $A$ to the opposite side $BC$, we also have

$$
\frac{b}{\sin(\beta)}=\frac{c}{\sin(\gamma)},
$$

and from $B$ to the opposite side $AC$ gives

$$
\frac{a}{\sin(\alpha)}=\frac{c}{\sin(\gamma)}.
$$

So, we conclude that

$$
\frac{a}{\sin(\alpha)}=\frac{b}{\sin(\beta)}=\frac{c}{\sin(\gamma)}.
$$

Now we consider the circumscribed circle of the triangle as shown in {numref}`Fig:Trigonometry:LawOfSinesProof`.

```{figure} Images/Fig-Trigonometry-LawOfSinesProof.png
---
width: 50%
name: Fig:Trigonometry:LawOfSinesProof
class: dark-light
---

An illustration for the proof of the law of sines.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:LawOfSinesProof` into an applet.
:::

Consider the line segment $AD$ through the center $M$ of the circumscribed circle of the triangle. According to {prf:ref}`Thales's theorem <Thm:Trigonometry:Thales>` the triangle $\triangle ABD$ then is a right-angled triangle. Since $C$ and $D$ are two points on the same circle, which are connected to the same chord $AB$, we have $\gamma=\delta$. Then we have

$$
\sin(\gamma)=\sin(\delta)=\frac{c}{2r}\quad\Longleftrightarrow\quad\frac{c}{\sin(\gamma)}=2r.
$$

This proves the theorem.
::::::

## Standard values

For certain special angles the trigonometric ratios can be evaluated exactly.

First consider a right-angled isosceles triangle with two equal sides of length $1$, as shown in {numref}`Fig:Trigonometry:IsoscelesTriangle`. Then the {prf:ref}`Pythagorean theorem <Thm:Trigonometry:Pythagoras>` implies that the hypotenuse has length $\sqrt{2}$. The two equal angles are $\frac{1}{4}\pi$, which implies that $\cos(\frac{1}{4}\pi)=\frac{1}{2}\sqrt{2}=\sin(\frac{1}{4}\pi)$.

```{figure} Images/Fig-Trigonometry-IsoscelesTriangle.png
---
width: 25%
name: Fig:Trigonometry:IsoscelesTriangle
class: dark-light
---

A right-angled isosceles triangle with equal sides of length $1$.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:IsoscelesTriangle` into an applet.
:::

Secondly, consider an equilateral triangle with three equal sides of length $2$, as shown in {numref}`Fig:Trigonometry:EquilateralTriangle`. Then the line segment from the top perpendicular to the opposite side leads to two right-angled triangles with one side of length $1$ and hypotenuse of length $2$. Then the {prf:ref}`Pythagorean theorem <Thm:Trigonometry:Pythagoras>` implies that the vertical line segment has length $\sqrt{3}$. Note that the three equal angles are $\frac{1}{3}\pi$ and that the angle at the top of each of the two right-angled triangles is $\frac{1}{6}\pi$. Then we easily deduce that $\cos(\frac{1}{3}\pi)=\frac{1}{2}=\sin(\frac{1}{6}\pi)$ and $\cos(\frac{1}{6}\pi)=\frac{1}{2}\sqrt{3}=\sin(\frac{1}{3}\pi)$.

```{figure} Images/Fig-Trigonometry-EquilateralTriangle.png
---
width: 25%
name: Fig:Trigonometry:EquilateralTriangle
class: dark-light
---

An equilateral triangle with three equal sides of length $2$.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:EquilateralTriangle` into an applet.
:::

This leads to the following table of standard values:


```{list-table} Standard values of sine, cosine and tangent.
:name: Tab:Trigonometry:StandardValues
:header-rows: 2
:align: center
:class: mid-align center-align

* - $\theta$ (in radians)
  - $0$
  - $\frac{1}{6}\pi$
  - $\frac{1}{4}\pi$
  - $\frac{1}{3}\pi$
  - $\frac{1}{2}\pi$
  - $\frac{2}{3}\pi$
  - $\frac{3}{4}\pi$
  - $\frac{5}{6}\pi$
  - $\pi$
  - $\frac{3}{2}\pi$
  - $2\pi$
* - $\theta$ (in degrees)
  - $0^{\circ}$
  - $30^{\circ}$
  - $45^{\circ}$
  - $60^{\circ}$
  - $90^{\circ}$
  - $120^{\circ}$
  - $135^{\circ}$
  - $150^{\circ}$
  - $180^{\circ}$
  - $270^{\circ}$
  - $360^{\circ}$
* - $\sin(\theta)$
  - $0$
  - $\frac{1}{2}$
  - $\frac{\sqrt{2}}{2}$
  - $\frac{\sqrt{3}}{2}$
  - $1$
  - $\frac{\sqrt{3}}{2}$
  - $\frac{\sqrt{2}}{2}$
  - $\frac{1}{2}$
  - $0$
  - $-1$
  - $0$
* - $\cos(\theta)$
  - $1$
  - $\frac{\sqrt{3}}{2}$
  - $\frac{\sqrt{2}}{2}$
  - $\frac{1}{2}$
  - $0$
  - $-\frac{1}{2}$
  - $-\frac{\sqrt{2}}{2}$
  - $-\frac{\sqrt{3}}{2}$
  - $-1$
  - $0$
  - $1$
* - $\tan(\theta)$
  - $0$
  - $\frac{\sqrt{3}}{3}$
  - $1$
  - $\sqrt{3}$
  - 
  - $-\sqrt{3}$
  - $-1$
  - $-\frac{\sqrt{3}}{3}$
  - $0$
  - 
  - $0$
```

Note that $\tan(\frac{1}{2}\pi)$ and $\tan(\frac{3}{2}\pi)$ are not defined since $\cos(\frac{1}{2}\pi)=0$ and $\cos(\frac{3}{2}\pi)=0$. We also omitted in this table the angles within the third and fourth quadrant, since their sine, cosine and tangent values can be derived from the above values using the identities listed in the next section.

These standard values can also be visualised using the unit circle, as shown in {numref}`Fig:Trigonometry:UnitCircleStandardValues`.

```{figure} https://study.com/cimages/multimages/16/unit_circle3684925022841182452.png
---
width: 50%
name: Fig:Trigonometry:UnitCircleStandardValues
class: dark-light
---

The unit circle with standard angles marked.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:UnitCircleStandardValues` into an applet.
:::

:::{note}
It is important to memorise these standard values. It might be helpful to note that

```{list-table} Standard values of sine and cosine for angles in the first quadrant.
:header-rows: 2
:align: center
:class: mid-align center-align

* - $\theta$ (in radians)
  - $0$
  - $\frac{1}{6}\pi$
  - $\frac{1}{4}\pi$
  - $\frac{1}{3}\pi$
  - $\frac{1}{2}\pi$
* - $\theta$ (in degrees)
  - $0^{\circ}$
  - $30^{\circ}$
  - $45^{\circ}$
  - $60^{\circ}$
  - $90^{\circ}$
* - $\sin(\theta)$
  - $\frac{\sqrt{0}}{2}$
  - $\frac{\sqrt{1}}{2}$
  - $\frac{\sqrt{2}}{2}$
  - $\frac{\sqrt{3}}{2}$
  - $\frac{\sqrt{4}}{2}$
* - $\cos(\theta)$
  - $\frac{\sqrt{4}}{2}$
  - $\frac{\sqrt{3}}{2}$
  - $\frac{\sqrt{2}}{2}$
  - $\frac{\sqrt{1}}{2}$
  - $\frac{\sqrt{0}}{2}$
```

The other standard values can be deduced from these.
:::

## Trigonometric identities

Now we have the basics, we can proceed with some important identities involving the sine, the cosine and the tangent.

::::{prf:theorem} Pythagorean identity
:label: Thm:Trigonometry:UnitCircleIdentity

For any angle $\theta$ we have

$$
\sin^2(\theta)+\cos^2(\theta)=1.
$$

::::

::::::{admonition} Proof of {prf:ref}`Thm:Trigonometry:UnitCircleIdentity`
:class: tudproof, dropdown

Using {numref}`Fig:Trigonometry:UnitCircle` and the {prf:ref}`Pythagorean theorem <Thm:Trigonometry:Pythagoras>` with $a=x=\cos(\theta)$ and $b=y=\sin(\theta)$ and $c=1$ we have:

\begin{align*}
\sin^2(\theta)+\cos^2(\theta) &= y^2+x^2 \\
&= x^2 +y^2 \\
&= a^2+b^2 \\
& = c^2 \\
& = 1.
\end{align*}
::::::

::::::{prf:theorem} Periodicity
:label: Thm:Trigonometry:Periodicity

For any angle $\theta$ we have

::::{math}
:label: Eq:Trigonometry:SinePeriodicity

\sin(\theta+2\pi)=\sin(\theta),
::::

::::{math}
:label: Eq:Trigonometry:CosinePeriodicity

\cos(\theta+2\pi)=\cos(\theta),
::::

and

::::{math}
:label: Eq:Trigonometry:TangentPeriodicity

\tan(\theta+\pi)=\tan(\theta).
::::

::::::

::::::{admonition} Proof of {prf:ref}`Thm:Trigonometry:Periodicity`
:class: tudproof, dropdown

Consider the point $P$ in {numref}`Fig:Trigonometry:UnitCircle`. Rotating the point $P$ by $2\pi$ leads to the same point $P$. Hence the sine and cosine values do not change, by {prf:ref}`Def:Trigonometry:Angle`.

Finally, rotating the point $P$ by $\pi$ leads to the point $R$, which has coordinates $(-x,-y)$. Hence we have $\tan(\theta+\pi)=\dfrac{-y}{-x}=\dfrac{y}{x}=\tan(\theta)$.

::::::

::::::{prf:definition} Periodicity
:label: Def:Trigonometry:Period

The value $2\pi$ in Equations {eq}`Eq:Trigonometry:SinePeriodicity` and {eq}`Eq:Trigonometry:CosinePeriodicity` is called the **period** of the sine and the cosine. This means that the sine and the cosine repeat their values every $2\pi$.

The value $\pi$ in Equation {eq}`Eq:Trigonometry:TangentPeriodicity` is called the **period** of the tangent. This means that the tangent repeats its values every $\pi$.

::::::

::::::{prf:theorem} Negative angles
:label: Thm:Trigonometry:NegativeAngles

For any angle $\theta$ we have

$$
\sin(-\theta)=-\sin(\theta),
$$

$$
\cos(-\theta)=\cos(\theta),
$$

and

$$
\tan(-\theta)=-\tan(\theta).
$$

::::

::::::

::::::{admonition} Proof of {prf:ref}`Thm:Trigonometry:NegativeAngles`
:class: tudproof, dropdown

```{figure} Images/Fig-Trigonometry-NegativeAnglesProof.png
---
width: 50%
name: Fig:Trigonometry:NegativeAnglesProof
class: dark-light
---

An illustration for the proof of the negative angles identities.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:NegativeAnglesProof` into an applet.
:::

Consider mirroring the point $P$ in {numref}`Fig:Trigonometry:NegativeAnglesProof` across the $x$-axis to obtain the point $Q$. Then the $x$-coordinate of $Q$ equals the $x$-coordinate of $P$, while the $y$-coordinate of $Q$ equals the negative of the $y$-coordinate of $P$. As a result of the mirroring, the angle has become $-\theta$. So we find 

$$
\sin(-\theta) = -\sin(\theta)\quad\text{and}\quad\cos(-\theta) = \cos(\theta).
$$

For the tangent function we have 

$$
\tan(-\theta)=\dfrac{\sin(-\theta)}{\cos(-\theta)}=\dfrac{-\sin(\theta)}{\cos(\theta)}=-\tan(\theta).
$$

::::::

Two angles are called **complementary** if their sum is equal to $\frac{1}{2}\pi$.

::::::{prf:theorem} Complementary angle identities
:label: Thm:Trigonometry:ComplementaryAngles

For any angle $\theta$ we have

$$
\sin(\tfrac{1}{2}\pi-\theta)=\cos(\theta)
$$

and

$$
\cos(\tfrac{1}{2}\pi-\theta)=\sin(\theta).
$$
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Trigonometry:ComplementaryAngles`
:class: tudproof, dropdown

```{figure} Images/Fig-Trigonometry-ComplementaryAnglesProof.png
---
width: 50%
name: Fig:Trigonometry:ComplementaryAnglesProof
class: dark-light
---

An illustration for the proof of the complementary angles identities.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:ComplementaryAnglesProof` into an applet.
:::

Consider the point $P$ in {numref}`Fig:Trigonometry:ComplementaryAnglesProof` with angle $\theta$ and the point $Q$ with angle $\frac{1}{2}\pi-\theta$. Then the $y$-coordinate of $Q$ equals the $x$-coordinate of $P$, while the $x$-coordinate of $Q$ equals the $y$-coordinate of $P$. So we find 

$$
\sin(\tfrac{1}{2}\pi-\theta) = \cos(\theta)\quad\text{and}\quad\cos(\tfrac{1}{2}\pi-\theta) = \cos(\theta).
$$

::::::

Two angles are called **supplementary** if their sum is equal to $\pi$.

::::::{prf:theorem} Supplementary angle identities
:label: Thm:Trigonometry:SupplementaryAngles

For any angle $\theta$ we have

$$
\sin(\pi-\theta)=\sin(\theta),
$$

$$
\cos(\pi-\theta)=-\cos(\theta),
$$

and

$$
\tan(\pi-\theta)=-\tan(\theta).
$$
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Trigonometry:SupplementaryAngles`
:class: tudproof, dropdown

```{figure} Images/Fig-Trigonometry-SupplementaryAnglesProof.png
---
width: 50%
name: Fig:Trigonometry:SupplementaryAnglesProof
class: dark-light
---

An illustration for the proof of the supplementary angles identities.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:SupplementaryAnglesProof` into an applet.
:::

Consider mirroring the point $P$ in {numref}`Fig:Trigonometry:SupplementaryAnglesProof` across the $y$-axis to obtain the point $Q$. Then the $y$-coordinate of $Q$ equals the $y$-coordinate of $P$, while the $x$-coordinate of $Q$ equals the negative of the $x$-coordinate of $P$. As a result of the mirroring, the angle has become $\pi-\theta$. So we find 

$$
\sin(\pi-\theta) = \sin(\theta)\quad\text{and}\quad\cos(\pi-\theta) = -\cos(\theta).
$$

For the tangent function we have 

$$
\tan(\pi-\theta)=\dfrac{\sin(\pi-\theta)}{\cos(\pi-\theta)}=\dfrac{\sin(\theta)}{-\cos(\theta)}=-\tan(\theta).
$$

::::::

::::{question} Short-answer blocks
:type: short-answer
:variant: blocks
:admonition:
:class: question
:showanswer:

Fill in the correct answer in the input fields.
---
MR[-sqrt(2)/2] $\sin(\frac{5}{4}\pi)=$

MR[sqrt(2)/2] $\cos(\frac{7}{4}\pi)=$

MR[-1/2] $\sin(\frac{7}{6}\pi)=$

MR[sqrt(3)/2] $\cos(\frac{11}{6}\pi)=$

MR[-sqrt(2)/2] $\cos(\frac{19}{4}\pi)=$

MR[1/2] $\sin(\frac{25}{6}\pi)=$
---

::::

::::::{prf:theorem} Addition and subtraction formulas
:label: Thm:Trigonometry:AdditionSubtractionFormulas

For every $x,y\in\mathbb{R}$ we have

\begin{align*}
\sin(x+y) &= \sin(x)\cos(y)+\cos(x)\sin(y), \\
\cos(x+y) &= \cos(x)\cos(y)-\sin(x)\sin(y),
\end{align*}
\begin{align*}
\sin(x-y) &=\sin(x)\cos(y)-\cos(x)\sin(y), \\
\cos(x-y) &=\cos(x)\cos(y)+\sin(x)\sin(y),
\end{align*}
and

\begin{align*}
\tan(x+y) &=\frac{\tan(x)+\tan(y)}{1-\tan(x)\tan(y)}, \\
\tan(x-y) &=\frac{\tan(x)-\tan(y)}{1+\tan(x)\tan(y)}.
\end{align*}
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Trigonometry:AdditionSubtractionFormulas`
:class: tudproof, dropdown

For this proof, we need the following figure:

```{figure} Images/Fig-Trigonometry-CosineDifference.png
---
width: 50%
name: Fig:Trigonometry:CosineDifference
class: dark-light
---

An illustration for the proof of the addition and subtraction formulas.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:CosineDifference` into an applet.
:::

In order to prove the summation formulas, we consider {numref}`Fig:Trigonometry:CosineDifference` above with $\angle QOP=\beta-\alpha$. Hence we have $P=(\cos(\alpha),\sin(\alpha))$ and $Q=(\cos(\beta),\sin(\beta))$. The distance between $P$ and $Q$ can be computed using the {prf:ref}`law of cosines <Thm:Trigonometry:LawOfCosines>` as

$$
(PQ)^2=(OP)^2+(OQ)^2-2(OP)(OQ)\cos(\alpha-\beta)=2-2\cos(\alpha-\beta).
$$

On the other hand, this distance can be computed using the {prf:ref}`Pythagorean theorem <Thm:Trigonometry:Pythagoras>` as

\begin{align*}
(PQ)^2&=(\cos(\beta)-\cos(\alpha))^2+(\sin(\beta)-\sin(\alpha))^2\\
&=\cos^2(\beta)-2\cos(\alpha)\cos(\beta)+\cos^2(\alpha)\\
&{}\hspace{25mm}{}+\sin^2(\beta)-2\sin(\alpha)\sin(\beta)+\sin^2(\alpha)\\
&=2-2\left(\cos(\alpha)\cos(\beta)+\sin(\alpha)\cos(\alpha)\right).
\end{align*}
This implies that $\cos(\alpha-\beta)=\cos(\alpha)\cos(\beta)+\sin(\alpha)\sin(\beta)$.

Replacing $\beta$ with $-\beta$ we obtain that $\cos(\alpha+\beta)=\cos(\alpha)\cos(\beta)-\sin(\alpha)\sin(\beta)$.

In {prf:ref}`Thm:Trigonometry:ComplementaryAngles` we obtained that $\sin(\frac{1}{2}\pi-\theta)=\cos(\theta)$ and $\cos(\frac{1}{2}\pi-\theta)=\sin(\theta)$. Using these complementary angles formulas, we obtain

\begin{align*}
\sin(\alpha+\beta)&=\cos(\tfrac{1}{2}\pi-\alpha-\beta)\\
&=\cos(\tfrac{1}{2}\pi-\alpha)\cos(\beta)+\sin(\tfrac{1}{2}\pi-\alpha)\sin(\beta)\\
&=\sin(\alpha)\cos(\beta)+\cos(\alpha)\sin(\beta).
\end{align*}
Replacing $\beta$ with $-\beta$ we obtain $\sin(\alpha-\beta)=\sin(\alpha)\cos(\beta)-\cos(\alpha)\sin(\beta)$.

Now the summation formulas for the tangent follow from these summation formulas for the sine and the cosine:

$$
\begin{align*}
\tan(x+y)&=\frac{\sin(x+y)}{\cos(x+y)}\\
&=\frac{\sin(x)\cos(y)+\cos(x)\sin(y)}{\cos(x)\cos(y)-\sin(x)\sin(y)}\\
&=\frac{\dfrac{\sin(x)\cos(y)}{\cos(x)\cos(y)}+\dfrac{\cos(x)\sin(y)}{\cos(x)\cos(y)}}{\dfrac{\cos(x)\cos(y)}{\cos(x)\cos(y)}-\dfrac{\sin(x)\sin(y)}{\cos(x)\cos(y)}}\\
&=\frac{\dfrac{\sin(x)}{\cos(y)}+\dfrac{\sin(y)}{\cos(y)}}{1-\dfrac{\sin(x)}{\cos(x)}\dfrac{\sin(y)}{\cos(y)}}\\
&=\frac{\tan(x)+\tan(y)}{1-\tan(x)\tan(y)}.
\end{align*}
$$

Replacing $y$ with $-y$ we obtain $\tan(x-y)=\dfrac{\tan(x)-\tan(y)}{1+\tan(x)\tan(y)}$.

::::::

::::::{prf:corollary} Product formulas
:label: Thm:Trigonometry:ProductFormulas

For every $x,y\in\mathbb{R}$ we have

$$
2\sin(x)\cos(y)=\sin(x-y)+\sin(x+y),
$$

$$
2\cos(x)\cos(y)=\cos(x-y)+\cos(x+y)
$$

and

$$
2\sin(x)\sin(y)=\cos(x-y)-\cos(x+y).
$$

::::::

::::::{prf:corollary} Double-angle formulas
:label: Thm:Trigonometry:DoubleAngleFormulas

For every $x\in\mathbb{R}$ we have

$$
\sin(2x)=2\sin(x)\cos(x)
$$

and

$$
\cos(2x)=\cos^2(x)-\sin^2(x).
$$

Combination of the latter formula with {prf:ref}`Thm:Trigonometry:UnitCircleIdentity` leads to

$$
\cos(2x)=2\cos^2(x)-1\quad\text{and}\quad\cos(2x)=1-2\sin^2(x).
$$

::::::

::::::{prf:corollary} Half-angle formulas
:label: Thm:Trigonometry:HalfAngleFormulas

For every $x\in\mathbb{R}$ we have

$$
\sin^2(x)=\frac{1-\cos(2x)}{2}
$$

and

$$
\cos^2(x)=\frac{1+\cos(2x)}{2}.
$$

::::::

## The area of a triangle

Using the fact that a right-angled triangle is half of a rectangle, the area $S$ equals half the product of its legs. This is easily generalised to half the product of a base and the height of a general triangle: $S=\frac{1}{2}ch$. See {numref}`Fig:Trigonometry:Area`.

```{figure} Images/Fig-Trigonometry-ABHTriangle.png
---
width: 50%
name: Fig:Trigonometry:Area
class: dark-light
---

The area of a triangle $\triangle ABC$.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:UnitCircleStandardValues` into an applet.
:::

However, it is not always easy to find this height $h=b\sin(\alpha)$ or $h=a\sin(\beta)$.

There is a formula for the area of a triangle, that only needs the lengths of the three sides. This formula is called Heron's formula named after the Greek mathematician [Heron of Alexandria (probably 1st century AD)](https://en.wikipedia.org/wiki/Hero_of_Alexandria).

::::::{prf:theorem} Heron
:label: Thm:Trigonometry:Heron

```{figure} Images/Fig-Trigonometry-ABCTriangle.png
---
width: 50%
name: Fig:Trigonometry:Heron
class: dark-light
---

Triangle $\triangle ABC$.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:Heron` into an applet.
:::

Let $s=\frac{1}{2}(a+b+c)$ be the semiperimeter of the triangle in {numref}`Fig:Trigonometry:Heron`, then the area $S$ of this triangle equals

$$
S=\sqrt{s(s-a)(s-b)(s-c)}.
$$

::::::

::::::{admonition} Proof of {prf:ref}`Thm:Trigonometry:Heron`
:class: tudproof, dropdown

Consider the perpendicular from $C$ to the opposite side $AB$, as shown in {numref}`Fig:Trigonometry:LawOfCosinesProof`.

Using the Pythagorean theorem we have $h^2=b^2-e^2$ and $h^2=a^2-(c-e)^2$. This implies that $b^2-e^2=a^2-(c-e)^2$ or equivalently $b^2=a^2-c^2+2ce$. Hence we have $e=\dfrac{b^2+c^2-a^2}{2c}$. Then we have

$$
\begin{align*}
h^2&=b^2-e^2 \\
&= b^2-\frac{(b^2+c^2-a^2)^2}{4c^2} \\
&= \frac{4b^2c^2-(b^2+c^2-a^2)^2}{4c^2}\\
&=\frac{(2bc+b^2+c^2-a^2)(2bc-b^2-c^2+a^2)}{4c^2}\\
&=\frac{((b+c)^2-a^2)(a^2-(b-c)^2)}{4c^2}\\
&=\frac{(b-c+a)(b-c-a)(a+b-c)(a-b+c)}{4c^2}.
\end{align*}
$$

Now the area $S$ of the triangle equals $S=\frac{1}{2}ch$ which reads

$$
\begin{align*}
&\frac{c}{2}\sqrt{\frac{(b-c+a)(b-c-a)(a+b-c)(a-b+c)}{4c^2}}\\
&{}\quad{}=\frac{1}{4}\sqrt{(b-c+a)(b-c-a)(a+b-c)(a-b+c)}.
\end{align*}
$$

Let $s=\dfrac{a+b+c}{2}$, then $s-a=\dfrac{b+c-a}{2}$, $s-b=\dfrac{a+c-b}{2}$ and $s-c=\dfrac{a+b-c}{2}$.

Now we conclude that the area $S$ of the triangle equals

$$
\sqrt{\frac{a+b+c}{2}\cdot\frac{b+c-a}{2}\cdot\frac{a+b-c}{2}\cdot\frac{a+c-b}{2}}=\sqrt{s(s-a)(s-b)(s-c)}.
$$

::::::

## The sine as a product

Although we will not cover infinite products in this book we mention the following about the sine.

::::::{prf:Remark}
:label: Ex:Integration:IntroductionExamplesProductSine
It can be shown that

$$
\sin(\pi x)=\pi x\prod_{n=1}^{\infty}\left(1-\frac{x^2}{n^2}\right).
$$

The factors of this infinite product give rise to all zeros of $\sin(\pi x)$ being $0,\pm1,\pm2,\ldots$.
::::::

## Exercises

```{exercise}
:label: Exc:Trigonometry:Exercise_1
Show that $1+\tan^2(x)=\dfrac{1}{\cos^2(x)}$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_1`
:class: solution, dropdown

$$
\begin{align*}
\sin^2(x)+\cos^2(x)=1&\quad\Longleftrightarrow\quad\dfrac{\sin^2(x)}{\cos^2(x)}+\dfrac{\cos^2(x)}{\cos^2(x)}=\dfrac{1}{\cos^2(x)}\\
&\quad\Longleftrightarrow\quad\tan^2(x)+1=\dfrac{1}{\cos^2(x)}.
\end{align*}
$$

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_2
Show that $1+\dfrac{1}{\tan^2(x)}=\dfrac{1}{\sin^2(x)}$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_2`
:class: solution, dropdown

$$
\begin{align*}
\sin^2(x)+\cos^2(x)=1&\quad\Longleftrightarrow\quad\dfrac{\sin^2(x)}{\sin^2(x)}+\dfrac{\cos^2(x)}{\sin^2(x)}=\dfrac{1}{\sin^2(x)}\\
&\quad\Longleftrightarrow\quad1+\dfrac{1}{\tan^2(x)}=\dfrac{1}{\sin^2(x)}.
\end{align*}
$$

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_3
Show that $2\sin(x+y)\cos(x-y)=\sin(2x)+\sin(2y)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_3`
:class: solution, dropdown
Using 

$$
\sin(x+y)=\sin(x)\cos(y)+\cos(x)\sin(y)
$$ 

and 

$$
\cos(x-y)=\cos(x)\cos(y)+\sin(x)\sin(y)
$$ 

we obtain

$$
\begin{align*}
\sin(x+y)\cos(x-y)&=\left(\sin(x)\cos(y)+\cos(x)\sin(y)\right)\\
&{}\hspace{25mm}{}\times\left(\cos(x)\cos(y)+\sin(x)\sin(y)\right)\\
&=\sin(x)\cos(x)\cos^2(y)+\sin^2(x)\sin(y)\cos(y)\\
&{}\quad{}+\cos^2(x)\sin(y)\cos(y)+\sin(x)\cos(x)\sin^2(y).
\end{align*}
$$

Now we use 

$$
\sin^2(x)+\cos^2(x)=1=\sin^2(y)+\cos^2(y),
$$

$$
\sin(2x)=2\sin(x)\cos(y)
$$ 

and 

$$
\sin(2y)=2\sin(y)\cos(y)
$$ 

to find that

$$
2\sin(x+y)\cos(x-y)=2\sin(x)\cos(x)+2\sin(y)\cos(y)=\sin(2x)+\sin(2y).
$$

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_4
Show that $2\cos(x+y)\sin(x-y)=\sin(2x)-\sin(2y)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_4`
:class: solution, dropdown
Using 

$$
\cos(x+y)=\cos(x)\cos(y)-\sin(x)\sin(y)
$$ 

and 

$$
\sin(x-y)=\sin(x)\cos(y)-\cos(x)\sin(y)
$$ 

we obtain

$$
\begin{align*}
\cos(x+y)\sin(x-y)&=\left(\cos(x)\cos(y)-\sin(x)\sin(y)\right)\\
&{}\hspace{25mm}{}\times\left(\sin(x)\cos(y)-\cos(x)\sin(y)\right)\\
&=\sin(x)\cos(x)\cos^2(y)-\cos^2(x)\sin(y)\cos(y)\\
&{}\quad{}-\sin^2(x)\sin(y)\cos(y)+\sin(x)\cos(x)\sin^2(y).
\end{align*}
$$

Now we use 

$$
\sin^2(x)+\cos^2(x)=1=\sin^2(y)+\cos^2(y),
$$ 

$$
\sin(2x)=2\sin(x)\cos(y)
$$ 

and 

$$
\sin(2y)=2\sin(y)\cos(y)
$$ 

to find that

$$
2\cos(x+y)\sin(x-y)=2\sin(x)\cos(x)-2\sin(y)\cos(y)=\sin(2x)-\sin(2y).
$$

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_5
Use the fact that $\frac{1}{12}\pi=\frac{1}{3}\pi-\frac{1}{4}\pi$ to find the exact value of $\sin(\frac{1}{12}\pi)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_5`
:class: solution, dropdown

$$
\begin{align*}
\sin(\tfrac{1}{12}\pi)=\sin(\tfrac{1}{3}\pi-\tfrac{1}{4}\pi)&=\sin(\tfrac{1}{3}\pi)\cos(\tfrac{1}{4}\pi)-\cos(\tfrac{1}{3}\pi)\sin(\tfrac{1}{4}\pi)\\
&=\tfrac{1}{2}\sqrt{3}\cdot\tfrac{1}{2}\sqrt{2}-\tfrac{1}{2}\cdot\tfrac{1}{2}\sqrt{2}=\tfrac{1}{4}\sqrt{6}-\tfrac{1}{4}\sqrt{2}.
\end{align*}
$$

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_6
Use the fact that $\frac{1}{12}\pi=\frac{1}{3}\pi-\frac{1}{4}\pi$ to find the exact value of $\cos(\frac{1}{12}\pi)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_6`
:class: solution, dropdown

$$
\begin{align*}
\cos(\tfrac{1}{12}\pi)=\cos(\tfrac{1}{3}\pi-\tfrac{1}{4}\pi)&=\cos(\tfrac{1}{3}\pi)\cos(\tfrac{1}{4}\pi)+\sin(\tfrac{1}{3}\pi)\sin(\tfrac{1}{4}\pi)\\
&=\tfrac{1}{2}\cdot\tfrac{1}{2}\sqrt{2}+\tfrac{1}{2}\sqrt{3}\cdot\tfrac{1}{2}\sqrt{2}=\tfrac{1}{4}\sqrt{2}+\tfrac{1}{4}\sqrt{6}.
\end{align*}
$$

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_7
Use the fact that $\frac{5}{12}\pi=\frac{1}{6}\pi+\frac{1}{4}\pi$ to find the exact value of $\sin(\frac{5}{12}\pi)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_7`
:class: solution, dropdown

$$
\begin{align*}
\sin(\tfrac{5}{12}\pi)=\sin(\tfrac{1}{6}\pi+\tfrac{1}{4}\pi)&=\sin(\tfrac{1}{6}\pi)\cos(\tfrac{1}{4}\pi)+\cos(\tfrac{1}{6}\pi)\sin(\tfrac{1}{4}\pi)\\
&=\tfrac{1}{2}\cdot\tfrac{1}{2}\sqrt{2}+\tfrac{1}{2}\sqrt{3}\cdot\tfrac{1}{2}\sqrt{2}=\tfrac{1}{4}\sqrt{2}+\tfrac{1}{4}\sqrt{6}.
\end{align*}
$$

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_8
Use the fact that $\frac{5}{12}\pi=\frac{1}{6}\pi+\frac{1}{4}\pi$ to find the exact value of $\cos(\frac{5}{12}\pi)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_8`
:class: solution, dropdown

$$
\begin{align*}
\cos(\tfrac{5}{12}\pi)=\cos(\tfrac{1}{6}\pi+\tfrac{1}{4}\pi)&=\cos(\tfrac{1}{6}\pi)\cos(\tfrac{1}{4}\pi)-\sin(\tfrac{1}{6}\pi)\sin(\tfrac{1}{4}\pi)\\
&=\tfrac{1}{2}\sqrt{3}\cdot\tfrac{1}{2}\sqrt{2}-\tfrac{1}{2}\cdot\tfrac{1}{2}\sqrt{2}=\tfrac{1}{4}\sqrt{6}-\tfrac{1}{4}\sqrt{2}.
\end{align*}
$$

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_9
Let $a=\cos(\frac{1}{5}\pi)$ and $b=\cos(\frac{2}{5}\pi)$. Use $\cos(2x)=2\cos^2(x)-1$ and $\cos(\pi-x)=-\cos(x)$ to find two equations involving $a$ and $b$. Then find the exact values of $\cos(\frac{1}{5}\pi)$, $\cos(\frac{2}{5})$, $\cos(\frac{3}{5}\pi)$ and $\cos(\frac{4}{5}\pi)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_9`
:class: solution, dropdown

$$
\cos(\tfrac{2}{5}\pi)=2\cos^2(\tfrac{1}{5}\pi)-1\quad\Longleftrightarrow\quad b=2a^2-1
$$

and

$$
-\cos(\tfrac{1}{5}\pi)=\cos(\tfrac{4}{5}\pi)=2\cos^2(\tfrac{2}{5}\pi)-1\quad\Longleftrightarrow\quad -a=2b^2-1.
$$

Subtracting we obtain $a+b=2a^2-2b^2=2(a+b)(a-b)$, which implies that $1=2(a-b)$ since $a+b\neq0$. Substituting $b=a-\frac{1}{2}$ we obtain

$$
\begin{align*}
a-\tfrac{1}{2}=2a^2-1&\quad\Longleftrightarrow\quad4a^2-4a-1=0\quad\Longleftrightarrow\quad(2a-\tfrac{1}{2})^2=\tfrac{5}{4}\\
&\quad\Longleftrightarrow\quad a=\tfrac{1}{2}(1\pm\sqrt{5}).
\end{align*} 
$$

Since $a=\cos(\frac{1}{5}\pi)>0$, we conclude that $a=\frac{1}{4}(1+\sqrt{5})$. This implies that $b=a-\frac{1}{2}=\frac{1}{4}(\sqrt{5}-1)$. We conclude that $\cos(\frac{1}{5}\pi)=\frac{1}{4}(1+\sqrt{5})$, $\cos(\frac{2}{5}\pi)=\frac{1}{4}(\sqrt{5}-1)$, $\cos(\frac{3}{5}\pi)=-\cos(\frac{2}{5}\pi)=\frac{1}{4}(1-\sqrt{5})$ and $\cos(\frac{4}{5}\pi)=-\cos(\frac{1}{5}\pi)=-\frac{1}{4}(1+\sqrt{5})$.

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_10
Use the double angle formula $\tan(2x)=\dfrac{2\tan(x)}{1-\tan^2(x)}$ to find the exact values of $\tan(\frac{1}{8}\pi)$ and $\tan(\frac{3}{8}\pi)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_10`
:class: solution, dropdown
Using the double angle formula $\tan(2x)=\dfrac{2\tan(x)}{1-\tan^2(x)}$ for $x=\frac{1}{8}\pi$ we find

$$
\begin{align*}
1=\tan(\tfrac{1}{4}\pi)=\frac{2\tan(\frac{1}{8}\pi)}{1-\tan^2(\frac{1}{8}\pi)}
&\quad\Longleftrightarrow\quad1-\tan^2(\tfrac{1}{8}\pi)=2\tan(\tfrac{1}{8}\pi)\\
&\quad\Longleftrightarrow\quad\tan^2(\tfrac{1}{8}\pi)+2\tan(\tfrac{1}{8}\pi)-1=0.
\end{align*}
$$

Hence $(\tan(\frac{1}{8}\pi)+1)^2-2=0$ or equivalently $\tan(\frac{1}{8}\pi)=-1\pm\sqrt{2}$. Since $\tan(\frac{1}{8}\pi)>0$, we conclude that $\tan(\frac{1}{8}\pi)=-1+\sqrt{2}$.

Similarly, for $x=\frac{3}{8}\pi$ we obtain

$$
\begin{align*}
-1=\tan(\tfrac{3}{4}\pi)=\frac{2\tan(\frac{3}{8}\pi)}{1-\tan^2(\frac{3}{8}\pi)}
&\quad\Longleftrightarrow\quad-1+\tan^2(\tfrac{3}{8}\pi)=2\tan(\tfrac{3}{8}\pi)\\
&\quad\Longleftrightarrow\quad\tan^2(\tfrac{3}{8}\pi)-2\tan(\tfrac{3}{8}\pi)-1=0.
\end{align*}
$$

Hence $(\tan(\frac{3}{8}\pi)-1)^2-2=0$ or equivalently $\tan(\frac{3}{8}\pi)=1\pm\sqrt{2}$. Since $\tan(\frac{3}{8}\pi)>0$, we conclude that $\tan(\frac{3}{8}\pi)=1+\sqrt{2}$.
:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_11
In the picture below we have $\alpha=\frac{1}{7}\pi$. Find the exact value of $\cos(\frac{1}{7}\pi)\cos(\frac{2}{7}\pi)\cos(\frac{3}{7}\pi)$.
```

```{figure} Images/Fig-Trigonometry-Cosines.png
---
width: 50%
name: Fig:Trigonometry:Cosines
align: center
---

A triangle with angles $3\alpha$, $3\alpha$ and $\alpha$, subdivided into two isosceles triangles.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:Cosines` into an applet.
:::

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_11`
:class: solution, dropdown
In each of the three isosceles triangles we use a rectangular triangle being half of it to find that $\cos(\frac{1}{7}\pi)=\dfrac{x+y}{2x}$, $\cos(\frac{2}{7}\pi)=\dfrac{x}{2y}$ and $\cos(\frac{3}{7}\pi)=\dfrac{y}{2(x+y)}$. This implies that

$$
\cos(\tfrac{1}{7}\pi)\cos(\tfrac{2}{7}\pi)\cos(\tfrac{3}{7}\pi)=\frac{x+y}{2x}\cdot\frac{x}{2y}\cdot\frac{y}{2(x+y)}=\frac{1}{8}.
$$

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_12
Let $\alpha=\frac{1}{7}\pi$. Use the double angle formula $\sin(2x)=2\sin(x)\cos(x)$ and the formula $2\sin(x)\cos(y)=\sin(x+y)-\sin(x-y)$ to find the exact value of $\cos(\alpha)\cos(2\alpha)\cos(3\alpha)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_12`
:class: solution, dropdown
Multiply and divide by $2\sin(\alpha)$ to find

$$
\begin{align*}
\cos(\alpha)\cos(2\alpha)\cos(3\alpha)&=\frac{\sin(2\alpha)\cos(2\alpha)\cos(3\alpha)}{2\sin(\alpha)}=\frac{\sin(4\alpha)\cos(3\alpha)}{4\sin(\alpha)}\\
&=\frac{\sin(7\alpha)+\sin(\alpha)}{8\sin(\alpha)}=\frac{1}{8},
\end{align*}
$$

since $\sin(7\alpha)=\sin(\pi)=0$.
:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_13
Let $\alpha=\frac{1}{5}\pi$. Use the double angle formula $\sin(2x)=2\sin(x)\cos(x)$ and the formula $2\sin(x)\cos(y)=\sin(x+y)-\sin(x-y)$ to find the exact value of $\cos(\alpha)+\cos(3\alpha)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_13`
:class: solution, dropdown
Multiply and divide by $2\sin(\alpha)$ to find

$$
\begin{align*}
\cos(\alpha)+\cos(3\alpha)&=\frac{2\sin(\alpha)\cos(\alpha)+2\sin(\alpha)\cos(3\alpha)}{2\sin(\alpha)}\\
&=\frac{\sin(2\alpha)+\sin(4\alpha)-\sin(2\alpha)}{2\sin(\alpha)}=\frac{\sin(4\alpha)}{2\sin(\alpha)}=\frac{1}{2},
\end{align*}
$$

since $\sin(4\alpha)=\sin(\alpha)$ for $\alpha=\frac{1}{5}\pi$.
:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_14
Let $\alpha=\frac{1}{7}\pi$. Use the double angle formula $\sin(2x)=2\sin(x)\cos(x)$ and the formula $2\sin(x)\cos(y)=\sin(x+y)-\sin(x-y)$ to find the exact value of $\cos(\alpha)+\cos(3\alpha)+\cos(5\alpha)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_14`
:class: solution, dropdown
Multiply and divide by $2\sin(\alpha)$ to find

$$
\begin{align*}
&\cos(\alpha)+\cos(3\alpha)+\cos(5\alpha)\\
&{}\quad{}=\frac{2\sin(\alpha)\cos(\alpha)+2\sin(\alpha)\cos(3\alpha)+2\sin(\alpha)\cos(5\alpha)}{2\sin(\alpha)}\\
&{}\quad{}=\frac{\sin(2\alpha)+\sin(4\alpha)-\sin(2\alpha)+\sin(6\alpha)-\sin(4\alpha)}{2\sin(\alpha)}\\
&{}\quad{}=\frac{\sin(6\alpha)}{2\sin(\alpha)}=\frac{1}{2},
\end{align*}
$$

since $\sin(6\alpha)=\sin(\alpha)$ for $\alpha=\frac{1}{7}\pi$.
:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_15
Show that $\displaystyle\frac{\sin(\alpha)+\sin(\beta)}{\cos(\alpha)+\cos(\beta)}=\tan\left(\frac{\alpha+\beta}{2}\right)$ for $\alpha+\beta\neq\pi$ (mod $2\pi$).
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_15`
:class: solution, dropdown
Setting $x+y=\alpha$ and $x-y=\beta$ in 

$$
\sin(x+y)+\sin(x-y)=2\sin(x)\cos(y)
$$ 

and 

$$
\cos(x+y)+\cos(x-y)=2\cos(x)\cos(y),
$$ 

we obtain $x=\dfrac{\alpha+\beta}{2}$ and $y=\dfrac{\alpha-\beta}{2}$ and therefore

$$
\sin(\alpha)+\sin(\beta)=2\sin\left(\frac{\alpha+\beta}{2}\right)\cos\left(\frac{\alpha-\beta}{2}\right)
$$

and

$$
\cos(\alpha)+\cos(\beta)=2\cos\left(\frac{\alpha+\beta}{2}\right)\cos\left(\frac{\alpha-\beta}{2}\right),
$$

which implies that

$$
\frac{\sin(\alpha)+\sin(\beta)}{\cos(\alpha)+\cos(\beta)}=\tan\left(\frac{\alpha+\beta}{2}\right),\quad\alpha+\beta\neq\pi\quad(\operatorname{mod}\;2\pi).
$$

:::

In the exercises below we consider an arbitrary triangle $ABC$ with vertices $A$, $B$ and $C$, sides $a$, $b$ and $c$, and angles $\alpha$, $\beta$ and $\gamma$ as indicated.

```{figure} Images/Fig-Trigonometry-ABCTriangle.png
---
width: 50%
name: Fig:Trigonometry:ABCTriangle
align: center
---
Triangle $\triangle ABC$ with sides $a$, $b$ and $c$ opposite to angles $\alpha$, $\beta$ and $\gamma$ respectively.
```

:::{todo}
Convert {numref}`Fig:Trigonometry:ABCTriangle` into an applet.
:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_16
Show that $a\sin(\beta-\gamma)+b\sin(\gamma-\alpha)+c\sin(\alpha-\beta)=0$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_16`
:class: solution, dropdown
Use the law of sines $\dfrac{a}{\sin(\alpha)}=\dfrac{b}{\sin(\beta)}=\dfrac{c}{\sin(\gamma)}=d$, where $d$ denotes the diameter of the circumscribed circle, to obtain

$$
\begin{align*}
&a\sin(\beta-\gamma)+b\sin(\gamma-\alpha)+c\sin(\alpha-\beta)\\
&=d\sin(\alpha)\sin(\beta-\gamma)+d\sin(\beta)\sin(\gamma-\alpha)+d\sin(\gamma)\sin(\alpha-\beta)\\
&=d\sin(\pi-\alpha)\sin(\beta-\gamma)+d\sin(\pi-\beta)\sin(\gamma-\alpha)+d\sin(\pi-\gamma)\sin(\alpha-\beta)\\
&=d\sin(\beta+\gamma)\sin(\beta-\gamma)+d\sin(\gamma+\alpha)\sin(\gamma-\alpha)+d\sin(\alpha+\beta)\sin(\alpha-\beta)\\
&=d\left(\sin^2(\beta)-\sin^2(\gamma)+\sin^2(\gamma)-\sin^2(\alpha)+\sin^2(\alpha)-\sin^2(\beta)\right)=0.
\end{align*}
$$

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_17
Show that $\sin^2(\alpha)+\sin^2(\beta)+\sin^2(\gamma)=2+2\cos(\alpha)\cos(\beta)\cos(\gamma)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_17`
:class: solution, dropdown

$$
\begin{align*}
&\sin^2(\alpha)+\sin^2(\beta)+\sin^2(\gamma)\\
&=1-\cos^2(\alpha)+1-\cos^2(\beta)+\sin^2(\gamma)
=2-\left(\cos^2(\alpha)-\sin^2(\gamma)\right)-\cos^2(\beta)\\
&=2-\cos(\alpha+\gamma)\cos(\alpha-\gamma)-\cos^2(\beta)=2+\cos(\beta)\cos(\alpha-\gamma)-\cos^2(\beta)\\
&=2+\cos(\beta)\left(\cos(\alpha-\gamma)-\cos(\beta)\right)=2+\cos(\beta)\left(\cos(\alpha-\gamma)+\cos(\alpha+\gamma)\right)\\
&=2+2\cos(\alpha)\cos(\beta)\cos(\gamma).
\end{align*}
$$

Note that this implies that a triangle with angles $\alpha$, $\beta$ and $\gamma$ is a right-angled triangle if and only if $\sin^2(\alpha)+\sin^2(\beta)+\sin^2(\gamma)=2$ since then $\cos(\alpha)=0$, $\cos(\beta)=0$ or $\cos(\gamma)=0$.
:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_18
Show that $\cos^2(\alpha)+\cos^2(\beta)+\cos^2(\gamma)=1-2\cos(\alpha)\cos(\beta)\cos(\gamma)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_18`
:class: solution, dropdown

$$
\begin{align*}
&\cos^2(\alpha)+\cos^2(\beta)+\cos^2(\gamma)\\
&=1-\sin^2(\alpha)+\cos^2(\beta)+\cos^2(\gamma)
=1+\left(\cos^2(\beta)-\sin^2(\alpha)\right)+\cos^2(\gamma)\\
&=1+\cos(\beta+\alpha)\cos(\beta-\alpha)+\cos^2(\gamma)=1-\cos(\gamma)\cos(\beta-\alpha)+\cos^2(\gamma)\\
&=1-\cos(\gamma)\left(\cos(\beta-\alpha)-\cos(\gamma)\right)=1-\cos(\gamma)\left(\cos(\beta-\alpha)+\cos(\beta+\alpha)\right)\\
&=1-2\cos(\alpha)\cos(\beta)\cos(\gamma).
\end{align*}
$$

Note that this implies that a triangle with angles $\alpha$, $\beta$ and $\gamma$ is a right-angled triangle if and only if $\cos^2(\alpha)+\cos^2(\beta)+\cos^2(\gamma)=1$ since then $\cos(\alpha)=0$, $\cos(\beta)=0$ or $\cos(\gamma)=0$.
:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_19
Show that $\sin(2\alpha)+\sin(2\beta)+\sin(2\gamma)=4\sin(\alpha)\sin(\beta)\sin(\gamma)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_19`
:class: solution, dropdown

$$
\begin{align*}
\sin(2\alpha)+\sin(2\beta)+\sin(2\gamma)&=2\sin(\alpha+\beta)\cos(\alpha-\beta)+\sin(2\gamma)\\
&=2\sin(\gamma)\cos(\alpha-\beta)+2\sin(\gamma)\cos(\gamma)\\
&=2\sin(\gamma)\left(\cos(\alpha-\beta)+\cos(\gamma)\right)\\
&=2\sin(\gamma)\left(\cos(\alpha-\beta)-\cos(\alpha+\beta)\right)\\
&=4\sin(\alpha)\sin(\beta)\sin(\gamma).
\end{align*}
$$

:::

```{exercise} 
:label: Exc:Trigonometry:Exercise_20
Show that $\tan(\alpha)+\tan(\beta)+\tan(\gamma)=\tan(\alpha)\tan(\beta)\tan(\gamma)$.
```

:::{admonition} Solution of {numref}`Exc:Trigonometry:Exercise_20`
:class: solution, dropdown
Note that 

$$
\tan(\gamma)=\tan(\pi-\alpha-\beta)=-\tan(\alpha+\beta)=-\frac{\tan(\alpha)+\tan(\beta)}{1-\tan(\alpha)\tan(\beta)}.
$$ 

Hence we have:

$$
\begin{align*}
\tan(\alpha)+\tan(\beta)+\tan(\gamma)&=\tan(\alpha)+\tan(\beta)-\frac{\tan(\alpha)+\tan(\beta)}{1-\tan(\alpha)\tan(\beta)}\\
&=\left(\tan(\alpha)+\tan(\beta)\right)\left(1-\frac{1}{1-\tan(\alpha)\tan(\beta)}\right)\\
&=\left(\tan(\alpha)+\tan(\beta)\right)\frac{1-\tan(\alpha)\tan(\beta)-1}{1-\tan(\alpha)\tan(\beta)}\\
&=\left(\tan(\alpha)+\tan(\beta)\right)\left(\frac{-\tan(\alpha)\tan(\beta)}{1-\tan(\alpha)\tan(\beta)}\right)\\
&=\tan(\alpha)\tan(\beta)\left(-\frac{\tan(\alpha)+\tan(\beta)}{1-\tan(\alpha)\tan(\beta)}\right)\\
&=\tan(\alpha)\tan(\beta)\tan(\gamma).
\end{align*}
$$

:::

```{todo} 
Perhaps add a Grasple exercise here on Heron’s formula, with the diagram of the triangle adapting to the parameters (the side lengths), if that’s possible. See the area calculator on Wikipedia: https://en.wikipedia.org/wiki/Heron%27s_formula.
```

