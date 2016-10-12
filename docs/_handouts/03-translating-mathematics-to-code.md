---
layout     : post
categories : 2016-2017
title      : "2016-2017: Handout 03 - Translating mathematics to code."
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1400-1600**

# What was in this lab sheet:

- Lists
- For loops and list comprehensions
- Functions

## List comprehensions

This is using a `for` loop to create a list of squares:

```python
>>> squares = []
>>> for n in range(10):
...     squares.append(n ** 2)
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```

This is doing the same thing using a **list comprehension** (the above is
**not** a list comprehension):

```python
>>> squares = [n ** 2 for n in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```

## Translating mathematics to

Difficulties in question 6 and question 9 almost universally came from not
having an understanding of what the question was trying to achieve
**mathematically**.

Both questions were of the same form:

1. Write a function for a given mathematical expression;
2. Check **another** expression for the summation of the previous expression.

When working through **any mathematical problem** you should try and work
things out for small examples by hand. This will help understand things.

For example for question 6, it would be helpful as you read the question to
write down the following table:

| \\(n\\)       | \\(f_n\\)     | \\(\sum_{i=0}^n f_n\\)  | \\(f_{n+2}\\) |
| ------------- |:-------------:| :----------------------:|:-------------:|
| 0             | 1             | 1                       | 2             |
| 1             | 1             | 2 					  | 3             |
| 2             | 2             | 4 					  | 5             |
| 3             | 3             | 7 					  | 8             |
| 4             | 5             | 12					  | 13            |

By doing this, you would:

- gain an underlying understanding of what the question is asking you to do
- have some insight as to the calculations required for \\(f_n\\);
- have some values ready that might help with debugging.

## Make notes

Whilst watching the videos and working through the lab sheets I **recommend**
you make your own notes. This will help with your understanding. (I recommend
this for all your modules.)
