---
layout     : post
categories : 2016-2017
title      : "2016-2017: Handout 08 - Libraries, referencing and floating figures."
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1400-1600**

## What you have learnt this week:

Using Sympy to carry out calculations relevant to Calculus: limits, derivatives,
integrals and plotting.

## Libraries

Python has various libraries that comes as standard (`import math`, `import
random` etc). With Anaconda, there are a number of other scientific libraries
readily available to you (`import sympy`, `import numpy` etc...).

There are however a **huge** number of libraries that are not included with
Anaconda but that are readily available to you (this is one of the strengths of
Python).

To install them you can write a simple command at the command line of your
computer:

- On Mac OSX: look for "terminal";
- On Windows: look for "command prompt".

Once there simply type:

```bash
pip install <package-name>
```

Note that if you're on a university computer you need to type:

```bash
pip install --user <package-name>
```

For example, if you wanted to study queues, you could use a package called `ciw`
which is actually written by a Cardiff University PhD student ([Geraint
Palmer](http://www.geraintianpalmer.org.uk/)). To install this you'd run:

```bash
pip install ciw
```

To use it you'd take a look at the documentation which is here:
[ciw.readthedocs.org/](http://ciw.readthedocs.org/).

There are numerous libraries that exist in Python, depending on what you're
working on they might be helpful.

## Referencing in LaTeX

As you will have noticed in the instructions your individual coursework has the
following statement in it:

> You are submitting work this way as “Turnitin” is a product purchased by the
> University which checks for plagiarism.

Plagiarism is a serious offense and comes under Cardiff University's unfair
practice regulations:
[www.cardiff.ac.uk/public-information/policies-and-procedures/academic-regulations](http://www.cardiff.ac.uk/public-information/policies-and-procedures/academic-regulations)

Here is some guidance on avoiding plagiarism:
[intranet.cardiff.ac.uk/students/your-study/exams-and-assessment/sitting-your-exam/cheating-and-unfair-practice/plagiarism](https://intranet.cardiff.ac.uk/students/your-study/exams-and-assessment/sitting-your-exam/cheating-and-unfair-practice/plagiarism)

To put this simply: make sure you reference work that is not original work being
done for the purposes of this assessment.

To reference an article here is the corresponding bibtex code:

```latex
@article{knight2016open,
  title={An Open Framework for the Reproducible Study of the Iterated Prisoner’s Dilemma},
  author={Knight, Vincent and Campbell, Owen and Harper, Marc and Langner, Karol and Campbell, James and Campbell, Thomas and Carney, Alex and Chorley, Martin and Davidson-Pilon, Cameron and Glass, Kristian and others},
  journal={Journal of Open Research Software},
  volume={4},
  number={1},
  year={2016},
  publisher={Ubiquity Press}
}
```

Here is one way of referencing a website:

```latex
@misc{onsemployement,
  title = {The ONS: employement rate},
  howpublished = {\url{https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/lf24/lms}},
  note = {Accessed: 2016-11-16}
}
```

Note: to use `\url` you need to include `\usepackage{hyperref}` in your
preamble.

## Floating figures

We can include figures and tables in LaTeX using:

    \begin{figure}
    \begin{center}
    \includegraphics{...}
    \end{center}
    \end{figure}

    \begin{table}
    \begin{tabular}
    \begin{center}
    ...
    \end{center}
    \end{tabular}
    \end{table}

Figures and Tables _move_ in LaTeX, ie if we put them in some specific place in
the code they potentially do not appear there in the pdf. This is called
_floating_.

In general 'trust' LaTeX to put them in the correct place and refer to figure
and tables using `\ref` and `\label`.

LaTeX places these things in such a way as to format documents in an
esthetically pleasing way. You can pass certain options to LaTeX to get it to
ignore certain constraints:

- `h` indicates that it can place the float inline;
- `t` indicates that it can place the float in the top area;
- `b` indicates that it can place the float in the bottom area;
- `p` indicates that it can place the float on a float page or column area;
- `!` indicates that further constraints can be ignored.

In practice this means, use:

    \begin{figure}[!htbp]

Take a look at this writeLaTeX [http://goo.gl/k83ZHi](http://goo.gl/k83ZHi)
template to play around with this.
