# Inverse functions

So far, we have mainly been interested in evaluating function values, i.e. for a given function $f$ and $x$ in the domain of $f$, we want to find $y=f(x)$. However, often it also interesting to try to find for which value(s) of $x$, if any, we have $y=f(x)$. That is, we want to somehow undo the function $f$ and go back to the domain.

In some cases, this is possible. Consider, for instance, the function $f(x)=2x+3$ and say we want to find out for which value of $x$, if any, we have $f(x)=5$. This means that we want to solve the equation $2x+3=5$, which has $x=1$ as a solution. Indeed, we have $f(1)=5$.

In other cases, we can even find multiple values. Indeed, suppose that we have $f(x)=x^2$ and we want to find for which values of $x$ we have $f(x)=4$. Then we need to solve $x^2=4$, which has both $x=2$ and $x=-2$ as a solution. Indeed, we have $f(2)=f(-2)=4$. However, this does pose a problem: we cannot really undo the function $f$, since if we know that $f(x)=y$ then there are two choices for $x$ and there is no way of knowing which of the two choices is the correct one.

Finally, there are also cases where we cannot find any values. If we again consider $f(x)=x^2$ then there are no values of $x$ with $f(x)=-1$. Indeed, such a number $x$ would need to satisfy $x^2=-1$, which does not have any (real) solutions.

If it is always possible to find exactly $1$ value of $x$ with $y=f(x)$ for each $y$, this means we can consider the function that maps each value of $y$ to the unique $x$ with $f(x)=y$. Such a function is called the **inverse function** of $f$. In this section, we will define and anlyse inverse fuctions and show under which conditions they exist. Then, we will consider inverse functions of certain standard functions, logarithms for exponential functions and inverse trigonometric functions for trigonometric functions, that are so well-known that they can be called standard functions themselves.

(Subsec:InverseExistProp)=

## Existence and properties of inverse functions

::::::{prf:definition} Inverse function
:label: Def:Inverse:Inverse

Let $f$ be a function with domain $D$ and range $R$. A function $g$ with domain $R$ and range $D$ is called the **inverse function** of $f$ if for all $x$ in $D$ and $y$ in $R$ we have $f(x)=y$ precisely when $g(y)=x$. If the inverse function exists, we denote it by $f^{-1}$.
::::::

::::::{warning} 
:name: Warning:Inverse:Notation

Do not confuse $f^{-1}$ with $\frac{1}{f}$. Usually, these are different functions.
::::::


::::::{prf:theorem}
:label: Thm:Inverse:Inverseinverse

- If the inverse function exists, it must be unique. 
- If $g$ is the inverse function of $f$, then $f$ is the inverse fuction of $g$.

::::::

:::{admonition} Proof 
:class: tudproof
Suppose $g$ and $h$ are both inverses of the same function $f$, which has domain $D$ and range $R$. Let $y$ in $R$ and write $x_1=g(y)$ and $x_2=h(y)$. Since $x_1=g(y)$ we have by the definition of the inverse that $f(x_1)=y$. Similarly, we must have $f(x_2)=y$ since $x_2=h(y)$. Since $f(x_1)=y$ and $h$ is an inverse of $f$, we must have $h(y)=x_1$, so $x_1=x_2$. This means that $g(y)=x_1=x_2=h(y)$. So $g$ and $h$ must be the same function. Hence, $f$ only has $1$ inverse function.

Suppose the function $g$ with domain $R$ and range $D$ is the inverse function of $f$, which has domain $D$ and range $R$. Then for all $y$ in the domain of $g$ and $x$ in the range of $g$ we have $g(y)=x$ precisely when $f(x)=y$, since $g$ is the inverse of $f$. This precisely means that $f$ is also the inverse function of $g$.
:::

The interpretation of the inverse function is that it 'undoes' what $f$ does. Indeed, if $x$ is in the domain of a function $f$ which has an inverse function $f^{-1}$, then we have $f^{-1}(f(x))=x$. This follows, since by definition $f^{-1}(f(x))$ is the unique number $\tilde{x}$ in the domain of $f$ with $f(\tilde{x})=f(x)$, which must mean that $\tilde{x}=x$. This also works the other way around: for $y$ in the the domain of $f^{-1}$ we must have $f(f^{-1}(y))=y$, since by definition $f^{-1}(y)$ is the unique number $x$ in the domain of $f$ with $f(x)=y$. The two equations $f^{-1}(f(x))=x$ and $f(f^{-1}(y))=y$ are called the **cancelling equations**. In fact, the cancelling equations $g(f(x))=x$ and $f(g(y))=y$ hold precisely when $f$ and $g$ are inverses of each other. In fact, verifying that the cancelling equations hold is usually the easiest way to show that two functions are inverses of each other.

::::::{prf:theorem}
:label: Thm:Inverse:Cancelling equations

Let $f$ be a function with domain $D$ and range $R$ and let $g$ be a function with domain $R$. Then $g=f^{-1}$ precisely when the cancelling equations $g(f(x))=x$ and $f(g(y))=y$ hold for all $x$ in $D$ and all $y$ in $R$.

::::::

:::{admonition} Proof 
:class: tudproof
In the discussion preceding this theorem, we already showed that the cancelling equations hold if $g=f^{-1}$. Hence, we now assume that the cancelling equations $g(f(x))=x$ and $f(g(y))=y$ hold for all $x$ in $D$ and all $y$ in $R$ and we will show that $g=f^{-1}$. Let $x$ in $D$ and write $y=f(x)$. Then $g(y)=g(f(x))=x$ because of the first cancelling equation. Moreover, let $y$ in $R$ and write $x=g(y)$. Then $f(x)=f(g(y))=y$ because of the second cancelling equation. As such, we have $f(x)=y$ precisely when $g(y)=x$. This means that $g=f^{-1}$.
:::

::::::{prf:example}
:label: Ex:Inverse:FirstEx

Consider the function $f(x)=2x+5$. We want to try to find an inverse of this function. For this we want to find a function $g$ such that $g(y)=x$ precisely when $y=f(x)=2x+5$. As such, we write $y=2x+5$ and aim to express $x$ as a function of $y$. For this, we rewrite

$$
 y=2x+5,\quad\Longleftrightarrow\quad y-5=2x,\quad\Longleftrightarrow\quad \frac{y-5}{2}=x
$$

This suggests that the function $g(y)=\frac{y-5}{2}$ is the inverse of $f$. In order to check that this is correct, we verify that the cancelling equations hold. Note that the domain and range of $f$ are both $\mathbb{R}$. Hence, for $x$ and $y$ in $\mathbb{R}$ we find

$$
 \begin{array}{lclclclcl}g(f(x))&=&g(2x+5)&=&\dfrac{(2x+5)-5}{2}&=&\dfrac{2x}{2}&=&x,\\ f(g(y))&=&f\left(\dfrac{y-5}{2}\right)&=&2\dfrac{y-5}{2}+5&=&(y-5)+5&=&y\end{array}
$$

So the cancelling equations indeed hold and we find that $g$ is the inverse of $f$. As such, we find $f^{-1}(x)=\frac{x-5}{2}$.
::::::

::::::{note}
:label: Note:Inverse:Inputnamexory

In {prf:ref}`Ex:Inverse:FirstEx` we used the symbol $y$ as the input for $g$, while we use $x$ for $f^{-1}$. This is simply a matter of convenience: since we obtain the expression for $g$ by rewriting the equation $y=f(x)$ it is natural to use $y$ there. On the other hand, $f^{-1}$ is a function of which the domain is the real numbers, so it is customary to use the symbol $x$ there. However, these are still just choices for which letter we use and we could just as well have used a different choice. 

::::::

::::::{prf:example}
:label: Ex:Inverse:SecondEx

Consider the function $f(x)=x^2$. We want to try to find an inverse of this function. For this we want to find a function $g$ such that $g(y)=x$ precisely when $y=f(x)=x^2$. As such, we write $y=x^2$ and aim to express $x$ as a function of $y$. For this, we rewrite

$$
 y=x^2,\quad\Longleftrightarrow\quad x=\pm\sqrt{y}
$$

This means that we have two choices for what $x$ should be in terms of $y$, which does not sound very promising. Since mathematicians tend to be very stubborn people, we choose to not give up here (yet) and just make a choice and see where we end up. So here, we define $g(y)=\sqrt{y}$. Then for any $y$ in the domain of $g$ we have $f(g(y))=f(\sqrt{y})=(\sqrt{y})^2=y$, so at least one of the cancelling equations holds. However, the other cancelling equation does not hold. Indeed, we have, for instance, that $g(f(-2))=g\left((-2)^2\right)=g(4)=\sqrt{4}=2$. So $g$ cannot be the inverse of $f$. The other choice for $g$ does not fare any better, so we are ready to conclude that the function $f$ does not have an inverse. How can we be sure of that, though? In general, failing to show that something is true does not mean that it is not true. Maybe we were just not creative enough. Well, let us take any function $g$ with domain $[0,\infty)$ (the domain of an inverse function should always be the range of the original function). We will show that this function $g$ runs into the same issues as the choices we have made before. Indeed, if $g$ were to be the inverse function of $f$, then since $f(2)=2^2=4$, we would need to have $g(4)=2$. On the other hand, since $f(-2)=(-2)^2=4$, we would also need to have $g(4)=-2$. However, $g(4)$ cannot at the same time be $2$ and $-2$, so such a function $g$ does not exist.
::::::

{prf:ref}`Ex:Inverse:SecondEx` shows a major issue we have at this point: we lack a quick way of showing that a function does not have an inverse function. If a function has an inverse function, we can (hopefully) find it and prove that it is an inverse function by, for instance, verifying that the cancelling equations hold, but this does not work the other way around. So the goal now is to develop a criterion to check whether a certain function has an inverse function.

The main reason why we could not find an inverse function for the function $f(x)=x^2$ in {prf:ref}`Ex:Inverse:SecondEx` was that $f(2)=f(-2)=4$, so we there was no way to determine whether, if $g$ were an inverse of $f$, $g(4)$ should be $2$ or $-2$. In fact, the reason a function $f$ does not have an inverse will **always** be that there are two different points, $a$ and $b$, with $f(a)=f(b)$, since in such a case it is impossible to determine what the inverse should in do in this point $f(a)=f(b)$. This idea will allow us to find a criterion to determine invertibility. Before we formulate this, we will introduce some terminology.

::::::{prf:definition}
:label: Def:Inverse:Onetoone

A function $f$ is called **one-to-one** or **injective** if for every two different points $a$ and $b$ in the domain of $f$ we have $f(a)\neq f(b)$. 
::::::

Stated differently, $f$ is one-to-one precisely when it does not take the same value more than once. For a one-to-one function the problem of having a choice which value to assign to a certain number can never arise. As such, we finally obtain our desired criterion.

::::::{prf:theorem} 
:label: Thm:Inverse:InverseInjective

Let $f$ be a function with domain $D$ and range $R$. Then $f$ has an inverse function (with domain $R$) precisely when $f$ is one-to-one.
::::::

:::{admonition} Proof 
:class: tudproof
Assume that $f$ is one-to-one. Let $y$ in $R$. Since $R$ is the range of $f$, there is at least one $x$ with $f(x)=y$ and since $f$ is one-to-one, there is precisely one such $x$. Then we define $g(y)=x$. By construction, we have $f(g(y))=f(x)=y$, so one of the cancelling equations holds. Now we pick an arbitrary $x$ in $D$ and write $y=f(x)$. Since $x$ is the only number that maps to $y$ (since $f$ is one-to-one) we have $g(y)=x$, so we find $g(f(x))=g(y)=x$. Hence, both cancelling equations hold, which means that $g=f^{-1}$. We conclude that $f$ has an inverse function with domain $R$.

Now we assume that $f$ has an inverse function. Let $a$ and $b$ be different points in the domain of $f$ and suppose that $f(a)=f(b)$. Then we find that

$$
 a=f^{-1}(f(a))=f^{-1}(f(b))=b
$$

Since $a$ and $b$ were assumed to be different, this gives a contradiction. So no such points $a$ and $b$ exist, which means that $f$ must be one-to-one.

:::

::::::{prf:example}
:label: Ex:Inverse:ThirdEx

Consider the function $h(x)=\sqrt{x}$. Then we know that $\sqrt{a}=\sqrt{b}$ precisely when $a=b$, so the function $h$ is one-to-one. By {prf:ref}`Thm:Inverse:InverseInjective` it must have an inverse function. Let us try to find this inverse function. Since we want $h^{-1}(y)=x$ precisely when $h(x)=y$, we write $\sqrt{x}=y$ and try to express $x$ as a function of $y$. From $\sqrt{x}=y$ it quickly follows that $x=y^2$, so the function $k(y)=y^2$ must be the inverse function of $h$. So $h^{-1}(x)=x^2$. 

No wait, that cannot be right. In {prf:ref}`Ex:Inverse:SecondEx` we showed that the function $f(x)=x^2$ did not have an inverse function, so how can it be the inverse function of $h$? The point here is that the functions $f$ and $h^{-1}$ do not have the same domain. For the function $f$ we simply assume it is defined on its maximal domain, which is the real line $\mathbb{R}$. On the other hand, the domain of the inverse function is always equal to the range of the original function. Since the range of $h$ is equal to $[0,\infty)$, this must be the the domain of the function $h^{-1}$. 

Still, why does this difference in domain make that $h^{-1}$ is invertible, while $f$ is not? The reason why $f$ is not invertible is that it is not one-to-one, since for any $x>0$ we have $f(x)=f(-x)$. However, since the domain of $h^{-1}$ does not contain any negative numbers, it does not run into this issue: for each $y$ there is at most one $x\geq 0$ with $x^2=y$. Indeed, the graph of the function $h^{-1}$ is only the right half of the parabola $y=x^2$, so each value of $y$ corresponds to at most one value of $x$. So the function $h^{-1}$ is one-to-one, which is the reason why it does have an inverse function.

Hier een plaatje van de functies $\sqrt{x}$, $x^2$ met vol domein en $x^2$ met rechterhalf domein. Ik weet niet of dat goed zichbaar te maken is. 
::::::

::::::{note}
:label: Note:Inverse:Restrictdomain

As we experienced in {prf:ref}`Ex:Inverse:ThirdEx` restricting the domain of a function can make it one-to-one, and, therefore, have an inverse function, even if the function does not have an inverse when it is defined on its maximal domain.

Reversely, we know that the domain of the inverse function is always the range of the original function. Hence, it can happen that the domain of the inverse function is not its maximal domain.

::::::

In the preceding examples, we have found the inverse function (whenever it exists) by starting with the equation $y=f(x)$ and trying to express $x$ as a function of $y$. This method works in general, so let us present it as an alogrithm.

::::::{prf:algorithm} How to find the inverse of a one-to-one function?
Let $f$ be a one-to-one function. Then the inverse of $f$ can be found as follows.

1. Start with the equation $y=f(x)$;
2. Solve this equation for $x$ (in terms of $y$);
3. Interchange the roles of $x$ and $y$, then we have $y=f^{-1}(x)$.

::::::


::::::{prf:example}
:label: Ex:Inverse:FourthEx

Consider the function $f(x)=x^2-4x$, defined for $x\leq 2$. Then the bottom of the parabola $y=x^2-4x$ is at $x=2$, so the graph of $x$ is the left half of a parabola. Hence, the function $f$ is one-to-one on this domain (note that it is not one-to-one on its maximal domain). We follow the algorithm presented above to find the inverse function of $f$.

We start with the equation $y=f(x)$, i.e. $y=x^2-4x$. We write this equation to $x^2-4x-y=0$, which is a quadratic equation in $x$. As such, we can find the solutions by the quadratic formula or by completing the square and we find

$$
 x=\frac{4\pm\sqrt{(-4)^2-4\cdot1\cdot(-y)}}{2\cdot 1}=2\pm\sqrt{4+y}
$$

Now we wonder whether we should have $x=2+\sqrt{4+y}$ or $x=2-\sqrt{4+y}$. For this we use that $f$ is only defined for $x\leq 2$, so our choice must ensure that $x\leq 2$. 

NOG NIET AF

::::::

In this section we cover

- Injectivity/one-to-one
- Surjectivity/onto
- Inverse function
- Graph of inverse function
- Logarithms
- Inverse trigonometric functions