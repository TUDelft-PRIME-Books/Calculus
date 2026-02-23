# First-order linear differential equations

In this section we cover:

- standard form
- Integrating factor
- Solving linear first order differential equations
- Mention name Bernouilli equations
- Link with separable equations, same example?













::::::{prf:Definition}
A first-order differential equation is called **linear** if it can be written in the form:
```{math}
\frac{dy}{dx}+P(x)y=Q(x),
```
where $P(x)$ and $Q(x)$ are continuous functions on any interval.
::::::

We consider two methods to solve this kind of differential equations: using an *integrating factor* and the method of *variation of the parameter*.

Using an **integrating factor**:

If we multiply the differential equation (in standard form) by a factor $I(x)\neq0$, then the solutions remain the same. We try to find such a factor $I(x)$ such that
```{math}
I(x)y'(x)+I(x)P(x)y(x)=I(x)Q(x)
```
implies that
```{math}
\frac{d}{dx}\left(I(x)y(x)\right)=I(x)Q(x).
```
Then we must have that: $I'(x)=I(x)P(x)$. Such a factor $I(x)$ is called an integrating factor because then we can integrate:
```{math}
I(x)y(x)=\int I(x)Q(x)\,dx.
```
And since $I(x)\neq0$ this leads to the solution: $y(x)=\displaystyle\frac{1}{I(x)}\int I(x)Q(x)\,dx$.
In order to find such an integrating factor $I(x)\neq0$ we have to solve the differential equation
```{math}
I'(x)=I(x)P(x).
```
However, this is a separable differential equation. Note that $I(x)=\exp\left(\displaystyle\int P(x)\,dx\right)$ is a solution, where $\displaystyle\int P(x)\,dx$ denotes any antiderivative of $P(x)$.

This leads to the following 'recipe':

* Write the differential equation in the standard form $\displaystyle\frac{dy}{dx}+P(x)y=Q(x)$.

* Find an (arbitrary) *integrating factor* $I(x)\neq0$ such that $I'(x)=I(x)P(x)$.

* Multiply the differential equation in *standard form* by $I(x)$:
```{math}
\underbrace{I(x)y'(x)+I(x)P(x)y(x)}_{\displaystyle\left(I(x)y(x)\right)'}=I(x)Q(x). 
``` 
 
* Integrate both sides of this equation: $I(x)y(x)=\displaystyle\int I(x)Q(x)\,dx$.

* Divide by $I(x)\neq0$: $y(x)=\displaystyle\frac{1}{I(x)}\int I(x)Q(x)\,dx$.

**Examples**

::::::{prf:Example}
Consider the differential equation $y'+2y=3$. This has $I(x)=e^{2x}\neq0$ as an integrating factor (since $I'(x)=2I(x)$). Hence: $(e^{2x}y(x))'=3e^{2x}$. This implies that $e^{2x}y(x)=\displaystyle\int 3e^{2x}\,dx=\tfrac{3}{2}e^{2x}+C$ with $C$ an arbitrary (integration) constant. Hence: $y(x)=\frac{3}{2}+Ce^{-2x}$ with $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
Consider the differential equation $y'-2xy=4x$. This has $I(x)=e^{-x^2}\neq0$ as an integrating factor (since $I'(x)=-2xI(x)$). Hence: $(e^{-x^2}y(x))'=4xe^{-x^2}$. This implies that $e^{-x^2}y(x)=\displaystyle\int 4xe^{-x^2}\,dx=-2e^{-x^2}+C$ with $C$ an arbitrary (integration) constant. Hence: $y(x)=-2+Ce^{x^2}$ with $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
The differential equation $xy'+y=1$ with $x>0$ is not in *standard form*. So, first we write it as $y'+\displaystyle\frac{1}{x}y=\frac{1}{x}$ and then note that $I(x)=e^{\ln(x)}=x>0$ is an integrating factor (since $I'(x)=\displaystyle\frac{1}{x}I(x)$). Then we have: $(xy(x))'=1$ and therefore $xy(x)=x+C$ with $C$ an arbitrary (integration) constant. Hence: $y(x)=\displaystyle\frac{x+C}{x}=1+\frac{C}{x}$ with $C\in\mathbb{R}$.
::::::

We might also use **variation of the parameter**:

First consider the corresponding homogeneous differential equation (also in *standard form* with 
$Q(x)$ replaced by $0$):
```{math}
\frac{dy}{dx}+P(x)y=0.
``` 
This differential equation is separable, since for $y\neq0$ it can be written in the form
```{math}
\frac{dy}{y}=-P(x)\,dx\quad\Longrightarrow\quad\ln|y(x)|=-\int P(x)\,dx.
``` 
This leads to a general solution of the form $y(x)=C\exp\left(-\displaystyle\int P(x)\,dx\right)$ with $C$ an arbitrary (integration) constant.

Now we replace this constant by a function of $x$, say $u(x)$, then substitution into the nonhomogeneous differential equation implies:
```{math}
\begin{align*}
&u'(x)\exp\left(-\int P(x)\,dx\right)-P(x)u(x)\exp\left(-\int P(x)\,dx\right)+P(x)u(x)\exp\left(-\int P(x)\,dx\right)=Q(x)\\[2.5mm]
&{}\hspace{25mm}\Longleftrightarrow\quad u'(x)=Q(x)\exp\left(\int P(x)\,dx\right).
\end{align*}
``` 
Integration then leads to $u(x)$ including an arbitrary (integration) constant. Substitution into 
$y(x)=u(x)\left(-\displaystyle\int P(x)\,dx\right)$ then gives the general solution.

::::::{prf:Example}
Consider the differential equation $y'+2y=3$. Now first we consider the homogeneous equation $y'+2y=0$ with general solution $y(x)=Ce^{-2x}$. Now we sustitute $y(x)=u(x)e^{-2x}$ into the original nonhomogeneous equation:
```{math}
u'(x)e^{-2x}-2u(x)e^{-2x}+2u(x)e^{-2x}=3\quad\Longrightarrow\quad u'(x)=3e^{2x}\quad\Longrightarrow\quad u(x)=\tfrac{3}{2}e^{2x}+C.
```
So, the general solution is: $y(x)=u(x)e^{-2x}=\frac{3}{2}+Ce^{-2x}$ with $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
Consider the differential equation $y'-2xy=4x$. Now first we consider the homogeneous equation $y'-2xy=0$ with general solution $y(x)=Ce^{x^2}$. Now we sustitute $y(x)=u(x)e^{x^2}$ into the original nonhomogeneous equation:
```{math}
u'(x)e^{x^2}+2xu(x)e^{x^2}-2xu(x)e^{x^2}=4x\quad\Longrightarrow\quad u'(x)=4xe^{-x^2}\quad\Longrightarrow\quad u(x)=-2e^{-x^2}.
```
So, the general solution is: $y(x)=u(x)e^{x^2}=-2+Ce^{x^2}$ with $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
Consider the differential equation $xy'+y=1$ with $x>0$. First we write it in *standard form* $y'+\displaystyle\frac{1}{x}y=\frac{1}{x}$. Then we consider the homogeneous equation $y'+\displaystyle\frac{1}{x}y=0$ with general solution $y(x)=\displaystyle\frac{C}{x}$. Now we sustitute $y(x)=\displaystyle\frac{u(x)}{x}$ into the original nonhomogeneous equation:
```{math}
\frac{u'(x)}{x}-\frac{u(x)}{x^2}+\frac{u(x)}{x^2}=\frac{1}{x}\quad\Longrightarrow\quad u'(x)=1\quad\Longrightarrow\quad u(x)=x+C.
```
So, the general solution is: $y(x)=\displaystyle\frac{u(x)}{x}=\frac{x+C}{x}=1+\frac{C}{x}$ with $C\in\mathbb{R}$.
::::::


## Applications

**Learning curve**

Let $P(t)$ be the performance level of someone learning a skill as a function of the training time $t$. The graph of $P$ is called a *learning curve*.

If $M$ is the maximum level of performance of which the learner is capable, then
```{math}
\frac{dP}{dt}=k(M-P)
```
is a a reasonable model for learning, where $k$ is a positive constant.

Note that this differential equation is *linear*. So we look for an integrating factor $I(t)$:
```{math}
I(t)P'(t)+kI(t)P(t)=kMI(t)\quad\text{with}\quad I'(t)=kI(t)\quad\Longrightarrow\quad I(t)=e^{kt}\;\text{for instance}.
```
This implies that
```{math}
\frac{d}{dt}\left[e^{kt}P(t)\right]=kMe^{kt}\quad\Longrightarrow\quad e^{kt}P(t)=\int kMe^{kt}\,dt=Me^{kt}+C.
```
Hence we have: $P(t)=M+Ce^{-kt}$.

```{figure} Images/learning.png
---
width: 50%
name: Learning curve
align: center
---
```

**Free fall**
```{figure} Images/freefall.png
---
width: 50%
name: Free fall
align: center
---
```

If a skydiver jumps out of a plane with no initial velocity, the air resistance will be proportional to its velocity. A model for the velocity of the skydiver is:
```{math}
m\frac{dv}{dt}=mg-kv,\quad v(0)=0,
```
where $m$ denotes the mass of the skydiver, $g=9.81\;\text{m}/\text{s}^2$ is the acceleration due to gravity and $k$ is a positive constant.

Assume that $m=90\;\text{kg}$ and $k=15$, then we have:
```{math}
90\frac{dv}{dt}=90g-15v\quad\Longleftrightarrow\quad v'(t)+\tfrac{1}{6}v(t)=g.
```
This is a *linear* differential equation. Using the integrating factor $e^{\frac{1}{6}t}$ we find that:
```{math}
\frac{d}{dt}\left[e^{\frac{1}{6}t}v(t)\right]=ge^{\frac{1}{6}t}\quad\Longrightarrow\quad e^{\frac{1}{6}t}v(t)=6ge^{\frac{1}{6}t}+C
\quad\Longrightarrow\quad v(t)=6g+Ce^{-\frac{1}{6}t}.
```
Now we use the initial condition $v(0)=0$ to find that $C=-6g$. Hence we have: $v(t)=6g\left(1-e^{-\frac{1}{6}t}\right)$.

Using $6g=6\cdot9.8=58.8$, for instance this implies that the speed of the skydiver after $10$ seconds is: $v(10)=58.8\left(1-e^{-\frac{5}{3}}\right)\approx47.7\;\text{m}/\text{s}$.

Furthermore, since $v(t)=50\;\Longleftrightarrow\displaystyle\;t=-6\ln\left(\frac{8.8}{58.8}\right)\approx11.4$ we conclude that it takes approximately $$11.4$ seconds to reach a speed of $50\;\text{m}/\text{s}$ (which is $180\;\text{km}/\text{h}$).

Finally, if the free fall could last forever, the (theoretical) maximum speed would be $\lim\limits_{t\to\infty}v(t)=58.8\;\text{m}/\text{s}$. Solving
```{math}
v(t)=58\quad\Longleftrightarrow\quad t=-6\ln\left(\frac{0.8}{58.8}\right)\approx25.8
``` 
we conclude that it takes approximately $25.8$ seconds to reach a speed of $58\;\text{m}/\text{s}$ (which is $208.8\;\text{km}/\text{h}$).

**Mixing problems**

The differential equations in the examples 8 and 9 in the previous section are both separable and linear. We can also solve these differential equations using the methods explained in this section. Extra examples or exercises?

::::::{prf:example}
A tank contains $100\;\ell$ brine with $100\;\text{g}$ salt dissolved in water. This solution is kept thoroughly mixed and drains from the tank at a rate of $3\;\ell/\text{min}$. Simultaneously, brine with a concentration of $10\;\text{g}/\ell$ enters the tank at a rate of $1\;\ell/\text{min}$. What is the amount of salt (in $\text{g}$) in the tank after $25$ minutes?
::::::

::::::{admonition} Solution
Let $y(t)$ denote the amount of salt (in $\text{g}$) in the tank at time $t$ (in $\text{min}$). Then we have: $y(0)=100$ (initial condition) and $\displaystyle\frac{dy}{dt}=10−3\cdot\frac{y}{100-2t}$. This differential equation is linear (and not separable). So we look for an integrating factor $I(t)$:
```{math}
I(t)y'(t)+\frac{3}{100-2t}I(t)y(t)=10I(t)\quad\text{with}\quad I'(t)=\frac{3}{100-2t}I(t). 
``` 
Hence: $I(t)=\exp\left(-\frac{3}{2}\ln(100-2t)\right)=(100-2t)^{-\frac{3}{2}}$ for instance. Then we have:
```{math}
\frac{d}{dt}\left[(100-2t)^{-\frac{3}{2}}y(t)\right]=10(100-2t)^{-\frac{3}{2}}\quad\Longrightarrow\quad
(100-2t)^{-\frac{3}{2}}y(t)=10(100-2t)^{-\frac{1}{2}}+C 
``` 
and therefore: $y(t)=10(100-2t)+C(100-2t)^{\frac{3}{2}}$. The initial condition $y(0)=100$ leads to: 
```{math}
100=1000+1000C\quad\text{or equivalently}\quad C=-\frac{900}{1000}=-\frac{9}{10}.
```
Hence: $y(t)=10(100-2t)-\frac{9}{10}(100-2t)^{\frac{3}{2}}$.

For $t=25$ we obtain: $y(25)=500-\frac{9}{10}\cdot50\sqrt{50}=500-225\sqrt{2}$.

*Remark:* Note that the differential equation only holds for $0 < t < 50$. After $50$ minutes the tank will be empty.
::::::

::::::{prf:example}
A tank with a volume of $500\;\ell$ contains $25\;\text{g}$ salt dissolved in $100\;\ell$ water. This solution is kept thoroughly mixed and drains from the tank at a rate of $1\;\ell/\text{min}$. Simultaneously, brine with a concentration of $5\;\text{g}/\ell$ enters the tank at a rate of $2\;\ell/\text{min}$. What is the amount of salt (in $\text{g}$) in the tank after $25$ minutes?
::::::

::::::{admonition} Solution
Let $y(t)$ denote the amount of salt (in $\text{g}$) in the tank at time $t$ (in $\text{min}$). Then we have: $y(0)=25$ (initial condition) and $\displaystyle\frac{dy}{dt}=10−1\cdot\frac{y}{100+t}$. This differential equation is linear (and not separable). So we look for an integrating factor $I(t)$:
```{math}
I(t)y'(t)+\frac{1}{100+t}I(t)y(t)=10I(t)\quad\text{with}\quad I'(t)=\frac{1}{100+t}I(t).
``` 
Hence: $I(t)=\exp\left(\ln(100+t)\right)=100+t$ for instance. Then we have:
```{math}
\frac{d}{dt}\left[(100+t)y(t)\right]=10(100+t)=1000+10t\quad\Longrightarrow\quad
(100+t)y(t)=1000t+5t^2+C.
```
The initial condition $y(0)=25$ leads to $C=2500$. Hence: $y(t)=\displaystyle\frac{5t^2+1000t+2500}{100+t}$.

For $t=25$ we obtain: $y(25)=\displaystyle\frac{5\cdot625+25000+2500}{125}=25+200+20=245$.

*Remark:* Note that the differential equation only holds for $0 < t < 400$. After $400$ minutes the tank will overflow.
::::::

## (Grasple) exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/35be7874-2885-4c35-809a-28a6ffe13a07?id=64429
:label: grasple_exercise_12_2_1
:dropdown:
:description: Is the differential equation linear and/or separable?
::::::