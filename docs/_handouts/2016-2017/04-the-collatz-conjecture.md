---
layout     : post
categories : 2016-2017
title      : "2016-2017: Handout 04 - The Collatz conjecture."
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1400-1600**

# What was in this lab sheet:

- Recursion
- Writing to file
- Reading from file

## The Collatz conjecture

There was not many difficulties that became apparent with the code this week.
The main difficulty seemed to be with the Mathematical notation for summation.

Here is a mathematical conjecture (that has not been proved) that is easy to
implement with code using recursion.

**The Collatz conjecture**

> Take any positive integer \\(n\\). If \\(n\\) is even, divide it by 2 to get
\\(n / 2\\). If \\(n\\) is odd, multiply it by 3 and add 1 to obtain \\(3n +
1\\). Repeat the process indefinitely. The conjecture is that no matter what
number you start with, you will always eventually reach 1.

Here is some code that calculates the procedure for given \\(n\\):

```python
>>> def collatz(n):
...     """
...     Implement the collatz reduction:
...
...     - if n is even: repeat with n/2
...     - if n is odd: repeat with 3n + 1
...
...     The conjecture states that this terminates at 1.
...
...     This function returns the number of iterations needed to get to 1.
...     """
...     if n == 1:  # If the value is already 1. Then there is just 1 step.
...         return 1
...     if n % 2 == 0:
...         # If n is even then, we keep track of 1 step and carry on with n/2
...         return collatz(n / 2) + 1
...     # Finally, we keep track of 1 step and carry on with 3n+1
...     return collatz(3 * n + 1) + 1

```

Let's see how this works for a couple of numbers:

```python
>>> collatz(4)
3

```

Indeed: \\(4\to 2\to 1\\).  Also:

```python
>>> collatz(3)
8

```

Indeed: \\(3\to 10\to 5\to 16\to 8\to 4\to 2\to 1\\).

We see what the largest value is for the first 200 positive
integers:

```python
>>> max([collatz(n) for n in range(1, 200)])
125

```

Proving that this always happens (or finding a counter example) is an open
mathematical problem.
