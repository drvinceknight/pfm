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

## Question 1

> `1`. For each of the following sets of data:

>      Calculate:

>      - The mean,
>      - The median,
>      - The max,
>      - The min,
>      - The population standard deviation,
>      - The sample standard deviation,
>      - The population variance,
>      - The sample variance,
>      - The quartiles (the set of $n=4$ quantiles),
>      - The deciles (the set of $n=10$ quantiles),
>
> `1`. `data_set_1 = (...)

```{code-cell} ipython3
import statistics as stat

data_set_1 = (
    74,
    -7,
    58,
    82,
    60,
    3,
    49,
    85,
    24,
    99,
    73,
    76,
    11,
    -4,
    61,
    87,
    93,
    13,
    1,
    28,
)
```

> - The mean,

```{code-cell} ipython3
stat.mean(data_set_1)
```

> - The median,

```{code-cell} ipython3
stat.median(data_set_1)
```

> - The max,

```{code-cell} ipython3
max(data_set_1)
```

> - The min,

```{code-cell} ipython3
min(data_set_1)
```

> - The population standard deviation,

```{code-cell} ipython3
stat.pstdev(data_set_1)
```

> - The sample standard deviation,

```{code-cell} ipython3
stat.stdev(data_set_1)
```

> - The population variance,

```{code-cell} ipython3
stat.pvariance(data_set_1)
```

> - The sample variance,

```{code-cell} ipython3
stat.variance(data_set_1)
```

> - The quartiles (the set of $n=4$ quantiles),

```{code-cell} ipython3
stat.quantiles(data_set_1, n=4)
```

> - The deciles (the set of $n=10$ quantiles),

```{code-cell} ipython3
stat.quantiles(data_set_1, n=10)
```

> `2`. `data_set_2 = (...)

```{code-cell} ipython3
import statistics as stat

data_set_2 = (
    65,
    59,
    81,
    81,
    76,
    93,
    91,
    88,
    55,
    97,
    86,
    94,
    79,
    54,
    63,
    56,
    58,
    77,
    85,
    88,
)
```

> - The mean,

```{code-cell} ipython3
stat.mean(data_set_2)
```

> - The median,

```{code-cell} ipython3
stat.median(data_set_2)
```

> - The max,

```{code-cell} ipython3
max(data_set_2)
```

> - The min,

```{code-cell} ipython3
min(data_set_2)
```

> - The population standard deviation,

```{code-cell} ipython3
stat.pstdev(data_set_2)
```

> - The sample standard deviation,

```{code-cell} ipython3
stat.stdev(data_set_2)
```

> - The population variance,

```{code-cell} ipython3
stat.pvariance(data_set_2)
```

> - The sample variance,

```{code-cell} ipython3
stat.variance(data_set_2)
```

> - The quartiles (the set of $n=4$ quantiles),

```{code-cell} ipython3
stat.quantiles(data_set_2, n=4)
```

> - The deciles (the set of $n=10$ quantiles),

```{code-cell} ipython3
stat.quantiles(data_set_2, n=10)
```

> `3`. `data_set_3 = (...)

```{code-cell} ipython3
import statistics as stat

data_set_3 = (
    0.31,
    -0.13,
    0.19,
    0.46,
    -0.27,
    -0.06,
    0.20,
    0.42,
    -0.07,
    0.11,
    -0.11,
    -0.43,
    -0.36,
    0.45,
    -0.42,
    0.11,
    0.08,
    0.31,
    0.48,
    0.17,
)
```

> - The mean,

```{code-cell} ipython3
stat.mean(data_set_3)
```

> - The median,

```{code-cell} ipython3
stat.median(data_set_3)
```

> - The max,

```{code-cell} ipython3
max(data_set_3)
```

> - The min,

```{code-cell} ipython3
min(data_set_3)
```

> - The population standard deviation,

```{code-cell} ipython3
stat.pstdev(data_set_3)
```

> - The sample standard deviation,

```{code-cell} ipython3
stat.stdev(data_set_3)
```

> - The population variance,

```{code-cell} ipython3
stat.pvariance(data_set_3)
```

> - The sample variance,

```{code-cell} ipython3
stat.variance(data_set_3)
```

> - The quartiles (the set of $n=4$ quantiles),

```{code-cell} ipython3
stat.quantiles(data_set_3, n=4)
```

> - The deciles (the set of $n=10$ quantiles),

```{code-cell} ipython3
stat.quantiles(data_set_3, n=10)
```

> `4`. `data_set_4 = (...)

```{code-cell} ipython3
import statistics as stat

data_set_4 = (
    2,
    4,
    2,
    2,
    2,
    2,
    2,
    3,
    2,
    2,
    2,
    4,
    2,
    4,
    2,
    2,
    3,
    4,
    3,
    4,
)
```

> - The mean,

```{code-cell} ipython3
stat.mean(data_set_4)
```

> - The median,

```{code-cell} ipython3
stat.median(data_set_4)
```

> - The max,

```{code-cell} ipython3
max(data_set_4)
```

> - The min,

```{code-cell} ipython3
min(data_set_4)
```

> - The population standard deviation,

```{code-cell} ipython3
stat.pstdev(data_set_4)
```

> - The sample standard deviation,

```{code-cell} ipython3
stat.stdev(data_set_4)
```

> - The population variance,

```{code-cell} ipython3
stat.pvariance(data_set_4)
```

> - The sample variance,

```{code-cell} ipython3
stat.variance(data_set_4)
```

> - The quartiles (the set of $n=4$ quantiles),

```{code-cell} ipython3
stat.quantiles(data_set_4, n=4)
```

> - The deciles (the set of $n=10$ quantiles),

```{code-cell} ipython3
stat.quantiles(data_set_4, n=10)
```

> `2`. Calculate the sample covariance and the correlation coefficient for the
> following pairs of data sets from question 1:

> `1`. `data_set_1` and `data_set_4`

```{code-cell} ipython3
stat.covariance(data_set_1, data_set_4)
```

```{code-cell} ipython3
stat.correlation(data_set_1, data_set_4)
```

> `2`. `data_set_3` and `data_set_4`

```{code-cell} ipython3
stat.covariance(data_set_3, data_set_4)
```

```{code-cell} ipython3
stat.correlation(data_set_3, data_set_4)
```

> `3`. `data_set_2` and `data_set_3`

```{code-cell} ipython3
stat.covariance(data_set_2, data_set_3)
```

```{code-cell} ipython3
stat.correlation(data_set_2, data_set_3)
```

> `4`. `data_set_1` and `data_set_2`

```{code-cell} ipython3
stat.covariance(data_set_1, data_set_2)
```

```{code-cell} ipython3
stat.correlation(data_set_1, data_set_2)
```

> `3`. For each of the data sets from question 1 obtain the covariance and
> correlation coefficient for the data set with itself.

> `1`. `data_set_1 = (...)

```{code-cell} ipython3
stat.covariance(data_set_1, data_set_1)
```

```{code-cell} ipython3
stat.correlation(data_set_1, data_set_1)
```

> `2`. `data_set_2 = (...)

```{code-cell} ipython3
stat.covariance(data_set_2, data_set_2)
```

```{code-cell} ipython3
stat.correlation(data_set_2, data_set_2)
```

> `3`. `data_set_3 = (...)

```{code-cell} ipython3
stat.covariance(data_set_3, data_set_3)
```

```{code-cell} ipython3
stat.correlation(data_set_3, data_set_3)
```

> `4`. `data_set_4 = (...)

```{code-cell} ipython3
stat.covariance(data_set_4, data_set_4)
```

```{code-cell} ipython3
stat.correlation(data_set_4, data_set_4)
```

> `4`. Obtain a line of best fit for the pairs of data sets from question 2.

> `1`. `data_set_1` and `data_set_4`

```{code-cell} ipython3
stat.linear_regression(data_set_1, data_set_4)
```

> `2`. `data_set_3` and `data_set_4`

```{code-cell} ipython3
stat.linear_regression(data_set_3, data_set_4)
```

> `3`. `data_set_2` and `data_set_3`

```{code-cell} ipython3
stat.linear_regression(data_set_2, data_set_3)
```

> `4`. `data_set_1` and `data_set_2`

```{code-cell} ipython3
stat.linear_regression(data_set_1, data_set_2)
```
