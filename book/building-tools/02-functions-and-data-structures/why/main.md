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

## What formats can be used to write a docstring?

The format used to write a docstring described in {ref}`how_to_write_a_docstring` is the one specified
by the Numpy project.

Amongst other things you can see how to specify further functionality:

- How to indicate if a parameter is optional.
- How to specify what types of errors might be raised by a function.
- How to specify when a function is a generator.

## Are there tools available to assist with writing docstrings?

The `darglint` library can be used
to check if docstrings match a given format.

## A part from removing duplicates and set operations what are they advantages to using `set`?

One valuable uses of `set` is to efficiently identify if an element
is in a given iterable or not:

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

numbers = list(range(100000))
%timeit 100000 in numbers
```

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

numbers = set(range(100000))
%timeit 100000 in numbers
```
