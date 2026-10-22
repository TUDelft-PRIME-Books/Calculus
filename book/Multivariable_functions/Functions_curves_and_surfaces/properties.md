# Properties of functions

In this section we cover:

- Sums, products, scalar multiples
- Composition of functions
- Shifting
- Stretching and reflecting
- Even and odd functions (parity) around (coordinate) planes and (coordinate) axes

## Introduction

Just like with single-variable functions, we can manipulate and combine multivariable functions to obtain new ones. Having more than one input variables increases the number of possibilities when considering operations like shifting, stretching and reflecting. Even though the composition of two functions of $n$ variables (for $n\geq 2$) itself does not exist, we will consider creative ways in which we can still use the output of one such function as (part of) the input for the other function.

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

Let $f_1,\ldots,f_k$ be functions that are all defined on a domain $D$ and have codomain $\mathbb{R}$. Then the **pairing** $\left\langle f_1,\ldots,f_k\right\rangle$ is the function

$$
 \left\langle f_1,\ldots,f_k\right\rangle:D\rightarrow \mathbb{R}^k,\quad \mathbf{x}\rightarrow \left(f_1(\mathbf{x}),\ldots,f_k(\mathbf{x})\right).
$$

The functions $f_1,\ldots,f_k$ are known as the **components** of the pairing $\left\langle f_1,\ldots,f_k\right\rangle$.
::::::