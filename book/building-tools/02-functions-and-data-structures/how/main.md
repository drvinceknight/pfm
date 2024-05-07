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

Two important data structures have already been seen in previous chapters:

- Tuples: [Combinatorics: How to create a tuple](create_a_tuple).
- Lists: [Probability: How to create a list](create_a_list).

## How to define a function

See: [Probability: How to define a function](define_a_function).

(how_to_write_a_docstring)=

## How to write a docstring

A docstring is an attribute of a function that describes what it is. This can
describe what it does, how it does it and/or why it does it.
Here is how to write a docstring for a function that takes variables and returns
a value.

````{tip}
```
def name(parameter1, parameter2, ...):
    """
    <A description of what the function is.>

    Parameters
    ----------
    parameter1 : <type of parameter1>
        <description of parameter1>
    parameter2 : <type of parameter2>
        <description of parameter2>
    ...

    Returns
    -------
    <type of what the function returns>
        <description of what the function returns>

    """
    INDENTED BLOCK OF CODE
    return output
```
````

For example, here is how to write a function that returns $x ^ 3$ for a given
$x$:

```{code-cell} ipython3
def x_cubed(x):
    """
    Calculates and returns the cube of x. Does this by using Python
    exponentiation.

    Parameters
    ----------
    x : float
        The value of x to be raised to the power 3

    Returns
    -------
    float
        The cube.
    """
    return x ** 3
```

## Create a tuple

See [Combinatorics: How to create a tuple](create_a_tuple).

## Create a list

See [Probability: How to create a list](create_a_list).

## Create a list using a list comprehension

See [Probability: Create a list using a list comprehension](create_a_list_using_a_list_comprehension).

## Combine lists

Given two lists it is possible to combine them to create a new list using the `+` operator:

````{tip}
```
first_list + other_list
```
````

Here is an example a single list from two separate lists:

```{code-cell} ipython3
first_list = [1, 2, 3]
other_list = [5, 6, 100]
combined_list = first_list + other_list
combined_list
```

## Append an element to a list

Appending an element to a list is done using the `append` method.

````{tip}
```
a_list.append(element)
```
````

Here is an example where we append a new string to a list of strings:

```{code-cell} ipython3
names = ["Vince", "Zoe", "Julien", "Kaitlynn"]
names.append("Riggins")
names
```

```{attention}
It is not possible to do this with a `tuple` as a `tuple` **immutable**](difference_between_a_list_and_a_tuple).
```

## Remove an element from a list

To remove a given element from a list use the `remove` method.

````{tip}
```
a_list.remove(element)
```
````

Here is an example where we remove a number from a list of numbers:

```{code-cell} ipython3
numbers = [1, 94, 23, 202, 5]
numbers.remove(23)
numbers
```

```{attention}
It is not possible to remove an element from a `tuple` as a `tuple` **immutable**](difference_between_a_list_and_a_tuple).
```

## Sort a list

To sort a list use the `sort` method.

````{tip}
```
a_list.sort()
```
````

Here is an example:

```{code-cell} ipython3
names = ["Vince", "Zoe", "Kaitlynn", "Julien"]
names.sort()
names
```

To sort a list in reverse order use the `sort` method with the `reverse=True`
parameter.

```{code-cell} ipython3
names.sort(reverse=True)
names
```

```{attention}
It is not possible to sort a `tuple` as a `tuple` is [**immutable**](difference_between_a_list_and_a_tuple).
```

## Create a sorted list from an iterable

To create a sorted list from an iterable use the `sorted` function.

````{tip}
```
sorted(iterable)
```
````

Here is an example:

```{code-cell} ipython3
tuple_of_numbers = (20, 50, 10, 6, 1, 50, 105)
sorted(tuple_of_numbers)
```

## Access an element of an iterable

See: [Combinatorics: How to access particular elements in a tuple](how_to_access_particular_elements_in_a_tuple).

## Find the index of an element in an iterable

To identify the position of an element in an iterable use the `index` method.

````{tip}
```
iterable.index(element)
```
````

Here is an example:

```{code-cell} ipython3
numbers = [1, 94, 23, 202, 5]
numbers.index(23)
```

```{attention}
Recall that python uses `0`-based indexing. The first element in an iterable has
index `0`.
```

(access_an_element_using_negative_indexing)=

## Access an element of an iterable using negative indexing

It is possible to access an element of an iterable by counting from the end of
the iterable using negative indexing.

````{tip}
```
iterable[-index_from_end]
```
````

Here is an example showing how to access the penultimate element in a tuple:

```{code-cell} ipython3
basket = ("Carrots", "Potatoes", "Strawberries", "Juice", "Ice cream")
basket[-2]
```

(slice_an_iterable)=

## Slice an iterable

To create a new iterable from an iterable use `[]` and specify a start
(inclusive) and end (exclusive) pair of indices.

````{tip}
```
iterable[include_start_index: exclusive_end_index]
```
````

For example:

```{code-cell} ipython3
basket = ("Carrots", "Potatoes", "Strawberries", "Juice", "Ice cream")
basket[2: 5]
```

(find_the_number_of_elements_in_an_iterable)=

## Find the number of elements in an iterable

To count the number of elements in an iterable use `len`:

````{tip}
```
len(iterable)
```
````

For example:

```{code-cell} ipython3
basket = ("Carrots", "Potatoes", "Strawberries", "Juice", "Ice cream")
len(basket)
```

## Create a set

A set is a collection of distinct objects. This can be created in Python using
the `set` command on any iterable. If there are non distinct objects in the
iterable then this is an efficient way to remove duplicates.

````{tip}
```
set(iterable)
```
````

Here is an example of creating a set:

```{code-cell} ipython3
iterable = (1, 1, 3, 4, 4, 3, 2, 1, 10)
unique_values = set(iterable)
unique_values
```

## Do set operations

Set operations between two sets can be done using Python:

- $S_1 \cup S_2$: `set_1 | set_2`
- $S_1 \cap S_2$: `set_1 & set_2`
- $S_1 \setminus S_2$: `set_1 - set_2`
- $S_1 \subseteq S_2$ (checking if $S_1$ is a subset of $S_2$): `set_1 <= set_2`

Here are some examples of carrying out the above:

```{code-cell} ipython3
set_1 = set((1, 2, 3, 4, 5))
set_2 = set((4, 5, 6, 7, 8, 9))

set_1 | set_2
```

```{code-cell} ipython3
set_1 & set_2
```

```{code-cell} ipython3
set_1 - set_2
```

```{code-cell} ipython3
set_1 <= set_2
```

(create_hash_tables) =

## Create hash tables

Lists and tuples allow us to immediately recover a value given its position.
Hash tables allow us to create arbitrary `key` `value` pairs so that given any
`key` we can immediately recover the value. This is called a dictionary in
Python and is created using `{}` which takes a collection of `key: value`
pairs.

````{tip}
```
{key_1: value, key_2: value, …}
```
````

For example the following dictionary maps pet names to their ages:

```{code-cell} ipython3
ages = {"Riggins": 4, "Chick": 7, "Duck": 7}
ages
```

To recover a value we pass the key to the dictionary using `[]`.

For example:

```{code-cell} ipython3
ages["Riggins"]
```

```{attention}
If a key is used to recover the value with `[]` but the key is not in the dictionary then
an error will be raised.
```

## Access element in a hash table

As described [here](create_hash_tables) to access the value of a `key` in a hash
table use `[]`.

````{tip}
```
dictionary[key]
```
````

It is also possible to use the `get` method.
The `get` method can also be passed the value of a `default` variable to return when the
`key` is not in the hash table:

````{tip}
```
dictionary.get(key, default)
```
````

For example:

```{code-cell} ipython3
ages = {"Riggins": 4, "Chick": 7, "Duck": 7}
ages.get("Vince", -1)
```

## Iterate over keys in a hash table

To iterate over the keys in a hash table use the `keys()` method:

````{tip}
```
dictionary.keys()
```
````

For example:

```{code-cell} ipython3
ages = {"Riggins": 4, "Chick": 7, "Duck": 7}
ages.items()
```

## Iterate over values in a hash table

To iterate over the values in a hash table use the `values()` method:

````{tip}
```
dictionary.values()
```
````

For example:

```{code-cell} ipython3
ages = {"Riggins": 4, "Chick": 7, "Duck": 7}
ages.values()
```

## Iterate over pairs of keys and value in a hash table

To iterate over pairs of keys and values in a hash table use the `items()` method:

````{tip}
```
dictionary.items()
```
````

For example:

```{code-cell} ipython3
ages = {"Riggins": 4, "Chick": 7, "Duck": 7}
ages.items()
```
