# Properties of functions



## Introduction

Just like with single-variable functions, we can manipulate and combine multivariable functions to obtain new ones. Having more than one input variables increases the number of possibilities when considering operations like shifting, stretching and reflecting. Even though the composition of two functions of $n$ variables (for $n\geq 2$) itself does not exist, we will consider creative ways in which we can still use the output of one such function as (part of) the input for the other function. Finally, there are many ways in which multivariable function can possess symmetries.

## Combining functions

Since the codomain of a function of $n$ variables is $\mathbb{R}$, we can perform arithmetic operations on these functions by performing them point-wise. In particular, we obtain the following definition, which very much resembles {prf:ref}`Def:PropertiesFunctions:Arithmetic`


::::::{prf:definition} 
:label: Def:PropertiesMultiFunctions:Arithmetic

Let $f$ and $g$ be functions of $n$ variables. Then we can define the following functions.

- The **sum function** $f+g$ is defined by $(f+g)(\mathbf{x})=f(\mathbf{x})+g(\mathbf{x})$.
- The **difference function** $f-g$ is defined by $(f-g)(\mathbf{x})=f(\mathbf{x})-g(\mathbf{x})$.
- The **product function** $fg$ is defined by $(fg)(\mathbf{x})=f(\mathbf{x})g(\mathbf{x})$.
- The **quotient function** $\frac{f}{g}$ is defined by $\left(\frac{f}{g}\right)(\mathbf{x})=\frac{f(\mathbf{x})}{g(\mathbf{x})}$.
- If $c$ is a real number, then the **scalar multiple function** $cf$ is defined by $(cf)(\mathbf{x})=cf(\mathbf{x})$.
- If $c$ and $d$ are real numbers, then the **linear combination** $h=cf+dg$ is defined by $h(x)=cf(\mathbf{x})+dg(\mathbf{x})$.

::::::

::::::{prf:example} 
:label: Ex:PropertiesMultiFunctions:Arithmetic

Consider the functions of two variables

$$
 f(x,y)=\sin(x+y),\quad g(x,y)=-2y,\quad h(x,y)=e^{xy}.
$$

Then the function $\dfrac{f+h}{g}$ is given by

$$
 \left(\dfrac{f+h}{g}\right)(x,y)=\frac{f(x,y)+h(x,y)}{g(x,y)}=\frac{\sin(x+y)+e^{xy}}{-2y}.
$$

The maximal domain of this function is the set of all $(x,y)$ for which the formula $\dfrac{\sin(x+y)+e^{xy}}{-2y}$ prodces a real number. Since the only restriction here is that we are not allowed to divide by $0$, the maximal domain $D_{\frac{f+h}{g}}$ is given by

$$
 D_{\frac{f+h}{g}}=\left\{(x,y)\in\mathbb{R}^2\,\middle|\,y\neq 0\right\}.
$$

::::::

If $f$ and $g$ are two functions of $n$ variables with $n\geq 2$ then the composition $f\circ g$ does not exist, as it is impossible to use the output of $g$ (a real number) as input for the function $f$. What we can do however, is use the output of $g$ as one of input variable for $f$. For instance, if $f$ and $g$ are both functions of two variables, we could consider a function that maps $(x,y)$ to $f(x,g(x,y))$. This means that we first pair the function $x$ and the function $g(x,y)$ and plug in the result into $f$. In order to streamline the notation, we need to introduce the concept of a pairing.

::::::{prf:definition} 
:label: Def:PropertiesMultiFunctions:Pairing

Let $f_1,\ldots,f_n$ be functions that are all defined on a domain $D$ and have codomain $\mathbb{R}$. Then the **pairing** $\left\langle f_1,\ldots,f_n\right\rangle$ is the function

$$
 \left\langle f_1,\ldots,f_n\right\rangle:D\rightarrow \mathbb{R}^n,\quad \mathbf{x}\rightarrow \left(f_1(\mathbf{x}),\ldots,f_n(\mathbf{x})\right).
$$

The functions $f_1,\ldots,f_n$ are known as the **components** of the pairing $\left\langle f_1,\ldots,f_n\right\rangle$.
::::::

:::{note}
Since the pairing $\left\langle f_1,\ldots,f_n\right\rangle$ has codomain $\mathbb{R}^n$, it is a different type of function than what we have studied before. If $f_1,\ldots,f_n$ are functions of $n$ variables, then we call this pairing a **vector field** on $\mathbb{R}^n$. Vector fields will be studied in more detail in {numref}`Chapter:VectorCalculusIntro`.
:::

Since the output of a pairing of $n$ functions is an element of $\mathbb{R}^n$, we can use this as an input for a function of $n$ variables. Specifically, if $f_1,\ldots,f_n$ are all functions of $m$ variables that are defined on some domain $D\subset\mathbb{R}^m$ and $g$ is a function of $n$ variables, then the composition

$$
 h=g\circ\left\langle f_1,\ldots,f_n\right\rangle
$$

exists. Since the domain of the pairing $\left\langle f_1,\ldots,f_n\right\rangle$ is a part of $\mathbb{R}^m$, while the codomain of $g$ is $\mathbb{R}$, the function $h$ is a function of $m$ variables. Let us consider a few examples to make this more concrete.

::::::{prf:example} 
:label: Ex:PropertiesMultiFunctions:Pairing

Consider the functions $f_1(s,t)=s+t$, $f_2(s,t)=s-t$ and $f_3(s,t)=s$ and the function $g(x,y,z)=x^2-y^2+z^2$. Then the pairing $\left\langle f_1,f_2,f_3\right\rangle$ is given by

$$
 \left\langle f_1,f_2,f_3\right\rangle(s,t)=\left(s+t,s-t,s\right).
$$

In addition, the composition $h=g\circ \left\langle f_1,f_2,f_3\right\rangle$ is given by

\begin{align*}
 h(s,t)&=g\left(\left\langle f_1,f_2,f_3\right\rangle(s,t)\right)\\ &=g\left(s+t,s-t,s\right)\\ &=\left(s+t\right)^2-\left(s-t\right)^2+s^2\\ &=s^2+4st.
\end{align*}
::::::

::::::{prf:example} 
:label: Ex:PropertiesMultiFunctions:Pairingswitch

Consider the functions $f_1(x,y)=y$, $f_2(x,y)=s$ and some function $g$ of two variables. Then the pairing $\left\langle f_1,f_2\right\rangle$ is given by

$$
 \left\langle f_1,f_2\right\rangle(x,y)=\left(y,x\right).
$$

In addition, the composition $h=g\circ \left\langle f_1,f_2\right\rangle$ is given by

$$
 h(x,y)=g\left(\left\langle f_1,f_2\right\rangle(x,y)\right)=g\left(y,x\right).
$$

That is, composing $g$ with this pairing $\left\langle f_1,f_2\right\rangle$ switches around the two input variables $x$ and $y$.
::::::

In {numref}`Subsec:PropertiesFunctionsCombinations` we studied how single-variable functions can be stretched and/or shifted in the $x$- and/or $y$-direction. For a function of $n$ variables, there are $n+1$ directions in which we can stretch and/or shift: $n$ directions corresponding to the input variables and $1$ direction corresponding to the output variable. Directly analogous to {prf:ref}`Thm:PropertiesFunctions:Shifts` and {prf:ref}`Thm:PropertiesFunctions:ReflectionStretching` we obtain the following results.

::::::{prf:theorem} 
:label: Thm:PropertiesMultiFunctions:Shifts

Let $f$ be a function of $n$ variables $x_1,\ldots ,x_n$ and $a>0$ be a positive real number. We let $z$ denote the output variable $z=f(x_1,\ldots,x_n)$. Let $1\leq i\leq n$. Then we can perform to the graph of $f$

- a **shift in the positive $x_i$-direction** of size $a$ to obtain the graph of the function $g(x_1,\ldots,x_n)=f(x_1,\ldots,x_{i-1},x_i-a,x_{i+1},\ldots,x_n)$;
- a **shift in the negative $x_i$-direction** of size $a$ to obtain the graph of the function $g(x_1,\ldots,x_n)=f(x_1,\ldots,x_{i-1},x_i+a,x_{i+1},\ldots,x_n)$;
- a **shift in the positive $z$-direction** of size $a$ to obtain the graph of the function $g(x_1,\ldots,x_n)=f(x_1,\ldots,x_n)+a$;
- a **shift in the negative $z$-direction** of size $a$ to obtain the graph of the function $g(x_1,\ldots,x_n)=f(x_1,\ldots,x_n)-a$.

::::::

::::::{prf:theorem} 
:label: Thm:PropertiesMultiFunctions:ReflectionStretching

Let $f$ be a function of $n$ variables $x_1,\ldots ,x_n$ and $c\neq 0$ a real number. We let $z$ denote the output variable $z=f(x_1,\ldots,x_n)$. Let $1\leq i\leq n$. Consider the functions $g(x_1,\ldots,x_n)=cf(x_1,\ldots,x_n)$ and $h(x_1,\ldots,x_n)=f\left(x_1,\ldots,x_{i-1},\frac{x_i}{c},x_{i+1},\ldots,x_n\right)$. Then, if $c>0$,

- the graph of $g$ is obtained from the graph of $f$ by **stretching the graph in the $z$-direction** by a factor $c$;
- the graph of $h$ is obtained from the graph of $f$ by **stretching the graph in the $x_i$-direction** it by a factor $c$.

In addition, if $c=-1$,

- the graph of $g(x_1,\ldots,x_n)=-f(x_1,\ldots,x_n)$ is obtained from the graph of $f$ by **reflecting** it over the coordinate (hyper)plane $z=0$;
- the graph of $h(x_1,\ldots,x_n)=f\left(x_1,\ldots,x_{i-1},-x_i,x_{i+1},\ldots,x_n\right)$ is obtained from the graph of $f$ by **reflecting** it over the coordinate (hyper)plane $x_i=0$.

::::::

::::::{prf:example} 
:label: Ex:PropertiesMultiFunctions:ReflectionStretching

Consider the function $f(x,y)=x^5-y^3$. We will, step by step, manipulate the function to obtain new functions and we will look specifically at the impact on the graph. Starting with the graph $z=f(x,y)$, we first perform a stretching by in the $y$-direction by a factor $\frac{1}{2}$ to obtain the graph given by $z=x^5-(2y)^3=x^5-8x^3$. Then we perform a shift of $1$ in the positive $x$-direction to obtain the graph given by $z=(x-1)^5-8y^3$. Subsequently, we perform a reflection across the $xy$-plane to obtain the graph given by $z=-\left((x-1)^5-8y^3\right)=-(x-1)^5+8y^3$. Then we perform a stretching in the positive $z$-direction by a factor $3$ to obtain the graph given by $z=3\left(-(x-1)^5+8y^3\right)=-3(x-1)^5+24y^3$. Finally, we perform a shift in the positive $z$-direction to obtain the graph given by $z=-3(x-1)^5+24y^3+4$.  That is, we obtain the graph of the function $g(x,y)=-3(x-1)^5+24y^3+4$.

:::{todo}
Include an applet like {numref}`Fig:PropertiesFunctions:ReflectionStretching`.
:::

As we noticed in {prf:ref}`Ex:PropertiesFunctions:ReflectionStretching`, performing these operations in a different order might give us a different function.
::::::

## Even and odd functions

In {prf:ref}`Def:PropertiesFunctions:EvenOdd` we defined what it means for a single-variable function to be even or odd. In what might be starting to become a recurring theme, having more input variables gives more ways in which symmetries can be present. Specifically, we will define when a function is even or odd as a whole, when it is even or odd in a specific variable and when it is even or odd in a coordinate (hyper)plane.

::::::{prf:definition} 
:label: Def:PropertiesMultiFunctions:EvenOdd

Let $f$ be a function of $n$ variables $x_1,\ldots,x_n$ and let $D\subset\mathbb{R}^n$. Then $f$ is called **even** on $D$ if for all $\mathbf{x}$ in $D$ we have $-\mathbf{x}$ in $D$ and $f(-\mathbf{x})=f(\mathbf{x})$. In addition, $f$ is called **odd** on $D$ if for all $\mathbf{x}$ in $D$ we have $-\mathbf{x}$ in $D$ and $f(-\mathbf{x})=-f(\mathbf{x})$.

In addition, we let $1\leq i\leq n$. Then we say that $f$ is **even in $x_i$** on $D$ if for all $(x_1,\ldots,x_n)$ in $D$ we have $(x_1,\ldots,x_{i-1},-x_i,x_{i+1},\ldots,x_n)$ in $D$ and 

$$
 f(x_1,\ldots,x_{i-1},-x_i,x_{i+1},\ldots,x_n)=f(x_1,\ldots,x_n).
$$

In addition, $f$ is **odd in $x_i$** on $D$ if for all $(x_1,\ldots,x_n)$ in $D$ we have $(x_1,\ldots,x_{i-1},-x_i,x_{i+1},\ldots,x_n)$ in $D$ and 

$$
 f(x_1,\ldots,x_{i-1},-x_i,x_{i+1},\ldots,x_n)=-f(x_1,\ldots,x_n).
$$

Finally, we say that $f$ is **even in the coordinate (hyper)plane $x_i=0$** on $D$ if for all $(x_1,\ldots,x_n)$ in $D$ we have $(-x_1,\ldots,-x_{i-1},x_i,-x_{i+1},\ldots,-x_n)$ in $D$ and 

$$
 f(-x_1,\ldots,-x_{i-1},x_i,-x_{i+1},\ldots,-x_n)=f(x_1,\ldots,x_n).
$$

In addition, $f$ is **odd in the coordinate (hyper)plane $x_i=0$** on $D$ if for all $(x_1,\ldots,x_n)$ in $D$ we have $(-x_1,\ldots,-x_{i-1},x_i,-x_{i+1},\ldots,-x_n)$ in $D$ and 

$$
 f(-x_1,\ldots,-x_{i-1},x_i,-x_{i+1},\ldots,-x_n)=-f(x_1,\ldots,x_n).
$$

::::::


::::::{prf:example} 
:label: Ex:PropertiesMultiFunctions:EvenOdd
Consider the function of three variables

$$
 f(x,y,z)=xyz^2+x^2z^4.
$$

This function is even on $\mathbb{R}^3$, as for any $(x,y,z)$ in $\mathbb{R}^3$ we have 

$$
 f(-x,-y,-z)=(-x)(-y)(-z)^2+(-x)^2(-z)^4=xyz^2+x^2z^4=f(x,y,z).
$$

However, it is not even or odd in $x$ on $\mathbb{R}^3$ as we have

$$
 f(-x,y,z)=(-x)yz^2+(-x)^2z^4=-xyz^2+x^2z^4
$$

and expression is, in general, not equal to either $xyz^2+x^2z^4$ or $-\left(xyz^2+x^2z^4\right)$. Similarly, it is not even or odd in $y$ on $\mathbb{R}^3$ as we have

$$
 f(x,-y,z)=x(-y)z^2+x^2z^4=-xyz^2+x^2z^4.
$$

In addition, it is even in $z$ on $\mathbb{R}^3$, as we have

$$
 f(x,y,-z)=xy(-z)^2+x^2(-z)^4=xyz^2+x^2z^4=f(x,y,z).
$$

Now we will investigate whether the function is even or odd in the coordinate planes. We observe that

$$
 f(-x,-y,z)=(-x)(-y)z^2+(-x)^2z^2=xyz^2+x^2z^4=f(x,y,z),
$$

so $f$ is even in the $xy$-plane on $\mathbb{R}^3$. In addition, we have

$$
 f(-x,y,-z)=(-x)y(-z)^2+(-x)^2(-z)^2=-xyz^2+x^2z^4,
$$

so $f$ is neither even nor odd in the $xz$-plane on $\mathbb{R}^3$. Finally, we find

$$
 f(x,-y,-z)=x(-y)(-z)^2+(-x)^2(-z)^2=-xyz^2+x^2z^4,
$$

so $f$ is neither even nor odd in the $yz$-plane on $\mathbb{R}^3$.
::::::

::::::{prf:example} 
:label: Ex:PropertiesMultiFunctions:EvenOddeachvar
Consider the functions

$$
 f(x,y)=xy,\qquad g(x,y,z)=xyz.
$$

The functions $f$ and $g$ are odd on their domains in each of their variables. However, we note that

$$
 f(-x,-y)=(-x)(-y)=xy=f(x,y),
$$

while

$$
 g(-x,-y,-z)=(-x)(-y)(-z)=-xyz=-g(x,y,z).
$$

So $f$ is even on its domain while $g$ is odd on its domain.

In general, if $h$ is a function of $n$ variables that is odd in each of its variables on a domain $D$, then we note that

$$
 h(-x_1,\ldots,-x_n)=-h(x_1,-x_2,\ldots,-x_n)=(-1)^2h(x_1,x_2,-x_3,\ldots,-x_n)
$$

$$
 =\ldots=(-1)^nh(x_1,\ldots,x_n).
$$

We conclude that $h$ is even on $D$ if $n$ is even, while $h$ is odd on $D$ if $n$ is odd.
::::::