# Special substitutions

In the method of integration by substitution from {numref}`Sec:Integration:Substitution` we learned that you have to choose a suitable substitution in order to simplify the integral. In this section we will discuss two special substitutions that are often used in practice: **trigonometric substitutions** and the **midpoint mirror substitution**.

## Trigonometric substitutions

For certain integrals involving square roots of the form $\sqrt{a^2-x^2}$, $\sqrt{a^2+x^2}$ or $\sqrt{x^2-a^2}$ we might use a **trigonometric substitution** in order to get rid of the square root. This will lead to integrals involving trigonometric functions, which will be treated in the section on integration of trigonometric functions. However, here we will show how the method of trigonometric substitution works.

Note that $1-\sin^2(x)=\cos^2(x)$. So if we set $x=a\sin(t)$ in $\sqrt{a^2-a^2}$ we obtain 

$$
\sqrt{a^2-a^2\sin^2(t)}=\sqrt{a^2\cos^2(t)}=|a\cos(t)|.
$$

Combined with $dx=a\cos(t)\,dt$ this leads to an integral involving trigonometric functions.

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample1
We want to determine $\displaystyle\int_{-1}^1\sqrt{1-x^2}\,dx$.

Let $x=\sin(t)$, then we have $dx=\cos(t)\,dt$. Furthermore, if $x=-1$ then $t=-\frac{1}{2}\pi$ and if $x=1$ then $t=\frac{1}{2}\pi$. Hence we find that

$$
\int_{-1}^1\sqrt{1-x^2}\,dx=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}|\cos(t)|\cos(t)\,dt.
$$

Note that $\cos(t)\geq0$ for $-\frac{1}{2}\pi\leq t\leq\frac{1}{2}\pi$. Using $\cos^2(t)=\frac{1}{2}(1+\cos(2t))$ we then obtain

$$
\begin{align*}
\int_{-1}^1\sqrt{1-x^2}\,dx&=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\cos^2(t)\,dt=\frac{1}{2}\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}(1+\cos(2t))\,dt\\
&=\bigg[\frac{1}{2}t+\frac{1}{4}\sin(2t)\bigg]_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}=\frac{1}{2}\pi.
\end{align*}
$$

::::::

:::{prf:remark}
:label: Remark:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample1Remark

The integral of {prf:ref}`Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample1` denotes the area of the upper half of the unit circle.
:::

Instead of using the substitution $x=a\sin(t)$ we may also use the substitution $x=a\cos(t)$, which leads to $dx=-a\sin(t)\,dt$ and 

$$
\sqrt{a^2-x^2}=\sqrt{a^2-a^2\cos^2(t)}=\sqrt{a^2\sin^2(t)}=|a\sin(t)|.
$$ 

::::{exercise}
:label: Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution1
Evaluate $\displaystyle\int_{-1}^1\sqrt{1-x^2}\,dx$ using the substitution $x=\cos(t)$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution1`
:class: solution, dropdown
Let $x=\cos(t)$, then we have $dx=-\sin(t)\,dt$. Furthermore, if $x=-1$ then $t=\pi$ and if $x=1$ then $t=0$. Hence we find that

$$
\int_{-1}^1\sqrt{1-x^2}\,dx=-\int_{\pi}^0|\sin(t)|\sin(t)\,dt=\int_0^{\pi}|\sin(t)|\sin(t)\,dt.
$$

Note that $\sin(t)\geq0$ for $0\leq t\leq\pi$. Using $\sin^2(t)=\frac{1}{2}(1-\cos(2t))$ we then obtain

$$
\begin{align*}
\int_{-1}^1\sqrt{1-x^2}\,dx&=\int_0^{\pi}\sin^2(t)\,dt=\frac{1}{2}\int_0^{\pi}(1-\cos(2t))\,dt\\
&=\bigg[\frac{1}{2}t-\frac{1}{4}\sin(2t)\bigg]_0^{\pi}=\frac{1}{2}\pi.
\end{align*}
$$

:::

::::{exercise}
:label: Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution2
Evaluate $\displaystyle\int_{-1}^1x^2\sqrt{1-x^2}\,dx$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution2`
:class: solution, dropdown
Let $x=\sin(t)$, then we have $dx=\cos(t)\,dt$. Furthermore, if $x=-1$ then $t=-\frac{1}{2}\pi$ and if $x=1$ then $t=\frac{1}{2}\pi$. Hence we find that

$$
\int_{-1}^1x^2\sqrt{1-x^2}\,dx=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\sin^2(t)|\cos(t)|\cos(t)\,dt
=\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\sin^2(t)\cos^2(t)\,dt.
$$

Now we use $\sin(2t)=2\sin(t)\cos(t)$ to find 

$$
\int_{-1}^1x^2\sqrt{1-x^2}\,dx=\frac{1}{4}\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}\sin^2(2t)\,dt.
$$

Finally, we have $\sin^2(2t)=\frac{1}{2}(1-\cos(4t))$ which leads to

$$
\begin{align*}
\int_{-1}^1x^2\sqrt{1-x^2}\,dx&=\frac{1}{8}\int_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}(1-\cos(4t))\,dt\\
&=\bigg[\frac{1}{8}t-\frac{1}{32}\sin(4t)\bigg]_{-\frac{1}{2}\pi}^{\frac{1}{2}\pi}=\frac{1}{8}\pi.
\end{align*}
$$

:::

For $\sqrt{a^2+x^2}$ we use the fact that for $x=a\tan(t)$ we have

$$
\sqrt{a^2+x^2}=\sqrt{a^2(1+\tan^2(x))}=\sqrt{\frac{a^2}{\cos^2(t)}}=\left|\frac{a}{\cos(t)}\right|.
$$

Combined with $dx=\dfrac{a}{\cos^2(t)}\,dt$ this will also give rise to an integral involving trigonometric functions.

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample2
Evaluate $\displaystyle\int_0^1\frac{1}{\sqrt{1+x^2}}\,dx$.

Solution. Let $x=\tan(t)$, then we have $dx=\dfrac{dt}{\cos^2(t)}$. Furthermore, if $x=0$ then $t=0$ and if $x=1$ then $t=\frac{1}{4}\pi$. Hence we find that

$$
\int_0^1\frac{1}{\sqrt{1+x^2}}\,dx=\int_0^{\frac{1}{4}\pi}|\cos(t)|\frac{1}{\cos^2(t)}\,dt.
$$

Note that $\cos(t)\geq0$ for $0\leq t\leq\frac{1}{4}\pi$. Hence we have

$$
\int_0^1\frac{1}{\sqrt{1+x^2}}\,dx=\int_0^{\frac{1}{4}\pi}\frac{dt}{\cos(t)}.
$$

In 1668 the Scottish mathematician [James Gregory (1638-1675)](https://en.wikipedia.org/wiki/James_Gregory_(mathematician)) discovered that

$$
\int\frac{dt}{\cos(t)}=\ln\left|\tan(t)+\frac{1}{\cos(t)}\right|+C.
$$



We conclude that

$$
\int_0^{\frac{1}{4}\pi}\frac{1}{\cos(t)}\,dt=\left[\ln\left|\tan(t)+\frac{1}{\cos(t)}\right|\right]_0^{\frac{1}{4}\pi}=\ln(1+\sqrt{2}).
$$

and therefore $\displaystyle\int_0^1\frac{1}{\sqrt{1+x^2}}\,dx=\ln(1+\sqrt{2})$.
::::::

:::{prf:theorem}
:label: Theorem:Integration:GregoryIntegral

$$
\int\frac{dt}{\cos(t)}=\int\frac{du}{u}=\ln|u|+C=\ln\left|\tan(t)+\frac{1}{\cos(t)}\right|+C.
$$

:::

:::{admonition} Proof of {prf:ref}`Theorem:Integration:GregoryIntegral`
:class: tudproof, dropdown

This can be shown as follows

$$
\int\frac{dt}{\cos(t)}=\int\frac{1}{\cos(t)}\cdot\frac{\tan(t)+\dfrac{1}{\cos(t)}}{\tan(t)+\dfrac{1}{\cos(t)}}\,dt=\int\frac{\dfrac{\tan(t)}{\cos(t)}+\dfrac{1}{\cos^2(t)}}{\tan(t)+\dfrac{1}{\cos(t)}}\,dt.
$$

Now we set $u=\tan(t)+\dfrac{1}{\cos(t)}$ which implies that

$$
\frac{du}{dt}=\frac{1}{\cos^2(t)}-\frac{1}{\cos^2(t)}\cdot(-\sin(t))=\frac{1}{\cos^2(t)}+\frac{\tan(t)}{\cos(t)}.
$$

Hence we have $du=\left(\dfrac{1}{\cos^2(t)}+\dfrac{\tan(t)}{\cos(t)}\right)\,dt$. Thus

$$
\int\frac{dt}{\cos(t)}=\int\frac{du}{u}=\ln|u|+C=\ln\left|\tan(t)+\frac{1}{\cos(t)}\right|+C.
$$

:::

::::{exercise}
:label: Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution3
Evaluate $\displaystyle\int_0^1\frac{1}{1+x^2}\,dx$ using the substitution $x=\tan(t)$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionDefiniteIntegralTrigSubstitution3`
:class: solution, dropdown
Let $x=\tan(t)$, then we have $dx=\left(1+\tan^2(t)\right)\,dt$. Furthermore, if $x=0$ then $t=0$ and if $x=1$ then $t=\frac{1}{4}\pi$. Hence we find that

$$
\int_0^1\frac{1}{1+x^2}\,dx=\int_0^{\frac{1}{4}\pi}\frac{1}{1+\tan^2(t)}\left(1+\tan^2(t)\right)\,dt=\int_0^{\frac{1}{4}\pi}1\,dt=\frac{1}{4}\pi.
$$

*Remark*: Of course, it is easier to evaluate the integral directly using the fundamental theorem of calculus (see: {prf:ref}`Ex:Integration:FundamentalTheoremPart2Example3`).

:::

In the case of $\sqrt{x^2-a^2}$ we use the substitution $x=\dfrac{a}{\cos(t)}$. Then we have $dx=\dfrac{a\sin(t)}{\cos^2(t)}$ and

$$
\sqrt{x^2-a^2}=\sqrt{\frac{a^2}{\cos^2(t)}-a^2}=\sqrt{\frac{a^2-a^2\cos^2(t)}{\cos^2(t)}}=\sqrt{\frac{a^2\sin^2(t)}{\cos^2(t)}}=|a\tan(t)|.
$$

::::::{prf:Example}
:label: Ex:Integration:SubstitutionDefiniteIntegralTrigSubstitutionExample3
Evaluate $\displaystyle\int_0^{\sqrt{2}}\sqrt{x^2-1}\,dx$.

Solution. Let $x=\dfrac{1}{\cos(t)}$, then we have $dx=\dfrac{\sin(t)}{\cos^2(t)}\,dt$. Furthermore, if $x=1$ then $t=0$ and if $x=\sqrt{2}$ then $t=\frac{1}{4}\pi$. Hence we find that

$$
\begin{align*}
\int_0^{\sqrt{2}}\sqrt{x^2-1}\,dx&=\int_0^{\frac{1}{4}\pi}|\tan(t)|\frac{\sin(t)}{\cos^2(t)}\,dt=\int_0^{\frac{1}{4}\pi}\frac{\sin^2(t)}{\cos^3(t)}\,dt\\
&=\int_0^{\frac{1}{4}\pi}\frac{\sin^2(t)}{\cos^4(t)}\cos(t)\,dt.
\end{align*}
$$

Now we use $\cos^2(t)=1-\sin^2(t)$ and the substitution $u=\sin(t)$ to find that

$$
\int_0^{\frac{1}{4}\pi}\frac{\sin^2(t)}{\cos^4(t)}\cos(t)\,dt=\int_0^{\frac{1}{2}\sqrt{2}}\frac{u^2}{(1-u^2)^2}\,du.
$$

Then we use the partial fraction decomposition (see {numref}`sec:PartialFractionDecomposition`)

$$
\frac{u^2}{(1-u^2)^2}=\frac{1}{4}\left(-\frac{1}{1-u}+\frac{1}{(1-u)^2}-\frac{1}{1+u}+\frac{1}{(1+u)^2}\right),
$$

to find that

$$
\begin{align*}
&\int_0^{\frac{1}{2}\sqrt{2}}\frac{u^2}{(1-u^2)^2}\,du\\
&=\frac{1}{4}\int_0^{\frac{1}{2}\sqrt{2}}\left(-\frac{1}{1-u}+\frac{1}{(1-u)^2}-\frac{1}{1+u}+\frac{1}{(1+u)^2}\right)\,dt\\
&=\frac{1}{4}\bigg[\ln|1-u|+\frac{1}{1-u}-\ln|1+u|-\frac{1}{1+u}\bigg]_0^{\frac{1}{2}\sqrt{2}}\\
&=\frac{1}{4}\left(\ln(1-\tfrac{1}{2}\sqrt{2})+\frac{1}{1-\frac{1}{2}\sqrt{2}}-\ln(1+\tfrac{1}{2}\sqrt{2})-\frac{1}{1+\frac{1}{2}\sqrt{2}}\right)\\
&=\frac{1}{4}\ln\left(\frac{2-\sqrt{2}}{2+\sqrt{2}}\right)+\frac{1}{2}\sqrt{2}.
\end{align*}
$$

::::::

:::{prf:example} Serret's integral

Consider the integral $\displaystyle\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx$, which is named after the French mathematician [Joseph Alfred Serret (1819-1885)](https://en.wikipedia.org/wiki/Joseph-Alfred_Serret).

One way to evaluate the integral is by using the substitution $x=\tan(\theta)$:

$$
\begin{align*}
\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx&=\int_0^{\frac{1}{4}\pi}\ln\left(1+\tan(\theta)\right)\,d\theta=\int_0^{\frac{1}{4}\pi}\ln\left(\frac{\cos(\theta)+\sin(\theta)}{\cos(\theta)}\right)\,d\theta\\
&=\int_0^{\frac{1}{4}\pi}\left(\ln\left(\cos(\theta)+\sin(\theta)\right)-\ln\left(\cos(\theta)\right)\right)\,d\theta.
\end{align*}
$$

Now we use $\cos(\theta)+\sin(\theta)=\sqrt{2}\cos(\theta-\frac{1}{4}\pi)$ (see exercise 2) to obtain

$$
\begin{align*}
\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx&=\int_0^{\frac{1}{4}\pi}\left(\ln\left(\sqrt{2}\cos(\theta-\tfrac{1}{4}\pi)\right)-\ln\left(\cos(\theta)\right)\right)\,d\theta\\
&=\int_0^{\frac{1}{4}\pi}\left(\ln\left(\sqrt{2}\right)+\ln\left(\cos\left(\theta-\tfrac{1}{4}\pi\right)-\ln\left(\cos(\theta)\right)\right)\right)\,d\theta.
\end{align*}
$$

Finally, the substitution $t=\frac{1}{4}\pi-\theta$ or $\theta=\frac{1}{4}\pi-t$ shows that

$$
\int_0^{\frac{1}{4}\pi}\ln\left(\cos\left(\theta-\tfrac{1}{4}\pi\right)\right)\,d\theta=-\int_{\frac{1}{4}\pi}^0\ln\left(\cos(t)\right)\,dt=\int_0^{\frac{1}{4}\pi}\ln\left(\cos(t)\right)\,dt,
$$

which implies that

$$
\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx=\frac{1}{4}\pi\ln\left(\sqrt{2}\right)=\frac{1}{8}\pi\ln(2).
$$

In this evaluation we obtained that

$$
\begin{align*}
&\int_0^{\frac{1}{4}\pi}\ln\left(\cos\left(\theta-\tfrac{1}{4}\pi\right)\right)\,d\theta=\int_0^{\frac{1}{4}\pi}\ln\left(\cos(t)\right)\,dt\\
&{}\quad\Longrightarrow\quad\int_0^{\frac{1}{4}\pi}\left(\ln\left(\cos\left(\theta-\tfrac{1}{4}\pi\right)-\ln\left(\cos(\theta)\right)\right)\right)\,d\theta=0.
\end{align*}
$$

The value of the integral $\displaystyle\int_0^{\frac{1}{4}\pi}\ln\left(\cos(t)\right)\,dt$ is closely related to *Catalan's constant*, which will be considered later in {numref}`sec:CatalansConstant`. 

:::

::::{exercise}
:label: Exc:Integration:SubstitutionTrigForm
Show that $\cos(\theta)+\sin(\theta)=\sqrt{2}\cos(\theta-\frac{1}{4}\pi)$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionTrigForm`
:class: solution, dropdown
Using $\cos(x-y)=\cos(x)\cos(y)+\sin(x)\sin(y)$ we obtain

$$
\cos(\theta-\tfrac{1}{4}\pi)=\cos(\theta)\cos(\tfrac{1}{4}\pi)+\sin(\theta)\sin(\tfrac{1}{4}\pi)=\tfrac{1}{2}\sqrt{2}\cos(\theta)+\tfrac{1}{2}\sqrt{2}\sin(\theta).
$$

Multiplying by $\sqrt{2}$ we find that

$$
\sqrt{2}\cos(\theta-\tfrac{1}{4}\pi)=\cos(\theta)+\sin(\theta).
$$

:::

## Midpoint mirror substitution

Using the substitution $x=a+b-t$ or $t=a+b-x$ we obtain that a definite integral of the form $I=\displaystyle\int_a^b\frac{f(x)}{f(x)+f(a+b-x)}\,dx$ can be evaluated as follows. First apply the substitution:

$$
\begin{align*}
I=\int_a^b\frac{f(x)}{f(x)+f(a+b-x)}\,dx&=-\int_b^a\frac{f(a+b-t)}{f(a+b-t)+f(t)}\,dt\\
&=\int_a^b\frac{f(a+b-t)}{f(a+b-t)+f(t)}\,dt.
\end{align*}
$$

This implies that, using a change of variable back to $x$ in the last integral,

$$
I=\int_a^b\frac{f(x)}{f(x)+f(a+b-x)}\,dx=\int_a^b\frac{f(a+b-x)}{f(a+b-x)+f(x)}\,dx.
$$

Hence we have

$$
2I=\int_a^b\frac{f(x)}{f(x)+f(a+b-x)}\,dx+\int_a^b\frac{f(a+b-x)}{f(a+b-x)+f(x)}\,dx=\int_a^b1\,dx=b-a,
$$

which implies that

$$
\int_a^b\frac{f(x)}{f(x)+f(a+b-x)}\,dx=\frac{b-a}{2}.
$$

:::{prf:remark}
:label: Remark:Integration:SubstitutionNiceFormula

We call the substitution $x=a+b-t$ or $t=a+b-x$ the **midpoint mirror substitution** because it mirrors the interval $[a,b]$ around the midpoint $\frac{a+b}{2}$ of the interval.
:::

::::::{prf:Example}
:label: Ex:Integration:SubstitutionNiceFormula1
For $a=0$, $b=1$ and $f(x)=\sqrt{x}$ we obtain

$$
\int_0^1\frac{\sqrt{x}}{\sqrt{x}+\sqrt{1-x}}\,dx=\frac{1-0}{2}=\frac{1}{2}.
$$

::::::

:::{prf:remark}
:label: Remark:Integration:GraspleExercise

Grasple-opgave met varianten: $\displaystyle\int_a^b\frac{\sqrt{x}}{\sqrt{x}-\sqrt{a+b-x}}\,dx=\frac{b-a}{2}$ met $a\in\{0,1,2,3,4,5,6,7,8\}$ en $b\in\{1,2,3,4,5,6,7,8,9\}$ met $a<b$ (met uitzondering van $a=0$ en $b=1$).
:::


::::::{prf:Example}
:label: Ex:Integration:SubstitutionNiceFormula2
For $a=0$, $b=\frac{1}{2}\pi$ and $f(x)=\sin(x)$ we obtain

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\frac{\sin(x)}{\sin(x)+\cos(x)}\,dx&=\int_0^{\frac{1}{2}\pi}\frac{\sin(x)}{\sin(x)+\sin(\frac{1}{2}\pi-x)}\,dx\\
&=\frac{\frac{1}{2}\pi-0}{2}=\frac{1}{4}\pi.
\end{align*}
$$

::::::

:::{prf:remark}
:label: Remark:Integration:GraspleExercise2

Grasple-opgave met varianten: $\displaystyle\int_0^{\frac{1}{2}\pi}\frac{(\sin(x))^a}{(\sin(x))^a+(\cos(x))^a}\,dx=\frac{\frac{1}{2}\pi-0}{2}=\tfrac{1}{4}\pi$ met $a\in\{1/2,2,3,4,5\}$.
:::


::::{exercise}
:label: Exc:Integration:SubstitutionNiceFormula
Evaluate $\displaystyle\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\tan(x)}$.
::::

:::{admonition} Solution of {numref}`Exc:Integration:SubstitutionNiceFormula`
:class: solution, dropdown

$$
\begin{align*}
\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\tan(x)}&=\int_0^{\frac{1}{2}\pi}\frac{dx}{1+\dfrac{\sin(x)}{\cos(x)}}=\int_0^{\frac{1}{2}\pi}\frac{\dfrac{1}{\sin(x)}}{\dfrac{1}{\sin(x)}+\dfrac{1}{\cos(x)}}\,dx\\
&=\frac{\frac{1}{2}\pi-0}{2}=\frac{1}{4}\pi.
\end{align*}
$$

:::