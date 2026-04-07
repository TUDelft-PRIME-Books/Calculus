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

Note that in the final step, we obtained the limit $\displaystyle \lim_{x\rightarrow 1}\frac{1}{-\frac{1}{2}}$. By how the linearisation was constructed, this final limit is $\displaystyle \frac{g'(1)}{h'(1)}$. This suggest that in order to evaluate the limit $\displaystyle \lim_{x\rightarrow 1}\frac{g(x)}{h(x)}$, we can, instead, evaluate $\displaystyle \lim_{x\rightarrow 1}\frac{g'(x)}{h'(x)}$. This result is known as **l'Hospital's rule** and is a very important technique for evaluating limits.

L'Hospital's rule is named after the French mathematician [Guillaume François Antoine, Marquis de l'Hospital (1661-1704)](https://en.wikipedia.org/wiki/Guillaume_de_l%27H%C3%B4pital), who first published the result. However, he did not come up with it himself. That honour goes to the Swiss mathematician [Johan Bernoulli (1667-1748)](https://en.wikipedia.org/wiki/Johann_Bernoulli).



:::{todo}
Make an applet showing the graphs of the functions $f$, $g$ and $h$ with label Fig:lHospital:Motivation. Make a toggle, that switches $g$ and $h$ to their linarisations around $1$ (with $g$ and $h$ shown faded out in the background)
:::

If you ask a student what their favorite rule is to evaluate limits, most students will answer that it is l'Hospital's rule. There is a good reason for this: it is a rule that is applicable to various different limits and the execution is often straightforward. However, l'Hospital's rule is not the catch-all rule that many students seem to think it is. So usually, when we discuss a new technique, we mainly focus on what you **can** do with it. Here, we will also put a lot of focus on what limits **cannot** be evaluated with this technique.

## Indeterminate forms and l'Hospital's rule

There are various reasons why it takes effort to evaluate a limit. For instance, we might we dealing with a fraction where both the numerator and denominator approach $0$, or one where they both approach $\infty$. In order to better help us distinguish between these general categories of limits, we will give them names. For instance, a limit of the form

$$
 \lim_{x\rightarrow a}\frac{f(x)}{g(x)}
$$

with $\displaystyle\lim_{x\rightarrow a}f(x)=\lim_{x\rightarrow a}g(x)=0$ is called an **indeterminate form of type** $\dfrac{0}{0}$. Similarly, a limit of the form 

$$
 \lim_{x\rightarrow a}\frac{f(x)}{g(x)}
$$

with $\displaystyle\lim_{x\rightarrow a}f(x)=\infty$ and $\displaystyle\lim_{x\rightarrow a}g(x)=-\infty$ is called an **indeterminate form of type** $\dfrac{\infty}{-\infty}$. In general, an indeterminate form is a type of limit involving a combination of two or more functions (such as a difference or a quotient) where knowing the limits of the separate functions is not enough to find the limit of the combination. Other types of indeterminate forms include $0\cdot \infty$, $\infty-\infty$, $1^\infty$, $\infty^0$ and $0^0$. For these limits, techniques like cancelling the common factor, the square root trick and, of course, l'Hospital's rule can sometimes be used to turn the limit into something that can be evaluated directly. In this section, we will consider examples of many of these indeterminate forms. Many, but definitely not all, can be solve using l'Hospital's rule.

So without further ado, let us state this rule.


::::::{prf:theorem} l'Hospital's rule for limits at a point
:label: Thm:lHospital:lHospital
Let $I$ be an open interval containing a point $a$. Supppose that the functions $f$ and $g$ are differentiable on $I$, except possibly at $a$. Suppose that 

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

The result also holds when replacing all occurences of $\displaystyle \lim_{x\rightarrow a}$ by the left limit $\displaystyle \lim_{x\rightarrow a^-}$, or by replacing all of them by the right limit $\displaystyle \lim_{x\rightarrow a^+}$. For the left limits, $I$ can also be an open interval of the form $(z,a)$, while for the right limits, $I$ can also be an open interval of the form $(a,b)$.
::::::

[^FootnoteShorthand]: This notation is a shorthand for the four types $\dfrac{\infty}{\infty}$, $\dfrac{-\infty}{\infty}$, $\dfrac{\infty}{-\infty}$ and $\dfrac{-\infty}{-\infty}$.

:::{note}
The conditions in the theorem state that l'Hospital's rule can be applied to indeterminate forms of type either $\dfrac{0}{0}$ or $\dfrac{\pm\infty}{\pm\infty}$[^FootnoteShorthand]. Later we will see how we can apply it to indeterminate forms of other types. 
:::

We first consider a few examples where l'Hospital's rule can be applied directly.

::::::{prf:example} 
:label: Ex:lHospital:lHospital1
Consider the limit 

$$
 \displaystyle\lim_{x\rightarrow 0}\frac{\sin(x)}{x}.
$$

Since both $\displaystyle\lim_{x\rightarrow 0}\sin(x)=0$ and $\displaystyle\lim_{x\rightarrow 0}x=0$, this limit is of the indeterminate form $\dfrac{0}{0}$. In addition, the functions $f(x)=\sin(x)$ and $g(x)=x$ are differentiable. In order to see whether l'Hospital's rule can be used, we compute

$$
 \lim_{x\rightarrow 0}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow 0}\frac{\cos(x)}{x}=\frac{1}{1}=1.
$$

Since the limit $\displaystyle \lim_{x\rightarrow 0}\frac{f'(x)}{g'(x)}$ exists, we have checked all conditions to use l'Hospital's rule. Then we obtain

$$
 \lim_{x\rightarrow 0}\frac{\sin(x)}{x}=\lim_{x\rightarrow 0}\frac{f(x)}{g(x)}=\lim_{x\rightarrow 0}\frac{f'(x)}{g'(x)}=1.
$$

This limit is a rather well-known limit, and it is sometimes even called a standard limit. We already encountered it in the proof of {prf:ref}`Thm:Differentiability:Standard1`. However, we could not have used l'Hospital's rule in that proof, since there, we were showing that the cosine is the derivative of the sine. So it would have been a very circular reasoning to already use this in the computation.
::::::

::::::{prf:example} 
:label: Ex:lHospital:lHospital2
Let us return to the limit 

$$
 \displaystyle \lim_{x\rightarrow 1}\frac{\ln(x)}{1-\sqrt{x}}
$$

from {numref}`Subsec:lHospitalintro`. Writing $f(x)=\ln(x)$ and $g(x)=1-\sqrt{x}$, we have $\displaystyle\lim_{x\rightarrow 1}f(x)=\displaystyle\lim_{x\rightarrow 1}g(x)=0$, so we are again dealing with an indeterminate form of type $\dfrac{0}{0}$. In addition, the functions $f$ and $g$ are both differentiable around $1$. Then, we check that the limit of the quotient of the derivatives exists by evaluating

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

Writing $f(x)=\cos(x)-1$ and $g(x)=x^2$, we have $\displaystyle\lim_{x\rightarrow 0}f(x)=\displaystyle\lim_{x\rightarrow 0}g(x)=0$, so we are again dealing with an indeterminate form of type $\dfrac{0}{0}$. In addition, the functions $f$ and $g$ are both differentiable around $0$. Finally, we check that the limit of the quotient of the derivatives exists by evaluating

$$
 \lim_{x\rightarrow 0}\frac{f'(x)}{g'(x)}=\lim_{x\rightarrow 0}\frac{-\sin(x)}{2x}.
$$

[^FootnotePrevEx]: This limit is a constant multiple of the one in {prf:ref}`Ex:lHospital:lHospital1`, so we, actually, do know its value. For the sake of the argument, we now pretend that we do not know this result.

However, we now run into an issue, since this again an indeterminate form of type $\dfrac{0}{0}$, so we do not know if the limit exists[^FootnotePrevEx]. For this, we will again use l'Hopsital's rule. Since $f'$ and $g'$ are differentiable, we can check the limit of the quotient of their derivatives by evaluating

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
Consider the interval $I=(a,\infty)$. Supppose that the functions $f$ and $g$ are differentiable on $I$. Suppose that 

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

The result also holds when replacing all occurences of $\displaystyle \lim_{x\rightarrow \infty}$ by $\displaystyle \lim_{x\rightarrow -\infty}$ with $I=(-\infty,a)$.
::::::

::::::{prf:example} 
:label: Ex:lHospital:lHospitalinf
Consider the limit

$$
 \displaystyle \lim_{x\rightarrow \infty}\frac{\ln\left(x^3+1\right)}{\ln\left(x^2+1\right)}.
$$

Writing $f(x)=\ln\left(x^3+1\right)$ and $g(x)=\ln\left(x^2+1\right)$, we have $\displaystyle\lim_{x\rightarrow \infty}f(x)=\displaystyle\lim_{x\rightarrow \infty}g(x)=\infty$, so we are again dealing with an indeterminate form of type $\dfrac{\infty}{\infty}$. In addition, the functions $f$ and $g$ are both differentiable on the interval $(0,\infty)$. Finally, we check that the limit of the quotient of the derivatives exists by evaluating

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

This is also the result we obtained in {numref}`Subsec:lHospitalintro`.

::::::

## When should you NOT use l'Hospital's rule?


PROOF MOET NOG; OOK VAN VERSIE OP ONEINDIG

In this section we cover:

- Indeterminate forms
- l'Hospital's rule
- Indeterminate products and powers
- Proof of {prf:ref}`Theorem:LimitAtInfinity:Standardgrowthrates`