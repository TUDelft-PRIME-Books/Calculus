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

The interpretation of the inverse function is that it 'undoes' what $f$ does. Indeed, if $x$ is in the domain of a function $f$ which has an inverse function $f^{-1}$, then we have $f^{-1}(f(x))=x$. This follows, since by definition $f^{-1}(f(x))$ is the unique number $\tilde{x}$ in the domain of $f$ with $f(\tilde{x})=f(x)$, which must mean that $\tilde{x}=x$. This also works the other way around: for $y$ in the the domain of $f^{-1}$ we must have $f(f^{-1}(y))=y$, since by definition $f^{-1}(y)$ is the unique number $x$ in the domain of $f$ with $f(x)=y$. The two equations $f^{-1}(f(x))=x$ and $f(f^{-1}(y))=y$ are called the **cancelling equations**. In fact, the cancelling equations $f(g(x))=x$ and $g(f(y))=y$ hold precisely when $f$ and $g$ are inverses of each other.

HIER STELLING CANCELLING

In this section we cover

- Injectivity/one-to-one
- Surjectivity/onto
- Inverse function
- Graph of inverse function
- Logarithms
- Inverse trigonometric functions