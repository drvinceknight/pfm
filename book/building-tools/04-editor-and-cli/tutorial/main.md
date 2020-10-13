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

(cli_editor_tutorial)=
# Tutorial

We will here consider a problem we have already solved (in the Algebra
{ref}`algebra_tutorial`) but use a different interface to do so than Jupyter.
The code itself will be the same. The way we run it will differ.

```{admonition} Problem
Consider the following quadratics:

$$
f(x) = 5 x ^ 2 + 2 x + 7\\
g(x) = 4 x ^ 2 - 3 x + 12\\
h(x) = f(x) + g(x)
$$

Without using `sympy`, obtain the roots for all the quadratics.
```

Open a command line tool:

1. On **Windows** search for `Anaconda Prompt` (it should be available to you
   after installing Anaconda). See
   {ref}`fig:starting_the_notebook_server_windows`.
2. On **OS X** search for `terminal`. See
   {ref}`fig:starting_the_notebook_server`.

Whether or not your are on Windows or OS X changes the commands you need to
type. We will first list the directory we are currently in:


````{panels}
On Windows:

```bash
$ dir
```

---

On OS X:

```bash
$ ls
```

````

This is similar to using your file explorer to view the contents in a given
directory. Similarly to the way we click on a directory in the file explorer we
can navigate to a directory in the command line.

To do this we use the same command on both operating systems:


````{panels}
On Windows:

```bash
$ cd <target_directory_name>
```

---

On OS X:

```bash
$ cd <target_directory_name>
```

````

We will do this to navigate to our `cfm` directoy. For example if, as in the
Algebra {ref}`algebra_tutorial` the `cfm` directory was on the `Desktop`
directory we would run the following:


````{panels}
On Windows:

```bash
$ cd Desktop
$ cd cfm
```

---

On OS X:

```bash
$ cd Desktop
$ cd cfm
```

````
