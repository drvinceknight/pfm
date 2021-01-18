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

# Solutions

> Write documentation for the `statistics.py` file written in the exercises of
> [Modularisation Exercises](modularisation_exercises).

````md

# Stats

Functionality for basic statistical operations.

## Tutorial

In this tutorial we will see how to use `stats.py` to compute the mean and
population variance of the following set of data:

```
x = (1, 2, 3, 1, 1, 1, 2, 3, 54, 5, 6, 70, 10, 12, 10)
```

First we import the library:


```python
import stats
```

Next let us define the data:

```python
x = (1, 2, 3, 1, 1, 1, 2, 3, 54, 5, 6, 70, 10, 12, 10)
```

To view the mean we use `stats.get_mean`:

```python
stats.get_mean(x)
```

To view the population variance we use `stats.get_population_variance`:

```python
stats.get_population_variance(x)
```

## How to guide

### How to compute a mean

To compute a mean we use `stats.get_mean`:

```python
import stats

stats.get_mean((1, 2, 3, 4))
```

### How to compute population variance

To compute a mean we use `stats.get_population_variance`:

```python
import stats

stats.get_population_variance((1, 2, 3, 4))
```

## Explanation

The mean is calculated using the following formula:

$$
 \bar x \frac{\sum_{i=1}^{N} x_i}{N}
$$


The population variance is defined by:

$$
 \sigma ^ 2 = \frac{\sum_{i=1}^{N} (x_i - \bar x) ^ 2}{N}
$$

Note that the population variance differs from the sample variance.

## Reference

### List of functionality

The following functions are written in `absorption`:

- `get_mean`
- `get_population_variance`

### Bibliography

The wikipedia page on the mean and population variance gives a good overview of the
topic:

- Mean: <https://en.wikipedia.org/wiki/Mean#Arithmetic_Mean_(AM)>
- Population variance: <https://en.wikipedia.org/wiki/Variance#Population_variance>

This introductory statistics text book is recommended reading:

> Ross, Sheldon M. Introductory statistics. Academic Press, 2017.

````
