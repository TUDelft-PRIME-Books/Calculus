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

We will postpone the precise definition of a limit to section ({numref}`Subsec:Limitsformaldef`). Instead, for now, we will use the following more intuitive definition of a limit.

::::::{prf:definition}
:label: Def:LimitatPoint:Intuitivelimit

Let $f$ be a function that is defined for values of $x$ close to $x=a$ (except possibly at $x=a$ itself). We say that the **limit** of $f$ as $x$ approaches $a$ is equal to $L$, and we write $\lim\limits_{x\rightarrow a}f(x)=L$, if the function values $f(x)$ approach $L$ as $x$ approaches $a$ (but $x$ not equal to $a$). If no such real number $L$ exists, we say that the limit of the function $f$ as $x$ approaches $a$ does not exist.
::::::

When trying to evaluate a limit of the form $\lim\limits_{x\rightarrow a}f(x)$, it is sometimes helpful to consider values of $x$ smaller than $a$, and values of $x$ larger than $a$ separately. For this we use **one-sided limits**.

::::::{prf:definition}
:label: Def:LimitatPoint:Intuitiveleftrightlimit

Let $f$ be a function that is defined for values of $x<a$ close to $x=a$. We say that the **left limit** of $f$ as $x$ approaches $a$ is equal to $L$, and we write $\lim\limits_{x\rightarrow a^-}f(x)=L$, if the function values $f(x)$ approach $L$ as $x$ approaches $a$ from the left (but $x$ not equal to $a$). If no such real number $L$ exists, we say that the left limit of the function $f$ as $x$ approaches $a$ does not exist.

Similarly, if $f$ is defined for values of $x>a$ close to $a$, we say that the **right limit** of $f$ as $x$ approaches $a$ is equal to $L$, and we write $\lim\limits_{x\rightarrow a^+}f(x)=L$, if the function values $f(x)$ approach $L$ as $x$ approaches $a$ from the right (but $x$ not equal to $a$). If no such real number $L$ exists, we say that the right limit of the function $f$ as $x$ approaches $a$ does not exist.
::::::

For the left and right limits, several different notation is used throughout the literature. Here, we will stick to the notation used above, but, for completeness, we will list the alternative notation here as well.

::::::{prf:definition}
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

So how do you evaluate limits (regular, left or right)? There are various techniques, which we will discuss throughout this section. In several of these, we evaluate the limit by rewriting or simplifying the function at hand. Indeed, in Example ({prf:ref}`Ex:LimitatPoint:FirstLimitEx`) we evaluated the limit $\lim\limits_{x\rightarrow 1}f(x)$ by finding a function $h$ which is equal to $f$ everywhere except at $x=1$ and for which $1$ was in the domain of $h$. The following two results show that this idea works more generally.
::::::{prf:theorem}
:label: Theorem:LimitatPoint:Rewritingworks
If $f(x)=g(x)$ whenever $x\neq a$, then $\lim\limits_{x\rightarrow a}f(x)=\lim_{x\rightarrow a}g(x)$, provided the limits exist, or $\lim\limits_{x\rightarrow a}f(x)$ and $\lim_{x\rightarrow a}g(x)$ both do not exist.
::::::


::::::{prf:theorem}
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

We conclude that the left and right limit of $f$ as $x$ approaches $0$ both exist, but are unequal. Using theorem ({prf:ref}`Theorem:LimitatPoint:Leftrightequal`) we conclude that $\lim\limits_{x\rightarrow 0}\frac{|x|}{x}$ does not exist.

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

 Using theorem ({prf:ref}`Theorem:LimitatPoint:Leftrightequal`) we conclude that $\lim\limits_{x\rightarrow 0}f(x)=2$, since both the left and right limit at that point are equal to $2$.

Hier nog plaatje van deze functie rond x=2, met als onderschrift een samenvatting van bovenstaande.

::::::

Note that in Example ({prf:ref}`Ex:LimitatPoint:LimitLeftRightComposite`) the function $f$ was defined in the point $x=2$, but that did not influence the value of the limit at all; in fact, the limit $\lim\limits_{x\rightarrow 2}f(x)$ is unequal to $f(2)$. This is because, when evaluating a limit, we are only interested in the behaviour of the function values $f(x)$ for $x$ close to, but *unequal to* $a$. We can summarize this observation as follows.

::::::{prf:remark}
:label: RemarkLimitatPoint:Valueirrelevant
If $f(a)$ is defined, then its value is *irrelevant* for the existence and value of $\lim\limits_{x\rightarrow a} f(x)$.
::::::

(Subsec:Limitsformaldef)=

## Precise definition of limits

In this section we cover

- Intuitive definition (including one-sided limits)
- Basic rules of calculation
- Vertical asymptotes
- Cancelling common factors, square root trick, squeeze theorem
- Formal definition