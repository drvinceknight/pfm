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

# Question 11

Another good example of this is understanding question 11. Let us use the
formula to find the square root of 10.

- Where do we start (\\(x_0\\))?
- When do we finish?

These questions become immediately clear if we try to do this by hand.

# Understanding the problem before you program 

Be sure to spend time working on the exact steps you want to explain to the
computer (through code) before coding.

**For example let us find the number of perfect numbers less than 30.**

First of all: what is a perfect number?

A number whose divisors sum to it.

We start by understanding how to find these by hand:

1. Count to 30: which means have a number that increments by 1 until we get to
   30.
2. For every number, find all divisors of that number: this means go through all
   numbers that are smaller than it and see if they divide our number.
3. Sum those divisors and if they're equal to the original number keep track of
   that.


```python
>>> n = 0
>>> count = 0
>>> while n < 30:
...     n += 1
...     potential_divisor = 1
...     sum_of_divisors = 0
...     while potential_divisor < n:
...         if n % potential_divisor == 0:
...             sum_of_divisors += potential_divisor
...         potential_divisor += 1
...     if sum_of_divisors == n:
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
