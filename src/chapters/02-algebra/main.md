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

## Algebra

### Introduction

As of 2020, the A-level syllabus includes Algebra which
https://www.cambridgeinternational.org/Images/415060-2020-2022-syllabus.pdf
describes as:

> Algebra: this is an essential tool which supports and expresses mathematical
> reasoning and provides a means to generalise across a number of contexts.

In practice this often means:

- Manipulating numeric expressions;
- Manipulating symbolic expressions;
- Solving equations.

We can use a computer to carry out some of these techniques.

## Tutorial

To demonstrate the ways in which we can use a computer to assist with Algebra we
will solve the following two problems:

---

1. Rationalise the denominator of \\(\frac{1}{\sqrt{2} + 1}\\)
2. Consider the quadratic: \\(f(x)=2x ^ 2 + x + 1\\):
  1. Calculate the descriminant of the quadratic equation \\(2x ^ 2 + x + 1 =
     0\\). What does this tell us about the solutions to the equation? What
     does this tell us about the graph of \\(f(x)\\)?
  2. By completing the square, show that the minimum point of \\(f(x)\\) is
     \\(\left(-\frac{1}{4}, \frac{7}{8}\right)\\)

---

To do this we will be using a specific collections of tools available in Python.
Often specific sets of tools are separated in to things called **libraries**. We
start by telling Python that we want to use the specific library for **symbolic
mathematics**:

```{code-cell} ipython3
import sympy
```

This allows us to solve the first part of the question. First we create a variable `expression` and **assign** it a value of \\(\frac{1}{\sqrt{2} + 1}\\).

```{code-cell} ipython3
expression = 1 / (sympy.sqrt(2) + 1)
expression
```

**Note** that this is not what would happen if we plugged the above in to a basic calculator, it would instead give us a value of:

```{code-cell} ipython3
float(expression)
```

The `sympy` library has a diverse set of tools available, one of which is to
algorithmically attempt to simplify an expression. Here is how we do that:

```{code-cell} ipython3
sympy.simplify(expression)
```

This implies that:

\\[
    \frac{1}{\sqrt{2} + 1} = -1 + \sqrt{2}
\\]

If we multiply both sides by \\({\sqrt{2} + 1}\\) we get:

\\[
    1=\frac{1}{\sqrt{2} + 1}\times \left(\sqrt{2} + 1\right) = \left(-1 + \sqrt{2}\right)\times \left(\sqrt{2} + 1\right)
\\]

The `sympy.simplify` command did not give us much insight in to what happened but we can further confirm that above manipulation by expanding \\(\left(-1 + \sqrt{2}\right)\times \left(\sqrt{2} + 1\right)\\). 

Here is how we do that:

```{code-cell} ipython3
sympy.expand((-1 + sympy.sqrt(2)) * (1 + sympy.sqrt(2)))
```

We see that `sympy` allows us to carry out basic expression manipulation. We will now consider the second part of the question:


---

2. Consider the quadratic: \\(f(x)=2x ^ 2 + x + 1\\):
  1. Calculate the descriminant of the quadratic equation \\(2x ^ 2 + x + 1 =
     0\\). What does this tell us about the solutions to the equation? What
     does this tell us about the graph of \\(f(x)\\)?
  2. By completing the square, show that the minimum point of \\(f(x)\\) is
     \\(\left(-\frac{1}{4}, \frac{7}{8}\right)\\)

---

We will start by reassigning the value of the variable `expression` to be the expression: \\(2x ^ 2 + x + 1\\).

```{code-cell} ipython3
x = sympy.Symbol("x")
expression = 2 * x ** 2 + x + 1
expression
```

**Recall** that the `**` symbol is how we communicate exponentiation.

**Note** we start by communicating to the code that `x` is going to be a symbolic variable.

We can immediately use this to compute the discriminant:

```{code-cell} ipython3
sympy.discriminant(expression)
```

Now we can complement this with our mathematical knowledge: if a quadratic has a negative descriminant then it does not have any roots and all the values are of the same sign as the coefficient of \\(x ^ 2 \\). Which in this case is \\(2>0\\).

We can confirm this by directly creating the equation. We do this by creating a variable `equation` and assigning it the equation which has a `lhs` and a `rhs`:

```{code-cell} ipython3
equation = sympy.Eq(lhs=expression, rhs=0)
equation
```

and asking Sympy to solve it:

```{code-cell} ipython3
sympy.solveset(equation)
```

Indeed the only solutions are imaginary numbers: the graph of \\(f(x)\\) is thus a convex parabola.

Let us know complete the square so that we can write:

\\[
    f(x) = a (x - b) ^ 2 + c
\\]

for some values of \\(a, b, c\\).

First let us create variables that have those 3 constants as value but also create a variable `completed_square` and assign it the general expression:

```{code-cell} ipython3
a, b, c = sympy.Symbol("a"), sympy.Symbol("b"), sympy.Symbol("c")
completed_square = a * (x - b) ** 2 + c
completed_square
```

We can expand this:

```{code-cell} ipython3
sympy.expand(completed_square)
```

We will now use sympy to solve the various equations that arise from comparing the coefficients of:

\\[
    f(x) = 2x ^2 + x + 1
\\]

with the completed square.

First, we see that the coefficient of \\(x ^ 2\\) gives us a simple equation:

\\[
    a = 2
\\]

For completeness we will write the code that solves this trivial equation:

```{code-cell} ipython3
equation = sympy.Eq(a, 2)
sympy.solveset(equation, a)
```

We will now substitute this value of \\(a\\) in to the completed square and update the variable with the new value:

```{code-cell} ipython3
completed_square = completed_square.subs({a: 2})
completed_square
```

**Note** the different types of brackets being used there: both `()` and `{}`. This is important and has specific meaning in Python which we will cover soon.

Now let us look at the expression with our two remaining constants:

```{code-cell} ipython3
sympy.expand(completed_square)
```

Comparing the coefficients of \\(x\\) we have the equation:
    
\\[
  - 4 b = 1  
\\]

```{code-cell} ipython3
equation = sympy.Eq(-4 * b, 1)
sympy.solveset(equation, b)
```

We will now substitute this value of \\(b\\) back in to our expression.

**Note** that we make a point to tell sympy to treat \\(1 / 4\\) symbolically and to not calculate the numeric value:

```{code-cell} ipython3
completed_square = completed_square.subs({b: -1 / sympy.S(4)})
completed_square
```

Expanding this to see our expression with the one remaining constant gives:

```{code-cell} ipython3
sympy.expand(completed_square)
```

We have a final equation for the constant term:

\\[
    c + 1 / 8 = 1
\\]

We will use sympy to find the value of \\(c\\):

```{code-cell} ipython3
sympy.solveset(sympy.Eq(c + sympy.S(1) / 8, 1), c)
```

As before we will substitute that in and update the value of `completed_square`:

```{code-cell} ipython3
completed_square = completed_square.subs({c: 7 / sympy.S(8)})
completed_square
```

Using this we can see that the there are indeed no values of \\(x\\) which give negative values of \\(f(x)\\) as \\(f(x)\\) is a square added to a constant.

The minimum is clearly when \\(x=-1/4\\) which gives: \\(f(-1/4)=7/8\\):

```{code-cell} ipython3
completed_square.subs({x: -1 / sympy.S(4)})
```

### How To


#### How to create a symbolic numeric value

To create a symbolic numerical value use `sympy.S`. For example:

```{code-cell} ipython3
value = sympy.S(3)
value
```

Note that if we combine a symbolic value with a non symbolic value it will automatically give a symbolic value:

```{code-cell} ipython3
1 / value
```

#### How to get the numerical value of a symbolic expression

We can get the numerical value of a symbolic value using `float` or `int`:

- `float` will give the numeric approximation in \\(\mathbb{R}\\)
- `int` will give the integer value

For example, let us create a symbolic numeric variable with value \\(\frac{1}{5}\\):

```{code-cell} ipython3
value = 1 / sympy.S(5)
value
```

To get the numerical value:

```{code-cell} ipython3
float(value)
```

If we wanted the integer value:

```{code-cell} ipython3
int(value)
```

**Note** this is not rounding to the nearest integer. It is returning the integer part.

+++

#### How to factor an expression

We use the `sympy.factor` tool to factor expressions:

```{code-cell} ipython3
sympy.factor(x ** 2 - 9)
```

#### How to expand an expression

We use the `sympy.expand` tool to expand expressions:

```{code-cell} ipython3
sympy.expand((x - 3) * (x + 3))
```

#### How to simplify an expression

We use the `sympy.simplify` tool to simplify an expression. 

```{code-cell} ipython3
sympy.simplify((x - 3) * (x + 3))
```

**Note** this will not always give the expected (or any) result. At times it could be more beneficial to use `sympy.expand` and/or `sympy.factor`.

+++

#### How to solve an equation

We use the `sympy.solveset` tool to solve an equation. It takes two values as inputs. The first is either:

- An expression for which a root is to be found
- An equation

The second is the variable we want to solve for. 

Here is how we can use Sympy to obtain the roots of the general quadratic:

\\[
    a x ^ 2 + bx + c
\\]

```{code-cell} ipython3
quadratic = a * x ** 2 + b * x + c
sympy.solveset(quadratic, x)
```

Here is how we would solve the same equation but not for \\(x\\) but for \\(b\\):

```{code-cell} ipython3
sympy.solveset(quadratic, b)
```

It is however clearer to specifically write the equation that we want to solve:

```{code-cell} ipython3
equation = sympy.Eq(a * x ** 2 + b * x + c, 0)
sympy.solveset(equation, x)
```

#### How to substitute a value in to an expression

Given a Sympy expression it is possible to substite values in to it using the `.subs()` tool. This takes the variables and their values in the following format:

```python
expression.subs({variable: value})
```

Note that it is possible to pass multiple variables at a time.

For example we can substitute the values for \\(a, b, c\\) in to our quadratic:

```{code-cell} ipython3
quadratic = a * x ** 2 + b * x + c
quadratic.subs({a: 1, b: sympy.S(7) / 8, c: 0})
```

### Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. Simplify the following expressions:
    1. \\(\frac{3}{\sqrt{3}}\\)
    2. \\(\frac{2 ^ {78}}{2 ^ {12}2^{-32}}\\)
    3. \\(8^0\\)
    4. \\(a^4b^{-2}+a^{3}b^{2}+a^{4}b^0\\)
2. Solve the following equations:
    1. \\(x + 3 = -1\\)
    2. \\(3 x ^ 2 - 2 x = 5\\)
    3. \\(x (x - 1) (x + 3) = 0\\)
    4. \\(4 x ^3 + 7x - 24 = 1\\)
3. Consider the equation: \\(x ^ 2 + 4 - y = \frac{1}{y}\\):
    1. Find the solution to this equation for \\(x\\).
    2. Obtain the specific solution when \\(y = 5\\). Do this in two ways: subsitute the value in to your equation and substitue the value in to your solution.
4. Consider the quadratic: \\(f(x)=4x ^ 2 + 16x + 25\\):
  1. Calculate the descriminant of the quadratic equation \\(4x ^ 2 + 16x + 25 =
     0\\). What does this tell us about the solutions to the equation? What
     does this tell us about the graph of \\(f(x)\\)?
  2. By completing the square, show that the minimum point of \\(f(x)\\) is
     \\(\left(-2, 9\right)\\)
5. Consider the quadratic: \\(f(x)=-3x ^ 2 + 24x - 97\\):
  1. Calculate the descriminant of the quadratic equation \\(-3x ^ 2 + 24x - 97 =
     0\\). What does this tell us about the solutions to the equation? What
     does this tell us about the graph of \\(f(x)\\)?
  2. By completing the square, show that the minimum point of \\(f(x)\\) is
     \\(\left(4, -97\right)\\)
6. Consider the function \\(f(x) = x^ 2 +ax + b\\).
  1. Given that \\(f(0) = 0\\) and \\(f(3) = 0\\) obtain the values of \\(a\\) and \\(b\\).
  2. By completing the square confirm that graph of \\(f(x)\\) has a line of symmetry at \\(x=\frac{3}{2}\\)

+++

### Reference


#### Why is some code in separate libraries?

When we run the `import sympy` command we are telling Python that we want to use a specific set of tools. We will see other examples of this throughout this course.

One of the advantages of having code in libraries is that it is more efficient for Python to only use what is needed.

There are two types of Python libraries:

- Those that are part of the so called "standard library": these are part of Python itself.
- Those that are completely seperate: Sympy is one such example of this.

This seperation allows for the development of tools to be not dependent on each others. The developers of Sympy do not need to coordinate with the developers of Python to make new releases of the software.

#### Why do we need to use sympy?

Sympt is the library for symbolic mathematics. There are other python libraries for carrying out mathematics in Python.

For example, let us compute the value of the following expression:

\\[
    (\sqrt{2} + 2) ^ 2 - 2
\\]

We could compute this using the `math` library (for the square root tool):

```{code-cell} ipython3
import math

(math.sqrt(2) + 2) ** 2 - 2
```

We could also make use of the fact that we do not need a square root tool at all:

\\[
    (\sqrt{2} + 2) ^ 2 - 2 = (2 ^ {1 / 2} + 2) ^ 2 - 2
\\]

```{code-cell} ipython3
(2 ** (1 / 2) + 2) ** 2 - 2
```

We see that in both those instances, we have a numeric value for the expression that seems to be precise up to 14 decimal places.

However, that is **not** the exact value of that expression. The exact value of the expression needs to be computed symbolically:

```{code-cell} ipython3
expression = (sympy.sqrt(2) + 2) ** 2 - 2
sympy.expand(expression)
```

This is just one example of why Sympy is an effective tool for mathematicians. The other one seen in this chapter is being able to compute expressions with no numerical value at all:

```{code-cell} ipython3
sympy.factor(a ** 2 - b ** 2)
```

#### Why do I sometimes see `from sympy import *`?

There a number of resources available from which you can learn to use Sympy. In some isntances you will not see `import sympy` but instead you will see `from sympy import *`.

**This it not a good way to do it.**

What this does is taking all the tools inside of sympy and putting it at the same level of all the other tools available to you.

The problem with doing this is that it no longer makes your code clear.

An example of this are trigonometric functions. These exist in a number of libraries:

```{code-cell} ipython3
import math
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

If we chose to import all the functionality using `from sympy import *` then we cannot tell immediately which function we are using (except from its output):

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

**It is never recommended to use** `import *` this makes your code less clear and you are more likely to make mistakes when your code is not clear.

+++

#### Why do I sometimes see `import sympy as sym`?

In some resources you will see that instead of `import sympy` people use: `import sympy as sym`. This is common and take advantage of the fact that Python can import a library and give it an alias/nickname at the same time:

```python
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

**It is important** when doing this to use accepted conventions for these nicknames. For sympy, an accepted convention is indeed `import sympy as sym`.

+++

#### Are there other resources for learning sympy?

There are a large number of resources for learning Sympy. Not all concentrate on the algebra that we have considered in this chapter, and we will be covering further Sympy functionality in the next chapters.

Here are some resources:

- The main sympy documentation: https://docs.sympy.org/latest/index.html
- The scientific python lecture notes chapter on sympy: https://scipy-lectures.org/packages/sympy.html
- A short tutorial: https://github.com/drvinceknight/Python-Mathematics-Handbook/blob/master/01-Symbolic-mathematics-with-Sympy.ipynb

There are numerous other resources on the web, if you would like to know if they are reliable or not do not hesitate to ask.
