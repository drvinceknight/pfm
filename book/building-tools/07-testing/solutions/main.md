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

# Solutions

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

Write documentation for the `statistics.py` file written in the exercises of
[Modularisation Exercises](modularisation_exercises).

We start by writing the tests for the code. The following is in a
`test_stats.py` file:

```py
import stats

def test_get_mean():
    """
    This tests the `get_mean` function for a small iterable
    """
    iterable = (1, 2, 3)
    assert stats.get_mean(iterable) == 2


def test_get_population_variance():
    """
    This tests the `get_population_variance` function for a small iterable
    """
    iterable = (1, 2, 3)
    assert round(stats.get_population_variance(iterable), 3) == 0.667
```

Next to test the documentation we modify the code snippets in the documentation
written in [Documentation Exercises](documentation_exercises):
