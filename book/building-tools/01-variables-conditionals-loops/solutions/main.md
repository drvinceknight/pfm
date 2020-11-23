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

> `1`. Using a `for` loop print the types of the variables in each of the
> following iterables:


>  `1`. `iterable = (1, 2, 3, 4)`

```{code-cell} ipython 3
for variable in (1, 2, 3, 4):
    print(type(variable))
```

> `2`. `iterable = (1, 2.0, 3, 4.0)`

```{code-cell} ipython3
for variable in (1, 2.0, 3, 4.0):
    print(type(variable))
```

> `3`. `iterable = (1, "dog", 0, 3, 4.0)`

```{code-cell} ipython3
for variable in (1, "dog", 0, 3, 4.0):
    print(type(variable))
```

## Question 2

> `2`. Consider the following polynomial:

> $$ 3 n ^ 3 - 183n ^ 2 + 3318n - 18757 $$

> `1`. Use the `sympy.isprime` function to find the lowest positive integer value
> of $n$ for which the absolute value of that polynomial is not prime?

Start by defining the cubic:

```{code-cell} ipython3
import sympy as sym


def cubic(n):
    """
    Return the value of the absolute value of the cubic for the given value of n
    """
    return abs(3 * n ** 3 - 183 * n ** 2 + 3318 * n - 18757)
```

Increment `n` until `cubic(n)` is no longer prime:

```{code-cell} ipython3
n = 1
while sym.isprime(cubic(n)) is True:
    n += 1

n
```

> `2`. How many **unique** primes up until the first non prime value are there?
> (Hint: the `set` tool might prove useful here.)

```{code-cell} ipython3
:tags: ["output_scroll"]

primes = [cubic(n_value) for n_value in range(1, n)]
unique_primes = set(primes)
unique_primes
```

Let us count them:

```{code-cell} ipython3
len(unique_primes)
```

## Question 3

> `3`. Check the following identify for each value of $n\in\{0, 10, 100, 2000\}$:
>  $ \sum_{i=0}^n i=\frac{n(n+1)}{2} $

Define a function to check the identity:

```{code-cell} ipython3
def check_identity(n):
    """
    Computes lhs and the rhs of the given identity.
    """
    lhs = sum(i for i in range(n + 1))
    rhs = n * (n + 1) / 2
    return lhs == rhs
```

Checks the identify for the given values:

```{code-cell} ipython3
all(check_identity(n) for n in (0, 10, 100, 2000))
```

## Question 4

> `4`. Check the following identify for all positive integer values of $n$ less
> than 5000: $ \sum_{i=0}^n i^2=\frac{n(n+1)(2n+1)}{6} $

Define a function to check the identity:

```{code-cell} ipython3
def check_identity(n):
    """
    Computes lhs and the rhs of the given identity.
    """
    lhs = sum(i ** 2 for i in range(n + 1))
    rhs = n * (n + 1) * (2 * n + 1) / 6
    return lhs == rhs
```

Checks the identify for the given values:

```{code-cell} ipython3
all(check_identity(n) for n in range(1, 5001))
```

## Question 5

> `5`. Repeat the experiment of selecting a random integer between 0 and 10
> until it is even 1000 times (see
> {ref}`repeat_code_while_a_given_condition_holds`).  What is the average number
> of times taken to select an even number?

Write a function to repeat the code from
{ref}`repeat_code_while_a_given_condition_holds`:

```{code-cell} ipython3
import random


def count_number_of_selections_until_even(seed):
    """
    Repeatedly sample an integer between 0 and 10 for a given random seed.

    This function returns the number of selections needed.
    """
    random.seed(seed)
    selected_integer = random.randint(0, 10)
    number_of_selections = 1
    while selected_integer % 2 == 1:
        selected_integer = random.randint(0, 10)
        number_of_selections += 1
    return number_of_selections
```

Now use this for 1000 random repetitions (we use each repetition as a seed):

```{code-cell} ipython3
:tags: ["output_scroll"]

number_of_selections = [
    count_number_of_selections_until_even(seed) for seed in range(1000)
]
number_of_selections
```

We will use `numpy` which has a `mean` function:

```{code-cell} ipython3
import numpy as np

np.mean(number_of_selections)
```
