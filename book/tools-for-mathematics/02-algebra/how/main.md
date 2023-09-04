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

## How to create a symbolic numeric value

To create a symbolic numerical value use `sympy.S`.

````{tip}
```
sympy.S(a)
```
````

For example:

```{code-cell} ipython3
import sympy

value = sympy.S(3)
value
```

```{attention}
If we combine a symbolic value with a non symbolic value it will automatically
give a symbolic value:
```

```{code-cell} ipython3
1 / value
```

## How to get the numerical value of a symbolic expression

We can get the numerical value of a symbolic value using `float` or `int`:

- `float` will give the numeric approximation in \\(\mathbb{R}\\)
  ````{tip}
  ```
  float(x)
  ```
  ````
- `int` will give the integer value
  ````{tip}
  ```
  int(x)
  ```
  ````

For example, let us create a symbolic numeric variable with value
\\(\frac{1}{5}\\):

```{code-cell} ipython3
value = 1 / sympy.S(5)
value
```

To get the numerical value:

```{code-cell} ipython3
float(value)
```

If we wanted the integer value:

```{code-cell} ipython3
int(value)
```

```{attention}
This is not rounding to the nearest integer. It is returning the integer part.
```

## How to factor an expression

We use the `sympy.factor` tool to factor expressions.

````{tip}
```
sympy.factor(expression)
```
````

For example:

```{code-cell} ipython3
x = sympy.Symbol("x")
sympy.factor(x ** 2 - 9)
```

## How to expand an expression

We use the `sympy.expand` tool to expand expressions.

````{tip}
```
sympy.expand(expression)
```
````

For example:

```{code-cell} ipython3
sympy.expand((x - 3) * (x + 3))
```

## How to simplify an expression

We use the `sympy.simplify` tool to simplify an expression.

````{tip}
```
sympy.simplify(expression)
```
````

For example:

```{code-cell} ipython3
sympy.simplify((x - 3) * (x + 3))
```

```{attention}
This will not always give the expected (or any) result. At times it could be
more beneficial to use `sympy.expand` and/or `sympy.factor`.
```

## How to solve an equation

We use the `sympy.solveset` tool to solve an equation. It takes two values as
inputs. The first is either:

- An expression for which a root is to be found
- An equation

The second is the variable we want to solve for.

````{tip}
```
sympy.solveset(equation, variable)
```
````

Here is how we can use `sympy` to obtain the roots of the general quadratic:

$$
a x ^ 2 + bx + c
$$

```{code-cell} ipython3
a = sympy.Symbol("a")
b = sympy.Symbol("b")
c = sympy.Symbol("c")
quadratic = a * x ** 2 + b * x + c
sympy.solveset(quadratic, x)
```

Here is how we would solve the same equation but not for \\(x\\) but for
\\(b\\):

```{code-cell} ipython3
sympy.solveset(quadratic, b)
```

It is however clearer to specifically write the equation that we want to solve:

```{code-cell} ipython3
equation = sympy.Eq(a * x ** 2 + b * x + c, 0)
sympy.solveset(equation, x)
```

(how-to-substitute-a-value-in-to-an-expression)=

## How to substitute a value in to an expression

Given a `sympy` expression it is possible to substitute values in to it using
the `.subs()` tool.

````{tip}
```
expression.subs({variable: value})
```
````

```{attention}
It is possible to pass multiple variables at a time.
```

For example we can substitute the values for \\(a, b, c\\) in to our quadratic:

```{code-cell} ipython3
quadratic = a * x ** 2 + b * x + c
quadratic.subs({a: 1, b: sympy.S(7) / 8, c: 0})
```
