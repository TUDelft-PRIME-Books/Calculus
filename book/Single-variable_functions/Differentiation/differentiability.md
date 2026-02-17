(Section:Differentiability)=

# Differentiability

(Subsec:Differentiabilityintro)=

## Introduction

Suppose you are walking from your house to your favorite coffee shop to buy an XXL iced pumpkin spice latte (or a regular old cup of coffee, or the things you typically buy at Dutch "coffee shops", whichever you prefer). For simplicity, we assume that you walk in a straight line, so that your position $x$ (in meters) can be descibed as a function of time $t$ (in seconds). If you were to walk at a constant speed, you walk a fixed amount of meters each secons, so the graph of your position would look like a straight line. Say your house would be at position $x=0$ while the coffee shop is at position $x=600$ and that it takes you $400$ seconds to walk this distance. So what would be the function describing your position in this case? Since the graph should be a straight line, the function should be of the form

$$
 x(t)=at+b, \qquad 0\leq t\leq 400
$$

for some constants $a$ and $b$. Since at the starting time we are at home, we should have $x(0)=0$ and since we should arrive after $400$ seconds, we should have $x(400)=600$. Plugging these conditions into the function gives the two equations

$$
 0=x(0)=a\cdot0+b=b,\qquad 600=x(400)=a\cdot400+b.
$$

Solving these equations give $b=0$ and $a=\frac{3}{2}$, so the function becomes

$$
 x(t)=\frac{3}{2}t.
$$

Suppose we want to know the velocity at which we were walking. In this case, we were walking at a constant speed, so the velocity can be computed by dividing the distance we traveled, which we will denote by $\Delta x$, by the time that has passed, which we will denote by $\Delta t$. Then, the velocity at any point in time is given by

$$
 \mathrm{velocity}=\frac{\Delta x}{\Delta t}=\frac{600}{400}=\frac{3}{2}.
$$

Notice that this $\frac{3}{2}$ is the same as the coefficient of the $t$ term in the function $x(t)=\frac{3}{2}t$. This is no coincidence. Whenever we the position is a function of time of the form $x(t)=at+b$ and we measure the position at two points in time $t_1<t_2$, then the velocity can be found as the difference in position divided by the difference in time and we find

$$
 \mathrm{velocity}=\frac{\Delta x}{\Delta t}=\frac{\left(at_2+b\right)-\left(at_1+b\right)}{t_2-t_1}=\frac{at_2-at_1}{t_2-t_1}=a,
$$

so that $a$ is the velocity at any point in time. In particular, $a$ is the slope of the line $y=at+b$, so the slope has the interpretation of a velocity in this setting.

Now suppose that when arriving at the coffee shop, you remember that you forgot your phone and decided to walk back to pick it up and go to the coffee shop again. In that case your position might be given by the function

$$
 x(t)=300\sin\left(\frac{3\pi t}{1200}-\frac{\pi}{2}\right)+300, \qquad 0\leq t\leq 1200
$$

of which the graph is shown below.

Hier naast elkaar de grafieken van de twee functies $x(t)=\frac{3}{2}t$ en $x(t)=300\sin\left(\frac{3\pi t}{1200}-\frac{\pi}{2}\right)+300$. 

In this case, we can find the **average velocity** during our walk (where going back counts as a negative velocity) by dividing the difference in position $\Delta x$ by the difference in time. This gives that the average velocity is

$$
 \mathrm{average velocity}=\frac{\Delta x}{\Delta t}=\frac{x(1200)-x(0)}{1200-0}=\frac{600-0}{1200}=\frac{1}{2}.
$$

An important question now remains: can we somehow determine our velocity at a certain moment in time, say at $t=200$. Note that we are not walking with a constant velocity, so very likely at most point in time the velocity is not going to be equal to the average velocity of $\frac{1}{2}$ meters per second. The main idea to resolve this, is that if just zoom in very close to $t=200$, the graph of the function is approximately a straight line. The velocity at $t=200$ can then be approximated by dividing the difference in position by the difference in time. For $\Delta t=10$, we would be comparing the positions at $t=200$ with the one $10$ time steps further, so at $t=210$, and we would obtain

$$
 \mathrm{velocity}\approx \frac{\Delta x}{\Delta t}=\frac{x(210)-x(200)}{1}\approx 2.354.
$$

If we zoom in more, we should get a better approximation. Repeating these steps for $\Delta t=1$, we would obtain

$$
 \mathrm{velocity}\approx \frac{\Delta x}{\Delta t}=\frac{x(201)-x(200)}{1}\approx 2.356.
$$

So we can say that the volicity at $t=200$ is approximately equal to $2.356$ meter per second and by taking $\Delta t$ smaller, we get a better and better result. As before, the velocity can be thought of as the slope of the function at this point in time.

The expression $\frac{\Delta x}{\Delta t}$ is called a **difference quotient** and we conclude that it can be used to approximate the slope of the function. So how can we compute the exact slope of the function? Well, since as $\Delta t$ becomes small, the approximation gets better, we get the best result when taking the limit $\Delta t\rightarrow 0$. This means that we must have

$$
 \mathrm{velocity}=\lim_{\Delta t\rightarrow 0} \frac{\Delta x}{\Delta t}=\lim_{\Delta t\rightarrow 0} \frac{x(200+\Delta t)-x(200)}{\Delta t}.
$$

We call the value of the limit $\lim_{\Delta t\rightarrow 0} \frac{x(200+\Delta t)-x(200)}{\Delta t}$ the **derivative** of the function $x$ at $t=200$. Evaluating this limit is a bit tricky, but later we will learn some powerful tools which allow us to find

$$
 \mathrm{velocity}=\lim_{\Delta t\rightarrow 0} \frac{x(200+\Delta t)-x(200)}{\Delta t}=\frac{3\pi}{4}\approx 2.356.
$$

So we saw that our approximation by means of a difference quotient was actually correct up to at least $3$ decimal positions, which is pretty good.

(Subsec:Derivativestangent)=

## Derivatives and tangent lines

In this chapter, we will study the general concept of a derivative. The process of finding the derivative of a function is called **differentiation**. Within the field of calculus (and also in more advanced subjects like mathematical analysis), differentiation is one of the most important subjects and it will play a very important role throughout this book. In this chapter we focus both on the computation part (finding derivatives) and on the interpretation (what does a derivative say about the graph of a function?). 

::::::{prf:definition} 
:label: Def:Differentiability:Diffquot
Let $f$ be a function and consider real numbers $x$ and $h$ for which $x$ and $x+h$ are in the domain of $f$. Then we an expression of the form $\dfrac{f(x+h)-f(x)}{h}$ is called a **difference quotient**.
::::::

::::::{prf:definition} 
:label: Def:Differentiability:Derivative
Let $f$ be a function and a number $a$ in the domain of $f$. Then the **derivative** of $f$ at $a$, denoted by $f'(a)$ and pronounced as $f$-prime at $a$, is 

$$
 f'(a)=\lim\limits_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h},
$$

provided this limit exists. If the limit exists, we say that $f$ is **differentiable** in $a$.
::::::

Alternatively, we can find the derivative of $f$ by evaluating a different limit.

::::::{prf:theorem} 
:label: Thm:Differentiability:Derivativealt
Let $f$ be a function and a number $a$ in the domain of $f$. Then $f$ is differentiable at $a$ whenever the limit $\displaystyle\lim\limits_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}$ exists. Moreover, if this limit exists it is equal to $f'(a)$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Differentiability:Derivativealt`
:class: tudproof, dropdown
Let $\varepsilon>0$. Writing $x=a+h$ we have for any $\delta>0$ we have $|x-a|<\delta$ precisely when $|h|<\delta$. Moreover, we note that

$$
 \frac{f(x)-f(a)}{x-a}=\frac{f(a+h)-f(a)}{a+h-a}=\frac{f(a+h)-f(a)}{h}.
$$

This means that $\displaystyle\left|\frac{f(x)-f(a)}{x-a}-f'(a)\right|<\varepsilon$ precisely when $\displaystyle\left|\frac{f(a+h)-f(a)}{h}-f'(a)\right|<\varepsilon$. We find that the limits $\displaystyle\lim\limits_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}$ and $\displaystyle\lim\limits_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h}$ either both exist or both do not exist, and if they exist, that they must be equal.
:::

Note that for a given function $f$, we can try to evaluate the derivative at each point in the domain. This means we can interpret the derivative itself as a function again: for each $x$ for which the derivative exists, the derivative function gives the value of the derivative at that point. This gives the following definition.

::::::{prf:definition} 
:label: Def:Differentiability:Derivativefunction
The **derivative** $f'$, pronounced: $f$-prime, of a function $f$ is the function that associates to each value $x$ at which $f$ is differentiable the derivative $f'(x)$.
::::::

::::::{prf:notation} 
:label: Not:Differentiability:Derivative
Let $f$ be a function. Then the following notations all represent the derivative of $f$

$$
 f'(x)=\frac{d}{dx}f(x)=\frac{df}{dx}(x)=\frac{df(x)}{x}=Df(x).
$$

The notation $\dfrac{df}{dx}$ is called the **Leibniz notation**, named after the German philosopher and mathematician [Gottfried Wilhelm Leiniz (1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz). The notation $Df(x)$ is sometimes called the **Euler notation**, although there is no indication that the Swiss mathematician [Leonhard Euler (1707-1783)](https://en.wikipedia.org/wiki/Leonhard_Euler) ever used this notation.

In physics, when considering a quantity $y$ that is a function of **time** $t$, the notation $\dot{y}(t)$ represents the derivative of $y'(t)$
::::::

So what does the derivative represent geomtrically? For this, we need the definition of a tangent line.

::::::{prf:definition} 
:label: Def:Differentiability:Tangentline
Let $f$ be a function and let $a$ be a point in the domain of $a$ such that $f$ is differentiable at $a$. Then the tangent line of $f$ at $a$ is the straight line that goes through the point $(a,f(a))$ and has slope $f'(a)$.
::::::

The idea here is that the tangent line **touches the graph of the function at the specified point**. Indeed, consider the difference quotient $\dfrac{f(a+h)-f(a)}{h}$ for a small value of $h$. Since we can write $\dfrac{f(a+h)-f(a)}{h}=\dfrac{f(a+h)-f(a)}{(a+h)-a}$, this difference quotient is the slope of the straight line through the points $(a,f(a))$ and $(a+h,f(a+h))$. By taking taking the limit $h$ to $0$, this slope goes towards $f'(a)$, which is the slope of the tangent line. As such, we can think of the slope of the tangent line as the slope of function at the point, which means that we can also think of the derivative in this way.

Hier een applet. De functie $x^3$ moet geplot zijn, net als de lijn door $(1,1)$ en $(1+h,(1+h)^3)$ met een schuifje voor wat $h$ is (zeg $h$ tussen $-1$ en $1$).  

::::::{prf:theorem} 
:label: Thm:Differentiability:Tangentline
Let $f$ be a function and let $a$ be a point in the domain of $a$ such that $f$ is differentiable at $a$. Then the tangent line of $f$ at $a$ is given by the equation

$$
 y=f(a)+f'(a)(x-a).
$$
::::::

:::{admonition} Proof of {prf:ref}`Thm:Differentiability:Tangentline`
:class: tudproof
Notice that the equation $y=f(a)+f'(a)(x-a)$ defines a straight line with slope $f'(a)$. Moreover, it passes through the point $(a,f(a))$, since by plugging in $x=a$ we obtain

$$
 y=f(a)+f'(a)(a-a)=f(a),
$$

as desired. So this equation defines the unique line with slope $f'(a)$ that passes through $(a,f(a))$, so it must define the tangent line of $f$ at $a$. 

:::

::::::{prf:example} 
:label: Ex:Differentiability:Usinglimit
Consider the function $f(x)=x^2$. We will use the definition of find the derivative of this function. For any value of $x$ we can evaluate the limit

$$
 f'(x)=\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}=\lim_{h\rightarrow 0}\frac{(x+h)^2-x^2}{h}=\lim_{h\rightarrow 0}\frac{x^2+2xh+h^2-x^2}{h}=\lim_{h\rightarrow 0}\frac{2xh+h^2}{h}=\lim_{h\rightarrow 0}2x+h=2x+0=2x.
$$

As such, we find that the function $f(x)=x^2$ is differentiable everywhere and that the derivative is given by $f'(x)=2x$.

Hier een applet met de functie en de raaklijn aan deze functie in een door de gebruiker in te voeren punt.
::::::


::::::{prf:example} 
:label: Ex:Differentiability:Usinglimit2
Consider the function $k(t)=|t|$. We will try use the definition of find the derivative of this function, if possible. Since the limit is a bit tricky to compute in general, we will consider the derivative of $k$ at $t$ separately for $t>0$, $t<0$ and $t=0$.

First consider any $t>0$. If $h$ is close enough to $0$, we can ensure that $t+h>0$ as well. In that case, we will have $|t|=t$ and $|t+h|=t+h$. Hence, we can find the derivative by evaluating

$$
 \frac{dk}{dt}(t)=\lim_{h\rightarrow 0}\frac{k(t+h)-k(t)}{h}=\lim_{h\rightarrow 0}\frac{|t+h|-|t|}{h}=\lim_{h\rightarrow 0}\frac{t+h-t}{h}=\lim_{h\rightarrow 0}\frac{h}{h}=\lim_{h\rightarrow 0}1=1.
$$

Now we consider any $t<0$. If $h$ is close enough to $0$, we can ensure that $t+h<0$ as well. In that case, we will have $|t|=-t$ and $|t+h|=-(t+h)=-t-h$. Hence, we can find the derivative by evaluating

$$
 \frac{dk}{dt}(t)=\lim_{h\rightarrow 0}\frac{k(t+h)-k(t)}{h}=\lim_{h\rightarrow 0}\frac{|t+h|-|t|}{h}=\lim_{h\rightarrow 0}\frac{-t-h-(-t)}{h}=\lim_{h\rightarrow 0}\frac{-h}{h}=\lim_{h\rightarrow 0}-1=-1.
$$

Finally, we consider $t=0$. Here, we need to consider the left and right limits separately, because for $h<0$ we have $|0+h|=|h|=-h$, while for $h>0$ we have $|0+h|=|h|=h$. Then we find

$$
 \lim_{h\rightarrow 0^-}\frac{k(0+h)-k(0)}{h}=\lim_{h\rightarrow 0^-}\frac{|0+h|-|0|}{h}=\lim_{h\rightarrow 0^-}\frac{-h}{h}=-1
$$

and

$$
 \lim_{h\rightarrow 0^+}\frac{k(0+h)-k(0)}{h}=\lim_{h\rightarrow 0^+}\frac{|0+h|-|0|}{h}=\lim_{h\rightarrow 0^+}\frac{h}{h}=1.
$$

Since the left and right limits are unequal, we know from {prf:ref}`Theorem:LimitAtPoint:Leftrightequal` that the limit $\displaystyle\lim_{h\rightarrow 0}\frac{k(t+h)-k(t)}{h}$ does not exist.

We conclude that $k$ is differentiable at any point $t\neq0$, but that it is not differentiable at $t=0$. In addition, we have found that

$$
 \frac{dk}{dt}(t)=\left\{\begin{array}{l}-1,\qquad&\text{if }t<0, \\ 1,\qquad &\text{if }t>0.\end{array}\right.
$$

Note that this result is not unexpected. Indeed, the absolute value is a straight line with slope $-1$ for $t<0$, while it is a straight line with slope $1$ for $t>0$. In addition, at $t=0$ the function has a sharp edge, so it is not possible to determine a slope there.
::::::

From {prf:ref}`Ex:Differentiability:Usinglimit2` we deduce that not every continuous function is differentiable. Indeed, according to {prf:ref}`Theorem:Continuity:Standardfunctions`, the absolute value function is continuous, but we saw that it is not differentiable everywhere. The reverse statement is true, however, as can be seen from the following theorem.

::::::{prf:theorem} 
:label: Thm:Differentiability:Diffimpliescont
Let $f$ be a function and let $a$ be a point in the domain of $f$ such that $f$ is differentiable at $a$. Then $f$ is continuous at $a$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Differentiability:Diffimpliescont`
:class: tudproof
We set out to show that $\displaystyle \lim_{x\rightarrow a}f(x)-f(a)=0$. Since $f$ is differentiable at $a$, the limit $\displaystyle\lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}$ exists on account of {prf:ref}`Thm:Differentiability:Derivativealt`. Moreover, we can easily evaluate the limit

$$
 \lim_{x\rightarrow a}x-a=a-a=0.
$$

On account of {prf:ref}`Theorem:LimitAtPoint:Basiccomputationrules` the product of these limits exists and is equal to the product of the limits. This means that

$$
 \lim_{x\rightarrow a}f(x)-f(a)=\lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}(x-a)=\lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}\cdot\lim_{x\rightarrow a}(x-a)=f'(a)\cdot0=0.
$$

By definition, this means that $f$ is continuous at $a$.

:::

::::::{warning} 
:name: Warning:Differentiability:Diffimpliescont

The reverse statement of {prf:ref}`Theorem:LimitAtPoint:Basiccomputationrules` is not true. That is, there are functions $f$ which are continuous at a point $a$, but not differentiable at $a$, see {prf:ref}`Ex:Differentiability:Usinglimit2`.
::::::

Before we go over to computing derivatives, we need to introduce on more concept.

::::::{prf:definition} 
:label: Def:Differentiability:Differential
Let $f$ be a differentiable function and write $y=f(x)$. The notation $dx$ represents an **infinitesimal change** ("infinitely small") change in $x$. Then the **differential** $dy$ is given by

$$
 dy=f'(x)\,dx.
$$
::::::

Using the Leibniz notation $f'(x)=\frac{dy}{dx}$ we can write the differential in the form $dy=\frac{dy}{dx}\,dx$. This equation sort of seems to arise from regular calculation rules for numbers (indeed, if $a$ and $b\neq 0$ are numbers then $\frac{a}{b}b=a$), but remember that $\frac{dy}{dx}$ is not actually a fraction. It is just notation for the derivative. Moreover, since $dx$ is infinitesimal, it is not an actual number, so the usual rules of calculation do not apply. The formula $dy=\frac{dy}{dx}\,dx$ simply represents some sort of consistency in the notation that we use.

However, even though the differential is just a notation, it will pop up from time to time. It is featured most prominently in {numref}`Sec:Integration:Substitution`, where it will be used to rewrite an integral over one variable into an integral over another variable. 

::::::{warning} 
:name: Warning:Differentiability:Differential

Some authors try to give meaning to the differential by pretending $dx$ can be an actual number. However, in the way we have defined the differential, $dx$ is not a number and cannot be assigned any value. 

Still, it is useful to discuss this interpretation, since you might encounter it elsewhere. However, to avoid confusion, we use a different notation. Consider a differentiable function $f$ and let $a$ be a point in the domain of $f$. Let $\Delta x>0$ be a small number. Writing $\Delta y=f(a+\Delta x)-f(a)$, a common way to approximate $\Delta y$ is given by

$$
 \Delta y\approx f'(a)\Delta x.
$$

Indeed, the tangent line of $f$ at $a$ is given by $y=f(a)+f'(a)(x-a)$. This line goes through the point $(a+\Delta x,f(a)+f'(a)\Delta x)$, so on the tangent line we have if $x$ changes from $a$ to $a+\Delta x$ that $y$ changes from $f(a)$ to $f(a)+f'(a)\Delta x$. The difference between these two values is exactly $f'(a)\Delta x$. So the idea here is that the difference between $f(a+\Delta x)$ and $f(a)$ can be approximated by the difference between the points of the tangent line at $a$ with $x$-values $x=a+\Delta x$ and $x=a$, see the picture below.

As such, authors we do not use our definition of a differential might say that the differential has the interpretation that if $x$ changes by $dx$, $y=f(x)$ will change by $dy=f'(x)dx$.

```{figure} Images/differential.png
---
width: 100%
name: Fig:Differentiability:Differential
class: dark-light
---
Hier een mooiere versie van dit plaatje.
```
::::::

(Subsec:Derivativestangent)=

## Computation rules and standard derivatives

In this section we will study some basic computation rules for derivatives. However, some important computation rules will be left for the upcoming sections {numref}`Section:Chainrule1d` and {numref}`Section:DiffProdQuot`. In addition, although we will provide some derivatives of standard functions here (power functions, the sine, cosine and the natural exponential function), we will leave others to later sections. For derivatives of other exponential functions, see {numref}`Section:Chainrule1d`, for the derivative of the tangent function, see {numref}`Section:DiffProdQuot` and for the derivatives of logarithms and inverse trigonometric functions, see {numref}`Subsec:Invdiff`.

::::::{prf:theorem} Scalar products and sums
:label: Thm:Differentiability:Sumscalar
Let $f$ be a function and let $a$ be a point in the domain of $f$ such that $f$ is differentiable at $a$. Let $c$ be a real number. Then the function $cf$ is also differentiable at $a$ and we have

$$
 (cf)'(a)=cf'(a).
$$

In addition, if $g$ is another function such that $g$ is differentiable at $a$, then $f+g$ is differentiable at $a$ and we have

$$
 (f+g)'(a)=f'(a)+g'(a).
$$
::::::

:::{admonition} Proof of {prf:ref}`Thm:Differentiability:Sumscalar`
:class: tudproof
Because of {prf:ref}`Theorem:LimitAtPoint:Basiccomputationrules` we find that

$$
 \lim_{h\rightarrow 0}\frac{(cf)(x+h)-(cf)(x)}{h}=\lim_{h\rightarrow 0}\frac{c\left(f(x+h)-f(x)\right)}{h}=c\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}=cf'(a).
$$

This means that $cf$ is also differentiable at $a$ and that $(cf)'(a)=cf'(a)$.

Similarly, we find that

$$
 \lim_{h\rightarrow 0}\frac{(f+g)(x+h)-(f+g)(x)}{h}=\lim_{h\rightarrow 0}\frac{f(x+h)+g(x+h)-f(x)-g(x)}{h}=\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}+\lim_{h\rightarrow 0}\frac{g(x+h)-g(x)}{h}=f'(a)+g'(a).
$$

This means that $f+g$ is also differentiable at $a$ and that $(f+g)'(a)=f'(a)+g'(a)$.

:::

In this section we cover:

- Slopes and derivatives and graphs
- Notation, including differential notation
- Differentiability (including limit definition, also including theorem differentiable implies continuous)
- Derivatives of elemental functions (powers of x, sin, cos, e^x)
- Sums and scalar multiples
- Tangent line
- Higher-order derivatives