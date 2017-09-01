---
layout: post
title:  "Lab Sheet 07: Symbolic Calculus"
comments: true
---

In this lab sheet we will see how to carry out basic aspects of Calculus
(limits, differentiation and integration) with Python.

**Building blocks**

1. Calculating limits.

   [A video describing the concept.](https://youtu.be/hJ4MSWx-EhU)

   [A video demo.](https://youtu.be/5cjxM38yoCY)

   It is possible to calculate limits easily with SymPy. Let us consider the
   following function as a running example:

   $$f(x)=1/x$$

   First let us define this function in Python as a function:

   ```python
   >>> import sympy as sym
   >>> def f(x):
   ...     return 1 / x
   >>> f(2)
   0.5

   ```

   We can now pass it symbolic variable:

   ```python
   >>> x  = sym.symbols('x')
   >>> f(x)
   1/x

   ```

   We can compute the limits at \\(\pm\infty\\):

   ```python
   >>> sym.limit(f(x), x, sym.oo)
   0
   >>> sym.limit(f(x), x, -sym.oo)
   0
   >>> sym.limit(f(x), x, +sym.oo)
   0

   ```

   We can also compute the limit at \\(0\\) however we must be careful here (you
   will recall from basic calculus that the limit depends on the direction):

   ```python
   >>> sym.limit(f(x), x, 0)  # The default direction of approach is positive.
   oo
   >>> sym.limit(f(x), x, 0, dir="+")
   oo
   >>> sym.limit(f(x), x, 0, dir="-")
   -oo

   ```

   **Experiment with caculating the limit of different functions.**

2. Differentiation.

   [A video describing the concept.](https://youtu.be/-03PrW-S_-w)

   [A video demo.](https://youtu.be/EDv2eEH47J0)

   We can use SymPy to carry out differentiation:

   ```python
   >>> sym.diff(f(x), x)
   -1/x**2
   >>> sym.diff(sym.cos(x), x)
   -sin(x)

   ```

   We can carry out various orders of differentiation. These all give the second
   order derivative of \\(\cos(x)\\):

   ```python
   >>> sym.diff(sym.diff(sym.cos(x), x), x)
   -cos(x)
   >>> sym.diff(sym.cos(x), x, x)
   -cos(x)
   >>> sym.diff(sym.cos(x), x, 2)
   -cos(x)

   ```

   SymPy can handle differentiation of functions with multiple variables (you
   will learn more about this in further Calculus):

   ```python
   >>> y = sym.symbols('y')
   >>> sym.diff(sym.cos(x) * sym.sin(y), x)  # Differentiating with respect to x
   -sin(x)*sin(y)
   >>> sym.diff(sym.cos(x) * sym.sin(y), y)  # Differentiating with respect to y
   cos(x)*cos(y)

   ```

   Finally it is also possible for SymPy to differentiate hypothetical functions
   (ones that we do not know anything about):

   ```python
   >>> g = sym.Function('g')  # We create g as a generic function
   >>> sym.diff(g(x), x, 2)
   Derivative(g(x), x, x)

   ```

   **Try and experiment with differentiating more complicated functions.**

3. Integration.

   [A video describing the concept.](https://youtu.be/w9RpnPGR4O0)

   [A video demo.](https://youtu.be/viGfOqV6qiA)

   As well as differentiation it is possible to carry out integration.

   We can do both definite and indefinite integrals:

   ```python
   >>> sym.integrate(f(x), x)  # An indefinite integral
   log(x)
   >>> sym.integrate(f(x), (x, sym.exp(1), sym.exp(5)))  # A definite integral
   4

   ```

   We can use this to verify the [fundamental theorem of
   calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus) for
   the specific example of our function \\(f\\):

   ```python
   >>> sym.integrate(sym.diff(f(x), x), x)
   1/x

   ```

   We can also verify this for generic functions:

   ```python
   >>> g = sym.Function('g')
   >>> sym.integrate(sym.diff(g(x), x), x) == g(x)
   True
   >>> sym.diff(sym.integrate(g(x), x), x) == g(x)
   True

   ```

   **Experiment with integrating other functions.**

4. Plotting. It is possible to use SymPy to create plots.

   [A video describing the concept.](https://youtu.be/ue9BBmvS7zw)

   [A video demo.](https://youtu.be/g-aWhcFqnec)

   To view these in jupyter we need to run this line:

   ```python
   %matplotlib inline
   ```

   We can then create plots using the `plot` command:

   ```python
   >>> sym.plot(f(x), (x, -1, 1))
   <...

   ```

   That's not very clear, let us modify the limits on the y axis.

   ```python
   >>> sym.plot(f(x), (x, -1, 1), ylim=(-10, 10))
   <...

   ```

   We can also choose to modify the labels on the axes:

   ```python
   >>> sym.plot(f(x), (x, -1, 1), ylim=(-10, 10), xlabel=None, ylabel="$1/x$")
   <...

   ```

   Finally we can also combine various plots of different functions together. To
   do this we build each plot separately (telling Python not to `show` them) and
   then combine them:

   ```python
   >>> p1 = sym.plot(f(x), (x, -1, 1), show=False)
   >>> p2 = sym.plot(x, (x, -1, 1), show=False, line_color="red")
   >>> p1.extend(p2)
   >>> p1.ylim = (-10, 10)
   >>> p1.xlabel = None  # Try using strings here
   >>> p1.ylabel = None
   >>> p1.show()

   ```

   It is also possible to save a file of the graph. Depending on how you name
   the file the type of tile will be different:

   ```python
   >>> p1.save("my_plot.pdf")  # Try `.png` etc...

   ```

   **Attempt to create plots of other functions.**

5. **TICKABLE: Worked example**

   [A video describing the concept.](https://youtu.be/RZFC6kHapuY)

   [A video demo.](https://youtu.be/7PhZKOkZPiY)

   We are going to use the above to attempt to find and classify all points of
   inflection for the following quartic function:

   $$f(x) = - x^{4} + 9 x^{2} + 4 x - 12$$

   First let us take a look at the function:

   ```python
   >>> def f(x):
   ...     return  -x ** 4 + 9 * x ** 2 + 4 * x - 12
   >>> sym.plot(f(x), (x, -20, 20) , ylim=(-20, 20))
   <...

   ```

   Let us find the roots of the functions:

   ```python
   >>> sym.solveset(f(x), x)
   {-2, 1, 3}

   ```

   We have a quatric so one of those roots (of which there are only 3) must be
   repeated, let us see if we can factor our function:

   ```python
   >>> f(x).factor()
   -(x - 3)*(x - 1)*(x + 2)**2

   ```

   We see that \(-2\) is a repeated root.

   Let us confirm the limiting behaviour of our function:

   ```python
   >>> sym.limit(f(x), x, sym.oo)
   -oo
   >>> sym.limit(f(x), x, -sym.oo)
   -oo

   ```

   Finally, we also see that there are 3 points of inflection so let us find
   them:

   ```python
   >>> poi = sym.solveset(sym.diff(f(x), x), x)
   >>> poi
   {-2, 1 + sqrt(6)/2, -sqrt(6)/2 + 1}

   ```

   Let us now evaluate which of these gives a positive or negative value of the
   second derivative:

   ```python
   >>> for point in list(poi):  # We convert the poi to a list
   ...     print(point, (sym.diff(f(x), x, 2).subs({x: point})) > 0)
   -2 False
   1 + sqrt(6)/2 False
   -sqrt(6)/2 + 1 True

   ```

   We see that 2 points of inflection give negative second derivative (so they
   are local maxima), whereas \\(-\sqrt{6}/2+1\\) is a local minimum. This
   confirms the plot.

   **Further work**

   These questions aim to push a bit further.

6. Consider the function below:

   $$f(x) =- x^{4} + 10 x^{3} - 29 x^{2} + 8 x + 48$$

   Identify the roots and limits (at \\(\pm\infty\\)) of the function and
   confirm this with a plot.

7. For the function of question 6, identify and classify all points
   of inflection.

8. There are various algebraic relationships on limits:

   $$\lim_{x\to a}[f(x)+g(x)]=\lim_{x\to a}f(x) + \lim_{x\to a}g(x)$$

   $$\lim_{x\to a}[f(x)\times g(x)]=\lim_{x\to a}f(x) \times \lim_{x\to a}g(x)$$

   $$\lim_{x\to a}[f(x)/g(x)]=\lim_{x\to a}f(x) / \lim_{x\to a}g(x) \text{ if } \lim_{x\to a}g(a)\ne 0$$

   Confirm these for the following particular examples:

    $$f(x) = x^2 + x$$

    $$g(x) = 1 / (x ^ 2 + 1)$$

9. The point of this question is to investigate the definition of a derivative:

   $$\frac{df}{dx}=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$$

   1. Consider \\(f(x) = x^3 + 3x - 20\\);
   2. Compute \\(\frac{f(x+h)-f(x)}{h}\\);
   3. Compute the above limit as \\(h\to 0\\) and verify that this is the
      derivative of \\(f\\).
