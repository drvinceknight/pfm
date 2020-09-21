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

# Why

## What is the difference between a Python list and a Python tuple?

Two of the most used Python iterables are lists and tuples. In practice they
have a number of similarities, they are both ordered collections of objects that
can be used in list comprehensions as well as in other ways.

- Tuples are **immutable**
- Lists are **mutable**

This means that once created tuples cannot be changed and lists can.

As a general rule of thumb: if you do not need to modify your iterable then use
a tuple as they are more computationally efficient.

This blog post is a good explanation of the difference:
<https://www.afternerd.com/blog/difference-between-list-tuple/>

## Why does the sum of booleans counts the `True`s?

In the tutorial and elsewhere we created a list of booleans and then take the
sum. Here are some of the steps:

```{code-cell} ipython3
samples = ("Red", "Red", "Blue")
```

```{code-cell} ipython3
booleans = [sample == "Red" for sample in samples]
booleans
```

When we take the `sum` of that list we get a numeric value:

```{code-cell} ipython3
sum(booleans)
```

This has in fact counted the `True` values as 1 and the `False` values as 0.

```{code-cell} ipython3
int(True)
```

```{code-cell} ipython3
int(False)
```

## What is the difference between `print` and `return`?

In functions you see we use the `return` statement. This does two things:

1. Assigns a value to the function run;
2. Ends the function.

The `print` statement **only** displays the output.

As an example let us create the following set:

$$
    S = \{f(x)\text{ for }x \in \{0, \pi / 4, \pi / 2, 3\pi / 4\}\}
$$

where $f(x)= \cos^2(x)$.


The correct way to do this is:

```{code-cell} ipython3
import sympy as sym


def f(x):
    """
    Return the square of the cosine of x
    """
    return sym.cos(x) ** 2


S = [f(x) for x in (0, sym.pi / 4, sym.pi / 2, 3 * sym.pi / 4)]
S
```

If we replaced the `return` statement in the function definition with a `print` we obtain:

```{code-cell} ipython3
def f(x):
    """
    Return the square of the cosine of x
    """
    print(sym.cos(x) ** 2)


S = [f(x) for x in (0, sym.pi / 4, sym.pi / 2, 3 * sym.pi / 4)]
```

We see now that as the function has been run it displays the output.

**However** if we look at what `S` is we see that the function has not returned
anything:

```{code-cell} ipython3
S
```

Here are some other materials on this subject:

- <https://www.tutorialspoint.com/Why-would-you-use-the-return-statement-in-Python>
- <https://pythonprinciples.com/blog/print-vs-return/>


## How does Python sample randomness?

When using the Python random module we are in fact generating a pseudo random
process. True randomness is actually not common.

Pseudo randomness is an important area of mathematics as strong algorithms that
create unpredictable sequences of numbers are vital to cryptographic security.

The specific algorithm using in Python for randomness is called the Mersenne
twister algorithm is state of the art.

You can read more about this here:
<https://docs.python.org/3/library/random.html#module-random>.


## What is the difference between a docstring and a comment

In Python it is possible to write statements that are ignored using the `#`
symbol. This creates something called a "comment". For example:

```{code-cell} ipython3
# create a list to represent the tokens in a bag
bag = ["Red", "Red", "Blue"]
```

A docstring however is something that is "attached" to a function and can be
accessed by Python.

If we rewrite the function to sample the experiment of the tutorial without a
docstring but using comments we will have:

```{code-cell} ipython3
def sample_experiment(bag):
    # Select a token
    selected_token = pick_a_token(container=bag)

    # If the token is red then the probability of selecting heads is 2/3
    if selected_token == "Red":
        probability_of_selecting_heads = 2 / 3
    # Otherwise it is 1 / 2
    else:
        probability_of_selecting_heads = 1 / 2

    # Select a coin according to the probability.
    if random.random() < probability_of_selecting_heads:
        coin = "Heads"
    else:
        coin = "Tails"

    # Return both the selected token and the coin.
    return selected_token, coin
```

Now if we try to access the help for the function we will not get it:

```{code-cell} ipython3
help(sample_experiment)
```

Furthermore, if you look at the code with comments you will see that because of
the choice of variable names the comments are in fact redundant.

In software engineering it is generally accepted that comments indicate that
your code is not clear and so it is preferable to write clear documentation
explaining why something is done through docstrings.

```{code-cell} ipython3
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

Here are some resources on this:

- <https://blog.codinghorror.com/coding-without-comments/>
- <https://visualstudiomagazine.com/articles/2013/07/26/why-commenting-code-is-still-bad.aspx>
