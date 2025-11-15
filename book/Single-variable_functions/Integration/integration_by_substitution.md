# Integration by substitution

In this section we cover:

- Integration by substitution for indefinite integrals
- Integration by substitution for definite integrals
- Even and odd functions

The method of **substitution** is based on the chain rule:
```{math}
\frac{d}{dx}F(g(x))=F'(g(x))g'(x).
```
This implies that
```{math}
\int f(g(x))g'(x)\,dx=F(g(x))+C\quad\text{with}\quad F'=f.
```
This leads to the following theorem:
::::::{prf:Theorem} Substitution in indefinite integrals
:label: Thm:Integration:SubstitutionIndefiniteIntegral
If $u=g(x)$ is a differentiable function whose range is an interval $I$ and $f$ is continuous on $I$, then
```{math}
\int f(g(x))g'(x)\,dx=\int f(u)\,du.
```
**Note**: if $u=g(x)$, then $du=g'(x)\,dx$.
::::::

::::::{prf:Example}
Consider $\displaystyle\int\cos(x)e^{\sin(x)}\,dx$.

If we set $u=\sin(x)$, we obtain that $du=\cos(x)\,dx$. Hence, we find that
```{math}
\int\cos(x)e^{\sin(x)}\,dx=\int e^u\,du=e^u+C=e^{\sin(x)}+C.
```
::::::

::::::{prf:Example}
Consider $\displaystyle\int\frac{x}{1+x^2}\,dx$.

If we set $u=1+x^2$, we obtain that $du=2x\,dx$ or $x\,dx=\dfrac{1}{2}\,du$. Hence, we find that
```{math}
\int\frac{x}{1+x^2}\,dx=\frac{1}{2}\int\frac{1}{u}\,du=\frac{1}{2}\ln|u|+C=\frac{1}{2}\ln(1+x^2)+C.
```
::::::

::::::{prf:Example}
Consider $\displaystyle\int\frac{1}{(1+x)\sqrt{x}}\,dx$.

If we set $u=\sqrt{x}$ (or $x=u^2$), we obtain that $du=\dfrac{1}{2\sqrt{x}}\,dx$ or $\dfrac{1}{\sqrt{x}}\,dx=2\,du$. Hence, we find that
```{math}
\int\frac{1}{(1+x)\sqrt{x}}\,dx=2\int\frac{1}{1+u^2}\,du=2\arctan(u)+C=2\arctan(\sqrt{x})+C.
```
::::::

::::::{prf:Theorem} Substitution in definite integrals
:label: Thm:Integration:SubstitutionDefiniteIntegral
If $g'$ is continuous on $[a,b]$ and $f$ is continuous on the range of $u=g(x)$, then
```{math}
\int_a^b f(g(x))g'(x)\,dx=\int_{g(a)}^{g(b)} f(u)\,du.
```
**Note**: if $x=a$ then $u=g(a)$, and if $x=b$ then $u=g(b)$.
::::::

::::::{prf:Example}
Evaluate $\displaystyle\int_1^e\frac{\ln(x)}{x}\,dx$.

Solution. If we set $u=\ln(x)$, then we have $du=\dfrac{1}{x}\,dx$. Furthermore, we have: if $x=1$ then $u=0$, and if $x=e$ then $u=1$. Hence, we find that
```{math}
\int_1^e\frac{\ln(x)}{x}\,dx=\int_0^1u\,du=\frac{1}{2}u^2\bigg|_0^1=\frac{1}{2}.
```
::::::

::::::{prf:Example}
Evaluate $\displaystyle\int_1^4\frac{e^{\sqrt{x}}}{\sqrt{x}}\,dx$.

Solution. If we set $u=\sqrt{x}$, then we have $du=\dfrac{1}{2\sqrt{x}}\,dx$ or $\dfrac{1}{\sqrt{x}}\,dx=2\,du$. Furthermore, we have: if $x=1$ then $u=1$, and if $x=4$ then $u=2$. Hence, we find that
```{math}
\int_1^4\frac{e^{\sqrt{x}}}{\sqrt{x}}\,dx=2\int_1^2e^u\,du=2e^u\bigg|_1^2=2e^2-2e=2e(e-1).
```
::::::

## Grasple exercises

64141, 64618, 64879, 75957, 64878, 64599, 64834, 65945, 64831, 64653, 64660, 64601, 64825, 64652, 64835, 64850, 64648, 64830, 64826, 64832, 64827, 64881, 75951, 64877