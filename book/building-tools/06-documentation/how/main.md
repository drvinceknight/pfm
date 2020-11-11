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

## How to include code in markdown

To include code in markdown use three ` marks followed by the name of the
language:

`````{tip}
````
```<language>

<code>
```
````
`````

For example:

````
```python
import sympy as sym

x = sym.Symbol("x")
```
````

Would render as:

```python
import sympy as sym

x = sym.Symbol("x")
```

It is also possible to include code in markdown using an indented block:

For example:

```md
Here is some code:

    import sympy as sym

    x = sym.Symbol("x")
```


Would render as:

---

Here is some code:

    import sympy as sym

    x = sym.Symbol("x")

---

```{attention}
Using an indented block does not allow you to specify the language and can lead
to mistake when combining with other nested statement.
```


## How to write a tutorial

A tutorial should include step by step instructions with expected behaviours.
This should not focus on any deeper explanation.

An analogy of this is teaching a young toddler to build a toy train
track. They do not need to know the physics related to how the train will go
through the track. They need only to see how to lay the track pieces.

## How to write a how to guide

A how to guide should provide a quick and to the point description of how to
solve a specific problem.

An analogy of this would be a recipe. The recipe will not necessarily explain
how to chop an onion and/or why we are chopping an onion it will tell you
to chop an onion as a step of cooking a particular meal.

## How to write an explanation section

The explanation section should provide a deeper understanding of the concepts
under the code.

An analogy of this again related to a recipe would be a book on the chemistry of
taste and why a chopped onion adds a specific type of flavour to a meal.

## How to write a reference section

The reference section should provide an overview of the specific tools, commands
and indeed place for background reading as well (although this can also be
referred to in the explanation section).
