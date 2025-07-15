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

## Why do we write functions in tests?

In {ref}`testing_tutorial` we wrote all the tests using `assert` statements
inside of functions. **Technically** this is not necessary as you could write a
single script with all the assert statements one after the other.

This is not recommended: by using functions we directly have a place to document
the test (in the docstring) and the tests themselves are modularised.
Furthermore, this is actually how to write the tests when using a more
appropriate way of running tests as described in
{ref}`is_there_a_more_efficient_way_to_run_tests`.

(is_there_a_more_efficient_way_to_run_tests)=

## Is there a more efficient way to run tests?

Writing tests as a script and directly running them has one immediate problem:
once the first `assert` statement fails the rest of them are not run.

There is a Python library for running tests called `pytest` <https://docs.pytest.org/>.
There are a number of resources from which to learn how to use `pytest` to its
full extent {cite}`oliveira2018pytest`.

## What should be tested?

The short answer to this is that all software should be tested and that software
is compromised of documentation and code.

Note that it is often not sufficient to test a function in a single way. For
example, consider a function that does two different things depending on the
parity of some input:

```python
def feedback_on_guess(guess, chosen_number):
    """
    Returns whether or not a guess is:

    - Larger than  a chosen_number
    - Smaller than a chosen_number
    - Equal to a chosen number
    """
    if guess < chosen_number:
        return "Guess is lower than chosen number"
    if guess > chosen_number:
        return "Guess is larger than chosen number"
    return "Guess is equal to chosen number"
```

In this case you would need to write at least 3 tests that check the 3
behaviours.

In practice there might be some functionality that is not tested but this should
be made clear and explicit and documented as to why should be written.

## Why do you need doc tests?

The purpose of doctests is to ensure that the code written in documentation is
correct.

It is important to not use doctests to test the functionality of the code: this
risks making the documentation unclear.

## What is test driven development?

Test driven development is the development process of writing the test before
you write the code. Whilst this might seem counter-intuitive it is in fact a
strong approach to writing robust code efficiently.

In practice the process is as follows:

1. Write a test for some new functionality.
2. Run the tests to confirm that it fails (as the functionality is not yet
   written).
3. Write the functionality.
4. Run the test.
5. Modify the test and/or the functionality

Steps 4 and 5 might be repeated many times.

A good overview of test driven development is given in {cite}`percival2014test`.

## How are modularisation, documentation and testing related.

In {ref}`modularisation_tutorial`, {ref}`documentation` and this chapter we have
seen 3 concepts that move us from writing code that works to writing software
that is reliable:

- Modularisation.
- Documentation.
- Testing.

In reality **all 3** of these concepts are closely related and fundamental to
good software. Figure {ref}`fig:best_practice_triangle` shows this.

```{figure} ./img/best_practice_triangle/main.png
---
width: 75%
name: fig:best_practice_triangle
---
The relationship between modularisation, documentation and testing
```
