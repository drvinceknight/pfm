words = set(
    (
        "ABCD",
        "Anscombe's",
        "Ashville",
        "Bertolt",
        "Bewton",
        "CamelCase",
        "Carnets",
        "Combinatorics",
        "Df",
        "Eq",
        "Esc",
        "Eval",
        "Galton",
        "Github",
        "Gottfried",
        "Gruber",
        "IDEs",
        "Isla",
        "Isort",
        "Jupyter",
        "Jupyterbook",
        "LaTeX",
        "Lah",
        "Matplotlib",
        "Mersenne",
        "Modularisation",
        "Modularise",
        "MuggleCountry",
        "Nbval",
        "Numpy",
        "OSX",
        "Oldtown",
        "OtherPetDog",
        "PetDog",
        "Proselint",
        "Pseudo",
        "PyCharm",
        "PyPI",
        "PyPi",
        "QuadraticExpression",
        "QuadraticExpressionWithAllRoots",
        "README",
        "REPL",
        "REPLs",
        "Riggins",
        "Rollerblades",
        "StableMarriage",
        "Sympy",
        "VScode",
        "alex",
        "algorithmically",
        "allclose",
        "amelia",
        "aspell",
        "auraya",
        "ava",
        "blech",
        "boolean",
        "booleans",
        "cd",
        "cfm",
        "chromebook",
        "ciw",
        "cli",
        "cms",
        "cocalc",
        "color",
        "coloring",
        "combinatorial",
        "combinatorics",
        "conda",
        "cryptographic",
        "csv",
        "det",
        "df",
        "dir",
        "directoy",
        "discriminant",
        "displaystyle",
        "docstring",
        "docstrings",
        "doctest",
        "doctests",
        "docx",
        "dominica",
        "dunder",
        "dx",
        "ectory",
        "ella",
        "emily",
        "endregion",
        "eval",
        "evelopment",
        "factorint",
        "fibonacci",
        "fname",
        "formatter",
        "fowler",
        "functools",
        "galton",
        "gif",
        "github",
        "gusfield",
        "hange",
        "html",
        "iOS",
        "ij",
        "im",
        "img",
        "incircle",
        "ing",
        "init",
        "inv",
        "ipynb",
        "ipython",
        "irectory",
        "isla",
        "isort",
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
        "librery",
        "linalg",
        "linspace",
        "loadtxt",
        "lru",
        "markov",
        "martraire",
        "math",
        "matplotlib",
        "matplotlib",
        "md",
        "mia",
        "mkdir",
        "modularisation",
        "modularise",
        "modularised",
        "modularising",
        "monty",
        "myst",
        "nash",
        "nbs",
        "nbval",
        "nd",
        "ni",
        "np",
        "ntegrated",
        "numpy",
        "nvironment",
        "oliveira",
        "olivia",
        "onwards",
        "oo",
        "pdf",
        "percival",
        "plt",
        "png",
        "polyfit",
        "pre",
        "prefs",
        "proselint",
        "py",
        "pyplot",
        "pytest",
        "randint",
        "repo",
        "repr",
        "rhs",
        "riggins",
        "rokens",
        "roseau",
        "savefig",
        "scipy",
        "solveset",
        "sophia",
        "sqrt",
        "str",
        "submatrix",
        "svg",
        "sym",
        "sympy",
        "tex",
        "th",
        "txt",
        "url",
        "vectorized",
        "venv",
        "vscode",
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
    "book/building-tools/05-modularisation/why/main.md": set(
        (
            r"Code should be obvious",
            r"easily and make the change quickly without",
        )
    ),
    "book/about-this-book/how-is-this-book-written/main.md": set(
        (
            r"black",
            r"Black",
        )
    ),
}
prose_suggestions_to_ignore = {
    "book/tools-for-mathematics/02-algebra/introduction/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/tools-for-mathematics/02-algebra/solutions/main.md": set(
        ("needless_variants.misc",)
    ),
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
    "book/tools-for-mathematics/07-sequences/how/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/tools-for-mathematics/07-sequences/why/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
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
    "book/building-tools/01-variables-conditionals-loops/solutions/main.md": set(
        (
            "typography.symbols.curly_quotes",
            "consistency.spacing",
        )
    ),
    "book/building-tools/02-functions-and-data-structures/tutorial/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/02-functions-and-data-structures/solutions/main.md": set(
        (
            "typography.symbols.curly_quotes",
            "leonard.exclamation.30ppm",
        )
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
    "book/building-tools/03-objects/why/main.md": set(
        (("typography.symbols.curly_quotes"),)
    ),
    "book/building-tools/04-editor-and-cli/tutorial/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/04-editor-and-cli/how/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/05-modularisation/tutorial/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/05-modularisation/how/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/05-modularisation/exercises/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/05-modularisation/why/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/06-documentation/tutorial/main.md": set(
        (
            "typography.symbols.curly_quotes",
            "typography.symbols.sentence_spacing",
        )
    ),
    "book/building-tools/06-documentation/tutorial/img/documentation_in_vscode/main.md": set(
        ("typography.symbols.sentence_spacing",)
    ),
    "book/building-tools/06-documentation/how/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/06-documentation/exercises/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/06-documentation/why/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/building-tools/07-testing/tutorial/main.md": set(
        (
            "typography.symbols.curly_quotes",
            "typography.symbols.ellipsis",
            "typography.symbols.sentence_spacing",
        )
    ),
    "book/building-tools/07-testing/how/main.md": set(
        (
            "typography.symbols.curly_quotes",
            "typography.symbols.ellipsis",
        )
    ),
    "book/building-tools/07-testing/why/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
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
    "book/further-information/03-kernel/tutorial/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/further-information/04-pip-installing/why/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
    "book/about-this-book/software-packages-used/main.md": set(
        ("typography.symbols.curly_quotes",)
    ),
}
