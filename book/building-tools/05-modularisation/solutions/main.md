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

> `1`. Use the code written in the [Modularisation Tutorial](modularisation_tutorial) to obtain the average time
   until absorption from the first state of the Markov chains with the following transition matrices:

**After making sure the `absorption.py` file written in the [Modularisation
Tutorial](modularisation_tutorial) is in the same directory as our notebook we
can answer the questions:**

> `1`. $P = \begin{pmatrix}1/2 & 1/2 \\ 0 & 1 \end{pmatrix}$

```{code-cell} ipython3
import numpy as np
import absorption

P = np.array(((1 / 2, 1 / 2), (0, 1)))
t = absorption.compute_t(P)
t[0]
```

> `2`. $P = \begin{pmatrix}1/2 & 1/4 & 1/4\\ 1/3 & 1/3 & 1/3  \\0 & 0 & 1 \end{pmatrix}$

```{code-cell} ipython3
P = np.array(((1 / 2, 1 / 4, 1 / 4), (1 / 3, 1 / 3, 1 / 3), (0, 0, 1)))
t = absorption.compute_t(P)
t[0]
```

> `3`. $P = \begin{pmatrix}1 & 0 \\ 1/2 & 1/2 \end{pmatrix}$

```{code-cell} ipython3
P = np.array(((1, 0), (1 / 2, 1 / 2)))
t = absorption.compute_t(P)
t[0]
```

> `4`. $P = \begin{pmatrix}1/2 & 1/4 & 1/4\\ 1/3 & 1/3 & 1/3  \\1/5 & 0 & 4/5 \end{pmatrix}$


```{code-cell} ipython3
P = np.array(((1 / 2, 1 / 4, 1 / 4), (1 / 3, 1 / 3, 1 / 3), (1 / 5, 0, 4 / 5 )))
t = absorption.compute_t(P)
t[0]
```

We see here that we get a large negative number which is nonsensical as an
average time till absorption. **However** the matrix given is not absorbing (it
has no diagonal entry with value 1).

## Question 2

> 2. Modularise the following code by creating a function `flip_coin` that takes a
   `probability_of_selecting_heads` variable.

>   ```
>   def sample_experiment(bag):
>       """
>       This samples a token from a given bag and then
>       selects a coin with a given probability.
>
>       If the sampled token is red then the probability
>       of selecting heads is 4/5 otherwise it is 2/5.
>
>       This function returns both the selected token
>       and the coin face.
>       """
>       selected_token = pick_a_token(container=bag)
>
>       if selected_token == "Red":
>           probability_of_selecting_heads = 4 / 5
>       else:
>           probability_of_selecting_heads = 2 / 5
>
>       if random.random() < probability_of_selecting_heads:
>           coin = "Heads"
>       else:
>           coin = "Tails"
>       return selected_token, coin
>   ```

```{code-cell} ipython3
:tags: ["remove-input"]

def pick_a_token(container):
    """
    A function to randomly sample from a `container`.
    """
    return random.choice(container)
```

```{code-cell} ipython3
import random


def flip_coin(probability_of_selecting_heads):
    """
    This flips a coin with a given probablity of selecting heads.
    """
    if random.random() < probability_of_selecting_heads:
        return "Heads"
    return "Tails"
```

Now the above function becomes:

```{code-cell} ipython3
def sample_experiment(bag):
    """
    This samples a token from a given bag and then
    selects a coin with a given probability.

    If the sampled token is red then the probability
    of selecting heads is 4/5 otherwise it is 2/5.

    This function returns both the selected token
    and the coin face.
    """
    selected_token = pick_a_token(container=bag)

    if selected_token == "Red":
        return selected_token, flip_coin(probability_of_selecting_heads=4 / 5)
    return selected_token, flip_coin(probability_of_selecting_heads=2 / 5)
```

## Question 3

> 3. Modularise the following code by writing 2 further functions:

>   - `get_potential_divisors`: A function to return the integers between 2 and
     $\sqrt{N}$ for a given $N$.
>   - `is_divisor`: A function to check if $n | N$ ("$n$ divides $N$") for given
     $n, N$.

>   ```
>   import math
>
>   def is_prime(N):
>        """
>       Checks if a number N is prime by checking all that positive integers
>       numbers less sqrt(N) than it that divide it.
>
>       Note that if N is not a positive integer great than 1 then it does not
>       check: it returns False.
>       """
>       if N <= 1 or type(N) is not int:
>           return False
>       for potential_divisor in range(2, int(math.sqrt(N)) + 1):
>           if (N % potential_divisor) == 0:
>               return False
>       return True
>   ```

```{code-cell} ipython3
def get_potential_divisors(N):
    """
    Returns the integers between 2 and $\sqrt{N}$.
    """
    return range(2, int(math.sqrt(N) + 1))
```

```{code-cell} ipython3
def is_divisor(N, n):
    """
    Returns a boolean whether or not n divides N
    """
    return N % n == 0
```

Now the `is_prime` function can be written as:

```{code-cell} ipython3
import math

def is_prime(N):
    """
    Checks if a number N is prime by checking all that positive integers
    numbers less sqrt(N) than it that divide it.

    Note that if N is not a positive integer great than 1 then it does not
    check: it returns False.
    """
    if N <= 1 or type(N) is not int:
        return False

    for potential_divisor in get_potential_divisors(N):
        if is_divisor(N, potential_divisor):
            return False
    return True
```

>   Confirm your work by comparing to the results of using `sympy.isprime`.

We see that `sympy.isprime` and `isprime` give the same value for the first 100
possible values:

```{code-cell} ipython3
:tags: ["output_scroll"]

import sympy as sym

for N in range(101):
    print(sym.isprime(N) == is_prime(N))
```

## Question 4

> 4. Write a `stats.py` file with two functions to implement the calculations of
>    mean and population variance.

We place the following code in a `stats.py` file:

```{code-cell} ipython3
def get_mean(iterable):
    """
    Returns the mean of a given iterable which is defined as the sum divided by
    the number of items.
    """
    return sum(iterable) / len(iterable)

def get_population_variance(iterable):
    """
    Returns the population variance of a given iterable which is defined as the
    mean square of the differences from the mean.
    """
    mean = get_mean(iterable)
    squares_of_differences = [(value - mean) ** 2 for value in iterable]
    return get_mean(squares_of_differences)
```

>    Use your functions to compute the mean and population variance of the following
>    collections of numbers:

>    1. $S_1=(1, 2, 3, 4, 4, 4, 4, 4)$

```{code-cell} ipython3
import stats

s1 = (1, 2, 3, 4, 4, 4, 4)
stats.get_mean(iterable=s1)
```

```{code-cell} ipython3
stats.get_population_variance(iterable=s1)
```

>    2. $S_1=(1)$

```{code-cell} ipython3
s2 = (1,)
stats.get_mean(iterable=s2)
```

```{code-cell} ipython3
stats.get_population_variance(iterable=s2)
```
>    3. $S_1=(1, 1, 1, 2, 3, 4, 4, 4, 4, 4)$

```{code-cell} ipython3
s3 = (1, 1, 1, 2, 3, 4, 4, 4, 4, 4)
stats.get_mean(iterable=s3)
```

```{code-cell} ipython3
stats.get_population_variance(iterable=s3)
```


>    Compare your results to the results of using the `statistics.mean`,
>     and `statistics.pvariance`. Note: the `statistics` library
>    is part of the standard python library.

```{code-cell} ipython3
import statistics
statistics.mean(s1)
```

```{code-cell} ipython3
statistics.pvariance(s1)
```

```{code-cell} ipython3
statistics.mean(s2)
```

```{code-cell} ipython3
statistics.pvariance(s2)
```

```{code-cell} ipython3
statistics.mean(s3)
```

```{code-cell} ipython3
statistics.pvariance(s3)
```
