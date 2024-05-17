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

## How to write documentation

Follow the Diataxis framework for documentation.

This involves separating your documentation in to 4 different sections based on
separate aims for readers.

- [Tutorial](how_to_write_a_tutorial): for learning.
- [How to guides](how_to_write_a_how_to_guide): to achieve a specific goal.
- [Explanation](how_to_write_an_explanation_section): to understand.
- [Reference](how_to_write_a_reference_section): to find information.

(how_to_write_a_tutorial)=

### How to write a tutorial

A tutorial should include step by step instructions with expected behaviours.
This should not focus on any deeper explanation.

An analogy of this is teaching a young toddler to build a toy train
track. They do not need to know the physics related to how the train will go
through the track. They need only to see how to lay the track pieces.

(how_to_write_a_how_to_guide)=

### How to write a how to guide

A how to guide should provide a quick and to the point description of how to
solve a specific problem.

An analogy of this would be a recipe. The recipe will not necessarily explain
how to chop an onion and/or why we are chopping an onion it will tell you
to chop an onion as a step of cooking a particular meal.

(how_to_write_an_explanation_section)=

### How to write an explanation section

The explanation section should provide a deeper understanding of the concepts
under the code.

An analogy of this again related to a recipe would be a book on the chemistry of
taste and why a chopped onion adds a specific type of flavour to a meal.

(how_to_write_a_reference_section)=

### How to write a reference section

The reference section should provide an overview of the specific tools, commands
and indeed place for background reading as well (although this can also be
referred to in the explanation section).

(how_to_include_section_headers_in_markdown)=

## How to include section headers in markdown

To include a section header in markdown use `#`. The number of `#` corresponds
to the level of the section header.

````{tip}
```md
# Section
```
````

For example:

```md
# The absorption library

Functionality to study the absorbing Markov chains.

## Tutorial
```

(how_to_include_code_in_markdown)=

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

(how_to_include_a_hyperlink_in_markdown)=

## How to include a hyperlink in markdown

To include a hyperlink in markdown use `[]()`
language:

````{tip}
```md
[text](url)
```
````

For example:

```md
The [Online Encyclopedia of Integer Sequences](https://oeis.org) is a good resources for studying
resources.
```

(how_to_include_an_image_in_markdown)=

## How to include an image in markdown

To include an image in markdown use `![]()`
language:

````{tip}
```md
![caption](path)
```
````

For example:

```md
Here is an image:

![An image](image.jpg)
```

```{attention}
If the image file is not located in the same directory as the markdown file the
path to the file must be correct.
```
