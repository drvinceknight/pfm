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

(why_modularise)=

## Why modularise?

Best practice when writing code is to break up code in to modular parts. One
guiding principle described in {cite}`fowler2018refactoring`:

<!--alex disable obvious-->
<!--alex disable easy-->

> "Code should be obvious. When someone needs to make a change, they should be
> able to find the code to be changed easily and make the change quickly without
> introducing any errors."

<!--alex enable easy-->
<!--alex enable obvious-->

Whilst this guiding principle is ambiguous and all concepts related to clean
code writing and refactoring are not things that can be covered in this book one
specific principle is the one referred to in {cite}`martin2009clean`:

> "Functions should do one thing. They should do it well. They should do it
> only."

```{note}
In some texts on code architecture you will see arbitrary rules about how many
lines of code should be in a given function. Having a function with 10 or more
lines of could might indicate that it can be modularised. **However**, I do not
recommend following such rules as sometimes they might add more complexity than
they remove. I recommend you stick to the principles of making your code clear and
ensuring your functions do one thing well and one thing only.
```

## Why do I get an import error?

The most probable explanation for this is that you are importing a file that is
not in the same directory or that you have not imported the file with the
correct name.

If we assume that your code is in a `library.py` directory but that your
notebook is in a **different** directory then you will get an error as shown
below:

```{code-cell}
---
tags: [raises-exception]
---
import library
```

Similarly if you perhaps incorrectly saved your `library.py` file with a typo in
the name such as: `librery.py` then you would get the same error.

## How do I make my file importable from other directories?

This falls under the subject matter of "packaging". We will not cover this in
this book but some good information on the practice is available at the
following:

- <https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/>
- <https://packaging.python.org>
- <https://packaging.python.org/overview/>
- <https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html>
