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
 \mathrm{average}\,\,\mathrm{velocity}=\frac{\Delta x}{\Delta t}=\frac{x(1200)-x(0)}{1200-0}=\frac{600-0}{1200}=\frac{1}{2}.
$$

An important question now remains: can we somehow determine our velocity at a certain moment in time, say at $t=200$? Note that we are not walking with a constant velocity, so very likely at most point in time the velocity is not going to be equal to the average velocity of $\frac{1}{2}$ meters per second. The main idea to resolve this, is that if just zoom in very close to $t=200$, the graph of the function is approximately a straight line. The velocity at $t=200$ can then be approximated by dividing the difference in position by the difference in time. For $\Delta t=10$, we would be comparing the positions at $t=200$ with the one $10$ time steps further, so at $t=210$, and we would obtain

$$
 \mathrm{velocity}\approx \frac{\Delta x}{\Delta t}=\frac{x(210)-x(200)}{1}\approx 2.354.
$$

If we zoom in more, we should get a better approximation. Repeating these steps for $\Delta t=1$, we would obtain

$$
 \mathrm{velocity}\approx \frac{\Delta x}{\Delta t}=\frac{x(201)-x(200)}{1}\approx 2.356.
$$

So we can say that the velocity at $t=200$ is approximately equal to $2.356$ meter per second and by taking $\Delta t$ smaller, we get a better and better result. As before, the velocity can be thought of as the slope of the function at this point in time.

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

This means that for any number $L$ we have $\displaystyle\left|\frac{f(x)-f(a)}{x-a}-L\right|<\varepsilon$ precisely when $\displaystyle\left|\frac{f(a+h)-f(a)}{h}-L\right|<\varepsilon$. We find that the limits $\displaystyle\lim\limits_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}$ and $\displaystyle\lim\limits_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h}$ either both exist or both do not exist, and if they exist, that they must be equal.
:::

Note that for a given function $f$, we can try to evaluate the derivative at each point in the domain. This means we can interpret the derivative itself as a function again: for each $x$ for which the derivative exists, the derivative function gives the value of the derivative at that point. This gives the following definition.

::::::{prf:definition} 
:label: Def:Differentiability:Derivativefunction
The **derivative** $f'$, pronounced: $f$-prime, of a function $f$ is the function that associates to each value $x$ at which $f$ is differentiable the derivative $f'(x)$. The process of finding a derivative of a function is called **differentiating** the function.
::::::

::::::{prf:notation} 
:label: Not:Differentiability:Derivative
Let $f$ be a function. Then the following notations all represent the derivative of $f$

$$
 f'(x)=\frac{d}{dx}f(x)=\frac{df}{dx}(x)=\frac{df(x)}{dx}=Df(x).
$$

The notation $\dfrac{df}{dx}$ is called the **Leibniz notation**, named after the German philosopher and mathematician [Gottfried Wilhelm Leiniz (1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz). The notation $Df(x)$ is sometimes called the **Euler notation**, although there is no indication that the Swiss mathematician [Leonhard Euler (1707-1783)](https://en.wikipedia.org/wiki/Leonhard_Euler) ever used this notation.

In physics, when considering a quantity $y$ that is a function of **time** $t$, the notation $\dot{y}(t)$ represents the derivative $y'(t)$
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
Consider the function $f(x)=x^2$. We will use the definition of the derivative to find the derivative of this function. For any value of $x$ we can evaluate the limit

$$
 f'(x)=\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}=\lim_{h\rightarrow 0}\frac{(x+h)^2-x^2}{h}=\lim_{h\rightarrow 0}\frac{x^2+2xh+h^2-x^2}{h}=\lim_{h\rightarrow 0}\frac{2xh+h^2}{h}=\lim_{h\rightarrow 0}2x+h=2x+0=2x.
$$

As such, we find that the function $f(x)=x^2$ is differentiable everywhere and that the derivative is given by $f'(x)=2x$.

Hier een applet met de functie en de raaklijn aan deze functie in een door de gebruiker in te voeren punt.
::::::

::::::{prf:example} 
:label: Ex:Differentiability:Usinglimit2
Consider the function $f(x)=x^{\frac{1}{3}}$. We will try to use the definition of the derivative to find the derivative of this function at $0$. We can rewrite the limit to

$$
 \lim_{h\rightarrow 0}\frac{f(0+h)-f(0)}{h}=\lim_{h\rightarrow 0}\frac{h^{\frac{1}{3}}-0}{h}=\lim_{h\rightarrow 0}h^{-\frac{2}{3}},
$$

which is a limit that does not exist (the function $g(h)=h^{-\frac{2}{3}}$ has a vertical asymptote at $h=0$). So the function is not differentiable at $h=0$. 

We will see later that this function is differentiable at any other point and that $f'(x)=\frac{1}{3}x^{-\frac{2}{3}}$ for $x\neq 0$. The idea here is that the tangent lines of the function at $a$ become steeper and steeper as $a\rightarrow 0$. In some sense, the function $f$ has a **vertical tangent line** at $x=0$ (althought this is not a tangent line in the sense of {prf:ref}`Def:Differentiability:Tangentline`). Whenever a fuction has a vertical tangent line at a point, it will not be differentiable at this point (otherwise its derivative would need to $\infty$ or $-\infty$ at that point, but $\infty$ or $-\infty$ are not numbers, so a derivative can never have one of these values)

Hier een applet met de functie, de verticale 'raaklijn' rond 0 en de raaklijn aan deze functie in een door de gebruiker in te voeren punt.
::::::


::::::{prf:example} 
:label: Ex:Differentiability:Usinglimit3
Consider the function $k(t)=|t|$. We will try use the definition of the derivative to find the derivative of this function, if possible. Since the limit is a bit tricky to compute in general, we will consider the derivative of $k$ at $t$ separately for $t>0$, $t<0$ and $t=0$.

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

Note that this result is not unexpected. Indeed, the absolute value is a straight line with slope $-1$ for $t<0$, while it is a straight line with slope $1$ for $t>0$. In addition, at $t=0$ the function has a sharp corner, so it is not possible to determine a slope there.
::::::

From {prf:ref}`Ex:Differentiability:Usinglimit3` we deduce that not every continuous function is differentiable. Indeed, according to {prf:ref}`Theorem:Continuity:Standardfunctions`, the absolute value function is continuous, but we saw that it is not differentiable everywhere. The reverse statement is true, however, as can be seen from the following theorem.

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

On account of {prf:ref}`Theorem:LimitAtPoint:Basiccomputationrules` the limit of the product of these functions exists and is equal to the product of the limits. This means that

$$
 \lim_{x\rightarrow a}f(x)-f(a)=\lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}(x-a)=\lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}\cdot\lim_{x\rightarrow a}(x-a)=f'(a)\cdot0=0.
$$

By definition, this means that $f$ is continuous at $a$.

:::

::::::{warning} 
:name: Warning:Differentiability:Diffimpliescont

The reverse statement of {prf:ref}`Thm:Differentiability:Diffimpliescont` is not true. That is, there are functions $f$ which are continuous at a point $a$, but not differentiable at $a$, see {prf:ref}`Ex:Differentiability:Usinglimit3`.
::::::

In fact, we have now seen the most typical ways a function can fail to be differentiable at a point $a$: the function has a sharp corner at $a$ (see {prf:ref}`Ex:Differentiability:Usinglimit3`), it has a vertical asymptote at $a$ (see {prf:ref}`Ex:Differentiability:Usinglimit2`) or it is not continuous at $a$. A mathematician can provide you with examples that do not necessarily look like on of these three cases (such as the [Weierstrass function](https://en.wikipedia.org/wiki/Weierstrass_function)), but in practice, most nondifferentiable functions will be of one of these three forms.

```{figure} Images/majorcasesnondiff.png
---
width: 100%
name: Fig:Differentiability:majorcasesnondiff
class: dark-light
---
Hier een mooiere versie van dit plaatje.
```

The derivative of a differentiable function does not need to be continuous. For instance, we will see in {prf:ref}`Def:Differentiability:Higherorderderivative3` that the function $f(x)=\left\{\begin{array}{l}0,\qquad&\text{if}\,x\leq 0,\\ 2x,\qquad &\text{if}\,x>0.\end{array}\right.$ is differentiable, but not continuously differentiable. Since "a differentiable function for which the derivative is continuous" is such a mouthful, we give this concept a name.

::::::{prf:definition} 
:label: Def:Differentiability:ContDiff
A function $f$ is called **continuously differentiable** if it is differentiable and the derivative $f'$ is continuous.
::::::

Before we go over to computing derivatives, we need to introduce on more concept.

::::::{prf:definition} 
:label: Def:Differentiability:Differential
Let $f$ be a differentiable function and write $y=f(x)$. The notation $dx$ represents an **infinitesimal change** ("infinitely small") change in $x$. Then the **differential** $dy$ is given by

$$
 dy=f'(x)\,dx.
$$
::::::

Using the Leibniz notation $f'(x)=\frac{dy}{dx}$ we can write the differential in the form $dy=\frac{dy}{dx}\,dx$. This equation sort of seems to arise from regular calculation rules for numbers (indeed, if $a$ and $b\neq 0$ are numbers then $\frac{a}{b}b=a$), but remember that $\frac{dy}{dx}$ is not actually a fraction. It is just notation for the derivative. Moreover, since $dx$ is infinitesimal, it is not an actual number, so the usual rules of calculation do not apply. The formula $dy=\frac{dy}{dx}\,dx$ simply represents consistency in the notation that we use.

However, even though the differential is just a notation, it will pop up from time to time. It is featured most prominently in {numref}`Sec:Integration:Substitution`, where it will be used to rewrite an integral over one variable into an integral over another variable. 

::::::{warning} 
:name: Warning:Differentiability:Differential

Some authors try to give meaning to the differential by pretending $dx$ can be an actual number. However, in the way we have defined the differential, $dx$ is not a number and cannot be assigned any value. 

Still, it is useful to discuss this interpretation, since you might encounter it elsewhere. However, to avoid confusion, we use a different notation. Consider a differentiable function $f$ and let $a$ be a point in the domain of $f$. Let $\Delta x>0$ be a small number. Writing $\Delta y=f(a+\Delta x)-f(a)$, a common way to approximate $\Delta y$ is given by

$$
 \Delta y\approx f'(a)\Delta x.
$$

Indeed, the tangent line of $f$ at $a$ is given by $y=f(a)+f'(a)(x-a)$. This line goes through the point $(a+\Delta x,f(a)+f'(a)\Delta x)$, so on the tangent line we have if $x$ changes from $a$ to $a+\Delta x$ that $y$ changes from $f(a)$ to $f(a)+f'(a)\Delta x$. The difference between these two values is exactly $f'(a)\Delta x$. So the idea here is that the difference between $f(a+\Delta x)$ and $f(a)$ can be approximated by the difference between the points of the tangent line at $a$ with $x$-values $x=a+\Delta x$ and $x=a$, see the picture below.

As such, authors who do not use our definition of a differential might say that the differential has the interpretation that if $x$ changes by $dx$, $y=f(x)$ will change by $dy=f'(x)dx$.

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

In this section we will study some basic computation rules for derivatives. However, some important computation rules will be left for the upcoming sections {numref}`Sec:Differentiation:ChainRule` and {numref}`Section:DiffProdQuot`. In addition, although we will provide some derivatives of standard functions here (polynomials, the sine, cosine and the natural exponential function), we will leave others to later sections. For derivatives of other exponential functions, see {numref}`Sec:Differentiation:ChainRule`, for the derivative of the tangent function, see {numref}`Section:DiffProdQuot` and for the derivatives of logarithms, inverse trigonometric functions and power functions, see {numref}`Subsec:Invdiff`.

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

{prf:ref}`Thm:Differentiability:Sumscalar` allows us to find derivatives of linear combinations of functions of which we know the derivative. However, for this to work, we need have the derivatives of at least some functions ready to use. Indeed, needing to find the derivative of a function using the limit definition is rather tedious. For this, we now provide the derivatives of some standard functions. It is highly recommended to know these by heart.

::::::{prf:theorem} Standard derivatives, part 1 out of 4
:label: Thm:Differentiability:Standard1
We have the following standard derivatives.

- If $n$ is an integer, then $\dfrac{d}{dx}\left[x^n\right]=nx^{n-1}$. In particular, we have $\dfrac{d}{dx}\left[1\right]=0$, $\dfrac{d}{dx}\left[x\right]=1$ and $\dfrac{d}{dx}\left[x^2\right]=2x$ and, if $n\geq 1$, we have $\dfrac{d}{dx}\left[\frac{1}{x^n}\right]=\dfrac{d}{dx}\left[x^{-n}\right]=-nx^{-n-1}$.
- We have $\dfrac{d}{dx}\left[\sqrt{x}\right]=\frac{1}{2\sqrt{x}}$ for $x>0$.
- We have $\dfrac{d}{dx}\left[\sin(x)\right]=\cos(x)$ and $\dfrac{d}{dx}\left[\cos(x)\right]=-\sin(x)$.
- We have $\dfrac{d}{dx}\left[e^x\right]=e^x$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Differentiability:Standard1`
:class: tudproof, dropdown
First we consider the case $n=0$. Then $f(x)=x^0=1$ and we can directly evaluate the derivative using the limit definition

$$
 f'(x)=\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}=\lim_{h\rightarrow 0}\frac{1-1}{h}=\lim_{h\rightarrow 0}0=0.
$$

So we find that $f'(x)=0$ for all $x$. This is equal to the expression in the theorem, since $nx^{n-1}=0\cdot x^{0-1}=0$.

Next, we consider the case $n=1$. Then $f(x)=x^1=x$ and, again, we can directly evaluate the derivative using the limit definition

$$
 f'(x)=\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}=\lim_{h\rightarrow 0}\frac{x+h-x}{h}=\lim_{h\rightarrow 0}\frac{h}{h}=\lim_{h\rightarrow 0}1=1.
$$

So we find that $f'(x)=1$ for all $x$. This is equal to the expression in the theorem, since $nx^{n-1}=1\cdot x^{1-1}=x^0=1$.

Let $n>1$ be a natural number and consider the function $f(x)=x^n$. Consider any real number $a$. We will use the limit from {prf:ref}`Thm:Differentiability:Derivativealt` to find the derivative $f'(a)$. This means that we need to evaluate the limit

$$
 \lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}=\lim_{x\rightarrow a}\frac{x^n-a^n}{x-a}.
$$

Now we use a common trick to rewrite $x^n-a^n$. Indeed, we can compute

$$
 \begin{array}{lcl}(x-a)\left(a^{n-1}+a^{n-2}x+a^{n-3}x^2+...+ax^{n-2}+x^{n-1}\right)&=&x\left(a^{n-1}+a^{n-2}x+a^{n-3}x^2+...+ax^{n-2}+x^{n-1}\right)-a\left(a^{n-1}+a^{n-2}x+a^{n-3}x^2+...+ax^{n-2}+x^{n-1}\right)\\
 &=&\left(a^{n-1}x+a^{n-2}x^2+a^{n-3}x^3+...+ax^{n-1}+x^{n}\right)-\left(a^{n}+a^{n-1}x+a^{n-2}x^2+...+a^2x^{n-2}+ax^{n-1}\right)\\
 &=&x^n-a^n.\end{array}
$$

We use this formula to evaluate the limit. Indeed, we find

$$
 \begin{array}{lcl}f'(a)&=&\displaystyle\lim_{x\rightarrow a}\frac{x^n-a^n}{x-a}\\
 &=&\displaystyle\lim_{x\rightarrow a}\frac{(x-a)\left(a^{n-1}+a^{n-2}x+a^{n-3}x^2+...+ax^{n-2}+x^{n-1}\right)}{x-a}\\
 &=&\displaystyle\lim_{x\rightarrow a}\left(a^{n-1}+a^{n-2}x+a^{n-3}x^2+...+ax^{n-2}+x^{n-1}\right)\\
 &=&\displaystyle a^{n-1}+a^{n-2}a+a^{n-3}a^2+...+aa^{n-2}+a^{n-1}\\
 &=&\displaystyle\underbrace{a^{n-1}+...+a^{n-1}}_{n\text{ times}}\\
 &=&\displaystyle na^{n-1}.\end{array}
$$

So $f$ is differentiable in $a$ and we find $f'(a)=na^{n-1}$. 

Finally we let $n\geq 1$ and consider the function $f(x)=x^{-n}$. Consider any real number $a\neq 0$. We will use the limit from {prf:ref}`Thm:Differentiability:Derivativealt` to find the derivative $f'(a)$. This means that we need to evaluate the limit

$$
 \lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}=\lim_{x\rightarrow a}\frac{\frac{1}{x^n}-\frac{1}{a^n}}{x-a}=\lim_{x\rightarrow a}\frac{a^n-x^n}{\left(x-a\right)x^na^n}.
$$

Previously in this proof, we showed that $(x-a)\left(a^{n-1}+a^{n-2}x+a^{n-3}x^2+...+ax^{n-2}+x^{n-1}\right)=x^n-a^n$. So we can use this to evaluate the limit and we find

$$
 \begin{array}{lcl} \lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}&=&\lim_{x\rightarrow a}\frac{a^n-x^n}{\left(x-a\right)x^na^n}\\
 &=&\lim_{x\rightarrow a}\frac{-(x-a)\left(a^{n-1}+a^{n-2}x+a^{n-3}x^2+...+ax^{n-2}+x^{n-1}\right)}{\left(x-a\right)x^na^n}\\
 &=&\lim_{x\rightarrow a}\frac{-\left(a^{n-1}+a^{n-2}x+a^{n-3}x^2+...+ax^{n-2}+x^{n-1}\right)}{x^na^n}\\
 &=&\frac{-\left(a^{n-1}+a^{n-2}a+a^{n-3}a^2+...+aa^{n-2}+a^{n-1}\right)}{a^na^n}\\
 &=&\frac{-na^{n-1}}{a^2n}\\
 &=&-na^{-n-1}.\end{array}
$$

So $f$ is differentiable in $a$ and we find $f'(a)=-na^{n-1}$. 

Now, we consider the function $f(x)=\sqrt{x}$. Then for any $x>0$ we can evaluate

$$
 \begin{array}{lcl}f'(x)&=&\displaystyle\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{\sqrt{x+h}-\sqrt{x}}{h}.\end{array}
$$

In order to evaluate this limit, we use the square root trick (see {numref}`Subsec:Limitsrules`) and we obtain

$$
 \begin{array}{lcl}f'(x)&=&\displaystyle\lim_{h\rightarrow 0}\frac{\sqrt{x+h}-\sqrt{x}}{h}\frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{h}{h\left(\sqrt{x+h}+\sqrt{x}\right)}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{1}{\left(\sqrt{x+h}+\sqrt{x}\right)}\\
 &=&\frac{1}{\sqrt{x+0}+\sqrt{x}}\\
 &=&\frac{1}{2\sqrt{x}}.\end{array}
$$

In the final step we used the continuity of the function $f$. Hence, we obtain $f'(x)=\dfrac{1}{2\sqrt{x}}$, as desired.

Next, we consider the function $f(x)=\sin(x)$. Then for any value of $x$ we can use the addition formula for the sine {prf:ref}`Thm:Trigonometry:AdditionSubtractionFormulas` to compute

$$
 \begin{array}{lcl}f'(x)&=&\displaystyle\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{\sin(x+h)-\sin(x)}{h}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{\sin(x)\cos(h)+\cos(x)\sin(h)-\sin(x)}{h}\\
 &=&\displaystyle\sin(x)\lim_{h\rightarrow 0}\frac{\cos(h)-1}{h}+\cos(x)\lim_{h\rightarrow 0}\frac{\sin(h)}{h}.\end{array}
$$

So in order to find the derivative of the sine, we need to evaluate the two limits $\displaystyle\lim_{h\rightarrow 0}\frac{\cos(h)-1}{h}$ and $\displaystyle\frac{\sin(h)}{h}$. We first evaluate the second of these two limits and for this, we first consider the right limit, which we evaluate using the squeeze theorem. From the proof of {prf:ref}`Theorem:Continuity:Standardfunctions`, we recall that $\sin(h)\leq h$ for any $0<h<\frac{\pi}{2}$. This inequality can be rewritten as $\frac{\sin(h)}{h}\leq 1$ for any $0<h<\frac{\pi}{2}$. In order to find a lower bound on the function $\frac{\sin(h)}{h}$, we will fix $0<h<\frac{\pi}{2}$ show that $h\leq \tan(h)$.  For this, consider the triangle shown in {numref}`Fig:Differentiability:tanhgreaterh`. The point $A$ lies on the circle with center at the origin and radius $1$. The point $B$ is the point directly above $A$ such that the angle between $OA$ and $OB$ is $h$. The line segment $OB$ intersect the circle at the point $C$. The point $D$ is chosen on the line segement $AB$ in such a way that the line segments $CD$ and $CB$ make a right angle.

```{figure} Images/tanhgreaterh.png
---
width: 100%
name: Fig:Differentiability:tanhgreaterh
class: dark-light
---
Hier een mooiere versie van dit plaatje.
```

Recall that the lenght of the part of the circle from $A$ to $C$ is equal to $h$. Indeed, the full circumference of the circle is $2\pi$, so since we only consider $\frac{h}{2\pi}$ part of this, the length of this piece is $\frac{h}{2\pi}2\pi=h$. From the picture, we immediately see that the this length is less than the sum of the distances $|AD|+|CD|$. Since the line segments $CD$ and $CB$ make a right angle, it follows from the Pythagorean theorem that $|CD|\leq |BD|$. As such, we find

$$
 \begin{array}{lcl}h&\leq&|AD|+|DC|\\
 &\leq &|AD|+|BD|\\
 &=&|AB|\\
 &=&|OA|\tan(h)\\
 &=&\tan(h),\end{array}
$$

as desired. This means that for $0<h<\frac{\pi}{2}$ we have 

$$
 h\leq \tan(h)=\frac{\sin(h)}{\cos(h)}\qquad \Longleftrightarrow\qquad \cos(h)\leq \frac{\sin(h)}{h}.
$$

Combining all inequalities that we have found so far, we find that for $0<h<\frac{\pi}{2}$ we have 

$$
 \cos(h)\leq \frac{\sin(h)}{h}\leq 1.
$$

Since the cosine is continuous, we know that $\displaystyle\lim_{h\rightarrow 0^+}\cos(h)=\cos(0)=1$ and of course we also have $\displaystyle\lim_{h\rightarrow 0^+}1=1$. So by the squeeze theorem, we find that $\displaystyle\lim_{h\rightarrow 0^+}\frac{\sin(h)}{h}=1$. Note that $\displaystyle\frac{\sin(-h)}{-h}=\frac{-\sin(h)}{-h}=\frac{\sin(h)}{h}$, so the left limit must be equal to the right limit, i.e. $\displaystyle\lim_{h\rightarrow 0^-}\frac{\sin(h)}{h}=\displaystyle\lim_{h\rightarrow 0^+}\frac{\sin(h)}{h}=1$. This means that we have $\displaystyle\lim_{h\rightarrow 0}\frac{\sin(h)}{h}=1$ as well, as desired.

Luckily, the other limit $\displaystyle\lim_{h\rightarrow 0}\frac{\cos(h)-1}{h}$ is slightly less involved (at least, now that we have established $\displaystyle\lim_{h\rightarrow 0}\frac{\sin(h)}{h}=1$). By multiplying both parts of the fraction with $\cos(h)+1$ and using {prf:ref}`Thm:Trigonometry:UnitCircleIdentity`, we find that

$$
 \begin{array}{lcl} \displaystyle\lim_{h\rightarrow 0}\frac{\cos(h)-1}{h}&=&\displaystyle\lim_{h\rightarrow 0}\frac{\left(\cos(h)-1\right)\left(\cos(h)+1\right)}{h\left(\cos(h)+1\right)}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{\cos^2(h)-1}{h\left(\cos(h)+1\right)}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{-\sin^2(h)}{h\left(\cos(h)+1\right)}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{\sin(h)}{h}\cdot\lim_{h\rightarrow 0}\frac{-\sin(h)}{\cos(h)+1}\\
 &=&\displaystyle1\cdot \lim_{h\rightarrow 0}\frac{-\sin(h)}{\cos(h)+1}\\
 &=&\displaystyle1\cdot\frac{-\sin(0)}{\cos(0)+1}\\
 &=&0.\end{array}
$$

Now that we have finally established the two necessary limits, we can finish the computation of the derivative of $f(x)=\sin(x)$. Indeed, we obtain

$$
 \begin{array}{lcl}f'(x)&=&\displaystyle\sin(x)\lim_{h\rightarrow 0}\frac{\cos(h)-1}{h}+\cos(x)\lim_{h\rightarrow 0}\frac{\sin(h)}{h}\\
 &=&\sin(x)\cdot 0+\cos(x)\cdot 1\\
 &=&\cos(x),\end{array}
$$

as desired. 

The derivative of $g(x)=\cos(x)$ follows similarly (but we have done most of the hard work already). Here, we obtain

$$
 \begin{array}{lcl}g'(x)&=&\displaystyle\lim_{h\rightarrow 0}\frac{g(x+h)-g(x)}{h}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{\cos(x+h)-\cos(x)}{h}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{\cos(x)\cos(h)-\sin(x)\sin(h)-\cos(x)}{h}\\
 &=&\displaystyle\cos(x)\lim_{h\rightarrow 0}\frac{\cos(h)-1}{h}-\sin(x)\lim_{h\rightarrow 0}\frac{\sin(h)}{h}\\
 &=&\displaystyle\cos(x)\cdot 0-\sin(x)\cdot 1\\
 &=&-\sin(x).\end{array}
$$

Finally, we will find the derivative of the natural exponential function $f(x)=e^x$. For any value of $x$ we find that

$$
 \begin{array}{lcl}f'(x)&=&\displaystyle\lim_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{e^{x+h}-e^x}{h}\\
 &=&\displaystyle\lim_{h\rightarrow 0}\frac{e^{x}e^h-e^x}{h}\\
 &=&\displaystyle e^x \lim_{h\rightarrow 0}\frac{e^h-1}{h}.\end{array}
$$

Now from {prf:ref}`Thm:RealNumbers:Numbere`, we recall that the final limit was one of the defining properties of the number $e$. As such, we find that $f'(x)=e^x$, as desired.
:::

::::::{prf:remark}
:label: Remark:Differentiability:Powerfunctions

Derivatives of power functions of the form $f(x)=x^r$ for $r$ any real number follow a very similar pattern to those given in {prf:ref}`Thm:Differentiability:Standard1`. However, in order to prove that, we need some more advanced tools, so we will postpone finding the derivatives of these functions.

::::::

::::::{prf:example} 
:label: Ex:Differentiability:Usingrules
Consider the function $f(x)=6x^3+5x-4$. We will find the derivative of this function using the basic computation rules {prf:ref}`Thm:Differentiability:Sumscalar` and the standard derivatives {prf:ref}`Thm:Differentiability:Standard1`. First, we note that we have

$$
 f'(x)=\frac{d}{dx}\left[6x^3+5x^2-4\right]=6\frac{d}{dx}\left[x^3\right]+5\frac{d}{dx}\left[x^2\right]-4\frac{d}{dx}\left[1\right].
$$

Each of the derivatives of $x^3$, $x^2$ and $1$ are standard derivatives, and we find

$$
 f'(x)=6\frac{d}{dx}\left[x^3\right]+5\frac{d}{dx}\left[x^2\right]-4\frac{d}{dx}\left[1\right]=6\left(3x^{3-1}\right)+5\left(2x^{2-1}\right)-4\cdot 0=18x^2+10x.
$$
::::::

::::::{prf:example} 
:label: Ex:Differentiability:Usingrules2
Consider the function $h(t)=2\cos(t)-3\sin(t)$. We will find the derivative of this function using the basic computation rules {prf:ref}`Thm:Differentiability:Sumscalar` and the standard derivatives {prf:ref}`Thm:Differentiability:Standard1`. First, we note that we have

$$
 h'(t)=\frac{d}{dt}\left[2\cos(t)-3\sin(t)\right]=2\frac{d}{dt}\left[\cos(t)\right]-3\frac{d}{dt}\left[\sin(t)\right].
$$

As we know the derivatives of $\cos(t)$ and $\sin(t)$, we find

$$
 h'(t)=2\frac{d}{dt}\left[\cos(t)\right]-3\frac{d}{dt}\left[\sin(t)\right]=2(-\sin(t))-3(\cos(t))=-2\sin(t)-3\cos(t).
$$
::::::

::::::{prf:example} 
:label: Ex:Differentiability:Usingrulespiecewise
Consider the piecewise defined function $\displaystyle f(x)=\left\{\begin{array}{l}x^5,\qquad &\text{if}\,x<0,\\ x^2,\qquad &\text{if}\,0\leq x<1,\\ -2x,\qquad&\text{if}\,x\geq 1.\end{array}\right.$ For $x<0$, we have $f(x)=x^5$ and since differentiability is a 'local' property (i.e. whether $f'(a)$ exists only depends of the behaviour of $f(x)$ for $x$ close to $a$), we find that $f'(x)=5x^4$ for these values of $x$. Similarly, we find that $f'(x)=2x$ for $0<x<1$ and $f'(x)=-2$ for $x>1$. To see what happens at $x=0$ and at $x=1$, we have no choice but to use the limit definition. For both points, we need to evaluate the corresponding left and right limits in the definition of the derivative separately. For $x=0$, we obtain

$$
 \lim_{h\rightarrow 0^-}\frac{f(h)-f(0)}{h}=\lim_{h\rightarrow 0^-}\frac{h^5-0}{h}=\lim_{h\rightarrow 0^-}h^4=0
$$

and

$$
 \lim_{h\rightarrow 0^+}\frac{f(h)-f(0)}{h}=\lim_{h\rightarrow 0^+}\frac{h^2-0}{h}=\lim_{h\rightarrow 0^-}h=0.
$$

Since the left and right limits are equal, the total limit exists and we find that $f'(0)=\displaystyle \lim_{h\rightarrow 0}\frac{f(h)-f(0)}{h}=0$.

For $x=1$, we obtain on the other hand

$$
 \lim_{h\rightarrow 1^-}\frac{f(1+h)-f(1)}{h}=\lim_{h\rightarrow 0^-}\frac{(1+h)^2-(-2)}{h}=\lim_{h\rightarrow 0^-}\frac{1+2h+h^2+2}{h}=\lim_{h\rightarrow 0^-}\frac{3+2h+h^2}{h},
$$

which does not exist (the limit $\lim_{h\rightarrow 1^+}\frac{f(1+h)-f(1)}{h}$ does exist and is equal to to $-2$). So this means that $f$ is not differentiable in $x=1$. We could have seen this coming, since the function is also not continuous at $x=1$, so it had no cahnce of being differentiable on account of {prf:ref}`Thm:Differentiability:Diffimpliescont`.
::::::

## Higher order derivatives

If, just like in the example from {numref}`Subsec:Differentiabilityintro`, position $x$ is given as a function of time $t$, then we saw that the derivative of $x$ with respect to $t$ represents the velocity. Note that this velocity is a function of time itself, since at each point in time we can determine the velocity. So we now might wonder, does this velocity have a derivative itself and if so, what does it represent? Since the derivative represents the rate of change of a quantity, the derivative of the velocity should represent the rate at which the velocity changes with respect to time. This is precisely the **acceleration**. So in order to find the acceleration, we can take the position and differentiate twice with respect to time. We say that the acceleration is the **second derivative** of the position.

In general, whenever we have a differentiable function $f$, the derivative $f'$ is also a function, so we can try to differentiate that one as well. If the derivative $f'$ is differentiable, we obtain the second derivative, which we can denote by $f''$. There is no reason to stop there. Whenever the second derivative is differentiable again, we can differentiate yet again to obtain the third derivative, and so on.


::::::{prf:definition} 
:label: Def:Differentiability:Higherorderderivative
If the derivative $f'$ is differentiable, then its derivative $(f')'$ is called the **second derivative** of $f$ and is denoted by $f''$. If the second derivative exists, we say that $f$ is **twice differentiable**.

Similarly, if the second derivative is again differentiable, its derivative is called the **third derivative** of $f$ and is denoted by $f^{(3)}$. If the third derivative exists, we say that $f$ is **three times differentiable**.

In general, if $n>0$ is a nonzero natural number, then the $n$th derivative of $f$ is the derivative of the $(n-1)$st derivative and is denoted by $f^{(n)}$. If the $n$th derivative exists, we say that $f$ is **$n$ times differentiable**.
::::::

The prime notation is only customary for the first and second derivatives (and sometimes the third derivative), but not for higher order derivatives, since that notation would come down to counting a lot of primes.

::::::{prf:notation} 
:label: Not:Differentiability:Higherorderderivative
Let $f$ be a function and $n>0$ a nonzero natural number. Then the following notations all represent the $n$th derivative of $f$

$$
 f^{(n)}(x)=\frac{d^n}{dx^n}f(x)=\frac{d^nf}{dx^n}(x)=\frac{d^nf(x)}{dx^n}=D^nf(x).
$$


In physics, when considering a quantity $y$ that is a function of **time** $t$, the notation $\ddot{y}(t)$ represents the second derivative $y''(t)$.
::::::

For notational convenience, specifically when considering Taylor polynomials (see {numref}`Sec:Taylor polynomials`), we also introduce the concept of a zeroth derivative, which is just the function itself.

::::::{prf:definition} 
:label: Def:Differentiability:Higherorderderivative
For any function $f$, the **zeroth derivative** of $f$, is the function itself. We write $\displaystyle f^{(0)}=\frac{d^0}{dx^0}f=D^0f=f$.
::::::

::::::{prf:example} 
:label: Def:Differentiability:Higherorderderivative1
Consider the function $g(t)=-3\cos(t)+4t^3-t$. Using the basic computation rules {prf:ref}`Thm:Differentiability:Sumscalar` and the standard derivatives {prf:ref}`Thm:Differentiability:Standard1` we find that

$$
\frac{dg}{dt}=-3\frac{d\cos(t)}{dt}+4\frac{dt^3}{dt}-\frac{dt}{dt}=-3(-\sin(t))+4(3t^{3-1})-1=-3\sin(t)+12t^2-1.
$$

The resulting function is again differentiable and we obtain

$$
\frac{d^2g}{dt^2}=\frac{d}{dt}\left[\frac{dg}{dt}\right]=-3\frac{d\sin(t)}{dt}+12\frac{dt^2}{dt}-\frac{d1}{dt}=-3\cos(t)+12(2t^{2-1})-0=-3\cos(t)+24t.
$$
::::::

::::::{prf:example} 
:label: Def:Differentiability:Higherorderderivative2
Consider the function $h(\theta)=\sin(\theta)$. Then we find $h'(\theta)=\cos(\theta)$, $h''(\theta)=-\sin(\theta)$, $h^{(3)}(\theta)=-\cos(\theta)$ and $h^{(4)}(\theta)=\sin(\theta)$. So after differentiating $4$ times, we obtain the original function again. This allows us to find high order derivatives of this function very quickly. Indeed, if we want to know the $1001$st derivative of $h$, we notice that $1000$ is divisible by $4$, so if we compute the thousandth derivative we make $250$ full loops of $4$ derivatives and end up with the original function. This means that $h^{(1000)}(\theta)=\sin(\theta)$. As such, we find that $h^{(1001)}(\theta)=\cos(\theta)$.
::::::

::::::{prf:example} 
:label: Def:Differentiability:Higherorderderivative3
Consider the function $f(x)=\left\{\begin{array}{l}0,\qquad&\text{if}\,x\leq 0,\\ x^2,\qquad &\text{if}\,x>0.\end{array}\right.$ We want to know how often this function is differentiable in $0$. We first compute the first derivative by evaluating the corresponding left and right limits in the definition of the derivative. This gives

$$
 \lim_{h\rightarrow 0^-}\frac{f(x+h)-f(x)}{h}=\frac{0-0}{h}=0
$$

and

$$
 \lim_{h\rightarrow 0^-}\frac{f(x+h)-f(x)}{h}=\frac{(0+h)^2-0}{h}=0.
$$

So $f$ is differentiable in $0$ and $f'(0)=0$. Moreover, we note that $f'(x)=0$ for $x<0$ and $f'(x)=2x$ for $x>0$. 

Now we try to find the second derivative. For this, we compute

$$
 \lim_{h\rightarrow 0^-}\frac{f'(x+h)-f'(x)}{h}=\frac{0-0}{h}=0
$$

and

$$
 \lim_{h\rightarrow 0^-}\frac{f'(x+h)-f'(x)}{h}=\frac{2h-0}{h}=0.
$$

So $f$ is twice differentiable in $0$ and $f''(0)=0$. In addition, we note that $f''(x)=0$ for $x<0$ and $f''(x)=2$ for $x>0$. However, this means that $f''$ is not continuous in $0$, so it cannot be differentiable again on account of {prf:ref}`Thm:Differentiability:Diffimpliescont`. So $f$ is twice differentiable in $0$, but not $3$ times.
::::::

::::::{prf:remark}
:label: Remark:Differentiability:Nbutnotnplus1

The idea from {prf:ref}`Def:Differentiability:Higherorderderivative3` works more general: if $n>0$ is a nonzero natural number the function $f(x)=\left\{\begin{array}{l}0,\qquad&\text{if}\,x\leq 0,\\ x^n,\qquad &\text{if}\,x>0.\end{array}\right.$ is $n$ times differentiable in $0$, but not $n+1$ times.

::::::