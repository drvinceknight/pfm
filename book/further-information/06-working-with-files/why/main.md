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

# Further information.

## What is a context manager

Instead of using the approach shown in [How to write to a file](how_to_write_to_a_file) it is
possible to write to a file using the following:

```{code-cell} ipython3
f = open("squares.csv", "w")
for n in range(1, 101):
    f.write(f"{n}, {n ** 2}\n")
f.close()
```

However, when doing so it is important to `close` the file. Without this the
file remains inaccessible for other purposes.

Thus, it is preferred to use:

```{code-cell} ipython3
with open("squares.csv", "w") as f:
    for n in range(1, 101):
        f.write(f"{n}, {n ** 2}\n")
```

In this case, the indented block after `with open("squares.csv", "w") as f:` is
the context within which the file `f` is open. It will be closed outside of that
indented block.

This is an example of a _context manager_. There are other examples of this in
Python such as `try` and `except` loops.

## Working with files with `numpy`

It is possible to write a [`numpy`](numpy) array to a file using the `savetxt` function. For
example:

```{code-cell} ipython3
import numpy as np

A = np.array(
    (
        (1, 5, 3),
        (8, 1, 2),
        (3, 5, 1),
    )
)
np.savetxt("array.txt", A)
```

It is possible read a file in to a numpy array using the `loadtxt` function:

```{code-cell} ipython3
A = np.loadtxt("array.txt")
A
```

## Working with files with pathlib

The `pathlib` library is a powerful tool for reading, writing and manipulating
files.

The documentation for `pathlib` is available here: [docs.python.org/3/library/pathlib.html](https://docs.python.org/3/library/pathlib.html)
