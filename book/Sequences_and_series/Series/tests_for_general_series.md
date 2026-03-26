# Tests for general series

In this section we cover:

- nth term test (i.e. if the terms of a series do not approach 0, it is divergent) (mention the used theorems in the previous section, but only mention the test here)
- Alternating series test
- Ratio test
- Root test
- Rearrangements

Error estimations included in each test where applicable.

## Alternating series

In {prf:ref}`Def:Sequences:AlternatingSequence` we defined an *alternating sequence* being a sequence $\{a_n\}$ with $a_na_{n+1}<0$ for all $n$, id est every two consecutive terms have opposite signs. Trying to add the terms of such an alternating sequence leads to an *alternating series*.

::::::{prf:definition}
:label: Def:Series:AlternatingSeries
An **alternating series** is a series whose terms are alternately positive and negative.

These alternating series can be written as $\displaystyle\sum(-1)^{n-1}b_n$ or $\displaystyle\sum(-1)^nb_n$ with $b_n>0$ for all $n$.
::::::

::::::{prf:example}
1) $\quad\displaystyle1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\cdots=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$;

2) $\quad\displaystyle-\frac{1}{2}+\frac{2}{3}-\frac{3}{4}+\frac{4}{5}-\frac{5}{6}+\cdots=\sum_{n=1}^{\infty}(-1)^n\frac{n}{n+1}$.
::::::

For convergence, at least the general term should tend to zero (so $\lim\limits_{n\to\infty}b_n=0$). In fact, if the sequence $\{b_n\}$ decreases towards zero, the alternating series converges.

:::::{prf:theorem} Alternating series test
:label: Thm:Series:AlternatingSeriesTest
If the *alternating series* $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}b_n$ with $b_n>0$ satisfies

1) $b_{n+1}\leq b_n$ for all $n$,

2) $\lim\limits_{n\to\infty}b_n=0$,

then the series converges.
:::::

::::::{note}
It is not important whether the first term is positive or negative.

Sometimes the alternating series test is called the **Leibniz criterion**, named after the German mathematician [Gottfried Wilhelm Leibniz (1646-1716)](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz).
::::::

:::{figure} Images/alternating.png
:width: 95%
:name: alternating series
:align: center

Proof of the alternating series test
:::

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

::::::{prf:example}
1) The series $\displaystyle1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$ is convergent, since $\displaystyle\frac{1}{n+1}\leq\frac{1}{n}$ for all $n$ and $\lim\limits_{n\to\infty}\displaystyle\frac{1}{n}=0$.

2) The series $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{3n}{4n+1}$ is divergent, since $\displaystyle\lim\limits_{n\to\infty}\frac{3n}{4n+1}=\lim\limits_{n\to\infty}\frac{3}{4+\frac{1}{n}}=\frac{3}{4}\neq0$. This implies that the limit of the general term does not exist (and therefore is not equal to zero).

3) The series $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}\frac{n^2}{n^3+1}$ is convergent, since $b_n=\displaystyle\frac{n^2}{n^3+1}=f(n)$ with $f(x)=\displaystyle\frac{x^2}{x^3+1}$ and therefore

$$
f'(x)=\frac{2x(x^3+1)-3x^4}{(x^3+1)^2}=\frac{x(2-x^3)}{(x^3+1)^2}<0\quad\text{for}\quad x>1.
$$

This implies that $b_{n+1}\leq b_n$ for $n\geq2$. Further we have: 

$$
\lim\limits_{n\to\infty}b_n=\lim\limits_{n\to\infty}\frac{n^2}{n^3+1}
=\lim\limits_{n\to\infty}\frac{\frac{1}{n}}{1+\frac{1}{n^3}}=0.
$$

::::::

::::::{prf:theorem} Estimating the sum of an alternating series
:label: Thm:Series:EstimatingSumAlternatingSeries
Let $\displaystyle\sum(-1)^{n-1}b_n$ be an alternating series with $b_n>0$ and $b_{n+1}\leq b_n$ for all $n$, and $\displaystyle\lim\limits_{n\to\infty}b_n=0$. If $s_n$ denotes the $n$th partial sum of the series and $s=\lim\limits_{n\to\infty}s_n$, then we have for the remainder $R_n$:

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
Use the first $10$ terms of the series $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}$ to approximate its sum. What can be said about the error?

Solution. The $10$th partial sum is

\begin{align*}
s_{10}=\sum_{n=1}^{10}\frac{(-1)^{n-1}}{n^2}&=1-\frac{1}{4}+\frac{1}{9}-\frac{1}{16}+\frac{1}{25}-\frac{1}{36}+\frac{1}{49}-\frac{1}{64}\\
&{}\quad{}+\frac{1}{81}-\frac{1}{100}=\frac{5194387}{6350400}\approx0.81796.
\end{align*}
Then: $|R_{10}|=|s-s_{10}|\leq\dfrac{1}{121}\approx0.00826$. 
::::::

::::::{prf:example}
Consider the series $\displaystyle\sum_{n=2}^{\infty}\frac{(-1)^n}{n!}$ with sum $s$ and let $s_N=\displaystyle\sum_{n=2}^N\frac{(-1)^n}{n!}$. What is the minimum value of $N$ such that $s_N$ is an approximation of the sum $s$ correct to three decimal places?

Solution. The $N$th partial sum is

$$
s_N=\sum_{n=2}^N\frac{(-1)^n}{n!}=\frac{1}{2}-\frac{1}{6}+\frac{1}{24}-\cdots+\frac{(-1)^{N-1}}{(N-1)!}+\frac{(-1)^N}{N!}
$$

with $|R_N|=|s-s_N|\leq\dfrac{1}{(N+1)!}$. Now we have 

$$
\frac{1}{(N+1)!}<0.0005=\frac{1}{2000}\quad\Longleftrightarrow\quad(N+1)!>2000. 
$$

Note that $6!=720<2000$ and $7!=5040>2000$. This implies that we should take $N\geq6$ to get an approximation which is correct to three decimal places. We have

$$
\sum_{n=2}^6\frac{(-1)^n}{n!}=\frac{1}{2}-\frac{1}{6}+\frac{1}{24}-\frac{1}{120}+\frac{1}{720}=\frac{53}{144}\approx0.36806.
$$

::::::

::::::{note}
Later we will be able to show that $\displaystyle\sum_{n=2}^{\infty}\frac{(-1)^n}{n!}=e^{-1}\approx0.36788$. See {prf:ref}`Ex:Series:LogTwo`.
::::::

## The ratio test

::::::{prf:Theorem} Ratio test
:label: Thm:Series:RatioTest
Consider the series $\displaystyle\sum a_n$ with $a_n\in\mathbb{R}$ for all $n$. Then

1) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L<1$, then the series $\displaystyle\sum a_n$ is absolutely convergent;

2) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\infty$, then the series $\displaystyle\sum a_n$ is divergent;

3) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=1$, then this test is inconclusive: the series $\displaystyle\sum a_n$ might be convergent or divergent.
::::::

::::::{note}
Sometimes the ratio test is called **d'Alembert's criterion**, named after the French mathematician  [Jean-Baptiste le Rond d'Alembert (1717-1783)](https://en.wikipedia.org/wiki/Jean_le_Rond_d%27Alembert).
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:RatioTest`
:class: tudproof, dropdown
1) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L<1$ we can choose a number $r$ such that $L<r<1$. Then $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L$ implies that there exists an integer $N$ such that $\displaystyle\left|\frac{a_{n+1}}{a_n}\right| < r$ for all $n\geq N$ or equivalently $|a_{n+1}| < |a_n|r$ for all $n\geq N$. Hence we have:

\begin{align*}
&|a_{N+1}| < |a_N|r,\quad |a_{N+2}| < |a_{N+1}|r < |a_N|r^2,\\
&{}\quad|a_{N+3}| < |a_{N+2}|r < |a_N|r^3,\quad\ldots.
\end{align*}
So we have: $|a_{N+k}| < |a_N|r^k$ for $k=1,2,3,\ldots$. Now the series $\displaystyle\sum_{k=1}^{\infty}|a_N|r^k$ is convergent because it is a geometric series with common ratio $r$ and $0 < r < 1$. This implies that the series $\displaystyle\sum_{n=N+1}^{\infty}|a_n|=\sum_{k=1}^{\infty}|a_{N+k}|$ is convergent. Hence the series $\displaystyle\sum|a_n|$ is convergent.

2) If $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\infty$ we can choose a number $r$ such that $1<r<L$. Then $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L$ implies that the ratio $\displaystyle\left|\frac{a_{n+1}}{a_n}\right|$ will eventually be greater than $r$, that is: there exists an integer $N$ such that $\displaystyle\left|\frac{a_{n+1}}{a_n}\right|>r$ for all $n\geq N$. This implies that $|a_{N+k}|>r^{N+k}$ for $k=0,1,2,\ldots$. This implies that $\displaystyle\sum_{k=0}^{\infty}|a_{N+k}|$ is divergent, since $\displaystyle\sum_{k=1}^{\infty}r^{N+k}$ is a geometric series with common ratio $r>1$ which is divergent.

3) In order to show that the test is inconclusive if $\displaystyle\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=1$, consider the divergent series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$ and the convergent series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$. Note that

$$
\lim\limits_{n\to\infty}\frac{\dfrac{1}{n+1}}{\dfrac{1}{n}}=\lim\limits_{n\to\infty}\frac{n}{n+1}=1
$$

and

$$
\lim\limits_{n\to\infty}\frac{\dfrac{1}{(n+1)^2}}{\dfrac{1}{n^2}}=\lim\limits_{n\to\infty}\frac{n^2}{(n+1)^2}=\lim\limits_{n\to\infty}\left(\frac{n}{n+1}\right)^2=1.
$$

:::

::::::{prf:example}
1) Consider the alternating series $\displaystyle\sum_{n=0}^{\infty}(-1)^n\frac{2n+1}{2^n}$. Let $a_n=\displaystyle(-1)^n\frac{2n+1}{2^n}$, then we have:

\begin{align*}
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|&=\lim\limits_{n\to\infty}\left|(-1)^{n+1}\frac{2n+3}{2^{n+1}}\cdot(-1)^n\frac{2^n}{2n+1}\right|\\
&=\lim\limits_{n\to\infty}\frac{2n+3}{2n+1}\cdot\frac{1}{2}=\frac{1}{2}<1.
\end{align*}
This implies that the series is absolutely convergent.

2) Consider the series $\displaystyle\sum_{n=0}^{\infty}\frac{n!}{5^n}$. Let $a_n=\displaystyle\frac{n!}{5^n}$, then we have:

$$
\lim\limits_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim\limits_{n\to\infty}\left|\frac{(n+1)!}{5^{n+1}}\cdot\frac{5^n}{n!}\right|
=\lim\limits_{n\to\infty}\frac{1}{5}(n+1)=\infty.
$$ 
 
This implies that the series is divergent.
::::::

## The root test

::::::{prf:Theorem} Root test
:label: Thm:Series:RootTest
Consider the series $\displaystyle\sum a_n$ with $a_n\in\mathbb{R}$ for all $n$. Then

1) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L<1$, then the series $\displaystyle\sum a_n$ is absolutely convergent;

2) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\infty$, then the series $\displaystyle\sum a_n$ is divergent;

3) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=1$, then this test is inconclusive: the series $\displaystyle\sum a_n$ might be convergent or divergent.
::::::

::::::{note}
Sometimes the root test is called **Cauchy's criterion**, named after the French mathematician  [Augustin-Louis Cauchy (1789-1857)](https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy).
::::::

:::{admonition} Proof of {prf:ref}`Thm:Series:RootTest`
:class: tudproof, dropdown
1) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L<1$ we can choose a number $r$ such that $L<r<1$. Then $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L$ implies that there exists an integer $N$ such that $\displaystyle\sqrt[n]{|a_n|} < r$. This implies that

$$
\sqrt[N+k]{|a_{N+k}|} < r\quad\Longrightarrow\quad |a_{N+k}| < r^{N+k},\quad k=0,1,2,\ldots.
$$

This implies that $\displaystyle\sum_{k=0}^{\infty}|a_{N+k}|$ is convergent, since $\displaystyle\sum_{k=0}^{\infty}r^{N+k}$ is a geometric series with common ratio $r$ with $0 < r < 1$ which is convergent.

2) If $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L>1$ or $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\infty$, we can choose a number $r$ such that $1<r<L$. Then $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=L$ implies that $\displaystyle\sqrt[n]{|a_n|}$ will eventually be greater than $r$, that is: there exists an integer $N$ such that $\displaystyle\sqrt[n]{|a_n|}>r$ for all $n\geq N$. This implies that

$$
\sqrt[N+k]{|a_{N+k}|} > r\quad\Longrightarrow\quad |a_{N+k}| > r^{N+k},\quad k=0,1,2,\ldots.
$$

This implies that $\displaystyle\sum_{k=0}^{\infty}|a_{N+k}|$ is divergent, since $\displaystyle\sum_{k=0}^{\infty}r^{N+k}$ is a geometric series with common ratio $r$ with $r > 1$ which is divergent.

3) In order to show that the test is inconclusive if $\displaystyle\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=1$, consider the series $\displaystyle\sum a_n$ with $a_n=e^{-\sqrt{n}}$ and the series $\displaystyle\sum b_n$ with $b_n=\left(1+\dfrac{1}{n}\right)^n$. Then we have

$$
\lim_{n\to\infty}\sqrt[n]{|a_n|}=\lim_{n\to\infty}e^{-\frac{1}{\sqrt{n}}}=e^0=1
$$

and

$$
\lim_{n\to\infty}\sqrt[n]{|b_n|}=\lim_{n\to\infty}\left(1+\frac{1}{n}\right)=1+0=1.
$$

The series $\displaystyle\sum a_n$ is convergent due to the integral test, since by using the substitution $x=t^2$ and integration by parts we have

\begin{align*}
\int_0^{\infty}e^{-\sqrt{x}}\,dx&=\int_0^{\infty}e^{-t}\,2t\,dt=-\int_0^{\infty}2t\,de^{-t}\\
&=-2te^{-t}\bigg|_0^{\infty}+2\int_0^{\infty}e^{-t}\,dt=0-2e^{-t}\bigg|_0^{\infty}=2.
\end{align*}
The series $\displaystyle\sum b_n$ is divergent, since 

$$
\lim_{n\to\infty}b_n=\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e\neq0.
$$

:::

::::::{prf:example}
1) Consider the alternating series $\displaystyle\sum_{n=0}^{\infty}\left(\frac{2n+1}{3n+4}\right)^n$. Let $a_n=\displaystyle\left(\frac{2n+1}{3n+4}\right)^n$, then we have:

$$ 
\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\lim\limits_{n\to\infty}\left|\frac{2n+1}{3n+4}\right|=\frac{2}{3}<1.
$$ 
 
This implies that the series is absolutely convergent.

2) Consider the series $\displaystyle\sum_{n=1}^{\infty}\left(\frac{2n+1}{n}\right)^n$. Let $a_n=\displaystyle\frac{2n+1}{n}$, then we have:

$$
\lim\limits_{n\to\infty}\sqrt[n]{|a_n|}=\lim\limits_{n\to\infty}\left|\frac{2n+1}{n}\right|=2.
$$ 
 
This implies that the series is divergent.
::::::
