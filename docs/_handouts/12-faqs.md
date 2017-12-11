---
layout     : post
categories : 2017-2018
title      : "2017-2018: Handout 12 - Frequently asked questions"
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

Using Sympy to solve differential equations

## What title to use with the submission?

When submitting via turnitin, there is a field to enter a submission title: it
doesn't matter what you put there but use the title of your coursework.

## What do I submit?

You submit the pdf (**not** the source LaTeX code or any jupyter notebooks).

## How to include a plot in my LaTeX document?

The most straightforward way to include a plot in your LaTeX document is to draw
the plot using `sympy` and/or `matplotlib` and the save that do a file which is
then included in your LaTeX.

For example:

```python
>>> import matplotlib.pyplot as plt
>>> plt.plot([1, 2, 3], [5, 1, 3])
>>> plt.savefig("plot.pdf")
```

Then put the `plot.pdf` file in the same directory as your LaTeX document
(**or** upload it to your overleaf project) and include it in your document
using:

```latex
\includegraphics[width=5cm]{plot.pdf}
```

## My floats (tables and figures) are moving around in my document?

There are various reasons for this and the short answer is to not worry about
it. But, you can allow your tables and figures to be slightly more anchored to
where you locate them. An explanation of why and how to do this is here:
https://vknight.org/cfm/handouts/2016-2017/06-latex-file-paths-and-figures/

## How can I draw a picture in LaTeX?

You can draw a picture and save it and include it using `includegraphics`. You
can also draw various pictures using tikz (see the lab sheet on LaTeX).

Some examples of pictures I have used in a recent research paper:

- [A moran
  process](https://github.com/Axelrod-Python/axelrod-moran/blob/master/tex/moran_process.tex)
- [A finite state
  machine](https://github.com/Axelrod-Python/axelrod-moran/blob/master/tex/fsm_one.tex)

Here is a gallery of many impressive tikz
pictures: http://www.texample.net/tikz/examples/http://www.texample.net/tikz/examples/

## I would like to change how my references appear?

You can modify the style of your references in various ways. Using the default
bibliography, the simplest is to change `\bibliographystyle{plain}` to other
styles. A good list of options is available here:
https://www.sharelatex.com/learn/Bibtex_bibliography_styles

Another way to control your references is to use a completely different LaTeX
package called `biblatex`. Here is a minimal working version:

```latex
\documentclass{article}
\usepackage{biblatex}
\addbibresource{bibliography.bib}

\begin{document}
    \cite{reference_key}

\printbibliography
\end{document}
```

A good guide for using biblatex is available here:
https://www.sharelatex.com/blog/2013/07/31/getting-started-with-biblatex.html

## How do I reference a website?

Here is a simple way to reference a website:

```
@misc{onsemployement,
  title = {The ONS: employement rate},
  howpublished = {\url{https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/lf24/lms}},
  note = {Accessed: 2016-11-16}
}
```

When you do this, include the following at the top of your main LaTeX document:

```
\usepackage{hyperref}
```

## Can I reference wikipedia?

If you take your information from wikipedia you **should** reference wikipedia.
**But** I recommend thinking of wikipedia as a great open conversation with
friends: if a friend told you to write something in your report you would
(hopefully) be likely to check if what they said is correct in another source.

## My code doesn't work?

At this stage of the course I'm hoping you've gained the ability to debug your
code but I understand that this can sometimes still be difficult.

When you code is not working, my advice:

- Step away from the keyboard;
- Write things out step by step;
- Go back to the lab sheets:
  - If your code is using recursion, go back to the lab sheet on recursion and
    check you're using it correctly.
  - If your code is using lists, go back to the lab sheet on lists and check
    that you understood how they work correctly.
  - ...

Here is a concrete example of some code that runs but that does not do what is
expected.

```python
>>> def sum_until(N):
...    """
...    Return the sum of all numbers from 0 to N (inclusive)
...    """
...    return sum(range(N))
>>> sum_until(3)
3

```

Here is another example.

```python
>>> def factors(N):
...     """
...     Find all numbers that divide N (not just the prime numbers)
...     """
...     n = 1
...     factors = []
...     while n < N:
...         n += 1
...         if N % n == 0:
...             N = N / n
...             factors.append(n)
...     return factors
>>> factors(9 * 7 * 4)
[2, 3, 6, 7]

```

We see that 4 does not appear and neither does 9 and a few others...
