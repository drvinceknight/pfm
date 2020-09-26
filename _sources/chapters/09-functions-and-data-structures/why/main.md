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

# Why

## A part from removing duplicates and set operations what are they advantages to using `set`?

One valuable uses of `set` is to efficiently identify is an element
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
