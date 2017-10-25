---
layout     : post
categories : 2017-2018
title      : "2017-2018: Handout 05 - "
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1300-1500**

# What was in this lab sheet

- Recursion;
- Reading and writing to files.

# Catalan numbers

A lot of difficulty came from question 6: Catalan numbers. The recursive formula
for Catalan numbers is very similar to the formula for the Fibonacci sequence:

1. Base case: \\(C(0)=1\\);
2. Recursive rule: \\(C(n)=\sum_{i=0}^{n-1}C(i)C(n-1-i)\\);

This gives:

- \\(C(0) = 0\\)
- \\(C(1) = C(0)C(-0)\\)
- \\(C(2) = C(0)C(1) + C(1)(0)\\)
- \\(C(3) = C(0)C(2) + C(1)(1) + C(2)C(0)\\)

For each number \\(n\\):

- We find the terms (products of two other Catalan numbers);
- We sum them together

The solution shows an approach for this.

# Reading files and displaying a lot of data

If you read in the primes file and attempt to display it, your machine might
says that it can't display them. This is just a question of displaying them. You
can display less numbers:

```python
>>> string[:10]

```

# Another example of recursion

Take a look at this handout from last year which looks at the collatz conjecture
using recursion:
[http://vknight.org/cfm/handouts/2016-2017/04-the-collatz-conjecture/](http://vknight.org/cfm/handouts/2016-2017/04-the-collatz-conjecture/)
