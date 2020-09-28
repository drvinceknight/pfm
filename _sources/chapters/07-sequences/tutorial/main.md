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

We will solve the following problem using a computer to using a programming
technique called **recursion**.

```{admonition} Problem

A sequence $a_1, a_2, a_3, …$ is defined by:

$$
    \left\{
    \begin{array}{l}
        a_1 = k,\\
        a_{n + 1} = 2a_n – 7, n \geq 1,
    \end{array}
    \right.
$$

where $k$ is a constant.


1. Write down an expression for $a_2$ in terms of $k$.
2. Show that $a_3 = 4k -21$
3. Given that $\sum_{r=1}^4 a_r = 43$ find the value of $k$.
```

We will use a Python to define a function that reproduces the mathematical
definition of $a_k$:

```{code-cell} ipython3
def generate_a(k_value, n):
    """
    Uses recursion to return a_n for a given value of k:

    a_1 = k
    a_n = 2a_n - 7
    """
    if n == 1:
        return k_value
    return 2 * generate_a(k_value, n - 1) - 7
```

```{attention}
This is similar to the mathematical definition the Python definition of
the function refers to itself.
```


We can use this to compute $a_3$ for $k=4$:

```{code-cell} ipython3
generate_a(k_value=4, n=3)
```

We can use this to compute $a_5$ for $k=1$:

```{code-cell} ipython3
generate_a(k_value=1, n=5)
```

Finally it is also possible to pass a symbolic value to `k_value`. This allows
us to answer the first question:

```{code-cell} ipython3
import sympy as sym

k = sym.Symbol("k")
generate_a(k_value=k, n=2)
```

Likewise for $a_3$:

```{code-cell} ipython3
generate_a(k_value=k, n=3)
```

For the last question we start by computing the sum:

$$
    \sum_{r=1}^4 a_r = 43
$$

```{code-cell} ipython3
sum_of_first_four_terms = sum(generate_a(k_value=k, n=r) for r in range(1, 5))
sum_of_first_four_terms
```

This allows us to create the given equation and solve it:

```{code-cell} ipython3
equation = sym.Eq(sum_of_first_four_terms, 43)
sym.solveset(equation, k)
```

```{important}
In this tutorial we have

- Defined a function using recursion.
- Called this function using both numeric and symbolic values.
```
