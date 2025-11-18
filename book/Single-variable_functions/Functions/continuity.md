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

Since the definition of the continuity involves limits, we can use the precise definition of a limit {prf:ref}`Def:LimitAtPoint:Precisedef` to rephrase the condition for continuity as follows.

::::::{prf:theorem} 
:label: Theorem:Continuity:EpsilonDelta

Let $f$ be a function and $a$ a point in the domain of $f$. Then $f$ is continuous at $a$ if, and only if, for every $\varepsilon>0$ there exists a $\delta>0$ such that for every $x$ in the domain of $f$ with $0<|x-a|<\delta$ we have $|f(x)-f(a)|<\varepsilon$.
::::::

::::::{admonition} 
:class: tudproof, dropdown
This follows directly from rephrasing the statement $\lim\limits_{x\rightarrow a}f(x)=f(a)$ using the precise definition of a limit {prf:ref}`Def:LimitAtPoint:Precisedef`.
::::::

The statement in {prf:ref}`Theorem:Continuity:EpsilonDelta` is sometimes used as the definition of continuity, especially in a more theoretical setting. The advantage of doing so, is that this statement generalises more easily to more abstractly defined functions. The disadvantage, however, is that for the functions we tend to encounter the most in practice, it is much harder to work with. As such, we will stick to the definition involving limits.

In this section we cover

- Definition (limit definition), standard continuous functions and basic rules of calculation (including left- and right-continuity)
- "Taking a limit inside a continuous function"
- Intermediate value theorem