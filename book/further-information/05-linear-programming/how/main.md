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

# How

## How to solve a linear program using `scipy`

A general linear program of the form

$$
\begin{aligned}
\text{minimise: } c^t x&  \\
\text{subject to: } & \nonumber \\
A_{\text{ub}}x&\leq b_{\text{ub}}\\
A_{\text{eq}}x&= b_{\text{eq}}\\
\end{aligned}
$$

can be solved using:

````{tip}
```
scipy.optimize.linprog(c, A_ub, b_ub, A_eq, b_eq)
```
````

For example:

```{code-cell} ipython3
import numpy as np
import scipy.optimize

c = np.array((-2, -2, -3, -1))
A_ub = np.array(
        [[2, -3, -3, 1], [3, 4, 1, 1], [-2, 1, 1, 1]]
    )
b_ub = np.array([[3], [2], [1]])
A_eq = np.array([[1, 1, 2, 1]])
b_eq = np.array([1])

scipy.optimize.linprog(c=c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq)
```
