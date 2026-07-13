# Multivariable integrals

In this section we cover:

- Multivariable integrals
- Improper multivariable integrals (discontinuous integrand)
- Coordinate transformations in $\mathbb{R}^n$
  - Link with substitution rule for single variable integrals

## The Riemann zeta function

In {numref}`Sec:MultivariableIntegration:RiemannZetaFunction1` and {numref}`Sec:MultivariableIntegration:RiemannZetaFunction2` we obtained that

$$
\int_0^1\int_0^1\frac{dx\,dy}{1-xy}=\zeta(2)=\frac{1}{6}\pi^2\quad\text{and}\quad\int_0^1\int_0^1\int_0^1\frac{dx\,dy\,dz}{1-xyz}=\zeta(3).
$$

Similarly, using the series representation $\displaystyle\frac{1}{1-wxyz}=\sum_{n=0}^{\infty}(wxyz)^n$ for $|wxyz|<1$ we obtain

\begin{align*}
\int_0^1\int_0^1\int_0^1\int_0^1\frac{dw\,dx\,dy\,dz}{1-wxyz}&=\int_0^1\int_0^1\int_0^1\int_0^1\sum_{n=0}^{\infty}(wxyz)^n\,dw\,dx\,dy\,dz\\
&=\sum_{n=0}^{\infty}\left(\int_0^1w^n\,dw\right)\left(\int_0^1x^n\,dx\right)\\
&{}\quad\quad{}\times\left(\int_0^1y^n\,dy\right)\left(\int_0^1z^n\,dz\right)\\
&=\sum_{n=0}^{\infty}\frac{1}{(n+1)^4}\\
&=\sum_{n=1}^{\infty}\frac{1}{n^4}\\
&=\zeta(4)\\
&=\frac{1}{90}\pi^4.
\end{align*}

In {numref}`Sec:MultivariableIntegration:RiemannZetaFunction1` and {numref}`Sec:MultivariableIntegration:RiemannZetaFunction2` we also obtained that

$$
\int_0^1\int_0^1\frac{dx\,dy}{1-x^2y^2}=\frac{3}{4}\zeta(2)=\frac{1}{8}\pi^2\quad\text{and}\quad\int_0^1\int_0^1\int_0^1\frac{dx\,dy\,dz}{1-x^2y^2z^2}=\frac{7}{8}\zeta(3).
$$

Similarly, using the series representation $\displaystyle\frac{1}{1-w^2x^2y^2z^2}=\sum_{n=0}^{\infty}(wxyz)^{2n}$ for $|wxyz|<1$ and {eq}`Eq:Series:RiemannZetaFunction1` we obtain

\begin{align*}
\int_0^1\int_0^1\int_0^1\int_0^1\frac{dx\,dy\,dz}{1-w^2x^2y^2z^2}&=\int_0^1\int_0^1\int_0^1\int_0^1\sum_{n=0}^{\infty}(wxyz)^{2n}\,dw\,dx\,dy\,dz\\
&=\sum_{n=0}^{\infty}\left(\int_0^1w^{2n}\,dw\right)\left(\int_0^1x^{2n}\,dx\right)\\
&{}\quad\quad{}\times\left(\int_0^1y^{2n}\,dy\right)\left(\int_0^1z^{2n}\,dz\right)\\
&=\sum_{n=0}^{\infty}\frac{1}{(2n+1)^4}\\
&=\left(1-\frac{1}{16}\right)\zeta(4)\\
&=\frac{15}{16}\zeta(4)\\
&=\frac{15}{16}\cdot\frac{1}{90}\pi^4\\
&=\frac{1}{96}\pi^4.
\end{align*}
