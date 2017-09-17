---
layout     : post
categories : 2016-2017
title      : "2016-2017: Handout 06 - File paths, formatting, floating figures."
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

## Bibliographies

Some difficulties occurred when using bibliographies. These usually were caused
by 1 of the following errors:

- Not writing the correct code (wrong file name etc.).
- Not deleting the auxiliary files.

The first situation will happen and it's nothing to worry about, as you gain
more experience you will recognise small errors sooner.

The second situation is because of how LaTeX compiles documents: it needs to
create auxiliary files to be able to build the bibliography (it keeps track of
where things go). If you've made a slight error then some of those auxiliary
files will need to be deleted. If you're using overleaf this takes care of
itself, if you're using a local install or cloud.sagemath you'll need to
manually delete these (there is, depending on your system, usually an option to
do this).
