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

# Tutorial

We will solve the following problem using a computer to do some of the more
tedious calculations.

````{admonition} Problem

Anna is investigating the relationship between exercise and resting heart rate.
She takes a random sample of 19 people in her year group and records for each person

- their resting heart rate, $h$ beats per minute.
- the number of minutes, $m$, spent exercising each week.

A table with the data is here:

```{list-table} Collected data from Anna's year group.
:header-rows: 1

* - h
  - m
* - 76.0
  - 5
* - 72.0
  - 5
* - 71.0
  - 21
* - 74.0
  - 30
* - 71.0
  - 42
* - 69.0
  - 20
* - 68.0
  - 20
* - 68.0
  - 35
* - 66
  - 80.0
* - 64
  - 120.0
* - 65
  - 140.0
* - 63
  - 180.0
* - 63
  - 205.0
* - 62
  - 225.0
* - 65
  - 237.0
* - 63
  - 280.0
* - 65
  - 300.0
* - 64
  - 356.0
* - 64
  - 360.0
```

You can see a scatter plot below.

1. For all collected values of $h$ and $m$ obtain:

    - The mean
    - The median
    - The quartiles
    - The standard deviation
    - The variation
    - The maximum
    - The minimum

2. Obtain the Pearson Coefficient of correlation for the variables $h$ and $m$.
3. Obtain the line of best fit for variables $x$ and $y$ as
   defined by:

   $$x=\ln(m)\qquad y=\ln(h)$$

4. Using the above obtain a relationship between $m$ and $h$ of the form:

   $$h=cm^k$$
````

```{code-cell} ipython3
:tags: ["remove-input", "style-check-ignore", "nbval-ignore-output"]

import matplotlib.pyplot as plt

h_data = (
    76.0,
    72.0,
    71.0,
    74.0,
    71.0,
    69.0,
    68.0,
    68.0,
    66.0,
    64.0,
    65.0,
    63.0,
    63.0,
    62.0,
    65.0,
    63.0,
    65.0,
    64.0,
    64.0,
)
m_data = (
    5,
    5,
    21,
    30,
    42,
    20,
    20,
    35,
    80,
    120,
    140,
    180,
    205,
    225,
    237,
    280,
    300,
    356,
    360,
)

plt.figure()
plt.scatter(x=m_data, y=h_data)
plt.xlabel("Minutes of exercise: $m$")
plt.ylabel("Resting heart rate: $h$")
plt.title("Data collected by Anne");
```

Let us start by inputting all the data:

```{code-cell} ipython3
h = (
    76.0,
    72.0,
    71.0,
    74.0,
    71.0,
    69.0,
    68.0,
    68.0,
    66.0,
    64.0,
    65.0,
    63.0,
    63.0,
    62.0,
    65.0,
    63.0,
    65.0,
    64.0,
    64.0,
)
m = (
    5,
    5,
    21,
    30,
    42,
    20,
    20,
    35,
    80,
    120,
    140,
    180,
    205,
    225,
    237,
    280,
    300,
    356,
    360,
)
```

The main tool we are going to use for this is `statistics`.

```{code-cell} ipython3
import statistics as st
```

To calculate the mean:

```{code-cell} ipython3
st.mean(h)
```

```{code-cell} ipython3
st.mean(m)
```

To calculate the median:

```{code-cell} ipython3
st.median(h)
```

```{code-cell} ipython3
st.median(m)
```

To calculate the quartiles, we use `statistics.quantiles` and specify that we
want to separate the date in to $n=4$ quarters.

```{code-cell} ipython3
st.quantiles(h, n=4)
```

```{code-cell} ipython3
st.quantiles(m, n=4)
```

Note that this calculation confirms the median which corresponds to the 50%
quartile.

To calculate the sample standard deviation:

```{code-cell} ipython3
st.stdev(h)
```

```{code-cell} ipython3
st.stdev(m)
```

To calculate the sample variance:

```{code-cell} ipython3
st.variance(h)
```

```{code-cell} ipython3
st.variance(m)
```

To compute that maximum:

```{code-cell} ipython3
max(h)
```

```{code-cell} ipython3
max(m)
```

To compute the minimum:

```{code-cell} ipython3
min(h)
```

```{code-cell} ipython3
min(m)
```

In order to compute the Pearson Coefficient of correlation we use
`statistics.correlation`:

```{code-cell} ipython3
st.correlation(h, m)
```

This negative value indicates a negative correlation between $h$ and $m$,
indicating that the more you exercise the lower your heart rate is likely to be.

To calculate the line of best fit for the transformed variables we need to first
create them. We will do this using a list comprehension. As we are doing
everything numerically, we will use `math.log` which by default computes the
natural logarithm:

```{code-cell} ipython3
import math
x = [math.log(value) for value in m]
y = [math.log(value) for value in h]
```

Now to compute the line of best fit we will use `statistics.linear_regression`:

```{code-cell} ipython3
slope, intercept = st.linear_regression(x, y)
```

The slope is:

```{code-cell} ipython3
slope
```

The intercept is:

```{code-cell} ipython3
intercept
```

If we recall the transformation of the variables:

$$x=\ln(m)\qquad y=\ln(h)$$

We now have the relationship:

$$y=ax + b$$

Where $a$ corresponds to the `slope` and $b$ corresponds to the `intercept`.

The question was asking for a relationship between $m$ and $h$ of the form:

$$h=cm^k$$

We can use `sympy` to manipulate the expressions:

```{code-cell} ipython3
import sympy as sym

h = sym.Symbol("h")
m = sym.Symbol("m")
a = sym.Symbol("a")
b = sym.Symbol("b")
x = sym.ln(m)
y = sym.ln(h)
```

A general line of best fit for $x$ and $y$ can be expressed in terms of $m$ and
$h$:

```{code-cell} ipython3
line = sym.Eq(lhs=y, rhs=a * x + b)
line
```

Taking the exponential of both sides gives the required relationship:

```{code-cell} ipython3
sym.exp(line.lhs)
```

```{code-cell} ipython3
sym.expand(sym.exp(line.rhs))
```

Which can be rewritten as:

$$
e^bm^a
$$

Substituting our values for the `slope` and `intercept` in to these expressions
gives the required relationship:

```{code-cell} ipython3
sym.exp(line.rhs).subs({a: slope, b: intercept})
```

Below is a plot that shows this relationship:

```{code-cell} ipython3
:tags: ["remove-input", "style-check-ignore", "nbval-ignore-output"]

import matplotlib.pyplot as plt
import numpy as np

m_range = np.linspace(np.min(m_data), np.max(m_data), 100)
relationship_image = np.exp(intercept) * m_range ** (slope)

plt.figure()
plt.scatter(x=m_data, y=h_data)
plt.plot(m_range, relationship_image, color="black")
plt.xlabel("Minutes of exercise: $m$")
plt.ylabel("Resting heart rate: $h$")
plt.title(f"Data collected by Anne with fitted relationship: $h={np.exp(intercept):.2f}m^{{{slope:.2f}}}$");
```

```{important}
In this tutorial we have

- Calulated values of central tendency and spread
- Calculated some bivariate coefficients
- Fitted a line of best fit
```
