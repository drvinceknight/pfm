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

> `1`. For each of the following, Write a function, and repeatedly use it to simulate the probability of an
> event occurring with the following chances:

> `1`. $\frac{2}{7}$

```{code-cell} ipython3
:tags: [nbval-ignore-output]

import random


def sample_experiment():
    """
    Returns true if a random number is less than 2 / 7
    """
    return random.random() < 2 / 7


number_of_experiments = 1000
sum(
    sample_experiment() for repetition in range(number_of_experiments)
) / number_of_experiments
```

> `2`. $\frac{1}{10}$

```{code-cell} ipython3
:tags: [nbval-ignore-output]

def sample_experiment():
    """
    Returns true if a random number is less than 1 / 10
    """
    return random.random() < 1 / 10


number_of_experiments = 1000
sum(
    sample_experiment() for repetition in range(number_of_experiments)
) / number_of_experiments
```

> `3`. $\frac{1}{100}$

```{code-cell} ipython3
:tags: [nbval-ignore-output]

def sample_experiment():
    """
    Returns true if a random number is less than 1 / 100
    """
    return random.random() < 1 / 100


number_of_experiments = 1000
sum(
    sample_experiment() for repetition in range(number_of_experiments)
) / number_of_experiments
```

> `4`. $1$

```{code-cell} ipython3
:tags: [nbval-ignore-output]

def sample_experiment():
    """
    Returns true if a random number is less than 1
    """
    return random.random() < 1


number_of_experiments = 1000
sum(
    sample_experiment() for repetition in range(number_of_experiments)
) / number_of_experiments
```

````{attention}
We can in fact write a single function for all the probabilities here:

```python
def sample_experiment(probability):
    """
    Returns true of a random number is less than probability
    """
    return random.random() < probability
```
````

## Question 2

> `2`. Write a function, and repeatedly use it to simulate the probability of
> selecting a red token from each of the following configurations:

> `1`. A bag with 4 red tokens and 4 green tokens.

```{code-cell} ipython3
def sample_experiment(number_of_red, number_of_green, number_of_yellow):
    """
    This samples a token from a bag with number_of_red red tokens,
    number_of_green green tokens and number_of_yellow yellow tokens
    """
    bag = (
        ["Red"] * number_of_red
        + ["Green"] * number_of_green
        + ["Yellow"] * number_of_yellow
    )

    return random.choice(bag)
```

We now use this function:

```{code-cell} ipython3
number_of_experiments = 1000
random.seed(0)
sum(
    sample_experiment(number_of_red=4, number_of_green=4, number_of_yellow=0) == "Red"
    for repetition in range(number_of_experiments)
) / number_of_experiments
```

> `2`. A bag with 4 red tokens, 4 green tokens and 10 yellow tokens.

```{code-cell} ipython3
random.seed(0)
sum(
    sample_experiment(number_of_red=4, number_of_green=4, number_of_yellow=10) == "Red"
    for repetition in range(number_of_experiments)
) / number_of_experiments
```

> `3`. A bag with 0 red tokens, 4 green tokens and 10 yellow tokens.

```{code-cell} ipython3
random.seed(0)
sum(
    sample_experiment(number_of_red=0, number_of_green=4, number_of_yellow=10) == "Red"
    for repetition in range(number_of_experiments)
) / number_of_experiments
```

## Question 3

> `3`. An experiment consists of selecting a token from a bag and spinning a coin.
> The bag contains 3 red tokens and 4 blue tokens. A token is selected at random
> from the bag, its colour is noted and then the token is returned to the bag.
> When a red token is selected, a biased coin with probability $\frac{4}{5}$ of landing heads is spun.
> When a blue token is selected, a biased coin with probability $\frac{2}{5}$ of landing heads is spun.

> `1`. Approximate the probability of picking a red token?

We will use the code from the tutorial, making the necessary modifications:

```{code-cell} ipython3
def pick_a_token(container):
    """
    A function to randomly sample from a `container`.
    """
    return random.choice(container)


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
        probability_of_selecting_heads = 4 / 5
    else:
        probability_of_selecting_heads = 2 / 5

    if random.random() < probability_of_selecting_heads:
        coin = "Heads"
    else:
        coin = "Tails"
    return selected_token, coin
```

```{code-cell} ipython3
:tags: [nbval-ignore-output]

bag = ["Red"] * 3 + ["Blue"] * 4
number_of_repetitions = 10000
random.seed(0)
samples = [sample_experiment(bag=bag) for repetition in range(number_of_repetitions)]
sum(token == "Red" for token, coin in samples) / number_of_repetitions
```

> `2`. Approximate the probability of obtaining Heads?

```{code-cell} ipython3
sum(coin == "Heads" for token, coin in samples) / number_of_repetitions
```

> `3`. If a heads is obtained, approximate the probability of having selected a red token.

```{code-cell} ipython3
samples_with_heads = [(token, coin) for token, coin in samples if coin == "Heads"]
sum(token == "Red" for token, coin in samples_with_heads) / len(samples_with_heads)
```

## Question 4

> `4`. On a randomly chose day, the probability of an individual travelling to
> school by car, bicycle or on foot is $1/2$, $1/6$ and $1/3$ respectively.
> The probability of being late when using these methods of travel is $1/5$,
> $2/5$ and $1/10$ respectively.

> `1`. Approximate the probability that an individual travels by foot and is late.

We will write a function to sample the experiment.

```{code-cell} ipython3
def sample_experiment():
    """
    Sample a travel method followed by whether or not the individual is late.
    """
    random_number = random.random()
    if random_number < 1 / 2:
        travel_method = "car"
        is_late = random.random() < 1 / 5
        return travel_method, is_late
    if random_number < 1 / 6:
        travel_method = "bicycle"
        is_late = random.random() < 2 / 5
        return travel_method, is_late
    travel_method = "foot"
    is_late = random.random() < 1 / 10
    return travel_method, is_late
```

We will use this to now obtain a number of samples:

```{code-cell} ipython3
:tags: [output_scroll]

number_of_repetitions = 10000
random.seed(0)
samples = [sample_experiment() for repetition in range(number_of_repetitions)]
samples
```

Using this we can approximate the probability:

```{code-cell} ipython3
sum(
    is_late and travel_method == "foot" for travel_method, is_late in samples
) / number_of_repetitions
```

> `2`. Approximate the probability that an individual is not late.

```{code-cell} ipython3
sum(not is_late for travel_method, is_late in samples) / number_of_repetitions
```

> `3`. Given that an individual is late, approximate the probability that they did not travel on foot.

```{code-cell} ipython3
samples_with_late = [
    (travel_method, is_late) for travel_method, is_late in samples if is_late is True
]
number_of_samples = len(samples_with_late)
sum(
    travel_method != "foot" for travel_method, is_late in samples_with_late
) / number_of_samples
```
