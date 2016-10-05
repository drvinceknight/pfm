---
layout     : post
categories : 2016-2017
title      : "2016-2017: Indentation, while loops, debugging (and crashing Jupyter)"
comments   : false
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1400-1600**

# What was in this lab sheet:

- Defining variables;
- If statements and boolean variables;
- While loops.

# Housekeeping

You should watch **and listen** to the videos. These are there to help and offer
an initial explanation of the work. They are the equivalent of the lecture.

Some students have been confused by the `>>>` on the lab sheets which do not
appear in the videos. In the lab sheets and handouts, is important these are
just there so that you can see the difference between the input and outputs.
When you type the code you do not need to type the `>>>`.

# Indentation is important in Python

The levels at which Python indents things is important. This helps creates
blocks of code that Python runs on certain occasions.

Let us take a look at the following:

```python
>>> n = 0
>>> while n < 6:
...    n += 1
...    if n % 2 == 0:
...        print(n)
2
4
6

```

The above repeats the code and prints `n` if it is even until `n` is greater
than or equal to 10.

Here is a slightly different statement:

```python
>>> n = 0
>>> while n < 6:
...    n += 1
>>> if n % 2 == 0:
...    print(n)
6

```

# While loops

So far, we have mainly used `while` loops to repeat an action whilst
incrementing a given variable. In fact `while` loops can be used to repeat
actions until **any** boolean condition is no longer true.

In the next lab session we will see the use of our first 'library'. These are
parts of python that can be loaded in and used as necessary. To illustrate the
above point we're going to make use of the `random` library which can be used to
get random numbers.

```python
>>> import random
>>> random_number = random.randint(1, 6)
```

The variable `random_number` will be a random integer between 1 and 6.

So we can now use that in conjunction with a `while` loop to simulate rolling a
dice until we get a 6:

```python
>>> number_of_rolls = 1
>>> while random.randint(1, 6) != 6:
...     number_of_rolls += 1

```

The variable `number_of_rolls` increments each time we do not 'roll' a six. Take
a look at the variable, it will be different every time the above code is run.

# Debugging

# Crashing jupyter
