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

Similarly to the previous chapter, we will use a computer to gain numerical
evidence for a problem.

```{admonition} Problem
The Fibonacci numbers are defined by the following sequence:

$$
\left\{\begin{array}{l}
    a_0 = 0,\\
    a_1 = 1,\\
    a_n = a_{n - 1} + a_{n - 2}, n \geq 2\end{array}\right.
$$

Verify the following that the following identify holds for $n\leq 500$:

$$
    \sum_{i=0}^n a_i = a_{n + 2} - 1
$$
```

We will start by defining a function for $a(n)$:

```{code-cell} ipython3
import functools


@functools.lru_cache()
def get_fibonacci(n):
    """
    Return the nth Fibonacci number
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return get_fibonacci(n - 1) + get_fibonacci(n - 2)
```

```{attention}
We are using caching in that function definition with `lru_cache`. This is not
necessary but makes the code more efficient. We spoke about caching in
{ref}`what_is_caching`.
```

We will print the first 10 numbers to ensure everything is working correctly:

```{code-cell} ipython3
for n in range(10):
    print(get_fibonacci(n))
```

Now we will write a function that returns a boolean: `True` if the equation
holds for a given value of $n$, `False` otherwise.

```{code-cell} ipython3
def check_theorem(n):
    """
    Check the relationship for the sum of the first n fibonacci numbers
    """
    sum_of_fibonacci = sum(get_fibonacci(n) for n in range(n + 1))
    return sum_of_fibonacci == get_fibonacci(n + 2) - 1
```

We can then generate checks for $n\leq 500$:

```{code-cell} ipython3
checks = [check_theorem(n) for n in range(501)]
checks
```

Confirm that all the booleans in `check` are `True`:

```{code-cell} ipython3
all(checks)
```

```{attention}
Similarly to `and` and `or` (see {ref}`how_to_combine_boolean_variables`), `all`
is an operator that takes an iterable of booleans and returns if they are all
`True`. Another similar operator is `any`.
```
