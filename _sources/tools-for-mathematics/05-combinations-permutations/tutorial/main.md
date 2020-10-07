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

We will solve the following problem using a computer to illustrate how a
computer can be used to solve combinatorial problems:


```{admonition} Problem

The digits 1, 2, 3, 4 and 5 are arranged in random order, for form a five-digit number.

1. How many different five-digit numbers can be formed?
2. How many different five-digit numbers are:
    1. Odd
    2. Less than 23000
```

First we are going to get the 5 digits. Python has a nice tool for this called
`range` which gives us directly the integers from a given bound to another:

```{code-cell} ipython3
import itertools

digits = range(1, 6)
digits
```

At present that is only the instructions containing the integers from 1 to 5
(the 6 is a strict upper bound). We can transform this to a tuple, using the
`tuple` tool:

```{code-cell} ipython3
tuple(range(1, 6))
```

The question is asking us to get all the permutations of size 5 of that set of
integers.

The main tool we use for this is a library specifically designed to iterate over
objects in different ways: `itertools`.

```{code-cell} ipython3
:tags: [nbval-ignore-output]

permutations = itertools.permutations(digits)
permutations
```

That is again only the set of instructions, to view the actual permutations we
will again transform this in to a tuple. We will do this an overwrite the value
of `permutations` to not be the instructions but the actual tuple of all the
permutations:

```{code-cell} ipython3
:tags: [output_scroll]

permutations = tuple(permutations)
permutations
```

Now to answer the question we need to find out how many tuples are in that
tuple. We do this using the Python `len` tool which returns the length of
something:

```{code-cell} ipython3
len(permutations)
```

We can confirm this to be correct as we know that there are $5!$ ways of
arranging those numbers. The `math` library has a `factorial` tool:

```{code-cell} ipython3
import math

math.factorial(5)
```

In order to find out how many 5 digit numbers are odd we are going to compute
the following sum:


$$
    \sum_{\pi \in \Pi} \pi_5 \mod 2
$$

Where $\Pi$ is the set of permutations and $\pi_5$ denotes the 5th (and last)
element of the permutation. So for example, if the first element of $\Pi$ was
$(1, 2, 3, 4, 5)$ then $\pi_5=5$ and $5 \mod 2=1$.

To do this we use the `sum` tool in python coupled with the expressions `for`
and `in`. We also access the 5th element of a `permutation` using `[4]` (the
first element is denoted with a 0, so the 5th is 4):

```{code-cell} ipython3
sum(permutation[4] % 2 for permutation in permutations)
```

We can again check this theoretically, there are three valid choices for the
last digit of a given tuple to be odd: $1$, $3$ and $5$. For each of those,
there are then 4 choices for the remaining digits:

```{code-cell} ipython3
math.factorial(4) * 3
```

To compute the number of digits that are less than or equal to 2300 we compute a
similar sum except we use the `<=` operator and also convert the tuple of digits
to a number in base 10:

$$
    (\pi_1, \pi_2, \pi_3, \pi_4, \pi_5) \to \pi_1 10 ^ 4 + \pi_2 10 ^ 3 + \pi_3 10 ^ 2 + \pi_4 10 + \pi_5
$$

Thus we are going to compute the following sum:

$$
    \sum_{\pi \in \Pi \text{ if }\pi_1 10 ^ 4 + \pi_2 10 ^ 3 + \pi_3 10 ^ 2 + \pi_4 10 + \pi_5 \leq 2300} 1
$$

```{code-cell} ipython3
sum(
    1
    for permutation in permutations
    if permutation[0] * 10 ** 4
    + permutation[1] * 10 ** 3
    + permutation[2] * 10 ** 2
    + permutation[3] * 10
    + permutation[0]
    <= 23000
)
```

We can again confirm this theoretically, for a given tuple to be less than 2300
that is only possible if the first digit is 1 or 2:

- If it is 1 then any of the other $4!$ permutations of the other digits is
  valid;
- If it is 2 then the second digit must be 1 and any of the other $3!$
  permutations of the other digits is valid.

```{code-cell} ipython3
(math.factorial(4) + math.factorial(3))
```

```{important}
In this tutorial we have

- Created permutations of a given tuples.
- Created permutations of a given tuples that obey a given condition.
- Counted how many permutations exist.
- Directly computed the expected number of permutations.
```
