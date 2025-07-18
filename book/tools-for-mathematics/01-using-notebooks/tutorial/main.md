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

(chp:using_notebooks)=

# Tutorial

This tutorial will take the reader through an example of using Jupyter
notebooks. Jupyter is the interface to the Python programming language
used in the first part of this book.

## Installation

1. Navigate to <https://www.anaconda.com/download/success>.
2. Identify and download the version of Python 3 for your operating
   system (Windows, MacOS, Linux).
3. Run the installer. I recommend using the default choices during the
   installation process.

```{warning}
If you have already used Python it is still recommended that you use the
Anaconda distribution. An explanation for this is available in
[in the further information section of this chapter](sec:why_use_anaconda).
If you are using a Chromebook or a
Tablet there are websites and applications that you can use instead of
Anaconda to follow along in this book. See [the further information section of
this chapter for information on this](sec:using_notebooks_further_information).
```

### Starting a Jupyter notebook server

Open a command line tool:

1.  On **Windows** search for `Anaconda Prompt` (it should be available
    to you after installing Anaconda). See
    {ref}`fig:starting_the_notebook_server_windows`.
2.  On **MacOS** search for `terminal`. {ref}`fig:starting_the_notebook_server`

In there type (without the `$`):

```console
$ jupyter notebook
```

Press `Enter` on your keyboard.

```{tip}
Throughout this book, when there are commands to be typed in a command
line they will be prefixed them with a `$`. Do not type the `$`.
```

This
will open a new page in your browser. The url bar at the top should have
something that looks like: `http://localhost:8888/tree`. This is the
general interface to the Jupyter server. It shows the general file
structure on your computer as shown in {ref}`fig:the_jupyter_interface_windows`.

```{figure} ./img/starting_the_notebook_server/main.png
---
width: 75%
name: fig:starting_the_notebook_server
---
Starting the notebook server on MacOS
```

```{figure} ./img/starting_the_notebook_server_windows/main.png
---
width: 75%
name: fig:starting_the_notebook_server_windows
---
Starting the notebook server on Windows
```

```{figure} ./img/the_jupyter_interface/main.png
---
width: 75%
name: fig:the_jupyter_interface_windows
---
The Jupyter interface
```

### Creating a new notebook

In the top right, click on the `New` button {ref}`fig:creating_a_new_notebook` and click on `Notebook`.
This will be followed by a prompt to choose the programming language to
use, this is referred to as the kernel: select Python 3. Change the name
of the notebook by clicking on "Untitled" and changing the name. You
will call it "introduction" as shown in {ref}`fig:changing_notebook_name`.

```{figure} ./img/creating_a_new_notebook/main.png
---
width: 75%
name: fig:creating_a_new_notebook
---
Creating a new notebook
```

Let us change the name of the notebook by clicking on "Untitled" and changing
the name. We will call it "introduction".

```{figure} ./img/changing_notebook_name/main.png
---
width: 75%
name: fig:changing_notebook_name
---
Changing the notebook name
```

## Organising our files

Open your file browser:

1. File Explorer on **Windows** (see {ref}`fig:new_directory_structure_windows`).
2. Finder on **MacOS** (see {ref}`fig:new_directory_structure`).

Navigate to where your notebook is (this might not be immediately
evident): you should see a `introduction.ipynb` file. Find a location on
your computer where you want to keep the files for this book, using your
file browser:

1.  Create a new directory called `pfm` (short for "Python for
    Mathematics");
2.  Inside that directory create a new directory called `nbs` (short for
    "Notebooks");
3.  Move the `introduction.ipynb` file to this `nbs` directory.

```{figure} ./img/new_directory_structure/main.png
---
width: 75%
name: fig:new_directory_structure
---
Creating a new directory on MacOS
```

```{figure} ./img/new_directory_structure_windows/main.png
---
width: 75%
name: fig:new_directory_structure_windows
---
Creating a new directory on Windows
```

## Writing some basic Python code

Go back to the Jupyter notebook server (in your browser). Use the
interface to navigate to the `pfm` directory and inside that the `nbs`
directory and open the `introduction.ipynb` notebook.

```{figure} ./img/opening_notebook/main.png
---
width: 75%
name: fig:opening_notebook
---
Opening a notebook
```

In the first available "cell" write the following calculation:

```python
2 + 2
```

When you have done that click on the `Run` button (you can also use `Shift + Enter` as a keyboard shortcut).
When you have done that click on the `Run` button shown in
{ref}`fig:running_code`. You can also use `Shift + Enter` as a
keyboard shortcut.

```{figure} ./img/running_code/main.png
---
width: 75%
name: fig:running_code
---
Running code
```

```{code-cell} ipython3
2 + 2
```

Figure {ref}`fig:running_code` shows two different things:

1.  The input: which is the instruction to Python to use the
    mathematical technique of addition to compute 2 + 2.

2.  The output: showing the output that Python has returned as a result
    of the instruction.

## Writing markdown

One of the reasons for using Jupyter notebooks is that it allows a user
to include both code and communication using something called
`markdown`. Create a new cell and change the cell type to `Markdown`.
Now write the following in there:

```md
As well as using Python in Jupyter notebooks we can also write using Markdown.
This allows us to use basic $\LaTeX$ as a way to display mathematics.
For example:

1. $\frac{2}{3}$
2. $\sum_{i=0}^n i$
```

When you run that it should look like {ref}`fig:rendering_markdown`.

```{figure} ./img/rendering_markdown/main.png
---
width: 75%
name: fig:rendering_markdown
---
Rendering markdown
```

## Saving your notebook to a different format

Click on `File` and `Download As` this brings up a number of formats
that Jupyter notebooks can be exported to. Some of these might need
other tools installed on your computer but a portable option is `HTML`.
Click on `HTML (.html)`. Now use your file browser and open the
downloaded file. This will open in your browser a static version of the
file you have been working on. This is a helpful way to share your work
with someone who might not have Jupyter (or even Python).

```{important}
This tutorial has:

- Installed the Anaconda distribution of Python.
- Started a notebook server.
- Created a new notebook.
- Run some Python code.
- Written some markdown.
- Saved the notebook to a different format.
```
