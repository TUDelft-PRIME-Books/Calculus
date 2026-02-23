(Chapter:Series)=

# Series
In this chapter: Under Construction

```{tableofcontents}
```

In this chapter we will study what happens if we try to add the terms of a sequence. Since all sequences have an infinite number of terms, we have to deal with infinite sums. These will be defined as the limit of certain finite sums. So, let's start with finite summations.

The Fibonacci sequence $\{F_n\}_{n=1}^{\infty}$ is defined by $F_{n+2}=F_n+F_{n+1}$ for $n=1,2,3,\ldots$ with $F_1=F_2=1$. Then we have

:::{math}
:label: Eq:Series:FibonacciTelescoping
\begin{align*}
\sum_{k=1}^nF_k&=\sum_{k=1}^n\left(F_{k+2}-F_{k+1}\right)\\
&=F_{n+2}-\cancel{F_{n+1}}+\cancel{F_{n+1}}-\cancel{F_n}+\cdots+\cancel{F_4}-\cancel{F_3}+\cancel{F_3}-F_2\\
&=F_{n+2}-2.
\end{align*}
:::

This is called a **telescoping sum**.

::::{exercise}
:label: Exc:Series:LucasTelescoping
The Lucas sequence $\{L_n\}_{n=1}^{\infty}$ is defined by $L_{n+2}=L_n+L_{n+1}$ for $n=1,2,3,\ldots$ with $L_1=1$ and $L_2=3$.

Simplify $\displaystyle\sum_{k=1}^nL_k$.
::::

:::{admonition} Solution of {numref}`Exc:Series:LucasTelescoping`
:class: solution, dropdown
Again we use the *telescoping property* to find

\begin{align*}
\sum_{k=1}^nL_k&=\sum_{n=1}^n\left(L_{k+2}-L_{k+1}\right)\\
&=L_{n+2}-\cancel{L_{n+1}}+\cancel{L_{n+1}}-\cancel{L_n}+\ldots+\cancel{L_4}-\cancel{L_3}+\cancel{L_3}-L_2\\
&=L_{n+2}-3.
\end{align*}
:::

::::{exercise}
:label: Exc:Series:TelescopingExercise
Use the facts that $n^4+n^2+1=n^4+2n^2+1-n^2=(n^2+1)^2-n^2$ and $2n=n^2+1+n-(n^2+1-n)$ to find the sum of

$$
\sum_{n=1}^{100}\frac{n}{n^4+n^2+1}.
$$

::::

:::{admonition} Solution of {numref}`Exc:Series:TelescopingExercise`
:class: solution, dropdown
Using $n^4+n^2+1=(n^2+1)^2-n^2=(n^2+1+n)(n^2+1-n)$ and $2n=n^2+1+n-(n^2+1-n)$ we obtain

\begin{align*}
\sum_{n=1}^{100}\frac{n}{n^4+n^2+1}&=\frac{1}{2}\sum_{n=1}^{100}\frac{n^2+1+n-(n^2+1-n)}{(n^2+1+n)(n^2+1-n)}\\
&=\frac{1}{2}\sum_{n=1}^{100}\left(\frac{1}{n^2+1-n}-\frac{1}{n^2+1+n}\right).
\end{align*}
In order to see that this is a telescoping sum, let $f(n)=n^2+1-n$, then $f(n+1)=(n+1)^2+1-(n+1)=n^2+2n+1+1-n-1=n^2+1+n$. Hence, we have

\begin{align*}
&\sum_{n=1}^{100}\left(\frac{1}{n^2+1-n}-\frac{1}{n^2+1+n}\right)=\sum_{n=1}^{100}\left(\frac{1}{f(n)}-\frac{1}{f(n+1)}\right)\\
&{}=\frac{1}{f(1)}-\cancel{\frac{1}{f(2)}}+\cancel{\frac{1}{f(2)}}-\cancel{\frac{1}{f(3)}}+\cdots+\cancel{\frac{1}{f(100)}}-\frac{1}{f(101)}\\
&=\frac{1}{f(1)}-\frac{1}{f(101)}.
\end{align*}
We conclude that

\begin{align*}
\sum_{n=1}^{100}\frac{n}{n^4+n^2+1}&=\frac{1}{2}\left(\frac{1}{f(1)}-\frac{1}{f(101)}\right)=\frac{1}{2}\left(1-\frac{1}{100^2+1+100}\right)\\
&=\frac{1}{2}\cdot\frac{10101-1}{10101}=\frac{5050}{10101}.
\end{align*}
:::

In {prf:ref}`Ex:Integration:IntroductionExamplesSum` we have seen that $\displaystyle\sum_{k=1}^nk=\frac{1}{2}n(n+1)$ for all $n\in\{1,2,3,\ldots\}$. This can also be proved using the principle of mathematical induction:

For $n=1$ this reads: $1=\frac{1}{2}\cdot1\cdot2$, which is true.

Suppose that $\displaystyle\sum_{k=1}^nk=\frac{1}{2}n(n+1)$ holds for certain value of $n$. Then we have

$$
\sum_{k=1}^{n+1}k=\sum_{k=1}^nk+(n+1)=\frac{1}{2}n(n+1)+(n+1)=\frac{1}{2}(n+1)(n+2).
$$

Since this is exactly the formula with $n$ replaced by $n+1$, this proves the statement for all $n\in\{1,2,3,\ldots\}$.

::::{exercise}
:label: Exc:Series:IntroductionInduction1
Show that $\displaystyle\sum_{k=1}^nk^2=\frac{1}{6}n(n+1)(2n+1)$ for all $n\in\{1,2,3,\ldots\}$.
::::

:::{admonition} Solution of {numref}`Exc:Series:IntroductionInduction1`
:class: solution, dropdown
For $n=1$ this reads: $1=\frac{1}{6}\cdot1\cdot2\cdot3$, which is true. 

Suppose that $\displaystyle\sum_{k=1}^nk^2=\frac{1}{6}n(n+1)(2n+1)$ holds for certain value of $n$. Then we have

\begin{align*}
\sum_{k=1}^{n+1}k^2&=\sum_{k=1}^nk^2+(n+1)^2=\frac{1}{6}n(n+1)(2n+1)+(n+1)^2\\
&=\frac{1}{6}(n+1)\left\{n(2n+1)+6(n+1)\right\}\\
&=\frac{1}{6}(n+1)(2n^2+7n+6)=\frac{1}{6}(n+1)(n+2)(2n+3).
\end{align*}
Since this is exactly the formula with $n$ replaced by $n+1$, this proves the statement for all $n\in\{1,2,3,\ldots\}$.
:::

::::{exercise}
:label: Exc:Series:IntroductionInduction2
Show that $\displaystyle\sum_{k=1}^nk^3=\left(\sum_{k=1}^nk\right)^2=\frac{1}{4}n^2(n+1)^2$ for all $n\in\{1,2,3,\ldots\}$.
::::

:::{admonition} Solution of {numref}`Exc:Series:IntroductionInduction2`
:class: solution, dropdown
For $n=1$ this reads: $1=\frac{1}{4}\cdot1^2\cdot2^2$, which is true. 

Suppose that $\displaystyle\sum_{k=1}^nk^3=\frac{1}{4}n^2(n+1)^2$ holds for certain value of $n$. Then we have

\begin{align*}
\sum_{k=1}^{n+1}k^3&=\sum_{k=1}^nk^3+(n+1)^3=\frac{1}{4}n^2(n+1)^2+(n+1)^3\\
&=\frac{1}{4}(n+1)^2\left\{n^2+4(n+1)\right\}\\
&=\frac{1}{4}(n+1)^2(n^2+4n+4)=\frac{1}{4}(n+1)^2(n+2)^2.
\end{align*}
Since this is exactly the formula with $n$ replaced by $n+1$, this proves the statement for all $n\in\{1,2,3,\ldots\}$.
:::

::::::{prf:example} Another interesting result
Prove that $\displaystyle\sum_{k=n^2+1}^{(n+1)^2}k=n^3+(n+1)^3$ for all $n\in\{1,2,3,\ldots\}$.

Solution. This can be shown directly: note that the sum has $2n+1$ terms, so we have

\begin{align*}
\sum_{k=n^2+1}^{(n+1)^2}k&=\frac{1}{2}(2n+1)\left\{n^2+1+(n+1)^2\right\}=(2n+1)(n^2+n+1)\\
&=2n^3+3n^2+3n+1=n^3+(n+1)^3.
\end{align*}
::::::
