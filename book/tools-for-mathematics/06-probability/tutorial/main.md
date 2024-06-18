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

We will solve the following problem using a computer to estimate the expected
probabilities:

```{admonition} Problem

An experiment consists of selecting a token from a bag and spinning a coin. The
bag contains 5 red tokens and 7 blue tokens. A token is selected at random from
the bag, its colour is noted and then the token is returned to the bag.

When a red token is selected, a biased coin with probability $\frac{2}{3}$
of landing heads is spun.

When a blue token is selected a fair coin is spun.

1. What is the probability of picking a red token?
2. What is the probability of obtaining Heads?
3. If a heads is obtained, what is the probability of having selected a red
   token.
```

You will use the `random` library from the Python standard library to do this.
First start by building a Python **tuple** to represent the bag with the
tokens. Assign this to a variable `bag`:

```{code-cell} ipython3
bag = (
    "Red",
    "Red",
    "Red",
    "Red",
    "Red",
    "Blue",
    "Blue",
    "Blue",
    "Blue",
    "Blue",
    "Blue",
    "Blue",
)
bag
```

```{attention}
You are there using the circular brackets `()` and the quotation marks
`"`. Those are important and cannot be omitted. The choice of brackets `()` as
opposed to `{}` or `[]` is in fact important as it instructs Python to do
different things. You can use `"` or `'`
interchangeably.
```

Instead of writing every copy of color you can create a Python **list** which allows
you to carry out some basic algebra on the items:

- Create a list with 5 `"Red"`s.
- Create a list with 7 `"Blue"`s.
- Combine both lists:

```{code-cell} ipython3
bag = ["Red"] * 5 + ["Blue"] * 7
bag
```

Now to sample from that we use the `random` library which has a `choice`
command:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

import random

random.choice(bag)
```

If we run this many times we will not always get the same outcome:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

random.choice(bag)
```

```{attention}
The `bag` variable is unchanged:
```

```{code-cell} ipython3
bag
```

In order to answer the first question (what is the probability of picking a red
token) repeat this many times.

Do this by defining a Python function (which is akin to a mathematical
function) that makes repeating code possible:

```{code-cell} ipython3
def pick_a_token(container):
    """
    A function to randomly sample from a `container`.
    """
    return random.choice(container)
```

We can then call this function, passing our `bag` to it as the `container` from
which to pick:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

pick_a_token(container=bag)
```

```{code-cell} ipython3
:tags: [nbval-ignore-output]

pick_a_token(container=bag)
```

In order to simulate the probability of picking a red token repeat
this not once or twice but tens of thousands of times. You will do this using
something called a "list comprehension" which is akin to the mathematical
notation commonly used to create sets:

$$
    S_1 = \{f(x)\text{ for }x\text{ in }S_2\}
$$

```{code-cell} ipython3
:tags: [nbval-ignore-output, output_scroll]

number_of_repetitions = 10000
samples = [pick_a_token(container=bag) for repetition in range(number_of_repetitions)]
samples
```

You can confirm that we have the correct number of samples:

```{code-cell} ipython3
len(samples)
```

```{attention}
`len` is the Python tool to get the length of a given Python iterable.
```

Using this we can now use `==` (double `=`) to check how many of those samples are `Red`:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

sum(token == "Red" for token in samples) / number_of_repetitions
```

You have sampled a probability of around .41. The theoretic value is $\frac{5}{5 +
7}$:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

5 / (5 + 7)
```

To answer the second question (What is the probability of obtaining Heads?) you
need to make use of another Python tool: an `if` statement. This will allow you
to write a function that does precisely what is described in the problem:

- Choose a token;
- Set the probability of flipping a given coin;
- Select that coin.

```{attention}
For the second random selection (flipping a coin) you will not choose from a list
but instead select a random number between 0 and 1.
```

```{code-cell} ipython3
import random


def sample_experiment(bag):
    """
    This samples a token from a given bag and then
    selects a coin with a given probability.

    If the sampled token is red then the probability
    of selecting heads is 2/3 otherwise it is 1/2.

    This function returns both the selected token
    and the coin face.
    """
    selected_token = pick_a_token(container=bag)

    if selected_token == "Red":
        probability_of_selecting_heads = 2 / 3
    else:
        probability_of_selecting_heads = 1 / 2

    if random.random() < probability_of_selecting_heads:
        coin = "Heads"
    else:
        coin = "Tails"
    return selected_token, coin
```

Using this we can sample according to the problem description:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

sample_experiment(bag=bag)
```

```{code-cell} ipython3
:tags: [nbval-ignore-output]

sample_experiment(bag=bag)
```

You can now find out the probability of selecting heads by carrying out a large
number of repetitions and checking which ones have a coin that is heads:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

samples = [sample_experiment(bag=bag) for repetition in range(number_of_repetitions)]
sum(coin == "Heads" for token, coin in samples) / number_of_repetitions
```

You can compute this theoretically as well, the expected probability is:

```{code-cell} ipython3
import sympy as sym

sym.S(5) / (12) * sym.S(2) / 3 + sym.S(7) / (12) * sym.S(1) / 2
```

```{code-cell} ipython3
:tags: [nbval-ignore-output]

41 / 72
```

You can also use our samples to calculate the conditional probability that a
token was read if the coin is heads. This is done again using the list
comprehension notation but including an `if` statement which
emulates the mathematical notation:

$$
    S_3 = \{x \in S_1  | \text{ if some property of \(x\) holds}\}
$$

```{code-cell} ipython3
:tags: [nbval-ignore-output]

samples_with_heads = [(token, coin) for token, coin in samples if coin == "Heads"]
sum(token == "Red" for token, coin in samples_with_heads) / len(samples_with_heads)
```

Using Bayes' theorem this is given theoretically by:

$$
    P(\text{Red}|\text{Heads}) = \frac{P(\text{Heads} | \text{Red})P(\text{Red})}{P(\text{Heads})}
$$

```{code-cell} ipython3
(sym.S(2) / 3 * sym.S(5) / 12) / (sym.S(41) / 72)
```

```{code-cell} ipython3
:tags: [nbval-ignore-output]

20 / 41
```

```{important}
In this tutorial we have

- Randomly sampled from an iterable.
- Randomly sampled a number between 0 and 1.
- Written a function to represent a random experiment.
- Created a list using list comprehensions.
- Counted outcomes of random experiments.
```
