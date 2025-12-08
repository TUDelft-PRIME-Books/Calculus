
# Real numbers

In this section we cover

- Start from natural numbers (includes $0$), integers, rational numbers, and and with real numbers
- Intervals
- Set notation (union, intersection, difference)
- Equations (including quadratic)
- Absolute values
- Inequalities (including quadratics and absolute values)
- Linear systems of two variables (solving by "row" reduction, not by back substitution)

::::{prf:theorem} Triangle inequality for real numbers
:label: thm:triangle_inequality_real_numbers

For any real numbers $a$ and $b$, we have

$$
|a+b| \leq |a| + |b|.
$$

::::::

(Subsec:RealnumbersExp)=

## Exponentiation

We know how to add, subtract, multipy and divide real numbers, but we can perform one more important arithmical operation: exponentiation. You have most likely seen before that by $2^{10}$ we mean

$$
 2^{10}=\underbrace{2\cdot 2\cdot...\cdot 2}_{10\text{ times}}=1024
$$

Now, what do we mean by more complicated powers like $2^0$, $2^{-5}$ or $2^{\frac{1}{2}}$? Or worse, what do we mean when we write $2^\pi$? Let us start by defining the most basic cases and slowly work towards the harder cases.

::::::{prf:definition} 
:label: Def:RealNumbers:Powers1
Let $y$ be a real number. 

- If $n\geq 1$ is a natural number, then $y^n=\underbrace{y\cdot y\cdot...\cdot y}_{n\text{ times}}$
- We have $y^0=1$.
- If $y\neq 0$ and $n\geq 1$ is a natural number then $y^{-n}=\frac{1}{y^n}$.

::::::

::::::{prf:remark}
:label: Remark:RealNumbers:0to0

Following the previous definition we define $0^0=1$. This definition is consistent with the rules of exponentiation that we will see below and there are other good mathematical reasons why this definition makes sense (for instance, it is consistent with the definition of $n^m$ for natural numbers $n,m$ from set theory). However, this definition is not fully standard. The main reason for this is that if $x$ and $y$ both approach $0$ at the same time (but at possibly different rates) the number $x^y$ will not necessarily approach $0$. We will see examples of this in {numref}`Section:lHospital`.

::::::

::::::{prf:theorem} 
:label: Thm:RealNumbers:Squarerootsexsit
Let $y$ be a real number and $n\geq 1$ a natural number. If $n$ is even, then the equation $x^n=y$ has exactly two solutions $x_1$ and $x_2$ if $y>0$, which satisfy $x_1=-x_2$, while the equation $x^n=y$ only has the solution $x=0$ if $y=0$ and the equation $x^n=y$ has no (real) solutions if $y<0$. If $n$ is odd, the equation $x^n=y$ has exactly one solution for each value of $y$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:RealNumbers:Squarerootsexsit`
:class: tudproof, dropdown

This proof uses the completeness of the real numbers, so feel free to skip the proof.

We will only the existence of a solution of the equation $x^n=y$ with $y>0$ when $n=2$. The idea of the proof works for other values of $n$, but there the notation is way more cumbersome. 

Let $y>0$. Consider the set $S=\{x\in\mathbb{R}\,|\,x\geq 0\,\text{and}\,x^2<y\}$. Choose a natural number $k>\frac{1}{y}$. Then $0<\frac{1}{k^2}\leq \frac{1}{k}<y$. So $\frac{1}{k}$ is in $S$, so $S$ is nonempty. Moreover, we can choose a natural number $m>y$. Then for $x\geq m$ we have $x^2\geq m^k\geq m>y$, so such an $x$ does not lie in $S$. As such, $S$ is bounded above by $m$. This means that $S$ is both nonempty and bounded above, so $S$ has a supremum, which we will denote by $x_*$. Moreover, $m\geq x_*\geq\frac{1}{k}>0$, so $x_*$ is positive and satisfies $\frac{1}{k}\leq x_*\leq m$.

Now we will show that $x_*^2=y$. We argue by contradiction, so we assume that this is not the case. First suppose that $x_*^2<y$. For any small number $0<\varepsilon<1$ we have $\varepsilon^2<\varepsilon$, so we can estimate

\begin{align*}
 (x_*+\varepsilon)^2&=x_*^2+2\varepsilon x_*+\varepsilon^2\\ &\leq x_*^2+2\varepsilon x_*+\varepsilon\\ &\leq x_*^2+2\varepsilon m+\varepsilon\\ &=x_*^2+(2m+1)\varepsilon.
\end{align*}

Since $x_*^2<y$ we can choose $\varepsilon$ small enough that $x_*^2+(2m+1)\varepsilon<y$. In that case, we have $(x_*+\varepsilon)^2<y$, so we must have $x_*+\varepsilon$ in $S$. However, this contradicts the fact that $x_*$ is the supremum of $S$.

Now suppose that $x_*^2>y$. Then for $0<\varepsilon<1$ we can estimate

\begin{align*}
 (x_*-\varepsilon)^2&=x_*^2-2\varepsilon x_*+\varepsilon^2\\ &\geq x_*^2-2\varepsilon x_*\\ &\geq x_*^2-2\varepsilon \frac{1}{k}.
\end{align*}

Since $x_*^2>y$ we can choose $\varepsilon$ small enough that $x_*^2-2\varepsilon \frac{1}{k}>y$ and $x_*-\varepsilon>0$. In that case, we have $(x_*-\varepsilon)^2>y$. We claim that $x_*-\varepsilon>x$ for all $x$ in $S$. Indeed, if $0<x_*-\varepsilon<x$ for some $x$ in $S$ then we would have $y<(x_*-\varepsilon)^2<x^2<y$, which gives a contradiction. Hence, $x_*-\varepsilon$ is an upper bound of $S$, smaller than $x_*$. However, this contradicts the fact that $x_*$ is the supremum of $S$.

We conclude that $x_*^2=y$. Now if $0<z<x_*$ then $z^2<x_*^2=y$, while if $z>x_*$ we have $z^2>x_*^2=y$. So the equation $x^2=y$ has exactly one positive solution. 


For the other statements, we return to the general values of $n$. Let $y>0$. First suppose that $n$ is even and that $x_*$ is a positive solution of the equation $x^n=y$. If $x_-<0$ satisfies $x_-^2=y$ then we have

$$
 (-x_-)^n=(-1)^n(x_-)^n=1\cdot x_-^n=x_-^n=y,
$$

so then $-x_-$ is a positive solution of the equation $x^n=y$. Hence, we must have $-x_-=x_*$, i.e. $x_-=-x_*$. On the other hand, if $n$ is odd and $x$ is negative then $x^n$ is the product of an odd amount of negative numbers, which must be negative. Hence, the equation $x^n=y$ does not have any negative solutions if $n$ is odd.

In addition, the equation $x^n=0$ means that $x\cdot x\cdot...\cdot x=0$, which implies that $x=0$. 
 
Finally, since the product of an even amount of positive numbers is always positive and the product of an even amount of negative numbers is always positive, the equation $x^n=y$ does not have any solutions if $y<0$ and $n$ is even. On the other hand, if $n$ is odd, then $(-x)^n=(-1)^nx^n=-x^n$, so if $x^n=y$ then $(-x)^n=-y$. This means that if $n$ is odd, the equation $x^n=y$ also has exactly $1$ solution if $y<0$.
:::

::::::{prf:definition} 
:label: Def:RealNumbers:Powers2
If $y\geq 0$ and $n\geq 1$ is an even natural number, the unique positive solution of the equation $x^n=y$ is called the  $\mathbf{n}$**th square root** of $y$ and is denoted by $\sqrt[n]{y}=y^{\frac{1}{n}}$. If $n=2$, we call this number the **square root** of $y$ and write $\sqrt{y}$ instead of $\sqrt[2]{y}$. In addition, if $y$ is a real number and $n\geq 1$ is an odd natural number, then the unique solution of the equation $x^n=y$ is called the $\mathbf{n}$**th square root** of $y$ and is denoted by $\sqrt[n]{y}=y^{\frac{1}{n}}$.

::::::

We can now consistently define what we mean by $y^{\frac{p}{q}}$ for integers $p\geq 1$ and $q>0$.


::::::{prf:definition} 
:label: Def:RealNumbers:Powers3
Let $y\geq 0$ and $r\neq 0$ be a rational number. Write $r=\frac{p}{q}$ with $p$ and $q$ integers and $q>0$. Then we define $y^{\frac{p}{q}}=\sqrt[q]{y^p}=\left(\sqrt[q]{y}\right)^p$.

Moreover if $y<0$ and $q$ is odd we define $y^{\frac{p}{p}}=\sqrt[q]{y^p}=\left(\sqrt[q]{y}\right)^p$.
::::::

So far, we have been able to define rational powers of nonnegative numbers. So how would we define something like $2^\pi$? Note that our definitions so far give that if $p$ and $q$ are rational numbers with $0<p<q$ we have $2^p<2^q$. Naturally, we want this property to be valid for irrational powers of $x$ as well. So since $3<\pi<4$, we must have

$$
 8=2^3<2^\pi<2^4=16.
$$

Of course, we also know that $3.1<\pi<3.2$ and both of these numbers are rational numbers so we know what we mean by $2^{3.1}$ and $2^{3.2}$. Hence, we must have

$$
 8.6\approx 2^{3.1}<2^\pi<2^{3.2}\approx 9.2.
$$ 

Indeed, we obtain a smaller range of value in which $2^\pi$ can lie, since $3.1$ and $3.2$ are closer to $\pi$ than $3$ and $4$ are. By using more and more decimals, we find

$$
 \begin{array}{lclclcl}
  8&=&2^3&<&2^\pi&<&2^4&=&16,\\
  8.82&\approx &2^{3.14}&<&2^\pi&<&2^{3.15}&\approx& 8.88,\\
  8.821&\approx &2^{3.141}&<&2^\pi&<&2^{3.142}&\approx& 8.827,\\
  8.8244&\approx &2^{3.1415}&<&2^\pi&<&2^{3.1416}&\approx& 8.8250,\\
  &&&&\vdots&&&&
 \end{array}
$$

and we continue like this as long as we want, obtaining better and better approximations for $2^\pi$. It can be shown, and we will do so below, that there is exactly $1$ number greater than all of $2^3,2^{3.1},2^{3.141},2^{3.1415},...$ and less than all of $2^{4},2^{3.15},2^{3.142},2^{3.1416}$ and we define this number to be $2^\pi$. Indeed, we obtain the following result.

::::::{prf:theorem} 
:label: Thm:RealNumbers:Irrationalexp
Let $r\neq 0$ be a real number. For $n\geq 0$ we let $l_n$ be the number $r$ rounded down to $n$ decimals and $u_n$ be the number $r$ rounded up to $n$ decimals. Then for each $y\geq 1$ there is exactly one number greater than or equal to all of $y^{l_0},y^{l_1},y^{l_2},...$ and less than or equal to all of $y^{u_0},y^{u_1},y^{u_2},...$, while for each $0\leq y<1$ there is exactly one number less than or equal to all of $y^{l_0},y^{l_1},y^{l_2},...$ and greater than or equal to all of $y^{u_0},y^{u_1},y^{u_2},...$.
::::::

::::::{prf:definition} 
:label: Def:RealNumbers:Powers4
Let $y\geq 0$ and $r\neq 0$ be a real number. The number from {prf:ref}`Thm:RealNumbers:Irrationalexp` is denoted by $y^r$.
::::::




::::::{warning} 
:name: Warning:Realnumbers:Powersofnegativenumbers

We have seen how to define things like $(-1)^{2}$, $(-1)^{-4}$ and $(-1)^{\frac{5}{3}}$. Now, what do we mean by $(-1)^{\frac{1}{2}}$? We know that for $x\geq 0$ and real numbers $a$ and $b$ we always have the identity $\left(x^a\right)^b=x^{ab}$. Unfortunately, it is impossible to define $(-1)^{\frac{1}{2}}$ in such a way that it is consistent with this rule. Indeed, if we could define it, we would find that

$$
 -1=(-1)^1=(-1)^{2\cdot{\frac{1}{2}}}=\left((-1)^2\right)^{\frac{1}{2}}=1^{\frac{1}{2}}=1
$$

which is not the case. As such, we will not try to define those powers of negative numbers that we have not already defined.
::::::

Het bewijs van die laatste stelling lijkt echt veel te veel en bevat ook veel te veel details en geneuzel. Liever verwijzen.