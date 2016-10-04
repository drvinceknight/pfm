---
layout: post
title:  "Lab Sheet 06: Symbolic Mathematics"
comments: true
---

In the previous week we saw a variety of different libraries:

```python
>>> import random
>>> import math

```

and there are many more. These libraries are part of the ''standard library''.
This means that they come with the base version of Python. There are a variety
of other libraries that exist and are developed independently. Some of these
come as standard with Anaconda.

This lab sheet will introduce one such library:
[SymPy](http://www.sympy.org/en/index.html) which allows us to do symbolic
mathematics.

**Building blocks**

These questions aim to show you the basic building blocks of programming

1. **TICKABLE** Exact valued computations.

   Using python we can calculate the square root and trigonometric values of
   numbers (we do this by importing the `math` library)::

   ```python
   >>> import math
   >>> math.sqrt(20)
   4.472...
   >>> math.cos(math.pi / 4)
   0.707...

   ```

   These are fine for numerical work but not when it comes to carrying out
   mathematical calculations, where for example we know that:

   $$\cos{\pi/4} = \sqrt{2} / 2$$

   We can use a python library called SymPy to import various new commands that
   allow for exact calculations.

   ```python
   >>> import sympy as sym
   >>> sym.sqrt(20)
   2*sqrt(5)
   >>> sym.cos(sym.pi / 4)
   sqrt(2)/2

   ```

   We also have access to complex numbers:

   ```python
   >>> sym.I ** 2
   -1
   >>> sym.sqrt(-20)
   2*sqrt(5)*I

   ```

   Whereas this would not have worked in the standard library:

   ```python
   >>> math.sqrt(-20)
   Traceback (most recent call last):
   ...
   ValueError: math domain error

   ```

   Note that if we **do** want to get the inexact numeric values we can:

   ```python
   >>> sym.sqrt(2).evalf()
   1.41...

   ```

   **Experiment with other mathematical functions: `tan`, `sin`, `exp`.**

2. **TICKABLE** Manipulating natural numbers.

   As well as exact numerics as described above, SymPy can also be used to
   explore the factors and primality of a number.

   ```python
   >>> N = 45 * 63
   >>> sym.isprime(N)
   False
   >>> sym.primefactors(N)
   [3, 5, 7]
   >>> all(sym.isprime(p) for p in sym.primefactors(N))  # All prime factors are prime
   True
   >>> sym.factorint(N)
   {3: 4, 5: 1, 7: 1}
   >>> N == 3 ** 4 * 5 * 7  # Checking the output of `factorint`
   True

   ```

   **Repeat the above example with a different value of `N`.**

3. **TICKABLE** Creating a symbolic variable.

   Using SymPy it is possible to carry out symbolic computations. To do this we
   need to creates instances of the SymPy Symbols class. We do this using the
   `symbols` function:

   ```python
   >>> x = sym.symbols('x')
   >>> x
   x
   >>> type(x)
   <class 'sympy.core.symbol.Symbol'>

   ```

   We can also create multiple symbols at a time:

   ```python
   >>> y, z = sym.symbols('y, z')
   >>> y, z
   (y, z)

   ```

   A symbolic variable no longer needs to have a numeric value to be
   manipulated:

   ```python
   >>> x + x
   2*x

   ```

   **Experiment with other symbolic manipulations.**

4. **TICKABLE** Manipulating symbolic expressions.

   We can substitute values in to our symbolic expressions:

   ```python
   >>> expr = x + y + z
   >>> 2 * expr
   2*x + 2*y + 2*z
   >>> 2 * expr.subs({z:x, y:2})  # Replacing z with x and y with 2
   4*x + 4

   ```

   We can also `factor`, `expand` and/or `simplify` them:

   ```python
   >>> expr2 = 2 * expr.subs({z:x, y:2})  # Repeating the previous
   >>> expr2
   4*x + 4
   >>> expr2.factor()
   4*(x + 1)

   ```

   Here is another example:

   ```python
   >>> alpha, beta = sym.symbols('alpha, beta')
   >>> ((alpha + beta) ** 2).expand()
   alpha**2 + 2*alpha*beta + beta**2

   ```

   **Experiment with other expressions and `expand`/`simplify`.**

5. **TICKABLE** Solving equations.

   Sympy has the ability to solve equations. For example let us solve the
   following quadratic:

   $$x^2 + 3x - 2=0$$

   We do this using the `solveset` function

   ```python
   >>> sym.solveset(x ** 2 + 3 * x - 2, x)
   {-3/2 + sqrt(17)/2, -sqrt(17)/2 - 3/2}

   ```

   If our equation had a non zero right hand side we can use one of two
   approaches:

   $$x^2 + 3x - 2=y$$

   1. Modify the equation so that it corresponds to an equation with zero right
      hand side:

      ```python
      >>> sym.solveset(x ** 2 + 3 * x - 2 - y, x)
      {-sqrt(4*y + 17)/2 - 3/2, sqrt(4*y + 17)/2 - 3/2}

      ```

   2. Create an `Eq` object:

      ```python
      >>> eqn = sym.Eq(x ** 2 + 3 * x - 2, y)
      >>> sym.solveset(eqn, x)
      {-sqrt(4*y + 17)/2 - 3/2, sqrt(4*y + 17)/2 - 3/2}

      ```

   We can also specify a domain. For example the following equation has two
   solutions (it's a quadratic):

   $$x^2 = -9$$

   ```python
   >>> sym.solveset(x ** 2 + 9, x)
   {-3*I, 3*I}

   ```

   However if we restrict ourselves to the Reals this is no longer the case:

   ```python
   >>> sym.solveset(x ** 2 + 9, x, domain=sym.S.Reals)
   EmptySet()

   ```

   **Experiment with solving different equations.**

6. **Worked example**

   In this example we are going to investigate the claim that the following
   polynomial expression can be used to generate primes:

   $$n^2 -79n+1601$$

   Here are a couple of values:

   ```python
   >>> def polynomial(n):
   ...    return n ** 2 - 79 * n + 1601
   >>> sym.isprime(polynomial(0))
   True
   >>> sym.isprime(polynomial(1))
   True
   >>> sym.isprime(polynomial(2))
   True
   >>> sym.isprime(polynomial(3))
   True

   ```

   Let us first identify for which numbers this is true.
   We will do this by using a while loop to keep generating the output of this
   polynomial until it is no longer prime:

   ```python
   >>> n = 0
   >>> while sym.isprime(polynomial(n)):  # Keep checking values until a composite
   ...    n += 1
   >>> n
   80

   ```

   We see that for natural numbers \\(n\\) from 0 to 80, the quadratic gives
   primes in our polynomial.

   ```python
   >>> p79 = polynomial(79)
   >>> sym.isprime(p79), p79
   (True, 1601)
   >>> sym.factorint(p79)
   {1601: 1}
   >>> p80 = polynomial(80)
   >>> sym.isprime(p80), p80
   (False, 1681)
   >>> sym.factorint(p80)
   {41: 2}

   ```

   We can list all these primes:

   ```python
   >>> for n in range(80):
   ...     p = polynomial(n)
   ...     print(p, sym.isprime(p))
   1601 True
   1523 True
   ...
   1447 True
   1523 True
   1601 True

   ```

   **Further work**

   These questions aim to push a bit further.

7. For what values of \\(n\\) are the following polynomials prime:

   $$p_1(n) = n^2+n+41$$

   $$p_2(n) = n^2-n+41$$

8. **TICKABLE** Use SymPy to verify that:

   $$n^2 -79n+1601 = (n - 40) ^ 2 + (n - 40) + 41$$

   Use this and the work done in question 7 to try and explain why
   \\(n^2-79n+1601\\) gives primes for \\(0\leq n \leq 79\\).

9. Solve the following equations (for \\(x\\):

   1. \\(x^2=−1\\)
   2. \\(x^2−53x+2a=0\\)
   3. \\(xy=\frac{y}{x}\\)

   Note that **not** all equations can be solved exactly. There is a whole area
   of mathematics that studies how to solve equations numerically. One such
   implementation is in a library called `scipy`. Investigate the `newton`
   method in scipy (which implements the
   [Newton-Raphson](https://en.wikipedia.org/wiki/Newton%27s_method) method for
   finding roots of equations) and use it to solve the following equation (try
   and solve it using SymPy first):

   $$sin(x)=x−1$$

   Here is a similar example (finding the solution to \\(x^2=9\\), which we
   could of course do exactly):

   ```python
   >>> from scipy.optimize import newton
   >>> def eqn(x):
   ...    return x ** 2 - 9
   >>> newton(eqn, 0)  # How could we obtain the other root?
   3.000...

   ```

10. Trigonometry

    Use SymPy's `simplify` method (and other things) to verify the follow
    trigonometric identities:

    1. \\(\sin^2(\theta) + \cos^2(\theta) = 1\\)
    2. \\(2\cos(\theta) \sin(\theta) = \sin(2\theta)\\)
    3. \\((1 - \cos(\theta)) / 2 = \sin^2(\theta / 2)\\)
    4. \\(\cos(n\pi)=(-1) ^ n\\) (for \\(n\in\mathbb{Z}\\) (Hint: you will need to
       look in to options that can be passed to `symbols` for this).

11. Use SymPy to write the first \\(10^6\\) prime numbers to file. Compare this
    file to [primes.csv]({{site.baseurl}}/assets/data/primes.csv) (not by hand!)
    and check that it is the same.

# Further resources

- [A SymPy tutorial given by some SymPy
  developers](https://www.youtube.com/watch?v=AqnpuGbM6-Q)
- [The SymPy documentation](http://docs.sympy.org/dev/index.html)
