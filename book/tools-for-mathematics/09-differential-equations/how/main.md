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

## How to create a symbolic function

To create a symbolic function use `sympy.Function`.

````{tip}
```
sympy.Function("y")
```
````

For example:

```{code-cell} ipython3
import sympy as sym

y = sym.Function("y")
y
```

We can pass symbolic variables to this symbolic function:

```{code-cell} ipython3
x = sym.Symbol("x")
y(x)
```

We can create the derivative of a symbolic function:

```{code-cell} ipython3
sym.diff(y(x), x)
```

## How to create a differential equation

To create a differential equation we use `sympy.Eq`.

````{tip}
```
import sympy as sym

y = sym.Function("y")
x = sym.Symbol("x")

equation = sym.Eq(lhs, rhs)
```
````

Where `lhs` and `rhs` are expressions in $y$, $\frac{dy}{dx}$ and $x$.

For example to create the differential equation: $\frac{dy}{dx} = \cos(x) y$
we would write:

```{code-cell} ipython3
import sympy as sym

y = sym.Function("y")
x = sym.Symbol("x")

lhs = sym.diff(y(x), x)
rhs = sym.cos(x) * y(x)
differential_equation = sym.Eq(lhs, rhs)
differential_equation
```

## How to obtain the general solution of a differential equation

To obtain the generation solution to a differential equation we use:
`sympy.dsolve`.

````{tip}
```
import sympy as sym

y = sym.Function("y")
x = sym.Symbol("x")

equation = sym.Eq(lhs, rhs)
sym.dsolve(equation, y(x))
```
````

For example to solve the differential equation: $\frac{dy}{dx} = \cos(x) y$ we
would write:

```{code-cell} ipython3
import sympy as sym

y = sym.Function("y")
x = sym.Symbol("x")

lhs = sym.diff(y(x), x)
rhs = sym.cos(x) * y(x)
differential_equation = sym.Eq(lhs, rhs)
sym.dsolve(differential_equation, y(x))
```

## How to obtain the particular solution of a differential equation

To obtain the particular solution to a differential equation we use:
`sympy.dsolve` and pass the initial conditions: `ics`.

````{tip}
```
import sympy as sym

y = sym.Function("y")
x = sym.Symbol("x")

equation = sym.Eq(lhs, rhs)
sym.dsolve(equation, y(x), ics={y(x_0): value})
```
````

For example to solve the differential equation: $\frac{dy}{dx} = \cos(x) y$
with the condition $y(5)= \pi$ we
would write:

```{code-cell} ipython3
import sympy as sym

y = sym.Function("y")
x = sym.Symbol("x")

lhs = sym.diff(y(x), x)
rhs = sym.cos(x) * y(x)
differential_equation = sym.Eq(lhs, rhs)

condition = {y(5): sym.pi}
sym.dsolve(differential_equation, y(x), ics=condition)
```

```{note}
The syntax used here is similar to the way we
{ref}`substitute values in to algebraic expressions <how-to-substitute-a-value-in-to-an-expression>`.
```
