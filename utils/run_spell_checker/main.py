import pathlib
import subprocess
import sys

import known


def get_root_path():
    return pathlib.Path(__file__).absolute().parent.parent.parent


root = get_root_path()
exit_code = 0
for markdown_file_path in filter(
    lambda path: ".ipynb_checkpoints" not in str(path), root.glob("**/*md")
):

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
