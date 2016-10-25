---
layout     : post
categories : 2016-2017
title      : "2016-2017: Handout 05 - Classes."
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1400-1600**

# What was in this lab sheet:

- Classes
- Reading from csv files

## Reading from csv file

Reading from csv files proved to be a distraction from the main point of the
sheet which is object oriented programming and classes.

We saw how to read from csv files in the previous lab sheet. What proved
difficult here was the our rows of numbers did not contain a single number but
three numbers.

We can approach this by splitting the data once on the `\n` character to get
something like:

```
['1,2,3', '4,5,6', '7,8,9']
```

Now each single element is a string once again. We need to split this on the `,`
character. This is just one more processing step than before (before: we had to
convert out single number to an integer).

We can do this by doing something like:

```python
>>> data = ['1,2,3', '4,5,6', '7,8,9']
>>> data = [row.split(',') for row in data]
>>> data
[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

```

**Look through the solutions for a longer explanation of this.**

## Using a class

Let us assume we wanted to count the number of linear expressions of the form
\\(ax+b\\) that have a root out of the following linear expressions:

$$4x + 6$$

$$0x + 6$$

$$2x - 2$$

$$0x + 3$$

(This is trivial but it's just to serve as an example). Here is the
`LinearExpression` class from the worked example:

```python
>>> class LinearExpression:
...     """A class for a linear expression"""
...     def __init__(self, a, b):
...         self.a = a
...         self.b = b
...     def root(self):
...         """Return the root of the linear expression"""
...         if self.a != 0:
...             return - self.b / self.a
...         return False
...     def __add__(self, linexp):
...         """A special method: let's us have addition between expressions"""
...         return LinearExpression(self.a + linexp.a, self.b + linexp.b)
...     def __repr__(self):
...         """A special method: changes the default way an instance is displayed"""
...         return "Linear expression: " + str(self.a) + "x + " + str(self.b)

```

Let us put the coefficients above in a list:

```python
>>> coefficients = [[4, 6], [0, 6], [2, -2], [0, 3]]

```

Now, let us create Linear expressions for each pair of coefficients:

```python
>>> linear_exps = [LinearExpression(row[0], row[1]) for row in coefficients]
>>> linear_exps  # We have a list of expressions:
[Linear expression: 4x + 6, Linear expression: 0x + 6, Linear expression: 2x + -2, Linear expression: 0x + 3]

```

Finally let us count the ones that have a root:

```python
>>> linear_exps_with_root = [exp for exp in linear_exps if exp.root() is not False]
>>> linear_exps_with_root
[Linear expression: 4x + 6, Linear expression: 2x + -2]
>>> len(linear_exps_with_root)
2

```
