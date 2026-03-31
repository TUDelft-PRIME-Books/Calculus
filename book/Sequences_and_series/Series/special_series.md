(Sec:Series:SpecialSeries)=
# Special types of series

## Introduction

In this section we consider several special types of series. These types of series are important because they often appear in applications, we know under which conditions they converge or diverge, and because they can be used to find the convergence of some series that do not belong to these types in later sections.

## Geometric series

One of the most important examples of an infinite series is the geometric series, which is the sum of the terms of a geometric sequence.

::::::{prf:example} 
:label: Ex:Series:GeometricSeries1

Consider the _geometric series_

$$
\sum_{n=1}^{\infty}\left(\frac{1}{2}\right)^n.
$$

The $n$th partial sum of this series is, using $a=1$ and $r=\frac{1}{2}$ in {prf:ref}`Ex:Integration:IntroductionFiniteGeometric`:

\begin{align*}
s_n &= \sum_{k=1}^n\left(\frac{1}{2}\right)^k \\
&= \frac{1}{2}\cdot\frac{1-\left(\frac{1}{2}\right)^n}{1-\frac{1}{2}} \\
&= 1-\left(\frac{1}{2}\right)^n.
\end{align*}


This means that

$$
\lim_{n\to\infty}s_n=\lim_{n\to\infty}\left(1-\left(\frac{1}{2}\right)^n\right)=1,
$$

and so the geometric series $\displaystyle\sum_{n=1}^{\infty}\left(\frac{1}{2}\right)^n$ converges and its sum equals $1$. In other words, we have

$$
\sum_{n=1}^{\infty}\left(\frac{1}{2}\right)^n=1.
$$

This result can also be visualised as shown in {numref}`Fig:Series:GeometricSeries`, which gives a visual proof of the fact that $\displaystyle\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots=1$. The idea behind the visualisation is that when you take a unit square, which has area $1$, and you cut half of it off, then you are left with a rectangle with area $\frac{1}{2}$. If you cut half of this rectangle off, then you are left with a square with area $\frac{1}{4}$. If you cut half of this square off, then you are left with a rectangle with area $\frac{1}{8}$, and so on. If you keep cutting half of the remaining rectangle/square off, then the total area of the cut off rectangles/squares will be $\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots$, which in the end approaches to the area of the original unit square, which is $1$.

```{figure} Images/geometric.png
---
width: 50%
name: Fig:Series:GeometricSeries
align: center
---
A visual proof of $\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\cdots=1$.
```

:::{todo}
Replace {numref}`Fig:Series:GeometricSeries` with an applet.
::: 

::::::

The result of {prf:ref}`Ex:Integration:IntroductionFiniteGeometric` can be used to find the sum of any infinite geometric series:

::::::{prf:theorem} Geometric series
:label: Thm:Series:GeometricSeries
A **geometric series** $\displaystyle\sum_{n=1}^{\infty}ar^{n-1}=a+ar+ar^2+\cdots$ with $a\neq0$ and **common ratio** $r$ is convergent if $|r|<1$ and divergent if $|r|\geq1$.

For $|r|<1$ the sum of the series equals $\displaystyle\frac{a}{1-r}$.
::::::

::::::{admonition} Proof of {prf:ref}`Thm:Series:GeometricSeries`
:class: tudproof, dropdown
For $r=1$ the series trivially diverges. For $r\neq1$ consider the $n$th partial sum

$$
s_n=\displaystyle\sum_{k=1}^nar^{k-1}=a+ar+ar^2+\cdots+ar^{n-1}.
$$

Then we have (compare with {prf:ref}`Ex:Integration:IntroductionFiniteGeometric`)

\begin{align*}
s_n&=a&+ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&\\
rs_n&=&ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&+ar^n.
\end{align*}
Subtracting the two equations we obtain

$$
(1-r)s_n=a-ar^n=a(1-r^n)\quad\Longrightarrow\quad s_n=\frac{a(1-r^n)}{1-r},\quad r\neq1.
$$

In {prf:ref}`Thm:Sequences:ConvergenceGeometric` we have seen that $\lim\limits_{n\to\infty}r^n$ only converges for $-1<r\leq1$ and 

$$
\lim\limits_{n\to\infty}r^n=\begin{cases}0, &-1<r<1\\1, &r=1.\end{cases}
$$

We conclude that the series $\displaystyle\sum_{n=1}^{\infty}ar^{n-1}$ converges for $|r|<1$ and diverges for $|r|\geq1$.

Furthermore, for $|r|<1$ the sum of the series equals $\displaystyle\frac{a}{1-r}$.
::::::

::::::{important}
The best way to remember the sum of a convergent geometric series is

$$
\text{sum}=\frac{\text{first term}}{1-\text{common ratio}}.
$$

Do remember that the series should have starting index $1$ and the power of the common ration should be $n-1$ for this formula to work. If the series does not have this form, then you can always use the properties of finite series to rewrite the series in a form that does have this form, and then apply the formula.

::::::

::::::{note}
:name: Note:Series:GeometricSeries

The special case $a=1$ with starting index $n=0$ reads

$$
\sum_{n=0}^{\infty}r^n=1+r+r^2+\cdots=\frac{1}{1-r},\quad|r|<1.
$$

In {numref}`Sec:Series:PowerSeries` on power series we will often make use of this result.
::::::

::::{prf:example}
:label: Ex:Series:GeometricSeriesExample1

Consider the following infinite sequence:

$$
\frac{1}{5},-\frac{2}{25},\frac{4}{125},-\frac{8}{625},\cdots
$$

In this sequence each next term is the previous term multiplied by $-\frac{2}{5}$, so the common ratio is $r=-\frac{2}{5}$. The first term of the sequence is $a=\frac{1}{5}$, so we can write the series related to this sequence as

$$
\frac{1}{5}-\frac{2}{25}+\frac{4}{125}-\frac{8}{625}+\cdots = \sum_{n=1}^{\infty}\frac{1}{5}\left(-\frac{2}{5}\right)^{n-1}.
$$

Because the common ratio $r=-\frac{2}{5}$ satisfies $|r|<1$, the geometric series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{5}\left(-\frac{2}{5}\right)^{n-1}$ converges and its sum equals

$$
\frac{\frac{1}{5}}{1-\left(-\frac{2}{5}\right)} = \frac{\frac{1}{5}}{1+\frac{2}{5}} = \frac{\frac{1}{5}}{\frac{7}{5}} = \frac{1}{7},
$$

so we can conclude that

$$
\frac{1}{5}-\frac{2}{25}+\frac{4}{125}-\frac{8}{625}+\cdots=\frac{1}{7}.
$$

::::

In your previous studies you may have already encountered the notation $0.\overline{12}=0.1212121212\ldots$ to represent the number that has $12$ repeated indefinitely after the decimal point. We can convert this number into a quotient of integers by using the sum of a geometric series:

::::::{prf:example}
:label: Ex:Series:GeometricSeriesExample2

Notice that $0.\overline{12}$ can be written as:

\begin{align*}
0.\overline{12} &= 0.12121212\ldots \\
&= 0.12 + 0.0012 + 0.000012 + 0.00000012 \cdots \\
&= \frac{12}{100} + \frac{12}{100^2} + \frac{12}{100^3} + \frac{12}{100^4} + \cdots \\
&= \sum_{n=1}^{\infty}\frac{12}{100}\left(\frac{1}{100}\right)^{n-1}.
\end{align*}

By {prf:ref}`Thm:Series:GeometricSeries` the geometric series $\displaystyle\sum_{n=1}^{\infty}\frac{12}{100}\left(\frac{1}{100}\right)^{n-1}$ converges and its sum equals

\begin{align*}
\displaystyle\sum_{n=1}^{\infty}\frac{12}{100}\left(\frac{1}{100}\right)^{n-1} &= \frac{\frac{12}{100}}{1-\frac{1}{100}} \\
&= \frac{\frac{12}{100}}{\frac{99}{100}} \\
&= \frac{12}{99} \\
&= \frac{4}{33}.
\end{align*}

Although this shows the power of geometric series, it is a bit of an overkill to use the formula for the sum of a geometric series to find a fraction for $0.\overline{12}$. The next method is much more straightforward:

$$
100p=12.\overline{12}=12+0.\overline{12}=12+p\quad\Longrightarrow\quad99p=12\quad\Longleftrightarrow\quad p=\frac{12}{99}=\frac{4}{33}.
$$


::::::


::::::{prf:example} 
We express the number $0.\overline{135}=0.135135135\ldots$ as a quotient of integers in two different ways.

First, the number can be written as a geometric series:

$$
0.\overline{135}=\sum_{n=1}^{\infty}\frac{135}{1000^n}.
$$
 
Then, the common ratio is $\dfrac{1}{1000}$ and therefore the geometric series converges and

$$
0.\overline{135}=\frac{\dfrac{135}{1000}}{1-\dfrac{1}{1000}}=\frac{135}{1000-1}=\frac{135}{999}=\frac{15}{111}=\frac{5}{37}.
$$

Second, let $q=0.\overline{135}$, then we have

\begin{align*}
&1000q=135.\overline{135}=135+0.\overline{135}=135+q\\
&\quad\Longrightarrow\quad999q=135\quad\Longleftrightarrow\quad q=\frac{135}{999}=\frac{15}{111}=\frac{5}{37}.
\end{align*}

::::::

(Sec:Series:pSeries)=
## $p$-series

Another type of series are _$p$-series_, which are series of the form $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^p}$ for some real number $p$. The _harmonic series_ is the special case of a $p$-series with $p=1$, which you have already seen to be divergent in {prf:ref}`Ex:Series:HarmonicSeries`. You also have seen a $p$-series with $p=2$ in {prf:ref}`Ex:Series:AbsoluteConvergence1`, which is convergent and has sum $\frac{3}{4}$.

The next theorem gives us a complete characterisation of the convergence and divergence of $p$-series:

::::{prf:theorem} $p$-series
:label: Thm:Series:pSeries

The $p$-series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^p}$ is convergent if $p>1$ and divergent if $p\leq1$.
::::

The proof of this theorem relies again on the use of integrals:

::::::{admonition} Proof of {prf:ref}`Thm:Series:pSeries`
:class: tudproof

For $p=1$ the series is the harmonic series, which we have already shown to be divergent in {prf:ref}`Ex:Series:HarmonicSeries`.

For $p>1$ we will start with a visualisation of the $n$th partial sum of the $p$-series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^p}$, which is given in {numref}`Fig:Series:pSeries`.

```{figure} Images/harmonic.png
:name: Fig:Series:pSeries

Visualisation of the partial sums of a $p$-series for $p>1$. For comparison the graph of $f(x)=\frac{1}{x^p}$ and of $g(x)=\frac{1}{(x+1)^p}$ are also given.
```

:::{todo}
Replace {numref}`Fig:Series:pSeries` with an applet.

Make $p=2$ by default, but allow the user to change $p$ and $n$ to see how the graph changes.
:::

The area of the $n$th rectangle is $\dfrac{1}{n^p}$, so the area of all the rectangles is exactly the $n$th partial sum of the $p$-series. The graph of $f(x)=\dfrac{1}{x^p}$ is also given for comparison. Again we can use the fact that $f$ is a decreasing function to find a lower bound for the $n$th partial sum:

\begin{align*}
s_n &= \sum_{k=1}^n\frac{1}{k^p} \\
&> \sum_{k=1}^n\int_k^{k+1}\frac{1}{x^p}dx \\
&= \int_1^{n+1}\frac{1}{x^p}dx \\
&= \bigg[\frac{1}{1-p}\frac{1}{x^{p-1}}\bigg]_1^{n+1} \\
&= \frac{1}{1-p}\frac{1}{(n+1)^{p-1}} - \frac{1}{1-p}\frac{1}{1^{p-1}} \\
&= \frac{1}{1-p}\left(\frac{1}{(n+1)^{p-1}} - 1\right).
\end{align*}

Because $p>1$, we have $p-1>0$, so $\displaystyle\lim_{n\to\infty}\frac{1}{(n+1)^{p-1}}=0$. Hence, we have

$$
\lim_{n\to\infty}\frac{1}{1-p}\left(\frac{1}{(n+1)^{p-1}} - 1\right) = \frac{1}{1-p}(0-1) = \frac{1}{p-1},
$$

and so

$$
\lim_{n\to\infty}s_n > \frac{1}{p-1}.
$$

On the other hand, we can also find an upper bound for the $n$th partial sum by comparison with the graph of $g(x)=\frac{1}{(x-1)^p}$ for $x\geq2$, as $g$ is also a decreasing function and each rectangle is below the graph of $g$. Hence, we have

\begin{align*}
s_n &= \sum_{k=1}^n\frac{1}{k^p} \\
&= \frac{1}{1^p} + \sum_{k=2}^{n}\frac{1}{k^p} \\
&< 1 + \sum_{k=2}^n\int_{k}^{k+1}\frac{1}{(x-1)^p}dx \\
&= 1 + \int_2^{n+1}\frac{1}{(x-1)^p}dx \\
&= 1 + \bigg[\frac{1}{1-p}\frac{1}{(x-1)^{p-1}}\bigg]_2^{n+1} \\
&= 1 + \frac{1}{1-p}\frac{1}{n^{p-1}} - \frac{1}{1-p}\frac{1}{1^{p-1}} \\
&= 1 + \frac{1}{1-p}\left(\frac{1}{n^{p-1}} - 1\right).
\end{align*}

Again we take the limit as $n$ approaches infinity and we find

$$
\lim_{n\to\infty}s_n < 1 + \frac{1}{1-p}(0-1) = 1-\frac{1}{1-p} = \frac{p}{p-1}.
$$

Since we  now  have found

$$
\frac{1}{p-1}<\lim\limits_{n\to\infty}s_n<\frac{p}{p-1},
$$

the partial sums of the $p$-series are bounded and therefore the series is convergent. Moreover, the sum of the series is a number between $\frac{1}{p-1}$ and $\frac{p}{p-1}$, but we cannot find the exact value of the sum using this method. However, the important thing is that we conclude that the $p$-series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^p}$ is convergent for $p>1$.

For $0<p<1$ we start with observing that we still can compare with the graph of $f(x)=\frac{1}{x^p}$ to find a lower bound for the $n$th partial sum:

$$
s_n > \frac{1}{1-p}\left(\frac{1}{(n+1)^{p-1}} - 1\right).
$$

However, because $0<p<1$ we have $-1<p<0$, so $\displaystyle\lim_{n\to\infty}\frac{1}{(n+1)^{p-1}}=\infty$. Hence the partial sums also must diverge and the $p$-series is divergent for $0<p<1$.

Finally, for $p\leq0$ the general term of the series $\dfrac{1}{n^p}$ does not even approach zero as $n\to\infty$, so by the _test for divergence_ the series is divergent for $p\leq0$.

This proves that the $p$-series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^p}$ is convergent if $p>1$ and divergent if $p\leq1$.
::::::

Later we will see that for $p=2$ the $p$-series evaluates to $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{1}{6}\pi^2\approx1.64493$. We wil do this in {prf:ref}`Ex:Series:FourierExample2` and {prf:ref}`Ex:Series:FourierExample3`.

## Telescoping series

In {numref}`Sec:Series:FiniteSeries` we already encountered _telescoping sums_, which were finite series that have the _telescoping property_. We now extend that concept to infinite series, which are called _telescoping series_:

::::{prf:definition}
:label: Def:Series:TelescopingSeries

An infinite series $\displaystyle\sum_{n=1}^{\infty}a_n$ is called a **telescoping series** if there exists a sequence $\{b_n\}_{n=1}^{\infty}$ and a positive integer $p$ such that $a_n=b_{n}-b_{n+p}$ for all $n\in\{1,2,3,\ldots\}$.
::::

::::::{prf:example}
:label: Ex:Series:TelescopingSeries1

An example of a *telescoping series* is: $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n+1)}$.

Then the $n$th partial sum is: $s_n=\displaystyle\sum_{k=1}^n\frac{1}{k(k+1)}=\sum_{k=1}^n\left(\frac{1}{k}-\frac{1}{k+1}\right)$. Hence we have

$$
s_n=\frac{1}{1}-\cancel{\frac{1}{2}}+\cancel{\frac{1}{2}}-\cancel{\frac{1}{3}}+\cancel{\frac{1}{3}}-\cancel{\frac{1}{4}}+\cdots+\cancel{\frac{1}{n}}-\frac{1}{n+1}=1-\frac{1}{n+1}.
$$

Hence we have $\lim\limits_{n\to\infty}s_n=1$. This implies that the series is convergent and that 

$$
\sum_{n=1}^{\infty}\frac{1}{n(n+1)}=1.
$$

::::::

::::::{prf:example}
:label: Ex:Series:TelescopingSeries2
Another example is: $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n^2-1}$. Then we have

\begin{align*}
\sum_{k=2}^n\frac{1}{k^2-1}&=\sum_{k=2}^n\frac{1}{(k-1)(k+1)}=\frac{1}{2}\sum_{k=2}^n\left(\frac{1}{k-1}-\frac{1}{k+1}\right)\\
&=\frac{1}{2}\left(\frac{1}{1}-\cancel{\frac{1}{3}}+\frac{1}{2}-\cancel{\frac{1}{4}}+\cancel{\frac{1}{3}}-\cancel{\frac{1}{5}}+\cancel{\frac{1}{4}}-\cancel{\frac{1}{6}}+\right.\\
&{}\quad\quad\quad\quad\quad\left.{}\cdots+\cancel{\frac{1}{n-2}}-\frac{1}{n}+\cancel{\frac{1}{n-1}}-\frac{1}{n+1}\right)\\
&=\frac{1}{2}\left(1+\frac{1}{2}-\frac{1}{n}-\frac{1}{n+1}\right).
\end{align*}
This implies that the series converges and that 

$$
\sum_{n=2}^{\infty}\frac{1}{n^2-1}
=\lim\limits_{n\to\infty}\frac{1}{2}\left(\frac{3}{2}-\frac{1}{n}-\frac{1}{n+1}\right)=\frac{3}{4}.
$$

::::::

::::::{prf:example}
:label: Ex:Series:TelescopingSeries3
A third example is: $\displaystyle\sum_{n=2}^{\infty}\frac{1}{(n-1)(n+2)}$. Then we have

\begin{align*}
&\sum_{k=2}^n\frac{1}{(k-1)(k+2)}=\frac{1}{3}\sum_{k=2}^n\left(\frac{1}{k-1}-\frac{1}{k+2}\right)\\
&=\frac{1}{3}\left(\frac{1}{1}-\cancel{\frac{1}{4}}+\frac{1}{2}-\cancel{\frac{1}{5}}+\frac{1}{3}-\cancel{\frac{1}{6}}+\cancel{\frac{1}{4}}-\cancel{\frac{1}{7}}+\right.\\
&{}\quad\quad\quad\quad\quad\left.{}\cdots+\cancel{\frac{1}{n-3}}-\frac{1}{n}+\cancel{\frac{1}{n-2}}-\frac{1}{n+1}+\cancel{\frac{1}{n-1}}-\frac{1}{n+2}\right)\\
&=\frac{1}{3}\left(1+\frac{1}{2}+\frac{1}{3}-\frac{1}{n}-\frac{1}{n+1}-\frac{1}{n+2}\right).
\end{align*}
This implies that the series converges and that 

$$
\sum_{n=2}^{\infty}\frac{1}{(n-1)(n+2)}
=\lim\limits_{n\to\infty}\frac{1}{3}\left(\frac{11}{6}-\frac{1}{n}-\frac{1}{n+1}-\frac{1}{n+2}\right)=\frac{11}{18}.
$$

::::::

If we inspect the last three examples, we see that the sum of a telescoping series is the addition of the first $p$ terms of the sequence $\{b_n\}$ minus $p$ times the limit of the sequence $\{b_n\}$, which is a direct consequence of the telescoping property. We have already summarised this in {prf:ref}`Thm:Series:SumTelescopingSum` for finite telescoping sums, but a similar theorem also holds for infinite telescoping series:

::::{prf:theorem}
:label: Thm:Series:SumTelescopingSeries
If $\displaystyle\sum_{n=1}^{\infty}a_n$ is a telescoping series with $a_n=b_{n}-b_{n+p}$ for all $n\in\{1,2,3,\ldots\}$ and some integer $p\geq1$, then we have

$$
\sum_{n=1}^{\infty}a_n=\sum_{n=1}^{p}b_n-p\cdot\lim_{n\to\infty}b_n,
$$

provided that the limit $\lim\limits_{n\to\infty}b_n$ exists.

If the limit $\lim\limits_{n\to\infty}b_n$ does not exist, the series $\displaystyle\sum_{n=1}^{\infty}a_n$ is divergent.
::::

::::{admonition} Proof of {prf:ref}`Thm:Series:SumTelescopingSeries`
:class: tudproof

The $n$th partial sum of the series $\displaystyle\sum_{n=1}^{\infty}a_n$ is

\begin{align*}
s_n &= \sum_{k=1}^na_k \\
&= \sum_{k=1}^n(b_k - b_{k+p}) \\
&= \sum_{k=1}^nb_k - \sum_{k=1}^nb_{k+p} \\
&= \sum_{k=1}^nb_k - \sum_{k=p+1}^{n+p}b_k \\
&= \sum_{k=1}^pb_k + \sum_{k=p+1}^nb_k - \sum_{k=p+1}^{n+p}b_k \\
&= \sum_{k=1}^pb_k - \sum_{k=n+1}^{n+p}b_k.
\end{align*}

Now assume that $\lim\limits_{n\to\infty}b_n$ exists. We take the limit as $n$ approaches infinity and we find

\begin{align*}
\lim_{n\to\infty}s_n &= \lim_{n\to\infty}\left(\sum_{k=1}^pb_k - \sum_{k=n+1}^{n+p}b_k\right) \\
&= \sum_{k=1}^pb_k - \lim_{n\to\infty}\sum_{k=n+1}^{n+p}b_k \\
&= \sum_{k=1}^pb_k - \sum_{k=n+1}^{n+p}\lim_{n\to\infty}b_k \\
&= \sum_{k=1}^pb_k - p\cdot\lim_{n\to\infty}b_n.
\end{align*}

A final change of the name of the index of summation from $k$ to $n$ gives us

$$
\sum_{n=1}^{\infty}a_n=\sum_{n=1}^{p}b_n-p\cdot\lim_{n\to\infty}b_n.
$$

If the limit $\lim\limits_{n\to\infty}b_n$ does not exist, the limit of the sequence of partial sums $\{s_n\}$ also does not exist, so the series $\displaystyle\sum_{n=1}^{\infty}a_n$ is divergent.

::::

## Alternating series

In {prf:ref}`Def:Sequences:AlternatingSequence` we defined an *alternating sequence* being a sequence $\{a_n\}$ with $a_na_{n+1}<0$ for all $n$, meaning every two consecutive terms have opposite signs. Trying to add the terms of such an alternating sequence leads to an *alternating series*.

::::::{prf:definition}
:label: Def:Series:AlternatingSeries
An **alternating series** is a series whose terms are alternately positive and negative, that is, it is a series of the form

$$
\sum_{n=1}^{\infty}a_n
$$

satisfying $a_na_{n+1}<0$ for all $n\in\{1,2,3,\ldots\}$.

::::::

You already have seen examples of alternating series in {prf:ref}`Ex:Series:AbsoluteConvergence1` and {prf:ref}`Ex:Series:AbsoluteConvergence2` when we studied absolute convergence. Here is one more example of an alternating series: 

::::::{prf:example}
:label: Ex:Series:AlternatingSeries1

We investigate the series $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{n}{n+1}$. The first part of this series is

$$
-\frac{1}{2}+\frac{2}{3}-\frac{3}{4}+\frac{4}{5}-\frac{5}{6},\cdots
$$

Because of the alternating plus and minus signs, we suspect that it is an alternating series. Define $a_n=(-1)^n\dfrac{n}{n+1}$ for all $n\in\{1,2,3,\ldots\}$. Then we have

\begin{align*}
a_na_{n+1} &= (-1)^n\dfrac{n}{n+1}(-1)^{n+1}\dfrac{n+1}{n+2} \\
&= (-1)^{2n+1}\dfrac{n(n+1)}{(n+1)(n+2)} \\
&= -\dfrac{n}{n+2}.
\end{align*}

As $n\geq1$, we have $a_na_{n+1}<0$ for all $n$, so the series $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{n}{n+1}$ is an alternating series.

::::::


Alternating series can always be written as $\displaystyle\sum(-1)^{n-1}b_n$ or $\displaystyle\sum(-1)^nb_n$ with $b_n>0$ for all $n$. 

So what could the sum of alternating series be? Does it even converge?

An initial step could be to investigate whether the series is absolutely convergent. If it is, then we know that the series is convergent, just like in {prf:ref}`Ex:Series:AbsoluteConvergence1`. However, if the series is not absolutely convergent, it could still be (conditionally) convergent. In fact, many alternating series are not absolutely convergent but are still convergent, which is shown by {prf:ref}`Ex:Series:AbsoluteConvergence2`.

If we compare both examples, we see that in both cases the general term of the absolute value of the series tends to zero, i.e. the sequence $\{b_n\}$ tends to zero, ánd in both cases the sequence $\{b_n\}$ is decreasing. It turns out that these two conditions are sufficient for the convergence of an alternating series:

:::::{prf:theorem} Alternating series test
:label: Thm:Series:AlternatingSeriesTest
If the *alternating series* $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}b_n$ with $b_n>0$ satisfies

1) $b_{n+1}\leq b_n$ for all $n$,

2) $\lim\limits_{n\to\infty}b_n=0$,

then the series converges.
:::::

::::{prf:remark}
:label: Rmk:Series:AlternatingSeriesTest
If the first term of the alternating series is negative, i.e. the series is of the form $\displaystyle\sum_{n=1}^{\infty}(-1)^nb_n$ with $b_n>0$, then the conditions for convergence are the same.
::::

::::::{note}
Sometimes the alternating series test is called the **Leibniz criterion**, named after the German mathematician [Gottfried Wilhelm Leibniz (1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz).
::::::

Before we give the proof of {prf:ref}`Thm:Series:AlternatingSeriesTest`, let us first have a visualisation of the alternating series test, which is given in {numref}`Fig:Series:AlternatingSeriesTest`. Consider your series satisfies the conditions of the alternating series test, so $b_n$ is a positive ànd decreasing sequence that tends to zero. Now draw the real number line and put a mark at $0$. Next, mark each of the partial sums $s_1, s_2, s_3, s_4, s_5, \ldots$ on the real number line.

:::{figure} Images/alternating.png
:width: 95%
:name: Fig:Series:AlternatingSeriesTest
:align: center

Visualisation of the alternating series test.
:::

:::{todo}
Replace {numref}`Fig:Series:AlternatingSeriesTest` with an applet.

Make $b_n$ a function of $n$ that the user can change to see how the graph changes?
:::

The alternating nature of the series implies $s_1$ is to the right of $0$, $s_2$ is to the left of $s_1$, $s_3$ is to the right of $s_2$, and so on. Because $b_n$ is a decreasing sequence that tends to zero, the amount you jump to the right or to the left becomes smaller and smaller, so the partial sums seem to get closer and closer to a certain number $s$. This is exactly what it means for the series to be convergent, so it seems the theorem is plausible. The proof of the theorem will make this intuition rigorous, and makes use of the observation that the sequence of even partial sums $s_2,s_4,s_6,\ldots=\{s_{2n}\}$ seems to be located on the left of $s$, and the sequence of odd partial sums $s_1,s_3,s_5,\ldots=\{s_{2n+1}\}$ seems to be located on the right of $s$, but both sequences seem to converge to that same number $s$.


:::{admonition} Proof of {prf:ref}`Thm:Series:AlternatingSeriesTest`
:class: tudproof, dropdown

We first consider the even partial sums $s_2=b_1-b_2\geq0$, $s_4=s_2+(b_3-b_4)\geq s_2$, and so on. In general:

$$
s_{2n+2}=s_{2n}+(b_{2n+1}-b_{2n+2})\geq s_{2n}\quad\text{for}\quad n=1,2,3,\ldots.
$$

Hence:

$$
0\leq s_2\leq s_4\leq s_6\leq \cdots.
$$

However, we also have:

$$
s_{2n}=b_1-(b_2-b_3)-(b_4-b_5)-\cdots-(b_{2n-2}-b_{2n-1})-b_{2n}\leq b_1.
$$

Hence the sequence $\{s_{2n}\}$ of even partial sums is increasing and bounded above and therefore convergent. Say: $\lim\limits_{n\to\infty}s_{2n}=s$. Then we have

$$
\lim\limits_{n\to\infty}s_{2n+1}=\lim\limits_{n\to\infty}(s_{2n}+b_{2n+1})=\lim\limits_{n\to\infty}s_{2n}+\lim\limits_{n\to\infty}b_{2n+1}=s+0=s.
$$  
  
Since both the sequence of even and the sequence of odd partial sums converge to $s$, we conclude that $\lim\limits_{n\to\infty}s_n=s$ and this implies that the series converges.
:::

Let us put the alternating series test to the test by applying it to some examples:

::::::{prf:example}
:label: Ex:Series:AlternatingSeries2
We consider the series $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}\frac{n^2}{n^3+1}$ and investigate the convergence.

It is an alternating series, with $b_n=\displaystyle\frac{n^2}{n^3+1}>0$ for all $n$.

If we define $f(x)=\displaystyle\frac{x^2}{x^3+1}$, we obtain

$$
f'(x)=\frac{2x(x^3+1)-3x^4}{(x^3+1)^2}=\frac{x(2-x^3)}{(x^3+1)^2}<0\quad\text{for}\quad x>1.
$$

This implies that $b_{n+1}\leq b_n$ for $n\geq2$. We also have that $b_1=\frac{1}{2}$ and $b_2=\frac{4}{9}$, so the sequence $\{b_n\}$ is decreasing for $n\geq1$.

Finally, we have

$$
\lim\limits_{n\to\infty}b_n=\lim\limits_{n\to\infty}\frac{n^2}{n^3+1}
=\lim\limits_{n\to\infty}\frac{\frac{1}{n}}{1+\frac{1}{n^3}}=0.
$$

This means that the series $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}\frac{n^2}{n^3+1}$ satisfies the conditions of the alternating series test and therefore is convergent.

::::::

::::::{prf:example}
:label: Ex:Series:AlternatingSeries3

The series $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{3n}{4n+1}$ is an alternating series with $b_n=\displaystyle\frac{3n}{4n+1}>0$ for all $n$. We have

$$
\lim\limits_{n\to\infty}b_n=\lim\limits_{n\to\infty}\frac{3n}{4n+1}=\lim\limits_{n\to\infty}\frac{3}{4+\frac{1}{n}}=\frac{3}{4}.
$$

This means that the series $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{3n}{4n+1}$ does not satisfy the conditions of the alternating series test and we cannot make a conclusion about the convergence of the series using the alternating series test.

::::::

In the previous example the alternating series did not give any definitive conclusion about the convergence of the series, as the conditions were not satisfied. In some, but definitely not all cases, we can still conclude that the series is divergent by using the _test for divergence_, as the general term of the series does not even approach zero. The next two examples illustrate this.

::::::{prf:example}
:label: Ex:Series:AlternatingSeriesDivergence1

We continue {prf:ref}`Ex:Series:AlternatingSeries3` and investigate the convergence of the series $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{3n}{4n+1}$. We have seen that

$$
\lim\limits_{n\to\infty}\frac{3n}{4n+1}=\frac{3}{4}.
$$

Because of the alternating nature of the series, the sequence $\{(-1)^n\frac{3n}{4n+1}\}$ is bounded between $-\frac{3}{4}$ and $\frac{3}{4}$, but not monotonic as it jumps between positive and negative values. Hence, the sequence $\{(-1)^n\frac{3n}{4n+1}\}$ does not converge to zero, so by the _test for divergence_ the series $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{3n}{4n+1}$ is divergent.

::::::

::::::{prf:example}
:label: Ex:Series:AlternatingSeriesDivergence2

Now consider the series $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}b_n$ with

$$
b_n=\begin{cases}
\frac{2}{n+3} & \text{if $n$ is odd},\\
\frac{4}{(n+2)^2} & \text{if $n$ is even}.
\end{cases}
$$

First we take a look at the odd sequence:

$$
\lim\limits_{n\to\infty}b_{2n+1}=\lim\limits_{n\to\infty}\frac{2}{2n+4} = 0
$$

For the even sequence we have

$$
\lim\limits_{n\to\infty}b_{2n}=\lim\limits_{n\to\infty}\frac{4}{(2n+2)^2} = 0
$$

So all terms of the sequence $\{b_n\}$ tend to zero, and the first condition of the alternating series test is satisfied. Next we check whether the sequence $\{b_n\}$ is decreasing.

The first terms of the sequence $\{b_n\}$ are

$$
\frac{1}{2},\frac{1}{4},\frac{1}{3},\frac{1}{9},\frac{1}{4},\frac{1}{16},\ldots
$$

or also written as

$$
\frac{1}{2},\frac{1}{2^2},\frac{1}{3},\frac{1}{3^2},\frac{1}{4},\frac{1}{4^2},\ldots
$$

As $\frac{1}{k+1}>\frac{1}{(k+1)^2}$ for all $k\geq1$, we have $b_{2n+1}>b_{2n}$ for all $n\geq1$. Hence the sequence $\{b_n\}$ is not _always_ decreasing, so the second condition of the alternating series test is not satisfied. Therefore, we cannot conclude that the series $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}b_n$ is convergent by the alternating series test.

To further investigate the convergence of this series, we need more tests that we do not have yet.

::::::

If an alternating series satisfies the conditions of the alternating series test, and so converges, we can also estimate this sum with an upper bound for the remainder in that estimation. This is given by the following theorem:

::::::{prf:theorem} Estimating the sum of an alternating series
:label: Thm:Series:EstimatingSumAlternatingSeries

Let $\displaystyle\sum(-1)^{n-1}b_n$ be an alternating series with $b_n>0$ and $b_{n+1}\leq b_n$ for all $n$, and $\displaystyle\lim\limits_{n\to\infty}b_n=0$. If $s_n$ denotes the $n$th partial sum of the series and $s=\lim\limits_{n\to\infty}s_n$, then we have for the remainder $R_n=s-s_n$:

$$
|R_n|=|s-s_n|\leq b_{n+1}.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:EstimatingSumAlternatingSeries`
:class: tudproof, dropdown
In the proof of the {prf:ref}`alternating series test <Thm:Series:AlternatingSeriesTest>` we have seen that the sum $s$ lies between any two consecutive partial sums $s_n$ and $s_{n+1}$. This implies that

$$
|s-s_n|\leq|s_{n+1}-s_n|=b_{n+1}.
$$

:::

::::::{prf:example}
If we use the first $10$ terms of the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}$ to approximate its sum, what can we say about the error?

The $10$th partial sum is

\begin{align*}
s_{10}=\sum_{n=1}^{10}\frac{(-1)^{n-1}}{n^2}&=1-\frac{1}{4}+\frac{1}{9}-\frac{1}{16}+\frac{1}{25}-\frac{1}{36}+\frac{1}{49}-\frac{1}{64}\\
&{}\quad{}+\frac{1}{81}-\frac{1}{100}=\frac{5194387}{6350400}\approx0.81796.
\end{align*}

{prf:ref}`Thm:Series:EstimatingSumAlternatingSeries` implies that the remainder satisfies:

$$
|R_{10}|=|s-s_{10}|\leq\dfrac{1}{121}\approx0.00826
$$

::::::

::::::{prf:example}
Consider the series $\displaystyle\sum_{n=2}^{\infty}\frac{(-1)^n}{n!}$ with sum $s$ and let $s_N=\displaystyle\sum_{n=2}^N\frac{(-1)^n}{n!}$.

We want to approximate the sum $s$ with the $N$th partial sum $s_N$ such that the approximation is correct to three decimal places using the smallest possible $N$.

An accuracy of three decimal places means that the error can be at most $0.0005$. Hence, we want to find the smallest $N$ such that $|R_N|=|s-s_N|\leq0.0005$.

The $N$th remainder satisfies

$$
|R_N|\leq\dfrac{1}{(N+1)!}$.
$$

Using the required accuracy of $0.0005$, we find that we need to find the smallest $N$ such that

$$
\frac{1}{(N+1)!}<0.0005=\frac{1}{2000}\quad\Longleftrightarrow\quad(N+1)!>2000. 
$$

Note that $6!=720<2000$ and $7!=5040>2000$. This implies that we should take $N+1\geq7$ or $N\geq 6$ to get an approximation which is correct to three decimal places. We have

$$
\sum_{n=2}^6\frac{(-1)^n}{n!}=\frac{1}{2}-\frac{1}{6}+\frac{1}{24}-\frac{1}{120}+\frac{1}{720}=\frac{53}{144}=0.3680\overline{55}\approx0.368.
$$

Note that we round to three decimal places, so the approximation should be correct to three decimal places.

To check that we indeed found an approximation which is correct to three decimal places, we can calculate also the next partial sum:

$$
\sum_{n=2}^7\frac{(-1)^n}{n!}=\frac{1}{2}-\frac{1}{6}+\frac{1}{24}-\frac{1}{120}+\frac{1}{720}-\frac{1}{5040}=\frac{103}{280}=0.367\overline{857142}\approx0.368.
$$

After rounding to three decimal places, we get the same approximation, so we can be sure that the approximation is correct to three decimal places.

If we would have taken $N=5$, we would have found the approximation

$$
\sum_{n=2}^5\frac{(-1)^n}{n!}=\frac{1}{2}-\frac{1}{6}+\frac{1}{24}-\frac{1}{120}=\frac{11}{30}=0.3\overline{66}\approx0.367,
$$

which is the a different approximation as for $N=6$, which indicates that our choice of $N=6$ is best.
::::::

::::::{note}
Later we will be able to show that $\displaystyle\sum_{n=2}^{\infty}\frac{(-1)^n}{n!}=e^{-1}\approx0.36788$. See {prf:ref}`Ex:Series:LogTwo`.
::::::


## Grasple exercises

:::{todo}
Add Grasple exercises for this section.
:::

## Exercises

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