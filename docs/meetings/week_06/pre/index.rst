Pre: Demo of Sympy
==================

Corresponding lab sheet:
------------------------

- `Symbolic mathematics with Sympy <vknight.org/cfm/chapters/05/>`_

Objectives
----------

- Understand the difference between symbolic and numeric variables;
- Manipulate symbolic expressions;
- Use basic Sympy.

Notes
-----

**Ask students if the following expression is true and if/how they would check
this using Python?**

.. math::

    (\alpha + \beta)(\alpha - \beta)^2 =
    \alpha^{3} - \alpha^{2} \beta - \alpha \beta^{2} + \beta^{3}

Let students discuss in groups and write some code to do this.

Expect them to say that they would "try this for a large number of examples".
Explain that this won't prove anything but just tries a number of examples: in
the same way that you could do this by hand.

Some might say they would use wolfram alpha: explain that we're essentially
going to see how to use an equivalent version of that with Python.

Explain that we are going to use a Python library called Sympy which allows us
to do symbolic mathematics::

    >>> import sympy as sym
    >>> alpha, beta = sym.symbols("alpha, beta")
    >>> sym.expand((alpha + beta) * (alpha - beta) ** 2)
    alpha**3 - alpha**2*beta - alpha*beta**2 + beta**3

Now say we're going to use Sympy to answer a "textbook" secondary school
question:

**Identify all points of inflection of the following quartic:**

.. math::

    f(x) = -x^4 + 9x^2+4x-12

**Ask students in groups to identify the steps we need to solve:**

1. Identify derivative;
2. Identify roots of derivative;
3. Evaluate the second derivate at these roots.

Some other suggestions might be to look at roots of the function itself as well
as asymptotic limits (say we can do this too!).

Let us first write a Python function::

    >>> def f(x):
    ...     return - x ** 4 + 9 * x ** 2 + 4 * x - 12
    >>> f(5)
    -392

Now let us pass a symbolic variable to this function::

    >>> x = sym.Symbol("x")
    >>> f(x)
    -x**4 + 9*x**2 + 4*x - 12

We can compute the derivative::

    >>> der = sym.diff(f(x), x)
    >>> der
    -4*x**3 + 18*x + 4

We can find the roots of this derivative using Sympy's function called
:code:`solveset`::

    >>> poi = sym.solveset(der, x)  # Find the points of inflection
    >>> poi
    FiniteSet(-2, 1 - sqrt(6)/2, 1 + sqrt(6)/2)


Finally, we can take the second derivative and evaluate it at each point::

    >>> second_der = sym.diff(der, x)
    >>> for point in list(poi):  # We convert the poi to a list
    ...     print(point, (second_der.subs({x: point})) > 0)
    -2 False
    1 - sqrt(6)/2 True
    1 + sqrt(6)/2 False

We see that 2 points of inflection give negative second derivative (so they are
local maxima), whereas the other is a local minimum.

Lab sheet
---------

Discuss the Sympy labsheet showing that there are other things that are covered
as well.

Highlight that this and the labsheet is a brief overview and that there is a
large amount of capability in Sympy.
