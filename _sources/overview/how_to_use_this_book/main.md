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

## How to use this book?

Readers are welcome to use this book in any way they find useful; however, it is
designed with the following suggestion in mind:

- Start by following along with the **tutorial**, carrying out the steps and
  observing the outcomes. It is not expected that a reader gains a deep
  understanding of a given topic when working through the tutorial. The goal
  here is to achieve some level of familiarity.

- After the tutorial, work through the **how-to** section. It is through this
  section that a deeper understanding should be gained, making connections to
  the steps taken in the tutorial. **After working through the how-to section,
  it is hoped that the reader would understand all steps taken in the tutorial**.

- The **exercise section** provides an opportunity for readers to practice the
  topics covered in the how-to section.

- After working through these three sections, some readers may have further
  questions or want more information about a given topic. This is covered in
  the **further information** section.

## How is code displayed in this book?

In this book, you will see code displayed in several different formats. The most
common format is input to the programming tool **Jupyter**, described at length
in [the Using Notebooks chapter](chp:using_notebooks). For example:

```{code-cell} ipython3
2 + 2
```

You will see typical usage instructions for particular code commands:

````{admonition} Usage
:class: tip
```
sym.solveset(<equation>)
```
````

You will see how to write a particular language called **markdown** (covered in
[the Using Notebooks Chapter](chp:using_notebooks) and [the Documentation
Chapter](chp:documentation))

```md
# Algebra with Python
```

In chapters [the Command Line Chapter](chp:cli) to [the Testing Chapter](chp:testing), you will see Python code saved to
files:

```py
print(2 + 2)
```

You will also see commands written for a command-line tool. This is how you will
start **Jupyter** in [the Using Notebooks Chapter](chp:using_notebooks) but is introduced more formally
in [the Command Line Chapter](chp:cli):

```console
$ ls
```

# What this version of the book has that the printed version does not

Thanks to the publisher's progressive understanding, this online version
of the book allows for more content than the [printed version](https://www.taylorfrancis.com/books/mono/10.1201/9781003451860/python-mathematics-vincent-knight?context=ubx&refId=df92ae24-7381-40f4-96a6-e543be95b30b).
As such, there are two specific things that are included:

1. Solutions to the exercises.
2. A collection of further information chapters, covering specific tools like
   `numpy` for numerical mathematics and detailed descriptions of working with
   Jupyter kernels.

Additionally, grammatical fixes, more exercises, and new further information
chapters will continue to be added to the online version.
