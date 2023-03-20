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

1. Use the code written in the [Modularisation Tutorial](modularisation_tutorial) to obtain the average time
   until absorption from the first state of the Markov chains with the following transition matrices:
   1. $P = \begin{pmatrix}1/2 & 1/2 \\ 0 & 1 \end{pmatrix}$
   2. $P = \begin{pmatrix}1/2 & 1/4 & 1/4\\ 1/3 & 1/3 & 1/3  \\0 & 0 & 1 \end{pmatrix}$
   3. $P = \begin{pmatrix}1 & 0 \\ 1/2 & 1/2 \end{pmatrix}$
   4. $P = \begin{pmatrix}1/2 & 1/4 & 1/4\\ 1/3 & 1/3 & 1/3  \\1/5 & 0 & 4/5 \end{pmatrix}$
2. Modularise the following code by creating a function `flip_coin` that takes a
   `probability_of_selecting_heads` variable.

   ```
   import random
   
   def sample_experiment(bag):
       """
       This samples a token from a given bag and then
       selects a coin with a given probability.

       If the sampled token is red then the probability
       of selecting heads is 4/5 otherwise it is 2/5.

       This function returns both the selected token
       and the coin face.
       """
       selected_token = random.choice(bag)

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

3. Modularise the following code by writing 2 further functions:

   - `get_potential_divisors`: A function to return the integers between 2 and
     $\sqrt{N}$ for a given $N$.
   - `is_divisor`: A function to check if $n | N$ ("$n$ divides $N$") for given
     $n, N$.

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
   mean and population variance.

   Note that the mean is defined by:

   $$
    \bar x \frac{\sum_{i=1}^{N} x_i}{N}
   $$
   
   The population variance is defined by:

   $$
    \sigma ^ 2 = \frac{\sum_{i=1}^{N} (x_i - \bar x) ^ 2}{N}
   $$

   Use your functions to compute the mean and population variance of the following
   collections of numbers:

   1. $S_1=(1, 2, 3, 4, 4, 4, 4, 4)$
   2. $S_1=(1)$
   3. $S_1=(1, 1, 1, 2, 3, 4, 4, 4, 4, 4)$

   Compare your results to the results of using the `statistics.mean`,
    and `statistics.pvariance`. Note: the `statistics` library
   is part of the standard python library.
