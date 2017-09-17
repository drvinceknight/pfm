---
layout     : post
categories : 2016-2017
title      : "2016-2017: Handout 09 - is close and including code in LaTeX."
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1400-1600**

## What you have learnt this week:

Using numpy to carry out linear algebraic calculations.

## Numerical approximation

Some of you carried out the following calculation and noticed that something
wasn't quite right:

```python
>>> import numpy as np
>>> A = np.matrix([[1, 2, 4], [5, 3, 1], [5, 1, 8]])
>>> Ainv = np.linalg.inv(A)
>>> b = np.matrix([[1], [2], [3]])
>>> np.array_equal(Ainv * b, np.linalg.solve(A, b))
False

```

However:

```python
>>> Ainv * b
matrix([[ 0.35632184],
        [ 0.02298851],
        [ 0.14942529]])
>>> np.linalg.solve(A, b)
matrix([[ 0.35632184],
        [ 0.02298851],
        [ 0.14942529]])

```

This is due to **numerical error** which is a normal process when dealing with
numerical calculations.

We can however check for equality with a **tolerance** for numerical error:

```python
>>> np.isclose(Ainv * b, np.linalg.solve(A, b))
matrix([[ True],
        [ True],
        [ True]], dtype=bool)

```

## Including code in LaTeX

There are various ways to include code in LaTeX documents, one of the nicest is
to use the
[minted](https://www.sharelatex.com/learn/Code_Highlighting_with_minted)
library, however this might not work on all systems (it works fine on overleaf).
The simplest approach is to use the listings package like in the [model
solution](http://goo.gl/ly8fdG). Here is a small example:

```latex
\documentclass{article}

\usepackage{listings}

\begin{document}
Here is some amazing code:

\begin{lstlisting}[language=python]
for i in range(20):
    print(i)
\end{lstlisting}

\end{document}
```

## Searching for LaTeX commands

Keep in mind that overleaf, texworks, cloud.sagemath are just interfaces to
LaTeX, so when searching for how to do things don't include those terms. For
example search for "how to change margin size in LaTeX" and **not** "how to
change margin size in overleaf".

## Page limit

3 pages is a *strict* **upper** limit.

## Ideas

Most of you have come up with great ideas for your projects, **if** you are
still looking for inspiration, here are some blog posts I have written that
might be of interest:

- Game Theory and Christmas: [vknight.org/unpeudemath/code/2015/12/15/The-Prisoners-Dilemma-of-Christmas-Gifts.html](http://vknight.org/unpeudemath/code/2015/12/15/The-Prisoners-Dilemma-of-Christmas-Gifts.html)
- Jokes: [knight.org/unpeudemath/code/2015/06/14/natural-language-and-predicting-funny.html](http://vknight.org/unpeudemath/code/2015/06/14/natural-language-and-predicting-funny.html)
- Twitter: [vknight.org/unpeudemath/code/2016/03/31/Analyzing-my-own-twitter-network-using-python.html](http://vknight.org/unpeudemath/code/2016/03/31/Analyzing-my-own-twitter-network-using-python.html)
- Queues: [vknight.org/unpeudemath/mathematics/2016/10/29/anscombes-quartet-variability-and-ciw.html](http://vknight.org/unpeudemath/mathematics/2016/10/29/anscombes-quartet-variability-and-ciw.html)
