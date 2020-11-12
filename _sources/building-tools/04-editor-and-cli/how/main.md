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

# How

## How to navigate directories in the command line

In the command line the `cd` command (short for "*c*hange *d*irectory") can be
used to enter a given directory.

````{tip}
```
$ cd directory
```
````

```{attention}
The target directory must be contained in the directory you are currently in.
```

For example to change directory in to a directory called `cfm`:

```bash
% cd cfm
```

To go back to the previous directory use `..`:

```bash
$ cd ..
```

## How to create a new directory in the command line

In the command line the `mkdir` command (short for "*m*a*k*e *dir*ectory) can be
used to create a new directory.

````{tip}
```
$ mkdir directory
```
````

For example to create a director called `scripts`:

```bash
$ mkdir scripts
```

## How to see the contents of a directory in the command line

In the command line we can see the contents of the current directory:

- On Windows using `dir`
- On OS X using `ls`

`````{tip}
````{panels}
On Windows:

```bash
$ dir
```

---

On OS X:

```bash
$ ls
```

````
`````

## How to run python code in a file

To run code in a file we type `python` followed by the name of the file in the
command line.

````{tip}
```
$ python file.py
```
````

For example to run code in a file called `main.py`:

```bash
$ python main.py
```

## How to run python code without using a file or Jupyter

In the command line if you type `python` without passing a filename this will
create a prompt in which you can directly write Python code.

````{tip}
```
$ python
```
````

When doing this, we see a prompt appear with `>>>`, we can directly type python
code in there and press enter:

```
>>> 2 + 2
4
```

```{attention}
This interface to Python is called a Read-Eval-Print-Loop and is often referred
to as a REPL.
```

Using `python` is the simplest of REPLs, there are others (for example
`ipython`).

```{attention}
This interface to Python is quite limited and should only be used for quick
access to Python as a way to run simple commands.
```

(how_to_install_a_vscode_plugin)=

## How to install VScode plugins

VScode is a powerful editor with a number of plugins for different languages and
functionalities.

To install a particular plugin in the menu bar, click on `Code > Preferences > Extensions`.

From there you can search for a specific plugin and install it by clicking on
the install button.

Click the toggle ("Click to Show") to see a demo of this:

```{toggle}
![](./img/installing_a_vscode_plugin/main.gif)
```
