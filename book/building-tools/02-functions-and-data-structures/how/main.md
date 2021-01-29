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

We covered functions in a previous chapter as well: [Probability: How to define
a function](define_a_function)

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

## Using hash tables

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
If a key is used to recover the value but the key is not in the dictionary then
an error will be raised.
```
