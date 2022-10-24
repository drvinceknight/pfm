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

# Further information

## Why are we not commenting our code?

In Python it is possible to annotate code using `#`. For example:

```{code-cell} ipython3
import sympy as sym  # Importing the sympy library using the alias sym
```

Comments like these often do not add to the readability of the code. In fact
they can make the code less readable or at worse confusing {cite}`martin2009clean`.

In this section of the book there is in fact no need for comments like this as
we are mainly using tools that are well documented. Furthermore when using
Jupyter notebooks we can add far more to the readbility of the code by adding
prose alongside our code instead of using small brief inline comments.

This does not mean that readability of code is not important.

```{important}
Being able to read and understand the code we write is important.
```

In {ref}`probability` we will start to write our own functions and emphasis will
be given there on readability and documenting (as opposed to commenting) the
code we will write.

In {ref}`modularisation` and {ref}`documentation` there is a lot more
information on how to ensure code is readable and understandable.

## Why do we use `@` for matrix multiplication and not `*`?

With `sympy` it is in fact possible to use the `*` operator for matrix
multiplication:

```{code-cell} ipython3
import sympy as sym

matrix = sym.Matrix([[sym.S(1) / 5, 1], [1, 1]])
other_matrix = sym.Matrix([[sym.S(4) / 5, 0], [0, 0]])
matrix * other_matrix
```

However there are other libraries that can be used for linear algebra and in
those libraries the `*` does not do matrix multiplication, it does element wise
multiplication instead. So for clarity it is preferred to use `@` throughout.

## I have read that `numpy` is a library for linear algebra?

`numpy` is one of the most popular and important libraries in the Python
ecosystem. It is in fact the best library to use when doing linear algebra as it
is computationally efficient, **however** it cannot handle symbolic variables
which is why we are seeing how to use `Sympy` here. {ref}`numpy` gives an
introduction to `numpy`.
