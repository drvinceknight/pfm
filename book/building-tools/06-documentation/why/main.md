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

(documentation_further_information)=
# Further information

## What is documentation

Documentation can have many different interpretations. A good definition is
given in {cite}`martraire2019living`:

> The process of transferring valuable knowledge to other people now and also to
> people in the future.

```{note}
It is important to realise that the target of the documentation can be the
writer of the software itself at a future date.
```

There are two types of documentation:

- **Internal documentation** which includes things like docstrings and a good
  choice of variable name.
- **External documentation** which includes things like `README.md` and other
  separate documentation.

For a software project to be well documented it needs **both** internal and
external documentation.

In {cite}`martraire2019living` there are 4 properties of documentation:

- Reliable: it needs to be accurate.
- Low effort: it should require minimal effort when changes are made to the code
  base.
- Collaborative: it should be a tool from which collaboration can occur.
- Insightful: it should give information not only to be able to use the code but
  also to understand specific reasons why certain decisions have been made as to
  its design.

## What is the purpose of the four separate sections in documentation

As discussed in <https://documentation.divio.com>:

> "Tutorials are lessons that take the reader by the hand through a series of
> steps to complete a project of some kind. They are what your project needs in
> order to show a beginner that they can achieve something with it."

> "How-to guides take the reader through the steps required to solve a
> real-world problem"

> "Reference guides are technical descriptions of the machinery and how to
> operate it."

> "Explanation, or discussions, clarify and illuminate a particular topic. They
> broaden the documentation’s coverage of a topic."

It is natural when describing a project for the boundaries between these four
topics to become fuzzy. Thus, having them explicitly in four separate sections
ensures the reader is able to specifically find what they need.

## What alternatives are there to writing documentation in `README.md`

A single `README.md` file is a good way to start documenting code. However as a
project grows it could be beneficial to use some other tools. One such example
of this is to use `sphinx`: <https://www.sphinx-doc.org/en/>. This uses a
different markup language called _restructured text_
<https://docutils.sourceforge.io/rst.html> and helps build more complex
documents but also interfaces to the code itself if necessary. So for example it
is possible to include the code docstrings directly in the documentation (a good
way of adding to the reference section).
