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

## How to import code from python files

Given a `<file.py>` file in a directory any other python process in the same
directory can import that file as it would a normal library.


````{tip}
```
import <file>
```
````

At that stage it is possible to uses any python object (a `function`, a `class`, a
`variable`) by referring to the `<file.py>` as  library:

```
<file>.function
<file>.class
<file>.variable
```

See the {ref}`modularisation` for examples of this.

## How to break up code in to modular components

When modularising code aim to identify specific components of the code that can
be isolated from the rest.

In practice this means writing multiple functions that use the correct inputs
and outputs in chain for an overall goal.

Often this allows us to write a more comprehensive docstring that explains
specific parts of the implemented process.

As an example, consider the problem of wanting to pay a shared bill after
applying a tip, the following function will do this:

```{code-cell} ipython3
def add_tip_and_get_bill_share(total, tip_proportion, number_of_payers):
    """
    This returns the share of a bill to be paid by `number_of_payers`
    ensuring the total paid includes a tip.
    """
    tip_amount = tip_proportion * total
    total += tip_amount
    return total / number_of_payers
```

We can check that this works:

```{code-cell} ipython3
add_tip_and_get_bill_share(total=100, tip_proportion=.2, number_of_payers=6)
```

An improvement of the above would be:

```{code-cell} ipython3
def add_tip(total, tip_proportion):
    """
    This adds the given proportion to a bill total.

    Note that tip_proportion is a number between 0 and 1. A tip_proportion of 0
    corresponds to no tip and a tip_proportion of 1 corresponds to paying the
    total twice.
    """
    tip_amount = tip_proportion * total
    return total + tip_amount

def get_bill_share(total, number_of_payers):
    """
    This returns the share of a bill by dividing the total by the number of
    payers.
    """
    return total / number_of_payers
```

Then to use the above we would be able to explicitly write out each step which
ensures that there is clarity in what is being done:

```{code-cell} ipython3
total = add_tip(total=100, tip_proportion=.2)
get_bill_share(total=total, number_of_payers=6)
```

You can read more and find reference texts about
modularisation at {ref}`why_modularise`.
