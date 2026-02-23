(Sec:ODE1:Linear)=

# First-order linear differential equations

In this section we cover:

- standard form
- Integrating factor
- Solving linear first order differential equations
- Mention name Bernoulli equations
- Link with separable equations, same example?

Another specific form of a differential equation for which we have a method for solving is a *linear* differential equation.

::::::{prf:Definition}
A first-order differential equation is called **linear** if it can be written in the form:

$$
\frac{dy}{dx}+P(x)y=Q(x),
$$

where $P(x)$ and $Q(x)$ are continuous functions on any interval.
::::::

We consider two methods to solve this kind of differential equations: using an *integrating factor* and the method of *variation of the parameter*.

Using an **integrating factor**:

If we multiply the differential equation (in standard form) by a factor $I(x)\neq0$, then the solutions remain the same. We try to find such a factor $I(x)$ such that

$$
I(x)y'(x)+I(x)P(x)y(x)=I(x)Q(x)
$$

implies that

$$
\frac{d}{dx}\left(I(x)y(x)\right)=I(x)Q(x).
$$

Then we must have that: $I'(x)=I(x)P(x)$. Such a factor $I(x)$ is called an integrating factor because then we can integrate:

$$
I(x)y(x)=\int I(x)Q(x)\,dx.
$$

And since $I(x)\neq0$ this leads to the solution: $y(x)=\displaystyle\frac{1}{I(x)}\int I(x)Q(x)\,dx$.
In order to find such an integrating factor $I(x)\neq0$ we have to solve the differential equation

$$
I'(x)=I(x)P(x).
$$

However, this is a separable differential equation. Note that $I(x)=\exp\left(\displaystyle\int P(x)\,dx\right)$ is a solution, where $\displaystyle\int P(x)\,dx$ denotes any antiderivative of $P(x)$.

This leads to the following 'recipe':

* Write the differential equation in the standard form $\displaystyle\frac{dy}{dx}+P(x)y=Q(x)$.

* Find an (arbitrary) *integrating factor* $I(x)\neq0$ such that $I'(x)=I(x)P(x)$.

* Multiply the differential equation in *standard form* by $I(x)$:

$$
\underbrace{I(x)y'(x)+I(x)P(x)y(x)}_{\displaystyle\left(I(x)y(x)\right)'}=I(x)Q(x). 
$$
 
* Integrate both sides of this equation: $I(x)y(x)=\displaystyle\int I(x)Q(x)\,dx$.

* Divide by $I(x)\neq0$: $y(x)=\displaystyle\frac{1}{I(x)}\int I(x)Q(x)\,dx$.

**Examples**

::::::{prf:Example}
Consider the differential equation $y'+2y=3$. 

This has $I(x)=e^{2x}\neq0$ as an integrating factor (since $I'(x)=2I(x)$). Hence: 

$$
y'+2y=3\quad\Longleftrightarrow\quad(e^{2x}y(x))'=3e^{2x}.
$$ 

This implies that $e^{2x}y(x)=\displaystyle\int 3e^{2x}\,dx=\tfrac{3}{2}e^{2x}+C$ with $C$ an arbitrary (integration) constant. Hence: $y(x)=\frac{3}{2}+Ce^{-2x}$ with $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
Consider the differential equation $y'-2xy=4x$. 

This has $I(x)=e^{-x^2}\neq0$ as an integrating factor (since $I'(x)=-2xI(x)$). Hence: 

$$
y'-2xy=4x\quad\Longleftrightarrow\quad(e^{-x^2}y(x))'=4xe^{-x^2}.
$$ 

This implies that $e^{-x^2}y(x)=\displaystyle\int 4xe^{-x^2}\,dx=-2e^{-x^2}+C$ with $C$ an arbitrary (integration) constant. Hence: $y(x)=-2+Ce^{x^2}$ with $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
The differential equation $xy'+y=1$ with $x>0$ is not in *standard form*. So, first we write it as $y'+\displaystyle\frac{1}{x}y=\frac{1}{x}$ and then note that $I(x)=e^{\ln(x)}=x>0$ is an integrating factor (since $I'(x)=\displaystyle\frac{1}{x}I(x)$). Then we have: 

$$
xy'+y=1\quad\Longrightarrow\quad(xy(x))'=1
$$

and therefore $xy(x)=x+C$ with $C$ an arbitrary (integration) constant. Hence: $y(x)=\displaystyle\frac{x+C}{x}=1+\frac{C}{x}$ with $C\in\mathbb{R}$.
::::::

We might also use **variation of the parameter**:

First consider the corresponding homogeneous differential equation (also in *standard form* with 
$Q(x)$ replaced by $0$):

$$
\frac{dy}{dx}+P(x)y=0.
$$

This differential equation is separable, since for $y\neq0$ it can be written in the form

$$
\frac{dy}{y}=-P(x)\,dx\quad\Longrightarrow\quad\ln|y(x)|=-\int P(x)\,dx.
$$

This leads to a general solution of the form $y(x)=C\exp\left(-\displaystyle\int P(x)\,dx\right)$ with $C$ an arbitrary (integration) constant.

Now we replace this constant by a function of $x$, say $u(x)$, then substitution into the inhomogeneous differential equation implies:

$$
\begin{align*}
&u'(x)\exp\left(-\int P(x)\,dx\right)-P(x)u(x)\exp\left(-\int P(x)\,dx\right)\\
&{}\quad{}+P(x)u(x)\exp\left(-\int P(x)\,dx\right)=Q(x)\\
&{}\hspace{25mm}\Longleftrightarrow\quad u'(x)=Q(x)\exp\left(\int P(x)\,dx\right).
\end{align*}
$$

Integration then leads to $u(x)$ including an arbitrary (integration) constant. Substitution into 
$y(x)=u(x)\left(-\displaystyle\int P(x)\,dx\right)$ then gives the general solution.

::::::{prf:Example}
Consider the differential equation $y'+2y=3$. 

Now we first consider the homogeneous equation $y'+2y=0$ with general solution $y(x)=Ce^{-2x}$. 

Then we substitute $y(x)=u(x)e^{-2x}$ into the original inhomogeneous equation:

$$
\begin{align*}
u'(x)e^{-2x}-2u(x)e^{-2x}+2u(x)e^{-2x}=3&\quad\Longrightarrow\quad u'(x)=3e^{2x}\\
&\quad\Longrightarrow\quad u(x)=\tfrac{3}{2}e^{2x}+C.
\end{align*}
$$

So, the general solution is: $y(x)=u(x)e^{-2x}=\frac{3}{2}+Ce^{-2x}$ with $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
Consider the differential equation $y'-2xy=4x$. 

Now we first consider the homogeneous equation $y'-2xy=0$ with general solution $y(x)=Ce^{x^2}$.

Then we substitute $y(x)=u(x)e^{x^2}$ into the original inhomogeneous equation:

$$
\begin{align*}
u'(x)e^{x^2}+2xu(x)e^{x^2}-2xu(x)e^{x^2}=4x&\quad\Longrightarrow\quad u'(x)=4xe^{-x^2}\\
&\quad\Longrightarrow\quad u(x)=-2e^{-x^2}.
\end{align*}
$$

So, the general solution is: $y(x)=u(x)e^{x^2}=-2+Ce^{x^2}$ with $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
Consider the differential equation $xy'+y=1$ with $x>0$. 

First we write it in *standard form* $y'+\displaystyle\frac{1}{x}y=\frac{1}{x}$. 

Then we consider the homogeneous equation $y'+\displaystyle\frac{1}{x}y=0$ with general solution $y(x)=\displaystyle\frac{C}{x}$. 

Then we substitute $y(x)=\displaystyle\frac{u(x)}{x}$ into the original inhomogeneous equation:

$$
\frac{u'(x)}{x}-\frac{u(x)}{x^2}+\frac{u(x)}{x^2}=\frac{1}{x}\quad\Longrightarrow\quad u'(x)=1\quad\Longrightarrow\quad u(x)=x+C.
$$

So, the general solution is: $y(x)=\displaystyle\frac{u(x)}{x}=\frac{x+C}{x}=1+\frac{C}{x}$ with $C\in\mathbb{R}$.
::::::

## Bernoulli equations

A differential equation of the form

:::{math}
:label: Eq:ODE1:Bernoulli
y'+P(x)y=Q(x)y^n,\quad n\in\mathbb{N}
:::

is called a **Bernoulli equation**, named after the Swiss mathematician [Jacob Bernoulli (1655-1705)](https://en.wikipedia.org/wiki/Jacob_Bernoulli).

:::{prf:remark}
Note that $y(x)=0$ is a constant solution of every Bernoulli equation with $n\neq0$. We will ignore this uninteresting solution in the sequel.
:::

For $n=0$ and $n=1$ this is a linear differential equation. However, for $n\geq2$ the Bernoulli equation is nonlinear. In 1696 [Gottfried Wilhelm Leibniz (1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) was the first one to solve the nonlinear Bernoulli equation using the substitution $u=y^{1-n}$. Note that this implies that $u'=(1-n)y^{-n}\cdot y'$.

If we divide {eq}`Eq:ODE1:Bernoulli` by $y^n$ we obtain

$$
\frac{y'}{y^n}+\frac{P(x)}{y^{n-1}}=Q(x)\quad\Longleftrightarrow\quad y^{-n}y'+P(x)y^{1-n}=Q(x).
$$

Applying the substitution $u=y^{1-n}$ this transfers into

$$
\frac{u'}{1-n}+P(x)u=Q(x)\quad\Longrightarrow\quad u'+(1-n)P(x)u=(1-n)Q(x).
$$

This shows that the substitution $u=y^{1-n}$ turns the nonlinear Bernoulli equation into a linear differential equation.

::::::{prf:example}
Consider the differential equation $y'+\dfrac{1}{x}y=y^2$ for $x>0$. This is a Bernoulli equation with $P(x)=\dfrac{1}{x}$, $Q(x)=1$ and $n=2$.

If we divide by $y^2$ we obtain

$$
y^{-2}y'+\frac{1}{x}y^{-1}=1.
$$

Then the substitution $u=y^{-1}$ and therefore $u'=-y^{-2}y'$ leads to

$$
-u'+\frac{1}{x}u=1\quad\text{or equivalently}\quad u'-\frac{1}{x}u=-1.
$$

Looking for an integrating factor $I(x)$ we obtain

$$
I(x)u'(x)-\frac{1}{x}I(x)u(x)=-I(x).
$$

Now we want $I(x)$ to satisfy $I'(x)=-\dfrac{1}{x}I(x)$, which leads to $I(x)=\dfrac{1}{x}$. Hence we have

$$
\frac{d}{dx}\left(\frac{1}{x}u(x)\right)=-\frac{1}{x}\quad\Longrightarrow\quad\frac{1}{x}u(x)=-\ln(x)+C.
$$

This implies that $u(x)=x\left(C-\ln(x)\right)$.

Finally, we use $u=y^{-1}$ or $y=u^{-1}$ to conclude that $y(x)=\dfrac{1}{x\left(C-\ln(x)\right)}$ with $C\in\mathbb{R}$.
::::::

```{exercise} 
:label: Exc:ODE1:BernoulliExercise1
Solve the differential equation $y'+\dfrac{1}{x}y=xy^2$ for $x>0$.
```

:::{admonition} Solution of {numref}`Exc:ODE1:BernoulliExercise1`
:class: solution, dropdown
The substitution $u=y^{-2}$ and therefore $u'=-2y^{-3}y'$ leads to

$$
-\frac{1}{2}u'+\frac{1}{x}u=x\quad\Longleftrightarrow\quad u'-\frac{1}{x}u=-x.
$$

An integrating factor is $I(x)=e^{-\ln(x)}=x^{-1}$, which leads to

$$
\frac{d}{dx}\left(x^{-1}u(x)\right)=-1\quad\Longrightarrow\quad x^{-1}u(x)=-x+C.
$$

Hence, we have: $u(x)=x(C-x)$.

Now we use $u=y^{-1}$ or equivalently $y=\dfrac{1}{u}$ to find

$$
y(x)=\frac{1}{x(C-x)},\quad C\in\mathbb{R}.
$$

:::

```{exercise} 
:label: Exc:ODE1:BernoulliExercise2
Solve the differential equation $y'-y=3xy^4$.
```

:::{admonition} Solution of {numref}`Exc:ODE1:BernoulliExercise2`
:class: solution, dropdown
The substitution $u=y^{-3}$ and therefore $u'=-3y^{-4}y'$ leads to

$$
-\frac{1}{3}u'-u=3x\quad\Longleftrightarrow\quad u'+3u=-9x.
$$

An integrating factor is $I(x)=e^{3x}$, which leads to

$$
\frac{d}{dx}\left(e^{3x}u(x)\right)=-9xe^{3x}\quad\Longrightarrow\quad e^{3x}u(x)=(1-3x)e^{3x}+C.
$$

Hence, we have: $u(x)=1-3x+Ce^{-3x}$.

Now we use $u=y^{-3}$ or equivalently $y^3=\dfrac{1}{u}$ to find

$$
y^3=\frac{1}{1-3x+Ce^{-3x}}\quad\Longrightarrow\quad y(x)=\frac{1}{\left(1-3x+Ce^{-3x}\right)^{1/3}},\quad C\in\mathbb{R}.
$$

:::

```{exercise} 
:label: Exc:ODE1:BernoulliExercise3
Solve the differential equation $x^2y'+2xy=y^3$ for $x>0$.
```

:::{admonition} Solution of {numref}`Exc:ODE1:BernoulliExercise3`
:class: solution, dropdown
First rewrite the differential equation in the standard form {eq}`Eq:ODE1:Bernoulli` and divide by $y^3$:

$$
y'+\frac{2}{x}y=\frac{1}{x^2}y^3\quad\Longrightarrow\quad y^{-3}y'+\frac{2}{x}y^{-2}=\frac{1}{x^2}.
$$

Now the substitution $u=y^{-2}$ and therefore $u'=-2y^{-3}y'$ leads to

$$
-\frac{1}{2}u'+\frac{2}{x}u=\frac{1}{x^2}\quad\Longleftrightarrow\quad u'-\frac{4}{x}u=-\frac{2}{x^2}.
$$

An integrating factor is $I(x)=e^{-4\ln(x)}=x^{-4}$, which leads to

$$
\frac{d}{dx}\left(x^{-4}u(x)\right)=-2x^{-6}\quad\Longrightarrow\quad x^{-4}u(x)=\frac{2}{5}x^{-5}+C.
$$

Hence, we have: $u(x)=\dfrac{2}{5}x^{-1}+Cx^4=\dfrac{2+5Cx^5}{5x}$.

Now we use $u=y^{-2}$ or equivalently $y^2=\dfrac{1}{u}$ to find

$$
y^2=\frac{5x}{2+5Cx^5}\quad\Longrightarrow\quad y(x)=\pm\sqrt{\frac{5x}{2+5Cx^5}},\quad C\in\mathbb{R}.
$$

:::

**The logistic equation**

We have seen that the *logistic equation* $\displaystyle\frac{dP}{dt}=kP\left(1-\frac{P}{M}\right)$
is autonomous and separable. However, it is also a Bernoulli equation:

$$
\frac{dP}{dt}-kP=-\frac{k}{M}P^2.
$$

We divide by $P^2$ to obtain

$$
P^{-2}\frac{dP}{dt}-kP^{-1}=-\frac{k}{M}
$$

and apply the substitution $u=P^{-1}$ and therefore $u'=-P^{-2}P'$ to find

$$
-u'-ku=-\frac{k}{M}\quad\Longleftrightarrow\quad u'+ku=\frac{k}{M}.
$$

Note that $I(t)=e^{kt}$ is an integrating factor, which implies that

$$
\frac{d}{dt}\left(e^{kt}u(t)\right)=\frac{k}{M}e^{kt}\quad\Longrightarrow\quad e^{kt}u(t)=\frac{1}{M}e^{kt}+C.
$$

Hence, we have: $u(t)=\dfrac{1+Ke^{-kt}}{M}$ with $K=MC$. Finally, since $u=P^{-1}$ we conclude that

$$
P(t)=\frac{1}{u(t)}=\frac{M}{1+Ke^{-kt}},\quad K\in\mathbb{R}.
$$

Earlier we have seen that the initial value $P(0)=P_0$ leads to $K=\dfrac{M-P_0}{P_0}$.

## Riccati equations

A differential equation of the form

:::{math}
:label: Eq:ODE1:Riccati
y'=P(x)+Q(x)y+R(x)y^2
:::

is called a **Riccati equation**, named after the Italian mathematician [Jacopo Francesco Riccati (1676-1754)](https://en.wikipedia.org/wiki/Jacopo_Riccati).

If $P(x)=0$ this is a Bernoulli equation. If $R(x)=0$ this is a linear differential equation. For $R(x)\neq0$ this is a nonlinear differential equation.

In 1760 the Swiss mathematician [Leonhard Euler 1707-1783)](https://en.wikipedia.org/wiki/Leonhard_Euler) introduced the following method. 

If one particular solution $y_1(x)$ is known, a more general solution can be obtained using the substitution $y(x)=y_1(x)+\dfrac{1}{u(x)}$. Since then we have $y'(x)=y_1'(x)-\dfrac{u'(x)}{u^2(x)}$ and substiution into {eq}`Eq:ODE1:Riccati` leads to

$$
y_1'-\frac{u'}{u^2}=P(x)+Q(x)y_1+\frac{Q(x)}{u}+R(x)\left(y_1^2+\frac{2y_1}{u}+\frac{1}{u^2}\right).
$$

Since $y_1$ is a solution of {eq}`Eq:ODE1:Riccati` we have $y_1'=P(x)+Q(x)y_1+R(x)y_1^2$. Hence we obtain

$$
-\frac{u'}{u^2}=\frac{Q(x)}{u}+R(x)\left(\frac{2y_1}{u}+\frac{1}{u^2}\right)\quad\Longrightarrow\quad-u'=Q(x)u+R(x)\left(2y_1u+1\right).
$$

Note that this is a linear differential equation which can be solved. The general solution of this linear differential equations contains an arbitrary constant of integration. This leads to a more general solution of the Riccati equation containing an arbitrary constant of integration. When the conditions of {prf:ref}`Thm:DE:ExistenceUniquenessODE1Nonlinear` hold, this should be the general solution. 

::::::{prf:example}
Note that $y_1(x)=\dfrac{2}{x}$ is a solution of the Riccati equation

:::{math}
:label: Eq:ODE1:RiccatiExample
y'=\frac{2}{x^2}-y^2,\quad x>0.
:::

Let $y(x)=\dfrac{2}{x}+\dfrac{1}{u(x)}$, then we have $y'(x)=-\dfrac{2}{x^2}-\dfrac{u'(x)}{u^2(x)}$. Substitution into {eq}`Eq:ODE1:RiccatiExample` leads to

$$
-\frac{2}{x^2}-\frac{u'}{u^2}=\frac{2}{x^2}-\left(\frac{2}{x}+\frac{1}{u}\right)^2.
$$

Simplifying we obtain

$$
-\frac{u'}{u^2}=-\frac{4}{x\,u}-\frac{1}{u^2}\quad\Longrightarrow\quad u'-\frac{4}{x}u=1.
$$

Using the integrating factor $e^{-\int\frac{4}{x}\,dx}=e^{-4\ln(x)}=x^{-4}$ we find

$$
\frac{d}{dx}\left(x^{-4}u(x)\right)=x^{-4}\quad\Longrightarrow\quad x^{-4}u(x)=-\frac{1}{3}x^{-3}+C,
$$

which implies that $u(x)=-\frac{1}{3}x+Cx^4$. This leads to a more general solution

$$
y(x)=\frac{2}{x}+\frac{1}{Cx^4-\frac{1}{3}x},\quad C\in\mathbb{R}.
$$

Note that the solution $y(x)=\dfrac{2}{x}$ is retrieved by taking the limit $C\to\infty$. Therefore, it might be slightly better to use $C=\dfrac{1}{K}$ to find

$$
y(x)=\frac{2}{x}+\frac{K}{x^4-\frac{1}{3}Kx},\quad K\in\mathbb{R}.
$$

::::::

```{exercise} 
:label: Exc:ODE1:RiccatiExercise1
Note that $y_1(x)=x$ is a solution of the Riccati equation $y'=1+x^2-2xy+y^2$.

Find the general solution.
```

:::{admonition} Solution of {numref}`Exc:ODE1:RiccatiExercise1`
:class: solution, dropdown
Note that $f(x,y)=1+x^2-2xy+y^2$ and $\dfrac{\partial}{\partial y}f(x,y)=-2x+2y$ are continuous. Then {prf:ref}`Thm:DE:ExistenceUniquenessODE1Nonlinear` implies that the general solution has one degree of freedom (an arbitrary constant of integration).

We set $y(x)=x+\dfrac{1}{u(x)}$ and therefore $y'(x)=1-\dfrac{u'(x)}{u^2(x)}$ to find

$$
1-\frac{u'}{u^2}=1+x^2-2x\left(x+\frac{1}{u}\right)+\left(x+\frac{1}{u}\right)^2\quad\Longrightarrow\quad-\frac{u'}{u^2}=\frac{1}{u^2}.
$$

Multiplying by $u^2$ we obtain $-u'=1$ which implies that $u(x)=-x+C$ with $C\in\mathbb{R}$. Hence, we have

$$
y(x)=x+\frac{1}{C-x},\quad C\in\mathbb{R}.
$$

Again, the solution $y(x)=x$ is retrieved by taking the limit $C\to\infty$. Therefore, it might be slightly better to use $C=\dfrac{1}{K}$ to find

$$
y(x)=x+\frac{K}{1-Kx},\quad K\in\mathbb{R}.
$$

:::

```{exercise} 
:label: Exc:ODE1:RiccatiExercise2
Note that $y_1(x)=\dfrac{1}{x}$ is a solution of the Riccati equation 

$$
y'=\frac{1}{x^2}-\frac{y}{x}+y^2,\quad x>0.
$$

Find a more general solution with an arbitrary constant.
```

:::{admonition} Solution of {numref}`Exc:ODE1:RiccatiExercise2`
:class: solution, dropdown
We set $y(x)=\dfrac{1}{x}+\dfrac{1}{u(x)}$ and therefore $y'(x)=-\dfrac{1}{x^2}-\dfrac{u'(x)}{u^2(x)}$ to find

$$
-\frac{1}{x^2}-\frac{u'}{u^2}=\frac{1}{x^2}-\frac{1}{x}\left(\frac{1}{x}+\frac{1}{u}\right)-\left(\frac{1}{x}+\frac{1}{u}\right)^2
$$

or equivalently

$$
-\frac{1}{x^2}-\frac{u'}{u^2}=\frac{1}{x^2}-\frac{1}{x^2}-\frac{1}{x\,u}-\frac{1}{x^2}-\frac{2}{x\,u}-\frac{1}{u^2}.
$$

Simplifying we obtain

$$
-\frac{u'}{u^2}=-\frac{3}{x\,u}-\frac{1}{u^2}\quad\Longleftrightarrow\quad u'-\frac{3}{x}u=1.
$$

Using the integrating factor $e^{-\int\frac{3}{x}\,dx}=x^{-3}$ we obtain

$$
\frac{d}{dx}\left(x^{-3}u(x)\right)=x^{-3}\quad\Longrightarrow\quad x^{-3}u(x)=-\frac{1}{2}x^{-2}+C.
$$

This implies that $u(x)=-\frac{1}{2}x+Cx^3$. Hence we have

$$
y(x)=\frac{1}{x}+\frac{1}{Cx^3-\frac{1}{2}x},\quad C\in\mathbb{R}.
$$

In order to include the solution $y(x)=\dfrac{1}{x}$ we might use $C=\dfrac{1}{K}$ to find

$$
y(x)=\frac{1}{x}+\frac{K}{x^3-\frac{1}{2}Kx},\quad K\in\mathbb{R}.
$$

:::

```{exercise} 
:label: Exc:ODE1:RiccatiExercise3
Note that $y_1(x)=x^2$ is a solution of the Riccati equation 

$$
y'=x^3+\frac{2y}{x}-\frac{y^2}{x},\quad x>0.
$$

Find a more general solution with an arbitrary constant.
```

:::{admonition} Solution of {numref}`Exc:ODE1:RiccatiExercise3`
:class: solution, dropdown
We set $y(x)=x^2+\dfrac{1}{u(x)}$ and therefore $y'(x)=2x-\dfrac{u'(x)}{u^2(x)}$ to find

$$
2x-\frac{u'}{u^2}=x^3+\frac{2}{x}\left(x^2+\frac{1}{u}\right)-\frac{1}{x}\left(x^2+\frac{1}{u}\right)^2
$$

or equivalently

$$
2x-\frac{u'}{u^2}=x^3+2x+\frac{2}{x\,u}-x^3-\frac{2x}{u}-\frac{1}{x\,u^2}.
$$

Simplifying we obtain

$$
-\frac{u'}{u^2}=\frac{2}{x}u-2x\,u-\frac{1}{x}\quad\Longleftrightarrow\quad u'+\left(\frac{2}{x}-2x\right)u=\frac{1}{x}.
$$

Using the integrating factor $e^{\int\left(\frac{2}{x}-2x\right)\,dx}=x^2e^{-x^2}$ we obtain

$$
\frac{d}{dx}\left(x^2e^{-x^2}u(x)\right)=xe^{-x^2}\quad\Longrightarrow\quad x^2e^{-x^2}u(x)=-\frac{1}{2}e^{-x^2}+C.
$$

This implies that $u(x)=-\dfrac{1}{2x^2}+\dfrac{Ce^{x^2}}{x^2}$. Hence we have

$$
y(x)=x^2+\frac{2x^2}{2Ce^{x^2}-1},\quad C\in\mathbb{R}.
$$

In order to include the solution $y(x)=x^2$ we might use $C=\dfrac{1}{K}$ to find

$$
y(x)=x^2+\frac{2Kx^2}{2e^{x^2}-K},\quad K\in\mathbb{R}.
$$

:::

:::{note}
If no particular solution is known, there is another method that changes the Riccati equation into a second-order linear differential equation that might be easier to solve.

Using the subsitution $y=-\dfrac{1}{R}\cdot\dfrac{v'}{v}$ and therefore

$$
y'=-\frac{v''Rv-R'vv'-R(v')^2}{R^2v^2}
$$

we obtain

$$
-\frac{v''}{Rv}+\frac{R'v'}{R^2v}+\frac{R(v')^2}{R^2v^2}=P-\frac{Qv'}{Rv}+\frac{(v')^2}{Rv^2}.
$$

Simplifying and after multiplication by $R^2v$ we find

$$
-Rv''+R'v'=PR^2v-QRv'\quad\Longleftrightarrow\quad Rv''-(R'+QR)v'+PRv=0.
$$

This is a second-order linear differential equation in $v(x)$. In the next chapter we will see how these can be solved in case of constant coefficients. In {numref}`Sec:ODE2:Series` we also cover some other cases as well.
:::

:::::{prf:remark}
The general solution of the second-order differential equation above has two degrees of freedom, which might lead to an even more general solution of the Riccati equation.

For instance, note that $y(x)=-1$ is a solution of the Riccati equation

:::{math}
:label: Eq:ODE1:RiccatiRemark
y'=1+2y+y^2.
:::

Hence, the substitution $y(x)=-1+\dfrac{1}{u(x)}$ and therefore $y'(x)=-\dfrac{u'(x)}{u^2(x)}$ leads to

$$
-\frac{u'}{u^2}=1+2\left(-1+\frac{1}{u}\right)+\left(-1+\frac{1}{u}\right)^2
$$

or equivalently

$$
-\frac{u'}{u^2}=1-2+\frac{2}{u}+1-\frac{2}{u}+\frac{1}{u^2}.
$$

Simplifying and multiplying by $u^2$ we obtain $-u'=1$ with general solution $u(x)=-x+C$. This leads to the solution

$$
y(x)=-1+\frac{1}{C-x}=-\frac{C-x-1}{C-x},\quad C\in\mathbb{R}
$$

of the Riccati equation {eq}`Eq:ODE1:RiccatiRemark`.

Since in this case we have $P(x)=1$, $Q(x)=2$ and $R(x)=1$ the second-order linear differential equation for $v(x)$ reads

$$
v''-2v'+v=0.
$$

As will be explained in the next chapter the general solution of this differential equation is $v(x)=c_1e^x+c_2xe^x$ with $c_1,c_2\in\mathbb{R}$. This leads to

$$
y(x)=-\frac{1}{R}\cdot\frac{v'}{v}=-\frac{c_1e^x+c_2(x+1)e^x}{c_1e^x+c_2xe^x}=-\frac{c_1+c_2(x+1)}{c_1+c_2x},\quad c_1,c_2\in\mathbb{R}.
$$

Note that $c_2=0$ leads to the constant solution $y(x)=-1$ and $c_2=-1$ to the earlier obtained solution $y(x)=-\dfrac{c_1-x-1}{c_1-x}$ with $c_1\in\mathbb{R}$.

Note that $f(y)=1+2y+y^2$ and $f'(y)=2+2y$ are continuous. So, {prf:ref}`Thm:DE:ExistenceUniquenessODE1Nonlinear` implies that the general solution should only have one arbitrary constant. In fact, if we divide by $c_2$ and set $K=\dfrac{c_1}{c_2}$ the solution above reduces to

$$
y(x)=-\frac{c_1+c_2(x+1)}{c_1+c_2x}=-\frac{\dfrac{c_1}{c_2}+x+1}{\dfrac{c_1}{c_2}+x}=-\frac{K+x+1}{K+x},
$$

where $K$ can be chosen arbitrarily with $K\to\infty$ leading to the constant solution $y(x)=-1$.

Finally, note that the differential equation {eq}`Eq:ODE1:RiccatiRemark` is separable as well. For $y\neq0$ we obtain

$$
y'=(1+y)^2\quad\Longrightarrow\quad\frac{dy}{(1+y)^2}=dx\quad\Longrightarrow\quad-\frac{1}{1+y}=x+K.
$$

This leads to

$$
y(x)=-1-\frac{1}{x+K}=-\frac{x+K+1}{x+K},\quad K\in\mathbb{R}.
$$

:::::

## Applications

**Learning curve**

Let $P(t)$ be the performance level of someone learning a skill as a function of the training time $t$. The graph of $P$ is called a *learning curve*.

If $M$ is the maximum level of performance of which the learner is capable, then

$$
\frac{dP}{dt}=k(M-P)
$$

is a a reasonable model for learning, where $k$ is a positive constant.

Note that this differential equation is *linear*. So we look for an integrating factor $I(t)$:

$$
I(t)P'(t)+kI(t)P(t)=kMI(t)\;\text{with}\;I'(t)=kI(t)\;\Longrightarrow\;I(t)=e^{kt}\;\text{for instance}.
$$

This implies that

$$
\frac{d}{dt}\left[e^{kt}P(t)\right]=kMe^{kt}\quad\Longrightarrow\quad e^{kt}P(t)=\int kMe^{kt}\,dt=Me^{kt}+C.
$$

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

$$
m\frac{dv}{dt}=mg-kv,\quad v(0)=0,
$$

where $m$ denotes the mass of the skydiver, $g=9.81\;\text{m}/\text{s}^2$ is the acceleration due to gravity and $k$ is a positive constant.

Assume that $m=90\;\text{kg}$ and $k=15$, then we have:

$$
90\frac{dv}{dt}=90g-15v\quad\Longleftrightarrow\quad v'(t)+\tfrac{1}{6}v(t)=g.
$$

This is a *linear* differential equation. Using the integrating factor $e^{\frac{1}{6}t}$ we find that:

$$
\frac{d}{dt}\left[e^{\frac{1}{6}t}v(t)\right]=ge^{\frac{1}{6}t}\quad\Longrightarrow\quad e^{\frac{1}{6}t}v(t)=6ge^{\frac{1}{6}t}+C
\quad\Longrightarrow\quad v(t)=6g+Ce^{-\frac{1}{6}t}.
$$

Now we use the initial condition $v(0)=0$ to find that $C=-6g$. Hence we have: $v(t)=6g\left(1-e^{-\frac{1}{6}t}\right)$.

Using $6g=6\cdot9.8=58.8$, for instance this implies that the speed of the skydiver after $10$ seconds is: $v(10)=58.8\left(1-e^{-\frac{5}{3}}\right)\approx47.7\;\text{m}/\text{s}$.

Furthermore, since $v(t)=50\;\Longleftrightarrow\displaystyle\;t=-6\ln\left(\frac{8.8}{58.8}\right)\approx11.4$ we conclude that it takes approximately $11.4$ seconds to reach a speed of $50\;\text{m}/\text{s}$ (which is $180\;\text{km}/\text{h}$).

Finally, if the free fall could last forever, the (theoretical) maximum speed would be $\lim\limits_{t\to\infty}v(t)=58.8\;\text{m}/\text{s}$. Solving

$$
v(t)=58\quad\Longleftrightarrow\quad t=-6\ln\left(\frac{0.8}{58.8}\right)\approx25.8
$$

we conclude that it takes approximately $25.8$ seconds to reach a speed of $58\;\text{m}/\text{s}$ (which is $208.8\;\text{km}/\text{h}$).

**Mixing problems**

The differential equations in {prf:ref}`Ex:ODE1:MixingProblemExample1` and {prf:ref}`Ex:ODE1:MixingProblemExample2` in the previous section are both separable and linear. We can also solve these differential equations using the methods explained in this section.

::::::{prf:example}
A tank contains $100\;\ell$ brine with $100\;\text{g}$ salt dissolved in water. This solution is kept thoroughly mixed and drains from the tank at a rate of $3\;\ell/\text{min}$. Simultaneously, brine with a concentration of $10\;\text{g}/\ell$ enters the tank at a rate of $1\;\ell/\text{min}$. What is the amount of salt (in $\text{g}$) in the tank after $25$ minutes?
::::::

::::::{admonition} Solution
Let $y(t)$ denote the amount of salt (in $\text{g}$) in the tank at time $t$ (in $\text{min}$). Then we have: $y(0)=100$ (initial condition) and $\displaystyle\frac{dy}{dt}=10−3\cdot\frac{y}{100-2t}$. This differential equation is linear (and not separable). So we look for an integrating factor $I(t)$:

$$
I(t)y'(t)+\frac{3}{100-2t}I(t)y(t)=10I(t)\quad\text{with}\quad I'(t)=\frac{3}{100-2t}I(t). 
$$

Hence: $I(t)=\exp\left(-\frac{3}{2}\ln(100-2t)\right)=(100-2t)^{-\frac{3}{2}}$ for instance. Then we have:

$$
\begin{align*}
&\frac{d}{dt}\left[(100-2t)^{-\frac{3}{2}}y(t)\right]=10(100-2t)^{-\frac{3}{2}}\\
&{}\hspace{25mm}{}\Longrightarrow\quad(100-2t)^{-\frac{3}{2}}y(t)=10(100-2t)^{-\frac{1}{2}}+C
\end{align*} 
$$

and therefore: $y(t)=10(100-2t)+C(100-2t)^{\frac{3}{2}}$. The initial condition $y(0)=100$ leads to: 

$$
100=1000+1000C\quad\text{or equivalently}\quad C=-\frac{900}{1000}=-\frac{9}{10}.
$$

Hence: $y(t)=10(100-2t)-\frac{9}{10}(100-2t)^{\frac{3}{2}}$.

For $t=25$ we obtain: $y(25)=500-\frac{9}{10}\cdot50\sqrt{50}=500-225\sqrt{2}$.

*Remark:* Note that the differential equation only holds for $0 < t < 50$. After $50$ minutes the tank will be empty.
::::::

::::::{prf:example}
A tank with a volume of $500\;\ell$ contains $25\;\text{g}$ salt dissolved in $100\;\ell$ water. This solution is kept thoroughly mixed and drains from the tank at a rate of $1\;\ell/\text{min}$. Simultaneously, brine with a concentration of $5\;\text{g}/\ell$ enters the tank at a rate of $2\;\ell/\text{min}$. What is the amount of salt (in $\text{g}$) in the tank after $25$ minutes?
::::::

::::::{admonition} Solution
Let $y(t)$ denote the amount of salt (in $\text{g}$) in the tank at time $t$ (in $\text{min}$). Then we have: $y(0)=25$ (initial condition) and $\displaystyle\frac{dy}{dt}=10−1\cdot\frac{y}{100+t}$. This differential equation is linear (and not separable). So we look for an integrating factor $I(t)$:

$$
I(t)y'(t)+\frac{1}{100+t}I(t)y(t)=10I(t)\quad\text{with}\quad I'(t)=\frac{1}{100+t}I(t).
$$

Hence: $I(t)=\exp\left(\ln(100+t)\right)=100+t$ for instance. Then we have:

$$
\begin{align*}
&\frac{d}{dt}\left[(100+t)y(t)\right]=10(100+t)=1000+10t\\
&{}\hspace{25mm}{}\Longrightarrow\quad(100+t)y(t)=1000t+5t^2+C.
\end{align*}
$$

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