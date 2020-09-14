---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region -->
## Probability

### Introduction

Probability is the study of random events. Computers are particularly helpful here as they can be used to carry out a number of experiments to confirm and/or explore theoretic results.

> a group of numbers or other symbols arranged in a rectangle that can be used together as a single unit to solve particular mathematical problems

In practice studying probability will often involve:

- calculating expected chances of an event occurring;
- calculating the conditional chances of an event occurring given another event occurring.

Here we will see how to instruct a computer to sample such events.

## Tutorial

We will solve the following problem using a computer to estimate the expected probabilities:


---

An experiment consists of selecting a token from a bag and spinning a coin. The bag contains 5 red tokens and 7 blue tokens. A token is selected at random from the bag, its colour is noted and then the token is returned to the bag.

When a red token is selected, a biased coin with probability \\(\frac{2}{3}\\) of landing heads is spun.

When a blue token is selected a fair coin is spun.

1. What is the probability of picking a red token?
2. What is the probability of obtaining Heads?
3. If a heads is obtained, what is the probability of having selected a red token.

---

We will use the `random` library from the Python standard library to do this.

First we start off by building a Python **tuple** to represent the bag with the tokens. We assign this to a variable `bag`:
<!-- #endregion -->

```python
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

**Note** We are there using the circular brackets `()` and the quotation marks
`"`. Those are important and cannot be omitted. The choice of brackets `()` as
opposed to `{}` or `[]` is in fact important as it instructs Python to do
different things (we will learn about this later). You can use `"` or `'`
interchangeably.


Instead of writing every entry out we can create a Python **list** which allows for us to carry out some basic algebra on the items. Here we essentially:

- Create a list with 5 `"Red"`s.
- Create a list with 7 `"Blue"`s.
- Combine both lists:

```python
bag = ["Red"] * 5 + ["Blue"] * 7
bag
```

Now to sample from that we use the `random` library which has a `choice` command:

```python tags=["nbval-ignore-output"]
import random


random.choice(bag)
```

If we run this many times we will not always get the same outcome:

```python tags=["nbval-ignore-output"]
random.choice(bag)
```

**Note** that the `bag` variable is unchanged:

```python
bag
```

In order to answer the first question (what is the probability of picking a red token) we want to repeat this many times.

We do this by defining a Python function (which is akin to a mathematical function) that allows us to repeat code:

```python
def pick_a_token(container):
    """
    A function to randomly sample from a `container`.
    """
    return random.choice(container)
```

We can then call this function, passing our `bag` to it as the `container` from which to pick:

```python tags=["nbval-ignore-output"]
pick_a_token(container=bag)
```

```python tags=["nbval-ignore-output"]
pick_a_token(container=bag)
```

In order to simulate the probability of picking a red token we need to repeat this not once or twice but tens of thousands of times. We will do this using something called a "list comprehension" which is akin to the mathematical notation we use all the time to create sets:

\\[
    S_1 = \{f(x)\text{ for }x\text{ in }S_2\}
\\]

```python tags=["nbval-ignore-output"]
number_of_repetitions = 10000
samples = [pick_a_token(container=bag) for repetition in range(number_of_repetitions)]
samples
```

We can confirm that we have the correct number of samples:

```python
len(samples)
```

`len` is the Python tool to get the length of a given Python iterable.


Using this we can now use `==` (double `=`) to check how many of those samples are `Red`:

```python tags=["nbval-ignore-output"]
sum(token == "Red" for token in samples) / number_of_repetitions
```

We have sampled  probability of around .41. The theoretic value is \\(\frac{5}{5 + 7}\\):

```python tags=["nbval-ignore-output"]
5 / (5 + 7)
```

To answer the second question (What is the probability of obtaining Heads?) we need to make use of another Python tool: an `if` statement. This will allow us to write a function that does precisely what is described in the problem:

- Choose a token;
- Set the probability of flipping a given coin;
- Select that coin.

**Note** that for the second random selection (flipping a coin) we will not choose from a list but instead select a random number between 0 and 1.

```python
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

```python tags=["nbval-ignore-output"]
sample_experiment(bag=bag)
```

```python tags=["nbval-ignore-output"]
sample_experiment(bag=bag)
```

We can now find out the probability of selecting heads by carrying out a large number of repetitions and checking which ones have a coin that is heads:

```python tags=["nbval-ignore-output"]
samples = [sample_experiment(bag=bag) for repetition in range(number_of_repetitions)]
sum(coin == "Heads" for token, coin in samples) / number_of_repetitions
```

We can compute this theoretically as well, the expected probability is:

```python
import sympy as sym

sym.S(5) / (12) * sym.S(2) / 3 + sym.S(7) / (12) * sym.S(1) / 2
```

```python tags=["nbval-ignore-output"]
41 / 72
```

We can also use our samples to calculate the conditional probability that a token was read if the coin is heads. This is done again using the list comprehension notation but including an `if` statement which allows us to emulate the mathematical notation:

\\[
    S_3 = \{x \in S_1  | \text{ if some property of \(x\) holds}\}
\\]

```python tags=["nbval-ignore-output"]
samples_with_heads = [(token, coin) for token, coin in samples if coin == "Heads"]
sum(token == "Red" for token, coin in samples_with_heads) / len(samples_with_heads)
```

Using Bayes' theorem this is given theoretically by:

\\[
    P(\text{Red}|\text{Heads}) = \frac{P(\text{Heads} | \text{Red})P(\text{Red})}{P(\text{Heads})}
\\]

```python
(sym.S(2) / 3 * sym.S(5) / 12) / (sym.S(41) / 72)
```

```python tags=["nbval-ignore-output"]
20 / 41
```

<!-- #region -->
### How to


#### Create a tuple

To create a tuple which is an ordered collection of objects that cannot be changed we use the `()` brackets:
<!-- #endregion -->

```python
basket = ("Bread", "Biscuits", "Coffee")
basket
```

<!-- #region -->
If we need to we can access elements of this collection using `[]` brackets. The first element is has index `0`:

```python
tuple[index]
```

For example:
<!-- #endregion -->

```python
basket[1]
```

#### Create a list

To create a list which is an ordered collection of objects that **can** be changed we use the `[]` brackets:

```python
basket = ["Bread", "Biscuits", "Coffee"]
basket
```

We can add to our list by appending to it:

```python
basket.append("Tea")
basket
```

We can also combine lists together:

```python
other_basket = ["Toothpaste"]
basket = basket + other_basket
basket
```

As for tuples we can also access elements using their indices:

```python
basket[3]
```

#### Define a function

We define a function using the `def` keyword (short for define):

```
def name(variable1, variable2, ...):
    """
    A docstring between triple quotation to describe what is happening
    """
    INDENTED BLOCK OF CODE
    return output
```

INCLUDE IMAGE HERE

We can for example define \\(f:\mathbb{R}\to\mathbb{R}\\) given by \\(f(x) = x ^ 3\\) using the following:

```python
def x_cubed(x):
    """
    A function to return x ^ 3
    """
    return x ** 3
```

It is important to include the *docstring* as this allows us to make sure our code is clear. We can access that docstring using `help`:

```python
help(x_cubed)
```

#### Call a function

Once a function is defined we call it using the `()`:

```
name(variable1, variable2, ...)
```


For example:

```python
x_cubed(2)
```

```python
x_cubed(5)
```

```python
x = sym.Symbol("x")
x_cubed(x)
```

#### Creating boolean variables

A boolean variable has one of two values: `True` or `False`.

To create a boolean variable we can use:

- Equality: `value == other_value`
- Inequality `value != other_value`
- Strictly less than `value < other_value`
- Less than or equal`value <= other_value`

This a subset of the operators available.

For example:

```python
value = 5
other_value = 10

value == other_value
```

```python
value != other_value
```

```python
value <= other_value
```

```python
value < value
```

```python
value <= value
```

<!-- #region -->
#### Conditional running of code

To run code depending on whether or not a particular condition is met we use something called an `if` statement.


```
if condition:
    INDENTED BLOCK OF CODE TO RUN IF CONDITION IS TRUE
else:
    OTHER INDENTED BLOCK OF CODE TO RUM IF CONDITION IS NOT TRUE
```
<!-- #endregion -->

These `if` statements are most useful when combined with functions. For example we can define the following function:

\\[
    f(x) = \begin{cases}
            x ^ 3&\text{ if }x < 0\\
            x ^ 2&\text{ otherwise}
            \end{cases}
\\]

```python
def f(x):
    """
    A function that returns x ^ 3 if x is negative.
    Otherwise it returns x ^ 2.
    """
    if x < 0:
        return x ** 3
    return x ** 2
```

```python
f(0)
```

```python
f(-1)
```

```python
f(3)
```

Here is another example of a function that returns the price of a given item, if the item is not specific in the function then the price is free:

```python
def get_price_of_item(item):
    """
    Returns the price of an item:

    - 'Bread': 2
    - 'Biscuits': 3
    - 'Coffee': 1.80
    - 'Tea': .50
    - 'Toothpaste': 3.50

    Other items will give a price of 0.
    """
    if item == "Bread":
        return 2
    if item == "Biscuits":
        return 3
    if item == "Coffee":
        return 1.80
    if item == "Tea":
        return 0.50
    if item == "Toothpaste":
        return 3.50
    return 0
```

```python
get_price_of_item("Toothpaste")
```

```python
get_price_of_item("Biscuits")
```

```python
get_price_of_item("Rollerblades")
```

<!-- #region -->
#### Create a list using a list comprehension

We can create a new list from an old list using a **list comprehension**. This corresponds to building a set from another set in the usual mathematical notation:

\\[
S_2 = \{f(x)\text{ for x in }S_1\}
\\]

If \\(f(x)=x - 5\\) and \\(S_1=\{2, 5, 10\}\\) then we would have:

\\[
S_2 = \{-3, 0, 5\}
\\]

In Python this is done as follows:


```python
new_list = [object for object in old_list]
```
<!-- #endregion -->

```python
s_1 = [2, 5, 10]
s_2 = [x - 5 for x in s_1]
s_2
```

We can combine this with functions to write succinct efficient code.

For example we can compute the price of a basket of goods using the following:

```python
basket = ["Tea", "Tea", "Toothpaste", "Bread"]
prices = [get_price_of_item(item) for item in basket]
prices
```

#### Creating an iterable with a given number of items

A common use of list comprehensions is to combine it with the `range` tool which gives a given number of integers.

For example:

```python
[number for number in range(10)]
```

Note that `range(N)` gives the integers from 0 until \\(N - 1\\) (inclusive).


#### Adding items in a list

We can compute the sum of items in a list using the `sum` tool:

```python
sum([1, 2, 3])
```

<!-- #region -->
We can also directly use the `sum` without specifically creating the list. This corresponds to the following mathematical notation:

\\[
    \sum_{s\in S}f(s)
\\]

and is done using the following:


```python
sum(f(object) for object in old_list)
```

This gives the same result as:


```python
sum([f(object) for object in old_list])
```

but it is not as efficient.

Here is an example of getting the total price of a basket of goods:
<!-- #endregion -->

```python
basket = ["Tea", "Tea", "Toothpaste", "Bread"]
total_price = sum(get_price_of_item(item) for item in basket)
total_price
```

#### Sample from an iterable

To randomly sample from any collection of items (this is called an **iterable**) we use the random library and the `choice` tool:

```python tags=["nbval-ignore-output"]
import random


basket = ["Tea", "Tea", "Toothpaste", "Bread"]
random.choice(basket)
```

#### Sample a random number

To sample a random number between 0 and 1 we use the random library and the `random` tool:

```python tags=["nbval-ignore-output"]
import random


random.random()
```

#### Reproduce random events

The random numbers processes generated by the Python random module are what are called pseudo random which means that we can get a computer to reproduce them by **seeding** the random process:

```python
import random

random.seed(0)
random.random()
```

```python
random.random()
```

```python
random.seed(0)
random.random()
```

### Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. Simulate the probability of an event occurring with the following chances:
    1. \\(\frac{2}{7}\\)
    2. \\(\frac{1}{10}\\)
    3.  \\(\frac{1}{100}\\)
    4.  \\(1\\)
2. Simulate the probability of selecting a red token from each of the following configurations:
    1. A bag with 4 red tokens and 4 green tokens.
    2. A bag with 4 red tokens, 4 green tokens and 10 yellow tokens.
    3. A bag with 0 red tokens, 4 green tokens and 10 yellow tokens.
3. An experiment consists of selecting a token from a bag and spinning a coin. The bag contains 3 red tokens and 4 blue tokens. A token is selected at random from the bag, its colour is noted and then the token is returned to the bag.

    When a red token is selected, a biased coin with probability \\(\frac{4}{5}\\) of landing heads is spun.

    When a blue token is selected, a biased coin with probability \\(\frac{2}{5}\\) of landing heads is spun.

    1. What is the probability of picking a red token?
    2. What is the probability of obtaining Heads?
    3. If a heads is obtained, what is the probability of having selected a red token.
4. On a randomly chose day, the probability of an individual travelling to school by car, bicycle or on foot is \\(1/2\\), \\(1/6\\) and \\(1/3\\) respectively. The probability of being late when using these methods of travel is \\(1/5\\), \\(2/5\\) and \\(1/10\\) respectively.

    1. Find the probability that an individual travels by foot and is late.
    2. Find the probability that an individual is not late.
    3. Given that an individual is late, find the probability that they did not travel on foot.

### References

#### What is the difference between a Python list and a Python tuple?

Two of the most used Python iterables are lists and tuples. In practice they have a number of similarities, they are both ordered collections of objects that can be used in list comprehensions as well as in other ways.

- Tuples are **immutable**
- Lists are **mutable**

This means that once created tuples cannot be changed and lists can.

As a general rule of thumb: if you do not need to modify your iterable then use a tuple as they are more computationally efficient.

This blog post is a good explanation of the difference: https://www.afternerd.com/blog/difference-between-list-tuple/

#### Why does the sum of booleans counts the `True`s?

In the tutorial and elsewhere we created a list of booleans and then take the sum. Here are some of the steps:


```python
samples = ("Red", "Red", "Blue")
```

```python
booleans = [sample == "Red" for sample in samples]
booleans
```

When we take the `sum` of that list we get a numeric value:

```python
sum(booleans)
```

This has in fact counted the `True` values as 1 and the `False` values as 0.

```python
int(True)
```

```python
int(False)
```

#### What is the difference between `print` and `return`?

In functions you see we use the `return` statement. This does two things:

1. Assigns a value to the function run;
2. Ends the function.

The `print` statement **only** displays the output.

As an example let us create the following set:

\\[
    S = \{f(x)\text{ for }x \in \{0, \pi / 4, \pi / 2, 3\pi / 4\}\}
\\]

where \\(f(x)= \cos^2(x)\\).


The correct way to do this is:

```python
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

```python
def f(x):
    """
    Return the square of the cosine of x
    """
    print(sym.cos(x) ** 2)


S = [f(x) for x in (0, sym.pi / 4, sym.pi / 2, 3 * sym.pi / 4)]
```

We see now that as the function has been run it displays the output.

**However** if we look at what `S` is we see that the function has not returned anything:

```python
S
```

Here are some other materials on this subject:

- https://www.tutorialspoint.com/Why-would-you-use-the-return-statement-in-Python
- https://pythonprinciples.com/blog/print-vs-return/


#### How does Python sample randomness?

When using the Python random module we are in fact generating a pseudo random process. True randomness is actually not common.

Pseudo randomness is an important area of mathematics as strong algorithms that
create unpredictable sequences of numbers are vital to cryptographic security.

The specific algorithm using in Python for randomness is called the Mersenne twister algorithm is state of the art.

You can read more about this here: https://docs.python.org/3/library/random.html#module-random


#### What is the difference between a docstring and a comment

In Python it is possible to write statements that are ignored using the `#` symbol. This creates something called a "comment". For example:

```python
# create a list to represent the tokens in a bag
bag = ["Red", "Red", "Blue"]
```

A docstring however is something that is "attached" to a function and can be accessed by Python.

If we rewrite the function to sample the experiment of the tutorial without a docstring but using comments we will have:

```python
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

```python
help(sample_experiment)
```

Furthermore, if you look at the code with comments you will see that because of the choice of variable names the comments are in fact redundant.

In software engineering it is generally accepted that comments indicate that your code is not clear and so it is preferable to write clear documentation explaining why something is done through docstrings.

```python
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

- https://blog.codinghorror.com/coding-without-comments/
- https://visualstudiomagazine.com/articles/2013/07/26/why-commenting-code-is-still-bad.aspx
