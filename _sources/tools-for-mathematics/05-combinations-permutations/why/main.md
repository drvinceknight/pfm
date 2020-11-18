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

## How does tuple indexing work?

We have seen in this chapter how to access a single element in a tuple. There
are various ways of indexing tuples:

1. Indexing (what we have seen here)
2. Negative indexing (indexing starting from the end)
3. Slicing (selecting a number of elements)

This document gives good information on this:
<https://www.programiz.com/python-programming/tuple>

## Why does `range`, `itertools.permutations` and `itertools.combinations` not directly give the elements?

When you run either of the three `range`, `itertools.permutations` or
`itertools.combinations` tools this is an example of creating a **generator**.
This allows us to create the instructions to build something without building
it.

In practice this means that we can create large sets without needing to generate
them until we wanted to.
