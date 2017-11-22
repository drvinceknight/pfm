---
layout     : post
categories : 2017-2018
title      : "2017-2018: Handout 09 - Plotting symbolic functions numerically"
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

Using Sympy to carry out symbolic operations relevant to calculus.

## Plotting with matplotlib

We can also plot this directly in matplotlib. There are advantages to this as
matplotlib is very flexible.

```python
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> def f(x):
...    return 1 / x
>>>    xs = np.linspace(-1, 1, 200)
>>>    ys = [f(x) for x in xs]
>>>    plt.plot(xs, ys, label="$y=\\frac{1}{x}$")
>>>    plt.plot(xs, xs, label="$y=x$")
>>>    plt.ylim(-10, 10)
>>>    plt.legend();

```

This is just an alternative way. Feel free to plot directly with Sympy if you
prefer.

## Assistance with your project

If you would like some assistance with your project, feel free to arrange to
come and see me.
