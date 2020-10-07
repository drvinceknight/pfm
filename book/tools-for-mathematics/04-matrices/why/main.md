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

## I have read that `numpy` is a library for linear algebra?|

`numpy` is one of the most popular and important libraries in the Python
ecosystem. It is in fact the best library to use when doing linear algebra as it
is computationally efficient, **however** it cannot handle symbolic variables
which is why we are seeing how to use `Sympy` here. {ref}`numpy` gives an
introduction to `numpy`.
