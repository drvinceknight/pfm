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

(algebra_tutorial)=

# Tutorial

To demonstrate the ways in which we can use a computer to assist with Algebra we
will solve the following two problems:

```{admonition} Problem

1. Rationalise the denominator of $\frac{1}{\sqrt{2} + 1}$
2. Consider the quadratic: $f(x)=2x ^ 2 + x + 1$:
    1. Calculate the discriminant of the quadratic equation $2x ^ 2 + x + 1 =
     0$. What does this tell us about the solutions to the equation? What
     does this tell us about the graph of $f(x)$?
    2. By completing the square, show that the minimum point of $f(x)$ is
     $\left(-\frac{1}{4}, \frac{7}{8}\right)$
```

To do this we will be using a specific collections of tools available in Python.
Often specific sets of tools are separated in to things called **libraries**. We
start by telling Python that we want to use the specific library for **symbolic
mathematics**:

```{code-cell} ipython3
import sympy
```

This allows us to solve the first part of the question. First we create a
variable `expression` and **assign** it a value of $\frac{1}{\sqrt{2} + 1}$.

```{code-cell} ipython3
expression = 1 / (sympy.sqrt(2) + 1)
expression
```

```{attention}
This is not what would happen if we plugged the above in to a basic calculator,
it would instead give us a value of:
```

```{code-cell} ipython3
float(expression)
```

The `sympy` library has a diverse set of tools available, one of which is to
algorithmically attempt to simplify an expression. Here is how we do that:

```{code-cell} ipython3
sympy.simplify(expression)
```

This implies that:

$$
    \frac{1}{\sqrt{2} + 1} = -1 + \sqrt{2}
$$

If we multiply both sides by ${\sqrt{2} + 1}$ we get:

$$
    1=\frac{1}{\sqrt{2} + 1}\times \left(\sqrt{2} + 1\right) = \left(-1 + \sqrt{2}\right)\times \left(\sqrt{2} + 1\right)
$$

The `sympy.simplify` command did not give us much insight in to what happened
but we can further confirm that above manipulation by expanding $\left(-1 +
\sqrt{2}\right)\times \left(\sqrt{2} + 1\right)$.

Here is how we do that:

```{code-cell} ipython3
sympy.expand((-1 + sympy.sqrt(2)) * (1 + sympy.sqrt(2)))
```

We see that `sympy` allows us to carry out basic expression manipulation. We
will now consider the second part of the question:

```{admonition} Problem

2. Consider the quadratic: $f(x)=2x ^ 2 + x + 1$:
  1. Calculate the discriminant of the quadratic equation $2x ^ 2 + x + 1 =
     0$. What does this tell us about the solutions to the equation? What
     does this tell us about the graph of $f(x)$?
  2. By completing the square, show that the minimum point of $f(x)$ is
     $\left(-\frac{1}{4}, \frac{7}{8}\right)$
```

We will start by reassigning the value of the variable `expression` to be the
expression: $2x ^ 2 + x + 1$.

```{code-cell} ipython3
x = sympy.Symbol("x")
expression = 2 * x ** 2 + x + 1
expression
```

```{tip}
**Recall** that the `**` symbol is how we communicate exponentiation.
```

```{attention}
We start by communicating to the code that `x` is going to be a symbolic variable.
```

We can immediately use this to compute the discriminant:

```{code-cell} ipython3
sympy.discriminant(expression)
```

Now we can complement this with our mathematical knowledge: if a quadratic has a
negative discriminant then it does not have any roots and all the values are of
the same sign as the coefficient of $x ^ 2 $. Which in this case is $2>0$.

We can confirm this by directly creating the equation. We do this by creating a
variable `equation` and assigning it the equation which has a `lhs` and a `rhs`:

```{code-cell} ipython3
equation = sympy.Eq(lhs=expression, rhs=0)
equation
```

and asking `sympy` to solve it:

```{code-cell} ipython3
sympy.solveset(equation)
```

Indeed the only solutions are imaginary numbers: this confirms that the graph of
$f(x)$ is a convex parabola that is above the $y=0$ line.

Let us know complete the square so that we can write:

$$
    f(x) = a (x - b) ^ 2 + c
$$

for some values of $a, b, c$.

First let us create variables that have those 3 constants as value but also create a variable `completed_square` and assign it the general expression:

```{code-cell} ipython3
a, b, c = sympy.Symbol("a"), sympy.Symbol("b"), sympy.Symbol("c")
completed_square = a * (x - b) ** 2 + c
completed_square
```

We can expand this:

```{code-cell} ipython3
sympy.expand(completed_square)
```

We will now use `sympy` to solve the various equations that arise from comparing
the coefficients of:

$$
    f(x) = 2x ^2 + x + 1
$$

with the completed square.

First, we see that the coefficient of $x ^ 2$ gives us an equation:

$$
    a = 2
$$

For completeness we will write the code that solves this trivial equation:

```{code-cell} ipython3
equation = sympy.Eq(a, 2)
sympy.solveset(equation, a)
```

We will now substitute this value of $a$ in to the completed square and update the variable with the new value:

```{code-cell} ipython3
completed_square = completed_square.subs({a: 2})
completed_square
```

```{attention}
The different types of brackets being used there: both `()` and `{}`. This is
important and has specific meaning in Python which we will cover soon.
```

Now let us look at the expression with our two remaining constants:

```{code-cell} ipython3
sympy.expand(completed_square)
```

Comparing the coefficients of $x$ we have the equation:

$$
  - 4 b = 1
$$

```{code-cell} ipython3
equation = sympy.Eq(-4 * b, 1)
sympy.solveset(equation, b)
```

We will now substitute this value of $b$ back in to our expression.

```{attention}
We make a point to tell sympy to treat $1 / 4$ symbolically and to not
calculate the numeric value:
```

```{code-cell} ipython3
completed_square = completed_square.subs({b: -1 / sympy.S(4)})
completed_square
```

Expanding this to see our expression with the one remaining constant gives:

```{code-cell} ipython3
sympy.expand(completed_square)
```

We have a final equation for the constant term:

$$
    c + 1 / 8 = 1
$$

We will use sympy to find the value of $c$:

```{code-cell} ipython3
sympy.solveset(sympy.Eq(c + sympy.S(1) / 8, 1), c)
```

As before we will substitute that in and update the value of `completed_square`:

```{code-cell} ipython3
completed_square = completed_square.subs({c: 7 / sympy.S(8)})
completed_square
```

Using this we can see that the there are indeed no values of $x$ which give
negative values of $f(x)$ as $f(x)$ is a square added to a constant.

The minimum is when $x=-1/4$ which gives: $f(-1/4)=7/8$:

```{code-cell} ipython3
completed_square.subs({x: -1 / sympy.S(4)})
```

```{important}
In this tutorial we have

- Created symbolic expressions.
- Obtained approximate values for numerical symbolic expressions.
- Expanded and simplified symbolic expressions.
- Created symbolic equations.
- Solve symbolic equations.
- Substituted values in to symbolic expressions.
```
