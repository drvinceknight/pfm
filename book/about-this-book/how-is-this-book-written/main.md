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

# How is this book written

## Jupyterbook

The book is written using Jupyterbook: <https://jupyterbook.org/>.

> Jupyter Book is an open source project for building beautiful,
> publication-quality books and documents from computational material.

The source files are written in the myst format
(<https://myst-nb.readthedocs.io/>) format which is a plaintext format for
Jupyter notebooks. This ensures:

- That the notebooks are version controlled effectively.
- The output of the code is an actual computation.

## Continuous integration

The source files of the book are hosted on GitHub and any contribution is tested
using Github Actions which runs a full set of tests.

### Proselint

The proselint <http://proselint.com> tool is used to check various common
suggestions about the prose in text:

> `proselint` places the world’s greatest writers and editors by your side, where
> they whisper suggestions on how to improve your prose. You’ll be guided by
> advice inspired by Bryan Garner, David Foster Wallace, Chuck Palahniuk, Steve
> Pinker, Mary Norris, Mark Twain, Elmore Leonard, George Orwell, Matthew
> Butterick, William Strunk, E.B. White, Philip Corbett, Ernest Gowers, and the
> editorial staff of the world’s finest literary magazines and newspapers, among
> others. Our goal is to aggregate knowledge about best practices in writing and
> to make that knowledge immediately accessible to all authors in the form of a
> linter for prose.

### Alex

The alex <https://github.com/get-alex/alex> tool is used to catch insensitive
and/or inconsiderate language.

> Whether your own or someone else’s writing, alex helps you find gender
> favoring, polarizing, race related, religion inconsiderate, or other unequal
> phrasing in text.

This does not ensure that all writing could not be made more inclusive and
suggestions are actively encouraged in this domain.

### Spell check

The aspell <http://aspell.net> spell checker is used to check the spelling of
the text.

(black)=
### Black

All code in book is checked to follow the `black` code formatter
<https://github.com/psf/black> this ensure that not only PEP8 is followed but
that specific formatting convention is used.

> Black is the uncompromising Python code formatter. By using it, you agree to
> cede control over minutiae of hand-formatting. In return, Black gives you
> speed, determinism, and freedom from pycodestyle nagging about formatting. You
> will save time and mental energy for more important matters.

### Isort

All imports are sorted according using the `isort`
<https://github.com/PyCQA/isort> tool. Similarly to {ref}`black` this ensures
that all code follows a given condition.

### Nbval

All myst format files are backed up to a Jupyter notebook which includes the
outpout as well as the input. The Continuous Integration then installs up to
date versions of all libraries used and validates the outputs using
<https://nbval.readthedocs.io/en/latest/>. This ensures that the outputs are not
giving unexpected results as a result of an update of a library.
