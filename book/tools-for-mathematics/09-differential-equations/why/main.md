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

## How to solve a system of differential equations?

Given a system of differential equations like the following:

$$
    \begin{cases}
        \frac{dx}{dt} =& x - y\\
        \frac{dy}{dt} =& x + y\\
        y(0) =& 250\\
        y(1) =& 300
    \end{cases}
$$

We can solve it using `sym.dsolve` but instead of passing a single differential
equation, we pass an iterable of multiple equations:

```{code-cell} ipython3
import sympy as sym


y = sym.Function("y")
x = sym.Function("x")

t = sym.Symbol("t")
alpha = sym.Symbol("alpha")
beta = sym.Symbol("beta")

system_of_equations = (
    sym.Eq(sym.diff(y(t), t), alpha * x(t)),
    sym.Eq(sym.diff(x(t), t), beta * y(t)),
)
conditions = {y(0): 250, y(1): 300}

y_solution, x_solution = sym.dsolve(system_of_equations, ics=conditions, set=True)
x_solution
```

```{code-cell} ipython3
y_solution
```

## How to solve differential equations numerically

Some differential equations do not have a closed form solution in terms of
elementary functions. For example, the [Airy or Stokes equation](https://en.m.wikipedia.org/wiki/Airy_function):

$$
\frac{d^2y}{dx^2} = xy
$$

Attempting to solve this with Sympy gives:

```{code-cell} ipython3
import sympy as sym

y = sym.Function("y")
x = sym.Symbol("x")

equation = sym.Eq(sym.diff(y(x), x, 2), x * y(x))
sym.dsolve(equation, y(x))
```

which is a linear combination of $A_i$ and $B_i$ which are special functions
called the Airy functions of the first and second kind.

Using `scipy.integrate` it is possible to solve this differential equation numerically.

First, we will define a new variable $u=\frac{dy}{dx}$ so that the second order
differential equation can be expressed as a system of single order differential
equations:

$$
    \begin{cases}
        \frac{du}{dx}=&xy\\
        \frac{dy}{dx}=&u
    \end{cases}
$$

We now define a python function to that returns the right hand side of that
system of equations:

```{code-cell} ipython3
def diff(state, x):
    """
    Returns the value of the derivates for a given set of state values (u, y).
    """
    u, y = state
    return x * y, u
```

We can pass this to `scipy.integrate.odeint` which is a tool that carries out
numerical integration of differential equations. Note, that it is incapable of
dealing with symbolic variables, thus an initial numeric value of $(u, y)$ is
required.

```{code-cell} ipython3
import numpy as np
import scipy.integrate

condition = (.1, -.5)

xs = np.linspace(0, 1, 50)
states = scipy.integrate.odeint(diff, y0=condition, t=xs)

```

```{note}
We make use of
{ref}`how-to-create-a-given-number-of-values-between-two-bounds` to create a set
of `x` values over which to carry out the numerical integration.
```

This returns an array of values of `states` corresponding to $(u, y)$.

```{code-cell} ipython3
:tags: [output_scroll]

states
```

A plot of the above with a comparison to the exact expected values (obtained
using the Airy functions of the first and second kind):

```{code-cell} ipython3
:tags: ["remove-input", "style-check-ignore", "nbval-ignore-output"]

import matplotlib.pyplot as plt

x = sym.Symbol("x")
y = sym.Function("y")

equation = sym.Eq(lhs=sym.diff(y(x), x, 2), rhs=x * y(x) )
solution = sym.dsolve(equation, y(x), ics={y(0): condition[1], y(x).diff(x).subs(x, 0): condition[0]})

states = scipy.integrate.odeint(diff, y0=condition, t=xs)
plt.figure()
plt.scatter(xs, states.T[1], label="numeric", marker="+", color="black")
plt.plot(xs, [solution.rhs.subs({x: value}) for value in xs], label="closed form")
plt.xlabel("$x$")
plt.ylabel("y")
plt.legend();
```
