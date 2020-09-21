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

## Matrices

### Introduction

Matrices form the building block of an area of mathematics referred to as Linear Algebra. The dictionary definition of a matrix is:

> a group of numbers or other symbols arranged in a rectangle that can be used together as a single unit to solve particular mathematical problems

The specific mathematical problems discussed usually correspond to solving large systems of linear equations. However they have become an area of interest in their own right and manipulating matrices usually corresponds to:

- calculating the determinant of a matrix;
- calculating the inverse of a matrix.

Here we will see how to instruct a computer to carry out these techniques.

## Tutorial

We will solve the following problem using a computer to assist with the technical aspects:


---

The matrix \\(A\\) is given by \\(A=\begin{pmatrix}a & 1 & 1\\ 1 & a & 1\\ 1 & 1 & 2\end{pmatrix}\\).

1. Find the determinant of \\(A\\)
2. Hence find the values of \\(a\\) for which \\(A\\) is singular.
3. For the following values of \\(a\\), when possible obtain \\(A ^ {- 1}\\) and confirm the result by computing \\(AA^{-1}\\):
    1. \\(a = 0\\);
    2. \\(a = 1\\);
    3. \\(a = 2\\);
    4. \\(a = 3\\).

---

Sympy is once again the library we will use for this.

We will start by our matrix \\(A\\):

```{code-cell} ipython3
import sympy as sym

a = sym.Symbol("a")
A = sym.Matrix([[a, 1, 1], [1, a, 1], [1, 1, 2]])
```

We can now create a variable `determinant` and assign it the value of the determinant of \\(A\\):

```{code-cell} ipython3
determinant = A.det()
determinant
```

A matrix is singular if it has determinant 0. We can find the values of \\(a\\) for which this occurs:

```{code-cell} ipython3
sym.solveset(determinant, a)
```

Thus it is not possible to find the determinant of \\(A\\) for \\(a\in\{0, 1\}\\).

However for \\(a = 2\\):

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

and for \\(a = 3\\):

```{code-cell} ipython3
A.subs({a: 3}).inv()
```

```{code-cell} ipython3
A.subs({a: 3}).inv() @ A.subs({a: 3})
```

### How to


#### Create a matrix

We create a matrix using the `sym.Matrix` tool. We combine this with the square brackets `[]` which we nest so that every row is also inside square brackets.

For example, the following creates the matrix:

\\[
    B = \begin{pmatrix}
            1 & 2 & 3 & 4\\
            5 & 6 & 7 & 8\\
            9 & 10 & 11 & 12
        \end{pmatrix}
\\]

```{code-cell} ipython3
B = sym.Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
B
```

**Note** that it is possible to write the code in a more readable way as long as an incomplete line ends with an open bracket:


```
B = sym.Matrix(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
)
```

+++

#### Calculate the determinant of a matrix

To calculate the determinant of a matrix, we use the `.det` tool. For example to calculate the determinant of:

\\[
    \begin{pmatrix}
    1 & 5\\
    5 & 1
    \end{pmatrix}
\\]

```{code-cell} ipython3
matrix = sym.Matrix([[1, 5], [5, 1]])
matrix.det()
```

#### Calculate the inverse of a matrix


To calculate the inverse of a matrix, we use the `.inv` tool. For example to calculate the inverse of:

\\[
    \begin{pmatrix}
        1 / 2 & 1\\
        5     & 0
    \end{pmatrix}
\\]

```{code-cell} ipython3
matrix = sym.Matrix([[sym.S(1) / 2, 1], [5, 0]])
matrix.inv()
```

#### Multiply matrices by a scalar

To multiple a matrix by a scalar we use the `*` operator. For example to multiply the following matrix by \\(6\\):

\\[
    \begin{pmatrix}
        1 / 5 & 1\\
        1 & 1
    \end{pmatrix}
\\]

```{code-cell} ipython3
matrix = sym.Matrix([[sym.S(1) / 5, 1], [1, 1]])
6 * matrix
```

#### Add matrices together

To add matrices we use the `+` operator. For example to compute:

\\[
    \begin{pmatrix}
        1 / 5 & 1\\
        1 & 1
    \end{pmatrix} +
    \begin{pmatrix}
        4 / 5 & 0\\
        0 & 0
    \end{pmatrix}
\\]

```{code-cell} ipython3
matrix = sym.Matrix([[sym.S(1) / 5, 1], [1, 1]])
other_matrix = sym.Matrix([[sym.S(4) / 5, 0], [0, 0]])
matrix + other_matrix
```

#### Multiply matrices together

To multiply matrices together we use the `@` operator. For example to compute:


\\[
    \begin{pmatrix}
        1 / 5 & 1\\
        1 & 1
    \end{pmatrix}
    \begin{pmatrix}
        4 / 5 & 0\\
        0 & 0
    \end{pmatrix}
\\]

```{code-cell} ipython3
matrix @ other_matrix
```

#### How to create a vector

A vector is essentially a matrix with a single row or column. For example to create the vector:

\\[
    \begin{pmatrix}
    3 \\
    2 \\
    1
    \end{pmatrix}
\\]

```{code-cell} ipython3
vector = sym.Matrix([[3], [2], [1]])
vector
```

#### How to solve a linear system

To solve a given linear system that can be represented in matrix form, we create the corresponding matrix and vector and use the matrix inverse. For example to solve the following equations:

\\[
    \begin{array}
        a x + 2y = 3\\
        3x + y + 2z = 4\\
        - y + z = 1\\
    \end{array}
\\]

```{code-cell} ipython3
A = sym.Matrix([[1, 2, 0], [3, 1, 2], [0, -1, 1]])
b = sym.Matrix([[3], [4], [1]])
A.inv() @ b
```

### Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. Obtain the determinant and the inverses of the following matrices:
    1. \\(A = \begin{pmatrix} 1 / 5 & 1\\1 & 1\end{pmatrix}\\)
    2. \\(B = \begin{pmatrix} 1 / 5 & 1 & 5\\3 & 1 & 6 \\ 1 & 2 & 1\end{pmatrix}\\)
    3. \\(C = \begin{pmatrix} 1 / 5 & 5 & 5\\3 & 1 & 7 \\ a & b & c\end{pmatrix}\\)
2. Compute the following:
    1. \\(500\begin{pmatrix} 1 / 5 & 1\\1 & 1\end{pmatrix}\\)
    2. \\(\pi \begin{pmatrix} 1 / \pi & 2\pi\\3/\pi & 1\end{pmatrix}\\)
    3. \\(500\begin{pmatrix} 1 / 5 & 1\\1 & 1\end{pmatrix} + \pi \begin{pmatrix} 1 / \pi & 2\pi\\3/\pi & 1\end{pmatrix}\\)
    4. \\(500\begin{pmatrix} 1 / 5 & 1\\1 & 1\end{pmatrix}\begin{pmatrix} 1 / \pi & 2\pi\\3/\pi & 1\end{pmatrix}\\)
3. The matrix \\(A\\) is given by \\(A=\begin{pmatrix}a & 4 & 2\\ 1 & a & 0\\ 1 & 2 & 1\end{pmatrix}\\).
    1. Find the determinant of \\(A\\)
    2. Hence find the values of \\(a\\) for which \\(A\\) is singular.
    3. State, giving a brief reason in each case, whether the simultaneous equations
        \\[
            \begin{array}
                a x + 4y + 2z= 3a\\
                x + a  = 1\\
                x + 2y + z = 3\\
            \end{array}
        \\]

        have any solutions when:
          1. \\(a = 3\\);
          2. \\(a = 2\\)
4. Q1 The matrix \\(D\\) is given by \\(D = \begin{pmatrix} a & 2 & 0\\ 3 & 1 & 2\\ 0 & -1 & 1\end{pmatrix}\\) where \\(a\ne 2\\).
    1. Find \\(D^{-1}\\).
    2. Hence of otherwise, solve the equations:

    \\[
    \begin{array}
        a x + 2y = 3\\
        3x + y + 2z = 4\\
        - y + z = 1\\
    \end{array}
    \\]


### References

#### Why do we use `@` for matrix multiplication and not `*`?

With sympy it is in fact possible to use the `*` operator for matrix multiplication:

```{code-cell} ipython3
matrix = sym.Matrix([[sym.S(1) / 5, 1], [1, 1]])
other_matrix = sym.Matrix([[sym.S(4) / 5, 0], [0, 0]])
matrix * other_matrix
```

However there are other libraries that can be used for linear algebra and in those libraries the `*` does not do matrix multiplication, it does element wise multiplication instead. So for clarity it is preferred to use `@` throughout.

+++

#### I have read that `numpy` is a library for linear algebra?|

`numpy` is one of the most popular and important libraries in the Python ecosystem. It is in fact the best library to use when doing linear algebra as it is computationally efficient, **however** it cannot handle symbolic variables which is why we are seeing how to use `Sympy` here.
