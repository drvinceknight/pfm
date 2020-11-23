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

1. Using a `for` loop print the types of the variables in each of the following
   iterables:
   1. `iterable = (1, 2, 3, 4)`
   2. `iterable = (1, 2.0, 3, 4.0)`
   3. `iterable = (1, "dog", 0, 3, 4.0)`
2. Consider the following polynomial:

   $$
    3 n ^ 3 - 183n ^ 2 + 3318n - 18757
   $$

   1. Use the `sympy.isprime` function to find the first value of $n$ for which
      that polynomial is not prime?
   2. How many **unique** primes up until the first non prime value are there?
      (Hint: the `set` tool might prove useful here.)

3. Check the following identify for each value of $n\in\{0, 10, 100, 2000\}$:

   $$
       \sum_{i=0}^n i=\frac{n(n+1)}{2}
   $$

4. Check the following identify for all positive integer values of $n$ less than
   5000:

   $$
       \sum_{i=0}^n i^2=\frac{n(n+1)(2n+1)}{6}
   $$

5. Repeat the experiment of selecting a random integer between 0 and 10 until it
   is even 1000 times (see {ref}`repeat_code_while_a_given_condition_holds`).
   What is the average number of times taken to select an even number?
