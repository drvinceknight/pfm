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

## Using notebooks

### Introduction

At the advent of Calculus two mathematicians are credited with its formalisation/invention:

- Isaac Newton
- Gottfried Leibniz

One of the differences between the approaches taken by Newton and Leibniz is their notation:

Newton denoted the derivative of a function \\(f\\) as:

\\[Df\\]

and Leibniz denoted the derivative with the now more commonly used notation:

\\[\frac{df}{dx}\\]

The mathematics itself is unchanged: what changes is the language/notation used to communicate it.

Similarly when giving instructions through code to a computer there are a number
of notations, more commonly called languages available.

We will be using a language called [**Python**](https://www.python.org).

Python was originally designed as a teaching language but it is now popular both in academia and in industry.

In this chapter we will cover:

- Installing the specific distribution of Python on your computer.
- Using something called a Jupyter notebook to write and run Python code.
- Writing descriptive notes using `markdown` and \\(\LaTeX\\) (pronounced Lay-tech).

### Tutorial

#### Installation

1. Navigate to https://www.anaconda.com/products/individual.
2. Identify and download the version of Python 3 for your operating system (Windows, Mac OSX, Linux).
3. Run the installer.

**Note:** If you have already used Python it is still recommended that you use the Anaconda distribution. An explanation for this is available later.

#### Starting a Jupyter notebook server

We are going to use **Jupyter notebooks** for the first part of this course. This interface to Python works inside your web browser but does not require an internet connect.

Open a command line tool:

1. On **Windows** search for `Anaconda Prompt` (it should be available to you after installing Anaconda.
2. On **OS X** search for `terminal`

In there type:

    $ jupyter notebook

and then press `Enter` on your keyboard.

**Note:** Throughout this course, when there are commands to be typed in a command line tool I will prefix them with a `$`. Do not type the `$`.

![](./img/starting_the_notebook_server/main.png)

This will open a new page in your browser. The url bar at the top should have something that looks like: `http://localhost:8888/tree`.

![](./img/the_jupyter_interface/main.png)

This is the general interface to the Jupyter server. It shows the general file structure on your computer.

#### Creating a new notebook

In the top right, click on the `new` button and click on `Python 3`.

![](./img/creating_a_new_notebook/main.png)

Let us change the name of the notebook by clicking on "Untitled" and changing the name. We will call it "introduction".

![](./img/changing_notebook_name/main.png)

Once this is done let us close the notebook by closing the corresponding tab of your web browser.

#### Organising our files

Open your file browser:

1. File Explorer on **Windows**
2. Finder on **OS X**

Navigate to where your notebook is (this might not be immediately evident): you
should see a `introduction.ipynb` file.

Let us rearrange things.

Find a location on your computer where you want to keep the files for this course, using your file browser:

1. Create a new directory called `cfm` (short for "Computer for Mathematics");
2. Inside that directory create a new directory called `nbs` (short for "Notebooks");
3. Move the `introduction.ipynb` file to this `nbs` directory.

![](./img/new_directory_structure/main.png)

#### Writing some basic Python code

Go back to our Jupyter notebook server (in your browser).

Use the interface to navigate to the `cfm` directory and inside that the `nbs` directory and open the `introduction.ipynb` notebook.

![](./img/opening_notebook/main.png)

In the first available "cell" write the following calculation:

```python
2 + 2
```

When you have done that click on the `Run` button (you can also use `Shift + Enter` as a keyboard shortcut).

![](./img/running_code/main.png)

```{code-cell} ipython3
2 + 2
```

We see two different things there:

1. The input: `In [1]` which is the instruction to Python to use the mathematical technique of addition to compute 2 + 2.
2. The output: `Out [1]` showing the output that Python has returned as a result of the instruction.


#### Writing markdown

One of the reasons for using Jupyter notebooks is that it allows us to include both code and communication using something called `markdown`.

Create a new cell and change the cell type to `Markdown`. Now write the following in there:

```md
As well as using Python in Jupyter notebooks we can also write using Markdown. This allows us to use basic \\(\LaTeX\\) as a way to display mathematics. For example:

1. \\(\frac{2}{3}\\)
2. \\(\sum_{i=0}^n i\\)

```

When you run that it should look like:

![](./img/rendering_markdown/main.png)

#### Saving your notebook to a different format

Click on `File` and `Download As` this brings up a number of formats that
Jupyter notebooks can be exported to. Some of these might need other tools
installed on your computer but a portable option is `HTML`.

Click on `HTML (.html)`.

Now use your file browser and open the downloaded file. This will open in your browser a static version of the file you have been working on. This is a helpful way to share your work with someone who might not have Jupyter (or even Python).

+++

### How To

#### Install Anaconda

1. Navigate to https://www.anaconda.com/products/individual
2. Download the distribution of anaconda for your Operating System
3. Run the installer

#### Start a Jupyter notebook server

1. Open a command line tool (`Anaconda prompt` on Windows, `terminal` on OS X);
2. Type `jupyter notebook` and press `Enter`

#### Create a new notebook

1. Navigate to the location you want using the Jupyter interface;
2. Click on the `new` button in the top right;
3. Rename the notebook (change `Untitled` in the top left to a name of your choice).

#### Find/open a notebook

Using a file browser you can navigate the directories and files on your computer. Jupyter notebooks appear as generic files with the `.ipynb` extension.

You cannot double click on these to open them, you need to navigate to them through the Jupyter interface.

#### Run Python code

In a Jupyter notebook cell write an instruction, for example:

```python
3 / 5
```

and click on the `Run` button or use `Shift + Enter` as a keyboard shortcut.

##### Carry out basic arithmetic operations

The python code for the following arithmetic operations are:

1. Addition, \\(2 + 2\\): `2 + 2`;
2. Subtraction, \\(3 - 1\\): `3 - 1`;
3. Multiplication, \\(3 \times 5\\): `3 * 5`;
5. Division, \\(20 / 5\\): `20 / 5`;
6. Exponentiation, \\(2 ^ 4\\): `2 ** 4`;
7. Integer remainder, \\(5 \mod 2\\): `5 % 2`;
8. Combining operations, \\(\frac{2 ^ 3 + 1}{4}\\): `(2 ** 3 + 1) / 4`;

**Note** that instructions to a computer (through the code we write) need to be specific. For example the `^` symbol in Python does not mean exponentiation. If you were to type `2 ^ 4` you would get an error.

In later chapters we will see what the specific instructions are to carry out more complex operations.

#### Write markdown

To write markdown click no a cell and change the type to `Markdown`, you can do this by click on `Cell`, `Cell Type` or by using the scroll wheel in the menu bar.

Markdown is a lightweight "mark up" language that allows you to write and
include various types of formatting which include:

1. Headings;
2. Bold and italics;
3. Ordered and unordered lists;
4. Code (which will only be displayed but not run);
5. Hyperlinks

The syntax is relatively straightforward and the following is a good guide:

https://www.markdownguide.org/cheat-sheet/


#### Write basic LaTeX

Jupyter notebooks allow for markdown cells to not only include markdown but also include mathematics using another "mark up" language called \\(\LaTeX\\). In the second part of the course we will see how to write \\(\LaTeX\\) more formally (usually it is not written inside of a Jupyter notebook).

Here is a brief overview of the syntax for arithmetic operations:

- `\\\(a+b\\\)` gives: \\(a + b\\):
- `\\\(a-b\\\)` gives: \\(a-b\\)
- `\\\(-a\\\)` gives: \\(-a\\)
- `\\\(ab\\\)` gives \\(ab\\)
- `\\\(a\cdot b\\\)` gives \\(a\cdot b\\)
- `\\\(a\times b\\\)` gives \\(a\times b\\)
- `\\\(a/b\\\)` gives \\(a/b\\)
- `\\\(\frac{a}{b}\\\)` gives \\(\frac{a}{b}\\)

The `\\\(<expression>\\\)` delimiters create what is called an "inline" mathematics. You can change the brackets to `\\\[<expression>\\\]` to give "displayed mathematics".

We can write a matrix:

```
\\\[
    \begin{pmatrix}
        a&b\\
        c&d\\
        e&f\\
    \end{pmatrix}
\\\]
```

gives:

\\[
    \begin{pmatrix}
        a&b\\
        c&d\\
        e&f\\
    \end{pmatrix}
\\]

We can write integrals:


```
\\\[
    \int_{0}^{\infty}x dx
\\\]
```

gives:

\\[
    \int_{0}^{\infty}x dx
\\]

We can write summations:


```
\\\[
    \sum_{0}^{n}i
\\\]
```

gives:

\\[
    \sum_{0}^{n}i
\\]

**Note** when writing \\(\LaTeX\\) in jupyter notebooks we need the double slash `\\` but when writing \\(\LaTeX\\) in its native environment a single quote is the correct syntax. We will see this in the second part of the course.

#### Save the output in a different format

Click on `File` then `Download as` and choose the format you want to use. `HTML`
is a portable option that can be viewed on most devices, note however that you
cannot run the cells: what you are downloading a is static version of your
notebook.  

+++

### Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. Create a new notebook rename it "exercises". Navigate to it using your file browser to make sure you can find it.
2. Write and run some Python code to carry out the following calculations
    1. \\(3 + 8\\)
    2. \\(3 / 7\\)
    3. \\(456 / 21\\)
    5. \\(\frac{4 ^ 3 + 2}{2\times 5} - 5 ^ {\frac{1}{2}}\\)
3. Write a markdown cell with the following and view the rendered version:

    ```md
    # Euler's equation

    \\\[
     e ^ {i\pi} = -1
 \\\]
    ```
4. Render the following expressions by writing markdown
   1. \\(\frac{4 ^ 3 + 2}{2\times 5}\\)
   2. \\(- 5 ^ {\frac{1}{2}}\\)
   3. \\(\frac{df}{dx}\\)
   4. \\(\int_{5}^{12}x^2dx\\)
   5. \\(\begin{pmatrix}4 & 12 & 3\\2 & x & i\\\end{pmatrix}\\)
5. Save your notebook to `HTML` and open and view it.

+++

### Reference

#### Why use anaconda?

Python is a free an open source piece of software. One of the main reasons for its popularity is that there are a number of separate tools that work well with it, these are called libraries. Sometimes installing these libraries can require an understanding of some potential pitfalls. In scientific circles the Anaconda distribution was developed to give a single download of not only Python but a lot of commonly used libraries.

If you want to read more about this here are some web resources:

- https://medium.com/@RustyComer/why-use-anaconda-524bb6765e4d
- https://medium.com/pankajmathur/what-is-anaconda-and-why-should-i-bother-about-it-4744915bf3e6
- https://www.reddit.com/r/Python/comments/betkoj/why_use_anaconda/

#### Why use Jupyter?

There are are variety of ways to write and run Python:

1. Using an interactive notebook environment like Jupyter;
2. Using an integrated development environment and/or editor.

We will in fact use the second approach in the second part of this course.

One strength of Jupyter are that it allows you to include communication (writing through markdown) with your code. This allows you to use code and describe what you're using it for.

Another advantage is that it allows you to immediately have your output next to your input.

There are some limitations to Jupyter as an editor which is why we will explore using a powerful editor in the second part of the course.

In general:

1. Jupyter is a fantastic way to interactively use and communicate code;
2. Integrated development environments and/or editors are the correct tool to write software.

In this course you will learn to use either approach in the appropriate manner for the right task. For the first part we will mainly be using code interactively and so we will use Jupyter notebooks.

If you are interested here are some further resources:

- Why Jupyter Notebooks Are So Popular Among Data Scientists: https://analyticsindiamag.com/why-jupyter-notebooks-are-so-popular-among-data-scientists/
- 10 reasons why data scientists love Jupyter notebooks: https://hub.packtpub.com/10-reasons-data-scientists-love-jupyter-notebooks/
- I don't like notebooks.- Joel Grus (Allen Institute for Artificial Intelligence): https://www.youtube.com/watch?v=7jiPeIFXb6U

Some further information on using Jupyter:

- https://jupyter-notebook-beginner-guide.readthedocs.io/
- https://www.analyticsvidhya.com/blog/2018/05/starters-guide-jupyter-notebook/


#### Why can I not double click on a Jupyter notebook file

When you double click on a file and your computer opens it in an application
that is because a default is set for the particular file extension. For example
double clicking on `main.docx` will automatically open up the document using a
word processor (like Microsoft word). This is because the file has the extension
`.docx` and your operating system has set that anything with that extension will
be opened in that particular application. You could also open the
application and navigate to the file and open it directly.

With Jupyter notebooks no default is set by the operating system as the application that opens it is in fact a local web server in your browser. As such you do not have a choice and need to open it in the Jupyter interface.

#### What is markdown

As described here https://www.markdownguide.org/getting-started/:

> Markdown is a lightweight markup language that you can use to add formatting elements to plain text text documents. Created by John Gruber in 2004, Markdown is now one of the world’s most popular markup languages


#### What is LaTeX

As described here https://www.latex-project.org/about/:

> LaTeX, which is pronounced «Lah-tech» or «Lay-tech» (to rhyme with «blech» or «Bertolt Brecht»), is a document preparation system for high-quality typesetting. It is most often used for medium-to-large technical or scientific documents but it can be used for almost any form of publishing.

> LaTeX is not a word processor! Instead, LaTeX encourages authors not to worry too much about the appearance of their documents but to concentrate on getting the right content.

We will learn more about \\(\LaTeX\\) in the later part of this course but for
now we only need to know that it we can use \\(\LaTeX\\) to write an instruction
for Jupyter to display mathematics.

#### What is a markup language

\\(\LaTeX\\) and markdown are both examples of what is called a **markup language**. Another common example of a markup language is html (the way web pages are written).

A markup language is a system that allows us to write content alongside annotations to specify how the content is to appear.

This description of markdown from https://www.markdownguide.org/getting-started/ is not specific to markdown but to any markup language:

> Using Markdown is different than using a WYSIWYG editor. In an application like Microsoft Word, you click buttons to format words and phrases, and the changes are visible immediately. Markdown isn’t like that. When you create a Markdown-formatted file, you add Markdown syntax to the text to indicate which words and phrases should look different.

In general whilst it might take a little while to learn all the intricacies of a markup language it allows for more portability and precision.

Markup languages differ in complexity:

- \\(\LaTeX\\) is incredibly sophisticated and has a huge range of capabilities.
- Markdown is designed to be basic with a few specific annotations to remember.
