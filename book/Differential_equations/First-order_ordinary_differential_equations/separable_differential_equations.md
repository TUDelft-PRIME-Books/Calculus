(Sec:ODE1:Separable)=

# Separable differential equations

## Introduction

[^FootnoteInt]: It might happen that when solving the equation we obtain an integral that we cannot evaluate by hand.

In {numref}`Sec:DE:Intro` we mentioned that differential equations can only be solved when they have a specific form. In this section we consider a class of first-order differential equations called **separable differential equations**. For these differential equations, it turns out to always[^FootnoteInt] be possible to find an implicit solution, though it is not always possible to turn this into an explicit solution. 

## Solving separable differential equations

::::::{prf:Definition}
A first-order differential equation is called **separable** if it can be written in the form

$$
\frac{dy}{dx}=f(x)g(y)
$$

for some functions $f$ and $g$ that are both defined and continuous on some open interval $I$.

::::::
That is, a first-order differential equation is separable if the right-hand side can be written as the product of a part that only depends on $x$ and a part that only depends on $y$.

Often, the quickest way to see that a differential equation is separable is to write it into the correct form. Of course, if you cannot figure out how to do this for a certain first-order differentiable equation it might very well be possible that the differential equation is not separable, but it might also be the case that you simply do not 'see' the right functions $f$ and $g$. If you want to make sure that a differential equation is not separable, you can use the following criterion, which uses partial derivatives (see {numref}`Sec:PartialDerivatives`).

::::::{prf:theorem}
:label: Thm:DiffSep:CheckSep
Consider a first-order differential equation 

$$
 \frac{dy}{dx}=F(x,y)
$$

and suppose that $F$ and its first and second partial derivatives are continuous. Then the differential equation is separable if, and only if, we have

$$
 FF_{xy}-F_xF_y=0.
$$
::::::

:::{admonition} Proof of {prf:ref}`Thm:DiffSep:CheckSep`
:class: tudproof, dropdown
Suppose that the differential equation is separable, which means that we can write $F(x,y)=f(x)g(y)$. Then we obtain

$$
 FF_{xy}-F_xF_y=\left(f(x)g(y)\right)\left(f'(x)g'(y)\right)-\left(f'(x)g(y)\right)\left(f(x)g'(y)\right)=0.
$$

On the other hand, suppose that $FF_{xy}-F_xF_y=0$. Let $R$ be any connected subset of the domain of $F$ such that $F(x,y)\neq 0$ for all $(x,y)\in R$. On $R$, we define the function

$$
 G(x,y)=\ln|F(x,y)|.
$$

Using {prf:ref}`Thm:Diffinverse:Logdiff` we obtain

$$
 G_x=\frac{F_x}{F}.
$$

In addition, we obtain using the quotient rule and our assumption $FF_{xy}-F_xF_y=0$ that

$$
 G_{xy}=\frac{FF_{xy}-F_xF_y}{F^2}=0.
$$

Since $R$ is connected, we find that

$$
 G_x=a(x)
$$

for some function $a$. Integrating this equation with respect to $x$, we find

$$
 G(x,y)=\int a(x)\,dx=A(x)+B(y)
$$

for some continuous functions $A$ and $B$. Taking the exponent of this expression, we find

$$
 |F(x,y)|=e^{G(x,y)}=e^{A(x)}e^{B(y)}.
$$

Since $S$ is connected, $F\neq 0$ on $R$ and $F$ is continuous, the sign of $F$ is constant on $R$, so we obtain

$$
 F(x,y)=e^{A(x)}e^{B(y)},\qquad\text{or}\qquad F(x,y)=-e^{A(x)}e^{B(y)}.
$$

In both cases, we have $F(x,y)=f(x)g(y)$ for some continuous functions $f$ and $g$ for $(x,y)\in R$. With this, we have defined the functions $f$ and $g$ on the set

$$
 S=\left\{(x,y)\in\mathbb{R}^2\,\middle|\,F(x,y)\neq 0\right\}.
$$

Since $f$ and $g$ are continuous on each connected component of $S$, they are continuous on $S$.

We now only need to show that these functions can be extended continuously to the full domain of $F$. Let $(x_0,y_0)$ in the domain of $F$ with $F(x_0,y_0)=0$. If there is an open neighbourhood of $(x_0,y_0)$ on which $F$ is identically $0$, we can extende $X$ and and $Y$ to be $0$ on this neighbourhood and they will be continuous there. So we assume that for any neighbourhood of $(x_0,y_0)$ the function $F$ is not identically $0$. Let $(a,b)$ be any point in $S$. Then we note that for any $(x,y)$ in $S$ we have

$$
 F(x,b)\frac{F(a,y)}{F(a,b)}=\frac{F(x,b)F(a,y)}{F(a,b)}=\frac{f(x)g(b)f(a)g(y)}{f(a)f(b)}=f(x)g(y).
$$

This means that on $S$ we have

$$
 f(x)=F(x,b),\qquad g(y)=\frac{F(a,y)}{F(a,b)}.
$$

Since $F$ is continuous, we see that we can extend $f$ and $g$ continuously to the domain of $F$.

:::

::::::{prf:example} 
:label: Ex:DiffSep:SepCheck1
Consider the differential equation

$$
 \frac{dy}{dx}=e^{x+2y}.
$$

Even though this equation is not in the correct form yet, it is separable, since we can write

$$
 \frac{dy}{dx}=e^{x+2y}=e^xe^{2y}.
$$
::::::

::::::{prf:example} 
:label: Ex:DiffSep:SepCheck2
Consider the differential equation

$$
 y'=t+y.
$$

Although we clearly see a part that only depends on $t$ and a part that only depends on $y$, this equation is not separable. In order for it to be separable, the right-hand side of the equation needs to be a product of a part that only depends on $t$ and a part that only depends on $y$, while here we see a sum. We can manipulate this equation all we want, it is not possible to bring it into the correct form.

To be absolutely sure that it cannot be written in the correct form, we use {prf:ref}`Thm:DiffSep:CheckSep`. Writing $F(t,y)=t+y$, we see that

$$
 FF_{ty}-F_tF_y=(t+y)\cdot 0-1\cdot 1\neq 0,
$$

which means that the differential equation is not separable, as we suspected already.
::::::

Now the main question arises: how should we solve a separable differential equation? For this, we consider the separable differential equation

$$
 \frac{dy}{dx}=f(x)g(y).
$$

If $g(y)\neq0$, then this equation can be written as

$$
\frac{dy}{dx}=f(x)g(y)=\frac{f(x)}{h(y)},
$$

where

$$
 h(y)=\frac{1}{g(y)}.
$$

It is important to note that by assuming that $g(y)\neq 0$, we lose all the equilibrium solutions of the differential equations, as those satisfy $g(y)=0$. As such, the method that we use to solve separable equations does not, usually, allow you to find equilibrium solutions so we have to find these separately.

[^FootnoteJust]: If you are panicking slightly right now, do not worry; we will give a formal justification soon.

We have seen that $\dfrac{dy}{dx}$ is simply a notation for the derivative and should *not* be interpreted as a fraction. For now, let us pretend that we did not know this, and treat $\dfrac{dy}{dx}$ as an actual fraction. This means that we can bring all the terms that depend on $y$ to the left-hand side of the equation, and all the terms that depend on $x$, *including* $dx$, to the right-hand side of the equation.[^FootnoteJust] We then obtain.

$$
h(y)\,dy=f(x)\,dx.
$$

This way we have *separated* the differential equation, in the sense that the left-hand side of the equation only depends on $y$, while the right-hand side of the equation only depends on $x$. The next step suggest even more than the previous one that we have let go of all pretention of mathematical rigor: we place an integral symbol before both parts of the equation to obtain

$$
 \int h(y)\,dy=\int f(x)\,dx
$$

Fortunately, this resulting equation makes sense mathematically. The following theorem shows that, even though some steps in this derivation can feel a bit iffy, the resulting equation defines $y$ implicitly as a function of $x$, which means that we have obtained an implicit solution of the differential equation.

::::::{prf:theorem} 
:label: Thm:DiffSep:SepWorks
Consider the first-order separable differential equation 

$$
\frac{dy}{dx}=\frac{f(x)}{h(y)}.
$$

Then the equation

$$
 \int h(y)\,dy=\int f(x)\,dx
$$

implicitly defines $y$ as a differentiable function of $x$ on any interval $I$ with $h(x)\neq 0$ for all $x\in I$. In addition, this function $y$ satisfies the original differential equation. 
::::::

::::{admonition} Proof of {prf:ref}`Thm:DiffSep:SepWorks`
:class: dropdown, tudproof
Since the differential equation is separable, the functions $f$ and $h$ must be continuous. The further assumptions on $h$ precisely mean that all the conditions of {prf:ref}`Thm:SlopeCurves:IFT` are met, so $y$ is defined implicitly as a differentiable function of $x$.

Subsequently, we can use the chain rule to evaluate

$$
 f(x)=\frac{d}{dx}\left(\int f(x)\,dx\right)=\frac{d}{dx}\left(\int h(y)\,dy\right)=h(y)\frac{dy}{dx},
$$

which means that $y$ satisfies the differential equation

$$
 \frac{dy}{dx}=\frac{f(x)}{h(y)},
$$

as desired.
::::

With this, we can formulate an algorithm that can be used to solve separable differential equations.

::::::{prf:algorithm}
:label: Alg:DiffSep:SolvingAlgorithm

Consider the separable differential equation $\dfrac{dy}{dx}=f(x)g(y)$.

1. Find the equilibrium solutions by solving $g(y)=0$.
2. To find the remaining solutions, rewrite the equation into the form $\dfrac{dy}{dx}=\frac{f(x)}{h(y)}$.
3. Separate the variables by writing the differential equation as $h(y)\,dy=f(x)\,dx$.
4. Take the antiderivative of both sides of the equation $\displaystyle \int h(y)\,dy=\int f(x)\,dx$.
5. Write down the implicit form of the solution $H(y)=F(x)+C$. 
6. If possible, solve for $y$ to obtain an explicit solution $y(x)=H^{-1}\left(F(x)+C\right)$.
7. If applicable, use the initial condition to find the value of the arbitrary constant $C$.

::::::



::::::{prf:Example}
:label: Ex:DiffSep:yoverx
The differential equation $\displaystyle\frac{dy}{dx}=\frac{y}{x}$ with $x>0$ is separable, as it is of the form $\dfrac{dy}{dx}=f(x)g(y)$ with $f(x)=\dfrac{1}{x}$ and $g(y)=y$. We apply {prf:ref}`Alg:DiffSep:SolvingAlgorithm` to solve this differential equation. Note that $y=0$ is the only equilibrium solution. For $y\neq0$ we have

$$
\frac{1}{y}\,dy=\frac{1}{x}\,dx.
$$

We integrate both sides of the equation

$$
 \int\frac{1}{y}\,dy=\int\frac{1}{x}\,dx,
$$

which gives

$$
 \ln|y(x)|=\ln|x|+C.
$$

This is an implicit form of the solution. Note that it is not necessary to include a constant of integration on both sides of the equation as they can be combined into a single constant.

We take the exponential on both sides of the equation to obtain

$$
 |y(x)|=e^{\ln|y(x)|}=e^{\ln|x|+C}=|x|e^C=e^Cx,
$$

since we assumed that $x>0$. This means that $y(x)=e^Cx$ or $y(x)=-e^Cx$. Since $C$ is an arbitrary constant, $e^C$ can be any positive real number. This means that we can combine these two sets of solutions to see that $y(x)=Kx$ for $K\neq 0$ is a solution of the differential equation. 

Since $y=0$ is a solution as well (it is an equilibrium solution and we found it before separating the differential equation), this implies that the general solution is $y=Kx$ with $K\in\mathbb{R}$.
::::::

::::::{prf:Example}
:label: Ex:DiffSep:xy
The differential equation $\dfrac{dy}{dx}=2xy$ is separable. Note that $y=0$ is the only equilibrium solution. For $y\neq0$ we have:

$$
\frac{dy}{y}=2x\,dx.
$$

We integrate both sides of the equation

$$
 \int\frac{dy}{y}=\int2x\,dx,
$$

which gives

$$
 ln|y(x)|=x^2+C.
$$

Taking the exponential on both sides of the equation then gives

$$
 |y(x)|=e^{\ln|y(x)|}=e^{x^2+C}=e^Ce^{x^2}.
$$

As such, we find $y(x)=e^Ce^{x^2}$ or $y(x)=-e^Ce^{x^2}$. Since $e^C$ can be any positive real number, we obtain that $y(x)=Ke^{x^2}$ is a solution for all $K\neq 0$. Since $y=0$ is a solution too, this implies that the general solution is $y(x)=Ke^{x^2}$ with $K\in\mathbb{R}$.
::::::



::::::{prf:Example}
:label: Ex:DiffSep:xysq
The differential equation $\displaystyle\frac{dy}{dx}=2x(1+y^2)$ is separable. Note that it does not have any equilibrium solutions. We solve it by separating the variables which gives

$$
\frac{dy}{1+y^2}=2x\,dx.
$$

We then integrate both sides of the equation

$$
 \int\frac{dy}{1+y^2}=\int 2x\,dx,
$$

which gives

$$
 \arctan(y)=x^2+C.
$$

We can solve this equation for $y$ and we obtain

$$
y(x)=\tan(x^2+C)
$$

for $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
:label: Ex:DiffSep:xovery
Consider the initial-value problem

$$
 \frac{dy}{dx}=\frac{x}{y},\qquad y(0)=-2.
$$

This differential equation equation is separable. First we note that there are no $y\in\mathbb{R}$ such that $\dfrac{x}{y}=0$, which means that the differential equation does not have any equilibrium solutions. Next, we separate the variables to obtain

$$
y\,dy=x\,dx.
$$

We can now integrate both sides of the equation

$$
\int y\,dy=\int x\,dx,
$$

which gives

$$
 \frac{1}{2}y^2=\frac{1}{2}x^2+C.
$$



We can solve this equation for $y$ and we obtain

$$
 y=\sqrt{x^2+C},\qquad \text{or}\qquad y=-\sqrt{x^2+C}.
$$

Finally, we need to use the initial condition $y(0)=-2$. Since the initial value of $y$ is negative, we need to work with the negative square root. We then obtain

$$
 -2=y(0)=-\sqrt{0^2+C}=-\sqrt{C}.
$$

As such, we find $C=4$, which gives

$$
 y(x)=-\sqrt{x^2+4}.
$$

::::::

(SubSec:ODE1:SeparableAppl)=

## Applications

**Mixing problems**

A common application 

::::::{prf:example}
:label: Ex:ODE1:MixingProblemExample1
A tank contains $100\;\text{g}$ salt dissolved in $250\;\ell$ water. This solution is kept thoroughly mixed and drains from the tank at a rate of $5\;\ell/\text{min}$. Simultaneously, brine with a concentration of $10\;\text{g}/\ell$ enters the tank at the same rate of $5\;\ell/\text{min}$. After how many minutes is the amount of salt in the tank equal to $1300\;\text{g}$?
::::::

::::::{admonition} Solution
Let $y(t)$ denote the amount of salt (in 
) in the tank at time $t$ (in $\text{min}$). Then we have: $y(0)=100$ (initial condition) and $\displaystyle\frac{dy}{dt}=50−\frac{y}{50}$. This differential equation is separable. Note that 
 is a (constant) solution of this differential equation. For $y(t)\neq2500$ we have:

$$
\frac{dy}{dt}=\frac{2500-y}{50}\quad\Longleftrightarrow\quad\frac{dy}{2500-y}=\frac{dt}{50}.
$$

Integration now leads to

$$
\int\frac{dy}{2500-y}=\int\frac{dt}{50}\quad\Longleftrightarrow\quad-\ln|2500-y|=\frac{1}{50}t+C.
$$

This implies that

$$
2500-y(t)=\pm e^{-\frac{1}{50}t-C}=\pm e^{-C}\cdot e^{-\frac{1}{50}t}.
$$

Note that $\pm e^{-C}$ is an arbitrary positive or negative constant. If we replace this by an arbitrary constant $K$ we retrieve the "lost" constant solution $y(t)=2500$: $y(t)=2500-Ke^{-\frac{1}{50}t}$. Finally, the initial condition $y(0)=100$ leads to $K=2400$.

So the solution of the initial-value problem is $y(t)=2500-2400e^{-\frac{1}{50}t}$.

Now we are able to answer the question:

$$
y(t)=1300\quad\Longleftrightarrow\quad e^{-\frac{1}{5}t}=\tfrac{1}{2}\quad\Longleftrightarrow\quad t=50\ln(2),
$$

which implies that after $50\ln(2)\approx35$ minutes the amount of salt in the tank will be $1300\;\text{g}$. It is easy to check that

$$
y(50\ln(2))=2500-2400e^{-\ln(2)}=2500-1200=1300.
$$

::::::

::::::{prf:example}
:label: Ex:ODE1:MixingProblemExample2
A tank contains $100\;\ell$ beer with $5\%$ alcohol. Beer with $7\%$ alcohol is pumped into the tank at a rate of $1\;\ell/\text{min}$. The fluid in the tank is kept thoroughly mixed and drains from the tank at a rate of $1\;\ell/\text{min}$. What is the alcohol percentage of the beer in the tank after $1$ hour ($60$ minutes)?
::::::

::::::{admonition} Solution
Let $y(t)$ denote the amount of alcohol (in $\ell$) in the tank at time $t$ (in $\text{min}$). Then we have: $y(0)=5$ (initial condition) and $\displaystyle\frac{dy}{dt}=\frac{7}{100}-\frac{y}{100}$. This differential is separable. Note that $y(t)=7$ is a (constant) solution of this differential equation. For $y(t)\neq7$ we have:

$$
\frac{dy}{dt}=\frac{7-y}{100}\quad\Longleftrightarrow\quad\frac{dy}{7-y}=\frac{dt}{100}. 
$$

Integration now leads to

$$
\int\frac{dy}{7-y}=\int\frac{dt}{100}\quad\Longleftrightarrow\quad-\ln|7-y|=\frac{1}{100}t+C. 
$$

This implies that

$$
7-y(t)=\pm e^{-\frac{1}{100}t-C}=\pm e^{-C}\cdot e^{-\frac{1}{100}t}. 
$$

Note that $\pm e^{-C}$ is an arbitrary positive or negative constant. If we replace this by an arbitrary constant $K$ we retrieve the "lost" constant solution $y(t)=7$: $y(t)=7-Ke^{-\frac{1}{100}t}$. Finally, the initial condition $y(0)=5$ leads to $K=2$.

So the solution of the initial-value problem is $y(t)=7-2e^{-\frac{1}{100}t}$.

Now we obtain that $y(60)=7-2e^{-\frac{3}{5}}\approx5.9$. Since the volume of the fluid in the tank is $100\;\ell$, this is the alcohol percentage after $1$ hour.
::::::


### The logistic equation

In {prf:ref}`Ex:Diffclass:population` we studied the logistic differential equation 

$$
 \frac{dP}{dt}=kP\left(1-\frac{P}{M}\right).
$$

This differential equation is separable. Observe that $P(t)=0$ and $P(t)=M$ are two equilibrium solutions. For $P\neq0$ and $P\neq M$ we can separate the variables to obtain

$$
\frac{dP}{P\displaystyle\left(1-\frac{P}{M}\right)}=k\,dt.
$$

Integrating on both sides of the equation, we obtain

$$
 \int\frac{M}{P(M-P)}\,dP=\int k\,dt.
$$

Now we use the partial fraction decomposition (see {numref}`sec:PartialFractionDecomposition`) 

$$
 \frac{M}{P(M-P)}=\frac{1}{P}+\frac{1}{M-P}
$$

to find that

$$
\int\frac{M}{P(M-P)}\,dP=\int\left(\frac{1}{P}+\frac{1}{M-P}\right)\,dP=\ln|P|-\ln|M-P|+C.
$$

Hence, we have

$$
\ln\left|\frac{P}{M-P}\right|=kt+C,
$$

which gives

$$
 \frac{M-P}{P}=\pm e^{-C}\cdot e^{-kt}.
$$

Note that $\pm e^{-C}$ is an arbitrary positive or negative constant. If we replace this by an arbitrary constant $K$ we retrieve the "lost" constant solution $P=M$. So we find 

$$
 \frac{M-P}{P}=Ke^{-kt}
$$

for $K\in\mathbb{R}$. This is an implicit form of the solution. Solving for $P$ we obtain 

$$
 M-P=Ke^{-kt}P,
$$

which gives

$$
 P(t)=\frac{M}{1+Ke^{-kt}}.
$$

For an initial condition $P(0)=P_0>0$ we find that $K=\displaystyle\frac{M-P_0}{P_0}$. So we conclude that

$$
P(t)=\frac{M}{1+Ke^{-kt}}\quad\text{with}\quad K=\frac{M-P_0}{P_0}.
$$

### Newton's law of cooling

Newton's law of cooling states that the rate of cooling of an object is proportional to the temperature difference between the object and its surroundings, provided that this difference is not too large. Let $T(t)$ be the temperature of the object at time $t$, $T_s$ the temperature of the surroundings and $T_0$ the temperature of the object at time $t=0$. Since the rate of cooling is the derivative of the temperature with respect to time, this law can be written as

$$
\frac{dT}{dt}=-k(T-T_s),\quad T(0)=T_0,
$$

where $k>0$ is a proportionality constant. You might notice the minus sign in front of this $k$. Can you figure out why it is there?

:::{admonition} Click to see the solution
:class: tudproof, dropdown
The minus sign is there, since otherwise we obtain get some very unphysical behaviour. Indeed, with the minus sign, we see that $\dfrac{dT}{dT}<0$ when $T>T_s$, since we assumed $k>0$. This means the temperature of the object decreases if it is higher than the temperature of the surroundings, which is, of course, what we expect here. If the minus were not there, the object would heat up instead. A similar argument can be made for the situation where $T<T_s$.
:::

We note that the differential equation is separable and that $T(t)=T_s$ is the only equilibrium solution. For $T(t)\neq T_s$ we have

$$
\frac{dT}{T-T_s}=-k\,dt.T(t)-T_s=\pm e^C\cdot e^{kt}.
$$

We integrate both sides of the equation

$$
 \int \frac{dT}{T-T_s}=\int -k\,dt,
$$

which gives

$$
 \ln|T-T_s|=-kt+C.
$$

Taking the exponential on both sides of the equation, we obtain

$$
 |T-T_s|=e^{\ln|T-T_s|}=e^{-kt+C}=e^Ce^{-kt},
$$

which gives

$$
 T-T_s=\pm e^Ce^{-kt}.
$$

Since $T(t)=T_s$ is a solution too, we conclude that the general solution is 

$$
 T(t)-T_s=Ke^{-kt}
$$

with $K\in\mathbb{R}$. Now the initial condition $T(0)=T_0$ leads to $K=T_0-T_s$. Hence, we find

$$
 T(t)=T_s+(T_0-T_s)e^{kt}.
$$

::::::{prf:example}
:label: Ex:DiffSep:cooling
A bottle of soda pop with a temperature of $20^{\circ}\;\text{C}$ is placed in a refrigerator where the temperature is $5^{\circ}\;\text{C}$. Suppose that after half an hour the soda pop has cooled to $15^{\circ}\;\text{C}$. Then we can ask, for instance, the following questions:

1) What is the temperature of the soda pop after one hour?

2) How long does it take for the soda pop to cool to $10^{\circ}\;\text{C}$?

To answer these question, we first note that $T_s=5$ and $T(0)=20$ here. So we have

$$
\frac{dT}{dt}=-k(T-5),\quad T(0)=20. 
$$

Using the general solution above, we obtain

$$
 T(t)=5+15e^{-kt}.
$$

Assuming that the time $t$ is measured in minutes, we can express the fact that it took half an hour for the soda pop to be cooled to $15^{\circ}\;\text{C}$ as the condition $T(30)=15$. Plugging in this condition gives

$$
15=5+15e^{-30k},
$$

from which we obtain

$$
 -30k=\ln\left(\frac{10}{15}\right)=\ln\left(\frac{2}{3}\right).
$$

This implies that 

$$
 k=-\frac{1}{30}\ln\left(\frac{2}{3}\right)\approx0.0135.
$$


Then we can answer question (1), since we find

$$
 T(60)= 5+15e^{\frac{1}{30}\ln\left(\frac{2}{3}\right)\cdot60}\approx11.7^{\circ}\;\text{C}.
$$

So, the temperatue of the soda pop after one hour is approximately $11.7^{\circ}\;\text{C}$.

In order to answer the second question, we need to find $t$ for which we have $T(t)=10$. This means that we need to solve

$$
 10=5+15e^{−kt},
$$

which gives

$$
 −kt=\ln\left(\frac{5}{15}\right)=\ln\left(\frac{1}{3}\right).
$$


This implies that it takes approximately $\displaystyle\frac{\ln\left(\frac{1}{3}\right)}{−k}\approx81.4$ minutes for the soda pop to cool to $10^{\circ}\;\text{C}$.
::::::

%::::::{prf:example}
%A cup of coffee with a temperature of $95^{\circ}\;\text{C}$ is placed in a room where the temperature is $20^{\circ}\;\text{C}$. After $10$ minutes the coffee has cooled to $75^{\circ}\;%\text{C}$.

%1) What is the temperature of the coffee after $15$ minutes?

%2) How long does it take for the coffee to cool to $80^{\circ}\;\text{C}$?
%::::::

%::::::{admonition} Solution
%Note that $T_s=20$ and $T(0)=95$ here. So we have:

%$$
%\frac{dT}{dt}=k(T-20),\quad T(0)=95\quad\Longrightarrow\quad T(t)=20+75e^{kt}.
%$$

%Note that

%$$
%T(10)=75\;\Longleftrightarrow\;75=20+75e^{10k}\;\Longleftrightarrow\;10k=\ln\left(\frac{55}{75}\right)=\ln\left(\frac{11}{15}\right).
%$$

%This implies that $k=\frac{1}{10}\ln\left(\frac{11}{15}\right)\approx−0.031$. Then we have:

%1) $T(15)=20+75e^{−0.031\cdot15}\approx67^{\circ}\;\text{C}$.

%So, the temperature of the coffee after $15$ minutes is approximately $67^{\circ}\;\text{C}$.

%2) $T(t)=80\;\Longleftrightarrow\;80=20+75e^{−0.031t}\;\Longleftrightarrow\;−0.031t=\ln\left(\frac{60}{75}\right)=\ln\left(\frac{4}{5}\right)$.

%This implies that it takes approximately $\displaystyle\frac{\ln\left(\frac{4}{5}\right)}{−0.031}\approx7.2$ minutes for the coffee to cool to $80^{\circ}\;\text{C}$.
%::::::

### Torricelli's law

```{figure} Images/torricelli.png
---
width: 50%
name: Fig:DiffSep:Torricelli
align: right
---
```
Torricelli's law, also known as Torricelli's theorem, is a theorem in fluid dynamics relating the speed of fluid flowing out of an orifice to the height of the fluid above the hole. The law states that the speed of efflux $v$ of a fluid through a sharp-edged hole at the bottom of a tank filled to a depth $h$ is the same as the speed that a body (in this case a drop of water) would acquire in falling freely from a height $h$, i.e. $v=\sqrt{2gh}$, where $g$ is the acceleration due to gravity ($9.81\;\text{m}/\text{s}^2$ near the surface of the earth).

Now consider a cylindrical tank that has a hole with area $a$ in its bottom (see {numref}`Fig:DiffSep:Torricelli`) and assume that water is draining from the hole. If $V(t)$ denotes the volume of the water at time $t$, then Torricelli's law leads to

$$
\frac{dV}{dt}=-a\sqrt{2gh}.
$$

If the cross-sectional area of the tank is $A$, then we have:

$$
A\frac{dh}{dt}=-a\sqrt{2gh}.
$$

Note that this differential equation is only valid when $h\geq 0$, since otherwise we would be taking the square root of a negative number (and we would be in the unphysical situation where the water level in the tank is negative). We also observe that this is a separable differential equation, we we should be able to solve it. Let us consider a more concrete situation to work out the solution.


::::::{prf:Example}
:label: Ex:DiffSep:torricelli
Consider the tank from {numref}`Fig:DiffSep:Torricelli`. Suppose that the radius of the tank is $10\;\text{cm}$, the radius of the hole is $1\;\text{cm}$ and the initial height of the water is $10\;\text{cm}$. This means that the physical quantities in the differential equation are given by

$$
A=100\pi\;\text{cm}^3,\quad a=\pi\;\text{cm}^3\quad\text{and}\quad h=10\;\text{cm}.
$$

In particular, we are dealing with the initial-value problem

$$
100\frac{dh}{dt}=-\sqrt{2gh},\quad h(0)=10.
$$

Let us see if we can figure out how long does it take for the water to drain completely.



Note that $h(t)=0$ is the only equilibrium solution of the differential equation. For $h(t)\neq0$ we can separate the variables to obtain

$$
100\frac{dh}{\sqrt{h}}=-\sqrt{2g}\,dt, 
$$

which after integrating both sides of the equation gives

$$
 200\sqrt{h}=-\sqrt{2g}t+C.
$$

The initial condition $h(0)=10$ leads to $C=200\sqrt{10}$. This implies that the solution can be written as

$$
h(t)=\left(\frac{200\sqrt{10}-\sqrt{2g}t}{200}\right)^2.
$$

Now we can determine when the taking is empty. Solving the equation $h(t)=0$ gives $t=\displaystyle\frac{200\sqrt{10}}{\sqrt{2g}}$. This implies that the tank will be empy after $\displaystyle\frac{200\sqrt{10}}{\sqrt{2g}}\approx14.3$ seconds.

What happens after the the moment the tank is empty? Physically speaking, that is a silly question: the tank will obviously stay empty. However, the function $h(t)$ above is defined for all $t$ and if we plot this function, we see that $h$ starts increasing again after hitting $0$. So that would mean that the tank would fill up again, which is nonsensical. So what is wrong here? A first guess might be that it has to do with the fact that the differential equation is only defined for $h\geq 0$. That is not (directly at least) the issue here, as this particular function $h$ has $h(t)\geq 0$ for all $t$. Can you come up with the actual reason?

:::{admonition} Click to see the solution
:class: tudproof, dropdown
We introduced this problem ourselves by squaring the implicit solution $200\sqrt{h}=-\sqrt{2g}t+200\sqrt{10}$. Since $200\sqrt{h}$ can never be negative, this implicit solution is only valid when 

$$
 -\sqrt{2g}t+200\sqrt{10}\geq0,
$$

i.e. when

$$
 t\leq \frac{200\sqrt{10}}{\sqrt{2g}}.
$$

That is, the implicit solution is only valid as long as the tank is non-empty and stops being valid afterwards. 

:::

From a physical point of view, we find that the solution must be

$$
 h(t)=\begin{cases} \left(\frac{200\sqrt{10}-\sqrt{2g}t}{200}\right)^2,\qquad &t\leq \frac{200\sqrt{10}}{\sqrt{2g}};\\ 0,\qquad &t>\frac{200\sqrt{10}}{\sqrt{2g}}.\end{cases}
$$

Let us check that this function is, mathematically speaking, also the solution of the initial-value problem. By construction, it satisfies the differential equation when $t<\frac{200\sqrt{10}}{\sqrt{2g}}$. It also satisfies the initial condition. Since $0$ is an equilibrium solution, it satisfies the differential equation for $t>\frac{200\sqrt{10}}{\sqrt{2g}}$. So we only need to check the behaviour at $t=\frac{200\sqrt{10}}{\sqrt{2g}}$. We note that for $t<\frac{200\sqrt{10}}{\sqrt{2g}}$ we have

$$
 h'(t)=-\frac{1}{100}\sqrt{2gh(t)},
$$

which approaches $0$ as $t$ approaches $\frac{200\sqrt{10}}{\sqrt{2g}}$. For $t>\frac{200\sqrt{10}}{\sqrt{2g}}$, we have $h'(t)=0$ which also approaches $0$ as $t$ approaches $\frac{200\sqrt{10}}{\sqrt{2g}}$. As such, we find

$$
 h'\left(\frac{200\sqrt{10}}{\sqrt{2g}}\right)=0.
$$

Since we know that

$$
 -\frac{1}{100}\sqrt{2gh\left(\frac{200\sqrt{10}}{\sqrt{2g}}\right)}=0,
$$

we find that $h$ also satisfies the differential equation at the moment the tank empties. So this function $h$ is the solution of the differential equation we are looking for.
::::::


### Orthogonality of families of curves

We know from {prf:ref}`Thm:Differentiability:Orthot` that the graphs of two functions that intersect in a certain point are orthogonal precisely when the product of their derivatives is $-1$. We can use this fact to find a curve that is orthogonal to a given family of curves. For this, we will need to solve a separable differential equation.

::::::{prf:Example}
:label: Ex:DiffSep:orthogonal

::::::

### A family of improper integrals

The following example shows that seemingly unrelated mathematical problems can sometimes be reduced to solving a differential equation.

::::::{prf:Example}
:label: Ex:DiffSep:improper
For each $t\in\mathbb{R}$ we consider the improper integral

$$
 I(t)=\displaystyle\int_0^{\infty}e^{-x^2}\cos(xt)\,dx.
$$

It is rather hard to solve these integrals by hand, but we will show that $I(t)$ satisfies a differential equation.

First we note that we obtain from {prf:ref}`Ex:MultivariableIntegration:PolarApplicationsExample2` that

$$ 
 I(0)=\displaystyle\int_0^{\infty}e^{-x^2}\,dx=\tfrac{1}{2}\sqrt{\pi}.
$$

In addition, since we integrate over $x$ we can differentiate the integral with respect to $t$ and bring this derivative inside to obtain

$$
 I'(t)=-\int_0^{\infty}xe^{-x^2}\sin(xt)\,dx.
$$


We now use integration by parts to obtain

\begin{align*}
 I'(t)$=-\int_0^{\infty}xe^{-x^2}\sin(xt)\,dx\\
 &=\bigg[\frac{1}{2}e^{-x^2}\sin(xt)\bigg]_0^{\infty}-\frac{1}{2}\int_0^{\infty}e^{-x^2}t\cos(xt)\,dx\\
 &=0-\frac{1}{2}t\int_0^{\infty}e^{-x^2}\cos(xt)\,dx\\
 &=-\frac{1}{2}tI(t).
\end{align*}

As such, the function $I(t)$ satisfies the differential equation

$$
 I'(t)=-\frac{1}{2}tI(t).
$$

This is a separable differential equation with general solution $I(t)=Ce^{-\frac{1}{4}t^2}$. We now use that we know $I(0)=\frac{1}{2}\sqrt{\pi}$ to find $C$. We obtain 

$$
 \frac{1}{2}\sqrt{\pi}=I(0)=Ce^0=C.
$$

We conclude that $I(t)=\frac{1}{2}\sqrt{\pi}e^{-\frac{1}{4}t^2}$.
::::::

## Grasple exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8ef26791-6d07-4dc6-b31a-d23b4a8edafa?id=75340
:label: Grasple:75340
:dropdown:
:description: Is the differential equation separable or not?
::::::


::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3ac90b56-b25d-4bbc-8d0b-326ddfd7efa5?id=63873
:label: Grasple:63873
:dropdown:
:description: Find an implicit equation for the solution of a differential equation.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/decc0087-6a85-40e2-b92b-37829a582615?id=116697
:label: Grasple:116697
:dropdown:
:description: Find an implicit equation for the solution of a differential equation.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/27da33fb-d9a8-4ece-b760-b0181caee606?id=116695
:label: Grasple:116695
:dropdown:
:description: Find an implicit equation for the solution of a differential equation.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d551cdba-18f9-4b36-9c74-b4e8aa299301?id=63857
:label: Grasple:63857
:dropdown:
:description: Find the general solution of a differential equation.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2a6b33b7-0782-4b83-af1c-b3775eba9088?id=63901
:label: Grasple:63901
:dropdown:
:description: Find the general solution of a differential equation and check influence of parameters.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d12048c1-c31a-4d1d-9c84-9f4418258819?id=63869
:label: Grasple:63869
:dropdown:
:description: Find an implicit equation for the solution of an initial-value problem.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5f064275-7dec-45f6-b5b7-da5790682345?id=63892
:label: Grasple:63892
:dropdown:
:description: Find an implicit equation for the solution of an initial-value problem.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e6a2f44c-e1c5-4f22-aa26-f53f16cbb4bd?id=63896
:label: Grasple:63896
:dropdown:
:description: Solve the initial-value problem.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/15504676-92b6-4d0c-b681-d724fc4cffb6?id=63894
:label: Grasple:63894
:dropdown:
:description: Solve the initial-value problem.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c810a536-88bf-459c-88bc-fb4d7602a0df?id=63867
:label: Grasple:63867
:dropdown:
:description: Solve the initial-value problem.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/21af550c-dd42-4fa8-b12e-70d7cd08b616?id=63866
:label: Grasple:63866
:dropdown:
:description: Solve the initial-value problem.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e8c3ea19-6c17-4bf8-bdb8-6ac722d65411?id=78843
:label: Grasple:78843
:dropdown:
:description: Solve the initial-value problem.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/20968844-29ce-4bcc-b753-137fa62fe80f?id=63909
:label: Grasple:63909
:dropdown:
:description: Solve the initial-value problem.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6473b06b-91a4-441b-be93-f8ad539b1ca4?id=63871
:label: Grasple:63871
:dropdown:
:description: Solve the initial-value problem.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/36832dfa-9660-4c93-9bea-edb1493e9079?id=63876
:label: Grasple:63876
:dropdown:
:description: Solve the initial-value problem.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c9173f0f-2942-4850-ac7c-3fc9eb33d38c?id=116703
:label: Grasple:116703
:dropdown:
:description: Solve the initial-value problem.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/86ded33d-618b-4b70-845a-fb8bdd34153d?id=78877
:label: Grasple:78877
:dropdown:
:description: Find a curve orthogonal to a family of curves.
::::::


::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/eb39547d-1f15-4685-8f0d-2c09777965f9?id=63863
:label: Grasple:63863
:dropdown:
:description: Application: a mixing problem
::::::


::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b041f047-91d9-460f-afd2-f2a379434eb4?id=63860
:label: Grasple:63860
:dropdown:
:description: Application: a mixing problem
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/697ea999-d14b-4a5d-a2dc-c2f276bbf99c?id=63858
:label: Grasple:63858
:dropdown:
:description: Application: Newton's law of cooling
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d62ee61a-85a4-48a9-a1a2-4dadcf47a52d?id=63895
:label: Grasple:63895
:dropdown:
:description: Application: Newton's law of cooling
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6928adcc-1906-4c45-8484-04dc0f3d0d3d?id=63882
:label: Grasple:63882
:dropdown:
:description: Application: Torricelli's law
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/12cc3b35-01b3-4110-9601-544025150187?id=78875
:label: Grasple:78875
:dropdown:
:description: Application: Chemical reaction
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a5da4212-f724-4786-a164-fba1b17c898b?id=78933
:label: Grasple:78933
:dropdown:
:description: Application: Chemical reaction
::::::


::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6fed8a5e-0676-4618-aa97-4a755b9b307b?id=78845
:label: Grasple:78845
:dropdown:
:description: Application: Channels in cell membrane
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9b62831e-6f13-41a5-8ff6-53c170efb005?id=78889
:label: Grasple:78889
:dropdown:
:description: Application: Logistic equation
::::::
