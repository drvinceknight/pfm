import sympy as sym

x = sym.Symbol("x")
p = sym.plot(x ** 2 + 3 * x + 1, xlim=(-5, 5))
p.save("main.pdf")
