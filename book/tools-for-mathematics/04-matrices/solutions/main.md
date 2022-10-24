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

# Solutions

## Question 1

> `1`. Obtain the determinant and the inverses of the following matrices:

> `1`. $A = \begin{pmatrix} 1 / 5 & 1\\1 & 1\end{pmatrix}$

```{code-cell} ipython3
import sympy as sym

A = sym.Matrix([[sym.S(1) / 5, 1], [1, 1]])
A.det()
```

```{code-cell} ipython3
A.inv()
```

> `2`. $B = \begin{pmatrix} 1 / 5 & 1 & 5\\3 & 1 & 6 \\ 1 & 2 & 1\end{pmatrix}$

```{code-cell} ipython3
B = sym.Matrix([[sym.S(1) / 5, 1, 5], [3, 1, 6], [1, 2, 1]])
B.det()
```

```{code-cell} ipython3
B.inv()
```

> `3`. $C = \begin{pmatrix} 1 / 5 & 5 & 5\\3 & 1 & 7 \\ a & b & c\end{pmatrix}$

```{code-cell} ipython3
a, b, c = sym.Symbol("a"), sym.Symbol("b"), sym.Symbol("c")
C = sym.Matrix([[sym.S(1) / 5, 5, 5], [3, 1, 7], [a, b, c]])
C.det()
```

```{code-cell} ipython3
C.inv()
```

## Question 2

> `2`. Compute the following:

> `1`. $500\begin{pmatrix} 1 / 5 & 1\\1 & 1\end{pmatrix}$

```{code-cell} ipython3
A = 500 * sym.Matrix([[sym.S(1) / 5, 1], [1, 1]])
A
```

> `2`. $\pi \begin{pmatrix} 1 / \pi & 2\pi\\3/\pi & 1\end{pmatrix}$

```{code-cell} ipython3
B = sym.pi * sym.Matrix([[1 / sym.pi, 2 * sym.pi], [3 / sym.pi, 1]])
B
```

> `3`. $500\begin{pmatrix} 1 / 5 & 1\\1 & 1\end{pmatrix} + \pi \begin{pmatrix} 1 / \pi & 2\pi\\3/\pi & 1\end{pmatrix}$

```{code-cell} ipython3
A + B
```

> `4`. $500\begin{pmatrix} 1 / 5 & 1\\1 & 1\end{pmatrix}\begin{pmatrix} 1 / \pi & 2\pi\\3/\pi & 1\end{pmatrix}$

```{code-cell} ipython3
C = sym.Matrix([[1 / sym.pi, 2 * sym.pi], [3 / sym.pi, 1]])
A @ C
```

## Question 3

> `3`. The matrix $A$ is given by $A=\begin{pmatrix}a & 4 & 2\\ 1 & a & 0\\ 1 & 2 & 1\end{pmatrix}$.

> `1`. Find the determinant of $A$

```{code-cell} ipython3
A = sym.Matrix([[a, 4, 2], [1, a, 0], [1, 2, 1]])
determinant = A.det()
determinant
```

> `2`. Hence find the values of $a$ for which $A$ is singular.

$A$ is singular when the determinant is $0$ so we solve that equation:

```{code-cell} ipython3
sym.solveset(determinant, a)
```

> `3`. State, giving a brief reason in each case, whether the simultaneous equations
>
> $$
  \begin{array}{l}
          a x + 4y + 2z= 3a\\
          x + a y  = 1\\
          x + 2y + z = 3\\
  \end{array}
  $$

> have any solutions when:
> `1`. $a = 3$;

When $a$ is 3 the determinant is none zero, and so the matrix that represents
that linear system can be inverted.

> `2`. $a = 2$

When $a$ is 2 the determinant is zero and so the matrix that represents
that linear system cannot be inverted.

## Question 4

> `4`. The matrix $D$ is given by $D = \begin{pmatrix} a & 2 & 0\\ 3 & 1 & 2\\ 0 & -1 & 1\end{pmatrix}$ where $a\ne 2$.
> `1`. Find $D^{-1}$.

```{code-cell} ipython3
D = sym.Matrix([[a, 2, 0], [3, 1, 2], [0, -1, 1]])
D_inverse = D.inv()
D_inverse
```

> `2`. Hence or otherwise, solve the equations:
>
> $$
    \begin{array}{l}
        a x + 2y = 3\\
        3x + y + 2z = 4\\
        - y + z = 1\\
    \end{array}
    $$

This corresponds to calculating: $D^{-1} \begin{pmatrix}3\\4\\1\end{pmatrix}$

```{code-cell} ipython3
b = sym.Matrix([[3], [4], [1]])
D_inverse @ b
```
