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

## Define a function using recursion

It is possible to define a recursive expression using a recursive
function in Python. This requires two things:

- A recursive rule: something that relates the current term to another
  one;
- A base case: a particular term that does not need the recursive rule
  to be calculated.

Consider the following mathematical expression:

$$
    \left\{
    \begin{array}{l}
        a_1 = 1,\\
        a_n = 2a_{n - 1}, n > 1,
    \end{array}
    \right.
$$

- The recursive rule is: $a_n = 2a_{n - 1}$;
- The base case is: $a_1 = 1$.

In Python this can be written as:

```{code-cell} ipython3
def generate_sequence(n):
    """
    Generate the sequence defined by:

    a_1 = 1
    a_n = 2 a_{n - 1}

    This is done using recursion.
    """
    if n == 1:
        return 1
    return 2 * generate_sequence(n - 1)
```

Here you can get the first 7 terms:

```{code-cell} ipython3
values_of_sequence = [generate_sequence(n) for n in range(1, 8)]
values_of_sequence
```
