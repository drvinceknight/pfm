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

We will solve the following problem using a computer to do some of the more
tedious calculations.

```{admonition} Problem
A container has volume $V$ of liquid which is poured in at a rate proportional
to $e^{-t}$ (where $t$ is some measurement of time). Initially the container is empty and
after $t=3$ time units the rate at which the liquid is poured is 15.

1. Show that $V(t)=\frac{-15e^{3}}{1-e^{3}}(1 - e^{-t})$
2. Obtain the limit $\lim_{t\to \infty}V(t)$
```

We first need to create the differential equation described in the text:

$$\frac{V(t)}{dt}=ke^{-t}$$

We create this differential equation in python:

```{code-cell} ipython3
import sympy as sym

t = sym.Symbol("t")
k = sym.Symbol("k")
V = sym.Function("V")

differential_equation = sym.Eq(lhs=sym.diff(V(t), t), rhs=k * sym.exp(-t))
differential_equation
```

In order to solve the differential equation we can write:

```{code-cell} ipython3
sym.dsolve(differential_equation, V(t))
```

Note that the question gives us an initial condition: "initially the container
is empty" which corresponds to $V(0)=0$.

We can pass this to the call to solve the differential equation:

```{code-cell} ipython3
condition = {V(0): 0}
particular_solution = sym.dsolve(differential_equation, V(t), ics=condition)
sym.simplify(particular_solution)
```

We also know that $V(3)=15$ which corresponds to the following equation:

```{code-cell} ipython3
equation = sym.Eq(particular_solution.rhs.subs({t: 3}), 15)
equation
```

We can solve this equation to find a value for $k$:

```{code-cell} ipython3
sym.simplify(sym.solveset(equation, k))
```

which is the required value.

We can use the complete expression for $V(t)$ to take the limit:

```{code-cell} ipython3
limit = sym.limit((-15 * sym.exp(3) / (1- sym.exp(3))) *  (1 - sym.exp(-t)), t, sym.oo)
limit
```

This is approximately:

```{code-cell} ipython3
float(limit)
```

```{important}
In this tutorial we have

- Created a differential equation
- Obtained the general solution of a differential equation
- Obtained the particular solution of a differential equation.
```
