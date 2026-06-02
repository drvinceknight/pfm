---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Further information

## Why do you need to use the `print` function with an editor?

When using a Jupyter notebook, the last line of a cell corresponds to the
output of the cell and is automatically displayed.
When running code written in an editor directly through the Python interpreter
there is nowhere for code to be output to. Thus, you need to specifically tell it
to display the code which is what the `print` statement does.

## Can you use a Python plugin to run my code from inside my editor?

When using the Python plugin buttons become available that let you run code
without using the command line. Before using those buttons it is good to become comfortable using a
command line tool to fully understand what the underlying process is. Furthermore,
at times when debugging sometimes the user interface might be at fault.

## Can you open a Jupyter notebook inside vscode?

When using the Python plugin it is possible to use Jupyter notebooks
from within VScode.

The notebooks will not look exactly the same but have the same functionality.

```{figure} ./img/notebook_in_vscode/main.png
---
width: 75%
name: fig:notebook_in_vscode
---
A notebook in vscode
```

## What is the difference between an Integrated Development Environment and an editor?

An *I*ntegrated *D*evelopment *E*nvironment or IDE is another type of tool used
to write code. A popular one for Python is PyCharm
<https://www.jetbrains.com/pycharm/>.

Generally IDEs are powerful tools designed for one specific language whereas
editors are supposedly lightweight and designed to be flexible to be used with
many languages.

I recommend experimenting with IDEs and/or editors to find what you prefer but
throughout this book we will use VScode.

## Why can I not use `\\(` and `\\)` for markdown in VScode.

When using Jupyter notebooks or the markdown preview feature in VScode the
single `$` and `$$` must be used as delimiters for mathematics. (See
{ref}`why_do_we_use_brackets_instead_of_dollars_for_latex`).

## Terminal alternatives on Windows

The commands used in this book work in any Windows terminal. The main options
are:

- **Windows Terminal** — the recommended choice. Pre-installed on Windows 11;
  available free from the Microsoft Store on Windows 10. Supports multiple
  tabs, modern font rendering, and both PowerShell and Command Prompt in the
  same window.
- **PowerShell** — pre-installed on all modern Windows versions. More powerful
  scripting language than Command Prompt. Available by searching in the Start
  menu.
- **Command Prompt (`cmd`)** — the classic Windows terminal, pre-installed on
  all Windows versions. All commands in this book work here.
- **Git Bash** — installed alongside Git for Windows
  (<https://gitforwindows.org/>). Provides a Unix-like shell experience on
  Windows, useful if you are following Unix-oriented instructions elsewhere.

## Terminal alternatives on macOS

- **Terminal.app** — the built-in terminal, always available. Found in
  `Applications > Utilities > Terminal` or via Spotlight (`Cmd + Space`).
- **iTerm2** (<https://iterm2.com/>) — a popular free alternative with split
  panes, search, autocomplete, and many other features. A common choice among
  developers.
- **Warp** (<https://www.warp.dev/>) — a modern terminal with built-in command
  history search and AI assistance.

All terminals on macOS give access to the same shell (zsh by default on macOS
Catalina and later), so all commands in this book work identically across them.

## Using `uv` to manage project dependencies

When working on a Python project with specific library requirements it is good
practice to isolate those dependencies from the rest of your system. `uv` is
a fast, modern tool that handles this automatically.

Install `uv` by following the instructions at <https://docs.astral.sh/uv/>.

To create a new project:

```bash
$ uv init my-project
$ cd my-project
```

To add a library to the project:

```bash
$ uv add sympy
```

To run a script inside the project's environment (no manual activation needed):

```bash
$ uv run python main.py
```

`uv` creates and manages a `.venv` directory for the project automatically and
records all dependencies in a `pyproject.toml` file, making it easy to
reproduce the same environment on another machine.
