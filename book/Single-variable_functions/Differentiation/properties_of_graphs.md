(Section:GraphsDerivatives)=

# Properties of graphs

## Introduction



In this section, we will specifically see what the first and second derivatives say about the graph of a function. The ideas presented here can be generalized to give interpretations of higher order derivatives, but these are typically less useful in practice.

## Convexity, concavity and inflection points

In {numref}`Subsec:MinMax:Incrdecr` we saw how we can use the first derivative to say something about the graph of a function. However, we have not found any uses for higher order derivatives yet. In this subsection we will focus on the second derivative.

Consider the functions $f(x)=\sin\left(\frac{\pi}{2}x\right)$ and $g(x)=x^2$ on the interval $[0,1]$. Both functions are strictly increasing on this interval, but they still show very different behaviour in their growth. Indeed, the function $f$ first grows quickly and then slows down, while for the function $g$ it is the other way around.

:::{figure} Images/Fig-Graph1d-Intro.png
:name: Fig:Graphsderivatives:Intro

On the left the graphs of the functions $f(x)=\sin\left(\frac{\pi}{2}x\right)$ and $g(x)=x^2$ on the interval $[0,1]$. On the right the graphs of their derivatives.
:::

:::{todo}
Replace {numref}`Fig:Graphsderivatives:Intro` with an applet. Maybe nice if you can slide the point $(x,0)$ and see the corresponding points on the graphs of $f$ and $g$ and their derivatives.
:::

We can see this behaviour back in the derivatives of these functions. If we look at the graphs of the derivatives of these functions, we see that the function $f'$ is strictly decreasing, while the function $g'$ is strictly increasing. This matches the behaviour that we observed in the original function. Indeed, the fact that the function $f'$ is strictly decreasing, means that the slope of the original function $f$ gets lower so that it grows slower. On the other hand, the function $g'$ is strictly increasing, so the slope of the function $g$ strictly increases as well, which means that the function grows more quickly. So how can we establish that $f'$ strictly decreases and $g'$ strictly increases? The same way you would do that for any other function: you check whether the derivative is positive or negative. This means that in order to distinguish between the behaviour of the functions $f$ and $g$, we should take a look at the derivatives of their derivatives, so at their second derivatives. We will call the function $f$ **concave** and the function $g$ **convex**.

Stated plainly, concave functions bend downwards, while convex functions bend upwards. Even though we used the second derivative in our previous discussing, we will not define these concepts in terms of the second derivative. We do this, because we also want to be able to use this terminology for function that do not have second derivative. Instead, we will use the following definition.

::::::{prf:definition} 
:label: Def:Graphsderivatives:Concavity
A function $f$ is called **convex** on an interval if for any two points $a<b$ in the interval and for all $c$ in $(a,b)$ we have

$$
 f(c)\leq f(a)+\frac{f(b)-f(a)}{b-a}(c-a).
$$ 


A function $f$ is called **concave** on an interval if for any two points $a<b$ in the interval and for all $0\leq t\leq 1$ we have

$$
 f(c)\geq f(a)+\frac{f(b)-f(a)}{b-a}(c-a).
$$ 

::::::

Since the line segment between points $(a,f(a))$ and $(b,f(b))$ is the graph of the function $L(c)=\displaystyle f(a)+\frac{f(b)-f(a)}{b-a}(c-a)$ , $f$ is convex if the line segment between any two distinct points on the graph of $f$ lies above the graph of $f$.

Similarly, $f$ is concave on an interval precisely when for any two points $a<b$ in that interval the line segment between any two distinct points on the graph of $f$ lies below the graph of $f$.




:::{figure} Images/Fig-Graph1d-convexdef.png
---
width: 100%
name: Fig:Graphsderivatives:Convexdef
class: dark-light
---
An illustration of the definition of a convex function (left) and a concave function (right), with the line segment between any two points $a$ and $b$ lying above or below the function respectively.
:::

:::{todo}
Turn {numref}`Fig:Graphsderivatives:Convexdef` into an applet. Maybe nice if you can slide the points $(x(t),f(x(t)))$ and $(x(t),y(t))$.
:::


:::{note}
A function $f$ is convex on an interval precisely when $-f$ is concave on that interval. This follows since $f(c)\leq f(a)+\frac{f(b)-f(a)}{b-a}(c-a)$ precisely when $-f(c)\geq -f(a)+\frac{-f(b)-(-f(a))}{b-a}(c-a)$.
:::

Similarly to strictly increasing and strictly decreasing, we can also define strictly convex and strictly concave functions. 

::::::{prf:definition} 
:label: Def:Graphsderivatives:StrictConcavity
A function $f$ is called **strictly convex** on an interval if for any two points $a<b$ in the interval and for all $c$ in $(a,b)$ we have

$$
 f(c)< f(a)+\frac{f(b)-f(a)}{b-a}(c-a).
$$ 


A function $f$ is called **strictly concave** on an interval if for any two points $a<b$ in the interval and for all $c$ in $(a,b)$ we have

$$
 f(c)>f(a)+\frac{f(b)-f(a)}{b-a}(c-a).
$$ 

::::::

:::{note}
A function that is (strictly) convex on an interval, is sometimes called **(strictly) concave upwards** or **(strictly) convex downwards** on that interval. In addition, a function that (strictly) concave on an interval, is sometimes called **(strictly) concave downwards** or **(strictly) convex upwards** on that interval.
:::


Before we make a link between convex and concave functions and the second derivative, let us first make a connection with the first derivative.

::::::{prf:theorem} 
:label: Thm:Graphsderivatives:Concavitytangent
A differentiable function $f$ is convex on an interval precisely when $f$ lies above each of its tangent lines in that interval. That is, $f$ is convex precisely when for any two points $a$ and $b$ in the interval we have $f(b)\geq f(a)+f'(a)(b-a)$.

$f$ is concave on an interval precisely when $f$ lies below all tangent lines in that interval. That is, $f$ is concave precisely when for any two points $a$ and $b$ in the interval we have $f(b)\leq f(a)+f'(a)(b-a)$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Graphsderivatives:Concavitytangent`
:class: tudproof, dropdown
Let $I$ be an interval. 

Suppose first that $f$ is convex on $I$. Let $a<b$ in $I$. Then, since $f$ is convex, we have for any $ a<c<b$ that 

$$
 f(c)\leq f(a)+\frac{f(b)-f(a)}{b-a}(c-a).
$$

Then we can subtract $f(a)$ from both sides of the inequality to obtain

$$
 f(c)-f(a) \leq \frac{f(b)-f(a)}{b-a}(c-a) .
$$

Now we divide this inequality by the positive number $c-a$ to obtain

$$
 \frac{f(c)-f(a)}{c-a}\leq \frac{f(b)-f(a)}{b-a}.
$$

Using {prf:ref}`Thm:Differentiability:Derivativealt` we have

$$
 \lim_{c\rightarrow a}\frac{f(c)-f(a)}{c-a}=f'(a),
$$

so we obtain

$$
 f'(a)\leq \frac{f(b)-f(a)}{b-a}.
$$

Since $b-a>0$ we can multiply both parts of the inequality by $b-a$ to obtain

$$
 f'(a)(b-a)\leq f(b)-f(a),
$$

which gives

$$
 f(b)\geq f(a)+f'(a)(b-a),
$$

as desired. 

Now suppose that for all $x$ and $y$ in the interval we have $f(y)\geq f(x)+f'(x)(y-x)$. Let $a<b$ in $I$ and let $c$ in $(a,b)$. Then we want to show $f(a)+\frac{f(b)-f(a)}{b-a}(c-a)\geq f(c)$, i.e. $f(a)+\frac{f(b)-f(a)}{b-a}(c-a)-f(c)\geq 0$. Then we can write 

\begin{align*}
 f(c) &= 1\cdot f(c) \\
 &= \left(1-\frac{c-a}{b-a}+\frac{c-a}{b-a}\right)f(c) \\
 &= \left(1-\frac{c-a}{b-a}\right)f(c)+\frac{c-a}{b-a}f(c).
\end{align*}

With this, we have 

\begin{align*}
 f(a)+\frac{f(b)-f(a)}{b-a}(c-a)-f(c) &= f(a)+\frac{f(b)-f(a)}{b-a}(c-a) \\
 &\phantom{=} \quad\quad\quad-\left(1-\frac{c-a}{b-a}\right)f(c)-\frac{c-a}{b-a}f(c)\\
 &=f(a)\left(1-\frac{c-a}{b-a}\right)+f(b)\frac{c-a}{b-a} \\
 &\phantom{=} \quad\quad\quad -\left(1-\frac{c-a}{b-a}\right)f(c)-\frac{c-a}{b-a}f(c)\\
 &=\Big(f(a)-f(c)\Big)\left(1-\frac{c-a}{b-a}\right)+\Big(f(b)-f(c)\Big)\frac{c-a}{b-a}.
\end{align*}

Since $a$, $b$ and $c$ are all points in the interval $I$, and since $1-\dfrac{c-a}{b-a}>0$ and $\dfrac{c-a}{b-a} >0$ we can use our assumption to obtain the estimate

\begin{align*}
&\phantom{=} f(a)+\frac{f(b)-f(a)}{b-a}(c-a)-f(c) \\
&= \Big(f(a)-f(c)\Big)\left(1-\frac{c-a}{b-a}\right)+\Big(f(b)-f(c)\Big)\frac{c-a}{b-a} \\
&\geq f'(c)(a-c)\left(1-\frac{c-a}{b-a}\right)+f'(c)(b-c)\frac{c-a}{b-a}\\
&= f'(c)\left((a-c)+\frac{(c-a)^2}{b-a}+\frac{(b-c)(c-a)}{b-a}\right) \\
&= f'(c)\left(\frac{(a-c)(b-a)+(c-a)^2+(b-c)(c-a)}{b-a}\right) \\
&= f'(c)\cdot 0 \\
&= 0.
\end{align*}

Hence, we must have $f(a)+\frac{f(b)-f(a)}{b-a}(c-a)\geq f(c)$, which means that $f$ is convex.

The results about concavity follow by applying the first part to the function $-f$.
:::

:::{figure} Images/Fig-Graph1d-convextangent.png
---
width: 100%
name: Fig:Graphsderivatives:Convextangent
class: dark-light
---
An illustration of the classification of a convex function (left) and a concave function (right) from {prf:ref}`Thm:Graphsderivatives:Concavitytangent`.
:::

:::{todo}
Turn {numref}`Fig:Graphsderivatives:Convextangent` into an applet. 
:::

For many functions, both {prf:ref}`Def:Graphsderivatives:Concavity` and the classification from {prf:ref}`Thm:Graphsderivatives:Concavitytangent` are rather hard to check. Fortunately, for functions that are twice differentiable we have a criterion, similar to {prf:ref}`Thm:MinMax:Increasingdecreasing`, that is much easier to check.

::::::{prf:theorem} 
:label: Thm:Graphsderivatives:Concaveseconddiv
Let $f$ be a twice differentiable function.

- $f$ is convex on an interval precisely when $f''(x)\geq 0$ on that interval.
- $f$ is concave on an interval precisely when $f''(x)\leq 0$ on that interval.
- If $f''(x)> 0$ on an interval, then $f$ is strictly convex on that interval.
- If $f''(x)< 0$ on an interval, then $f$ is strictly concave on that interval.

::::::


:::{admonition} Proof of {prf:ref}`Thm:Graphsderivatives:Concaveseconddiv`
:class: tudproof, dropdown
Suppose first that $f''(x)\geq 0$ for all $x$ in an interval $I$. Let $a<b$ be two distinct points in $I$. Then by {prf:ref}`Thm:MinMax:MVT`, we can find $c$ in $(a,b)$ with 

$$
 f'(c)=\frac{f(b)-f(a)}{b-a}.
$$

Since $f''(x)\geq 0$ for all $x$, it follows from {prf:ref}`Thm:MinMax:Increasingdecreasing` that $f'$ is non-decreasing on $I$. Hence, we find that 

$$
 f'(a)\leq f'(c).
$$ 

Then we multiply both sides of this inequality by  $(b-a)$ (which is positive) and we add $f(a)$ to obtain

$$
 f(a)+f'(a)(b-a)\leq f(a)+f'(c)(b-a).
$$

Now the equation $f'(c)=\frac{f(b)-f(a)}{b-a}$ can be rewritten to $f(a)+f'(c)(b-a)=f(b)$, so we find that

$$
 f(a)+f'(a)(b-a)\leq f(b).
$$

Then we obtain that $f$ must be convex by {prf:ref}`Thm:Graphsderivatives:Concavitytangent`.

Now suppose that $f$ is convex on an interval $I$. We will show that $f''(x)\geq 0$ on $I$ by showing that $f'$ is non-decreasing on $I$ and then using {prf:ref}`Thm:MinMax:Increasingdecreasing`. Let $a<b$ be two distinct points in $I$. Consider any point $c$ in $(a,b)$. Then by the definition of convexity, we find that

$$
 f(c)\leq f(a)+\frac{f(b)-f(a)}{b-a}(c-a)=\frac{b-c}{b-a}f(a)+\frac{c-a}{b-a}f(b).
$$

Then we multiply this inequality by the positive term $b-a$, which gives

$$
 (b-a)f(c)\leq (b-c)f(a)+(c-a)f(b).
$$

Now we subtract $(b-a)f(a)$ from both sides of the inequality to obtain

\begin{align*}
 (b-a)f(c)-(b-a)f(a) &\leq (b-c)f(a)+(c-a)f(b)-(b-a)f(a) \\
 &= (a-c)f(a)+(c-a)f(b) \\
 &= (c-a)f(b)-(c-a)f(a).
\end{align*}

Then we divide both sides of the inequality by the positive term $(b-a)(c-a)$ to obtain

$$
 \frac{f(c)-f(a)}{c-a}\leq \frac{f(b)-f(a)}{b-a}.
$$

Taking the limit $c\rightarrow a^+$ gives

$$
 f'(a)=\lim_{c\rightarrow a^+}\frac{f(c)-f(a)}{c-a}\leq \frac{f(b)-f(a)}{b-a}.
$$

Now we return to a previous inequality: $(b-a)f(c)\leq (b-c)f(a)+(c-a)f(b)$. This time, we first bring a few terms to the other side of the equation, which gives

$$
 -(b-c)f(a)\leq (c-a)f(b)-(b-a)f(c).
$$

Then, we add $(b-c)f(b)$ to both sides of the equation to obtain

\begin{align*}
 (b-c)f(b)-(b-c)f(a) &\leq (c-a)f(b)-(b-a)f(c)+(b-c)f(b) \\
 &= (b-a)f(b)-(b-a)f(c).
\end{align*}

Then we divide both sides of the inequality by the positive term $(b-a)(b-c)$ to obtain

$$
 \frac{f(b)-f(a)}{b-a}\leq \frac{f(b)-f(c)}{b-c}.
$$

Taking the limit $c\rightarrow b^-$ gives

$$
 f'(b)=\lim_{c\rightarrow b^-}\frac{f(b)-f(c)}{b-c}\geq \frac{f(b)-f(a)}{b-a}.
$$

Combining these two inequalities gives

$$
 f'(a)\leq \frac{f(b)-f(a)}{b-a}\leq f'(b).
$$

This means that $f'$ is non-decreasing, so by {prf:ref}`Thm:MinMax:Increasingdecreasing` we must have $f''(x)\geq 0$ on $I$, as desired.

The other cases follow similarly.
:::

:::{warning}
A function $f$ can be strictly convex on an interval even if its second derivative is $0$ somewhere. For instance, consider the function $f(x)=x^4$. Then $f''(x)=12x^2$, which is $0$ at $x=0$. Still, this function is strictly convex on $\mathbb{R}$, which can be seen from the graph of the function.

::::{todo}
Include an applet with the graph of $f$.
:::
::::

As a consequence, we can also check for convexity by checking whether the derivative is non-decreasing or non-increasing. In fact, we already used this in the proof of {prf:ref}`Thm:Graphsderivatives:Concaveseconddiv`.

::::::{prf:theorem} 
:label: Thm:Graphsderivatives:Concaveincrdecr
Let $f$ be a twice differentiable function. 

- $f$ is convex on an interval precisely when $f'$ is non-decreasing on that interval.
- $f$ is concave on an interval precisely when $f'$ is non-increasing on that interval.
- If $f'$ is strictly increasing on an interval, then $f$ is strictly convex on that interval.
- If $f'$ is strictly decreasing on an interval, then $f$ is strictly concave on that interval.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Graphsderivatives:Concaveincrdecr`
:class: tudproof, dropdown

This follows directly from combining {prf:ref}`Thm:Graphsderivatives:Concaveseconddiv` and {prf:ref}`Thm:MinMax:Increasingdecreasing`.

:::

Before we move on to discussing an example, we need one more definition.

::::::{prf:definition} 
:label: Def:Graphsderivatives:Inflection
Let $x$ be in the domain of a function $f$. Then the point $(x,f(x))$ is called an **inflection point** if it is a point where the function changes from being convex to concave or vice versa.
::::::

For a twice differentiable function $f$, we see from {prf:ref}`Thm:Graphsderivatives:Concaveseconddiv` that an inflection point occurs if the second derivative changes from positive (meaning $f$ is convex) to negative (meaning $f$ is concave) or vice versa. If $f''$ is itself continuous, this can only happen if the second derivative is $0$ at this point. Hence, we obtain the following result.

::::::{prf:theorem} 
:label: Thm:Graphsderivatives:Inflection
Let $f$ be a twice differentiable function. If $f$ has an inflection point at $x$ and $f''$ is continuous at $x$, then $f''(x)=0$.

::::::

:::{warning}
{prf:ref}`Thm:Graphsderivatives:Inflection` does not work the other way around. For instance, if we consider $f(x)=x^4$, then we have $f''(0)=0$. However, $0$ is not an inflection point of $f$, since $f''(x)=12x^2>0$ for all $x\neq 0$. So the function does not change from convex to concave or vice versa at $0$, since it is convex on both the intervals $(-\infty,0)$ and $(0,\infty)$.
:::

To conclude, let us see how we determine the convexity of a function in practice. 

::::::{prf:example} 
:label: Ex:Graphsderivatives:Convex
Consider the function $f(x)=x^4+2x^3-36x^2+3x+4$. We want to know on which intervals the function is convex or concave and where the inflection points are. For this, we evaluate its second derivative. We obtain

$$
 f'(x)=4x^3+6x^2-72x+3
$$

and

$$
 f''(x)=12x^2+12x-72.
$$

In order to find out where $f''$ is positive or negative, we first look where it is $0$. Solving $12x^2+12x-72=0$ gives $x=-3$ and $x=2$. Since the graph of $f''$ is a parabola opening upwards, we find that $f''(x)>0$ for $x<-3$ and for $x>2$, while $f''(x)<0$ for $-3<x<2$. By {prf:ref}`Thm:Graphsderivatives:Concaveseconddiv`, the function $f$ is strictly convex on the intervals $(-\infty,-3)$ and $(2,\infty)$, while it is strictly concave on the interval $(-3,2)$. At $x=-3$ the function changes from convex to concave, while at $x=2$ it changes from concave back to convex. So both points are inflection points.

:::{figure} Images/Fig-Graphsderivatives-Convex.png
:name: Fig:Graphsderivatives:Convex

The graph of the function $f(x)=x^4+2x^3-36x^2+3x+4$, and the first and second derivatives of this function.
:::

:::{todo}
Replace {numref}`Fig:Graphsderivatives:Convex` with an applet.
:::

::::::
