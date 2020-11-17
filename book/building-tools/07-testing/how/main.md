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

## How to write an `assert` statement?

An `assert` statement is followed by 2 values: a boolean and an optional
string that gets returned if the boolean is `False`.

````{tip}
```
assert boolean, string
```
````

For example, given a function that adds one to a variable:

```{code-cell} ipython3
def add_one(a):
    """
    Returns a + 1
    """
    return a + 1
```

We can assert that we have the expected behaviour:

```{code-cell} ipython3
assert add_one(5) == 6, "The function gave the wrong answer."
```

Note that if we change the function to include an error for example here adding
2 and not 1, and run the same assert
we get an error as well as the specific string,

```{code-cell} ipython3
:tags: ["raises-exception"]

def add_one(a):
    """
    Returns a + 1
    """
    return a + 2

assert add_one(5) == 6, "The function gave the wrong answer."
```

## How to write `assert` statements for code that acts randomly?

When making an assertion about code that behaves in a random manner, we use
seeding as described in {ref}`reproduce_random_events`.

For example:

```{code-cell} ipython3
import random

def roll_a_dice():
    """
    Pick a random integer between 1 and 6 (inclusive)
    """
    return random.choice(range(1, 7))
```

To test this we can include a number of seeded assertions:

```{code-cell} ipython3
random.seed(0)
assert roll_a_dice() == 4, "The 0 seed did not give the epected result"
random.seed(1)
assert roll_a_dice() == 2, "The 1 seed did not give the epected result"
random.seed(2)
assert roll_a_dice() == 1, "The 2 seed did not give the epected result"
random.seed(3)
assert roll_a_dice() == 2, "The 3 seed did not give the epected result"
```

We can also check behaviour over a number of repetitions:

```{code-cell} ipython3
random.seed(0)
samples = [roll_a_dice() for repetition in range(1000)]
assert set(samples) == {1, 2, 3, 4, 5, 6}, "Not all values have been obtained over 1000 repetitions"
```

We can also confirm that the count of a given value is in an expected range:

```{code-cell} ipython
assert [samples.count(k) for k in range(1, 7)] == [193, 150, 166, 170, 152, 169], "The count of the values is not giving the expected count"
```

```{tip}
The last assertion used the `count` method on a list that counts a given number
of items in a list.
```

## How to write a test file?

To write tests assertion statement can be put in to a file separate to the code
in functions.

For example, if the `dice.py` file contained:

```python
import random

def roll_a_dice():
    """
    Pick a random integer between 1 and 6 (inclusive)
    """
    return random.choice(range(1, 7))
```

Then a separate `test_dice.py` file with the following would be written:

```python
import dice

def test_roll_a_dice_with_specific_values():
    """
    Check the roll a dice function gives specific numbers for a number of seeds.
    """
    random.seed(0)
    assert dice.roll_a_dice() == 4, "The 0 seed did not give the epected result"
    random.seed(1)
    assert dice.roll_a_dice() == 2, "The 1 seed did not give the epected result"
    random.seed(2)
    assert dice.roll_a_dice() == 1, "The 2 seed did not give the epected result"
    random.seed(3)
    assert dice.roll_a_dice() == 2, "The 3 seed did not give the epected result"

def test_roll_a_dice_for_a_large_sample():
    """
    Collect a sample of 1000 rolls and confirm that we have expected results.
    """
    random.seed(0)
    samples = [dice.roll_a_dice() for repetition in range(1000)]
    assert set(samples) == {1, 2, 3, 4, 5, 6}, "Not all values have been obtained over 1000 repetitions"
    assert [samples.count(k) for k in range(1, 7)] == [193, 150, 166, 170, 152, 169], "The count of the values is not giving the expected count"

test_roll_a_dice_with_specific_values()
test_roll_a_dice_for_a_large_sample()
```

To run the tests we would then type the following at the command line:

```bash
$ python test_dice.py
```

## How to format doc tests?

When writing code in documentation if we write it using a specific format then
python can be used to confirm that the code and its output is correct.

````{tip}
```
>>> <python_code>
<expected_output
>>> <python_code_over_multiples_lines>
... <python_code_over_multiple_lines>
<expected_output>
```
````

- `>>>` is marks the start of a python statement.
- `...` is used if the statement is multiple lines.
- The expected output is written after the python statements.

For example if we were documenting the following code written in a `dice.py`
file:

```python
import random

def roll_a_dice():
    """
    Pick a random integer between 1 and 6 (inclusive)
    """
    return random.choice(range(1, 7))
```

We would write:

```
>>> import dice
>>> random.seed(0)
>>> dice.roll_a_dice()
4

```

## How to run doctests?

Given a <file> with doctests to run them we type the following at the
command line:

````{tip}
```
$ python -m doctest <file>
```
````

For example:

```bash
python -m doctest README.md
```
