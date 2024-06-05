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

# How to

## Install Anaconda

1. Navigate to <https://www.anaconda.com/products/individual>
2. Download the distribution of anaconda for your Operating System
3. Run the installer

## Start a Jupyter notebook server

1. Open a command line tool (`Anaconda prompt` on Windows, `terminal` on OS X);
2. Type `jupyter notebook` and press `Enter`

## Create a new notebook

1. Navigate to the location you want using the Jupyter interface;
2. Click on the `new` button in the top right;
3. Rename the notebook (change `Untitled` in the top left to a name of your choice).

## Find/open a notebook

Using a file browser you can navigate the directories and files on your computer. Jupyter notebooks appear as generic files with the `.ipynb` extension.

You cannot double click on these to open them, you need to navigate to them through the Jupyter interface.

## Run Python code

In a Jupyter notebook cell write an instruction, for example:

```python
3 / 5
```

and click on the `Run` button or use `Shift + Enter` as a keyboard shortcut.

(carry_out_basic_arithmetic_operations)=

## Carry out basic arithmetic operations

The Python code for the following arithmetic operations are:

1. Addition, $2 + 2$: `2 + 2`;
2. Subtraction, $3 - 1$: `3 - 1`;
3. Multiplication, $3 \times 5$: `3 * 5`;
4. Division, $20 / 5$: `20 / 5`;
5. Exponentiation, $2 ^ 4$: `2 ** 4`;
6. Integer remainder, $5 \mod 2$: `5 % 2`;
7. Combining operations, $\frac{2 ^ 3 + 1}{4}$: `(2 ** 3 + 1) / 4`;

**Note** that instructions to a computer (through the code we write) need to be specific. For example the `^` symbol in Python does not mean exponentiation. If you were to type `2 ^ 4` you would get an error.
In later chapters we will see what the specific instructions are to carry out more complex operations.

## Write markdown

To write markdown click on a cell and change the type to `Markdown`, you can do
this by click on `Cell`, `Cell Type` or by using the scroll wheel in the menu
bar.
Markdown is a lightweight mark up language that allows you to write and
include various types of formatting which include:

1. Headings;
2. Bold and italics;
3. Ordered and unordered lists;
4. [Code](how_to_include_code_in_markdown) (which will only be displayed but not run);
5. [Hyperlinks](how_to_include_a_hyperlink_in_markdown)

A more detailed guide is given in Section~ref{}.

<https://www.markdownguide.org/cheat-sheet/>

## Write basic LaTeX

Jupyter notebooks allow for markdown cells to not only include markdown but also
include mathematics using another mark up language called $\LaTeX$.
Here is a brief overview of the syntax for arithmetic operations:

- `$a+b$` gives: $a + b$:
- `$a-b$` gives: $a-b$
- `$-a$` gives: $-a$
- `$ab$` gives $ab$
- `$a\cdot b$` gives $a\cdot b$
- `$a\times b$` gives $a\times b$
- `$a/b$` gives $a/b$
- `$\frac{a}{b}$` gives $\frac{a}{b}$
- `$a ^ b$` gives $a ^ b$

The `$<expression>$` delimiters create what is called an "inline" mathematics
environment.
You can change these to `$$<expression>$$` to give "displayed
mathematics".

You can write a matrix:

```
$$
    \begin{pmatrix}
        a&b\\
        c&d\\
        e&f\\
    \end{pmatrix}
$$
```

gives:

$$
    \begin{pmatrix}
        a&b\\
        c&d\\
        e&f\\
    \end{pmatrix}
$$

We can write integrals:

```
$$
    \int_{0}^{\infty}x dx
$$
```

gives:

$$
    \int_{0}^{\infty}x dx
$$

We can write summations:

```
$$
    \sum_{0}^{n}i
$$
```

gives:

$$
    \sum_{0}^{n}i
$$

## Save the output in a different format

Click on `File` then `Download as` and choose the format you want to use. `HTML`
is a portable option that can be viewed on most devices, note however that you
cannot run the cells: what you are downloading a is static version of your
notebook.
