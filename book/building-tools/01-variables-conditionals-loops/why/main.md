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

## Why can I not only use a `while` loop

The `for` loop allows us to iterate over any selection of objects. Some
languages do not have a generic `for` loop like this. In some cases it is only
possible to iterate over a set of integers (similar to the `for i in range(n)`
pattern) or to only use a `while` loop.

Because of this, it is often the case that you will see code that uses `while`
loops instead of `for` loops. For example:

```{code-cell} ipython3
seasons = ("Winter", "Spring", "Summer", "Autumn")

number_of_seasons = len(seasons)
i = 0
while i < number_of_seasons:
    season = seasons[i]
    print(season)
    i += 1
```

The above code is equivalent to:

```{code-cell} ipython3
seasons = ("Winter", "Spring", "Summer", "Autumn")
for season in seasons:
    print(season)
```

While it is possible to use a `while` loop instead of a `for` loop there are no
advantages to doing that and in fact only disadvantages:

- Using the `while` loop requires iterating over the iterable twice: the first
  time when counting the length of it using `len` and the second time during the
  `while` statement itself.
- There is more potential for error in the code: it would not be unlikely to
  have an off by one error in the boolean condition.
- It is less readable.

The following is a good guideline:

- Use a `for` loop when you know what you are iterating over.
- Use a `while` loop when only know a specific condition under which you should
  iterate.

## Why should I not check if a boolean is `True`

It is possible to create a boolean by comparing another boolean to `True` or
`False` for example:

```{code-cell} ipython3
boolean = False
boolean == True
```

Thus when using `if` or `while` statements you might sometimes see things like
the following:

```{code-cell} ipython3
import random

random.seed(4)
selected_integer = random.randint(0, 10)
number_of_selections = 1
while (selected_integer % 2 == 1) == True:
    selected_integer = random.randint(0, 10)
    number_of_selections += 1
number_of_selections
```

However this is not as clear as writing:

```{code-cell} ipython3
import random

random.seed(4)
selected_integer = random.randint(0, 10)
number_of_selections = 1
while selected_integer % 2 == 1:
    selected_integer = random.randint(0, 10)
    number_of_selections += 1
number_of_selections
```
