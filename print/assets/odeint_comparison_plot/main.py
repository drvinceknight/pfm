import matplotlib.pyplot as plt
import sympy as sym
import scipy.integrate
import numpy as np

x = sym.Symbol("x")
y = sym.Function("y")

def diff(state, x):
    """
    Returns the value of the derivates for a given set of state values (u, y).
    """
    u, y = state
    return x * y, u

condition = (.1, -.5)
xs = np.linspace(0, 1, 50)

equation = sym.Eq(lhs=sym.diff(y(x), x, 2), rhs=x * y(x) )
solution = sym.dsolve(equation, y(x), ics={y(0): condition[1], y(x).diff(x).subs(x, 0): condition[0]})

states = scipy.integrate.odeint(diff, y0=condition, t=xs)
plt.figure()
plt.scatter(xs, states.T[1], label="numeric", marker="+", color="black")
plt.plot(xs, [solution.rhs.subs({x: value}) for value in xs], label="closed form")
plt.xlabel("$x$")
plt.ylabel("y")
plt.legend()
plt.savefig("main.pdf")
