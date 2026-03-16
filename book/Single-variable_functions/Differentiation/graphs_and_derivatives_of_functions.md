(Section:GraphsDerivatives)=

# Graphs and derivatives of functions

## Introduction

Now that we know the derivatives of most standard functions, we have not really touched upon what should be the most important question: what can we actually do with derivatives? We have seen that we can use them to find tangent lines, but that is about it. For higher order derivatives we have not even seen *any* uses (yet). However, there is much more that derivatives can tell us. In fact, most qualitative behaviour of a function is captured in its derivatives. For instance, we will see that we can use the first derivative to determine whether a function is increasing or decreasing at a point.

In this section, we will specifically see what the first and second derivatives say about the graph of a function. The ideas presented here can be generalized to give interpretations of higher order derivatives, but these are typically less useful in practice. In order to prove most of these results, we will need a very important theorem, called the **mean value theorem**, so let us start there.

## Mean value theorem

Suppose you are running a marathon and you let $f(t)$ describe the distance you travelled at time $t$. Then $f'(t)$ represents your velocity at time $t$. Say it takes you four and a half hours to finish the marathon. Then you average running speed is around $2.6$ meters per second. Likely, you are not running equally fast at each point of time, so for most values of $t$, $f'(t)$ will be unequal to $2.6$. The idea of the mean value theorem is that there must be at least one point in time (but possibly more) where your velocity is exactly equal to the average velocity. Intuitively this makes sense. If you were to run slower than $2.6$ meters per second at all points in time, or faster than $2.6$ meters per second at all points in time, your average velocity can never be $2.6$. So there must be points in time where you run slower than your average speed and points in time where you run faster than your average speed. Since your speed does not make sudden jumps (that is, your speed is continuous), it has to attain this average speed at some point in time.

With this idea in mind, let us formulate and prove the mean value theorem, which is also known as **Lagrange's mean value theorem**, named after the Italian mathematician and physicist [Joseph-Louis Lagrange (1736-1813)](https://en.wikipedia.org/wiki/Joseph-Louis_Lagrange).

::::::{prf:theorem} The mean value theorem
:label: Thm:Graphsderivatives:MVT
Let $f$ be a function that is continuous on a closed interval $[a,b]$ and differentiable on the open interval $(a,b)$. Then there exists a point $c$ in $(a,b)$ with

$$
 f'(c)=\frac{f(b)-f(a)}{b-a}.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Graphsderivatives:MVT`
:class: tudproof, dropdown

:::

The interpretation of this theorem works as follows: $\dfrac{f(b)-f(a)}{b-a}$ represents the **average slope** of the function on the interval $[a,b]$.

In this section we cover:

- Relationship between graphs and derivatives
- Increasing and decreasing functions (hier een stukje {prf:ref}`Thm:PropertiesFunctions:HyperbolicProperties` bewijzen en terugverwijzen)
- Convexity and inflection points
- Mean value theorem