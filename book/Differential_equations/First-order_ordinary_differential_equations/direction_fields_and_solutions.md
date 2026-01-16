# Direction fields and solutions

In this section we cover:

- autonomous first-order differential equations:
    - Autonomous equations
    - Stability by y'vs y plots
- slope fields
- equilibrium solutions in slope fields
- Educated guess for solutions (not Euler!)
- Logistic equation

## Slope fields

Not every first-order differential equation can be solved easily. However, in many cases there is no need for a *quantitive* solution. A *qualtitive* solution might suffice. For instance, we might look at a so-called **slope field** (or **direction field**).

For a differential equation of the form $\dfrac{dy}{dx}=F(x,y)$ we might consider points $(x,y)$ where the right-hand side $F(x,y)$ exists. This gives rise to a value for the derivative $\dfrac{dy}{dx}$ of the unknown function $y(x)$ at this point $(x,y)$. This indicates the *slope* of the graph of a solution $y=y(x)$. This leads to a **slope field** of the differential equation.

::::::{prf:example}
Consider the differential equation $\dfrac{dy}{dx}=x+y$ and the initial-value $y(0)=1$.

```{figure} Images/direction1.png
---
width: 50%
name: direction field
align: left
---
```
```{figure} Images/direction2.png
---
width: 50%
name: direction field
align: right
---
```

Following the line segments in the direction field, we can sketch the graph of the solution that satisfies the initial condition $y(0)=1$.
::::::

::::::{prf:example}
Consider the differential equation $\dfrac{dy}{dx}=x^2+y^2-1$ and the initial-value $y(0)=0$.

```{figure} Images/direction3.png
---
width: 50%
name: direction field
align: left
---
```
```{figure} Images/direction4.png
---
width: 50%
name: direction field
align: right
---
```
::::::

::::::{prf:example}
Consider the differential equation $\dfrac{dy}{dx}=x^2+y^2-1$ and the initial-value $y(0)=k$ with $k\in\{-2,-1,0,1,2\}$.

```{figure} Images/direction5.png
---
width: 50%
name: direction field
align: left
---
```
```{figure} Images/direction6.png
---
width: 50%
name: direction field
align: right
---
```
::::::

## Autonomous differential equations

We consider differential equations of the form

$$
y'=f(y),
$$

where $f(y)$ denotes a function of the dependent variable $y$ only. So, it does not explicitly depend on the independent variable. Then, every solution of

$$
f(y)=0
$$

is called an **equilibrium solution** since then $y'=0$ as well. For other values of $y$ the function $f(y)$ is either positive or negative, which implies that $y'$ is either positive or negative. When $y'$ is positive, the solution $y$ increases. And when $y'$ is negative, the solution $y$ decreases.

::::::{prf:example}
Consider the autonomous differential equation

$$
\frac{dy}{dt}=y^3(4-y).
$$

Then $y(t)=0$ and $y(t)=4$ are the only equilibrium solutions. For $y<0$ the function $f(y)=y^3(4-y)$ is negative, for $0<y<4$ we have $f(y)>0$ and for $y>4$ we have $f(y)<0$. This leads to

```{figure} Images/autonomous.png
---
width: 75%
name: autonomous differential equation
align: center
---
```

We conclude that the equilibrium solution $y(t)=0$ is **unstable** and that the equilibrium solution is **stable**. 
::::::

In {numref}`Sec:DE:Intro` we mentioned the *logistic equation* as an example of an autonomous differential equation. In {numref}`Sec:ODE1:Separable` we will solve this differential equation.
