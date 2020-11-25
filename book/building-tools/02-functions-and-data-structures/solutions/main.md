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

> `1`. Write a function that generates $n!$.

There are two approaches to do this, the first is to use recursion:

```{code-cell} ipython3
def generate_n_factorial(n):
    """
    Return n! using recursion.
    """
    if n == 0:
        return 1
    return n * generate_n_factorial(n - 1)
```

We can use this:

```{code-cell} ipython3
generate_n_factorial(5)
```

Here is another approach, to use iteration and making use of the actual
expression for $n!$:

$$
    n! = \prod_{i=1}^ni
$$

```{code-cell} ipython3
def generate_n_factorial_using_iteration(n):
    """
    Return n! using iteration
    """
    cumulative_product = 1
    for i in range(1, n + 1):
        cumulative_product *= i
    return cumulative_product
```

We can use this:

```{code-cell} ipython3
generate_n_factorial_using_iteration(5)
```

## Question 2

> `2`. Write a function that generates the $n$th triangular numbers defined by:
> $ T_n = \frac{n(n+1)}{2} $

```{code-cell} ipython3
def generate_triangular_numbers(n):
    """
    Return the nth triangular number
    """
    return n * (n + 1) / 2
```


## Question 3

> `3`. Verify the following that the following identify holds for positive integer
> values $n\leq 500$:
> $ \sum_{i=0}^n T_i = \frac{n(n+1)(n+2)}{6} $

We will write a function to check the equality:

```{code-cell} ipython3
def check_inequality(n):
    """
    Returns a boolean variable whether or not the equality is true for a given n
    """
    lhs = sum(generate_triangular_numbers(i) for i in range(n + 1))
    rhs = n * (n + 1) * (n + 2) / 6
    return lhs == rhs
```

Using this we can check all the values of $n$ as required:

```{code-cell} ipython3
all([check_inequality(n) for n in range(1, 501)])
```

Note that we can also use `all` directly without creating the list first (this
is similar to `sum`):

```{code-cell} ipython3
all(check_inequality(n) for n in range(1, 501))
```


## Question 4

> `4`. Consider the [Monty Hall
> problem](https://en.wikipedia.org/wiki/Monty_Hall_problem):
`1`. Write a
> function that simulates the play of the game when you 'stick' with the initial
> choice.


This corresponds to sampling from a list of three choices:

```{code-cell} ipython3
import random


def play_monty_hall_with_stick():
    """
    Instead of picking a random element we will shuffle it and return the first
    element.

    We make use of `random.shuffle` to shuffle and `pop()` to remove the first
    element of a list (and return it).
    """
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    return doors.pop()
```

We can check that this gives expected behaviour:

```{code-cell} ipython3
random.seed(0)

play_monty_hall_with_stick()
```

```{code-cell} ipython3
play_monty_hall_with_stick()
```

```{code-cell} ipython3
play_monty_hall_with_stick()
```

> `2`. Write a function that simulates the play of the game when you 'change'
>  your choice.


This corresponds to sampling from a list of three choices, removing that choice
and then sampling again:

```{code-cell} ipython3
def play_monty_hall_with_switch():
    """
    Instead of picking a random element we will shuffle it and return the first
    element.

    We make use of `random.shuffle` to shuffle and `pop()` to remove the first
    element of a list. We then use `remove()` to remove an element from a list.
    We then pop the first
    element of the remaining list (and return it).
    """
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    doors.pop()
    doors.remove("goat")
    return doors.pop()
```

```{code-cell} ipython3
random.seed(0)

play_monty_hall_with_switch()
```

```{code-cell} ipython3
play_monty_hall_with_switch()
```

```{code-cell} ipython3
play_monty_hall_with_switch()
```

> `3`. Repeat the play of the game using both those functions and compare the
> probability of winning.

We can calculate the probability of winning the car when we stick:

```{code-cell} ipython3
repetitions = 100000
count_of_winning_with_stick = sum(
    play_monty_hall_with_stick() == "car" for repetition in range(repetitions)
)
probability_of_winning_with_stick = count_of_winning_with_stick / repetitions
probability_of_winning_with_stick
```

We can calculate the probability of winning the car when we switch:

```{code-cell} ipython3
count_of_winning_with_switch = sum(
    play_monty_hall_with_switch() == "car" for repetition in range(repetitions)
)
probability_of_winning_with_switch = count_of_winning_with_switch / repetitions
probability_of_winning_with_switch
```
