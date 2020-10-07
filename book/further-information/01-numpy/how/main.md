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

# How

`numpy` is a large library with incredible functionality all of which will not be
listed here. Instead some specific tools will be described so as to give a
sufficient understanding of the capabilities of the library.

## How to create an array

To create a `numpy` array we use the `numpy.array` tool which takes any iterable.

````{tip}
```
numpy.array(iterable)
```
````

For example:

```{code-cell} ipython3
import numpy as np

array = np.array((0, 12, 3, 1))
array
```

## How to create a given number of values between two bounds

`numpy` has a popular tool to create a linear space: `numpy.linspace` which take
a lower bound, an upper bounds and a number. It returns the given number of points
uniformly spaced between the bounds.

````{tip}
```
numpy.linspace(lower_bound, upper_bound, number)
```
````

For example:

```{code-cell} ipython3
import numpy as np

np.linspace(10, 400, 4)
```

## How to create an array of zeros

To create an array of zeros we can use the `numpy.zeros` tool. It takes an
argument for the dimension of the array. This can either be a single number in
which case a single dimensional array is created or a tuple with multiple
dimensions.

````{tip}
```
numpy.zeros(size)
```
````

For example:

```{code-cell} ipython3
import numpy as np

np.zeros(4)
```


Or:

```{code-cell} ipython3
np.zeros((3, 5))
```

## How to generate random arrays

`numpy` has a powerful random number generator. It can be accessed from
`numpy.random` and has multiple tools. The simplest of which is
`numpy.random.random`. This takes an optional argument that is the dimension of
the array.

````{tip}
```
numpy.random.random(size)
```
````

For example:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

import numpy as np

np.random.random()
```

Or:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

import numpy as np

np.random.random((3, 5))
```

## How to index arrays

Multiple dimensional arrays can be indexed in a natural mathematical way using
`array[position]`.

````{tip}
```
array[position]
```
````

For example:

```{code-cell} ipython3
import numpy as np

array = np.array(((1, 2, 3), (4, 5, 6)))
array[1, 2]
```

## How to do arithmetic on arrays

It is possible to directly do arithmetic on arrays in a mathematical way.

````{tip}
```
array1 + array2
```
````

For example to do element wise multiplication:

```{code-cell} ipython3
array1 = np.array((1, 2, 3, 4))
array2 = np.array((2, 0, -1, 0.5))
array1 * array2
```

## How to invert a matrix

`numpy` can invert a matrix using `np.linalg.inv`. There are numerous other
linear algebraic tools available in `np.linalg`.

````{tip}
```
np.linalg.inv(array)
```
````

For example:

```{code-cell} ipython3
import numpy as np

matrix = np.array(((1, 2), (3, 1)))
matrix_inverse = np.linalg.inv(matrix)
matrix_inverse
```

We can confirm the expected result:

```{code-cell} ipython3
matrix @ matrix_inverse
```

## How to raise a matrix to a power

Using the usual operator for exponentiation `**` with a `numpy` array carries
out element wise exponentiation. To raise a matrix to a power we use
`np.linalg.matrix_power`. This takes an array and the exponent.

````{tip}
```
np.linalg.ing(array, exponent)
```
````

For example:

```{code-cell} ipython3
import numpy as np

matrix = np.array(((1, 2), (3, 1)))
np.linalg.matrix_power(matrix, 3)
```

## How to fit a line of best fit

`numpy` can be used to fit polynomials to a points. This is done with the
`numpy.polyfit` tool. This takes an array of x values, an array of y values and
a degree. It returns the coefficients of a polynomial of given degree that best
approximates $f(x)=y$.

````{tip}
```
np.polyfit(x, y, degree)
```
````

For example, the code below creates `y` using a quadratic and recovers the
coefficients of the quadratic:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

x = np.array((1, 2, 3, 4))
y = 2 * x ** 2 + 3 * x + 1
a, b, c = np.polyfit(x, y, 2)
a, b, c
```
