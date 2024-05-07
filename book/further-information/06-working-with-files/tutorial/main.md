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

We will consider the following problem.

```{admonition} Problem
An Alternating Sign Matrix (ASM) of size $n$ is a square matrix with entries:
$0, 1$ or $-1$ such that:

- The sum of all rows and columns is 1.
- The non zero entries in each row and column alternate in sign.

For example there are 7 alternating sign matrices of size $n=3$

$$
\begin{pmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1\\
\end{pmatrix}
\qquad
\begin{pmatrix}
1 & 0 & 0\\
0 & 0 & 1\\
0 & 1 & 0\\
\end{pmatrix}
$$
$$
\begin{pmatrix}
0 & 1 & 0\\
0 & 0 & 1\\
1 & 0 & 0\\
\end{pmatrix}
\qquad
\begin{pmatrix}
0 & 0 & 1\\
1 & 0 & 0\\
0 & 1 & 0\\
\end{pmatrix}
$$
$$
\begin{pmatrix}
0 & 1 & 0\\
1 & 0 & 0\\
0 & 0 & 1\\
\end{pmatrix}
\qquad
\begin{pmatrix}
0 & 0 & 1\\
0 & 1 & 0\\
1 & 0 & 0\\
\end{pmatrix}
$$
$$
\begin{pmatrix}
0 & 1 & 0\\
1 & -1 & 1\\
0 & 1 & 0\\
\end{pmatrix}
$$

The number of Alternating Sign Matrices of size $n$ is given by the following
formula {cite}`bressoud1999proofs`:

$$
A_n = \prod_{i=0}^{n-1}\frac{(3i+1)!}{(n + i)!}
$$

The file available at [10.5281/zenodo.11121413](https://zenodo.org/records/11121414/files/main.txt?download=1) is believed to contain the number $A_n$ for $1\leq n\leq 20$.

1. Confirm that the values in the file are correct.
2. Create a new file with the values of $A_n$ for $1\leq n \leq 500$.
```

First let us write a function to generate $A_n$ from the formula:

```{code-cell} ipython3
import sympy as sym

def get_A_n(n):
    """
    Return the number of Alternating Sign Matrices of size n as given by

    A_n = \prod_{i=0}^{n-1}\frac{(3i+1)!}{(n + i)!}

    Parameters
    ----------
    n : int
        The size

    Returns
    -------
    int
        The number of Alternating Sign Matrices
    """
    return sym.prod(sym.factorial(3 * i + 1) / sym.factorial(n + i) for i in range(n))
```

Note that we choose to use `sympy` here to handle the integer division without
any numeric approximation.

Let us confirm the number of $n=3$:

```{code-cell} ipython3
get_A_n(n=3)
```

Next, let us read the data file after downloading it:

```{code-cell} ipython3
with open("main.txt", "r") as f:
    data_as_string = f.read()
```

This reads the contents of the data file as a string:

```{code-cell} ipython3
data_as_string
```

Note the `\n` character which indicates a line break. We can create a list from
this string by splitting on that character:

```{code-cell} ipython3
data_as_strings_as_list = data_as_string.split("\n")
data_as_strings_as_list
```

Finally we create a list by converting each substring to an `int`.

```{code-cell} ipython3
data = [int(item) for item in data_as_strings_as_list]
data
```

First let us confirm that the formula confirms that the data is correct.

```{code-cell} ipython3
check = all(get_A_n(n=i + 1) == value for i, value in enumerate(data))
check
```

Now, let us write a new file with $A_n$ for $1\leq n \leq 200$:

```{code-cell} ipython3
with open("data.txt", "w") as f:
    for n in range(1, 101):
        A_n = get_A_n(n=n)
        f.write(f"{A_n}\n")
```

```{important}
In this chapter we have:

- Read information stored in a file.
- Write information to a file.
```
