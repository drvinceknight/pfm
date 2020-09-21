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

## Combinatorics

### Introduction

Combinatorics is the mathematical area interested specific finite sets. In a lot of instances this comes down to counting things and is often first encountered by mathematicians through combinations and permutations.

Computers are useful when doing this as they can be used to generate the finite sets we want. Thus we can essentially count things "by hand" (using a computer) to confirm theoretic results. We will see how to do this here.

## Tutorial

We will solve the following problem using a computer to illustrate how a computer can be used to solve combinatorial problems:


---

The digits 1, 2, 3, 4 and 5 are arranged in random order, for form a five-digit number.

1. How many different five-digit numbers can be formed?
2. How many different five-digit numbers are:
    1. Odd
    2. Less than 23000
---

First we are going to get the 5 digits. Python has a nice tool for this called `range` which gives us directly the integers from a given bound to another:

```{code-cell} ipython3
import itertools

digits = range(1, 6)
digits
```

At present that is only the instructions containing the integers from 1 to 5 (the 6 is a strict upper bound). We can transform this to a tuple, using the `tuple` tool:

```{code-cell} ipython3
tuple(range(1, 6))
```

The question is asking us to get all the permutations of size 5 of that set of integers.

The main tool we use for this is a library specifically designed to iterate over objects in different ways: `itertools`.

```{code-cell} ipython3
:tags: [nbval-ignore-output]

permutations = itertools.permutations(digits)
permutations
```

That is again only the set of instructions, to view the actual permutations we will again transform this in to a tuple. We will do this an overwrite the value of `permutations` to not be the instructions but the actual tuple of all the permutations:

```{code-cell} ipython3
permutations = tuple(permutations)
permutations
```

Now to answer the question we need to find out how many tuples are in that tuple. We do this using the Python `len` tool which returns the length of something:

```{code-cell} ipython3
len(permutations)
```

We can confirm this to be correct as we know that there are \\(5!\\) ways of arranging those numbers. The `math` library has a `factorial` tool:

```{code-cell} ipython3
import math

math.factorial(5)
```

In order to find out how many 5 digit numbers are odd we are going to compute the following sum:


\\[
    \sum_{\pi \in \Pi} \pi_5 \mod 2
\\]

Where \\(\Pi\\) is the set of permutations and \\(\pi_5\\) denotes the 5th (and last) element of the permutation. So for example, if the first element of \\(\Pi\\) was \\((1, 2, 3, 4, 5)\\) then \\(\pi_5=5\\) and \\(5 \mod 2=1\\).

To do this we use the `sum` tool in python coupled with the expressions `for` and `in`. We also access the 5th element of a `permutation` using `[4]` (the first element is denoted with a 0, so the 5th is 4):

```{code-cell} ipython3
sum(permutation[4] % 2 for permutation in permutations)
```

We can again check this theoretically, there are three valid choices for the last digit of a given tuple to be odd: \\(1\\), \\(3\\) and \\(5\\). For each of those, there are then 4 choices for the remaining digits:

```{code-cell} ipython3
math.factorial(4) * 3
```

To compute the number of digits that are less than or equal to 2300 we compute a similar sum except we use the `<=` operator and also convert the tuple of digits to a number in base 10:

\\[
    (\pi_1, \pi_2, \pi_3, \pi_4, \pi_5) \to \pi_1 10 ^ 4 + \pi_2 10 ^ 3 + \pi_3 10 ^ 2 + \pi_4 10 + \pi_5
\\]

Thus we are going to compute the following sum:

\\[
    \sum_{\pi \in \Pi \text{ if }\pi_1 10 ^ 4 + \pi_2 10 ^ 3 + \pi_3 10 ^ 2 + \pi_4 10 + \pi_5 \leq 2300} 1
\\]

```{code-cell} ipython3
sum(
    1
    for permutation in permutations
    if permutation[0] * 10 ** 4
    + permutation[1] * 10 ** 3
    + permutation[2] * 10 ** 2
    + permutation[3] * 10
    + permutation[0]
    <= 23000
)
```

We can again confirm this theoretically, for a given tuple to be less than 2300 that is only possible if the first digit is 1 or 2:

- If it is 1 then any of the other \\(4!\\) permutations of the other digits is valid;
- If it is 2 then the second digit must be 1 and any of the other \\(3!\\) permutations of the other digits is valid.

```{code-cell} ipython3
(math.factorial(4) + math.factorial(3))
```

### How to


#### Create a tuple

To create a tuple which is an ordered collection of objects that cannot be changed we use the `()` brackets:

```{code-cell} ipython3
basket = ("Bread", "Biscuits", "Coffee")
basket
```

#### How to access particular elements in a tuple

If we need to we can access elements of this collection using `[]` brackets. The first element is has index `0`:

```python
tuple[index]
```

For example:

```{code-cell} ipython3
basket[1]
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

#### Creating an iterable with a given number of items

A common use of list comprehensions is to combine it with the `range` tool which gives a given number of integers.

For example:

```{code-cell} ipython3
tuple(range(10))
```

Note that `range(N)` gives the integers from 0 until \\(N - 1\\) (inclusive).

+++

It is also possible to pass two values as inputs so that we have a different lower bound:

```{code-cell} ipython3
tuple(range(4, 10))
```

It is also possible to pass a third value as an step size:

```{code-cell} ipython3
tuple(range(4, 10, 3))
```

#### Creating permutations of a given set of elements

The python `itertools` library has a `permutations` tool that will generate all permutations of a given set:

```{code-cell} ipython3
import itertools

basket = ("Bread", "Biscuits", "Coffee")
tuple(itertools.permutations(basket))
```

It is possible to limit the size to only be permutations of size `r`:

```{code-cell} ipython3
tuple(itertools.permutations(basket, r=2))
```

#### Creating combinations of a given set of elements

The python `itertools` library has a `combinations` tool that will generate all combinations of size `r` of a given set:

```{code-cell} ipython3
tuple(itertools.combinations(basket, r=2))
```

A combination does not care about order so by default the combinations generated are sorted.

+++

#### Adding items in a tuple

We can compute the sum of items in a list using the `sum` tool:

```{code-cell} ipython3
sum((1, 2, 3))
```

We can also directly use the `sum` without specifically creating the list. This corresponds to the following mathematical notation:

\\[
    \sum_{s\in S}f(s)
\\]

and is done using the following:


```python
sum(f(object) for object in old_list)
```

Here is an example of calculating the following sum:


\\[
    \sum_{n=0}^{10} n ^ 2
\\]

```{code-cell} ipython3
sum(n ** 2 for n in range(11))
```

Finally we can compute conditionally sums by only summing over elements that meet a given condition using the following:

```python
sum(f(object) for object in old_list if condition)
```

Here is an example of calculating the following sum:

\\[
    \sum_{\begin{array}{c}n=0\\\text{ if }n\text{ odd}\end{array}}^{10} n ^ 2
\\]

```{code-cell} ipython3
sum(n ** 2 for n in range(11) if n % 2 == 1)
```

#### Directly computing \\(n!\\)

The `math` library has a `factorial` tool:

```{code-cell} ipython3
math.factorial(5)
```

#### Directly computing \\({n \choose i}\\)

The `scipy.special` library has a `comb` tool:

```{code-cell} ipython3
import scipy.special

scipy.special.comb(3, 2)
```

#### Directly computing \\(^n P_r\\)

The `scipy.special` library has a `perm` tool:

```{code-cell} ipython3
scipy.special.perm(3, 2)
```

### Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. Obtain the following tuples using the `range` command:
    1. \\((0, 1, 2, 3, 4, 5)\\)
    2. \\((2, 3, 4, 5)\\)
    3. \\((2, 4, 6, 8)\\)
    4. \\(-1, 2, 5, 8\\)
2. By **both** generating and directly computing obtain the **number of** the following:
    1. All permutations of \\((0, 1, 2, 3, 4, 5)\\).
    2. All permutations of \\(("A", "B", "C")\\).
    3. Permutations of size 3 of \\((0, 1, 2, 3, 4, 5)\\).
    4. Permutations of size 2 of \\((0, 1, 2, 3, 4, 5, 6)\\).
    5. Combinations of size 3 of  \\((0, 1, 2, 3, 4, 5)\\).
    6. Combinations of size 2 of  \\((0, 1, 2, 3, 4, 5)\\).
    7. Combinations of size 5 of  \\((0, 1, 2, 3, 4, 5)\\).
3. A class consists of 7 students from Ashville and 8 from Bewton. A committee of 5 students is chosen at random the class.
    1. Find the number of committees that include 2 students from Ashville and 3 from Bewton are chosen.
    2. In fact 2 students, from Ashville and 3 from Bewton are chosen. In order to watch a video, all 5 committee members sit in a row. In how many different orders can they sit if no two students from Bewton sit next to each other.
4. Three letters are selected at random from the 8 letters of the word `COMPUTER`, without regard to order.
    1. Find the number of possible selections of 3 letters.
    2. Find the number of selections of 3 letters with the letter `P`.
    3. Find the number of selections of 3 letters where the 3 letters form the word `TOP`.

### References

#### How does tuple indexing work

We have seen in this chapter how to access a single element in a tuple. There are various ways of indexing tuples:

1. Indexing (what we have seen here)
2. Negative indexing (indexing starting from the end)
3. Slicing (selecting a number of elements)

This document gives good information on this: https://www.programiz.com/python-programming/tuple

#### Why does `range`, `itertools.permutations` and `itertools.combinations` not directly give the elements

When you run either of the three `range`, `itertools.permutations` or
`itertools.combinations` tools this is an example of creating a **generator**.
This allows us to create the instructions to build something without building
it.

In practice this means that we can create large sets without needing to generate
them until we wanted to.
