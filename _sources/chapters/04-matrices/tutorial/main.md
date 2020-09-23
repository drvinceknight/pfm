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

We will solve the following problem using a computer to assist with the technical aspects:

```{admonition} Problem

The matrix $A$ is given by $A=\begin{pmatrix}a & 1 & 1\\ 1 & a & 1\\ 1 & 1 & 2\end{pmatrix}$.

1. Find the determinant of $A$
2. Hence find the values of $a$ for which $A$ is singular.
3. For the following values of $a$, when possible obtain $A ^ {- 1}$ and confirm the result by computing $AA^{-1}$:
    1. $a = 0$;
    2. $a = 1$;
    3. $a = 2$;
    4. $a = 3$.

```

Sympy is once again the library we will use for this.

We will start by our matrix $A$:

```{code-cell} ipython3
import sympy as sym

a = sym.Symbol("a")
A = sym.Matrix([[a, 1, 1], [1, a, 1], [1, 1, 2]])
```

We can now create a variable `determinant` and assign it the value of the
determinant of $A$:

```{code-cell} ipython3
determinant = A.det()
determinant
```

A matrix is singular if it has determinant 0. We can find the values of $a$ for
which this occurs:

```{code-cell} ipython3
sym.solveset(determinant, a)
```

Thus it is not possible to find the determinant of $A$ for $a\in\{0, 1\}$.

However for $a = 2$:

```{code-cell} ipython3
A.subs({a: 2})
```

```{code-cell} ipython3
A.subs({a: 2}).inv()
```

To carry out matrix multiplication we use the `@` symbol:

```{code-cell} ipython3
A.subs({a: 2}).inv() @ A.subs({a: 2})
```

and for $a = 3$:

```{code-cell} ipython3
A.subs({a: 3}).inv()
```

```{code-cell} ipython3
A.subs({a: 3}).inv() @ A.subs({a: 3})
```
