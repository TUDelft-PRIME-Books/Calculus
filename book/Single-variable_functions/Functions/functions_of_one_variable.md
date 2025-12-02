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

In this book, the domain and codomain will almost always be (subsets of) $\mathbb{R}^m$ and $\mathbb{R}^n$ respectively, for some integers $n,m\geq 1$. In the first few chapters, we will specifically focus on functions where the domain and codomain are both (subsets of) the real numbers $\mathbb{R}$. Such a function is usually referred to as a **function of one variable** or a **function of a single variable**. For many such functions, it is possible to define the function by means of a formula, of which an example is given below. 

::::::{prf:example} 
:label: Ex:Functions1var:Formula

Consider the function $f:\mathbb{R}\rightarrow\mathbb{R}$ given by $f(x)=x^2$. This is the function that for each real number $x$ that is put into the function outputs the real number $x^2$. For instance, for the input value $x=2$, we obtain the output 

$$
 f(x)=f(2)=2^2=4$.
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

Although most functions in this book can be described by means of formula, this does not need to be the case. Moreover, the domain and/or codomain do not need to be part of $\mathbb{R}^n$. For instance, we can let $D$ be the set that contains $3$ people, Alice, Bob and Charlie, and let $f$ be the function that maps a person to their age. So, we could write this down like $f(\mathrm{Alice})=31$, $f(\mathrm{Bob})=66$ and $f(\mathrm{Charlie})=19$. Here, the output is still a number, but even that does not need to be the case. For instance, we could let $g$ be the function that specifies who the person has a crush on, so we could write $g(\mathrm{Alice})=\mathrm{Charlie}$, $f(\mathrm{Bob})=\mathrm{Charlie}$ and $f(\mathrm{Charlie})=\mathrm{Bob}$. This might seem a bit silly, but it actually quite beneficial that a lot of results that we develop in this section can also be applied to any type of domain or codomain, since it makes it possible to directly use these results in a more abstract mathematical setting.

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
