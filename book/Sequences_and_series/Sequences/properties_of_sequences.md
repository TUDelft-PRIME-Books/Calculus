(Sec:PropertiesOfSequences)=
# Properties of sequences

## Introduction

In the previous section we have seen that a sequence is an ordered list of numbers. We have also seen that there are many different types of sequences, such as arithmetic, geometric, harmonic and alternating sequences. These sequences have different properties, such as being increasing or decreasing, being bounded above or below, and so on. In this section we will study these properties in more detail.

## Increasing and decreasing sequences

Consider the following sequences:

$$
\begin{array}{rcl}
\{a_n\}_{n=1}^{\infty} & \text{with} & a_n=\dfrac{n}{2}, \\
\{b_n\}_{n=1}^{\infty} & \text{with} & b_n=\dfrac{5}{n^2}, \\
\{c_n\}_{n=1}^{\infty} & \text{with} & c_n=\dfrac{5}{2}+\cos(n\pi).
\end{array}
$$

Although these sequences are all infinite, we can graph several of their terms to get a better understanding of their behaviour.

```{figure} Images/Fig-PropertiesOfSequences-Introduction.png
:name: Fig:PropertiesOfSequences:Introduction
:class: dark-light

The first 10 terms of the sequences $\{a_n\}$, $\{b_n\}$ and $\{c_n\}$ are plotted in the graph above.
```

:::{todo}
Make an applet from {numref}`Fig:PropertiesOfSequences:Introduction` that allows the user to change the number of terms plotted and to zoom in and out.

The applet should have a parameter in the url to set the initial number of terms shown.
:::

As you can see, the terms of the sequence $\{a_n\}$ seem to keep going up, the terms of the sequence $\{b_n\}$ seem to keep going down, but are staying above zero,  and the terms of the sequence $\{c_n\}$ seem the switch between two values. These observations can also be described using some terminology, which we will define next:

::::{prf:definition}
:label: Def:PropertiesOfSequences:Affirming

A sequence is called **strictly increasing** if the difference between consecutive terms is always positive.

A sequence is called **decreasing** if the difference between consecutive terms is always negative.

A sequence is called **ultimately increasing** if there is a term after which the sequence is increasing.

A sequence is called **ultimately decreasing** if there is a term after which the sequence is decreasing.

::::

As sometimes symbols feel better than words, we can also give you the next theorem.

::::::{prf:theorem}
:label: Thm:PropertiesOfSequences:Affirming

A sequence $\{a_n\}_{n=p}^{\infty}$ is **strictly increasing** if and only if $a_n < a_{n+1}$ for all $n\geq p$.

A sequence $\{a_n\}_{n=p}^{\infty}$ is **strictly decreasing** if and only if $a_n > a_{n+1}$ for all $n\geq p$.

A sequence $\{a_n\}_{n=p}^{\infty}$ is **ultimately increasing** if and only if there exists a number $N\geq p$ such that $a_n < a_{n+1}$ for all $n\geq N$.

A sequence $\{a_n\}_{n=p}^{\infty}$ is **ultimately decreasing** if and only if there exists a number $N\geq p$ such that $a_n > a_{n+1}$ for all $n\geq N$.

::::::

Next to the affirming definitions of {prf:ref}`Def:PropertiesOfSequences:Affirming`, we also have several invalidating definitions, with a corresponding theorem.

::::{prf:definition}
:label: Def:PropertiesOfSequences:Invalidating

A sequence is called **non-increasing** if the difference between consecutive terms is always non-positive.

A sequence is called **non-decreasing** if the difference between consecutive terms is always non-negative.
::::

::::::{prf:theorem}
:label: Thm:PropertiesOfSequences:Invalidating

A sequence $\{a_n\}_{n=p}^{\infty}$ is **non-increasing** if and only if $a_n \geq a_{n+1}$ for all $n\geq p$.

A sequence $\{a_n\}_{n=p}^{\infty}$ is **non-decreasing** if and only if $a_n \leq a_{n+1}$ for all $n\geq p$.

::::::

Because of the similarity of the behavior of (non)-decreasing and (non-)increasing sequences, we will often use the term *monotonic* to refer to both of these types of sequences:

::::{prf:definition}
:label: Def:PropertiesOfSequences:Monotonic

A sequence is called **monotonic** if it is either non-increasing or non-decreasing.

A sequence is called **non-monotonic** if it is not monotonic, which means that it is neither non-increasing nor non-decreasing.
::::

Let us revisit the three sequences we introduced at the beginning of this section:

::::{prf:example}
:label: Ex:PropertiesOfSequences:Example1

We look at the difference between two consecutive terms in the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{n}{2}$:

$$
a_{n+1} - a_n = \dfrac{n+1}{2} - \dfrac{n}{2} = \dfrac{1}{2}>0.
$$

As this difference is always positive, we conclude that the sequence $\{a_n\}$ is _strictly increasing_.
::::

::::{prf:example}
:label: Ex:PropertiesOfSequences:Example2

We look at the difference between two consecutive terms in the sequence $\{b_n\}_{n=1}^{\infty}$ with $b_n=\dfrac{5}{n^2}$:

\begin{align*}
b_{n+1} - b_n &= \dfrac{5}{(n+1)^2} - \dfrac{5}{n^2} \\
&= \dfrac{5n^2}{(n+1)^2n^2} - \dfrac{5(n+1)^2}{(n+1)^2n^2} \\
&= \dfrac{5n^2 - 5(n+1)^2}{(n+1)^2n^2} \\
&= \dfrac{5n^2 - 5(n^2+2n+1)}{(n+1)^2n^2} \\
&= \dfrac{-10n-5}{(n+1)^2n^2}.
\end{align*}

Because the denominator is always positive, the sign of this difference is determined by the numerator, which is always negative.

As this difference is always negative, we conclude that the sequence $\{b_n\}$ is _strictly decreasing_.
::::

::::{prf:example}
:label: Ex:PropertiesOfSequences:Example3

We look at the difference between two consecutive terms in the sequence $\{c_n\}_{n=1}^{\infty}$ with $c_n=\dfrac{5}{2}+\cos(n\pi)$:

\begin{align*}
c_{n+1} - c_n &= \left(\dfrac52+\cos((n+1)\pi)\right)-\left(\dfrac52+\cos(n\pi)\right) \\
&= \cos((n+1)\pi)-\cos(n\pi) \\
&= \cos(n\pi+\pi)-\cos(n\pi) \\
&= -\cos(n\pi)-\cos(n\pi) \\
&= -2\cos(n\pi) \\
&= -2(-1)^n.
\end{align*}

Because $(-1)^n$ is either $1$ or $-1$, the sign of this difference is alternating between positive and negative.

We must conclude that the sequence $\{c_n\}$ is *non-monotonic*, as it is neither non-increasing nor non-decreasing.
::::

For several of the common types of sequences of {numref}`Sec:SeqAndTypes:Types` we can easily determine whether they are strictly increasing, strictly decreasing or non-monotonic:

::::{prf:theorem}
:label: Thm:PropertiesOfSequences:CommonTypesBehaviour

- An *arithmetic* sequence is *strictly increasing* if the common difference $d$ is *positive*, and *strictly decreasing* if the common difference $d$ is *negative*.

- A *harmonic* sequence is *strictly decreasing* if the reciprocals of its terms form an *strictly increasing* arithmetic sequence, and *strictly increasing* if the reciprocals of its terms form a *strictly decreasing* arithmetic sequence.

- A *geometric* sequence is *strictly increasing* if its first term is positive and the common ratio $r>1$, or if its first term is negative and the common ratio $0<r<1$.

- A *geometric* sequence is *strictly decreasing* if its first term is positive and the common ratio $0<r<1$, or if its first term is positive and the common ratio $r>1$.

- An *alternating sequence* is always non-monotonic.
::::

For sequence that are not of the common type, it sometimes is harder to show whether they are strictly increasing, strictly decreasing, monotonic or one of the other classifications, as the next examples show.

::::::{prf:example}
:label: Ex:Sequences:IncreasingExample1
We show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{n}{n+1}$ is strictly increasing.

To do so, we want to show that $\dfrac{n}{n+1}<\dfrac{n+1}{n+2}$ for all $n=1,2,3,\ldots$.

Since $n>0$ this is equivalent to showing that

$$
n(n+2)<(n+1)^2\;\Longleftrightarrow\;n^2+2n<n^2+2n+1.
$$

The last inequality reduces to $0<1$, which definitely is true. This shows that the sequence is *strictly increasing*.

::::::

::::::{prf:example}
:label: Ex:Sequences:UltimateIncreasingExample

Consider the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{n^2}{2^n}$. Then the first terms are

$$
\frac{1}{2},\quad1,\quad\frac{9}{8},\quad1,\quad\frac{25}{32},\quad\frac{9}{16},\quad\frac{49}{128},\quad\ldots
$$

Although the first two pairs of consecutive terms have a positive difference, the next pairs of consecutive terms have a negative difference. So this sequence is non-monotonic, but it might be ultimately decreasing.

To investigate this, we consider the ratio between two consecutive terms:

\begin{align*}
\dfrac{a_{n+1}}{a_n} &= \dfrac{(n+1)^2}{2^{n+1}}\cdot\dfrac{2^{n}}{n^2} \\
&= \dfrac{2^n}{2^{n+1}}\cdot\dfrac{(n+1)^2}{n^2} \\
&= \dfrac{1}{2}\cdot\dfrac{(n+1)^2}{n^2}.
\end{align*}

If this sequence would be ultimately decreasing, then we should be able to find an integer $N\geq 1$ such $\dfrac{1}{2}\cdot\dfrac{(n+1)^2}{n^2}<1$ for all $n\geq N$. We will solve this inequality to find such an integer $N$:

\begin{align*}
&~ & \dfrac{1}{2}\cdot\dfrac{(n+1)^2}{n^2} &< 1  \\
&\Rightarrow & \dfrac{(n+1)^2}{n^2} &< 2 \\
&\Rightarrow & (n+1)^2 &< 2n^2 \\
&\Rightarrow & n^2 + 2n + 1 &< 2n^2 \\
&\Rightarrow & 2n + 1 &< n^2 \\
&\Rightarrow & 0 &< n^2 - 2n - 1.
\end{align*}

The quadratic expression on the right of the last equality would be zero if $n=1-\sqrt{2}\approx -0.414<0$ or if $n=1+\sqrt{2}\approx 2.414>0$. Since $n$ is a positive integer, we conclude that $n^2 - 2n - 1>0$ for all $n\geq3$. Hence, we have $\dfrac{1}{2}\cdot\dfrac{(n+1)^2}{n^2}<1$ for all $n\geq3$.

This means that this sequence is indeed *ultimately decreasing* (for $n\geq3$).
::::::

::::::{prf:example}
:label: Ex:Sequences:IncreasingExample2
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{2n}{n^2+1}$.

We will show that $\dfrac{2n}{n^2+1}>\dfrac{2(n+1)}{(n+1)^2+1}$ for all $n=1,2,3,\ldots$.

Note that

$$
\begin{array}{rclcrcl}
\frac{2n}{n^2+1} & > & \frac{2n+2}{n^2+2n+2} & \Longleftrightarrow & 2n(n^2+2n+2) & > & (2n+2)(n^2+1)\\
&&& \Longleftrightarrow & 2n^3+4n^2+4n & > & 2n^3+2n^2+2n+2\\
&&& \Longleftrightarrow & 2n^2+2n & > & 2\\
&&& \Longleftrightarrow & n(n+1) & > & 1.
\end{array}
$$

This is true for $n\geq1$, so the sequence is *strictly increasing*.

::::::

Solving or reducing these inequalities can sometimes be hard, but luckily we can do this also in another way.

In {numref}`Fig:PropertiesOfSequences:Functions` we show the sequences from {numref}`Fig:PropertiesOfSequences:Introduction`, being

$$
\begin{array}{rcl}
\{a_n\}_{n=1}^{\infty} & \text{with} & a_n=\dfrac{n}{2}, \\
\{b_n\}_{n=1}^{\infty} & \text{with} & b_n=\dfrac{5}{n^2}, \\
\{c_n\}_{n=1}^{\infty} & \text{with} & c_n=\dfrac{5}{2}+\cos(n\pi),
\end{array}
$$

but also the functions $f$, $g$ and $h$ defined by

$$
\begin{array}{rcl}
f(n) & = & \dfrac{n}{2}, \\
g(n) & = & \dfrac{5}{n^2}, \\
h(n) & = & \dfrac{5}{2}+\cos(n\pi).
\end{array}
$$

```{figure} Images/Fig-PropertiesOfSequences-Functions.png
:name: Fig:PropertiesOfSequences:Functions
:class: dark-light

The first 10 terms of the sequences $\{a_n\}$, $\{b_n\}$ and $\{c_n\}$ are plotted in the graph above, including the three functions $f$, $g$ and $h$ associated with these sequences.
```

:::{todo}
Make an applet from {numref}`Fig:PropertiesOfSequences:Functions` that allows the user to change the number of terms plotted and to zoom in and out.

The applet should have a parameter in the url to set the initial number of terms shown.
:::

As you can see, the function $f$, just like the sequence $\{a_n\}$, is strictly increasing. Even better, the function $g$ is strictly decreasing, similar to how the sequence $\{b_n\}$ is strictly decreasing. Finally, the non-monotonic nature of the sequence $\{c_n\}$ is also reflected in the function $h$.

This relation between sequences and functions can be formalised in the next theorem:

::::{prf:theorem}
:label: Thm:PropertiesOfSequences:Functions

Let $\{a_n\}_{p}^{\infty}$ be a sequence and $f:\mathbb{R}\rightarrow\mathbb{R}$ a function such that $f(n)=a_n$ for $n=p,p+1,p+2,\ldots$

- If $f$ is a strictly increasing function for $x\geq p$, then $\{a_n\}_{p}^{\infty}$ is a strictly increasing sequence.

- If $f$ is a strictly decreasing function for $x\geq p$, then $\{a_n\}_{p}^{\infty}$ is a strictly decreasing sequence.

- If $f$ is a monotonic function for $x\geq p$, then $\{a_n\}_{p}^{\infty}$ is a monotonic sequence.

- If $f$ is a strictly increasing function for $x\geq N>p$ for some integer $N$, then $\{a_n\}_{p}^{\infty}$ is an ultimately increasing sequence (for $n\geq N$).

- If $f$ is a strictly decreasing function for $x\geq N>p$ for some integer $N$, then $\{a_n\}_{p}^{\infty}$ is an ultimately decreasing sequence (for $n\geq N$).

::::

::::{warning}
:name: Warn:PropertiesOfSequences:Functions

Note that this theorem only states a relation between the affirmative properties of functions and sequences. For the invalidating properties of {prf:ref}`Def:PropertiesOfSequences:Invalidating` no such theorem exists.

::::

::::::{prf:example}
:label: Ex:Sequences:IncreasingExample1Function
We show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{n}{n+1}$ is increasing by looking at an appropriate function:

```{figure} Images/sequence1.png
---
width: 50%
name: Fig:Sequences:IncreasingExample1Function
align: center
---
The terms of the sequence $\{a_n\}$ lie on the graph of $f(x)=\dfrac{x}{x+1}$.
```

:::{todo}
Replace {numref}`Fig:Sequences:IncreasingExample1Function` by an applet.
:::

Note that $a_n=f(n)$ if we (simply) choose $f(x)=\dfrac{x}{x+1}$. Now we have

$$
f'(x)=\frac{x+1-x}{(x+1)^2}=\frac{1}{(x+1)^2}>0.
$$

This implies that $f$ is strictly increasing and therefore that the sequence increases strictly also.
::::::

::::::{prf:example}
:label: Ex:Sequences:IncreasingExample2Function
We show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{2n}{n^2+1}$ is decreasing.

```{figure} Images/sequence2.png
---
width: 50%
name: Fig:Sequences:IncreasingExample2Function
align: center
class: dark-light
---
The terms of the sequence $\{a_n\}$ lie on the graph of $f(x)=\dfrac{2x}{x^2+1}$.
```

:::{todo}
Replace {numref}`Fig:Sequences:IncreasingExample2Function` by an applet.
:::


Note that $a_n=f(n)$ if $f(x)=\dfrac{2x}{x^2+1}$. Then we have

$$
f'(x)=\frac{2(x^2+1)-2x\cdot2x}{(x^2+1)^2}=\frac{2(1-x^2)}{(x^2+1)^2},
$$

which is negative for $x>1$. This implies that $f$ is strictly decreasing on $(1,\infty)$ and so $f(n)>f(n+1)$. Therefore $\{a_n\}$ is strictly decreasing.
::::::

If a sequence is defined by a recursive formula, it is often somewhat more difficult to show any of the properties. This is of course not always, as in the next example:

::::::{prf:example}
:label: Ex:PropertiesOfSequences:Fibonacci
We revisit the Fibonacci sequence from {numref}`Sec:SeqAndTypes:Fibonacci`: $\{F_n\}_{n=1}^{\infty}$ with $F_1=1$, $F_2=1$ and $F_{n+2}=F_{n+1}+F_n$ for $n=1,2,3,\ldots$

The first few terms of the Fibonacci sequence are

$$
1,1,2,3,5,8,13,21,34,55,89,\ldots
$$

from which we can see that after the second term it seems to keep increasing. We take a look at the difference of two consecutive terms, with $n\geq1$:

$$
F_{n+2} - F_{n+1} = \left(F_{n+1}+F_n\right)-F_{n+1} = F_n.
$$

Because we start with two positive numbers, and keep adding these positive numbers, every term in the Fibonacci sequence will be positive. But this means that two consecutive terms will have a positive difference number as soon as we are allowed to use the recursive formula.

This is the case if $n\geq1$, and indeed we see that $F_3-F_2 = 2 - 1 = 1 > 0$. This results in the conclusion that $F_2<F_3$, $F_3<F_4$ and so on. In conclusion we can say that the Fibonacci sequence is *ultimately increasing*. Because this occurs for $n\geq2$, and $F_1=F_2$, we can also say that the Fibonacci sequence is *non-decreasing*.

::::::

In many other situations the principle of mathematical induction might be helpful, which we now state:

::::::{prf:theorem} Mathematical induction
:label: Thm:SeqAndTypes:MathInduction

Let $S_n$ be a statement for all integers $n$ larger than or equal to $p$.

If 

1) $S_p$ is true,

and

2) $S_{k+1}$ is true whenever $S_k$ is true for a $k\geq p$,

then $S_n$ is true for all integers $n\geq p$.

::::::

::::::{note}
This procedure describes the *domino effect*. Since $S_p$ is true, the second condition with $k=p$ implies that $S_{p+1}$ is true as well. Then, using the second condition with $k=p+1$ we conclude that $S_{p+2}$ is true. Again, using the second condition with $k=p+2$, we conclude that $S_{p+3}$ is true. This procedure can be followed indefinitely.

More information about the principle of mathematical induction can be found in [Section 3.4. Mathematical Induction of the book Delftse Foundations of Computation](https://interactivetextbooks.tudelft.nl/delftse-foundations-of-computation/content/logic/induction.html).
::::::

::::::{prf:example}
:label: Ex:Sequences:RecurrenceExample1
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=1$ and $a_{n+1}=\frac{1}{2}(a_n+5)$ for $n=1,2,3,\ldots$. 

We will apply the principle of mathematical induction to show that the sequence increases strictly.

To do that, we first need to reformulate what we want to show. Using {prf:ref}`Thm:PropertiesOfSequences:Affirming`, we see that we must show that $a_n<a_{n+1}$ for all $n=1,2,3,\ldots$. So our statement $S_n$ is $a_n<a_{n+1}$.

First, consider $n=1$ (because $p=1$ for this sequence). So statement $S_1$ is $a_1<a_2$. Because we have $a_1=1$ and $a_2=3$, we also have $a_2-a_1=3-2=1$ and therefore $a_1<a_2$. This means our first statement $S_1$ is true.

Second, assume that the statement $S_k$ given by $a_k<a_{k+1}$ is true for a $k\geq 1$. Then we must show that the statement $S_{k+1}$ given by $a_{k+1}<a_{k+2}$ is also true, which we will do next:

$$
a_{k+1}=\frac{1}{2}(a_k+5)<\frac{1}{2}(a_{k+1}+5)=a_{k+2}.
$$

As this shows that $S_{k+1}$ is true if $S_{k}$ is true, we can conclude that our general statement $S_n$ is true for $n\geq 1$.

This shows that $a_n<a_{n+1}$ for all $n=1,2,3,\ldots$ and so the sequence is *strictly increasing*.
::::::

::::::{prf:example}
:label: Ex:Sequences:RecurrenceExample2
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=10$ and $a_{n+1}=\sqrt{a_n+6}$ for $n=1,2,3,\ldots$. 

We want to prove that $a_n>a_{n+1}$ for all $n=1,2,3,\ldots$.

We again use the principle of mathematical induction.

For $n=1$ we have $a_1=10>4=a_2$. So the first condition of {prf:ref}`Thm:SeqAndTypes:MathInduction` is satisfied.

Now, suppose that $a_k>a_{k+1}$ for a certain value of $k\geq1$, then we have

$$
a_{k+1}=\sqrt{a_k+6}>\sqrt{a_{k+1}+6}=a_{k+2}.
$$

This shows that $a_n>a_{n+1}$ for all $n=1,2,3,\ldots$ and so the sequence is *strictly decreasing*.
::::::

Even if a sequence is strictly increasing, strictly decreasing, non-increasing or non-decreasing, this does not mean that a sequence will always attain a very positive or a very negative value. This concept is called the boundedness of sequences, which we will discuss next. 

## Bounded sequences

Again we consider the same sequences as before:

$$
\begin{array}{rcl}
\{a_n\}_{n=1}^{\infty} & \text{with} & a_n=\dfrac{n}{2}, \\
\{b_n\}_{n=1}^{\infty} & \text{with} & b_n=\dfrac{5}{n^2}, \\
\{c_n\}_{n=1}^{\infty} & \text{with} & c_n=\dfrac{5}{2}+\cos(n\pi).
\end{array}
$$

{numref}`Fig:PropertiesOfSequences:Bounds` shows these sequences again, but now the first 50 terms:

```{figure} Images/Fig-PropertiesOfSequences-Bounds.png
:name: Fig:PropertiesOfSequences:Bounds
:class: dark-light

The first 50 terms of the sequences $\{a_n\}$, $\{b_n\}$ and $\{c_n\}$ are plotted in the graph above.
```

:::{todo}
Make an applet from {numref}`Fig:PropertiesOfSequences:Bounds` that allows the user to change the number of terms plotted and to zoom in and out.

The applet should have a parameter in the url to set the initial number of terms shown.
:::

In this figure, you can clearly see that the first sequence keeps on increasing and does not seem to stop. The other two sequences do stay within some bounds. Let us formalise these observations:

:::{prf:definition}
:label: Def:Sequences:Bounded

We define the follow affirming terms:

- A sequence $\{a_n\}_{n=p}^{\infty}$ is called **bounded above** if there exists a number $M$ such that $a_n\leq M$ for all $n\geq p$.

- A sequence $\{a_n\}_{n=p}^{\infty}$ is called **bounded below** if there exists a number $m$ such that $m\leq a_n$ for all $n\geq p$.

- A sequence is called **bounded** if it is *both bounded above and bounded below*.

We define the follow invalidating terms:

- A sequence is called **unbounded above** if it is *not bounded above*.

- A sequence is called **unbounded below** if it is *not bounded below*.

- A sequence is called **unbounded** if it is *either unbounded below or unbounded below*.

::::::

For several of the common types of sequences of {numref}`Sec:SeqAndTypes:Types` we can easily determine whether they are bounded above, bounded below or both.

::::{prf:theorem}
:label: Thm:PropertiesOfSequences:CommonTypesBounds

- An *arithmetic sequence* with a positive common difference is bounded below by the first term, but not bounded above.

- An *arithmetic sequence* with a negative common difference is bounded above by the first term, but not bounded below.

- A *geometric sequence* is bounded if the common ratio $r$ satisfies $|r|\leq 1$.

- A *geometric sequence* is neither bounded above nor bounded below if the common ratio $r$ satisfies $|r|>1$.
::::

The next example gives some quick examples of sequences and their bounds.

::::::{prf:example}
1) The sequence $1,2,3,4,5,\ldots$ of positive integers is *bounded below* with $m\leq1$ and *unbounded above*, making it also *unbounded*.

2) The geometric sequence $1,\frac{1}{2},\frac{1}{4},\frac{1}{8},\frac{1}{16},\ldots$ is *bounded above* with $M\geq1$ and *bounded below* with $m=0$, making it *bounded*.

3) The arithmetic sequence $5,3,1,-1,-3,\ldots$ is *bounded above* with $M\geq5$ and *unbounded below*, making it *unbounded* too.

4) The arithmetic sequence $1,3,5,7,9,\ldots$ is *bounded below* with $m\leq1$ and *unbounded above*, which makes another *unbounded* sequence.

5) The harmonic sequence $1,\frac{1}{2},\frac{1}{3},\frac{1}{4},\frac{1}{5},\ldots$ is *bounded* with $M\geq1$ and $m\leq0$.
::::::

::::::{prf:example}
:label: Ex:Sequences:BoundedExample1
We investigate wether the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{n}{n+1}$ has bounds.

```{figure} Images/sequence1.png
---
width: 50%
name: Fig:Sequences:BoundedExample1
align: center
class: dark-light
---
The terms of the sequence $\{a_n\}$ lie on the graph of $f(x)=\dfrac{x}{x+1}$.
```

:::{todo}
Replace {numref}`Fig:Sequences:BoundedExample1` by an applet.
:::

Note that $a_n=f(n)$ with $f(x)=\dfrac{x}{x+1}$. Now we have

$$
f'(x)=\frac{x+1-x}{(x+1)^2}=\frac{1}{(x+1)^2}>0.
$$

This implies that $f$ is increasing. Further we have $f(1)=\frac{1}{2}$ and $\lim\limits_{x\to\infty}f(x)=1$.

Hence, we have $\frac{1}{2}\leq f(x)<1$ for $x\geq1$.

This implies that the sequence is bounded with $M\geq1$ and $m\leq\frac{1}{2}$.

::::::

::::::{prf:example}
:label: Ex:Sequences:BoundedExample2
Now consider the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{2n}{n^2+1}$ and it's bounds.

```{figure} Images/sequence2.png
---
width: 50%
name: Fig:Sequences:BoundedExample2
align: center
class: dark-light
---
The terms of the sequence $\{a_n\}$ lie on the graph of $f(x)=\dfrac{2x}{x^2+1}$.
```

:::{todo}
Replace {numref}`Fig:Sequences:BoundedExample2` by an applet.
:::

Again we turn to a function $f$. In this case we choose $f(x)=\dfrac{2x}{x^2+1}$ so that $f(n)=a_n$ as required. Then we have

$$
f'(x)=\frac{2(x^2+1)-2x\cdot2x}{(x^2+1)^2}=\frac{2(1-x^2)}{(x^2+1)^2},
$$

which is negative for $x>1$. This implies that $f$ is decreasing on $(1,\infty)$. Further we have $f(1)=1$ and $\lim\limits_{x\to\infty}f(x)=0$.

Hence, we have $0<f(x)\leq1$ for $x\geq1$.

This implies that the sequence is bounded with $M\geq1$ and $m\leq0$.
::::::

::::::{prf:example}
:label: Ex:Sequences:BoundedExample3
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=1$ and $a_{n+1}=\frac{1}{2}(a_n+5)$ for $n=1,2,3,\ldots$. 

We show that the sequence is bounded above.

We want to prove that $a_n<M$ for some number $M$ for all $n=1,2,3,\ldots$. Let's take $M=10$ and use the principle of mathematical induction to show that $a_n<10$ for $n\geq 1$.

For $n=1$ we have $a_1=1$, which definitely satisfies $a_1<10$.

Now suppose that $a_k<10$ for certain value of $k\geq 1$, then we have

$$
a_{k+1}=\frac{1}{2}(a_k+5)<\frac{1}{2}(10+5)=\frac{15}{2}<10.
$$

This shows that $a_n<10$ for all $n=1,2,3,\ldots$.

::::::

::::::{prf:example}
:label: Ex:Sequences:BoundedExample4
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=10$ and $a_{n+1}=\sqrt{a_n+6}$ for $n=1,2,3,\ldots$. 

Now we show that the sequence is bounded below.

Again we use the principle of mathematical induction to show that $a_n>0$ for all $n=1,2,3,\ldots$.

For $n=1$ we have $a_1=10>0$.

Suppose that $a_k>0$ for certain value of $k\geq1$, then we have

$$
a_{k+1}=\sqrt{a_k+6}>\sqrt{0+6}=\sqrt{6}>0.
$$

This shows that $a_n>0$ for all $n=1,2,3,\ldots$.
::::::

## Grasple exercises

:::{todo}
Add Grasple exercises to {numref}`Sec:PropertiesOfSequences`.
:::


## Exercises

::::{exercise}
:label: Exc:Sequences:PropertiesExercise1
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=7$ and $a_{n+1}=\frac{1}{2}(a_n+5)$ for $n=1,2,3,\ldots$. 

Show that the sequence decreases.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:PropertiesExercise1`
:class: solution, dropdown
We want to prove that $a_n>a_{n+1}$ for all $n=1,2,3,\ldots$.

We use the principle of mathematical induction.

For $n=1$ we have $a_1=7>6=a_2$.

Suppose that $a_k>a_{k+1}$ for certain value of $k$, then we have

$$
a_{k+1}=\frac{1}{2}(a_k+5)>\frac{1}{2}(a_{k+1}+5)=a_{k+2}.
$$

This shows that $a_n>a_{n+1}$ for all $n=1,2,3,\ldots$.
:::

::::{exercise}
:label: Exc:Sequences:PropertiesExercise2
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=2$ and $a_{n+1}=\sqrt{a_n+6}$ for $n=1,2,3,\ldots$. 

Show that the sequence increases.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:PropertiesExercise2`
:class: solution, dropdown
We want to prove that $a_n<a_{n+1}$ for all $n=1,2,3,\ldots$.

We use the principle of mathematical induction.

For $n=1$ we have $a_1=2<2\sqrt{2}=a_2$.

Suppose that $a_k<a_{k+1}$ for certain value of $k$, then we have

$$
a_{k+1}=\sqrt{a_k+6}<\sqrt{a_{k+1}+6}=a_{k+2}.
$$

This shows that $a_n<a_{n+1}$ for all $n=1,2,3,\ldots$.
:::

::::{exercise}
:label: Exc:Sequences:PropertiesExercise3
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=7$ and $a_{n+1}=\frac{1}{2}(a_n+5)$ for $n=1,2,3,\ldots$. 

Show that the sequence is bounded below.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:PropertiesExercise3`
:class: solution, dropdown
We want to prove that $a_n>1$ (for instance) for all $n=1,2,3,\ldots$.

We use the principle of mathematical induction.

For $n=1$ we have $a_1=7>1$.

Suppose that $a_k>1$ for certain value of $k$, then we have

$$
a_{k+1}=\frac{1}{2}(a_k+5)>\frac{1}{2}(1+5)>1.
$$

This shows that $a_n>1$ for all $n=1,2,3,\ldots$.
:::

::::{exercise}
:label: Exc:Sequences:PropertiesExercise4
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=2$ and $a_{n+1}=\sqrt{a_n+6}$ for $n=1,2,3,\ldots$. 

Show that the sequence is bounded above.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:PropertiesExercise4`
:class: solution, dropdown
We want to prove that $a_n<10$ (for instance) for all $n=1,2,3,\ldots$.

We use the principle of mathematical induction.

For $n=1$ we have $a_1=2<10$.

Suppose that $a_k<10$ for certain value of $k$, then we have

$$
a_{k+1}=\sqrt{a_k+6}<\sqrt{10+6}<10.
$$

This shows that $a_n<10$ for all $n=1,2,3,\ldots$.
:::
