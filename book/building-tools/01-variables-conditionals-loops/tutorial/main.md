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

We will here use a computer to gain some evidence to help tackle the following
problem.

```{admonition} Problem

Consider the following polynomial:

$$
    p(n) = n ^ 2 + n + 41
$$

1. Verify that $p(n)$ is prime for $n\in \mathbb{Z}$ up until $n=20$.
2. What is the smallest value of $n$ for which $p(n)$ is no longer prime?

```

We will start by defining a function for $p(n)$:

```{code-cell} ipython3
def p(n):
    """
    Return the value of n ^ 2 + n + 41 for a given value of n.
    """
    return n ** 2 + n + 41
```

We will use `sympy` to check if a number is prime.

```{code-cell} ipython3
import sympy as sym

sym.isprime(3)
```

```{code-cell} ipython3
sym.isprime(4)
```

Now to answer the first question we will use a list comprehension to create a
list of boolean variables that confirm if $p(n)$ is prime.

```{tip}
This is similar to what we did in {ref}`probability`.
```

```{code-cell} ipython3
checks = [sym.isprime(p(n)) for n in range(21)]
checks
```

We can use the `all` tool to check if all the boolean values are true:

```{code-cell} ipython3
all(checks)
```

```{attention}
Using list comprehensions is a mathematical way of repeating code but at times
it might prove useful to repeat code in a different way using a standard `if`
statement.
```

In that case we can essentially repeat the previous exercise using:

```{code-cell} ipython3
checks = []
for n in range(21):
    value = p(n)
    is_prime = sym.isprime(value)
    checks.append(is_prime)
all(checks)
```

The main difference between the two approaches is that we can include multiple
lines of indented code to be repeated for every value of `n` in `range(21)`.

```{attention}
A `for` loop or a list comprehension should be used when we know how many
repetitions we want to make.
```

To answer the second question we will repeat the code until the value of $p(n)$
is no longer prime.

```{code-cell} ipython3
n = 0
while sym.isprime(p(n)):
    n += 1
n
```

```{attention}
A `while` loop should be used when we do not know how many times a repetition
should be made **but** we know under what conditions is should be made
```

Indeed for that value of $n$ we have:

```{code-cell} ipython3
p(n)
```

and

```{code-cell} ipython3
sym.isprime(p(n))
```

`sympy` can also factor the number for us:

```{code-cell} ipython3
sym.factorint(p(n))
```

Indeed:

```{code-cell} ipython3
41 ** 2
```
