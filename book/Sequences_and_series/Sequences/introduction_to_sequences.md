# Sequences and their types

In this section we cover:

- Notation of sequences
- Sequences defined by a formula for general term a_n
- Recursively defined sequences
- Examples of common sequences (arithmetic, geometric, Fibonacci, harmonic)

::::::{prf:definition}
:label: Def:Sequences:Definition
A **sequence** $\{a_n\}_{n=1}^{\infty}$ is an ordered list of (real) numbers $a_1,a_2,a_3,\ldots$. 
::::::

::::::{note}
The number $a_n$ is called the $n$th *term* of the sequence. Sequences always have an infinite number of terms. The first *index* needs not to be $1$; it might be convenient to start the sequence with $a_0$ for instance.

Sometimes we just write $\{a_n\}$ to denote a sequence.
::::::

::::::{prf:example} Examples of sequences
1) $1,2,3,4,5,\ldots$ is the sequence of positive integers $\{a_n\}_{n=1}^{\infty}$ with $a_n=n$ for $n=1,2,3,\ldots$.

2) $1,\frac{1}{4},\frac{1}{9},\frac{1}{16},\frac{1}{25},\ldots$ is the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\displaystyle\frac{1}{n^2}$ for $n=1,2,3,\ldots$.

3) $\frac{1}{2},\frac{2}{5},\frac{3}{10},\frac{4}{17},\frac{5}{26},\ldots$ is the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\displaystyle\frac{n}{n^2+1}$ for $n=1,2,3,\ldots$.

4) $1,-\frac{1}{2},\frac{1}{4},-\frac{1}{8},\frac{1}{16},-\frac{1}{32},\ldots$ is the sequence $\{a_n\}_{n=0}^{\infty}$ with $a_n=\displaystyle\frac{(-1)^n}{2^n}$ for $n=0,1,2,\ldots$.

5) The sequence $\{a_n\}_{n=1}^{\infty}$ defined by $a_{n+2}=a_n+a_{n+1}$ with $n=1,2,3,\ldots$ and $a_1=a_2=1$ is called the **Fibonacci sequence**:

$$
1,1,2,3,5,8,13,21,34,55,89,\ldots.
$$

::::::

::::::{prf:definition}
:label: Def:Sequences:ArithmeticSequence
A sequence is called an **arithmetic sequence** if the difference between two consecutive terms is always the same. This difference is called the **common difference**. 
::::::

::::::{prf:example} Examples of arithmetic sequences
1) The sequence of positive integers $1,2,3,4,5,\ldots$ is an arithmetic sequence with common difference $1$.

2) The sequence $1,3,5,7,9,\ldots$ is an arithmetic sequence with common difference $2$.

3) The sequence $3,1,-1,-3,-5,\ldots$ is an arithmetic sequence with common difference $-2$.
::::::

::::::{note}
Let $\{a_n\}_{n=1}^{\infty}$ be an arithmetic sequence with common difference $d$ and first term $a_1=a$.

Then it can be defined by the *explicit formula* $a_n=a+(n-1)d$ for $n=1,2,3,\ldots$.

It can also be defined by the *recursive formula* $a_1=a$ and $a_{n+1}=a_n+d$ for $n=1,2,3,\ldots$.
::::::

::::::{prf:definition}
:label: Def:Sequences:HarmonicSequence
A sequence is called a **harmonic sequence** if the reciprocals of its terms form an arithmetic sequence. 
::::::

::::::{prf:example} Examples of harmonic sequences
1) The sequence $1,\frac{1}{2},\frac{1}{3},\frac{1}{4},\frac{1}{5},\ldots$ is a harmonic sequence.

2) The sequence $1,\frac{1}{3},\frac{1}{5},\frac{1}{7},\frac{1}{9},\ldots$ is a harmonic sequence.

3) The sequence $\frac{1}{3},1,-1,-\frac{1}{3},-\frac{1}{5},\ldots$ is a harmonic sequence.
::::::

::::::{prf:definition}
:label: Def:Sequences:GeometricSequence
A sequence is called a **geometric sequence** if each term, except for the first one, is obtained by multiplying the previous term by a fixed nonzero number, called the **common ratio**. 
::::::

::::::{prf:example} Examples of geometric sequences
1) The sequence $1,2,4,8,16,\ldots$ is a geometric sequence with common ratio $2$.

2) The sequence $1,\frac{1}{2},\frac{1}{4},\frac{1}{8},\frac{1}{16},\ldots$ is a geometric sequence with common ratio $\frac{1}{2}$.

3) The sequence $-1,1,-1,1,-1,\ldots$ is a geometric sequence with common ratio $-1$.
::::::

::::::{note}
Let $\{a_n\}_{n=1}^{\infty}$ be a geometric sequence with common ratio $r$ and first term $a_1=a$.

Then it can be defined by the *explicit formula* $a_n=ar^{n-1}$ for $n=1,2,3,\ldots$.

It can also be defined by the *recursive formula* $a_1=a$ and $a_{n+1}=ra_n$ for $n=1,2,3,\ldots$.
::::::

::::::{prf:definition}
:label: Def:Sequences:AlternatingSequence
A sequence $\{a_n\}_{n=1}^{\infty}$ is called an **alternating sequence** if $a_na_{n+1}<0$ for all $n=1,2,3,\ldots$, id est if every two consecutive terms have opposite signs. 
::::::

::::::{prf:example} Examples of alternating sequences
1) The sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\cos(n\pi)$ is an alternating sequence.

2) The sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=(-1)^{n-1}2^n$ is an alternating sequence.

3) The sequence $1,-\frac{1}{2},\frac{1}{3},-\frac{1}{4},\frac{1}{5},\ldots$ is an alternating sequence.
::::::

## The Fibonacci sequence

::::::{prf:definition} The Fibonacci numbers
:label: Def:Sequences:FibonacciSequence
The **Fibonacci sequence** $1,1,2,3,5,8,13,21,34,55,89,\ldots$ is defined by

$F_{n+2}=F_n+F_{n+1}$ for $n=1,2,3,\ldots$ with $F_1=F_2=1$.
::::::

::::::{note}
For computational reasons we use

$F_{n+2}=F_n+F_{n+1}$ for $n=0,1,2,\ldots$ with $F_0=0$ and $F_1=1$.

This is called a **recurrence relation** for the **Fibonacci numbers**, which are named after [Fibonacci or Leonardo of Pisa (c. 1170 – c. 1240–50)](https://en.wikipedia.org/wiki/Fibonacci).
::::::

::::::{topic} Question
What is $F_{100}$ (for instance) or what is $F_n$ for arbitrary $n$?
::::::

::::::{topic} Solution
The equation

$$
F_{n+2}=F_n+F_{n+1}\quad\Longleftrightarrow\quad F_{n+2}-F_{n+1}-F_n=0
$$

is called a *difference equation*. In this case a linear difference equation with constant coefficients. The theory of these linear difference equations with constant coefficients is similar to the theory of linear differential equations with constant coefficients. Try to find a solution of the form $F_n=r^n$ for certain $r\in\mathbb{R}$, then we have: 

$$
r^{n+2}-r^{n+1}-r^n=0\quad\Longleftrightarrow\quad r^n(r^2-r-1)=0.
$$

If we assume that $r\neq0$, then we have: $r^2-r-1=0$. This is (also) called an auxiliary equation. This auxiliary equation has two (different) real solutions:

$$
r^2-r-1=0\quad\Longrightarrow\quad r=\frac{1\pm\sqrt{5}}{2}.
$$

Due to the linearity (the principle of superposition) it follows that

$$
F_n=c_1\left(\frac{1+\sqrt{5}}{2}\right)^n+c_2\left(\frac{1-\sqrt{5}}{2}\right)^n,\quad n=0,1,2,\ldots
$$

is the general solution of the second-order difference equation. Now we use the initial conditions 
$F_0=0$ and $F_1=1$ to find that

$$
c_1+c_2=0\quad\text{and}\quad c_1\left(\frac{1+\sqrt{5}}{2}\right)+c_2\left(\frac{1-\sqrt{5}}{2}\right)=1.
$$

Hence:

$$
\begin{cases}c_1+c_2=0\\c_1(1+\sqrt{5})+c_2(1-\sqrt{5})=2\end{cases}\quad\Longleftrightarrow\quad\begin{cases}c_1+c_2=0\\c_1\sqrt{5}-c_2\sqrt{5}=2\end{cases}
$$

which implies that $c_1=\displaystyle\frac{1}{\sqrt{5}}$ and $c_2=-\displaystyle\frac{1}{\sqrt{5}}$.

Hence we have

\begin{align*}
F_n&=\frac{1}{\sqrt{5}}\left(\frac{1+\sqrt{5}}{2}\right)^n-\frac{1}{\sqrt{5}}\left(\frac{1-\sqrt{5}}{2}\right)^n\\
&=\frac{(1+\sqrt{5})^n-(1-\sqrt{5})^n}{2^n\sqrt{5}},\quad n=0,1,2,\ldots.
\end{align*}
This formula is remarkable since all numbers in the Fibonacci sequence are integers. In this formula this is far from evident. However we have for instance:

$$
F_{100}=\frac{(1+\sqrt{5})^{100}-(1-\sqrt{5})^{100}}{2^{100}\sqrt{5}}=354224848179261915075.
$$

The number $\varphi=\displaystyle\frac{1+\sqrt{5}}{2}\approx1.618$ is also known as the **golden ratio**. Now we have

$$
F_n=\frac{\varphi^n-(1-\varphi)^n}{\sqrt{5}},\quad n=0,1,2,\ldots.
$$

::::::

::::::{note}
The *golden ratio* $\displaystyle\varphi=\lim_{n\to\infty}\frac{F_{n+1}}{F_n}$ often appears in nature:

```{figure} Images/fibonacci1.png
---
width: 45%
name: Fibonacci1
align: left
---
$\varphi=\lim\limits_{n\to\infty}\dfrac{F_{n+1}}{F_n}$ in nature
```
```{figure} Images/fibonacci2.png
---
width: 45%
name: Fibonacci2
align: right
---
$\varphi=\lim\limits_{n\to\infty}\dfrac{F_{n+1}}{F_n}$ in nature
```

Plaatjes naast elkaar

In order to prove that $\displaystyle\lim\limits_{n\to\infty}\frac{F_{n+1}}{F_n}=\varphi$ we use the fact that 

$$
-1<\frac{1-\varphi}{\varphi}=\frac{1-\sqrt{5}}{1+\sqrt{5}}<0
$$ 

to obtain

\begin{align*}
\lim\limits_{n\to\infty}\frac{F_{n+1}}{F_n}&=\lim\limits_{n\to\infty}\frac{\varphi^{n+1}+(1-\varphi)^{n+1}}{\varphi^n+(1-\varphi)^n}
=\lim\limits_{n\to\infty}\frac{\varphi+(1-\varphi)\left(\frac{1-\varphi}{\varphi}\right)^n}{1+\left(\frac{1-\varphi}{\varphi}\right)^n}\\
&=\frac{\varphi+0}{1+0}=\varphi.
\end{align*}
*Remark*: $\varphi=\dfrac{1+\sqrt{5}}{2}\approx1.618$, $\displaystyle\frac{1}{\varphi}=\varphi-1=\frac{\sqrt{5}-1}{2}\approx0.618$ and $\dfrac{1-\varphi}{\varphi}\approx-0.382$.
::::::

::::{exercise} The Lucas numbers
:label: Exc:Sequences:Lucas
The **Lucas sequence** $1,3,4,7,11,18,29,47,76,123,\ldots$ is defined by

$L_{n+2}=L_n+L_{n+1}$ for $n=1,2,3,\ldots$ with $L_1=1$ and $L_2=3$.

The **Lucas numbers**, named after the French mathematician [François Édouard Anatole Lucas (1842-1891)](https://en.wikipedia.org/wiki/%C3%89douard_Lucas), satisfy the same recurrence relation as the *Fibonacci numbers* with different initial values.

An alternative definition is: 

$L_{n+2}=L_n+L_{n+1}$ for $n=0,1,2,\ldots$ with $L_0=2$ and $L_1=1$.

Find a general formula for $L_n$ with $n=0,1,2,\ldots$ and show that $\displaystyle\lim_{n\to\infty}\frac{L_{n+1}}{L_n}=\varphi$.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:Lucas`
:class: solution, dropdown
Since the Lucas numbers satisfy the same recurrence relation as the Fibonacci numbers, we have the same general solution

$$
L_n=c_1\left(\frac{1+\sqrt{5}}{2}\right)^n+c_2\left(\frac{1-\sqrt{5}}{2}\right)^n,\quad n=0,1,2,\ldots.
$$

The initial values $L_0=2$ and $L_1=1$ imply that

$$
c_1+c_2=2\quad\text{and}\quad c_1\left(\frac{1+\sqrt{5}}{2}\right)+c_2\left(\frac{1-\sqrt{5}}{2}\right)=1.
$$

Hence:

$$
\begin{cases}c_1+c_2=2\\c_1(1+\sqrt{5})+c_2(1-\sqrt{5})=2\end{cases}\quad\Longleftrightarrow\quad\begin{cases}c_1+c_2=2\\c_1\sqrt{5}-c_2\sqrt{5}=0\end{cases}
$$

which implies that $c_1=c_2=1$.

Hence we have

$$
L_n=\left(\frac{1+\sqrt{5}}{2}\right)^n+\left(\frac{1-\sqrt{5}}{2}\right)^n,\quad n=0,1,2,\ldots.
$$

Again using the *golden ratio* $\varphi=\displaystyle\frac{1+\sqrt{5}}{2}$ we have

$$
L_n=\varphi^n+(1-\varphi)^n,\quad n=0,1,2,\ldots.
$$

Similarly as for the Fibonacci numbers we use that fact that 

$$
-1<\frac{1-\varphi}{\varphi}=\frac{1-\sqrt{5}}{1+\sqrt{5}}<0
$$ 

to obtain

\begin{align*}
\lim\limits_{n\to\infty}\frac{L_{n+1}}{L_n}&=\lim\limits_{n\to\infty}\frac{\varphi^{n+1}+(1-\varphi)^{n+1}}{\varphi^n+(1-\varphi)^n}
=\lim\limits_{n\to\infty}\frac{\varphi+(1-\varphi)\left(\frac{1-\varphi}{\varphi}\right)^n}{1+\left(\frac{1-\varphi}{\varphi}\right)^n}\\
&=\frac{\varphi+0}{1+0}=\varphi.
\end{align*}
:::

::::{exercise} Relations between Fibonacci and Lucas numbers
:label: Exc:Sequences:LucasFibonacci
We have seen that the Fibonacci numbers $\{F_n\}_{n=0}^{\infty}$ and the Lucas numbers $\{L_n\}_{n=0}^{\infty}$ can be written in terms of the golden ratio $\varphi=\dfrac{1+\sqrt{5}}{2}$:

$$
F_n=\frac{\varphi^n-(1-\varphi)^n}{\sqrt{5}}\quad\text{and}\quad L_n=\varphi^n+(1-\varphi)^n.
$$

(a) Show that $F_{2n}=F_nL_n$ for $n=0,1,2,\ldots$, which implies that $\dfrac{F_{2n}}{F_n}=L_n$ for $n=1,2,3,\ldots$.

(b) Use the relation $\varphi^2-\varphi-1=0$ to show that $\dfrac{1}{\varphi}+\varphi=2\varphi-1=\sqrt{5}$ and $\dfrac{1}{1-\varphi}=1-2\varphi$.

(c) Show that $F_{n-1}+F_{n+1}=L_n$ for $n=1,2,3,\ldots$.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:LucasFibonacci`
:class: solution, dropdown
(a) $F_nL_n=\displaystyle\frac{\varphi^n-(1-\varphi)^n}{\sqrt{5}}\cdot\frac{\varphi^n+(1-\varphi)^n}{1}=\frac{\varphi^{2n}-(1-\varphi)^{2n}}{\sqrt{5}}=F_{2n}$ for $n=0,1,2,\ldots$.

(b) We have: $\varphi^2-\varphi-1=0\;\Longleftrightarrow\;\varphi^2=\varphi+1\;\Longleftrightarrow\;\varphi=1+\dfrac{1}{\varphi}$.

This implies that $\dfrac{1}{\varphi}=\varphi-1\;\Longleftrightarrow\;\dfrac{1}{\varphi}+\varphi=2\varphi-1=1+\sqrt{5}-1=\sqrt{5}$ and 

$$
\frac{1}{1-\varphi}=-\varphi\;\Longleftrightarrow\;\dfrac{1}{1-\varphi}+1-\varphi=1-2\varphi.
$$

(c) For $n=1,2,3,\ldots$ we obtain

\begin{align*}
F_{n-1}+F_{n+1}&=\frac{\varphi^{n-1}-(1-\varphi)^{n-1}}{\sqrt{5}}+\frac{\varphi^{n+1}-(1-\varphi)^{n+1}}{\sqrt{5}}\\
&=\frac{\varphi^{n-1}+\varphi^{n+1}-(1-\varphi)^{n-1}-(1-\varphi)^{n+1}}{\sqrt{5}}\\
&=\frac{\varphi^n\left(\dfrac{1}{\varphi}+\varphi\right)-(1-\varphi)^n\left(\dfrac{1}{1-\varphi}+1-\varphi\right)}{\sqrt{5}}\\
&=\varphi^n+(1-\varphi)^n=L_n.
\end{align*}
:::

::::::{admonition} Collatz sequences (bonus material)
:class: solution, dropdown
Consider the **Collatz sequence** defined by $a_1=N$ and $a_{n+1}=\begin{cases}a_n/2 &\text{if }a_n \text{ is even}\\3a_n+1 &\text{if } a_n \text{ is odd.}\end{cases}$

For every choice of $N\in\{1,2,3,\ldots\}$ we obtain a different sequence.

These *Collatz sequences* are named after the German mathematician [Lothar Collatz (1910-1990)](https://en.wikipedia.org/wiki/Lothar_Collatz).

For $N=1$ we obtain: $\{1,4,2,1,4,2,1,\ldots\}$. Hence, we end up in the cycle $\{4,2,1\}$, which is clearly also the case for $N=2$ and $N=4$.

For $N=6$ we obtain: $\{6,3,10,5,16,8,4,2,1,4,2,1,\ldots\}$ and we end up in the same cycle, which also holds for $N=3$, $N=5$, $N=8$ and $N=10$ for instance.

For $N=9$ we obtain: $\{9,28,14,7,22,11,32,16,8,4,2,1,4,2,1,\ldots\}$ and we end up in the same cycle, which also holds for $N=7$ for instance.

This gives rise to the **Collatz conjecture**: *for every choice of $N$ we eventually end up in the cylce $\{4,2,1\}$*.

This Collatz conjecture is still an open, unsolved, problem in mathematics.
::::::
