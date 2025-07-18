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

# How to

(create_a_list)=

## Create a list

To create a list which is an ordered collection of objects that **can**
be changed use the `[``]` brackets.

````{admonition} Usage
:class: tip

```
collection = [value_1, value_2, value_3, …, value_n]
```
````

For example:

```{code-cell} ipython3
basket = ["Bread", "Biscuits", "Coffee"]
basket
```

You can insert an element to the end of a list by appending to it:

```{code-cell} ipython3
basket.append("Tea")
basket
```

You can also combine lists together:

```{code-cell} ipython3
other_basket = ["Toothpaste"]
basket = basket + other_basket
basket
```

As for tuples you can also access elements using their indices:

```{code-cell} ipython3
basket[3]
```

(define_a_function)=

## Define a function

We define a function using the `def` keyword (short for define):

````{admonition} Usage
:class: tip

```
def name(variable1, variable2, ...):
    """
    A docstring between triple quotation to describe what is happening
    """
    INDENTED BLOCK OF CODE
    return output
```
````

For example define $f:\mathbb{R}\to\mathbb{R}$ given by $f(x) = x ^
3$ using the following:

```{code-cell} ipython3
def x_cubed(x):
    """
    A function to return x ^ 3
    """
    return x ** 3
```

It is important to include the `docstring` as this allows you to document
your code clarity. You can access that docstring using `help`:

```{code-cell} ipython3
help(x_cubed)
```

## Call a function

Once a function is defined call it using the `()`:

````{admonition} Usage
:class: tip

```
name(variable1, variable2, ...)
```
````

For example:

```{code-cell} ipython3
x_cubed(2)
```

```{code-cell} ipython3
x_cubed(5)
```

```{code-cell} ipython3
import sympy as sym

x = sym.Symbol("x")
x_cubed(x)
```

## Run code based on a condition

To run code depending on whether or not a particular condition is met
use an `if` statement.

````{admonition} Usage
:class: tip

```
if condition:
    INDENTED BLOCK OF CODE TO RUN IF CONDITION IS TRUE
else:
    OTHER INDENTED BLOCK OF CODE TO RUN IF CONDITION IS NOT TRUE
```
````

These `if` statements are most useful when combined with functions. For
example you can define the following function:

$$
    f(x) = \begin{cases}
            x ^ 3&\text{ if }x < 0\\
            x ^ 2&\text{ otherwise}
            \end{cases}
$$

```{code-cell} ipython3
def f(x):
    """
    A function that returns x ^ 3 if x is negative.
    Otherwise it returns x ^ 2.
    """
    if x < 0:
        return x ** 3
    return x ** 2
```

```{code-cell} ipython3
f(0)
```

```{code-cell} ipython3
f(-1)
```

```{code-cell} ipython3
f(3)
```

Here is another example of a function that returns the price of a given
item, if the item is not specific in the function then the price is 0:

```{code-cell} ipython3
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

```{code-cell} ipython3
get_price_of_item("Toothpaste")
```

```{code-cell} ipython3
get_price_of_item("Biscuits")
```

```{code-cell} ipython3
get_price_of_item("Rollerblades")
```

(create_a_list_using_a_list_comprehension)=

## Create a list using a list comprehension

You can create a new list from an old list using a **list
comprehension**.

````{admonition} Usage
:class: tip

```
collection = [f(item) for item in iterable]
```
````

This corresponds to building a set from another set in the usual
mathematical notation:

$$
S_2 = \{f(x)\text{ for x in }S_1\}
$$

If $f(x)=x - 5$ and $S_1=\{2, 5, 10\}$ then you would have:

$$
S_2 = \{-3, 0, 5\}
$$

In Python this is done as follows:

```pyadmonition Usage
:class: tip

new_list = [object for object in old_list]
```

```{code-cell} ipython3
s_1 = [2, 5, 10]
s_2 = [x - 5 for x in s_1]
s_2
```

You can combine this with functions to write succinct efficient code.

For example you can compute the price of a basket of goods using the
following:

```{code-cell} ipython3
basket = ["Tea", "Tea", "Toothpaste", "Bread"]
prices = [get_price_of_item(item) for item in basket]
prices
```

## Summing items in a list

You can compute the sum of items in a list using the `sum` tool:

```{code-cell} ipython3
sum([1, 2, 3])
```

You can also directly use `sum` without specifically creating the list.
This corresponds to the following mathematical notation:

$$
    \sum_{s\in S}f(s)
$$

and is done using the following:

````{admonition} Usage
:class: tip

```
sum(f(object) for object in old_list)
```
````

This gives the same result as:

```python
sum([f(object) for object in old_list])
```

but it is more efficient.

Here is an example of getting the total price of a basket of goods:

```{code-cell} ipython3
basket = ["Tea", "Tea", "Toothpaste", "Bread"]
total_price = sum(get_price_of_item(item) for item in basket)
total_price
```

## Sample from an iterable

To randomly sample from any collection of items use the random library
and the `choice` tool.

````{admonition} Usage
:class: tip

```
random.choice(collection)
```
````

```{code-cell} ipython3
:tags: [nbval-ignore-output]

import random

basket = ["Tea", "Tea", "Toothpaste", "Bread"]
random.choice(basket)
```

## Sample a random number

To sample a random number between 0 and 1 use the random library and the
`random` tool.

````{admonition} Usage
:class: tip

```
random.random()
```
````

For example:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

import random

random.random()
```

(reproduce_random_events)=

## Reproduce random events

The random numbers generated by the Python random module are
what are called pseudo random which means that it is possible to get a
computer to reproduce them by **seeding** the random process.

````{admonition} Usage
:class: tip

```
random.seed(int)
```
````

```{code-cell} ipython3
import random

random.seed(0)
random.random()
```

```{code-cell} ipython3
random.random()
```

```{code-cell} ipython3
random.seed(0)
random.random()
```
