---
layout     : post
categories : 2017-2018
title      : "2017-2018: Handout 11 - is close and including code in LaTeX and machine learning"
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1300-1500**

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

## Machine learning

One of Python's most popular libraries is called scikit-learn. This is a popular
machine learning library. (It's included in Anaconda).

Here is a simple example of using something called "unsupervised learning". It's
an algorithm called k-means which allows us to take data and cluster it.

Let us create some random data:

```python
>>> import random
>>> import matplotlib.pyplot as plt
>>> import pandas as pd
>>> random.seed(0)
>>> N = 10000
>>> xs = [(.1 + random.random()) * (-1) ** random.choice([1, 2]) for _ in range(N)]
>>> ys = [(.1 + random.random()) * (-1) ** random.choice([1, 2]) for _ in range(N)]
>>> df = pd.DataFrame({"x": xs, "y": ys})
>>> df.head()
          x         y
0  0.944422  0.859947
1  0.140484  0.366374
2  0.504934  0.174009
3  1.067800 -0.599188
4 -0.683382  0.400789

```

This creates 4 quadrants ("clusters") of data:

```python
>>> plt.scatter(df["x"], df["y"]);

```

That's not a hard conclusion for a human to arrive at, *but* as the dimension
size of the data increases it might become more difficult. So we can use machine
learning. Let us use the scikit learn library:

```python
>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(n_clusters=4).fit(df)
>>> df["cluster"] = kmeans.labels_
>>> df.head()
          x         y  cluster
0  0.944422  0.859947        3
1  0.140484  0.366374        3
2  0.504934  0.174009        3
3  1.067800 -0.599188        2
4 -0.683382  0.400789        0

```

Let us plot this and specify the color of the points needs to be the cluster:

```python
>>> plt.scatter(df["x"], df["y"], c=df["cluster"]);

```

This is one of the simpler examples of what machine learning is but you might be
interested in reading more here:

- [www.scipy-lectures.org/packages/scikit-learn/index.html](http://www.scipy-lectures.org/packages/scikit-learn/index.html)
- [scikit-learn.org](http://scikit-learn.org)
- [www.kaggle.com/competitions](https://www.kaggle.com/competitions)
- [Predicting the weather using linear
  regression](http://stackabuse.com/using-machine-learning-to-predict-the-weather-part-2/?utm_content=buffer34689&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer)
