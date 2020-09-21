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

## Calculus

### Introduction

As of 2020, the A-level syllabus includes Calculus which
https://www.cambridgeinternational.org/Images/415060-2020-2022-syllabus.pdf
describes as:

> Calculus: this is a fundamental element which describes change in dynamic situations and underlines the links between functions and graphs.

In practice this often means:

- taking limits of functions;
- differentiating functions;
- integrating functions.

Here we will see how to instruct a computer to carry out these techniques.

## Tutorial

We will solve the following problem using a computer to assist with the technical aspects:


---

Consider the function \\(f(x)= \frac{24 x \left(a - 4 x\right) + 2 \left(a - 8 x\right) \left(b - 4 x\right)}{\left(b - 4 x\right)^{4}}\\)

1. Given that \\(\frac{df}{dx}|_{x=0}=0\\), \\(\frac{d^2f}{dx^2}|_{x=0}=-1\\) and that \\(b>0\\) find the values of \\(a\\) and \\(b\\).
2. For the specific values of \\(a\\) and \\(b\\) find:
    1. \\(\lim_{x\to 0}f(x)\\);
    2. \\(\lim_{x\to \infty}f(x)\\);
    3. \\(\int f(x) dx\\);
    4. \\(\int_{5}^{20} f(x) dx\\).

---

Sympy is once again the library we will use for this.

We will start by creating a variable `expression` that has the value of the expression of \\(f(x)\\):

```{code-cell} ipython3
import sympy as sym

x = sym.Symbol("x")
a = sym.Symbol("a")
b = sym.Symbol("b")
expression = (2 * (12 * x * (a - 4 * x) + (a - 8 * x) * (b - 4 * x))) / (
    (b - 4 * x) ** 4
)
expression
```

now we can will use `sympy.diff` to calculate the derivative. This tool takes two inputs: 

- the first is the expression we are differentiating. Essentially this is the numerator of \\(\frac{df}{dx}\\).
- the first is the variable we are differentiating for. Essentially this is the denominator of \\(\frac{df}{dx}\\).

**Note** that we have imported `import sympy as sym` so we are going to write `sym.diff`:

```{code-cell} ipython3
derivative = sym.diff(expression, x)
derivative
```

Let us factorise that to make it slightly clearer:

```{code-cell} ipython3
sym.factor(derivative)
```

We will now create the first equation, which is obtained by substituting \\(x=0\\) in to the value of the derivative and equating that to \\(\pi\\):

```{code-cell} ipython3
first_equation = sym.Eq(derivative.subs({x: 0}), 0)
first_equation
```

We will factor that equation:

```{code-cell} ipython3
sym.factor(first_equation)
```

Now we are going to create the second equation, substituting \\(x=0\\) in to the value of the second derivative. We calculate the second derivative by passing a third (optional) input to `sym.diff`:

```{code-cell} ipython3
second_derivative = sym.diff(expression, x, 2)
second_derivative
```

We equate this expression to \\(-1\\):

```{code-cell} ipython3
second_equation = sym.Eq(second_derivative.subs({x: 0}), -1)
second_equation
```

Now to solve the first equation to obtain a value for \\(a\\):

```{code-cell} ipython3
sym.solveset(first_equation, a)
```

Now to substitute that value for \\(a\\) and solve the second equation for \\(b\\):

```{code-cell} ipython3
second_equation = second_equation.subs({a: b / 3})
second_equation
```

```{code-cell} ipython3
sym.solveset(second_equation, b)
```

```{code-cell} ipython3
sym.root(192, 4)
```

Recalling the question we know that \\(b>0\\) thus: \\(b = 2\sqrt{2}\sqrt[4]{3}\\) and \\(a=\frac{2\sqrt{2}\sqrt[4]{3}}{3}\\).

We will substitute these values back and finish the question:

```{code-cell} ipython3
expression = expression.subs(
    {a: 2 * sym.sqrt(2) * sym.root(3, 4) / 3, b: 2 * sym.sqrt(2) * sym.root(3, 4)}
)
expression
```

**Note** that we are using the `sym.root` command for the generic \\(n\\)th root. 

We can confirm our findings:

```{code-cell} ipython3
sym.diff(expression, x).subs({x: 0})
```

```{code-cell} ipython3
sym.diff(expression, x, 2).subs({x: 0})
```

Now we will calculate the limits using `sym.limit`, these takes 3 inputs:

- The expression we are taking the limit of.
- The variable that is changing.
- The value that the variable is tending towards.

```{code-cell} ipython3
sym.limit(expression, x, 0)
```

```{code-cell} ipython3
sym.limit(expression, x, sym.oo)
```

Now we are going to calculate the **indefinite** integral using `sympy.integrate`. This tool takes 2 inputs as:

- the first is the expression we're integrating. This is the \\(f\\) in \\(\int_a^b f dx\\).
- the second is the remaining information needed to calculate the integral: \\(x\\).

```{code-cell} ipython3
sym.factor(sym.integrate(expression, x))
```

If we want to calculate a **definite** integral then instead of passing the single variable we pass a tuple which contains the variable as well as the bounds of integration:

```{code-cell} ipython3
sym.factor(sym.integrate(expression, (x, 5, 20)))
```

### How to


#### Calculate the derivative of an expression.

We can calculate the derivative of an expression using `sym.diff(<expression>, <variable>, [<degree>])`.

For example to compute \\(\frac{d (4 x ^ 3 + 2 x + 1}{dx}\\):

```{code-cell} ipython3
x = sym.Symbol("x")
expression = 4 * x ** 3 + 2 * x + 1
sym.diff(expression, x)
```

To compute the second derivative: \\(\frac{d ^ 2 (4 x ^ 3 + 2 x + 1}{dx ^ 2}\\)

```{code-cell} ipython3
sym.diff(expression, x, 2)
```

#### Calculate the indefinite integral of an expression.

We can calculate the indefinite integral of an expression using `sym.integrate(<expression>, <variable>)`.

For example to compute \\(\int 4x^3 + 2x + 1 dx\\):

```{code-cell} ipython3
sym.integrate(expression, x)
```

#### Calculate the definite integral of an expression.

We can calculate the definite integral of an expression using `sym.integrate(<expression>, (<variable>, <lower_bound>, <upper_bound>))`.

For example to compute \\(\int_0^4 4x^3 + 2x + 1 dx\\):

```{code-cell} ipython3
sym.integrate(expression, (x, 0, 4))
```

#### Use \\(\infty\\)

In sympy we can access \\(\infty\\) using `sym.oo`:

```{code-cell} ipython3
sym.oo
```

#### Calculate limits

We can calculate limits using `sym.limit(<expression>, <variable>, <value>)`.

For example to compute \\(\lim_{h \to 0} \frac{4(x - h)^3 + 2(x - h) + 1  - 4x^3 - 2x - 1}{h}\\):

```{code-cell} ipython3
h = sym.Symbol("h")
expression = (4 * x ** 3 + 2 * x + 1 - 4 * (x - h) ** 3 - 2 * (x - h) - 1) / h
sym.limit(expression, h, 0)
```

### Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. For each of the following functions calculate \\(\frac{df}{dx}\\), \\(\frac{d^2f}{dx^2}\\) and \\(\int f(x) dx\\).
    1. \\(f(x) = x\\)
    2. \\(f(x) = x ^(1/3)\\)
    3. \\(f(x) = 2 x (x - 3) (\sin(x) - 5)\\)
    4. \\(f(x) = \frac{3  x ^ 3 + 6 \sqrt{x} + 3}{3  x ^ {1 / 4}}\\)
2. Consider the function \\(f(x)=2x+1\\). By differentiating *from first principles* show that \\(f'(x)=2\\).
3. Consider the second derivative \\(f''(x)=6x+4\\) of some cubic function \\(f(x)\\).
    1. Find \\(f'(x)\\)
    2. You are given that \\(f(0)=10\\) and \\(f(1)=13\\), find \\(f(x)\\).
    3. Find all the stationary points of \\(f(x)\\) and determine their nature.
4. Consider the function \\(f(x)=\frac{2}{3}x ^ 3 + b x ^ 2 + 2 x + 3\\), where \\(b\\) is some undetermined coefficient.
    1. Find \\(f'(x)\\) and \\(f''(x)\\)
    2. You are given that \\(f(x)\\) has a stationary point at \\(x=2\\). Use this information to find \\(b\\).
    3. Find the coordinates of the other stationary point.
    4. Determine the nature of both stationary points.
5. Consider the functions \\(f(x)=-x^2+4x+4x\\) and \\(g(x)=-2x^3+5x^2-2x-1\\).
    1. Create a variable `turning_points` which has value the turning points of \\f(x)\\).
    2. Create variable `intersection_points` which has value of the points where \\(f(x)\\) and \\(g(x)\\) intersect.
    3. Using your answers to parts 2., calculate the area of the region between \\(f\\) and \\(g\\). Assign this value to a variable `area_of_shaded_region`.

+++

### References

#### How can I plot a function

It is possible to plot a function using Sympy using the `sym.plot` function:

```
sym.plot(f(x))
```

So for example, here is a plot of \\(f(x)=x^2 + 3x + 1\\):

```{code-cell} ipython3
:tags: [nbval-ignore-output]

sym.plot(x ** 2 + 3 * x + 1);
```

It is possible to specify the x limits and combine it with other plots:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

sym.plot(x ** 2 + 3 * x + 1, xlim=(-5, 5));
```

**This plotting solution is fine it you want to take a look at a function quickly but it is not recommended.** The main library for plotting is called `matplotlib` and we will see how to use that at a later date.

- Here is the Sympy documentation for plotting: https://docs.sympy.org/latest/modules/plotting.html
- Here is a the official matplotlib documentation: https://matplotlib.org
