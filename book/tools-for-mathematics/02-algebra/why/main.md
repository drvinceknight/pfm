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

# Further information

## Why is some code in separate libraries?

When we run the `import sympy` command we are telling Python that we want to use
a specific set of tools. We will see other examples of this throughout this
course.

One of the advantages of having code in libraries is that it is more efficient
for Python to only use what is needed.

There are two types of Python libraries:

- Those that are part of the so called "standard library": these are part of
  Python itself.
- Those that are completely separate: `sympy` is one such example of this.

This separation allows for the development of tools to be not dependent on each
others. The developers of `sympy` do not need to coordinate with the developers
of Python to make new releases of the software.

## Why do we need to use sympy?

`sympy` is the library for symbolic mathematics. There are other python libraries
for carrying out mathematics in Python.

For example, let us compute the value of the following expression:

$$
    (\sqrt{2} + 2) ^ 2 - 2
$$

We could compute this using the `math` library (for the square root tool):

```{code-cell} ipython3
import math

(math.sqrt(2) + 2) ** 2 - 2
```

We could also make use of the fact that we do not need a square root tool at all:

$$
    (\sqrt{2} + 2) ^ 2 - 2 = (2 ^ {1 / 2} + 2) ^ 2 - 2
$$

```{code-cell} ipython3
(2 ** (1 / 2) + 2) ** 2 - 2
```

We see that in both those instances, we have a numeric value for the expression
that seems to be precise up to 14 decimal places.

However, that is **not** the exact value of that expression. The exact value of
the expression needs to be computed symbolically:

```{code-cell} ipython3
import sympy

expression = (sympy.sqrt(2) + 2) ** 2 - 2
sympy.expand(expression)
```

This is one example of why `sympy` is an effective tool for mathematicians.
The other one seen in this chapter is being able to compute expressions with no
numerical value at all:

```{code-cell} ipython3
a = sympy.Symbol("a")
b = sympy.Symbol("b")
sympy.factor(a ** 2 - b ** 2)
```

## Why do I sometimes see `from sympy import *`?

There a number of resources available from which you can learn to use `sympy`. In
some instances you will not see `import sympy` but instead you will see `from sympy import *`.

**This it not a good way to do it.**

What this does is taking all the tools inside of sympy and putting it at the
same level of all the other tools available to you.

The problem with doing this is that it no longer makes your code clear.

An example of this are trigonometric functions. These exist in a number of
libraries:

```{code-cell} ipython3
import math
```

```{code-cell} ipython3
import sympy
```

```{code-cell} ipython3
sympy.cos(0)
```

```{code-cell} ipython3
math.cos(0)
```

One however allows us to carry out exact computations:

```{code-cell} ipython3
sympy.cos(sympy.pi / 4)
```

```{code-cell} ipython3
math.cos(math.pi / 4)
```

If we chose to import all the functionality using `from sympy import *` then we
cannot tell immediately which function we are using (except from its output):

```{code-cell} ipython3
from sympy import *
```

```{code-cell} ipython3
from math import *
```

```{code-cell} ipython3
cos(pi / 4)
```

In that case the second import has overwritten the first.

```{warning}
**It is never recommended to use** `import *` this makes your code less clear
and you are more likely to make mistakes when your code is not clear.
```

## How to extract a solution from the output of `sympy.solveset`?

In some cases you might want to directly access the items in a solution set. For
example if consider the equation $(x - 1)(x -
2)$.

```{code-cell} ipython3
import sympy as sym

x = sym.Symbol("x")
expression = (x - 1) * (x - 2)
equation = sym.Eq(expression, 0)
set_of_solutions = sym.solveset(equation, x)
set_of_solutions
```

The `set_of_solutions` has value the **set** of solutions of the equation. If we
wanted to access them directly we can use the following:

```{code-cell} ipython3
tuple_of_solutions = set_of_solutions.args
tuple_of_solutions
```

This creates a **finite** ordered tuple of the solutions. We can use concepts
that are covered in {ref}`how_to_access_particular_elements_in_a_tuple` to
access them directly. Because there are two roots we can use the following to
create two new variables:

```{code-cell} ipython3
x1, x2 = tuple_of_solutions
```

Let us substitute these value directly in to the expression:

```{code-cell} ipython3
expression.subs({x: x1})
```

```{code-cell} ipython3
expression.subs({x: x2})
```

Note that this is not always possible to get a finite ordered tuple of the
solutions, for example there are some equations
where the set of solutions is an infinite set:

```{code-cell} ipython3
equation = sym.Eq(sym.cos(x / 5), 0)
set_of_solutions = sym.solveset(equation, x)
set_of_solutions
```

In this case, `set_of_solutions.args` does not necessarily make sense to use.

## Why do I sometimes see `import sympy as sym`?

In some resources you will see that instead of `import sympy` people use:
`import sympy as sym`. This is called **aliasing**. This is common and takes
advantage of the fact that Python can import a library and give it an
alias/nickname at the same time:

```
import <library> as <nickname>
```

So with sympy we can use:

```{code-cell} ipython3
import sympy as sym

sym.cos(sym.pi / 4)
```

There is nothing stopping you using whatever alias you want:

```{code-cell} ipython3
import sympy as a_poor_name_choice

a_poor_name_choice.cos(a_poor_name_choice.pi / 4)
```

```{attention}
**It is important** when aliasing to use accepted conventions for these
nicknames. For `sympy`, an accepted convention is indeed `import sympy as sym`.
```

## Are there other resources for learning sympy?

There are a large number of resources for learning `sympy`. Not all concentrate
on the algebra that we have considered in this chapter, and we will be covering
further `sympy` functionality in the next chapters.

Here are some resources:

- The main `sympy` documentation: <https://docs.sympy.org/latest/index.html>
- The scientific python lecture notes chapter on `sympy`:
  <https://scipy-lectures.org/packages/sympy.html>
- A short tutorial:
  <https://github.com/drvinceknight/Python-Mathematics-Handbook/>
