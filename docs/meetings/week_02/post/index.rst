Post: Reactive discussion + peer exercise
=========================================

2019
----

Have a general chat with students:

- How did they find things?

Start by highlighting that we have seen 3 things:

- Variable assignment (3 types: numeric, string and boolean);
- If statements;
- While loops.

Ask students to read the first few topics in the list of topics. With their
neighbour discuss the expected output, the code itself and ask them to write
their own examples.

Explain that today we will go over exercise 4 and 5.

Before doing that: show that this is going to be a very small modification of
tutorial 4.

After discussing the code run with :code:`nbtutor`, include :code:`%load_ext
nbtutor` in a cell and then include :code:`%%nbtutor` in a given cell.

Highlight the role of indentation and the difference between both examples.

Now as a class, aim to find the number of the numbers less than 500 that are
perfect squares:

.. math::

   |\{n \in \mathbb{N} | \sqrt{n} \in \mathbb{Z} \text{ and }n \leq 500\}|


Before we start show::

    >>> import math
    >>> n = 64
    >>> int(math.sqrt(n)) ** 2 == n
    True
    >>> int(math.sqrt(n + 1)) ** 2 == n + 1
    False

**In groups write down some code to do this.**

Show a solution::

    >>> upper_limit = 500
    >>> number = 0
    >>> count = 0
    >>> while number < upper_limit:
    ...     number += 1
    ...     if int(math.sqrt(number)) ** 2 == number:
    ...         count += 1
    >>> count
    22

Discuss possible modifications, for example how to print them, but also what
about finding the 500th perfect square?::

    >>> upper_limit = 500
    >>> number = 0
    >>> count = 0
    >>> while count < upper_limit:
    ...     number += 1
    ...     if int(math.sqrt(number)) ** 2 == number:
    ...         count += 1
    >>> number
    250000


If there is time, explain that question 6 is difficult. Ask them to use it by
hand to find the sqrt of a 4 and 5. Immediately should arrive at the problem of
how to start?
