---
layout     : post
categories : 2016-2017
title      : "2016-2017: File paths, formatting, floating figures"
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1400-1600**

## What you have learnt this week:

LaTeX.

## Paths

There are two (popular) types of operating systems:

- *nix (which powers Linux and Mac computers): more popular for coding.
- Windows: more popular for gaming.

File paths on *nix machines use `/` to separate directories:

    /home/vince/photos

On Windows machines `\` is used:

    C:\vince\photos

LaTeX uses the *nix syntax **even** on Windows.

Good practice:

- No spaces in files and/or directory names.
- Have a directory in your folder with your images: `images`. Refer to those images:

        \includegraphics{./images/pic.png}

  This helps keep your directory tidy.

## Page formatting

The following in your 'preamble' (before the `\begin{document}`) will use up the full page:

    \usepackage{fullpage}
    \usepackage{parskip}

There are other ways to change the layout of a LaTeX page: [http://en.wikibooks.org/wiki/LaTeX/Page_Layout](http://en.wikibooks.org/wiki/LaTeX/Page_Layout).

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

Figures and Tables _move_ in LaTeX, ie if we put them in some specific place in the code they potentially do not appear there in the pdf. This is called _floating_.

In general 'trust' LaTeX to put them in the correct place and refer to figure and tables using `\ref` and `\label`.

LaTeX places these things in such a way as to format documents in an esthetically pleasing way. You can pass certain options to LaTeX to get it to ignore certain constraints:

- `h` indicates that it can place the float inline;
- `t` indicates that it can place the float in the top area;
- `b` indicates that it can place the float in the bottom area;
- `p` indicates that it can place the float on a float page or column area;
- `!` indicates that further constraints can be ignored.

In practice this means, use:

    \begin{figure}[!htbp]

Take a look at this writeLaTeX [http://goo.gl/k83ZHi](http://goo.gl/k83ZHi) template to play around with this.
