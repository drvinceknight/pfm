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

# Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. Write a function that generates $n!$.
2. Write a function that generates the $n$th triangular numbers defined by:

    $$
        T_n = \frac{n(n+1)}{2}
    $$
3. Verify the following that the following identify holds for $n\leq 500$:

    $$
        \sum_{i=0}^n T_i = \frac{n(n+1)(n+2)}{6}
    $$
4. Consider the [Monty Hall
   problem](https://en.wikipedia.org/wiki/Monty_Hall_problem):
   1. Write a function that simulates the play of the game when you 'stick' with
      the initial choice.
   2. Write a function that simulates the play of the game when you 'change'
      your choice.
   3. Repeat the play of the game using both those functions and compare the
      probability of winning.
