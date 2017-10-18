---
layout     : post
categories : 2017-2018
title      : "2017-2018: Handout 04 - Functions and the return statement"
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1300-1500**

# What was in this lab sheet

- Lists;
- Functions.

# Range

The `range` function is short hand to be able to iterate over numbers:

```python
>>> range(1, 10)
range(1, 10)

```

This doesn't specifically create a `list` but we can turn it in to one:

```python
>>> list(range(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]

```

# Breaking up code

Functions are very useful for breaking code up in to small working pieces. For
example the following rewrites the code for finding the number of perfect
numbers less than 30
(http://vknight.org/cfm/handouts/03-understanding-the-mathematics/):

First let us define a function to get the divisors of any number:

```python
>>> def get_divisors_of(n):
...     """
...     Obtain the divisors of n
...     """
...     return [i for i in range(1, n) if n % i == 0]
>>> get_divisors_of(6)
[1, 2, 3]

```

Now we can use this to make the code for counting perfect numbers simpler:

```
>>> n = 0
>>> count = 0
>>> for n in range(1, 30):
...     if sum(get_divisors_of(n)) == n:
...         count += 1
>>> count
2

```

# The `return` statement ends a function

So this function:

```python
>>> def f(n):
...     """
...     This is text in between triple quoatation marks is a doc string.
...     We use it to describe what a function does. For example here we would
...     write: This function returns f(n) as described above.
...     """
...     if n <= 5:
...        return 1
...     elif n % 2 == 0:  # Otherwise if (else if)
...        return 2
...     else:  # Otherwise
...        return 3
>>> f(11)
3

```

Can equivalently be written as:

```python
>>> def f(n):
...     """
...     This is text in between triple quoatation marks is a doc string.
...     We use it to describe what a function does. For example here we would
...     write: This function returns f(n) as described above.
...     """
...     if n <= 5:
...        return 1
...     if n % 2 == 0:  # Otherwise if (else if)
...        return 2
...     return 3
>>> f(11)
3

```

Keep this in mind when you use `return` statements inside loops.

# Submitting code in a notebook

When you type code and submit the code that sends the instructions to Python.
Some errors I saw in labs where due to the fact that code was written prior had
not been submitted (so Python did not know the definition of a particular
function).
