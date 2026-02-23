# Second-order linear ordinary differential equations
In this chapter: Under Construction

```{tableofcontents}
```

In this chapter we will only consider linear differential equations. A second-order **linear** differential equation has the form
```{math}
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)=G(x),
```
where $P$, $Q$, $R$ and $G$ are continuous functions with $P(x)\neq0$. Such a differential equation is called **homogeneous** if $G(x)\equiv0$ and **nonhomogeneous** if $G(x)\not\equiv0$.

So, a homogeneous second-order linear differential equation has the form
```{math}
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)=0,
```
where $P$, $Q$ and $R$ are continuous functions with $P(x)\neq0$. Then we have:

::::::{prf:theorem}
If $y_1(x)$ and $y_2(x)$ are both solutions, then $y(x)=c_1y_1(x)+c_2y_2(x)$ is also a solution for each $c_1,c_2\in\mathbb{R}$.
::::::

::::::{prf:proof}
Since $y_1(x)$ and $y_2(x)$ are both solutions, we have
```{math}
P(x)y_1''(x)+Q(x)y_1'(x)+R(x)y_1(x)=0\quad\text{and}\quad P(x)y_2''(x)+Q(x)y_2'(x)+R(x)y_2(x)=0.
``` 
Let $y(x)=c_1y_1(x)+c_2y_2(x)$, then we have
```{math}
\begin{align*}
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)&=P(x)\left[c_1y_1''(x)+c_2y_2''(x)\right]+Q(x)\left[c_1y_1'(x)+c_2y_2'(x)\right]+R(x)\left[c_1y_1(x)+c_2y_2(x)\right]\\
&=c_1\left[P(x)y_1''(x)+Q(x)y_1'(x)+R(x)y_1(x)\right]+c_2\left[P(x)y_2''(x)+Q(x)y_2'(x)+R(x)y_2(x)\right]\\
&=c_1\cdot0+c_2\cdot0=0.
\end{align*}
```
::::::

::::::{prf:definition}
Two functions $f(x)$ and $g(x)$ are called **linearly independent** on an interval $I$ if 
```{math}
c_1f(x)+c_2g(x)=0\quad\text{for all}\quad x\in I
```
implies that $c_1=0$ and $c_2=0$.
::::::

::::::{prf:example}
The functions $x$ and $x^2$ are linearly independent on the interval $[0,1]$, since
```{math}
c_1x+c_2x^2=0
```
leads to $c_1+c_2=0$ if $x=1$ and to $\frac{1}{2}c_1+\frac{1}{4}c_2=0$ if $x=\frac{1}{2}$. This implies that $c_1=0$ and $c_2=0$.
::::::

::::::{prf:example}
The functions $e^{-2x}$ and $e^{3x}$ are linearly independent on $\mathbb{R}$, since
```{math}
c_1e^{-2x}+c_2e^{3x}=0
```
leads to $c_1+c_2=0$ if $x=0$ and to $e^{-2}c_1+e^{3}c_2=0$ if $x=1$. This implies that $c_1=0$ and $c_2=0$.
::::::

::::::{prf:example}
The functions $\cos(x)$ and $\sin(x)$ are linearly independent on $\mathbb{R}$, since
```{math}
c_1\cos(x)+c_2\sin(x)=0
```
leads to $c_1=0$ if $x=0$ and to $c_2=0$ if $x=\frac{1}{2}\pi$.
::::::

::::::{prf:theorem}
If $y_1(x)$ and $y_2(x)$ are linearly independent solutions on an interval, and $P(x)$ is never $0$
there, then the general solution is given by $y(x)=c_1y_1(x)+c_2y_2(x)$, where $c_1$ and $c_2$ are arbitrary constants.
 ::::::

A nonhomogeneous second-order linear differential equation has the form
```{math}
P(x)y''(x)+Q(x)y'(x)+R(x)y(x)=G(x),
```
where $P$, $Q$, $R$ and $G$ are continuous functions with $P(x)\neq0$ and $G(x)\not\equiv0$. Then we have:

::::::{prf:theorem}
If $y_p(x)$ is a particular solution and $y_h(x)$ is the general solution of the corresponding homogeneous (also called: *complementary*) differential equation (with $G(x)$ replaced by $0$), then $y(x)=y_p(x)+y_h(x)$ is the general solution.
::::::

## (Grasple) exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c83c4815-8d8c-4a1d-bade-f720cf165406?id=79453
:label: grasple_exercise_13_0_1
:dropdown:
:description: Are two functions linearly independent?
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fa7c4299-9811-428f-80dc-ee1ad8503e6c?id=79449
:label: grasple_exercise_13_0_2
:dropdown:
:description: Is the differential equation homogeneous or not?
::::::