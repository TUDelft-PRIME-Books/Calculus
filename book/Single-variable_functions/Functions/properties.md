(Section:Propertiesfunctions)=

# Properties of functions

In {numref}`Section:Functionsintro` we encountered several types of functions that we called standard functions (for instance, polynomial functions, trigonometric functions and exponential functions). In this section, we try to find in what ways we can combine these standard functions to obtain other, perhaps more complicated functions. In addition, we saw that these standard functions show some very different qualitative behaviour. For instance, exponential functions either always grow or always decay, while the sine and the cosine show periodic behaviour. We will, therefore, also use this section to define various classifications of functions and we will try to find out, if possible, which standard functions fall under which class of functions.

(Subsec:PropertisfunctionsCombinations)=

## Combining functions

There are many ways to combine several functions into a new function. We start with an example to showcase one possibility.

::::::{prf:example} Sum of two functions
:label: Ex:Propertiesfunctions:Sum
The most straightforward way to combine several functions is to use arithmic operations such as addition and multiplication. For instance, consider the function $f(x)=x^2+e^x$. We observe that this function is some sort of combination of the functions $g(x)=x^2$ and $h(x)=e^x$. Indeed, for each value of $x$ we have

$$
 f(x)=x^2+e^x=g(x)+h(x),
$$

so that the function value $f(x)$ is the sum of the function values $g(x)$ and $h(x)$. As such, we say that the function $f$ is the **sum** of the functions $g$ and $h$, and we write $f=g+h$. 

So what does the graph of $f$ look like in terms of the graphs of $g$ and $h$? For each value of $x$, we know that $f(x)=g(x)+h(x)$, so $f(x)$ is $h(x)$ higher than $g(x)$. That means that if we start from the graph of $g$, we obtain the graph of $f$ by rising the function value $x^2$ by $e^x$ for each value of $x$. This can be seen in the figure below. We can also think of this as that the graph of $g$ is stacked on top of the graph of $f$. 

```{figure} Images/schetssomfunctie.png
---
width: 100%
name: Fig:Propertiesfunctions:Sum
class: dark-light
---
Hier een mooiere versie van dit plaatje.
```

::::::

In the previous example we saw that we can take two functions and make a new function by adding the two functions. In general, we can perform arithmic operations to functions just like we can with numbers. 

::::::{prf:definition} Arithmetic with functions
:label: Def:Propertiesfunctions:Arithmetic

Let $f$ and $g$ be functions. Then we can define the following functions.

- The **sum function** $f+g$ is defined by $(f+g)(x)=f(x)+g(x)$.
- The **difference function** $f-g$ is defined by $(f-g)(x)=f(x)-g(x)$.
- The **product function** $fg$ is defined by $(fg)(x)=f(x)g(x)$.
- The **quotient function** $\frac{f}{g}$ is defined by $\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}$.
- If $c$ is a real number, then the **scalar multiple function** $cf$ is defined by $(cf)(x)=cf(x)$.
- If $c$ and $d$ are real numbers, then the **linear combination** $cf+dg$ is defined by $(cf+dg)(x)=cf(x)+dg(x)$.

::::::

Notice that each of these functions is found by applying the corresponding operation pointwise. That means that, for instance, we define the product function $fg$ by specifying that each point $x$ we evaluate the function value of $fg$ at $x$ by computing the product of the real numbers $f(x)$ and $g(x)$. 

Recall that we made the convention that, unless specified otherwise, the domain of a function is its maximal domain. So what does this tell us about the domains of functions like $f+g$ or $\frac{f}{g}$? For $f+g$, we defined $(f+g)(x)=f(x)+g(x)$, so whenever $f(x)$ and $g(x)$ both exist, we can define their sum and, with that, we can define $(f+g)(x)$. As such, the domain of $f+g$ are precisely those $x$ that are both in the domain of $f$ and the domain of $g$. That is, the domain of $f+g$ is the intersection of the domains of $f$ and $g$.

For $\frac{f}{g}$, things are a bit more complicated. Indeed, we defined $\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}$, so in order for $\left(\frac{f}{g}\right)(x)$ to exist, both $f(x)$ and $g(x)$ certainly need to exist. However, that is not sufficient. Indeed, if $g(x)=0$ for some $x$, then we cannot define $\frac{f(x)}{g(x)}$ because we cannot divide by $0$. As such, the domain of $\frac{f}{g}$ consists of those values of $x$ that are both in the domain of $f$ and the domain of $g$ **and** have $g(x)\neq 0$.

::::::{prf:example} 
:label: Ex:Propertiesfunctions:Productsanddomains

Consider the functions $r(t)=t^3$ and $s(t)=\frac{1}{t}$. Then their product function $rs$ is defined by $(rs)(t)=t^3\frac{1}{t}$. For example, for $t=2$ we have $r(2)=2^3=8$ and $s(2)=\frac{1}{2}$, which gives $(rs)(2)=r(2)s(2)=8\cdot\frac{1}{2}=4$.  For $t\neq 0$, we can simplify this expression to

$$
 (rs)(t)=t^3\frac{1}{t}=t^2.
$$

So what is the domain of the product function? You might be tempted to think that the domain is the set of all real numbers $\mathbb{R}$, since $t^2$ is defined for all values of $t$. However, $(rs)(t)$ is only equal to $t^2$ when $t\neq 0$. If $t=0$, the function value $s(0)$ is not defined as we cannot divide by $0$. As such, $0$ cannot be in the domain of $rs$. So the domain of $rs$ is the set of real numbers $\mathbb{R}$ without the point $0$, i.e. it is $\mathbb{R}\setminus\{0\}$.

Hier nog plaatje van de grafieken van $r$, $s$ en $rs$. 

::::::



::::::{prf:example} 
:label: Ex:Propertiesfunctions:Composition

Apart from arithemetic operations, there is another very common way of combining two functions. Indeed, consider the function $f(x)=e^{\sin(x)}$. This function is somehow obtain from the functions $g(x)=e^x$ and $h(x)=\sin(x)$, but how? It is not one of the way described in {prf:ref}`Def:Propertiesfunctions:Arithmetic`. Instead, we should think how you could end up with something like $e^{\sin(x)}$. The answer is the following: we are used to plugging $x$ into the formula describing a function, but we could also plug in something else. Indeed, we could plug in $\sin(x)$ into the function $g$ and obtaing $g(\sin(x))=e^{\sin(x)}$. Since $\sin(x)=h(x)$, we can write this as

$$
 g(h(x))=g(\sin(x))=e^{\sin(x)}=f(x).
$$

As such we notice that for each value of $x$ we have $f(x)=g(h(x))$. We say that $f$ is the **composition** of $g$ with $h$ and we write $f=g\circ h$. We can think of the composition $g\circ h$ as first applying $h$ and plugging the resulting number into $g$.

Notice that $g\circ h$ is **not** the same as $h\circ g$. Indeed, for any value of $x$ we can compute

$$
 (h\circ g)(x)=h(g(x))=h\left(e^x\right)=\sin\left(e^x\right).
$$

Since $e^{\sin(x)}$ and $\sin\left(e^x\right)$ typically are not equal, the functions $h\circ g$ and $g\circ h$ are not equal.

::::::

We can generalise this concept as follows. 

::::::{prf:definition} 
:label: Def:Propertiesfunctions:Composition

Let $f$ and $g$ be functions. Then we can the **composition** of $f$ with $g$, which we denote by $f\circ g$, to be defined by

$$
 (f\circ g)(x)=f(g(x)).
$$

::::::

::::::{warning} 
:name: Warning:Propertiesfunctions:Composition

The compositions $f\circ g$ and $g\circ f$ are typically not the same function.
::::::

So what can we say about the domain of the composition $f\circ g$? Since $(f\circ g)(x)=f(g(x))$, at the very least we need to able to compute $g(x)$, since otherwise we could never plug it into $f$. So for $x$ to be in the domain of $f\circ g$, $x$ needs to be in the domain of $g$. That is not all, though, since we also need to be able to plug $g(x)$ into $f$, so $g(x)$ should be in the domain of $f$. Since those are the only restrictions, the domain of $f\circ g$ consists precisely of those values of $x$ in the domain of $g$ for which $g(x)$ is in the domain of $f$. Notice that this means that it is not necessarily so that $x$ in the domain of $f\circ g$ is also in the domain of $f$; only $g(x)$ needs to be in the domain of $f$.

In {prf:ref}`Ex:Propertiesfunctions:Sum` we saw that we can obtain the graph of $f+g$ from the graphs of $f$ and $g$ by stacking one on top of the other. For other combinations of functions like the product $fg$ or the composition $f\circ g$, this is a bit trickier in most cases. However, we can also reverse questions like these. For instance, if we take the graph of a function $f$ as shift every point $1$ to the right we obtain the graph of a different function (indeed, the result of shifting the graph to the right is a curve in $\mathbb{R}^2$ that still passes the vertical line test ({prf:ref}`Thm:Functions1var:Verticallinetest`)). The main question now is: which function gives this graph? Let us call this new function $g$. Since we obtained the graph of $g$ by shifting the graph of $f$ $1$ to the right, a point $(x,y)$ lies on the graph of $g$ precisely when $(x-1,y)$ lies on the graph of $f$. Since $(x,y)$ lies on the graph of $g$ precisely when $g(x)=y$, while $(x-1,y)$ lies on the graph of $f$ precisely when $f(x-1)=y$, we find that $g(x)=f(x-1)$. We say that we performed a **horizontal shift** of $1$ to the right to obtain $g$ from $f$.

Similarly, we can perform a **vertical shift** of $2$ downwards to the graph of $f$ to obtain the graph of a new function $h$. Since $(x,y)$ is on the graph of $h$ precisely when $(x,y+2)$ on the graph of $f$, we find that $h(x)=f(x)-2$.

We can generalize these considerations as follows.

::::::{prf:theorem} 
:label: Thm:Propertiesfunctions:Shifts

Let $f$ be a function and $a>0$ be a positive real number. Then we can perform to $f$

- a **horizontal shift to the right** of size $a$ to obtain the function $g(x)=f(x-a)$;
- a **horizontal shift to the left** of size $a$ to obtain the function $g(x)=f(x+a)$;
- a **vertical shift upwards** of size $a$ to obtain the function $g(x)=f(x)+a$;
- a **vertical shift downwards** of size $a$ to obtain the function $g(x)=f(x)-a$.

::::::

Recall that for a function $f$ and a real number $c$ we defined the scalar multiple function $cf$ by $(cf)(x)$. What is the consequence of applying such a multiplication by a scalar to the graph of the function $f$? For that, we need to make a distinction between the cases where $c>0$, $c=0$ and $c<0$. 

Let us first consider the case $c>0$. In that case, $(x,y)$ is on the graph of $f$ precisely when $(x,cy)$ is on the graph of $cf$. In terms of the graph, this means that the graph of $f$ is stretched in the $y$-direction with a factor $c$ (for $0<c<1$ this stretching is actually more akin to a compression, but we will call it stretching nonetheless). If $c=0$, then $(cf)(x)=0\cdot f(x)=0$ for all $x$, so then the graph is flattened onto the $x$-axis. Finally, we consider the case $c<0$. For convenience, we first let $c=-1$. In that case $(x,y)$ is on the graph of $f$ precisely when $(x,-y)$ is on the graph of $-f$. This means that we obtain the graph of $-f$ by reflecting the graph of $f$ in the $x$-axis. Now if $c<0$ is any negative scalar, then we notice that $c=-|c|$ so that $cf=-(|c|f)$. This means that we obtain the graph of $cf$ by first stretching it in the $y$ direction with a factor $|c|$ and then reflecting it in the $x$-axis.

So going from $f$ to $cf$ corresponds to vertical stretching and/or reflecting. So what would correspond to horizontal stretching and/or reflecting? For this, let us first consider the function $h$ of which the graph is obtained by reflecting the graph of $f$ in the $y$-axis. That means that $(x,y)$ is on the graph of $h$ precisely when $(-x,y)$ is on the graph of $f$. As such, we must have $h(x)=f(-x)$. Similarly, if we obtain $h$ by stretching the graph of $f$ by a factor $c$ (with $c>0$) in the $x$-direction, then $(x,y)$ is on the graph of $f$ precisely when $(cx,y)$ is on the graph of $h$. Hence, we must have $h(x)=f(cx)$. Combining these two ideas, gives that for $c<0$ the function $h(c)=f(cx)=f(-|c|x)$ is obtained by first stretching in the $x$-direction with a factor $|c|$ and then reflecting it in the $y$-axis.

We combine these results as follows.

::::::{prf:theorem} 
:label: Thm:Propertiesfunctions:Reflectionstretching

Let $f$ be a function and $c\neq 0$ a real number. Consider the functions $g(x)=cf(x)$ and $h(x)=f(cx)$. Then, if $c>0$,

- the graph of $g$ is obtained from the graph of $f$ by **vertically stretching** it by a factor $c$;
- the graph of $h$ is obtained from the graph of $f$ by **horizontally stretching** it by a factor $c$;

while if $c<0$

- the graph of $g$ is obtained from the graph of $f$ by **vertically stretching** it by a factor $|c|$ and subsequently **reflecting** it in the $x$-axis;
- the graph of $h$ is obtained from the graph of $f$ by **horizontally stretching** it by a factor $|c|$ and subsequently **reflecting** it in the $y$-axis.

::::::

::::::{prf:example} 
:label: Ex:Propertiesfunctions:Reflectionstretching

Consider the function $f(x)=-3\sin(2x-2)+4$. How is the graph of $f$ related to the graph of the 'basic' sine function? For this, it turns out to be convenient to write

$$
 f(x)=-3\sin(2x-2)+4=-3\sin(2(x-1))+4.
$$

Starting with the graph of the sine function, which is given $y=\sin(x)$, we first perform a horizontal stretching by a factor $2$ to obtain the graph given by $y=\sin(2x)$. Then we perform a horizontal shift of $1$ to right to obtain the graph given by $y=\sin(2(x-1))$. Subsequently, we perform a reflection in the $x$-axis and a vertical stretching by a factor $3$ to obtian the graph given by $y=-3\sin(2(x-1))$. Finally, we perform a vertical shift of $4$ upwards to obtain the graph given by $y=-3\sin(2(x-1))+4$, i.e. the graph of $f$.

Hier vijf plaatjes naast elkaar van sin(x), sin(x-1), sin(2(x-1)), -3sin(2(x-1)) en -3sin(2(x-1))+4 met pijlen er tussen om de 4 operaties te laten zien.

Notice that if we performed these 4 operations in a different order, we would obtain a different function. Indeed, if we start with the graph given by $y=\sin(x)$ and perform the vertical shift of $4$ upwards first, we obtain the graph given by $y=\sin(x)+4$. If we then perform the reflection in the $x$-axis and the vertical stretching by a factor $3$ we obtain the graph given by $y=-3\left(\sin(x)+4\right)=-3\sin(x)-12$. If we then perform the horizontal shift of $1$ to the right we obtain the graph given by $y=-3\sin(x-1)-12$. Finally, if we then perform the horizontal stretching by a factor $2$ we obtain the graph given by $y=-3\sin(2x-1)-12$. This function is very different from $f$, as can be seen from the graphs shown below.

Hier vijf plaatjes naast elkaar van sin(x), sin(x)+4, -3sin(x)-12, -3sin(x-1)-12 en -3sin(2x-1)-12 met pijlen er tussen om de 4 operaties te laten zien.

::::::

(Subsec:PropertisfunctionsIncreasingdecreasing)=

## Increasing and decreasing functions

When analysing the graph of a function, one of the most eye-catching properties is where the graph goes up and where it goes down. In more mathematical terms, we say that the function increases when the graph goes up and the function decreases when the graph goes down. 

::::::{prf:definition} 
:label: Def:Propertiesfunctions:Increasingdecreasing

Let $f$ be a function and $(a,b)$ be an interval that is contained in the domain of $f$. Then we say that $f$ is **increasing** on the interval $(a,b)$ whenever for each two points $a<x_1<x_2<b$ in this interval we have $f(x_1)\leq f(x_2)$. Similarly, we say that $f$ is **decreasing** on the interval $(a,b)$ whenever for each two points $a<x_1<x_2<b$ in this interval we have $f(x_1)\geq f(x_2)$.

::::::

::::::{prf:example} 
:label: Ex:Propertiesfunctions:Increasingdecreasing


A function can be increasing on some parts on its domain, while it is decreasing on other parts of its domain. For instance, consider the function $f(x)=x^2$, of which the graph is shown below.

Hier de grafiek van $f(x)=x^2$

The graph suggests that the function increases on the interval $(0,\infty)$. Indeed, if we have $0<x_1<x_2$ then we have $f(x_1)=x_1^2<x_2^2=f(x_2)$. 

Similarly, on the interval $(-\infty,0)$ the function is decreasing. Indeed, if we have $x_1<x_2<0$ then we have $0<-x_2<-x_1$, so we obtain $f(x_1)=x_1^2=(-x_1)^2\geq (-x_2^2)=x_2^2=f(x_2)$.

However, on the interval $(-2,2)$ the function is neither increasing, nor decreasing. Indeed, we have $-1$ and $0$ are numbers in this interval with $-1<0$ and we have $f(-1)=1>0=f(0)$, so $f$ is not increasing on this interval. On the other hand, $0$ and $1$ are also numbers in this interval and they have $0<1$ and $f(0)=0<1=f(1)$, so $f$ is not decreasing on this interval.

::::::

::::::{prf:example} 
:label: Ex:Propertiesfunctions:Increasingdecreasingflat

Consider the piecewise defined function $k(t)=\left\{\begin{array}{ll}t-3,\quad&\text{if }t<0;\\ 2,\quad&\text{if }0\leq t\leq 1;\\ t+4,\quad&\text{if }t>1.\end{array}\right.$
The graph of the function is shown below.

Hier de grafiek van de functie $k$.

From the graph of the function, we see that the function is definitely increasing on the intervals $(-\infty,0)$ and $(1,\infty)$, but what about the interval $[0,1]$? The graph of the function is horizontal there, so it does not seem to "grow" on this interval. Still, according to the definition that we used, the function is increasing on this interval. Indeed, for any $0<t_1<t_2<1$ we have $k(t_1)=2\leq 2=k(t_2)$. We conclude that the function is indeed increasing on this interval. Moreover, it is also decreasing on the same interval as for any $0<t_1<t_2<1$ we have $k(t_1)=2\geq 2=k(t_2)$. In general, a function is both increasing and decreasing on a certain interval precisely when it is constant on that interval.

In fact, the function is increasing on its entire domain. Indeed, we already know that it is increasing on each of the intervals $(-\infty,0)$, $[0,1]$ and $(1,\infty)$. So we only need to consider what happens if we have two values of $t$ that are in different intervals. First consider $t_1$ in $(-\infty,0)$ and $t_2$ in $[0,1]$. Then $t_1<0$, so $k(t_1)=t-3\leq -3<2=k(t_2)$. Similarly if $t_1$ is in $[0,1]$ and $t_2$ is in $(1,\infty)$ then $t_2>1$, so we find $k(t_2)=t+4>5>2=k(t_1)$. Finally, if $t_1$ is in $(-\infty,0)$ and $t_2$ is in $(1,\infty)$, then $t_1<t_2$, so we must have $k(t_1)=t_1-3<t_2-3<t_2+4=k(t_2)$. We find that $k$ is increasing on its entire domain.

::::::

In {prf:ref}`Ex:Propertiesfunctions:Increasingdecreasingflat` we saw that a constant function is both increasing and decreasing. Sometimes, we want to specifically look at functions that actually grow. For this, we adopt some new terminology.

::::::{prf:definition} 
:label: Def:Propertiesfunctions:Strictlyincreasingdecreasing

Let $f$ be a function and $(a,b)$ be an interval that is contained in the domain of $f$. Then we say that $f$ is **strictly increasing** on the interval $(a,b)$ whenever for each two points $a<x_1<x_2<b$ in this interval we have $f(x_1)< f(x_2)$. Similarly, we say that $f$ is **strictly decreasing** on the interval $(a,b)$ whenever for each two points $a<x_1<x_2<b$ in this interval we have $f(x_1)> f(x_2)$.

::::::

In particular, constant functions are increasing and decreasing, but neither strictly increasing nor strictly decreasing.

::::::{warning} 
:name: Warning:Propertiesfunctions:Strictlyincreasingdecreasing

In some literature, the terminology increasing and decreasing is used for what we call strictly increasing and strictly decreasing (so in those books, constant functions are neither increasing nor decreasing). Usually, the terms **nondecreasing** and **nonincreasing** are then used for what we call increasing and decreasing. We will stick to the terms used in this section, but be aware of this when you read other literature.
::::::

Showing that a function is increasing or decreasing can be tricky in practice. In {numref}`Chapter:Differentiation` we will learn a more efficient way to determine this. For future reference, we already show that exponential functions are either always strictly increasing or always strictly decreasing or constant.

::::::{prf:theorem} 
:label: Thm:Propertiesfunctions:Expincrdecr

Let $a>0$ and consider the exponential function $f(x)=a^x$. If $0<a<1$, the function $f$ is strictly decreasing on $\mathbb{R}$. If $a>1$, the function $f$ is strictly decreasing on $\mathbb{R}$. If $a=1$, the function $f$ is constant, and, therefore, both increasing and decreasing on $\mathbb{R}$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Propertiesfunctions:Expincrdecr`
:class: tudproof
This follows directly from {prf:ref}`Thm:RealNumbers:ExpCalcReal`.
:::

(Subsec:PropertisfunctionsEvenodd)=

## Even and odd functions

The graph of a function can possess many different symmetries. In this section, we consider the two most important ones.

First, let $f$ be a function of which the graph is symmetric in the $y$-axis. That is, a point $(x,y)$ lies on the graph of $f$ precisely when $(-x,y)$ lies on the graph of $f$. Since $(x,y)$ lies on the graph of $f$ precisely when $f(x)=y$, we find that we must have $f(-x)=f(x)$ for each $x$ in the domain of $f$. As we saw in {prf:ref}`Ex:Functions1var:Cubicandhigher` functions of the form $f(x)=x^n$ with $n$ even have this property. Indeed, for such a function we have

$$
 f(-x)=(-x)^n=(-1)^nx^n=1\cdot x^n=x^n=f(x).
$$

As such, we will call such a function **even**. Other examples of even functions include $f(x)=|x|$ and $f(x)=\cos(x)$. 

In the same example, we saw that functions of the form $f(x)=x^n$ with $n$ odd also possess a certian symmetry. Indeed, for such a function we have

$$
 f(-x)=(-x)^n=(-1)^nx^n=(-1)\cdot x^n=-x^n=-f(x).
$$

So we find that for these functions the point $(x,y)$ lies on the graph of $f$ precisely when $(-x,-y)$ lies on the graph of $f$. This means that the graph of the function is symmetric in the origin. Such a function will be called **odd**. Other examples of odd functions include $f(x)=\sin(x)$ and $f(x)=\tan(x)$ (the latter only when restricted to the interval $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$).

::::::{prf:definition} 
:label: Def:Propertiesfunctions:Evenodd

Let $f$ be a function. Then $f$ is called **even** if $f(-x)=f(x)$ for all $x$ in the domain of $f$. In addition, $f$ is called **odd** if $f(-x)=-f(x)$ for all $x$ in the domain of $f$.

::::::

::::{figure} Images/even.png
:name: Fig:Propertiesfunctions:Even
:class: dark-light

The graph of an even function is symmetric in the $y$-axis.

::::

::::{figure} Images/odd.png
:name: Fig:Propertiesfunctions:Odd
:class: dark-light

The graph of an odd function is symmetric in the origin.

::::


::::::{prf:example} 
:label: Ex:Propertiesfunctions:Evenodd

Consider the function $f(x)=|x|\sin(x)$. Then for any $x$ we have

$$
 f(-x)=|-x|\sin(-x)=|x|\sin(-x)=|x|\left(-\sin(x)\right)=-|x|\sin(x)=-f(x).
$$

As such, the function $f$ is odd. Note that $f=gh$ with $g(x)=|x|$ and $h(x)=\sin(x)$. By inspecting the computation above, you can see that $g(-x)=g(x)$ and $h(-x)=-h(x)$. So $g$ is even, while $h$ is odd. It is true, in general, that the product of an even and an odd function is odd again. You could make a list of whether a sum or product of any combination of even and odd functions is even again, but in practice, it is usually quicker to just plug $-x$ into your function and see where you end up.

Hier nog de grafiek van f met de symmetrie erin aangegeven.
::::::

::::::{prf:example} 
:label: Ex:Propertiesfunctions:Notevenodd

Consider the function $f(x)=x^2+x$. Then $f=g+h$ with $g(x)=x^2$ and $h(x)=x$, so $f$ is the sum of an even and an odd function. However, $f$ itself is neither even nor odd. Indeed, for any $x$ we have

$$
 f(-x)=(-x)^2+(-x)=x^2-x
$$

and this is not (necessarily) equal to $f(x)$ or to $-f(x)$. Indeed, we find $f(2)=6$, while $f(-2)=2$ which is neither $f(2)$ nor $-f(2)$. So in general, the sum of an even and an odd function will be neither even nor odd, though exceptions exist. Can you come up with one?

Hier nog de grafiek van f.

::::::

Sometimes, it turns out to be convenient to write a function as the sum of an even and an odd function. The following theorem shows how we can construct these new functions.

::::::{prf:theorem} 
:label: Thm:Propertiesfunctions:Evenoddparts

Let $f$ be a function that is defined on a symmetric interval of the form $(-a,a)$ for some $a>0$. On this interval, $f$ can uniquely be written as $f=f_e+f_o$ with $f_e$ an even function and $f_0$ an odd function. The function $f_e$ is called the **even part** of $f$ and is given by $f_e(x)=\frac{f(x)+f(-x)}{2}$, while the function $f_0$ is called the **odd part** of $f$ and is given by $f_o(x)=\frac{f(x)-f(-x)}{2}$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Propertiesfunctions:Evenoddparts`
:class: tudproof,dropdown
We consider the functions given by $f_e(x)=\frac{f(x)+f(-x)}{2}$ and $f_o(x)=\frac{f(x)-f(-x)}{2}$. We first note that for any $x$ we have

$$
 f_e(-x)=\frac{f(-x)+f(-(-x))}{2}=\frac{f(-x)+f(x)}{2}=f_e(x),
$$

while

$$
 f_o(-x)=\frac{f(-x)-f(-(-x))}{2}=\frac{f(-x)-f(x)}{2}=-\frac{f(x)-f(-x)}{2}=f_e(x).
$$

Moreover, we find that

$$
 f_e(x)+f_o(x)=\frac{f(x)+f(-x)}{2}+\frac{f(x)-f(-x)}{2}=\frac{f(x)+f(-x)+f(x)-f(-x)}{2}=\frac{2f(x)}{2}=f(x).
$$

So we obtain that $f=f_e+f_o$ and that $f_e$ is even and $f_o$ is odd.

Now we show that this decomposition is unique, so we write $f=g+h$ with $g$ even and $h$ odd and aim to show that $g=f_e$ and $h=f_o$. Then we find

$$
 2f_e(x)=f(x)+f(-x)=\left(g(x)+h(x)\right)+\left(g(-x)+h(-x)\right)=\left(g(x)+h(x)\right)+\left(g(x)-h(x)\right)=2g(x)
$$

and

$$
 2f_o(x)=f(x)-f(-x)=\left(g(x)+h(x)\right)-\left(g(-x)+h(-x)\right)=\left(g(x)+h(x)\right)-\left(g(x)-h(x)\right)=2h(x).
$$

Hence, we must have $g=f_e$ and $h=f_0$, as desired.
:::

The even and odd parts of the exponential function are so common that they have their own names.

::::::{prf:definition} 
:label: Def:Propertiesfunctions:Hyperbolic

Consider the exponential function $f(x)=e^x$. The **hyperbolic cosine function**, denoted by $g(x)=\cosh(x)$, is the even part of $f$. That is, we have $\cosh(x)=\frac{e^x+e^{-x}}{2}$. The **hyperbolic sine function**, denoted by $h(x)=\sinh(x), is the odd part of $f$. That is, we have $\sinh(x)=\frac{e^x-e^{-x}}{2}$.

Finally, the **hyperbolic tangent function** is defined by $\tanh(x)=\frac{\sinh(x)}{\cosh(x)}$.

::::::

Hier de grafieken van cosh(x), sinh(x) en tanh(x).

The naming of these functions suggests some sort of connection to the trigonometric functions. Indeed, the hyperbolic sine and cosine have an interpretation similar to the regular sine and cosine when using [hyperbolic angles](https://en.wikipedia.org/wiki/Hyperbolic_angle) instead of regular angles. Moreover, the derivatives (see {numref}`Chapter:Differentiation`) of the hyperbolic functions follow a similar, though slightly different, pattern to those of the trigonometric functions. Finally, the sine and the hyperbolic sine are both odd functions, while the cosine and the hyperbolic cosine are both even functions.


