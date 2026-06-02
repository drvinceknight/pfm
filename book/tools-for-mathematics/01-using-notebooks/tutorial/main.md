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

`````{tab-set}
````{tab-item} Windows
The recommended way to install Python on Windows is through the
**Python Install Manager** from python.org.

1. Navigate to <https://www.python.org/downloads/> and click
   **"Download Python install manager"**.

   ```{figure} ./img/python_download_windows/main.png
   ---
   width: 75%
   name: fig:python_download_windows
   ---
   The python.org downloads page with the Python install manager button.
   ```

2. Once the download finishes, open the downloaded file. In the dialog that
   appears, click **"Install Python"**.

   ```{figure} ./img/python_install_manager_dialog/main.png
   ---
   width: 75%
   name: fig:python_install_manager_dialog
   ---
   Confirming the Python Install Manager installation.
   ```

3. The Python Install Manager opens in your terminal. When asked "Add
   commands directory to your PATH now?", type `y` and press `Enter`.

   ```{figure} ./img/python_install_manager_path/main.png
   ---
   width: 75%
   name: fig:python_install_manager_path
   ---
   Adding Python to PATH via the Python Install Manager.
   ```

4. When asked "Install CPython now?", type `Y` and press `Enter` and wait
   for the installation to complete.

   ```{figure} ./img/python_install_manager_cpython/main.png
   ---
   width: 75%
   name: fig:python_install_manager_cpython
   ---
   Installing CPython via the Python Install Manager.
   ```

5. Open **Windows PowerShell** from the Start menu (search for "Terminal" or
   "PowerShell").

   ```{figure} ./img/windows_terminal_open/main.png
   ---
   width: 75%
   name: fig:windows_terminal_open
   ---
   Opening Windows PowerShell from the Start menu.
   ```

6. Install the Python libraries needed for this book by typing the following
   and pressing `Enter`:

   ```console
   $ python -m pip install jupyter sympy numpy matplotlib scipy
   ```

   ```{figure} ./img/pip_install_windows/main.png
   ---
   width: 75%
   name: fig:pip_install_windows
   ---
   Installing the required libraries in Windows PowerShell.
   ```
````

````{tab-item} macOS
1. Navigate to <https://www.python.org/downloads/> and download the latest
   Python 3 installer for macOS.

   ```{figure} ./img/python_download_macos/main.png
   ---
   width: 75%
   name: fig:python_download_macos
   ---
   Downloading Python for macOS from python.org.
   ```

2. Run the installer and follow the default prompts.

   ```{figure} ./img/python_installer_macos/main.png
   ---
   width: 75%
   name: fig:python_installer_macos
   ---
   The Python installer on macOS.
   ```

3. Open **Terminal** (press `Cmd + Space`, type `Terminal`, press `Enter`).

   ```{figure} ./img/terminal_open_macos/main.png
   ---
   width: 75%
   name: fig:terminal_open_macos
   ---
   Opening Terminal on macOS.
   ```

4. Install the Python libraries needed for this book by typing the following
   and pressing `Enter`:

   ```console
   $ python3 -m pip install jupyter sympy numpy matplotlib scipy
   ```

   ```{figure} ./img/pip_install_macos/main.png
   ---
   width: 75%
   name: fig:pip_install_macos
   ---
   Installing the required libraries in Terminal on macOS.
   ```
````

````{tab-item} Google Colab
Google Colab is a free cloud-based Jupyter notebook environment provided by
Google. It runs entirely in your browser and requires no local installation —
only a Google account.

1. Navigate to <https://colab.research.google.com/> and sign in with your
   Google account.

   ```{figure} ./img/colab_sign_in/main.png
   ---
   width: 75%
   name: fig:colab_sign_in
   ---
   Signing in to Google Colab.
   ```

2. Click **"New notebook"** to create a new notebook.

   ```{figure} ./img/colab_new_notebook/main.png
   ---
   width: 75%
   name: fig:colab_new_notebook
   ---
   Creating a new notebook in Google Colab.
   ```

3. The libraries used in this book (`sympy`, `numpy`, `matplotlib`, `scipy`)
   come pre-installed in Google Colab. You can verify this by running the
   following in the first cell (press `Shift + Enter` to run):

   ```python
   import sympy
   import numpy
   import matplotlib
   import scipy
   print("All libraries available.")
   ```

   ```{figure} ./img/colab_verify_libraries/main.png
   ---
   width: 75%
   name: fig:colab_verify_libraries
   ---
   Verifying the required libraries are available in Google Colab.
   ```

4. Rename your notebook by clicking on "Untitled0.ipynb" at the top of the
   page and typing a new name, then press `Enter`.

   ```{figure} ./img/colab_rename_notebook/main.png
   ---
   width: 75%
   name: fig:colab_rename_notebook
   ---
   Renaming a notebook in Google Colab.
   ```

Your notebook is automatically saved to Google Drive. You can now skip ahead
to [Writing some basic Python code](writing-some-basic-python-code).
````
`````

### Starting a Jupyter notebook server

```{note}
If you are using Google Colab you can skip this section and continue from
[Writing some basic Python code](writing-some-basic-python-code).
```

`````{tab-set}
````{tab-item} Windows
Open **Windows PowerShell** from the Start menu
(see {ref}`fig:windows_terminal_open`). In there type (without the `$`):

```console
$ python -m notebook
```
````

````{tab-item} macOS
Open **Terminal** (see {ref}`fig:terminal_open_macos`). In there type
(without the `$`):

```console
$ python3 -m notebook
```
````
`````

Press `Enter` on your keyboard.

```{tip}
Throughout this book, when there are commands to be typed in a command
line they will be prefixed with a `$`. Do not type the `$`.
```

This will open a new page in your browser. The url bar at the top should have
something that looks like: `http://localhost:8888/tree`. This is the
general interface to the Jupyter server. It shows the general file
structure on your computer as shown in {ref}`fig:the_jupyter_interface_windows`.

`````{tab-set}
````{tab-item} Windows

```{figure} ./img/starting_the_notebook_server_windows/main.png
---
width: 75%
name: fig:starting_the_notebook_server_windows
---
Starting the notebook server on Windows.
```
````

````{tab-item} macOS

```{figure} ./img/starting_the_notebook_server/main.png
---
width: 75%
name: fig:starting_the_notebook_server
---
Starting the notebook server on macOS.
```
````
`````

```{figure} ./img/the_jupyter_interface/main.png
---
width: 75%
name: fig:the_jupyter_interface_windows
---
The Jupyter interface.
```

### Creating a new notebook

```{note}
If you are using Google Colab you can skip this section and continue from
[Writing some basic Python code](writing-some-basic-python-code).
```

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
Creating a new notebook.
```

Let us change the name of the notebook by clicking on "Untitled" and changing
the name. We will call it "introduction".

```{figure} ./img/changing_notebook_name/main.png
---
width: 75%
name: fig:changing_notebook_name
---
Changing the notebook name.
```

## Organising our files

```{note}
If you are using Google Colab your notebook is already saved to Google Drive.
You can organise it there using the Google Drive interface. Skip ahead to
[Writing some basic Python code](writing-some-basic-python-code).
```

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

(writing-some-basic-python-code)=
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

- Installed Python and the required libraries (or set up Google Colab).
- Started a notebook server (or created a notebook in Google Colab).
- Created a new notebook.
- Run some Python code.
- Written some markdown.
- Saved the notebook to a different format.
```
