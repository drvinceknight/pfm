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

# How

(create_a_tuple)=

## Create a tuple

To create a tuple which is an ordered collection of objects that cannot be
changed we use the `()` brackets.

````{tip}
```
collection = (value_1, value_2, value_3, …, value_n)
```
````

For example:

```{code-cell} ipython3
basket = ("Bread", "Biscuits", "Coffee")
basket
```

(how_to_access_particular_elements_in_a_tuple)=

## How to access particular elements in a tuple

If we need to we can access elements of this collection using `[]` brackets. The
first element is has index `0`:

```python
tuple[index]
```

For example:

```{code-cell} ipython3
basket[1]
```

(creating_boolean_variables)=

## Creating boolean variables

A boolean variable has one of two values: `True` or `False`.

To create a boolean variable here are some of the things we can use:

- Equality: `value == other_value`
- Inequality `value != other_value`
- Strictly less than `value < other_value`
- Less than or equal`value <= other_value`
- Inclusion `value in iterable`

This a subset of the operators available.

For example:

```{code-cell} ipython3
value = 5
other_value = 10

value == other_value
```

```{code-cell} ipython3
value != other_value
```

```{code-cell} ipython3
value <= other_value
```

```{code-cell} ipython3
value < value
```

```{code-cell} ipython3
value <= value
```

```{code-cell} ipython3
value in (1, 2, 4, 19)
```

It is also possible to combine booleans to create new booleans:

- And: `first_boolean and second_boolean`
- Or: `first_boolean or second_boolean`

```{code-cell} ipython3
True and True
```

```{code-cell} ipython3
False and True
```

```{code-cell} ipython3
True or False
```

```{code-cell} ipython3
False or False
```

(creating_an_iterable_with_a_given_number_of_items)=

## Creating an iterable with a given number of items

The `range` tool gives a given number of integers.

````{tip}
```
range(number_of_integers)
```
````

For example:

```{code-cell} ipython3
tuple(range(10))
```

```{attention}
`range(N)` gives the integers from 0 until $N - 1$ (inclusive).
```

It is also possible to pass two values as inputs so that we have a different lower bound:

```{code-cell} ipython3
tuple(range(4, 10))
```

It is also possible to pass a third value as an step size:

```{code-cell} ipython3
tuple(range(4, 10, 3))
```

## Creating permutations of a given set of elements

The python `itertools` library has a `permutations` tool that will generate all
permutations of a given set.

````{tip}
```
itertools.permutations(iterable)
```
````

```{code-cell} ipython3
import itertools

basket = ("Bread", "Biscuits", "Coffee")
tuple(itertools.permutations(basket))
```

It is possible to limit the size to only be permutations of size `r`:

```{code-cell} ipython3
tuple(itertools.permutations(basket, r=2))
```

## Creating combinations of a given set of elements

The python `itertools` library has a `combinations` tool that will generate all combinations of size `r` of a given set:

````{tip}
```
itertools.combinations(iterable, r)
```
````

For example:

```{code-cell} ipython3
basket = ("Bread", "Biscuits", "Coffee")
tuple(itertools.combinations(basket, r=2))
```

A combination does not care about order so by default the combinations generated
are sorted.

(adding_items_in_a_tuple)=

## Adding items in a tuple

We can compute the sum of items in a list using the `sum` tool:

```{code-cell} ipython3
sum((1, 2, 3))
```

We can also directly use the `sum` without specifically creating the list. This
corresponds to the following mathematical notation:

$$
    \sum_{s\in S}f(s)
$$

and is done using the following:

```python
sum(f(object) for object in old_list)
```

Here is an example of calculating the following sum:

$$
    \sum_{n=0}^{10} n ^ 2
$$

```{code-cell} ipython3
sum(n ** 2 for n in range(11))
```

Finally we can compute conditionally sums by only summing over elements that
meet a given condition using the following:

```python
sum(f(object) for object in old_list if condition)
```

Here is an example of calculating the following sum:

$$
    \sum_{\begin{array}{c}n=0\\\text{ if }n\text{ odd}\end{array}}^{10} n ^ 2
$$

```{code-cell} ipython3
sum(n ** 2 for n in range(11) if n % 2 == 1)
```

## Directly computing \\(n!\\)

The `math` library has a `factorial` tool.

````{tip}
```
math.factorial(N)
```
````

```{code-cell} ipython3
import math

math.factorial(5)
```

## Directly computing ${n \choose i}$

The `scipy.special` library has a `comb` tool.

````{tip}
```
scipy.special.comb(n, i)
```
````

For example:

```{code-cell} ipython3
import scipy.special

scipy.special.comb(3, 2)
```

## Directly computing $^n P_i$

The `scipy.special` library has a `perm` tool.

````{tip}
```
scipy.special.perm(n, i)
```
````

```{code-cell} ipython3
scipy.special.perm(3, 2)
```
