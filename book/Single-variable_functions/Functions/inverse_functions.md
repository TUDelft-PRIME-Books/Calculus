(Section:Inverse)=

# Inverse functions

## Introduction

%::::{figure} Images/Fig-Inverse-Intro.png
%:name: Fig:Inverse:Intro
%:class: dark-light
%:figclass: margin

%Easier said than done?

%::::



So far, we have mainly been interested in evaluating functions, i.e. for a given function $f$ and $x$ in the domain of $f$, we want to find $y=f(x)$. However, often it is also interesting for some value of $y$ in the range of $f$ to try to find for which value(s) of $x$, if any, we have $f(x)=y$. That is, we want to somehow undo the function $f$ and go back to the domain.

In some cases, this is possible. Consider, for instance, the function $f(x)=2x+3$ and say we want to find out for which value of $x$, if any, we have $f(x)=5$. This means that we want to solve the equation $2x+3=5$, which has $x=1$ as a solution. Indeed, we have $f(1)=5$.

In other cases, we can even find multiple values. Indeed, suppose that we have $f(x)=x^2$ and we want to find for which values of $x$ we have $f(x)=4$. Then we need to solve $x^2=4$, which has both $x=2$ and $x=-2$ as solutions. Indeed, we have $f(2)=f(-2)=4$. However, this does pose a problem: we cannot really undo the function $f$, since if we know that $f(x)=y$ then there are two choices for $x$ and there is no way of knowing which of the two choices is the correct one.

Finally, there are also cases where we cannot find any values. If we again consider $f(x)=x^2$ then there are no values of $x$ with $f(x)=-1$. Indeed, such a number $x$ would need to satisfy $x^2=-1$, which does not have any (real) solutions.

If it is always possible to find exactly $1$ value of $x$ with $y=f(x)$ for each $y$, this means we can consider the function that maps each value of $y$ to the unique $x$ with $f(x)=y$. Such a function is called the **inverse function** of $f$. In this section, we will define and analyse inverse functions and show under which conditions they exist. Then, we will consider inverse functions of certain standard functions: logarithms for exponential functions and inverse trigonometric functions for trigonometric functions. These are so well-known that they can be called standard functions themselves.

(Subsec:InverseExistProp)=

## Definition, existence and properties

Before we can introduce the definition of an inverse function, we need one more concept.

::::::{prf:definition}
:label: Def:Inverse:Onto
A function $f$ is called **onto** or **surjective** whenever the codomain of $f$ coincides with the range of $f$. That is, the equation $f(x)=y$ should have at least one solution $x$ for each $y$ in the codomain of $f$.
::::::

::::{note}
:name: Note:Inverse:Onto

In order for any function to have an inverse function, it needs to be onto. However, we do not put emphasis on this now and you should not worry too much about it. Indeed, if a function is not onto, we can make it onto by restricting its codomain to be equal to its range, without changing the behaviour of the function. At the end of {numref}`Subsec:InverseExistProp`, we go more into detail on this. For now, we just assume that all functions that we are dealing with are onto.
::::



::::::{prf:definition} Inverse function
:label: Def:Inverse:Inverse

Let $f$ be an onto function with domain $D$ and range $R$. An onto function $g$ with domain $R$ and range $D$ is called the **inverse function** of $f$ if for all $x$ in $D$ and $y$ in $R$ we have $f(x)=y$ precisely when $g(y)=x$. If the inverse function exists, we denote it by $f^{-1}$. A function which has an inverse function is called **invertible**.
::::::

::::::{warning} 
:name: Warning:Inverse:Notation

Do not confuse $f^{-1}$ with $\frac{1}{f}$. Usually, these are different functions.
::::::

Notice that in the definition we talk about *the* inverse function. This must mean that a function cannot have multiple inverse functions. Indeed, we obtain the following result.

::::::{prf:theorem}
:label: Thm:Inverse:InverseInverse

- If the inverse function of $f$ exists, it must be unique. 
- If $g$ is the inverse function of $f$, then $f$ is the inverse function of $g$. This means that $\left(f^{-1}\right)^{-1}=f$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Inverse:InverseInverse`
:class: tudproof

Suppose $g$ and $h$ are both inverses of the same function $f$, which has domain $D$ and range $R$. Let $y$ be in $R$ and write $x_1=g(y)$ and $x_2=h(y)$. Since $x_1=g(y)$ we have by the definition of the inverse that $f(x_1)=y$. Similarly, we must have $f(x_2)=y$ since $x_2=h(y)$. Since $f(x_1)=y$ and $h$ is an inverse of $f$, we must have $h(y)=x_1$, so $x_1=x_2$. This means that $g(y)=x_1=x_2=h(y)$. Since this holds for every $y$ in $R$, $g$ and $h$ must be the same function. Hence, $f$ only has $1$ inverse function.

Suppose the function $g$ with domain $R$ and range $D$ is the inverse function of $f$, which has domain $D$ and range $R$. Then for all $y$ in the domain of $g$ and $x$ in the range of $g$ we have $g(y)=x$ precisely when $f(x)=y$, since $g$ is the inverse of $f$. This precisely means that $f$ is also the inverse function of $g$. As such, $\left(f^{-1}\right)^{-1}$ is the inverse function of $f^{-1}=g$, which must be $f$, so we find $\left(f^{-1}\right)^{-1}=f$.
:::

::::::{prf:example}
:label: Ex:Inverse:FirstEx

Consider the function $f(x)=2x+5$. We want to try to find the inverse of this function. For this, we want to find a function $g$ such that $g(y)=x$ precisely when $y=f(x)=2x+5$. As such, we write $y=2x+5$ and aim to express $x$ as a function of $y$. We rewrite

$$
 y=2x+5\quad\Longleftrightarrow\quad y-5=2x\quad\Longleftrightarrow\quad \frac{y-5}{2}=x.
$$

This means that the function $g(y)=\frac{y-5}{2}$ is the inverse of $f$. Indeed, we have $y=f(x)=2x+5$ precisely when $x=g(y)=\frac{y-5}{2}$.
::::::

We can also nicely visualise the graph of an inverse function by manipulating the graph of the original function. Indeed, if $f$ has an inverse function $f^{-1}$, then $(x,y)$ is on the graph of $f$ precisely when $f(x)=y$. By definition of the inverse function, for such a point $(x,y)$ we must have $f^{-1}(y)=x$. This means that the point $(y,x)$ is on the graph of $f^{-1}$. This also works the other way around, so $(x,y)$ is on the graph of $f$ precisely when $(y,x)$ is on the graph of $f^{-1}$. As such, we find the graph of $f^{-1}$ by reflecting the graph of $f$ along the line $y=x$ (since this reflection maps a point $(x,y)$ to $(y,x)$). With that, we have shown the following result.

::::::{prf:theorem} Graph of inverse function
:label: Thm:Inverse:Graphinverse

If a single-variable function $f$ has an inverse function $f^{-1}$, then the graph of $f^{-1}$ can be found by reflecting the graph of $f$ along the line $y=x$.

::::::

The interpretation of the inverse function is that it 'undoes' what $f$ does. Indeed, if $x$ is in the domain of a function $f$ which has an inverse function $f^{-1}$, then we have $f^{-1}(f(x))=x$. This follows, since if we write $y=f(x)$ then the definition of the inverse function tells us that $f^{-1}(f(x))=f^{-1}(y)=x$. This also works the other way around: for $y$ in the the domain of $f^{-1}$ we must have $f(f^{-1}(y))=y$, since if we write $x=f^{-1}(y)$ then the definition of the inverse function tells us that $f(x)=f(f^{-1}(y))=x$. The two equations $f^{-1}(f(x))=x$ and $f(f^{-1}(y))=y$ are called the **cancelling equations**. In fact, the cancelling equations $g(f(x))=x$ and $f(g(y))=y$ hold precisely when $f$ and $g$ are inverses of each other. Moreover, verifying that the cancelling equations hold is usually the easiest way to show that two functions are inverses of each other.

::::::{prf:theorem}
:label: Thm:Inverse:CancellingEquations

Let $f$ be an onto function with domain $D$ and range $R$ and let $g$ be a function with domain $R$. Then $f$ is invertible with $g=f^{-1}$ precisely when the cancelling equations $g(f(x))=x$ and $f(g(y))=y$ both hold for all $x$ in $D$ and all $y$ in $R$.

::::::
:::{admonition} Proof of {prf:ref}`Thm:Inverse:CancellingEquations`
:class: tudproof

In the discussion preceding this theorem, we already showed that the cancelling equations hold if $g=f^{-1}$. Hence, we now assume that the cancelling equations $g(f(x))=x$ and $f(g(y))=y$ hold for all $x$ in $D$ and all $y$ in $R$ and we will show that $g=f^{-1}$. Let $x$ be in $D$ and write $y=f(x)$. Then $g(y)=g(f(x))=x$ because of the first cancelling equation. Moreover, let $y$ be in $R$ and write $x=g(y)$. Then $f(x)=f(g(y))=y$ because of the second cancelling equation. As such, we have $f(x)=y$ precisely when $g(y)=x$. This means that $g=f^{-1}$.
:::



::::::{prf:example} {prf:ref}`Ex:Inverse:FirstEx` continued
:label: Ex:Inverse:FirstExContinued

Again consider the function $f(x)=2x+5$. We saw that the function $g(y)=\frac{y-5}{2}$ is the inverse of $f$. In order to check that this is correct, we verify that the cancelling equations hold. Note that the domain and range of $f$ are both $\mathbb{R}$. Hence, for $x$ and $y$ in $\mathbb{R}$ we find

$$
 \begin{array}{lclclclcl}g(f(x))&=&g(2x+5)&=&\dfrac{(2x+5)-5}{2}&=&\dfrac{2x}{2}&=&x,\\ f(g(y))&=&f\left(\dfrac{y-5}{2}\right)&=&2\dfrac{y-5}{2}+5&=&(y-5)+5&=&y.\end{array}
$$

So the cancelling equations indeed hold and we reaffirm that $g$ is the inverse of $f$. Hence, we have $f^{-1}(x)=\frac{x-5}{2}$.

In the graphs of the functions $f$ and $f^{-1}$ shown below, we see that the graph of $f^{-1}$ can be obtained by reflecting the graph of $f$ along the line $y=x$, as we expected from {prf:ref}`Thm:Inverse:Graphinverse`.

:::{applet}
:url: calculus/inverse_functions/reflection_of_linear_function
:name: Fig:Inverse:FirstEx
:class: dark-light

The functions $f$, $f^{-1}$ and the line $y=x$.
:::

::::::

::::::{note}
:name: Note:Inverse:Inputnamexory

In {prf:ref}`Ex:Inverse:FirstEx` we used the symbol $y$ as the input for $g$, while we use $x$ for $f^{-1}$. This is simply a matter of convenience: since we obtain the expression for $g$ by rewriting the equation $y=f(x)$ it is natural to use $y$ there. On the other hand, $f^{-1}$ is a function of which the domain is the real numbers, so it is customary to use the symbol $x$ there. However, these are still just choices for which letter we use and we could just as well have used a different choice. 

::::::

:::{figure} Images/Fig-Inverse-SocksShoes.png
:name: Fig:Inverse:SocksShoes
:figclass: margin

Undoing the two actions in the incorrect order will result in torn socks, which means that you do not end up where you started.
:::

Now suppose that we have a function $h$ that is a composition of two other functions, so $h=f\circ g$. If $f$ and $g$ both have an inverse, does $h$ automatically have an inverse as well? To determine this, we should really think about having an inverse as being able to undo the action of the original function. So since $f\circ g$ first applies $g$ and then $f$, we can undo this by undoing both, but then **in reverse order**. This is sometimes known as the **socks and shoes rule**, since (normally, at least) you first put on your socks and then your shoes and if you want to undo this composition of two actions, you should undo them in reverse order, so you should take off your shoes first and then take off your socks. Otherwise, you might end up with torn socks like in {numref}`Fig:Inverse:SocksShoes`.

As such, we obtain the following result.

::::::{prf:theorem} Socks and shoes rule
:label: Thm:Inverse:Composition

Let $f$ and $g$ be invertible functions for which the domain of $f$ is equal to the range of $g$. Then $f\circ g$ is invertible and $(f\circ g)^{-1}=g^{-1}\circ f^{-1}$.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Inverse:Composition`
:class: tudproof

First we show that the function $g^{-1}\circ f^{-1}$ exists and that its domain and range are what they need to be in order for this function to be the inverse of $f\circ g$. Since the domain of $f$ is equal to the range of $g$, the range of $f^{-1}$ (which is the domain of $f$) is equal to the domain of $g^{-1}$ (which is the range of $g$). Hence, the function $g^{-1}\circ f^{-1}$ is defined. Moreover, that the domain of $f$ is equal to the range of $g$, means that the domain and range of $f\circ g$ are the domain of $g$ and the range of $f$ respectively. Similarly, the domain of $g^{-1}\circ f^{-1}$ is the domain of $f^{-1}$, which is the range of $f\circ g$, and the range of $g^{-1}\circ f^{-1}$ is the range of $g^{-1}$, which is the domain of $g$.

Now we show that the cancelling equations hold. For $x$ in the domain of $f\circ g$ we have

$$
 (g^{-1}\circ f^{-1})\left((f\circ g)(x)\right)=g^{-1}\left(f^{-1}\left(f(g(x))\right)\right)=g^{-1}(g(x))=x,
$$

while for $y$ in the range of $f\circ g$ we have

$$
 (f\circ g)\left((g^{-1}\circ f^{-1})(y)\right)=f\left(g\left(g^{-1}\left(f^{-1}(y)\right)\right)\right)=f\left(f^{-1}(y)\right)=y.
$$

Hence, both cancelling equations hold, so we must have that $f\circ g$ is invertible and $(f\circ g)^{-1}=g^{-1}\circ f^{-1}$.
:::

::::::{prf:example} 
:label: Ex:Inverse:Socksshoes

Again consider the function $f(x)=2x+5$. We saw that the function $f^{-1}(x)=\frac{x-5}{2}$ is the inverse of $f$. Moreover, consider the function $g(x)=x^3$. Then we have $x^3=y$ precisely when $x=\sqrt[3]{y}$, so the function $g$ is also invertible with inverse function $g^{-1}(x)=\sqrt[3]{x}$. Note, in addition, that the range of $f$ and the domain of $g$ are both $\mathbb{R}$. Now consider the composition $g\circ f$, which is given by

$$
 (g\circ f)(x)=g(f(x))=\left(2x+5\right)^3.
$$

According to {prf:ref}`Thm:Inverse:Composition`, the function $g\circ f$ is also invertible and we can find its inverse by evaluating

$$
 (g\circ f)^{-1}(x)=(f^{-1}\circ g^{-1})(x)=f^{-1}\left(g^{-1}(x)\right)=\frac{\sqrt[3]{x}-5}{2}.
$$

Note that we switched the order from $g\circ f$ to $f^{-1}\circ g^{-1}$ when finding the inverse function, since we do not want to tear our socks by trying to take them off before taking off our shoes.

:::{applet}
:url: calculus/inverse_functions/reflection_of_composite_function
:name: Fig:Inverse:SocksshoesEx
:class: dark-light

The graphs of the functions $g\circ f$ and $(g\circ f)^{-1}$ with the line $y=x$.
:::

::::::

::::::{prf:example}
:label: Ex:Inverse:SecondEx

Consider the function $f(x)=x^2$ with codomain equal to its range $[0,\infty)$, so that it is onto. We want to try to find the inverse of this function. For this, we want to find a function $g$ such that $g(y)=x$ precisely when $y=f(x)=x^2$. As such, we write $y=x^2$ and aim to express $x$ as a function of $y$. For this, we rewrite

$$
 y=x^2\quad\Longleftrightarrow\quad x=\pm\sqrt{y}.
$$

This means that we have two choices for what $x$ should be in terms of $y$, which does not sound very promising. Since mathematicians tend to be very stubborn people, we choose to not give up here (yet) and just make a choice and see where we end up. So here, we define $g(y)=\sqrt{y}$. Then for any $y$ in the domain of $g$ we have 

$$
 f(g(y))=f(\sqrt{y})=(\sqrt{y})^2=y,
$$

so at least one of the cancelling equations holds. However, the other cancelling equation does not hold. Indeed, we have, for instance, that 

$$
 g(f(-2))=g\left((-2)^2\right)=g(4)=\sqrt{4}=2\neq -2.
$$

So $g$ cannot be the inverse of $f$. The other choice for $g$ does not fare any better, so we are ready to conclude that the function $f$ does not have an inverse. How can we be sure of that, though? In general, failing to show that something is true does not mean that it is not true. Maybe we were just not creative enough. Well, let us take any function $g$ with domain $[0,\infty)$ (the domain of an inverse function should always be the range of the original function). We will show that this function $g$ runs into the same issues as the choices we have made before. Indeed, if $g$ were to be the inverse function of $f$, then since $f(2)=2^2=4$, we would need to have $g(4)=2$. On the other hand, since $f(-2)=(-2)^2=4$, we would also need to have $g(4)=-2$. However, $g(4)$ cannot at the same time be $2$ and $-2$, so such a function $g$ does not exist.

We can also show this visually. Indeed, {prf:ref}`Thm:Inverse:Graphinverse` tells us that the graph of a potential inverse function can be obtained by reflecting the graph of $f$ along the line $x=y$. In the figure below, you see the graph of $f$ and the corresponding reflection. Note that the curve that we obtain this way can never be the graph of function. Indeed, for $x=4$ we see two corresponding values of $y$, namely $y=-2$ and $y=2$, which is not possible if this curve were the graph of a function (it fails the vertical line test {prf:ref}`Thm:Functions1var:VerticalLineTest`).

:::{applet}
:url: calculus/inverse_functions/reflection_of_quadratic_function
:name: Fig:Inverse:SecondEx
:class: dark-light

The functions $f$, the line $y=x$ and the reflection of the graph of $f$ along the line $y=x$.
:::

::::::

{prf:ref}`Ex:Inverse:SecondEx` shows a major issue we have at this point: we lack a quick way of showing that a function does not have an inverse function. If a function has an inverse function, we can (hopefully) find it and prove that it is an inverse function by, for instance, verifying that the cancelling equations hold, but this does not work the other way around. So the goal now is to develop a criterion to check whether a certain function has an inverse function.

The main reason why we could not find an inverse function for the function $f(x)=x^2$ in {prf:ref}`Ex:Inverse:SecondEx` was that $f(2)=f(-2)=4$, so there was no way to determine whether, if $g$ were an inverse of $f$, $g(4)$ should be $2$ or $-2$. In fact, the reason a function $f$ does not have an inverse will **always** be that there are two different points, $a$ and $b$, with $f(a)=f(b)$, since in such a case it is impossible to determine what the inverse should in do in the point $f(a)=f(b)$. Indeed, the reflection of the graph of such a function along the line $x=y$ (which would be the graph of the inverse function if an inverse function exists) can never be the graph of a function, as multiple values of $y$ correspond to the same value of $x$. This idea will allow us to find a criterion to determine invertibility. Before we formulate this, we will introduce some terminology.

::::::{prf:definition}
:label: Def:Inverse:Onetoone

A function $f$ is called **one-to-one** or **injective** if for every two different points $a$ and $b$ in the domain of $f$ we have $f(a)\neq f(b)$. 
::::::

Stated differently, $f$ is one-to-one precisely when it does not take the same value more than once. Visually, we can consider this concept as follows. Consider the horizontal line $y=b$. This line intersects the graph of a function $f$ precisely at points $(x,b)$ with $f(x)=b$. For one-to-one functions, there is at most one such value of $x$, so the horizontal line intersects the graph at most once.

::::::{prf:theorem} Horizontal line test 
:label: Thm:Inverse:Horizontallinetest
A function $f$ is one-to-one precisely when each vertical line $y=b$ intersects the graph of $f$ at most once.
::::::

For a one-to-one function the problem of having a choice which value to assign to a certain number when attempting to find an inverse function can never arise. As such, we finally obtain our desired criterion.

::::::{prf:theorem} 
:label: Thm:Inverse:InverseInjective

Let $f$ be an onto function with domain $D$ and range $R$. Then $f$ has an inverse function (with domain $R$) precisely when $f$ is one-to-one.
::::::

:::{admonition} Proof of {prf:ref}`Thm:Inverse:InverseInjective`
:class: tudproof
Assume that $f$ is one-to-one. Let $y$ in $R$. Since $R$ is the range of $f$, there is at least one $x$ with $f(x)=y$ and since $f$ is one-to-one, there is exactly one such $x$. Then we define $g(y)=x$. By construction, we have $f(g(y))=f(x)=y$, so one of the cancelling equations holds. Now we pick an arbitrary $x$ in $D$ and write $y=f(x)$. Since $x$ is the only number that maps to $y$ (since $f$ is one-to-one) we have $g(y)=x$, so we find $g(f(x))=g(y)=x$. Hence, both cancelling equations hold, which means that $g=f^{-1}$. We conclude that $f$ has an inverse function with domain $R$.

Now we assume that $f$ has an inverse function. Let $a$ and $b$ be different points in the domain of $f$ and suppose that $f(a)=f(b)$. Then we find that

$$
 a=f^{-1}(f(a))=f^{-1}(f(b))=b
$$

Since $a$ and $b$ were assumed to be different, this gives a contradiction. So no such points $a$ and $b$ exist, which means that $f$ must be one-to-one.

:::

::::::{prf:example}
:label: Ex:Inverse:ThirdEx

Consider the function $h(x)=\sqrt{x}$. Then we know that $\sqrt{a}=\sqrt{b}$ precisely when $a=b$, so the function $h$ is one-to-one. By {prf:ref}`Thm:Inverse:InverseInjective` it must have an inverse function. Let us try to find this inverse function. Since we want $h^{-1}(y)=x$ precisely when $h(x)=y$, we write $\sqrt{x}=y$ and try to express $x$ as a function of $y$. From $\sqrt{x}=y$ it quickly follows that $x=y^2$, so the function $k(y)=y^2$ must be the inverse function of $h$. So $h^{-1}(x)=x^2$. 

No wait, that cannot be right, can it? In {prf:ref}`Ex:Inverse:SecondEx` we showed that the function $f(x)=x^2$ did not have an inverse function, so how can it be the inverse function of $h$? The point here is that the functions $f$ and $h^{-1}$ do not have the same domain. For the function $f$ we simply assume it is defined on its maximal domain, which is the real line $\mathbb{R}$. On the other hand, the domain of the inverse function is always equal to the range of the original function. Since the range of $h$ is equal to $[0,\infty)$, this must be the the domain of the function $h^{-1}$. 

Still, why does this difference in domain make that $h^{-1}$ is invertible, while $f$ is not? The reason why $f$ is not invertible is that it is not one-to-one, since for any $x\neq 0$ we have $f(x)=f(-x)$. However, since the domain of $h^{-1}$ does not contain any negative numbers, it does not run into this issue: for each $y$ there is at most one $x\geq 0$ with $x^2=y$. Indeed, the graph of the function $h^{-1}$ is only the right half of the parabola $y=x^2$, so each value of $y$ corresponds to at most one value of $x$. So the function $h^{-1}$ is one-to-one, which is the reason why it does have an inverse function.

:::{applet}
:url: calculus/inverse_functions/reflection_of_square_root_function
:name: Fig:Inverse:ThirdEx
:class: dark-light

The functions $h(x)=\sqrt{x}$ and $q(x)=x^2$ with their full domain, $h^{-1}(x)=x^2$ with domain $[0,\infty)$, and the line $x = y$. Note that we indeed obtain $x^2$ with domain $[0,\infty)$ by reflecting $\sqrt{x}$ along the line $x = y$.
:::

::::::

::::::{prf:remark}
:label: Remark:Inverse:Restrictdomain

As we experienced in {prf:ref}`Ex:Inverse:ThirdEx`, restricting the domain of a function can make it one-to-one, and, therefore, have an inverse function, even if the function does not have an inverse when it is defined on its maximal domain.

Conversely, we know that the domain of the inverse function is always the range of the original function. Hence, it can happen that the domain of the inverse function is not its maximal domain.

::::::

In the preceding examples, we found the inverse function (whenever it exists) by starting with the equation $y=f(x)$ and trying to express $x$ as a function of $y$. This method works in general, so let us present it as an algorithm.

::::::{prf:algorithm} How to find the inverse of a one-to-one function?
:label: Alg:Inverse:FindInverse

Let $f$ be a function that is both onto and one-to-one function. Then the inverse of $f$ can be found as follows.

1. Start with the equation $y=f(x)$;
2. Solve this equation for $x$ (in terms of $y$);
3. Interchange the roles of $x$ and $y$, then we have $y=f^{-1}(x)$.

::::::


::::::{prf:example}
:label: Ex:Inverse:FourthEx

Consider the function $f(x)=x^2-4x=(x-2)^2-4$, defined for $x\leq 2$ with codomain equal to its range, so that it is onto. Then the vertex of the parabola $y=x^2-4x$ is at $x=2$, so the graph of $f$ is the left half of a parabola. Hence, the function $f$ is one-to-one on this domain (note that it is not one-to-one on its maximal domain). We follow the algorithm presented above to find the inverse function of $f$.

We start with the equation $y=f(x)$, i.e. $y=x^2-4x$. We write this equation to $x^2-4x-y=0$, which is a quadratic equation in $x$. As such, we can find the solutions by the quadratic formula or by completing the square and we find

$$
 x=\frac{4\pm\sqrt{(-4)^2-4\cdot1\cdot(-y)}}{2\cdot 1}=2\pm\sqrt{4+y}
$$

Now we wonder whether we should have $x=2+\sqrt{4+y}$ or $x=2-\sqrt{4+y}$. For this, we use that $f$ is only defined for $x\leq 2$, so our choice must ensure that $x\leq 2$. Since a square root is always nonnegative, we must choose $x=2-\sqrt{4+y}$. Now we can interchange the roles of $x$ and $y$, so $y=2-\sqrt{4+x}$, and we find that $f^{-1}(x)=2-\sqrt{4+x}$. 

In order to check that our answer is correct, we first note that the domain of $2-\sqrt{4+x}$ is the interval $[-4,\infty)$, since $\sqrt{4+x}$ is only defined when $4+x\geq 0$, i.e. when $x\geq -4$. This interval is also equal to the range of $f$, since we already noticed that the graph of $f$ is the left half of the parabola $y=x^2-4x$. The lowest value of $y$ on this parabola is at $x=2$, where $y=2^2-4\cdot2=-4$. So indeed, the range of $f$ is also equal to $[-4,\infty)$. Moreover, the cancelling equations hold: for $x\leq 2$ we have

\begin{align*}
 f^{-1}(f(x))&=f^{-1}\left(x^2-4x\right)=2-\sqrt{4+x^2-4x}\\ &=2-\sqrt{(x-2)^2}=2-|x-2|=2-(2-x)=x,
\end{align*}

since $x\leq 2$ implies $|x-2|=2-x$. Similarly, we find for $y\geq -4$ that

\begin{align*}
 f\left(f^{-1}(y)\right)&=f\left(2-\sqrt{4+y}\right)=\left(2-\sqrt{4+y}\right)^2-4\left(2-\sqrt{4+y}\right)\\ &=4-4\sqrt{4+y}+(4+y)-8+4\sqrt{4+y}=y.
\end{align*}

So indeed, the domain of $f^{-1}$ is the range of $f$ and both cancelling equations hold, which means that our answer must be correct.

:::{applet}
:url: calculus/inverse_functions/reflection_of_restricted_polynomial
:name: Fig:Inverse:FourthEx
:class: dark-light

The functions $f$ and $f^{-1}$ and the line $x = y$. Note that we indeed obtain the graph of $f^{-1}$ by reflecting the graph of $f$ along the line $x = y$.
:::

::::::

Since we can determine whether a function has an inverse function by finding out whether it is one-to-one, it is useful to find some conditions on a function which guarantee the function to be one-to-one. It turns out that strictly monotonic functions, i.e. functions that are either strictly increasing or strictly decreasing on their domain, form an important class of one-to-one functions.

::::::{prf:theorem}
:label: Thm:Inverse:MonotonicOnetoone
If an onto function $f$ is strictly monotonic on its domain, then $f$ is one-to-one. In particular, such a function $f$ is invertible. In such a case, the inverse function is strictly monotonic as well.

::::::

:::{admonition} Proof of {prf:ref}`Thm:Inverse:MonotonicOnetoone`
:class: tudproof
Suppose first that $f$ is strictly increasing on its domain. Then $f(x_1)<f(x_2)$ for any $x_1<x_2$, but that immediately means that $f$ does not take on the same function value more than once, since $f(x_1)<f(x_2)$ implies $f(x_1)\neq f(x_2)$. So $f$ must be one-to-one, which means that it must have an inverse function. Now, let $y_1$ and $y_2$ in the domain of $f^{-1}$ with $y_1<y_2$ and write $x_1=f^{-1}(y_1)$ and $x_2=f^{-1}(y_2)$. Then we cannot have $x_1\geq x_2$, since $x_1>x_2$ would imply $y_1=f(x_1)>f(x_2)=y_2$, while $x_1=x_2$ would imply $y_1=f(x_1)=f(x_2)=y_2$. Hence, we must have $x_1<x_2$, which means $f^{-1}(y_1)<f^{-1}(y_2)$, which means that $f^{-1}$ is strictly increasing as well.

The case when $f$ is strictly decreasing is similar.
:::

::::::{note}
:name: Note:Inverse:Monotonicnotnecessary

{prf:ref}`Thm:Inverse:MonotonicOnetoone` states that strictly monotonic functions are always one-to-one and, therefore, always have an inverse function. However, there are functions which are one-to-one, but not strictly monotonic. Consider, for instance, the function $f(x)=\dfrac{1}{x}$. Since $\dfrac{1}{x_1}\neq \dfrac{1}{x_2}$ when $x_1\neq x_2$, the function $f$ is one-to-one. However, it is not strictly monotonic on its domain. It is not strictly decreasing, since $f(-1)=\dfrac{1}{-1}=-1$, while $f(1)=\dfrac{1}{1}=1>f(-1)$, but also not strictly increasing, since $f(1)=1$, while $f(2)=\dfrac{1}{2}<f(1)$. 

::::::

::::{question}
:type: multiple-choice
:variant: multiple-select
:admonition:
:class: question
:showanswer:
:columns: 1

Which of these functions is/are equal to its own inverse function?
---
[x] $f(x)=\pi-x$ with domain $\mathbb{R}$.
> The equation $y=\pi-x$ gives $x=\pi-y$. This means that this function is invertible and the inverse function is $f^{-1}(x)=\pi-x$. In addition, the range of the original function $f$ is $\mathbb{R}$. So $f$ is its own inverse function.
:::{applet}
:url: calculus/inverse_functions/polling_question_A
:name: Fig:Inverse:Selfinverse:A
:class: dark-light
The graph of the function $f(x)=\pi-x$ and the line $x=y$.
:::
[ ] $f(x)=2x$ with domain $\mathbb{R}$.
> The equation $y=2x$ gives $x=\dfrac{y}{2}$. This means that this function is invertible, but its inverse is $f^{-1}(x)=\dfrac{x}{2}$. So this function is not its own inverse function.
:::{applet}
:url: calculus/inverse_functions/polling_question_B
:name: Fig:Inverse:Selfinverse:B
:class: dark-light
The graph of the function $f(x)=2x$, its reflection across the line $x=y$, and the line $x=y$.
:::
[x] $f(x)=\dfrac{1}{x}$ with domain $(0,\infty)$.
> The equation $y=\dfrac{1}{x}$ gives $x=\dfrac{1}{y}$. This means that this function is invertible and the inverse function is $f^{-1}(x)=\dfrac{1}{x}$. In addition, the range of the original function $f$ is $(0,\infty)$. So $f$ is its own inverse function.
:::{applet}
:url: calculus/inverse_functions/polling_question_C
:name: Fig:Inverse:Selfinverse:C
:class: dark-light
The graph of the function $f(x)=\dfrac{1}{x}$ on $(0,\infty)$ and the line $x=y$.
:::
[ ] $f(x)=\dfrac{-1}{x}$ with domain $(0,\infty)$.
> The equation $y=\dfrac{-1}{x}$ gives $x=\dfrac{-1}{y}$. This means that this function is invertible and the inverse function is $f^{-1}(x)=\dfrac{-1}{x}$. However, the range of the original function is $(-\infty,0)$, which is the domain of the inverse function. So the inverse function is defined by the same formula as the original function, but their domains are different, so they are not the same functions.
:::{applet}
:url: calculus/inverse_functions/polling_question_D
:name: Fig:Inverse:Selfinverse:D
:class: dark-light
The graph of the function $f(x)=\dfrac{-1}{x}$ on $(0,\infty)$, its reflection across the line $x=y$, and the line $x=y$.
:::
[ ] $f(x)=1$ with domain $\mathbb{R}$.
> The equation $y=1$ cannot be solved for $x$. Indeed, the function $f$ is not one-to-one, as all values of $x$ are mapped to the same number $1$. So this function does not have an inverse function.
:::{applet}
:url: calculus/inverse_functions/polling_question_E
:name: Fig:Inverse:Selfinverse:E
:class: dark-light
The graph of the function $f(x)=1$, its reflection across the line $x=y$, and the line $x=y$.
:::
[x] $f(x)=\sqrt{1-x^2}$ with domain $[0,1]$.
> The equation $y=\sqrt{1-x^2}$ gives $y^2=1-x^2$, which means $x=\pm\sqrt{1-y^2}$. Since the domain of the function in $[0,1]$, we know that any input $x$ is nonnegative, so we need the positive square root. So for $x$ in the domain of $f$ we have $y=\sqrt{1-x^2}$ precisely when $x=\sqrt{1-y^2}$. This means that this function is invertible and the inverse function is $f^{-1}(x)=\sqrt{1-x^2}$. In addition, the range of the original function $f$ is $[0,1]$. So $f$ is its own inverse function.
:::{applet}
:url: calculus/inverse_functions/polling_question_F
:name: Fig:Inverse:Selfinverse:F
:class: dark-light
The graph of the function $f(x)=\sqrt{1-x^2}$ on $[0,1]$ and the line $x=y$.
:::
---
*Note*: a function which is its own inverse function is called a **self-inverse** function.
::::

So far, we have not put emphasis on the codomain of a function in relation to invertibility. However, if the range of the function is not equal to the codomain, i.e. if the function is not onto, the equation $f(x)=y$ does not have a solution $x$ for each $y$ in the codomain of $f$ (it only has a solution for $y$ in the range of $f$). So a function can only have an inverse function if the range and the codomain coincide. This is not a real problem in practice though, since we can always change the codomain of the function to be equal to the range, without changing the behaviour of the function. First, we introduce some terminology and then reformulate these considerations into a theorem.

::::::{prf:definition}
:label: Def:Inverse:Bijective
A function $f$ is called **bijective** whenever it is both one-to-one and onto.
::::::

::::::{prf:theorem}
:label: Thm:Inverse:Onto
A function $f$ is invertible precisely when it is bijective. If it is only one-to-one, it can be made invertible by restricting the codomain to be equal to the range.

::::::

::::::{prf:example}
:label: Ex:Inverse:Onto
Consider the function $h(x)=\sqrt{x}$ with domain $[0,\infty)$ and codomain $\mathbb{R}$. Since $\sqrt{x}\geq 0$ for all $x\geq 0$, the range of $f$ cannot coincide with the codomain $\mathbb{R}$. Indeed, the equation $\sqrt{x}=-1$ does not have any solutions for $x\geq 0$. So, this function is not invertible when $\mathbb{R}$ is the codomain. However, in {prf:ref}`Ex:Inverse:ThirdEx` we saw that this function is one-to-one. So, if we restrict the codomain of $h$ to be equal to the range of $h$, which is the interval $[0,\infty)$, it becomes invertible as we saw in this previous example.

::::::



(Subsec:InverseLog)=

## Logarithms

In {numref}`Section:FunctionsIntro` we considered functions of the form $f(x)=b^x$ for $b\geq 0$. In {prf:ref}`Thm:PropertiesFunctions:Expnondecreasenonincrease` we saw that such a function is strictly decreasing for $0<b<1$, while it is strictly increasing for $b>1$. From {prf:ref}`Thm:Inverse:MonotonicOnetoone` we find that for these values of $b$ the function $f(x)=b^x$ is invertible.

::::::{prf:definition}
:label: Thm:Inverse:Logarithm
Let $b>0$ with $b\neq 1$ and consider the function $f(x)=b^x$. Then the inverse function of $f$ is called the **logarithmic function with base $b$** and is denoted by $f^{-1}(x)=\log_b(x)$. 

In the special case when $b=e$, we write $\log_e(x)=\ln(x)$ and we call this function the **natural logarithmic function** or the **Napierian logarithmic function** (named after the Scottish mathematician [John Napier (1550-1617)](https://en.wikipedia.org/wiki/John_Napier)). In the special case when $b=10$, we call this function the **common logarithm** or **Briggsian logarithm** (named after the English mathematician [Henry Briggs (1561-1630)](https://en.wikipedia.org/wiki/Henry_Briggs_(mathematician))).
::::::

::::{note}
:name: Note:Inverse:Base10log

In some literature, the notation $\log(x)$ (so without a subscript) is used for the common logarithm $\log_{10}(x)$. In other literature, this same notation is used for the natural logarithm $\ln(x)=\log_e(x)$. To avoid confusion, we will not use this notation. If you use this notation in the Grasple exercises, it will be interpreted as the common logarithm.
::::

Logarithms are so commonly used that they are usually considered standard functions, in the same vein as polynomials, trigonometric functions or exponential functions. 

Using the definition of the inverse function, we find that $y=\log_b(x)$ precisely when $b^y=x$. So the logarithm is a way to "undo" exponentiation.

::::::{note}
:name: Note:Inverse:Cancellinglogarthmexp

Since a logarithmic function is defined as the inverse function of an exponential function, the cancelling equations must hold for these functions. That is, for $x$ in $\mathbb{R}$ and $y>0$ we have

$$
 \log_b\left(b^x\right)=x,\qquad b^{\log_b(y)}=y
$$

::::::

::::::{prf:example}
:label: Ex:Inverse:Logarithmbasisbasis
Suppose we want to evaluate $\log_2(8)$. Writing $y=\log_2(8)$, this means that we try to find a number $y$ with $2^y=8$. Fortunately, we know that $2^3=8$, so we find that $\log_2(8)=3$.
::::::

Let us first analyse the behaviour of logarithmic functions. Since the graph of an inverse function can be obtained by reflecting the graph of the original function along the line $y=x$, we can use our knowledge of the graphs of exponential functions to sketch the graphs of logarithmic functions.

:::::{grid} 2
:gutter: 1
:class-container: full-width

::::{grid-item}

:::{applet}
:url: calculus/inverse_functions/reflection_of_exponential_with_base_2
:name: Fig:Inverse:LogarithmbasisbasisLeft
:class: dark-light

The functions $f(x)=2^x$ and $f^{-1}(x)=\log_2(x)$ and the line $x = y$.
:::

::::

::::{grid-item}

:::{applet}
:url: calculus/inverse_functions/reflection_of_exponential_with_base_1_over_2
:name: Fig:Inverse:LogarithmbasisbasisRight
:class: dark-light

 The functions $f(x)=\left(\frac{1}{2}\right)^x$ and $f^{-1}(x)=\log_{\frac{1}{2}}(x)$ and the line $x = y$.
:::

::::
:::::

First we note that the logarithm is only defined for $x>0$. This makes sense since the domain of an inverse function is equal to the range of the original function, which for the function $b^x$ is equal to $(0,\infty)$. Next, we recall that the logarithm $\log_b(x)$ is strictly increasing when $b>1$ while it is strictly decreasing if $0<b<1$. This follows from {prf:ref}`Thm:Inverse:MonotonicOnetoone`, since the function $b^x$ has the same properties. Finally, we notice that for $0<b<1$ the function values $\log_b(x)$ blow up as $x$ gets closer to $0$. In the terminology that we will introduce in {numref}`Section:LimitPoint` the logarithm has a vertical asymptote at $x=0$. This is because the graph of the logarithm is obtained by reflecting the graph of $b^x$ along the line $y=x$, and this function has the property that the function values get arbitrarily close to $0$ as $x$ gets very large (in the terminology of {numref}`Section:Limitinf`, the function $b^x$ has a horizontal asymptote at $y=0$). For $b>1$, the logarithm has a similar property, but the function values will, instead, blow up in the negative direction as $x$ approaches $0$.




Since we know many computation rules for exponential functions, we can carry these over to logarithms.

::::::{prf:theorem}
:label: Thm:Inverse:Logarithmcomputationrules
Let $b>0$ with $b\neq 1$. Then for $x>0$, $y>0$ and a real number $p$ we have

- $\log_b(xy)=\log_b(x)+\log_b(y)$
- $\log_b\left(\frac{x}{y}\right)=\log_b(x)-\log_b(y)$
- $\log_b\left(x^p\right)=p\log_b(x)$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Inverse:Logarithmcomputationrules`
:class: tudproof
Since a logarithm is the inverse function of an exponential function, we find that $\log_b(xy)$ is the unique number $z$ with $b^z=xy$. We will show that $\log_b(x)+\log_b(y)$ also has this property. Indeed, we find, using the standard computation rules for exponential functions, that

$$
 b^{\log_b(x)+\log_b(y)}=b^{\log_b(x)}b^{\log_b(y)}=xy,
$$

using the cancelling equations for the logarithm and the exponential function. As such, $z=\log_b(x)+\log_b(y)$ also satisfies $b^z=xy$, so we must have $\log_b(xy)=\log_b(x)+\log_b(y)$.

We first prove the third property, since the second follows from combining the first and the third. As before, $\log_b\left(x^p\right)$ is the unique number $z$ with $b^z=x^p$. Using the standard computation rules for exponential functions, we find

$$
 b^{p\log_b(x)}=\left(b^{\log_b(x)}\right)^p=x^p.
$$

Hence, $z=p\log_b(x)$ also satisfies $b^z=x^p$, so we must have $\log_b\left(x^p\right)=p\log_b(x)$.

To prove the second property, we rewrite and use the first and third properties to find

\begin{align*}
 \log_b\left(\frac{x}{y}\right)&=\log_b\left(x\frac{1}{y}\right)=\log_b(x)+\log_b\left(\frac{1}{y}\right)\\ &=\log_b(x)+\log_b\left(y^{-1}\right)=\log_b(x)-\log_b(y).
\end{align*}

:::

::::::{prf:example}
:label: Ex:Inverse:Logarithmbasiccomputation
Suppose we want to simplify the expression $\ln\left(\frac{x^3}{(x+2)\sqrt{1+x}}\right)$ (recall that $\ln(x)=\log_e(x)$ is the natural logarithm, i.e. the logarithm with base number $e$). Using the rules from {prf:ref}`Thm:Inverse:Logarithmcomputationrules` we find that

$$
 \begin{array}{lcl}\ln\left(\frac{x^3}{(x+2)\sqrt{1+x}}\right)&=&\ln\left(x^3\right)-\ln\left((x+2)\sqrt{1+x}\right)\\
 &=&\ln\left(x^3\right)-\ln\left(x+2\right)-\ln\left(\sqrt{1+x}\right)\\ &=&3\ln(x)-\ln\left(x+2\right)-\ln\left(\left(1+x\right)^{\frac{1}{2}}\right)\\ &=&3\ln(x)-\ln\left(x+2\right)-\frac{1}{2}\ln\left(1+x\right). \end{array}
$$

Note that we cannot simplify this expression any further, since there are no rules to simplify an expression of the form $\ln(a+b)$.
::::::

::::::{prf:example}
:label: Ex:Inverse:Logarithmbasicsolving
Suppose we want to solve the equation $2^{x-3}=5$. Since $\log_2(x)$ is the inverse function of $2^x$ we find that $2^{x-3}=5$ precisely when $x-3=\log_2(5)$. Alternatively, we can find this equation by taking the $\log_2$ of both sides of the equation $2^{x-3}=5$. Since $x-3=\log_2(5)$ we find $x=3+\log_2(5)$, which cannot be simplified any further. Using a calculator, we find $3+\log_2(5)\approx 5.4219\ldots$.
::::::

Actually, the base of the logarithm does not play as important a role as you might be tempted to think at first. For example, consider the two numbers $x=\log_2(64)$ and $y=\log_8(64)$. Then $x$ is the unique number with $2^x=64$, while $y$ is the unique number with $8^y=64$. Now we notice that

$$
 64=8^y=\left(2^3\right)^y=2^{3y}
$$

which must mean that $3y=x$. Of course, we knew this already, since the unique solution of $2^x=64$ is $x=6$, while the unique solution of $8^y=64$ is $y=2$ and we indeed have $3\cdot 2=6$. However, this calculation works more generally, since for $z>0$ we have

$$
 z=8^{\log_8(z)}=\left(2^3\right)^{\log_8(z)}=2^{3\log_8(z)}
$$

which must mean that $\log_2(z)=3\log_8(z)$. So for the functions $f(x)=\log_2(x)$ and $g(x)=\log_8(x)$ we find $f=3g$, so the one logarithm is a constant multiple of the other. Now, where does this number $3$ come from? Well, in the computation above we note that it comes from the fact that $8=2^3$. This equation can be written to $3=\log_2(8)$. So, in fact, we find that for all $x>0$ we have

$$
 \log_2(x)=\log_2(8)\log_8(x)
$$

The general version of this result is as follows.

::::::{prf:theorem} Change of base in a logarithm
:label: Thm:Inverse:Logarithmbasechange
Consider two numbers $a>0$ and $b>0$ with $a\neq1$ and $b\neq 1$. Then, for all $x>0$ we have

$$
 \log_b(x)=\log_b(a)\log_a(x).
$$

As a consequence, each logarithm can be expressed in terms of the natural logarithm by writing

$$
 \log_a(x)=\frac{\ln(x)}{\ln(a)}.
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Inverse:Logarithmbasechange`
:class: tudproof
We write $y=\log_a(x)$. Then $y$ is the unique number with $a^y=x$. Then we must have

$$
 \log_b(x)=\log_b\left(a^y\right)=y\log_b(a)=\log_a(x)\log_b(a),
$$

as desired. The consequence directly follows by taking $b=e$.

:::

::::{question}
:type: multiple-choice
:variant: single-select
:admonition:
:class: question
:showanswer:
:columns: 1

Using that $2^{10}=1024$, which of the following numbers is closest to $\log_2\left(1\,000\,000\,000\,000\right)$?
---
[ ] $12$
> Hint: Write $1\,000\,000\,000\,000$ as a power of $1000$ and write $2^{10}=1024$ as a logarithm.
[x] $40$
> We have $1\,000\,000\,000\,000=(1000)^4$, so using the rule of calculation for logarithms we find

$$
 \log_2\left(1\,000\,000\,000\,000\right)=\log_2\left(1000^4\right)=4\log_2\left(1000\right).
$$

Now, $2^{10}=1024$ precisely means that $\log_2(1024)=10$. So $\log_2\left(1000\right)$ will be close to $10$, which means that $\log_2\left(1\,000\,000\,000\,000\right)=4\log_2\left(1000\right)$ will be close to $40$.
[ ] $1000$
> Hint: Write $1\,000\,000\,000\,000$ as a power of $1000$ and write $2^{10}=1024$ as a logarithm.
[ ] $10\,000$
> Hint: Write $1\,000\,000\,000\,000$ as a power of $1000$ and write $2^{10}=1024$ as a logarithm.
---
::::

(Subsec:InverseTrig)=

## Inverse trigonometric functions

When trying to find inverses of the common trigonometric functions (sine, cosine and tangent) we run into the ever so slight problem that these functions are not one-to-one, so they do not have an inverse function. Indeed, for any value of $x$ we have $\sin(x)=\sin(x+2\pi)$, $\cos(x)=\cos(x+2\pi)$ and $\tan(x)=\tan\left(x+\pi\right)$ (the latter one assuming $\tan(x)$ exists for this value of $x$), so these functions definitely take on function values more than once. In fact, each number in the range is taken on infinitely often by each of these three functions. Fortunately, we have noticed before in {prf:ref}`Remark:Inverse:Restrictdomain` that we can restrict the domain of a function to make it invertible. 

So which part of the domain should we choose? Well, we want to make sure that we do not lose too much behaviour of the function, so at the very least we want to ensure that the range does not change, so that we do not suddenly go from $\sin(x)=y$ having infinitely many solutions to the same equation having no solutions in the restricted domain. Moreover, for values of $x$ close to $0$ we have the geometric interpretation of $x$ as an angle, so it makes sense to include $0$ in the restricted domains.

Let us start with $f(x)=\sin(x)$. We want to choose an interval as our domain that includes $0$, such that $f$ is one-to-one on this interval and that the range remains $[-1,1]$. For this, we actually only have one single choice: we restrict the domain to the interval $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$. Indeed, the geometrical interpretation of the sine (see {numref}`Fig:Trigonometry:LawOfSines`) tells us that for $-\frac{\pi}{2}\leq x\leq\frac{\pi}{2}$ the function $\sin(x)$ takes on each value between $-1$ and $1$ exactly once. This can also be seen in the graph of the function.

:::::{grid} 2
:gutter: 1
:class-container: full-width

::::{grid-item}

:::{applet}
:url: calculus/inverse_functions/graph_of_sine_function
:name: Fig:Inverse:RestrictSinLeft
:class: dark-light

The function $f(x)=\sin(x)$.
:::

::::

::::{grid-item}

:::{applet}
:url: calculus/inverse_functions/graph_of_restricted_sine_function
:name: Fig:Inverse:RestrictSinRight
:class: dark-light

The function $f(x)=\sin(x)$ restricted to the interval $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$.
:::

::::
:::::

Now we turn our attention to $f(x)=\cos(x)$. Again, we want to choose an interval as our domain that includes $0$, such that $f$ is one-to-one on this interval and that the range remains $[-1,1]$. However, the interval $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$ does not work in this case, since 1) $f$ is not one-to-one on this interval, because, for instance, $\cos\left(\frac{\pi}{4}\right)=\cos\left(-\frac{\pi}{4}\right)$ and 2) the range changes when we restrict to this interval, since for $-\frac{\pi}{2}\leq x\leq\frac{\pi}{2}$ we have $\cos(x)\geq 0$. So we should choose something different. Keeping the geometric interpretation of the cosine in mind, there are actually two choices that work: the intervals $[-\pi,0]$ and $[0,\pi]$. For convenience, we choose the interval $[0,\pi]$, since it is a little nicer to work with positive input values than with negative ones. We can see that this choice works in the graph of the function.

:::::{grid} 2
:gutter: 1
:class-container: full-width

::::{grid-item}
:::{applet}
:url: calculus/inverse_functions/graph_of_cosine_function
:name: Fig:Inverse:RestrictCosLeft
:class: dark-light

The function $f(x)=\cos(x)$.
:::

::::

::::{grid-item}
:::{applet}
:url: calculus/inverse_functions/graph_of_restricted_cosine_function
:name: Fig:Inverse:RestrictCosRight
:class: dark-light

The function $f(x)=\cos(x)$ restricted to the interval $\left[0,\pi\right]$.
:::
::::
:::::

Finally, we consider $f(x)=\tan(x)$. Here the range is actually the entire real line $\mathbb{R}$, so want to make sure we cover the entire range. As was the case with the sine, there is only one choice for an interval that includes $0$, such that $f$ is one-to-one on this interval and that the range remains $\mathbb{R}$ and that choice is the open interval $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$. As before, we can see that this choice works in the graph of the function.

:::::{grid} 2
:gutter: 1
:class-container: full-width

::::{grid-item}

:::{applet}
:url: calculus/inverse_functions/graph_of_tangent_function
:name: Fig:Inverse:RestrictTanLeft
:class: dark-light

The function $f(x)=\tan(x)$.
:::
::::

::::{grid-item}

:::{applet}
:url: calculus/inverse_functions/graph_of_restricted_tangent_function
:name: Fig:Inverse:RestrictTanRight
:class: dark-light

The function $f(x)=\tan(x)$ restricted to the interval $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$.
:::
::::
:::::

Since we have now found intervals on which the trigonometric functions are one-to-one, we can define their inverse functions.

::::::{prf:definition} Inverse trigonometric functions
:label: Def:Inverse:Inversetrig
The inverse of the function $\sin(x)$, restricted to the interval $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$, is called the **arcsine function** or **inverse sine function** and is denoted by $\arcsin(x)$. That is, we have $x=\arcsin(y)$ precisely when $\sin(x)=y$ for $-\frac{\pi}{2}\leq x\leq \frac{\pi}{2}$ and $-1\leq y\leq 1$.

The inverse of the function $\cos(x)$, restricted to the interval $\left[0,\pi\right]$, is called the **arccosine function** or **inverse cosine function** and is denoted by $\arccos(x)$. That is, we have $x=\arccos(y)$ precisely when $\cos(x)=y$ for $0\leq x\leq \pi$ and $-1\leq y\leq 1$.

The inverse of the function $\tan(x)$, restricted to the interval $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$, is called the **arctangent function** or **inverse tangent function** and is denoted by $\arctan(x)$. That is, we have $x=\arctan(y)$ precisely when $\tan(x)=y$ for $-\frac{\pi}{2}<x< \frac{\pi}{2}$ and $y$ in $\mathbb{R}$.
::::::

::::::{prf:notation} 
:label: Notation:Inverse:Inversetrig

In some literature (and most calculators), the notations $\sin^{-1}(x)$, $\cos^{-1}(x)$ and $\tan^{-1}(x)$ are used to denote $\arcsin(x)$, $\arccos(x)$ and $\arctan(x)$ respectively. Since it is very easy to mistakenly read $\sin^{-1}(x)$ as $\dfrac{1}{\sin(x)}$, while these are very different functions, we will avoid these notations like the plague.
::::::

Since the graph of an inverse function is obtained by reflecting the graph of the original function along the line $y=x$, we can quickly sketch the graphs of the inverse trigonometric functions.

::::::{grid} 2
:gutter: 1
:class-container: full-width

::::{grid-item}

:::{applet}
:url: calculus/inverse_functions/reflection_of_sine_function
:name: Fig:Inverse:InversetrigSin
:class: dark-light

The function $\sin(x)$ and its inverse $\arcsin(x)$ and the line $x = y$.
:::

::::

::::{grid-item}
:::{applet}
:url: calculus/inverse_functions/reflection_of_cosine_function
:name: Fig:Inverse:InversetrigCos
:class: dark-light

The function $\cos(x)$ and its inverse $\arccos(x)$ and the line $x = y$.
:::

::::

::::{grid-item}
:columns: 12

:::{applet}
:url: calculus/inverse_functions/reflection_of_tangent_function
:name: Fig:Inverse:InversetrigTan
:class: dark-light

The function $\tan(x)$ and its inverse $\arctan(x)$ and the line $x = y$.
:::
::::
::::::

::::{question}
:type: multiple-choice
:variant: single-select
:admonition:
:class: question
:showanswer:
:columns: 1

Consider the cotangent function $\cot(x)=\frac{\cos(x)}{\sin(x)}$. How would you restrict its domain to make it one-to-one?
---
[x] $(0,\pi)$.
> Note that for $0<x<\pi$ with $x\neq \frac{\pi}{2}$ we have $\cot(x)=\frac{\cos(x)}{\sin(x)}=\frac{1}{\tan(x)}$. Now we know that the tangent is strictly increasing on the intervals $\left(0,\frac{\pi}{2}\right)$ and $\left(\frac{\pi}{2},\pi\right)$. In addition, the tangent is positive on the first of these intervals and negative on the second one. That means that the cotangent is strictly decreasing on both intervals $\left(0,\frac{\pi}{2}\right)$ and $\left(\frac{\pi}{2},\pi\right)$ and that it is positive on the first of the intervals and negative on the second of these intervals. So the cotangent does not take the same value twice on the union of the intervals $\left(0,\frac{\pi}{2}\right)$ and $\left(\frac{\pi}{2},\pi\right)$. Finally, we note that $\cot\left(\frac{\pi}{2}\right)=\frac{\cos\left(\frac{\pi}{2}\right)}{\sin\left(\frac{\pi}{2}\right)}=\frac{0}{1}=0$. So we conclude that the cotangent never takes the same value twice on the full interval $(0,\pi)$, so it is one-to-one on this interval. In particular, we could use this interval to define the inverse cotangent function, the arccotangent $\operatorname{arccot}(x)$.

:::{applet}
:url: calculus/inverse_functions/graph_of_cotangent_function
:name: Fig:Inverse:InversetrigCot
:class: dark-light
The graph of the cotangent function $\cot(x)=\frac{\cos(x)}{\sin(x)}$.
:::

[ ] $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$.
> Note that $0$ is not in the domain of the cotangent, since $\sin(0)=0$ and we cannot divide by $0$. So any interval which contains $0$ cannot be the correct answer.
[ ] $[0,\pi]$.
> Note that $0$ is not in the domain of the cotangent, since $\sin(0)=0$ and we cannot divide by $0$. So any interval which contains $0$ cannot be the correct answer.
[ ] $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$.
> Note that $0$ is not in the domain of the cotangent, since $\sin(0)=0$ and we cannot divide by $0$. So any interval which contains $0$ cannot be the correct answer.
---
::::

::::::{prf:example} 
:label: Ex:Inverse:Inversetrig1
Suppose we want to simplify $\arcsin\left(-\frac{1}{2}\right)$. Writing $y=\arcsin\left(-\frac{1}{2}\right)$, we find that $y$ is the unique number with $-\frac{\pi}{2}\leq y\leq\frac{\pi}{2}$ and $\sin(y)=-\frac{1}{2}$ (notice that this means that we can interpret $y$ as an angle). Using the standard values for the sine function, we must have $y=-\frac{\pi}{6}$. So we find $\arcsin\left(-\frac{1}{2}\right)=-\frac{\pi}{6}$

::::::

The cancelling equations for the (inverse) trigonometric functions now become

$$
 \begin{array}{lcll} \arcsin(\sin(x))&=&x,\quad &\text{for}\,-\frac{\pi}{2}\leq x\leq\frac{\pi}{2}\\
 \sin(\arcsin(y))&=&y,\quad &\text{for}\,-1\leq y\leq1\\ \arccos(\cos(x))&=&x,\quad &\text{for}\,0\leq x\leq\pi\\
 \cos(\arccos(y))&=&y,\quad &\text{for}\,-1\leq y\leq1\\ \arctan(\tan(x))&=&x,\quad &\text{for}\,-\frac{\pi}{2}< x<\frac{\pi}{2}\\
 \tan(\arctan(y))&=&y,\quad &\text{for}\,y\,\text{in}\,\mathbb{R} \end{array}
$$

::::::{warning} 
:name: Warning:Inverse:Inversetrigcancelling

The cancelling equations for the (inverse) trigonometric functions **only** hold on the intervals stated above. 
::::::

::::::{prf:example} 
:label: Ex:Inverse:Inversetrig2
Suppose we want to simplify $\displaystyle\arctan\left(\tan\left(\frac{5\pi}{4}\right)\right)$. Although it is very tempting to think to think that the answer should be $\displaystyle\frac{5\pi}{4}$, this is not correct. Indeed, the arctangent only outputs values between $\displaystyle-\frac{\pi}{2}$ and $\displaystyle\frac{\pi}{2}$, so it can never output $\displaystyle\frac{5\pi}{4}$. In order to find the correct value, we notice that the tangent is periodic with fundamental period $\pi$, so we can compute

$$
 \arctan\left(\tan\left(\frac{5\pi}{4}\right)\right)=\arctan\left(\tan\left(\frac{5\pi}{4}-\pi\right)\right)=\arctan\left(\tan\left(\frac{\pi}{4}\right)\right).
$$

Notice that $\dfrac{\pi}{4}$ is in between $-\dfrac{\pi}{2}$ and $\dfrac{\pi}{2}$ so the cancelling equations are valid there. As such, we find

$$ 
 \arctan\left(\tan\left(\frac{5\pi}{4}\right)\right)=\arctan\left(\tan\left(\frac{\pi}{4}\right)\right)=\frac{\pi}{4}.
$$

::::::

::::::{prf:example} 
:label: Ex:Inverse:Inversetrig3
Suppose we want to simplify $\displaystyle\arcsin\left(\sin\left(\frac{11\pi}{12}\right)\right)$. Not falling in the same trap that was pointed out in {prf:ref}`Ex:Inverse:Inversetrig2`, we already know that the answer is definitely not going to be $\dfrac{11\pi}{12}$. However, the method we used in {prf:ref}`Ex:Inverse:Inversetrig2` does not work here. Indeed, the fundamental period of the sine is $2\pi$ and if we subtract $2\pi$ from $\dfrac{11\pi}{12}$, we obtain $-\dfrac{13\pi}{12}$, which is still not in the region where the cancelling equations hold. Instead, we can use another property of the sine. Indeed, {prf:ref}`Thm:Trigonometry:SupplementaryAngles` tells us that $\sin\left(\pi-\theta\right)=\sin(\theta)$ for any angle $\theta$. This identity can be used to get us into the region where the cancelling equations hold. Indeed, we obtain that 

$$
 \sin\left(\frac{11\pi}{12}\right)=\sin\left(\pi-\frac{11\pi}{12}\right)=\sin\left(\frac{\pi}{12}\right)
$$

and $\dfrac{\pi}{12}$ is in the region where the cancelling equations hold. Hence, we obtain

$$
 \arcsin\left(\sin\left(\frac{11\pi}{12}\right)\right)=\arcsin\left(\sin\left(\frac{\pi}{12}\right)\right)=\frac{\pi}{12}.
$$

::::::

Finally, we study expressions like $\cos(\arcsin(x))$. It turns out that these type of expressions can often be simplified into an expression that does not involve any inverse trigonometric functions. In the following example, we will show two different methods of approaching these types of problems.

::::::{prf:example} 
:label: Ex:Inverse:InversetrigSimplify

Suppose we want to simplify $\displaystyle\cos(\arcsin(x))$. Writing $y=\arcsin(x)$ we note that $y$ takes the role of an angle. Indeed, it is the unique angle with $-\frac{\pi}{2}\leq y\leq \frac{\pi}{2}$ and $\sin(y)=x$. We will use two methods to simplify the expression, the first of which uses a geometrical approach, while the second one uses trigonometric identities.

**Method 1 (using geometrical arguments)**

Since $y$ takes the role of an angle, we make use of that. Assume, for now that $0<y<\frac{\pi}{2}$. Then we can draw a right triangle where one of the angles is $y$, see {numref}`Fig:Inverse:Simplify1`.

:::{applet}
:url: calculus/inverse_functions/right-angled_triangle
:name: Fig:Inverse:Simplify1
:class: dark-light

Initial triangle with sides $a$, $b$, $c$ and angle $y$ indicated.

:::
:::::

We write $a$ for the side of the triangle opposite to the angle $y$, $b$ for the adjacent side and $c$ for the hypotenuse. Since we know that $\sin(y)=x$, the geometrical definition of the sine gives that

$$
 x=\sin(y)=\frac{a}{c}.
$$

So we know that the ratio between $a$ and $c$ must be $x$, but we still have some freedom in how we choose them. Indeed, we can scale the triangle without changing the angles and all of these triangles are valid representations of the current situation. For convenience, we set $c=1$, but there are other choices possible that, in the end, give the same result. This means that $a=c\cdot x=1\cdot x=x$. Because of all the talk about triangles, you might have almost forgotten by now that the goal was to simplify $\cos(\arcsin(x))=\cos(y)$. Fortunately, we can also use the geometrical interpretation of the cosine to find

$$
 \cos(y)=\frac{b}{c}=\frac{b}{1}=b.
$$

So how do we find the adjacent side $b$? By using the Pythagorean theorem, of course (you thought you were reading a book on advanced mathematics, but really, we are just doing Pythagoras here). As such, we must have $b=\sqrt{c^2-a^2}=\sqrt{1-x^2}$, see {numref}`Fig:Inverse:Simplify2`.

::::{applet}
:url: calculus/inverse_functions/right-angled_triangle_for_cosine_of_arcsine_of_x
:name: Fig:Inverse:Simplify2
:class: dark-light

Final triangle with sides $x$, $\sqrt{1-x^2}$, $1$ and angle $y$ indicated.

::::

 We conclude that

$$
 \cos(\arcsin(x))=\cos(y)=b=\sqrt{1-x^2}.
$$

Now what happens if $-\frac{\pi}{2}< y<0$? In that case, the triangle we drew does not make as much sense, but, fortunately, we have already done the hard work. Notice that in that case $0<-y<\frac{\pi}{2}$ and $\sin(-y)=-\sin(y)=-x$, so $-y=\arcsin(-x)$, so by the previous computation we have $\cos(-y)=\cos(\arcsin(-x))=\sqrt{1-(-x)^2}$. As such, we must have

$$
 \cos(\arcsin(x))=\cos(y)=\cos(-y)=\sqrt{1-(-x)^2}=\sqrt{1-x^2}.
$$

All that remains are the cases $y=-\frac{\pi}{2}$, $y=0$ and $y=\frac{\pi}{2}$. 

If $y=-\frac{\pi}{2}$ then $x=-1$, since $x=\sin\left(-\frac{\pi}{2}\right)=-1$. In that case $\cos(\arcsin(x))=\cos(\arcsin(-1))=\cos\left(-\frac{\pi}{2}\right)=0=\sqrt{1-(-1)^2}=\sqrt{1-x^2}$. 

If $y=0$ then $x=0$, since $x=\sin(0)=0$. In that case $\cos(\arcsin(x))=\cos(\arcsin(0))=\cos(0)=1=\sqrt{1-0^2}=\sqrt{1-x^2}$. 

Finally, if $y=\frac{\pi}{2}$ then $x=1$, since $x=\sin\left(\frac{\pi}{2}\right)=-1$. In that case $\cos(\arcsin(x))=\cos(\arcsin(1))=\cos\left(\frac{\pi}{2}\right)=0=\sqrt{1-1^2}=\sqrt{1-x^2}$.

So for all relevant values of $x$ we have $\cos(\arcsin(x))=\sqrt{1-x^2}$, which is indeed an expression that does not contain any (inverse) trigonometric functions.  

**Method 2 (using trigonometric identities)**

Recall that we wrote $y=\arcsin(x)$ and that we had $-\frac{\pi}{2}\leq y\leq \frac{\pi}{2}$ and $\sin(y)=x$. Using the standard identity $\cos(\theta)^2+\sin(\theta)^2$, we find

$$
 \cos(\arcsin(x))^2=\cos(y)^2=1-\sin(y)^2=1-x^2.
$$

Here we used that $\sin(y)=x$. As such, we must have $\cos(\arcsin(x))=\pm\sqrt{1-x^2}$. In order to determine whether we need the positive or the negative square root, we use the other piece of information: we know that $-\frac{\pi}{2}\leq y\leq \frac{\pi}{2}$. Since the cosine is nonnegative on the interval $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$, see {numref}`Fig:Inverse:Simplify3`, we must have $\cos(y)\geq 0$. As such, $\cos(\arcsin(x))=\cos(y)\geq0$, so $\cos(\arcsin(x))$ must be the positive root. We find that $\cos(\arcsin(x))=\sqrt{1-x^2}$, which is indeed an expression that does not contain any (inverse) trigonometric functions. 

:::{applet}
:url: calculus/inverse_functions/graph_of_cosine_function_with_focus
:name: Fig:Inverse:Simplify3
:class: dark-light

The cosine function where the solid part is the function on the interval $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$.
:::

::::::

(Subsec:InverseGrasple)=

## Grasple exercises


### Exercises on inverses of general functions

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/60bcd474-3239-4e71-8946-cee3a7637bcd?id=70819
:label: Grasple:70819
:dropdown:
:description: Graph of an inverse function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8a519661-0c39-4d97-9557-8ff1733f51cb?id=70839
:label: Grasple:70839
:dropdown:
:description: Checking whether three functions are one-to-one.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/aa012c3c-6c14-48d6-a2f6-c53da9c30ac6?id=63408
:label: Grasple:63408
:dropdown:
:description: Checking on which domain a function is invertible.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/72d35828-d237-4037-b971-c2556ff5ccee?id=63410
:label: Grasple:63410
:dropdown:
:description: Finding inverse of quadratic function on half domain.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6a9dd364-6d70-482e-882b-bdd6e21e1f25?id=63411
:label: Grasple:63411
:dropdown:
:description: Finding inverse of rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c24ee782-910e-4004-b300-1e0a00fb6da6?id=70842
:label: Grasple:70842
:dropdown:
:description: Finding inverse of quadratic function on full domain.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c8969c93-0ace-4865-a212-87a26495a911?id=63122
:label: Grasple:63122
:dropdown:
:description: Finding maximal domain + inverse of rational function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c8969c93-0ace-4865-a212-87a26495a911?id=63122
:label: Grasple:63122
:dropdown:
:description: Making a self-inverse function.

::::

### Exercises on logarithms.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/44e2b007-c172-41e5-bd5a-8048f699e407?id=130661
:label: Grasple:130661
:dropdown:
:description: Finding exact values of expressions with logarithms.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/72fd9d97-9f93-45e9-adb5-b0bed0ff089e?id=130648
:label: Grasple:130648
:dropdown:
:description: Expanding an expression involving logarithms.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f92f31b2-292c-4417-95ec-a60fb3168943?id=130649
:label: Grasple:130649
:dropdown:
:description: Writing an expression as a single logarithm.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b489c899-aa03-40ce-95e4-25f56486164a?id=130640
:label: Grasple:130640
:dropdown:
:description: Solving an equation with an exponential function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3bd2251c-d349-40f8-bc4b-1bf2ddf93ca4?id=130641
:label: Grasple:130641
:dropdown:
:description: Solving an equation with an exponential function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ad1638df-2fc3-444b-8179-d587b95da3f0?id=130636
:label: Grasple:130636
:dropdown:
:description: Solving an equation with an exponential function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ffa4ab1e-e00d-4051-85d2-09008bea23c8?id=130642
:label: Grasple:130642
:dropdown:
:description: Solving an equation with an exponential function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a2a59639-0069-4bbb-bc8f-5b13817028a0?id=130637
:label: Grasple:130637
:dropdown:
:description: Solving an equation with an exponential function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4d0ef697-c0cc-403e-8288-bf69f7fa5757?id=130646
:label: Grasple:130646
:dropdown:
:description: Solving an equation with an exponential function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d730ecaf-01a1-440c-b7a6-fe4673701273?id=130664
:label: Grasple:130664
:dropdown:
:description: Solving an equation with a logarithmic function.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e2160262-6257-4f0b-94ff-1267eed83a62?id=63125
:label: Grasple:63125
:dropdown:
:description: Two statements about logarithms.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/abe00184-8aca-474b-a39d-6d1bd51b4e63?id=130665
:label: Grasple:130665
:dropdown:
:description: Solving an equation with a logarithmic function.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/582e83c2-9982-4531-8616-053fc9af3cc4?id=63127
:label: Grasple:130627
:dropdown:
:description: Finding inverse of exponential function with base different from $e$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f0b8a169-2217-43ed-8c87-00384fa431e7?id=63129
:label: Grasple:130629
:dropdown:
:description: Finding maximal domain + inverse of exponential function composed with a square root.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/18f05192-771d-4586-94f5-62a05967ce6a?id=63133
:label: Grasple:130633
:dropdown:
:description: Finding maximal domain + inverse of logarithm.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f6d59bf9-b8e3-4ab1-ba5b-1e638f4288d7?id=63065
:label: Grasple:130665
:dropdown:
:description: Finding maximal domain + inverse of logarithm composed with logarithm.

::::

### Exercises on inverse trigonometric functions.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/92f70639-7718-4894-922e-fabd8f446459?id=76291
:label: Grasple:76291
:dropdown:
:description: Finding $\arcsin(a)$ without a calculator.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/60f540d8-e5ea-4698-8003-0a7e48934bea?id=76295
:label: Grasple:76295
:dropdown:
:description: Finding $\arctan(a)$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0614ebe8-eeca-4302-a383-09552e8e6510?id=76296
:label: Grasple:76296
:dropdown:
:description: Finding $\sin(\arcsin(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4807abf6-1c06-44c5-b5da-f46a72c8144c?id=76297
:label: Grasple:76297
:dropdown:
:description: Finding $\cos(\arccos(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/29236142-b0f0-45b3-b6be-64e7566e6294?id=76298
:label: Grasple:76298
:dropdown:
:description: Finding $\tan(\arctan(a))$ without a calculator.

::::




::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3407acde-0574-4d2e-8953-b78d60e90308?id=76327
:label: Grasple:76327
:dropdown:
:description: Finding $\arcsin(\sin(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7cd1cc53-2795-4e95-ab3c-a741dbabe0b0?id=76417
:label: Grasple:76417
:dropdown:
:description: Finding $\arccos(\cos(a))$ without a calculator.

::::




::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/59a91832-fbc0-4679-b505-ca44359c0b28?id=76318
:label: Grasple:76318
:dropdown:
:description: Finding $\arctan(\tan(a))$ without a calculator.

::::





::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fde17784-4aee-4dc7-9677-57458daeb2f3?id=76644
:label: Grasple:76644
:dropdown:
:description: Finding $\tan(\arccos(a))$ without a calculator.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7d035172-e80d-42d8-a82a-0fc02bea8d28?id=76647
:label: Grasple:76647
:dropdown:
:description: Finding $\sin(\arctan(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/70d2c0b0-d1ff-494b-a27e-61c049745da3?id=70734
:label: Grasple:70734
:dropdown:
:description: Simplifying expresion of the form $\tan(\arcsin(ax+b))$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/92ad8603-2d81-410e-a353-ce2f488f6ab7?id=76760
:label: Grasple:76760
:dropdown:
:description: Finding $\arcsin(\cos(a))$ without a calculator.

::::





::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/af1de926-d272-4a64-bd5f-2e0663b70395?id=76763
:label: Grasple:76763
:dropdown:
:description: Finding $\arccos(\sin(a))$ without a calculator.

::::





::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f60a5f16-6f93-4a94-971c-881114053625?id=76768
:label: Grasple:76768
:dropdown:
:description: Finding $\cos(2\arccos(a))$ without a calculator.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3b37b0a9-6cd0-4644-923a-b0ba267d6348?id=76770
:label: Grasple:76770
:dropdown:
:description: Finding $\tan(2\arcsin(a))$ without a calculator.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/467d06b4-26be-4de5-93fa-4aae7acb33bd?id=70788
:label: Grasple:70788
:dropdown:
:description: Simplify $\arcsin(a)+\arccos(a)$.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fe2885ec-92fe-4fe8-949d-0173ab2da53b?id=70735
:label: Grasple:70735
:dropdown:
:description: Simplify $\cos(\arctan(x)+\arcsin(x))$.

::::


:::::::::{admonition} Bonus: more exercises on inverse trigonometric functions
:class: bonus

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/aae81382-48c0-459d-a5c1-7bca0cde1adc?id=76292
:label: Grasple:76292
:dropdown:
:description: Finding $\arccos(a)$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7cbcea4e-9acf-4b2f-9655-80c806e73dfe?id=76293
:label: Grasple:76293
:dropdown:
:description: Finding $\arcsin(a)$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0a6e8840-b3c0-4794-ac3e-6aeb0147b989?id=76294
:label: Grasple:76294
:dropdown:
:description: Finding $\arccos(a)$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9cec25fb-66a4-4c1d-9a84-b3b8890a1663?id=76299
:label: Grasple:76299
:dropdown:
:description: Finding $\arcsin(\sin(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cb640771-58ae-401e-8d2c-08bb3adab1bd?id=76416
:label: Grasple:76416
:dropdown:
:description: Finding $\arccos(\cos(a))$ without a calculator.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9422563f-f242-4347-9782-2a1211df789e?id=76300
:label: Grasple:76300
:dropdown:
:description: Finding $\arccos(\cos(a))$ without a calculator.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3e477d9d-43e8-442d-aaa8-335a37aec458?id=76418
:label: Grasple:76418
:dropdown:
:description: Finding $\arctan(\tan(a))$ without a calculator.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cc2b528d-6ddc-4129-ad4d-f75795ba584c?id=76337
:label: Grasple:76337
:dropdown:
:description: Finding $\arcsin(\sin(a))$ without a calculator.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/33fccbbd-7097-4d46-aa91-e5f5cee2c767?id=76643
:label: Grasple:76643
:dropdown:
:description: Finding $\sin(\arccos(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/accb1d37-1ff1-41a5-9ae6-d47d197d909e?id=76645
:label: Grasple:76645
:dropdown:
:description: Finding $\cos(\arcsin(a))$ without a calculator.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ce1f5503-af66-4522-b736-fd2fb1cb036b?id=76646
:label: Grasple:76646
:dropdown:
:description: Finding $\tan(\arcsin(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9b94b891-8843-4c0a-a220-b011963637b1?id=76762
:label: Grasple:76762
:dropdown:
:description: Finding $\arcsin(\cos(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/86a4a21d-b196-442c-8555-037b5dc4ab80?id=76759
:label: Grasple:76759
:dropdown:
:description: Finding $\arccos(\sin(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7ae0935c-e566-4248-9130-9c4484b6a587?id=76771
:label: Grasple:76771
:dropdown:
:description: Finding $\tan(2\arccos(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2fd9249e-ea57-4e78-9059-21d532050afc?id=76767
:label: Grasple:76767
:dropdown:
:description: Finding $\cos(2\arcsin(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/47631c23-5c8d-4635-ad93-ac5229f6b28d?id=76772
:label: Grasple:76772
:dropdown:
:description: Finding $\tan(2\arctan(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bc484860-d226-4197-aee9-eb2b94dfd2be?id=76766
:label: Grasple:76766
:dropdown:
:description: Finding $\sin(2\arctan(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/248fd92a-2a93-4683-9c2c-4f1dbc6f6c81?id=76769
:label: Grasple:76769
:dropdown:
:description: Finding $\cos(2\arctan(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/170eaec5-2c53-4f0e-beb6-6a3000405d9b?id=76764
:label: Grasple:76764
:dropdown:
:description: Finding $\sin(2\arcsin(a))$ without a calculator.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/83944556-70e7-4fd0-84b6-fda11dedc5a7?id=76765
:label: Grasple:76765
:dropdown:
:description: Finding $\sin(2\arccos(a))$ without a calculator.

::::

:::::::::