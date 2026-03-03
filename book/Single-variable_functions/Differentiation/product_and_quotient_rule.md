(Section:DiffProdQuot)=

# Product and quotient rule

##Introduction

## The product rule

::::::{prf:theorem} The product rule
:label: Thm:Productquotientrule:Productrule
Let $f$ and $g$ be functions and consider the product function $p=fg$. Let $a$ be in the domain of $p$. Assume that $f$ and $g$ are both differentiable at $a$. Then $p$ is differentiable at $a$ and the derivative $p'(a)$ is given by

$$
 p'(a)=f'(a)g(a)+f(a)g'(a).
$$

::::::

:::{admonition} Proof of {prf:ref}`Thm:Productquotientrule:Productrule`
:class: tudproof, dropdown

The derivative $p'(a)$, if it exists, is given by the limit

$$
 p'(a)=\lim_{h\rightarrow 0}\frac{p(a+h)-p(a)}{h}=\lim_{h\rightarrow 0}\frac{f(a+h)g(a+h)-f(a)g(a)}{h}.
$$

Now we add the term $-f(a+h)g(a)+f(a+h)g(a)$, which is just a very fancy way of writing $0$, to the numerator of this expression. Then we can split the limit in two parts and we obtain

$$
 p'(a)=\lim_{h\rightarrow 0}\frac{f(a+h)g(a+h)-f(a)g(a)}{h}=\lim_{h\rightarrow 0}\frac{f(a+h)g(a+h)-f(a+h)g(a)+f(a+h)g(a)-f(a)g(a)}{h}=\lim_{h\rightarrow 0}\frac{f(a+h)g(a+h)-f(a+h)g(a)}{h}+\lim_{h\rightarrow 0}\frac{f(a+h)g(a)-f(a)g(a)}{h}.
$$

Now we can write both of these limits as a product of two limits to obatin

$$
 p'(a)=\lim_{h\rightarrow 0}\frac{f(a+h)g(a+h)-f(a+h)g(a)}{h}+\lim_{h\rightarrow 0}\frac{f(a+h)g(a)-f(a)g(a)}{h}=\lim_{h\rightarrow 0}f(a+h)\lim_{h\rightarrow 0}\frac{g(a+h)-g(a)}{h}+\lim_{h\rightarrow 0}g(a)\lim_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h}.
$$

Note that since $f$ is differentiable at $a$, it must be continuous at $a$ as well, see {prf:ref}`Thm:Differentiability:Diffimpliescont`, so we must have $\displaystyle \lim_{h\rightarrow 0}f(a+h)=f(a)$. Then we use that $f$ and $g$ are differentiable at $h$ to obtain

$$
 p'(a)=\lim_{h\rightarrow 0}f(a+h)\lim_{h\rightarrow 0}\frac{g(a+h)-g(a)}{h}+\lim_{h\rightarrow 0}g(a)\lim_{h\rightarrow 0}\frac{f(a+h)-f(a)}{h}=f(a)g'(a)+g(a)f'(a),
$$

as desired.

:::

::::{caution}
:name: Caution:Productquotientrule:Commonerrors

The most common error when trying to use the product rule is take the product of the two derivatives. In that case, the incorrect expression would become

$$
 (f g)'(x)=f'(x)g'(x)\qquad\qquad \left(\textbf{INCORRECT}\right).
$$

Make sure to avoid this error and to use the product rule as stated.

::::

Let us see how we can use the product rule in practice, by considering a few examples.

::::::{prf:example} 
:label: Thm:Productquotientrule:Example1
Consider the function $h(x)=x^2\cos(x)$. Then $h$ is the product of the two functions $f(x)=x^2$ and $g(x)=\cos(x)$, of which we both know the derivative. As such, we can use the product rule to obtain

$$
 h'(x)=f'(x)g(x)+f(x)g'(x)=(2x)\cos(x)+x^2\left(-\sin(x)\right)=2x\cos(x)-x^2\sin(x).
$$

::::::

::::::{prf:example} 
:label: Thm:Productquotientrule:Example2
Consider the function $r(t)=2^t\sinh(t)$. Then $r$ is the product of the two functions $p(t)=2^t$ and $q(t)=\sinh(t)$. In {numref}`Sec:Differentiation:ChainRule` we obtained the derivatives of these functions. As such, we can use the product rule to obtain

$$
 r'(t)=p'(t)q(t)+p(t)q'(t)=\left(\ln(2)2^t\right)\sinh(t)+2^t\cosh(t).
$$

::::::

We can also use the product rule to differentiate functions that are the product of three (or more) functions.

::::::{prf:example} 
:label: Thm:Productquotientrule:Exampletripleproduct
Consider the function $f(x)=x^4\sin(x)\cos(x)$. Then $f$ is the product of three functions, so what should be our approach here? It turns out to be a good idea to first write it as a product of two functions. In this case, we can write $f=gh$ with $g(x)=x^4$ and $h(x)=\sin(x)\cos(x)$. Then the product rule gives

$$
 f'(x)=g'(x)h(x)+g(x)h'(x)=4x^3\sin(x)\cos(x)+x^4h'(x).
$$

To fully work out this derivative, we would need to know $h'(x)$, so how do we find that derivative? Well, $h$ is a product of two functions, so we can use the product rule again. Indeed, we can write $h=pq$ with $p(x)=\sin(x)$ and $q(x)=\cos(x)$. Then the product rule gives

$$
 h'(x)=p'(x)q(x)+p(x)q'(x)=\cos(x)\cos(x)+\sin(x)\left(-\sin(x)\right)=\cos^2(x)-\sin^2(x).
$$

Combining this with the previous equation, we obtain

$$
 f'(x)=4x^3\sin(x)\cos(x)+x^4h'(x)=4x^3\sin(x)\cos(x)+x^4\left(\cos^2(x)-\sin^2(x)\right).
$$

::::::

Finally, we can combine the product and chain rules to find the derivatives of complicated functions.

::::::{prf:example} 
:label: Thm:Productquotientrule:Exampleproductchain
Consider the function $f(x)=x^2\sin\left(x^3+2x+1\right)$. Then $f$ can be written as the product $f=gh$ with $g(x)=x^2$ and $h(x)=\sin\left(x^3+2x+1\right)$. Using the product rule, we find

$$
 f'(x)=g'(x)h(x)+g(x)h'(x)=2x\sin\left(x^3+2x+1\right)+x^2h'(x).
$$

Then in order to find the derivative $h'(x)$ we need the chain rule. Indeed, we can write $h(x)=p\circ q$ with $p(x)=\sin(x)$ and $q(x)=x^3+2x+1$. With the chain rule we obtain

$$
 h'(x)=p'(q(x))q'(x)=\cos\left(x^3+2x+1\right)\left(3x^2+2\right).
$$

Combining these equations gives

$$
 f'(x)=2x\sin\left(x^3+2x+1\right)+x^2h'(x)=2x\sin\left(x^3+2x+1\right)+x^2\cos\left(x^3+2x+1\right)\left(3x^2+2\right)=2x\sin\left(x^3+2x+1\right)+\left(3x^4+2x^2\right)\cos\left(x^3+2x+1\right).
$$

::::::

In this section we cover

- The product rule
- The quotient rule
- Derivative of tan(x)