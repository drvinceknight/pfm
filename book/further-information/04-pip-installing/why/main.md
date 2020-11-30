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
of Python that you choose to use for different things.

Two common ways of using virtual environments are:

- `venv`: this is in the standard Python library.
- `conda`: this is a dependency manager that comes with Anaconda.

You can read more about virtual environments at the following links:

- <https://realpython.com/python-virtual-environments-a-primer/>
- <https://docs.python.org/3/library/venv.html>
- <https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe>
- <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>

## What is `conda install`

Some libraries can be installed using the Anaconda dependency manager `conda`,
in these cases a pre built binary of the library will be installed. You can read
about this here: <https://www.anaconda.com/blog/understanding-conda-and-pip>.
