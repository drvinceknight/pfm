import tempfile
import pathlib
import subprocess
import sys
import re


MD_PATTERN = re.compile(
    r"(?P<before>^(?P<indent> *)```\s*python\n)"
    r"(?P<code>.*?)"
    r"(?P<after>^(?P=indent)```\s*$)",
    re.DOTALL | re.MULTILINE,
)


def get_root_path():
    return pathlib.Path(__file__).absolute().parent.parent.parent


root = get_root_path()
max_exit_code = 0
for markdown_file_path in filter(
    lambda path: ".ipynb_checkpoints" not in str(path), root.glob("**/*md")
):

    markdown_string = markdown_file_path.read_text()
    for match in re.finditer(pattern=MD_PATTERN, string=markdown_string):
        python_code = match.group(3)
        temporary_file = tempfile.NamedTemporaryFile()
        temporary_file_path = pathlib.Path(temporary_file.name)
        temporary_file_path.write_text(python_code)

        output = subprocess.run(
            ["black", "--check", temporary_file_path], capture_output=True, check=False
        )

        if (exit_code := output.returncode) > 0:
            max_exit_code = max(max_exit_code, exit_code)
            stderr_with_correct_filename = output.stderr.decode("utf-8").replace(
                str(temporary_file_path), str(markdown_file_path)
            )
            stderr_with_snippet_wording = stderr_with_correct_filename.replace(
                "1 file would be reformatted", "1 code snippet does not follow black:"
            )
            print(stderr_with_snippet_wording)
            print(python_code)

        output = subprocess.run(
            ["isort", "--check-only", temporary_file_path],
            capture_output=True,
            check=False,
        )

        if (exit_code := output.returncode) > 0:
            max_exit_code = max(max_exit_code, exit_code)
            stderr_with_correct_filename = output.stderr.decode("utf-8").replace(
                str(temporary_file_path), str(markdown_file_path)
            )
            print(stderr_with_correct_filename)
            print(python_code)

sys.exit(max_exit_code)
