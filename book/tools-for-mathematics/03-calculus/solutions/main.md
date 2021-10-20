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

> 1. For each of the following functions calculate $\frac{df}{dx}$,
>    $\frac{d^2f}{dx^2}$ and $\int f(x) dx$.

> $f(x) = x$

```{code-cell} ipython3
import sympy as sym

x = sym.Symbol("x")
expression = x
sym.diff(expression, x)
```

```{code-cell} ipython3
sym.diff(expression, x, 2)
```

```{code-cell} ipython3
sym.integrate(expression, x)
```

> $f(x) = x ^{\frac{1}{3}}$

```{code-cell} ipython3
expression = x ** (sym.S(1) / 3)
sym.diff(expression, x)
```

```{code-cell} ipython3
sym.diff(expression, x, 2)
```

```{code-cell} ipython3
sym.integrate(expression, x)
```

> $f(x) = 2 x (x - 3) (\sin(x) - 5)$

```{code-cell} ipython3
expression = 2 * x * (x - 3) * (sym.sin(x) - 5)
sym.diff(expression, x)
```

```{code-cell} ipython3
sym.diff(expression, x, 2)
```

```{code-cell} ipython3
sym.integrate(expression, x)
```

> $f(x) = 3  x ^ 3 + 6 \sqrt{x} + 3$

```{code-cell} ipython3
expression = 3 * x ** 3 + 6 * sym.sqrt(x) + 3
sym.diff(expression, x)
```

```{code-cell} ipython3
sym.diff(expression, x, 2)
```

```{code-cell} ipython3
sym.integrate(expression, x)
```

## Question 2

> `2`. Consider the function $f(x)=2x+1$. By differentiating _from first
> principles_ show that $f'(x)=2$.

Using the definition of the derivative:

```{code-cell} ipython3
h = sym.Symbol("h")
expression = 2 * x + 1
sym.limit((expression - expression.subs({x: x - h})) / h, h, 0)
```

## Question 3

> `3`. Consider the second derivative $f''(x)=6x+4$ of some cubic function $f(x)$.

> `1`. Find $f'(x)$

We know the derivative will be the integral of the second derivative with a
constant:

```{code-cell} ipython3
c1 = sym.Symbol("c1")

second_derivative = 6 * x + 4
derivative = sym.integrate(second_derivative, x) + c1
derivative
```

> `2`. You are given that $f(0)=10$ and $f(1)=13$, find $f(x)$.

We know that the cubic will be the integral of the derivative with constant:

```{code-cell} ipython3
c2 = sym.Symbol("c2")

cubic = sym.integrate(derivative, x) + c2
cubic
```

We substitute $x=0$:

```{code-cell} ipython3
cubic.subs({x: 0})
```

This gives $c_2=10$. We substitute that back in to our expression for the cubic:

```{code-cell} ipython3
cubic = cubic.subs({c2: 10})
cubic
```

and now substitute $x=1$:

```{code-cell} ipython3
cubic.subs({x: 1})
```

which gives $c_1=0$ which we substitute back in to our expression for the cubic:

```{code-cell} ipython3
cubic = cubic.subs({c1: 0})
cubic
```

> `3`. Find all the stationary points of $f(x)$ and determine their nature.

The stationary points are the points that give $\frac{df}{dx}=0$:

```{code-cell} ipython3
stationary_points = sym.solveset(sym.diff(cubic, x), x)
stationary_points
```

We determine the nature of these turning points by considering the sign of $\frac{d^2f}{dx^2}$ at each point.

```{code-cell} ipython3
second_derivative.subs({x: -4 / sym.S(3)})
```

This is negative, so it is a local maximum.

```{code-cell} ipython3
second_derivative.subs({x: 0})
```

This is positive, so it is a local minimum.

## Question 4

> `4`. Consider the function $f(x)=\frac{2}{3}x ^ 3 + b x ^ 2 + 2 x + 3$, where
> $b$ is some undetermined coefficient.

> `1`. Find $f'(x)$ and $f''(x)$

```{code-cell} ipython3
b = sym.Symbol("b")
expression = sym.S(2) / 3 * x ** 3 + b * x ** 2 + 2 * x + 3
derivative = sym.diff(expression, x)
derivative
```

```{code-cell} ipython3
second_derivative = sym.diff(expression, x, 2)
```

> `2`. You are given that $f(x)$ has a stationary point at $x=2$. Use this
> information to find $b$.

We solve the equation that arises when substituting $x=2$ in to the derivative:

```{code-cell} ipython3
equation = sym.Eq(derivative.subs({x: 2}), 0)
equation
```

```{code-cell} ipython3
sym.solveset(equation, b)
```

> `3`. Find the coordinates of the other stationary point.

We substitute this value of $b$ in to the expression:

```{code-cell} ipython3
b_value = -sym.S(5) / 2
expression = expression.subs({b: b_value})
expression
```

and the derivative and then solve the equation:

```{code-cell} ipython3
derivative = derivative.subs({b: b_value})
sym.solveset(derivative)
```

This confirms that one stationary point is indeed at $x=2$, the other is at
$x=1/2$.
To get the full coordinate of this other stationary point we substitute this
value of $x$ in to $f$:

```{code-cell} ipython3
expression.subs({b: b_value, x: sym.S(1) / 2})
```

> `4`. Determine the nature of both stationary points.

Substituting both values in to the second derivative:

```{code-cell} ipython3
second_derivative = second_derivative.subs({b: b_value})
second_derivative.subs({x: sym.S(1) / 2})
```

This is negative so it is a local maxima.

```{code-cell} ipython3
second_derivative.subs({x: 2})
```

This is positive so it is a local minima.

## Question 5

> `5`. Consider the functions $f(x)=-x^2+4x+4$ and $g(x)=3x^2-2x-2$.

> `1`. Create a variable `turning_points` which has value the turning points of
> $f(x)$.

```{code-cell} ipython3
f = -(x ** 2) + 4 * x + 4
derivative = sym.diff(f, x)
turning_points = sym.solveset(derivative, x)
```

> `2`. Create variable `intersection_points` which has value of the points where
> $f(x)$ and $g(x)$ intersect.

```{code-cell} ipython3
g = 3 * x ** 2 - 2 * x - 2
equation = sym.Eq(f, g)
intersection_points = sym.solveset(equation, x)
intersection_points
```

> `3`. Using your answers to parts 2., calculate the area of the region between
> $f$ and $g$. Assign this value to a variable `area_between`.

The area between $f$ and $g$ corresponds to the integral of $\pm (f - g)$
between the points of intersection. We here use $f - g$, if the outcome was
negative we would take the opposite.

```{code-cell} ipython3
area_between = sym.integrate(
    f - g, (x, sym.S(3) / 4 - sym.sqrt(33) / 4, sym.S(3) / 4 + sym.sqrt(33) / 4)
)
sym.simplify(area_between)
```
