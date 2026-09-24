# First-order autonomous differential equations

In this section we cover:

- autonomous first-order differential equations:
    - Autonomous equations
    - Stability by y'vs y plots



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

## Grasple exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d2b9bcae-7518-4872-bd04-6c0fce3b1707?id=116490
:label: Grasple:116490
:dropdown:
:description: Stability of equilibrium solutions
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/84c87c47-56a2-4f48-a2e9-e0893950345c?id=63920
:label: Grasple:63920
:dropdown:
:description: Stability of equilibrium solutions
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bf483631-d9e0-4885-8f68-c6ee8812d13f?id=78880
:label: Grasple:78880
:dropdown:
:description: Stability of equilibrium solutions
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3643c628-6d6a-409a-a87f-1a08d6967940?id=78912
:label: Grasple:78912
:dropdown:
:description: Stability of equilibrium solutions
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7c02fc09-6ec1-4565-8f04-c04ccce910e5?id=63916
:label: Grasple:63916
:dropdown:
:description: Application: Gompertz equation
::::::