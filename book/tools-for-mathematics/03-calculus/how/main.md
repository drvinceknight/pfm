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

## Calculate the derivative of an expression.

We can calculate the derivative of an expression using `sympy.diff` which takes,
an expression, a variable and a degree.

````{tip}
```
sympy.diff(expression, variable, degree=1)
```
````

The default value of `degree` is 1.

For example to compute $\frac{d (4 x ^ 3 + 2 x + 1}{dx}$:

```{code-cell} ipython3
import sympy as sym

x = sym.Symbol("x")
expression = 4 * x ** 3 + 2 * x + 1
sym.diff(expression, x)
```

To compute the second derivative: $\frac{d ^ 2 (4 x ^ 3 + 2 x + 1}{dx ^ 2}$

```{code-cell} ipython3
sym.diff(expression, x, 2)
```

## Calculate the indefinite integral of an expression.

We can calculate the indefinite integral of an expression using
`sympy.integrate`. Which takes an expression and a variable.

````{tip}
```
sympy.integrate(expression, variable)
```
````

For example to compute $\int 4x^3 + 2x + 1 dx$:

```{code-cell} ipython3
sym.integrate(expression, x)
```

## Calculate the definite integral of an expression.

We can calculate the definite integral of an expression using
`sympy.integrate`. The first argument is an expression but instead of passing a
variable as the second argument we pass a tuple with the variable and the upper
and lower bounds of integration.

````{tip}
```
sympy.integrate(expression, (variable, lower_bound, upper_bound))
```
````

For example to compute $\int_0^4 4x^3 + 2x + 1 dx$:

```{code-cell} ipython3
sym.integrate(expression, (x, 0, 4))
```

## Use $\infty$

In `sympy` we can access $\infty$ using `sym.oo`:

````{tip}
```
sympy.oo
```
````

For example:

```{code-cell} ipython3
sym.oo
```

## Calculate limits

We can calculate limits using `sympy.limit`. The first argument is the
expression, then the variable and finally the expression the variable tends to.

````{tip}
```
sympy.limit(expression, variable, value)
```
````

For example to compute $\lim_{h \to 0} \frac{4 x ^ 3 + 2 x + 1 - 4(x - h)^3 - 2(x - h) - 1}{h}$:

```{code-cell} ipython3
h = sym.Symbol("h")
expression = (4 * x ** 3 + 2 * x + 1 - 4 * (x - h) ** 3 - 2 * (x - h) - 1) / h
sym.limit(expression, h, 0)
```
