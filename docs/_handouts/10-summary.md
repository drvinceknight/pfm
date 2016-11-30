---
layout     : post
categories : 2016-2017
title      : "2016-2017: Handout 10 - Summary."
comments   : false
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1400-1600**

## What you have learnt this week:

Using sympy to solve differential equations.

## Summary of everything you have learnt this term

No one seems to have had many difficulties with differential equations. So I'll
take this opportunity to go (briefly) recap everything we have seen this term:

### Assignment, variables and boolean statements

In the first lab sheet we saw how to create and manipulate variables:

```python
>>> nbr = 42
>>> nbr += 1
>>> nbr
43

```

We also saw how to use boolean variables with `if` and `while` statements:

```python
>>> if nbr == 43:
...     nbr = 0
>>> nbr
0
>>> while nbr < 4:
...     nbr += 1
...     print(nbr)
1
2
3
4

```

### Lists, for loops and functions

In the second lab sheet we saw how to create and use lists:

```python
>>> nbrs = [1, 4, 9, 16]
>>> nbrs.append(-10)
>>> nbrs
[1, 4, 9, 16, -10]
>>> nbrs[0], nbrs[-1]
(1, -10)

```

We also saw how we could loop over elements in a list using a dummy variable:

```python
>>> for n in nbrs:
...    print(n, n >= 0)
1 True
4 True
9 True
16 True
-10 False

```

We learned how to create functions which give us a way of making reusable code:

```python
>>> import math
>>> def f(x):
...     return math.sqrt(x)
>>> f(nbrs[2])
3.0

```

We also learnt the way to create new lists from old lists using list
comprehensions:

```python
>>> [f(n) for n in nbrs if n >= 0]
[1.0, 2.0, 3.0, 4.0]

```

### Recursive functions, reading and writing data

In the third lab sheet we saw how to use recursion:

```python
>>> def fibonacci(n):
...     if n in [0, 1]:
...         return 1
...     return fibonacci(n - 1) + fibonacci(n - 2)
>>> for n in range(4):
...     print(fibonacci(n))
1
1
2
3

```

We also saw how to write to file:

```python
with open("fibs.csv", 'w') as outfile:
    for n in range(4):
        outfile.write(str(n) + "," + str(fibonacci(n)) + "\n")
```

We saw how to read from file:


```python
>>> with open("fibs.csv", 'r') as outfile:
...      string = outfile.read()
>>> string
'0,1\n1,1\n2,2\n3,3\n'
>>> data = [row.split(',') for row in string.split('\n')][:-1]
>>> data  # Note these are al strings
[['0', '1'], ['1', '1'], ['2', '2'], ['3', '3']]

```

### Symbolic variables

We saw how to define and manipulate symbolic variables using Sympy:

```python
>>> import sympy as sym
>>> x = sym.symbols('x')
>>> sym.solveset(x ** 2 + 1, x)
{-I, I}

```

### Symbolic calculus

We saw how to calculate study Calculus:

```
>>> expr = x ** 2 + 1
>>> sym.limit(expr, x, 0)
1
>>> sym.diff(expr, x)
2*x
>>> sym.integrate(expr, x)
x**3/3 + x

```

### Linear algebra

We saw how to use Numpy to study Linear Algebra:

```python
>>> import numpy as np
>>> A = np.matrix([[1, 2], [1, 1]])
>>> b = np.matrix([[0], [1]])
>>> np.linalg.solve(A, b)
matrix([[ 2.],
        [-1.]])

```

### Differential equations

We saw how to use Sympy to solve differential equations:

```python
>>> y = sym.Function('y')
>>> eq = sym.diff(y(x), x) - sym.cos(x)
>>> sym.dsolve(eq, y(x))
Eq(y(x), C1 + sin(x))

```

---

This is just the start of writing code. Python is one of the
most popular languages in modern software development:

- It was used to help analyse gravitational waves and other scientific
  discoveries;
- It is used in software you use everyday (YouTube, Dropbox, Instagram etc...)
- It is used by Mathematicians.

**Who knows what you end up doing at the end of your degree. Having Python on
your CV will be a positive thing.**

Continue to build your skills in it (you will have the opportunity to do so next
term) but my advice is to over the next 3 or 4 years, try and pick and learn
more programming languages. They all have strengths and weaknesses.
