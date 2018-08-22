Pre: Demo of creating a random number generator
===============================================

Corresponding lab sheet:
------------------------

- `Data Structures and Functions <vknight.org/cfm/chapters/03/>`_

Objectives
----------

- Motivate the use of lists and functions by creating a random number generator.
- Describe list manipulation;
- Describe functions and start discussing writing good code;
- Give insight about random numbers.

Notes
-----

Explain to students that we are going to use programming to generate random
numbers.

**Ask students to discuss in groups how they would generate a random number?**

Bring this discussion together, perhaps some students will talk about using
dice, flipping a coin, etc...

**Ask how would we be able to check that a number is being generated randomly?**

Lead the conversation to the notion of being able to predict a number no better
than by "chance".

Discuss how this could be done by a computer, there are actually only very few
**true** random number generators:

- Atmospheric noise.
- Thermal noise.
- Cosmic background radiation measured over a short amount of time.

We are going to look at something called *pseudo*-random number generators.

There are a number we could choose:

- `Middle Square Method <https://en.wikipedia.org/wiki/Middle-square_method>`_
- `Blum Blum Shub <https://en.wikipedia.org/wiki/Blum_Blum_Shub>`_
- `Linear Congruence Generator <https://en.wikipedia.org/wiki/Linear_congruential_generator>`_

We will consider the last one (LCG) which was considered for a little while to
be state of the art (before being proved to be cyrptographically unsafe: ie
predictable).

This generator takes the form:

.. math::
   X_{n + 1} = aX_n + c \text{mod} m
   X_0 = \text{s}

Where :math:`a, c, m, s` are some parameters.

**In groups choose some parameters and ask students to generate some random
numbers.**

Here is an example using :math:`a=2`, :math:`c=1`, :math:`s=0` and :math:`m=4`:

+------------+------------+
| n          | X_n        |
+============+============+
| 0          | 0          |
+------------+------------+
| 1          | 1          |
+------------+------------+
| 2          | 3          |
+------------+------------+
| 3          | 3          |
+------------+------------+
| 4          | 3          |
+------------+------------+
| 5          | 3          |
+------------+------------+

**Is this random? Did any other group come up with more randomness?**

Now let us code this, to do so we will make use of two new programming concepts:

- Lists
- Functions

First let us write a function that represents the definition of the random
number generator::

    >>> def random_number_generator(previous_term,
    ...                             modulus=4,
    ...                             multiplier_a=2,
    ...                             multiplier_c=1):
    ...     """
    ...     Generate a random number using
    ...     the linear congruential generator
    ...     """
    ...     return (previous_term * multiplier_a + multiplier_c) % modulus


Let us confirm the table above::

    >>> random_number_generator(previous_term=0)
    1
    >>> random_number_generator(previous_term=1)
    3
    >>> random_number_generator(previous_term=3)
    3
    >>> random_number_generator(previous_term=3)
    3

This becomes quickly tedious: it would be much easier to be able to "hold" the
calculated numbers in a container of some sort. In python these are called
lists::

    >>> seed = 0
    >>> random_numbers = [seed]
    >>> number_of_numbers = 10
    >>> for _ in range(number_of_numbers):
    ...     random_numbers.append(random_number_generator(random_numbers[-1]))
    >>> random_numbers
    [0, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3]

If the numbers we were generating were truly random what would the mean of our
list be?::

    >>> sum(random_numbers) / len(random_numbers)
    2.545...
    >>> sum(range(4)) / 4
    1.5

Our choice of parameters is clearly poor, here is a more common choice::

    >>> modulus = 2 ** 32
    >>> multiplier_a = 1664525
    >>> multiplier_c = 1013904223

I am going to use the code I wrote previously so I will wrap it in a function::

    >>> def generate_random_numbers(number_of_numbers, seed, modulus, multiplier_a, multiplier_c):
    ...     """Generate N random numbers"""
    ...     random_numbers = [seed]
    ...     for repetition in range(number_of_numbers):
    ...         random_numbers.append(random_number_generator(random_numbers[-1],
    ...                                                       modulus=modulus,
    ...                                                       multiplier_a=multiplier_a,
    ...                                                       multiplier_c=multiplier_c,))
    ...     return random_numbers


Let us generate a thousand random numbers::

    >>> random_numbers = generate_random_numbers(number_of_numbers=10 ** 3,
    ...                                          seed=0,
    ...                                          modulus=modulus,
    ...                                          multiplier_a=multiplier_a,
    ...                                          multiplier_c=multiplier_c)
    >>> sum(random_numbers) / len(random_numbers)
    2114463563.02497...


We will see in a few weeks time how to plot with python but here's a quick
example::

    >>> import matplotlib.pyplot as plt
    >>> plt.plot(random_numbers)
    [<matplotlib.lines...

Lab sheet
---------

Show how these two things will be gone over in the lab sheet. Potentially
discuss how the previous demo could be improved.

Highlight that
this is just a demo of using lists and functions: not a course on random number
generation: in fact this algorithm is known to not be sufficient and **also**
python and most programming languages all have random number generators that can
be used directly.
