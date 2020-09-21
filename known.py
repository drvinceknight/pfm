words = set(
    (
        "Ashville",
        "Bertolt",
        "Bewton",
        "Combinatorics",
        "Df",
        "Eq",
        "Gottfried",
        "Gruber",
        "Jupyter",
        "LaTeX",
        "Lah",
        "Mersenne",
        "OSX",
        "Oldtown",
        "Pseudo",
        "Rollerblades",
        "Sympy",
        "algorithmically",
        "blech",
        "boolean",
        "booleans",
        "cfm",
        "combinatorial",
        "combinatorics",
        "cryptographic",
        "discriminant",
        "det",
        "df",
        "displaystyle",
        "docstring",
        "docstrings",
        "docx",
        "dx",
        "endregion",
        "functools",
        "html",
        "img",
        "inv",
        "ipynb",
        "ipython",
        "iterable",
        "iterables",
        "itertools",
        "jupyter",
        "jupytext",
        "kernelspec",
        "latexmk",
        "len",
        "lhs",
        "lru",
        "math",
        "matplotlib",
        "md",
        "myst",
        "nbs",
        "nbval",
        "numpy",
        "oo",
        "pdf",
        "plt",
        "png",
        "pyplot",
        "rhs",
        "scipy",
        "solveset",
        "sqrt",
        "sym",
        "sympy",
        "tex",
        "th",
        "url",
        "xelatex",
        "xlim",
    )
)

prose_exceptions = {
    "src/book/02-algebra/tutorial/main.md": set(
        (
            "We can immediately use this to compute the discriminant:",
            "sympy.discriminant(expression)",
            "negative discriminant then it does not have any roots and all the values are of",
            "1. Calculate the discriminant of the quadratic equation $2x ^ 2 + x + 1 =",
        )
    ),
    "src/book/02-algebra/exercises/main.md": set(
        (
            "1. Calculate the discriminant of the quadratic equation $4x ^ 2 + 16x + 25 =",
            "1. Calculate the discriminant of the quadratic equation $-3x ^ 2 + 24x - 97 =",
        )
    ),
    "src/book/04-matrices/exercises/main.md": set(
        (
            r"4. Q1 The matrix $D$ is given by $D = \begin{pmatrix} a & 2 & 0\\ 3 & 1 & 2\\ 0 & -1 & 1\end{pmatrix}$ where $a\ne 2$.",
        )
    ),
    "src/book/04-matrices/exercises/main.md": set(
        (
            r"4. Q1 The matrix $D$ is given by $D = \begin{pmatrix} a & 2 & 0\\ 3 & 1 & 2\\ 0 & -1 & 1\end{pmatrix}$ where $a\ne 2$.",
        )
    ),
}
prose_suggestions_to_ignore = {
    "src/book/02-algebra/introduction/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "src/book/06-probability/tutorial/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "src/book/05-combinations-permutations/tutorial/main.md": set(
        ("leonard.exclamation.30ppm",)
    ),
    "src/book/06-probability/why/main.md": set(("typography.symbols.curly_quotes",)),
    "src/book/06-probability/how/main.md": set(("typography.symbols.curly_quotes",)),
    "src/book/07-sequences/how/main.md": set(("typography.symbols.curly_quotes",)),
    "src/book/07-sequences/why/main.md": set(("typography.symbols.curly_quotes",)),
    "src/book/07-sequences/tutorial/main.md": set(("typography.symbols.curly_quotes",)),
}
