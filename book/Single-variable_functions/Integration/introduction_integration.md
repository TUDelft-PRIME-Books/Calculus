# Integration
In this chapter: Under Construction

```{tableofcontents}
```

In this chapter we will cover the concept of integration. An **integral** will be introduced as a limit of sums. So, we start with summations.

**Notation for sums**

The notation $\sum$ (capital Greek letter sigma) is used to denote a (finite) sum:
::::::{prf:Definition}
If $a_m,a_{m+1},\ldots,a_n$ are real or complex numbers and $m$ and $n$ are integers with $m\leq n$, then
```{math}
\sum_{i=m}^na_i:=a_m+a_{m+1}+\ldots+a_n.
```
::::::
The letter $i$ is called the **index of summation**.

::::::{prf:Example}
* $\displaystyle\sum_{i=3}^5i^2=3^3+4^2+5^2=9+16+25=50$;
* $\displaystyle\sum_{j=-1}^15^{\frac{1}{2}j}=5^{-\frac{1}{2}}+5^0+5^{\frac{1}{2}}=\frac{1}{\sqrt{5}}+1+\sqrt{5}=1+\frac{6}{5}\sqrt{5}$;
* $\displaystyle\sum_{k=0}^32^k=2^0+2^1+2^2+2^3=1+2+4+8=15$.
::::::

::::::{prf:Example}
Show that the sum $S$ of the first $n$ positive integers equals $\frac{1}{2}n(n+1)$.

**Solution**

Let $S:=\displaystyle\sum_{i=1}^ni$, then we have:
```{math}
\begin{align*}
S&=1&+2&+\ldots&+(n-1)&+n\\
S&=n&+(n-1)&+\ldots&+2&+1.
\end{align*}
```
Adding the two expressions we obtain
```{math}
2S=\underbrace{(n+1)+(n+1)+\ldots+(n+1)+(n+1)}_{n\;\text{times}}.
```
Hence we have: $2S=n(n+1)$ and therefore $S=\frac{1}{2}n(n+1)$.
::::::

::::::{prf:Example}
Let $S=\displaystyle\sum_{i=1}^nar^{i-1}=a+ar+ar^2+\ldots+ar^{n-1}$ with $r\neq1$ and $n$ a positive integer. 

Show that $S=\dfrac{a(1-r^n)}{1-r}$.

**Solution**

```{math}
\begin{align*}
S &=a&+ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&\\
rS&=  &ar&+ar^2&+\ldots&+ar^{n-2}&+ar^{n-1}&+ar^n.
\end{align*}
```
Subtracting the two equations we obtain
```{math}
(1-r)S=a-ar^n=a(1-r^n)\quad\Longrightarrow\quad S=\frac{a(1-r^n)}{1-r},\quad r\neq1.
```
::::::

See chapter~?? for more details about finite sums and series (infinite sums).