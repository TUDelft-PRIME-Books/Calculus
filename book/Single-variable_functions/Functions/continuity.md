(Section:Continuity)=

# Continuity

Almost all functions we have encountered so far have the nice property that it is possible to sketch their graph without lifting your pen, except possibly for skipping over a vertical asymptote. Indeed, all of polynomials, powers of $x$, rational functions, (inverse) trigonometric functions, exponential functions and logarithms have this property. A function with this property is called **continuous**. Stated differently, a function is continuous whenever small changes in the input give rise to small changes in the function values. 

In science and engineering, most variables depend on each other in a continuous way. However, that does not need to be the case. Consider, for instance, a simple electrical circuit, where a DC voltage source is connected to a resistor. Initially, the voltage source is turned off, but at $t=0$, we turn on the voltage source. Instantly, the currenct through the resistor will jump from $0$ to a non-zero value, so a small change in time will give rise to a large change in current. As such, the current is not continuous at the moment in time the voltage source is turned on (it is continuous at other points in time).


Hier plaatje van het circuit beschreven in de tekst hierboven. Voor mijn vak bij EE heeft een TA ooit mooie plaatjes gemaakt, maar ik weet niet hoe. Ik heb wel voorbeelden van hoe dat er typisch uitziet. Ook een grafiek van de stroom, wat dus een Heaviside functie is. Omdat we geen getallen gegeven hebben wil je misschien geen maatvoering op de assen?

(Subsec:ContProp)=

## Definition and properties

Continuity of a function can conveniently be expressed in terms of limits.

::::::{prf:definition} Continuity
:label: Def:Continuity:ContinuityLimit

Let $f$ be a function and $a$ a point in the domain of $f$. Then we say that $f$ is **continuous** at $a$ whenever $\lim\limits_{x\rightarrow a}f(x)=f(a)$. If $f$ is not continuous at $a$, we say that it is **discontinuous** at $a$.

If a function $f$ is continuous at each points in each point in its domain, we say that $f$ is **continuous**. 
::::::

You might be tempted to think that this definition means that a function $f$ is continuous at a point $a$, whenever $\lim\limits_{x\rightarrow a}f(x)$ exists. However, this is not the case. In the definition, it stated explicitly that this limit should not only exist, but it should also be equal to the function value $f(a)$. For instance, for the function $f$ defined in {prf:ref}`Ex:LimitAtPoint:LimitLeftRightComposite`, the limit $\lim\limits_{x\rightarrow 2}f(x)$ exists, but it is unequal to $f(2)$. Hence this function $f$ is not continuous at the point $2$.

Since the definition of the continuity involves limits, we can use the precise definition of a limit ({prf:ref}`Def:LimitAtPoint:Precisedef`) to rephrase the condition for continuity as follows.

::::::{prf:theorem} 
:label: Theorem:Continuity:EpsilonDelta

Let $f$ be a function and $a$ a point in the domain of $f$. Then $f$ is continuous at $a$ if, and only if, for every $\varepsilon>0$ there exists a $\delta>0$ such that for every $x$ in the domain of $f$ with $0<|x-a|<\delta$ we have $|f(x)-f(a)|<\varepsilon$.
::::::

:::{admonition} Proof
:class: tudproof, dropdown
This follows directly from rephrasing the statement $\lim\limits_{x\rightarrow a}f(x)=f(a)$ using the precise definition of a limit ({prf:ref}`Def:LimitAtPoint:Precisedef`).
:::

::::::{prf:example} 
:label: Theorem:Continuity:Firstexample

Consider the function $f(x)=x^2$. In {prf:ref}`Ex:LimitAtPoint:Formaldefexists` we showed that $\lim\limits_{x\rightarrow 2}x^2=4$. Since $f(2)=2^2=4$, this means that $\lim\limits_{x\rightarrow 2}x^2=f(2)$. So this function is continuous at $2$. In fact, it is continuous everywhere, as we will show later.
::::::

Before being able to show that many standard functions are continuous, it pays off to first show that we can combine continuous functions in several ways to obtain new continuous functions. Since we already know several computation rules for limits, and continuity is defined in terms of limits, we can directly lift these results to obtain computation rules for continuity.

::::::{prf:theorem} Basic rules of calculation for continuity
:label: Theorem:Continuity:Basiccomputationrules
Consider two functions $f$ and $g$ and let $a$ be a point that is both in the domain of $f$ and in the domain of $g$. Also let $c$ be a real number. Suppose that both $f$ and $g$ are continuous at $a$. Then the following functions are also continuous at $a$.

- $cf$
- $f+g$
- $fg$
- $\frac{f}{g}$, provided $g(a)\neq 0$.

::::::

:::{admonition} Proof
:class: tudproof, dropdown
These statements follow directly from {prf:ref}`Theorem:LimitAtPoint:Basiccomputationrules`.
:::

In addition to the rules above, the composition of two continuous functions is again continuous, as can be seen from the following results.

::::::{prf:theorem} Composition of continuous functions
:label: Theorem:Continuity:Composition
Consider two functions $f$ and $g$ and let $a$ be a point in the domain of $g$ for which $g(a)$ is in the domain of $f$. Suppose that $g$ is continuous at $a$ and $f$ is continuous at $g(a)$. Then the composite function $f\circ g$ is continuous at $a$.

::::::

:::{admonition} Proof
:class: tudproof, dropdown
We use the classification of continuity given in {prf:ref}`Theorem:Continuity:EpsilonDelta`. Let $\varepsilon>0$ be given. Since $f$ is continuous at $g(a)$, we can pick $\delta_1>0$ in such a way that for each $x$ in the domain of $f$ with $0<|x-g(a)|<\delta_1$ we have $|f(x)-f(g(a))|<\varepsilon$. Since $g$ is continuous at $a$ and $\delta_1>0$, we can find $\delta_2>0$ in such a way that for each $x$ in the domain of $g$ with $0<|x-a|<\delta_2$ we have $|g(x)-g(a)|<\delta_1$ (so $\delta_1$ takes the role here that $\varepsilon$ usually takes). Consider any $x$ in the domain of $f\circ g$ with $0<|x-a|<\delta_2$. Then $x$ is also in the domain of $g$ and it satisfies $0<|x-a|<\delta_2$, so we must have $|g(x)-g(a)|<\delta_1$. As such, $g(x)$ is an element of the domain of $f$ with $0<|g(x)-g(a)|<\delta_1$, which means that we must have $|f(g(x))-f(g(a))|<\varepsilon$. This precisely means that $f\circ g$ is continuous at $a$.
:::

::::::{warning} 
:name: Warning:Continuity:Oppositecomposition

The reverse of the statment in {prf:ref}`Theorem:Continuity:Composition` is not true. That is, there are functions $f$ and $g$ for which there is a point $a$, such that either $f$ is discontinuous at $g(a)$ or $g$ is discontinuous at $a$ (or both), but $f\circ g$ is continuous at $a$. For instance, if $f=0$, then $f\circ g=0$ as well (independently of what $g$ is), which is a continuous function even if $g$ is not continuous function everywhere.
::::::

As a final preparation before showing the continuity of standard functions, we can show that inverse functions (if they exist) of continuous functions are continuous. Intuitively, this result makes sense: the graph of the inverse function is obtained by reflecting the graph of the original function in the line $y=x$, so if the first one does not contain any jumps, the second one will not contain any jumps as well.

::::::{prf:theorem} Continuity of inverse functions
:label: Theorem:Continuity:Inverse
Let $f$ be one-to-one function that is continuous at a point $a$. Then the inverse function $f^{-1}$ is continuous at $f(a)$. In particular, if $f$ is continuous everywhere, then $f^{-1}$ is continuous everywhere as well.

::::::


:::{admonition} Proof
:class: tudproof, dropdown
We use the classification of continuity given in {prf:ref}`Theorem:Continuity:EpsilonDelta`. Let $\varepsilon>0$ be given. NOG NIET AF
:::


Nog te doen: inverse functie bewijs, standaard functies, links en rechts.

In this section we cover

- Definition (limit definition), standard continuous functions and basic rules of calculation (including left- and right-continuity)
- "Taking a limit inside a continuous function"
- Intermediate value theorem