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

# References

## What are the differences between recursion and iteration?

When giving instructions to a computer it is possible to use recursion to directly implement a common mathematical definition. For example consider the following sequence:

$$
    \left\{\begin{array}{l}
    a_1 = 1\\
    a_{n + 1}= 3a_n, n > 1
    \end{array}\right.
$$

We can define this in Python as follows:

```{code-cell} ipython3
def generate_sequence(n):
    """
    Generate the sequence defined by:

    a_1 = 1
    a_n = 3 a_{n - 1}

    This is done using recursion.
    """
    if n == 1:
        return 1
    return 3 * generate_sequence(n - 1)
```

The first 6 terms:

```{code-cell} ipython3
[generate_sequence(n) for n in range(1, 7)]
```

We note that in this case this corresponds to powers of $3$, and indeed we can
prove that: $a_n = 3 ^ {n - 1}$. We will not carry out the proof here but one
approach to doing it would be to use proof by induction which is closely related
to recursive functions.

We can write a different python function that uses this formulae. This is called
**iteration**:

```{code-cell} ipython3
def calculate_sequence(n):
    """
    Calculate the nth term of the sequence defined by:

    a_1 = 1
    a_n = 3 a_{n - 1}

    This is done using iteration using the direct formula:

    a_n = 3 ^ n
    """
    return 3 ** (n - 1)
```

```{code-cell} ipython3
[calculate_sequence(n) for n in range(1, 7)]
```

We can in fact use a Jupyter [magic
command](https://ipython.readthedocs.io/en/stable/interactive/magics.html) to
time the run time of a command. It is clear that recursion is slower.

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

%timeit [generate_sequence(n) for n in range(1, 25)]
```

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

%timeit [calculate_sequence(n) for n in range(1, 25)]
```

In practice:

- Using recursion is powerful as it can be used to directly implement recursive
  definitions.
- Using iteration is more computationally efficient but it is not always
  straightforward to obtain an iterative formula.


## What is caching

One of the reasons that recursion is computationally inefficient is that it
always has to recalculate previously calculated values.

For example:


$$
    \left\{\begin{array}{l}
    a_1 = 1\\
    a_{n + 1}= 3a_n, n > 1
    \end{array}\right.
$$

One way to overcome this is to use caching which means that when a function is
called for a value it has already computed it remembers the value.

Python has a caching tool available in the functools library:

```{code-cell} ipython3
import functools


def generate_sequence(n):
    """
    Generate the sequence defined by:

    a_1 = 1
    a_n = 3 a_{n - 1}

    This is done using recursion.
    """
    if n == 1:
        return 1
    return 3 * generate_sequence(n - 1)


@functools.lru_cache()
def cached_generate_sequence(n):
    """
    Generate the sequence defined by:

    a_1 = 1
    a_n = 3 a_{n - 1}

    This is done using recursion but also includes a cache.
    """
    if n == 1:
        return 1
    return 3 * cached_generate_sequence(n - 1)
```

Timing both these approaches confirms a substantial increase in time for the
cached version.

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

%timeit [generate_sequence(n) for n in range(1, 25)]
```

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

%timeit [cached_generate_sequence(n) for n in range(1, 25)]
```
