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

> `1`. Simplify the following expressions:

> $\frac{3}{\sqrt{3}}$:

```{code-cell} ipython3
import sympy as sym

expression = sym.S(3) / sym.sqrt(3)
sym.simplify(expression)
```

> $\frac{2 ^ {78}}{2 ^ {12}2^{-32}}$:

```{code-cell} ipython3
sym.S(2) ** 78 / (sym.S(2) ** 12 * sym.S(2) ** (-32))
```

> $8^0$:

```{code-cell} ipython3
sym.S(8) ** 0
```

> $a^4b^{-2}+a^{3}b^{2}+a^{4}b^0$:

```{code-cell} ipython3
a = sym.Symbol("a")
b = sym.Symbol("b")
sym.factor(a ** 4 * b ** (-2) + a ** 3 * b ** 2 + a ** 4 * b ** 0)
```

## Question 2

> `2`. Solve the following equations:

> $x + 3 = -1$:

```{code-cell} ipython3
x = sym.Symbol("x")
equation = sym.Eq(x + 3, -1)
sym.solveset(equation, x)
```

> $3 x ^ 2 - 2 x = 5$:

```{code-cell} ipython3
equation = sym.Eq(3 * x ** 2 - 2 * x, 5)
sym.solveset(equation, x)
```

> $x (x - 1) (x + 3) = 0$:

```{code-cell} ipython3
equation = sym.Eq(x * (x - 1) * (x + 3), 0)
sym.solveset(equation, x)
```

> $4 x ^3 + 7x - 24 = 1$:

```{code-cell} ipython3
equation = sym.Eq(4 * x ** 3 + 7 * x - 24, 1)
sym.solveset(equation, x)
```

## Question 3

> `3`. Consider the equation: $x ^ 2 + 4 - y = \frac{1}{y}$:

> Find the solution to this equation for $x$.

```{code-cell} ipython3
y = sym.Symbol("y")
equation = sym.Eq(x ** 2 + 4 - y, 1 / y)
solution = sym.solveset(equation, x)
solution
```

> Obtain the specific solution when $y = 5$. Do this in two ways:
> substitute the value in to your equation and substitute the value in to
> your solution.

```{code-cell} ipython3
solution.subs({y: 5})
```

```{code-cell} ipython3
solution = sym.solveset(equation.subs({y: 5}), x)
solution
```

## Question 4

> `4`. Consider the quadratic: $f(x)=4x ^ 2 + 16x + 25$:

> Calculate the discriminant of the quadratic equation $4x ^ 2 + 16x + 25 =
> 0$. What does this tell us about the solutions to the equation? What
> does this tell us about the graph of $f(x)$?

```{code-cell} ipython3
quadratic = 4 * x ** 2 + 16 * x + 25
sym.discriminant(quadratic)
```
 
This is negative so we know that the equation does not have any real solutions and
hence the graph does not cross the x-axis. 
Since the coefficient of $x^2$ is positive it means that the graph is above 
the $y=0$ line.


> By completing the square, show that the minimum point of $f(x)$ is
> $\left(-2, 9\right)$

```{code-cell} ipython3
a, b, c = sym.Symbol("a"), sym.Symbol("b"), sym.Symbol("c")
completed_square = a * (x - b) ** 2 + c
sym.expand(completed_square)
```

This gives $a=4$.

```{code-cell} ipython3
completed_square = completed_square.subs({a: 4})
sym.expand(completed_square)
```

Comparing the coefficients of $x$ we have the equation:

$$
  - 8 b = 16
$$

```{code-cell} ipython3
equation = sym.Eq(-8 * b, 16)
sym.solveset(equation, b)
```

Substituting:

```{code-cell} ipython3
completed_square = completed_square.subs({b: -2})
sym.expand(completed_square)
```

Comparing the coefficients of $x^0$ this gives:

$$c+16=25$$

```{code-cell} ipython3
equation = sym.Eq(c + 16, 25)
sym.solveset(equation, c)
```

```{code-cell} ipython3
completed_square = completed_square.subs({c: 9})
completed_square
```

The lowest value of $f(x)$ is for $x=-2$ which gives: $f(-2)=9$ as expected.

## Question 5

> `5`. Consider the quadratic: $f(x)=-3x ^ 2 + 24x - 97$:

> Calculate the discriminant of the quadratic equation $-3x ^ 2 + 24x - 97 =
> 0$. What does this tell us about the solutions to the equation? What
> does this tell us about the graph of $f(x)$?


```{code-cell} ipython3
quadratic = -3 * x ** 2 + 24 * x - 97
sym.discriminant(quadratic)
```

This is negative so we know that the equation does not have any real solutions and
hence the graph does not cross the x-axis. 
Since the coefficient of $x^2$ is negative it means that the graph is below 
the $y=0$ line.


> By completing the square, show that the maximum point of $f(x)$ is
> $\left(4, -49\right)$

```{code-cell} ipython3
a, b, c = sym.Symbol("a"), sym.Symbol("b"), sym.Symbol("c")
completed_square = a * (x - b) ** 2 + c
sym.expand(completed_square)
```

This gives $a=-3$.

```{code-cell} ipython3
completed_square = completed_square.subs({a: -3})
sym.expand(completed_square)
```

Comparing the coefficients of $x$ we have the equation:

$$
  6 b = 24
$$

```{code-cell} ipython3
equation = sym.Eq(6 * b, 24)
sym.solveset(equation, b)
```

Substituting:

```{code-cell} ipython3
completed_square = completed_square.subs({b: 4})
sym.expand(completed_square)
```

Comparing the coefficients of $x^0$ this gives:

$$c-48=-97$$

```{code-cell} ipython3
equation = sym.Eq(c - 48, -97)
sym.solveset(equation, c)
```

```{code-cell} ipython3
completed_square = completed_square.subs({c: -49})
completed_square
```

The highest value of $f(x)$ is for $x=4$ which gives: $f(4)=-49$ as expected.

`6`. Consider the function $f(x) = x^ 2 + a x + b$.

> Given that $f(0) = 0$ and $f(3) = 0$ obtain the values of $a$ and $b$.

Substituting 0 in to $f$ gives:

```{code-cell} ipython3
expression = x ** 2 + a * x + b
expression.subs({x: 0})
```

This implies that $b=0$. Substituting back in to the expression:

```{code-cell} ipython3
expression = expression.subs({b: 0})
expression
```

Substituting $x=3$ in to this expression gives:

```{code-cell} ipython3
expression.subs({x: 3})
```

This gives the equation:

$$
    3 a + 9 = 0
$$

```{code-cell} ipython3
sym.solveset(expression.subs({x: 3}), a)
```

Our expression is thus:

```{code-cell} ipython3
expression = expression.subs({a: -3})
expression
```

> By completing the square confirm that graph of $f(x)$ has a line of symmetry
> at $x=\frac{3}{2}$

```{code-cell} ipython3
completed_square = a * (x - b) ** 2 + c
sym.expand(completed_square)
```

We see that $a=1$ and. Substituting:

```{code-cell} ipython3
completed_square = completed_square.subs({a: 1})
sym.expand(completed_square)
```

This gives:

$$
    -2b=-3
$$

```{code-cell} ipython3
equation = sym.Eq(-2 * b, -3)
sym.solveset(equation, b)
```

Substituting:

```{code-cell} ipython3
completed_square = completed_square.subs({b: sym.S(3) / 2})
sym.expand(completed_square)
```

Which gives:

$$
    c + 9 / 4 = 0
$$

```{code-cell} ipython3
equation = sym.Eq(c + sym.S(9) / 4, 0)
sym.solveset(equation, c)
```

Substituting:

```{code-cell} ipython3
completed_square = completed_square.subs({c: -sym.S(9) / 4})
completed_square
```

Thus $x=3/2$ is a line of symmetry.
