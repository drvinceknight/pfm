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

(how_to_write_to_a_file)=

## How to write to a file

To write to a file use `open` with the `w` parameter:

````{tip}
```
with open(filename, "w") as temporary_name:
    ...
```
````

For example, the following creates a file with the values of integer $n$ and $n^2$ on
each row for $1\leq n \leq 100$.

```{code-cell} ipython3
with open("squares.csv", "w") as f:
    for n in range(1, 101):
        f.write(f"{n}, {n ** 2}\n")
```

## How to append to a file

To write to a file without deleting what is already in the file use `open` with the `a` parameter:

````{tip}
```
with open(filename, "a") as temporary_name:
    ...
```
````

For example, the following appends integer $n$ and $n^2$ on
each row for $101\leq n \leq 200$.

```{code-cell} ipython3
with open("squares.csv", "a") as f:
    for n in range(101, 201):
        f.write(f"{n}, {n ** 2}\n")
```

## How to read from a file

To read a file use `open` with the `r` parameter:

````{tip}
```
with open(filename, "r") as temporary_name:
    ...
```
````

For example, the following reads the data from `squares.csv`.

```{code-cell} ipython3
with open("squares.csv", "r") as f:
    data_as_string = f.read()

data_as_string
```

## How to turn a string in to a list

To split a string on a given character and turn it in to a list use the `split`
method:

````{tip}
```
string.split()
```
````

For example to convert the `data_as_string` variable to a list of string:

```{code-cell} ipython3
:tags: [output_scroll]

data = data_as_string.split("\n")
data
```

Note that the last element is an empty row.

We can use the `split` method on each element of the data splitting on the `,`
and also convert the entries to an integer.

```{code-cell} ipython3
:tags: [output_scroll]

data = [[int(n) for n in row.split(",")] for row in data_as_string.split("\n")[:-1]]
data
```
