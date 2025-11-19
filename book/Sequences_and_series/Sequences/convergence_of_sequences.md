# Convergence of sequences

In this section we cover:

- Intuitive definition of convergence
- Precise definition of convergence
- Rules of calculations (i.e. sums, products etc.)
- Convergence of sequences defined by a function
- Monotone convergence theorem
- Convergence of recursively defined sequences

Reference for induction: https://interactivetextbooks.tudelft.nl/delftse-foundations-of-computation/content/logic/induction.html

In the study of sequences the notion of **convergence** is important. The concept of a limit of a sequence is a special case of the concept of a limit of a function (see: Chapter 3). We say that a sequence $\{a_n\}$ converges to a limit $L$, and we write $\lim\limits_{n\to\infty}a_n=L$, if the distance from $a_n$ to $L$ approaches $0$ as $n$ increases towards $\infty$. Formally we have:

::::::{prf:definition} Limit of a sequence
:label: Def:Sequences:LimitSequence
A sequence $\{a_n\}$ converges to a limit $L$, and we write $\lim\limits_{n\to\infty}a_n=L$, if for every positive real number $\epsilon$ there exists an integer $N$ such that if $n\geq N$, then $|a_n-L|<\epsilon$. 
::::::

::::::{prf:example}
1) $\displaystyle\lim_{n\to\infty}\frac{2n^2-3n+4}{3n^2+4n+5}=\lim_{n\to\infty}\frac{2-\dfrac{3}{n}+\dfrac{4}{n^2}}{3+\dfrac{4}{n}+\dfrac{5}{n^2}}=\frac{2-0+0}{3+0+0}=\frac{2}{3}$.

2) $\displaystyle\lim_{n\to\infty}\frac{2n-1}{\sqrt{n^2+1}}=\lim_{n\to\infty}=\lim_{n\to\infty}\frac{2-\dfrac{1}{n}}{\sqrt{1+\dfrac{1}{n^2}}}=\frac{2-0}{1+0}=2$.

3) 

$$
\begin{align*}\lim_{n\to\infty}\left(n-\sqrt{n(n+2)}\right)&=\lim_{n\to\infty}\left(n-\sqrt{n(n+2)}\right)\cdot\frac{n+\sqrt{n(n+2)}}{n+\sqrt{n(n+2)}}\\
&=\lim_{n\to\infty}\frac{n^2-n(n+2)}{n+\sqrt{n(n+2)}}=\lim_{n\to\infty}\frac{-2n}{n+\sqrt{n(n+2)}}\\
&=\lim_{n\to\infty}\frac{-2}{1+\sqrt{1+\dfrac{2}{n}}}=\frac{-2}{1+1}=-1.
\end{align*}
$$

::::::

::::::{prf:definition} Convergence and divergence of sequence
:label: Def:Sequences:ConvergenceSequence
A sequence $\{a_n\}$ is called **convergent** if $\lim\limits_{n\to\infty}a_n$ exists. Otherwise, the sequence is called **divergent**. 
::::::

::::::{note}
A sequence $\{a_n\}$ either converges or diverges. That is, either $\lim\limits_{n\to\infty}a_n=L$ exists (is a real number) or $\lim\limits_{n\to\infty}a_n$ does not exist. If $\lim\limits_{n\to\infty}a_n=\infty$ we say that the sequence diverges to $\infty$. If $\lim\limits_{n\to\infty}a_n=-\infty$ we say that the sequence diverges to $-\infty$. If $\lim\limits_{n\to\infty}a_n$ does not exist, but is not $\infty$ or $-\infty$, we can only say that the sequence diverges.
:::::: 

::::::{prf:example}
1) The sequence $\{a_n\}$ with $a_n=n$ diverges to $\infty$.

2) The sequence $\{a_n\}$ with $a_n=\dfrac{1}{n^2}$ is convergent and $\lim\limits_{n\to\infty}a_n=0$.

3) The geometric sequence $\{a_n\}$ with $a_n=\dfrac{1}{2^n}$ is convergent and $\lim\limits_{n\to\infty}=0$.
::::::

::::::{prf:theorem}
:label: Thm:Sequences:ConvergenceGeometric
The geometric sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=r^n$ is convergent for $-1<r\leq1$ and divergent for all other values of $r\in\mathbb{R}$.

Moreover, for $-1<r\leq1$ we have: $\lim\limits_{n\to\infty}r^n=\begin{cases}0, &-1<r<1\\1, &r=1.\end{cases}$
::::::

::::::{prf:proof}
We have $\displaystyle\lim_{n\to\infty}r^n=\begin{cases}0, &0<r<1\\ \infty, &r>1.\end{cases}$

Furthermore, we have $\lim\limits_{n\to\infty}0^n=0$ and $\lim\limits_{n\to\infty}1^n=1$.

If $-1<r<0$, then $0<|r|<1$ and $\lim\limits_{n\to\infty}|r^n|=\lim\limits_{n\to\infty}|r|^n=0$.

This proves the theorem.
::::::

::::::{prf:example}
1) The sequence $\{a_n\}$ with $a_n=\left(\dfrac{4}{5}\right)^n$ is convergent and $\lim\limits_{n\to\infty}a_n=0$.

2) The sequence $\{a_n\}$ with $a_n=2^n$ diverges to $\infty$.

3) The sequence $\{a_n\}$ with $a_n=(-1)^n$ is divergent. It does not diverge to $\infty$ or $-\infty$.
::::::

::::::{prf:theorem}
:label: Thm:Sequences:LimitFunctionSequence
If $\lim\limits_{x\to\infty}f(x)=L$ and $a_n=f(n)$ for all $n=1,2,3,\ldots$, then $\lim\limits_{n\to\infty}a_n=L$.
::::::

::::::{prf:example}
:label: Ex:Sequences:ConvergenceExample1
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{n}{n+1}$ is convergent.

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
\lim_{x\to\infty}f(x)=\lim_{x\to\infty}\frac{x}{x+1}=1.
$$

This implies that the sequence $\{a_n\}_{n=1}^{\infty}$ is convergent and $\lim\limits_{n\to\infty}a_n=1$.
::::::

::::::{prf:example}
:label: Ex:Sequences:ConvergenceExample2
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ with $a_n=\dfrac{2n}{n^2+1}$ is convergent.

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
\lim_{x\to\infty}f(x)=\lim_{x\to\infty}\frac{2x}{x^2+1}=0.
$$

This implies that the sequence $\{a_n\}_{n=1}^{\infty}$ is convergent and $\lim\limits_{n\to\infty}a_n=0$.
::::::

::::::{prf:theorem}
:label: Thm:Sequences:SqueezeTheorem
If $\lim\limits_{n\to\infty}|a_n|=0$, then $\lim\limits_{n\to\infty}a_n=0$.
::::::

::::::{prf:proof}
We can prove this using the *squeeze theorem*, since $-|a_n|\leq a_n\leq|a_n|$.
::::::

::::::{prf:example}
1) The sequence $\{a_n\}$ with $a_n=\dfrac{(-1)^n}{n}$ is convergent and $\lim\limits_{n\to\infty}a_n=0$.

2) The sequence $\{a_n\}$ with $a_n=\dfrac{\cos(n)}{\sqrt{n}}$ is convergent and $\lim\limits_{n\to\infty}a_n=0$.

3) The sequence $\{a_n\}$ with $a_n=\dfrac{\sin(n^2)}{n}$ is convergent and $\lim\limits_{n\to\infty}a_n=0$.
::::::

::::::{prf:theorem}
:label: Thm:Sequences:Continuity
If $\lim\limits_{x\to\infty}f(x)=L$ and the function $f$ is continuous at $L$, then $\lim\limits_{n\to\infty}f(a_n)=f(L)$.
::::::

::::::{prf:proof}
This is an immediate consequence of the continuity of the function $f$.
::::::

::::::{prf:example}
1) The sequence $\{a_n\}$ with $a_n=\sin\left(\dfrac{1}{n}\right)$ is convergent and $\lim\limits_{n\to\infty}a_n=\sin(0)=0$.

2) The sequence $\{a_n\}$ with $a_n=\cos\left(\dfrac{n\pi}{n+1}\right)$ is convergent and $\lim\limits_{n\to\infty}a_n=\cos(\pi)=-1$.

3) The sequence $\{a_n\}$ with $a_n=\arctan\left(\dfrac{n+1}{n+2}\right)$ is convergent and $\lim\limits_{n\to\infty}a_n=\arctan(1)=\frac{1}{4}\pi$.
::::::

::::::{prf:theorem}
:label: Thm:Sequences:MonotonicBounded
Every *increasing* sequence that is *bounded above* is convergent and every *decreasing* sequence that is *bounded below* is convergent.
::::::

```{figure} Images/convergent.png
---
width: 50%
name: convergent sequence
align: center
---
An increasing sequence that is bounded above
```

::::::{prf:proof}
Suppose that $\{a_n\}$ is an increasing sequence that is bounded above. Then it has a *least upper bound* $L$. Let $\epsilon>0$, then $L-\epsilon$ is *not* an upper bound, since $L$ is the least upper bound. Therefore

$$
a_N>L-\epsilon\quad\text{for some integer $N$.}
$$

However, since the sequence is increasing, we have $a_n>a_N$ for every $n>N$. Thus, if $n>N$, we have

$$
a_n>L-\epsilon\quad\Longrightarrow\quad0\leq L-a_n<\epsilon,
$$

since $a_n\leq L$. Thus

$$
|L-a_n|<\epsilon\quad\text{whenever}\quad n>N.
$$

So, $\lim\limits_{n\to\infty}a_n=L$.

A similar proof, using the greatest lower bound, works for a decreasing sequence that is bounded below.
::::::

::::::{prf:example}
:label: Ex:Sequences:MonotonicBoundedExample1
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=1$ and $a_{n+1}=\frac{1}{2}(a_n+5)$ for $n=1,2,3,\ldots$. 

Show that the sequence converges and find its limit.

Proof. We have seen that the sequence increases and is bounded above. This implies that the sequence converges. So, the limit $\lim\limits_{n\to\infty}a_n$ exists.

Let $L=\lim\limits_{n\to\infty}a_n$, then we have $\lim\limits_{n\to\infty}a_{n+1}=L$ and

$$
L=\frac{1}{2}(L+5)\quad\Longleftrightarrow\quad2L=L+5\quad\Longleftrightarrow\quad L=5.
$$

::::::

::::::{prf:example}
:label: Ex:Sequences:MonotonicBoundedExample2
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=10$ and $a_{n+1}=\sqrt{a_n+6}$ for $n=1,2,3,\ldots$. 

Show that the sequence converges and find its limit.

Proof. We have seen that the sequence decreases and is bounded below by $0$. This implies that the sequence converges. So, the limit $\lim\limits_{n\to\infty}a_n$ exists.

Let $L=\lim\limits_{n\to\infty}a_n$, then we have $\lim\limits_{n\to\infty}a_{n+1}=L$ and

$$
\begin{align*}
L=\sqrt{L+6}\quad\Longrightarrow\quad L^2=L+6&\quad\Longleftrightarrow\quad L^2-L-6=0\\
&\quad\Longleftrightarrow\quad(L-3)(L+2)=0.
\end{align*}
$$

Hence: $L=3$ or $L=-2$. Since the sequence is bounded below by $0$, we conclude that $L=3$.
::::::

::::::{warning}
It is important that we first showed that the limit exists before setting $L=\lim\limits_{n\to\infty}a_n$. Otherwise, you might draw wrong conclusions.

For instance, it is clear that the Fibonacci sequence, which is defined by $F_{n+2}+F_n+F_{n+1}$ for $n=1,2,3,\ldots$ with $F_1=F_2=1$ is divergent. So, the limit $\lim\limits_{n\to\infty}a_n=\infty$ does not exist.

If we would assume that $L=\lim\limits_{n\to\infty}a_n$, then we would have that

$$
L=L+L\quad\Longleftrightarrow\quad L=0.
$$

::::::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise1
Consider the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=7$ and $a_{n+1}=\frac{1}{2}(a_n+5)$ for $n=1,2,3,\ldots$. 

Show that the sequence is convergent and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise1`
:class: solution, dropdown
We have seen that the sequence decreases and is bounded below by $1$. This implies that the sequence converges. So, the limit $\lim\limits_{n\to\infty}a_n$ exists.

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
We have seen that the sequence increases and is bounded above. This implies that the sequence converges. So, the limit $\lim\limits_{n\to\infty}a_n$ exists.

Let $L=\lim\limits_{n\to\infty}a_n$, then we have $\lim\limits_{n\to\infty}a_{n+1}=L$ and

$$
\begin{align*}
L=\sqrt{L+6}\quad\Longrightarrow\quad L^2=L+6&\quad\Longleftrightarrow\quad L^2-L-6=0\\
&\quad\Longleftrightarrow\quad(L-3)(L+2)=0.
\end{align*}
$$

This implies that $L=3$ or $L=-2$. Since $a_1=1$ and the sequence is increasing, we conclude that $L=3$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise3
Show that the sequence $\left\{\sqrt{2},\sqrt{2\sqrt{2}},\sqrt{2\sqrt{2\sqrt{2}}},\ldots\right\}$ converges and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise3`
:class: solution, dropdown
Note that the sequence can be written as $\{a_n\}_{n=1}^{\infty}$ with $a_1=\sqrt{2}$ and $a_{n+1}=\sqrt{2a_n}$ for $n=1,2,3,\ldots$.

1) Using mathematical induction we prove that the sequence is increasing: $a_{n+1}>a_n$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_2=\sqrt{2a_1}=\sqrt{2\sqrt{2}}>\sqrt{2}=a_1$ which is true.

Assuming that $a_{k+1}>a_k$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{2a_{k+1}}>\sqrt{2a_k}=a_{k+1}.
$$

This proves that the sequence is increasing.

2) Using mathematical induction we prove that the sequence is bounded above, for instance that $a_n\leq2$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=\sqrt{2}\leq2$, which is true.

Assuming that $a_k\leq2$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{2a_{k+1}}\leq\sqrt{2a_k}=a_{k+1}.
$$

This proves that the sequence is bounded above by $2$.

3) Since the sequence is increasing and bounded above, we conclude that the sequence is convergent. So: $L=\lim\limits_{n\to\infty}a_n$ exists and must satisfy

$$
L=\sqrt{2L}\quad\Longrightarrow\quad L^2=2L\quad\Longleftrightarrow\quad L=0\quad\text{or}\quad L=2.
$$

Since $a_1=\sqrt{2}>1$ and the sequence is increasing, we conclude that $L=2$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise4
Show that the sequence $\left\{\sqrt{2},\sqrt{2+\sqrt{2}},\sqrt{2+\sqrt{2+\sqrt{2}}},\ldots\right\}$ converges and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise4`
:class: solution, dropdown
Note that the sequence can be written as $\{a_n\}_{n=1}^{\infty}$ with $a_1=\sqrt{2}$ and $a_{n+1}=\sqrt{2+a_n}$ for $n=1,2,3,\ldots$.

1) Using mathematical induction we prove that the sequence is increasing: $a_{n+1}>a_n$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_2=\sqrt{2+a_1}=\sqrt{2+\sqrt{2}}>\sqrt{2}=a_1$ which is true.

Assuming that $a_{k+1}>a_k$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{2+a_{k+1}}>\sqrt{2+a_k}=a_{k+1}.
$$

This proves that the sequence is increasing.

2) Using mathematical induction we prove that the sequence is bounded above, for instance that $a_n\leq2$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=\sqrt{2}\leq2$, which is true.

Assuming that $a_k\leq2$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{2+a_{k+1}}\leq\sqrt{2+a_k}=a_{k+1}.
$$

This proves that the sequence is bounded above by $2$.

3) Since the sequence is increasing and bounded above, we conclude that the sequence is convergent. So: $L=\lim\limits_{n\to\infty}a_n$ exists and must satisfy

$$
\begin{align*}
L=\sqrt{2+L}\quad\Longrightarrow\quad L^2=2+L&\quad\Longleftrightarrow\quad L^2-L-2=0\\
&\quad\Longleftrightarrow\quad(L-2)(L+1)=0.
\end{align*}
$$

Hence: $L=2$ or $L=-1$. Since $a_1=\sqrt{2}>1$ and the sequence is increasing, we conclude that $L=2$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise5
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=1$ and $a_{n+1}=4-\dfrac{1}{a_n}$ is convergent and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise5`
:class: solution, dropdown
1) Using mathematical induction we prove that the sequence is increasing: $a_{n+1}>a_n$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_2=4-1=3>1=a_1$ which is true.

Assuming that $a_{k+1}>a_k$ for certain value of $k$ we obtain $-a_{k+1}<-a_k$ and $-\displaystyle\frac{1}{a_{k+1}}>-\frac{1}{a_k}$ and therefore

$$
a_{k+2}=4-\frac{1}{a_{k+1}}>4-\frac{1}{a_k}=a_{k+1}.
$$

This proves that the sequence is increasing.

2) Using mathematical induction we prove that the sequence is bounded above, for instance that $a_n\leq3$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=1\leq3$, which is true.

Assuming that $a_k\leq4$ for certain value of $k$ we obtain $-a_k\geq-4$ and $-\displaystyle\frac{1}{a_k}\leq-\frac{1}{4}$ and therefore

$$
a_{k+2}=4-\frac{1}{a_k}\leq4-\frac{1}{4}\leq4.
$$

This proves that the sequence is bounded above by $4$.

3) Since the sequence is increasing and bounded above, we conclude that the sequence is convergent. So: $L=\lim\limits_{n\to\infty}a_n$ exists and must satisfy

$$
\begin{align*}
L=4-\frac{1}{L}\quad\Longrightarrow\quad L^2=4L-1&\quad\Longleftrightarrow\quad L^2-4L+1=0\\
&\quad\Longleftrightarrow\quad (L-2)^2=3.
\end{align*}
$$

Hence: $L=2+\sqrt{3}$ or $L=2-\sqrt{3}$. Since $a_2=3$ and the sequence is increasing, we conclude that $L=2+\sqrt{3}$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise6
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=3$ and $a_{n+1}=\dfrac{1}{4-a_n}$ is convergent and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise6`
:class: solution, dropdown
1) Using mathematical induction we prove that the sequence is decreasing: $a_{n+1}<a_n$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_2=\dfrac{1}{4-3}=1<3=a_1$ which is true.

Assuming that $a_{k+1}<a_k$ for certain value of $k$ we obtain $4-a_{k+1}>4-a_k$ and $\displaystyle\frac{1}{4-a_{k+1}}<\frac{1}{4-a_k}$ and therefore

$$
a_{k+2}=\frac{1}{4-a_{k+1}}<\frac{1}{4-a_k}=a_{k+1}.
$$

This proves that the sequence is decreasing.

2) Using mathematical induction we prove that the sequence is bounded below, for instance that $a_n\geq0$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=3\geq0$, which is true.

Assuming that $a_k\geq0$ for certain value of $k$ we obtain $4-a_k\leq4$ and $\displaystyle\frac{1}{4-a_k}\geq\frac{1}{4}$ and therefore

$$
a_{k+2}=\frac{1}{4-a_k}\geq\frac{1}{4}\geq0.
$$

This proves that the sequence is bounded below by $0$.

3) Since the sequence is decreasing and bounded below, we conclude that the sequence is convergent. So: $L=\lim\limits_{n\to\infty}a_n$ exists and must satisfy

$$
\begin{align*}
L=\frac{1}{4-L}\quad\Longrightarrow\quad 4L-L^2=1&\quad\Longleftrightarrow\quad L^2-4L+1=0\\
&\quad\Longleftrightarrow\quad (L-2)^2=3.
\end{align*}
$$

Hence: $L=2+\sqrt{3}$ or $L=2-\sqrt{3}$. Since $a_1=3$ and $a_2=1$ and the sequence is decreasing, we conclude that $L=2-\sqrt{3}$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise7
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=1$ and $a_{n+1}=\sqrt{1+2a_n}$ is convergent and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise7`
:class: solution, dropdown
1) Using mathematical induction we prove that the sequence is increasing: $a_{n+1}>a_n$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_2=\sqrt{3}>1=a_1$ which is true.

Assuming that $a_{k+1}>a_k$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{1+2a_{k+1}}>\sqrt{1+2a_k}=a_{k+1}.
$$

This proves that the sequence is increasing.

2) Using mathematical induction we prove that the sequence is bounded above, for instance that $a_n\leq5$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=1\leq5$, which is true.

Assuming that $a_k\leq5$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{1+2a_{k+1}}\leq\sqrt{1+10}\leq5.
$$

This proves that the sequence is bounded above by $5$.

3) Since the sequence is increasing and bounded above, we conclude that the sequence is convergent. So: $L=\lim\limits_{n\to\infty}a_n$ exists and must satisfy

$$
\begin{align*}
L=\sqrt{1+2L}\quad\Longrightarrow\quad L^2=1+2L&\quad\Longleftrightarrow\quad L^2-2L-1=0\\
&\quad\Longleftrightarrow\quad(L-1)^2=2.
\end{align*}
$$

Hence: $L=1+\sqrt{2}$ or $L=1-\sqrt{2}$. Since $a_1=1$ and the sequence is increasing, we conclude that $L=1+\sqrt{2}$.
:::

::::{exercise}
:label: Exc:Sequences:ConvergenceExercise8
Show that the sequence $\{a_n\}_{n=1}^{\infty}$ given by $a_1=3$ and $a_{n+1}=\sqrt{15+2a_n}$ is convergent and find its limit.
::::

:::{admonition} Solution of {numref}`Exc:Sequences:ConvergenceExercise8`
:class: solution, dropdown
1) Using mathematical induction we prove that the sequence is increasing: $a_{n+1}>a_n$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_2=\sqrt{21}>3=a_1$ which is true.

Assuming that $a_{k+1}>a_k$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{15+2a_{k+1}}>\sqrt{15+2a_k}=a_{k+1}.
$$

This proves that the sequence is increasing.

2) Using mathematical induction we prove that the sequence is bounded above, for instance that $a_n\leq10$ for $n=1,2,3,\ldots$.

For $n=1$ this reads: $a_1=3\leq10$, which is true.

Assuming that $a_k\leq10$ for certain value of $k$ we obtain

$$
a_{k+2}=\sqrt{15+2a_{k+1}}\leq\sqrt{15+10}\leq10.
$$

This proves that the sequence is bounded above by $10$.

3) Since the sequence is increasing and bounded above, we conclude that the sequence is convergent. So: $L=\lim\limits_{n\to\infty}a_n$ exists and must satisfy

$$
\begin{align*}
L=\sqrt{15+2L}\quad\Longrightarrow\quad L^2=15+2L&\quad\Longleftrightarrow\quad L^2-2L-15=0\\
&\quad\Longleftrightarrow\quad(L-5)(L+3)=0.
\end{align*}
$$

Hence: $L=5$ or $L=-3$. Since $a_1=3$ and the sequence is increasing, we conclude that $L=5$.
:::

## Grasple exercises
