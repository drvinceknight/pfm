---
layout: post
title:  "Lab Sheet 09: Differential Equations"
comments: true
---

The final topic that we will consider is the study of differential equations.

**Building blocks**

1. Solving differential equations.

   [A video describing the concept.](https://youtu.be/FGv5-AnyXDI)

   [A video demo.](https://youtu.be/tLwmMUZGIxU)

   We can use SymPy to solve differential equations. For example:

   $$\frac{dy}{dx}=y$$

   ```python
   >>> import sympy as sym
   >>> y = sym.Function('y')
   >>> x = sym.symbols('x')
   >>> sol = sym.dsolve(sym.Derivative(y(x), x) - y(x), y(x))
   >>> sol
   Eq(y(x), C1*exp(x))

   ```

   The output given is an instance of the SymPy equation class that states:

   $$y(x) = C1e^{x}$$

   Let us verify that the solution is correct:

   ```python
   >>> sym.diff(sol.rhs, x) == sol.rhs
   True

   ```

   Here is the more general equation:

   $$\frac{dy}{dx}=ky$$

   ```python
   >>> k = sym.symbols('k')
   >>> sol = sym.dsolve(sym.Derivative(y(x), x) - k * y(x), y(x))
   >>> sol
   Eq(y(x), C1*exp(k*x))
   >>> sym.diff(sol.rhs, x) == k * sol.rhs
   True

   ```

   **Experiment with solving a modified version of the differential equation
   considered here.**

2. Higher order differential equations.

   [A video describing the concept.](https://youtu.be/yDr0Fwiu-Tc)

   [A video demo.](https://youtu.be/DjYHy2qOXGw)

   We can also solve higher order differential equations. For example, the
   following can be used to model the position of a mass on a spring:

   $$m\frac{d^2x}{dt^2}+c\frac{dx}{dt}+kx=0$$

   ```python
   >>> m, c, k, t = sym.symbols('m, c, k, t')
   >>> x = sym.Function('x')
   >>> sym.dsolve(m * sym.Derivative(x(t), t, 2) + c * sym.Derivative(x(t), t) + k * x(t), x(t))
   Eq(x(t), C1*exp(t*(-c - sqrt(c**2 - 4*k*m))/(2*m)) + C2*exp(t*(-c + sqrt(c**2 - 4*k*m))/(2*m)))

   ```

   **Experiment with solving a modified version of the differential equation
   considered here.**

3. Systems of differential equations.

   [A video describing the concept.](https://youtu.be/FTSKHQJKzzg)

   [A video demo.](https://youtu.be/Q_XVeh9yWUI)

   We can solve systems of differential equations like the following:

   $$
   \begin{align}
   \frac{dx}{dt} &= 1-y\\
   \frac{dy}{dt} &= 1-x\\
   \end{align}
   $$

   We still use `dsolve` we just pass it both equations as an argument:

   ```python
   >>> eq1 = sym.Derivative(x(t), t) - 1 + y(t)
   >>> eq2 = sym.Derivative(y(t), t) - 1 + x(t)
   >>> sym.dsolve((eq1, eq2))
   [Eq(x(t), -C1*exp(-t) - C2*exp(t) + 1), Eq(y(t), -C1*exp(-t) + C2*exp(t) + 1)]

   ```

   The solution is given as:

   $$
   \begin{align}
   x(t)&=-C_1e^{-t}-C_2e^{t} + 1\\
   y(t)&=-C_1e^{-t}-C_2e^{t} + 1\\
   \end{align}
   $$

   **Experiment with solving a modified version of the differential equations
   considered here.**

4. **TICKABLE: Worked example**: Solving and visualising the solution of a differential
   equation.

   [A video describing the concept.](https://youtu.be/S3GsOrh8FpE)

   [A video demo.](https://youtu.be/MvWkpqc41bI)

   Let us solve the following differential equation:

   $$\frac{dy}{dx}+4y=5e^{x}$$

   ```python
   >>> y, x = sym.Function('y'), sym.symbols('x')
   >>> eq = sym.Derivative(y(x), x) + 4 * y(x) - 5 * sym.exp(x)
   >>> sol = sym.dsolve(eq, y(x))
   >>> sol
   Eq(y(x), (C1 + exp(5*x))*exp(-4*x))

   ```

   As before the right hand side of our equation has a constant of integration
   which defines a whole family of solutions.

   However, because this is a first order differential equation, only one of
   those equations will go through any given point. So let us assume that
   \\(y(0)=1)\\) and find the particular solution of our differential equation.

   ```python
   >>> C1 = sym.symbols('C1')  # We're going to use this as a symbolic variable
   >>> boundary_cond = sym.Eq(sol.rhs.subs({x: 0}), 1)
   >>> boundary_cond
   Eq(C1 + 1, 1)
   >>> particular_constant = sym.solveset(boundary_cond, C1)
   >>> particular_constant
   {0}

   ```

   So we can now create the particular solution:

   ```python
   >>> particular_sol = sol.subs({C1: list(particular_constant)[0]})
   >>> particular_sol
   Eq(y(x), exp(x))

   ```

   We can plot this:

   ```python
   >>> sym.plot(particular_sol.rhs, (x, 0, 10))
   <...

   ```

   **Further work**

   These questions aim to push a bit further.

5. Find the general solutions to the following 4 differential equations:

   1. \\(\frac{dy}{dx}-6y=3e^x\\)
   2. \\(\frac{dy}{dx}+\frac{x(2x-3)}{x^2+1}=\sin(x)\\)
   3. \\(\frac{d^2y}{dx^2}-y=\sin(5x)\\)
   4. \\(\frac{d^2y}{dx^2}+2\frac{dy}{dx}+2x=\cosh(x)\\)

6. For each of the differential equations from question 5, obtain
   particular solutions with the corresponding conditions **and plot** the
   solutions.

   1. \\(y(0)=3\\)
   2. \\(y(0)=4\\)
   3. \\(y(3)=1, y'(3)=0\\)
   4. \\(y(1)=2, y'(1)=72\\)

   (Hint: to be able to solve the systems of linear equations for 3 and 4 you
   can use linear algebra or perhaps look at the `sympy` function: `linsolve`.)

7. The love story between Romeo and Juliet can be modelled with the
   following system of differential equations:

   $$\begin{cases} \frac{dx}{dt} = -y\\
   \frac{dy}{dt} = .7x \end{cases}$$

   Where \\(x(t)\\) represents the affection of Juliet towards Romeo and
   \\(y(t)\\) the affection of Romeo towards Juliet (negative affection
   represents 'hatred').

   Solve this system of equations and, assuming that Romeo is initially
   attracted to Juliet (\\(y(0)=1\\)) but that Juliet is initially indifferent
   to Romeo (\\(x(0)=0\\)), describe the long term relationship between the two
   characters.

   Describe the behaviour of the system if Romeo and Juliet are initially
   indifferent to each other.

8. A battle between two armies can be modelled with the following set of
   differential equations:

   $$\begin{cases}
     \frac{dx}{dt} = - y\\
     \frac{dy}{dt} = -5x
   \end{cases}$$

   Obtain the solution to this system of equations. Assuming that \\(x(0)=100\\)
   and that \\(y(0)=700\\) plot the two solutions of the equations, which army
   wins this battle? When does the battle end?

# Further resources

- [SymPy documentation for solving differential
  equations.](http://docs.sympy.org/dev/modules/solvers/ode.html)
