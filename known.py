words = set(
    (
        "iOS",
        "Anscombe's",
        "Ashville",
        "Bertolt",
        "Bewton",
        "CamelCase",
        "Carnets",
        "Combinatorics",
        "Df",
        "Eq",
        "Galton",
        "Gottfried",
        "Gruber",
        "Jupyter",
        "LaTeX",
        "Lah",
        "Matplotlib",
        "Mersenne",
        "MuggleCountry",
        "Numpy",
        "OSX",
        "Oldtown",
        "OtherPetDog",
        "PetDog",
        "Pseudo",
        "QuadraticExpression",
        "QuadraticExpressionWithAllRoots",
        "Riggins",
        "Rollerblades",
        "Sympy",
        "algorithmically",
        "auraya",
        "blech",
        "boolean",
        "booleans",
        "cfm",
        "chromebook",
        "cms",
        "cocalc",
        "color",
        "combinatorial",
        "combinatorics",
        "cryptographic",
        "det",
        "df",
        "discriminant",
        "displaystyle",
        "docstring",
        "docstrings",
        "docx",
        "dominica",
        "dunder",
        "dx",
        "endregion",
        "factorint",
        "fibonacci",
        "fname",
        "functools",
        "galton",
        "github",
        "html",
        "im",
        "img",
        "incircle",
        "init",
        "inv",
        "ipynb",
        "ipython",
        "isprime",
        "iterable",
        "iterables",
        "itertools",
        "jupyter",
        "jupytext",
        "kernelspec",
        "latexmk",
        "len",
        "lhs",
        "linalg",
        "linspace",
        "lru",
        "math",
        "matplotlib",
        "matplotlib",
        "md",
        "myst",
        "nash",
        "nbs",
        "nbval",
        "np",
        "numpy",
        "oo",
        "pdf",
        "plt",
        "png",
        "polyfit",
        "pre",
        "pyplot",
        "randint",
        "repo",
        "repr",
        "rhs",
        "riggins",
        "roseau",
        "savefig",
        "scipy",
        "solveset",
        "sqrt",
        "str",
        "svg",
        "sym",
        "sympy",
        "tex",
        "th",
        "url",
        "vectorized",
        "wikipedia",
        "xelatex",
        "xlabel",
        "xlim",
        "ylabel",
    )
)

prose_exceptions = {
    "book/tools-for-mathematics/02-algebra/tutorial/main.md": set(
        (
            "We can immediately use this to compute the discriminant:",
            "sympy.discriminant(expression)",
            "negative discriminant then it does not have any roots and all the values are of",
            "1. Calculate the discriminant of the quadratic equation $2x ^ 2 + x + 1 =",
        )
    ),
    "book/tools-for-mathematics/02-algebra/exercises/main.md": set(
        (
            "1. Calculate the discriminant of the quadratic equation $4x ^ 2 + 16x + 25 =",
            "1. Calculate the discriminant of the quadratic equation $-3x ^ 2 + 24x - 97 =",
        )
    ),
    "book/tools-for-mathematics/04-matrices/exercises/main.md": set(
        (
            r"4. The matrix $D$ is given by $D = \begin{pmatrix} a & 2 & 0\\ 3 & 1 & 2\\ 0 & -1 & 1\end{pmatrix}$ where $a\ne 2$.",
        )
    ),
    "book/tools-for-mathematics/04-matrices/solutions/main.md": set(
        (
            r"> `4`. The matrix $D$ is given by $D = \begin{pmatrix} a & 2 & 0\\ 3 & 1 & 2\\ 0 & -1 & 1\end{pmatrix}$ where $a\ne 2$.",
        )
    ),
}
prose_suggestions_to_ignore = {
    "book/tools-for-mathematics/02-algebra/introduction/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/tools-for-mathematics/02-algebra/solutions/main.md": set(("needless_variants.misc",)),
    "book/tools-for-mathematics/06-probability/tutorial/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/tools-for-mathematics/06-probability/solutions/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/tools-for-mathematics/05-combinations-permutations/tutorial/main.md": set(
        ("leonard.exclamation.30ppm",)
    ),
    "book/tools-for-mathematics/06-probability/why/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/tools-for-mathematics/06-probability/how/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/tools-for-mathematics/07-sequences/how/main.md": set(("typography.symbols.curly_quotes",)),
    "book/tools-for-mathematics/07-sequences/why/main.md": set(("typography.symbols.curly_quotes",)),
    "book/tools-for-mathematics/07-sequences/tutorial/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/tools-for-mathematics/07-sequences/solutions/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/01-variables-conditionals-loops/tutorial/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/01-variables-conditionals-loops/how/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/02-functions-and-data-structures/tutorial/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/03-objects/tutorial/main.md": set(
        (("typography.symbols.curly_quotes"), ("needless_variants.misc"))
    ),
    "book/building-tools/03-objects/how/main.md": set(
        (("typography.symbols.curly_quotes"), ("needless_variants.misc"))
    ),
    "book/building-tools/03-objects/exercises/main.md": set(
        (("typography.symbols.curly_quotes"),)
    ),
    "book/building-tools/03-objects/why/main.md": set((("typography.symbols.curly_quotes"),)),
    "book/further-information/01-numpy/tutorial/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/further-information/02-matplotlib/tutorial/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/further-information/02-matplotlib/how/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/further-information/02-matplotlib/why/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
}
