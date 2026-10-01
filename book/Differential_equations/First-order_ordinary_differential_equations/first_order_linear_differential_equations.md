(Sec:ODE1:Linear)=

# First-order linear differential equations

## Introduction


In {numref}`Sec:ODE1:Separable` we have seen how we can solve separable first-order separable equations. However, in {prf:ref}`Ex:DiffSep:SepCheck2` we saw that even a seemingly simple differential equation such as 

$$
 y'=t+y
$$

is not separable, so we are not able to solve it (yet). In {numref}`Subsec:DiffclassLinear` we introduced the concept of a linear differential equation. The differential equation above is linear. In this section, we will learn two different methods to solve first-order linear differential equations: using an **integarting factor** and the method of **variation of parameters**. 

Let us first repeat a part of {prf:ref}`Def:ClassDiff:Linear` specifically for first-order differential equations.

::::::{prf:definition}
:label: Def:ODE1Lin:Linear

A first-order differential equation $F(x,y,y')=0$ is called **linear** if it can be written in the form

$$
a_1(x)y'+a_0(x)y=f(x).
$$

The first-order differential equation is in **standard form**, when it is written as

$$
y'+p(x)y=q(x).
$$
::::::

::::::{prf:example} 
:label: Ex:ODE1Lin:LinCheck1
Consider the differential equation

$$
 e^x\frac{dy}{dx}=x^2y-\sin(x).
$$

Even though this equation is not in the correct form yet, it is linear, since we can write

$$
 e^x\frac{dy}{dx}-x^2y=-\sin(x).
$$

It is important to realise that even though a linear differential equation needs to be linear in $y$ and $\dfrac{dy}{dx}$, it is no problem that it contains nonlinear functions of $x$, such as $e^x$, $-x^2$ and $-\sin(x)$. The standard form of this linear differential equation can be found by dividing the entire equation by $e^x$, i.e. by multiplying it by $e^{-x}$, which gives

$$
\frac{dy}{dx}-e^{-x}x^2y=-e^{-x}\sin(x).
$$
::::::

::::::{prf:example} 
:label: Ex:ODE1Lin:LinCheck12
Consider the differential equation

$$
 y'=t^2+\frac{1}{y}.
$$

Because of the term $\dfrac{1}{y}$, the differential equation is not linear. Even if we were to multiply the equation by $y$, we would obtain

$$
 yy'=t^2y+1
$$

and the term $yy'$ cannot be a part of a linear differential equation.

To be absolutely sure that it cannot be written in the correct form, we use {prf:ref}`Thm:ClassDiff:Linear`. We can rewrite the differential equation as $F(t,y,y')=0$ with

$$
 F(t,y,y')=y'-t^2-\frac{1}{y}.
$$

Then we see that

$$
 \frac{\partial^2}{\partial y_0^2}F(t,y_0,y_1)=-\frac{2}{y_0^3}\neq 0,
$$

so the differential equation is not linear.
::::::

## Integrating factor



In order to derive a method for solving first-order linear differential equations, we first consider one of the form

:::{math}
:label: Eq:ODE1Lin:Step1
 y(x)'=q(x).
:::

This is a first-order linear differential equation and it is written in standard form. Even better, we already know how to solve it: the differential equation asks us to find a function $y$ of which the derivative is the known function $q$. Then $y$ must be an antiderivative of $q$, i.e. we find that

$$
 y(x)=\int q(x)\,dx.
$$

So far so good, so let us consider the slightly more difficult first-order linear differential equation

:::{math}
:label: Eq:ODE1Lin:Step2
 \left(y(x)I(x)\right)'=I(x)q(x),
:::

where $I(x)$ is some known function. Writing the differential equation like this might seem a bit weird, but it will turn out to be a convenient form. Just like {eq}`Eq:ODE1Lin:Step1`, the differential equation {eq}`Eq:ODE1Lin:Step2` asks us to find a function, this time called $y(x)I(x)$, of which the derivative is the known function $I(x)q(x)$. This means that, as before, $y(x)I(x)$ needs to be an antiderivative of $I(x)q(x)$, which gives

$$
 y(x)I(x)=\int I(x)q(x)\,dx.
$$

From this, we obtain

$$
 y(x)=\frac{1}{I(x)}\int I(x)q(x)\,dx.
$$



We are still going strong, so let us consider a first-order linear differential equation, which appears to be yet one step harder

:::{math}
:label: Eq:ODE1Lin:Step3
 y'(x)I(x)+y(x)I'(x)=I(x)q(x).
:::

However, this equation is not harder at all, since it is the exact same equation as {eq}`Eq:ODE1Lin:Step2`. Indeed, we can use {prf:ref}`Thm:Productquotientrule:Productrule` to write out the term $(y(x)I(x))'$ in {eq}`Eq:ODE1Lin:Step2` to obtain

$$
 y'(x)I(x)+y(x)I'(x)=I(x)q(x),
$$

which exactly matches {eq}`Eq:ODE1Lin:Step3`. But then, we also know how to solve it: we first write it back into the form {eq}`Eq:ODE1Lin:Step2` and then integrate to obtain

$$
 y(x)=\frac{1}{I(x)}\int I(x)q(x)\,dx.
$$

We now feel confident enough to try to solve the most general case: a first-order linear differential equation in standard form, which is given by

:::{math}
:label: Eq:ODE1Lin:Step4
 y'(x)+p(x)y(x)=q(x).
:::

If we multiply {eq}`Eq:ODE1Lin:Step4` by a function $I(x)$ with $I(x)\neq 0$ for all $x$, then the solutions do not change. Multiplying with the, as of now unknown, function $I(x)$, we obtain

$$
 y'(x)I(x)+p(x)y(x)I(x)=I(x)q(x).
$$ 

This is *almost* in the same form as {eq}`Eq:ODE1Lin:Step3`. The only thing we do need to ensure is that the coefficient of $y(x)$ matches, which means that we must have

$$
 I'(x)=p(x)I(x).
$$

This is a separable differential equation for $I(x)$, so we know how to solve it. Indeed, letting $P(x)$ denote any antiderivative of $p(x)$, we see that

$$
 I(x)=e^{P(x)}
$$

satisfies

$$
 I'(x)=e^{P(x)}P'(x)=I(x)p(x).
$$

This function $I(x)$ is called an **integrating factor** for the differential equation. We conclude that if we multiply {eq}`Eq:ODE1Lin:Step4` by $I(x)=e^{P(x)}$ we obtain an equation in the same form as {eq}`Eq:ODE1Lin:Step3`, which means that we obtain the solution

$$
 y(x)=\frac{1}{I(x)}\int I(x)q(x)\,dx.
$$

Let us formalise the terminology used here and, subsequently, turn this solution procedure into an algorithm that can be used to solve any first-order linear differential equation.

::::::{prf:definition} 
:label: Def:ODE1Lin:Integratingfactor
For a first-order linear differential equation in $y(x)$ in standard form

$$
 y' + p(x)y = q(x),
$$

an **integrating factor** $I$ is given by

$$
 I(x)=e^{P(x)},
$$

where $P(x)$ is any antiderivative of $p(x)$.


::::::

::::::{prf:algorithm}
:label: Alg:ODE1Lin:SolvingAlgorithm

[^FootnoteCheck]: At this point, the left-hand side of the equation reads $I(x)y'(x)+I(x)p(x)y(x)$. You should verify that this expression is the same as $\left(I(x)y(x)\right)'$.

Consider the first-oder linear differential equation $a_1(x)y'(x)+a_0(x)y(x)=f(x)$.

1. Write the differential equation in the standard form.
2. Find any integrating factor $I(x)$ for this differential equation.
3. Multiply the result of step 1 by the integrating factor.[^FootnoteCheck]
4. Take the antiderivative of both sides of the equation.
5. Solve for $y$ to obtain the general solution.
6. If applicable, use the initial condition to find the value of the arbitrary constant $C$.

::::::




::::::{prf:Example}
:label: Def:ODE1Lin:ExConst

[^FootnoteAntider]: There is no need to write $2x+C$ for the antiderivative of $2$. Indeed, we are only looking for some integrating factor that works, not for all of them. Picking a different antiderivative, such as $2x+5$ would give the same solution in the end.

Consider the differential equation 

$$
 y'+2y=3.
$$

This is a first-order linear differential equation and it is written in standard form. The coefficient function of $y$ in this standard form is $2$, of which $2x$ is an antiderivative[^FootnoteAntider]. Hence, $I(x)=e^{2x}$ is an integrating factor for this differential equation. We multiply the differential equation by this integrating factor to obtain

$$
 e^{2x}y'+2e^{2x}y=3e^{2x}.
$$

By construction, we have

$$
 e^{2x}y'+2e^{2x}=\left(e^{2x}y\right)',
$$

which means that the differential equation becomes

$$
 \left(e^{2x}y\right)'=3e^{2x}.
$$

We integrate this equation to obtain

$$
 e^{2x}y=\int 3e^{2x}\,dx=\frac{3}{2}e^{2x}+C.
$$

We conclude that the general solution of the differential equation is given by

$$
 y(x)=\frac{3}{2}+Ce^{-2x}
$$

with $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
:label: Ex:ODE1Lin:xy
Consider the differential equation $y'=2xy$, which we solved in {prf:ref}`Ex:DiffSep:xy`. This differential equation is not only separable, but also linear. First we need to write it in standard form

$$
 y'-2xy=0.
$$

The coefficient function of $y$ in this standard form is $-2x$, of which $-x^2$ is an antiderivative. Hence, $I(x)=e^{-x^2}$ is an integrating factor for this differential equation. We multiply the differential equation by this integrating factor to obtain

$$
 e^{-x^2}y'-2xe^{-x^2}y=0.
$$

By construction, we have

$$
 e^{-x^2}y'-2xe^{-x^2}y=\left(e^{-x^2}y\right)',
$$

which means that the differential equation becomes

$$
 \left(e^{-x^2}y\right)'=0.
$$

We integrate this equation to obtain

$$
 e^{-x^2}y=\int 0\,dx=C.
$$

We conclude that the general solution of the differential equation is given by

$$
 y(x)=Ce^{x^2}
$$

with $C\in\mathbb{R}$.
::::::

::::::{prf:Example}
:label: Ex:ODE1Lin:1overx
Consider the initial-value problem

$$
 xy'+y=1,\qquad y(1)=2
$$

with $x>0$. The differential equation is not in standard form, so we first write it as 

$$
 y'+\displaystyle\frac{1}{x}y=\frac{1}{x}.
$$

We then note that 

$$
 I(x)=e^{\int \frac{1}{x}\,dx}=e^{\ln(x)}=x
$$

is an integrating factor. We multiply the differential equation by this integrating factor to obtain

$$
 xy'+y=1.
$$

By construction, we have

$$
 xy'+y=\left(xy\right)',
$$

which means that the differential equation becomes

$$
 \left(xy\right)'=1.
$$

We integrate this equation to obtain

$$
 xy=\int 1\,dx=x+C.
$$

We conclude that the general solution of the differential equation is given by

$$
 y(x)=1+\frac{C}{x}
$$

with $C\in\mathbb{R}$. As the final step, we use the initial condition $y(1)=2$ to find the value of $C$. We must have

$$
 2=y(1)=1+\frac{C}{1}=1+C,
$$

which gives $C=1$. So the solution of the inital-value problem is given by

$$
 y(x)=1+\frac{1}{x}.
$$
::::::

## Variation of parameters

Another method of solving linear first-order differential equations is the method of **variation of parameters**, also known as **variation of constants**. In general, this method is a little more work than the integrating factor and since the integrating factor already works for all linear first-order differential equations, variation of parameters will not allow us to solve any new equations. The one major advantage this method has over the integrating factor is that it can be generalised to second-order (and higher-order) differential equations, see {numref}`Sec:ODE2:Nonconst`.

Consider a first-order linear differential equation in standard-form

$$
 y'+p(x)y=q(x).
$$

First consider the corresponding complementary equation (see {prf:ref}`Def:DE:ComplEq`)

$$
 y'+p(x)y=0.
$$

This differential equation is separable. Apart from the equilibrium solution $y=0$, we can solve it by writing 

$$
\frac{dy}{y}=-p(x)\,dx.
$$

Integrating both sides of the equation gives

$$
 \ln|y|=\int-p(x)\,dx.
$$

Writing $P(x)$ for an arbitrary antiderivative of $p(x)$, we can solve for $y$ to obtain

$$
 y=\pm e^{-P(x)+C}=\pm e^Ce^{-P(x)}.
$$

Combining this with the constant solution $y=0$, we obtain the solution

$$
 y=Ce^{-P(x)}.
$$

where $C$ is an arbitrary constant.

We now set out to solve the original, nonhomogeneous, linear differential equation. The main idea of the method of variation of parameters is to replace the arbitrary constant $C$ in the solution to the complementary equation by an arbitrary function $u(x)$, i.e. to try to find a solution of the form

$$
 y(x)=u(x)e^{-P(x)}.
$$

Then substitution into the nonhomogeneous differential equation yields

$$
 u'(x)e^{-P(x)}-p(x)u(x)e^{-P(x)}+p(x)u(x)e^{-P(x)}=q(x)
$$

which gives

$$ 
 u'(x)=q(x)e^{P(x)}.
$$

This equation can be integrated to find $u(x)$ including an arbitrary integration constant. Substitution into 
$y(x)=u(x)e^{P(x)}$ then gives the general solution.

This leads to the following algorithm.

::::::{prf:algorithm}
:label: Alg:ODE1Lin:SolvingAlgorithm2

Consider the first-oder linear differential equation $a_1(x)y'(x)+a_0(x)y(x)=f(x)$.

1. Write the differential equation in the standard form.
2. Solve the complementary equation, which is separable to obtain a solution of the form $y(x)=Cw(x)$.
3. In the differential equation found in step 1, substitute a solution of the form $y(x)=u(x)w(x)$.
4. Solve for $u(x)$.
5. Give the general solution $y(x)=u(x)w(x)$.
6. If applicable, use the initial condition to find the value of the arbitrary constant $C$.

::::::

::::::{prf:Example}
:label: Def:ODE1Lin:ExConstv2
Consider the differential equation 

$$
 y'+2y=3,
$$

which we solved in {prf:ref}`Def:ODE1Lin:ExConst`.  TOT HIER!

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