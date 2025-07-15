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

## How to pronounce the double underscore?

The double underscore used in magic methods like `__init__` or `__repr__` is
pronounced "dunder".

## What is the `self` variable for?

In methods the first variable is used to refer to the instance of a given class.
It is conventional to use `self`.

As an example consider this class:

```{code-cell} ipython3
class PetDog:
    """
    A class for a Pet.

    Has two methods:
        - `bark` which returns "Woof" as a string.
        - `give_toy` which gives a toy to the dog in question. This updates the
          `toys` attribute.
    """

    def __init__(self):
        self.toys = []

    def bark(self):
        """
        Returns the string Woof.
        """
        return "Woof"

    def give_toy(self, toy):
        """
        Updates the instances toys list.
        """
        self.toys.append(toy)
```

If we now create two dogs:

```{code-cell} ipython3
auraya = PetDog()
riggins = PetDog()
```

Both have no toys:

```{code-cell} ipython3
auraya.toys
```

```{code-cell} ipython3
riggins.toys
```

Now when we want to give `riggins` a toy we need to specify which of those two
empty lists to update:

```{code-cell} ipython3
riggins.give_toy("ball")
riggins.toys
```

However `auraya` still has no toys:

```{code-cell} ipython3
auraya.toys
```

When running `riggins.give_toy("ball")`, internally the `give_toy` method is
taking `self` to be `riggins` and so the
line `self.toys.append(toy)` in fact is running as `riggins.toys.append(toy)`.

The variable name `self` is a convention and not a functional requirement.
If we modify it (using {ref}`inheritance <how_to_use_inheritance>`):

```{code-cell} ipython3
class OtherPetDog(PetDog):
    """
    A class for a Pet.

    Has two methods:
        - `bark` which returns "Woof" as a string.
        - `give_toy` which gives a toy to the dog in question. This updates the
          `toys` attribute.
    """

    def give_toy(the_dog_in_question, toy):
        """
        Updates the instances toys list.
        """
        the_dog_in_question.toys.append(toy)
```

Then we get the same outcome:

```{code-cell} ipython3
riggins = OtherPetDog()
riggins.toys
```

```{code-cell} ipython3
riggins.give_toy("ball")
riggins.toys
```

Indeed the line `the_dog_in_question.toys.append(toy)` is run as
`riggins.toys.append(toy)`.

You should however use `self` as it is convention and helps with readability of
your code.

## Why do we use `CamelCase` for classes but `snake_case` for functions?

This is specified by the Python convention:
<https://www.python.org/dev/peps/pep-0008/>

These conventions are important as it helps with readability of code.

## What is the difference between a method and a function?

A method is a function defined on a class and always takes a first parameter
which is the specific instance from which the method is called.
