(Section:SlopeCurves)=

# Slopes of curves in $\mathbb{R}^2$

(Subsec:SlopeCurveIntro)=
## Introduction

Consider the unit circle which is defined by the equation $x^2+y^2=1$, see {numref}`Fig-SlopeCurveIntro-Circle`. Suppose we want to find the slope of this curve at the point $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$. If the circle were the graph of a function, we would know what to do: we would take the derivative of the function and insert the value $x=\frac{1}{2}$. However, we saw in {numref}`Section:Curves` that this curve is not the graph of a function, so this does not seem possible here. On the other hand, if we zoom in close to the point $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$ we do not see the lower half of the circle and the part we do see perfectly resembles the graph of a function. To make this idea a bit more precise, we know that on the upper half of the circle we have $y=\sqrt{1-x^2}$. Hence, the upper half of the circle **is** the graph of a function, so we can use the derivative here. In particular, writing $f(x)=\sqrt{1-x^2}$, we find, using the chain rule, that

$$
 f'(x)=\frac{1}{2\sqrt{1-x^2}}(-2x)=\frac{-x}{\sqrt{1-x^2}}.
$$

For $x=\frac{1}{2}$ we then obtain 

$$
 \displaystyle f'\left(\frac{1}{2}\right)=\dfrac{-\frac{1}{2}}{\sqrt{1-\left(\frac{1}{2}\right)^2}}=-\frac{1}{\sqrt{3}}.
$$

Hence, the slope of the unit circle at $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$ is $-\dfrac{1}{\sqrt{3}}$. In particular, the line 

$$
 y=\frac{1}{2}\sqrt{3}-\frac{1}{\sqrt{3}}\left(x-\frac{1}{2}\right)
$$

is tangent to the unit circle at $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$. 

:::{applet}
:url: calculus/slopes_of_curves_in_R2/unit_circle
:name: Fig-SlopeCurveIntro-Circle
:class: dark-light

The unit circle with the tangent line at $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$. You can drag the point along the circle and the tangent line will update accordingly.
:::

We conclude that when it is possible to write (part of) a curve as the graph of a function, we can find the slope of a curve. However, what should we do if that is not the case, for instance because it is hard (or even impossible) to explicitly express $y$ as a function of $x$. In that case, we need other tools, which will be the main topic of this section.

(Subsec:ImplicitDiff)=

## Implicit differentiation

Consider a curve that is implicitly defined by an equation of the form $f(x,y)=0$. If it is possible to turn this into an explicit equation $y=g(x)$ (on at least some part of the curve), we can explicitly find the derivative using regular differentiation techniques. However, in most cases that is not necessary. We can, instead, work with the assumption that, at least if zoom in enough, it is theoretically possible to obtain an explicit equation $y=g(x)$. By using the chain rule, we can avoid ever having to find this explicit equation. This technique is called **implicit differentiation**. Even for curves where an explicit form can be found (such as for the unit circle) it is typically easier and quicker to use implicit differentiation. This technique is best explained by means of several examples.

::::::{prf:example} 
:label: Ex:SlopeCurves:Circle

[^FootnoteImplicit2]: If you find this step difficult, it might perhaps be useful to pick a few functions for $y$ and see how it works there. For instance, if $y=\sin(x)$, then $y^2=\sin^2(x)$ and by we would obtain $\dfrac{d}{dx}\left(y^2\right)=\dfrac{d}{dx}\sin^2(x)=2\sin(x)\cos(x)=2y\dfrac{dy}{dx}$.

Again consider the unit circle $x^2+y^2=1$ that was discussed in {numref}`Subsec:SlopeCurveIntro`. We will use implicit differentiation to (again) find the slope at $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$. For this, we take the equation $x^2+y^2=1$ and assume that, when we zoom in enough, $y$ is a differentiable function of $x$, so that $y=y(x)$. Then we can take the derivative with respect to $x$ of both sides of the equation. This gives

$$
 \frac{d}{dx}\left(x^2+y^2\right)=\frac{d}{dx}1.
$$

Using our knowledge of differentiation, we can compute several of these terms and we find

$$
 2x+\frac{d}{dx}y^2=0.
$$

Finally, we can use the chain rule to find the derivative $\dfrac{d}{dx}y^2$. Indeed, if we write $y^2=f(y(x))$ with $f(x)=x^2$ then the chain rule gives $\dfrac{d}{dx}y^2=f'(y(x))\dfrac{dy}{dx}$. Here we used that the derivative of $y$ is $\dfrac{dy}{dx}$ (which is of course what the notation $\dfrac{dy}{dx}$ means in the first place, but if you see this for the first time it might not be so clear immediately). We can quickly compute $f'(x)=2x$, so $f'(y(x))=2y(x)$. As such, we find $\dfrac{d}{dx}y^2=2y\dfrac{dy}{dx}$[^FootnoteImplicit2]. Plugging this back into the equation above, we find

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

which matches the result we obtained previously (as it should, of course). Note that the notation $\left.\dfrac{dy}{dx}\right|_{(x,y)=\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)}$ means that we evaluate $\dfrac{dy}{dx}$ at $(x,y)=\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$.

The advantage here is that this expression for $\dfrac{dy}{dx}$ is valid for all points on the circle (for the points with $y=0$ it tells us that the derivative does not exist, which is indeed the case since the tangent line is vertical at these points). Indeed, consider the point $\left(-\frac{1}{2}\sqrt{2},-\frac{1}{2}\sqrt{2}\right)$, which lies on the lower half of the circle. If we were to follow the method from {numref}`Subsec:SlopeCurveIntro`, we would need to start over as this point lies on a different part of the curve which is not part of the graph of the function $f(x)=\sqrt{1-x^2}$ (instead, it lies on the graph of the function $g(x)=-\sqrt{1-x^2}$). On the other hand, with implicit differentiation we directly find

$$
 \left.\frac{dy}{dx}\right|_{(x,y)=\left(-\frac{1}{2}\sqrt{2},-\frac{1}{2}\sqrt{2}\right)}=\left.\frac{-x}{y}\right|_{\left(-\frac{1}{2}\sqrt{2},-\frac{1}{2}\sqrt{2}\right)}=\frac{-\left(-\frac{1}{2}\sqrt{2}\right)}{-\frac{1}{2}\sqrt{2}}=-1.
$$


::::::



::::::{prf:example} 
:label: Ex:SlopeCurves:Folium
In {prf:ref}`Ex:Curves:FoliumDescartes` we studied the folium of Descartes, which is implicitly defined by the equation $x^3+y^3=3xy$. For this curve, it is rather complicated to explicitly write $y$ as a function of $x$. Therefore, if we want to find the slope of this curve at some point on the curve, we should use implicit differentiation. We assume that, if we zoom in enough, $y$ is a differentiable function of $x$. Then we take the derivative on both sides of the equation $x^3+y^3=3xy$ to obtain

$$
 3x^2+\frac{d}{dx}y^3=\frac{d}{dx}3xy.
$$

Now in order to find $\dfrac{d}{dx}y^3$ we use the chain rule and we obtain $\dfrac{d}{dx}y^3=3y^2\dfrac{dy}{dx}$ (similarly to how we found that $\dfrac{d}{dx}y^2=2y\dfrac{dy}{dx}$ in {prf:ref}`Ex:SlopeCurves:Circle`). For $\dfrac{d}{dx}3xy$, we first use the product rule to find

$$
 \frac{d}{dx}3xy=3y+3x\frac{dy}{dx}.
$$

Combining all of these, we find

$$
 3x^2+3y^2\frac{dy}{dx}=3y+3x\frac{dy}{dx}.
$$

If we want to solve this equation for $\dfrac{dy}{dx}$, we first rewrite it to

$$
 \left(3y^2-3x\right)\frac{dy}{dx}=3y-3x^2
$$

and then we obtain

$$
 \frac{dy}{dx}=\frac{3y-3x^2}{3y^2-3x}.
$$

We can use this expression to find the point on the curve where the tangent line is horizontal. Note that a horizontal line means a line with slope $0$, so we are looking for a point $(x,y)$ on the curve where $\dfrac{dy}{dx}=0$. This means that we need to find solutions of

$$
 0=\frac{dy}{dx}=\frac{3y-3x^2}{3y^2-3x},
$$

that lie on the curve. Solving $\dfrac{dy}{dx}=0$ gives $3y-3x^2=0$, i.e. $y=x^2$. That would suggest that there would be an entire curve of points where the tangent line is horizontal. This is clearly not the case when we consider a sketch of the curve, see {numref}`Fig:SlopeCurve:Folium`. So what is the issue here? The problem here is that most points on the curve $y=x^2$ do not lie on the folium. So we are actually only interested in those points that satisfy both $x^3+y^3=3xy$ *and* $y=x^2$. In order to find these points, we substitute $y=x^2$ into the equation describing the folium and we obtain

$$
 x^3+x^6=3x^3,
$$

which can be rewritten as

$$
 x^6=2x^3.
$$

Then we must have either $x=0$ or $x^3=2$, which gives $x=\sqrt[3]{2}$. This would give the two points $(0,0)$ and $\left(\sqrt[3]{2},\sqrt[3]{4}\right)$. However, at $(0,0)$ the expression for $\dfrac{dy}{dx}$ does not exist, so we should ignore this point. Indeed, the curve self-intersects at this point, and it is impossible to define a slope there. So the only point on the curve with a horizontal tangent is the point $\left(\sqrt[3]{2},\sqrt[3]{4}\right)$.

:::{applet}
:url: calculus/slopes_of_curves_in_R2/folium_of_Descartes
:name: Fig:SlopeCurve:Folium
:class: dark-light

The folium of Descartes with the point with a horizontal tangent.
:::

::::::

::::{question}
:type: short-answer
:variant: gaps
:showanswer:
:admonition:
:class: question

Consider the curve $\mathcal{C}$ that is shown in {numref}`Fig:SlopesCurves:Polling`.

:::{applet}
:url: calculus/slopes_of_curves_in_R2/dropplet
:name: Fig:SlopesCurves:Polling
:class: dark-light

Some curve $\mathcal{C}$.
:::



Complete the following sentences:
---
M[3]
DS[a vertical tangent;a horizontal tangent;a sharp turn;{self-intersection}]
DS[zero;{an undefined};non-zero]
DS[a vertical tangent;a horizontal tangent;{a sharp turn};self-intersection]
DS[zero;{an undefined};non-zero]
DS[{a vertical tangent};a horizontal tangent;a sharp turn;self-intersection]
DS[zero;{an undefined};non-zero]
DS[a vertical tangent;{a horizontal tangent};a sharp turn;self-intersection]
DS[{zero};an undefined;non-zero]
^^^
? :::{card}
Implicit differentiation can be used to find the slope of the curve at all except {gap} points.

At the point $(-2,3)$ the curve has {gap}, so it has {gap} slope.

At the point $(1,1)$ the curve has {gap}, so it has {gap} slope.

At the point $(2,2)$ the curve has {gap}, so it has {gap} slope.

At the point $(1,4)$ the curve has {gap}, so it has {gap} slope.
:::
---

::::





::::::{prf:example} 
:label: Ex:SlopeCurves:QuotientRule
As a slightly more theoretical application, we can also use implicit differentiation to derive the quotient rule. In {numref}`Section:DiffProdQuot` we derived this rule by combining the product rule and chain rule. 

We write 

$$
 y=\dfrac{f(x)}{g(x)}
$$

for some differentiable functions $f$ and $g$. This equation defines $y$ as an explicit function $x$, but we can turn it into an implicit equation by writing

$$
 g(x)y=f(x).
$$

Since $y$ is a differentiable function of $x$, we can take the derivative of both sides of the equation to find

$$
 \frac{d}{dx}\left(g(x)y\right)=\frac{d}{dx}f(x).
$$

Using the product rule, we obtain

$$
 g'(x)y+g(x)y'(x)=f'(x).
$$

Solving for $y'(x)$, we obtain

$$
 y'(x)=\frac{f'(x)-g'(x)y}{g(x)}=\frac{f'(x)-g'(x)\dfrac{f(x)}{g(x)}}{g(x)}=\frac{f'(x)g(x)-g'(x)f(x)}{\left(g(x)\right)^2},
$$

which is the quotient rule as we have seen in {numref}`Section:DiffProdQuot`.
::::::

## Second derivatives

::::::{prf:example} 
:label: Ex:SlopeCurves:Seconddiv
We can also use implicit differentiation to find second (or higher) order derivatives of curves. For instance, consider the curve that is defined by 

$$
 x^2+xy+y^2=1.
$$

This curve is an ellipse. We can assume that, implicitly, $y$ is a function of $x$, so we can take the derivatives of both sides of the equation to obtain

$$
 \frac{d}{dx}\left(x^2+xy+y^2\right)=\frac{d}{dx}1.
$$

Using the chain rule and the product rule we obtain

$$
 2x+x\frac{dy}{dx}+y+2y\frac{dy}{dx}=0,
$$

from which we can derive that

$$
 \frac{dy}{dx}=\frac{-2x-y}{x+2y}.
$$

Since $y$ is implicitly a function of $x$, $\dfrac{dy}{dx}$ is so as well. So we can use implicit differentiation again to obtain

$$
 \frac{d}{dx}\left(\frac{dy}{dx}\right)=\frac{d}{dx}\left(\frac{-2x-y}{x+2y}\right).
$$

The derivative of $\dfrac{dy}{dx}$ is, by definition, the second derivative $\dfrac{d^2y}{dx^2}$. For the derivative of the right-hand side we use the quotient rule and the chain rule to obtain

$$
\begin{align*}
 \frac{d}{dx}\left(\frac{-2x-y}{x+2y}\right)&=\frac{(x+2y)\left(-2-\frac{dy}{dx}\right)-\left(-2x-y\right)\left(1+2\frac{dy}{dx}\right)}{\left(x+2y\right)^2}\\
 &=\frac{3x\frac{dy}{dx}-3y}{\left(x+2y\right)^2}.
\end{align*}
$$

Combining these expressions, we obtain

$$
 \dfrac{d^2y}{dx^2}=\frac{3x\frac{dy}{dx}-3y}{\left(x+2y\right)^2}.
$$

If we want to find the second derivative at the point $(x,y)=(1,0)$, we first evaluate the first derivative at that point

$$
 \left.\frac{dy}{dx}\right|_{(x,y)=(1,0)}=\left.\frac{-2x-y}{x+2y}\right|_{(x,y)=(1,0)}=\frac{-2\cdot 1- 0}{1+2\cdot 0}=-2
$$

and we can find the second derivative

$$
 \left.\dfrac{d^2y}{dx^2}\right|_{(x,y)=(1,0)}=\left.\frac{3x\frac{dy}{dx}-3y}{\left(x+2y\right)^2}\right|_{(x,y)=(1,0)}=\frac{3\cdot 1\cdot(-2)-3\cdot 0}{\left(1+2\cdot 0\right)^2}=-6.
$$

::::::



## The implicit function theorem

In the previous examples, we have assumed that $y$ is implicitly a differentiable function of $x$, but is that always the case? Unfortunately, this is not always the case. Indeed, we saw in {prf:ref}`Ex:SlopeCurves:Folium` that the expression for $\dfrac{dy}{dx}$ did not exist at the point $(0,0)$, which does lie on the curve. This is because the curve self-intersects at this point, and there is no meaningful way to define a slope there. Similarly, the expression we found for $\dfrac{dy}{dx}$ does not exist at the point $\left(\sqrt[3]{4},\sqrt[3]{2}\right)$, which also lies on the curve. This is because the tangent line to the curve at that point is vertical. 

In addition, the equation

$$
 x^2+y^2=0
$$

only defines the point $(0,0)$ and it is impossible to meaningfully define the slope at a single point. Even worse, we could be dealing with an implicit equation that does not even define a curve. The equation

$$
 x^2+y^2=-1
$$

has no solutions in $\mathbb{R}^2$. So is there a way to know, in advance, whether we can assume that $y$ is implicitly a differentiable function of $x$ on the curve?

The good news is that the answer is yes. This result is a well-known theorem in analysis, called the **implicit function theorem**. The bad news is that proving this result is way beyond our current capabilities. We will state the theorem now, and we will postpone the proof to {numref}`Sec:DE:ExistenceUniqueness`.

::::::{prf:theorem} Implicit function theorem
:label: Thm:SlopeCurves:IFT
Consider a curve that is implicitly defined by an equation $F(x,y)=0$ and let $(x_0,y_0)$ be a point on the curve. Let $g(x)=F(x,y_0)$ and $h(y)=F(x_0,y)$.

If $g$ is continuously differentiable on an open interval containing $x_0$ and $h$ is continuously differentiable on an open interval containing $y_0$ and $h'(y_0)\neq 0$, then there exists a unique differentiable function $k$ with $k(x_0)=y_0$ and $F(x,k(x))=0$ on an open interval containing $x_0$.

That is, on this interval, $y$ is implicitly defined as a differentiable function of $x$.
::::::

This result shows that we can apply implicit differentiation as long as we we can take the derivatives we want to and we subsequently do not divide by $0$ (it should not come as a surprise that we want to avoid dividing by $0$).


## Grasple exercises


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/42c0cf96-2708-4d3c-9adc-35a13e3af9c6?id=63545
:label: Grasple:63545
:dropdown:
:description: Find $\frac{dy}{dx}$ using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/344e4062-1e7c-4ecc-9d90-1ef2ea262e67?id=63540
:label: Grasple:63540
:dropdown:
:description: Find $\frac{dy}{dx}$ using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/90f7561b-3c36-4ef5-853e-2f10cb7f5ebb?id=63553
:label: Grasple:63553
:dropdown:
:description: Find $\frac{dx}{dy}$ using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/508a4c78-deda-406e-b98d-1b99224707ec?id=78670
:label: Grasple:78670
:dropdown:
:description: Find $\frac{dx}{dy}$ using implicit differentiation for a special curve.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2256e591-0a07-49eb-b554-cd7b31f401d9?id=63705
:label: Grasple:63705
:dropdown:
:description: Find a tangent line using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6f1effef-8138-4d33-a52f-459b5b8c90b1?id=63555
:label: Grasple:63555
:dropdown:
:description: Find a tangent line using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6863f9b7-5c6d-461b-8bfc-91f3ff06c1ee?id=63703
:label: Grasple:63703
:dropdown:
:description: Find a tangent line using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5f7a78b4-4431-411b-adac-99f33926d7e2?id=63554
:label: Grasple:63554
:dropdown:
:description: Find a tangent line using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2fec89c1-fefd-457b-9748-4fb4b1b0471b?id=63541
:label: Grasple:63541
:dropdown:
:description: Find a tangent line using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c4f11161-4e6f-4a36-a705-1bd4eaaa006f?id=63612
:label: Grasple:63612
:dropdown:
:description: Find $\frac{dy}{dx}$ using implicit differentiation and find tangent lines.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/30d7d686-5961-44dd-80f8-5a8d21771d88?id=63548
:label: Grasple:63548
:dropdown:
:description: Finding points where curve is horizontal/vertical.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0c946230-7c9a-44cb-9d19-e6e62ecc87bf?id=70903
:label: Grasple:70903
:dropdown:
:description: Find $\frac{dx}{dy}$ and a special point on curve using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/00f1e1c1-4dab-40c3-9abf-c335d4f901ca?id=63546
:label: Grasple:63546
:dropdown:
:description: Find $\frac{d^2y}{dx^2}$ using implicit differentiation.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/369dc541-0a75-4bc7-8790-aefeca644a6c?id=63544
:label: Grasple:63544
:dropdown:
:description: Finding a normal line to a curve.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7165ae8c-b616-447a-b00d-209ab7172463?id=78762
:label: Grasple:78762
:dropdown:
:description: Finding equation for function that intersects curve orthogonally.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8e476818-f913-4b4a-abb9-d8246980afdf?id=78682
:label: Grasple:78682
:dropdown:
:description: Find an angle between two curves.
::::