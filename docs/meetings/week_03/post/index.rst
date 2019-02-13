Post: Reactive discussion + peer exercise
=========================================

Discuss with students what we have seen this week:

- Lists;
- For loops;
- Functions.

Small group exercises (**without a computer**) what does the following
produce::

    >>> friends_at_party = ["Aimee", "Brayden", "Caroline", "Douglas", "Emerys"]
    >>> best_friends = ["Aimee", "Douglas", "Zoe"]
    >>> count = 0
    >>> for friend in friends_at_party:
    ...     if friend in best_friends:
    ...         count += 1
    >>> count
    2

Mention that Python actually has a :code:`set` object that lets us do the above
easier.

Now what about the following::

    >>> def func(a, b):
    ...     if a >= b:
    ...         return a
    ...     return b
    >>> func(5, 3)
    5
    >>> func(4, 4)
    4

Mention that python actually has a :code:`max`.

Now what about the following::

    >>> pairs = [[4, 5], [6, 7], [1, 2], [3, 3]]
    >>> maxs = [func(a, b) for a, b in pairs]
    >>> maxs
    [5, 7, 2, 3]

I know that some students have been asking **why** we use :code:`return` and not
:code:`print`. Let us replace :code:`return` with :code:`print` in :code:`func`
and see the effect::

    >>> def alt_func(a, b):
    ...     if a >= b:
    ...         print(a)
    ...     print(b)
    >>> alt_func(6, 5)
    6
    5

And what happens when we want to use the function::

    >>> maxs = [alt_func(a, b) for a, b in pairs]
    5
    7
    2
    3
    3
    >>> maxs
    [None, None, None, None]

Time permitting, go over the solution to the Monty Hall problem in the lab
sheet.
