import pathlib
import subprocess
import sys

import proselint


def get_root_path():
    return pathlib.Path(__file__).absolute().parent.parent.parent


known_exceptions = {
    "02-algebra": set(
        (
            (
                "needless_variants.misc",
                "Needless variant. 'discriminating' is the preferred form.",
                129,
                43,
                3782,
                3795,
                13,
                "warning",
                "discriminating",
            ),
            (
                "needless_variants.misc",
                "Needless variant. 'discriminating' is the preferred form.",
                132,
                6,
                3813,
                3826,
                13,
                "warning",
                "discriminating",
            ),
            (
                "needless_variants.misc",
                "Needless variant. 'discriminating' is the preferred form.",
                128,
                43,
                3781,
                3794,
                13,
                "warning",
                "discriminating",
            ),
            (
                "needless_variants.misc",
                "Needless variant. 'discriminating' is the preferred form.",
                131,
                6,
                3812,
                3825,
                13,
                "warning",
                "discriminating",
            ),
        )
    )
}

root = get_root_path()
exit_code = 0
for markdown_file_path in filter(
    lambda path: ".ipynb_checkpoints" not in str(path), root.glob("**/*md")
):

    markdown = markdown_file_path.read_text()
    suggestions = proselint.tools.lint(markdown)
    exceptions = known_exceptions.get(markdown_file_path.parent.name, set(()))
    for suggestion in filter(
        lambda suggestion: suggestion not in exceptions, suggestions
    ):
        print(f"Proselint suggests the following in {markdown_file_path}")
        print(suggestion)
        exit_code = 1

sys.exit(exit_code)
