# Limits at infinity

(Subsec:LimitinfIntuitive)=

## Intuitive definition of limits at infinity

Many problems in nature and engineering feature quantities that for, relatively short periods of time, fluctuate or change rapidly, before stabilizing and moving towards a certain equilibrium. In such cases, we are often mainly intersted in what happens in the long term. Suppose, for instance, that we buy a cauliflower at the supermarket, which has a temperature of $20\,^\circ C$. We place it into a refrigerator, which has a temperature of $5\,^\circ C$ and we want to know how the temperature $T$ (in degrees Celcius) of the cauliflower changes as a function of time $t$ (in minutes). Using Newton's law of cooling, it can be shown that $T(t)=T_{\mathrm{env}}+(T(0)-T_{\mathrm{env}})e^{-rt}$. Here, $T_{\mathrm{env}}=5$ is the temperature of the refrigerator and $r>0$ is a constant representing the rate of the heat transfer between the object and the environment. For convenience, we take $r=1$ here. Note that $T(0)=20$, since the object starts at this temperature when we place it into the refrigerator. In particular, we can write $T(t)=5+15e^{-t}$. What happens after a very long time? Intuitively, we know the answer: the temperature of the cauliflower will be very close to the temperature of the refrigerator $5\,^\circ C$. Indeed, we can also observe this when we plot the temperature as a function of time.

Hier een plot van de functie T(t), waar ook de horizontale asymptoot T=5 is aangegeven.

We observe that our intuition was correct: the temperature of the object will first decrease rapidly before slowly moving towards the limiting value of $5\,^\circ C$. Notice that the temperature never becomes precisely equal to $5\,^\circ C$; it will always remain slightly above this value. We say that the function $T(t)$ has a **horizontal asymptote** at $T=5$ and we denote this by $\lim\limits_{t\rightarrow\infty}T(t)=5$. As was stated in {numref}`Section:LimitPoint`, the word asymptote comes from the Greek $\grave{\alpha}\sigma\acute{\upsilon}\mu\pi\tau\omega\tau o\varsigma$ (asumptotos), which means "not falling together". The notation $\lim\limits_{t\rightarrow\infty}T(t)=5$ can be pronounced as "the function values $T(t)$ approach the value $5$ as $t$ approaches infinity". The precise definition of such a limit at infinity is rather technical, so we postpone it to {numref}`Subsec:LimitinfPrecise`. Instead, we will use the following more intuitive definition.

::::::{prf:definition} Intuitive definition of a limit at plus or minus infinity
:label: Def:LimitAtInfinity:Intuitivelimit

Let $f$ be a function that is defined for values of $x>M$ for some $M$. We say that the **limit at infinity** of $f$ is equal to $L$, and we write $\lim\limits_{x\rightarrow \infty}f(x)=L$, if the function values $f(x)$ approach $L$ as $x$ grows arbitrarily large. If no such real number $L$ exists, we say that the limit of the function $f$ at infinity does not exist.

Similarly, if $f$ is defined for values of $x<M$ for some $M$, we say that the **limit at minus infinity** of $f$ is equal to $L$, and we write $\lim\limits_{x\rightarrow -\infty}f(x)=L$, if the function values $f(x)$ approach $L$ as $x$ grows arbitrarily large negative. If no such real number $L$ exists, we say that the limit of the function $f$ at minus infinity does not exist.

If either $\lim\limits_{x\rightarrow \infty}f(x)=L$ or $\lim\limits_{x\rightarrow -\infty}f(x)=L$, we say that the function $f$ has a **horizontal asymptote** at $y=L$.
::::::


Since we only work with an intuitive definition, we will also postpone all proofs in this section to {numref}`Subsec:LimitinfPrecise`.


::::::{prf:example} 
:label: Ex:LimitAtInfinity:Firstexample

Consider the function $f(x)=\dfrac{4+\frac{1}{x}}{2-\frac{3}{x^2}}$ and suppose we want to evaluate $\lim\limits_{x\rightarrow \infty}f(x)$. First, we make a table of the function values for increasing values of $x$.

Hier een tabel voor de functiewaarden van f voor x=1,10,100,1000,10000,100000,1000000

Notice that the function values seem to go towards the value $2$. This would suggest that $\lim\limits_{x\rightarrow \infty}f(x)=2$. Let us see if we can find out where this value comes from. If $x$ is very large, notice that $\frac{1}{x}$ and $-\frac{3}{x^2}$ are very close to $0$, since we are dividing a relatively small number by a much larger number. As such, for large values of $x$ we have

$$
 f(x)=\dfrac{4+\frac{1}{x}}{2-\frac{3}{x^2}}\approx \dfrac{4+0}{2-0}=\dfrac{4}{2}=2
$$

Later in this section, we will show that this reasoning is indeed mathematically valid. As such, the function $f$ has a horizontal asymptote at $y=2$. We can also see in the graph of $f$ that the function values tend towards the value $2$ as $x$ gets large.

Hier plot van deze functie voor x groot, met de lijn y=2 ook aangegeven.
::::::

::::::{prf:example} 
:label: Ex:LimitAtInfinity:Secondexample

Consider the function $f(x)=\dfrac{\sin(x)}{x^2}$ and suppose we want to evaluate $\lim\limits_{x\rightarrow -\infty}f(x)$. First, we make a table of the function values for increasingly negative values of $x$.

Hier een tabel voor de functiewaarden van f voor x=-1,-10,-100,-1000,-10000,-100000,-1000000

Notice that the function values seem to go towards the value $0$. This would suggest that $\lim\limits_{x\rightarrow -\infty}f(x)=0$. Indeed, we notice that $\sin(x)$ is always between $-1$ and $1$, even if $x$ is very negative. This means that $\dfrac{\sin(x)}{x^2}$ is a number, where something between $-1$ and $1$ is divided by something very large. As such, $\dfrac{\sin(x)}{x^2}$ is very close to $0$. In {prf:ref}`Ex:LimitAtInfinity:SqueezeThm` we will show that this reasoning is indeed valid.

Hier plot van deze functie voor x negatief, met de lijn y=0 ook aangegeven.

Notice that the function $f$ actually osciallates around the horizontal asymptote $x=0$. This is no problem, as the function values indeed tends towards $0$. However, this does mean that original Greek meaning of the word asymptote ("not falling together") does not exactly match the modern use.
::::::

::::::{prf:example} 
:label: Ex:LimitAtInfinity:Firstexamplenonexist

Consider the function $f(x)=x^2$ and suppose we want to evaluate $\lim\limits_{x\rightarrow \infty}f(x)$. First, we make a table of the function values for increasing values of $x$.

Hier een tabel voor de functiewaarden van f voor x=1,10,100,1000,10000,100000,1000000

Notice that the function values seem to blow up and that they do not towards a certain number. Indeed, as $x$ tends towards infinity, $x^2$ will do so as well. As such, the limit $\lim\limits_{x\rightarrow \infty}x^2$ does not exist. 
::::::

In {prf:ref}`Ex:LimitAtInfinity:Firstexamplenonexist` the limit of the function at infinity did not exist, because the function values blew up as $x$ grew. This is actually a very common situation, so it deserves its own notation.

::::::{prf:definition} Intuitive definition of an infinite limit at infinity
:label: Def:LimitAtInfinity:Inflimitint
Let $f$ be a function defined for values of $x>M$ for some $M$. Then we say that $f$ has an **infinite limit at infinity**, and we write $\lim\limits_{x\rightarrow \infty}f(x)=\infty$ whenever the function values $f(x)$ grow arbitrarily large as $x$ grows arbitrarily large.

Similarly, we say that $f$ has a **negative infinite limit at infinity**, and we write $\lim\limits_{x\rightarrow \infty}f(x)=-\infty$ whenever the function values $f(x)$ grow arbitrarily large negative as $x$ grows arbitrarily large.

Finally, we have the corresponding notations $\lim\limits_{x\rightarrow -\infty}f(x)=\infty$ and $\lim\limits_{x\rightarrow -\infty}f(x)=-\infty$ for a positive or negative **infinite limit at minus infinity**.
::::::

::::::{warning} 
:name: Warning:LimitAtInfinity:Infinitelimit

A notation like $\lim\limits_{x\rightarrow \infty}f(x)=\infty$ or $\lim\limits_{x\rightarrow \infty}f(x)=-\infty$ do not mean that $\infty$ and $-\infty$ are numbers, nor do they mean that these limits exist. A correct way to pronounce the notation $\lim\limits_{x\rightarrow \infty}f(x)=\infty$ is **the limit of $f$ at infinity does not exist, because the function values grow without bound**.
::::::

Notice that a function can have either $0$, $1$ or $2$ horizontal asymptotes, depending on whether $\lim\limits_{x\rightarrow \infty}f(x)$ and $\lim\limits_{x\rightarrow -\infty}f(x)$ exist. Even if both limits exist, the function might still have only $1$ horizontal asymptotes whenver $\lim\limits_{x\rightarrow \infty}f(x)=\lim\limits_{x\rightarrow -\infty}f(x)$.

Previously, we saw that a limit at infinity might not exist, because there the function has an infinite or negative limit there. There are other reasons why a limit might not exist, and we will show a few commonly occuring cases.

::::::{prf:example} 
:label: Ex:LimitAtInfinity:Secondexamplenonexist

Consider the function $f(x)=\cos(x)$ and suppose we want to evaluate $\lim\limits_{x\rightarrow \infty}f(x)$. First, we make a table of the function values for increasing values of $x$.

Hier een tabel voor de functiewaarden van f voor x=1,10,100,1000,10000,100000,1000000

Notice that the function values do not seem to tend to some particular value. This is because the cosine keeps on osciallating between $-1$ and $1$, even if $x$ grows large. As such, the limit $\lim\limits_{x\rightarrow \infty}\cos(x)$ does not exist.
::::::

::::::{prf:example} 
:label: Ex:LimitAtInfinity:Thirdexamplenonexist

Consider the function $f(x)=\sqrt{x}$ and suppose we want to evaluate $\lim\limits_{x\rightarrow -\infty}f(x)$. When we try to make a table of the funcion values for negative values of $x$, we immediately run into trouble as the function is not defined for negative values of $x$. As such, the limit $\lim\limits_{x\rightarrow -\infty}\sqrt{x}$ does not exist.
::::::

(Subsec:LimitinfEvaluating)=

## Evaluating limits

In order to evaluate limits at infinity, we need two important building blocks: standard limits and calculation rules. Combining these will allow us to evaluate most limits that you will encounter in practice. In particular, combining these two results, shows that the we evaluated the limit in {prf:ref}`Ex:LimitAtInfinity:Firstexample` correctly. As can be expected, many results are very similar to those in {numref}`Subsec:Limitsrules`, so we follow a very similar structure.

::::::{prf:theorem} Standard limits
:label: Theorem:LimitAtInfinity:Standardlimits
We have the following standard limits.


- $\lim\limits_{x\rightarrow\infty}x^r=0$ when $r<0$;
- $\lim\limits_{x\rightarrow\infty}x^r=\infty$ when $r>0$;
- $\lim\limits_{x\rightarrow-\infty}x^r=0$ when $r$ is a positive integer;
- $\lim\limits_{x\rightarrow\infty}e^{-ax}=0$ when $a>0$;
- $\lim\limits_{x\rightarrow\infty}e^{ax}=\infty$ when $a>0$;
- $\lim\limits_{x\rightarrow\infty}\frac{1}{\ln(x)}=0$;
- $\lim\limits_{x\rightarrow\infty}\ln(x)=\infty$;
- $\lim\limits_{x\rightarrow-\infty}\arctan(x)=-\dfrac{\pi}{2}$;
- $\lim\limits_{x\rightarrow\infty}\arctan(x)=\dfrac{\pi}{2}$.


WILLEM: Waarschijnlijk mooier om in twee kolommen te doen, maar dat kreeg ik niet werkend.
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
Suppose $f$ is a polynomial, rational function, power of $x$, (inverse) trigonometric function, exponential function or logarithmic function and that $b$ is in the domain of $f$. Moreover, suppose that $\lim\limits_{x\rightarrow \infty}g(x)=b$. Then $\lim\limits_{x\rightarrow \infty}f(g(x))=f\left(\lim\limits_{x\rightarrow \infty}g(x)\right)=f(b)$.

A similar result holds for limits at minus ifinity.
::::::

The result above shows that limits can be "taken inside" a nice enough function. In fact, there is a slightly more general version of this result, which will be covered in {numref}`Section:Continuity`.

In addition, we obtain the following comparison result for limits.

::::::{prf:theorem} Comparison of limits at infinity
:label: Theorem:LimitAtInfinity:Comparison
Suppose that $\lim\limits_{x\rightarrow \infty}f(x)=L$ and $\lim\limits_{x\rightarrow \infty}g(x)=M$. Also suppose that $f(x)\leq g(x)$ for all $x\geq N$ for a certain $N$. Then $L\leq M$.

::::::

Again, this result makes sense intuitively: if the function values $f(x)$ are always below $g(x)$, how could the limit $L$ suddenly become larger than $M$? However, in the situation of {prf:ref}`Theorem:LimitAtInfinity:Comparison` you might expect if we knew that $f(x)<g(x)$ for all $x$ close to $a$ that it should follow that $L<M$. This is not true, in general, as can be seen from the following example.

::::::{prf:example} 
:label: Ex:LimitAtInfinityComparison
Consider the function $f(x)=-\dfrac{1}{x^2}$ and $g(x)=\dfrac{1}{x^2}$. Then $f(x)<g(x)$ for all $x> 0$. So by {prf:ref}`Theorem:LimitAtInfinity:Comparison` we can immediately conclude that $\lim\limits_{x\rightarrow \infty}-\dfrac{1}{x^2}\leq \lim\limits_{x\rightarrow \infty}\dfrac{1}{x^2}$. However, we can quickly compute that $\lim\limits_{x\rightarrow \infty}-\frac{1}{x^2}= \lim\limits_{x\rightarrow \infty}\frac{1}{x^2}=0$ using {prf:ref}`Theorem:LimitAtInfinity:Standardlimits` and {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules`. So the limits are, in fact, equal even though the functions are never equal.
::::::

We continue the path we set foot on in {prf:ref}`Theorem:LimitAtInfinity:Comparison`, but now we consider the situation where we have $3$ functions, which satisfy

$$
f(x)\leq g(x)\leq h(x)
$$

for all $x$ close to $a$, so the function $g$ is squeezed in between the functions $f$ and $h$. Suppose that, in addition, we know that $\lim\limits_{x\rightarrow \infty}f(x)$ and $\lim\limits_{x\rightarrow \infty}h(x)$ are **equal**, say they are both $L$. What does that tell us about $\lim\limits_{x\rightarrow \infty}g(x)$?

Well, since $f(x)\leq g(x)$ and $\lim\limits_{x\rightarrow \infty}f(x)=L$, we know that $\lim\limits_{x\rightarrow \infty}g(x)$, if it exists, should be **at least** equal to $L$. On the other hand, since $g(x)\leq h(x)$ and $\lim\limits_{x\rightarrow \infty}h(x)=L$, we find that $\lim\limits_{x\rightarrow \infty}g(x)$, again if it exists, should be **at most** equal to $L$.

We conclude that the limit $\lim\limits_{x\rightarrow \infty}g(x)$ is forced to be equal to $L$, provided the limit exists. The following theorem, known as the **squeeze theorem**, or alternatively the **sandwich theorem** or **pinching theorem**, shows that we do not need to worry about the existence of the limit $\lim\limits_{x\rightarrow \infty}g(x)$.

::::::{prf:theorem} Squeeze theorem for limits at infinity
:label: Theorem:LimitAtInfinity:Squeezetheorem
Suppose that $\lim\limits_{x\rightarrow \infty}f(x)=\lim\limits_{x\rightarrow \infty}h(x)=L$. Also suppose that $f(x)\leq g(x)\leq h(x)$ for all $x\geq M$ for some $M$. Then $\lim\limits_{x\rightarrow \infty}g(x)$ also exists and $\lim\limits_{x\rightarrow \infty}g(x)=L$.

The corresponding result also holds for limits at minus infinity.

::::::

::::::{prf:example} Squeeze theorem
:label: Ex:LimitAtInfinity:SqueezeThm

Consider the function $f(x)=\dfrac{\sin(x)}{x^2}$ from {prf:ref}`Ex:LimitAtInfinity:Secondexample` and suppose that we want to evaluate $\lim\limits_{x\rightarrow -\infty}\dfrac{\sin(x)}{x^2}$. Since the sine always oscillates between $-1$ and $1$, we see that $\dfrac{-1}{x^2}\leq \dfrac{\sin(x)}{x^2}\leq \dfrac{1}{x^2}$ for all $x<0$. Similar to {prf:ref}`Ex:LimitAtInfinityComparison` we find that $\lim\limits_{x\rightarrow -\infty}-\dfrac{1}{x^2}= \lim\limits_{x\rightarrow -\infty}\dfrac{1}{x^2}=0$. By the squeeze theorem, we find that $\lim\limits_{x\rightarrow -\infty}\dfrac{\sin(x)}{x^2}=0$ as well.

Hier nog een plaatje van de drie functies, misschien niet al te erg uitgezoomd omdat het dan niet meer zichtbaar is.
::::::

Now consider a limit of the form $\lim\limits_{x\rightarrow \infty}\frac{p(x)}{q(x)}$ where $p$ and $q$ are polynomials. We write $p(x)=a_nx^n+a_{n-1}x^{n-1}+...+a_0$ and $q(x)=b_mx^m+b_{m-1}x^{m-1}+...+b_0$ with $a_n\neq 0$ and $b_m\neq 0$. Whenever both $p$ and $q$ are not constant, i.e. when $n\geq 1$ and $m\geq 1$, we cannot evaluate the limit directly since both $p$ and $q$ have terms that go to infinity and/or minus infinity as $x$ approaches infinity ($a_nx^n$ for $p$ and $b_mx^m$ for $q$). So how does the function $\frac{p(x)}{q(x)}$ behave for large values of $x$? Notice that if $x$ is large enough the term $a_nx^n$ will be much larger (in absolute value) than the other terms $a_{n-1}x^{n-1}+...+a_0$ of $p$. Similarly, the term $b_mx^m$ will dominate the other terms $b_{m-1}x^{m-1}+...+b_0$ of $q$. So for large values of $x$ we have

$$
 \frac{p(x)}{q(x)}=\frac{a_nx^n+a_{n-1}x^{n-1}+...+a_0}{b_mx^m+b_{m-1}x^{m-1}+...+b_0}\approx \frac{a_nx^n}{b_mx^m}=\frac{a_n}{b_m}x^{n-m}
$$

It now depends on whether $n-m\leq  0$ or $n-m> 0$ whether the limit $\lim\limits_{x\rightarrow \infty}\frac{a_n}{b_m}x^{n-m}$ on whether this limit exists or not, but at least, it gives us an idea of how to compute this limit. In fact, we can make the computation a bit more rigorous. Suppose, for now, that $n< m$. That means that $x^m$ is the dominant term in the fraction. In that case we divide both parts of the fraction by $x^m$ to write

$$
 \frac{p(x)}{q(x)}=\frac{a_nx^n+a_{n-1}x^{n-1}+...+a_0}{b_mx^m+b_{m-1}x^{m-1}+...+b_0}=\frac{\frac{a_n}{x^{m-n}}+\frac{a_{n-1}}{x^{m-n-1}}+...+\frac{a_0}{x^m}}{b_m+\frac{b_{m-1}}{x}+...+\frac{b_0}{x^m}}
$$

Since $n< m$, we can evaluate now evaluate the limit by using {prf:ref}`Theorem:LimitAtInfinity:Standardlimits`and {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules` to obtain

$$
 \lim\limits_{x\rightarrow \infty}\frac{p(x)}{q(x)}=\lim\limits_{x\rightarrow \infty}\frac{\frac{a_n}{x^{m-n}}+\frac{a_{n-1}}{x^{m-n+1}}+...+\frac{a_0}{x^m}}{b_m+\frac{b_{m-1}}{x}+...+\frac{b_0}{x^m}}=\frac{0+0+...+0}{b_m+0+...+0}=0
$$

This technique also works when $n=m$, in which case the limit is $\frac{a_n}{b_m}$, or when $n>m$, in which case the limit does not exist. This technique is known as **division by the dominant term**. It also works when $p$ and $q$ are not polynomials, but contain other powers of $x$ like $\sqrt[3]{x}$ or $\sqrt{x^2+x}$. In these cases it is sometimes a bit harder to see what the dominant term is. For instance, in the function $f(x)=\dfrac{x^2+1}{\sqrt{x^3+1}}$ the dominant power is **not** $x^3$, as this one is inside a square root. Indeed, for large values of $x$ we have $\sqrt{x^3+1}\approx \sqrt{x^3}=x^{\frac{3}{2}}$. As such, the dominant term is $x^2$ in this case.

::::::{prf:example} Division by dominant term
:label: Ex:LimitAtInfinity:Dominant

Suppose that we want to evaluate $\lim\limits_{x\rightarrow \infty}\dfrac{2x+\sqrt{x}-x^3}{3x^3+x^2}$. The highest power of $x$ is $x^3$, so that will be the dominant term. We evaluate the limit by dividing both parts of the fraction by this dominant term. This gives

$$
 \lim\limits_{x\rightarrow \infty}\dfrac{2x+\sqrt{x}-x^3}{3x^3+x^2}=\lim\limits_{x\rightarrow \infty}\dfrac{\frac{2}{x^2}+\frac{1}{x^{\frac{5}{2}}}-1}{3+\frac{1}{x}}
$$

We can now use {prf:ref}`Theorem:LimitAtInfinity:Standardlimits`and {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules` to obtain

$$
 \lim\limits_{x\rightarrow \infty}\dfrac{2x+\sqrt{x}-x^3}{3x^3+x^2}=\lim\limits_{x\rightarrow \infty}\dfrac{\frac{2}{x^2}+\frac{1}{x^{\frac{5}{2}}}-1}{3+\frac{1}{x}}=\dfrac{0+0-1}{3+0}=-\frac{1}{3}
$$
::::::


Nu voorbeeld met wortels. Daarna worteltruc. Nog een warning maken onderaan 3.7.1 dat tabellen niet goed werken, zie $\cos(n\pi)$.

(Subsec:LimitinfPrecise)=

## Precise definition of limits at infinity