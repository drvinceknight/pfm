---
layout     : post
categories : 2016-2017
title      : "2016-2017: Handout 07 - The class test and symbolic mathematics."
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1400-1600**

## What you have learnt this week:

Using Sympy to study symbolic mathematics.

## Coursework

Your next assessment is the individual coursework, this is due
 1300 Thursday of Week 11 (December 8th).

## Equality of expressions

Sympy expressions specifically keep track of their form.

For example, the following is just two ways of writing the same thing:

$$
\text{exp1} = x ^2 + x
$$

$$
\text{exp2} = x(x + 1)
$$

If we consider these in Python:

```python
>>> import sympy as sym
>>> x = sym.symbols('x')
>>> exp2 =  x ** 2 + x
>>> exp2
x**2 + x
>>> exp1 = x *(1 + x)
>>> exp1
x*(x + 1)

```

If we check that these two expressions are the same, we get that they are not:

```python
>>> exp1 == exp2
False

```

This is because they're not exactly the same expression, however, **of course**
they compute to the same expression:

```python
>>> exp3 = exp1 - exp2
>>> exp3
-x**2 + x*(x + 1) - x
>>> exp3.expand()
0

```

Note that sometimes it will automatically translate the expression somewhat.
For example, in question 10 of this lab sheet we were asked to verify that
\\(\cos(n\pi) = (-1) ^ n\\).

```python
>>> n = sym.symbols('n', integer=True)  # This is an important step
>>> exp1, exp2 = sym.cos(n * sym.pi), (-1) ** n
>>> exp1, exp2
((-1)**n, (-1)**n)

```
