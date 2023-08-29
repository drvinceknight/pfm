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

# How this book is written

## Jupyterbook

The book is written using Jupyterbook: <https://jupyterbook.org/>.

The source files are written in the myst format
(<https://myst-nb.readthedocs.io/>) which is a plain text format for
Jupyter notebooks. This ensures:

- That the notebooks are version controlled effectively.
- The output of the code is an actual computation.

## Continuous integration

The source files of the book are hosted on GitHub
<https://github.com/drvinceknight/pfm> and any contribution is tested using
Github Actions which runs a full set of tests.

### Proselint

The proselint <http://proselint.com> tool is used to check various common
suggestions about the prose in text.

### Alex

The alex <https://github.com/get-alex/alex> tool is used to catch insensitive
and/or inconsiderate language.

This does not ensure that all writing could not be made more inclusive and
suggestions are actively encouraged in this domain.

### Spell check

The aspell <http://aspell.net> spell checker is used to check the spelling of
the text.

<!--alex disable black-->

(black)=

### Black

All code in book is checked using the `black` code formatter
<https://github.com/psf/black> this ensures that not only PEP8 is followed but
that a specific consistent formatting convention is used.

<!--alex enable black-->

### Isort

All imports are sorted using the `isort`
<https://github.com/PyCQA/isort> tool. Similarly to {ref}`black` this ensures
that all code follows a given convention.
