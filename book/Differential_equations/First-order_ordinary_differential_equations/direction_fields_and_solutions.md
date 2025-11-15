# Direction fields and solutions

In this section we cover:

- Definition of solutions, including general solution
- Educated guess for solutions
- Superposition principle for linear differential equations
- Optional: existence and uniqueness theorem
- Direction fields

Not every first-order differential equation can be solved easily. However, in many cases there is no need for a *quantitive* solution. A *qualtitive* solution might suffice. For instance, we might look at a so-called **direction field**.

For a differential equation of the form $\dfrac{dy}{dx}=F(x,y)$ we might consider points $(x,y)$ where the right-hand side $F(x,y)$ exists. This gives rise to a value for the derivative $\dfrac{dy}{dx}$ of the unknown function $y(x)$ at this point $(x,y)$. This indicates the *slope* of the graph of a solution $y=y(x)$. This leads to a **direction field** (or **slope field**) of the differential equation.

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