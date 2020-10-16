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

# Further information

## Why do we need to use the `print` function with an editor?

When we use a Jupyter notebook, the last line of a cell corresponds to the
output of the cell and is automatically displayed.

When running code written in an editor directly through the Python interpreter
there is no where for code to be output to. Thus we need to specifically tell it
to display the code which is what the `print` statement does.

## Can I use a Python plugin to run my code from inside my editor?

When using the Python plugin buttons become available that let you run code
without using the command line. If this helps you with your programming than I
encourage you to use it. However, It is good to be comfortable using a
command line tool to fully understand what the underlying process. Furthermore,
at times when debugging sometimes the user interface might be at fault.

## Can I open a Jupyter notebook inside vscode?

When using the Python plugin it is actually possible to use Jupyter notebooks
from within VScode.

The notebooks will not look exactly the same but have the same functionality.

```{figure} ./img/notebook_in_vscode/main.png
---
width: 75%
name: fig:notebook_in_vscode
---
A notebook in vscode
```

Note that when writing markdown the `$` signs must be used to delimit
mathematics. (See {ref}`why_do_we_use_brackets_instead_of_dollars_for_latex`).

## What is the difference between an Integrated Development Environment and an editor?

An *I*ntegrated *D*evelopment *E*nvironment or IDE is another type of tool used
to write code. A popular one for Python is PyCharm
<https://www.jetbrains.com/pycharm/>.

Generally IDEs are powerful tools designed for one specific language whereas
editors are supposedly lightweight and designed to be flexible to be used with
many languages.

I recommend experimenting with IDEs and/or editors to find what you prefer but
throughout this book we will use VScode.

## Why can I not use ``\\(`` and ``\\)`` for markdown in VScode.

When using Jupyter notebooks or the markdown preview feature in VScode the
single `$` and `$$` must be used as delimiters for mathematics. (See
{ref}`why_do_we_use_brackets_instead_of_dollars_for_latex`).
