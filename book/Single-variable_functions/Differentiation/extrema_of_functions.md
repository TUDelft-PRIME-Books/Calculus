(Section:Extrema1d)=

# Extrema of functions

(Subsec:Extrema1dEVT)=

## Introduction

::::::{prf:theorem} Fermat's theorem
:label: Thm:MinMax:Fermat
If a function $f$ has a local maximum or local minimum at $c$ and if $f$ is differentiable at $c$, then $f'(c)=0$.
::::::

## Extreme value theorem

Consider a function $f$ that is continuous on a closed interval $[a,b]$. Is it possible for $f$ to have a vertical asymptote on this interval? The answer is no, since if the function has a vertical asymptote at a point $c$, the function values would need to make a jump from very large or very negative values to the value $f(c)$, which is impossible for a continuous function. In principle, continuous functions can have vertical asymtotes. For instance, the function $f(x)=\dfrac{1}{x}$ has a vertical asymptote at $x=0$. However, although this function is continuous on its domain, is not continuous on any closed interval that contains $0$, since it is undefined there. So the fact that we are dealing with a closed interval is essential here.

This idea suggests that continuous functions cannot "blow up" on closed intervals.

Before we can show that a continuous function on a closed interval attains an absolute maximum and an absolute minimum, we first show that such a function must be bounded.

::::::{prf:theorem} Boundedness theorem
:label: Thm:MinMax:Boundedness
Let $f$ be a function that is continuous on $[a,b]$. Then $f$ is bounded on $[a,b]$. That is, there are real numbers $m$ and $M$ with 

$$
 m\leq f(x)\leq M
$$

 for all $x$ in $[a,b]$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:MinMax:Boundedness`
:class: tudproof, dropdown
The proof of this result is a bit beyond the scope of this book as it used the completeness of the real numbers, but we include it for completeness. Feel free to skip the proof.

We let $S$ denote the set of all $s$ in the interval $[a,b]$ such that $f$ is bounded on the closed interval $[a,s]$. $f$ is definitely bounded on the interval $[a,a]$ (which is just the single point $\{a\}$), so $a$ is in $S$. In particular, $S$ is not the empty set.

Now if $s>a$ were another point in $S$, then $f$ is bounded on $[a,s]$. That means that we can find $m$ and $M$ with

$$
 m\leq f(x)\leq M
$$

for all $a\leq x\leq s$. Now for any $a<t<s$ and any $a\leq x\leq t$ we still have $m\leq f(x)\leq M$. That precisely means that $t$ is in $S$ as well. So if $s$ is in $S$, then the entire interval $[a,s]$ a subset of $S$ as well.

Since $f$ is continuous at $a$ (or, at least, right-continuous), we can let $\delta_1>0$ such that for all $x$ in $[a,b]$ with $0<|x-a|<\delta_1$ we have 

$$
 |f(x)-f(a)|<1.
$$

Without loss of generality, we can assume that $a+\frac{\delta_1}{2}\leq b$. Then for $a\leq x\leq a+\frac{\delta_1}{2}$ we have $|f(x)-f(a)|<1$, which means that

$$
 f(a)-1\leq f(x)\leq f(a)+1.
$$

That is, the function values of $f$ are bounded in between $f(a)-1$ and $f(a)+1$ on the interval $\left[a,a+\frac{\delta_1}{2}\right]$. As such, $a+\frac{\delta_1}{2}$ must be in $S$ and by our previous considerations, the entire interval $\left[a,a+\frac{\delta_1}{2}\right]$ is a subset of $S$.

Finally, for any $s$ in $S$, we have $s\leq b$ by definition of the set $S$. So $S$ is bounded above by $b$.

Since $S$ is a nonempty set that is bounded above, it has a supremum (least upper bound) by the completeness of the real numbers. Let us call this supremum $s$. Since $b$ is an upper bound of $S$, we have $s\leq b$. Since $S$ contains the interval $\left[a,a+\frac{\delta_1}{2}\right]$ we also have $s>a$. We will show that $s=b$. Let us argue by contradiction and assume that $s<b$. Since $f$ is continuous at $s$, we can find $\delta_2>0$ such that for all $x$ with $0<|x-s|<\delta_2$ we have

$$
 |f(x)-f(s)|<1.
$$

Just like before, this means that $f$ is bounded on $\left[s-\frac{\delta_2}{2},s+\frac{\delta_2}{2}\right]$. Since $s<b$, we can, without loss of generality assume that $s+\frac{\delta_2}{2}\leq b$. Since $s$ is the supremum of $S$, there must be a point $t$ in $S$ with $s-\frac{\delta_2}{2}\leq t$. Since $t$ is in $S$, $f$ is bounded on $[a,t]$. Then $f$ is bounded on both $[a,t]$ and $\left[s-\frac{\delta_2}{2},s+\frac{\delta_2}{2}\right]$ and since $s-\frac{\delta_2}{2}\leq t$, we find that $f$ is bounded on $\left[a,s+\frac{\delta_2}{2}\right]$. This means that $s+\frac{\delta_2}{2}$ is in $S$, but this is impossible, since $s$ is the supremum of $S$.

So we find that $s=b$. Unfortunately, that still does not automatically mean that $f$ is bounded on $[a,b]$ as $s$ does not necessarily need to be in $S$ ($S$ could, potentially, be the half-open interval $[a,b)$). To show that $f$ is bounded on $[a,b]$ we will use that $f$ is (left)-continuous in $b$. Indeed, we can take $\delta_3>0$ such that for all $x$ in $[a,b]$ with $0<|x-b|<\delta_3$ we have

$$
 |f(x)-f(b)|<1.
$$

Just like earlier, we find that $f$ must be bounded on $\left[b-\frac{\delta_3}{2},b\right]$. Since $b$ is the supremum of $S$, we can find $t$ in $S$ with $b-\frac{\delta_3}{2}\leq t$. Since $t$ is in $S$, $f$ is bounded on $[a,t]$. Then $f$ is bounded on both $[a,t]$ and $\left[b-\frac{\delta_3}{2},b\right]$ and since $b-\frac{\delta_3}{2}\leq t$, we find that $f$ is bounded on $\left[a,b\right]$, as desired.
:::


::::::{prf:theorem} Extreme value theorem
:label: Thm:MinMax:EVT
Let $f$ be a function that is continuous on $[a,b]$. Then there are $c$ and $d$ in $[a,b]$ such that $f(c)$ is the absolute maximum and $f(d)$ is the absolute minimum of $f$ on $[a,b]$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:MinMax:EVT`
:class: tudproof, dropdown
This proof uses the completeness of the real numbers, just like the proof of {prf:ref}`Thm:MinMax:Boundedness`. Feel free to skip the proof.

The range of $f$ on $[a,b]$, i.e. the set 

$$
 R=\{y\in\mathbb{R}\,|\,y=f(x)\ \mathrm{for}\ \mathrm{some}\ x\in[a,b]\},
$$

is a bounded set by {prf:ref}`Thm:MinMax:Boundedness`. In addition, it is nonempty as it contains $f(a)$. By the completeness of the real numbers, the set $R$ has a supremum $M$. We will show that $M$ is the absolute maximum of $f$ on $[a,b]$. We will argue by contradiction, so we assume that $f(x)<M$ for all $x$ in $[a,b]$. Consider the function

$$
 g(x)=\frac{1}{M-f(x)}.
$$

Since $f(x)<M$ for all $x$ in $[a,b]$, $g$ is a continuous function on $[a,b]$. We will show that $g$ is unbounded on this interval, which contradicts {prf:ref}`Thm:MinMax:Boundedness`.

Consider any $N>0$ and write $\varepsilon=\dfrac{1}{N}$. Since $M$ is the supremum of the range $R$, we can find $y$ in $R$ with $y>M-\varepsilon$. That is, we can find $x$ in $[a,b]$ with 

$$
 f(x)>M-\varepsilon,
$$

which means that

$$
 M-f(x)<\varepsilon.
$$

For this value of $x$, we find that 

$$
 g(x)=g(x)=\frac{1}{M-f(x)}>\frac{1}{\varepsilon}=N.
$$

So that means that $N$ is not an upper bound of $g$ on $[a,b]$. Since this holds for any $N>0$, $g$ cannot be bounded on $[a,b]$. This contradicts {prf:ref}`Thm:MinMax:Boundedness`. So there must be some $c$ in $[a,b]$ with $f(c)=M$, as desired.

Since the function $-f$ is continuous, we can find $d$ in $[a,b]$ with $-f(x)\leq -f(d)$ for all $x$ in $[a,b]$. This means that $f(x)\geq f(d)$ for all $x$ in $[a,b]$, so $f$ also attains an absolute minimum on $[a,b]$.
:::

We can now finally prove Rolle's theorem.

:::{admonition} Proof of {prf:ref}`Thm:MinMax:Rolle`
:class: tudproof, dropdown
First suppose that the function is constant on the interval $[a,b]$. Since the function is constant, we have $f'(c)=0$ for all $c$ in $(a,b)$.

Now suppose that the function is not constant on the interval $[a,b]$. By {prf:ref}`Thm:MinMax:EVT`, $f$ attains both a local maximum and a local minimum on the interval $[a,b]$. Since $f(a)=b(b)$ and $f$ is not constant, at least one of these two must occur at a point $c$ in the open interval $(a,b)$. Indeed, if they were to both occur at the edge values $a$ or $b$, then $f(a)=f(b)$ would both be the highest value and the lowest value of $f$ on $[a,b]$, which would mean that $f$ is constant on $[a,b]$. By {prf:ref}`Thm:MinMax:Fermat` we have that $f'(c)=0$, as desired.
:::

In this section we cover:

- Local minima and maxima
- First derivative test
- Second derivative test
- Extreme value theorem
- Global minimum and maximum on closed intervals