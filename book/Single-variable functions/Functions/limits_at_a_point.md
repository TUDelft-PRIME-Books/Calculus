(Section:LimitPoint)=

# Limits at a point

Often, when a point is not in the domain of a function, this is because this point cannot be entered into the formula describing the function, for insance, because that would involve dividing by $0$, taking square roots or logarithms of negative numbers, and so on. However, in some cases, the function values near the point still approach a certain value as the values of $x$ approach the problematic point. This is illustrated in the following example.

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

::::::{prf:definition} Intuitive definition of a limit
:label: Def:LimitatPoint:Intuitivelimit

Let $f$ be a function that is defined for values of $x$ close to $x=a$ (except possibly at $x=a$ itself). We say that the **limit** of $f$ as $x$ approaches $a$ is equal to $L$, and we write $\lim\limits_{x\rightarrow a}f(x)=L$, if the function values $f(x)$ approach $L$ as $x$ approaches $a$ (but $x$ not equal to $a$). If no such real number $L$ exists, we say that the limit of the function $f$ as $x$ approaches $a$ does not exist.
::::::

Since we only work with an intuitive definition, we will also postpone all proofs in this chapter to {numref}`Subsec:Limitsformaldef`.

When trying to evaluate a limit of the form $\lim\limits_{x\rightarrow a}f(x)$, it is sometimes helpful to consider values of $x$ smaller than $a$, and values of $x$ larger than $a$ separately. For this we use **one-sided limits**.

::::::{prf:definition} Intuitive definition of left and right limits
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

If $\lim\limits_{x\rightarrow a}f(x)=L$, then the function values $f(x)$ approach $L$ no matter from which direction (left or right) the values of $x$ approach $a$. That means that, in this case, the left and right limits of $f$ as $x$ approaches $a$ must both be equal to $L$ as well. Reversely, if one (or both) of the left and right limits does not exist, the regular limit $\lim\limits_{x\rightarrow a}f(x)$ cannot exist as well, since, apparently, the function values do not approach a single value when $x$ approaches $a$ in at least one direction. In addition, if the left and right limits at a point both exist, but are unequal, say $\lim\limits_{x\rightarrow a^-}f(x)=L$ and $\lim\limits_{x\rightarrow a^+}f(x)=M$ with $L\neq M$, the regular limit $\lim\limits_{x\rightarrow a}f(x)$ cannot exist as the function approaches two different values as $x$ approaches $a$. With that, we obtain the following theorem.

::::::{prf:theorem}
:label: Theorem:LimitatPoint:Leftrightequal
We have $\lim\limits_{x\rightarrow a}f(x)=L$ precisely when both $\lim\limits_{x\rightarrow a^-}f(x)=L$ and $\lim\limits_{x\rightarrow a^+}f(x)=L$, i.e. the regular limit at a point exists precisely when 
the left and right limits at that point both exist and are equal.
::::::

So how do you evaluate limits (regular, left or right)? There are various techniques, which we will discuss throughout this chapter. In several of these, we evaluate the limit by rewriting or simplifying the function at hand. Indeed, in {prf:ref}`Ex:LimitatPoint:FirstLimitEx` we evaluated the limit $\lim\limits_{x\rightarrow 1}f(x)$ by finding a function $h$ which is equal to $f$ everywhere except at $x=1$ and for which $1$ was in the domain of $h$. The following two results show that this idea works more generally.
::::::{prf:theorem}
:label: Theorem:LimitatPoint:Rewritingworks
If $f(x)=g(x)$ whenever $x\neq a$, then $\lim\limits_{x\rightarrow a}f(x)=\lim\limits_{x\rightarrow a}g(x)$, provided the limits exist, or $\lim\limits_{x\rightarrow a}f(x)$ and $\lim\limits_{x\rightarrow a}g(x)$ both do not exist.
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
Consider the composite function $f(x)=\left\{\begin{array}{ll}x-1,&\text{ if }x<2,\\ 4,&\text{ if }x=2,\\ 3-x,&\text{ if }x>2.\end{array}\right.$ 
We aim to evaluate $\lim\limits_{x\rightarrow 2}f(x)$ and we will do so by evaluating the left and right limits. For $x<2$ the function is given by $f(x)=x-1$, so we can directly evaluate the left limit

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

So far we have seen two examples where the limit did not exist. In {prf:ref}`Ex:LimitatPoint:FirstLimitEx` the limit $\lim\limits_{x\rightarrow 1}g(x)$ did not exist because the function values of $g$ blow up as $x$ approaches $1$. We will cover this case more extensively in {numref}`Subsec:Limitsvertical`. In addition, in {prf:ref}`Ex:LimitatPoint:LimitLeftRight` we saw that the limit $\lim\limits_{x\rightarrow 0}f(x)$ did not exist because the left and right limit were unequal. There are many other ways in which a limit can fail to exist. We will discuss two remaining commonly occuring ways in the remainder of this section.

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

## Evaluating limits

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

In addition, we obtain the following comparison result for limits.

::::::{prf:theorem} Comparison of limits
:label: Theorem:LimitatPoint:Comparison
Suppose that $\lim\limits_{x\rightarrow a}f(x)=L$ and $\lim\limits_{x\rightarrow a}g(x)=M$. Also suppose that $f(x)\leq g(x)$ for all $x$ close to $a$ (except possibly at $x=a$). Then $L\leq M$.

::::::

Again, this result makes sense intuitively: if the function values $f(x)$ are always below $g(x)$, how could the limit $L$ suddenly become larger than $M$? However, in the situation of {prf:ref}`Theorem:LimitatPoint:Comparison` you might expect if we knew that $f(x)<g(x)$ for all $x$ close to $a$ that it should follow that $L<M$. This is not true, in general, as can be seen from the following example.

::::::{prf:example} 
:label: Ex:LimitatPoint:Comparison
Consider the function $f(x)=-x^2$ and $g(x)=x^2$. Then $f(x)<g(x)$ for all $x\neq 0$. So by {prf:ref}`Theorem:LimitatPoint:Comparison` we can immediately conclude that $\lim\limits_{x\rightarrow 0}f(x)\leq \lim\limits_{x\rightarrow 0}g(x)$. However, we can quickly compute that $\lim\limits_{x\rightarrow 0}f(x)= \lim\limits_{x\rightarrow 0}g(x)=0$, so the limits are, in fact, equal even though the functions are never equal outside of $x=0$.
::::::

We continue the path we set foot on in {prf:ref}`Theorem:LimitatPoint:Comparison`, but now we consider the situation where we have $3$ functions, which satisfy $f(x)\leq g(x)\leq h(x)$ for all $x$ close to $a$, so the function $g$ is squeezed inbetween the functions $f$ and $h$. Suppose that, in addition, we know that $\lim\limits_{x\rightarrow a}f(x)$ and $\lim\limits_{x\rightarrow a}h(x)$ are **equal**, say they are both $L$. What does that tell us about $\lim\limits_{x\rightarrow a}g(x)$? Well, since $f(x)\leq g(x)$ and $\lim\limits_{x\rightarrow a}f(x)=L$, we know that $\lim\limits_{x\rightarrow a}g(x)$, if it exists, should be **at least** equal to $L$. On the other hand, since $g(x)\leq h(x)$ and $\lim\limits_{x\rightarrow a}h(x)=L$, we find that $\lim\limits_{x\rightarrow a}g(x)$, again if it exists, should be **at most** equal to $L$. We conclude that the limit $\lim\limits_{x\rightarrow a}g(x)$ is forced to be equal to $L$, provided the limit exists. The following theorem, known as the **squeeze theorem**, or alternatively the **sandwich theorem** or **pinching theorem**, shows that we do not need to worry about the existence of the limit $\lim\limits_{x\rightarrow a}g(x)$.

::::::{prf:theorem} Squeeze theorem for limits
:label: Theorem:LimitatPoint:Squeezetheorem
Suppose that $\lim\limits_{x\rightarrow a}f(x)=\lim\limits_{x\rightarrow a}h(x)=L$. Also suppose that $f(x)\leq g(x)\leq h(x)$ for all $x$ close to $a$ (except possibly at $x=a$). Then $\lim\limits_{x\rightarrow a}g(x)$ also exists and $\lim\limits_{x\rightarrow a}g(x)=L$.

::::::

::::::{prf:example} Squeeze theorem
:label: Ex:LimitatPoint:Squeeze theorem
Consider the function $g(x)=x^2\sin\left(\frac{1}{x}\right)$ and suppose we want to evaluate $\lim\limits_{x\rightarrow 0}g(x)$. In example {prf:ref}`Ex:LimitatPoint:Limitsinoneoverx` we saw that $\lim\limits_{x\rightarrow 0}\sin\left(\frac{1}{x}\right)$ does not exist, so we cannot use the product rule to evaluate this limit. We can, however, use the squeeze theorem. For this we note that the sine, no matter how ugly its input is, always takes values between $-1$ and $1$. As such, we conclude that $-x^2=x^2\cdot(-1)\leq x^2\sin\left(\frac{1}{x}\right)\leq x^2\cdot 1=x^2$ for all $x\neq 0$. So we define the functions $f(x)=-x^2$ and $h(x)=x^2$ and note that $f(x)\leq g(x)\leq h(x)$, so $g$ is squeezed in between the functions $f$ and $h$. Moreover, we note that $\lim\limits_{x\rightarrow 0}-x^2=\lim\limits_{x\rightarrow 0}x^2=0$. By the squeeze theorem, we obtain that $\lim\limits_{x\rightarrow 0}x^2\sin\left(\frac{1}{x}\right)=0$ as well.

Hier een plaatje dat bovenstaand voorbeeld illustreert, dus met de drie functies f, g en h rond 0.
::::::

Now consider a limit of the form $\lim\limits_{x\rightarrow a}\frac{p(x)}{q(x)}$ where $p$ and $q$ are polynomials that have $p(a)=q(a)=0$. We cannot evaluate the limit directly since we get something of the form "$\frac{0}{0}$". Recall that we encountered this situation in {prf:ref}`Ex:LimitatPoint:FirstLimitEx` when evaluating the limit $\lim\limits_{x\rightarrow 1}\frac{x-1}{x^2-1}$. There we evaluated the limit by factoring the denominator. This works in general. Recall from {prf:ref}`Thm:ComplexNumbers:fundamental` (Willem: handigste stelling om naar the verwijzen?) that $a$ being a root of the polynomials $p$ and $q$ means that we can take out the factor $x-a$ from both of them, i.e. we can write $p(x)=(x-a)r(x)$ and $q(x)=(x-a)s(x)$ for some polynomials $r$ and $s$, which are 1 degree lower than $p$ and $q$ respectively. As such, we can now evaluate the limit by writing

$$
 \lim\limits_{x\rightarrow a}\frac{p(x)}{q(x)}=\lim\limits_{x\rightarrow a}\frac{(x-a)r(x)}{(x-a)s(x)}=\lim\limits_{x\rightarrow a}\frac{r(x)}{s(x)}
$$


The limit $\lim\limits_{x\rightarrow a}\frac{r(x)}{s(x)}$ can then be either evaluated directly, or shown to not exist (i.e. when $r(a)\neq 0$ and $s(a)=0$), or, in case both $r(a)=0$ and $s(a)=0$, another factor $x-a$ can be factored from both of them. This technique is known as **cancelling the common factor**.

::::::{prf:example} Cancelling the common factor
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

Now consider a limit of the form $\lim\limits_{x\rightarrow a}\frac{f(x)}{g(x)}$ where $f(a)=g(a)=0$ and either $f$ or $g$ is of the form $p(x)+q(x)\sqrt{r(x)}$ for some functions $p$, $q$ and $r$. Then it can often help to multiply both the numerator and the denominator by the 'conjugate square root' $p(x)-q(x)\sqrt{r(x)}$. This technique is also known as the **square root trick**. The reason that this trick works, is that the product $(p(x)+q(x)\sqrt{r(x)})(p(x)-q(x)\sqrt{r(x)})$ simplifies into $p(x)^2-q(x)^2r(x)$, which no longer involves a square root. If $p$, $q$ and $r$ are polynomials, the previously discussed technique of cancelling the common factor can subsequently be used to evaluate the limit.

::::::{prf:example} Square root trick
:label: Ex:LimitatPoint:Squareroottrick.
Suppose we want to evaluate $\lim\limits_{x\rightarrow 0}\dfrac{2-\sqrt{x+4}}{x}$. Notice that both the numerator and the denominator are $0$ at $x=0$, and that the numerator is of the form described above. Using the square root trick we can evaluate the limit by rewriting

$$
 \lim\limits_{x\rightarrow 0}\dfrac{2-\sqrt{x+4}}{x}=\lim\limits_{x\rightarrow 0}\dfrac{2-\sqrt{x+4}}{x}\dfrac{2+\sqrt{x+4}}{2+\sqrt{x+4}}=\lim\limits_{x\rightarrow 0}\dfrac{4-(x+4)}{2x+x\sqrt{x+4}}=\lim\limits_{x\rightarrow 0}\frac{-x}{x(2+\sqrt{x+4})}
$$

Note that the new numerator and denominator both contain the common factor $x$, so we can cancel out this factor and evaluate

$$
 \lim\limits_{x\rightarrow 0}\dfrac{2-\sqrt{x+4}}{x}=\lim\limits_{x\rightarrow 0}\frac{-x}{x(2+\sqrt{x+4})}=\lim\limits_{x\rightarrow 0}\frac{-1}{2+\sqrt{x+4}}
$$

The remaining limit can be evaluated directly and we find

$$
 \lim\limits_{x\rightarrow 0}\dfrac{2-\sqrt{x+4}}{x}=\lim\limits_{x\rightarrow 0}\frac{-1}{2+\sqrt{4+x}}=-\frac{1}{4}
$$
::::::

(Subsec:Limitsvertical)=

## Vertical asymptotes

In {prf:ref}`Ex:LimitatPoint:FirstLimitEx` we saw that sometimes a limit of the form $\lim\limits_{x\rightarrow a}g(x)$ does not exist, because the function values $g(x)$ blow up near $x=a$. This is actually a very common reason for limits not existing and it also tells a lot about the qualitative behaviour of the function near $x=a$. As such, it is worth to introduce a special notation for this.

::::::{prf:definition} Intuitive definition of an infinite limit
:label: Def:LimitatPoint:Inflimitint
Let $f$ be a function defined near $x=a$ (except possible at $x=a$ itself). Then we say that $f$ has an **infinite limit** at $x=a$, and we write $\lim\limits_{x\rightarrow a}f(x)=\infty$ whenever the function values $f(x)$ grow arbitrarily large as $x$ approaches $a$.

Similarly, we say that $f$ has a **negative infinite limit** at $x=a$, and we write $\lim\limits_{x\rightarrow a}f(x)=-\infty$ whenever the function values $f(x)$ grow arbitrarily large negative as $x$ approaches $a$.
::::::

::::::{warning} 
:label: Warning:LimitatPoint:Infinitelimit
The notations $\lim\limits_{x\rightarrow a}f(x)=\infty$ and $\lim\limits_{x\rightarrow a}f(x)=-\infty$ do not mean that $\infty$ and $-\infty$ are numbers, nor do they mean that these limits exist. A correct way to pronounce the notation $\lim\limits_{x\rightarrow a}f(x)=\infty$ is **the limit of $f$ as $x$ approaches $a$ does not exist, because the function values grow without bound**.
::::::

Similarly, we use the corresponding notations $\lim\limits_{x\rightarrow a^-}f(x)=\infty$ and $\lim\limits_{x\rightarrow a^-}f(x)=-\infty$, or $\lim\limits_{x\rightarrow a^+}f(x)=\infty$ and $\lim\limits_{x\rightarrow a^+}f(x)=-\infty$, when considering only values of $x$ smaller than $a$, or larger than $a$ respectively. In each of the cases described above, the function $f$ approaches the vertical line $x=a$ asymptotically, either from the left, from the right, or from both sides. As such, we have the following definition.

::::::{prf:definition} Vertical asymptote
:label: Def:LimitatPoint:Verticalasymptote
Let $f$ be a function that is defined near $x=a$ (except possibly at $x=a$ itself). Then we say that $x=a$ is a **vertical asymptote** of $f$, whenever one (or more) of the following statements is true.

- $\lim\limits_{x\rightarrow a^-}f(x)=\infty$
- $\lim\limits_{x\rightarrow a^-}f(x)=-\infty$
- $\lim\limits_{x\rightarrow a^+}f(x)=\infty$
$\lim\limits_{x\rightarrow a^+}f(x)=-\infty$
::::::

::::::{prf:example} 
:label: Ex:LimitatPoint:Verticalasymptote1.
Suppose we want to evaluate $\lim\limits_{x\rightarrow 0}\dfrac{1}{x^2}$. Note that as $x$ approaches $0$, $x^2$ will approach $0$ as well and note that $x^2>0$ for all $x\neq 0$. So for $x$ close to $0$, $\dfrac{1}{x^2}$ is $1$ divided by a very small, positive number, which means that $\dfrac{1}{x^2}$ is a very large, positive number. As such, we find that $\lim\limits_{x\rightarrow 0}\dfrac{1}{x^2}=\infty$. In particular, the function has a vertical asymptote at $x=0$.
::::::

::::::{prf:example} 
:label: Ex:LimitatPoint:Verticalasymptote2.
Suppose we want to find all vertical asymptotes of $f(x)=\dfrac{1}{(x-1)(x-2)^2}$. The function is properly defined for $x$ unequal to either $1$ or $2$. For values of $x$ near either $x=1$ or $x=2$, we note that the denominator $(x-1)(x-2)^2$ is close to $0$, so the function blows up there. However, it depends whether it blows up to infinity or to minus infinity. We start near $x=1$. For $x<1$, we see that $\dfrac{1}{(x-1)(x-2)^2}<0$, so we have $\lim\limits_{x\rightarrow 1^-}f(x)=-\infty$. On the other hand, for $x>1$, we have $\dfrac{1}{(x-1)(x-2)}>0$, so we have $\lim\limits_{x\rightarrow 1^+}f(x)=\infty$. Using a similar reasoning, we find that $\lim\limits_{x\rightarrow 2^-}f(x)=\infty$ and $\lim\limits_{x\rightarrow 2^+}f(x)=\infty$.

We conclude that $f$ has $2$ vertical asymptotes, one at $x=1$ and $x=2$. Moreover, we see that $\lim\limits_{x\rightarrow 2}f(x)=\infty$, since the function values both on the left and right of $x=2$ grow arbitrarily large. Is there also a shorter way we can denote the behaviour near $x=1$? Unfortunately, there is not, since on the left the function values become negative, while on the right the function values become positive. So the only thing we can write down is that $\lim\limits_{x\rightarrow 1}f(x)$ does not exist.
::::::

::::::{warning} 
:label: Warning:LimitatPoint:Infinitelimitleftright
If either $\lim\limits_{x\rightarrow a^-}f(x)=\infty$ and $\lim\limits_{x\rightarrow a^+}f(x)=-\infty$, or $\lim\limits_{x\rightarrow a^-}f(x)=-\infty$ and $\lim\limits_{x\rightarrow a^+}f(x)=\infty$, then the only thing we can write for $\lim\limits_{x\rightarrow a}f(x)$ is that the limit does not exist. You should not use notation like $\lim\limits_{x\rightarrow a}f(x)=\pm\infty$ for this situation.
::::::


(Subsec:Limitsformaldef)=

## Precise definition of limits

So far, we have worked with a more intuitive understanding of what a limit is. However, {prf:ref}`Def:LimitatPoint:Intuitivelimit` contains some mathematically vague terms like "near" and "approaches". This also prevents us from proving the theorems stated throughout this section. In this final part, we make sure that those of you that have a more mathematically pure mindset can sleep well tonight by providing the precise definitions of regular, left and right limits, as well as proofs of the given theorems.

::::::{prf:definition} Precise definition of a limit
:label: Def:LimitatPoint:Precisedef
Let $f$ be a function that is defined near $x=a$ (except possibly at $x=a$ itself). Then we say that the **limit** of $f$ as $x$ approaches $a$ is equal to $L$, and we write $\lim\limits_{x\rightarrow a}f(x)=L$, whenever for each $\epsilon>0$ there exists a $\delta>0$, such that for all $x$ in the domain of $a$ with $0<|x-a|<\delta$, we have $|f(x)-L|<\epsilon$. If no such value $L$ exists we say that the limit does not exist.
::::::

This definition should be interpreted as follows. The arbitrary constant $\epsilon>0$ should be thought of as a vertical tolerance. In order for $\lim\limits_{x\rightarrow a}f(x)=L$, we want that, for $x$ close enough to $a$, the function values $f(x)$ are at most distance $\epsilon$ to $a$, i.e. $|f(x)-L|<\epsilon$. Here "$x$ close enough to $a$" means that this inequality should hold true for all $x$ in a (possibly very small) interval centered around $a$, i.e. an interval of the form $(x-\delta,x+\delta)$. Of course, what this $\delta$ is, depends both on the function $f$ and the choice of $\epsilon$. Typically, the smaller $\epsilon$ is, the smaller $\delta$ should be, as it becomes harder to satisfy the inequality $|f(x)-L|<\epsilon$. As such, the most interesting (and hardest) part of evaluating a limit using this definition is when $\epsilon$ is small. Remember that we cannot choose $\epsilon$ ourselves: for **each** $\epsilon>0$ there should be a corresponding $\delta$. Note that we can make $\delta$ always smaller if we want to: if at least one $\delta$ works for a given $\epsilon$, we are happy. Let us try to see how to work with this definition in practice.

::::::{prf:example} 
:label: Ex:LimitatPoint:Formaldefexists.
We aim to show that $\lim\limits_{x\rightarrow 2}x^2=4$ using the formal definition of a limit. For this, we let $\epsilon>0$ be an arbitrary positive number. Now, we need to choose $\delta>0$, which will very likely depend on $\epsilon$, in such a way that for any $x$ with $0<|x-2|<\delta$ we have $|x^2-4|<\epsilon$. For this, we note that $|x^2-4|=|x-2||x+2|$. First we consider the term $|x+2|$. Since we want to consider values of $x$ close to $2$, we can at the very least assume that $1<x<3$, i.e. $|x-2|<1$, and for those values of $x$ we know that $3<|x+2|<5. This means that we should choose $\delta$ to be at most $1$. If we do that, we find that for $x$ with $0<|x-2|<1$ we have $|x+2|<5$. In order for the product $|x-2||x+2|$ to be smaller than $\epsilon$, we should then ensure that the other term $|x-2|$ is less than $\dfrac{\epsilon}{5}$. Since choosing $\delta$ precisely restricts the values of $|x-2|$, this means that we should also ensure that $\delta$ is at most $\frac{\epsilon}{5}$.

We find that we have two conditions on $\delta$: $\delta$ should be at most $1$ and $\delta$ should be at most $\dfrac{\epsilon}{5}$. As such, we choose $\delta$ to be the lowest of these two values: $\delta=\mathrm{min}\left(1,\dfrac{\epsilon}{5}\right)$. Then for any $x$ with $0<|x-2|<\delta$ we obtain

$$
 \begin{array}{lcll}|x^2-a^2|&=&|x-a||x+a|\\
 &<&|x-a|\cdot 5\qquad\qquad&\left(\text{since }|x-a|<\delta\leq 1\right)\\
 &<&\dfrac{\epsilon}{5}\cdot 5&\left(\text{since }|x-a|<\delta\leq\dfrac{\epsilon}{5}\right)\\
 &=&\epsilon&\end{array}
$$

With that, we have shown that $\lim\limits_{x\rightarrow 2}x^2=4$.

Hier applet waarbij de functie te zien is en er met een slider in te stellen is wat epsilon is. Die wordt weergegeven als verticale strip. De bijbehorende horizontale strip geeft aan welke waarden er toegestaan zijn (met de keuze van delta uit deze opgave).
::::::

::::::{prf:example} 
:label: Ex:LimitatPoint:Formaldefdoesnotexist.
We aim to show that $\lim\limits_{x\rightarrow 0}\dfrac{|x|}{x}$ is not equal to $0$ using the formal definition of a limit (in fact, the limit does not exist at all, see {prf:ref}`Ex:LimitatPoint:LimitLeftRight`). Since this definition states that some property needs to hold for every $\epsilon>0$, we can show that the limit does not exist by showing that this property does not hold for a single choice of $\epsilon$. Note that $\epsilon=2$ is too large: for any $x\neq 0$ we have that $\dfrac{|x|}{x}$ is either $1$ or $-1$, which are both within distance $2$ of $0$. However, choosing $\epsilon=\dfrac{1}{2}$ does work. In order to show this, we need to verify that any choice of $\delta>0$ does not work, so we consider an arbitrary $\delta>0$. Then we take any $x$ with $0<x<\delta$. Since this $x$ is postive, we know that $\dfrac{|x|}{x}=1$, which means that $\left|\dfrac{|x|}{x}-0\right|=1>\dfrac{1}{2}=\epsilon$. We conclude that $\lim\limits_{x\rightarrow 0}\dfrac{|x|}{x}$ is unequal to $0$.

Hier applet waarbij de functie te zien is en er met een slider in te stellen is wat epsilon is. Die wordt weergegeven als verticale strip. De bijbehorende horizontale strip geeft aan welke waarden er toegestaan zijn: voor epsilon>1 verschijnt er een horizontale strip, terwijl voor epsilon<1 er niets te zien is.
::::::

Let us now consider the precise definitions of the other type of limits we have seen in these sections.

::::::{prf:definition} Precise definition of a left and right limit
:label: Def:LimitatPoint:Precisedefleftright
Let $f$ be a function that is defined for values of $x<a$ close to $x=a$. We say that the **left limit** of $f$ as $x$ approaches $a$ is equal to $L$, and we write $\lim\limits_{x\rightarrow a^-}f(x)=L$, if whenever for each $\epsilon>0$ there exists a $\delta>0$, such that for all $x$ in the domain of $a$ with $a-\delta<x<a$, we have $|f(x)-L|<\epsilon$. If no such value $L$ exists we say that the left limit does not exist.

Similarly, if $f$ is defined for values of $x>a$ close to $x=a$, we say that the **right limit** of $f$ as $x$ approaches $a$ is equal to $L$, and we write $\lim\limits_{x\rightarrow a^+}f(x)=L$, if whenever for each $\epsilon>0$ there exists a $\delta>0$, such that for all $x$ in the domain of $a$ with $a<x<a+\delta$, we have $|f(x)-L|<\epsilon$. If no such value $L$ exists we say that the right limit does not exist.
::::::

::::::{prf:definition} Precise definition of an infinite limit
:label: Def:LimitatPoint:Precisedefinflimit
Let $f$ be a function defined near $x=a$ (except possible at $x=a$ itself). Then we say that $f$ has an **infinite limit** at $x=a$, and we write $\lim\limits_{x\rightarrow a}f(x)=\infty$ whenever for each $M>0$ there exists $\delta>0$ such that for all $x$ in the domain of $f$ with $0<|x-a|<\delta$ we have $f(x)>M$.

Similarly, we say that $f$ has a **negative infinite limit** at $x=a$, and we write $\lim\limits_{x\rightarrow a}f(x)=-\infty$ whenever for each $M<0$ there exists $\delta>0$ such that for all $x$ in the domain of $f$ with $0<|x-a|<\delta$ we have $f(x)<M$.
::::::


