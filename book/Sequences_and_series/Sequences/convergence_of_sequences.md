(Section:SequenceConvergence)=

# Convergence of sequences

## Introduction

In the previous section we have seen that it is sometimes useful to think of a sequence $\{a_n\}$ as a function $f:\mathbb{N}\to\mathbb{R}$ with $f(n)=a_n$ for every $n=1,2,3,\ldots$. This allowed us to use the tools of calculus to study the properties of sequences, such as whether a sequence is strictly increasing, strictly decreasing, non-increasing or non-decreasing and whether it is bounded above or below.

During our study, we already took a quick look at how the values evolve as $n$ increases, when we were considering the bounds. For instance, in {prf:ref}`Ex:Sequences:BoundedExample1` we saw that the sequence $\{a_n\}$ with $a_n=\dfrac{n}{n+1}$ is strictly increasing and bounded above by $1$. This suggests that the terms of the sequence get closer and closer to $1$ as $n$ increases. If we would reuse the terms from {numref}`Section:Limitinf`,we would say that the sequence $\{a_n\}$ converges to $1$. In this section we will define what we mean by convergence of a sequence and we will see how to determine whether a sequence converges or diverges and how to find the limit of a convergent sequence.

## Limits and convergence

In the study of sequences the notion of **convergence** is important. The concept of a limit of a sequence is a special case of the concept of a limit of a function (see {numref}`Section:Limitinf`):

::::::{prf:definition} Limit of a sequence
:label: Def:Sequences:LimitSequence

A sequence $\{a_n\}$ converges to a **limit** $L$ if for every positive real number $\varepsilon$ there exists an integer $N$ such that if $n\geq N$, then $|a_n-L|<\varepsilon$. 

If $\{a_n\}$ converges to $L$, then we write

$$
\lim\limits_{n\to\infty}a_n=L.
$$
::::::

In a more intuitive way, we can say that a sequence $\{a_n\}$ converges to $L$ if the terms of the sequence get closer and closer to $L$ as $n$ increases, or the distance from $a_n$ to $L$ approaches $0$ as $n$ increases towards $\infty$.

We already used the term *converge* in the previous definition, but let us now give a precise definition of what we mean by convergence of a sequence.

::::::{prf:definition} Convergence and divergence of a sequence
:label: Def:Sequences:ConvergenceSequence
A sequence $\{a_n\}$ is called **convergent** if $\lim\limits_{n\to\infty}a_n$ exists. Otherwise, the sequence is called **divergent**. 
::::::

::::::{note}
:name: Note:SeqAndTypes:ConvergenceDivergence

A sequence $\{a_n\}$ either converges or diverges. That is, either $\lim\limits_{n\to\infty}a_n=L$ exists (as a real number) or $\lim\limits_{n\to\infty}a_n$ does not exist.

If $\lim\limits_{n\to\infty}a_n=\infty$ we say that the sequence *diverges* to $\infty$, but the limit $\lim\limits_{n\to\infty}a_n$ does not exist, since $\infty$ is not a real number.

If $\lim\limits_{n\to\infty}a_n=-\infty$ we say that the sequence *diverges* to $-\infty$, but the limit $\lim\limits_{n\to\infty}a_n$ does not exist, since $-\infty$ is not a real number.

If $\lim\limits_{n\to\infty}a_n$ does not exist, but is not $\infty$ or $-\infty$, we can only say that the sequence *diverges*.
:::::: 

Before we dive into depth of convergence of sequences, we will state the most important theorem of this section, which gives us a powerful tool to determine whether a sequence converges or diverges and to find the limit of a convergent sequence:

::::::{prf:theorem}
:label: Thm:Sequences:LimitFunctionSequence
Consider the sequence $\{a_n\}_{n=p}^{\infty}$ with $a_n=f(n)$ for all $n=p,p+1,p+2,\ldots$.

If $f$ is defined on $[p,\infty)$ and $\lim\limits_{x\to\infty}f(x)=L$, then $\lim\limits_{n\to\infty}a_n=L$.
::::::

::::{admonition} Proof of {prf:ref}`Thm:Sequences:LimitFunctionSequence`
:class: tudproof

Let us first recall the definition of $\lim\limits_{x\to\infty}f(x)=L$ from {prf:ref}`Def:LimitAtInfinity:Precisedefplusminus`: for every $\varepsilon>0$ there exists a number $M>0$ such that if $x>M$, then $|f(x)-L|<\varepsilon$.

By {prf:ref}`Def:Sequences:LimitSequence`, we need to show that for every $\varepsilon>0$ there exists an integer $N\geq p$ such that if $n\geq N$, then $|a_n-L|<\varepsilon$.

So let us assume that $\varepsilon>0$ is given. Since $\lim\limits_{x\to\infty}f(x)=L$, there exists a number $M\geq p$ such that if $x>M$, then $|f(x)-L|<\varepsilon$.

We set $N=\max\{p,\lceil M\rceil\}$, where $\lceil M\rceil$ is the smallest integer greater than or equal to $M$. Note that $N\geq M\geq p$.

Since $n\geq M$, we have

$$
|f(n)-L|<\varepsilon.
$$

Now, if $n\geq N$, then also $n\geq M\geq p$ and therefore $n$ is in the domain of $f$ and $a_n=f(n)$:

$$
|a_n-L|<\varepsilon.
$$

This shows that under the assumptions of the theorem, we have $\lim\limits_{n\to\infty}a_n=L$.

::::

A huge advantage of {prf:ref}`Thm:Sequences:LimitFunctionSequence` is that it allows us to use every tool that we have developed in {numref}`Section:Limitinf` to determine whether a sequence converges or diverges and to find the limit of a convergent sequence. For instance, we can use the rules of calculations for limits of functions, the squeeze theorem, the continuity of functions, etc. We can even use l'Hospital's rule from {numref}`Section:lHospital` to find limits of sequences. 

All these theorems indicate that we do not really have to go back and forth between sequences and functions, but that we can directly apply the tools that we have developed for limits of functions to determine whether a sequence converges or diverges and to find the limit of a convergent sequence, except when we use l'Hospital's rule from {numref}`Section:lHospital`, since l'Hospital's rule uses derivatives[^lHospital].

[^lHospital]: But even then, sometimes we allow it.

We state, without proof, the rules of calculations for limits of sequences, which are direct consequences of the rules of calculations for limits of functions, {prf:ref}`Theorem:LimitAtInfinity:Basiccomputationrules` and {prf:ref}`Thm:Sequences:LimitFunctionSequence`:

::::{prf:theorem}
:label: Thm:Sequences:LimitCalculationRules

Suppose that $\{a_n\}$ and $\{b_n\}$ are two sequences such that $\lim\limits_{n\to\infty}a_n=L$ and $\lim\limits_{n\to\infty}b_n=M$. Let $c$ be a real number. Then:

- $\lim\limits_{n\to\infty}ca_n=cL$.

- $\lim\limits_{n\to\infty}(a_n+b_n)=L+M$.

- $\lim\limits_{n\to\infty}(a_nb_n)=LM$.

- If $M\neq0$, then $\lim\limits_{n\to\infty}\dfrac{a_n}{b_n}=\dfrac{L}{M}$.
::::

Without further ado, let us now apply the tools that we have developed for limits of functions to determine whether a sequence converges or diverges and to find the limit of a convergent sequence.

::::::{prf:example}
:label: Ex:Sequences:ConvergenceExample1

Consider the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{2n^2-3n+4}{3n^2+4n+5}$. Then

\begin{align*}
\lim_{n\to\infty}\frac{2n^2-3n+4}{3n^2+4n+5} &= \lim_{n\to\infty}\frac{2-\dfrac{3}{n}+\dfrac{4}{n^2}}{3+\dfrac{4}{n}+\dfrac{5}{n^2}} \\
&= \frac{2-0+0}{3+0+0} \\
&= \frac{2}{3}.
\end{align*}

This means that as $n$ increases, the terms of the sequence $\{a_n\}$ get closer and closer to $\dfrac{2}{3}$, and therefore $\{a_n\}$ is convergent and $\lim\limits_{n\to\infty}a_n=\dfrac{2}{3}$.

::::::

:::::{prf:example}
:label: Ex:Sequences:ConvergenceExample2

For the sequence $\{b_n\}_{n=1}^{\infty}$ with $b_n=\dfrac{2n-1}{\sqrt{n^2+1}}$ we have

\begin{align*}
\lim_{n\to\infty}\frac{2n-1}{\sqrt{n^2+1}} &= \lim_{n\to\infty}\frac{2-\dfrac{1}{n}}{\sqrt{1+\dfrac{1}{n^2}}} \\
&=\frac{2-0}{\sqrt{1+0}} \\
&=2.
\end{align*}

:::::

:::::{prf:example}
:label: Ex:Sequences:ConvergenceExample3

Negative limits also can occur. For instance, for the sequence $\{c_n\}_{n=1}^{\infty}$ with $c_n=n-\sqrt{n(n+2)}$ we have       

\begin{align*}
\lim_{n\to\infty}\left(n-\sqrt{n(n+2)}\right) &= \lim_{n\to\infty}\left(n-\sqrt{n(n+2)}\right)\cdot\frac{n+\sqrt{n(n+2)}}{n+\sqrt{n(n+2)}} \\
&= \lim_{n\to\infty}\frac{n^2-n(n+2)}{n+\sqrt{n(n+2)}} \\
&= \lim_{n\to\infty}\frac{-2n}{n+\sqrt{n(n+2)}} \\
&= \lim_{n\to\infty}\frac{-2}{1+\sqrt{1+\dfrac{2}{n}}} \\
&= \frac{-2}{1+\sqrt{1+0}} \\
&= -1.
\end{align*}

:::::

::::::{prf:example}
:label: Ex:Sequences:ConvergenceExample4

The geometric sequence $\{d_n\}$ with $d_n=\dfrac{1}{2^n}$ is convergent and $\lim\limits_{n\to\infty}a_n=0$.

This follows directly from {prf:ref}`Thm:Sequences:LimitFunctionSequence` and {prf:ref}`Theorem:LimitAtInfinity:Standardlimits`.
::::::

For geometric sequences, we can go even further and determine for which values of $r\in\mathbb{R}$ the geometric sequence $\{a_n\}$ with $a_n=r^n$ is convergent or divergent and what the limit is in case it is convergent.

::::::{prf:theorem}
:label: Thm:Sequences:ConvergenceGeometric

The geometric sequence $\{a_n\}_{n=0}^{\infty}$ with $a_n=br^n$, $b\neq0$, is convergent for $-1<r\leq1$ and divergent for all other values of $r\in\mathbb{R}$.

Moreover, if $-1<r<1$, then $\lim\limits_{n\to\infty}r^n=0$, and  if $r=1$, then $\lim\limits_{n\to\infty}r^n=b$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Sequences:ConvergenceGeometric`
:class: tudproof

We distinguish four cases: $-1<r<1$, $r=1$, $r>1$ and $r<-1$.

If $-1<r<1$, then $|r|<1$ and $\lim\limits_{n\to\infty}|r^n|=\lim\limits_{n\to\infty}|r|^n=0$, so also $\lim\limits_{n\to\infty}br^n=0$.

If $r=1$, then $\lim\limits_{n\to\infty}r^n=\lim\limits_{n\to\infty}1^n=1$ and so $\lim\limits_{n\to\infty}br^n=b$.

If $r>1$, then $\lim\limits_{n\to\infty}r^n=\infty$, so also $\lim\limits_{n\to\infty}br^n=\infty$ or $\lim\limits_{n\to\infty}br^n=-\infty$, depending on the sign of $b$.

Finally, if $r<-1$, then $\lim\limits_{n\to\infty}r^n$ does not exist, since the terms of the sequence $r^n$ do not get closer and closer to a single real number as $n$ increases, but they oscillate between positive and negative values that get larger and larger in absolute value. So, also $\lim\limits_{n\to\infty}br^n$ does not exist.

This proves the theorem.
::::::

::::::{prf:example}
:label: Ex:Sequences:ConvergenceExample5
The sequence $\{a_n\}$ with $a_n=\left(-\dfrac{4}{5}\right)^n$ is a geometric sequence with $r=-\dfrac{4}{5}$, so $-1<r<1$, and is thus convergent and $\lim\limits_{n\to\infty}a_n=0$.

::::::

::::::{prf:example}
:label: Ex:Sequences:ConvergenceExample6
The sequence $\{b_n\}$ with $b_n=2^n$ diverges to $\infty$, because $2>1$ and it is a geometric sequence.

::::::

::::::{prf:example}
:label: Ex:Sequences:ConvergenceExample7

The sequence $\{c_n\}$ with $c_n=(-1)^n$ is divergent. It does not diverge to $\infty$ or $-\infty$.
::::::

## Using continuity

Because of the close relation between limits of functions and continuity of functions, we can also reuse the tools that we have developed in {numref}`Section:Continuity` to determine whether a sequence converges or diverges and to find the limit of a convergent sequence, and especially {prf:ref}`Theorem:Continuity:SubstitutionInf`. The sequence version of this last theorem is worth stating explicitly:

::::::{prf:theorem}
:label: Thm:Sequences:Continuity
If $\lim\limits_{x\to\infty}f(x)=L$ and the function $f$ is continuous at $L$, then $\lim\limits_{n\to\infty}f(a_n)=f(L)$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Sequences:Continuity`
:class: tudproof, dropdown
This is an immediate consequence of {prf:ref}`Theorem:Continuity:SubstitutionInf` and {prf:ref}`Thm:Sequences:LimitFunctionSequence`.
::::::

::::::{prf:example}
1) The sequence $\{a_n\}$ with $a_n=\sin\left(\dfrac{1}{n}\right)$ is convergent and $\lim\limits_{n\to\infty}a_n=\sin(0)=0$.

2) The sequence $\{b_n\}$ with $b_n=\cos\left(\dfrac{n\pi}{n+1}\right)$ is convergent and $\lim\limits_{n\to\infty}b_n=\cos(\pi)=-1$.

3) The sequence $\{c_n\}$ with $c_n=\arctan\left(\dfrac{n+1}{n+2}\right)$ is convergent and $\lim\limits_{n\to\infty}c_n=\arctan(1)=\frac{1}{4}\pi$.
::::::

## Connecting monotonicity, boundedness and convergence

Let us revisit {prf:ref}`Ex:Sequences:IncreasingExample1Function` and {prf:ref}`Ex:Sequences:IncreasingExample2Function` to determine whether the sequences $\{a_n\}$ with $a_n=\dfrac{n}{n+1}$ and $\{b_b\}$ with $b_n=\dfrac{2n}{n^2+1}$ are convergent or divergent and to find the limit in case they are convergent.

::::::{prf:example}
:label: Ex:Sequences:ConvergenceExampleIncreasing
We show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{n}{n+1}$ is convergent.

```{figure} Images/sequence1.png
---
width: 50%
name: Fig:Sequences:ConvergenceExampleIncreasing
align: center
class: dark-light
---
The terms of the sequence $\{a_n\}$ lie on the graph of $f(x)=\dfrac{x}{x+1}$.
```

:::{todo}
Replace {numref}`Fig:Sequences:ConvergenceExampleIncreasing` with an applet.
:::

Note that $a_n=f(n)$ with $f(x)=\dfrac{x}{x+1}$. Now we have

$$
\lim_{x\to\infty}f(x)=\lim_{x\to\infty}\frac{x}{x+1}=1.
$$

This implies that the sequence $\{a_n\}_{n=1}^{\infty}$ is convergent and $\lim\limits_{n\to\infty}a_n=1$.
::::::

::::::{prf:example}
:label: Ex:Sequences:ConvergenceExampleDecreasing
We show that the sequence $\{b_n\}_{n=1}^{\infty}$ with $b_n=\dfrac{2n}{n^2+1}$ is convergent.

```{figure} Images/sequence2.png
---
width: 50%
name: Fig:Sequences:ConvergenceExampleDecreasing
align: center
class: dark-light
---
The terms of the sequence $\{b_n\}$ lie on the graph of $g(x)=\dfrac{2x}{x^2+1}$.
```

:::{todo}
Replace {numref}`Fig:Sequences:ConvergenceExampleDecreasing` with an applet.
:::

Note that $b_n=g(n)$ with $g(x)=\dfrac{2x}{x^2+1}$. Then we have

$$
\lim_{x\to\infty}g(x)=\lim_{x\to\infty}\frac{2x}{x^2+1}=0.
$$

This implies that the sequence $\{b_n\}_{n=1}^{\infty}$ is convergent and $\lim\limits_{n\to\infty}b_n=0$.
::::::

From {prf:ref}`Ex:Sequences:IncreasingExample1Function`, {prf:ref}`Ex:Sequences:BoundedExample1` and {prf:ref}`Ex:Sequences:ConvergenceExampleIncreasing` we can conclude that the sequence $\{a_n\}$ with $a_n=\dfrac{n}{n+1}$ is strictly increasing, bounded above (by $1$) and convergent. From {prf:ref}`Ex:Sequences:IncreasingExample2Function`, {prf:ref}`Ex:Sequences:BoundedExample2` and {prf:ref}`Ex:Sequences:ConvergenceExampleDecreasing` we can conclude that the sequence $\{b_n\}$ with $b_n=\dfrac{2n}{n^2+1}$ is strictly decreasing, bounded below (by $0$) and convergent.

Every strictly increasing sequence is also non-decreasing, and every strictly decreasing sequence is also non-increasing. So, we can also say that the sequence $\{a_n\}$ with $a_n=\dfrac{n}{n+1}$ is non-decreasing, bounded above (by $1$) and convergent, and that the sequence $\{b_n\}$ with $b_n=\dfrac{2n}{n^2+1}$ is non-increasing, bounded below (by $0$) and convergent.

As you may expect this is no coincidence, and in fact we have the following important theorem:

::::::{prf:theorem} Monotone convergence theorem
:label: Thm:Sequences:MonotonicBounded
Every *non-decreasing* sequence that is *bounded above* is convergent and every *non-increasing* sequence that is *bounded below* is convergent.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Sequences:MonotonicBounded`
:class: tudproof, dropdown

:::{figure} Images/convergent.png
:width: 50%
:name: Fig:Sequences:MonotonicBounded
:align: center

A non-decreasing sequence that is bounded above.
:::

:::{todo}
Replace {numref}`Fig:Sequences:MonotonicBounded` with an applet.
:::

Suppose that $\{a_n\}$ is a non-decreasing sequence that is bounded above. Then it has a *least upper bound* $L$. Let $\epsilon>0$, then $L-\epsilon$ is *not* an upper bound, since $L$ is the least upper bound. Therefore

$$
a_N>L-\epsilon
$$

for some integer $N$.

However, since the sequence is non-decreasing, we have $a_n\geq a_N$ for every $n>N$. Thus, if $n>N$, we have

$$
a_n>L-\epsilon\quad\Longrightarrow\quad0\leq L-a_n<\epsilon,
$$

since $a_n\leq L$. Thus whenever $n>N$ we have

$$
|L-a_n|<\epsilon.
$$

So, $\lim\limits_{n\to\infty}a_n=L$.

A similar proof, using the greatest lower bound, works for a non-increasing sequence that is bounded below.
::::::

::::::{prf:example}
:label: Ex:Sequences:MonotonicBoundedExample1
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=1$ and $a_{n+1}=\frac{1}{2}(a_n+5)$ for $n=1,2,3,\ldots$. 

We have seen that the sequence strictly increases and is bounded above. This implies that the sequence converges. So, the limit $\lim\limits_{n\to\infty}a_n$ exists.

Let $L=\lim\limits_{n\to\infty}a_n$, then we have $\lim\limits_{n\to\infty}a_{n+1}=L$ and

$$
L=\frac{1}{2}(L+5)\quad\Longleftrightarrow\quad2L=L+5\quad\Longleftrightarrow\quad L=5.
$$

::::::

::::::{prf:example}
:label: Ex:Sequences:MonotonicBoundedExample2
Consider the sequence $\{b_n\}_{n=1}^{\infty}$ given by $b_1=10$ and $b_{n+1}=\sqrt{b_n+6}$ for $n=1,2,3,\ldots$. 

We will show that the sequence converges and find its limit.

We have seen that the sequence strictly decreases and is bounded below by $0$. This implies that the sequence converges. So, the limit $\lim\limits_{n\to\infty}b_n$ exists.

Let $L=\lim\limits_{n\to\infty}b_n$, then we also have $\lim\limits_{n\to\infty}b_{n+1}=L$ and

\begin{align*}
L=\sqrt{L+6}\quad\Longrightarrow\quad L^2=L+6&\quad\Longleftrightarrow\quad L^2-L-6=0\\
&\quad\Longleftrightarrow\quad(L-3)(L+2)=0.
\end{align*}
Hence: $L=3$ or $L=-2$. Since the sequence is bounded below by $0$, we conclude that $L=3$.
::::::


::::::{warning}
:name: Warning:Sequences:ConvergenceAssumption

It is important that we first showed that the limit exists before setting $L=\lim\limits_{n\to\infty}a_n$. Otherwise, you might draw wrong conclusions.

For instance, it is clear that the Fibonacci sequence, which is defined by 

$$
F_{n+2}+F_n+F_{n+1}\quad\text{for}\quad n=1,2,3,\ldots
$$ 

with $F_1=F_2=1$ is divergent. So, the limit $\lim\limits_{n\to\infty}F_n=\infty$ does not exist.

If we would assume that $L=\lim\limits_{n\to\infty}F_n$, then we would have that

$$
L=L+L\quad\Longleftrightarrow\quad L=0.
$$

::::::

## A final squeeze

Another important tool that we can reuse from {numref}`Section:Limitinf` is the squeeze theorem, which also has a sequence version:

::::::{prf:theorem}
:label: Thm:Sequences:SqueezeTheorem

If $\lim\limits_{n\to\infty}|a_n|=b$ for some $b\geq 0$, then $\lim\limits_{n\to\infty}a_n=b$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Sequences:SqueezeTheorem`
:class: tudproof, dropdown
You can prove this using {prf:ref}`Theorem:LimitAtInfinity:Squeezetheorem` and {prf:ref}`Thm:Sequences:LimitFunctionSequence`.
::::::

::::::{prf:example}
:label: Ex:Sequences:SqueezeTheoremExample1
The sequence $\{a_n\}$ with $a_n=\dfrac{(-1)^n}{n}$ is convergent and $\lim\limits_{n\to\infty}a_n=0$ because $|a_n|=\dfrac{1}{n}\to 0$ as $n\to\infty$.
::::::

::::::{prf:example}
:label: Ex:Sequences:SqueezeTheoremExample2
The sequence $\{b_n\}$ with $b_n=\dfrac{\cos(n)}{\sqrt{n}}$ is convergent and $\lim\limits_{n\to\infty}b_n=0$ because $|b_n|\leq\dfrac{1}{\sqrt{n}}\to 0$ as $n\to\infty$.
::::::
::::::

::::::{prf:example}
:label: Ex:Sequences:SqueezeTheoremExample3
The sequence $\{c_n\}$ with $c_n=\dfrac{\sin(n^2)}{n}$ is convergent and $\lim\limits_{n\to\infty}c_n=0$ because $|c_n|\leq\dfrac{1}{n}\to 0$ as $n\to\infty$.
::::::

## Grasple exercises

:::{todo}
Add Grasple exercises to {numref}`Section:SequenceConvergence`.
:::

## Exercises

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise1
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=7$ and $a_{n+1}=\frac{1}{2}(a_n+5)$ for $n=1,2,3,\ldots$. 

Show that the sequence is convergent and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise1`
:class: solution, dropdown
We have seen that the sequence strictly decreases and is bounded below by $1$. This implies that the sequence converges. So, the limit $\lim\limits_{n\to\infty}a_n$ exists.

Let $L=\lim\limits_{n\to\infty}a_n$, then we have $\lim\limits_{n\to\infty}a_{n+1}=L$ and

$$
L=\frac{1}{2}(L+5)\quad\Longleftrightarrow\quad2L=L+5\quad\Longleftrightarrow\quad L=5.
$$

:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise2
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=2$ and $a_{n+1}=\sqrt{a_n+6}$ for $n=1,2,3,\ldots$. 

Show that the sequence is convergent and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise2`
:class: solution, dropdown
We have seen that the sequence strictly increases and is bounded above. This implies that the sequence converges. So, the limit $\lim\limits_{n\to\infty}a_n$ exists.

Let $L=\lim\limits_{n\to\infty}a_n$, then we have $\lim\limits_{n\to\infty}a_{n+1}=L$ and

\begin{align*}
L=\sqrt{L+6}\quad\Longrightarrow\quad L^2=L+6&\quad\Longleftrightarrow\quad L^2-L-6=0\\
&\quad\Longleftrightarrow\quad(L-3)(L+2)=0.
\end{align*}
This implies that $L=3$ or $L=-2$. Since $a_1=1$ and the sequence is strictly increasing, we conclude that $L=3$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise3
Show that the sequence $\left\{\sqrt{2},\sqrt{2\sqrt{2}},\sqrt{2\sqrt{2\sqrt{2}}},\ldots\right\}$ converges and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise3`
:class: solution, dropdown
Note that the sequence can be written as $\{a_n\}_{n=1}^{\infty}$ with $a_1=\sqrt{2}$ and $a_{n+1}=\sqrt{2a_n}$ for $n=1,2,3,\ldots$.

1) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is strictly increasing: $a_{n+1}>a_n$ for $n=1,2,3,\ldots$.

  For $n=1$ this reads: $a_2=\sqrt{2a_1}=\sqrt{2\sqrt{2}}\sqrt{2}\sqrt{\sqrt{2}}>\sqrt{2}=a_1$ which is true.

  Assuming that $a_{k+1}>a_k$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{2a_{k+1}}>\sqrt{2a_k}=a_{k+1}.
$$

  This proves that the sequence is strictly increasing.

2) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is bounded above, for instance that $a_n\leq2$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=\sqrt{2}\leq2$, which is true.

Assuming that $a_k\leq2$ for certain value of $k$ we obtain

$$
a_{k+1}=\sqrt{2a_{k}}\leq\sqrt{2\cdot 2}=2.
$$

This proves that the sequence is bounded above by $2$.

3) Since the sequence is strictly increasing and bounded above, we conclude that the sequence is convergent. So $L=\lim\limits_{n\to\infty}a_n=\lim\limits_{n\to\infty}a_{n+1}$ exists. Then we have

\begin{align*}
L = \lim_{n\to\infty}a_{n+1} = \lim_{n\to\infty}\sqrt{2a_n} = \sqrt{2\lim_{n\to\infty}a_n} = \sqrt{2L}.
\end{align*}

From this we obtain

$$
L=\sqrt{2L}\quad\Longrightarrow\quad L^2=2L\quad\Longleftrightarrow\quad L=0\quad\text{or}\quad L=2.
$$

Since $a_1=\sqrt{2}>1$ and the sequence is strictly increasing, we conclude that $L=2$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise4
Show that the sequence $\left\{\sqrt{2},\sqrt{2+\sqrt{2}},\sqrt{2+\sqrt{2+\sqrt{2}}},\ldots\right\}$ converges and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise4`
:class: solution, dropdown
Note that the sequence can be written as $\{a_n\}_{n=1}^{\infty}$ with $a_1=\sqrt{2}$ and $a_{n+1}=\sqrt{2+a_n}$ for $n=1,2,3,\ldots$.

1) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is strictly increasing: $a_{n+1}>a_n$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_2=\sqrt{2+a_1}=\sqrt{2+\sqrt{2}}>\sqrt{2}=a_1$ which is true.

Assuming that $a_{k+1}>a_k$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{2+a_{k+1}}>\sqrt{2+a_k}=a_{k+1}.
$$

This proves that the sequence is strictly increasing.

2) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is bounded above, for instance that $a_n\leq2$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=\sqrt{2}\leq2$, which is true.

Assuming that $a_k\leq2$ for certain value of $k$ we obtain

$$
a_{k+1}=\sqrt{2+a_{k}}\leq\sqrt{2+2}=2.
$$

This proves that the sequence is bounded above by $2$.

3) Since the sequence is strictly increasing and bounded above, we conclude that the sequence is convergent. So: $L=\lim\limits_{n\to\infty}a_n$ exists and must satisfy

\begin{align*}
L=\sqrt{2+L}\quad\Longrightarrow\quad L^2=2+L&\quad\Longleftrightarrow\quad L^2-L-2=0\\
&\quad\Longleftrightarrow\quad(L-2)(L+1)=0.
\end{align*}
Hence: $L=2$ or $L=-1$. Since $a_1=\sqrt{2}>1$ and the sequence is strictly increasing, we conclude that $L=2$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise5
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=1$ and $a_{n+1}=4-\dfrac{1}{a_n}$ is convergent and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise5`
:class: solution, dropdown
1) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is strictly increasing: $a_{n+1}>a_n$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_2=4-1=3>1=a_1$ which is true.

Assuming that $a_{k+1}>a_k$ for certain value of $k$ we obtain $-a_{k+1}<-a_k$ and $-\displaystyle\frac{1}{a_{k+1}}>-\frac{1}{a_k}$ and therefore

$$
a_{k+2}=4-\frac{1}{a_{k+1}}>4-\frac{1}{a_k}=a_{k+1}.
$$

This proves that the sequence is strictly increasing.

2) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is bounded above, for instance that $a_n\leq3$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=1\leq3$, which is true.

Assuming that $a_k\leq4$ for certain value of $k$ we obtain $-a_k\geq-4$ and $-\displaystyle\frac{1}{a_k}\leq-\frac{1}{4}$ and therefore

$$
a_{k+2}=4-\frac{1}{a_k}\leq4-\frac{1}{4}\leq4.
$$

This proves that the sequence is bounded above by $4$.

3) Since the sequence is strictly increasing and bounded above, we conclude that the sequence is convergent. So: $L=\lim\limits_{n\to\infty}a_n$ exists and must satisfy

\begin{align*}
L=4-\frac{1}{L}\quad\Longrightarrow\quad L^2=4L-1&\quad\Longleftrightarrow\quad L^2-4L+1=0\\
&\quad\Longleftrightarrow\quad (L-2)^2=3.
\end{align*}
Hence: $L=2+\sqrt{3}$ or $L=2-\sqrt{3}$. Since $a_2=3$ and the sequence is strictly increasing, we conclude that $L=2+\sqrt{3}$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise6
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=3$ and $a_{n+1}=\dfrac{1}{4-a_n}$ is convergent and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise6`
:class: solution, dropdown
1) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is strictly decreasing: $a_{n+1}<a_n$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_2=\dfrac{1}{4-3}=1<3=a_1$ which is true.

Assuming that $a_{k+1}<a_k$ for certain value of $k$ we obtain $4-a_{k+1}>4-a_k$ and $\displaystyle\frac{1}{4-a_{k+1}}<\frac{1}{4-a_k}$ and therefore

$$
a_{k+2}=\frac{1}{4-a_{k+1}}<\frac{1}{4-a_k}=a_{k+1}.
$$

This proves that the sequence is strictly decreasing.

2) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is bounded below, for instance that $a_n\geq0$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=3\geq0$, which is true.

Assuming that $a_k\geq0$ for certain value of $k$ we obtain $4-a_k\leq4$ and $\displaystyle\frac{1}{4-a_k}\geq\frac{1}{4}$ and therefore

$$
a_{k+2}=\frac{1}{4-a_k}\geq\frac{1}{4}\geq0.
$$

This proves that the sequence is bounded below by $0$.

3) Since the sequence is strictly decreasing and bounded below, we conclude that the sequence is convergent. So: $L=\lim\limits_{n\to\infty}a_n$ exists and must satisfy

\begin{align*}
L=\frac{1}{4-L}\quad\Longrightarrow\quad 4L-L^2=1&\quad\Longleftrightarrow\quad L^2-4L+1=0\\
&\quad\Longleftrightarrow\quad (L-2)^2=3.
\end{align*}
Hence: $L=2+\sqrt{3}$ or $L=2-\sqrt{3}$. Since $a_1=3$ and $a_2=1$ and the sequence is strictly decreasing, we conclude that $L=2-\sqrt{3}$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise7
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=1$ and $a_{n+1}=\sqrt{1+2a_n}$ is convergent and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise7`
:class: solution, dropdown
1) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is strictly increasing: $a_{n+1}>a_n$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_2=\sqrt{3}>1=a_1$ which is true.

Assuming that $a_{k+1}>a_k$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{1+2a_{k+1}}>\sqrt{1+2a_k}=a_{k+1}.
$$

This proves that the sequence is strictly increasing.

2) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is bounded above, for instance that $a_n\leq5$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=1\leq5$, which is true.

Assuming that $a_k\leq5$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{1+2a_{k+1}}\leq\sqrt{1+10}\leq5.
$$

This proves that the sequence is bounded above by $5$.

3) Since the sequence is strictly increasing and bounded above, we conclude that the sequence is convergent. So: $L=\lim\limits_{n\to\infty}a_n$ exists and must satisfy

\begin{align*}
L=\sqrt{1+2L}\quad\Longrightarrow\quad L^2=1+2L&\quad\Longleftrightarrow\quad L^2-2L-1=0\\
&\quad\Longleftrightarrow\quad(L-1)^2=2.
\end{align*}
Hence: $L=1+\sqrt{2}$ or $L=1-\sqrt{2}$. Since $a_1=1$ and the sequence is strictly increasing, we conclude that $L=1+\sqrt{2}$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise8
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=3$ and $a_{n+1}=\sqrt{15+2a_n}$ is convergent and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise8`
:class: solution, dropdown
1) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is strictly increasing: $a_{n+1}>a_n$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_2=\sqrt{21}>3=a_1$ which is true.

Assuming that $a_{k+1}>a_k$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{15+2a_{k+1}}>\sqrt{15+2a_k}=a_{k+1}.
$$

This proves that the sequence is strictly increasing.

2) Using {prf:ref}`mathematical induction <Thm:Algebra:MathematicalInduction>` we prove that the sequence is bounded above, for instance that $a_n\leq10$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=3\leq10$, which is true.

Assuming that $a_k\leq10$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{15+2a_{k+1}}\leq\sqrt{15+10}\leq10.
$$

This proves that the sequence is bounded above by $10$.

3) Since the sequence is strictly increasing and bounded above, we conclude that the sequence is convergent. So: $L=\lim\limits_{n\to\infty}a_n$ exists and must satisfy

\begin{align*}
L=\sqrt{15+2L}\quad\Longrightarrow\quad L^2=15+2L&\quad\Longleftrightarrow\quad L^2-2L-15=0\\
&\quad\Longleftrightarrow\quad(L-5)(L+3)=0.
\end{align*}
Hence: $L=5$ or $L=-3$. Since $a_1=3$ and the sequence is increasing, we conclude that $L=5$.
:::