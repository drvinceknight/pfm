import pathlib
import re
import subprocess
import sys
import tempfile

import proselint

from pfm import known

ROOT = pathlib.Path(__file__).parent.parent

MD_PATTERN = re.compile(
    r"(?P<before>^(?P<indent> *)\s*(``*{code-cell} ipython3|`*python)\n)"
    r"(?P<code>.*?)"
    r"(?P<after>^(?P=indent)(``*)\s*$)",
    re.DOTALL | re.MULTILINE,
)

TAGS_PATTERN = re.compile(r":tags: \[.*\]\n\n")


def path_in_book(path):
    """
    A filter function that checks if a given path is part of the book.
    """
    if ".ipynb_checkpoints" in str(path):
        return False
    if "README.md" in str(path):
        return False
    if "documentation_in_vscode" in str(path):
        return False
    return True


def get_book_source_files():
    """
    Returns a generator of all the markdown source files of the book.
    """
    book_path = ROOT / "book/"
    return filter(path_in_book, book_path.glob("**/*md"))


def stylecheck():
    """
    Run all code snippets in the book through black, isort, and interrogate.

    Code snippets are extracted from markdown using MD_PATTERN. Tags are
    stripped via TAGS_PATTERN. Cells tagged with `style-check-ignore` or
    containing doctest-style `>>>` code are skipped.
    """
    max_exit_code = 0
    for markdown_file_path in get_book_source_files():
        markdown = markdown_file_path.read_text()
        for match in re.finditer(pattern=MD_PATTERN, string=markdown):
            python_code = match.group(4)
            if ("style-check-ignore" not in python_code) and (">>>" not in python_code):
                python_code = re.sub(
                    pattern=TAGS_PATTERN, repl="", string=python_code
                ).lstrip()

                temporary_file = tempfile.NamedTemporaryFile(suffix=".py")
                temporary_file_path = pathlib.Path(temporary_file.name)
                temporary_file_path.write_text(python_code)

                output = subprocess.run(
                    ["black", "--check", temporary_file_path],
                    capture_output=True,
                    check=False,
                )
                if (exit_code := output.returncode) > 0:
                    max_exit_code = max(max_exit_code, exit_code)
                    stderr = output.stderr.decode("utf-8").replace(
                        str(temporary_file_path), str(markdown_file_path)
                    ).replace(
                        "1 file would be reformatted",
                        "1 code snippet does not follow black:",
                    )
                    print(stderr)
                    diff = subprocess.run(
                        ["black", "--diff", temporary_file_path],
                        capture_output=True,
                        check=False,
                    )
                    print(diff.stdout.decode("utf-8"))

                output = subprocess.run(
                    ["isort", "--check-only", temporary_file_path],
                    capture_output=True,
                    check=False,
                )
                if (exit_code := output.returncode) > 0:
                    max_exit_code = max(max_exit_code, exit_code)
                    print(
                        output.stderr.decode("utf-8").replace(
                            str(temporary_file_path), str(markdown_file_path)
                        )
                    )

                if ("def" in python_code) or ("class" in python_code):
                    output = subprocess.run(
                        ["interrogate", "-v", "-M", "-i", "-f", "100", temporary_file_path],
                        capture_output=True,
                        check=False,
                    )
                    if (exit_code := output.returncode) > 0:
                        max_exit_code = max(max_exit_code, exit_code)
                        print(f"Docstring missing in {markdown_file_path}\n")

    sys.exit(max_exit_code)


def spellcheck():
    """
    Run the book through aspell. Known exceptions are in pfm/known.py.
    """
    exit_code = 0
    for markdown_file_path in get_book_source_files():
        markdown = markdown_file_path.read_text()
        aspell_output = subprocess.check_output(
            ["aspell", "-t", "--list", "--lang=en_GB"], input=markdown, text=True
        )
        incorrect_words = set(aspell_output.split("\n")) - {""} - known.words
        if incorrect_words:
            print(f"In {markdown_file_path} the following words are not known:")
            for word in sorted(incorrect_words):
                print(word)
            exit_code = 1
    sys.exit(exit_code)


def prosecheck():
    """
    Run proselint and alex on all markdown source files.
    Known exceptions are in pfm/known.py.
    """
    exit_code = 0
    for markdown_file_path in get_book_source_files():
        markdown = markdown_file_path.read_text()
        relative_path = str(markdown_file_path.relative_to(ROOT))
        exceptions = known.prose_exceptions.get(relative_path, set())

        for exception in exceptions:
            markdown = markdown.replace(exception, "")

        suggestions = proselint.tools.lint(markdown)
        ignored = known.prose_suggestions_to_ignore.get(relative_path, set())
        for suggestion in filter(lambda s: s[0] not in ignored, suggestions):
            print(f"proselint suggests the following in {markdown_file_path}")
            print(suggestion)
            exit_code = 1

        output = subprocess.run(
            ["alex", markdown_file_path], capture_output=True, check=False
        )
        if output.returncode > 0:
            exit_code = max(output.returncode, exit_code)
            print(output.stderr.decode("utf-8"))

    sys.exit(exit_code)
