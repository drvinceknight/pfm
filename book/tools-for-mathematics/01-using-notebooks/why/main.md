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

# Further information

## Why use anaconda?

Python is a free an open source piece of software. One of the main reasons for
its popularity is that there are a number of separate tools that work well with
it, these are called libraries. Sometimes installing these libraries can require
an understanding of some potential pitfalls. In scientific circles the Anaconda
distribution was developed to give a single download of not only Python but a
lot of commonly used libraries.

If you want to read more about this here are some web resources:

- <https://medium.com/@RustyComer/why-use-anaconda-524bb6765e4d>
- <https://medium.com/pankajmathur/what-is-anaconda-and-why-should-i-bother-about-it-4744915bf3e6>
- <https://www.reddit.com/r/Python/comments/betkoj/why_use_anaconda/>

## Why use Jupyter?

There are are variety of ways to write and run Python:

1. Using an interactive notebook environment like Jupyter;
2. Using an integrated development environment and/or editor.

We will in fact use the second approach in the second part of this course.

One strength of Jupyter are that it allows you to include communication (writing
through markdown) with your code. This allows you to use code and describe what
you're using it for.

Another advantage is that it allows you to immediately have your output next to your input.

There are some limitations to Jupyter as an editor which is why we will explore
using a powerful editor in the second part of the course.

In general:

1. Jupyter is a fantastic way to interactively use and communicate code;
2. Integrated development environments and/or editors are the correct tool to
   write software.

In this course you will learn to use either approach in the appropriate manner
for the right task. For the first part we will mainly be using code
interactively and so we will use Jupyter notebooks.

If you are interested here are some further resources:

- Why Jupyter Notebooks Are So Popular Among Data Scientists: <https://analyticsindiamag.com/why-jupyter-notebooks-are-so-popular-among-data-scientists/>
- 10 reasons why data scientists love Jupyter notebooks: <https://hub.packtpub.com/10-reasons-data-scientists-love-jupyter-notebooks/>
- I don't like notebooks - Joel Grus (Allen Institute for Artificial Intelligence): <https://www.youtube.com/watch?v=7jiPeIFXb6U>

Some further information on using Jupyter:

- <https://jupyter-notebook-beginner-guide.readthedocs.io/>
- <https://www.analyticsvidhya.com/blog/2018/05/starters-guide-jupyter-notebook/>

## Why can I not double click on a Jupyter notebook file?

When you double click on a file and your computer opens it in an application
that is because a default is set for the particular file extension. For example
double clicking on `main.docx` will automatically open up the document using a
word processor (like Microsoft word). This is because the file has the extension
`.docx` and your operating system has set that anything with that extension will
be opened in that particular application. You could also open the
application and navigate to the file and open it directly.

With Jupyter notebooks no default is set by the operating system as the
application that opens it is in fact a local web server in your browser. As such
you do not have a choice and need to open it in the Jupyter interface.

## Where can I find keyboard shortcuts for using Jupyter

In a notebook if you go to the menu bar and click on `Help` followed by
`Keyboard Shortcuts` you will find a number of helpful keyboard shortcuts.

For example, when on a cell pressing `Esc` followed by `m` will turn the cell in
to a markdown cell.

## What is markdown?

As described here <https://www.markdownguide.org/getting-started/>:

> Markdown is a lightweight markup language that you can use to add formatting
> elements to plain text text documents. Created by John Gruber in 2004,
> Markdown is now one of the world’s most popular markup languages

## What is LaTeX?

As described here <https://www.latex-project.org/about/>:

> LaTeX, which is pronounced «Lah-tech» or «Lay-tech» (to rhyme with «blech» or
> «Bertolt Brecht»), is a document preparation system for high-quality
> typesetting. It is most often used for medium-to-large technical or scientific
> documents but it can be used for almost any form of publishing.

> LaTeX is not a word processor! Instead, LaTeX encourages authors not to worry
> too much about the appearance of their documents but to concentrate on getting
> the right content.

We will learn more about $\LaTeX$ in the later part of this course but for
now we only need to know that it we can use $\LaTeX$ to write an instruction
for Jupyter to display mathematics.

(why_do_we_use_brackets_instead_of_dollars_for_latex)=

## Why do we use `\\(` and `\\)` instead of `$` for LaTeX?

You will see in some places that `$` can be used as a delimiter for LaTeX. This
is not recommended for a number of reasons one of which is given at
<https://vknight.org/tex/#12-inline-mathematics>:

> Note that using \( and \) is preferred over \$. One of the reasons is that it
> is easier for humans (and machines) to find the start and end of some
> mathematics.

## Why do we use a double `\\` for `\\(` and `\\)` and not a single `\` as can be seen elsewhere?

This is one of the particularities of using LaTeX in a Jupyter notebook as
opposed to using it elsewhere. The `\` symbol could be misinterpreted in Jupyter
and so it has to be "escaped" with a second `\`.

## Other resources for LaTeX syntax.

This cheat sheet: <http://tug.ctan.org/info/undergradmath/undergradmath.pdf>

This web page is my recommended set of resources for learning LaTeX:
<https://vknight.org/tex/>.

## What is a markup language?

$\LaTeX$ and markdown are both examples of what is called a **markup language**.
Another common example of a markup language is html (the way web pages are
written).

A markup language is a system that allows us to write content alongside
annotations to specify how the content is to appear.

This description of markdown from
<https://www.markdownguide.org/getting-started/> is not specific to markdown but
to any markup language:

> Using Markdown is different than using a WYSIWYG editor. In an application
> like Microsoft Word, you click buttons to format words and phrases, and the
> changes are visible immediately. Markdown isn’t like that. When you create a
> Markdown-formatted file, you add Markdown syntax to the text to indicate which
> words and phrases should look different.

In general whilst it might take a little while to learn all the intricacies of a
markup language it allows for more portability and precision.

Markup languages differ in complexity:

- $\LaTeX$ is incredibly sophisticated and has a huge range of capabilities.
- Markdown is designed to be basic with a few specific annotations to remember.

## I only have a chromebook: how can I use notebooks?

There are a number of cloud based services that give access to scientific Python
environments. This medium article gives a brief review of 5 of them:
<https://medium.com/@siddesh.001/top-5-online-free-notebook-ipynb-and-other-cloud-services-dbf9580d99e3>
(this is dated 2018).

I recommend using cocalc: <https://cocalc.com>. The free tier does have some
limitations but it should be sufficient to be able to work through this book.

## I only have a tablet: how can I use notebooks?

There are two iOS apps that I am aware of for notebooks:

- [Carnets](https://apps.apple.com/us/app/carnets-jupyter/id1450994949)
- [Juno](https://juno.sh)

I have experimented with Carnets but not with Juno.
