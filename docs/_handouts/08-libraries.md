---
layout     : post
categories : 2017-2018
title      : "2017-2018: Handout 08 - Libraries."
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

Using Sympy to carry out symbolic mathematics calculations.

## Libraries

Python has various libraries that comes as standard (`import math`, `import
random` etc). With Anaconda, there are a number of other scientific libraries
readily available to you (`import sympy`, `import numpy` etc...).

There are however a **huge** number of libraries that are not included with
Anaconda but that are readily available to you (this is one of the strengths of
Python).

To install them you can write a simple command at the command line of your
computer:

- On Mac OSX: look for "terminal";
- On Windows: look for "anaconda prompt".

Once there simply type:

```bash
pip install <package-name>
```

Note that if you're on a university computer you need to type:

```bash
pip install --user <package-name>
```

For example, if you wanted to study queues, you could use a package called `ciw`
which is actually written by a Cardiff University PhD student ([Geraint
Palmer](http://www.geraintianpalmer.org.uk/)). To install this you'd run:

```bash
pip install ciw
```

To use it you'd take a look at the documentation which is here:
[ciw.readthedocs.org/](http://ciw.readthedocs.org/).

There are numerous libraries that exist in Python, depending on what you're
working on they might be helpful.

## Data analysis with Pandas

Some of you have mentioned that you want to do some statistical analysis of some
data. The Python library for doing this is [Pandas](http://pandas.pydata.org).
The main tool used in Pandas is something called a "dataframe". Let us create a
data frame from scratch:


```python
>>> import pandas as pd
>>> names = ["Zoe", "Geraint", "Nikoleta", "Henry", "Vince"]
>>> places_of_birth = ["Wales", "Wales", "Greece", "England", float("NaN")]
>>> df = pd.DataFrame({"Names": names, "Birthplace": places_of_birth})
>>> df
  Birthplace     Names
0      Wales       Zoe
1      Wales   Geraint
2     Greece  Nikoleta
3    England     Henry
4        NaN     Vince

```

Pandas has a lot of powerful features for analysis data and of course can be
used to read in a data file without having to enter it by hand. For example,
let's read `primes.csv`
([download](http://vknight.org/cfm/assets/data/primes.csv)):

```python
>>> df = df = pd.read_csv("http://vknight.org/cfm/assets/data/primes.csv",
...                        header=None, names=["Prime"])
>>> df.head()
   Prime
0      2
1      3
2      5
3      7
4     11
>>> df["Prime"].mean()

```

This just touches the surface of what can be done. Here are two other resources:

- A short tutorial [github.com/drvinceknight/Python-Mathematics-Handbook/blob/master/nbs/03-Data-analysis-with-Pandas.ipynb](https://github.com/drvinceknight/Python-Mathematics-Handbook/blob/master/nbs/03-Data-analysis-with-Pandas.ipynb)
- A slightly longer tutorial
  [pandas.pydata.org/pandas-docs/stable/10min.html](https://pandas.pydata.org/pandas-docs/stable/10min.html)

## Plotting with matplotlib

The library most used for plotting with Python is called matplotlib.

To make plots appear in a Jupyter notebook you need to run the following
command:

```
%matplotlib inline
```

After that you can use matplotlib to plot various types of plots. For example,
here is the code to create simple scatter plot:

```python
>>> import matplotlib.pyplot as plt
>>> x = [1, 5, 2]
>>> y = [3, -2, 2]
>>> plt.scatter(x, y)

```

We will see (in the next lab sheet) how to use a simple wrapper of `matplotlib`
in SymPy but if you want/need to find out more about how to directly use `matplotlib`
these might be helpful:

- A short tutorial
  [github.com/drvinceknight/Python-Mathematics-Handbook/blob/master/nbs/04-Visualisation-with-matplotlib.ipynb](https://github.com/drvinceknight/Python-Mathematics-Handbook/blob/master/nbs/04-Visualisation-with-matplotlib.ipynb)
- A slightly longer tutorial that goes in depth in to how matplotlib works
  [pbpython.com/effective-matplotlib.html](http://pbpython.com/effective-matplotlib.html)
