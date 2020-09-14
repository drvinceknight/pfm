import pathlib
import subprocess
import sys

import proselint


def get_root_path():
    return pathlib.Path(__file__).absolute().parent.parent.parent


known_exceptions = {
    "02-algebra": set(("We can immediately use this to compute the discriminant:")),
    "04-matrices": set(
        (
            "4. Q1 The matrix \\(D\\) is given by \\(D = \begin{pmatrix} a & 2 & 0\\ 3 & 1 & 2\\ 0 & -1 & 1\end{pmatrix}\\) where \\(a\ne 2\\)."
        )
    ),
}

suggestions_to_ignore = {"05-probability": set(("typography.symbols.curly_quotes",))}

root = get_root_path()
exit_code = 0
for markdown_file_path in filter(
    lambda path: ".ipynb_checkpoints" not in str(path), root.glob("**/*md")
):

    markdown = markdown_file_path.read_text()
    exceptions = known_exceptions.get(markdown_file_path.parent.name, set(()))

    for exception in exceptions:
        markdown = markdown.replace(markdown, exception)

    suggestions = proselint.tools.lint(markdown)
    ignored_suggestions = suggestions_to_ignore.get(
        markdown_file_path.parent.name, set(())
    )
    for suggestion in filter(
        lambda suggestion: suggestion[0] not in ignored_suggestions, suggestions
    ):
        print(ignored_suggestions)
        print(f"Proselint suggests the following in {markdown_file_path}")
        print(suggestion)
        exit_code = 1

sys.exit(exit_code)
