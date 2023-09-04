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

# Solutions

## Question 1

> `1`. Create the following differential equations:

> `1`. $\frac{dy}{dx} = \cos(x)$

```{code-cell} ipython3
import sympy as sym

x = sym.Symbol("x")
y = sym.Function("y")

differential_equation = sym.Eq(sym.diff(y(x), x), sym.cos(x))
differential_equation
```

> `2`. $\frac{dy}{dx} = 1 - y$

```{code-cell} ipython3
differential_equation = sym.Eq(sym.diff(y(x), x), 1 - y(x))
differential_equation
```

> `3`. $\frac{dy}{dx} = \frac{x - 50}{10}$

```{code-cell} ipython3
differential_equation = sym.Eq(sym.diff(y(x), x), (x - 50) / 10)
differential_equation
```

> `4`. $\frac{dy}{dx} = y ^2 \ln (x)$

```{code-cell} ipython3
differential_equation = sym.Eq(sym.diff(y(x), x), y(x) ** 2 * sym.log(x))
differential_equation
```

> `5`. $\frac{dy}{dx} = (1 + y) ^ 2$

```{code-cell} ipython3
differential_equation = sym.Eq(sym.diff(y(x), x), (1 + y(x)) ** 2)
differential_equation
```

## Question 2

> `2`. Obtain the general solution for the equations in question 1.

> `1`. $\frac{dy}{dx} = \cos(x)$

```{code-cell} ipython3
differential_equation = sym.Eq(sym.diff(y(x), x), sym.cos(x))
sym.dsolve(differential_equation, y(x))
```

> `2`. $\frac{dy}{dx} = 1 - y$

```{code-cell} ipython3
differential_equation = sym.Eq(sym.diff(y(x), x), 1 - y(x))
sym.dsolve(differential_equation, y(x))
```

> `3`. $\frac{dy}{dx} = \frac{x - 50}{10}$

```{code-cell} ipython3
differential_equation = sym.Eq(sym.diff(y(x), x), (x - 50) / 10)
sym.dsolve(differential_equation, y(x))
```

> `4`. $\frac{dy}{dx} = y ^2 \ln (x)$

```{code-cell} ipython3
differential_equation = sym.Eq(sym.diff(y(x), x), y(x) ** 2 * sym.log(x))
sym.dsolve(differential_equation, y(x))
```

> `5`. $\frac{dy}{dx} = (1 + y) ^ 2$

```{code-cell} ipython3
differential_equation = sym.Eq(sym.diff(y(x), x), (1 + y(x)) ** 2)
sym.dsolve(differential_equation, y(x))
```

## Question 3

> `3`. Obtain the particular solution for the equations in question 1 with
> the following particular conditions:

> `1`. $y(0) = \pi$

```{code-cell} ipython3
conditions = {y(0): sym.pi}
differential_equation = sym.Eq(sym.diff(y(x), x), sym.cos(x))
sym.dsolve(differential_equation, y(x), ics=conditions)
```

> `2`. $y(2) = 3$

```{code-cell} ipython3
conditions = {y(2): 3}
differential_equation = sym.Eq(sym.diff(y(x), x), 1 - y(x))
sym.dsolve(differential_equation, y(x), ics=conditions)
```

> `3`. $y(50) = 1$

```{code-cell} ipython3
conditions = {y(50): 1}
differential_equation = sym.Eq(sym.diff(y(x), x), (x - 50) / 10)
sym.dsolve(differential_equation, y(x), ics=conditions)
```

> `4`. $y(e) = 1$

```{code-cell} ipython3
conditions = {y(sym.exp(1)): 1}
differential_equation = sym.Eq(sym.diff(y(x), x), y(x) ** 2 * sym.log(x))
sym.dsolve(differential_equation, y(x), ics=conditions)
```

> `5`. $y(-1) = 3$

```{code-cell} ipython3
conditions = {y(-1): 3}
differential_equation = sym.Eq(sym.diff(y(x), x), (1 + y(x)) ** 2)
sym.dsolve(differential_equation, y(x), ics=conditions)
```

## Question 4

> `4`. The rate of increase of a population ($p$) is equal to 1% of the size of the
> population.

> `1`. Define the differential equation that models this situation.

```{code-cell} ipython3
p = sym.Function("p")
t = sym.Symbol("t")

differential_equation = sym.Eq(sym.diff(p(t), t), p(t) / 100)
differential_equation
```

> `2`. Given that $p(0)=5000$ find the population after 5 time units.

```{code-cell} ipython3
condition = {p(0): 5000}
sym.dsolve(differential_equation, p(t), ics=condition)
```

Thus the population after 5 time units is:

```{code-cell} ipython3
5000 * sym.exp(sym.S(5) / 100)
```

## Question 5

> `5`. The rate of change of the temperature of a hot drink is proportional to the
> difference between the temperature of the drink ($T$) and the room temperature ($T_R$).

> `1`. Define the differential equation that models this situation.

```{code-cell} ipython3
T = sym.Function("T")
t = sym.Symbol("t")
T_r = sym.Symbol("T_r")
k = sym.Symbol("k")

differential_equation = sym.Eq(sym.diff(T(t), t), k * (T(t) - T_r))
differential_equation
```

> `2`. Solve the differential equation.

```{code-cell} ipython3
sym.dsolve(differential_equation, T(t))
```

> `3`. Given that $T(0) = 100$ and the room temperature is $T_R=20$ obtain the
> particular solution.

```{code-cell} ipython3
condition = {T(0): 100}
particular_differential_equation = differential_equation.subs({T_r: 20})
sym.dsolve(particular_differential_equation, T(t), ics=condition)
```

> `4`. Use the particular solution to identify how on it will take for the drink
> to be ready for consumption (a temperature of 80) given that after 3 time
> units $T(3)=90$.

First let us find the missing variable $k$ by using the fact that $T(3) = 90$:

```{code-cell} ipython3
equation = sym.Eq(80 * sym.exp(k * 3) + 20, 90)
sym.solveset(equation, k)
```

The set of solutions is infinite but contains a single real value element (when
$n=0$):

```{code-cell} ipython3
particular_k = sym.log(sym.S(7) / 8) / 3
```

The final equation to be solved is given by:

```{code-cell} ipython3
equation = sym.Eq(80 * sym.exp(particular_k * t) + 20, 80)
sym.solveset(equation, t)
```

which has a single real valued element (when $n=0$):

```{code-cell} ipython3
t_ready = 3 * sym.log(sym.S(3) / 4)/ sym.log(sym.S(7) / 8)
t_ready
```

Which means the hot drink will be ready in about 7 minutes:

```{code-cell} ipython3
float(t_ready)
```
