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

# Solutions

## Question 1

> `1`. Use the class created in {ref}`objects_tutorial` to find the roots of the
>  following quadratics:

> `1`. $f(x) = -4x ^ 2 + x + 6$

First we define the class:

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

Now we use it:

```{code-cell} ipython3
f = QuadraticExpressionWithAllRoots(a=-4, b=1, c=6)
f.get_roots()
```

> `2`. $g(x) = 3x^2 - 6$

```{code-cell} ipython3
g = QuadraticExpressionWithAllRoots(a=3, b=0, c=-6)
g.get_roots()
```

> `3`. $h(x) = f(x) + g(x)$

```{code-cell} ipython3
h = f + g
h.get_roots()
```

> `2`. Write a class for a Linear expression and use it to find the roots of the
>  following expressions:

>  `1`. $f(x) = 2x + 6$

First we define the class:

```{code-cell} ipython3
import math

class LinearExpression:
    """A class for a linear expression a x + b"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_roots(self):
        """Return the roots of the linear expression"""
        if self.a != 0:
            return -self.b / self.a
        return None

    def __add__(self, other):
        """A magic method: let's us have addition between expressions"""
        return LinearExpression(self.a + other.a, self.b + other.b)

    def __repr__(self):
        """A magic method: changes the default way an instance is displayed"""
        return f"Linear expression: {self.a} x + {self.b}"
```

Now we use it:

```{code-cell} ipython3
f = LinearExpression(a=2, b=6)
f.get_roots()
```

> `2`. $g(x) = 3x - 6$

```{code-cell} ipython3
g = LinearExpression(a=3, b=-6)
g.get_roots()
```

> `3`. $h(x) = f(x) + g(x)$

```{code-cell} ipython3
h = f + g
h.get_roots()
```

## Question 3

> `3`. If rain drops were to fall randomly on a square of side length $2r$ the
>  probability of the drops landing in an inscribed circle of radius $r$ would
>  be given by:

>  $$
      P = \frac{\text{Area of circle}}{\text{Area of square}}=\frac{\pi r ^2}{4r^2}=\frac{\pi}{4}
  $$

>  Thus, if we can approximate $P$ then we can approximate $\pi$ as $4P$. In this
>  question we will write code to approximate $P$ using the random library.

>  First create the following class:

>  ```
>  class Drop():
>      """
>      A class that to represent a random rain drop falling on a square of
>      length r.
>      """
>      def __init__(self, r=1):
>          self.x = (.5 - random.random()) * 2 * r
>          self.y = (.5 - random.random()) * 2 * r
>          self.in_circle = (self.y) ** 2 + (self.x) ** 2 <= r ** 2
>  ```

```{code-cell} ipython3
import random

class Drop():
    """
    A class that to represent a random rain drop falling on a square of
    length r.
    """
    def __init__(self, r=1):
        self.x = (.5 - random.random()) * 2 * r
        self.y = (.5 - random.random()) * 2 * r
        self.in_circle = (self.y) ** 2 + (self.x) ** 2 <= r ** 2
```

>  To approximate $P$ create $N=1000$ instances of Drops and count the
>  number of those that are in the circle. Use this to approximate $\pi$.

We start by creating the required number of drops:

```{code-cell} ipython3
number_of_instances = 10000
random.seed(0)
drops = [Drop() for number in range(number_of_instances)]
```

Now we count the number in the circle:

```{code-cell} ipython3
number_in_circle = len([drop for drop in drops if drop.in_circle])
number_in_circle
```

The number in the circle leads to the probability $P$:

```{code-cell} ipython3
P = number_in_circle / number_of_instances
```

And $\pi$ can be approximated:

```{code-cell} ipython3
4 * P
```

## Question 4

> `4`. In a similar fashion to question 3, approximate the integral
>  $\int_{0}^11-x^2\;dx$. Recall that the integral corresponds to the area
>  under a curve.

We create a different drop class changing the `in_circle` attribute to
`under_curve` and simplifying where the `x` and `y` are sampled from.

```{code-cell} ipython3
class Drop():
    """
    A class used to represent a random rain drop falling on a square of
    length 1.
    """

    def __init__(self):
        self.x = random.random()
        self.y = random.random()
        self.under_curve = self.y <= 1 - self.x ** 2
```

Now we repeat the steps of question 3:

```{code-cell} ipython3
number_of_instances = 10000
random.seed(0)
drops = [Drop() for number in range(number_of_instances)]
```

Now we count the number in the circle:

```{code-cell} ipython3
number_under_curve = len([drop for drop in drops if drop.under_curve])
number_under_curve
```

In this particular problem the area of the square is 1 so the probability of
being under the curve is equal to the 1: $P=\frac{\int_{0}^11-x^2\;dx}{1}$.

```{code-cell} ipython3
number_under_curve / number_of_instances
```

We can confirm this:

```{code-cell} ipython3
import sympy as sym

x = sym.Symbol("x")
sym.integrate(1 - x ** 2, (x, 0, 1))
```
