import pathlib
import subprocess
import sys


def get_root_path():
    return pathlib.Path(__file__).absolute().parent.parent.parent


root = get_root_path()
max_exit_code = 0
for markdown_file_path in root.glob("**/*md"):
    output = subprocess.run(
        ["proselint", markdown_file_path], capture_output=True, check=False
    )

    if (exit_code := output.returncode) > 0:
        max_exit_code = max(max_exit_code, exit_code)
        print(output.stdout.decode("utf-8"))

sys.exit(max_exit_code)
