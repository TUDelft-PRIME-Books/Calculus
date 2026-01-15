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

Recall that made the convention that, unless specified otherwise, the domain of a function is its maximal domain. So what does this tell us about the domains of functions like $f+g$ or $\frac{f}{g}$? For $f+g$, we defined $(f+g)(x)=f(x)+g(x)$, so whenever $f(x)$ and $g(x)$ both exist, we can define their sum and, with that, we can define $(f+g)(x)$. As such, the domain of $f+g$ are precisely those $x$ that are both in the domain of $f$ and the domain of $g$. That is, the domain of $f+g$ is the intersection of the domains of $f$ and $g$.

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

In {prf:ref}`Ex:Propertiesfunctions:Sum` we saw that we can obtain the graph of $f+g$ from the graphs of $f$ and $g$ by stacking one on top of the other. For other combinations of functions like the product $fg$ or the composition $f\circ g$, this is a bit trickier in most cases. However, we can also reverse this question. For instance, if we take the graph of a function $f$ as shift every point $1$ to the right we obtain the graph of a different function (indeed, the result of shifting the graph to the right is a curve in $\mathbb{R}^2$ that still passes the vertical line test ({prf:ref}`Thm:Functions1var:Verticallinetest`)). The main question now is: which function gives this graph. Let us call this new function $g$. Since we obtained the graph of $g$ by shifting the graph of $f$ $1$ to the right, a point $(x,y)$ lies on the graph of $g$ precisely when $(x-1,y)$ lies on the graph of $f$. Since $(x,y)$ lies on the graph of $g$ precisely when $g(x)=y$, while $(x-1,y)$ lies on the graph of $f$ precisely when $f(x-1)=y$, we find that $g(x)=f(x-1)$. We say that we performed a **horizontal shift** of $1$ to the right to obtain $g$ from $f$.

Similarly, we can perform a **vertical shift** of $2$ downwards to the graph of $f$ to obtain the graph of a new function $h$. Since $(x,y)$ is on the graph of $h$ precisely when $(x,y+2)$ on the graph of $f$, we find that $h(x)=f(x)-2$.

We can generalize these considerations as follows.

::::::{prf:definition} 
:label: Def:Propertiesfunctions:Composition

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

::::::{prf:definition} 
:label: Def:Propertiesfunctions:Reflectionstretching

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

Notice that if we performed these 4 operations in a different order, we would obtain a different function. Indeed, if we start with the graph given by $y=\sin(x)$ and perform the vertical shift of $4$ upwards first, we obtain the graph given by $y=\sin(x)+4$. If we then perform the reflection in the $x$-axis and the vertical stretching by a factor $3$ we obtain the graph given by $y=-3\left(\sin(x)+4\right)=-3\sin(x)-12$. If we then perform the horizontal shift of $1$ to the right we obtain the graph given by y=-3\sin(x-1)-12. Finally, if we then perform the horizontal stretching by a factor $2$ we obtain the graph given by $y=-3\sin(2x-1)-12$. This function is very different from $f$, as can be seen from the graphs shown below.

Hier vijf plaatjes naast elkaar van sin(x), sin(x)+4, -3sin(x)-12, -3sin(x-1)-12 en -3sin(2x-1)-12 met pijlen er tussen om de 4 operaties te laten zien.

::::::

In this section we cover:


- Sums, products, scalar multiples 
- Composition of functions
- Vertical and horizontal shifts
- Stretching and reflecting

- Increasing and decreasing (monotonicity, strictly increasing/decreasing) (hier moet staan dat de exponentiele functie strictly monotoon is, daarna verwijzing in inverse functies aanpassen)
- Even and odd functions (parity) -> Hyperbolic functions