# Trigonometry

**Thales's theorem**
```{figure} Images/thales.png
---
width: 50%
name: Thales
align: center
---
Thales's theorem
```
::::::{prf:theorem}
:label: Thm.Thales
If $AB$ is a diameter of a circle and $C$ is an arbitrary point on the circle, not equal to $A$ or $B$, then the angle $ACB$ equals $90^{\circ}$.
::::::

::::::{prf:proof} Consider the angles $\alpha$ and $\beta$ as indicated in the picture above. Since the triangle $AMC$ is isosceles ($AM$ and $MC$ are both equal to the radius of the circle), we have: $\angle ACM=\alpha$. Likewise, the triangle $BMC$ is isosceles ($BM$ and $MC$ are both equal to the radius of the circle) and therefore: $\angle BCM=\beta$. So, we have to prove that $\alpha+\beta$ equals $90^{\circ}$.

Now we have: $\angle AMC=180^{\circ}-2\alpha$ and $\angle BMC=180^{\circ}-2\beta$. Further we have: 
$\angle AMC=\angle BMC=180^{\circ}$. Hence:
```{math}
180^{\circ}-2\alpha+180^{\circ}-2\beta=180^{\circ}\quad\Longleftrightarrow\quad 180^{\circ}-2\alpha-2\beta=0
\quad\Longleftrightarrow\quad\alpha+\beta=90^{\circ}.
```
::::::

Angles can be measured in degrees or in radians (abbreviated as rad). The angle given by a complete revolution contains $360^{\circ}$, which is the same as $2\pi$ rad. Therefore:

$$\pi\;\text{rad}=180^{\circ}\quad\Longrightarrow\quad 1\;\text{rad}=\left(\dfrac{180}{\pi}\right)^{\circ}\quad\text{and}\quad 1^{\circ}=\dfrac{\pi}{180}\;\text{rad}.$$ 

In calculus we use radians to measure angles except when otherwise indicated. Moreover, we leave out the "rad".

```{figure} Images/trig.png
---
width: 65%
name: trig
align: left
---
The angle $\theta$
```

The standard position of an angle occurs when we place its vertex at the origin of a coordinate system and its initial side on the positive $x$-axis. A **positive** angle is obtained by rotating the initial side counterclockwise until it coincides with the terminal side. Likewise, **negative** angles are obtained by clockwise rotation.

<br /><br /><br />

For a general angle $\theta$ in standard position we let $P(x,y)$ be any point on the terminal side of $\theta$ and we let $r>0$ be the distance between $O$ and $P$. Then we define:

$$\sin(\theta)=\dfrac{y}{r},\quad\cos(\theta)=\dfrac{x}{r}\quad\text{and}\quad\tan(\theta)=\dfrac{\sin(\theta)}{\cos(\theta)}=\dfrac{y}{x}\quad(x\neq0).$$

<b>Standard values</b>

|$\theta$ (in degrees) | $0^{\circ}$ | $30^{\circ}$ | $45^{\circ}$ | $60^{\circ}$ | $90^{\circ}$ | $120^{\circ}$ | $135^{\circ}$ | $150^{\circ}$ | $180^{\circ}$ | $270^{\circ}$ | $360^{\circ}$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $\theta$ (in radians) | $0$ | $\frac{1}{6}\pi$ | $\frac{1}{4}\pi$ | $\frac{1}{3}\pi$ | $\frac{1}{2}\pi$ | $\frac{2}{3}\pi$ | $\frac{3}{4}\pi$ | $\frac{5}{6}\pi$ | $\pi$ | $\frac{3}{2}\pi$ | $2\pi$ |
| $\sin(\theta)$ | $0$ | $\frac{1}{2}$ | $\frac{1}{2}\sqrt{2}$ | $\frac{1}{2}\sqrt{3}$ | $1$ | $\frac{1}{2}\sqrt{3}$ | $\frac{1}{2}\sqrt{2}$ | $\frac{1}{2}$ | $0$ | $-1$ | $0$ |
| $\cos(\theta)$ | $1$ | $\frac{1}{2}\sqrt{3}$ | $\frac{1}{2}\sqrt{2}$ | $\frac{1}{2}$ | $0$ |$-\frac{1}{2}$ | $-\frac{1}{2}\sqrt{2}$ | $-\frac{1}{2}\sqrt{3}$ | $-1$ | $0$ | $1$ |
| $\tan(\theta)$ | $0$ | $\frac{1}{3}\sqrt{3}$ | $1$ | $\sqrt{3}$ | $-$ | $-\sqrt{3}$ | $-1$ | $-\frac{1}{3}\sqrt{3}$ | $0$ | $-$ | $0$ |

## The Pythagorean theorem
```{figure} Images/righttriangle.png
---
width: 50%
name: right-angled triangle
align: center
---
```
::::::{prf:theorem} 
In a right-angled triangle as in the figure above we have: $a^2+b^2=c^2$.
::::::

::::::{prf:proof} 
An elegant proof of the Pythagorean theorem is based on the following picture:
```{figure} Images/pythagoras.png
---
width: 50%
name: right-angled triangle
align: center
---
```
The area of the large square is $(a+b)^2$ and that of the small square is $c^2$. The area of each of the four triangles is $\frac{1}{2}ab$. So we have:
```{math}
(a+b)^2=c^2+4\cdot\frac{1}{2}ab\quad\Longleftrightarrow\quad a^2+2ab+b^2=c^2+2ab
\quad\Longleftrightarrow\quad a^2+b^2=c^2.
```
::::::

The *law of cosines* is a generalization of the Pythagorean theorem:
```{figure} Images/sincosrule.png
---
width: 50%
name: law of cosines
align: center
---
```
::::::{prf:theorem} 
In an arbitrary triangle as in the figure above we have: $a^2=b^2+c^2-2bc\cos(\alpha)$.
::::::

::::::{prf:proof} 
In the figure above we have according to the Pythagorean theorem:
$h^2=b^2-e^2$ and $h^2=a^2-(c-e)^2$. Hence
```{math}
b^2-e^2=a^2-c^2+2ce-e^2\quad\Longleftrightarrow\quad b^2=a^2-c^2+2ce.
```
Now we have: $\cos(\alpha)=\dfrac{e}{b}$, which implies that $e=b\cos(\alpha)$. So:
```{math}
a^2=b^2+c^2-2bc\cos(\alpha).
```
::::::

Further we have the *law of sines*:

::::::{prf:theorem} 
In an arbitrary triangle as in the figure above we have: $\dfrac{a}{\sin(\alpha)}=\dfrac{b}{\sin(\beta)}$.
::::::

::::::{prf:proof} 
In the figure above we have: $\sin(\alpha)=\dfrac{b}{h}$ and $\sin(\beta)=\dfrac{a}{h}$. Hence: $b\sin(\alpha)=h=a\sin(\beta)$ or equivalently $\dfrac{a}{\sin(\alpha)}=\dfrac{b}{\sin(\beta)}$.
::::::

The last result can be extended with:
```{figure} Images/sincosrule2.png
---
width: 50%
name: law of sines
align: center
---
```
::::::{prf:theorem} 
$\dfrac{c}{\sin(\gamma)}=2r$ with $r$ the radius of the circumscribed circle of the triangle.
::::::

::::::{prf:proof} 
Consider the line segment $AD$ through the center $M$ of the circumscribed circle of the triangle. According to Thales's theorem {prf:ref}`Thm:Thales` the triangle $ABD$ then is a right-angled triangle. Since $C$ and $D$ are two points on the same circle, which are connected to the same chord $AB$, we have: $\gamma=\delta$. Then we have:
```{math}
\sin(\gamma)=\sin(\delta)=\frac{c}{2r}\quad\Longleftrightarrow\quad\frac{c}{\sin(\gamma)}=2r.
```
::::::

## Identities
The Pythagorean theorem leads to $\sin^2(x)+\cos^2(x)=1$.

The sine and cosine are periodic with period $2\pi$: $\sin(\theta+2\pi)=\sin(\theta)$ and $\cos(\theta+2\pi)=\cos(\theta)$. 

The tangent is periodic with period $\pi$: $\tan(\theta+\pi)=\tan(\theta)$.

Further we have: $\sin(-\theta)=-\sin(\theta)$, $\cos(-\theta)=\cos(\theta)$ and $\tan(-\theta)=-\tan(\theta)$.

<b>Connection formulas</b>

$\sin(\theta+\frac{1}{2}\pi)=\cos(\theta)$ and $\cos(\theta+\frac{1}{2}\pi)=-\sin(\theta)$.

<b>Symmetry relations</b>

$\sin(\pi-\theta)=\sin(\theta)$, $\cos(\pi-\theta)=-\cos(\theta)$ and $\tan(\pi-\theta)=-\tan(\theta)$

<b>Double angle formulas</b>

$\sin(2x)=2\sin(x)\cos(x)$ and $\cos(2x)=\cos^2(x)-\sin^2(x)$.

<b>Summation formulas</b>

$\sin(x+y)=\sin(x)\cos(y)+\cos(x)\sin(y)$ and $\cos(x+y)=\cos(x)\cos(y)-\sin(x)\sin(y)$

$\sin(x-y)=\sin(x)\cos(y)-\cos(x)\sin(y)$ and $\cos(x-y)=\cos(x)\cos(y)+\sin(x)\sin(y)$

$\tan(x+y)=\displaystyle\frac{\tan(x)+\tan(y)}{1-\tan(x)\tan(y)}$ and $\tan(x-y)=\displaystyle\frac{\tan(x)-\tan(y)}{1+\tan(x)\tan(y)}$

```{figure} Images/cosdiff.png
---
width: 50%
name: summation
align: center
---
```

In order to prove these summation formulas, we consider the picture above with blue angle $\beta-\alpha$. Hence we have: $P=(\cos(\alpha),\sin(\alpha))$ and $Q=(\cos(\beta),\sin(\beta))$. The distance between $P$ and $Q$ can be computed using the law of cosines:
```{math}
(PQ)^2=(OP)^2+(OQ)^2-2(OP)(OQ)\cos(\alpha-\beta)=2-2\cos(\alpha-\beta).
```
On the other hand, this distance can be computed using the Pythagoran theorem as
```{math}
\begin{align*}
(PQ)^2&=(\cos(\beta)-\cos(\alpha))^2+(\sin(\beta)-\sin(\alpha))^2\\
&=\cos^2(\beta)-2\cos(\alpha)\cos(\beta)+\cos^2(\alpha)+\sin^2(\beta)-2\sin(\alpha)\sin(\beta)+\sin^2(\alpha)\\
&=2-2\left(\cos(\alpha)\cos(\beta)+\sin(\alpha)\cos(\alpha)\right).
\end{align*}
```
This implies that $\cos(\alpha-\beta)=\cos(\alpha)\cos(\beta)+\sin(\alpha)\sin(\beta)$.

Replacing $\beta$ with $-\beta$ we obtain that $\cos(\alpha+\beta)=\cos(\alpha)\cos(\beta)-\sin(\alpha)\sin(\beta)$.

Using $\sin(\beta+\frac{1}{2}\pi)=\cos(\beta)$ and $\cos(\beta+\frac{1}{2}\pi)=-\sin(\beta)$ we obtain
```{math}
\begin{align*}
\sin(\alpha+\beta)&=-\cos(\alpha+\beta+\tfrac{1}{2}\pi)=\sin(\alpha)\sin(\beta+\tfrac{1}{2}\pi)-\cos(\alpha)\cos(\beta+\tfrac{1}{2}\pi)\\
&=\sin(\alpha)\cos(\beta)+\cos(\alpha)\sin(\beta).
\end{align*}
```

Replacing $\beta$ with $-\beta$ we obtain: $\cos(\alpha-\beta)=\sin(\alpha)\cos(\beta)-\cos(\alpha)\sin(\beta)$.
Now the summation formulas for the tangent follow from these summation formulas for the sine and the cosine:

```{math}
\begin{align*}
\tan(x+y)&=\frac{\sin(x+y)}{\cos(x+y)}=\frac{\sin(x)\cos(y)+\cos(x)\sin(y)}{\cos(x)\cos(y)-\sin(x)\sin(y)}\\
&=\frac{\frac{\sin(x)\cos(y)}{\cos(x)\cos(y)}+\frac{\cos(x)\sin(y)}{\cos(x)\cos(y)}}{\frac{\cos(x)\cos(y)}{\cos(x)\cos(y)}-\frac{\sin(x)\sin(y)}{\cos(x)\cos(y)}}=\frac{\frac{\sin(x)}{\cos(y)}+\frac{\sin(y)}{\cos(y)}}{1-\frac{\sin(x)}{\cos(x)}\frac{\sin(y)}{\cos(y)}}=\frac{\tan(x)+\tan(y)}{1-\tan(x)\tan(y)}.
\end{align*}
```
Replacing $y$ with $-y$ we obtain: $\tan(x-y)=\dfrac{\tan(x)-\tan(y)}{1+\tan(x)\tan(y)}$.

The double angle formulas are special cases of these summation formulas.

Finally, we have Heron's formula:

::::::{prf:theorem}
Let $s=\frac{1}{2}(a+b+c)$ be the semiperimeter of the triangle, then the area of the triangle equals $\sqrt{s(s-a)(s-b)(s-c)}$.
::::::

```{figure} Images/abhtriangle.png
---
width: 50%
name: Heron's formula
align: center
---
```

::::::{prf:proof} 
Using the Pythagorean theorem we have $h^2=b^2-e^2$ and $h^2=a^2-(c-e)^2$. This implies that $b^2-e^2=a^2-(c-e)^2$ or equivalently $b^2=a^2-c^2+2ce$. Hence we have: $e=\dfrac{b^2+c^2-a^2}{2c}$. Then we have
```{math}
\begin{align*}
h^2&=b^2-e^2=b^2-\frac{(b^2+c^2-a^2)^2}{4c^2}=\frac{4b^2c^2-(b^2+c^2-a^2)^2}{4c^2}\\
&=\frac{(2bc+b^2+c^2-a^2)(2bc-b^2-c^2+a^2)}{4c^2}=\frac{((b+c)^2-a^2)(a^2-(b-c)^2)}{4c^2}\\
&=\frac{(b-c+a)(b-c-a)(a+b-c)(a-b+c)}{4c^2}
\end{align*}
```
Now the area of the triangle equals $\frac{1}{2}ch$ which reads
```{math}
\begin{align*}
&\frac{c}{2}\sqrt{\frac{(b-c+a)(b-c-a)(a+b-c)(a-b+c)}{4c^2}}\\
&{}\quad{}=\frac{1}{4}\sqrt{(b-c+a)(b-c-a)(a+b-c)(a-b+c)}.
\end{align*}
```
Let $s=\dfrac{a+b+c}{2}$, then: $s-a=\dfrac{b+c-a}{2}$, $s-b=\dfrac{a+c-b}{2}$ and $s-c=\dfrac{a+b-c}{2}$. Now we conclude that the area of the triangle equals
```{math}
\sqrt{\frac{a+b+c}{2}\cdot\frac{b+c-a}{2}\cdot\frac{a+b-c}{2}\cdot\frac{a+c-b}{2}}=\sqrt{s(s-a)(s-b)(s-c)}.
```
::::::

```{exercise}
:label: exercise 1
Show that $1+\tan^2(x)=\dfrac{1}{\cos^2(x)}$.
```

:::{admonition} Solution of exercise 1
:class: solution, dropdown
$\sin^2(x)+\cos^2(x)=1\quad\Longleftrightarrow\quad\dfrac{\sin^2(x)}{\cos^2(x)}+\dfrac{\cos^2(x)}{\cos^2(x)}=\dfrac{1}{\cos^2(x)}\quad\Longleftrightarrow\quad\tan^2(x)+1=\dfrac{1}{\cos^2(x)}$.
:::

```{exercise} 
:label: exercise 2
Show that $1+\dfrac{1}{\tan^2(x)}=\dfrac{1}{\sin^2(x)}$.
```

:::{admonition} Solution of exercise 2
:class: solution, dropdown
$\sin^2(x)+\cos^2(x)=1\quad\Longleftrightarrow\quad\dfrac{\sin^2(x)}{\sin^2(x)}+\dfrac{\cos^2(x)}{\sin^2(x)}=\dfrac{1}{\sin^2(x)}\quad\Longleftrightarrow\quad1+\dfrac{1}{\tan^2(x)}=\dfrac{1}{\sin^2(x)}$.
:::

```{exercise} 
:label: exercise 3
Show that $2\sin(x+y)\cos(x-y)=\sin(2x)+\sin(2y)$.
```

:::{admonition} Solution of exercise 3
:class: solution, dropdown
Using $\sin(x+y)=\sin(x)\cos(y)+\cos(x)\sin(y)$ and $\cos(x-y)=\cos(x)\cos(y)+\sin(x)\sin(y)$ we obtain
```{math}
\begin{align*}
\sin(x+y)\cos(x-y)&=\left(\sin(x)\cos(y)+\cos(x)\sin(y)\right)\left(\cos(x)\cos(y)+\sin(x)\sin(y)\right)\\
&=\sin(x)\cos(x)\cos^2(y)+\sin^2(x)\sin(y)\cos(y)\\
&{}\quad{}+\cos^2(x)\sin(y)\cos(y)+\sin(x)\cos(x)\sin^2(y).
\end{align*}
```
Now we use $\sin^2(x)+\cos^2(x)=1=\sin^2(y)+\cos^2(y)$, $\sin(2x)=2\sin(x)\cos(y)$ and $\sin(2y)=2\sin(y)\cos(y)$ to find that
```{math}
2\sin(x+y)\cos(x-y)=2\sin(x)\cos(x)+2\sin(y)\cos(y)=\sin(2x)+\sin(2y).
```
:::

```{exercise} 
:label: exercise 4
Show that $2\cos(x+y)\sin(x-y)=\sin(2x)-\sin(2y)$.
```

:::{admonition} Solution of exercise 4
:class: solution, dropdown
Using $\cos(x+y)=\cos(x)\cos(y)-\sin(x)\sin(y)$ and $\sin(x-y)=\sin(x)\cos(y)-\cos(x)\sin(y)$ we obtain
```{math}
\begin{align*}
\cos(x+y)\sin(x-y)&=\left(\cos(x)\cos(y)-\sin(x)\sin(y)\right)\left(\sin(x)\cos(y)-\cos(x)\sin(y)\right)\\
&=\sin(x)\cos(x)\cos^2(y)-\cos^2(x)\sin(y)\cos(y)\\
&{}\quad{}-\sin^2(x)\sin(y)\cos(y)+\sin(x)\cos(x)\sin^2(y).
\end{align*}
```
Now we use $\sin^2(x)+\cos^2(x)=1=\sin^2(y)+\cos^2(y)$, $\sin(2x)=2\sin(x)\cos(y)$ and $\sin(2y)=2\sin(y)\cos(y)$ to find that
```{math}
2\cos(x+y)\sin(x-y)=2\sin(x)\cos(x)-2\sin(y)\cos(y)=\sin(2x)-\sin(2y).
```
:::

```{exercise} 
:label: exercise 5
Use the fact that $\frac{1}{12}\pi=\frac{1}{3}\pi-\frac{1}{4}\pi$ to find the exact value of $\sin(\frac{1}{12}\pi)$.
```

:::{admonition} Solution of exercise 5
:class: solution, dropdown
```{math}
\begin{align*}
\sin(\tfrac{1}{12}\pi)=\sin(\tfrac{1}{3}\pi-\tfrac{1}{4}\pi)&=\sin(\tfrac{1}{3}\pi)\cos(\tfrac{1}{4}\pi)-\cos(\tfrac{1}{3}\pi)\sin(\tfrac{1}{4}\pi)\\
&=\tfrac{1}{2}\sqrt{3}\cdot\tfrac{1}{2}\sqrt{2}-\tfrac{1}{2}\cdot\tfrac{1}{2}\sqrt{2}=\tfrac{1}{4}\sqrt{6}-\tfrac{1}{4}\sqrt{2}.
\end{align*}
```
:::

```{exercise} 
:label: exercise 6
Use the fact that $\frac{1}{12}\pi=\frac{1}{3}\pi-\frac{1}{4}\pi$ to find the exact value of $\cos(\frac{1}{12}\pi)$.
```

:::{admonition} Solution of exercise 6
:class: solution, dropdown
```{math}
\begin{align*}
\cos(\tfrac{1}{12}\pi)=\cos(\tfrac{1}{3}\pi-\tfrac{1}{4}\pi)&=\cos(\tfrac{1}{3}\pi)\cos(\tfrac{1}{4}\pi)+\sin(\tfrac{1}{3}\pi)\sin(\tfrac{1}{4}\pi)\\
&=\tfrac{1}{2}\cdot\tfrac{1}{2}\sqrt{2}+\tfrac{1}{2}\sqrt{3}\cdot\tfrac{1}{2}\sqrt{2}=\tfrac{1}{4}\sqrt{2}+\tfrac{1}{4}\sqrt{6}.
\end{align*}
```
:::

```{exercise} 
:label: exercise 7
Use the fact that $\frac{5}{12}\pi=\frac{1}{6}\pi+\frac{1}{4}\pi$ to find the exact value of $\sin(\frac{5}{12}\pi)$.
```

:::{admonition} Solution of exercise 7
:class: solution, dropdown
```{math}
\begin{align*}
\sin(\tfrac{5}{12}\pi)=\sin(\tfrac{1}{6}\pi+\tfrac{1}{4}\pi)&=\sin(\tfrac{1}{6}\pi)\cos(\tfrac{1}{4}\pi)+\cos(\tfrac{1}{6}\pi)\sin(\tfrac{1}{4}\pi)\\
&=\tfrac{1}{2}\cdot\tfrac{1}{2}\sqrt{2}+\tfrac{1}{2}\sqrt{3}\cdot\tfrac{1}{2}\sqrt{2}=\tfrac{1}{4}\sqrt{2}+\tfrac{1}{4}\sqrt{6}.
\end{align*}
```
:::

```{exercise} 
:label: exercise 8
Use the fact that $\frac{5}{12}\pi=\frac{1}{6}\pi+\frac{1}{4}\pi$ to find the exact value of $\cos(\frac{5}{12}\pi)$.
```

:::{admonition} Solution of exercise 8
:class: solution, dropdown
```{math}
\begin{align*}
\cos(\tfrac{5}{12}\pi)=\cos(\tfrac{1}{6}\pi+\tfrac{1}{4}\pi)&=\cos(\tfrac{1}{6}\pi)\cos(\tfrac{1}{4}\pi)-\sin(\tfrac{1}{6}\pi)\sin(\tfrac{1}{4}\pi)\\
&=\tfrac{1}{2}\sqrt{3}\cdot\tfrac{1}{2}\sqrt{2}-\tfrac{1}{2}\cdot\tfrac{1}{2}\sqrt{2}=\tfrac{1}{4}\sqrt{6}-\tfrac{1}{4}\sqrt{2}.
\end{align*}
```
:::

```{exercise} 
:label: exercise 9
Let $a=\cos(\frac{1}{5}\pi)$ and $b=\cos(\frac{2}{5}\pi)$. Use $\cos(2x)=2\cos^2(x)-1$ and $\cos(\pi-x)=-\cos(x)$ to find two equations involving $a$ and $b$. Then find the exact values of $\cos(\frac{1}{5}\pi)$, $\cos(\frac{2}{5})$, $\cos(\frac{3}{5}\pi)$ and $\cos(\frac{4}{5}\pi)$.
```

:::{admonition} Solution of exercise 9
:class: solution, dropdown
```{math}
\cos(\tfrac{2}{5}\pi)=2\cos^2(\tfrac{1}{5}\pi)-1\quad\Longleftrightarrow\quad b=2a^2-1
```
and
```{math}
-\cos(\tfrac{1}{5}\pi)=\cos(\tfrac{4}{5}\pi)=2\cos^2(\tfrac{2}{5}\pi)-1\quad\Longleftrightarrow\quad -a=2b^2-1.
```
Subtracting we obtain $a+b=2a^2-2b^2=2(a+b)(a-b)$, which implies that $1=2(a-b)$ since $a+b\neq0$, Substituting $b=a-\frac{1}{2}$ we obtain
```{math}
a-\tfrac{1}{2}=2a^2-1\quad\Longleftrightarrow\quad4a^2-4a-1=0\quad\Longleftrightarrow\quad(2a-\tfrac{1}{2})^2=\tfrac{5}{4}\quad\Longleftrightarrow\quad a=\tfrac{1}{2}(1\pm\sqrt{5}). 
```
Since $a=\cos(\frac{1}{5}\pi)>0$, we conclude that $a=\frac{1}{4}(1+\sqrt{5})$. This implies that $b=a-\frac{1}{2}=\frac{1}{4}(\sqrt{5}-1)$. We conclude that $\cos(\frac{1}{5}\pi)=\frac{1}{4}(1+\sqrt{5})$, $\cos(\frac{2}{5}\pi)=\frac{1}{4}(\sqrt{5}-1)$, $\cos(\frac{3}{5}\pi)=-\cos(\frac{2}{5}\pi)=\frac{1}{4}(1-\sqrt{5})$ and $\cos(\frac{4}{5}\pi)=-\cos(\frac{1}{5}\pi)=-\frac{1}{4}(1+\sqrt{5})$.
```
:::

```{exercise} 
:label: exercise 10
Use the double angle formula $\tan(2x)=\dfrac{2\tan(x)}{1-\tan^2(x)}$ to find the exact values of $\tan(\frac{1}{8}\pi)$ and $\tan(\frac{3}{8}\pi)$.
```

:::{admonition} Solution of exercise 10
:class: solution, dropdown
Using the double angle formula $\tan(2x)=\dfrac{2\tan(x)}{1-\tan^2(x)}$ for $x=\frac{1}{8}\pi$ we find
```{math}
\begin{align*}
1=\tan(\tfrac{1}{4}\pi)=\frac{2\tan(\frac{1}{8}\pi)}{1-\tan^2(\frac{1}{8}\pi)}
&\quad\Longleftrightarrow\quad1-\tan^2(\tfrac{1}{8}\pi)=2\tan(\tfrac{1}{8}\pi)\\
&\quad\Longleftrightarrow\quad\tan^2(\tfrac{1}{8}\pi)+2\tan(\tfrac{1}{8}\pi)-1=0.
\end{align*}
```
Hence: $(\tan(\frac{1}{8}\pi)+1)^2-2=0$ or equivalently $\tan(\frac{1}{8}\pi)=-1\pm\sqrt{2}$. Since $\tan(\frac{1}{8}\pi)>0$, we conclude that $\cos(\frac{1}{8}\pi)=-1+\sqrt{2}$.

Similarly, for $x=\frac{3}{8}\pi$ we obtain
```{math}
\begin{align*}
-1=\tan(\tfrac{3}{4}\pi)=\frac{2\tan(\frac{3}{8}\pi)}{1-\tan^2(\frac{3}{8}\pi)}
&\quad\Longleftrightarrow\quad-1+\tan^2(\tfrac{3}{8}\pi)=2\tan(\tfrac{3}{8}\pi)\\
&\quad\Longleftrightarrow\quad\tan^2(\tfrac{3}{8}\pi)-2\tan(\tfrac{3}{8}\pi)-1=0.
\end{align*}
```
Hence: $(\tan(\frac{3}{8}\pi)-1)^2-2=0$ or equivalently $\tan(\frac{3}{8}\pi)=1\pm\sqrt{2}$. Since $\tan(\frac{3}{8}\pi)>0$, we conclude that $\cos(\frac{3}{8}\pi)=1+\sqrt{2}$.
:::

```{exercise} 
:label: exercise 11
In the picture below we have $\alpha=\frac{1}{7}\pi$. Find the exact value of $\cos(\frac{1}{7}\pi)\cos(\frac{2}{7}\pi)\cos(\frac{3}{7}\pi)$.
```

```{figure} Images/cosines.png
---
width: 50%
name: product of cosines
align: center
---
```

:::{admonition} Solution of exercise 11
:class: solution, dropdown
In each of the three equilateral triangles we use a rectangular triangle being half of it to find that $\cos(\frac{1}{7}\pi)=\dfrac{x+y}{2x}$, $\cos(\frac{2}{7}\pi)=\dfrac{x}{2y}$ and $\cos(\frac{3}{7}\pi)=\dfrac{y}{2(x+y)}$. This implies that
```{math}
\cos(\tfrac{1}{7}\pi)\cos(\tfrac{2}{7}\pi)\cos(\tfrac{3}{7}\pi)=\frac{x+y}{2x}\cdot\frac{x}{2y}\cdot\frac{y}{2(x+y)}=\frac{1}{8}.
```
:::

```{exercise} 
:label: exercise 12
Let $\alpha=\frac{1}{7}\pi$. Use the double angle formula $\sin(2x)=2\sin(x)\cos(x)$ and the formula $2\sin(x)\cos(y)=\sin(x+y)-\sin(x-y)$ to find the exact value of $\cos(\alpha)\cos(2\alpha)\cos(3\alpha)$.
```

:::{admonition} Solution of exercise 12
:class: solution, dropdown
Multiply and divide by $2\sin(\alpha)$ to find
```{math}
\cos(\alpha)\cos(2\alpha)\cos(3\alpha)=\frac{\sin(2\alpha)\cos(2\alpha)\cos(3\alpha)}{2\sin(\alpha)}=\frac{\sin(4\alpha)\cos(3\alpha)}{4\sin(\alpha)}=\frac{\sin(7\alpha)+\sin(\alpha)}{8\sin(\alpha)}=\frac{1}{8},
```
since $\sin(7\alpha)=\sin(\pi)=0$.
:::

```{exercise} 
:label: exercise 13
Let $\alpha=\frac{1}{5}\pi$. Use the double angle formula $\sin(2x)=2\sin(x)\cos(x)$ and the formula $2\sin(x)\cos(y)=\sin(x+y)-\sin(x-y)$ to find the exact value of $\cos(\alpha)+\cos(3\alpha)$.
```

:::{admonition} Solution of exercise 13
:class: solution, dropdown
Multiply and divide by $2\sin(\alpha)$ to find
```{math}
\begin{align*}
\cos(\alpha)+\cos(3\alpha)&=\frac{2\sin(a)\cos(\alpha)+2\sin(\alpha)\cos(3\alpha)}{2\sin(\alpha)}\\
&=\frac{\sin(2\alpha)+\sin(4\alpha)-\sin(2\alpha)}{2\sin(\alpha)}=\frac{\sin(4\alpha)}{2\sin(\alpha)}=\frac{1}{2},
\end{align*}
```
since $\sin(4\alpha)=\sin(\alpha)$ for $\alpha=\frac{1}{5}\pi$.
:::

```{exercise} 
:label: exercise 14
Let $\alpha=\frac{1}{7}\pi$. Use the double angle formula $\sin(2x)=2\sin(x)\cos(x)$ and the formula $2\sin(x)\cos(y)=\sin(x+y)-\sin(x-y)$ to find the exact value of $\cos(\alpha)+\cos(3\alpha)+\cos(5\alpha)$.
```

:::{admonition} Solution of exercise 14
:class: solution, dropdown
Multiply and divide by $2\sin(\alpha)$ to find
```{math}
\begin{align*}
\cos(\alpha)+\cos(3\alpha)+\cos(3\alpha)&=\frac{2\sin(\alpha)\cos(\alpha)+2\sin(\alpha)\cos(3\alpha)+2\sin(\alpha)\cos(5\alpha)}{2\sin(\alpha)}\\
&=\frac{\sin(2\alpha)+\sin(4\alpha)-\sin(2\alpha)+\sin(6\alpha)-\sin(4\alpha)}{2\sin(\alpha)}\\
&=\frac{\sin(6\alpha)}{2\sin(\alpha)}=\frac{1}{2},
\end{align*}
```
since $\sin(6\alpha)=\sin(\alpha)$ for $\alpha=\frac{1}{7}\pi$.
:::

```{exercise} 
:label: exercise 15
Show that $\displaystyle\frac{\sin(\alpha)+\sin(\beta)}{\cos(\alpha)+\cos(\beta)}=\tan\left(\frac{\alpha+\beta}{2}\right)$ for $\alpha+\beta\neq\pi$ (mod $2\pi$).
```

:::{admonition} Solution of exercise 15
:class: solution, dropdown
Setting $x+y=\alpha$ and $x-y=\beta$ in $\sin(x+y)+\sin(x-y)=2\sin(x)\cos(y)$ and $\cos(x+y)+\cos(x-y)=2\cos(x)\cos(y)$, we obtain $x=\dfrac{\alpha+\beta}{2}$ and $y=\dfrac{\alpha-\beta}{2}$ and therefore
```{math}
\sin(\alpha)+\sin(\beta)=2\sin\left(\frac{\alpha+\beta}{2}\right)\cos\left(\frac{\alpha-\beta}{2}\right)
```
and
```{math}
\cos(\alpha)+\cos(\beta)=2\cos\left(\frac{\alpha+\beta}{2}\right)\cos\left(\frac{\alpha-\beta}{2}\right),
```
which implies that
```{math}
\frac{\sin(\alpha)+\sin(\beta)}{\cos(\alpha)+\cos(\beta)}=\tan\left(\frac{\alpha+\beta}{2}\right),\quad\alpha+\beta\neq\pi\quad(\text{mod}\;2\pi).
```
:::

In the exercises below we consider an arbitrary triangle $ABC$ with vertices $A$, $B$ and $C$, sides $a$, $b$ and $c$, and angles $\alpha$, $\beta$ and $\gamma$ as indicated.

```{figure} Images/abctriangle.png
---
width: 50%
name: Triangle $ABC$
align: center
---
```

```{exercise} 
:label: exercise 16
Show that $a\sin(\beta-\gamma)+b\sin(\gamma-\alpha)+c\sin(\alpha-\beta)=0$.
```

:::{admonition} Solution of exercise 16
:class: solution, dropdown
Use the law of sines $\dfrac{a}{\sin(\alpha)}=\dfrac{b}{\sin(\beta)}=\dfrac{c}{\sin(\gamma)}=d$, where $d$ denotes the diameter of the circumscribed circle, to obtain
```{math}
\begin{align*}
&a\sin(\beta-\gamma)+b\sin(\gamma-\alpha)+c\sin(\alpha-\beta)\\
&=d\sin(\alpha)\sin(\beta-\gamma)+d\sin(\beta)\sin(\gamma-\alpha)+d\sin(\gamma)\sin(\alpha-\beta)\\
&=d\sin(\pi-\alpha)\sin(\beta-\gamma)+d\sin(\pi-\beta)\sin(\gamma-\alpha)+d\sin(\pi-\gamma)\sin(\alpha-\beta)\\
&=d\sin(\beta+\gamma)\sin(\beta-\gamma)+d\sin(\gamma+\alpha)\sin(\gamma-\alpha)+d\sin(\alpha+\beta)\sin(\alpha-\beta)\\
&=d\left(\sin^2(\beta)-\sin^2(\gamma)+\sin^2(\gamma)-\sin^2(\alpha)+\sin^2(\alpha)-\sin^2(\beta)\right)=0.
\end{align*}
```
:::

```{exercise} 
:label: exercise 17
Show that $\sin^2(\alpha)+\sin^2(\beta)+\sin^2(\gamma)=2+2\cos(\alpha)\cos(\beta)\cos(\gamma)$.
```

:::{admonition} Solution of exercise 17
:class: solution, dropdown
```{math}
\begin{align*}
&\sin^2(\alpha)+\sin^2(\beta)+\sin^2(\gamma)\\
&=1-\cos^2(\alpha)+1-\cos^2(\beta)+\sin^2(\gamma)
=2-\left(\cos^2(\alpha)-\sin^2(\gamma)\right)-\cos^2(\beta)\\
&=2-\cos(\alpha+\gamma)\cos(\alpha-\gamma)-\cos^2(\beta)=2+\cos(\beta)\cos(\alpha-\gamma)-\cos^2(\beta)\\
&=2+\cos(\beta)\left(\cos(\alpha-\gamma)-\cos(\beta)\right)=2+\cos(\beta)\left(\cos(\alpha-\gamma)+\cos(\alpha+\gamma)\right)\\
&=2+2\cos(\alpha)\cos(\beta)\cos(\gamma).
\end{align*}
```
Note that this implies that a triangle with angles $\alpha$, $\beta$ and $\gamma$ is a right-angled triangle if and only if $\sin^2(\alpha)+\sin^2(\beta)+\sin^2(\gamma)=2$ since then $\cos(\alpha)=0$, $\cos(\beta)=0$ or $\cos(\gamma)=0$.
:::

```{exercise} 
:label: exercise 18
Show that $\cos^2(\alpha)+\cos^2(\beta)+\cos^2(\gamma)=1-2\cos(\alpha)\cos(\beta)\cos(\gamma)$.
```

:::{admonition} Solution of exercise 18
:class: solution, dropdown
```{math}
\begin{align*}
&\cos^2(\alpha)+\cos^2(\beta)+\cos^2(\gamma)\\
&=1-\sin^2(\alpha)+\cos^2(\beta)+\cos^2(\gamma)
=1+\left(\cos^2(\beta)-\sin^2(\alpha)\right)+\cos^2(\gamma)\\
&=1+\cos(\beta+\alpha)\cos(\beta-\alpha)+\cos^2(\gamma)=1-\cos(\gamma)\cos(\beta-\alpha)+\cos^2(\gamma)\\
&=1-\cos(\gamma)\left(\cos(\beta-\alpha)-\cos(\gamma)\right)=1-\cos(\gamma)\left(\cos(\beta-\alpha)+\cos(\beta+\alpha)\right)\\
&=1-2\cos(\alpha)\cos(\beta)\cos(\gamma).
\end{align*}
```
Note that this implies that a triangle with angles $\alpha$, $\beta$ and $\gamma$ is a right-angled triangle if and only if $\cos^2(\alpha)+\cos^2(\beta)+\cos^2(\gamma)=1$ since then $\cos(\alpha)=0$, $\cos(\beta)=0$ or $\cos(\gamma)=0$.
:::

```{exercise} 
:label: exercise 19
Show that $\sin(2\alpha)+\sin(2\beta)+\sin(2\gamma)=4\sin(\alpha)\sin(\beta)\sin(\gamma)$.
```

:::{admonition} Solution of exercise 19
:class: solution, dropdown
```{math}
\begin{align*}
\sin(2\alpha)+\sin(2\beta)+\sin(2\gamma)&=2\sin(\alpha+\beta)\cos(\alpha-\beta)+\sin(2\gamma)\\
&=2\sin(\gamma)\cos(\alpha-\beta)+2\sin(\gamma)\cos(\gamma)\\
&=2\sin(\gamma)\left(\cos(\alpha-\beta)+\cos(\gamma)\right)\\
&=2\sin(\gamma)\left(\cos(\alpha-\beta)-\cos(\alpha+\beta)\right)\\
&=4\sin(\alpha)\sin(\beta)\sin(\gamma).
\end{align*}
```
:::

```{exercise} 
:label: exercise 20
Show that $\tan(\alpha)+\tan(\beta)+\tan(\gamma)=\tan(\alpha)\tan(\beta)\tan(\gamma)$.
```

:::{admonition} Solution of exercise 20
:class: solution, dropdown
Note that $\tan(\gamma)=\tan(\pi-\alpha-\beta)=-\tan(\alpha+\beta)=-\dfrac{\tan(\alpha)+\tan(\beta)}{1-\tan(\alpha)\tan(\beta)}$. Hence we have:
```{math}
\begin{align*}
\tan(\alpha)+\tan(\beta)+\tan(\gamma)&=\tan(\alpha)+\tan(\beta)-\frac{\tan(\alpha)+\tan(\beta)}{1-\tan(\alpha)\tan(\beta)}\\
&=\left(\tan(\alpha)+\tan(\beta)\right)\left(1-\frac{1}{1-\tan(\alpha)\tan(\beta)}\right)\\
&=\left(\tan(\alpha)+\tan(\beta)\right)\frac{1-\tan(\alpha)\tan(\beta)-1}{1-\tan(\alpha)\tan(\beta)}\\
&=\left(\tan(\alpha)+\tan(\beta)\right)\left(\frac{-\tan(\alpha)\tan(\beta)}{1-\tan(\alpha)\tan(\beta)}\right)\\
&=\tan(\alpha)\tan(\beta)\left(-\frac{\tan(\alpha)+\tan(\beta)}{1-\tan(\alpha)\tan(\beta)}\right)\\
&=\tan(\alpha)\tan(\beta)\tan(\gamma).
\end{align*}
```
:::
