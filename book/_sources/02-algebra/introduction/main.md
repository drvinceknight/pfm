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

# Algebra

## Introduction

As of 2020, the A-level syllabus includes Algebra which
https://www.cambridgeinternational.org/Images/415060-2020-2022-syllabus.pdf
describes as:

> Algebra: this is an essential tool which supports and expresses mathematical
> reasoning and provides a means to generalise across a number of contexts.

In practice this often means:

- Manipulating numeric expressions;
- Manipulating symbolic expressions;
- Solving equations.

We can use a computer to carry out some of these techniques.

```{note}
Here is a note
```

```{warning}
Here is a warning
```

Here is some inline mathematics $2 + 3$.

Here is some displaystyle mathematics

$$22 + 23$$

```{code-cell} ipython3
import sympy as sym

x = sym.Symbol("x")
x** 2
```

```{code-cell} ipython3
import matplotlib.pyplot as plt

plt.plot([1, 2], [3, 4]);
```

````{toggle}
```python
3 + 2
```
````
