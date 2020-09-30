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

(objects_tutorial)=
# Tutorial

We will here write some code to create and manipulate quadratic expressions.
With `sympy` this is not necessary as all functionality required is available
within `sympy` however this will be a good exercise in understanding how to
build such functionality.

```{admonition} Problem
Consider the following quadratics:

$$
f(x) = 5 x ^ 2 + 2 x + 7\\
g(x) = 4 x ^ 2 - 3 x + 12\\
h(x) = f(x) + g(x)
$$

Without using `sympy`, obtain the roots for all the quadratics.
```

We will start by defining an object to represent a quadratic. This is called a
class.

```{code-cell} ipython3
import math


class QuadraticExpression:
    """A class for a quadratic expression"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = self.b ** 2 - 4 * self.a * self.c

    def get_roots(self):
        """Return the real valued roots of the quadratic expression"""
        if self.discriminant >= 0:
            x1 = -(self.b + math.sqrt(self.discriminant)) / (2 * self.a)
            x2 = -(self.b - math.sqrt(self.discriminant)) / (2 * self.a)
            return x1, x2
        return ()

    def __add__(self, other):
        """A magic method: let's us have addition between expressions"""
        return QuadraticExpression(self.a + other.a, self.b + other.b, self.c + other.c)

    def __repr__(self):
        """A magic method: changes the default way an instance is displayed"""
        return f"Quadratic expression: {self.a} x ^ 2 + {self.b} x + {self.c}"
```

```{tip}
Four functions were created with this class:

- `__init__`: as this is surrounded by `__` (two underscores) this is a magic
  function that is run when we create an instance of our class.
- `root`: this returns the two real valued roots if the discriminant is
  positive.
- `__add__`: another magic function that is run when the `+` operator is used.
- `__repr__`: another magic function that gives the string representation of the
  instance.
```

Let us now use this class to solve the specified problem. First we create
instances the class that correspond to $f$ and $g$. This is using the `__init__`
function in the background.

```{code-cell} ipython3
f = QuadraticExpression(a=5, b=2, c=-7)
g = QuadraticExpression(a=-4, b=-3, c=12)
```

We can now take a look at both of these instances. This is using the `__repr__`
function in the background:

```{code-cell} ipython3
f
```

```{code-cell} ipython3
g
```

Now we are going to create $h(x) = f(x) + g(x)$. This is using the `__add__`
function in the background:


```{code-cell} ipython3
h = f + g
h
```

We can now iterate over our quadratics and find the roots. This is using the
`get_root` function in the background:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

roots = [quadratic.get_roots() for quadratic in (f, g, h)]
roots
```

We see that $f$ and $g$ have real valued roots but $h$ does not. We can check
the value of the discriminant of $h$:

```{code-cell} ipython3
h.discriminant
```

We are going to now create a new class from `QuadraticExpression` where we
replace the `get_roots` function with a new one that can handle imaginary roots
and update the `__add__` function to make sure we return an instance of the new
class.

```{code-cell} ipython3
class QuadraticExpressionWithAllRoots(QuadraticExpression):
    """
    A class for a quadratic expression that can return imaginary roots

    The `get_roots` function returns two tuples of the form (re, im) where re is
    the real part and im is the imaginary part.
    """

    def get_roots(self):
        """Return the real valued roots of the quadratic expression"""
        if self.discriminant >= 0:
            x1 = -(self.b + math.sqrt(self.discriminant)) / (2 * self.a)
            x2 = -(self.b - math.sqrt(self.discriminant)) / (2 * self.a)
            return (x1, 0), (x2, 0)

        real_part = self.b / (2 * self.a)
        im1 = math.sqrt(-self.discriminant) / (2 * self.a)
        im2 = -math.sqrt(-self.discriminant) / (2 * self.a)
        return ((real_part, im1), (real_part, im2))

    def __add__(self, other):
        """A special method: let's us have addition between expressions"""
        return QuadraticExpressionWithAllRoots(
            self.a + other.a, self.b + other.b, self.c + other.c
        )
```

Now let us define our quadratics once again but using this new class:

```{code-cell} ipython3
f = QuadraticExpressionWithAllRoots(a=5, b=2, c=-7)
g = QuadraticExpressionWithAllRoots(a=-4, b=-3, c=12)
h = f + g
```

```{code-cell} ipython3
f
```

```{code-cell} ipython3
g
```

```{code-cell} ipython3
h
```

````{attention}
We have not needed to redefine `__init__`, or `__repr__` as the new
class inherits these from `QuadraticExpression` due to this statement:

```
class QuadraticExpressionWithAllRoots(QuadraticExpression):
```
````

We can now get all the roots for both quadratics:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

roots = [quadratic.get_roots() for quadratic in (f, g, h)]
roots
```
