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

(sec:using_notebooks_further_information)=

# Further information

## Why use the standard Python distribution?

Python is a free and open source piece of software. One of the main
reasons for its popularity is that there are a number of separate tools
that work well with it, these are called libraries. The standard Python
distribution from <https://www.python.org> gives you Python itself and
`pip`, its built-in package installer. You can then install exactly the
libraries you need, nothing more. This makes it straightforward to understand
what is on your system and to keep it up to date.

## Why have we moved away from Anaconda?

Earlier editions of this book recommended Anaconda as the way to install
Python. We have moved away from that recommendation for two reasons.

First, Anaconda changed its licensing terms in 2020 so that its default
package repository is no longer free for all uses. Organisations with more
than a small number of users must now purchase a commercial licence to use
the default Anaconda channel. Using software under unclear licensing
conditions is not something we want to recommend to readers.

Second, installation on Windows has become considerably easier. The Python
Install Manager (available directly from <https://www.python.org>) provides
a straightforward terminal-based setup that takes only a few steps and
does not require any third-party tools. There is therefore no longer a
practical reason to add the complexity of Anaconda.

The standard distribution gives a cleaner, lighter environment: only the
libraries you explicitly install are present, which makes it easier to
understand what your code depends on and to reproduce your environment on
another machine.

## Why use `python -m notebook` rather than `jupyter notebook`?

Many tutorials and older books instruct readers to start Jupyter by typing
`jupyter notebook` in the terminal. Both commands launch the same
application, so if you encounter that instruction elsewhere it will work
provided the `jupyter` script is on your system's PATH.

We use `python -m notebook` (or `python3 -m notebook` on macOS) throughout
this book for one reason: it always works. When Python installs a library
it places any associated scripts (including `jupyter`) in a scripts
directory. Depending on how Python was installed, that directory may not
be on the system PATH, which means typing `jupyter notebook` produces a
"command not found" error even though the library is correctly installed.
Running `python -m notebook` bypasses the scripts directory entirely: it
asks the Python interpreter you are already using to run the `notebook`
module directly, so there is no PATH lookup to go wrong.

In practice this matters most on Windows, where the Python Install Manager
does not always add the scripts directory to PATH. On macOS the standard
Python from python.org installs the interpreter as `python3`, so the
equivalent command there is `python3 -m notebook`.

## Why use Jupyter?

There are a variety of ways to write and run Python:

1.  Using an interactive notebook environment like Jupyter;
2.  Using an integrated development environment and/or editor.

The second part of this book will use an editor. One strength of Jupyter
is that it allows you to include communication (writing through
markdown) with your code. This allows you to use code and describe what
you are using it for. Another advantage is that it allows you to
immediately have your output next to your input. There are some
limitations to Jupyter as an editor which is why you will explore using
a powerful editor in the second part of the course. In general:

1.  Jupyter is a fantastic way to interactively use and communicate
    code;
2.  Integrated development environments and/or editors are the correct
    tools to write software.

In this book you will learn to use either approach in the appropriate
manner for the right task. For the first part code will be used
interactively and so you will use Jupyter notebooks.

## Why can I not double click on a Jupyter notebook file?

When you double click on a file and your computer opens it in an
application that is because a default is set for the particular file
extension. For example double clicking on `main.docx` will automatically
open up the document using a word processor (like Microsoft word). This
is because the file has the extension `.docx` and your operating system
has set that anything with that extension will be opened in that
particular application. You could also open the application and navigate
to the file and open it directly.

With Jupyter notebooks no default is set by the operating system as the
application that opens it is in fact a local web server in your browser.
As such you do not have a choice and need to open it in the Jupyter
interface.

## Where can I find keyboard shortcuts for using Jupyter

In a notebook if you go to the menu bar and click on `Help` followed by
`Keyboard Shortcuts` you will find a number of helpful keyboard
shortcuts.

For example, when on a cell pressing `Esc` followed by `m` will turn the
cell into a markdown cell.

## What is markdown?

As described at <https://www.markdownguide.org/getting-started/>:

> Markdown is a lightweight markup language that you can use to add
> formatting elements to plain text text documents. Created by John
> Gruber in 2004, Markdown is now one of the world's most popular markup
> languages

## What is LaTeX?

As described here <https://www.latex-project.org/about/>:

> LaTeX, which is pronounced «Lah-tech» or «Lay-tech» (to rhyme with «blech» or
> «Bertolt Brecht»), is a document preparation system for high-quality
> typesetting. It is most often used for medium-to-large technical or scientific
> documents but it can be used for almost any form of publishing.

> LaTeX is not a word processor! Instead, LaTeX encourages authors not to worry
> too much about the appearance of their documents but to concentrate on getting
> the right content.

(why_do_we_use_brackets_instead_of_dollars_for_latex)=

## Can I use `\(` and `\)` instead of `$` for LaTeX?

You will see in some places that `\(`, `\)` or `\[`, `\]` can be used as
delimiters for LaTeX when used outside of Jupyter notebooks. This is in
fact recommended for a number of reasons, one of which is given at
<https://vknight.org/tex/>:

> "Note that using `\(` and `\)` is preferred over \$. One of the
> reasons is that it is easier for humans (and machines) to find the
> start and end of some mathematics."

> Note that using \( and \) is preferred over \$. One of the reasons is that it
> is easier for humans (and machines) to find the start and end of some
> mathematics.

```{warning}
If you want to use `\(`, `\)` or `\[`, `\]` as mathematics delimiters
within Jupyter notebooks you need to escape the `\` and use: `\\(`,
`\\)` or `\\[`, `\\]` instead.
```

## What is a markup language?

LaTeX and markdown are both examples of what is called a **markup
language**. Another common example of a markup language is html (the way
web pages are written). A markup language is a system that allows us to
write content alongside annotations to specify how the content is to
appear. This description of markdown from
<https://www.markdownguide.org/getting-started/> applies to any markup
language:

> Using Markdown is different than using a WYSIWYG editor. In an application
> like Microsoft Word, you click buttons to format words and phrases, and the
> changes are visible immediately. Markdown isn’t like that. When you create a
> Markdown-formatted file, you add Markdown syntax to the text to indicate which
> words and phrases should look different.

In general whilst it might take a little while to learn all the
intricacies of a markup language it allows for more portability and
precision. Markup languages differ in complexity:

- LaTeX is incredibly sophisticated and has a huge range of
  capabilities.

- Markdown is designed to be basic with a few specific annotations to
  remember.

## How to use Jupyter notebooks without a local installation

**Google Colab** (<https://colab.research.google.com/>) is the recommended
option if you cannot install Python locally. It is a free, cloud-based Jupyter
notebook environment provided by Google that runs entirely in your browser.
All libraries used in this book (`sympy`, `numpy`, `matplotlib`, `scipy`) come
pre-installed. The only requirement is a Google account.

Google Colab works on any device with a modern browser, including
Chromebooks and tablets.

(sec:how_to_use_notebooks_on_an_ipad)=

## How to use Jupyter notebooks on an iPad

Google Colab works well in a browser on iPad. Alternatively there are two
dedicated iOS apps:

- [Carnets](https://apps.apple.com/us/app/carnets-jupyter/id1450994949)
- [Juno](https://juno.sh/)
