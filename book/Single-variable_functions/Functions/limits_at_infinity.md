(Section:Limitinf)=

# Limits at infinity

## Introduction 

Many problems in nature and engineering feature quantities that, for relatively short periods of time, fluctuate or change rapidly, before stabilizing and moving towards a certain equilibrium. In such cases, we are often mainly interested in what happens in the long term.

:::::{margin}
::::{figure} Images/Fig-LimitAtInfinity-RefrigeratorCauliflower.png
:name: Fig:LimitAtInfinity:RefrigeratorCauliflower

A cauliflower in a refrigerator.
::::
:::::

Suppose, for instance, that we buy a cauliflower at the supermarket, which has a temperature of $20$ °C. We place it into a refrigerator, which has a temperature of $5$ °C and we want to know how the temperature $T$ (in degrees Celsius) of the cauliflower changes as a function of time $t$ (in minutes). Using Newton's law of cooling (see {numref}`SubSec:ODE1:SeparableAppl`), it can be shown that $T(t)=T_{\text{env}}+(T(0)-T_{\text{env}})e^{-rt}$. Here, $T_{\text{env}}=5$ °C is the temperature of the refrigerator and $r>0$ is a constant representing the rate of the heat transfer between the object and the environment.

Let us take, for example, $r=1\ \text{min}^{-1}$ here. Note that $T(0)=20$ °C, since the object starts at this temperature when we place it into the refrigerator. In particular, we can write $T(t)=5+15e^{-t}$ °C. What happens after a very long time? Intuitively, we know the answer: the temperature of the cauliflower will be very close to the temperature of the refrigerator, which is $5$ °C. Indeed, we can also observe this when we plot the temperature as a function of time.

::::{figure} Images/Fig-LimitAtInfinity-TempCauliflower.png
:name: Fig:LimitAtInfinity:TempCauliflower
:class: dark-light

The temperature $T(t)$ in degrees Celsius of the cauliflower within the refrigerator as a function of time $t$.

::::

:::{todo}
Turn {numref}`Fig:LimitAtInfinity:TempCauliflower` into an applet. Graph should only be for $t\geq 0$.
:::

We observe that our intuition was correct: the temperature of the object will first decrease rapidly before slowly moving towards the limiting value of $5$ °C. Notice that the temperature never becomes precisely equal to $5$ °C; it will always remain slightly above this value. We say that the function $T(t)$ has a **horizontal asymptote** at $T=5$ °C and we denote this by $\lim\limits_{t\rightarrow\infty}T(t)=5$ °C. As was stated in {numref}`Section:LimitPoint`, the word asymptote comes from the Greek ἀσύμπτωτος  (asumptotos), which means "not falling together". The notation $\lim\limits_{t\rightarrow\infty}T(t)=5$ °C can be pronounced as "the function values $T(t)$ approach the value $5$ °C as $t$ approaches infinity". The precise definition of such a limit at infinity is rather technical, so we postpone it to {numref}`Subsec:LimitinfPrecise`. Instead, we will use the following more intuitive definition.

(Subsec:LimitinfIntuitive)=
## Intuitive definition of limits at infinity

::::::{prf:definition} Intuitive definition of a limit at plus or minus infinity
:label: Def:LimitAtInfinity:Intuitivelimit

Let $f$ be a function that is defined on some interval $[d,\infty)$. We say that the **limit at infinity** of $f$ is equal to $L$, and we write $\lim\limits_{x\rightarrow \infty}f(x)=L$, if the function values $f(x)$ approach $L$ as $x$ grows arbitrarily large. If no such real number $L$ exists, we say that the limit of the function $f$ at infinity does not exist.

Similarly, if $f$ is defined on some interval $(-\infty,d]$, we say that the **limit at minus infinity** of $f$ is equal to $L$, and we write $\lim\limits_{x\rightarrow -\infty}f(x)=L$, if the function values $f(x)$ approach $L$ as $x$ grows arbitrarily large negative. If no such real number $L$ exists, we say that the limit of the function $f$ at minus infinity does not exist.

If either $\lim\limits_{x\rightarrow \infty}f(x)=L$ or $\lim\limits_{x\rightarrow -\infty}f(x)=L$, we say that the function $f$ has a **horizontal asymptote** at $y=L$.
::::::

::::::{prf:notation} Shorthand notations for limits
:label: Notation:LimitAtInfinity:Shorthand

Instead of writing $\lim\limits_{x\rightarrow \infty}f(x)=L$, we sometimes use the short hand notations

$$
 f(x)\rightarrow L\ \text{as}\ x\rightarrow \infty
$$

or

$$
 f(x)\xrightarrow{x\rightarrow \infty}L.
$$

We use a similar notation for limits at minus infinity.
::::::


Since we only work with an intuitive definition, we will also postpone all proofs in this section to {numref}`Subsec:LimitinfPrecise`.




::::::{prf:example} 
:label: Ex:LimitAtInfinity:Firstexample

Consider the function $f(x)=\dfrac{4+\frac{1}{x}}{2-\frac{3}{x^2}}$ and suppose we want to evaluate $\lim\limits_{x\rightarrow \infty}f(x)$. First, we make a table of the function values for increasing values of $x$.

```{list-table} Function values of $f$ for increasing values of $x$.
:header-rows: 1
:align: center
:class: mid-align
:name: Tab:LimitAtInfinity:FirstLimitExValues

* - $x$
  - $f(x)$
* - $1$
  - $-5$
* - $10$
  - $2.0812182741\ldots$
* - $100$
  - $2.0053007951\ldots$
* - $1000$
  - $2.0005030007\ldots$
* - $10000$
  - $2.0000500300\ldots$
* - $100000$
  - $2.0000050003\ldots$
* - $1000000$
  - $2.0000005000\ldots$

```

Notice that the function values seem to go towards the value $2$. This would suggest that $\lim\limits_{x\rightarrow \infty}f(x)=2$. Let us see if we can find out where this value comes from. If $x$ is very large, notice that $\frac{1}{x}$ and $-\frac{3}{x^2}$ are very close to $0$, since we are dividing a relatively small number by a much larger number. As such, for large values of $x$ we have

$$
 f(x)=\dfrac{4+\frac{1}{x}}{2-\frac{3}{x^2}}\approx \dfrac{4+0}{2-0}=\dfrac{4}{2}=2.
$$

Later in this section, we will show that this reasoning is indeed mathematically valid. As such, the function $f$ has a horizontal asymptote at $y=2$. We can also see in the graph of $f$ that the function values tend towards the value $2$ as $x$ gets large.

::::{figure} Images/Fig-LimitAtInfinity-Firstexample.png
:name: Fig:LimitAtInfinity:Firstexample
:class: dark-light

An illustration of the function $f(x)=\dfrac{4+\frac{1}{x}}{2-\frac{3}{x^2}}$ for large values of $x$.
::::

:::{todo}
Turn {numref}`Fig:LimitAtInfinity:Firstexample` into an applet.
:::


::::::

::::::{prf:example} 
:label: Ex:LimitAtInfinity:Secondexample

Consider the function $f(x)=\dfrac{\sin(x)}{x^2}$ and suppose we want to evaluate $\lim\limits_{x\rightarrow -\infty}f(x)$. First, we make a table of the function values for increasingly negative values of $x$.

```{list-table} Function values of $f$ for decreasing values of $x$.
:header-rows: 1
:align: center
:class: mid-align
:name: Tab:LimitAtInfinity:SecondLimitExValues

* - $x$
  - $f(x)$
* - $-1$
  - $-0.841470984\ldots$
* - $-10$
  - $\phantom{+}0.005440211\ldots$
* - $-100$
  - $\phantom{+}5.063656411\ldots\times10^{-5}$
* - $-1000$
  - $-8.268795405\ldots\times10^{-7}$
* - $-10000$
  - $\phantom{+}3.056143888\ldots\times10^{-9}$
* - $-100000$
  - $-3.574879797\ldots\times10^{-12}$
* - $-1000000$
  - $\phantom{+}3.499935021\ldots\times10^{-13}$

```

Notice that the function values seem to go towards the value $0$. This would suggest that $\lim\limits_{x\rightarrow -\infty}f(x)=0$. Indeed, we notice that $\sin(x)$ is always between $-1$ and $1$, even if $x$ is very negative. This means that $\dfrac{\sin(x)}{x^2}$ is a number, where something between $-1$ and $1$ is divided by something very large. As such, $\dfrac{\sin(x)}{x^2}$ is very close to $0$. In {prf:ref}`Ex:LimitAtInfinity:SqueezeThm` we will show that this reasoning is indeed valid.

::::{figure} Images/Fig-LimitAtInfinity-Secondexample.png
:name: Fig:LimitAtInfinity:Secondexample
:class: dark-light

An illustration of the function $f(x)=\dfrac{\sin(x)}{x^2}$ for large negative values of $x$.
::::

:::{todo}
Turn {numref}`Fig:LimitAtInfinity:Secondexample` into an applet. 
:::

Notice that the function $f$ actually oscillates around the horizontal asymptote $x=0$. This is not a problem, as the function values indeed tends towards $0$. However, this does mean that the original Greek meaning of the word asymptote ("not falling together") does not exactly match the modern use.
::::::

::::::{prf:example} 
:label: Ex:LimitAtInfinity:Firstexamplenonexist

Consider the function $f(x)=x^2$ and suppose we want to evaluate $\lim\limits_{x\rightarrow \infty}f(x)$. First, we make a table of the function values for increasing values of $x$.

```{list-table} Function values of $f$ for increasing values of $x$.
:header-rows: 1
:align: center
:class: mid-align
:name: Tab:LimitAtInfinity:FirstNonExistLimitExValues

* - $x$
  - $f(x)$
* - $1$
  - $1$
* - $10$
  - $100$
* - $100$
  - $10000$
* - $1000$
  - $1000000$
* - $10000$
  - $100000000$
* - $100000$
  - $10000000000$
* - $1000000$
  - $1000000000000$

```

Notice that the function values seem to blow up and that they do not tend towards a certain number. Indeed, as $x$ tends towards infinity, $x^2$ will do so as well. As such, the limit $\lim\limits_{x\rightarrow \infty}x^2$ does not exist. 
::::::

In {prf:ref}`Ex:LimitAtInfinity:Firstexamplenonexist` the limit of the function at infinity did not exist, because the function values blew up as $x$ grew. This is actually a very common situation, so it deserves its own notation.

::::::{prf:definition} Intuitive definition of an infinite limit at infinity
:label: Def:LimitAtInfinity:Inflimitint
Let $f$ be a function defined for values of $x>d$ for some $d$. Then we say that $f$ has an **infinite limit at infinity**, and we write $\lim\limits_{x\rightarrow \infty}f(x)=\infty$ whenever the function values $f(x)$ grow arbitrarily large as $x$ grows arbitrarily large.

Similarly, we say that $f$, defined for values of $x<d$ for some $d$, has a **negative infinite limit at infinity**, and we write $\lim\limits_{x\rightarrow \infty}f(x)=-\infty$ whenever the function values $f(x)$ grow arbitrarily large negative as $x$ grows arbitrarily large.

Finally, we have the corresponding notations $\lim\limits_{x\rightarrow -\infty}f(x)=\infty$ and $\lim\limits_{x\rightarrow -\infty}f(x)=-\infty$ for a positive or negative **infinite limit at minus infinity**.
::::::

::::::{warning} 
:name: Warning:LimitAtInfinity:Infinitelimit

A notation like $\lim\limits_{x\rightarrow \infty}f(x)=\infty$ or $\lim\limits_{x\rightarrow \infty}f(x)=-\infty$ does not mean that $\infty$ and $-\infty$ are numbers, nor do they mean that these limits exist. A correct way to pronounce the notation $\lim\limits_{x\rightarrow \infty}f(x)=\infty$ is **the limit of $f$ at infinity does not exist, because the function values grow without bound**.
::::::

Notice that a function can have either $0$, $1$ or $2$ horizontal asymptotes, depending on whether $\lim\limits_{x\rightarrow \infty}f(x)$ and $\lim\limits_{x\rightarrow -\infty}f(x)$ exist. Even if both limits exist, the function might still have only $1$ horizontal asymptote whenever $\lim\limits_{x\rightarrow \infty}f(x)=\lim\limits_{x\rightarrow -\infty}f(x)$.

Previously, we saw that a limit at infinity might not exist, because there the function has an infinite or negative limit there. There are other reasons why a limit might not exist, and we will show a few commonly occurring cases.

::::::{prf:example} 
:label: Ex:LimitAtInfinity:Secondexamplenonexist

Consider the function $f(x)=\cos(x)$ and suppose we want to evaluate $\lim\limits_{x\rightarrow \infty}f(x)$. First, we make a table of the function values for increasing values of $x$.

```{list-table} Function values of $f$ for increasing values of $x$.
:header-rows: 1
:align: center
:class: mid-align
:name: Tab:LimitAtInfinity:SecondNonExistLimitExValues

* - $x$
  - $f(x)$
* - $1$
  - $\phantom{+}0.5403023058681398$
* - $10$
  - $-0.8390715290764524$
* - $100$
  - $\phantom{+}0.8623188722876839$
* - $1000$
  - $\phantom{+}0.5623790762907029$
* - $10000$
  - $-0.9521553682590148$
* - $100000$
  - $-0.9993608074382124$
* - $1000000$
  - $\phantom{+}0.9367521275331447$

```

Notice that the function values do not seem to tend to some particular value. This is because the cosine keeps on oscillating between $-1$ and $1$, even if $x$ grows large. As such, the limit $\lim\limits_{x\rightarrow \infty}\cos(x)$ does not exist.
::::::

::::::{prf:example} 
:label: Ex:LimitAtInfinity:Thirdexamplenonexist

Consider the function $f(x)=\sqrt{x}$ and suppose we want to evaluate $\lim\limits_{x\rightarrow -\infty}f(x)$. When we try to make a table of the function values for negative values of $x$, we immediately run into trouble as the function is not defined for negative values of $x$. As such, the limit $\lim\limits_{x\rightarrow -\infty}\sqrt{x}$ does not exist.
::::::

::::::{warning} 
:name: Warning:LimitAtInfinity:Tables
Even though making tables like we did in the preceding examples can help to give an idea what the value of the limit at infinity is going to be, it is not sufficient to only make a table when evaluating a limit (see {prf:ref}`Ex:LimitAtInfinity:Warningtables`).
::::::

::::::{prf:example} 
:label: Ex:LimitAtInfinity:Warningtables

Consider the function $f(x)=\cos(\pi x)$ and suppose we make a table like we did in the previous examples.

```{list-table} Function values of $f$ for increasing values of $x$.
:header-rows: 1
:align: center
:class: mid-align
:name: Tab:LimitAtInfinity:WarningTables

* - $x$
  - $f(x)$
* - $1$
  - $-1$
* - $10$
  - $1$
* - $100$
  - $1$
* - $1000$
  - $1$
* - $10000$
  - $1$
* - $100000$
  - $1$
* - $1000000$
  - $1$

```

This would suggest that $\lim\limits_{x\rightarrow\infty}\cos(\pi x)=1$. However, we know that the function values do not tend to $1$, as they keep on oscillating between $-1$ and $1$. In this case, we simply chose the values of $x$ we inserted into our function rather poorly. Indeed, $f(x)=1$ for all even integer values of $x$. If we, on the other hand, had chosen values of $x$ of the form $x=n$ for an odd integer $n$, we might have got the idea that the limit would be $-1$. Indeed, the limit  $\lim\limits_{x\rightarrow\infty}\cos(\pi x)$ does not exist at all.
::::::


(Subsec:LimitinfEvaluating)=

## Evaluating limits

In order to evaluate limits at infinity, we need two important building blocks: standard limits and calculation rules. Combining these will allow us to evaluate most limits that you will encounter in practice. In particular, combining these two results, shows that we evaluated the limit in {prf:ref}`Ex:LimitAtInfinity:Firstexample` correctly. As can be expected, many results are very similar to those in {numref}`Subsec:Limitsrules`, so we follow a very similar structure.

::::::{prf:theorem} Standard limits
:label: Theorem:LimitAtInfinity:Standardlimits
We have the following standard limits.

:::::{grid} 2
:gutter: 1

::::{grid-item}
- $\lim\limits_{x\rightarrow\infty}1=1$;
- $\lim\limits_{x\rightarrow-\infty}1=1$;
- $\lim\limits_{x\rightarrow\infty}x^r=0$ when $r<0$;
- $\lim\limits_{x\rightarrow\infty}x^r=\infty$ when $r>0$;
- $\lim\limits_{x\rightarrow-\infty}x^{-r}=0$ when $r$ is a positive integer;

::::

::::{grid-item}
- $\lim\limits_{x\rightarrow\infty}e^{-ax}=0$ when $a>0$;
- $\lim\limits_{x\rightarrow\infty}e^{ax}=\infty$ when $a>0$;
- $\lim\limits_{x\rightarrow\infty}\frac{1}{\ln(x)}=0$;
- $\lim\limits_{x\rightarrow\infty}\ln(x)=\infty$;
- $\lim\limits_{x\rightarrow\infty}\arctan(x)=\dfrac{\pi}{2}$;
- $\lim\limits_{x\rightarrow-\infty}\arctan(x)=-\dfrac{\pi}{2}$.
::::

:::::

::::::

::::::{prf:theorem} Basic rules of calculation for limits at infinity
:label: Theorem:LimitAtInfinity:Basiccomputationrules
Suppose that $\lim\limits_{x\rightarrow \infty}f(x)=L$ and $\lim\limits_{x\rightarrow \infty}g(x)=M$. Also let $c$ be a real number. Then we have

- $\lim\limits_{x\rightarrow \infty}cf(x)=cL$ (scalar multiple rule).
- $\lim\limits_{x\rightarrow \infty}(f(x)+g(x)) = L+M$ (sum rule).
- $\lim\limits_{x\rightarrow \infty}f(x)g(x)=LM$ (product rule).
- $\lim\limits_{x\rightarrow \infty}\dfrac{f(x)}{g(x)}=\dfrac{L}{M}$ if $M\neq 0$ (quotient rule).

The equivalent rules hold for limits at minus infinity.

::::::

::::::{prf:remark}
:label: Remark:LimitAtInfinity:Productquotientrule
The product and quotient rules from {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules` should not be confused with the product and quotient rules for differentiation, which will be covered in {numref}`Section:DiffProdQuot`.

::::::

Intuitively, these computation rules make sense: if the function values $f(x)$ approach $L$ and the function values $g(x)$ approach $M$, both as $x$ gets very large, then $f(x)+g(x)$ will approach $L+M$. Still, showing that these rules hold using the formal definition of a limit at infinity can be tricky, see {numref}`Subsec:LimitinfPrecise`.



::::::{prf:theorem} Substitution
:label: Theorem:LimitAtInfinity:Substitution
Suppose $f$ is a polynomial, rational function, power function, (inverse) trigonometric function, exponential function or logarithmic function and that $b$ is in the domain of $f$. Moreover, suppose that $\lim\limits_{x\rightarrow \infty}g(x)=b$. Then $\lim\limits_{x\rightarrow \infty}f(g(x))=f\left(\lim\limits_{x\rightarrow \infty}g(x)\right)=f(b)$.

In addition, suppose  $h$ is any function for which the composition $f\circ h$. If $\lim\limits_{x\rightarrow\infty}h(x)=\infty$, then we also have the limit $\lim\limits_{x\rightarrow \infty}f(h(x))=\lim\limits_{x\rightarrow\infty}f(x)$. Similarly, if $\lim\limits_{x\rightarrow\infty}h(x)=-\infty$, then we have $\lim\limits_{x\rightarrow \infty}f(h(x))=\lim\limits_{x\rightarrow-\infty}f(x)$.

A similar result holds for limits at minus infinity.
::::::

The result above shows that limits can be "taken inside" a nice enough function. In fact, {prf:ref}`Theorem:Continuity:SubstitutionInf` is a slightly more general version of this result. In this part of {numref}`Section:Continuity`, we will also prove {prf:ref}`Theorem:LimitAtInfinity:Substitution`.

For compositions $f\circ g$ with $\lim\limits_{x\rightarrow\infty}g(x)=\infty$ or $\lim\limits_{x\rightarrow\infty}g(x)=-\infty$ we do not even need any conditions on $f$. 

::::::{prf:theorem} Substitution of infinite limits
:label: Theorem:LimitAtInfinity:Substitution2
Let $f$ and $g$ be any two functions for which the composition $f\circ g$ exists. If $\lim\limits_{x\rightarrow\infty}g(x)=\infty$ and $\lim\limits_{x\rightarrow\infty}f(x)$ exists, then we have the limit $\lim\limits_{x\rightarrow \infty}f(g(x))=\lim\limits_{x\rightarrow\infty}f(x)$. Similarly, if $\lim\limits_{x\rightarrow\infty}g(x)=-\infty$ and $\lim\limits_{x\rightarrow-\infty}f(x)$ exists, then we have $\lim\limits_{x\rightarrow \infty}f(g(x))=\lim\limits_{x\rightarrow-\infty}f(x)$.

In addition, if $\lim\limits_{x\rightarrow\infty}g(x)=\infty$ and $\lim\limits_{x\rightarrow\infty}f(x)=\infty$, then we also have $\lim\limits_{x\rightarrow \infty}f(g(x))=\infty$. Similarly, if $\lim\limits_{x\rightarrow\infty}g(x)=-\infty$ and $\lim\limits_{x\rightarrow-\infty}f(x)=\infty$, then we have $\lim\limits_{x\rightarrow \infty}f(g(x))=\lim\limits_{x\rightarrow-\infty}f(x)=-\infty$.

A similar result holds for limits of $f$ at minus infinity, or when the limit of $f$ is $-\infty$.
::::::

Basically, this result states that there is no difference between $\lim\limits_{x\rightarrow\infty}e^{-x}$ and $\lim\limits_{x\rightarrow\infty}e^{-x^2}$, since in both cases the input of the exponential tends towards $-\infty$. Similarly, there is no difference between $\lim\limits_{x\rightarrow\infty}e^{x}$ and $\lim\limits_{x\rightarrow\infty}e^{x^2}$, or even something like $\lim\limits_{x\rightarrow\infty}e^{e^x}$, since in all cases the input of the exponential tends towards $\infty$.

::::::{prf:example} 
:label: Ex:LimitAtInfinityComputationrules
Consider the function $f(x)=\dfrac{1}{1+e^{-x}}$ and suppose we want to find out whether it has horizontal asymptotes.

First we consider the limit at infinity. Note that $f$ can be written as the composition $f=g\circ h$ with $g(x)=\frac{1}{x}$ and $h(x)=1+e^{-x}$. Then we can use {prf:ref}`Theorem:LimitAtInfinity:Substitution` to evaluate

$$
 \lim_{x\rightarrow\infty}\frac{1}{1+e^{-x}}=\frac{1}{\lim_{x\rightarrow\infty}\left(1+e^{-x}\right)}.
$$

Using the basic computation rules {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules` to rewrite

$$
 \lim_{x\rightarrow\infty}\frac{1}{1+e^{-x}}=\frac{1}{\lim_{x\rightarrow\infty}1+\lim_{x\rightarrow\infty}e^{-x}}.
$$

Finally, we use the standard limits {prf:ref}`Theorem:LimitAtInfinity:Standardlimits` to evaluate

$$
 \lim_{x\rightarrow\infty}\frac{1}{1+e^{-x}}=\frac{1}{\lim_{x\rightarrow\infty}1+\lim_{x\rightarrow\infty}e^{-x}}=\frac{1}{1+0}=1.
$$

For the limit at minus infinity, we can, similarly, use {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules` and {prf:ref}`Theorem:LimitAtInfinity:Substitution` to write

$$
 \lim_{x\rightarrow-\infty}\frac{1}{1+e^{-x}}=\frac{1}{\lim_{x\rightarrow-\infty}1+\lim_{x\rightarrow-\infty}e^{-x}}.
$$

With {prf:ref}`Theorem:LimitAtInfinity:Standardlimits` we find $\displaystyle \lim_{x\rightarrow-\infty}1$ and $\lim_{x\rightarrow-\infty}e^{-x}=\infty$. Hence, we obtain with {prf:ref}`Theorem:LimitAtInfinity:Substitution2` that

$$
 \lim_{x\rightarrow-\infty}\frac{1}{1+e^{-x}}=\lim_{x\rightarrow\infty}\frac{1}{x}=0.
$$

So this function $f$ has two horizontal asymptotes: one at $y=1$ corresponding to the limit at infinity and one at $y=0$ corresponding to the limit at minus infinity.

:::{todo}
Make an applet with the graph of this function, clearly showing the two horizontal asymptotes.
:::
::::::

In addition, we obtain the following comparison result for limits.

::::::{prf:theorem} Comparison of limits at infinity
:label: Theorem:LimitAtInfinity:Comparison
Suppose that $\lim\limits_{x\rightarrow \infty}f(x)=L$ and $\lim\limits_{x\rightarrow \infty}g(x)=M$. Also suppose that $f(x)\leq g(x)$ for all $x$ in some interval $[d,\infty)$. Then $L\leq M$.

A similar result holds for the limit at minus infinity.
::::::

Again, this result makes sense intuitively: if the function values $f(x)$ are always below $g(x)$, how could the limit $L$ suddenly become larger than $M$? However, in the situation of {prf:ref}`Theorem:LimitAtInfinity:Comparison` you might expect if we knew that $f(x)<g(x)$ for all $x$ close to $a$ that it should follow that $L<M$. This is not true in general, as can be seen from the following example.

::::::{prf:example} 
:label: Ex:LimitAtInfinityComparison
Consider the function $f(x)=-\dfrac{1}{x^2}$ and $g(x)=\dfrac{1}{x^2}$. Then $f(x)<g(x)$ for all $x> 0$. So by {prf:ref}`Theorem:LimitAtInfinity:Comparison` we can immediately conclude that $\lim\limits_{x\rightarrow \infty}-\dfrac{1}{x^2}\leq \lim\limits_{x\rightarrow \infty}\dfrac{1}{x^2}$. However, we can quickly compute that $\lim\limits_{x\rightarrow \infty}-\frac{1}{x^2}= \lim\limits_{x\rightarrow \infty}\frac{1}{x^2}=0$ using {prf:ref}`Theorem:LimitAtInfinity:Standardlimits` and {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules`. So the limits are, in fact, equal even though the functions are never equal.
::::::

We continue the path we set foot on in {prf:ref}`Theorem:LimitAtInfinity:Comparison`, but now we consider the situation where we have $3$ functions, which satisfy

$$
f(x)\leq g(x)\leq h(x)
$$

for all $x$ in some interval $[d\infty)$, so the function $g$ is squeezed in between the functions $f$ and $h$. Suppose that, in addition, we know that $\lim\limits_{x\rightarrow \infty}f(x)$ and $\lim\limits_{x\rightarrow \infty}h(x)$ are **equal**, say they are both $L$. What does that tell us about $\lim\limits_{x\rightarrow \infty}g(x)$?

Well, since $f(x)\leq g(x)$ and $\lim\limits_{x\rightarrow \infty}f(x)=L$, we know that $\lim\limits_{x\rightarrow \infty}g(x)$, if it exists, should be **at least** equal to $L$. On the other hand, since $g(x)\leq h(x)$ and $\lim\limits_{x\rightarrow \infty}h(x)=L$, we find that $\lim\limits_{x\rightarrow \infty}g(x)$, again if it exists, should be **at most** equal to $L$.

We conclude that the limit $\lim\limits_{x\rightarrow \infty}g(x)$ is forced to be equal to $L$, provided the limit exists. The following theorem, known as the **squeeze theorem** (or alternatively the **sandwich theorem** or **pinching theorem**) shows that we do not need to worry about the existence of the limit $\lim\limits_{x\rightarrow \infty}g(x)$.

::::::{prf:theorem} Squeeze theorem for limits at infinity
:label: Theorem:LimitAtInfinity:Squeezetheorem
Suppose that $\lim\limits_{x\rightarrow \infty}f(x)=\lim\limits_{x\rightarrow \infty}h(x)=L$. Also suppose that $f(x)\leq g(x)\leq h(x)$ for all $x$ in some interval $[d,\infty)$. Then $\lim\limits_{x\rightarrow \infty}g(x)$ also exists and $\lim\limits_{x\rightarrow \infty}g(x)=L$.

The corresponding result also holds for limits at minus infinity.

::::::

::::::{prf:example} Squeeze theorem
:label: Ex:LimitAtInfinity:SqueezeThm

Consider the function $f(x)=\dfrac{\sin(x)}{x^2}$ from {prf:ref}`Ex:LimitAtInfinity:Secondexample` and suppose that we want to evaluate $\lim\limits_{x\rightarrow -\infty}\dfrac{\sin(x)}{x^2}$. Since the sine always oscillates between $-1$ and $1$, we see that $\dfrac{-1}{x^2}\leq \dfrac{\sin(x)}{x^2}\leq \dfrac{1}{x^2}$ for all $x<0$. Similar to {prf:ref}`Ex:LimitAtInfinityComparison` we find that $\lim\limits_{x\rightarrow -\infty}-\dfrac{1}{x^2}= \lim\limits_{x\rightarrow -\infty}\dfrac{1}{x^2}=0$. By the squeeze theorem, we find that $\lim\limits_{x\rightarrow -\infty}\dfrac{\sin(x)}{x^2}=0$ as well.

::::{figure} Images/Fig-LimitAtInfinity-SqueezeThm.png
:name: Fig:LimitAtInfinity:SqueezeThm
:class: dark-light

An illustration of the {prf:ref}`Squeeze theorem for limits at infinity <Theorem:LimitAtInfinity:Squeezetheorem>`.
::::

:::{todo}
Turn {numref}`Fig:LimitAtInfinity:SqueezeThm` into an applet. 
:::

::::::

Now consider a limit of a rational function, i.e. a limit of the form $\lim\limits_{x\rightarrow \infty}\frac{p(x)}{q(x)}$ where $p$ and $q$ are polynomials. We write $p(x)=a_nx^n+a_{n-1}x^{n-1}+\ldots+a_0$ and $q(x)=b_mx^m+b_{m-1}x^{m-1}+\ldots+b_0$ with $a_n\neq 0$ and $b_m\neq 0$. Whenever both $p$ and $q$ are not constant, i.e. when $n\geq 1$ and $m\geq 1$, we cannot evaluate the limit directly since both $p$ and $q$ have terms that go to infinity and/or minus infinity as $x$ approaches infinity ($a_nx^n$ for $p$ and $b_mx^m$ for $q$). So how does the function $\frac{p(x)}{q(x)}$ behave for large values of $x$? Notice that if $x$ is large enough the term $a_nx^n$ will be much larger (in absolute value) than the other terms $a_{n-1}x^{n-1}+\ldots+a_0$ of $p$. Similarly, the term $b_mx^m$ will dominate the other terms $b_{m-1}x^{m-1}+\ldots+b_0$ of $q$. So for large values of $x$ we have

$$
 \frac{p(x)}{q(x)}=\frac{a_nx^n+a_{n-1}x^{n-1}+\ldots+a_0}{b_mx^m+b_{m-1}x^{m-1}+\ldots+b_0}\approx \frac{a_nx^n}{b_mx^m}=\frac{a_n}{b_m}x^{n-m}
$$

It now depends on whether $n-m\leq  0$ or $n-m> 0$ whether the limit $\lim\limits_{x\rightarrow \infty}\frac{a_n}{b_m}x^{n-m}$ on whether this limit exists or not, but at least, it gives us an idea of how to compute this limit. In fact, we can make the computation a bit more rigorous. Suppose, for now, that $n< m$. That means that $x^m$ is the dominant term in the fraction. In that case we divide both parts of the fraction by $x^m$ to write

$$
 \frac{p(x)}{q(x)}=\frac{a_nx^n+a_{n-1}x^{n-1}+\ldots+a_0}{b_mx^m+b_{m-1}x^{m-1}+\ldots+b_0}=\frac{\frac{a_n}{x^{m-n}}+\frac{a_{n-1}}{x^{m-n+1}}+\ldots+\frac{a_0}{x^m}}{b_m+\frac{b_{m-1}}{x}+\ldots+\frac{b_0}{x^m}}.
$$

Since $n< m$, we can evaluate now evaluate the limit by using {prf:ref}`Theorem:LimitAtInfinity:Standardlimits`and {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules` to obtain

$$
 \lim\limits_{x\rightarrow \infty}\frac{p(x)}{q(x)}=\lim\limits_{x\rightarrow \infty}\frac{\frac{a_n}{x^{m-n}}+\frac{a_{n-1}}{x^{m-n+1}}+\ldots+\frac{a_0}{x^m}}{b_m+\frac{b_{m-1}}{x}+\ldots+\frac{b_0}{x^m}}=\frac{0+0+\ldots+0}{b_m+0+\ldots+0}=0.
$$

This technique also works when $n=m$, in which case the limit is $\frac{a_n}{b_m}$, or when $n>m$, in which case the limit does not exist. This technique is known as **division by the dominant term**. It also works when $p$ and $q$ are not polynomials, but contain other powers of $x$ like $\sqrt[3]{x}$ or $\sqrt{x^2+x}$. In these cases it is sometimes a bit harder to see what the dominant term is. For instance, in the function $f(x)=\dfrac{x^2+1}{\sqrt{x^3+1}}$ the dominant power is **not** $x^3$, as this one is inside a square root. Indeed, for large values of $x$ we have $\sqrt{x^3+1}\approx \sqrt{x^3}=x^{\frac{3}{2}}$. As such, the dominant term is $x^2$ in this case.

The technique even works when we are evaluating limits of expressions like $\dfrac{1+e^{2x}}{e^x+e^{2x}}$ or $\dfrac{3\ln(x)+\ln(x)^2}{4+\ln(x)^2}$, where the numerator and denominator are polynomials in $e^x$ or $\ln(x)$ instead of $x$, see {prf:ref}`Ex:LimitAtInfinity:Dominant3`.

::::::{prf:example} Division by dominant term
:label: Ex:LimitAtInfinity:Dominant

Suppose that we want to evaluate $\lim\limits_{x\rightarrow \infty}\dfrac{2x+\sqrt{x}-x^3}{3x^3+x^2}$. The highest power of $x$ is $x^3$, so that will be the dominant term. We evaluate the limit by dividing both parts of the fraction by this dominant term. This gives

$$
 \lim\limits_{x\rightarrow \infty}\dfrac{2x+\sqrt{x}-x^3}{3x^3+x^2}=\lim\limits_{x\rightarrow \infty}\dfrac{\frac{2}{x^2}+\frac{1}{x^{\frac{5}{2}}}-1}{3+\frac{1}{x}}.
$$

We can now use {prf:ref}`Theorem:LimitAtInfinity:Standardlimits` and {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules` to obtain

$$
 \lim\limits_{x\rightarrow \infty}\dfrac{2x+\sqrt{x}-x^3}{3x^3+x^2}=\lim\limits_{x\rightarrow \infty}\dfrac{\frac{2}{x^2}+\frac{1}{x^{\frac{5}{2}}}-1}{3+\frac{1}{x}}=\dfrac{0+0-1}{3+0}=-\frac{1}{3}.
$$
::::::

::::::{prf:example} Division by dominant term
:label: Ex:LimitAtInfinity:Dominant2

Suppose that we want to evaluate $\lim\limits_{x\rightarrow -\infty}\dfrac{1+3x}{\sqrt{1+x^2}+2}$. The highest power of $x$ is $x^2$, but $x^2$ is not the dominant term, since it appears inside of a square root. Note that for very negative values of $x$ we have $\sqrt{1+x^2}\approx \sqrt{x^2}=|x|=-x$, so the term $\sqrt{1+x^2}$ behaves like $-x$ for large negative values of $x$. As such, the dominant term in this expression is $x$. We evaluate the limit by dividing both parts of the fraction by this dominant term. This gives

$$
 \lim\limits_{x\rightarrow -\infty}\dfrac{1+3x}{\sqrt{1+x^2}+2}=\lim\limits_{x\rightarrow -\infty}\dfrac{\frac{1}{x}+3}{\frac{1}{x}\sqrt{1+x^2}+\frac{2}{x}}.
$$

A very common mistake, is to now write

$$
 \lim\limits_{x\rightarrow -\infty}\dfrac{\frac{1}{x}+3}{\frac{1}{x}\sqrt{1+x^2}+\frac{2}{x}}=\lim\limits_{x\rightarrow -\infty}\dfrac{\frac{1}{x}+3}{\sqrt{\frac{1}{x^2}+1}+\frac{2}{x}}.\qquad\qquad \left(\textbf{INCORRECT}\right)
$$

Can you spot the error? The computation would have been correct if we had considered the limit at infinity instead of at minus infinity. Notice that for $x<0$ the expression $\frac{1}{x}\sqrt{1+x^2}$ is negative, while the expression $\sqrt{\frac{1}{x^2}+1}$ is positive, so they can never be equal. Indeed, we can write

$$
 \frac{1}{x}\sqrt{1+x^2}=\frac{1}{x}\sqrt{x^2}\sqrt{\frac{1}{x^2}+1}=\frac{1}{x}|x|\sqrt{\frac{1}{x^2}+1}=-\sqrt{\frac{1}{x^2}+1}.
$$

Here we used that $\frac{1}{x}|x|=-1$ since $x<0$. As such, the correct computation is

$$
 \lim\limits_{x\rightarrow -\infty}\dfrac{\frac{1}{x}+3}{\frac{1}{x}\sqrt{1+x^2}+\frac{2}{x}}=\lim\limits_{x\rightarrow -\infty}\dfrac{\frac{1}{x}+3}{-\sqrt{\frac{1}{x^2}+1}+\frac{2}{x}}
$$

We can now use {prf:ref}`Theorem:LimitAtInfinity:Standardlimits` and {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules` to obtain

$$
 \lim\limits_{x\rightarrow -\infty}\dfrac{1+3x}{\sqrt{1+x^2}+2}=\lim\limits_{x\rightarrow -\infty}\dfrac{\frac{1}{x}+3}{-\sqrt{\frac{1}{x^2}+1}+\frac{2}{x}}=\dfrac{0+3}{-\sqrt{0+1}+0}=-3
$$
::::::

::::::{prf:example} Division by dominant term
:label: Ex:LimitAtInfinity:Dominant3

Suppose that we want to evaluate $\lim\limits_{x\rightarrow \infty}\dfrac{1+e^{2x}}{e^x+e^{2x}}$. Then we note that $e^{2x}=\left(e^x\right)^2$, so we can view this function as a rational function in $e^x$. The highest power of $e^x$ is $\left(e^x\right)^2=e^{2x}$. So we divide both parts of the fraction by this highest power to obtain

$$
 \lim\limits_{x\rightarrow \infty}\dfrac{1+e^{2x}}{e^x+e^{2x}}=\lim\limits_{x\rightarrow \infty}\dfrac{e^{-2x}+1}{e^{-x}+1}.
$$

We can now use {prf:ref}`Theorem:LimitAtInfinity:Standardlimits` and {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules` to obtain

$$
 \lim\limits_{x\rightarrow \infty}\dfrac{1+e^{2x}}{e^x+e^{2x}}=\lim\limits_{x\rightarrow \infty}\dfrac{e^{-2x}+1}{e^{-x}+1}=\dfrac{0+1}{0+1}=1.
$$
::::::


Now consider a limit of the form $\lim\limits_{x\rightarrow \infty}\left(p(x)-q(x)\sqrt{r(x)}\right)$ where both $\lim\limits_{x\rightarrow \infty}p(x)$ and $\lim\limits_{x\rightarrow \infty}q(x)\sqrt{r(x)}$ do not exist (for instance, because they are both infinite). Then it can often help to multiply by the 'conjugate square root' $\dfrac{p(x)+q(x)\sqrt{r(x)}}{p(x)+q(x)\sqrt{r(x)}}$ (effectively, we multiply by the constant function $1$, although it is written a bit uglier than usual, so the value of the limit does not change). This technique is also known as the **square root trick**. The reason that this trick works, is that the product $(p(x)-q(x)\sqrt{r(x)})(p(x)+q(x)\sqrt{r(x)})$ simplifies into $p(x)^2-q(x)^2r(x)$, which no longer involves a square root. If $p$, $q$ and $r$ are polynomials, the previously discussed technique of division by the dominant term can subsequently be used to evaluate the limit.

::::::{prf:example} Square root trick
:label: Ex:LimitAtInfinity:Squareroottrick.
Suppose we want to evaluate $\lim\limits_{x\rightarrow \infty}x-\sqrt{x^2+x}$. Notice that both the function is of the form described above and that $\lim\limits_{x\rightarrow\infty }x=\lim\limits_{x\rightarrow\infty }\sqrt{x^2+x}=\infty$. Hence, the limit is of the form "$\infty-\infty$" and as such, it is not clear what happens. Using the square root trick we can evaluate the limit by rewriting

\begin{align*}
 \lim\limits_{x\rightarrow \infty}x-\sqrt{x^2+x} &= \lim\limits_{x\rightarrow \infty}\left(x-\sqrt{x^2+x}\right)\dfrac{x+\sqrt{x^2+x}}{x+\sqrt{x^2+x}} \\
 &= \lim\limits_{x\rightarrow \infty}\dfrac{x^2-(x^2+x)}{x+\sqrt{x^2+1x}} \\
 &= \lim\limits_{x\rightarrow \infty}\frac{-x}{x+\sqrt{x^2+x}}.
\end{align*}
Note that the dominant term in this expression is $x$ and we divide both parts of the fraction by $x$ to evaluate

$$
 \lim\limits_{x\rightarrow \infty}x-\sqrt{x^2+x}=\lim\limits_{x\rightarrow \infty}\frac{-x}{x+\sqrt{x^2+x}}=\lim\limits_{x\rightarrow \infty}\frac{-1}{1+\frac{1}{x}\sqrt{x^2+x}}=\lim\limits_{x\rightarrow \infty}\frac{-1}{1+\sqrt{1+\frac{1}{x}}}.
$$

The remaining limit can be evaluated directly and we find

$$
 \lim\limits_{x\rightarrow \infty}x-\sqrt{x^2+x}=\lim\limits_{x\rightarrow \infty}\frac{-1}{1+\sqrt{1+\frac{1}{x}}}=\frac{-1}{1+1}=-\frac{1}{2}.
$$

::::::

Limits at infinity can also be used to compare the **growth rate** of two functions, i.e. whe can use them to determine whether a function "grows faster" than another function. 

::::::{prf:definition} Growth rate
:label: Def:LimitAtInfinity:Growthrate

Consider two functions $f$ and $g$ with $\lim\limits_{x\rightarrow\infty}f(x)=\infty$ and $\lim\limits_{x\rightarrow\infty}g(x)=\infty$. Then we say that

- $g$ **grows faster** than $f$ if $\lim\limits_{x\rightarrow\infty}\dfrac{g(x)}{f(x)}=\infty$, or, equivalently, if $\lim\limits_{x\rightarrow\infty}\dfrac{f(x)}{g(x)}=0$.
- $f$ and $g$ **grow at a comparable rate** if $\lim\limits_{x\rightarrow\infty}\dfrac{f(x)}{g(x)}=c$ for some $c\neq 0$.

::::::

:::{note}
Suppose we have two functions with $f$ and $g$ with $\lim\limits_{x\rightarrow\infty}f(x)=\infty$ and $\lim\limits_{x\rightarrow\infty}g(x)=\infty$. If $g$ grows faster than $f$, we can write $f(x)=o(g(x))$ as $x\rightarrow \infty$, which reads "$f(x)$ is little o of $g(x)$".

Similarly, if $f$ and $g$ grow at a comparable rate, we write $f(x)=O(g(x))$, which reads "$f(x)$ is big O of $g(x)$". 

However, the little o and big O notations are not used exclusively for functions that grow to infinity. In general, we write $f(x)=o(g(x))$ whenever $\lim\limits_{x\rightarrow\infty}\dfrac{f(x)}{g(x)}=0$ and we write $f(x)=O(g(x))$ whenever there is a positive real number $M$ such that $|f(x)|\leq Mg(x)$ for all $x$. 

In computer science, the big O notation is commonly used to classify the complexity of algorithms, i.e. to classify how much time or space their run time needs.
:::

::::::{prf:theorem} Standard growth rates
:label: Theorem:LimitAtInfinity:Standardgrowthrates
Consider the functions $f(x)=e^{ax}$, $g(x)=x^r$ and $h(x)=\ln(bx)$ for some $a>0$, $r>0$ and $b>0$. Then 


- $f$ grows faster than $g$.
- $g$ grows faster than $h$.



::::::

In order to prove {prf:ref}`Theorem:LimitAtInfinity:Standardgrowthrates` we need some tools that are beyond the scope of this section. We will prove it later in {numref}`Section:lHospital`.

(Subsec:LimitinfOblique)=

## Oblique asymptotes

Some functions do not approach a horizontal line as $x\rightarrow\infty$ or $x\rightarrow-\infty$, but, instead, approach a non-horizontal (straight) line.

::::::{prf:definition} Oblique asymptote
:label: Def:LimitAtInfinity:Oblique

Let $f$ be a function that is defined on some interval $[d,\infty)$. We say that $f$ has an **oblique asymptote** (sometimes called a **slant asymptote**) $y=ax+b$ with $a\neq 0$ at $\infty$, if $\lim\limits_{x\rightarrow\infty}\left(f(x)-ax-b\right)=0$.

Similarly if $f$ is a function that is defined on some interval $(-\infty,d]$, we say that $f$ has an **oblique asymptote** $y=ax+b$ with $a\neq 0$ at $-\infty$, if $\lim\limits_{x\rightarrow-\infty}\left(f(x)-ax-b\right)=0$.
::::::

::::::{prf:example} 
:label: Ex:LimitAtInfinity:Oblique.
Consider the function $f(x)=\frac{x^3+2x^2-4x+8}{x^2-4}$. Using polynomial long division (see {numref}`Subsec:RationalFunctions:PolynomialDivision`), we can write $f(x)=x+2+\frac{16}{x^2-4}$. Note that $f(x)$ consists of the sum of $x+2$, and a part that approaches $0$ as $x$ approaches $\infty$, $\frac{16}{x^2-4}$. This suggests that $f$ approaches the straight line $y=x+2$ as $x\rightarrow\infty$. Indeed, we find that

$$
 \lim\limits_{x\rightarrow\infty}f(x)-(x+2)=\lim\limits_{x\rightarrow\infty}\frac{16}{x^2-4}+x+2-(x+2)=\lim\limits_{x\rightarrow\infty}\frac{16}{x^2-4}=0.
$$

So, the function $f$ indeed has the oblique asymptote $y=x+2$ as $x$ approaches infinity. It has this same oblique asymptote as $x$ approaches minus infinity as well.

::::::

So, which functions have oblique asymptotes? A common example is functions of the form $\dfrac{p(x)}{q(x)}$ with $p$ and $q$ polynomials, where the degree of $p$ is $1$ higher than the degree of $q$, as can be seen from the following result.

::::::{prf:theorem} 
:label: Theorem:LimitAtInfinity:Obliquerational
If $f(x)=\dfrac{p(x)}{q(x)}$ with $p$ and $q$ polynomials where $\operatorname{deg}(p)=\operatorname{deg}(q)+1$, then there is a polynomial $r$ with $\operatorname{deg}(r)<\operatorname{deg}(q)$ for which 

$$
 f(x)=ax+b+\frac{r(x)}{q(x)}
$$

In that case, $f$ has the oblique asymptote $y=ax+b$ at both infinity and minus infinity.
::::::

::::::{admonition} Proof of {prf:ref}`Theorem:LimitAtInfinity:Obliquerational`
:class: tudproof, dropdown

The result follows almost directly from {prf:ref}`Thm:RationalFunctions:PolynomialLongDivision`. Indeed, this result allows us to write $f(x)=\frac{r(x)}{q(x)}+s(x)$ where $r(x)$ and $s(x)$ are polynomials with $\operatorname{deg}(r)<\operatorname{deg}(q)$ and $\operatorname{deg}(s)=\operatorname{p}-\operatorname{q}$. Since $\operatorname{deg}(p)=\operatorname{deg}(q)+1$, we obtain $\operatorname{deg}(s)=1$, so $s(x)=ax+b$ for some $a\neq 0$ and $b$. In order to show that $y=ax+b$ is indeed an oblique asymptote, we write $r(x)=a_nx^n+\ldots+a_1x+a_0$ and $q(x)=b_mx^m+\ldots+b_1x+b_0$ with $a_n\neq 0$ and $b_m\neq 0$. Since $\operatorname{deg}(r)<\operatorname{deg}(q)$ we have $n<m$. As such, the dominant term in the expression $\frac{r(x)}{q(x)}$ is $x^m$. Hence, we can evaluate the limit as

\begin{align*}
 \lim_{x\rightarrow\infty}f(x)-(ax+b) &=\lim_{x\rightarrow\infty}\frac{r(x)}{q(x)}+s(x)-(ax+b)\\
 &= \lim_{x\rightarrow\infty}\frac{a_nx^n+\ldots+a_1x+a_0}{b_mx^m+\ldots+b_1x+b_0}+ax+b-(ax+b)\\
 &= \lim_{x\rightarrow\infty}\frac{\frac{a_n}{x^{m-n}}+\ldots+\frac{a_1}{x^{m-1}}+\frac{a_0}{x^m}}{b_m+\ldots+\frac{b_1}{x^{m-1}}+\frac{b_0}{x^m}}\\
 &= \frac{0+\ldots+0}{b_m+0+\ldots+0}\\
 &= 0.
\end{align*}
As such, $y=ax+b$ is indeed the oblique asymptote of $f$ at infinity. The computation for the oblique asymptote at minus infinity is identical.
::::::

The following result shows an efficient way to find the coefficients of the oblique asymptote, even in case the function is not a quotient of two polynomials.

::::::{prf:theorem} 
:label: Theorem:LimitAtInfinity:Obliquecompute
If $f$ has an oblique asymptote $y=ax+b$ at infinity, then 

$$
 a=\lim\limits_{x\rightarrow\infty}\frac{f(x)}{x}\qquad\text{and}\qquad b=\lim_{x\rightarrow\infty}\left(f(x)-ax\right).
$$

The corresponding result holds for an oblique asymptote at minus infinity.
::::::

::::::{admonition} Proof of {prf:ref}`Theorem:LimitAtInfinity:Obliquecompute`
:class: tudproof, dropdown, full-width

Suppose $f$ has an oblique asymptote $y=ax+b$ at infinity. Then $\lim\limits_{x\rightarrow\infty}\left(f(x)-ax-b\right)=0$, so we can evaluate

$$
 \lim\limits_{x\rightarrow\infty}\frac{f(x)}{x}=\lim\limits_{x\rightarrow\infty}\left(\frac{f(x)-ax-b}{x}+\frac{ax+b}{x}\right)=\lim\limits_{x\rightarrow\infty}\frac{f(x)-ax-b}{x}+\lim\limits_{x\rightarrow\infty}\frac{ax+b}{x}=0+\lim\limits_{x\rightarrow\infty}\frac{a+\frac{b}{x}}{1}=\frac{a+0}{1}=a
$$

Moreover, we find that

$$
 \lim_{x\rightarrow\infty}\left(f(x)-ax\right)=\lim_{x\rightarrow\infty}\left(f(x)-ax-b+b\right)=\lim_{x\rightarrow\infty}\left(f(x)-ax-b\right)+\lim_{x\rightarrow\infty}b=0+b=b
$$

::::::


(Subsec:LimitinfPrecise)=

## Precise definition of limits at infinity

Notice that {prf:ref}`Def:LimitAtInfinity:Intuitivelimit` contains some mathematically vague terms such as 'approach' and 'arbitrarily large'. This intuitive definition is useful for the interpretation of limits at infinity, but not for proving the rules that we have encountered so far. As such, we use this remaining part of the section to provide the precise definition of limits at infinity and to prove the various results that we have encountered so far.

::::::{prf:definition} Precise definition of a limit at plus or minus infinity
:label: Def:LimitAtInfinity:Precisedefplusminus
Let $f$ be a function that is defined on some interval $[d,\infty)$. We say that the **limit at infinity** of $f$ is equal to $L$, and we write $\lim\limits_{x\rightarrow \infty}f(x)=L$, whenever for each $\varepsilon>0$ there exists an $N\geq d$, such that for all $x$ with $x> N$, we have $|f(x)-L|<\varepsilon$. If no such value $L$ exists we say that the limit does not exist.

Similarly, if $f$ is defined on some interval $(-\infty,d]$, we say that the **limit at minus infinity** of $f$ is equal to $L$, and we write $\lim\limits_{x\rightarrow -\infty}f(x)=L$, whenever for each $\varepsilon>0$ there exists an $N\leq d$, such that for all $x$ with $x< N$, we have $|f(x)-L|<\varepsilon$. If no such value $L$ exists we say that the limit does not exist.
::::::

This definition should be interpreted as follows. The arbitrary constant $\varepsilon>0$ should be thought of as a vertical tolerance. In order for $\lim\limits_{x\rightarrow \infty}f(x)=L$, we want that, for $x$ large enough, the function values $f(x)$ are at most distance $\varepsilon$ to $L$, i.e. $|f(x)-L|<\varepsilon$. Here "$x$ large enough" means that this inequality should hold true for all $x$ from a certain point onwards, i.e. an interval of the form $[N,\infty)$. Of course, what this $N$ is, depends both on the function $f$ and the choice of $\varepsilon$. Typically, the smaller $\varepsilon$ is, the larger $N$ should be, as it becomes harder to satisfy the inequality $|f(x)-L|<\varepsilon$. As such, the most interesting (and hardest) part of evaluating a limit using this definition is when $\varepsilon$ is small. Remember that we cannot choose $\varepsilon$ ourselves: for **each** $\varepsilon>0$ there should be a corresponding $N$. Note that we can make $N$ always larger if we want to: if at least one $N$ works for a given $\varepsilon$, we are happy. Before showing how to work with this definition in practice, we first provide the precise definition of infinite limits at infinity.

::::::{prf:definition} Precise definition of an infinite limit at infinity
:label: Def:LimitAtInfinity:Precisedef
Let $f$ be a function that is defined for values of $x>d$ for some $d$. We say that $f$ has an **infinite limit at infinity**, and we write $\lim\limits_{x\rightarrow \infty}f(x)=\infty$, whenever for each $B$ there exists an $N\geq d$, such that for all $x$ with $x> N$, we have $f(x)\geq B$.

Similarly, we say that $f$ has a **negative limit at infinity**, and we write $\lim\limits_{x\rightarrow \infty}f(x)=-\infty$, whenever for each $B$ there exists an $N\geq d$, such that for all $x$ with $x> N$, we have $f(x)\leq B$.

Finally, we have the corresponding notations $\lim\limits_{x\rightarrow -\infty}f(x)=\infty$ and $\lim\limits_{x\rightarrow- \infty}f(x)=-\infty$ for a positive or negative **infinite limit at minus infinity**.
::::::

We now procede with proving the results from the earlier parts of this section.

::::::{admonition} Proof of {prf:ref}`Theorem:LimitAtInfinity:Standardlimits`
:class: tudproof 
$\lim\limits_{x\rightarrow \infty}1=1$: First consider $f(x)=1$. Let $\varepsilon>0$ be given. Since $f$ is constant, we can take $N$ whatever we want, so we choose $N=0$. Then for all $x> N$ we have

$$
 |f(x)-1|=|1-1|=0<\varepsilon.
$$

Hence, we obtain $\lim\limits_{x\rightarrow \infty}1=1$. 

$\lim\limits_{x\rightarrow -\infty}1=1$: Similarly, for $x< N$ we have

$$
 |f(x)-1|=|1-1|=0<\varepsilon.
$$

Hence, we obtain $\lim\limits_{x\rightarrow -\infty}1=1$.

$\lim\limits_{x\rightarrow \infty}x^r=0$: Consider $f(x)=x^r$ with $r<0$. Let $\varepsilon>0$ be given. Since $x^r< \varepsilon$ precisely when $x>\varepsilon^{\frac{1}{r}}$ we choose $N=\varepsilon^{\frac{1}{r}}$. Then for $x> N$ we have

$$
 |f(x)-0|=x^r<\left(\varepsilon^{\frac{1}{r}}\right)^r=\varepsilon.
$$

Hence, we obtain $\lim\limits_{x\rightarrow \infty}x^r=0$.

$\lim\limits_{x\rightarrow \infty}x^r=\infty$: Now consider $f(x)=x^r$ with $r>0$. Let $B>0$ be given. We choose $N=B^{\frac{1}{r}}$. Then for $x> N$ we have

$$
 f(x)=x^r\geq N^r=\left(B^{\frac{1}{r}}\right)^r=B.
$$

We conclude that $\lim\limits_{x\rightarrow \infty}x^r=\infty$.

$\lim\limits_{x\rightarrow -\infty}x^{-r}=0$: Now suppose that $f(x)=x^{-r}$ where $r$ is a positive integer. Let $\varepsilon>0$ be given. Since $|x^{-r}|< \varepsilon$ precisely when $|x|>\frac{1}{\varepsilon^{\frac{1}{r}}}$ we choose $N=\frac{1}{\varepsilon^{\frac{1}{r}}}$. Then for $x< N$ we have

$$
 |f(x)-0|=|x^{-r}|=\frac{1}{|x|^r}<\left(\varepsilon^{\frac{1}{r}}\right)^r=\varepsilon.
$$

We conclude that $\lim\limits_{x\rightarrow -\infty}x^{-r}=0$.

$\lim\limits_{x\rightarrow \infty}e^{-ax}=0$: Now consider $f(x)=e^{-ax}$ with $a>0$. Let $\varepsilon>0$ be given. Since $e^{-ax}< \varepsilon$ precisely when $-ax<\ln(\varepsilon)$, i.e. $x>\frac{\ln(\varepsilon)}{-a}$ we choose $N=\frac{\ln(\varepsilon)}{-a}$. Then for $x> N$ we have

$$
 |f(x)-0|=e^{-ax}<e^{-a\frac{\ln(\varepsilon)}{-a}}=\varepsilon.
$$

We conclude that $\lim\limits_{x\rightarrow \infty}e^{-ax}=0$.

$\lim\limits_{x\rightarrow \infty}e^{ax}=\infty$: Now consider $f(x)=e^{ax}$ with $a>0$. Let $B>0$ be given. Since $e^{ax}> B$ precisely when $ax>\ln(B)$, i.e. $x>\frac{\ln(B)}{a}$, we choose $N=\frac{\ln(B)}{a}$. Then for $x> N$ we have

$$
 f(x)=e^{ax}>e^{a\frac{\ln(B)}{a}}=B.
$$

We conclude that $\lim\limits_{x\rightarrow \infty}e^{ax}=\infty$. 

$\lim\limits_{x\rightarrow \infty}\frac{1}{\ln(x)}=0$: Now consider $f(x)=\frac{1}{\ln(x)}$. Let $\varepsilon>0$ be given. Since $\frac{1}{\ln(x)}< \varepsilon$ precisely when $\ln(x)>\frac{1}{\varepsilon}$, i.e. $x>e^{\frac{1}{\varepsilon}}$ we choose $N=e^{\frac{1}{\varepsilon}}$. Note that $N>1$ so that for $x>N$ we have $x>1$ which gives $\ln(x)>0$. Then for $x> N$ we have

$$
 |f(x)-0|=\frac{1}{\ln(x)}<\frac{1}{\ln\left(e^{\frac{1}{\varepsilon}}\right)}=\varepsilon.
$$

We conclude that $\lim\limits_{x\rightarrow \infty}\frac{1}{\ln(x)}=0$.

$\lim\limits_{x\rightarrow \infty}\ln(x)=\infty$: Now consider $f(x)=\ln(x)$. Let $B>0$ be given. Since $\ln(x)> B$ precisely when $x>e^B$, we choose $N=e^B$. Then for $x> N$ we have

$$
 f(x)=\ln(x)>\ln\left(e^B\right)=B.
$$

We conclude that $\lim\limits_{x\rightarrow \infty}\ln(x)=\infty$. 

$\lim\limits_{x\rightarrow \infty}\arctan(x)=\frac{\pi}{2}$: Finally, we consider $f(x)=\arctan(x)$. Let $\varepsilon>0$ be given. If $\varepsilon\geq \pi$ then $|f(x)-\frac{\pi}{2}|<\varepsilon$, since the arctangent only takes values between $-\frac{\pi}{2}$ and $\frac{\pi}{2}$. As such, we assume that $\varepsilon<\pi$. Notice that $\frac{\pi}{2}-\arctan(x)<\varepsilon$ precisely when $x>\tan\left(\frac{\pi}{2}-\varepsilon\right)$, since the tangent is increasing on $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$, and that $-\frac{\pi}{2}<\frac{\pi}{2}-\varepsilon<\frac{\pi}{2}$, since $\varepsilon<\pi$. So we choose $N=\tan\left(\frac{\pi}{2}-\varepsilon\right)$. Then for $x>N$ we have

$$
 \left|f(x)-\frac{\pi}{2}\right|=\frac{\pi}{2}-\arctan(x)<\frac{\pi}{2}-\arctan\left(\tan\left(\frac{\pi}{2}-\varepsilon\right)\right)=\frac{\pi}{2}-\left(\frac{\pi}{2}-\varepsilon\right)=\varepsilon
$$

We conclude that $\lim\limits_{x\rightarrow \infty}\arctan(x)=\frac{\pi}{2}$. 

$\lim\limits_{x\rightarrow -\infty}\arctan(x)=\frac{-\pi}{2}$: This argument can be repeated for the limit at minus infinity, using $N=-\tan\left(\frac{\pi}{2}-\varepsilon\right)$.

::::{figure} Images/Fig-LimitAtInfinity-Illustrationarctanlimit.png
:name: Fig:LimitAtInfinity:ArctanLimit
:class: dark-light

An illustration of the choice $N$ when evaluating $\lim\limits_{x\rightarrow \infty}\arctan(x)=\frac{\pi}{2}$.
::::

:::{todo}
Turn {numref}`Fig:LimitAtInfinity:ArctanLimit` into an applet. 
:::
::::::


::::::{admonition} Proof of {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules`
:class: tudproof, full-width
We first prove the scalar multiple rule. If $c=0$, then the function $cf$ is constantly $0$, so its limit at infinity must be $0=cL$ as well. As such, we can assume that $c\neq 0$. Let $\varepsilon>0$ be given. Since $\lim\limits_{x\rightarrow \infty}f(x)=L$, we can pick $N$ in such a way that for $x> N$ we have $|f(x)-L|<\frac{\varepsilon}{|c|}$. Then for $x>N$ we have

$$
 |cf(x)-cL|=|c||f(x)-L|<|c|\frac{\varepsilon}{|c|}=\varepsilon.
$$

We conclude that $\lim\limits_{x\rightarrow \infty}cf(x)=cL$.

Now we prove the sum rule. Let $\varepsilon>0$ be given. Since $\lim\limits_{x\rightarrow \infty}f(x)=L$, we can pick $N_1$ in such a way that for $x$ with $x> N_1$ we have $|f(x)-L|<\frac{\varepsilon}{2}$. Similarly we can pick $N_2$ in such a way that for $x$ with $x> N_2$ we have $|g(x)-M|<\frac{\varepsilon}{2}$. We set $N=\max\left(N_1,N_2\right)$, i.e. $N$ is the largest of the two numbers $N_1$ and $N_2$. Then for $x$ with $x> N$ we have both $x> N_1$ and $x> N_2$, so we can estimate

\begin{align*}
 |f(x)+g(x)-(L+M)| &= |(f(x)-L)+(g(x)-M)| \\
 &\leq |f(x)-L|+|g(x)-M| \\
 &< \frac{\varepsilon}{2}+\frac{\varepsilon}{2} \\
 &= \varepsilon.
\end{align*}
Here we used the triangle inequality for absolute values ({prf:ref}`thm:triangle_inequality_real_numbers`). We conclude that $\lim\limits_{x\rightarrow \infty}\left(f(x)+g(x)\right)=L+M$.

Next we prove the product rule. Let $\varepsilon>0$ be given. We pick $N_1$ in such a way that for $x$ with $x> N_1$ we have both $|f(x)-L|<\frac{\varepsilon}{2(|M|+1)}$ and $|f(x)-L|<1$. The inequality $|f(x)-L|<1$ means that $L-1<f(x)<1+L$, which implies that $|f(x)|<|L|+1$. Now we pick $N_2$ in such a way that for $x$ with $x> N_2$ we hav $|g(x)-M|<\frac{\varepsilon}{2(|L|+1)}$. We set $N=\max\left(N_1,N_2\right)$, i.e. $N$ is the largest of the two numbers $N_1$ and $N_2$. Then for $x$ with $x> N$ we have both $x>N_1$ and $x> N_2$, so we can estimate

$$
\begin{array}{lcll}
 |f(x)g(x)-LM| &=& |f(x)g(x)-f(x)M+f(x)M-LM|& \\
 &\leq& |f(x)g(x)-f(x)M|+|f(x)M-LM| \qquad\quad &\left(\text{using the triangle inequality}\right)\\
 &=& |f(x)||g(x)-M|+|M||f(x)-L|& \\
 &\leq& (|L|+1)|g(x)-M|+|M||f(x)-L| \qquad\quad &\left(\text{since }x\geq N_1\text{, which implies }|f(x)|<|L|+1\right)\\
 &\leq& (|L|+1)|g(x)-M|+|M|\frac{\varepsilon}{2(|M|+1)}  &\left(\text{since }x\geq N_1\text{, which implies }|f(x)-L|<\frac{\varepsilon}{2(|M|+1)}\right)\\
 &<& (|L|+1)\frac{\varepsilon}{2(|L|+1)}+|M|\frac{\varepsilon}{2(|M|+1)}&\left(\text{since }x\geq N_2\text{, which implies }|g(x)-M|<\frac{\varepsilon}{2(|L|+1)}\right)\\
 &<& \frac{\varepsilon}{2}+\frac{\varepsilon}{2} &\\
 &=& \varepsilon.&
\end{array}
$$

Here we again used the triangle inequality for absolute values ({prf:ref}`thm:triangle_inequality_real_numbers`). We conclude that $\lim\limits_{x\rightarrow \infty}f(x)g(x)=LM$.

We prove the quotient rule by writing $\frac{f(x)}{g(x)}=f(x)\frac{1}{g(x)}$ and first showing that $\lim\limits_{x\rightarrow \infty}\frac{1}{g(x)}=\frac{1}{M}$. Let $\varepsilon>0$ be given. We pick $N$ in such a way that for $x$ with $x> N$ we have both have $|g(x)-M|<\frac{\varepsilon M^2}{2}$ and $|g(x)-M|<\frac{1}{2}|M|$. The inequality $|g(x)-M|<\frac{1}{2}|M|$ means that $\frac{1}{2}|M|\leq |g(x)|$ (which, in particular, means that $g(x)\neq 0$) and, finally, that $\frac{1}{|g(x)|}\leq\frac{2}{|M|}$. Hence, we can estimate

$$
\begin{array}{lcll}
 \left|\frac{1}{g(x)}-\frac{1}{M}\right| &=& \left|\frac{g(x)-M}{g(x)M}\right| &\\
 &= &\frac{1}{|g(x)|}\frac{1}{|M|}|g(x)-M|\qquad\quad&\\
 &\leq &\frac{2}{|M|}\frac{1}{|M|}|g(x)-M|&\left(\text{since }x\geq N\text{, which implies }\frac{1}{2}|M|\leq |g(x)|\right) \\
 &< &\frac{2}{M^2}\frac{\varepsilon M^2}{2}& \left(\text{since }x\geq N\text{, which implies }|g(x)-M|<\frac{\varepsilon M^2}{2}\right) \\
 &= &\varepsilon.&
\end{array}
$$

We conclude that $\lim\limits_{x\rightarrow \infty}\frac{1}{g(x)}=\frac{1}{M}$. By the product rule, we find that $\lim\limits_{x\rightarrow \infty}\frac{f(x)}{g(x)}=\lim\limits_{x\rightarrow \infty}f(x)\frac{1}{g(x)}=L\frac{1}{M}=\frac{L}{M}$.
::::::



::::::{admonition} {prf:ref}`Theorem:LimitAtInfinity:Substitution2`
:class: tudproof 
We first assume that $\lim\limits_{x\rightarrow\infty}g(x)=\infty$. Let $\varepsilon>0$ be given. We write $\lim\limits_{x\rightarrow\infty}f(x)=L$ and we pick $N$ in such a way that for $x$ with $x\geq N_1$ we have $|f(x)-L|<\varepsilon$. Since $\lim\limits_{x\rightarrow\infty}g(x)=\infty$, we can pick $N_2$ such that for all $x\geq N_2$ we have $g(x)\geq N_1$. Then for $x\geq N_2$ we have $|f(g(x))-L|<\varepsilon$, since $g(x)\geq N_1$. As such, we find that $\lim\limits_{x\rightarrow\infty}f(g(x))=L$. 


Now suppose that $\lim\limits_{x\rightarrow\infty}g(x)=\infty$ and $\lim\limits_{x\rightarrow\infty}f(x)=\infty$. Let $B$ be given. Since $\lim\limits_{x\rightarrow\infty}f(x)=\infty$ we can pick $N_1$ such that for $x$ with $x\geq N_1$ we have $f(x)\geq N_1$. Since $\lim\limits_{x\rightarrow\infty}g(x)=\infty$, we can pick $N_2$ such that for all $x\geq N_2$ we have $g(x)\geq N_1$. Then for $x\geq N_2$ we have $f(g(x))\geq B$, since $g(x)\geq N_1$. As such, we find that $\lim\limits_{x\rightarrow\infty}f(g(x))=\infty$. 


The other cases follow similarly.

::::::

::::::{admonition} Proof of {prf:ref}`Theorem:LimitAtInfinity:Comparison`
:class: tudproof 
We argue by contradiction, which means that we assume that $L>M$ and work towards a contradiction. Since $L>M$ we have $L-M>0$ and we can set $\varepsilon=\frac{L-M}{4}>0$.

Since we have $\lim\limits_{x\rightarrow \infty}f(x)=L$ we can pick $N_1$ in such a way that for $x$ with $x\geq N_1$ we have have $|f(x)-L|<\varepsilon$. Also, since $\lim\limits_{x\rightarrow \infty}g(x)=M$ we can pick $N_2$ in such a way that for $x$ with $x\geq N_2$ we have have $|g(x)-M|<\varepsilon$.

We set $N=\max\left(N_1,N_2\right)$, i.e. $N$ is the largest of the two numbers $N_1$ and $N_2$. Then for $x$ with $x\geq N$ we have both $x\geq N_1$ and $x\geq N_2$. For these values of $x$ we must have $|f(x)-L|<\varepsilon=\frac{L-M}{4}$, which implies $f(x)\geq L-\frac{L-M}{4}=\frac{3}{4}L+\frac{1}{4}M$.

Similarly we must have for these values of $x$ that $|g(x)-M|<\varepsilon=\frac{L-M}{4}$, which implies $g(x)\leq M+\frac{L-M}{4}=\frac{3}{4}M+\frac{1}{4}L$. Since $L>M$ we then obtain

$$
 g(x)\leq \frac{3}{4}M+\frac{1}{4}L=\frac{1}{4}\left(L+M\right)+\frac{M}{2}<\frac{1}{4}\left(L+M\right)+\frac{L}{2}=\frac{3}{4}L+\frac{1}{4}M\leq f(x),
$$

which is a contradiction, since we assumed that $f(x)\leq g(x)$ for all $x\geq d$. So that means that $L\leq M$.
::::::

::::::{admonition} Proof of {prf:ref}`Theorem:LimitAtInfinity:Squeezetheorem`
:class: tudproof 
We let $\varepsilon>0$ be given. Since we have $\lim\limits_{x\rightarrow \infty}f(x)=L$ we can pick $N_1$ in such a way that for $x$ with $x\geq N_1$ we have have $|f(x)-L|<\varepsilon$. Also, since $\lim\limits_{x\rightarrow \infty}h(x)=L$ we can pick $N_2$ in such a way that for $x$ with $x>N_2$ we have have $|h(x)-L|<\varepsilon$.

We set $N=\max\left(N_1,N_2\right)$, i.e. $N$ is the largest of the two numbers $N_1$ and $N_2$. Then for $x>N$ we both have $x>N_1$ and $x>N_2$. For these values of $x$ we have $|f(x)-L|<\varepsilon$, which implies that $L-\varepsilon< f(x)$. Similarly, for these values of $x$ we have $|h(x)-L|<\varepsilon$, which implies that $h(x)> L+\varepsilon$.

As such, we can estimate for $x$ with $x>N$:

\begin{align*}
 L-\varepsilon &< f(x) \\
 &\leq g(x) \\
 &\leq h(x) \\
 &< L+\varepsilon.
\end{align*}

In particular, we find for these values of $x$ that $L-\varepsilon<g(x)<L+\varepsilon$, which yields $|g(x)-L|<\varepsilon$. We conclude that $\lim\limits_{x\rightarrow \infty}g(x)=L$.
::::::

(Subsec:LimitAtInfinityGrasple)=

## Grasple exercises


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a6b4c8f6-cf3e-4aaa-85e0-0d76fdfc3d8b?id=71164
:label: Grasple:LimitAtInfinity:Quadoverquad
:dropdown:
:description: Limit at infinity of a rational function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4af8e229-c01b-4eb8-b148-8c0024bdc69b?id=71193
:label: Grasple:LimitAtInfinity:Linoverquad
:dropdown:
:description: Limit at infinity of a rational function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/008cf791-391e-47b2-9af3-cd385a21d8f5?id=71198
:label: Grasple:LimitAtInfinity:Cuboverquad
:dropdown:
:description: Limit at infinity of a rational function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c015f479-ee61-49b8-b49c-7351d30978b2?id=75781
:label: Grasple:LimitAtInfinity:xtonoverxton
:dropdown:
:description: Limit at infinity of a rational function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a95901e2-c3a4-4700-8057-651538308fcc?id=75769
:label: Grasple:LimitAtInfinity:xtonoverxtonwithcos
:dropdown:
:description: Limit at infinity, but now with an extra cosine

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1ae3fb96-1392-4018-8a7c-da08fa205c2f?id=71202
:label: Grasple:LimitAtInfinity:Cuboverquadmin
:dropdown:
:description: Limit at infinity of a rational function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6906d93e-496e-4953-a989-c39daeded01a?id=75780
:label: Grasple:LimitAtInfinity:Ratofexp
:dropdown:
:description: Limit at infinity of function containing exponentials

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1712135e-9d9c-4817-8021-4c9b1d22cdc7?id=74230
:label: Grasple:LimitAtInfinity:Firstsimplify
:dropdown:
:description: Limit at infinity of composition of exponential and logarithm

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/de13b607-0050-4942-aff6-13834c8d9846?id=74225
:label: Grasple:LimitAtInfinity:Sub
:dropdown:
:description: Turning one limit at infinity into another

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/afae0da5-b56d-43ef-a16f-3349b6cfc66a?id=71344
:label: Grasple:LimitAtInfinity:Linoversqquad
:dropdown:
:description: Limit at infinity and minus infinity of expression with square root

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/364d5cc0-c557-43a5-9d80-7617fef3c0e1?id=69511
:label: Grasple:LimitAtInfinity:sqquadminsqquad
:dropdown:
:description: Limit at infinity of expression with square roots

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/30f0be51-19c4-43fa-9168-26b96c8a54ec?id=69495
:label: Grasple:LimitAtInfinity:mininfsqquadminsqquad
:dropdown:
:description: Limit at minus infinity of expression with square roots

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0c4c33b1-0abc-4dc8-83bb-9e7044e29336?id=75620
:label: Grasple:LimitAtInfinity:squeezesinoverxton
:dropdown:
:description: Limit at infinity containing a sine

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2701792b-bac2-4d29-9812-d51e04d3673e?id=75623
:label: Grasple:LimitAtInfinity:squeezesexpcosoverxton
:dropdown:
:description: Limit at infinity containing a cosine and an exponential

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/200b7827-53cc-4649-806c-353cefbac20a?id=75625
:label: Grasple:LimitAtInfinity:squeezebetweenrational
:dropdown:
:description: Limit at infinity of function in between two other functions

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7cc6b0ea-88ca-488e-b3d2-d459c729c600?id=75644
:label: Grasple:LimitAtInfinity:Horasympquadoverquad
:dropdown:
:description: Horizontal asymptotes of a rational function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/eca4d037-1be9-4f2c-9795-683a8ce44245?id=75739
:label: Grasple:LimitAtInfinity:Horasympln
:dropdown:
:description: Horizontal asymptotes of logarithm

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0ff3a3ce-4627-4292-82a5-dc549b34f96c?id=69475
:label: Grasple:LimitAtInfinity:Horasymplinoversqquad
:dropdown:
:description: Horizontal asymptotes of a function containing a square root

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/16159b6e-64e4-46a6-8194-89e9a3a5320e?id=69474
:label: Grasple:LimitAtInfinity:Horasympquadoversqquad
:dropdown:
:description: Horizontal asymptotes of a function containing a square root

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c41a8138-9686-48d0-9ab6-a1b9da61d047?id=69473
:label: Grasple:LimitAtInfinity:Horasympratexp
:dropdown:
:description: Horizontal asymptotes of a function containing exponentials

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/047c46d7-70f6-490d-a879-4ff27a72ef74?id=75736
:label: Grasple:LimitAtInfinity:Horasympratabs
:dropdown:
:description: Horizontal asymptotes of a function containing an absolute value

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7d2aeced-4a0f-43bd-bdd0-93bd72a86df4?id=69483
:label: Grasple:LimitAtInfinity:Horvertasympquadoverquad
:dropdown:
:description: Horizontal and vertical asymptotes of a rational function

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/12e94043-637f-42ec-8db3-46f74a960f2a?id=69470
:label: Grasple:LimitAtInfinity:Horvertasymparctan1overx
:dropdown:
:description: Horizontal and vertical asymptotes of $\arctan\left(\frac{1}{x}\right)$

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6c17b1be-26a6-4238-8840-7a1a4d01870c?id=75715
:label: Grasple:LimitAtInfinity:Growthrategraph
:dropdown:
:description: Comparing growth rates in a graph

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/05f0d460-1708-457d-b6fc-525460cf1679?id=75714
:label: Grasple:LimitAtInfinity:Growthratecompute
:dropdown:
:description: Comparing growth between some functions

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/931e35df-c5d0-440e-ae9a-fff935f428d9?id=75721
:label: Grasple:LimitAtInfinity:Growthrateinbetween
:dropdown:
:description: Growth rate in between some other growth rates

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9d9ef2ef-1f17-4c01-8a6b-22fb40dbea0f?id=93108
:label: Grasple:LimitAtInfinity:Obliquerat2
:dropdown:
:description: How many oblique asymptotes does this rational function have

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/053924a4-e206-4646-b773-5543973c6ac6?id=93106
:label: Grasple:LimitAtInfinity:Obliquesqrt1
:dropdown:
:description: How many oblique asymptotes does this function containing a square root have?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ce2ad418-d71a-4453-98a2-b49a6990efb5?id=93107
:label: Grasple:LimitAtInfinity:Obliquerat1
:dropdown:
:description: Oblique asymptotes of a rational function

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/df936d9a-ed59-4d4b-bdb6-475292e4584c?id=93105
:label: Grasple:LimitAtInfinity:Obliquesqrt2
:dropdown:
:description: Oblique asymptotes of a function containing a square root

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d4ae69f9-e2da-4756-9c1f-01677905fe15?id=93091
:label: Grasple:LimitAtInfinity:Obliquesqrtmin
:dropdown:
:description: Oblique asymptotes of a function containing a square root

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a42deb9a-1079-4ee4-baad-c6689c07dd56?id=71340
:label: Grasple:LimitAtInfinity:Workingwithformaldef
:dropdown:
:description: Working with the formal definition of a limit at infinity

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/36eb98d4-ee3e-4fd1-9ef0-1c170b3cedfa?id=75716
:label: Grasple:LimitAtInfinity:Applraindrops
:dropdown:
:description: Application: equilibrium velocity of falling raindrop

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4cabfed3-8854-4d1d-8e84-c3081e8fc3ed?id=75718
:label: Grasple:LimitAtInfinity:Applbrine
:dropdown:
:description: Application: equilibrium concentration in salt tank

::::