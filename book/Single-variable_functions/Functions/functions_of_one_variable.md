(Section:FunctionsIntro)=

# Functions of one variable

(Subsec:Functions1dIntro)=

## Introduction

[^MyFootnote1]: If you do not live close to Delft, you should come visit once. Then you can experience all the nice (and maybe also the not so nice) things about cycling through a crowded, old town. 


Suppose you are riding your bicycle through the city center of Delft.[^MyFootnote1] As you move along, your speed might change. For instance, sometimes you have to wait for other traffic, or you speed up because you move down a small ramp (we do not have hills here in the Netherlands to use to increase your speed). So, for instance, after cycling for $120$ seconds, your speed might be $5$ meters per second, while after $300$ seconds you are at a traffic light and your speed is $0$. We can denote this by using the symbol $v$ for speed and writing $v(120)=5$ and $v(300)=0$. So a more general equation $v(t)=c$ should be read as that after cycling for $t$ seconds the speed $v$ is equal to $c$. This way, we have written the speed $v$ as a **function** of $t$. The time takes the role of the **input variable**, while the speed takes the role of the **output value** or **function value**. What makes a function a function is that for each input $t$ we have a corresponding **single** output $v(t)$, i.e. the speed $v$ at that particular point in time $t$. 

Instead of prescribing what the speed is at several different points in time, we could also try to be more efficient. Often, it is possible to give a formula that expresses the speed in terms of the time that has passed. For instance, we could have that

$$
 v(t)=\frac{5}{2}+\frac{5}{2}\cos\left(\frac{\pi t}{60}\right)
$$

for $0\leq t\leq 600$. Here $t$ describes the number of second that has passed since we have started cycling and since we consider values of $t$ with $0\leq t\leq 600$ we are describing the first $10$ minutes that we are cycling. At different points in time, we could fill in the value of $t$ to find the (single!) corresponding value of $v$. For instance, we find

\begin{align*}
 v(120)&=\frac{5}{2}+\frac{5}{2}\cos\left(\frac{\pi \cdot 120}{60}\right)=\frac{5}{2}+\frac{5}{2}\cos(2\pi)=\frac{5}{2}+\frac{5}{2}\cdot 1=5,\\ v(300)&=\frac{5}{2}+\frac{5}{2}\cos\left(\frac{\pi \cdot 300}{60}\right)=\frac{5}{2}+\frac{5}{2}\cos(5\pi)=\frac{5}{2}+\frac{5}{2}\cdot (-1)=0.
\end{align*}

So this formula indeed gives the right values at the moments in time $t=120$ and $t=300$. However, there are many other formulas with this property. For instance, we could consider

$$
 \tilde{v}(t)=\frac{25}{3}-\frac{t}{36}
$$

for $0\leq t\leq 600$ (we use the symbol $\tilde{v}$ to distinguish between this formula and the previous one). Since we still have a single speed corresponding to each point in time, $\tilde{v}$ is a function of $t$. Then, we find

\begin{align*}
 \tilde{v}(120)=\frac{25}{3}-\frac{120}{36}=5,\qquad \tilde{v}(300)=\frac{25}{3}-\frac{300}{36}=0
\end{align*}

so this formula also gives the right values at the moments in time $t=120$ and $t=300$. So which of these is correct? Without knowing more about our journey, it is impossible to know for sure, but, in this case, one is definitely more realistic than the other. For instance, we have $v(t)\geq 0$ for all $t$, while at $t=600$ we have

$$
 \tilde{v}(600)=\frac{25}{4}-\frac{600}{48}=-\frac{25}{4}
$$

So for the formula $\tilde{v}(t)=\frac{25}{4}-\frac{t}{48}$ we obtain a negative speed and since we were not taking into account in which direction we were moving a negative speed does not make any sense. So the first formula is, physically speaking, more realistic. Does that mean that it is correct, though? Probably not, since we have only specified the speed at two points in time and a lot can happen at different points. Hence, it would be a major coincidence that the formula we provided perfectly described our movement. Still, we can use this formula to model our journey. Moreover the more points in time we specify what the speed should be, the more realistic we can choose our model.

In fact, in almost all processes in nature, science and engineering one quantity depends on another quantity (or perhaps on multiple quantities) and can, therefore, be described by means of a function. The branch of mathematics concerned with finding functions describing natural phenomena is called **mathematical modelling**. In this book, the focus is not on the modelling part. Instead, we usually assume that the function is given to us and by analyzing it, we aim to understand the underlying process. 

From a purely mathematical standpoint, functions are one of the most central objects of investigation. Indeed, most mathematical procedures where one mathematical object is turned into another object can be described by means of a function. Understanding what functions are and what you can and cannot do with them is essentially everything that we do in calculus, and mathematical analysis more broadly.

(Subsec:Functions1dConcepts)=

## Basic concepts

We start off by giving a few essential definitions.

::::::{prf:definition} 
:label: Def:Functions1var:Function

A **function** $f$ assigns to each $x$ in a set $D$ a *unique* element, usually denoted by $f(x)$, in a set $C$. The set $D$ is called the **domain** of the function, while the set $C$ is called the **codomain** of the function.

::::::

::::::{prf:notation} 
:label: Notation:Functions1var:Function

If $f$ has domain $D$ and codomain $C$ we write $f:D\rightarrow C$. We also write $x\mapsto y$ when $f(x)=y$.
::::::

::::::{prf:notation} 
:label: Notation:Functions1var:Codomain

If we do not explicitly specify the domain and/or codomain of a function $f$, we use the symbols $D_f$ for the domain of $f$ and $C_f$ for the codomain of $f$.
::::::

{prf:ref}`Def:Functions1var:Function` is good enough for the purpose of this book, but for those of you who are interested, we also provide the formal definition of a function.

::::::{prf:definition} Formal definition of a function
:label: Def:Functions1var:Functionformal
:class: bonus, dropdown

Let $D$ and $C$ be sets. Then the **product set** $D\times C$ is the set of all ordered pairs $(x,y)$ with $x$ in $D$ and $y$ in $C$.

A **function** $f$ with **domain** $D$ and **codomain** $C$ is a subset $f\subset (D\times C)$ such that for each $x\in D$ there is exactly one $y\in C$ with $(x,y)\in f$. For each pair $(x,y)\in f$ we write $y=f(x)$.

::::::


So how should you think about a function? There are several different perspectives you can take, but it may be helpful to think about a function as a machine that takes an **input value** $x$ and turns this into an **output value** or **function value** $f(x)$. We also say that $x$ is **mapped to** $f(x)$. 

Note that a function only works in one direction: we can always insert an element of the domain to obtain an element of the codomain, but it is not always possible to go back, see {numref}`Fig:Functions1var:Diagram` (we will dive deeper into the question if/when it is possible to go back in {numref}`Section:Inverse`).

:::{applet}
:url: calculus/functions_of_one_variable/diagram
:name: Fig:Functions1var:Diagram
:class: dark-light

A diagram can be used to graphically represent that a function $f$ maps an element $x$ in the domain $D_f$ to another element $f(x)$ in the codomain $C_f$.
:::

In addition, if $f$ is a function and we have $f(x)=y$ for some $x$ in $D_f$ and $y$ in $C_f$, we see that $y$ is determined by $x$. That means that the value of $y$ depends on the value of $x$, while the value of $x$ can be chosen freely (within the domain of $f$). As such, for this formula $f(x)=y$ the variable $y$ is referred to as the **dependent variable**, while $x$ is an **independent variable**.

In this book, the domain and codomain will almost always be (subsets of) $\mathbb{R}^n$ and $\mathbb{R}^m$ respectively, for some integers $n,m\geq 1$. In the first few chapters, we will specifically focus on functions where the domain and codomain are both (subsets of) the real numbers $\mathbb{R}$. Such a function is usually referred to as a **function of one variable** or a **function of a single variable**. For many such functions, it is possible to define the function by means of a formula, of which an example is given below. 

::::::{prf:example} 
:label: Ex:Functions1var:Formula

Consider the function $f:\mathbb{R}\rightarrow\mathbb{R},x\mapsto x^2$. This is the function with domain $\mathbb{R}$ and codomain $\mathbb{R}$ that for each real number $x$ that is put into the function outputs the real number $x^2$. For instance, for the input value $x=2$, we obtain the output 

$$
 f(x)=f(2)=2^2=4.
$$

Similarly, we obtain 

$$
 f(-3)=(-3)^2=9.
$$

Note that each input value gives a unique output value, but there are different input values with the same output value. Indeed, we note that also

$$
 f(3)=3^2=9
$$

[^Footnotecomplex]: Note that we specified the domain of $f$ to be $\mathbb{R}$, so we are not interested in complex values of $x$ here.

so both the input values $-3$ and $3$ are mapped to the output value $9$. Finally, notice that not all potential output values, i.e. all elements in the codomain, are actually reached. Indeed, the number $-1$ is in the codomain, but there is no real number $x$ with $f(x)=x^2=-1$[^Footnotecomplex].

::::::

::::::{prf:example} 
:label: Ex:Functions1var:NoFormula

Although most functions in this book can be described by means of a formula, this does not need to be the case. Moreover, the domain and/or codomain do not need to be part of $\mathbb{R}^n$. For instance, we can let $D$ be the set that contains $3$ people, Alice, Bob and Charlie, and let $f$ be the function that maps a person to their age. So, we could write this down like $f(\text{Alice})=31$, $f(\text{Bob})=66$ and $f(\text{Charlie})=19$. Here, the output is still a number, but even that does not need to be the case. For instance, we could let $g$ be the function that gives the first letter of a person's name, so we could write $g(\text{Alice})=\text{A}$, $g(\text{Bob})=\text{B}$ and $g(\text{Charlie})=\text{C}$. This might seem a bit silly, but it is actually quite beneficial that a lot of results that we will see in this section can also be applied to any type of domain or codomain, since it makes it possible to directly use these results in a more abstract mathematical setting.

::::::

Although the domain and codomain of a function are integral parts of the function, we often do not explicitly state them. Most functions that we will encounter are defined by a formula and for those functions we will implicitly assume that the domain consists precisely of those values of $x$ for which the formula 'makes sense'. In addition, almost all functions in this book will have $\mathbb{R}$ as the codomain (exceptions can be found in {numref}`Section:VectorCalculusIntro`), so we will implicitly assume that we are always dealing with these type of functions. Let us make these conventions a bit more explicit.

::::::{prf:definition} 
:label: Def:Functions1var:MaxDomain

Let $f$ be a function of which the domain is a subset of $\mathbb{R}^n$, that has codomain $\mathbb{R}$ and that is defined by a formula. Then the **maximal domain** or **natural domain** is the set of all values of $x$ for which this formula makes sense.

::::::

::::::{important}
Whenever we do not specify the codomain of a function, we assume this codomain is the real numbers $\mathbb{R}$.
::::::

::::::{important}
Whenever we define a function by means of a formula and we do not specify the domain, we assume that the domain is equal to the maximal domain.
::::::

::::::{important}
In the chapters listed under "Single-variable functions", whenever we talk about a function and neither give a formula, nor specify the domain, we assume that the domain is a subset of the real numbers $\mathbb{R}$.
::::::

The codomain of a function should be thought of as the set of all potential output values. However, in {prf:ref}`Ex:Functions1var:Formula` we saw that not every value in the codomain is necessarily reached. Still, it is interesting to find out which elements in the codomain are actually reached. For this, we have the following definition.

::::::{prf:definition} 
:label: Def:Functions1var:Range

Let $f$ be a function with domain $D$ and codomain $C$. Then the **range** $R$ of $f$ is the set of all function values of $f$. That is, we have

$$
 R=\left\{y\,\,\text{in}\,\,C\,\middle|\,\text{There is an }x\,\text{in}\,D\,\text{with}\,f(x)=y\right\}=\left\{f(x)\,\middle|\,x\,\text{in}\,D\right\}.
$$
::::::

::::::{note}
The range is a subset of the codomain.
::::::

::::::{prf:notation} 
:label: Not:Functions1var:Range

If $f$ is a function, then we denote its range by $R_f$.
::::::

::::::{prf:example} 
:label: Ex:Functions1var:MaxDomRange

Let $f$ be the function defined by $f(x)=3+\sqrt{x-2}$. Since this function is defined by a formula, we assume that its domain is equal to the maximal domain. So what is the maximal domain is this case? For that, we need to find out for which values of $x$ the expression $3+\sqrt{x-2}$ makes sense. The only restriction we have is that we cannot enter negative numbers into a square root, so the expression is defined precisely when $x-2\geq 0$, i.e. when $x\geq 2$. So the maximal domain is the set of all $x$ with $x\geq 2$, i.e. the interval $[2,\infty)$.

We can also determine the range of this function. Since every nonnegative number is the square root of a real number, while negative numbers are not square roots of real numbers, the expression $\sqrt{x-2}$ can take on any value in the interval $[0,\infty)$. Adding $3$ to this square root raises all output values by $3$, so the function $f$ can take on any value in the interval $[3,\infty)$. This interval must, therefore, be the range of $f$.
::::::

::::::{prf:example} 
:label: Ex:Functions1var:NaturalDomain

:::{figure} Images/Fig-Functions1var-GasTank.png
:name: Fig:Functions1var:GasTank
:figclass: margin

A gas tank.
:::

Consider a container with constant volume $V_0$ full of gas, measured in cubic meters. The [Ideal Gas Law](https://en.wikipedia.org/wiki/Ideal_gas_law) states that the temperature $T$ of the gas, measured in kelvin, is related to the pressure $P$, measured in pascal, by 

$$
 PV_0=nRT.
$$

Here $n$ is the amount of substance of gas, measured in moles, and $R$ is the ideal gas constant. By writing

$$
 T=\frac{PV_0}{nR}=\frac{V_0}{nR}P
$$

we see that if the pressure increases the temperature increases, while if the pressure decreases the temperature decreases. As such, we can think of the temperature as being a function of the pressure, so we can write $T=f(P)=\dfrac{PV_0}{nR}$. So what is a natural choice for the domain of this function? Mathematically, the formula $\dfrac{PV_0}{nR}$ is defined for each value of $P$, so the maximal domain would be the entire real line $\mathbb{R}$. However, physically, a negative pressure cannot occur, so we should, at the very least, impose that $P\geq 0$. Moreover, for very extreme conditions the ideal gas law (which is only an approximation for the behaviour of real life gases to begin with) will no longer accurately describe the behaviour of the tank. So we note that the domain in which the relation between $P$ and $T$ is valid, is quite a bit smaller than the mathematical maximal domain. As such, it is necessary to be aware of the distinction between the maximal domain and the actual domain whenever physical quantities are involved.
::::::

(Subsec:Functions1dGraphs)=

## Graphs

An essential part of understanding functions of a single variable is to try to visualise their behaviour. In principle, a function is a rule that maps an element $x$ to another element $f(x)$, so how is it possible to visualise this? Since each $x$ in the domain corresponds to exactly one $f(x)$, we could try to plot the point $(x,f(x))$ in $\mathbb{R}^2$. If we do this for each value of $x$, we have captured the full behaviour of the function in one picture. Such a plot is called the **graph** of a function. So for each point $(x,y)$ on the graph of $f$ we necessarily have $f(x)=y$. 


::::{applet}
:url: calculus/functions_of_one_variable/concept_of_a_graph
:name: Fig:Functions1var:Graph
:class: dark-light

The graph of a function $f$ can be used to read off the value $f(a)$ for a given value $a$. The domain and range of $f$ can also be read off from the graph.
::::

::::::{prf:definition} 
:label: Def:Functions1var:Graph
If $f$ is a function with domain $D$ then the **graph** of $f$ is the set of all pairs $(x,f(x))$. That is, it is the set $\left\{(x,f(x))\,\middle|\,x\,\,\text{in}\,\,D\right\}$. 
::::::

There is one major restriction when sketching a graph, and that is that we only have a finite amount of space to draw the plot on. So, for instance, if the function is defined for all $x$ in $\mathbb{R}$ it is impossible to plot the full graph of the function, since we would need an infinite amount of space to do so. Still, in such a case it is possible to plot only part of the graph and try to make sure that this part captures as much qualitative behaviour of the function as possible.

When analysing functions, it is often iteresting to determine if and where the graph of a function intersects the $x$-axis and the $y$-axis.

::::::{prf:definition} 
:label: Def:Functions1var:Intercepts
Let $f$ be a function. Then $x$ in the domain of $f$ is called a **zero**, **root**, **$x$-intercept** or **horizontal intercept** when $f(x)=0$, i.e. the $x$-value of a point where the graph of $f$ intersects the $x$-axis.

$y$ in the range of $f$ is called a **$y$-intercept** or **vertical intercept** when $f(0)=y$, i.e. the $y$-value of a point where the graph of $f$ intersects the $y$-axis.
::::::

For most functions that we will encounter in this book, the graph looks like one or several curves in $\mathbb{R}^2$. For instance, the graph of the function $f(x)=x^2$ is the curve of all points $(x,y)$ with $y=x^2$, so the graph is a parabola. So we might wonder: is any curve in $\mathbb{R}^2$ the graph of a certain function? For instance, is the circle with radius $1$, centered around the origin, the graph of some function? Well, suppose that there is some function $f$ which has this circle as its graph. Since the point $(0,1)$ is on the circle, that means that $f(0)=1$. However, the point $(0,-1)$ is also on this circle, so that should mean that $f(0)=-1$. Since for a function, a given input ($0$ in this case) can only have a single output, it is impossible that $f(0)$ is both $1$ and $-1$ at the same time. As such, this circle cannot be the graph of any function.

How could we have seen this in advance? Well, the reason why the circle is not the graph of a function was that there are two different points on this circle which have the same $x$-coordinate. That means that the vertical line $x=0$ intersects the circle at two different points. This idea can be generalized as follows: the only reason a curve is not the graph of some function, is that there are two different points on the curve that have the same $x$-coordinate. In such a case, there is a vertical line that intersects the curve more than once. Conversely, a vertical line $x=a$ intersect the graph of a function $f$ exactly once if $a$ is in the domain of $f$ (they intersect at the point $(a,f(a))$), while such a vertical line does not intersect the graph at all if $a$ is not in the domain of $f$. We can formulate this result as follows.

::::::{prf:theorem} Vertical line test 
:label: Thm:Functions1var:VerticalLineTest
A curve in $\mathbb{R}^2$ is the graph of a function precisely when each vertical line of the form $x=a$ for some real number $a$ intersects the curve at most once.
::::::

You will learn more about curves that are not (necessarily) graphs of functions in {numref}`Section:Curves`.

::::::{prf:example} 
:label: Ex:Functions1var:Verticalline
:class: full-width

Consider the two curves shown below.

:::::{figure-start}
:name: Fig:Functions1var:Verticalline

Two curves in $\mathbb{R}^2$ and a vertical line for the vertical line test.
:::::

:::::{grid} 2 2 2 2
::::{grid-item}

:::{applet}
:url: calculus/functions_of_one_variable/vertical_line_test_1
:class: dark-light
:::

::::

::::{grid-item}

:::{applet}
:url: calculus/functions_of_one_variable/vertical_line_test_2
:class: dark-light
:::

::::
:::::

:::::{figure-end}
:::::

Can we check whether these curves are the graph of a function? For the curve on the left, each vertical line intersects the curve exactly once, so this curve is the graph function. You might wonder of which function this curve is the graph. Without further knowledge of the function, this is impossible, unfortunately. Still, for a given $x$, we can read off what the function value $f(x)$ will be approximately. For instance, we can read off that $f(0)=0$ (or maybe something very close to $0$), while $f(1)$ is approximately $ 1.9$.

The curve on the right, on the other hand, is not the graph of a function. Some vertical lines, like the line $x=-1$, intersect the curve once, but there are also vertical lines that intersect the curve multiple times, such as the line $x=1$, which intersects the curve $3$ times. If this curve were to be the graph of a function $f$, then $f(1)$ would need to be all three corresponding values of $y$ at the same time, which is impossible.
::::::


::::::{prf:example} 
:label: Ex:Functions1var:VerticalLine2

Let $C_1$ be the curve given by all points $(x,y)$ that satisfy the equation $x^2-y^3=0$. Is this curve the graph of a function, and if so, of which function? We could try to plot this function and apply the vertical line test, but that is rather hard to do without plotting software. It is also not necessary. Indeed, we can rewrite the equation as

$$
 x^2-y^3=0\quad \Longleftrightarrow\quad y^3=x^2\quad \Longleftrightarrow\quad y=\sqrt[3]{x^2}=x^{\frac{2}{3}}.
$$

So each point $(x,y)$ on the curve actually satisfies $y=x^{\frac{2}{3}}$. So that means that $C_1$ is the graph of the function $f$ with $f(x)=x^{\frac{2}{3}}$.

Similarly, we can let $C_2$ be the curve given by all points $(x,y)$ that satisfy the equation $x^2-y^2=0$. Here, we could try a similar approach and write

$$
 x^2-y^2=0\quad \Longleftrightarrow\quad y^2=x^2\quad \Longleftrightarrow\quad y=\pm x.
$$

Now, the expression $\pm x$ might look like a formula describing a function to you, but it is not. Indeed, for $x=1$, we obtain $y=\pm 1$, so we obtain two different output values for a single input value, which is impossible. So this curve cannot be the graph of a function.

This result is also visible in the plot of the two curves, shown below.

:::{applet}
:url: calculus/functions_of_one_variable/two_implicit_curves
:name: Fig:Functions1var:VerticalLine2
:class: dark-light

The curves $C_1$ and $C_2$.
:::


::::::

:::{todo}
Idea for interactivity: make tool that students can draw a curve. Then a draggable vertical line appears and it becomes red/bold/whatever whenever the vertical line intersets the curve more than once. It should not be too sensitive, as it is easy to go 1 pixel to the left when attempting to go to the right.
:::


(Subsec:Functions1dElementary)=

## Standard functions

Many functions can be expressed in terms of other functions. In {numref}`Section:PropertiesFunctions` we will see several ways we can combine two functions into another function (for instance, by addition, multiplication or composition). We use this section to define the 'building blocks', that is, the most common functions that can be used to build more complicated functions. Several of these we have already encountered in {numref}`Chapter:NumbersAndCoordinate` though we did not call them functions back then. The functions we will discuss in this section are often referred to as **standard** or **elementary** functions.

The most standard of standard functions are the polynomials. These come in various flavours, of which we will give the most important ones their own names.

::::::{prf:definition} 
:label: Def:Functions1var:Polynomial
A function $f$ is called a **polynomial function** if $f(x)=a_nx^n+a_{n-1}x^{n-1}+\ldots+a_1x+a_0$ for some integer $n\geq 0$ and real numbers $a_0,a_1,\ldots,a_n$. 

If the polynomial function consists of only one term, so if $f(x)=a_nx^n$, then we call it a **monomial function**.

If $a_n\neq 0$ (so that $x^n$ is highest power of $x$ that occurs in the formula describing $f$), we say that the **degree of the polynomial** is $n$.

A **constant function** is a polynomial function of degree $0$, i.e. one that can be written as $f(x)=a_0$.

A **linear function** is a polynomial function of degree $1$, i.e. one that can be written as $f(x)=a_1x+a_0$.

A **quadratic function** is a polynomial function of degree $2$, i.e. one that can be written as $f(x)=a_2x^2+a_1x+a_0$

A **cubic function** is polynomial function of degree $3$, i.e. one that can be written as $f(x)=a_3x^3+a_2x^2+a_1x+a_0$.
::::::

:::{note}
The maximal domain of any polynomial is $\mathbb{R}$.
:::

::::::{prf:definition} 
:label: Def:Functions1var:Rational
A **rational function** $r$ is a function that can be expressed as the ratio of two polynomials:

$$
r(x) = \frac{p(x)}{q(x)},
$$

where $p$ and $q$ are polynomials.
::::::

:::{note}
The maximal domain of a rational function $r(x)=\frac{p(x)}{q(x)}$ is the set $\left\{x\,\text{in}\,\mathbb{R}\,\middle|\,q(x)\neq 0\right\}$.
:::

Rational functions will be discussed more extensively in {numref}`Sec:RationalFunctions`.

In {numref}`Sec:Algebra:Trigonometry` we saw that for an angle $\theta$ we can consider the trigonometric ratios $\sin(\theta)$, $\cos(\theta)$ and $\tan(\theta)$. The sine, cosine and tangent take an angle as input and give a number back as output, which means that they are actually functions.

::::::{prf:definition} 
:label: Def:Functions1var:Trigonometry
The functions $f(x)=\sin(x)$, $f(x)=\cos(x)$ and $f(x)=\tan(x)$ are called the standard **trigonometric functions**.
::::::


:::{Note}
We always assume that the input of a trigonometric function is measured in radians, not in degrees.

The maximal domains of the sine and cosine is $\mathbb{R}$, while the maximal domain of the tangent is 

$$
 \left\{x\,\text{in}\,\mathbb{R}\,\middle|\,x\neq \frac{\pi}{2}+k\pi\,\text{for some}\,k\,\text{in}\,\mathbb{Z}\right\}.
$$

:::




In {numref}`Section:RealNumbers` we saw that for a base $b\geq 0$ and an exponent $r$ in $\mathbb{R}$ we could define the exponentiation $b^r$. This concept actually leads to two different types of functions: one where we vary $b$ and one where we vary $r$. For the second type, the one with base $e$, see {numref}`Subsec:RealNumbersE`, plays a particularly important role in calculus.

::::::{prf:definition} 
:label: Def:Functions1var:PowerFunction
If $r$ is a real number, then the function $f(x)=x^r$ is called a **power function**.

If $r=-1$ then the function $f(x)=x^{-1}=\frac{1}{x}$ is sometimes referred to as the **reciprocal function**.

If $r=\frac{1}{n}$ for some integer $n>0$ then the function $f(x)=x^{\frac{1}{n}}=\sqrt[n]{x}$ is sometimes referred to as the **nth root function**. If $n=2$, the function is called **the square root function** and if $n=3$, the function is called the **cube root function**.

::::::

:::{note}
The maximal domain of a power function $f(x)=x^r$ depends on $r$. 

- If $r=\frac{p}{q}$ for integers $p$ and $q$ with $q>0$, $q$ odd and $p> 0$, then the maximal domain of $f$ is $\mathbb{R}$.
- If $r=\frac{p}{q}$ for integers $p$ and $q$ with $q>0$, $q$ odd and $p\leq 0$, then the maximal domain of $f$ is $\mathbb{R}\setminus\{0\}=\left\{x\in\mathbb{R}\,\middle|\,x\neq 0\right\}$.
- For any other positive value of $r$, the maximal domain is the interval $[0,\infty)$, while for any other negative value of $r$, the maximal domain is the interval $(0,\infty)$.

:::

::::::{prf:definition} 
:label: Def:Functions1var:ExponentialFunction
For $b\geq 0$ the function $f(x)=b^x$ is called an **exponential function**.

The function $f(x)=e^x$ is referred to as the **natural exponential function**, or sometimes simply **the exponential function**.
::::::

:::{note}
If $b=0$, we have $f(x)=0^x=0$ for all $x\neq 0$ (and the function is not defined for $x=0$). The maximal domain is $\mathbb{R}\setminus\{0\}=\left\{x\in\mathbb{R}\,\middle|\,x\neq 0\right\}$ for this value of $b$. If $b=1$, we have $f(x)=1^x=1$ for all $x$, which means that the maximal domain is $\mathbb{R}$ for this value of $b$. In both cases, the function is constant.

For any other value of $b$, the maximal domain of the exponential function $f(x)=b^x$ is $\mathbb{R}$.

:::

Other important classes of functions are logarithms and inverse trigonometric functions. These will be covered in {numref}`Section:Inverse`.


Let us investigate the behaviour of these standard functions by considering a few examples.

::::::{prf:example} Linear function
:label: Ex:Functions1var:Linear
Consider the function given by $f(x)=2x+3$. This is a polynomial function, in particular, it is a linear function. Since for any value of $x$ it is possible to compute $2x+3$, the maximal domain of this function is the set of all real numbers $\mathbb{R}$. The graph of this function is shown below.

:::{applet}
:url: calculus/functions_of_one_variable/linear_function
:name: Fig:Functions1var:Linear
:class: dark-light

The graph of the linear function $f(x)=2x+3$.
:::

As you can see, the graph of this function is a straight line, which is always the case for linear functions. Can we find out where the numbers $2$ and $3$ in the definition of the function come back in the graph?

We note that the graph of the function crosses the $y$-axis at the point $(0,3)$. Indeed, we have $f(0)=2\cdot 0+3=3$. So for linear functions of the form $g(x)=ax+b$, the number $b$ specifies at which value of $y$ the graph of $g$ crosses the $y$-axis. The $2$ in the definition of $f$ also comes back in the graph of $f$, though it is not as directly visible. Note that if $x$ increases by $1$, $y$ increases by $2$. In fact, when $x$ increases by any value $\Delta x$, $y$ will increase by $\Delta y=2\Delta x$. We say that $2$ is the **slope** of the line. In general, for a linear function of the form $g(x)=ax+b$ the number $a$ specifies the slope of the graph of $g$. We will generalise the concept of a slope to other curves than straight lines in {numref}`Chapter:Differentiation`.
::::::

::::::{prf:example} Quadratic function
:label: Ex:Functions1var:Quadratic
Consider the function given by $h(x)=x^2-4x+3$. This is a quadratic function and, therefore, a special type of polynomial function. Since $h(x)$ exists for any real number $x$, the maximal domain of $h$ is $\mathbb{R}$. The graph of this function is shown below.

:::{applet}
:url: calculus/functions_of_one_variable/quadratic_function_1
:name: Fig:Functions1var:QuadraticH
:class: dark-light

The graph of the quadratic function $h(x)=x^2-4x+3$.
:::

The graph of this function is a **parabola**. The graph crosses the $x$-axis at $x=1$ and $x=3$, which can be seen from the fact that $h(x)=x^2-4x+3=(x-1)(x-3)$, so that $h(x)=0$ precisely when $x=1$ or $x=3$. 

Notice that the lowest value of $y$ occurs at $x=2$, where $h(2)=-1$. That is, $h(x)\geq -1$ for all values of $x$. In the terminology of {numref}`Section:Extrema1d`, the absolute minimum of the function function $h$ is $-1$ and occurs at $x=2$. As a result, the range of $h$ is not the full set of real numbers $\mathbb{R}$. Since $h(x)$ can get as large as we want to by increasing $x$, we find that the range of $h$ is the interval $[-1,\infty)$.

Since the graph of $h$ has a lowest value and then grows for both very large and very negative values of $x$, we say that the graph of $h$ is a parabola that **opens upwards**.  On the other hand, the graph of the function $k(x)=2-3x^2$ is also a parabola, as can be seen below. However, this one has a highest value and it becomes very negative for both very large and very negative values of $x$. Hence, the graph of $k$ is a parabola that **opens downwards**.

For more information on parabolas, see {numref}`Subsec:CurvesParabola`.

:::{applet}
:url: calculus/functions_of_one_variable/quadratic_function_2
:name: Fig:Functions1var:QuadraticK
:class: dark-light

The graph of the quadratic function $k(x)=2-3x^2$.
:::

::::::

:::{todo}
Make multiselect poll. Consider quadratic function $h(x)=ax^2+bx+c$. Which are true/false:

- $h(0)=c$ True
- $h(x)=0$ gives $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ provided $b^2-4ac\geq 0$. True
- If $a>0$ then the parabola opens upwards True
- If $a<0$ then the parabola opens downwards True
- If $a=0$ then the function is linear or even constant. True
:::

::::::{prf:example} Power functions with positive integer power
:label: Ex:Functions1var:CubicAndHigher
We now consider a function of the form $g(x)=x^n$ for some positive integer $n\geq 2$. This is both a polynomial and a power function. The behaviour of this function will greatly depend on whether $n$ is even or odd. 

:::{figure} Images/Fig-Functions1var-CubicAndHigher.png
:name: Fig:Functions1var:CubicAndHigher

On the left the functions $x^2$, $x^4$, $x^6$ and $x^8$ are plotted, while on the right the functions $x^3$, $x^5$, $x^7$ and $x^9$ are plotted. In both cases, the part of the graph between $-2$ and $2$ is shown.
:::

:::{todo}
Replace {numref}`Fig:Functions1var:CubicAndHigher` with an applet.

Alternative: make the left one into one graph with a slider for $n$ and same for the right one.
:::

Indeed, for even values of $n$, the graph of $g(x)=x^n$ resembles the parabola $y=x^2$, while for odd values of $n$, the graph is similar to that of $x^3$. In particular, for even values of $n$ the graph of the function is symmetric around the $y$-axis. In {numref}`Section:PropertiesFunctions` we will call a function with this property **even** (so now you already know where that name comes from). Similarly, for odd values of $n$ the graph of the function is point symmetric with respect to the origin and such a function will be called **odd**.

Note that as $n$ gets larger the graphs become more flat for $x$ between $-1$ and $1$. This is because for these values of $x$ we have $|x^2|>|x^3|>|x^4|>\ldots>0$. On the other hand, for values of $x$ larger than $1$ or smaller than $-1$, the function blows up quicker for larger values of $n$, since then we have $|x^2|<|x^3|<|x^4|<\ldots$


::::::

::::::{prf:example} Reciprocal function
:label: Ex:Functions1var:IdealGas2
Let us return to the Ideal Gas Law that was discussed in {prf:ref}`Ex:Functions1var:NaturalDomain`. However, instead of assuming that the volume is constant, we now assume that the temperature $T$ is constant. Then the pressure $P$ can be written as a function of the volume $V$ by writing

$$
 P=\frac{nRT}{V}=nRTV^{-1}.
$$

That is, the pressure is inversely proportional to the volume. This means that if $V$ doubles, $P$ will halve and vice versa. The graph of $P$ as a function of $V$ is shown below. Note that $P$ becomes very large if $V$ is close to $0$, while, reversely, $P$ is very close to $0$ whenever $V$ is very large. This makes sense from a physical point of view: when $V$ is small, the gas is compressed into a small amount of space, which means that the pressure must be very high, while if $V$ is large, the gas is distributed over a large amount of space, which means the pressure is much lower.


:::{figure} Images/Fig-Functions1var-IdealGas2.svg
:name: Fig:Functions1var:IdealGas2

The graph of the function $P(V)=\frac{nRT}{V}$ to indicate the shape of the function for several values of the constant $nRT$. Due to physical restrictions, the domain of this function only consists of positive values of $V$.


:::

:::{todo}
Replace {numref}`Fig:Functions1var:IdealGas2` with an applet.
Alternative: use a slider for $nRT$.
:::

::::::

::::::{prf:example} Power function with power $-2$
:label: Ex:Functions1var:Gravity
Consider two objects with masses $m_1$ and $m_2$ respectively (measured in $\mathrm{kg}$). Then [Newton's law of universal gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation) states that the gravitational force $F$ (measured in $\mathrm{N}$) acting between the two objects is a function of the distance $r$ (measured in $\mathrm{m}$) between the two objects

$$
 F(r)=G\frac{m_1m_2}{r^2}=Gm_1m_2r^{-2}.
$$

Here $G$ is the [gravitational constant](https://en.wikipedia.org/wiki/Gravitational_constant). The graph of the function is shown below. Since $F$ is proportional to $r^{-2}$, this law is a prime example of an **inverse square law**. This means that if the distance between the masses is doubled, the gravitational force drops by a factor $\frac{1}{4}$. Inverse square laws are rather common in nature, for example in certain electric, light and sound effects.

::::{figure} Images/Fig-Functions1var-Gravity.svg
:name: Fig:Functions1var:Gravity

The graph of the function  $F(r)=Gm_1m_2r^{-2}$ to indicate the shape of the function for several values of the constant $Gm_1m_2$.
::::

:::{todo}
Replace {numref}`Fig:Functions1var:Gravity` with an applet.
Alternative: use a slider for $Gm_1m_2$.
:::

The graph is, qualitatively speaking, somewhat similar to the one in {prf:ref}`Ex:Functions1var:IdealGas2`. However, in that case, $P$ was proportional to $V^{-1}$, while in this case $F$ is proportional to $r^{-2}$. This difference mainly manifests close to $0$ (where $F$ grows much faster than $P$), and far away from $0$ (where $F$ goes to $0$ much quicker than $P$). 

::::::

::::::{prf:example} Power functions with negative integer power
:label: Ex:Functions1var:NegativePowers
Let us now consider the power functions $f(x)=x^{-1}$ and $g(x)=x^{-2}$. Their graphs are shown below.

:::{figure} Images/Fig-Functions1var-NegativePowers.png
:name: Fig:Functions1var:NegativePowers

The graphs of the functions $f(x)=x^{-1}$ and $g(x)=x^{-2}$.
:::

:::{todo}
Replace {numref}`Fig:Functions1var:NegativePowers` with an applet.

Better: plot $x^{-n}$ and $x^{-m}$ for $n$ odd and $m$ even in one plot (so always two graphs visible). Default: $n=1$ and $m=2$, but make a slider for $n$ and one for $m$.
:::

Note that the graph of $f$ is very similar to the one in {prf:ref}`Ex:Functions1var:IdealGas2`, except that, since there are no physical restrictions, the function $f$ is also defined for negative values of $x$. In fact, whenever two (physical) quantities are inversely proportional to each other, the graph of one quantity as a function of the other one will be similar to the graph of $f$. Since the graph of $f$ is the set of all points $(x,y)$ with $y=\frac{1}{x}$, we can rewrite this equation to $xy=1$. This means that the graph of $f$ is a hyperbola. For more information on hyperbolas, see {numref}`Subsec:CurvesHyperbola`.

Similarly, the graph of $g$ is very similar to the one in {prf:ref}`Ex:Functions1var:Gravity` with again the main distinction that we now allow for negative input values. This does make the distinction between the graphs of $f$ and $g$ more clear, though, as $f$ is negative for negative input values, while $g$ is positive.

Note that the function values of both $f$ and $g$ blow up near $x=0$. In the terminology of {numref}`Section:LimitPoint`, both functions have a **vertical asymptote** at $x=0$.

Graphs of functions of the form $h(x)=x^{-n}$ with $n\geq 1$ a positive integer have similar qualitative behaviour to the ones of $f$, if $n$ is odd, or of $g$, if $n$ is even.
::::::

::::::{prf:example} Exponential function
:label: Ex:Functions1var:ExponentialGrowth
Many quantities in nature have the property that their growth rate is proportional to the current size. This can occur in the form of growth, for instance the population size of bacteria, the spread of a virus or the accumulated interest over savings, or in the form of decay, for instance the intensity of radioactive radiation, the amplitude of vibrations or the cooling of an object placed in a colder environment. In each of these cases, it is possible to model the physical quantity as an exponential function of time. That is true, because exponential functions have that same growth property that their growth rate (or in more mathematical terms, their derivative) is proportional to the function itself, see {numref}`Section:Differentiability`.

To show the typical behaviour of exponential functions, let us consider the functions $A(t)=2^t$ and $B(t)=\left(\frac{1}{3}\right)^t$. Using the computation rules for exponentiation, we can write the function $B$ alternatively as $B(t)=3^{-t}$. The graphs of the functions $A$ and $B$ are shown below.

:::{figure} Images/Fig-Functions1var-ExponentialGrowth.png
:name: Fig:Functions1var:ExponentialGrowth

The graphs of the functions $A(t)=2^t$ and $B(t)=\left(\frac{1}{3}\right)^t$.
:::

:::{todo}
Replace {numref}`Fig:Functions1var:ExponentialGrowth` with an applet.

Better: plot $A(t)=n^t$ and $B(t)=\left(\frac{1}{m}\right)^t$ in one plot. Default: $n=2$, $m=3$, with slider for $n,m$ (both $\geq 2$, half-integer steps, although it could be fun to include the case where one of them is $1$ to show the qualitative difference)
:::

For the function $A$, we notice that it is very close to $0$ for negative values of $t$, while it grows very fast for positive $t$. In fact, it grows faster the larger $t$ gets, which is indeed the **exponential growth** behaviour that we were trying to model. Conversely, the function $B$ is very large for negative values of $t$, while it get very close to $0$ for positive values of $t$. In fact, the decay rate decreases when $t$ gets larger, so again this function describes **exponential decay**.

In a physical context, $t$ often models time. In such cases, the process starts at $t=0$ and evolves for $t>0$ giving either growth or decay, while negative values of $t$ are not considered.

In general, an exponential function $C(t)=a^t$ gives rise to exponential growth when $a>1$ and exponential decay when $0<a<1$. In the edge case where $a=1$, we find that $C(t)=1$ for all values of $t$.


::::::

::::::{prf:example} Trigonometric functions
:label: Ex:Functions1var:Trigonometry
Apart from their role in geometry, the trigonometric functions $f(\theta)=\cos(\theta)$, $g(\theta)=\sin(\theta)$ and $h(\theta)=\tan(\theta)$ also play an important role in describing certain physical processes. For instance, the amplitude of an undamped mass-spring system as a function of time can be described in terms of sines and/or cosines. In fact, whenever there is oscillatory behaviour, these functions tend to be good candidates to use as models.

Let us analyse these functions a bit more in mathematical terms. First, let us consider their graphs.

:::{figure} Images/Fig-Functions1var-Trigonometry.png
:name: Fig:Functions1var:Trigonometry

The graphs of the trigonometric functions $f(\theta)=\cos(\theta)$, $g(\theta)=\sin(\theta)$ and $h(\theta)=\tan(\theta)$.
:::

:::{todo}
Replace {numref}`Fig:Functions1var:Trigonometry` with an applet.
:::

One of the first things you might notice is that $f$ and $g$ repeat themselves after each cycle of length $2\pi$, while $h$ repeats itself after each cycle of length $\pi$. We say that these functions are **periodic**. This periodicity follows from {prf:ref}`Thm:Trigonometry:Periodicity`. We will delve deeper into this subject in {numref}`Subsec:PropertiesFunctionsPeriodic`.

In addition, we note that the cosine and sine only take on values in between $-1$ and $1$. This follows from the geometric interpretation of the point $(\cos(\theta),\sin(\theta))$ as a point on the unit circle, which must mean that these values must be in between $-1$ and $1$. As such, the range of the functions $f$ and $g$ is the interval $[-1,1]$. By contrast, the tangent can take on any value, so its range is the set of real numbers $\mathbb{R}$.

Finally, we note that the graphs of the functions $f$ and $g$ intersect for $x$ somewhere between $0$ and $1$. Can we find this value of $x$ exactly? For that, we first need to understand what it means that the graphs of two functions intersect. Since the point $(\theta,y)$ is on the graph of $f$ precisely when $f(\theta)=y$, this means that we are looking for a value of $\theta$ for which $\cos(\theta)=\sin(\theta)$. There is only one value of $\theta$ between $0$ and $1$ for which that is the case, and that is $\theta=\frac{\pi}{4}$. Indeed, we have $\cos\left(\frac{\pi}{4}\right)=\sin\left(\frac{\pi}{4}\right)=\frac{1}{2}\sqrt{2}$. So the graphs of $f$ and $g$ intersect at the point $\left(\frac{\pi}{4},\frac{1}{2}\sqrt{2}\right)$. By the periodicity of the sine and cosine, they will intersect at each point of the form $\left(\frac{\pi}{4}+2n\pi,\frac{1}{2}\sqrt{2}\right)$ for integer values of $n$.

::::::

(Subsec:Functions1dPiecewise)=

## Piecewise defined functions

In most cases, functions are defined in terms of a single formula. For instance, for functions like $f(x)=\sin\left(x^2+2\right)$, $g(x)=\frac{1}{3e^{2x}}$ or $h(x)=\sqrt{x^3+1}$, the function value corresponding to a certain value of $x$ can be found by plugging in $x$ into the one and only formula describing the function. However, sometimes you want the function to behave differently on different parts of the domain. In such a case, it is possible to use different formulas describing the function on different parts of the domain. If a function is defined using different formulas, we usually refer to it as a **piecewise defined function**.

::::::{prf:example} 
:label: Ex:Functions1var:Abs
The absolute value $|x|$ of a number $x$ is actually a shorthand for $x$ if $x$ is positive or $-x$ if $x$ is negative. So the function $a(x)=|x|$ can alternatively be written as

$$
 a(x)=\left\{\begin{array}{lll}x,\qquad&\text{if }&x\geq 0,\\ -x,&\text{if }&x<0.\end{array}\right.
$$

This notation should be read as that $a$ follows the formula $a(x)=x$ for $x\geq 0$, while $a$ follows the formula $a(x)=-x$ for $x<0$.

:::{figure} Images/Fig-Functions1var-Abs.png
:name: Fig:Functions1var:Abs

The graph of the piecewise defined function $a(x)=|x|$.
:::

:::{todo}
Replace {numref}`Fig:Functions1var:Abs` with an applet.
:::


::::::

::::::{prf:example} 
:label: Ex:Functions1var:Heaviside
The **Heaviside (step) function** or **unit step function** is the function defined by

$$
 H(t)=\left\{\begin{array}{lll}1,\qquad&\text{if }&t\geq 0,\\ 0,&\text{if }&t<0.\end{array}\right.
$$

That is, the Heaviside function outputs the value $0$ when the input is negative and it outputs the value $1$ when the input is positive. It can be used to model a process that starts off (i.e. at state $0$) and is instantaneously turned on (i.e. state $1$), for instance when flipping a switch. The function is named after the British mathematician and electrical engineer [Oliver Heaviside (1850-1925)](https://en.wikipedia.org/wiki/Oliver_Heaviside).

:::{figure} Images/Fig-Functions1var-Heaviside.png
:name: Fig:Functions1var:Heaviside

The graph of the piecewise defined function $H(t)$.
:::

:::{todo}
Replace {numref}`Fig:Functions1var:Heaviside` with an applet.
:::

::::::

::::::{prf:example} 
:label: Ex:Functions1var:Piecewise
Consider the piecewise defined function

$$
 f(x)=\left\{\begin{array}{lll}2x+3,\qquad&\text{if }&x\leq -1,\\ 3,&\text{if }&0<x\leq 1,\\ 2-x^2,&\text{if }&x>1.\end{array}\right.
$$

This means that in order to evaluate $f(-2)$, we should look in which of the defining intervals $-2$ lies. In this case, we have $-2\leq -1$, so on this part of the domain the function follows the formula $2x+3$. This means that $f(-2)=2(-2)+3=-1$. 

Similarly, in order to evaluate $f(4)$, we note that $4>1$ so that $f(4)=2-4^2=-14$.

Finally, we note that the function is undefined for $-1<x\leq 0$. These values of $x$ simply do not lie in the domain of this function.

:::{figure} Images/Fig-Functions1var-Piecewise.png
:name: Fig:Functions1var:Piecewise

The graph of the piecewise defined function $f$.
:::

:::{todo}
Replace {numref}`Fig:Functions1var:Piecewise` with an applet.
:::

::::::

## Grasple exercises

### Exercises on domain and range.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2e95a962-8482-40a6-9c9a-5e2f34adaf5e?id=70778
:label: Grasple:70778
:dropdown:
:description: Maximal domain of a rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1e2dbd03-16e5-48de-9e71-0677e79b0276?id=68282
:label: Grasple:68282
:dropdown:
:description: Maximal domain of a function with a square root.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3fc2e557-4226-42f8-8749-34728d425a47?id=70774
:label: Grasple:70774
:dropdown:
:description: Range of an exponential function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ef3fce68-8504-4b63-925b-a5b5f3237c66?id=63052
:label: Grasple:63052
:dropdown:
:description: Maximal domain and range of a trigonometric function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bfefa695-a308-4d1b-a10a-eb648b00b4e4?id=63058
:label: Grasple:63058
:dropdown:
:description: Maximal domain and range of a function with a square root.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9cc94b7b-8fd6-4ba3-b43c-acc1974b9dc4?id=63060
:label: Grasple:63060
:dropdown:
:description: Maximal domain and range of a function with a square root.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d312bc3e-990f-46ff-bbc3-80e923dd4998?id=63063
:label: Grasple:63063
:dropdown:
:description: Maximal domain and range of a function with an exponential.

::::

### Exercises on graphs.


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2594ba5b-3806-4782-8a8b-935359701118?id=70719
:label: Grasple:70719
:dropdown:
:description: Is this the graph of a function?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/03a63ea0-4814-4467-a19c-8ddcdadf31b1?id=70720
:label: Grasple:70720
:dropdown:
:description: Is this the graph of a function?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8c83b344-557d-4a25-b876-d8a03787f7a9?id=70721
:label: Grasple:70721
:dropdown:
:description: Is this the graph of a function?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4ad27fb3-4dfa-4ed8-900a-d3f3c3b7969b?id=70722
:label: Grasple:70722
:dropdown:
:description: Is this the graph of a function?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ba2670f2-03b7-4b7b-a536-4ef2e008317e?id=70723
:label: Grasple:70723
:dropdown:
:description: Describing a circle as (several) functions.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/974c76a6-90c0-4e74-8a7e-802433c9e74e?id=70779
:label: Grasple:70779
:dropdown:
:description: Is this the graph of a function?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/baa47b92-4831-43aa-8634-c5bdcee67b0c?id=70865
:label: Grasple:70865
:dropdown:
:description: Is this the graph of a function?

::::