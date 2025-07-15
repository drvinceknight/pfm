import sympy as sym

x = sym.Symbol("x")
p = sym.plot(x ** 2 + 3 * x + 1)
p.save("main.pdf")
