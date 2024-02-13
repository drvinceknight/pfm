---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Tutorial

We will consider the following problem taken from {cite}`knight2022applied`.

```{admonition} Problem
"£50 of profit can be made on each
tonne of paint A produced, and £60 profit on each tonne of paint B
produced. A tonne of paint A needs 4 tonnes of component X and 5 tonnes of
component Y. A tonne of paint B needs 6 tonnes of component X and 4 tonnes of
component Y. Only 24 tonnes of X and 20 tonnes of Y are available per day. How
much of paint A and paint B should be produced to maximise profit?"
```

As discussed in {cite}`knight2022applied` this can be written in the following
form:

$$
\begin{align}
\text{Maximise: } 50 A + 60 B &  \\
\text{Subject to: } & \nonumber \\
4 A + 6 B &\leq 24  \\
5 A + 4 B &\leq 20
\end{align}
$$

This can be represented using the following matrices and vectors:

$$
\begin{align}
\text{minimise: } c^t x&  \\
\text{subject to: } & \nonumber \\
A_{\text{ub}}x&\leq b_{\text{ub}}\\
\end{align}
$$

with:

$$
c=\begin{pmatrix}-50, -60\end{pmatrix}\qquad
A_{\text{ub}}=\begin{pmatrix}4 & 6\\ 5 & 4\end{pmatrix}\qquad b_{\text{ub}}=\begin{pmatrix}24, 20\end{pmatrix}
$$

and $x=(A, B)$

Problems in this format can be solved using `scipy`. First let us create the
matrices and vectors as {ref}`numpy` arrays:

```{code-cell} ipython3
import numpy as np

c = np.array((-50, -60))
A_ub = np.array(((4, 6), (5, 4)))
b_ub = np.array((24, 20))
```

Now we can solve the linear program:

```{code-cell} ipython3
import scipy.optimize

result = scipy.optimize.linprog(c=c, A_ub=A_ub, b_ub=b_ub)
result
```

The specific solution can be accessed directly:

```{code-cell} ipython3
result.x
```

Indeed, it can be shown theoretically that the optimal result if $A=\frac{12}{7}\approx 1.714$ and $B=\frac{20}{7}\approx 2.857$.

```{important}
In this chapter we have:

- Plotted a scatter plot.
- Add a plot of a line to our scatter plot.
```
