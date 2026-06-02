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

## How to install a library

`````{tab-set}
````{tab-item} pip
To install a library from the Python Package Index:

```{tip}
```console
$ python -m pip install <library>
```
```

For example, to install `ciw` (a queuing-systems library):

```console
$ python -m pip install ciw
```
````

````{tab-item} uv
If you have not already initialised a `uv` project in your working directory,
do so first (this is a one-time step):

```{tip}
```console
$ uv init --no-package
```
```

Then add a library:

```{tip}
```console
$ uv add <library>
```
```

For example:

```console
$ uv add ciw
```

This installs the library and records it in `pyproject.toml`. To install
a library without adding it as a permanent dependency use
`uv pip install <library>` instead.
````
`````

```{attention}
Well documented libraries will always have installation instructions. It is
recommended to read those before installing a library.
```
