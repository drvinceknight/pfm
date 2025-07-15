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

# Further information

## Are there other ways to access elements in tuples?

You have seen in this chapter how to access a single element in a tuple.
There are various ways of indexing tuples:

1. Indexing (seen [here](how_to_access_particular_elements_in_a_tuple))
2. [Negative indexing](access_an_element_using_negative_indexing)
3. [Slicing](slice_an_iterable) (selecting a number of elements)

## Why does `range`, `itertools.permutations` and `itertools.combinations` not directly give the elements?

When you run either of the three `range`, `itertools.permutations` or
`itertools.combinations` tools this is an example of creating a
**generator**. This allows the creation of the instructions to build
something without building it.

In practice this means that you can create large sets without needing to
generate them until required.

### How does the summation notation $\sum$ correspond to the code?

The `sum` command corresponds to the mathematical $\sum$ notation. Here
are a few examples showing the `sum` command, the $\sum$ notation but
also the prose describing:

````{list-table}
:header-rows: 1

* - Mathematics
  - Python
  - Prose
* - $$\sum_{i=1}^{100}i ^2$$
  - ```
    sum(i ** 2 for i in range(1, 101))
    ```
  - The sum of the square of the integers from 1 to 100 (inclusive).
* - $$\sum_{\begin{array}{c}i=1\\\text{if }i\text{ is prime}\end{array}}^{100}i ^2$$
  - ```
    sum(i ** 2 for i in range(1, 101) if sym.isprime(i))
    ```
  - The sum of the square of the integers from 1 to 100 (inclusive) if they are
    prime.
* - $$\sum_{\begin{array}{c}i\in{S}\\\text{if }i\text{ is prime}\end{array}}i ^2$$
  - ```
    sum(i ** 2 for i in S if sym.isprime(i))
    ```
  - The sum of the square of the elements in the collection $S$ if they are
    prime.
````
