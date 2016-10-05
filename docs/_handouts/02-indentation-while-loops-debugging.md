---
layout     : post
categories : 2016-2017
title      : "2016-2017: Indentation, while loops, debugging (and crashing
Jupyter)"
comments   : true
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

## Housekeeping

You should watch **and listen** to the videos. These are there to help and offer
an initial explanation of the work. They are the equivalent of the lecture.

Some students have been confused by the `>>>` on the lab sheets which do not
appear in the videos. In the lab sheets and handouts, is important these are
just there so that you can see the difference between the input and outputs.
When you type the code you do not need to type the `>>>`.

Some of you have been showing me code on the chat channel. To make it easier to
read try and surround it in between 3 ticks: `. You can read more about
formatting markdown here:
[gitter.zendesk.com/hc/en-us/articles/200176682-Markdown-basics](https://gitter.zendesk.com/hc/en-us/articles/200176682-Markdown-basics)

## Indentation is important in Python

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

## While loops

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

When you get errors in your code, look at the last message in the print out.
For example. Something the following is saying that somewhere in the code ran
there was a `:` missing at the end of the `if n == 4` statement.

```python
Exception raised:
    Traceback (most recent call last):
      File "/Users/vince/anaconda/lib/python3.5/doctest.py", line 1321, in __run
        compileflags, 1), test.globs)
      File "<doctest 02-indentation-while-loops-debugging.md[10]>", line 1
        if n == 4
                ^
    SyntaxError: invalid syntax
```

Also, as described in the [debugging
video](https://www.youtube.com/watch?v=NvAEDqMRSEw&feature=youtu.be), it is
often useful to incorporate `print` statements throughout your code to
understand what some values are at given points in time.

## Crashing jupyter

It is possible that whilst coding you create an **infinite loop**. For example
the following will never complete:

```
n = 0
while True:
    n += 1
    print(n)
```

You can see that python is working because the circle in the top right will be
solid/filled in.  To stop such a loop, go to `Kernel` on the menu bar of your
notebook:

- Click on interrupt,
- If that's not enough click on restart kernel,

Finally, if both of those don't work, you might need to restart the server all
together.
