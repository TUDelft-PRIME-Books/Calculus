# First-order ordinary differential equations
In this chapter: Under Construction

```{tableofcontents}
```

In this chapter and the next one we will study differential equations.

::::::{prf:Definition}
A **differential equation** is an equation involving an unknown function and one or more of its derivatives. The order of the highest derivative involved is called the **order** of the differential equation.
::::::

In this chapter we only consider **first-order** differential equations of the form $\dfrac{dy}{dx}=F(x,y)$ with $y=y(x)$.

The variable $x$ is called an independent variable, while $y=y(x)$ is called a dependent variable.

A function $f(x)$ is called a **solution** of the differential equation if the equation is satisfied by $y=f(x)$, so if $f'(x)=F(x,f(x))$.

When we are asked to *solve* a differential equation, we are expected to find all possible solutions. However, in general it is not easy to solve a differential equation. There is no systematic approach that enables us to solve differential equations. Only when a differential equation has a specific form, we might have some techniques to find the general solution.

However, in many cases we are not interested in finding all solutions (the *general solution*) as in finding a specific solution that also satisfies some additional requirement. In many physical problems, we need to find a particular solution that also satisfies a condition of the form $y(t_0)=y_0$. This is called an **initial condition**. The problem of finding a solution of a first-order differential equation that also satisfies such an initial condition is called an **initial-value problem**.

**Population growth**

One model for the growth of a population is based on the assumption that the population grows at a rate proportional to the size of the population.

That is a reasonable assumption for a population of bacteria or animals under ideal conditions (unlimited environment, adequate nutrition, absence of predators, immunity of disease).

If $P(t)$ denotes the number of individuals in a population at time $t$, then: $\dfrac{dP}{dt}=kP$, where $k$ denotes the growth rate. This is called *exponential growth*, since the general solution is $P(t)=Ce^{kt}$ with $C\in\mathbb{R}$.

A more realistic model is $\displaystyle\frac{dP}{dt}=kP\left(1-\frac{P}{M}\right)$. This is called a *logistic differential equation*.

This differential equation was proposed by the Belgian mathematician Pierre-François Verhulst in 1838 as a model for world population growth.

This more realistic model reflects the fact that a given environment has limited resources. Many populations start by increasing in an exponential manner, but the population levels off when it approaches its *carrying capacity* $M$ (or decreases toward $M$ if it ever exceeds $M$).

Instead of *solving* differential equations of the form $\dfrac{dy}{dx}=F(x,y)$ it is possible to consider direction fields.