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

(cli_editor_tutorial)=

# Tutorial

We will here consider a problem we have already solved (in the Algebra
{ref}`algebra_tutorial`) but use a different interface to do so than Jupyter.
The code itself will be the same. The way we run it will differ.

```{admonition} Problem
Rationalise the denominator of $\frac{1}{\sqrt{2} + 1}$
```

Open a command line tool:

1. On **Windows** search for `Anaconda Prompt` (it should be available to you
   after installing Anaconda). See
   {ref}`fig:starting_the_notebook_server_windows`.
2. On **OS X** search for `terminal`. See
   {ref}`fig:starting_the_notebook_server`.

Whether or not your are on Windows or MacOS changes the commands you need to
type. We will first list the directory we are currently in:

`````{tab-set}
````{tab-item} Windows
```bash
$ dir
```
````

````{tab-item} MacOS
```bash
$ ls
```

````
`````

```{tip}
Throughout this book, when there are commands to be typed in a command line
tool I will prefix them with a `$`. Do not type the `$`.
```

This is similar to using your file explorer to view the contents in a given
directory. Similarly to the way we click on a directory in the file explorer we
can navigate to a directory in the command line.

To do this we use the same command on both operating systems:

`````{tab-set}
````{tab-item} Windows
```bash
$ cd <target_directory_name>
```
````
````{tab-item} MacOS
```bash
$ cd <target_directory_name>
```
````
`````

We will do this to navigate to our `cfm` directoy. For example if, as in the
Algebra {ref}`algebra_tutorial` the `cfm` directory was on the `Desktop`
directory we would run the following:

`````{tab-set}
````{tab-item} Windows
```bash
$ cd Desktop
$ cd cfm
```
````
````{tab-item} MacOS
```bash
$ cd Desktop
$ cd cfm
```
````
`````

```{attention}
The two statements are written under each other to denote that they are run
one after the other.
```

We will now create a new directory:

`````{tab-set}
````{tab-item} Windows
```bash
$ mkdir scripts
```
````
````{tab-item} MacOS
```bash
$ mkdir scripts
```
````
`````

Inside this directory we will run the same command as before to see the
contents:

`````{tab-set}
````{tab-item} Windows
```bash
$ dir
```
````
````{tab-item} MacOS
```bash
$ ls
```
````
`````

If you have followed the same steps described in {ref}`using_notebooks` then you
will see something similar to:

```{figure} ./img/output_of_dir/main.png
---
width: 75%
name: fig:output_of_dir
---
The contents of our directory on Windows
```

```{figure} ./img/output_of_ls/main.png
---
width: 75%
name: fig:output_of_ls
---
The contents of our directory on OS X
```

We will come back to this directory shortly but now we are going to install a
powerful code editor.

1. Navigate to <https://code.visualstudio.com>.
2. Download the installer making sure it is the correct one for your operating
   system (Windows, Mac OSX, Linux).
3. Run the installer.

This code editor will offer us a different way to write Python code.

Open VS code and create a new file.

In it write the following (which corresponds to the solution of our problem):

```python
"""
This script displays the solution to the problem considered.
"""
import sympy as sym

print("Question 1:")
expression = 1 / (sym.sqrt(2) + 1)
print(sym.simplify(expression))
```

This is shown:

```{figure} ./img/code_in_vscode/main.png
---
width: 75%
name: fig:code_in_vscode
---
The code above in VS code
```

We will now save this as `algebra.py` inside the `scripts` directory we created
earlier.

```{figure} ./img/saving_file_in_vscode/main.png
---
width: 75%
name: fig:saving_file_in_vscode
---
Saving `algebra.py` in VS code.
```

VScode now recognises the Python language and adds syntax colouring. It also
suggests a plugin specific for the Python language. There is more information
about plugins in the rest of this chapter.

```{figure} ./img/syntax_colouring_and_plugin_suggestion/main.png
---
width: 75%
name: fig:syntax_colouring_and_plugin_suggestion
---
Syntax colouring and plugin suggestion for the now recognised Python file.
```

All we have done so far is write the code. We now need to tell Python to run it.
To do this we will use the command line.

Navigate to the `scripts` directory that we created earlier:


`````{tab-set}
````{tab-item} Windows
```bash
$ cd scripts
```
````
````{tab-item} MacOS
```bash
$ cd scripts
```
````
`````

Now confirm that the `algebra.py` file is in that directory:

`````{tab-set}
````{tab-item} Windows
```bash
$ dir
```
````
````{tab-item} MacOS
```bash
$ ls
```
````
`````

Now we will run the python code in that script:

```bash
$ python algebra.py
```

When doing that you should see the following output:

```{figure} ./img/output_of_running_script/main.png
---
width: 75%
name: fig:output_of_running_script
---
Output of running the `algebra.py` script on OS X.
```
