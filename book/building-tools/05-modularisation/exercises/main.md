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

(modularisation_exercises)=

# Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. Use the code written in the {ref}`modularisation_tutorial` to obtain the average time
   until absorption of the Markov chains with the following transition matrices:
   1. $P = \begin{pmatrix}1/2 & 1/2 \\ 0 & 1 \end{pmatrix}$
   2. $P = \begin{pmatrix}1/2 & 1/4 & 1/4\\ 1/3 & 1/3 & 1/3  \\0 & 0 & 1 \end{pmatrix}$
   3. $P = \begin{pmatrix}1 & 0 \\ 1/2 & 1/2 \end{pmatrix}$
   4. $P = \begin{pmatrix}1/2 & 1/4 & 1/4\\ 1/3 & 1/3 & 1/3  \\1/5 & 0 & 4/5 \end{pmatrix}$
2. Modularise the following code by converting it to 2 functions:

   ```
   def sample_experiment(bag):
       """
       This samples a token from a given bag and then
       selects a coin with a given probability.

       If the sampled token is red then the probability
       of selecting heads is 4/5 otherwise it is 2/5.

       This function returns both the selected token
       and the coin face.
       """
       selected_token = pick_a_token(container=bag)

       if selected_token == "Red":
           probability_of_selecting_heads = 4 / 5
       else:
           probability_of_selecting_heads = 2 / 5

       if random.random() < probability_of_selecting_heads:
           coin = "Heads"
       else:
           coin = "Tails"
       return selected_token, coin
   ```

3. Modularise the following code by converting it to 3 functions:

   ```
   import math

   def is_prime(N):
        """
       Checks if a number N is prime by checking all that positive integers
       numbers less sqrt(N) than it that divide it.

       Note that if N is not a positive integer great than 1 then it does not
       check: it returns False.
       """
       if N <= 1 or type(N) is not int:
           return False
       for potential_divisor in range(2, int(math.sqrt(N)) + 1):
           if (N % potential_divisor) == 0:
               return False
       return True
   ```

   Confirm your work by comparing to the results of using `sympy.isprime`.

4. Write a `stats.py` file with two functions to implement the calculations of
   mean, median and variance of the following collections of numbers:

   1. $S_1=(1, 2, 3, 4, 4, 4, 4, 4)$
   2. $S_1=(1)$
   3. $S_1=(1, 1, 1, 2, 3, 4, 4, 4, 4, 4)$

   Compare your results to the results of using the `statistics.mean`,
   `statistics.median` and `statistics.variance`. Note: the `statistics` library
   is part of the standard python library.

5. Write a `calculus.py` file with tools to be able to find and qualify (using
   the second derivative test) the inflection
   points of a given quadratic (assumed to be a Sympy expression).
