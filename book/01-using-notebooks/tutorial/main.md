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

# Tutorial

## Installation

1. Navigate to https://www.anaconda.com/products/individual.
2. Identify and download the version of Python 3 for your operating system (Windows, Mac OSX, Linux).
3. Run the installer.

```{warning}
If you have already used Python it is still recommended that you use the
Anaconda distribution. An explanation for this is available later.
```

## Starting a Jupyter notebook server

We are going to use **Jupyter notebooks** for the first part of this course.
This interface to Python works inside your web browser but does not require an
internet connect.

Open a command line tool:

1. On **Windows** search for `Anaconda Prompt` (it should be available to you
   after installing Anaconda.
2. On **OS X** search for `terminal`

In there type:

    $ jupyter notebook

and then press `Enter` on your keyboard.

```{tip}
Throughout this course, when there are commands to be typed in a command line
tool I will prefix them with a `$`. Do not type the `$`.
```

```{figure} ./img/starting_the_notebook_server/main.png
---
width: 75%
name: fig:starting_the_notebook_server
---
Starting the notebook server
```

This will open a new page in your browser. The url bar at the top should have
something that looks like: `http://localhost:8888/tree`.

```{figure} ./img/the_jupyter_interface/main.png
---
width: 75%
name: fig:the_jupyter_interface
---
The Jupyter interface
```

This is the general interface to the Jupyter server. It shows the general file
structure on your computer.

## Creating a new notebook

In the top right, click on the `new` button and click on `Python 3`.

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

Once this is done let us close the notebook by closing the corresponding tab of your web browser.

## Organising our files

Open your file browser:

1. File Explorer on **Windows**
2. Finder on **OS X**

Navigate to where your notebook is (this might not be immediately evident): you
should see a `introduction.ipynb` file.

Let us rearrange things.

Find a location on your computer where you want to keep the files for this course, using your file browser:

1. Create a new directory called `cfm` (short for "Computer for Mathematics");
2. Inside that directory create a new directory called `nbs` (short for
   "Notebooks");
3. Move the `introduction.ipynb` file to this `nbs` directory.

```{figure} ./img/new_directory_structure/main.png
---
width: 75%
name: fig:new_directory_structure
---
Creating a new directory
```

## Writing some basic Python code

Go back to our Jupyter notebook server (in your browser).

Use the interface to navigate to the `cfm` directory and inside that the `nbs`
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

When you have done that click on the `Run` button (you can also use `Shift +
Enter` as a keyboard shortcut).

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

We see two different things there:

1. The input: `In [1]` which is the instruction to Python to use the
   mathematical technique of addition to compute 2 + 2.
2. The output: `Out [1]` showing the output that Python has returned as a result
   of the instruction.


## Writing markdown

One of the reasons for using Jupyter notebooks is that it allows us to include
both code and communication using something called `markdown`.

Create a new cell and change the cell type to `Markdown`. Now write the
following in there:

```md
As well as using Python in Jupyter notebooks we can also write using Markdown.
This allows us to use basic \\(\LaTeX\\) as a way to display mathematics.
For example:

1. \\(\frac{2}{3}\\)
2. \\(\sum_{i=0}^n i\\)

```

When you run that it should look like:

```{figure} ./img/rendering_markdown/main.png
---
width: 75%
name: fig:rendering_markdown
---
Rendering markdown
```

## Saving your notebook to a different format

Click on `File` and `Download As` this brings up a number of formats that
Jupyter notebooks can be exported to. Some of these might need other tools
installed on your computer but a portable option is `HTML`.

Click on `HTML (.html)`.

Now use your file browser and open the downloaded file. This will open in your
browser a static version of the file you have been working on. This is a helpful
way to share your work with someone who might not have Jupyter (or even Python).
