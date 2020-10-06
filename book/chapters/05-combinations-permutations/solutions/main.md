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

> `1`. Obtain the following tuples using the `range` command:

> `1`. $(0, 1, 2, 3, 4, 5)$

```{code-cell} ipython3
tuple(range(6))
```

> `2`. $(2, 3, 4, 5)$

```{code-cell} ipython3
tuple(range(2, 6))
```

> `3`. $(2, 4, 6, 8)$

```{code-cell} ipython3
tuple(range(2, 9, 2))
```

> `4`. $-1, 2, 5, 8$

```{code-cell} ipython3
tuple(range(-1, 9, 3))
```

## Question 2

> `2`. By **both** generating and directly computing obtain the **number of** the following:

> `1`. All permutations of $(0, 1, 2, 3, 4, 5)$.

Generating them all:

```{code-cell} ipython3
:tags: [output_scroll]

import itertools

digits = range(6)
permutations = tuple(itertools.permutations(digits))
permutations
```

Counting them:

```{code-cell} ipython3
len(permutations)
```

Computing the number directly:

```{code-cell} ipython3
import math

math.factorial(6)
```

> `2`. All permutations of $(A, B, C)$.

Generating them all:

```{code-cell} ipython3
:tags: [output_scroll]

letters = ("A", "B", "C")
permutations = tuple(itertools.permutations(letters))
permutations
```

Counting them:

```{code-cell} ipython3
len(permutations)
```

Computing the number directly:

```{code-cell} ipython3
math.factorial(3)
```

> `3`. Permutations of size 3 of $(0, 1, 2, 3, 4, 5)$.

Generating them all:

```{code-cell} ipython3
:tags: [output_scroll]

digits = range(6)
permutations = tuple(itertools.permutations(digits, r=3))
permutations
```

Counting them:

```{code-cell} ipython3
len(permutations)
```

Computing the number directly:

```{code-cell} ipython3
import scipy.special

scipy.special.perm(6, 3)
```

> `4`. Permutations of size 2 of $(0, 1, 2, 3, 4, 5, 6)$.

Generating them all:

```{code-cell} ipython3
:tags: [output_scroll]

digits = range(7)
permutations = tuple(itertools.permutations(digits, r=2))
permutations
```

Counting them:

```{code-cell} ipython3
len(permutations)
```

Computing the number directly:

```{code-cell} ipython3
import scipy.special

scipy.special.perm(7, 2)
```

> `5`. Combinations of size 3 of  $(0, 1, 2, 3, 4, 5)$.

Generating them all:

```{code-cell} ipython3
:tags: [output_scroll]

digits = range(6)
combinations = tuple(itertools.combinations(digits, r=3))
combinations
```

Counting them:

```{code-cell} ipython3
len(combinations)
```

Computing the number directly:

```{code-cell} ipython3
import scipy.special

scipy.special.comb(6, 3)
```

> `6.` Combinations of size 2 of  $(0, 1, 2, 3, 4, 5)$.

Generating them all:

```{code-cell} ipython3
:tags: [output_scroll]

digits = range(6)
combinations = tuple(itertools.combinations(digits, r=2))
combinations
```

Counting them:

```{code-cell} ipython3
len(combinations)
```

Computing the number directly:

```{code-cell} ipython3
import scipy.special

scipy.special.comb(6, 2)
```

> `7`. Combinations of size 5 of  $(0, 1, 2, 3, 4, 5)$.

Generating them all:

```{code-cell} ipython3
:tags: [output_scroll]

digits = range(6)
combinations = tuple(itertools.combinations(digits, r=5))
combinations
```

Counting them:

```{code-cell} ipython3
len(combinations)
```

Computing the number directly:

```{code-cell} ipython3
import scipy.special

scipy.special.comb(6, 5)
```

## Question 3

> `3`. A class consists of 3 students from Ashville and 4 from Bewton. A
> committee of 5 students is chosen at random the class.

> `1`. Find the number of committees that include 2 students from Ashville and 3
> from Bewton are chosen.

We directly enumerate them:

```{code-cell} ipython3
:tags: [output_scroll]

students = ("Ashville", "Ashville", "Ashville", "Bewton", "Bewton", "Bewton", "Bewton")
committees = tuple(itertools.combinations(students, 5))
committees
```

Selecting only the ones with 2 Ashville students (if there are 2 Ashville
students then there are 3 Bewton ones):

```{code-cell} ipython
sum(1 for committee in committees if committee == ("Ashville", "Ashville", "Bewton", "Bewton", "Bewton"))
```


> `2`. In fact 2 students, from Ashville and 3 from Bewton are chosen. In order
> to watch a video, all 5 committee members sit in a row. In how many different
> orders can they sit if no two students from Bewton sit next to each other.

To answer this we need to consider committees as permutations (as order
matters):


```{code-cell} ipython3
:tags: [output_scroll]

committee = ("Ashville", "Ashville", "Bewton", "Bewton", "Bewton")
seating_arrangements = tuple(itertools.permutations(committee))
seating_arrangements
```

For no two students from Bewton to site next to each other the order is fixed:

```{code-cell} ipython3
sum(1 for seating_arrangement in seating_arrangements if seating_arrangement == ("Bewton", "Ashville", "Bewton", "Ashville", "Bewton"))
```

## Question 4

> `4`. Three letters are selected at random from the 8 letters of the word
> `COMPUTER`, without regard to order.

> `1`. Find the number of possible selections of 3 letters.

```{code-cell} ipython3
:tags: [output_scroll]

letters = ("C", "O", "M", "P", "U", "T", "E", "R")
selections = tuple(itertools.combinations(letters, 3))
selections
```

Counting them:

```{code-cell} ipython3
len(selections)
```

Note that a string is in fact an iterable so we can also do:


```{code-cell} ipython3
:tags: [output_scroll]

letters = "COMPUTER"
selections = tuple(itertools.combinations(letters, 3))
len(selections)
```


> `2`. Find the number of selections of 3 letters with the letter `P`.

```{code-cell} ipython3
sum(1 for selection in selections if "P" in selection)
```

> `3`. Find the number of selections of 3 letters where the 3 letters form the word `TOP`.

```{code-cell} ipython3
sum(1 for selection in selections if selection == ("O", "P", "T"))
```
