Pre: Demo of Bisection Method
=============================

Corresponding lab sheet:
------------------------

- `Variables, Conditional Statements and Loops <vknight.org/cfm/chapters/01/>`_

Objectives
----------

- Motivate the use of code through an algorithm for solving equations
  numerically;
- Describe variable assignment;
- Conditional statements;
- While loops.

Notes
-----

Explain to students that we are going to use programming to solve the following
equation:

.. math::

   x ^ 3 - 2 - 3 cos(x) = 0

**Give students time to attempt to solve this equation.**

Some might use calculators and attempt to approximate: ask how and why.

**We're going to step back and consider a different equation first.**

Ask students to consider the equation:

.. math::

   x ^ 3 = 2

**How would we find solutions to this equation?**

Agree on :math:`x = \sqrt[3]{2} = (2) ^ {1/3}` and show how we can compute
this in Python::

    >>> (2) ** (1 / 3)
    1.259921...

Note that we can also assign variables::

    >>> x = 2 ** (1 / 3)
    >>> x
    1.259921...

We can then use this to check::

    >>> x ** 3
    2.0

Let us see what this value of :code:`x` gives in the equation we're considering.

Python has a number of libraries (we will see this more later) that give various
functionality, include the :code:`math` library, let us import it for
:code:`math.sqrt`. **Demo tab completion at this stage.**::

    >>> import math
    >>> x ** 3 - 2 - 3 * math.cos(x)
    -0.917676...

**Ask students if they have an idea of how to find an actual solution?**

- What is an actual solution?
- What is an acceptable solution?

**What does the following imply**::

    >>> x += 1
    >>> x ** 3 - 2 - 3 * math.cos(x)
    11.44955...

Have a discussion and discuss the fact that this implies that a solution is
somewhere between :math:`2^(1/3)` and :math:`2^(1/3) + 1`.

Then discuss the *bisection* method:

- Draw a plot;
- Explain the logic.

Do some steps by hand:

Let us reset our value of :code:`x`::

    >>> x -= 1
    >>> x
    1.259921...

Let us set up :math:`a` and :math:`b`::

    >>> a, b = x, x + 1
    >>> f_of_a = a ** 3 - 2 - 3 * math.cos(a)
    >>> f_of_b = b ** 3 - 2 - 3 * math.cos(b)


Now consider the mid point of :math:`a` and :math:`b`:

.. math::

   \frac{a + b}{2}

   >>> mid_point = (a + b) / 2

Compute f of this mid point::

    >>> f_of_mid_point = mid_point ** 3 - 2 - 3 * math.cos(mid_point)
    >>> f_of_mid_point
    4.01504...

**Have a discussion about what our next :math:`a` and :math:`b` should be (draw
this possibly).**

How can we test if two numbers of the same sign?::

    >>> f_of_a * f_of_mid_point
    -3.6845...
    >>> f_of_b * f_of_mid_point
    45.9704...
    >>> f_of_a * f_of_mid_point > 0
    False
    >>> f_of_b * f_of_mid_point > 0
    True

Now discuss what the next step would be::

    >>> b = mid_point
    >>> f_of_b = f_of_mid_point
    >>> mid_point = (a + b) / 2
    >>> f_of_mid_point = mid_point ** 3 - 2 - 3 * math.cos(mid_point)
    >>> f_of_mid_point
    1.25989793...
    >>> f_of_a * f_of_mid_point > 0
    False
    >>> f_of_b * f_of_mid_point > 0
    True

**How long should we repeat this for?**::

    >>> f_of_mid_point < 10 ** (-6)
    False

We will use :code:`if` statements and :code:`for` loops to get the computer to
automate this for as long as we require.

Write the following::

    >>> a, b = x, x + 1
    >>> f_of_a = a ** 3 - 2 - 3 * math.cos(a)
    >>> f_of_b = b ** 3 - 2 - 3 * math.cos(b)
    >>> tol = 10 ** (-6)
    >>> while abs(f_of_a) > tol:
    ...     mid_point = (a + b) / 2
    ...     f_of_mid_point = mid_point ** 3 - 2 - 3 * math.cos(mid_point)
    ...     if f_of_mid_point * f_of_a > 0:  # If a and mid point have same sign
    ...         a = mid_point
    ...         f_of_a = f_of_mid_point
    ...     else:
    ...         b = mid_point
    ...         f_of_b = f_of_mid_point

Now that this has run we can confirm::

    >>> mid_point
    1.3731447...
    >>> f_of_mid_point < tol
    True

Lab sheet
---------

Show how these three components will be gone over in the lab sheet. Encourage
students to investigate them fully to make sure they understand the approach.

Highlight that there is room for improving the code which we will do in the
**next** lab sheet.
