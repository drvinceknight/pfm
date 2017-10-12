---
layout     : post
categories : 2017-2018
title      : "2017-2018: Handout 03 - Understanding the mathematics"
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1300-1500**

# What was in this lab sheet

- Defining variables;
- If statements and boolean variables;
- While loops.


# Programming on paper

Consider the following problem:

Let us sum the first 6 numbers are divisible by 2:

```python
>>> count = 0
>>> total = 0
>>> n = 0
>>> while count < 6:
...     n += 1
...     if n % 2 == 0:
...         total += n
...         count += 1
>>> total
42

```

Is this correct?

Let us "program on paper". We will
step through the code and keep track of the variables:

```
n  | n % 2 |  total | count
0  | NA    |  0     | 0
1  | 1     |  0     | 0
2  | 0     |  2     | 1
3  | 1     |  2     | 1
4  | 0     |  6     | 2
5  | 1     |  6     | 2
6  | 0     |  12    | 3
7  | 1     |  12    | 3
8  | 0     |  20    | 4
9  | 1     |  14    | 4
10 | 0     |  30    | 5
11 | 1     |  30    | 5
12 | 0     |  42    | 6
```

This approach also helps with finding errors.

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

# Summary

- Use pen and paper to make sure you fully understand the problem.
- Reduce the complexity of the problem (perhaps try smaller examples)
- Come up with a plan!
