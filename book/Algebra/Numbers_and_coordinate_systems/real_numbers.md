
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

::::::{prf:definition} 
:label: Def:RealNumbers:Powers2
If $y\geq 0$ and $n\geq 1$ is an even natural number, the unique positive solution of the equation $x^n=y$ is called the  $\mathbf{n}$**th square root** of $y$ and is denoted by $\sqrt[n]{y}=y^{\frac{1}{n}}$. If $n=2$, we call this number the **square root** of $y$ and write $\sqrt{y}$ instead of $\sqrt[2]{y}$. In addition, if $y$ is a real number and $n\geq 1$ is an odd natural number, then the unique solution of the equation $x^n=y$ is called the $\mathbf{n}$**th square root** of $y$ and is denoted by $\sqrt[n]{y}=y^{\frac{1}{n}}$.

::::::

We can now consistently define what we mean by $y^{\frac{p}{q}}$ for integers $p\geq 1$ and $q>0$.


::::::{prf:definition} 
:label: Def:RealNumbers:Powers3
Let $y\geq 0$ and $r\neq 0$ be a rational number. Write $r=\frac{p}{q}$ with $p$ and $q$ integers and $q>0$. Then we define $x^{\frac{p}{q}}=\sqrt[q]{x^p}=\left(\sqrt[q]{x}\right)^p$.

Moreover if $y<0$ and $q$ is odd we define $x^{\frac{p}{p}}=\sqrt[q]{x^p}=\left(\sqrt[q]{x}\right)^p$.
::::::

::::::{warning} 
:name: Warning:Realnumbers:Powersofnegativenumbers

We have seen how to define things like $(-1)^{2}$, $(-1)^{-4}$ and $(-1)^{\frac{5}{3}}$. Now, what do we mean by $(-1)^{\frac{1}{2}}$? We will see below that for $x\geq 0$ and real numbers $a$ and $b$ we always have the identity $\left(x^a\right)^b=x^{ab}$. Unfortunately, it is impossible to define $(-1)^{\frac{1}{2}}$ in such a way that it is consistent with this rule. Indeed, if we could define it, we would find that

$$
 -1=(-1)^1=(-1)^{2\cdot{\frac{1}{2}}}=\left((-1)^2\right)^{\frac{1}{2}}=1^{\frac{1}{2}}=1
$$

which is not the case. As such, we will not try to define those powers of negative numbers that we have not already defined.
::::::

Nog bewijs van die ene stelling doen? Anders verwijzing. Hierna nietrationale machten en e-machten.