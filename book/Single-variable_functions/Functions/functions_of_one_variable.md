(Section:Functionsintro)=

# Functions of one variable

[^myfootnote1]: If you do not live close to Delft, you should come visit once. Then you can experience all the nice (and maybe also the not so nice) things about cycling through a crowded, old town. 

[^myfootnote2]: Delft is not that big, so it not unrealistic that it takes you $10$ minutes to get to your destination.

Suppose you are riding your bicycle through the city center of Delft.[^myfootnote1] As you move along, your speed might change. For instance, sometimes you have to wait for other traffic, or you speed up because move down a small ramp (we do not have hills here in the Netherlands to use to increase your speed). So, for instance, after cycling for $60$ seconds, your speed might be $5$ meters per second, while after $300$ seconds you are at a traffic light and your speed is $0$. We can denote this by using the symbol $v$ for speed and writing $v(120)=5$ and $v(300)=0$. So a more general equation $v(t)=c$ should be read as that after cycling for $t$ seconds the speed $v$ is equal to $c$. This way, we have written the speed $v$ at a **function** of $t$. The time takes the role of the **input variable**, while the speed takes the role of the **output value** or **function value**. So that means that for each input $t$ we have a corresponding output $v(t)$, i.e. the speed $v$ at that particular point in time $t$.

Instead of prescribing what the speed is at several different points in time, we could also try to be more efficient. Often, it is possible to give a formula that expresses the speed in terms of the time that has passed. For instance, we could have that

$$
 v(t)=\frac{5}{2}+\frac{5}{2}\cos\left(\frac{\pi t}{60}\right)
$$

for $0\leq t\leq 600$. Here $t$ describes the number of second that has passed since we have started cycling and since we consider values of $t$ with $0\leq t\leq 600$ we are describing the first $10$ minutes that we are cycling.[^myfootnote2] At different points in time, we could fill in the value of $t$ to find the corresponding value of $v$. For instance, we find

\begin{align*}
 v(120)&=\frac{5}{2}+\frac{5}{2}\cos\left(\frac{\pi \cdot 120}{60}\right)=\frac{5}{2}+\frac{5}{2}\cos(2\pi)=\frac{5}{2}+\frac{5}{2}\cdot 1=5,\\ v(300)&=\frac{5}{2}+\frac{5}{2}\cos\left(\frac{\pi \cdot 300}{60}\right)=\frac{5}{2}+\frac{5}{2}\cos(5\pi)=\frac{5}{2}+\frac{5}{2}\cdot (-1)=0
\end{align*}

So this formula indeed gives the right values at the moments in time $t=120$ and $t=300$. However, there are many other formulas with this property. For instance, we could consider

$$
 \tilde{v}(t)=\frac{25}{4}-\frac{t}{48}
$$

for $0\leq t\leq 600$. Then, we find

\begin{align*}
 \tilde{v}(60)=\frac{25}{4}-\frac{60}{48}=5,\qquad \tilde{v}(300)=\frac{25}{4}-\frac{300}{48}=0
\end{align*}

so this formula also gives the right values at the moments in time $t=120$ and $t=300$ (we use the symbol $\tilde{v}$ to distinguish between this formula and the previous one). So which of these is correct? Without knowing more about are journey, it is impossible to know for sure, but, in this case, one is definitely more realistic than the other. For instance, at $t=600$ we have

$$
 v(600)=\frac{5}{2}+\frac{5}{2}\cos\left(\frac{\pi \cdot 600}{60}\right)=5,\qquad \tilde{v}(600)=\frac{25}{4}-\frac{600}{48}=-\frac{25}{4}
$$

So for the formula $\tilde{v}(t)=\frac{25}{4}-\frac{t}{48}$ we obtain a negative speed and since we were not taking into account in which direction we were moving a negative speed does not make any sense. So the first formula is, physically speaking, more realistic. Does that mean that it is correct, though? Probably not, since we have only specified the speed at two points in time and a lot can happen at different points. Hence, it would be a major coincidence that the formula we provided perfectly described our movement. Still, we can use this formula to model our journey. Moreover the more points in time we specify what the speed should be, the realistic we can choose our model.

In fact, in almost all processes in nature, science and engineering one quantity depends on another quantity (or perhaps on multiple quantities) and can, therfore, be described by means of a funciton. The branch of mathematics concerned with finding functions describing natural phenomena is called **mathematical modelling**. In this book, the focus is not on the modelling part. Instead, we usually assume that the function is given to us and by analyzing it, we aim to understand the underlying process. 

From a purely mathematical standpoint, functions are equally fundamental. Indeed, most mathematical procedures where one mathematical object is turned into another object can be described by means of a function. As such, understanding what functions are and what you can and cannot do with them is essentially everything that we do in calculus, and mathematical analysis more broadly.

(Subsec:Functions1dConcepts)=

## Basic concepts

We start off this section by giving a few essential definitions.

::::::{prf:definition} 
:label: Def:Functions1var:Function

A **function** $f$ is a rule that assigns to each $x$ is a set $D$ a unique element, usually denoted by $f(x)$, in a set $C$. The set $D$ is called the **domain** of the function, while the set $C$ is called the **codomain** of the function.

::::::

::::::{prf:notation} 
:label: Notation:Functions1var:Function

If $f$ has domain $D$ and codomain $D$ we write $f:D\rightarrow C$. We also write $x\mapsto y$ when $f(x)=y$.
::::::

So how should you think about a function? There are several different perspectives you can take, but it maybe helpful to think about a function as a machine that takes an **input value** $x$ and turns this into an **output value** or **function value** $f(x)$. We also say that $x$ is **mapped into** $f(x)$ Note that a function only works in one direction: we can always insert an element of the domain to obtain an element of the codomain, but it is not always possible to go back, see {numref}`Section:Inverse`.

:::::{margin}
::::{figure} Images/Fig-Functions1var-Diagram.png
:name: Fig:Functions1var:Diagram

A diagram can be used to graphically represent that a function $f$ maps an element $x$ in the domain $D_f$ to another element $f(x)$ in the codomain $C_f$.
::::
:::::

Alternatively, for a function that is defined by $f(x)=y$, we see that $y$ is determined by $x$. That means that the value of $y$ depends on the value of $x$, while the value of $x$ can be chosen freely (within the domain of $f$). As such, for this formula $f(x)=y$ the variable $y$ is referred to as the **dependent variable**, while $x$ is an **independent variable**.

In this book, the domain and codomain will almost always be (subsets of) $\mathbb{R}^m$ and $\mathbb{R}^n$ respectively, for some integers $n,m\geq 1$. In the first few chapters, we will specifically focus on functions where the domain and codomain are both (subsets of) the real numbers $\mathbb{R}$. Such a function is usually referred to as a **function of one variable** or a **function of a single variable**. For many such functions, it is possible to define the function by means of a formula, of which an example is given below. 

::::::{prf:example} 
:label: Ex:Functions1var:Formula

Consider the function $f:\mathbb{R}\rightarrow\mathbb{R}$ given by $f(x)=x^2$. This is the function that for each real number $x$ that is put into the function outputs the real number $x^2$. For instance, for the input value $x=2$, we obtain the output 

$$
 f(x)=f(2)=2^2=4.
$$

Similarly, we obtain 

$$
 f(-3)=(-3)^2=9
$$

Note that each input value gives a unique output values, but there are output values that have multiple input values. Indeed, we note that

$$
 f(3)=3^2=9
$$

so both the input values $-3$ and $3$ are mapped into the output value $9$. Finally, notice that not all potential output values are actually reached. Indeed, the number $-1$ is in the codomain, but there is no real number $x$ with $f(x)=x^2=-1$ (note that we specified the domain of $f$ to be $\mathbb{R}$, so we are not interested in complex values of $x$ here).

::::::

::::::{prf:example} 
:label: Ex:Functions1var:Noformula

Although most functions in this book can be described by means of formula, this does not need to be the case. Moreover, the domain and/or codomain do not need to be part of $\mathbb{R}^n$. For instance, we can let $D$ be the set that contains $3$ people, Alice, Bob and Charlie, and let $f$ be the function that maps a person to their age. So, we could write this down like $f(\mathrm{Alice})=31$, $f(\mathrm{Bob})=66$ and $f(\mathrm{Charlie})=19$. Here, the output is still a number, but even that does not need to be the case. For instance, we could let $g$ be the function that gives the first letter of a person's name, so we could write $g(\mathrm{Alice})=\mathrm{A}$, $f(\mathrm{Bob})=\mathrm{B}$ and $f(\mathrm{Charlie})=\mathrm{C}$. This might seem a bit silly, but it actually quite beneficial that a lot of results that we develop in this section can also be applied to any type of domain or codomain, since it makes it possible to directly use these results in a more abstract mathematical setting.

::::::

Although the domain and codomain of a function are integral parts of the function, we often do not explicitly state them. Most functions that we will encounter are defined by a formula and for those functions we will implicitly assume that the domain consists precisely of those values of $x$ for which the formula 'makes sense'. In addition, almost all functions in this course will have $\mathbb{R}$ as the codomain (exceptions can be found in {numref}`Section:VerctorCalculusIntro`), so we will implicitly assume that we are always dealing with these type of functions. Let us make these conventions a bit more explicit.

::::::{prf:definition} 
:label: Def:Functions1var:Maxdomain

Let $f$ be a function with codomain $\mathbb{R}$ that is defined by a formula. Then the **maximal domain** or **natural domain** is the set of all values of $x$ for which this formula makes sense.

::::::

::::::{important}
Whenever we do not specifiy the codomain of a function, we assume this codomain is the real numbers $\mathbb{R}$.
::::::

::::::{important}
Whenever we define a function by means of a formula and we do not specify the domain, we assume that the domain is equal to the maximal domain.
::::::

::::::{important}
In the chapters listed under "Single-variable functions", whenever we talk about a function and neither give a formula, nor specify the domain, we assume that the domain is a subset of the real numbers $\mathbb{R}$.
::::::

The codomain of a function should be thought of as the set of all potential output values. However, in {prf:ref}`Ex:Functions1var:Formula` we saw that not every value in the codomain is reached necessarily. Still, it is interesting to find out which elements in the codomain are actually reached. For this, we have the following definition.

::::::{prf:definition} 
:label: Def:Functions1var:Range

Let $f$ be a function with domain $D$ and codomain $C$. Then the **range** $R$ of $f$ is the set of all function values of $f$. That is, we have

$$
 R=\left\{y\,\mathrm{in}\,C\,\middle|\,\text{There is an }x\,\mathrm{with}\,f(x)=y\right\}=\left\{f(x)\,\middle|\,x\,\mathrm{in}\,D\right\}
$$
::::::

::::::{note}
The range is a subset of the codomain.
::::::

::::::{prf:example} 
:label: Ex:Functions1var:MaxdomRange

Let $f$ be the function defined by $f(x)=3+\sqrt{x-2}$. Since this function is defined by a formula, we assume that its domain is equal to the maximal domain. So what is the maximal domain is this case? For that, we need to find out for which values of $x$ the expression $3+\sqrt{x-2}$ makes sense. The only restriction we have is that we cannot enter negative numbers into a square root, so the expression is defined precisely when $x-2\geq 0$, i.e. when $x\geq 2$. So the maximal domain is the set of all $x$ with $x\geq 2$, i.e. the interval $[2,\infty)$.

We can also determine the range of this function. Since every nonnegative number has a square root, while negative numbers do not have a square root, the expression $\sqrt{x-2}$ can take on any value in take on any value in the interval $[0,\infty)$. Adding $3$ to this square root raises all output values by $3$, so the function $f$ can take on any value in the interval $[3,\infty)$. This interval must, therefore, be the range of $f$.
::::::

::::::{prf:example} 
:label: Ex:Functions1var:Naturaldomain

Consider a container full of gas of constant volume $V_0$, measure in cubic meters. Then the Ideal Gas Law states that the temperature $T$ of the gas, measured in kelvins, is related to the pressure $P$, measured in pascals, by 

$$
 PV_0=nRT
$$

Hier in de margin een ChatGPT foto van een gastank.

Here $n$ is the amount of substance of gas, measured in moles, and $R$ is the ideal gas constant. By writing

$$
 T=\frac{PV_0}{nR}
$$

we see that if the pressure increases the temperature increases, while if the pressure decreases the temperature decreases. As such, we can think of the temperature as being a function of the pressure, so we can write $T=f(P)=\dfrac{PV_0}{nR}$. So what is the domain of this function? Mathematically, the formula $\dfrac{PV_0}{nR}$ is defined for each value of $P$, so the maximal domain would be the entire real line $\mathbb{R}$. However, physically, a negative pressure cannot occur, so we should, at the very least, impose that $P\geq 0$. Moreover, for very extreme conditions the ideal gas law (which is only an approximation for the behaviour of real life gasses to begin with) will no longer accurately describe the behaviour of the tank. So we note that the domain in which the relation between $P$ and $T$ is valid, is quite a bit smaller than the mathematical maximal domain. As such, it is necessary to be aware of the distinction between the maximal domain and the actual domain whenever physical quantities are involved.
::::::

(Subsec:Functions1dGraphs)=

## Graphs

An essential part of understanding functions of a single variable is to try to visualise their behaviour. In principle, a function is a rule that maps an element $x$ to another element $f(x)$, so how is it possible to visualise this? Since each $x$ in the domain corresponds to exactly one $f(x)$, we could try to plot the point $(x,f(x))$ in $\mathbb{R}^2$. Then, if we do this for each value of $x$, we have captured the full behaviour of the function in one picture. Such a plot is called the **graph** of a function. So for each point $(x,y)$ on the graph of $f$ we necessarily have $f(x)=y$. However, there is one major restriction here, and that is that we only have a finite amount of space to draw the plot on. So, for instance, if the function is defined for all $x$ in $\mathbb{R}$ it is impossible to plot the full graph of the function, since we would need an infinite amount of space to do so. Still, in such a case it is possible to plot only part of the graph and try to make sure that this part captures as much qualitative behaviour of the function as possible.

:::::{margin}
::::{figure} Images/Fig-Functions1var-Graphbasic.png
:name: Fig:Functions1var:Graph

The graph of a function $f$ can be used to reach of the value $f(a)$ for a given value $a$. The domain and range of $f$ can also be read off from the graph.
::::
:::::

::::::{prf:definition} 
:label: Def:Functions1var:Graph
If $f$ is a function with domain $D$ then the **graph** of $f$ is the set of all pairs $(x,f(x))$. That is, it is the set $\left\{(x,f(x))\,\middle|\,x\,\mathrm{in}\,D\right\}$. 
::::::

For most functions that we will encounter in this book, the graph looks like one or several curves in $\mathbb{R}^2$. For instance, the graph of the function $f(x)=x^2$ is the curve of all points $(x,y)$ with $y=x^2$, so the graph is a parabola. So we might wonder: is any curve in $\mathbb{R}^2$ the graph of a certain function? For instance, is the circle with radius $1$, centered around the origin, the graph of some function? Well, suppose that there would be some function $f$ which has this circle as its graph. Since the point $(0,1)$ is on the circle, that should mean that $f(0)=1$. However, the point $(0,-1)$ is also on this circle, so that should mean that $f(0)=-1$. Since for a function, a given input ($0$ in this case) can only have a single output, it is implossible that $f(0)$ is both $1$ and $-1$ at the same time. As such, this circle cannot be the graph of any function.

So how could we have seen this in advance? Well, the reason why the circle was not the graph of a function was that there were two different points on this circle which had the same $x$-coordinate. That means that the vertical line $x=0$ intersects the circle at two different points. This idea can be generalized as follows: the only reason a curve is not the graph of some function, is that there are two different points on the curve that have the same $x$-coordinate. In such a case, there would be a vertical line that intersects the curve at more than once. Reversely, a vertical line $x=a$ intersect the graph of a function $f$ exactly once if $a$ is in the domain of $f$ (they intersect at the point $(a,f(a))$), while such a vertical line does not intersect the graph at all if $a$ is not in the domain of $f$. We can formulate this result as follows.

::::::{prf:theorem} Vertical line test 
:label: Thm:Functions1var:Verticallinetest
A curve in $\mathbb{R}^2$ is the graph of a function precisely when each vertical line of the form $x=a$ for some real number $a$ intersects the curve at most once.
::::::

You will learn more about curves that are not (necessarily) the graph of a function in {numref}`Section:Curves`.

::::::{prf:example} 
:label: Ex:Functions1var:Verticalline

Consider the two curves shown below.

Hier twee plaatjes, links de grafiek van sin(x)+x, rechts de krome x^3+y^3-3xy. Niet erbij zetten wat ze zijn. Misschien nuttig om een versleepbare verticale lijn in beiden te hebben die goed de snijdpunten laat zien.

Can we check whether these curves are the graph of a function? For the curve on the left, each vertical line intersects the curve exactly once, so this curve is the graph function. You might wonder which function this curve is the graph of. Without further knowledge of the function, this is impossible, unfortunately. Still, for a given value of $x$, we can read off what the function value $f(x)$ will be approximately. For instance, we can read off that $f(0)=0$ (or maybe something very close to $0$), while $f(1)\approx 2$.

The curve on the right, on the other hand, is not the graph of a function. Some vertical lines, like the line $x=-1$ intersect the curve once, but there are also vertical line that intersect the curve multiple times, such as the line $x=1$, which intersects the curve $3$ times. If this curve were to be the graph of a function $f$, then $f(1)$ would need to be all three corresponding values of $y$ at the same time, which is impossible.
::::::

::::::{prf:example} 
:label: Ex:Functions1var:Verticalline2

Let $C_1$ be the curve given by all points $(x,y)$ that satisfy the equation $x^2-y^3=0$. Is this curve the graph of a function, and if so, of which function? We could try to plot this function and apply the vertical line test, but that is rather hard to do without plotting software. It is also not necessary. Indeed, we can rewrite the equation as

$$
 x^2-y^3=0,\quad \Longleftrightarrow\quad y^3=x^2,\quad \Longleftrightarrow\quad y=\sqrt[3]{x^2}=x^{\frac{2}{3}}
$$

So each point $(x,y)$ on the curve actually satisfies $y=x^{\frac{2}{3}}$. So that means that $C_1$ is the graph of the function $f$ with $f(x)=x^{\frac{{2}{3}}}$.

Similarly, we can let $C_2$ be the curve given by all points $(x,y)$ that satisfy the equation $x^2-y^2=0$. Here, we could try a similar approach and write

$$
 x^2-y^2=0,\quad \Longleftrightarrow\quad y^2=x^2,\quad \Longleftrightarrow\quad y=\pm x
$$

Now, the expression $\pm x$ might look like a formula describing a function to you, but it is not. Indeed, for $x=1$, we obtain $y=\pm 1$, so we obtain two different output values for a single input value, which is impossible. So this curve cannot be the graph of a function.

This result is also visible in the plot of the two curves, shown below.

Hier een plaatje van de twee krommen.
::::::

(Subsec:Functions1dElementary)=

## Standard functions

Many functions can be expressed in terms of other functions. In {numref}`Section:Propertiesfunctions` we will see several ways we can combine two functions into another function (for instance, by addition, multiplication or composition). As such, we use this section to define the 'building blocks', that is, the most commonly occuring functions that can be used to build more complicated functions. Several of these we have already encoutered in {numref}`Section:Numbersandcoordinate` though we did not call them functions back then. The functions we will discuss in this section are often referred to as standard functions (though there are functions that are called standard functions that are not discussed in this section, such as logarithms).

The most standard of standard functions are the polynomials. These come in various flavours, of which we will give the most important ones their own names.

::::::{prf:definition} 
:label: Def:Functions1var:Polynomial
A function $f$ is called a **polynomial function** if $f(x)=a_nx^n+a_{n-1}x^{n-1}+...+a_1x+a_0$ for some integer $n\geq 0$ and real numbers $a_0,a_1,...,a_n$. If $a_n\neq 0$ (so that $x^n$ is highest power of $x$ that occurs in the formula describing $f$), we say that the **degree of the polynomial** is $n$. A **linear function** is a polynomial function of degree $1$, i.e. one that can be written as $f(x)=a_1x+a_0$, a **quadratic function** is a polynomial function of degree $2$, i.e. one that can be written as $f(x)=a_2x^2+a_1x+a_0$, and a **cubic function** is polynomial function of degree $3$, i.e. one that can be written as $f(x)=a_3x^3+a_2x^2+a_1x+a_0$.
::::::

::::::{prf:definition} 
:label: Def:Functions1var:Rational
A **rational function** $r$ is a function that can be expressed as the ratio of two polynomials:

$$
r(x) = \frac{p(x)}{q(x)},
$$

where $p(x)$ and $q(x)$ are polynomials and $q(x) \neq 0$.
::::::

Rational functions will be discussed more extensively in {numref}`Sec:RationalFunctions`.

In {numref}`Section:Trigonometry` we saw that for an angle $\theta$ we can the trigonometric ratios $\sin(\theta)$, $\cos(\theta)$ and $\tan(\theta)$. As such, the sine, cosine and tangent take an angle as input and give a number back as output, which means that they are actually functions.

::::::{prf:definition} 
:label: Def:Functions1var:Trigonometry
The functions $f(x)=\sin(x)$, $f(x)=\cos(x)$ and $f(x)=\tan(x)$ are called the **trigonometric functions**.
::::::



In this section we cover:

- What is a function? (notation, (in)dependent variable)
- Domain and maximal domain
- Range and codomain
- Graphs (including vertical line test)
- Differences and similarities between graphs and curves
- Elementary functions (linear/quadratic/cubic,polynomials,power functions, rational functions, algebraic functions, exponential functions (hier moet definitie staan, ook e-macht, rekenregels nog verwijzen bij inverse functies), trigonometric functions. NOT YET: logarithms and inverse trigonometric functions)
- Hyperbolic functions?
- Piecewise defined functions (e.g. step functions)
