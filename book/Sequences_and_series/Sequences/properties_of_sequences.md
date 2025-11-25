# Properties of sequences

In this section we cover:

- Increasing and decreasing sequences (incl. monotonic sequences)
- Sequences that are bounded above and/or below

::::::{prf:definition}
:label: Def:Sequences:IncreasingDecreasing
A sequence $\{a_n\}_{n=1}^{\infty}$ is called **increasing** if $a_n < a_{n+1}$ for all $n\geq1$, that is $a_1 < a_2 < a_3 <\cdots$. 

It is called **decreasing** if $a_n > a_{n+1}$ for all $n\geq1$, that is $a_1 > a_2 > a_3 >\cdots$. 

A sequence is called **monotonic** if it is either *increasing* or *decreasing*.
::::::

::::::{note}
If the inequalities only hold for all $n\geq N$ for some integer $N>1$ the sequence is called **ultimately** increasing or decreasing.
::::::

::::::{prf:example}
:label: Ex:Sequences:UltimateIncreasingExample
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{n^2}{2^n}$. Then the first terms are

$$
\frac{1}{2},\quad1,\quad\frac{9}{8},\quad1,\quad\frac{25}{32},\quad\frac{9}{16},\quad\ldots.
$$

Although the first three terms increase, this sequence is *ultimately decreasing* (for $n\geq3$) since $2^n$ eventually increases faster than $n^2$.
::::::

::::::{note}
In the case that $a_n\leq a_{n+1}$ for all $n\geq1$ the sequence is sometimes called **nondecreasing** and if $a_n\geq a_{n+1}$ for all $n\geq1$ it is called **nonincreasing**.
::::::

It is clear that an arithmetic sequence is *increasing* if the common difference $d$ is *positive* and *decreasing* if the common difference $d$ is *negative*.

Furthermore, a harmonic sequence is *decreasing* if the reciprocals of its terms form an *increasing* arithmetic sequence.

A geometric sequence is *increasing* if its first term is positive and the common ratio $r>1$.

A geometric sequence is *decreasing* if its first term is positive and the common ratio $0<r<1$.

Every *alternating sequence* is not monotonic.

::::::{prf:example}
:label: Ex:Sequences:IncreasingExample1
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{n}{n+1}$ is increasing.

Proof. We want to show that $\dfrac{n}{n+1}<\dfrac{n+1}{n+2}$ for all $n=1,2,3,\ldots$.

Since $n>0$ this is equivalent to $n(n+2)<(n+1)^2\;\Longleftrightarrow\;n^2+2n<n^2+2n+1$, which is true.
::::::

::::::{prf:example}
:label: Ex:Sequences:IncreasingExample2
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{2n}{n^2+1}$ is decreasing.

Proof. We want to show that $\dfrac{2n}{n^2+1}>\dfrac{2(n+1)}{(n+1)^2+1}$ for all $n=1,2,3,\ldots$. Note that

$$
\begin{align*}
\frac{2n}{n^2+1}>\frac{2n+2}{n^2+2n+2}&\quad\Longleftrightarrow\quad2n(n^2+2n+2)>(2n+2)(n^2+1)\\
&\quad\Longleftrightarrow\quad2n^3+4n^2+4n>2n^3+2n^2+2n+2\\
&\quad\Longleftrightarrow\quad2n^2+2n>2\\
&\quad\Longleftrightarrow\quad n(n+1)>1.
\end{align*}
$$

This is trivially true for $n\geq1$.
::::::

Note that in both cases the terms of the sequence lie on the graph of a continuous function. It might be easier to study the behaviour of the corresponding function.

::::::{prf:example}
:label: Ex:Sequences:IncreasingExample1Function
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{n}{n+1}$ is increasing.

```{figure} Images/sequence1.png
---
width: 50%
name: increasing sequence
align: center
---
The terms of the sequence $\{a_n\}$ lie on the graph of $f(x)=\dfrac{x}{x+1}$
```

Proof. Note that $a_n=f(n)$ with $f(x)=\dfrac{x}{x+1}$. Now we have

$$
f'(x)=\frac{x+1-x}{(x+1)^2}=\frac{1}{(x+1)^2}>0.
$$

This implies that $f$ is increasing and therefore that the sequence increases.
::::::

::::::{prf:example}
:label: Ex:Sequences:IncreasingExample2Function
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{2n}{n^2+1}$ is decreasing.

```{figure} Images/sequence2.png
---
width: 50%
name: decreasing sequence
align: center
---
The terms of the sequence $\{a_n\}$ lie on the graph of $f(x)=\dfrac{2x}{x^2+1}$
```

Proof. Note that $a_n=f(n)$ with $f(x)=\dfrac{2x}{x^2+1}$. Then we have

$$
f'(x)=\frac{2(x^2+1)-2x\cdot2x}{(x^2+1)^2}=\frac{2(1-x^2)}{(x^2+1)^2},
$$

which is negative for $x>1$. This implies that $f$ is decreasing on $(1,\infty)$ and so $f(n)>f(n+1)$. Therefore $\{a_n\}$ is decreasing.
::::::

If the sequence is defined by a recursive formula, it is often somewhat more difficult. Not always as in the next example:

::::::{prf:example}
The Fibonacci sequence $1,1,2,3,5,8,13,21,34,55,89,\ldots$ is ultimately increasing.
::::::

In many other situations the principle of mathematical induction might be helpful.

::::::{prf:example}
:label: Ex:Sequences:RecurrenceExample1
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=1$ and $a_{n+1}=\frac{1}{2}(a_n+5)$ for $n=1,2,3,\ldots$. 

Show that the sequence increases.

Proof. We want to prove that $a_n<a_{n+1}$ for all $n=1,2,3,\ldots$.

We use the principle of mathematical induction.

For $n=1$ we have $a_1=1<3=a_2$.

Suppose that $a_k<a_{k+1}$ for certain value of $k$, then we have

$$
a_{k+1}=\frac{1}{2}(a_k+5)<\frac{1}{2}(a_{k+1}+5)=a_{k+2}.
$$

This shows that $a_n<a_{n+1}$ for all $n=1,2,3,\ldots$.
::::::

::::::{prf:example}
:label: Ex:Sequences:RecurrenceExample2
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=10$ and $a_{n+1}=\sqrt{a_n+6}$ for $n=1,2,3,\ldots$. 

Show that the sequence decreases.

Proof. We want to prove that $a_n>a_{n+1}$ for all $n=1,2,3,\ldots$.

We use the principle of mathematical induction.

For $n=1$ we have $a_1=10>4=a_2$.

Suppose that $a_k>a_{k+1}$ for certain value of $k$, then we have

$$
a_{k+1}=\sqrt{a_k+6}>\sqrt{a_{k+1}+6}=a_{k+2}.
$$

This shows that $a_n>a_{n+1}$ for all $n=1,2,3,\ldots$.
::::::

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

::::::{prf:definition}
:label: Def:Sequences:Bounded
A sequence $\{a_n\}_{n=1}^{\infty}$ is called **bounded above** if there exists a number $M$ such that $a_n\leq M$ for all $n\geq1$.

It is called **bounded below** if there exists a number $m$ such that $m\leq a_n$ for all $n\geq1$.

A sequence is called **bounded** if it is both *bounded above* and *bounded below*.
::::::

::::::{prf:example}
1) The sequence $1,2,3,4,5,\ldots$ of positive integers is *bounded below* with $m\leq1$.

2) The geometric sequence $1,\frac{1}{2},\frac{1}{4},\frac{1}{8},\frac{!}{16},\ldots$ is *bounded above* with $M\geq1$.

3) The arithmetic sequence $5,3,1,-1,-3,\ldots$ is *bounded above* with $M\geq5$.

4) The arithmetic sequence $1,3,5,7,9,\ldots$ is *bounded below* with $m\leq1$.

5) The harmonic sequence $1,\frac{1}{2},\frac{1}{3},\frac{1}{4},\frac{1}{5},\ldots$ is *bounded* with $M\geq1$ and $m\leq0$.
::::::

::::::{prf:example}
:label: Ex:Sequences:BoundedExample1
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{n}{n+1}$ is bounded.

```{figure} Images/sequence1.png
---
width: 50%
name: increasing sequence
align: center
---
The terms of the sequence $\{a_n\}$ lie on the graph of $f(x)=\dfrac{x}{x+1}$
```

Proof. Note that $a_n=f(n)$ with $f(x)=\dfrac{x}{x+1}$. Now we have

$$
f'(x)=\frac{x+1-x}{(x+1)^2}=\frac{1}{(x+1)^2}>0.
$$

This implies that $f$ is increasing. Further we have $f(1)=\frac{1}{2}$ and $\lim\limits_{x\to\infty}f(x)=1$.

Hence, we have $\frac{1}{2}\leq f(x)<1$ for $x\geq1$.

This implies that the sequence is bounded with $M\geq1$ and $m\leq\frac{1}{2}$.
::::::

::::::{prf:example}
:label: Ex:Sequences:BoundedExample2
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{2n}{n^2+1}$ is bounded.

```{figure} Images/sequence2.png
---
width: 50%
name: decreasing sequence
align: center
---
The terms of the sequence $\{a_n\}$ lie on the graph of $f(x)=\dfrac{2x}{x^2+1}$
```

Proof. Note that $a_n=f(n)$ with $f(x)=\dfrac{2x}{x^2+1}$. Then we have

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

Show that the sequence bounded above.

Proof. We want to prove that $a_n<10$ (for instance) for all $n=1,2,3,\ldots$.

We use the principle of mathematical induction.

For $n=1$ we have $a_1=1<10$.

Suppose that $a_k<10$ for certain value of $k$, then we have

$$
a_{k+1}=\frac{1}{2}(a_k+5)<\frac{1}{2}(10+5)<10.
$$

This shows that $a_n<10$ for all $n=1,2,3,\ldots$.
::::::

::::::{prf:example}
:label: Ex:Sequences:BoundedExample4
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=10$ and $a_{n+1}=\sqrt{a_n+6}$ for $n=1,2,3,\ldots$. 

Show that the sequence is bounded below.

Proof. We want to prove that $a_n>0$ (for instance) for all $n=1,2,3,\ldots$.

We use the principle of mathematical induction.

For $n=1$ we have $a_1=10>0$.

Suppose that $a_k>0$ for certain value of $k$, then we have

$$
a_{k+1}=\sqrt{a_k+6}>\sqrt{0+6}>0.
$$

This shows that $a_n>0$ for all $n=1,2,3,\ldots$.
::::::

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
