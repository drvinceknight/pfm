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

## How to draw a scatter plot

We use the `matplotlib.pyplot.scatter` tool. This takes two iterables as
arguments: one for the first dimension and one for the other dimension.

````{tip}
```
import matplotlib.pyplot as plt

plt.figure()
plt.scatter(x, y)
```
````

Here is an example:

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

import matplotlib.pyplot as plt
import numpy as np

x = np.array((1, 2, 3, 4, 5))
y = np.array((-1, -2, 4, -1, 7))
plt.figure()
plt.scatter(x, y);
```

## How to plot a function

We use the `matplotlib.pyplot.plot` tool. Similarly to
`matplotlib.pyplot.scatter` this takes two iterables. It plots a line plot. To
plot a function we use this an generate the required data.

````{tip}
```
import matplotlib.pyplot as plt

plt.figure()
plt.plot(x, y)
```
````

Here is an example of how we would plot $f(x)=x ^ 2 + 3x + 1$:

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-40, 40, 1000)
y = x ** 2 + 3 * x + 1
plt.figure()
plt.plot(x, y);
```

## How to combine plots

To combine plots they can be included one after the other after the
`matplotlib.pyplot.figure` call.

````{tip}
```
import matplotlib.pyplot as plt

plt.figure()
plt.plot(x, y)
plt.scatter(x, y)
```
````

For example the following will draw two different functions $f(x) = cos(x)$ and
$g(x)=sin(x)$ (we include an argument to plot $g$ in red):

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
f = np.cos(x)
g = np.sin(x)
plt.figure()
plt.plot(x, f)
plt.plot(x, g, color="red");
```

## How to add a title

To add a title we use `matplotlib.pyplot.title` which takes a string.

````{tip}
```
import matplotlib.pyplot as plt

plt.figure()
plt.title(label)
```
````

Here we add a title to a plot of $cos(x)$:

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
f = np.cos(x)
plt.figure()
plt.plot(x, f)
plt.title("Plot of cos(x)");
```

We can include LaTeX inside of `$` signs to render mathematics:

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
f = np.cos(x)
plt.figure()
plt.plot(x, f)
plt.title("Plot of $\cos(x)$");
```

## How to add axes labels

To add labels we use `matplotlib.pyplot.xlabel` or `matplotlib.pyplot.ylabel`.
These both take a string.

````{tip}
```
import matplotlib.pyplot as plt

plt.figure()
plt.xlabel(label)
plt.ylabel(label)
```
````

Here is an example:

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
f = np.cos(x)
plt.figure()
plt.plot(x, f)
plt.xlabel("$x$")
plt.ylabel("$y$");
```

## How to add a legend

When plotting multiple plots it can be helpful to include a legend. We do this
by passing a `label` to the specific plot as a string. The legend then also need
to be specified, that is done with `matpltlib.pyplot.legend`.

````{tip}
```
import matplotlib.pyplot as plt

plt.figure()
plt.scatter(x, y, label)
plt.legend()
```
````

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
f = np.cos(x)
g = np.sin(x)
plt.figure()
plt.plot(x, f, label="$cos(x)$")
plt.plot(x, g, label="$sin(x)$", color="red")
plt.legend();
```

## How to save a plot

To save a plot to file we use the `matplotlib.pyplot.savefig` tool that takes a
string as an argument for the name of the file.

````{tip}
```
import matplotlib.pyplot as plt

plt.figure()
plt.scatter(x, y, label)
plt.savefig(fname)
```

`fname` is a string that represents the name of the file.
````

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
f = np.cos(x)
g = np.sin(x)
plt.figure()
plt.plot(x, f, label="$cos(x)$")
plt.plot(x, g, label="$sin(x)$", color="red")
plt.legend();
```

````{tip}
```
import matplotlib.pyplot as plt

plt.figure()
plt.scatter(x, y, label)
plt.legend()
```
````

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

import matplotlib.pyplot as plt
import numpy as np

x = np.array((1, 2, 3, 4, 5))
y = np.array((-1, -2, 4, -1, 7))
plt.figure()
plt.scatter(x, y)
plt.savefig("plot.pdf")
```

You can pass various extensions as the name of the file (`.pdf`, `png`, `.svg`).
This specifies the format of the file. In general `.pdf` is the format of the
file that ensures the highest quality.
