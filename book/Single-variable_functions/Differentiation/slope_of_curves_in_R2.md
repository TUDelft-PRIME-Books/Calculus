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

(Subsec:ImplicitDiff)=

## Implicit differentiation



Consider a curve that is implicitly defined by an equation of the form $f(x,y)=0$. If it is possible to turn this into an explicit equation $y=g(x)$ (on at least some part of the curve) we can explicitly find the derivative using regular differentiation techniques. However, in most cases that is not neccesary. We can, instead, work with the assumption that, at least if zoom in enough, it is theoretically possible to obtain an explicit equation $y=g(x)$, but by using the chain rule, we can actually avoid ever having to find this explicit equation. This technique is called **implicit differentiation**. Even for curves where an explicit form can be found (such as for the unit circle) it is typically easier and quicker to use implicit differentiation. This technique is best explained by means of several examples.

::::::{prf:example} 
:label: Ex:SlopeCurves:Circle

[^FootnoteImplicit2]: If you find this step difficult, it might perhaps be useful to pick a few functions for $y$ and see how it works there. For instance, if $y=(3x+1)$, then $y^2=(3x+1)^2$, so by the chain rule we would have $\frac{d}{dx}\left[y^2\right]=\frac{d}{dx}(3x+1)^2=2(3x+1)3=2y\frac{dy}{dx}$. Or, if $y=\sin(x)$, then $y^2=\sin^2(x)$ and by we would obtain $\frac{d}{dx}\left[y^2\right]=\frac{d}{dx}\sin^2(x)=2\sin(x)\cos(x)=2y\frac{dy}{dx}$.

Again consider the unit circle $x^2+y^2=1$ that was discussed in {numref}`Subsec:SlopeCurveIntro`. We will use implicit differentiation to (again) find the slope at $\left(\frac{1}{2},\frac{1}{2}\sqrt{3}\right)$. For this, we take the equation $x^2+y^2=1$ and take the derivative with respect to $x$ of both sides of the equation. This gives

$$
 \frac{d}{dx}\left[x^2+y^2\right]=\frac{d}{dx}[1].
$$

Using our knowledge of differentiation, we can compute several of these terms and we find

$$
 2x+\frac{d}{dx}\left[y^2\right]=0.
$$

This is where the 'implicit' part of implicit differentiation comes in: we assume that, when we zoom in enough, $y$ is a function of $x$, so that $y=y(x)$. Then we can use the chain rule to find the derivative $\frac{d}{dx}\left[y^2\right]$. Indeed, if we write $y^2=f(g(x))$ with $f(x)=x^2$ and $g(x)=y$ then the chain rule gives $\frac{d}{dx}\left[y^2\right]=f'(g(x))g'(x)$. We can quickly commpute $f'(x)=2x$, so $f'(g(x))=f'(y)=2y$, but what about $g'(x)$? Since we have $g(x)=y$, $g'(x)$ is the derivative of $g$, meaning the derivative of $y$. That is, we have $g'(x)=\dfrac{dy}{dx}$. As such, we find $\frac{d}{dx}\left[y^2\right]=2y\frac{dy}{dx}$[^FootnoteImplicit2]. Plugging this back into the equation above, we find

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

Now in order to find $\frac{d}{dx}\left[y^3\right]$ we use the chain rule and we obtain $\frac{d}{dx}\left[y^3\right]=3y^2\frac{dy}{dx}$ (similarly to how we found that $\frac{d}{dx}\left[y^2\right]=2y\frac{dy}{dx}$ in {prf:ref}`Ex:SlopeCurves:Circle`). For $\frac{d}{dx}\left[3xy\right]$, we first use the product rule to find

$$
 \frac{d}{dx}\left[3xy\right]=3y+3x\frac{dy}{dx}.
$$

Here we used that the derivative of $y$ is $\frac{dy}{dx}$ (which is of course what the notation $\frac{dy}{dx}$ means in the first place, but if you see this for the first time it might not be so clear immediately). Combining all of these, we find

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

We can use this expression to find the point on the curve where the tangent line is horizontal. Note that a horizontal line means a line with $0$ slope, so we are looking for a point $(x,y)$ where $\dfrac{dy}{dx}=0$. This means that we need to solve

$$
 0=\frac{dy}{dx}=\frac{3y-3x^2}{3y^2-3x},
$$

which gives $3y-3x^2=0$, i.e. $y=x^2$. That would suggest that there would be an entire curve of points where the tangent line is horizontal. This is clearly not the case when we consider a sketch of the curve, see {numref}`Fig:SlopeCurve:Folium`. So what is the issue here? The problem here is that most points on the curve $y=x^2$ do not lie on the folium. So we are actually only interested in those points that satsify both $x^3+y^3=3xy$ **and** $y=x^2$. In order to find these points, we substitute $y=x^2$ into the equation describing the folium and we obtian

$$
 x^3+x^6=3x^3,
$$

which can be rewritten as

$$
 x^6=2x^3.
$$

Then we must have either $x=0$ or $x^3=2$, which gives $x=\sqrt[3]{2}$. This would give the two points $(0,0)$ and $\left(\sqrt[3]{2},\sqrt[3]{4}\right)$. However, at $(0,0)$ the expression for $\dfrac{dy}{dx}$ does not exist, so we should ignore this point. Indeed, the curve self-intersects at this point, so it is impossible to define a slope there. So the only point on the curve with a horizontal tangent is the point $\left(\sqrt[3]{2},\sqrt[3]{4}\right)$.

:::{todo}
Here sketch of the folium with the point with a horizontal tangent highlighted. Label of figure should be: Fig:SlopeCurve:Folium
:::
::::::

In the previous examples, we have assumed each time that on the curve $y$ is implicitly a differentiable function of $x$, but is that always the case? Unfortunately, this is not always the case. Indeed, we saw in {prf:ref}`Ex:SlopeCurves:Folium` that the expression for $\dfrac{dy}{dx}$ did not exist at the point $(0,0)$, which does lie on the curve. This is because the curve self-intersects at this point, so there is no meaningful way to define a slope there. Similarly, the expression we found for $\dfrac{dy}{dx}$ does not exist at the point $\left(\sqrt[3]{4},\sqrt[3]{2}\right)$, which also lies on the curve. This is because the tangent line to the curve at that point is vertical. 

Even worse, we could be dealing with an implicit equation that does not even define a curve. For instance, the equation

$$
 x^2+y^2=0
$$

only defines the point $(0,0)$ and it is impossible to meaningfully define the slope at a single point. The equation

$$
 x^2+y^2=-1
$$

does not even contain any points at all. So is there a way to know, in advance, whether it is allowed to assume that on the curve $y$ is implicitly a differentiable function of $x$? The good news is that the answer is yes. This result is a very important theorem in analysis, called the **implicit function theorem**. The bad news is that proving this result is way beyond our current capabilities. We will state the theorem now, and we will postpone the proof to {numref}`Sec:DE:ExistenceUniqueness`.

::::::{prf:theorem} Implicit function theorem
:label: Thm:SlopeCurves:IFT
Consider a curve that is implicitly defined by an equation $F(x,y)=0$ and let $(x_0,y_0)$ be a point on the curve. Let $f(x)=F(x,y_0)$ and $g(y)=F(x_0,y)$. If $f$ is continuously differentiable on an open interval containing $x_0$ and $g$ is continuously differentiable on an open interval containing $y_0$ and $g'(y_0)\neq 0$, then there exists a unique differentiable function $h$ with $h(x_0)=y_0$ and $F(x,h(x))=0$ on an open interval containing $x_0$. That is, on this interval, $y$ is implicitly defined as a differentiable function of $x$.
::::::

This result shows that we can apply implicit differentiation as long as we we can take the derivatives we want to and we subsequently do not divide by $0$ (it should not come as a surprise that we want to avoid dividing by $0$).

::::::{prf:example} 
:label: Ex:SlopeCurves:Seconddiv
We can also use implicit differentiation to find second (or higher) order derivatives of curves. For instance, consider the curve that is defined by 

$$
 x^2+2xy+y^2=1.
$$

This curve is an ellipse. We can assume that, implicitly, $y$ is a function of $x$, so we can take the derivatives of both sides of the equation to obtain

$$
 \frac{d}{dx}\left[x^2+2xy+y^2\right]=\frac{d}{dx}[1].
$$

Using the chain rule and the product rule we obtain

$$
 2x+2x\frac{dy}{dx}+2y+2y=0,
$$

from which we can derive that

$$
 \frac{dy}{dx}=\frac{-2x-4y}{2x}=\frac{-x-2y}{x}.
$$

Since $y$ is implicitly a function of $x$, $\dfrac{dy}{dx}$ is so as well. So we can use implicit differentiation again to obtain

$$
 \frac{d}{dx}\left[\frac{dy}{dx}\right]=\frac{d}{dx}\left[\frac{-x-2y}{x}\right].
$$

The derivative of $\dfrac{dy}{dx}$ is, by definition, the second derivative $\dfrac{d^2y}{dx^2}$. For the derivative of the right-hand side we use the quotient rule and the chain rule to obtain

$$
 \frac{d}{dx}\left[\frac{-x-2y}{x}\right]=\frac{x\left(-1-2\frac{dy}{dx}\right)-\left(-x-2y\right)\cdot1}{x^2}=\frac{2y-2\frac{dy}{dx}}{x^2}.
$$

Combining these expressions, we obtain

$$
 \dfrac{d^2y}{dx^2}=\frac{2y-2\frac{dy}{dx}}{x^2}.
$$

If we want to find the second derivative at the point $(x,y)=(1,0)$, we first evaluate the first derivative at that point

$$
 \left.\frac{dy}{dx}\right|_{(x,y)=(1,0)}=\left.\frac{-x-2y}{x}\right|_{(x,y)=(1,0)}=\frac{-1-2\cdot 0}{1}=-1
$$

and we can find the second derivative

$$
 \left.\dfrac{d^2y}{dx^2}\right|_{(x,y)=(1,0)}=\left.\frac{2y-2\frac{dy}{dx}}{x^2}\right|_{(x,y)=(1,0)}=\frac{2\cdot 0-2\cdot 1}{1}=-2.
$$

::::::

## Slopes of parametrised cuves

In {numref}`Section:Curves` we saw that for many curves it is easier or more convenient to describe them using a parametrisation than using an implicit equation. In addition, if you only have a parametrisation of a curve, it can be hard, or even impossible, to turn this into an implicit equation. Still, for those types of curves, we could still want to find the slope. In that case, we have the following result.

::::::{prf:theorem} 
:label: Thm:SlopeCurves:Param
Let $\mathcal{C}$ be curve with parametrisation $x=f(t)$ and $y=g(t)$ for $t_0\leq t\leq t_1$. Suppose $f$ and $g$ are both differentiable. Then for any $t$ with $f'(t)\neq 0$ we have 

$$
 \frac{dy}{dx}=\frac{g'(t)}{f'(t)}.
$$
::::::

::::{admonition} Proof of {prf:ref}`Thm:SlopeCurves:Param`
:class: tudproof, dropdown
We can assume that implicitly $y$ is a function of $x$. Then by the chain rule, we obtain

$$
 \frac{dy}{dt}=\frac{dy}{dx}\frac{dx}{dt}.
$$

By dividing by $\frac{dx}{dt}$ (assuming it is nonzero), we obtain

$$
 \frac{dy}{dx}=\frac{\frac{dy}{dt}}{\frac{dx}{dt}}=\frac{g'(t)}{f'(t)}.
$$
::::


::::::{prf:example} 
:label: Ex:SlopeCurves:Param
Let $\mathcal{C}$ be curve with parametrisation $x=e^{2t}-e^t$ and $y=e^{3t}+4e^{-2t}$ for $-1\leq t\leq 1$. Suppose we want to find the slope at $t=0$, i.e. at the point $(x,y)=\left(1,5\right)$. It does not seem feasible to find an implicit equation for this curve and to use implicit differentiaton, so we will use {prf:ref}`Thm:SlopeCurves:Param`. Using this theorem, we find

$$
 \frac{dy}{dx}=\frac{\frac{d}{dt}\left[e^{3t}+4e^{-2t}\right]}{\frac{d}{dt}\left[e^{2t}-e^t\right]}=\frac{3e^{3t}-8e^{-2t}}{2e^{2t}-e^t}.
$$

Plugging in $t=0$ gives

$$
 \left.\frac{dy}{dx}\right|_{(x,y)=(1,5)}=\frac{3e^{3\cdot 0}-8e^{-2\cdot 0}}{2e^{2\cdot 0}-e^0}=\frac{-5}{1}=-5.
$$

:::{todo}
Show curve with the specified point highlighted, including the tangent line there.
:::
::::::

::::::{prf:example} 
:label: Ex:SlopeCurves:ParamVert
Let $\mathcal{C}$ be curve with parametrisation $x=t^2+2t$ and $y=t^3$ for $-2\leq t\leq 2$. Suppose we want to find all points on the curve where the tangent line is vertical. A vertical tangent line means that we are dealing with an "infinite slope". For most values of $t$, the slope is given by 

$$
 \frac{dy}{dx}=\frac{\frac{d}{dt}\left[t^3\right]}{\frac{d}{dt}\left[t^2+2t\right]}=\frac{3t^2}{2t+2}.
$$

We see that for $t\neq -1$ this slope is a well-defined number, so there will be no vertical tangent lines for those values of $t$. However, we see that

$$
 \lim_{t\rightarrow -1}\left|\frac{3t^2}{2t+2}\right|=\infty,
$$

since the numerator goes to $3$ while the denominator goes to $0$ as $t\rightarrow -1$. As such, we obtain a vertical tangent line whenever $t=-1$, which corresponds to the point $(-1,-1)$.
:::{todo}
Show curve with the specified point highlighted, including the tangent line there.
:::
::::::
