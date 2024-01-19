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

Verify that the following identity holds for $n\leq 500$:

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
    A function to give the nth Fibonacci number using the recursive
    definition.

    Note that this also uses a cache.

    Parameters
    ----------
    n: int
        The index of the Fibonacci number

    Returns
    -------
    int
        The nth Fibonacci number
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
    A function that generate the lhs and rhs of the
    following relationship:

    \sum_{i=0}^n a_i = a_{n + 2} - 1

    Where `a_i` is the i-th Fibonacci number.

    It checks if the relationship holds.

    Parameters
    ----------
    n: int
        The index n for which the theorem is to be verified.

    Returns
    -------
    bool
        Whether or not the theorem holds for a given n.
    """
    sum_of_fibonacci = sum(get_fibonacci(i) for i in range(n + 1))
    return sum_of_fibonacci == get_fibonacci(n + 2) - 1
```

We can then generate checks for $n\leq 500$:

```{code-cell} ipython3
:tags: ["output_scroll"]

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
