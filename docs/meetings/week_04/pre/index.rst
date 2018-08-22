Pre: Demo of Collatz conjecture
===============================

Corresponding lab sheet:
------------------------

- `Recursion and Reading and writing to file <vknight.org/cfm/chapters/04/>`_

Objectives
----------

- Motivate the use of recursion and writing/reading to file through the study of the Collatz conjecture;
- Describe recursion;
- Describe reading and writing to file.

Notes
-----

Tell students we are going to investigate a particular mathematical process
defined by the following recursive relationship:

.. math::

    f(n) = \begin{cases}
        n / 2& \text{ if }n = 0 \text{mod } 2\\
        3n + 1& \text{ if }n = 0 \text{mod } 2\\
        \end{cases}

**Ask students what :math:`f(2)` is?**

Realise that we have what we will call a base case: computing :math:`n=2`
essentially ends the process.

**What happens when we recursively call :math:`f(n)`?**

Demonstrate what is meant by this with :math:`n=3`:

.. math::

    \begin{align}
    f(3)  &= 3\times 3 + 1 = 10\\
    f(10) &= 10/2 = 5\\
    f(5)  &= 3\times 5 + 1 = 16\\
    f(16) &= 16/2 = 8\\
    f(8)  &= 8/2 = 4\\
    f(4)  &= 4/2 = 2\\
    f(2)  &= 2/1 = 1
    \end{align}

We see that with :math:`n=3` the process eventually finishes.

**Ask students if they think this will always be the case? Why?**

**In groups, using pen and paper repeatedlycompute :math:`f(n)` for
:math:`n\in\{2, 3, 4, 5, 6, 7, 8, 9, 10\}**

We know it terminates for :math:`n\in\{2,3,4,5,8,10\}`.

For :math:`n=6`:

.. math::

    \begin{align}
    f(6)  &= 6/2 = 3
    \end{align}

which we know terminates.

For :math:`n=7`:

.. math::

    \begin{align}
        f(7)  &= 3\times 7 + 1 = 22\\
        f(22)  &= 22/2 = 11\\
        f(11)  &= 3\times 11 + 1 = 34\\
        f(34)  &= 34/2 = 17\\
        f(17)  &= 3\times 17 + 1 = 52\\
        f(52)  &= 52/2 = 26\\
        f(26)  &= 26/2 = 13\\
        f(13)  &= 3\times 13 + 1 = 40\\
        f(20)  &= 20/2 = 10
    \end{align}

which we know terminates.

**Ask students if they think this will always be the case? Why?**


Explain that there is overwhelming evidence that this does indeed always
terminate but that we do not know for sure if it is true.

**Ask students if they know what this is called?**

A conjecture.

Mention the following text from the corresponding `wiki page
<https://en.wikipedia.org/wiki/Collatz_conjecture>`_:

    "Paul Erdős said about the Collatz conjecture: 'Mathematics may not be ready
    for such problems.' He also offered $500 for its solution.[9] Jeffrey
    Lagarias in 2010 claimed that based only on known information about this
    problem, 'this is an extraordinarily difficult problem, completely out of
    reach of present day mathematics.'"

**In groups: write some code to check if the process terminates for a given
:code:`n`**

First let us write the function itself::

    >>> def func(N):
    ...     """Function to apply the Collatz transformation to an integer N"""
    ...     if N % 2 == 0:
    ...         return int(N / 2)
    ...     return 3 * N + 1
    >>> func(10)
    5
    >>> func(5)
    16

**Describe recursion as having two steps:**

- A base case: in our case this is :math:`N=1`.
- Recursive relationship: in our case :math:`a(N)=f(a(N - 1))`

Let us write the process::

    >>> def collatz_process(N, count=0):
    ...     """
    ...     Recursively call the collatz process and return the number of
    ...     times it was called. This is called the "stopping time".
    ...     """
    ...     if N == 1:
    ...         return count
    ...     count += 1
    ...     return collatz_process(func(N), count=count)
    >>> collatz_process(4)
    2
    >>> collatz_process(7)
    16

**Ask students, to in group discuss the code and check if there are any
questions.**

Finally, explain that so far essentially all mathematicians have been able to do
is test this process numerically and have found that it **always** terminates.

One way to do this is to keep track of the results so far on disk::

    >>> with open("collatz_data.txt", "w") as f:  # doctest: +SKIP
    ...     for N in range(2, 50):  # Could swap this for an infinite loop
    ...         stopping_time = collatz_process(N)
    ...         string = str(N) + "," + str(stopping_time) + "\n"
    ...         f.write(string)

We could then read this in and check from a given point or perhaps give the file
to other to use.

Lab sheet
---------

Show how these recursion will be gone over in the lab sheet. Also discuss
reading and writing: highlight where the files needs to be.
