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

## I plot a function

It is possible to plot a function using Sympy using the `sym.plot` function:

```
sym.plot(f(x))
```

So for example, here is a plot of $f(x)=x^2 + 3x + 1$:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

import sympy as sym

x = sym.Symbol("x")
sym.plot(x ** 2 + 3 * x + 1);
```

It is possible to specify the x limits and combine it with other plots:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

sym.plot(x ** 2 + 3 * x + 1, xlim=(-5, 5));
```

**This plotting solution is fine it you want to take a look at a function quickly but it is not recommended.** The main library for plotting is called `matplotlib` and we will see how to use that at a later date.

- Here is the Sympy documentation for plotting: <https://docs.sympy.org/latest/modules/plotting.html>
- Here is the official matplotlib documentation: <https://matplotlib.org>
