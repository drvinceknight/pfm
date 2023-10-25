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

## Create a matrix

We create a matrix using the `sympy.Matrix` tool. We combine this with
square brackets `[]` which we nest so that every row is also inside square
brackets.

````{tip}
```
sympy.Matrix([values])
```
````

For example, the following creates the matrix:

$$
    B = \begin{pmatrix}
            1 & 2 & 3 & 4\\
            5 & 6 & 7 & 8\\
            9 & 10 & 11 & 12
        \end{pmatrix}
$$

```{code-cell} ipython3
import sympy as sym

B = sym.Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
B
```

```{attention}
It is possible to write the code in a more readable way as long as an incomplete
line ends with an open bracket:
```

```
B = sym.Matrix(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
)
```

## Calculate the determinant of a matrix

To calculate the determinant of a matrix, we use the `.det` tool. For example to
calculate the determinant of:

````{tip}
```
matrix = sympy.Matrix([values])
matrix.det()
```
````

For example, the determinant of the following matrix:

$$
    \begin{pmatrix}
    1 & 5\\
    5 & 1
    \end{pmatrix}
$$

```{code-cell} ipython3
matrix = sym.Matrix([[1, 5], [5, 1]])
matrix.det()
```

## Calculate the inverse of a matrix

To calculate the inverse of a matrix, we use the `.inv` tool.

````{tip}
```
matrix = sympy.Matrix([values])
matrix.inv()
```
````

For example to
calculate the inverse of:

$$
    \begin{pmatrix}
        1 / 2 & 1\\
        5     & 0
    \end{pmatrix}
$$

```{code-cell} ipython3
matrix = sym.Matrix([[sym.S(1) / 2, 1], [5, 0]])
matrix.inv()
```

## Multiply matrices by a scalar

To multiple a matrix by a scalar we use the `*` operator. For example to
multiply the following matrix by $6$:

$$
    \begin{pmatrix}
        1 / 5 & 1\\
        1 & 1
    \end{pmatrix}
$$

```{code-cell} ipython3
matrix = sym.Matrix([[sym.S(1) / 5, 1], [1, 1]])
6 * matrix
```

## Add matrices together

To add matrices we use the `+` operator. For example to compute:

$$
    \begin{pmatrix}
        1 / 5 & 1\\
        1 & 1
    \end{pmatrix} +
    \begin{pmatrix}
        4 / 5 & 0\\
        0 & 0
    \end{pmatrix}
$$

```{code-cell} ipython3
matrix = sym.Matrix([[sym.S(1) / 5, 1], [1, 1]])
other_matrix = sym.Matrix([[sym.S(4) / 5, 0], [0, 0]])
matrix + other_matrix
```

## Multiply matrices together

To multiply matrices together we use the `@` operator. For example to compute:

$$
    \begin{pmatrix}
        1 / 5 & 1\\
        1 & 1
    \end{pmatrix}
    \begin{pmatrix}
        4 / 5 & 0\\
        0 & 0
    \end{pmatrix}
$$

```{code-cell} ipython3
matrix @ other_matrix
```

## How to create a vector

A vector is essentially a matrix with a single row or column. For example to
create the vector:

$$
    \begin{pmatrix}
    3 \\
    2 \\
    1
    \end{pmatrix}
$$

```{code-cell} ipython3
vector = sym.Matrix([[3], [2], [1]])
vector
```

## How to solve a linear system

To solve a given linear system that can be represented in matrix form, we create
the corresponding matrix and vector and use the matrix inverse. For example to
solve the following equations:

$$
    \begin{array}{l}
        x + 2y = 3\\
        3x + y + 2z = 4\\
        - y + z = 1\\
    \end{array}
$$

```{code-cell} ipython3
A = sym.Matrix([[1, 2, 0], [3, 1, 2], [0, -1, 1]])
b = sym.Matrix([[3], [4], [1]])
A.inv() @ b
```
