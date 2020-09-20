import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import proselint

from invoke import task

import known

ROOT = pathlib.Path(__file__).parent

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
    return True


def get_book_source_files(root=ROOT):
    """
    Returns a generator of all the markdown sources files of the book.
    """
    book_path = ROOT / "nbs/book/"
    return filter(path_in_book, book_path.glob("**/*md"))


@task
def stylecheck(c, root=ROOT, md_pattern=MD_PATTERN, tags_pattern=TAGS_PATTERN):
    """
    Run all code snippets in book through:

    - black
    - isort
    - interrogate

    This is done by capturing the code snippets using the `md_pattern` regex,
    writing them to a temporary file and running the cli tools on the temporary
    files.
    """
    max_exit_code = 0
    for markdown_file_path in get_book_source_files():
        markdown_string = markdown_file_path.read_text()
        for match in re.finditer(pattern=md_pattern, string=markdown_string):
            python_code = match.group(4)
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
                stderr_with_correct_filename = output.stderr.decode("utf-8").replace(
                    str(temporary_file_path), str(markdown_file_path)
                )
                stderr_with_snippet_wording = stderr_with_correct_filename.replace(
                    "1 file would be reformatted",
                    "1 code snippet does not follow black:",
                )
                print(stderr_with_snippet_wording)
                output = subprocess.run(
                    ["black", "--diff", temporary_file_path],
                    capture_output=True,
                    check=False,
                )
                print(output.stdout.decode("utf-8"))

            output = subprocess.run(
                ["isort", "--check-only", temporary_file_path],
                capture_output=True,
                check=False,
            )

            if ("def" in python_code) or ("class" in python_code):
                if (exit_code := output.returncode) > 0:
                    max_exit_code = max(max_exit_code, exit_code)
                    stderr_with_correct_filename = output.stderr.decode(
                        "utf-8"
                    ).replace(str(temporary_file_path), str(markdown_file_path))
                    print(stderr_with_correct_filename)

                output = subprocess.run(
                    ["interrogate", "-v", "-M", "-f", "100", temporary_file_path],
                    capture_output=True,
                    check=False,
                )

                if (exit_code := output.returncode) > 0:
                    max_exit_code = max(max_exit_code, exit_code)
                    print(f"Docstring missing in {markdown_file_path}")
                    print("\n")
                    print(python_code)

    sys.exit(max_exit_code)


@task
def spellcheck(c, root=ROOT):
    """
    Run the book through a spell checker.

    Known exceptions are in `known.py`
    """
    exit_code = 0

    for markdown_file_path in get_book_source_files():

        markdown = markdown_file_path.read_text()
        aspell_output = subprocess.check_output(
            ["aspell", "-t", "--list", "--lang=en_GB"], input=markdown, text=True
        )
        incorrect_words = set(aspell_output.split("\n")) - {""} - known.words
        if len(incorrect_words) > 0:
            print(f"In {markdown_file_path} the following words are not known: ")
            for string in sorted(incorrect_words):
                print(string)
            exit_code = 1

    sys.exit(exit_code)


@task
def prosecheck(c, root=ROOT):
    """
    Run the following checkers for prose on all markdown source files:

    - Proselint
    - Alex

    Proselint is used as a python library. Alex (an npm tool) is used by running
    the command line tool on the markdown file.

    Known exceptions are in `known.py`
    """
    exit_code = 0
    for markdown_file_path in get_book_source_files():
        markdown = markdown_file_path.read_text()
        relative_markdown_path = str(markdown_file_path.relative_to(root))
        exceptions = known.prose_exceptions.get(relative_markdown_path, set(()))

        for exception in exceptions:
            markdown = markdown.replace(markdown, exception)

        suggestions = proselint.tools.lint(markdown)
        ignored_suggestions = known.prose_suggestions_to_ignore.get(
            relative_markdown_path, set(())
        )
        for suggestion in filter(
            lambda suggestion: suggestion[0] not in ignored_suggestions, suggestions
        ):
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


@task
def buildbook(c, root=ROOT):
    """
    Remove previous build and rebuild the book.
    """
    output_path = root / "book/"
    shutil.rmtree(output_path, ignore_errors=True)
    c.run(f"jb build nbs/book --path-output {root}")

    build_path = root / "_build"
    shutil.copytree(src=build_path / "html", dst=output_path)
    shutil.rmtree(build_path, ignore_errors=True)


@task
def backupbook(c, root=ROOT):
    """
    Backup all markdown files to notebooks.

    This is done so that the notebooks can be tested. Whilst this may seem
    unnecessary it ensures that the outputs can be tested across different
    versions of the dependencies.

    An example use case:

    - Content is added with sympy version 1.6.1
    - Book is updated
    - Students using the book are using an updated version of sympy that no
      longer gives the exact same results.

    Using backup notebooks alongside with unpinned dependencies for the
    continuous integrations ensures this will become apparent.
    """
    for markdown_file_path in get_book_source_files():
        print(markdown_file_path)
        backup_path = markdown_file_path.with_suffix(".bcp.ipynb")
        markdown_file_to_delete = backup_path.with_suffix(".md")
        c.run(f"jupytext --to notebook --execute {markdown_file_path} -o {backup_path}")
        markdown_file_to_delete.unlink(missing_ok=True)


@task
def testnbs(c, root=ROOT):
    """
    Remove previous build and rebuild the book.
    """
    c.run(f"python -m pytest --ignore={root}/nbs/drafts --nbval --current-env")
