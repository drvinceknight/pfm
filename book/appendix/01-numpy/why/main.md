---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Why

## What is the difference between an array and other Python iterables?

Other iterables seen in this book so far include python lists and tuples. As
described in
{ref}`difference_between_a_list_and_a_tuple`
the difference between a list and a tuple is that a tuple is immutable: so that
it cannot be changed in place whereas a list can.

An array, in general in other languages, and in particular a `numpy` array is
mutable **but** one of the main differences is that all types of variables
inside the array must be the same. This is not the case for lists or arrays. As
an example consider the following collections of two types of variables (a `str`
and an `int`):

```{code-cell} ipython3
collection_as_tuple = ("dog", 3)
collection_as_tuple
```

```{code-cell} ipython3
collection_as_list = ["dog", 3]
collection_as_list
```

```{code-cell} ipython3
import numpy as np

collection_as_array = np.array(("dog", 3))
collection_as_array
```

This has in fact changed the integer value and stored it as a string.

## Why is Numpy computationally efficient?

Python is essentially two things:

- A language;
- An interpreter that takes the language and carries out the instructions.

That Interpreter is written in another programming language: specifically the
programming language [C](https://en.wikipedia.org/wiki/C_(programming_language).
C is a compiled language which means that there is an extra step to running C
code: after it has been written, it has to be compiled to something that the
computer can understand which is when it is run.

Python however is not a compiled language: it is an interpreted language. This
makes it faster to write and debug but slower for to run.

Numpy has a number of
[vectorized](https://en.wikipedia.org/wiki/Array_programming) functionalities
that essentially let Python speak more directly to C. Which is why it is fast.

Some example of this include using the `numpy.max` function over the standard
library `max` function.

```{code-cell} ipython3
:tags: [style-check-ignore, nbval-ignore-output]

import numpy as np

np.random.seed(0)
big_array = np.random.random(10 ** 7)
%timeit np.max(big_array)
```

```{code-cell} ipython3
:tags: [style-check-ignore, nbval-ignore-output]

import numpy as np

np.random.seed(0)
big_array = np.random.random(10 ** 7)
%timeit max(big_array)
```

Some further information on this includes:

- The wikipedia page for array programming to gain a general understanding of
  vectorized functionality: <https://en.wikipedia.org/wiki/Array_programming>
- This blog post has a number of other experiments but also some brief
  explanations: <https://www.geeksforgeeks.org/why-numpy-is-faster-in-python/>

## Where can I find more information on Numpy?

`numpy` is a fundamental building block to the scientific python ecosystem. There
is are a lot of resources available:

- The scipy-lecture notes: <https://scipy-lectures.org/intro/numpy/index.html>
- The `numpy` documentation has a good tutorial:
  <https://numpy.org/devdocs/user/quickstart.html>
