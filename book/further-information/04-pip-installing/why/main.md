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

# Further information.

## Why do we do `python -m pip install` and not `pip install`

In some places you will see that to install a Python library you can run the
following in the command line:

```bash
$ pip install <library>
```

Instead of:

```bash
$ python -m pip install <library>
```

This will work and most often will have the same effect however it is not
recommended.

On some occasions `pip`, which is the library used to install packages will not
correspond to the same `python` install you are using. To ensure this does not
create any problems it is recommended to use `python -m pip install <library>`.

Here is a short blog post discussing this:
<https://adamj.eu/tech/2020/02/25/use-python-m-pip-everywhere/>.

## How to install multiple libraries at a time

If you want to keep a record of multiple python libraries that you want to
install, the convention is to keep them in a file called `requirements.txt`.

Then to install all the libraries you can run the following in the command line:

```bash
$ python -m pip install -r requirements.txt
```

For example, the `requirements.txt` file for this software used to write this
book looks like:

```
black==20.8b1
interrogate==1.3.1
invoke==1.4.1
isort==4.3.21
jupyter-book==0.8.1
jupytext==1.6.0
nbval==0.9.6
proselint==0.10.2
pytest==5.4.3
```

If the version specifications are omitted then the latest versions of the
libraries would be installed.

```
black
interrogate
invoke
isort
jupyter-book
jupytext
nbval
proselint
pytest
```

## What is the Python package index

The Python package index commonly referred to as PyPI is:

> "The Python Package Index (PyPI) is a repository of software for the Python
> programming language."

In practical terms it is where developers upload their libraries so that they can
be installed with `pip`.

## What is a virtual environment

When using Python for a number of projects it can be beneficial to
isolate the entire software environment for each project. This is done using
something called a virtual environment and allows you to have multiple versions
of Python and different sets of libraries for different projects.

The standard Python library includes `venv` for creating virtual environments:

```bash
$ python -m venv .venv
$ source .venv/bin/activate   # macOS
$ .venv\Scripts\activate      # Windows
```

You can read more about `venv` at:

- <https://realpython.com/python-virtual-environments-a-primer/>
- <https://docs.python.org/3/library/venv.html>

## What is `uv`

`uv` is a fast, modern Python package and project manager. It can replace
`pip`, `venv`, and other tools with a single command-line utility. It is
written in Rust and considerably faster than `pip` for installing packages.

You can install `uv` by following the instructions at <https://docs.astral.sh/uv/>.

### Managing a project with `uv`

To create a new project with its own isolated environment:

```bash
$ uv init my-project
$ cd my-project
```

To add a library to the project (this installs it and records the dependency):

```bash
$ uv add sympy
```

To run a script or command inside the project's environment:

```bash
$ uv run python main.py
$ uv run jupyter notebook
```

`uv` automatically creates and manages a virtual environment for the project
so you do not need to activate it manually.

You can read the full `uv` documentation at <https://docs.astral.sh/uv/>.
