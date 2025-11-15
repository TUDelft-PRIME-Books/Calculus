# Series and their types

In this section we cover (see note in section convergence of series):

- Series and partial sums
- Convergence of sum(a_n+b_n)
- Geometric series
- Telescoping series
- Harmonic series and p-series (i.e. sum 1/n^p)
- Convergence and divergence
- Absolute and conditional convergence

::::::{prf:definition}
:label: Def:Series:Definition
Let $\{a_n\}_{n=1}^{\infty}$ be a sequence of real numbers $a_1,a_2,a_3,\ldots$. If we try to add these numbers we get an expression of the form $a_1+a_2+a_3+\cdots$, which is called an **infinite series** or just **series** and is denoted by $\displaystyle\sum_{n=1}^{\infty}a_n$ or just $\displaystyle\sum a_n$.
::::::

Does this make sense? What does it mean?

Given a series $\displaystyle\sum_{n=1}^{\infty}a_n=a_1+a_2+a_3+\cdots$, let $s_n$ denote its $n$th **partial sum**

$$
s_n=\displaystyle\sum_{k=1}^na_k=a_1+a_2+a_3+\cdots+a_n.
$$

These partial sums form a sequence $\{s_n\}_{n=1}^{\infty}$. Now we consider $\lim\limits_{n\to\infty}s_n$.

::::::{prf:definition}
:label: Def:Series:ConvergenceSum
If the limit $\lim\limits_{n\to\infty}s_n=s$ exists, then the series $\displaystyle\sum a_n$ is called **convergent** and we write $\displaystyle\sum_{n=1}^{\infty}a_n=s$ or $a_1+a_2+a_3+\cdots=s$.

The number $s$ is called the **sum** of the series. 

If the limit $\lim\limits_{n\to\infty}s_n$ does not exist, then the series is called **divergent**.
::::::

::::::{prf:example} 

```{figure} Images/geometric.png
---
width: 50%
name: geometric series
align: center
---
A visual proof of $\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots=1$
```

$$
\sum_{n=1}^{\infty}\left(\frac{1}{2}\right)^n=\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots=1.
$$

::::::

::::::{prf:theorem} Geometric series
:label: Thm:Series:GeometricSeries
A **geometric series** $\displaystyle\sum_{n=1}^{\infty}ar^{n-1}=a+ar+ar^2+\cdots$ with $a\neq0$ and **common ratio** $r$ is convergent if $|r|<1$ and divergent if $|r|\geq1$.

For $|r|<1$ the sum of the series equals $\displaystyle\frac{a}{1-r}$.
::::::

::::::{prf:proof}
For $r=1$ the series trivially diverges. For $r\neq1$ consider the $n$th partial sum

$$
s_n=\displaystyle\sum_{k=1}^nar^{k-1}=a+ar+ar^2+\cdots+ar^{n-1}.
$$

Then we have (compare with {prf:ref}`Ex:Integration:IntroductionFiniteGeometric`)

$$
\begin{align*}
s_n&=a&+ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&\\
rs_n&=&ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&+ar^n.
\end{align*}
$$

Subtracting the two equations we obtain

$$
(1-r)s_n=a-ar^n=a(1-r^n)\quad\Longrightarrow\quad s_n=\frac{a(1-r^n)}{1-r},\quad r\neq1.
$$

In {prf:ref}`Thm:Sequences:ConvergenceGeometric` we have seen that $\lim\limits_{n\to\infty}r^n$ only converges for $-1<r\leq1$ and 

$$
\lim\limits_{n\to\infty}r^n=\begin{cases}0, &-1<r<1\\1, &r=1.\end{cases}
$$

We conclude that the series $\displaystyle\sum_{n=1}^{\infty}ar^{n-1}$ only converges for $|r|<1$ and diverges for $|r|\geq1$.

Furthermore, for $|r|<1$ the sum of the series equals $\displaystyle\frac{a}{1-r}$.
::::::

::::::{note}
The best way to remember the sum of a convergent geometric series is

$$
\text{sum}=\frac{\text{first term}}{1-\text{common ratio}}.
$$

::::::

::::::{prf:example} 
1) $\displaystyle\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots=\sum_{n=1}^{\infty}\left(\frac{1}{2}\right)^n=\frac{\frac{1}{2}}{1-\frac{1}{2}}=1$.

2) $\displaystyle\frac{1}{5}-\frac{2}{25}+\frac{4}{125}-\frac{8}{625}+\cdots=\frac{1}{5}\sum_{n=0}^{\infty}\left(-\frac{2}{5}\right)^n=\frac{1}{5}\cdot\frac{1}{1+\frac{2}{5}}=\frac{1}{5}\cdot\frac{5}{7}=\frac{1}{7}$.

3) $\displaystyle0.\overline{12}:=0.1212121212\ldots=\sum_{n=1}^{\infty}\frac{12}{100^n}=\frac{\frac{12}{100}}{1-\frac{1}{100}}=\frac{12}{100-1}=\frac{12}{99}=\frac{4}{33}$.
::::::

In the last example $\overline{12}$ denotes that $12$ is repeated indefinitely. The number $p:=0.\overline{12}$ is an example of a convergent geometric series. However, it is easier to note that

$$
100p=1.\overline{12}=12+0.\overline{12}=12+p\quad\Longrightarrow\quad99p=12\quad\Longleftrightarrow\quad p=\frac{12}{99}=\frac{4}{33}.
$$

::::::{prf:example} 
Express the number $0.\overline{135}:=0.135135135\ldots$ as a quotient of integers.

Solution 1. The number can be written as a geometric series:

$$
0.\overline{135}=\sum_{n=1}^{\infty}\frac{135}{1000^n}.
$$
 
Then, the common ratio is $\dfrac{1}{1000}$ and therefore the geometric series converges and

$$
0.\overline{135}=\frac{\dfrac{135}{1000}}{1-\dfrac{1}{1000}}=\frac{135}{1000-1}=\frac{135}{999}=\frac{15}{111}=\frac{5}{37}.
$$

Solution 2. Let $q=0.\overline{135}$, then we have

$$
1000q=135.\overline{135}=135+0.\overline{135}=135+q\quad\Longrightarrow\quad999q=135\quad\Longleftrightarrow\quad q=\frac{135}{999}.
$$

::::::

::::{exercise}
:label: Exc:Series:DecimalsOne
Is the number $r=0.\overline{9}=0.99999\ldots$ smaller than $1$?

Find an easier expression for $r$.
::::

:::{admonition} Solution of {numref}`Exc:Series:DecimalsOne`
:class: solution, dropdown
Solution 1. Write $r=0.\overline{9}$ as a geometric series:

$$
r=0.\overline{9}=\sum_{n=1}^{\infty}\frac{9}{10^n}.
$$

This is a geometric series with common ratio $\dfrac{1}{10}$. Therefore, it is convergent and

$$
r=0.\overline{9}=\frac{\dfrac{9}{10}}{1-\dfrac{1}{10}}=\frac{9}{10-1}=\frac{9}{9}=1.
$$

Solution 2. If $r=0.\overline{9}$, then we have

$$
10r=9.\overline{9}=9+0.\overline{9}=9+r\quad\Longrightarrow\quad9r=9\quad\Longleftrightarrow\quad r=1.
$$

So, the notation $0.\overline{9}=0.99999\ldots$ is just a clumsy way to represent the number $1$.
:::

## Telescoping series

In {eq}`Eq:Series:FibonacciTelescoping` we have seen the *telescoping property* of the (finite) sum of the first $n$ Fibonacci numbers. Sometimes this property can be used to find the sum of a **telescoping series**.

::::::{prf:example}
:label: Ex:Series:TelescopingSeries1
An example of a *telescoping series* is: $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n+1)}$.

Then the $n$th partial sum is: $s_n=\displaystyle\sum_{k=1}^n\frac{1}{k(k+1)}=\sum_{k=1}^n\left(\frac{1}{k}-\frac{1}{k+1}\right)$. Hence we have

$$
s_n=\frac{1}{1}-\frac{1}{2}+\frac{1}{2}-\frac{1}{3}+\frac{1}{3}-\frac{1}{4}+\cdots+\frac{1}{n}-\frac{1}{n+1}=1-\frac{1}{n+1}.
$$

Hence we have $\lim\limits_{n\to\infty}s_n=1$. This implies that the series is convergent and that $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n+1)}=1$.
::::::

::::::{prf:example}
:label: Ex:Series:TelescopingSeries2
Another example is: $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n^2-1}$. Then we have

$$
\begin{align*}
\sum_{k=2}^n\frac{1}{k^2-1}&=\sum_{k=2}^n\frac{1}{(k-1)(k+1)}=\frac{1}{2}\sum_{k=2}^n\left(\frac{1}{k-1}-\frac{1}{k+1}\right)\\
&=\frac{1}{2}\left(\frac{1}{1}-\frac{1}{3}+\frac{1}{2}-\frac{1}{4}+\frac{1}{3}-\frac{1}{5}+\frac{1}{4}-\frac{1}{6}+\cdots+\frac{1}{n-2}-\frac{1}{n}+\frac{1}{n-1}-\frac{1}{n+1}\right)\\
&=\frac{1}{2}\left(1+\frac{1}{2}-\frac{1}{n}-\frac{1}{n+1}\right).
\end{align*}
$$

This implies that the series converges and that $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n^2-1}
=\lim\limits_{n\to\infty}\frac{1}{2}\left(\frac{3}{2}-\frac{1}{n}-\frac{1}{n+1}\right)=\frac{3}{4}$.
::::::

::::::{prf:example}
:label: Ex:Series:TelescopingSeries3
A third example is: $\displaystyle\sum_{n=2}^{\infty}\frac{1}{(n-1)(n+2)}$. Then we have

$$
\begin{align*}
\sum_{k=2}^n\frac{1}{(k-1)(k+2)}&=\frac{1}{3}\sum_{k=2}^n\left(\frac{1}{k-1}-\frac{1}{k+2}\right)\\
&=\frac{1}{3}\left(\frac{1}{1}-\frac{1}{4}+\frac{1}{2}-\frac{1}{5}+\frac{1}{3}-\frac{1}{6}+\frac{1}{4}-\frac{1}{7}+\right.\\
&\quad\quad\quad\quad\quad\left.+\cdots+\frac{1}{n-3}-\frac{1}{n}+\frac{1}{n-2}-\frac{1}{n+1}+\frac{1}{n-1}-\frac{1}{n+2}\right)\\
&=\frac{1}{3}\left(1+\frac{1}{2}+\frac{1}{3}-\frac{1}{n}-\frac{1}{n+1}-\frac{1}{n+2}\right).
\end{align*}
$$

This implies that the series converges and that 

$$
\sum_{n=2}^{\infty}\frac{1}{(n-1)(n+2)}
=\lim\limits_{n\to\infty}\frac{1}{3}\left(\frac{11}{6}-\frac{1}{n}-\frac{1}{n+1}-\frac{1}{n+2}\right)=\frac{11}{18}.
$$

::::::

## Divergence test

If a series is convergent, its general term should tend to zero:

::::::{prf:theorem}
:label: Thm:Series:GeneralTerm
If the series $\displaystyle\sum a_n$ is convergent, then $\lim\limits_{n\to\infty}a_n=0$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:GeneralTerm`
Let $\{s_n\}$ be the sequence of partial sums of the series $\displaystyle\sum a_n$.

If $\displaystyle\sum a_n$ is convergent, then $\lim\limits_{n\to\infty}s_n=s$ exists. Then we have

$$
\lim_{n\to\infty}a_n=\lim_{n\to\infty}\left(s_n-s_{n-1}\right)=\lim_{n\to\infty}s_n-\lim_{n\to\infty}s_{n-1}=s-s=0.
$$

::::::

::::::{prf:corollary}
:label: Thm:Series:GeneralTermCorollary
If $\lim\limits_{n\to\infty}a_n$ does not exist or if $\lim\limits_{n\to\infty}a_n\ne 0$, then the series $\sum a_n$ is divergent.
::::::

::::::{note}
{prf:ref}`Thm:Series:GeneralTermCorollary` is sometimes called "*the test for divergence*" which suggests that a series can only be divergent if the general term does not tend to zero. However, as we will see, this is not true!
::::::

::::::{prf:example}
:label: Ex:Series:DivergentSeries
1) The series $\displaystyle\sum_{n=1}^{\infty}\frac{2n}{3n+1}$ diverges, since $\displaystyle\lim_{n\to\infty}\frac{2n}{3n+1}=\frac{2}{3}\neq0$.

2) The series $\displaystyle\sum_{n=0}^{\infty}\left(\frac{3}{2}\right)^n$ diverges, since $\displaystyle\lim_{n\to\infty}\left(\frac{3}{2}\right)^n=\infty$ does not exist.

3) The series $\displaystyle\sum_{n=1}^{\infty}\sin(n)$ is divergent, since $\displaystyle\lim_{n\to\infty}\sin(n)$ does not exist.

4) The series $\displaystyle\sum_{n=1}^{\infty}\arctan(n)$ is divergent, since $\displaystyle\lim_{n\to\infty}\arctan(n)=\frac{1}{2}\pi\neq0$.
::::::

::::::{warning}
The converse is not true: if $\lim\limits_{n\to\infty}a_n=0$ the series needs not to be convergent!
::::::

::::::{prf:example} The harmonic series
:label: Ex:Series:HarmonicSeries
The **harmonic series** $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$ is divergent.
::::::

::::::{prf:proof}
Note that the terms of the *harmonic series* lie on the graph of $f(x)=\dfrac{1}{x}$:

```{figure} Images/harmonic.png
---
width: 50%
name: harmonic series
align: center
---
Proof of the divergence of the harmonic series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$
```

At each point $n$ we draw a rectangle with width $1$ and height $\dfrac{1}{n}$ to the right. Then, the upper side of each rectangle is above the graph of $f$ since $f$ is decreasing. Hence, we have

$$
\sum_{n=1}^{\infty}\frac{1}{n}=1+\frac{1}{2}+\frac{1}{3}+\cdots > \int_1^{\infty}\frac{1}{x}\,dx.
$$

Now we have: $\displaystyle\int_1^{\infty}\frac{1}{x}\,dx=\bigg[\ln(x)\bigg]_1^{\infty}=\infty$.

This proves that the harmonic series is divergent.
::::::

This proof uses the *integral test*, which will be treated in more details in the next section.

## (Grasple) exercises
