(Section:LimitPoint)=

# Limits at a point

Often, when a point is not in the domain of a function, this is because point cannot be entered into the formula describing the function, for insance, because that would involve dividing by $0$, taking square roots or logarithms of negative numbers, and so on. However, in some cases, the function values of the point still approach a certain value as the values of $x$ approach the problematic point. This is illustrated in the following example.

::::::{prf:example}
:label: Ex:LimitatPoint:FirstLimitEx
Consider the functions $f(x)=\dfrac{x-1}{x^2-1}$ and $g(x)=\dfrac{x}{x^2-2x+1}$. Both functions are undefined at $x=1$, as the denominators $x^2-1$ and $x^2-2x+1$ are zero there. However, the functions $f$ and $g$ behave very differently for values of $x$ close to $1$, as can be seen from the graph of the two functions below.

Hier 1 plaatje met grafieken van zowel f als g ingezoomd rond x=1.

Let us try to figure out what is going on here. For the function $g$, the function values seem to blow up near $x=1$, while for the function $f$ nothing bad seems to happen at all. We can make this a bit more explicit by evaluting the functions $f$ and $g$ at values of $x$ close to $1$.

Hier 2 tabellen met functiewaarden $f$ en $g$ voor $x=0.9,0.99,0.999,0.9999$ en voor $1.1,1.01,1.001,1.0001$.

As can be seen from the table, the function values of $f$ seem to approach the value $\frac{1}{2}$, while those of $g$ grow arbitrarily large. So is there some way we can show that the function $f$ indeed approaches this value? Well, note that for $x\neq 1$ we can write

$$
 f(x)=\frac{x-1}{x^2-1}=\frac{x-1}{(x-1)(x+1)}=\frac{1}{x+1}
$$

So for all $x\neq 1$, the function value $f(x)$ is equal to the function value $h(x)=\dfrac{1}{x+1}$. Moreover, for the function $h$, the point $x=1$ is in the domain and we can evaluate $h(1)=\frac{1}{1+1}=\frac{1}{2}$. Since the function $h$ does not make any jumps at $x=1$ and $f$ and $h$ coincide outside of $x=1$, this means that the function values $f(x)$ indeed must approach the value $\frac{1}{2}$ as $x$ approaches $1$. We say that the **limit of the function $f$ as $x$ approaches $1$ is equal to $\frac{1}{2}$** and denote this by writing $\lim\limits_{x\rightarrow 1}f(x)=\frac{1}{2}$. 

On the other hand, the function values of the function $g$ do not approach a real number as $x$ approaches $1$, so we will say that the **limit of the function $g$ as $x$ approaches $1$ does not exist**.

::::::

(Subsec:LimitIntuitive)=

## Intuitive definition of limits

We will postpone the precise definition of a limit to {numref}`Subsec:Limitsformaldef`. Instead, for now, we will use the following more intuitive definition of a limit.

::::::{prf:definition}
:label: Def:LimitatPoint:Intuitivelimit

Let $f$ be a function that is defined for values of $x$ close to $x=a$ (except possibly at $x=a$ itself). We say that the **limit** of $f$ as $x$ approaches $a$ is equal to $L$, and we write $\lim\limits_{x\rightarrow a}f(x)=L$, if the function values $f(x)$ approach $L$ as $x$ approaches $a$ (but $x$ not equal to $a$). If no such real number $L$ exists, we say that the limit of the function $f$ as $x$ approaches $a$ does not exist.
::::::

Since we only work with an intuitive definition, we will also postpone all proofs in this chapter to {numref}`Subsec:Limitsformaldef`.

When trying to evaluate a limit of the form $\lim\limits_{x\rightarrow a}f(x)$, it is sometimes helpful to consider values of $x$ smaller than $a$, and values of $x$ larger than $a$ separately. For this we use **one-sided limits**.

::::::{prf:definition}
:label: Def:LimitatPoint:Intuitiveleftrightlimit

Let $f$ be a function that is defined for values of $x<a$ close to $x=a$. We say that the **left limit** of $f$ as $x$ approaches $a$ is equal to $L$, and we write $\lim\limits_{x\rightarrow a^-}f(x)=L$, if the function values $f(x)$ approach $L$ as $x$ approaches $a$ from the left (but $x$ not equal to $a$). If no such real number $L$ exists, we say that the left limit of the function $f$ as $x$ approaches $a$ does not exist.

Similarly, if $f$ is defined for values of $x>a$ close to $a$, we say that the **right limit** of $f$ as $x$ approaches $a$ is equal to $L$, and we write $\lim\limits_{x\rightarrow a^+}f(x)=L$, if the function values $f(x)$ approach $L$ as $x$ approaches $a$ from the right (but $x$ not equal to $a$). If no such real number $L$ exists, we say that the right limit of the function $f$ as $x$ approaches $a$ does not exist.
::::::

For the left and right limits, several different notations are used throughout the literature. Here, we will stick to the notations used above, but, for completeness, we will list the alternative notations here as well.

::::::{prf:notation} Left and right limits
:label: Notation:LimitatPoint:Leftrightlimit

$$
 \lim_{x\rightarrow a^-}f(x)=\lim_{x\uparrow a}f(x)=f(a^-)
$$
$$
 \lim_{x\rightarrow a^+}f(x)=\lim_{x\downarrow a}f(x)=f(a^+)
$$
::::::

If $\lim\limits_{x\rightarrow a}f(x)=L$, then the function values $f(x)$ approach $L$ no matter from which direction (left or right) the values of $x$ approach $a$. That means that, in this case, the left and right limits of $f$ as $x$ approaches $a$ must both be equal to $L$ as well. Reversely, if one (or both) of the left and right limits does not exist, the regular limit $\lim\limits_{x\rightarrow a}f(x)$ cannot exist as well, since, apparently, the function values do not approach a single value when $x$ approaches $a$ in at least one direction. In addition, if the left and right limits at a point both exist, but are unequal, say $\lim\limits_{x\rightarrow a^-}f(x)=L$ and $\lim\limits_{x\rightarrow a^+}f(x)=M$ with $L\neq M$, since the function approaches two different values as $x$ approaches $a$. With that, we obtain the following theorem.

::::::{prf:theorem}
:label: Theorem:LimitatPoint:Leftrightequal
We have $\lim\limits_{x\rightarrow a}f(x)=L$ precisely when both $\lim\limits_{x\rightarrow a^-}f(x)=L$ and $\lim\limits_{x\rightarrow a^+}f(x)=L$, i.e. the regular limit at a point exists precisely when 
the left and right limits at that point both exist and are equal.
::::::

So how do you evaluate limits (regular, left or right)? There are various techniques, which we will discuss throughout this chapter. In several of these, we evaluate the limit by rewriting or simplifying the function at hand. Indeed, in {prf:ref}`Ex:LimitatPoint:FirstLimitEx` we evaluated the limit $\lim\limits_{x\rightarrow 1}f(x)$ by finding a function $h$ which is equal to $f$ everywhere except at $x=1$ and for which $1$ was in the domain of $h$. The following two results show that this idea works more generally.
::::::{prf:theorem}
:label: Theorem:LimitatPoint:Rewritingworks
If $f(x)=g(x)$ whenever $x\neq a$, then $\lim\limits_{x\rightarrow a}f(x)=\lim_{x\rightarrow a}g(x)$, provided the limits exist, or $\lim\limits_{x\rightarrow a}f(x)$ and $\lim_{x\rightarrow a}g(x)$ both do not exist.
::::::


::::::{prf:theorem} Direct substitution
:label: Theorem:LimitatPoint:Directsub
If $f$ is a polynomial, rational function, power of $x$, (inverse) trigonometric function, exponential function or logarithmic function and $a$ is in the domain of $f$, then $\lim\limits_{x\rightarrow a}f(x)=f(a)$.
::::::

::::::{prf:example}
:label: Ex:LimitatPoint:LimitLeftRight
Consider the function $f(x)=\dfrac{|x|}{x}$, which is defined for all values of $x\neq 0$. We want to try to evaluate $\lim\limits_{x\rightarrow 0}f(x)$. For this, we evaluate the left and right limits. For $x<0$ we have $|x|=-x$ (recall that the absolute value of a negative number $x$ is the positive number $-x$), so we can simplify the function $f$ to 

$$
 f(x)=\frac{|x|}{x}=\frac{-x}{x}=-1\qquad\text{if }x<0.
$$

The function $-1$ is defined in $0$, so we can use this to evaluate the left limit

$$
 \lim_{x\rightarrow 0^-}f(x)=\lim_{x\rightarrow 0^-}-1=-1.
$$

Similarly, we have $|x|=x$ for $x>0$, so we can simplify

$$
 f(x)=\frac{|x|}{x}=\frac{x}{x}=1\qquad \text{if }x>0
$$

and use this to evaluate the right limit

$$
 \lim_{x\rightarrow 0^+}f(x)=\lim_{x\rightarrow 0^+}1=1.
$$

We conclude that the left and right limit of $f$ as $x$ approaches $0$ both exist, but are unequal. Using {prf:ref}`Theorem:LimitatPoint:Leftrightequal` we conclude that $\lim\limits_{x\rightarrow 0}\frac{|x|}{x}$ does not exist.

Hier nog plaatje van deze functie rond x=0, met als onderschrift een samenvatting van bovenstaande.

::::::

Left and right limits are also convenient when evaluating limits of composite functions, as can be seen from the following example.

::::::{prf:example}
:label: Ex:LimitatPoint:LimitLeftRightComposite
Consider the composite function $f(x)=\left\{\begin{array}{ll}x-1,&\text{ if }x<2\\ 4,&\text{ if }x=2,\\ 3-x,&\text{ if }x>2\end{array}\right.$ We aim to evaluate $\lim\limits_{x\rightarrow 2}f(x)$ and we will do so by evaluating the left and right limits. For $x<2$ the function is given by $f(x)=x-1$, so we can directly evaluate the left limit

$$
 \lim_{x\rightarrow 2^-}f(x)=\lim_{x\rightarrow 2^-}x-1=2-1=1
$$

Similarly, for $x>2$ the function is given by $f(x)=3-x$, so we can directly evaluate the left limit

$$
 \lim_{x\rightarrow 2^+}f(x)=\lim_{x\rightarrow 2^+}3-x=3-1=2
$$

 Using {prf:ref}`Theorem:LimitatPoint:Leftrightequal` we conclude that $\lim\limits_{x\rightarrow 0}f(x)=2$, since both the left and right limit at that point are equal to $2$.

Hier nog plaatje van deze functie rond x=2, met als onderschrift een samenvatting van bovenstaande.

::::::

Note that in {prf:ref}`Ex:LimitatPoint:LimitLeftRightComposite` the function $f$ was defined in the point $x=2$, but that did not influence the value of the limit at all; in fact, the limit $\lim\limits_{x\rightarrow 2}f(x)$ is unequal to $f(2)$. This is because, when evaluating a limit, we are only interested in the behaviour of the function values $f(x)$ for $x$ close to, but *unequal to* $a$. We can summarize this observation as follows.

::::::{prf:remark}
:label: RemarkLimitatPoint:Valueirrelevant
If $f(a)$ is defined, then its value is *irrelevant* for the existence and value of $\lim\limits_{x\rightarrow a} f(x)$.
::::::

So far we have seen two examples where the limit did not exist. In {prf:ref}`Ex:LimitatPoint:FirstLimitEx` the limit $\lim\limits_{x\rightarrow 1}g(x)$ did not exist because the function values of $g$ blow up as $x$ approaches $1$. We will cover this case more extensively in {numref}`Subsec:Limitsvertical`. In addition, in {prf:ref}`Ex:LimitatPoint:LimitLeftRight` we saw that the limit $\lim\limits_{x\rightarrow 0}f(x)$ because the left and right limit were unequal. There are many other ways in which a limit can fail to exist. We will discuss two remaining commonly occuring ways in the remainder of this section.

::::::{prf:example}
:label: Ex:LimitatPoint:Limitoutsidedomain
Consider the function $f(x)=\sqrt{x-3}$ and suppose we want to evaluate the limit $\lim\limits_{x\rightarrow 2}f(x)$. For this, we would like to know how the function values $f(x)$ behave as $x$ approaches $2$. However, the domain of this function is the interval $[3,\infty)$, so the function is undefined for $x<3$. As such, it is impossible to study the behaviour or the function values $f(x)$ for these values of $x$ and this implies that the limit $\lim\limits_{x\rightarrow 2}f(x)$ does not exist. 

Hier nog plaatje van deze functie, met als onderschrift een samenvatting van bovenstaande.

::::::

::::::{prf:example}
:label: Ex:LimitatPoint:Limitsinoneoverx
Consider the function $f(x)=\sin\left(\frac{1}{x}\right)$ and suppose we want to evaluate the limit $\lim\limits_{x\rightarrow 0}f(x)$. So what happens with the function values $f(x)$ if $x$ approaches $0$, say from the right? In that case, $\frac{1}{x}$ will start to blow up, which means that as $x$ approaches $0$ the function values $\sin\left(\frac{1}{x}\right)$ will osciallate between $-1$ and $1$ with increasing frequency. As such, these function values do not approach a single value, as they will continue to osciallate between $-1$ and $1$, which means that the right limit does not exist. With a similar reasoning, the left limit does not exist as well. We conclude that the limit $\lim\limits_{x\rightarrow 0}\sin\left(\frac{1}{x}\right)$ does not exist.

Hier nog plaatje van deze functie, met als onderschrift een samenvatting van bovenstaande.

::::::

(Subsec:Limitsrules)=

## Rules of calculation

Now that we know what a limit is and how we can determine whether it it exists, let us now focus on evuatling limits. For this, we will see that limits behave rather nicely in combination with algebraic operations like addition and multiplication.

::::::{prf:theorem} Basic rules of calculation for limits
:label: Theorem:LimitatPoint:Basiccomputationrules
Suppose that $\lim\limits_{x\rightarrow a}f(x)=L$ and $\lim\limits_{x\rightarrow a}g(x)=M$. Also let $c$ be a real number. Then we have

- $\lim\limits_{x\rightarrow a}cf(x)=cL$ (scalar multiple rule)
- $\lim\limits_{x\rightarrow a}(f(x)+g(x)) = L+M$ (sum rule)
- $\lim\limits_{x\rightarrow a}f(x)g(x)=LM$ (product rule)
- $\lim\limits_{x\rightarrow a}\frac{f(x)}{g(x)}=\frac{L}{M}$ if $M\neq 0$ (quotient rule)

::::::

::::::{prf:remark}
:label: Remark:LimitatPoint:Productquotientrule
The product and quotient rules from {prf:ref}`Theorem:LimitatPoint:Basiccomputationrules` should not be confused with the product and quotient rules for differentiation, which will be covered in {numref}`Section:DiffProdQuot`

::::::

Intuitively, these computation rules make sense: if the function values $f(x)$ approach $L$ and the function values $g(x)$ approach $M$, both as $x$ approaches $a$, then $f(x)+g(x)$ will approach $L+M$. Still, showing that these rules hold using the formal definition of a limit can be tricky, see {numref}`Subsec:Limitsformaldef`.

Now consider a limit of the form $\lim\limits_{x\rightarrow a}\frac{p(x)}{q(x)}$ where $p$ and $q$ are polynomials that have $p(a)=q(a)=0$. We cannot evaluate the limit directly since we get something of the form "$\frac{0}{0}$". Recall that we encountered this situation in {prf:ref}`Ex:LimitatPoint:FirstLimitEx` when evaluating the limit $\lim\limits_{x\rightarrow 1}\frac{x-1}{x^2-1}$. There we evaluated the limit by factoring the denominator. This works in general. Recall from {prf:ref}`Thm:ComplexNumbers:fundamental` (Willem: handigste stelling om naar the verwijzen?) that $a$ being a root of the polynomials $p$ and $q$ means that we can take out the factor $x-a$ from both of them, i.e. we can write $p(x)=(x-a)r(x)$ and $q(x)=(x-a)s(x)$ for some polynomials $r$ and $s$, which are 1 degree lower than $p$ and $q$ respectively. As such, we can now evaluate the limit by writing

$$
 \lim\limits_{x\rightarrow a}\frac{p(x)}{q(x)}=\lim\limits_{x\rightarrow a}\frac{(x-a)r(x)}{(x-a)s(x)}=\lim\limits_{x\rightarrow a}\frac{r(x)}{s(x)}
$$


The limit $\lim\limits_{x\rightarrow a}\frac{r(x)}{s(x)}$ can then be either evaluated directly, or shown to not exist (i.e. when $r(a)\neq 0$ and $s(a)=0$), or, in case both $r(a)=0$ and $s(a)=0$, another factor $x-a$ can be factored from both of them. This technique is known as **cancelling the common factor**.

::::::{prf:example}
:label: Ex:LimitatPoint:Cancellingcommonfactor
Suppose we want to evaluate $\lim\limits_{x\rightarrow 1}\dfrac{x^3-3x^2+3x-1}{x^3-3x^2+5x-2}$. Notice that both the numerator and the denominator, which are both polynomials, are $0$ at $x=1$, so both polynomials contain a factor $x-1$. Using polynomial long division (see {prf:ref}`Ex:LimitatPoint:FirstLimitEx`), we find that $x^3-3x^2+3x-1=(x-1)(x^2-2x+1)$ and $x^3-3x^2+5x-2=(x-1)(x^2-3x+2)$, so we can compute

$$
 \lim\limits_{x\rightarrow 1}\frac{x^3-3x^2+3x-1}{x^3-3x^2+5x-2}=\lim\limits_{x\rightarrow 1}\frac{(x-1)(x^2-2x+1)}{(x-1)(x^2-3x+2)}=\lim\limits_{x\rightarrow 1}\frac{x^2-2x+1}{x^2-3x+2}
$$

Note that the new numerator and denominator are both $0$ at $x=1$ again, so we have to take out yet another factor $x-1$ from both of them. Luckily, these a quadratic polynomals, so factoring these is usually easier than for polynomials of higher degrees. In this case, we find

$$
 \lim\limits_{x\rightarrow 1}\frac{x^3-3x^2+3x-1}{x^3-3x^2+5x-2}=\lim\limits_{x\rightarrow 1}\frac{x^2-2x+1}{x^2-3x+2}=\lim\limits_{x\rightarrow 1}\frac{(x-1)^2}{(x-1)(x-2)}=\lim\limits_{x\rightarrow 1}\frac{x-1}{x-2}
$$

The remaining limit can be evaluated directly and we find

$$
 \lim\limits_{x\rightarrow 1}\frac{x^3-3x^2+3x-1}{x^3-3x^2+5x-2}=\lim\limits_{x\rightarrow 1}\frac{x-1}{x-2}=\frac{1-1}{1-2}=0
$$
::::::

(Subsec:Limitsvertical)=

## Vertical asymptotes

(Subsec:Limitsformaldef)=

## Precise definition of limits

In this section we cover

- Intuitive definition (including one-sided limits)
- Basic rules of calculation
- Vertical asymptotes
- Cancelling common factors, square root trick, squeeze theorem
- Formal definition