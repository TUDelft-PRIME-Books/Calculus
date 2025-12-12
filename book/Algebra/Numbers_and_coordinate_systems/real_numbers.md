
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
 2^{10}=\underbrace{2\cdot 2\cdot\cdots\cdot 2}_{10\text{ times}}=1024
$$

Now, what do we mean by more complicated powers like $2^0$, $2^{-5}$ or $2^{\frac{1}{2}}$? Or worse, what do we mean when we write $2^\pi$? Let us start by defining the most basic cases and slowly work towards the harder cases.

::::::{prf:definition} 
:label: Def:RealNumbers:Powers1
Let $y$ be a real number. 

- If $n\geq 1$ is a natural number, then $y^n=\underbrace{y\cdot y\cdot\cdots\cdot y}_{n\text{ times}}$
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

In addition, the equation $x^n=0$ means that $x\cdot x\cdot\cdots\cdot x=0$, which implies that $x=0$. 
 
Finally, since the product of an even amount of positive numbers is always positive and the product of an even amount of negative numbers is always positive, the equation $x^n=y$ does not have any solutions if $y<0$ and $n$ is even. On the other hand, if $n$ is odd, then $(-x)^n=(-1)^nx^n=-x^n$, so if $x^n=y$ then $(-x)^n=-y$. This means that if $n$ is odd, the equation $x^n=y$ also has exactly $1$ solution if $y<0$.
:::

::::::{prf:definition} 
:label: Def:RealNumbers:Powers2
If $y\geq 0$ and $n\geq 1$ is an even natural number, the unique positive solution of the equation $x^n=y$ is called the  $\mathbf{n}$**th square root** of $y$ and is denoted by $\sqrt[n]{y}=y^{\frac{1}{n}}$. If $n=2$, we call this number the **square root** of $y$ and write $\sqrt{y}$ instead of $\sqrt[2]{y}$. In addition, if $y$ is a real number and $n\geq 1$ is an odd natural number, then the unique solution of the equation $x^n=y$ is called the $\mathbf{n}$**th square root** of $y$ and is denoted by $\sqrt[n]{y}=y^{\frac{1}{n}}$.

::::::

We can now consistently define what we mean by $y^{\frac{p}{q}}$ for integers $p$ and $q>0$.


::::::{prf:definition} 
:label: Def:RealNumbers:Powers3
Let $y> 0$ and $r\neq 0$ be a rational number. Write $r=\frac{p}{q}$ with $p$ and $q$ integers and $q>0$. Then we define $y^{\frac{p}{q}}=\sqrt[q]{y^p}=\left(\sqrt[q]{y}\right)^p$.

Moreover if $y<0$ and $q$ is odd we define $y^{\frac{p}{q}}=\sqrt[q]{y^p}=\left(\sqrt[q]{y}\right)^p$. Finally if $y=0$ and $p>0$ we define $y^{\frac{p}{q}}=0$.
::::::

Before we move on to irrational powers, we first some general calculation rules for exponents. These will carry over to irrational exponents as well, but we need these rules to properly define irrational powers. Because of this, we will call this result a lemma, which is just a fancy word for an intermediate result that is useful for proving a bigger result, but not necessarily interesting in and by itself.

::::::{prf:lemma} 
:label: Thm:RealNumbers:ExpCalcRat
Let $y> 0$ and $z> 0$ and let $p$ and $q$ be rational numbers.

- We have $\left(y^p\right)^q=y^{pq}$.
- We have $(yz)^p=y^pz^p$.
- We have $y^{p+q}=y^py^q$.
- We have $y^{p-q}=\dfrac{y^p}{y^q}$.
- If $y>1$ and $p<q$ then $y^p<y^q$.
- If $0<y<1$ and $p<q$ then $y^p>y^q$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:RealNumbers:ExpCalcRat`
:class: tudproof, dropdown
Before we can prove any of the properties, we actually need to check that our definition of $y^{\frac{a}{b}}$ is well-defined. What we mean by this, is that there are multiple ways to represent a rational number as a fraction of an integer and a positive integer and we need to check whether different representations give the same definition of $y^{\frac{a}{b}}$. For this we let $r\neq 0$ be a rational number. We write $r=\frac{a}{b}$ for integers $a$ and $b$ with $b>0$ in such a way that the fraction $\frac{a}{b}$ cannot be simplified any further (that is to say, the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) of $a$ and $b$ should be $1$). Then if $r=\frac{c}{d}$ with $c$ and $d$ integers and $d>0$, we must have $c=na$ and $d=nb$ for some positive integer $n$. For this, we check that $\left(y^{\frac{a}{b}}\right)^{nb}=y^{na}$, which must mean that $y^{\frac{a}{b}}=\sqrt[nb]{y^{na}}=y^{\frac{na}{nb}}$. We can compute if $a>0$

\begin{align*}
 \left(y^{\frac{a}{b}}\right)^{nb}&=\underbrace{y^{\frac{a}{b}}\cdot\cdots\cdot  y^{\frac{a}{b}}}_{nb\text{ times}}\\
 &=\underbrace{\underbrace{y^{\frac{a}{b}}\cdot\cdots\cdot  y^{\frac{a}{b}}}_{b\text{ times}}\cdot\cdots\cdot \underbrace{y^{\frac{a}{b}}\cdot\cdots\cdot  y^{\frac{a}{b}}}_{b\text{ times}}}_{n\text{ times}}\\
 &=\underbrace{\left(y^{\frac{a}{b}}\right)^b\cdot\cdots\cdot \left(y^{\frac{a}{b}}\right)^b}_{n\text{ times}}\\
 &=\underbrace{y^a\cdot\cdots\cdot y^a}_{n\text{ times}}\\
 &=\underbrace{\underbrace{y\cdot\cdots\cdot y}_{a\text{ times}}\cdot\cdots\cdot \underbrace{y\cdot\cdots\cdot y}_{a\text{ times}}}_{n\text{ times}}\\
 &=\underbrace{y\cdot\cdots\cdot y}_{na\text{ times}}\\
 &=y^{na}.
\end{align*}

If $a<0$ the same computation and conclusion holds, except that we should write $y^a=\underbrace{\frac{1}{y}\cdot\cdots\cdot \frac{1}{y}}_{|a|\text{ times}}$. We conclude that $y^{\frac{a}{b}}=y^{\frac{na}{nb}}$, so the choice of how we represent the rational power does not influence the outcome.

First we prove $\left(y^p\right)^q=y^{pq}$. For this, we write $p=\frac{a}{b}$ and $q=\frac{c}{d}$ with $a$, $b$, $c$ and $d$ integers with $b>0$ and $d>0$. Then we have

$$
 \left(y^p\right)^q=\sqrt[d]{\left(y^p\right)^c}=\sqrt[d]{\left(\sqrt[b]{y^a}\right)^c}.
$$

Note that $pq=\frac{a}{b}\frac{c}{d}=\frac{ac}{bc}$, so we have

$$
 y^{pq}=\sqrt[bd]{y^{ac}}.
$$

We set out to show that $\left(\left(y^p\right)^q\right)^{bd}=y^{ac}$, which must imply that $\left(y^p\right)^q=\sqrt[bd]{y^{ac}}=y^{pq}$ For convenience, we assume that $a>0$ and $c>0$. In that case, we find

\begin{align*}
 \left(\left(y^p\right)^q\right)^{bd}&=\left(\sqrt[d]{\left(\sqrt[b]{y^a}\right)^c}\right)^{bd}\\
 &=\underbrace{\sqrt[d]{\left(\sqrt[b]{y^a}\right)^c}\cdot\cdots\cdot \sqrt[d]{\left(\sqrt[b]{y^a}\right)^c}}_{bd\text{ times}}\\
 &=\underbrace{\underbrace{\sqrt[d]{\left(\sqrt[b]{y^a}\right)^c}}_{d\text{ times}}\cdot\cdots\cdot\underbrace{\sqrt[d]{\left(\sqrt[b]{y^a}\right)^c}}_{d\text{ times}}}_{b\text{ times}}\\
 &=\underbrace{\left(\sqrt[d]{\left(\sqrt[b]{y^a}\right)^c}\right)^d\cdot\cdots\cdot\left(\sqrt[d]{\left(\sqrt[b]{y^a}\right)^c}\right)^d}_{b\text{ times}}\\
 &=\underbrace{\left(\sqrt[b]{y^a}\right)^c\cdot\cdots\cdot\left(\sqrt[b]{y^a}\right)^c}_{b\text{ times}}\\
 &=\underbrace{\underbrace{\sqrt[b]{y^a}}_{c\text{ times}}\cdot\cdots\cdot\underbrace{\sqrt[b]{y^a}}_{c\text{ times}}}_{b\text{ times}}\\
 &=\underbrace{\sqrt[b]{y^a}\cdot \cdots\cdot \sqrt[b]{y^a}}_{bc\text{ times}}\\
 &=\underbrace{\underbrace{\sqrt[b]{y^a}}_{b\text{ times}}\cdot\cdots\cdot\underbrace{\sqrt[b]{y^a}}_{b\text{ times}}}_{c\text{ times}}\\
 &=\underbrace{\left(\sqrt[b]{y^a}\right)^a\cdot\cdots\cdot\left(\sqrt[b]{y^a}\right)^a}_{c\text{ times}}\\
 &=\underbrace{y^a\cdot\cdots\cdot y^a}_{c\text{ times}}\\
 &=\underbrace{\underbrace{y\cdot\cdots\cdot y}_{a\text{ times}}\cdot\cdots\cdot\underbrace{y\cdot\cdots\cdot y}_{a\text{ times}}}_{c\text{ times}}\\
 &=\underbrace{y\cdot\cdots y}_{ac\text{ times}}\\
 &=y^{ac},
\end{align*}

as desired. If $a$ and/or $c$ is negative then expressions like $y^a$ should be written like $\underbrace{\frac{1}{y}\cdot\cdots\cdot{1}{y}}_{|a|\text{ times}}$, but otherwise the computation does not change. As such, we find that $\left(y^p\right)^q=\sqrt[bd]{y^{ac}}=y^{pq}$.

We now prove $(yz)^p=y^pz^p$. For this, we write $p=\frac{a}{b}$ with $a$ and $b$ integers and $b>0$. Then we have

$$
 \left(y^pz^p\right)^b=\underbrace{\left(y^pz^p\right)\cdot\cdots\cdot \left(y^pz^p\right)}_{b\text{ times}}=\underbrace{\left(y^p\right)\cdot\cdots\cdot \left(y^p\right)}_{b\text{ times}}\underbrace{\left(z^p\right)\cdot\cdots\cdot \left(z^p\right)}_{b\text{ times}}=\left(y^p\right)^b\left(z^p\right)^b
$$

Moreover, we have $\left(y^p\right)^b=\left(\sqrt[b]{y^a}\right)^b=y^a$ since $p=\frac{a}{b}$. Similalrly, we have $\left(z^p\right)^b=z^a$. Combining these equations, we find if $a>0$


$$
 \left(y^pz^p\right)^b=y^az^a=\underbrace{y\cdot\cdots\cdot y}_{a\text{ times}}\underbrace{z\cdot\cdots\cdot z}_{a\text{ times}}=\underbrace{yz\cdot\cdots\cdot yz}_{a\text{ times}}=(yz)^a,
$$

while if $a<0$ we have


$$
 \left(y^pz^p\right)^b=y^az^a=\underbrace{\frac{1}{y}\cdot\cdots\cdot \frac{1}{y}}_{|a|\text{ times}}\underbrace{\frac{1}{z}\cdot\cdots\cdot \frac{1}{z}}_{|a|\text{ times}}=\underbrace{\frac{1}{yz}\cdot\cdots\cdot \frac{1}{z}}_{|a|\text{ times}}=(yz)^a.
$$

As such, we find $y^pz^p=\sqrt[b]{(yz)^a}=(yz)^p$, as desired.

We now prove $y^{p+q}=y^py^q$. For this, we write $q=\frac{a}{b}$ with $a$ and $b$ integers and $b>0$. By multiplying both $a$ and $b$ by the same positive integer if necessary (which does not change the value of $q$), we can assume that $pb$ is an integer. Then using the previous properties, we find that

$$
 \left(\frac{y^{p+q}}{y^p}\right)^b=\frac{y^{bp+bq}}{y^{bp}}=\frac{y^{bp+a}}{y^{bp}}.
$$

Since both $bp+a$ and $bp$ are integers, the expressions $y^{bp+a}$ and $y^{bp}$ are the product of $bp+a$ respectively $bp$ factors $y$ (where if one of these exponents is negative, we mean the corresponding number of factors $\frac{1}{y}$). This means that both the numerator and the denominator have $bp$ factors $y$ which cancel out to each other. In the numerator, we still have $a$ factors $y$, while in the denominator we have nothing left. As such, we find that 

$$
 \left(\frac{y^{p+q}}{y^p}\right)^b=\frac{y^{bp+bq}}{y^{bp}}=\frac{y^{bp+a}}{y^{bp}}=\frac{y^a}{1}=y^a.
$$

By definition, this means that $\frac{y^{p+q}}{y^p}$ is the $b$th square root of $y^a$, so we find 

$$
 \frac{y^{p+q}}{y^p}=\sqrt[b]{y^a}=y^{\frac{a}{b}}=y^q
$$

Multiplying both sides of this equation by $y^p$ gives the desired result $y^{p+q}=y^py^q$.

We now prove $y^{p-q}=\frac{y^p}{y^q}$. By the first property we have 

$$
 y^{-q}=y^{(-1)\cdot q}=\left(y^q\right)^{-1}=\frac{1}{y^q}.
$$

As such, we obtain with the third property that

$$
 y^{p-q}=y^{p+(-q)}=y^py^{-q}=y^p\frac{1}{y^q}=\frac{y^p}{y^q},
$$ 

as desired.

Now suppose that $y>1$ and $p<q$. We will show that $y^p<y^q$. Since $y>0$, we have by definition that $y^p>0$. Using the fourth property we can compute

$$
 \frac{y^q}{y^p}=y^{q-p}.
$$

Since $y^p>0$, we see that $y^p<y^q$ precisely when $\frac{y^q}{y^p}>1$, i.e. when $y^{q-p}>1$. Since $p<q$ we have $q-p>0$. Write $q-p=\frac{a}{b}$ with $a$ and $b$ positive integers. We argue by contradiction, so we assume that $y^{q-p}\leq 1$. Again, since $y>0$ we must certainly have $y^{q-p}>0$, so $0<y^{q-p}\leq 1$. Then we must have 

$$
 \left(y^{q-p}\right)^b=\underbrace{y^{q-p}\cdot\cdots\cdot y^{q-p}}_{b\text{ times}}\leq 1,
$$

since the product of two real numbers between $0$ and $1$ is again between $0$ and $1$. However, since $y>1$ we must have $y^a>1$ as well, since the product of two real numbers greater than $1$ is again greater than $1$, so we also have

$$
 \left(y^{q-p}\right)^b=\left(y^{\frac{a}{b}}\right)^b=y^a>1.
$$

Since $\left(y^{q-p}\right)^b$ cannot at the same time be less than $1$ and greater than $1$, we arrive at a contradiction. So we must have $y^{q-p}>1$, which means that $y^p<y^q$, as desired.

Finally, we assume that $0<y<1$ and $p<q$. Then $\frac{1}{y}>1$ and $-q<-p$, so with the previous property we must have $\left(\frac{1}{y}\right)^{-q}<\left(\frac{1}{y}\right)^{-p}$. Moreover, using the first property we have

$$ 
 \left(\frac{1}{y}\right)^{-q}=\left(y^{-1}\right)^{-q}=y^{(-1)\cdot (-q)}=y^q
$$ 

and similarly we have $\left(\frac{1}{y}\right)^{-p}=y^{p}$. So we find $y^q<y^p$, as desired.

:::

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

and we continue like this as long as we want, obtaining better and better approximations for $2^\pi$. It can be shown, and we will do so below, that there is exactly $1$ number greater than all of $2^3,2^{3.1},2^{3.141},2^{3.1415},\ldots$ and less than all of $2^{4},2^{3.15},2^{3.142},2^{3.1416}$ and we define this number to be $2^\pi$. Indeed, we obtain the following result.

::::::{prf:theorem} 
:label: Thm:RealNumbers:Irrationalexp
Let $r\neq 0$ be a real number. For $n\geq 0$ we let $l_n$ be the number $r$ rounded down to $n$ decimals and $u_n$ be the number $r$ rounded up to $n$ decimals. Then for each $y\geq 1$ there is exactly one number greater than or equal to all of $y^{l_0},y^{l_1},y^{l_2},\ldots$ and less than or equal to all of $y^{u_0},y^{u_1},y^{u_2},\ldots$, while for each $0<y<1$ there is exactly one number less than or equal to all of $y^{l_0},y^{l_1},y^{l_2},\ldots$ and greater than or equal to all of $y^{u_0},y^{u_1},y^{u_2},\ldots$.
::::::

:::{admonition} Proof of {prf:ref}`Thm:RealNumbers:Irrationalexp`
:class: tudproof, dropdown
This proof uses the completeness of the real numbers, which is a bit beyond the scope of this book, so feel free to skip this proof.

We first suppose $y>1$. We consider the sets $L=\{y^{l_0},y^{l_1},y^{l_2},\ldots\}$ and $U=\left\{y^{u_0},y^{u_1},y^{u_2},\ldots\right\}$. Since $l_n$ is the number $r$ rounded down to $n$ decimals and $u_n$ is the number $r$ rounded up to $n$ decimals, we find that $l_0\leq l_1\leq\ldots\leq r\leq\ldots\leq u_1\leq u_0$. Since $l_0,l_1,\ldots$ and $u_0,u_1,\ldots$ are rational numbers and $y>1$, we obtain by {prf:ref}`Thm:RealNumbers:ExpCalcRat` that $y^{l_0}\leq y^{l_1}\leq\ldots\leq y^{u_1}\leq y^{u_0}$.  So $y^{u_0}$ is an upper bound for the set $L$ and $y^{l_0}$ is a lower bound for the set $U$. By the completeness of the real numbers, $L$ has a supremum, i.e. least upper bound, $l_*$; that is, $l_*\geq y^{l_n}$ for all natural numbers $n$ and $l_*\leq b$ for all upper bounds $b$ of $L$. Similarly, $U$ has an infimum, i.e. greatest lower bound, $u_*$; that is, $u_*\leq y^{u_n}$ for all natural numbers $n$ and $u_*\geq a$ for all lower bounds $a$ of $U$. We will show that $l_*=u_*$, which means that this number is the only number less than or equal to all of $y^{l_0},y^{l_1},y^{l_2},\ldots$ and greater than or equal to all of $y^{u_0},y^{u_1},y^{u_2},\ldots$.

Since $y^{l_n}\leq y^{u_m}$ for all natural numbers $n$ and $m$, each element in $U$ is an upper bound for $L$. So we find that $y^{u_m}\geq l_*$ for each $m$, since $l_*$ is the least upper bound of $L$. This means that $l_*$ is a lower bound of $U$, so we must have $l_*\leq u_*$. We argue by contradiction and assume that $l_*< u_*$. This means that $d=u_*-l_*>0$. Using {prf:ref}`Thm:RealNumbers:ExpCalcRat` we have for all $n$ that

$$
 y^{u_n}-y^{l_n}=y^{(u_n-l_n)+l_n}-y^{l_n}=y^{u_n-l_n}y^{l_n}-y^{l_n}=\left(y^{u_n-l_n}-1\right)y^{l_n}.
$$

We first note that $y^{l_n}\leq y^{u_0}$ for all $n$. In addition, since $u_n$ and $l_n$ are the number $r$ rounded to $n$ decimals up and down respectively, we have $u_n-l_n\leq \frac{1}{10^n}$ for all $n$. Using {prf:ref}`Thm:RealNumbers:ExpCalcRat` we find

$$
 y^{u_n}-y^{l_n}=\left(y^{u_n-l_n}-1\right)y^{l_n}\leq \left(y^{u_n-l_n}-1\right)y^{u_0}\leq \left(y^{\frac{1}{10^n}}-1\right)y^{u_0}
$$

 Since $d>0$ we have $1+\frac{d}{2y^{u_0}}>1$. As such, we can find a (possibly very large) natural number $n$ with $y<\left(1+\frac{d}{2y^{u_0}}\right)^{10^n}$. By {prf:ref}`Thm:RealNumbers:ExpCalcRat` we have, for this value of $n$, that 

\begin{align*}
 y^{u_n}-y^{l_n}&\leq \left(y^{\frac{1}{10^n}}-1\right)y^{u_0}\\ &\leq \left(\left(\left(1+\frac{d}{2y^{u_0}}\right)^{10^n}\right)^{\frac{1}{10^n}}-1\right)y^{u_0}\\ &\left(1+\frac{d}{2y^{u_0}}-1\right)y^{u_0}\\ &=\frac{d}{2}.
\end{align*}

However, since $y^{u_n}\geq u_*$ and $y^{l_n}\leq l_*$ we now obtain

$$
 d=u_*-l_*\leq y^{u_n}-l_*\leq y^{u_n}-y^{l_n}\leq \frac{d}{2},
$$

which is impossible since $d>0$. As such, we have $l_*=u_*$, which means that this number is the only number less than or equal to all of $y^{l_0},y^{l_1},y^{l_2},\ldots$ and greater than or equal to all of $y^{u_0},y^{u_1},y^{u_2},\ldots$, as desired.

Now if $y=1$, then $y^r=1$ for all rational numbers, so all of the numbers $y^{l_0},y^{l_1},y^{l_2},\ldots$ and $y^{u_0},y^{u_1},y^{u_2},\ldots$ are $1$, so there is indeed exactly one number in between these numbers, namely the number $1$.

Finally, if $0<y<1$ we can follow a very similar approach as for $y>1$, except that many inequalities are now reversed. It can be interesting to work out the full details yourself (or you can just believe us that it all works out).
:::

::::::{prf:definition} 
:label: Def:RealNumbers:Powers4
Let $y\geq 0$ and $r\neq 0$ be a real number. The number from {prf:ref}`Thm:RealNumbers:Irrationalexp` is denoted by $y^r$. Moreover, if $r>0$ we define $0^r=0$.
::::::


::::::{warning} 
:name: Warning:Realnumbers:Powersofnegativenumbers

We have seen how to define things like $(-1)^{2}$, $(-1)^{-4}$ and $(-1)^{\frac{5}{3}}$. Now, what do we mean by $(-1)^{\frac{1}{2}}$? We know that for $x\geq 0$ and real numbers $a$ and $b$ we always have the identity $\left(x^a\right)^b=x^{ab}$. Unfortunately, it is impossible to define $(-1)^{\frac{1}{2}}$ in such a way that it is consistent with this rule. Indeed, if we could define it, we would find that

$$
 -1=(-1)^1=(-1)^{2\cdot{\frac{1}{2}}}=\left((-1)^2\right)^{\frac{1}{2}}=1^{\frac{1}{2}}=1
$$

which is not the case. As such, we will not try to define those powers of negative numbers that we have not already defined.
::::::

The calculation rules from {prf:ref}`Thm:RealNumbers:ExpCalcRat` remain true for arbitrary exponents.

::::::{prf:theorem} 
:label: Thm:RealNumbers:ExpCalcReal
Let $y\geq 0$ and $z\geq 0$ and let $p$ and $q$ be real numbers.

- We have $\left(y^p\right)^q=y^{pq}$.
- We have $(yz)^p=y^pz^p$.
- We have $y^{p+q}=y^py^q$.
- We have $y^{p-q}=\dfrac{y^p}{y^q}$.
- If $y>1$ and $p<q$ then $y^p<y^q$.
- If $0<y<1$ and $p<q$ then $y^p>y^q$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:RealNumbers:ExpCalcReal`
:class: tudproof, dropdown
The first four properties use sequences, on which more information can be found in {numref}`Chapter:Sequences`. 

First we show if $r$ is a real number and $\{r_n\}_{n=1}^\infty$ is any sequence of rational numbers that converges to $r$ that the sequence $\left\{y^{r_n}\right\}_{n=1}^\infty$ converges to $y^r$. Suppose first that $r$ itself is rational. Let $\varepsilon>0$ be given. Note that $1+\frac{\varepsilon}{y^r}>1$, while $1-\frac{\varepsilon}{y^r}<1$, so we can choose $N$ sufficiently large that $\left(1-\frac{\varepsilon}{y^r}\right)^{N}<y<\left(1+\frac{\varepsilon}{y^r}\right)^{N}$. For this value of $N$ we have

$$
 y^{\frac{1}{N}}<\left(\left(1+\frac{\varepsilon}{y^r}\right)^{N}\right)^{\frac{1}{N}}=1+\frac{\varepsilon}{y^r}.
$$

Now we let $M$ be a natural number such that $|r_n-r|<\frac{1}{N}$ for all $n\geq M$. Then for $n\geq M$ we find if $r_n-r>0$ that

$$
 |y^{r_n}-y^r|=y^{r_n}-y^r=y^{r_n-r+r}-y^r=y^{r_n-r}y^r-y^r=\left(y^{r_n-r}-1\right)y^r<\left(y^{\frac{1}{N}}-1\right)y^r<\left(1+\frac{\varepsilon}{y^r}-1\right)y^r=\varepsilon,
$$

while if $r-r_n>0$ we find

$$
 |y^{r_n}-y^r|=y^{r}-y^{r_n}=y^r-y^{r_n-r+r}=y^r-y^{r_n-r}y^r=\left(1-y^{r_n-r}\right)y^r<\left(1-y^{\frac{1}{N}}\right)y^r<\left(1-\left(1-\frac{\varepsilon}{y^r}\right)\right)y^r=\varepsilon.
$$

We conclude that the sequence $\left\{y^{r_n}\right\}_{n=1}^\infty$$ converges to $y^r$. 

Now suppose that $r$ is irrational and let $\varepsilon>0$ be given. Let $l_n$ and $u_n$ be the number $r$ rounded down respectively up to $n$ decimals. By definition of $y^r$, we can choose $N$ sufficiently large that $y^{u_N}-y^{l_N}<\varepsilon$. Now since $r$ is irrational its decimal expansion does not terminate, so we must have $l_N<r<u_N$. Write $\delta=\text{min}\left\{u_N-r,l_N-r\right\}$, so $\delta$ is the smallest distance between $r$ and either $l_N$ or $u_N$. Then we can choose $M$ sufficiently large that $|r_n-r|<\frac{\delta}{2}$ for all $n\geq M$. For these values of $n$ we have $l_N<r_n<u_N$, so we find if $r_n>r$ that

$$
 \left|y^{r_n}-y^r\right|=y^{r_n}-y^r\leq y^{u_N}-y^r\leq y^{u_N}-y^{l_N}<\varepsilon,
$$

while if $r\leq r_n$ we find that

$$
 \left|y^{r_n}-y^r\right|=y^{r}-y^{r_n}\leq y^{u_N}-y^{r_n}\leq y^{u_N}-y^{l_N}<\varepsilon.
$$

As such, the sequence $\left\{y^{r_n}\right\}_{n=1}^\infty$$ converges to $y^r$. 

We now show that $(yz)^p=y^pz^p$. Let $\left\{p_n\right\}_{n=1}^\infty$ be a sequence of rational numbers that converges to $p$. Then the sequences $\left\{y^{p_n}\right\}_{n=1}^\infty$, $\left\{z^{p_n}\right\}_{n=1}^\infty$ and $\left\{(yz)^{p_n}\right\}_{n=1}^\infty$ converge to $y^p$, $z^p$ and $(yz)^p$ respectively. Since the term by term product of convergent sequences converges to the product of the limits, the sequence $\left\{y^{p_n}z^{p_n}\right\}_{n=1}^\infty$ converges to $y^pz^p$. Since $p_n$ is rational for all $n$, we have using {prf:ref}`Thm:RealNumbers:ExpCalcRat` that $(yz)^{p_n}=y^{p_n}z^{p_n}$. Hence, the seqeunce $\left\{(yz)^{p_n}\right\}_{n=1}^\infty$ converges to both $(yz)^p$ and to $y^pz^p$. As such, these limits are equal, so we have $(yz)^p=y^pz^p$.

We now show that $y^{p+q}=y^py^q$. Let $\left\{p_n\right\}_{n=1}^\infty$ and $\left\{q_n\right\}_{n=1}^\infty$ be sequences of rational numbers that converge to $p$ respectively $q$.Then the sequence $\left\{p_n+q_n\right\}_{n=1}^\infty$ is a sequence of rational numbers that converges to $p+q$. Hence, the sequence $\left\{y^{p_n+q_n}\right\}_{n=1}^\infty$ converges to $y^{p+q}$. On the other hand, we have $y^{p_n+q_n}=y^{p_n}y^{q_n}$ for all $n$ due to {prf:ref}`Thm:RealNumbers:ExpCalcRat`. The sequences $\left\{y^{p_n}\right\}_{n=1}^\infty$ and $\left\{y^{q_n}\right\}_{n=1}^\infty$ converge to $y^p$ respectively $y^q$. Since the term by term product of convergent sequences converges to the product of the limits, the sequence $\left\{y^{p_n}y^{q_n}\right\}_{n=1}^\infty$ converges to $y^py^q$. Hence, the seqeunce $\left\{y^{p_n}y^{q_n}\right\}_{n=1}^\infty$ converges to both $y^{p+q}$ and to $y^py^q$. As such, these limits are equal, so we have $y^{p+q}=y^py^q$.





Now we assume that $y>1$ and $p<q$. Write $u_n$ for the number $p$ rounded up to $n$ decimals and $l_n$ for the number $q$ rounded down to $n$ decimals. Since $p<q$ we must have $u_n<l_n$ for some $n$. For this value of $n$ we find using {prf:ref}`Thm:RealNumbers:ExpCalcRat` that

$$
 y^p\leq y^{u_n}<y^{l_n}<y^q,
$$

as desired. 

Finally, we assume that $0<y<1$ and $p<q$. Again, we write $u_n$ for the number $p$ rounded up to $n$ decimals and $l_n$ for the number $q$ rounded down to $n$ decimals. Since $p<q$ we must have $u_n<l_n$ for some $n$. For this value of $n$ we find using {prf:ref}`Thm:RealNumbers:ExpCalcRat` that

$$
 y^p\geq  y^{u_n}>y^{l_n}\geq y^q,
$$

as desired. 

Now we show that $\left(y^p\right)^q=y^{pq}$. For now, we assume that $y>1$ Let $\left\{p_n\right\}_{n=1}^\infty$ and $\left\{q_n\right\}_{n=1}^\infty$ be sequences of rational numbers that converge to $p$ respectively $q$. Then the sequence $\left\{p_nq_n\right\}_{n=1}^\infty$ is a sequence of rational numbers that converges to $pq$, so the sequence $\left\{y^{p_nq_n}\right\}_{n=1}^\infty$ converges to $y^{pq}$. For any value of $n$ we have, since $p_n$ and $q_n$ are rational numbers, that $y^{p_nq_n}=\left(y^{p_n}\right)^{q_n}$. We claim that the sequence $\left\{\left(y^{p_n}\right)^{q_n}\right\}_{n=1}^\infty$ converge to $\left(y^p\right)^q$. Since the sequence $\left\{\left(y^{p}\right)^{q_n}\right\}_{n=1}^\infty$ converge to $\left(y^p\right)^q$ we can let $N_1$ be such that for all $n\geq N_1$ we have $\left|\left(y^{p}\right)^{q_n}=\left(y^p\right)^q\right|<\frac{\varepsilon}{2}$. Moreover, the sequence $\left\{q_n\right\}_{n=1}^\infty$ converges, so it is bounded, say by a number $K>0$. Similarly, the sequence $\left\{\left(y^{p_n}\right)^{q_n}\right\}_{n=1}^\infty$ also converges, so it bounded, say by a number $L>0$. Since $\left\{p_n\right\}_{n=1}^\infty$ converges to $p$, we can let $N_2$ such that for all $n\geq N_2$ we have $y^{p-p_n}<\left(\frac{1+\frac{\varepsilon}{2}}{L}\right)^{\frac{1}{K}}$ (DIT MOET BETER GEFORMULEERD). Then we let $N=\text{max}\left\{N_1,N_2\right\}$, i.e. $N$ is the largest of the two numbers $N_1$ and $N_2$. Then using the properties we already proved, we have for $n\geq N$ if $p-p_n>0$ that

\begin{align*}
 \left(y^p\right)^q-\left(y^{p_n}\right)^{q_n}=\left(y^p\right)^q-\left(y^{p}\right)^{q_n}+\left(y^{p}\right)^{q_n}-\left(y^{p_n}\right)^{q_n}\\
 &<\frac{\varepsilon}{2}+\left(y^{p}\right)^{q_n}-\left(y^{p_n}\right)^{q_n}\\
 &=\frac{\varepsilon}{2}+\left(y^{p-p_n+p_n}\right)^{q_n}-\left(y^{p_n}\right)^{q_n}\\
 &=\frac{\varepsilon}{2}+\left(y^{p-p_n}y^{p_n}\right)^{q_n}-\left(y^{p_n}\right)^{q_n}\\
 &=\frac{\varepsilon}{2}+\left(y^{p-p_n}\right)^{q_n}\left(y^{p_n}\right)^{q_n}-\left(y^{p_n}\right)^{q_n}\\
 &=\frac{\varepsilon}{2}+\left(\left(y^{p-p_n}\right)^{q_n}-1\right)\left(y^{p_n}\right)^{q_n}\\
 &\leq\frac{\varepsilon}{2}+\left(\left(y^{p-p_n}\right)^{K}-1\right)\left(y^{p_n}\right)^{q_n}\\
 &\leq\frac{\varepsilon}{2}+\left(\left(\frac{1+\frac{\varepsilon}{2}}{L}\right)^{\frac{1}{K}}^{K}-1\right)\left(y^{p_n}\right)^{q_n}\\
 &=\frac{\varepsilon}{2}+\frac{\epsilon}{2L}\left(y^{p_n}\right)^{q_n}\\
 &\leq \frac{\varepsilon}{2}+\frac{\epsilon}{2L}L\\
 &=\varepsilon
\end{align*}

while if $p_n-p>0$ we get 
DIT STUK MOET NOG AF EN OPGESCHOOND.
:::