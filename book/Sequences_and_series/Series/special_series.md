(Sec:Series:SpecialSeries)=
# Special types of series

In this section we consider three special types of series: geometric series, telescoping series and $p$-series. These types of series are important because they often appear in applications and because they can be used to find the sum of some series that do not belong to these types.

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

The special case $a=1$ reads

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

## Telescoping series

In {numref}`Sec:Series:FiniteSeries` we already encountered _telescoping sums_, which were finite series that have the _telescoping property_. We now extend that concept to infinite series, which are called _telescoping series_:

::::{prf:definition}
:label: Def:Series:TelescopingSeries

An infinite series $\displaystyle\sum_{n=m}^{\infty}a_n$ is called a **telescoping series** if there exists a sequence $\{b_n\}_{n=m}^{\infty}$ and a positive integer $p$ such that $a_n=b_{n}-b_{n+p}$ for all $n\in\{m,m+1,m+2,\ldots\}$.
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
If $\displaystyle\sum_{n=m}^{\infty}a_n$ is a telescoping series with $a_n=b_{n}-b_{n+p}$ for all $n\in\{m,m+1,m+2,\ldots\}$ and some integer $p\geq1$, then we have

$$
\sum_{n=m}^{\infty}a_n=\sum_{n=m}^{m+p-1}b_n-p\cdot\lim_{n\to\infty}b_n,
$$

provided that the limit $\lim\limits_{n\to\infty}b_n$ exists.
::::

## $p$-series

A final type of series are _$p$-series_, which are series of the form $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^p}$ for some real number $p$. The _harmonic series_ is the special case of a $p$-series with $p=1$, which you have already seen to be divergent in {prf:ref}`Ex:Series:HarmonicSeries`. The next theorem gives us a complete characterisation of the convergence and divergence of $p$-series:

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