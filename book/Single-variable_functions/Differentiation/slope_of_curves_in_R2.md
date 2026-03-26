# Slopes of curves in $\mathbb{R}^2$

(Subsec:SlopeCurveIntro)=
## Introduction

Consider the unit circle which is defined by the equation $x^2+y^2=1$. Suppose we want to find the slope of this curve at the point $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$. If the circle were the graph of a function, we would know what to do: we would take the derivative of the function and insert the value $x=\frac{1}{2}$. However, we saw in {numref}`Section:Curves` that this curve is not the graph of a function, so this not seem possible here. On the other hand, if we zoom in close to the point $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$ we do not see the lower half of the circle and the part we do see perfectly resembles the graph of a function. To make this idea a bit more precise, we know that on the upper half of the circle we have $y=\sqrt{1-x^2}$. Hence, the upper half of the circle **is** the graph of a function, so we can use the derivative here. In particular, writing $f(x)=\sqrt{1-x^2}$, we find, using the chain rule, that

$$
 f'(x)=\frac{1}{2\sqrt{1-x^2}}(-2x)=\frac{-x}{\sqrt{1-x^2}}.
$$

For $x=\frac{1}{2}$ we then obtain 

$$
 \displaystyle f'\left(\frac{1}{2}\right)=\dfrac{-\frac{1}{2}}{\sqrt{1-\left(\frac{1}{2}\right)^2}}=-\frac{1}{\sqrt{3}}.
$$

Hence, the slope to the unit circle at $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$ is $-\dfrac{1}{\sqrt{3}}$. In particular, the line 

$$
 y=\frac{1}{2}\sqrt{3}-\frac{1}{\sqrt{3}}\left(x-\frac{1}{2}\right)
$$

is tangent to the unit circle at $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$. 

:::{todo}
Show the unit circle with the tangent line at $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$.
:::

We conclude that when it is possible to write (part of) a curve as the graph of a function, we can find the slope of a curve. However, what should we do if that is not the case, either because it is hard (or even impossible) to explicitly express $y$ as a function of $x$, or because our curve is defined by a parametrisation? In those cases, we need other tools, which will be the main topic of this section.

## Implicit differentiation

[^FootnoteImplicit]: To give a proper mathematical motivation of why this technique works, we need the concept of a partial derivative, see {numref}`Sec:PartialDerivatives`

Consider a curve that is implicitly defined by an equation of the form $f(x,y)=0$. If it is possible to turn this into an explicit equation $y=g(x)$ (on at least some part of the curve) we can explicitly find the derivative using regular differentiation techniques. However, in most cases that is not neccesary. We can, instead, work with the assumption that, at least if zoom in enough, it is theoretically possible to obtain an explicit equation $y=g(x)$, but by using the chain rule, we can actually avoid ever having to find this explicit equation. This technique is called **implicit differentiation**. Even for curves where an explicit form can be found (such as for the unit circle) it is typically easier and quicker to use implicit differentiation. This technique is best explained[^FootnoteImplicit] by means of several examples.

::::::{prf:example} 
:label: Ex:SlopeCurves:Circle

[^FootnoteImplicit2]: If you find this step difficult, it might perhaps be useful to pick a few functions for $y$ and see how it works there. For instance, if $y=(3x+1)$, then $y^2=(3x+1)^2$, so by the chain rule we would have $\frac{d}{dx}\left[y^2\right]=\frac{d}{dx}(3x+1)^2=2(3x+1)3=2y\frac{dy}{dx}$. Or, if $y=\sin(x)$, then $y^2=\sin^2(x)$ and by we would obtain $\frac{d}{dx}\left[y^2\right]=\frac{d}{dx}\sin^2(x)=2\sin(x)\cos(x)=2y\frac{dy}{dx}$.

Again consider the unit circle $x^2+y^2=1$ that was discussed in {numref}`Subsec:SlopeCurveIntro`. We will use implicit differentiation to (again) find the slope at $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$. For this, we take the equation $x^2+y^2=1$ and take the derivative with respect to $x$ of both sides of the equation. This gives

$$
 \frac{d}{dx}\left[x^2+y^2]=\frac{d}{dx}[1].
$$

Using our knowledge of differentiation, we can compute several of these terms and we find

$$
 2x+\frac{d}{dx}\left[y^2]=0.
$$

This is where the 'implicit' part of implicit differentiation comes in: we assume that, when we zoom in enough, $y$ is a function of $x$, so that $y=y(x)$. Then we can use the chain rule to find the derivative $\frac{d}{dx}\left[y^2]$. Indeed, if we write $y^2=f(g(x))$ with $f(x)=x^2$ and $g(x)=y$ then the chain rule gives $\frac{d}{dx}\left[y^2]=f'(g(x))g'(x)$. We can quickly commpute $f'(x)=2x$, so $f'(g(x))=f'(y)=2y$, but what about $g'(x)$? Since we have $g(x)=y$, $g'(x)$ is the derivative of $g$, meaning the derivative of $y$. That is, we have $g'(x)=\dfrac{dy}{dx}$. As such, we find $\frac{d}{dx}\left[y^2]=2y\frac{dy}{dx}$[^FootnoteImplicit2]. Plugging this back into the equation above, we find

$$
 2x+2y\frac{dy}{dx}=0.
$$

This equation can be solved for $\dfrac{dy}{dx}$ and we obtain

$$
 \frac{dy}{dx}=\frac{-2x}{2y}=\frac{-x}{y}.
$$

Then for the point $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$ we obtain

$$
 \left.\frac{dy}{dx}\right|_{(x,y)=\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)}=\left.\frac{-x}{y}\right|_{(x,y)=\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)}=\frac{-\frac{1}{2}}{\frac{1}{2}\sqrt{3}}=-\frac{1}{\sqrt{3}},
$$

which matches the result we obtained previously (as it should, of course). Note that the notation $\left.\frac{dy}{dx}\right|_{(x,y)=\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)}$ means that we evaluate $\dfrac{dy}{dx}$ at $(x,y)=\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$.

The advantage here is that this expression for $\frac{dy}{dx}$ is valid for all points on the circle (for the points with $y=0$ it tells us that the derivative does not exist, which is indeed the case since the tangent line is vertical at these points). Indeed, consider the point $\left(-\frac{1}{2}\sqrt{2},-\frac{1}{2}\sqrt{2}\right)$, which lies on the lower half of the circle. If we were to follow the method from {numref}`Subsec:SlopeCurveIntro`, we would need to start over as this point lies on a different part of the curve which is not part of the graph of the function $f(x)=\sqrt{1-x^2}$ (instead, it lies on the graph of the function $g(x)=-\sqrt{1-x^2}$). On the other hand, with implicit differentiation we directly find

$$
 \left.\frac{dy}{dx}\right|_{(x,y)=\left(-\frac{1}{2}\sqrt{2},-\frac{1}{2}\sqrt{2}\right)}=\left.\frac{-x}{y}\right|_{\left(-\frac{1}{2}\sqrt{2},-\frac{1}{2}\sqrt{2}\right)}=\frac{-\left(-\frac{1}{2}\sqrt{2}\right)}{-\frac{1}{2}\sqrt{2}}=-1.
$$


::::::

::::::{prf:example} 
:label: Ex:SlopeCurves:Folium
In {prf:ref}`Ex:Curves:FoliumDescartes` we studied the folium of Descartes, which is implicitly defined by the equation $x^3+y^3=3xy$. For this curve, it is not reasonable to explicitly write $y$ as a function of $x$. Therefore, if we want to find the slope of this function, we should use implicit differentiation. As such, we assume that, if we zoom in enough, $y$ is a function of $x$. Then we take the derivative on both sides of the equation $x^3+y^3=3xy$ to obtain

$$
 3x^2+\frac{d}{dx}\left[y^3\right]=\frac{d}{dx}\left[3xy\right].
$$

Now in order to find $\frac{d}{dx}\left[y^3\right]$ we use the chain rule and we obtain $\frac{d}{dx}\left[y^3\right]=3y^2\frac{dy}{dx}$ (similarly to how we found that $$\frac{d}{dx}\left[y^2\right]=2y\frac{dy}{dx}$ in {prf:ref}`Ex:SlopeCurves:Circle`). For $\frac{d}{dx}\left[3xy\right]$, we first use the product rule to find

$$
 \frac{d}{dx}\left[3xy\right]=3y+3x\frac{dy}{dx}.
$$

Here we used that the derivative of $y$ is $\frac{dy}{dx}$ (which is of course what the notation $\frac{dy}{dx}$ means in the first place, )
::::::

In this section we cover:

- Slopes of curves in $\mathbb{R}^2$
- Implicit differentiation (without using partial derivatives)