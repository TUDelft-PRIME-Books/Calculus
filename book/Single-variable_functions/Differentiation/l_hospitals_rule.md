(Section:lHospital)=

# l'Hospital's rule

(Subsec:lHospitalintro)=

## Introduction

Suppose we want to evaluate the limit

$$
 \lim_{x\rightarrow 1}\frac{x^2-x}{x^2-1}.
$$

Both the numerator and the denominator of the fraction approach $0$ as $x$ approaches $1$, so we cannot simply plug in $x=1$. In {numref}`Section:LimitPoint` we learned that limits like this one can be evaluated by factoring the numerator and the denominator and cancelling out the common factor. In this case, we obtain

$$
 \lim_{x\rightarrow 1}\frac{x^2-x}{x^2-1}=\lim_{x\rightarrow 1}\frac{x(x-1)}{(x-1)(x+1)}=\lim_{x\rightarrow 1}\frac{x}{x+1}.
$$

The remaining limit can be evaluated directly, since both the numerator and denominator are no longer $0$ at $x=1$, so we obtain

$$
 \lim_{x\rightarrow 1}\frac{x^2-x}{x^2-1}=\lim_{x\rightarrow 1}\frac{x}{x+1}\frac{1}{1+1}=\frac{1}{2}.
$$

Now suppose we want to evaluate the limit

$$
 \lim_{x\rightarrow 1}\frac{\ln(x)}{1-\sqrt{x}}.
$$

[^FootnoteNewTech]: Unfortunately, not every time we encounter a limit we cannot evaluate, we will be able to come up with a new technique to evaluate it.

Again, both the numerator and the denominator are $0$ in $x=1$. However, there is no straightforward way to continue here. Indeed, there is no common factor to cancel and all other techniques from {numref}`Section:LimitPoint` do not seem to help either, so we seem to be stuck. That means that it is time for a new technique[^FootnoteNewTech]. To motivate this technique, we take a look at the graphs of the functions $f(x)=\dfrac{\ln(x)}{1-\sqrt{x}}$, $g(x)=\ln(x)$ and $h(x)=1-\sqrt{x}$ in {numref}`Fig:lHospital:Motivation`. Now instead of considering the functions $g$ and $h$, we consider their linearisations around $x=1$, which we will denote by $L_g$ and $L_h$ respectively. These linearisations are given by

$$
 L_g(x)=g(1)+g'(1)(x-1)=(x-1),\qquad L_h(x)=h(1)+h'(1)(x-1)=-\frac{1}{2}(x-1).
$$

If we switch to the graphs of the linearisations in {numref}`Fig:lHospital:Motivation` using the button, we see that close to $x=1$ nothing has changed: the functions $g$ and $h$ behave almost the same as $L_g$ and $L_h$ for $x$ close to $1$ (which is of course the point of a using a linearisation). This suggests that we can evaluate the limit by using the linearisations and that we would obtain

$$
 \lim_{x\rightarrow 1}\frac{\ln(x)}{1-\sqrt{x}}=\lim_{x\rightarrow 1}\frac{g(x)}{h(x)}=\lim_{x\rightarrow 1}\frac{L_g(x)}{L_h(x)}.
$$

Of course, we have only motivated this final step and we have not actually proven that this is allowed (it is, which is the whole point of this section). The final limit **can** be evaluated directly and we obtain

$$
 \lim_{x\rightarrow 1}\frac{\ln(x)}{1-\sqrt{x}}=\lim_{x\rightarrow 1}\frac{L_g(x)}{L_h(x)}=\lim_{x\rightarrow 1}\frac{x-1}{-\frac{1}{2}(x-1)}=\lim_{x\rightarrow 1}\frac{1}{-\frac{1}{2}}=-2.
$$

[^Footnotespelling]: We use the spelling of l'Hospital's name that he himself used. Since then, the spelling rules in French have changed. In modern French, the correct spelling would be l'Hôspital, which is sometimes used for both the marquis and the rule. 

Note that in the final step, we obtained the limit $\displaystyle \lim_{x\rightarrow 1}\frac{1}{-\frac{1}{2}}$. By how the linearisation was constructed, this final limit is $\displaystyle \frac{g'(1)}{h'(1)}$. This suggest that in order to evaluate the limit $\displaystyle \lim_{x\rightarrow 1}\frac{g(x)}{h(x)}$, we can, instead, evaluate $\displaystyle \lim_{x\rightarrow 1}\frac{g'(x)}{h'(x)}$. This result is known as **l'Hospital's rule** and is a very important technique for evaluating limits.

L'Hospital's rule is named after the French mathematician [Guillaume François Antoine, Marquis de l'Hospital (1661-1704)](https://en.wikipedia.org/wiki/Guillaume_de_l%27H%C3%B4pital)[^Footnotespelling], who first published the result. However, he did not come up with it himself. That honour goes to the Swiss mathematician [Johan Bernoulli (1667-1748)](https://en.wikipedia.org/wiki/Johann_Bernoulli).

:::{figure} Images/Fig-lHospital-Motivation.png
:name: Fig:lHospital:Motivation

The graphs of the functions $f$, $g$ and $h$ and the graphs of the linearisations $L_g$ and $L_h$. You can toggle between the graphs of $g$ and $h$ and their linearisations to see how they behave close to $x=1$.
:::

:::{todo}
Make an applet showing the graphs of the functions $f$, $g$ and $h$ with label Fig:lHospital:Motivation. Make a toggle, that switches $g$ and $h$ to their linearisations around $1$ (with $g$ and $h$ shown faded out in the background)
:::

If you ask a student what their favorite rule is to evaluate limits, most students will answer that it is l'Hospital's rule. There is a good reason for this: it is a rule that is applicable to various different limits and the execution is often straightforward. However, l'Hospital's rule is not the catch-all rule that many students seem to think it is. So usually, when we discuss a new technique, we mainly focus on what you **can** do with it. Here, we will also put a lot of focus on what limits **cannot** be evaluated with this technique.

## Indeterminate forms and l'Hospital's rule

There are various reasons why it takes effort to evaluate a limit. For instance, we might we dealing with a fraction where both the numerator and denominator approach $0$, or one where they both approach $\infty$. In order to better help us distinguish between these general categories of limits, we will give them names. 

::::::{prf:definition}
:label: Def:lHospital:Indeterminateform
A limit of the form

$$
 \lim_{x\rightarrow a}\frac{f(x)}{g(x)}
$$

with $\displaystyle\lim_{x\rightarrow a}f(x)=\lim_{x\rightarrow a}g(x)=0$ is called an **indeterminate form of type** $\dfrac{0}{0}$. 

A limit of the form 

$$
 \lim_{x\rightarrow a}\frac{f(x)}{g(x)}
$$

with $\displaystyle\lim_{x\rightarrow a}f(x)=\infty$ and $\displaystyle\lim_{x\rightarrow a}g(x)=\infty$ is called an **indeterminate form of type** $\dfrac{\infty}{\infty}$. In a similar way, we can define an **indeterminate form of type** $\dfrac{-\infty}{\infty}$, $\dfrac{\infty}{-\infty}$ or $\dfrac{-\infty}{-\infty}$.

A limit of the form 

$$
 \lim_{x\rightarrow a}f(x)g(x)
$$

with $\displaystyle\lim_{x\rightarrow a}f(x)=0$ and $\displaystyle\lim_{x\rightarrow a}g(x)=-\infty$ is called an **indeterminate form of type** $0\cdot \infty$.

A limit of the form 

$$
 \lim_{x\rightarrow a}f(x)-g(x)
$$

with $\displaystyle\lim_{x\rightarrow a}f(x)=\infty$ and $\displaystyle\lim_{x\rightarrow a}g(x)=\infty$ is called an **indeterminate form of type** $\infty-\infty$. 

A limit of the form 

$$
 \lim_{x\rightarrow a}\left(f(x)\right)^{g(x)}
$$

with $\displaystyle\lim_{x\rightarrow a}f(x)=1$ and $\displaystyle\lim_{x\rightarrow a}g(x)=\infty$ is called an **indeterminate form of type** $1^\infty$. In a similar way, we can define an **indeterminate form** of type $1^{-\infty}$.

A limit of the form 

$$
 \lim_{x\rightarrow a}\left(f(x)\right)^{g(x)}
$$

with $\displaystyle\lim_{x\rightarrow a}f(x)=\infty$ and $\displaystyle\lim_{x\rightarrow a}g(x)=0$ is called an **indeterminate form of type** $\infty^0$.

A limit of the form 

$$
 \lim_{x\rightarrow a}\left(f(x)\right)^{g(x)}
$$

with $\displaystyle\lim_{x\rightarrow a}f(x)=0$ and $\displaystyle\lim_{x\rightarrow a}g(x)=0$ is called an **indeterminate form of type** $0^0$.

This terminology also applies to left limits, right limits and limits at plus or minus infinity.
::::::

In general, an indeterminate form is a type of limit involving a combination of two or more functions (such as a difference or a quotient) where knowing the limits of the separate functions is not enough to find the limit of the combination. For these limits, techniques like cancelling the common factor, the square root trick and, of course, l'Hospital's rule can sometimes be used to turn the limit into something that can be evaluated directly. In this section, we will consider examples of many of these indeterminate forms. Many, but definitely not all, can be solve using l'Hospital's rule.

So without further ado, let us state this rule.


::::::{prf:theorem} l'Hospital's rule for limits at a point
:label: Thm:lHospital:lHospital
Let $I$ be an open interval containing a point $a$. Suppose that the functions $f$ and $g$ are differentiable on $I$, except possibly at $a$, and that $g'(x)\neq0$ for all $x$ in $I$ with $x\neq a$. Suppose that 

$$
 \lim_{x\rightarrow a}\frac{f'(x)}{g'(x)}=L
$$

for either a real number $L$, or for $L=\infty$, or for $L=-\infty$. Finally, suppose that either

$$
 \lim_{x\rightarrow a}f(x)=\lim_{x\rightarrow a}g(x)=0
$$

or

$$
 \lim_{x\rightarrow a}|f(x)|=\lim_{x\rightarrow a}|g(x)|=\infty.
$$

Then we obtain

$$
 \lim_{x\rightarrow a}\frac{f(x)}{g(x)}=\lim_{x\rightarrow a}\frac{f'(x)}{g'(x)}=L.
$$

The result also holds when replacing all occurrences of $\displaystyle \lim_{x\rightarrow a}$ by the left limit $\displaystyle \lim_{x\rightarrow a^-}$, or by replacing all of them by the right limit $\displaystyle \lim_{x\rightarrow a^+}$. For the left limits, $I$ can also be an open interval of the form $(z,a)$, while for the right limits, $I$ can also be an open interval of the form $(a,b)$.
::::::

[^FootnoteShorthand]: This notation is a shorthand for the four types $\dfrac{\infty}{\infty}$, $\dfrac{-\infty}{\infty}$, $\dfrac{\infty}{-\infty}$ and $\dfrac{-\infty}{-\infty}$.

:::{note}
The conditions in the theorem state that l'Hospital's rule can be applied to indeterminate forms of type either $\dfrac{0}{0}$ or $\dfrac{\pm\infty}{\pm\infty}$[^FootnoteShorthand]. Later we will see how we can apply it to indeterminate forms of other types. 
:::

We postpone the proof until we have also formulated the version of l'Hospital's rule for limits at infinity.

We first consider a few examples where l'Hospital's rule can be applied directly.

::::::{prf:example} 
:label: Ex:lHospital:lHospital1
Consider the limit 

$$
 \displaystyle\lim_{x\rightarrow 0}\frac{\sin(x)}{x}.
$$

Since both $\displaystyle\lim_{x\rightarrow 0}\sin(x)=0$ and $\displaystyle\lim_{x\rightarrow 0}x=0$, this limit is of the indeterminate form $\dfrac{0}{0}$. In addition, the functions $f(x)=\sin(x)$ and $g(x)=x$ are differentiable and the derivative of $g$ is never $0$. In order to see whether l'Hospital's rule can be used, we compute

$$
 \lim_{x\rightarrow 0}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow 0}\frac{\cos(x)}{x}=\frac{1}{1}=1.
$$

Since the limit $\displaystyle \lim_{x\rightarrow 0}\frac{f'(x)}{g'(x)}$ exists, we have checked all conditions to use l'Hospital's rule. Then we obtain

$$
 \lim_{x\rightarrow 0}\frac{\sin(x)}{x}=\lim_{x\rightarrow 0}\frac{f(x)}{g(x)}=\lim_{x\rightarrow 0}\frac{f'(x)}{g'(x)}=1.
$$

This limit is a rather well-known limit, and it is sometimes even called a standard limit. We already encountered it in the proof of {prf:ref}`Thm:Differentiability:Standard1`. However, we could not have used l'Hospital's rule in that proof, since there, we were showing that the cosine is the derivative of the sine. So it would have been a circular reasoning to already use this in the computation.
::::::

::::::{prf:example} 
:label: Ex:lHospital:lHospital2
Let us return to the limit 

$$
 \displaystyle \lim_{x\rightarrow 1}\frac{\ln(x)}{1-\sqrt{x}}
$$

from {numref}`Subsec:lHospitalintro`. Writing $f(x)=\ln(x)$ and $g(x)=1-\sqrt{x}$, we have $\displaystyle\lim_{x\rightarrow 1}f(x)=\displaystyle\lim_{x\rightarrow 1}g(x)=0$, so we are again dealing with an indeterminate form of type $\dfrac{0}{0}$. In addition, the functions $f$ and $g$ are both differentiable around $1$ and $g'(x)\neq 0$ for $x$ close to $1$. Then, we check that the limit of the quotient of the derivatives exists by evaluating

$$
 \lim_{x\rightarrow 1}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow 1}\frac{\frac{1}{x}}{-\frac{1}{2\sqrt{x}}}=\lim_{x\rightarrow 1}\frac{-2\sqrt{x}}{x}=\lim_{x\rightarrow 1}\frac{-2}{\sqrt{x}}=-2.
$$

Since this limit exists, we can use l'Hospital's rule and we obtain

$$
 \lim_{x\rightarrow 1}\frac{\ln(x)}{1-\sqrt{x}}=\lim_{x\rightarrow 1}\frac{f(x)}{g(x)}=\lim_{x\rightarrow 1}\frac{f'(x)}{g'(x)}=-2.
$$

This is also the result we obtained in {numref}`Subsec:lHospitalintro`.

::::::

Sometimes, l'Hospital's rule needs to be used several times in a row to obtain the correct solution.

::::::{prf:example} 
:label: Ex:lHospital:lHospital3
Consider the limit

$$
 \displaystyle \lim_{x\rightarrow 0}\frac{\cos(x)-1}{x^2}.
$$

Writing $f(x)=\cos(x)-1$ and $g(x)=x^2$, we have $\displaystyle\lim_{x\rightarrow 0}f(x)=\displaystyle\lim_{x\rightarrow 0}g(x)=0$, so we are again dealing with an indeterminate form of type $\dfrac{0}{0}$. In addition, the functions $f$ and $g$ are both differentiable around $0$ and $g'(x)\neq 0$ for $x\neq 0$ close to $0$. Finally, we check that the limit of the quotient of the derivatives exists by evaluating

$$
 \lim_{x\rightarrow 0}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow 0}\frac{-\sin(x)}{2x}.
$$

[^FootnotePrevEx]: This limit is a constant multiple of the one in {prf:ref}`Ex:lHospital:lHospital1`, so, actually, we do know its value. For the sake of the argument, we now pretend that we do not know this result.

However, we now run into an issue, since this again an indeterminate form of type $\dfrac{0}{0}$, so we do not know if the limit exists[^FootnotePrevEx]. For this, we will again use l'Hospital's rule. Since $f'$ and $g'$ are differentiable, we can check the limit of the quotient of their derivatives by evaluating

$$
 \lim_{x\rightarrow 0}\frac{f''(x)}{g''(x)}=\lim_{x\rightarrow 0}\frac{-\cos(x)}{2}=-\frac{1}{2}.
$$

Since this limit exists, we can use l'Hospital's rule and we obtain

$$
 \lim_{x\rightarrow 0}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow 0}\frac{f''(x)}{g''(x)}=-\frac{1}{2}.
$$

Now that we know that $\displaystyle \lim_{x\rightarrow 0}\frac{f'(x)}{g'(x)}$ exists, we can apply l'Hospital's rule to the original limit and we find

$$
 \lim_{x\rightarrow 0}\frac{\cos(x)-1}{x^2}=\lim_{x\rightarrow 0}\frac{f(x)}{g(x)}=\lim_{x\rightarrow 0}\frac{f'(x)}{g'(x)}=-\frac{1}{2}.
$$



::::::

L'Hospital's rule can also be used to evaluate limits at plus or minus infinity.

::::::{prf:theorem} l'Hospital's rule for limits at $\pm\infty$
:label: Thm:lHospital:lHospitalinf
Consider the interval $I=(a,\infty)$. Suppose that the functions $f$ and $g$ are differentiable on $I$, and that $g'(x)\neq0$ for all $x$ in $I$. Suppose that 

$$
 \lim_{x\rightarrow \infty}\frac{f'(x)}{g'(x)}=L
$$

for either a real number $L$, or for $L=\infty$, or for $L=-\infty$. Finally, suppose that either

$$
 \lim_{x\rightarrow \infty}f(x)=\lim_{x\rightarrow \infty}g(x)=0
$$

or

$$
 \lim_{x\rightarrow \infty}|f(x)|=\lim_{x\rightarrow \infty}|g(x)|=\infty.
$$

Then we obtain

$$
 \lim_{x\rightarrow \infty}\frac{f(x)}{g(x)}=\lim_{x\rightarrow \infty}\frac{f'(x)}{g'(x)}=L.
$$

The result also holds when replacing all occurrences of $\displaystyle \lim_{x\rightarrow \infty}$ by $\displaystyle \lim_{x\rightarrow -\infty}$ with $I=(-\infty,a)$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:lHospital:lHospital` and {prf:ref}`Thm:lHospital:lHospitalinf`
:class: tudproof, dropdown
We prove both versions of l'Hospital's rule in one go. However, this proof is rather hard and technical, so feel free to skip the proof.

First, we consider either one of the cases

$$
 \lim_{x\rightarrow a^-}\frac{f(x)}{g(x)},\qquad\text{or}\qquad \lim_{x\rightarrow \infty}\frac{f(x)}{g(x)}.
$$

To handle these cases together, we write $c=a$ or $c=\infty$, depending on the case we are in and we write $\displaystyle\lim_{x\rightarrow c}$ whenever we mean $\displaystyle\lim_{x\rightarrow a^-}$ or $\displaystyle\lim_{x\rightarrow \infty}$. We can write $I=(b,c)$. 

First we show that we can make $I$ smaller so that $g$ is never $0$ on $I$. If there were two points $x\neq y$ in $I$ with $g(x)=g(y)=0$, then by {prf:ref}`Thm:MinMax:Rolle`, there would be $z$ in $I$ with $g'(z)=0$. This is not possible, since we assumed that $g'\neq 0$ on $I$. As such, there is at most one $x$ in $I$ with $g(x)=0$. By making $I$ smaller, if necessary, we can ensure that $g$ is never $0$ on $I$. With the same reasoning, we also see that we have $g(x)\neq g(y)$ whenever $x\neq y$ are in $I$.

The infimum of a set $S$ is its largest lower bound. That is $m=\inf(S)$ precisely when $m\leq s$ for all $s$ in $S$ and $m\geq n$ for all $n$ which have $n\leq s$ for all $s$ in $S$. Similarly, the supremum of $S$ is the smallest upper bound. That is $M=\sup(S)$ precisely when $M\geq s$ for all $s$ in $S$ and $M\leq N$ for all $N$ which have $N\geq s$ for all $s$ in $S$. The completeness of the real numbers states that each bounded subset of the real numbers has an infimum and a supremum. In this proof, we make the convention that $\inf(S)=-\infty$ and $\sup(S)=\infty$ whenever $S$ does not have a lower respectively upper bound. 

For each $x$ in $I$, we can now let 

$$
 m(x)=\inf\left\{\frac{f'(t)}{g'(t)}\middle|t\in[x,c)\right\},\qquad M(x)=\sup\left\{\frac{f'(t)}{g'(t)}\middle|t\in[x,c)\right\}.
$$

These expressions $m(x)$ and $M(x)$ can either be real numbers or $-\infty$ or $\infty$. The point of introducing these quantities is that

$$
 \lim_{x\rightarrow c}m(x)=\lim_{x\rightarrow c}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow c}M(x).
$$

This can be seen as follows. Since $m$ is a nondecreasing function and $M$ is a nonincreasing function, the limits $\displaystyle \lim_{x\rightarrow c}m(x)$ and $\displaystyle \lim_{x\rightarrow c}M(x)$ must either exist or be equal to $\pm\infty$. For any $x$ we have 

$$
 m(x)\leq \frac{f'(x)}{g'(x)}\leq M(x),
$$

which gives

$$
 \lim_{x\rightarrow c}m(x)\leq \lim_{x\rightarrow c}\frac{f'(x)}{g'(x)}\leq \lim_{x\rightarrow c}M(x).
$$

Let $\varepsilon>0$ be given and write $\displaystyle L=\lim_{x\rightarrow c}\frac{f'(x)}{g'(x)}$. Let $J$ be an interval of the form $(d,c)$ within $I$ such that for all $y$ in $J$ we have

$$
 \left|\frac{f'(y)}{g'(y)}-L\right|<\frac{\varepsilon}{2}.
$$

Now let $x$ in $J$. By definition of the supremum, we can find $t$ in $[x,c)$ with $\dfrac{f'(t)}{g'(t)}+\dfrac{\epsilon}{2}\geq M(x)$. Then, since $t$ must also be in $J$ as $J$ is an interval, we obtain

$$
 M(x)\leq \dfrac{f'(t)}{g'(t)}+\dfrac{\varepsilon}{2}\leq L+\dfrac{\varepsilon}{2}+\dfrac{\varepsilon}{2}=L+\varepsilon.
$$

Since this holds for all $\varepsilon>0$, we find that 

$$
 \lim_{x\rightarrow c}M(x)\leq L,
$$

which means that

$$
 \lim_{x\rightarrow c}M(x)=L.
$$

Similarly, we find

$$
 \lim_{x\rightarrow c}m(x)=L.
$$

Let $x$ and $y$ in $I$ with $x<y$. Recall that $g(x)\neq g(y)$. By {prf:ref}`Thm:MinMax:MVTCauchy`, we can find $z$ in between $x$ and $y$ with

$$
 \frac{f(x)-f(y)}{g(x)-g(y)}=\frac{f'(z)}{g'(z)}.
$$

Since $I$ is an interval and $x<y$, we have $z$ in $I$ and $z$ in $(x,c)$. By definition of $m(x)$ and $M(x)$, we find that

$$
 m(x)\leq \frac{f'(z)}{g'(z)}=\frac{f(x)-f(y)}{g(x)-g(y)}
$$

and

$$
 M(x)\geq \frac{f'(z)}{g'(z)}=\frac{f(x)-f(y)}{g(x)-g(y)}.
$$

Now we need to make a distinction between the cases where we are dealing with an indeterminate form of type $\dfrac{0}{0}$ of one of type $\dfrac{\pm\infty}{\pm\infty}$.

**Case 1:** $\displaystyle \lim_{x\rightarrow c}f(x)=\lim_{x\rightarrow c} g(x)=0$.

Let $x$ in $I$ be given. Then for any $y$ in $(x,c)$ we have

$$
 m(x)\leq \frac{f(x)-f(y)}{g(x)-g(y)}=\frac{\frac{f(x)}{g(x)}-\frac{f(y)}{g(x)}}{1-\frac{g(y)}{g(x)}}\leq M(x).
$$

Now we take the limit $y\rightarrow c$. Then, since $\displaystyle \lim_{y\rightarrow c}f(y)=\lim_{y\rightarrow c} g(y)=0$, we obtain

$$
 m(x)\leq \lim_{y\rightarrow c}\frac{\frac{f(x)}{g(x)}-\frac{f(y)}{g(x)}}{1-\frac{g(y)}{g(x)}}=\frac{f(x)}{g(x)}
$$

and

$$
 M(x)\geq \lim_{y\rightarrow c}\frac{\frac{f(x)}{g(x)}-\frac{f(y)}{g(x)}}{1-\frac{g(y)}{g(x)}}=\frac{f(x)}{g(x)}.
$$

We conclude that

$$
 m(x)\leq \frac{f(x)}{g(x)}\leq M(x).
$$

Since $\displaystyle \lim_{x\rightarrow c}m(x)=\lim_{x\rightarrow c}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow c}M(x)$, the squeeze theorem ({prf:ref}`Theorem:LimitAtPoint:Squeezetheorem` or {prf:ref}`Theorem:LimitAtInfinity:Squeezetheorem`) now yields that

$$
 \lim_{x\rightarrow c}\frac{f(x)}{g(x)}=\lim_{x\rightarrow c}\frac{f'(x)}{g'(x)},
$$

as desired.

**Case 2:** $\displaystyle \lim_{x\rightarrow c}|f(x)|=\lim_{x\rightarrow c} |g(x)|=\infty$.

Let $x$ in $I$ be given. Then for any $y$ in $(x,c)$ we have

$$
 m(x)\leq \frac{f(x)-f(y)}{g(x)-g(y)}=\frac{\frac{f(y)}{g(y)}-\frac{f(x)}{g(y)}}{1-\frac{g(x)}{g(y)}}\leq M(x).
$$

We want to take the limit $y\rightarrow c$. However, we have to be careful as we do not know yet that the limit $\displaystyle \lim_{y\rightarrow c}\frac{f(y)}{g(y)}$ exists. For this we look at the so-called [limit superior and limit inferior](https://en.wikipedia.org/wiki/Limit_inferior_and_limit_superior#Real-valued_functions). The limit superior and limit inferior of a function at a point always exists (or is plus or minus infinity) and the limit at the point exists whenever the limit superior and limit inferior coincide. Since $\displaystyle \lim_{y\rightarrow c} \frac{f(x)}{g(y)}=\lim_{y\rightarrow c} \frac{g(x)}{g(y)}=0$, we can take the limit inferior as $y\rightarrow c$ of the equation above to obtain

$$
 m(x)\leq \liminf_{y\rightarrow c}\frac{\frac{f(y)}{g(y)}-\frac{f(x)}{g(y)}}{1-\frac{g(x)}{g(y)}}=\liminf_{y\rightarrow c}\frac{f(y)}{g(y)}.
$$

Similarly, we obtain by using the limit superior

$$
 \limsup_{y\rightarrow c}\frac{f(y)}{g(y)}\leq M(x).
$$

Hence, we find that

$$
 m(x)\leq \liminf_{y\rightarrow c}\frac{f(y)}{g(y)}\leq \limsup_{y\rightarrow c}\frac{f(y)}{g(y)}\leq M(x),
$$

since the limit inferior is always less than or equal to the limit superior.

Since $\displaystyle \lim_{x\rightarrow c}m(x)=\lim_{x\rightarrow c}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow c}M(x)$, the squeeze theorem ({prf:ref}`Theorem:LimitAtPoint:Squeezetheorem` or {prf:ref}`Theorem:LimitAtInfinity:Squeezetheorem`) now yields that

$$
 \liminf_{y\rightarrow c}\frac{f(y)}{g(y)}=\limsup_{y\rightarrow c}\frac{f(y)}{g(y)}=\lim_{x\rightarrow c}\frac{f'(x)}{g'(x)}.
$$

Since the limit inferior and and limit superior are equal, the limit exists and we obtain

$$
 \lim_{x\rightarrow c}\frac{f(x)}{g(x)}=\lim_{x\rightarrow c}\frac{f'(x)}{g'(x)},
$$

as desired.

Now we are dealing with a right limit or limit at minus infinity, we can make the substitution $t=-x$ to turn it into a left limit respectively limit at plus infinity and use the results that we have established previously. Finally, for a two-sided limit at a point, we use the results for the left- and right-sided limits to establish that

$$
 \lim_{x\rightarrow a^-}\frac{f(x)}{g(x)}=\lim_{x\rightarrow a^-}\frac{f'(x)}{g'(x)}
$$

and

$$
 \lim_{x\rightarrow a^+}\frac{f(x)}{g(x)}=\lim_{x\rightarrow a^+}\frac{f'(x)}{g'(x)}.
$$

Since $\displaystyle \lim_{x\rightarrow a}\frac{f'(x)}{g'(x)}$ exists, its left- and right-limits are equal. So the original left- and right-limits are equal as well and we obtain

$$
 \lim_{x\rightarrow a}\frac{f(x)}{g(x)}=\lim_{x\rightarrow a}\frac{f'(x)}{g'(x)}.
$$

:::

With this version of l'Hospital's rule, we can now, finally, establish the growth rates that we discussed in {prf:ref}`Theorem:LimitAtInfinity:Standardgrowthrates`.

:::{admonition} Proof of {prf:ref}`Theorem:LimitAtInfinity:Standardgrowthrates`
:class: tudproof, dropdown
Let $f(x)=e^{ax}$ and $g(x)=x^r$ for some $a>0$ and $r>0$. Then we consider the limit

$$
 \lim_{x\rightarrow\infty}\frac{f(x)}{g(x)}.
$$

Since $\displaystyle \lim_{x\rightarrow\infty}f(x)= \lim_{x\rightarrow\infty}g(x)=\infty$, we are dealing with an indeterminate form of type $\dfrac{\infty}{\infty}$. In addition, the functions $f$ and $g$ are differentiable and have $g'(x)\neq 0$ for $x>0$. This suggests that we can use l'Hospital's rule. For this, we evaluate

$$
 \lim_{x\rightarrow\infty}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow\infty}\frac{ae^{ax}}{rx^{r-1}}.
$$

This limit is $\infty$ whenever $r-1\leq 0$, in which case we are done. Otherwise, we are still dealing with an indeterminate form of type $\dfrac{\infty}{\infty}$ and we can use l'Hospital's rule again to obtain

$$
 \lim_{x\rightarrow\infty}\frac{f''(x)}{g''(x)}=\lim_{x\rightarrow\infty}\frac{a^2e^{ax}}{r(r-1)x^{r-2}}.
$$

This time, the limit is $\infty$ whenever $r-2\leq 0$, while it is an indeterminate form of type $\dfrac{\infty}{\infty}$ otherwise. As such, we let $n$ be the smallest integer with $n\geq r$ (that is, we round $r$ up to $n$). Then each of the limits

$$
 \lim_{x\rightarrow\infty}\frac{f^{(k)}(x)}{g^{(k)}(x)}=\lim_{x\rightarrow\infty}\frac{a^ke^{ax}}{r(r-1)\ldots(r-k+1)x^{r-k}}
$$

for $0\leq k<n$ is an indeterminate form of type $\dfrac{\infty}{\infty}$. In addition,

$$
 \lim_{x\rightarrow\infty}\frac{f^{(n)}(x)}{g^{(n)}(x)}=\lim_{x\rightarrow\infty}\frac{a^ne^{ax}}{r(r-1)\ldots(r-n+1)x^{r-n}}=\infty,
$$

since $r-n\leq 0$. Then by applying l'Hospital's rule $n$ times, we find that

$$
 \lim_{x\rightarrow\infty}\frac{f(x)}{g(x)}=\lim_{x\rightarrow\infty}\frac{f'(x)}{g'(x)}=\ldots=\lim_{x\rightarrow\infty}\frac{f^{(n)}(x)}{g^{(n)}(x)}=\infty.
$$

As such, $f$ grows faster than $g$.

Now consider the function $h(x)=\ln(bx)$ for some $b>0$. Then we have $\displaystyle\lim_{x\rightarrow\infty}h(x)=\infty$, so the limit

$$
 \lim_{x\rightarrow\infty}\frac{g(x)}{h(x)}
$$

is an indeterminate form of type $\dfrac{\infty}{\infty}$. In addition, the functions $g$ and $h$ are both differentiable and we have $h'(x)\neq 0$ for $x>0$. This suggests that we can use l'Hospital's rule. For this we evaluate

$$
 \lim_{x\rightarrow\infty}\frac{g'(x)}{h'(x)}=\lim_{x\rightarrow\infty}\frac{rx^{r-1}}{\frac{b}{bx}}=\lim_{x\rightarrow\infty}rx^r=\infty.
$$

We conclude that $g$ grows faster than $h$.
:::

Let us now see how the version of l'Hospital's rule at infinity is used in practice.

::::::{prf:example} 
:label: Ex:lHospital:lHospitalinf
Consider the limit

$$
 \displaystyle \lim_{x\rightarrow \infty}\frac{\ln\left(x^3+1\right)}{\ln\left(x^2+1\right)}.
$$

Writing $f(x)=\ln\left(x^3+1\right)$ and $g(x)=\ln\left(x^2+1\right)$, we have $\displaystyle\lim_{x\rightarrow \infty}f(x)=\displaystyle\lim_{x\rightarrow \infty}g(x)=\infty$, so we are again dealing with an indeterminate form of type $\dfrac{\infty}{\infty}$. In addition, the functions $f$ and $g$ are both differentiable on the interval $(0,\infty)$ and $g'(x)\neq 0$ for all $x>0$. Finally, we check that the limit of the quotient of the derivatives exists by evaluating

$$
 \lim_{x\rightarrow \infty}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow \infty}\frac{\frac{3x^2}{x^3+1}}{\frac{2x}{x^2+1}}=\lim_{x\rightarrow \infty}\frac{3x^4+3x^2}{2x^4+2x}.
$$

In order to valuate this limit, we divide by the dominant term $x^4$ to obtain

$$
 \lim_{x\rightarrow \infty}\frac{3x^4+3x^2}{2x^4+2x}=\lim_{x\rightarrow \infty}\frac{3+\frac{3}{x^2}}{2+\frac{2}{x^3}}=\frac{3}{2}.
$$

Since this limit exists, we can use l'Hospital's rule and we obtain

$$
 \lim_{x\rightarrow \infty}\frac{\ln\left(x^3+1\right)}{\ln\left(x^2+1\right)}=\lim_{x\rightarrow \infty}\frac{f(x)}{g(x)}=\lim_{x\rightarrow \infty}\frac{f'(x)}{g'(x)}=\frac{3}{2}.
$$


::::::

## When should you NOT use l'Hospital's rule?

Some people are a bit too eager when using l'Hospital's rule. They seem to think that it is a catch-all method that can be used to evaluate just about any limit. In this section we will discuss the limitations of l'Hospital's rule. We will give examples of both limits where l'Hospital's rule cannot be used, and examples of limits where it can be used, but where it does not help in evaluating the limit.

::::::{prf:example} Not the correct indeterminate form
:label: Ex:lHospital:lHospitalnoind
Consider the limit

$$
 \lim_{x\rightarrow \pi^+}\frac{\sin(x)}{1-\cos(x)}.
$$

If we were to blindly use l'Hospital's rule, we would think that we would obtain

$$
 \lim_{x\rightarrow \pi^+}\frac{\sin(x)}{1-\cos(x)}=\lim_{x\rightarrow \pi^+}\frac{\cos(x)}{\sin(x)}=\infty.\qquad\qquad \left(\textbf{INCORRECT}\right)
$$

So what is wrong here? You might think that the problem is that the problem is that the resulting limit is infinite, but there no issues there: l'Hospital's rule can be used whenever $\displaystyle\lim\limits_{x\rightarrow a^+}\frac{f'(x)}{g'(x)}=\infty$ to conclude that $\displaystyle\lim\limits_{x\rightarrow a^+}\frac{f(x)}{g(x)}=\infty$. However, for this, we do need to be dealing with the correct indeterminate form. Indeed, in order to use l'Hospital's rule $\displaystyle\lim\limits_{x\rightarrow a^+}\frac{f(x)}{g(x)}$ needs to be an indeterminate form of either type $\dfrac{0}{0}$ or $\dfrac{\pm\infty}{\pm\infty}$. Both situations do not apply here. Indeed, the limit $\displaystyle \lim_{x\rightarrow \pi^+}\frac{\sin(x)}{1-\cos(x)}$ is not even an indeterminate form, as the limit can be evaluated directly. Indeed, we obtain

$$
 \lim_{x\rightarrow \pi^+}\frac{\sin(x)}{1-\cos(x)}=\frac{\sin(\pi)}{1-\cos(\pi)}=\frac{0}{1-(-1)}=0.
$$ 

So we conclude that in order to use l'Hospital's rule, it is essential that we first check that we are dealing with an appropriate indeterminate form.
::::::

::::::{prf:example} Limit of quotients of derivatives does not exist
:label: Ex:lHospital:lHospitallimitDNE
In order to use l'Hospital's rule, it is okay if the limit of the quotients of the derivatives is either plus or minus infinity, but if the limit does not exist in any other way, l'Hospital's rule cannot be used. For this, we consider the limit

$$
 \lim_{x\rightarrow\infty}\frac{\cos(x)+x}{x}.
$$

Then we have $\displaystyle\lim\limits_{x\rightarrow \infty}\cos(x)+x=\lim\limits_{x\rightarrow \infty}x=\infty$, so the limit is an indeterminate form of type $\dfrac{\infty}{\infty}$. In addition, the functions $f(x)=\cos(x)+x$ and $g(x)=x$ are differentiable everywhere and $g'(x)$ is never $0$. This would suggest that we could use l'Hospital's rule. However, we see that the limit of the quotient of the derivatives becomes

$$
 \lim_{x\rightarrow\infty}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow\infty}\frac{-\sin(x)+1}{1}=\lim_{x\rightarrow\infty}-\sin(x)+1.
$$

Since $-\sin(x)+1$ keeps on oscillating between $0$ and $2$ as $x\rightarrow \infty$, we find that the limit $\displaystyle \lim_{x\rightarrow\infty} -\sin(x)+1$ does not exist and it is also neither plus or minus infinity. This means that l'Hospital's rule cannot be used. Moreover, the original limit does exist. Indeed, we note that for $x>0$ we have

$$
 \frac{-1+x}{x}\leq \frac{\cos(x)+x}{x}\leq \frac{1+x}{x}.
$$

Then we see that

$$
 \lim_{x\rightarrow\infty}\frac{-1+x}{x}=\lim_{x\rightarrow\infty}\frac{1+x}{x}=1.
$$

So the function $\dfrac{\cos(x)+x}{x}$ is squeezed in between two functions that approach $1$, so by {prf:ref}`Theorem:LimitAtInfinity:Squeezetheorem` we obtain

$$
 \lim_{x\rightarrow\infty}\frac{\cos(x)+x}{x}=1.
$$

This means that the condition that $\displaystyle \lim_{x\rightarrow\infty}\frac{f'(x)}{g'(x)}$ should exist or be plus or minus infinity is necessary: here the limit of the quotient of the derivatives did not exist, while the original limit does exist.

So what is the idea behind the behaviour of this function? The point is that the function $f(x)=\cos(x)+x$ shows oscillations. Dividing by $g(x)=x$ makes the amplitude of these oscillations go to $0$, which means that the limit of $\dfrac{f}{g}$ exists. However, the derivative $f'(x)=-\sin(x)$ still shows these same oscillations, while the derivative $g'(x)=1$ can no longer be used to cancel them out.
::::::

::::::{prf:example} $g'(x)=0$ for too many values of $x$
:label: Ex:lHospital:lHospitalgprime0
Consider a limit of the form

$$
 \lim_{x\rightarrow \infty}\frac{f(x)}{g(x)}.
$$

The condition that is most often forgotten to check is that we should have $g'(x)\neq 0$ for $x$ on some interval $(a,\infty)$. Still, this conditions is necessary, as can be seen by considering the limit

$$
 \lim_{x\rightarrow \infty}\frac{x+\sin(x)\cos(x)}{\left(x+\sin(x)\cos(x)\right)e^{\sin(x)}}.
$$

As the sine takes on values in between $-1$ and $1$, $e^{\sin(x)}$ takes on values between $e^{-1}$ and $e^1$. As such, we have

$$
 \lim_{x\rightarrow \infty}x+\sin(x)\cos(x)=\lim_{x\rightarrow \infty}\left(x+\sin(x)\cos(x)\right)e^{\sin(x)}=\infty,
$$ 

so we are dealing with an indeterminate form of type $\dfrac{\infty}{\infty}$. In addition, the functions $f(x)=x+\sin(x)\cos(x)$ and $g(x)=\left(x+\sin(x)\cos(x)\right)e^{\sin(x)}$ are differentiable everywhere. We evaluate

\begin{align*}
 g'(x) &= \left(1+\cos^2(x)-\sin^2(x)\right)e^{\sin(x)}+\left(x+\sin(x)\cos(x)\right)e^{\sin(x)}\cos(x) \\
 &= \left(2\cos^2(x)\right)e^{\sin(x)}+\left(x+\sin(x)\cos(x)\right)e^{\sin(x)}\cos(x),
\end{align*}

which is $0$ for each $x$ for which $\cos(x)=0$, i.e. for $x=\dfrac{\pi}{2}+k\pi$ for some integer $k$. This means that there is no interval of the form $(a,\infty)$ on which $g'(x)\neq 0$. We will check that l'Hospital's rule indeed gives the incorrect conclusion here. First, we evaluate

\begin{align*}
 \lim_{x\rightarrow \infty}\frac{f'(x)}{g'(x)} &= \lim_{x\rightarrow \infty}\frac{2\cos^2(x)}{\left(2\cos^2(x)\right)e^{\sin(x)}+\left(x+\sin(x)\cos(x)\right)e^{\sin(x)}\cos(x)} \\
 &= \lim_{x\rightarrow \infty}\frac{2\cos(x)}{2\cos(x)+\left(x+\sin(x)\cos(x)\right)}e^{-\sin(x)}.
\end{align*}

Note that for sufficiently large values of $x$ we have

$$
 \frac{-2}{x-3}e\leq\frac{2\cos(x)}{2\cos(x)+\left(x+\sin(x)\cos(x)\right)}e^{-\sin(x)}\leq \frac{2}{x-3}e.
$$

Since we can evaluate

$$
 \lim_{x\rightarrow \infty}\frac{-2}{x-3}e=\lim_{x\rightarrow \infty}\frac{2}{x-3}e=0,
$$

we obtain with {prf:ref}`Theorem:LimitAtInfinity:Squeezetheorem` that

$$
 \lim_{x\rightarrow \infty}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow \infty}\frac{2\cos(x)}{2\cos(x)+\left(x+\sin(x)\cos(x)\right)}e^{-\sin(x)}=0.
$$

This would suggest that the original limit is $0$ as well. However, this is not the case. Indeed, we have

$$
 \lim_{x\rightarrow \infty}\frac{x+\sin(x)\cos(x)}{\left(x+\sin(x)\cos(x)\right)e^{\sin(x)}}=\lim_{x\rightarrow \infty}\frac{1+\frac{\sin(x)\cos(x)}{x}}{\left(1+\frac{\sin(x)\cos(x)}{x}\right)e^{\sin(x)}}.
$$

As $x\rightarrow0$, we have $\displaystyle \lim_{x\rightarrow \infty}\frac{\sin(x)\cos(x)}{x}=\lim_{x\rightarrow \infty}\frac{\sin(x)\cos(x)}{x}e^{\sin(x)}=0$ (again using {prf:ref}`Theorem:LimitAtInfinity:Squeezetheorem`). However, the remaining limit

$$
 \lim_{x\rightarrow \infty}\frac{1+0}{\left(1+0\right)e^{\sin(x)}}=\lim_{x\rightarrow \infty}e^{-\sin(x)}
$$

does not exist, as the function keeps on oscillating between $e^{-1}$ and $e^{1}$. 

So we conclude that the limit of the quotients of the derivatives is different from the original limit. This can only mean that the condition that $g'(x)\neq 0$ on an interval of the form $(a,\infty)$ is necessary.
::::::

::::::{prf:example} l'Hospital's rule sends you in an infinite loop
:label: Ex:lHospital:lHospitalloop
Consider the limit

$$
 \lim_{x\rightarrow\infty}\frac{x}{\sqrt{1+x^2}}.
$$

Writing $f(x)=x$ and $g(x)=\sqrt{1+x^2}$, we have $\displaystyle\lim_{x\rightarrow\infty}f(x)=\lim_{x\rightarrow\infty} g(x)=\infty$, so we are dealing with an indeterminate form of type $\dfrac{\infty}{\infty}$. In addition, the functions $f$ and $g$ are both differentiable and $g'(x)\neq 0$ for $x>0$. So in order to check whether we can use l'Hospital's rule, we check whether we can evaluate the limit of the quotient of derivatives. We obtain

$$
 \lim_{x\rightarrow\infty}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow\infty}\frac{1}{\frac{2x}{2\sqrt{1+x^2}}}=\lim_{x\rightarrow\infty}\frac{\sqrt{1+x^2}}{x}.
$$

This limit is again an indeterminate form of type $\dfrac{\infty}{\infty}$. Just like in {prf:ref}`Ex:lHospital:lHospital3`, we could now try to use l'Hospital's rule again and evaluate the limit

$$
 \lim_{x\rightarrow\infty}\frac{\frac{d}{dx}[\sqrt{1+x^2}]}{\frac{d}{dx}[x]}=\lim_{x\rightarrow\infty}\frac{\frac{2x}{2\sqrt{1+x^2}}}{1}=\lim_{x\rightarrow\infty}\frac{x}{\sqrt{1+x^2}}.
$$

This is the original limit that we started with! This means that l'Hospital's rule sends us in an infinite loop that we cannot get out of. Instead, we see that we can evaluate this limit without using l'Hospital's rule. Indeed, we can divide by the dominant term $x$ and obtain

$$
 \lim_{x\rightarrow\infty}\frac{x}{\sqrt{1+x^2}}=\lim_{x\rightarrow\infty}\frac{1}{\frac{1}{x}\sqrt{1+x^2}}=\lim_{x\rightarrow\infty}\frac{1}{\sqrt{\frac{1}{x^2}+1}}=\frac{1}{\sqrt{0+1}}=1.
$$

::::::

::::::{prf:example} l'Hospital's rule gives you a new limit after each step that cannot be evaluated directly
:label: Ex:lHospital:lHospitalinfnew
As a variation on {prf:ref}`Ex:lHospital:lHospitalloop`, it can happen that l'Hospital's rule can be applied an arbitrary number of times, but each time we obtain a new limit that still cannot be evaluated directly. For instance, consider the limit

$$
 \lim_{x\rightarrow\infty}\frac{x^{\frac{1}{2}}+x^{-\frac{1}{2}}}{x^{\frac{1}{2}}-x^{-\frac{1}{2}}}.
$$

Then we see that $\displaystyle \lim_{x\rightarrow\infty}x^{\frac{1}{2}}+x^{-\frac{1}{2}}=\lim_{x\rightarrow\infty}x^{\frac{1}{2}}-x^{-\frac{1}{2}}=\infty$, so we are dealing with an indeterminate form of type $\dfrac{\infty}{\infty}$. In addition, the functions $f$ and $g$ are differentiable and $g'(x)\neq 0$ for $x>0$. This suggests that we could try to use l'Hospital's rule. We note that

$$
 \lim_{x\rightarrow\infty}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow\infty}\frac{\frac{1}{2}x^{-\frac{1}{2}}-\frac{1}{2}x^{-\frac{3}{2}}}{\frac{1}{2}x^{-\frac{1}{2}}+\frac{1}{2}x^{-\frac{3}{2}}}.
$$

This new limit is of type $\dfrac{0}{0}$ and cannot be evaluated directly. So we could try to use l'Hospital's rule again and evaluate

$$
 \lim_{x\rightarrow\infty}\frac{f''(x)}{g''(x)}=\lim_{x\rightarrow\infty}\frac{-\frac{1}{4}x^{-\frac{3}{2}}+\frac{3}{4}x^{-\frac{5}{2}}}{-\frac{1}{4}x^{-\frac{3}{2}}-\frac{3}{4}x^{-\frac{5}{2}}}.
$$

So we obtain a yet again new limit of type $\dfrac{0}{0}$. You can see that this will be the case even after applying l'Hospital's rule an arbitrary number of times. So we will never get an answer when we continue this path.

Instead, we could have evaluated this limit using the square root trick. Indeed, we have

$$
 \lim_{x\rightarrow\infty}\frac{x^{\frac{1}{2}}+x^{-\frac{1}{2}}}{x^{\frac{1}{2}}-x^{-\frac{1}{2}}}=\lim_{x\rightarrow\infty}\frac{x^{\frac{1}{2}}+x^{-\frac{1}{2}}}{x^{\frac{1}{2}}-x^{-\frac{1}{2}}}\frac{x^{\frac{1}{2}}+x^{-\frac{1}{2}}}{x^{\frac{1}{2}}+x^{-\frac{1}{2}}}=\lim_{x\rightarrow\infty}\frac{x+2+\frac{1}{x}}{x-\frac{1}{x}}.
$$

Then we can divide by the dominant term and obtain

$$
 \lim_{x\rightarrow\infty}\frac{x^{\frac{1}{2}}+x^{-\frac{1}{2}}}{x^{\frac{1}{2}}-x^{-\frac{1}{2}}}=\lim_{x\rightarrow\infty}\frac{x+2+\frac{1}{x}}{x-\frac{1}{x}}=\lim_{x\rightarrow\infty}\frac{1+\frac{2}{x}+\frac{1}{x^2}}{1-\frac{1}{x^2}}=1.
$$

::::::

We conclude that it is very important to check all the conditions of l'Hospital's rule and to keep in mind that, while l'Hospital's rule is a very strong and broadly applicable method, it is sometimes a lot easier to use other techniques like division by the dominant term or the square root trick.

## Indeterminate products and powers

It turns out that many indeterminate forms that involve products and powers, like $0\cdot\infty$ or $1^\infty$, can be rewritten in such a way that other techniques, such as l'Hospital's rule, can be used.

Consider, for instance, a limit of the form

$$
 \lim_{x\rightarrow a}f(x)g(x)
$$

with $\displaystyle \lim_{x\rightarrow a}f(x)=0$ and $\displaystyle \lim_{x\rightarrow a}g(x)=\infty$. So far, we only know how to apply l'Hospital's rule to a quotient of functions, while here, we are dealing with a product of functions. Fortunately, products and quotients are closely related. Indeed, if we write $h(x)=\frac{1}{g(x)}$, then we have

$$
 \lim_{x\rightarrow a}f(x)g(x)=\lim_{x\rightarrow a}f(x)\frac{1}{h(x)}=\lim_{x\rightarrow a}\frac{f(x)}{h(x)}.
$$

Moreover, since $\displaystyle \lim_{x\rightarrow a}g(x)=\infty$ we know that $\displaystyle \lim_{x\rightarrow a}h(x)=0$. As such, we have rewritten the product into a quotient _and_ we can apply l'Hospital's rule to the newly obtained quotient (after having checked all other conditions, of course). Let us consider an example showcasing this idea.

::::::{prf:example} Indeterminate form of type $0\cdot \infty$
:label: Ex:lHospital:0infty
Consider the limit

$$
 \lim_{x\rightarrow 0^+}x\ln\left(1+\frac{1}{x}\right).
$$

[^FootnoteQuot]: We could have rewritten the limit to $\displaystyle \lim_{x\rightarrow 0^+}\frac{x}{\frac{1}{\ln\left(1+\frac{1}{x}\right)}}$, but differentiating the denominator of this fraction is considerably more work.

First we note that $\displaystyle \lim_{x\rightarrow 0^+}x=0$ and $\displaystyle \lim_{x\rightarrow 0^+}1+\frac{1}{x}=\infty$, which means that $\displaystyle \lim_{x\rightarrow 0^+}\ln\left(1+\frac{1}{x}\right)=\infty$. This means that we are dealing with an indeterminate form of type $0\cdot \infty$. We rewrite is to a quotient by writing[^FootnoteQuot]



$$
 \lim_{x\rightarrow 0^+}x\ln\left(1+\frac{1}{x}\right)=\lim_{x\rightarrow 0^+}\frac{\ln\left(1+\frac{1}{x}\right)}{\frac{1}{x}}.
$$

It seems that we our worse off, as the limits looks uglier. However, this is not the case: since $\displaystyle \lim_{x\rightarrow 0^+}\frac{1}{x}=\infty$, we have now rewritten our original limit to an indeterminate form of type $\dfrac{\infty}{\infty}$. Moreover, the functions $f(x)=\ln\left(1+\frac{1}{x}\right)$ and $g(x)=\frac{1}{x}$ are differentiable and have $g'(x)\neq0$ for $x>0$. This suggests that we can use l'Hospital's rule. For this, we evaluate

$$
 \lim_{x\rightarrow 0^+}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow 0^+}\frac{\frac{1}{1+\frac{1}{x}}\left(-\frac{1}{x^2}\right)}{-\frac{1}{x^2}}=\lim_{x\rightarrow 0^+}\frac{1}{1+\frac{1}{x}}=0.
$$

By l'Hospital's rule, we must have

$$
 \lim_{x\rightarrow 0^+}x\ln\left(1+\frac{1}{x}\right)=\lim_{x\rightarrow 0^+}\frac{\ln\left(1+\frac{1}{x}\right)}{\frac{1}{x}}=\lim_{x\rightarrow 0^+}\frac{f'(x)}{g'(x)}=0.
$$


::::::

Indeterminate powers, like $1^\infty$, $\infty^0$ and $0^0$ arise when dealing with limits of the form 

$$
 \lim_{x\rightarrow a}f(x)^{g(x)}.
$$

Expressions of the form $f(x)^{g(x)}$ are usually hard to work with as both the base and the power of this exponent are functions of $x$. Fortunately, there is a nice trick to rewrite such an expression to an exponential where only exponent depends on $x$. For this, we use that the exponential function and the natural logarithm are inverse functions. This means that

$$
 e^{\ln(x)}=\ln\left(e^x\right)=x
$$

for any $x>0$. As such, we can rewrite the limit into

$$
 \lim_{x\rightarrow a}f(x)^{g(x)}=\lim_{x\rightarrow a}\left(e^{\ln(f(x))}\right)^{g(x)}=\lim_{x\rightarrow a}e^{\ln(f(x))g(x)}.
$$

Since the exponential function is continuous, we can take the limit inside (using {prf:ref}`Theorem:Continuity:Substitution` or {prf:ref}`Theorem:Continuity:SubstitutionInf`) and we obtain

$$
 \lim_{x\rightarrow a}f(x)^{g(x)}=\lim_{x\rightarrow a}e^{\ln(f(x))g(x)}=e^{\lim_{x\rightarrow a}\ln(f(x))g(x)}.
$$

This means that we have rewritten the indeterminate power into an indeterminate product and we know, by now, how to handle those.

Let us showcase these ideas with a few examples.

::::::{prf:example} Indeterminate form of type $1^\infty$
:label: Ex:lHospital:1toinfty
Consider the limit

$$
 \lim_{x\rightarrow 1^+}\left(\frac{1}{x}\right)^{\frac{1}{x-1}}.
$$

[^Footnote1inf]: For this particular type of indeterminate form, some students have an issue believing that there is even a problem here, since $1$ to the power something is always $1$, right? That is the case, but that no longer holds when I am taking a high power of something that is close, but unequal to $1$. For instance, we have $0.9999999^{1000000000}=3.72\times 10^{-44}$, which is a smaller number than the [Planck constant](https://en.wikipedia.org/wiki/Planck_constant) in standard units. Also, we have $1.0000001^{10000000000}=1.97\times 10^{434}$, which is a larger number than the number of atoms in the observable universe. The point here is that these type of limits can go anywhere between $0$ and $\infty$ (including $0$ or $\infty$).

Then we have $\displaystyle\lim_{x\rightarrow 1^+} \frac{1}{x}=1$ and $\displaystyle\lim_{x\rightarrow 1^+}\frac{1}{x-1}=\infty$, so we are dealing with an indeterminate form of the type $1^\infty$[^Footnote1inf]. Using the trick described above, we rewrite this limit into

$$
 \lim_{x\rightarrow 1^+}\left(\frac{1}{x}\right)^{\frac{1}{x-1}}=\lim_{x\rightarrow 1^+}\left(e^{\ln\left(\frac{1}{x}\right)}\right)^{\frac{1}{x-1}}=\lim_{x\rightarrow 1^+}e^{\ln\left(\frac{1}{x}\right)\frac{1}{x-1}}=e^{\lim_{x\rightarrow 1^+}\frac{\ln\left(\frac{1}{x}\right)}{x-1}}.
$$

Writing $f(x)=\ln\left(\frac{1}{x}\right)=\ln\left(x^{-1}\right)=-\ln(x)$ and $g(x)=x-1$, we see that $\displaystyle \lim_{x\rightarrow 1^+}f(x)=-\ln(1)=0$ and $\displaystyle \lim_{x\rightarrow 1^+}g(x)=1-1=0$. Hence, the resulting limit is an indeterminate form of type $\dfrac{0}{0}$. In addition, the functions $f$ and $g$ are both differentiable and $g'(x)\neq0$ for any $x$. In order to use l'Hospital's rule, we evaluate

$$
 \lim_{x\rightarrow 1^+}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow 1^+}\frac{-\frac{1}{x}}{1}=-1.
$$

So we can use l'Hospital's rule to obtain

$$
 \lim_{x\rightarrow 1^+}\left(\frac{1}{x}\right)^{\frac{1}{x-1}}=e^{\lim_{x\rightarrow 1^+}\frac{\ln\left(\frac{1}{x}\right)}{x-1}}=e^{-1}=\frac{1}{e}.
$$

:::::::

::::::{prf:example} Indeterminate form of type $\infty^0$
:label: Ex:lHospital:inftyto0
Consider the limit

$$
 \lim_{x\rightarrow 0^+}\left(1+\frac{1}{x}\right)^x.
$$

Then we see that $\displaystyle \lim_{x\rightarrow 0^+}1+\frac{1}{x}=\infty$, while $\displaystyle \lim_{x\rightarrow 0^+}x=0$, so we are dealing with an indeterminate form of type $\infty^0$. Since this is an indeterminate power, we use the idea that we discussed previously to rewrite

$$
 \lim_{x\rightarrow 0^+}\left(1+\frac{1}{x}\right)^x=\lim_{x\rightarrow 0^+}\left(e^{\ln\left(1+\frac{1}{x}\right)}\right)^x=\lim_{x\rightarrow 0^+}e^{\ln\left(1+\frac{1}{x}\right)x}=e^{\lim_{x\rightarrow 0^+}\ln\left(1+\frac{1}{x}\right)x}.
$$

The remaining limit is the one from {prf:ref}`Ex:lHospital:0infty`, so we can use this previous result to obtain

$$
 \lim_{x\rightarrow 0^+}\left(1+\frac{1}{x}\right)^x=e^{\lim_{x\rightarrow 0^+}\ln\left(1+\frac{1}{x}\right)x}=e^0=1.
$$
::::::

::::::{prf:example} Indeterminate of type form $0^0$
:label: Ex:lHospital:inftyto0
As our final example, we consider the limit

$$
 \lim_{x\rightarrow 0^+}\sin(x)^x.
$$

Then we see that $\displaystyle \lim_{x\rightarrow 0^+}\sin(x)=0$, while $\displaystyle \lim_{x\rightarrow 0^+}x=0$, so we are dealing with an indeterminate form of type $0^0$. Since this is an indeterminate power, we use the idea that we discussed previously to rewrite

$$
 \lim_{x\rightarrow 0^+}\sin(x)^x=\lim_{x\rightarrow 0^+}\left(e^{\ln(\sin(x))}\right)^x=\lim_{x\rightarrow 0^+}e^{\ln(\sin(x))x}=e^{\lim_{x\rightarrow 0^+}\ln(\sin(x))x}.
$$

Since $\displaystyle\lim_{x\rightarrow 0^+}\sin(x)=0$, we find that $\displaystyle\lim_{x\rightarrow 0^+}\ln(\sin(x))=-\infty$, while $\displaystyle\lim_{x\rightarrow 0^+}x=0$. So we are dealing with an indeterminate product of type $-\infty\cdot 0$. This means that we should rewrite it into a quotient and we obtain

$$
 \lim_{x\rightarrow 0^+}\ln(\sin(x))x=\lim_{x\rightarrow 0^+}\frac{\ln(\sin(x))}{\frac{1}{x}}.
$$

We now write $f(x)=\ln(\sin(x))$ and $g(x)=\frac{1}{x}$. Since $\displaystyle\lim_{x\rightarrow 0^+}f(x)=-\infty$, while $\displaystyle\lim_{x\rightarrow 0^+}g(x)=\infty$, we are dealing with an indeterminate form of type $\dfrac{-\infty}{\infty}$. In addition, the functions $f$ and $g$ are differentiable and have $g'(x)\neq 0$ for $x>0$. This suggests that we can use l'Hospital's rule. For this, we first evaluate

$$
 \displaystyle\lim_{x\rightarrow 0^+}\frac{f'(x)}{g'(x)}=\displaystyle\lim_{x\rightarrow 0^+}\frac{\frac{\cos(x)}{\sin(x)}}{-\frac{1}{x^2}}=\lim_{x\rightarrow 0^+}\frac{-\cos(x)x^2}{\sin(x)}.
$$

From {prf:ref}`Ex:lHospital:lHospital1` we know that $\displaystyle\lim_{x\rightarrow 0^+}\frac{\sin(x)}{x}=1$, which means that 

$$
 \displaystyle\lim_{x\rightarrow 0^+}\frac{x}{\sin(x)}=\displaystyle\lim_{x\rightarrow 0^+}\frac{1}{\frac{\sin(x)}{x}}=\frac{1}{1}=1.
$$

Then we can rewrite the limit as the product of three known limits and we obtain

$$
  \lim_{x\rightarrow 0^+}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow 0^+}\frac{-\cos(x)x^2}{\sin(x)}=\lim_{x\rightarrow 0^+}(-\cos(x))\lim_{x\rightarrow 0^+}\frac{x}{\sin(x)}\lim_{x\rightarrow 0^+}x=-1\cdot1\cdot0=0.
$$

Then, by l'Hospital's rule we obtain

$$
 \lim_{x\rightarrow 0^+}\sin(x)^x=e^{\lim_{x\rightarrow 0^+}\ln(\sin(x))x}=e^0=1.
$$
::::::

