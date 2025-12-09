# Separable differential equations

In this section we cover:

- Separable differential equations
- Algorithmic check
- Link with first-order linear differential equations, same example?






::::::{prf:Definition}
A first-order differential equation is called **separable** if it can be written in the form:
```{math}
\frac{dy}{dx}=g(x)f(y).
```
::::::

If $f(y)\neq0$, then this can be written as
```{math}
\frac{dy}{dx}=g(x)f(y)=\frac{g(x)}{h(y)}\quad\text{with}\quad h(y)=\frac{1}{f(y)}.
```
Then we have
```{math}
h(y)\,dy=g(x)\,dx\quad\Longrightarrow\quad\int h(y)\,dy=\int g(x)\,dx.
```
This equation defines $y$ implicitly as a function of $x$.

::::::{prf:Example}
$\displaystyle\frac{dy}{dx}=\frac{x}{y}$ with $y\neq0$ is separable:
```{math}
y\,dy=x\,dx\quad\Longleftrightarrow\quad\tfrac{1}{2}y^2=\tfrac{1}{2}x^2+C\quad\Longleftrightarrow\quad y^2=x^2+K.
```
This is an implicit form of the solution. If necessary this implies the explicit form $y(x)=\pm\sqrt{x^2+K}$ with $K\in\mathbb{R}$.
::::::

::::::{prf:Example}
$\displaystyle\frac{dy}{dx}=\frac{y}{x}$ with $x>0$ is separable. Note that $y=0$ is a solution. For $y\neq0$ we have:
```{math}
\frac{dy}{y}=\frac{dx}{x}\quad\Longleftrightarrow\quad\ln|y(x)|=\ln|x|+C\quad\Longleftrightarrow\quad y(x)=\pm e^Cx.
```
Since $y=0$ is a solution too, this implies that the general solution is: $y=Kx$ with $K\in\mathbb{R}$.
::::::

::::::{prf:Example}
$\dfrac{dy}{dx}=2xy$ is separable. Note that $y=0$ is a solution. For $y\neq0$ we have:
```{math}
\frac{dy}{y}=2x\,dx\quad\Longleftrightarrow\quad\ln|y(x)|=x^2+C\quad\Longleftrightarrow\quad y(x)=\pm e^C\cdot e^{x^2}.
```
Since $y=0$ is a solution too, this implies that the general solution is: $y(x)=Ke^{x^2}$ with $K\in\mathbb{R}$.
::::::

::::::{prf:Example}
$\displaystyle\frac{dy}{dx}=2x(1+y^2)$ is separable:
```{math}
\frac{dy}{1+y^2}=2x\,dx\quad\Longleftrightarrow\quad\arctan(y)=x^2+C\quad\Longleftrightarrow\quad y=\tan(x^2+C).
```
Hence the general solution is: $y(x)=\tan(x^2+C)$ with $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
Consider the integral $I(t)=\displaystyle\int_0^{\infty}e^{-x^2}\cos(xt)\,dx$. Then we have: $I(0)=\displaystyle\int_0^{\infty}e^{-x^2}\,dx=\tfrac{1}{2}\sqrt{\pi}$ (see: the normal distribution) and
```{math}
\begin{align*}
I'(t)&=-\int_0^{\infty}xe^{-x^2}\sin(xt)\,dx=\frac{1}{2}\int_0^{\infty}\sin(xt)\,de^{-x^2}
=\frac{1}{2}e^{-x^2}\sin(xt)\bigg|_0^{\infty}-\frac{1}{2}\int_0^{\infty}e^{-x^2}\,d\sin(xt)\\[2.5mm]
&=0-\frac{1}{2}t\int_0^{\infty}e^{-x^2}\cos(xt)\,dx=-\frac{1}{2}tI(t).
\end{align*}
```
This is a separable differential equation with general solution $I(t)=Ce^{-\frac{1}{4}t^2}$. Now we have $C=I(0)=\frac{1}{2}\sqrt{\pi}$. Hence: $I(t)=\frac{1}{2}\sqrt{\pi}e^{-\frac{1}{4}t^2}$.
::::::

## Applications

**Population growth**

The logistic differential equation $\displaystyle\frac{dP}{dt}=kP\left(1-\frac{P}{M}\right)$ is separable. Observe that $P(t)=0$ and $P(t)=M$ are two constant solutions, which are called *equilibrium solutions*. For $P\neq0$ and $P\neq M$ we have:
```{math}
\frac{dP}{dt}=kP\left(1-\frac{P}{M}\right)\quad\Longrightarrow\quad\frac{dP}{P\displaystyle\left(1-\frac{P}{M}\right)}=k\,dt\quad\Longrightarrow\quad
\int\frac{M}{P(M-P)}\,dP=\int k\,dt.
```
Now we use the *partial fraction decomposition* $\displaystyle\frac{M}{P(M-P)}=\frac{1}{P}+\frac{1}{M-P}$ to find that
```{math}
\int\frac{M}{P(M-P)}\,dP=\int\left(\frac{1}{P}+\frac{1}{M-P}\right)\,dP=\ln|P|-\ln|M-P|+\text{a constant.}
```
Hence we have:
```{math}
\ln\left|\frac{P}{M-P}\right|=kt+C\quad\Longrightarrow\quad\frac{M-P}{P}=\pm e^{-C}\cdot e^{-kt}.
```
Note that $\pm e^{-C}$ is an arbitrary positive or negative constant. If we replace this by an arbitrary constant $K$ we retrieve the "lost" constant solution $P=M$: $\displaystyle\frac{M-P}{P}=Ke^{-kt}$. This is an implicit form of the solution. Solving for $P$ we obtain $P(t)=\displaystyle\frac{M}{1+Ke^{-kt}}$. For an *initial condition* $P(0)=P_0>0$ we find that $K=\displaystyle\frac{M-P_0}{P_0}$. So we conclude that
```{math}
P(t)=\frac{M}{1+Ke^{-kt}}\quad\text{with}\quad K=\frac{M-P_0}{P_0}.
```

**Newton's law of cooling**

Newton's law of cooling states that the rate of cooling of an object is proportional to the temperature difference between the object and its surroundings, provided that this difference is not too large. Let $T(t)$ be the temperature of the object at time $t$ and $T_s$ the temperature of the surroundings, then this law can be written as:
```{math}
\frac{dT}{dt}=k(T-T_s),\quad T(0)=T_0,
```
where $T_0$ denotes the temperature of the object at time $t=0$. Here $T(0)=T_0$ is called the *initial condition*.

Since $T_s$ is constant, the substitution $y(t)=T(t)-T_s$ easily leads to the solution:
```{math}
T(t)=T_s+(T_0-T_s)e^{kt}.
```
However, note that the differential equation is separable and that $T(t)=T_s$ is a (constant) solution. For $T(t)\neq T_s$ we have:
```{math}
\frac{dT}{T-T_s}=k\,dt\quad\Longrightarrow\quad\ln|T-T_s|=kt+C\quad\Longrightarrow\quad T(t)-T_s=\pm e^C\cdot e^{kt}.
```
Since $T(t)=T_s$ is a solution too, we conclude that the general solution is $T(t)-T_s=Ke^{kt}$ with $K\in\mathbb{R}$. Now the initial condition $T(0)=T_0$ leads to $K=T_0-T_s$. Hence we have: $T(t)=T_s+(T_0-T_s)e^{kt}$.

::::::{prf:example}
A bottle of soda pop with a temperature of $20^{\circ}\;\text{C}$ is placed in a refrigerator where the temperature is $5^{\circ}\;\text{C}$. After half an hour the soda pop has cooled to $15^{\circ}\;\text{C}$.

1) What is the temperature of the soda pop after one hour?

2) How long does it take for the soda pop to cool to $10^{\circ}\;\text{C}$?
::::::

::::::{admonition} Solution
Note that $T_s=5$ and $T(0)=20$ here. So we have:
```{math}
\frac{dT}{dt}=k(T-5),\quad T(0)=20\quad\Longrightarrow\quad T(t)=5+15e^{kt}.
```
If we choose to take *minutes* for the time $t$, we conclude that
```{math}
T(30)=15\quad\Longleftrightarrow\quad 15=5+15e^{30k}\quad\Longleftrightarrow\quad 30k=\ln\left(\frac{10}{15}\right)=\ln\left(\frac{2}{3}\right).
```
This implies that $k=\frac{1}{30}\ln\left(\frac{2}{3}\right)\approx−0.0135$. Then we have:

1) $T(60)=5+15e^{−0.0135\cdot60}\approx11.7^{\circ}\;\text{C}$.

So, the temperatue of the soda pop after one hour is approximately $11.7^{\circ}\;\text{C}$.

2) $T(t)=10\;\Longleftrightarrow\;10=5+15e^{−0.0135t}\quad\Longleftrightarrow\quad−0.0135t=\ln\left(\frac{5}{15}\right)=\ln\left(\frac{1}{3}\right)$.

This implies that it takes approximately $\displaystyle\frac{\ln\left(\frac{1}{3}\right)}{−0.0135}\approx81.4$ minutes for the soda pop to cool to $10^{\circ}\;\text{C}$.
::::::

::::::{prf:example}
A cup of coffee with a temperature of $95^{\circ}\;\text{C}$ is placed in a room where the temperature is $20^{\circ}\;\text{C}$. After $10$ minutes the coffee has cooled to $75^{\circ}\;\text{C}$.

1) What is the temperature of the coffee after $15$ minutes?

2) How long does it take for the coffee to cool to $80^{\circ}\;\text{C}$?
::::::

::::::{admonition} Solution
Note that $T_s=20$ and $T(0)=95$ here. So we have:
```{math}
\frac{dT}{dt}=k(T-20),\quad T(0)=95\quad\Longrightarrow\quad T(t)=20+75e^{kt}.
```
Note that
```{math}
T(10)=75\quad\Longleftrightarrow\quad 75=20+75e^{10k}\quad\Longleftrightarrow\quad 10k=\ln\left(\frac{55}{75}\right)=\ln\left(\frac{11}{15}\right).
```
This implies that $k=\frac{1}{10}\ln\left(\frac{11}{15}\right)\approx−0.031$. Then we have:

1) $T(15)=20+75e^{−0.031\cdot15}\approx67^{\circ}\;\text{C}$.

So, the temperature of the coffee after $15$ minutes is approximately $67^{\circ}\;\text{C}$.

2) $T(t)=80\;\Longleftrightarrow\;80=20+75e^{−0.031t}\quad\Longleftrightarrow\quad−0.031t=\ln\left(\frac{60}{75}\right)=\ln\left(\frac{4}{5}\right)$.

This implies that it takes approximately $\displaystyle\frac{\ln\left(\frac{4}{5}\right)}{−0.031}\approx7.2$ minutes for the coffee to cool to $80^{\circ}\;\text{C}$.
::::::

**Torricelli's law**

```{figure} Images/torricelli.png
---
width: 50%
name: Torricelli's law
align: right
---
```
Torricelli's law, also known as Torricelli's theorem, is a theorem in fluid dynamics relating the speed of fluid flowing out of an orifice to the height of the fluid above the hole. The law states that the speed of efflux $v$ of a fluid through a sharp-edged hole at the bottom of a tank filled to a depth $h$ is the same as the speed that a body (in this case a drop of water) would acquire in falling freely from a height $h$, i.e. $v=\sqrt{2gh}$, where $g$ is the acceleration due to gravity ($981\;\text{cm}/\text{s}^2$ near the surface of the earth).

Now consider a cylindrical tank that has a hole with area $a$ in its bottom (see the picture) and assume that water is draining from the hole. If $V(t)$ denotes the volume of the water at time $t$, then Torricelli's law leads to:
```{math}
\frac{dV}{dt}=-a\sqrt{2gh}.
```
If the cross-sectional area of the tank is $A$, then we have:
```{math}
A\frac{dh}{dt}=-a\sqrt{2gh}.
```
Note that this is a separable differential equation.

If the radius of the tank is $10\;\text{cm}$, the radius of the hole is $1\;\text{cm}$ and the height of the water is $10\;\text{cm}$, then
```{math}
A=100\pi\;\text{cm}^3,\quad a=\pi\;\text{cm}^3\quad\text{and}\quad h=10\;\text{cm}.
```
How long does it take for the water to drain completely?

So we want to solve the initial-value problem:
```{math}
100\frac{dh}{dt}=-\sqrt{2gh},\quad h(0)=10.
```
Note that $h(t)=0$ is a (constant) solution of the differential equation. For $h(t)\neq0$ we obtain
```{math}
100\frac{dh}{\sqrt{h}}=-\sqrt{2g}\,dt\quad\Longrightarrow\quad 200\sqrt{h}=-\sqrt{2g}t+C.
```
The initial condition $h(0)=10$ leads to $C=200\sqrt{10}$. This implies that the solution can be written as
```{math}
h(t)=\left(\frac{200\sqrt{10}-\sqrt{2g}t}{200}\right)^2.
```
Now we can answer the question: $h(t)=0\;\Longleftrightarrow\;t=\displaystyle\frac{200\sqrt{10}}{\sqrt{2g}}$. This implies that the tank will be empy after $\displaystyle\frac{200\sqrt{10}}{\sqrt{2g}}\approx14.3$ seconds.

**Mixing problems**

::::::{prf:example}
A tank contains $100\;\text{g}$ salt dissolved in $250\;\ell$ water. This solution is kept thoroughly mixed and drains from the tank at a rate of $5\;\ell/\text{min}$. Simultaneously, brine with a concentration of $10\;\text{g}/\ell$ enters the tank at the same rate of $5\;\ell/\text{min}$. After how many minutes is the amount of salt in the tank equal to $1300\;\text{g}$?
::::::

::::::{admonition} Solution
Let $y(t)$ denote the amount of salt (in 
) in the tank at time $t$ (in $\text{min}$). Then we have: $y(0)=100$ (initial condition) and $\displaystyle\frac{dy}{dt}=50−\frac{y}{50}$. This differential equation is separable. Note that 
 is a (constant) solution of this differential equation. For $y(t)\neq2500$ we have:
```{math}
\frac{dy}{dt}=\frac{2500-y}{50}\quad\Longleftrightarrow\quad\frac{dy}{2500-y}=\frac{dt}{50}.
```
Integration now leads to
```{math}
\int\frac{dy}{2500-y}=\int\frac{dt}{50}\quad\Longleftrightarrow\quad-\ln|2500-y|=\frac{1}{50}t+C.
```
This implies that
```{math}
2500-y(t)=\pm e^{-\frac{1}{50}t-C}=\pm e^{-C}\cdot e^{-\frac{1}{50}t}.
``` 
Note that $\pm e^{-C}$ is an arbitrary positive or negative constant. If we replace this by an arbitrary constant $K$ we retrieve the "lost" constant solution $y(t)=2500$: $y(t)=2500-Ke^{-\frac{1}{50}t}$. Finally, the initial condition $y(0)=100$ leads to $K=2400$.

So the solution of the initial-value problem is $y(t)=2500-2400e^{-\frac{1}{50}t}$.

Now we are able to answer the question:
```{math}
y(t)=1300\quad\Longleftrightarrow\quad e^{-\frac{1}{5}t}=\tfrac{1}{2}\quad\Longleftrightarrow\quad t=50\ln(2),
``` 
which implies that after $50\ln(2)\approx35$ minutes the amount of salt in the tank will be $1300\;\text{g}$. It is easy to check that
```{math}
y(50\ln(2))=2500-2400e^{-\ln(2)}=2500-1200=1300.
```
::::::

::::::{prf:example}
A tank contains $100\;\ell$ beer with $5\%$ alcohol. Beer with $7\%$ alcohol is pumped into the tank at a rate of $1\;\ell/\text{min}$. The fluid in the tank is kept thoroughly mixed and drains from the tank at a rate of $1\;\ell/\text{min}$. What is the alcohol percentage of the beer in the tank after $1$ hour ($60$ minutes)?
::::::

::::::{admonition} Solution
Let $y(t)$ denote the amount of alcohol (in $\ell$) in the tank at time $t$ (in $\text{min}$). Then we have: $y(0)=5$ (initial condition) and $\displaystyle\frac{dy}{dt}=\frac{7}{100}-\frac{y}{100}$. This differential is separable. Note that $y(t)=7$ is a (constant) solution of this differential equation. For $y(t)\neq7$ we have:
```{math}
\frac{dy}{dt}=\frac{7-y}{100}\quad\Longleftrightarrow\quad\frac{dy}{7-y}=\frac{dt}{100}. 
``` 
Integration now leads to
```{math}
\int\frac{dy}{7-y}=\int\frac{dt}{100}\quad\Longleftrightarrow\quad-\ln|7-y|=\frac{1}{100}t+C. 
``` 
This implies that
```{math}
7-y(t)=\pm e^{-\frac{1}{100}t-C}=\pm e^{-C}\cdot e^{-\frac{1}{100}t}. 
``` 
Note that $\pm e^{-C}$ is an arbitrary positive or negative constant. If we replace this by an arbitrary constant $K$ we retrieve the "lost" constant solution $y(t)=7$: $y(t)=7-Ke^{-\frac{1}{100}t}$. Finally, the initial condition $y(0)=5$ leads to $K=2$.

So the solution of the initial-value problem is $y(t)=7-2e^{-\frac{1}{100}t}$.

Now we obtain that $y(60)=7-2e^{-\frac{3}{5}}\approx5.9$. Since the volume of the fluid in the tank is $100\;\ell$, this is the alcohol percentage after $1$ hour.
::::::

## (Grasple) exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8ef26791-6d07-4dc6-b31a-d23b4a8edafa?id=75340
:label: grasple_exercise_12_1_1
:dropdown:
:description: Is the differential equation separable or not?
::::::