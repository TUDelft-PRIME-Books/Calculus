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
 x(t)=300\sin\left(\frac{3\pi t}{1200}-\frac{\pi}{}\right)+300, \qquad 0\leq t\leq 1200
$$

of which the graph is shown below.

Hier naast elkaar de grafieken van de twee functies $x(t)=\frac{3}{2}t$ en $x(t)=300\sin\left(\frac{3\pi t}{1200}-\frac{\pi}{}\right)+300$. 

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

The expression $\frac{Delta x}{\Delta t}$ is called a **difference quotient** and we conclude that it can be used to approximate the slope of the function. So how can we compute the exact slope of the function? Well, since as $\Delta t$ becomes small, the approximation gets better, we get the best result when taking the limit $\Delta t\rightarrow 0$. This means that we must have

$$
 \mathrm{velocity}=\lim_{\Delta t\rightarrow 0} \frac{\Delta x}{\Delta t}=\lim_{\Delta t\rightarrow 0} \frac{x(200+\Delta t)-x(200)}{\Delta t}.
$$

We call the value of the limit $\lim_{\Delta t\rightarrow 0} \frac{x(200+\Delta t)-x(200)}{\Delta t}$ the **derivative** of the function $x$ at $t=200$. Evaluating this limit is a bit tricky, but later we will learn some powerful tools which allow us to find

$$
 \mathrm{velocity}=\lim_{\Delta t\rightarrow 0} \frac{x(200+\Delta t)-x(200)}{\Delta t}=\frac{3\pi}{4}\approx 2.356.
$$

So we saw that our approximation by means of a difference quotient was actually correct up to at least $3$ decimal positions, which is pretty good.

(Subsec:Derivativesdifferentiability)=

## Derivatives and differentiability

In this chapter, we will study the general concept of a derivative. The process of finding the derivative of a function is called **differentiation**. Within the field of calculus (and also in more advanced subjects like mathematical analysis), differentiation is one of the most important subjects and it will play a very important role throughout this book. In this chapter we focus both on the computation part (finding derivatives) and on the interpretation (what does a derivative say about the graph of a function?). 

::::::{prf:definition} 
:label: Def:Differentiability:Diffquot
Let $f$ be a function and consider real numbers $x$ and $h$ for which $x$ and $x+h$ are in the domain of $f$. Then we an expression of the form $\dfrac{f(x+h)-f(x)}{h}$ is called a **difference quotient**.
::::::

::::::{prf:definition} 
:label: Def:Differentiability:Derivative
Let $f$ be a function and a number $a$ in the domain of $f$. Then the **derivative** of $f$ at $a$, denoted by $f'(a)$, is 

$$
 f'(a)=\lim\limits_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h},
$$

provided this limit exists. If the limit exists, we say that $f$ is **differentiable** in $a$.
::::::

Note that for a given function $f$, we can try to evaluate the derivative at each point in the domain. This means we can interpret the derivative itself as a function again: for each $x$ for which the derivative exists, the derivative function gives the value of the derivative at that point. This gives the following definition.

::::::{prf:definition} 
:label: Def:Differentiability:Derivativefunction
The **derivative** $f'$ (pronounced: $f$ prime) of a function $f$ is the function that associates to each value $x$ at which $f$ is differentiable the derivative $f'(x)$.
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

In this section we cover:

- Slopes and derivatives and graphs
- Notation, including differential notation
- Differentiability (including limit definition, also including theorem differentiable implies continuous)
- Derivatives of elemental functions (powers of x, sin, cos, e^x)
- Sums and scalar multiples
- Tangent line
- Higher-order derivatives