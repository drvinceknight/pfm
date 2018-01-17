---
layout     : post
title      : "05 - Packaging"
comments   : false
---


## Packaging

At present we need to be in the same directory as your software to be able to
`import` it.

It is possible however to package the code so this is not the case.

Let us rearrange our code directory so it looks like this:

```bash
Pack
|--- src/pack
         |--- __init__.py
         |--- deck.py
         |--- deal.py
|--- tests
     |--- test_pack.py
|--- setup.py
```

- The `Pack` directory (with a capital `P`) contains all the code for our project.
- The `src` directory contains the `pack` directory which contains the source
  code.
- The `tests` directory contains our test files.
- The `setup.py` file is a new file that contains the commands to let python
  know how to bring everything together.

This is what the `setup.py` file should contain:

```python
from setuptools import setup, find_packages

setup(
    name='pack',
    version='0.0.1',
    author='Vince Knight',
    author_email=('knightva@cardiff.ac.uk'),
    packages=find_packages('src'),
    package_dir={"": "src"},
    description='A library to make research using cards easier',
)
```

After we have done all this, if we try and run the tests, they will fail. Your
output will look something like:

```bash
Pack: pytest
================================================================ test session starts =================================================================
platform linux -- Python 3.5.2, pytest-3.3.0, py-1.5.2, pluggy-0.6.0
rootdir: /home/vince/Desktop/Pack, inifile:
plugins: hypothesis-3.2.0, nbval-0.7
collected 0 items / 1 errors

======================================================================= ERRORS =======================================================================
________________________________________________________ ERROR collecting tests/test_pack.py _________________________________________________________
ImportError while importing test module '/home/vince/Desktop/Pack/tests/test_pack.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
tests/test_pack.py:1: in <module>
    import pack
E   ImportError: No module named 'pack'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
============================================================== 1 error in 0.15 seconds ===============================================================

```

As indicated by the error message, this is because the `pack` library (contained
in the `src/pack` directory cannot be found by python.

We remedy this by installing it using the following command:

```bash
python setup.py develop
```

Now we can run the tests:

```bash
Pack: pytest
================================================================ test session starts =================================================================
platform linux -- Python 3.5.2, pytest-3.3.0, py-1.5.2, pluggy-0.6.0
rootdir: /home/vince/Desktop/Pack, inifile:
plugins: hypothesis-3.2.0, nbval-0.7
collected 2 items

tests/test_pack.py ..                                                                                                                          [100%]

============================================================== 2 passed in 0.02 seconds ==============================================================
```

Note that this is a very minimalistic `setup.py` and there are various other
options that can be include.

More information on setup.py files is available:

- [https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html](https://vknight.org/rsd/extras/markdown/)
- [https://github.com/kennethreitz/setup.py](https://github.com/kennethreitz/setup.py)

## Other important files to consider

There are a number of other files that are useful to have in `Pack`.

- `README.md`: a file describing the package.
- `LICENSE.md`: a file saying that people are allowed to use the software (if
  that's the case of course).

These files are generally written in a language called `markdown` which is a
simple set of conventions for things like bullet point lists, section headers
etc...

Here is some information on
`markdown`: [https://vknight.org/rsd/extras/markdown/](https://vknight.org/rsd/extras/markdown/).

You can use markdown to write your `README.md` file. For example:

```markdown
# Pack

This is a python package to obtain a pack of cards.

## Usage

To install:

    $ python setup.py install

To install a version that changes when changes are made to the source files.

    $ python setup.py develop

Here is a simple way to obtain a pack and deal a hand of 2 cards

    >>> import pack
    >>> deck = pack.get_deck()
    >>> hand = pack.deal(deck, 2)
    >>> len(hand)
    2

## Development

To run the tests:

    $ pytest

```

Things to include in your `README.md` file:

- Basic description of the project
- Basic usage example

For more information about the `LICENSE.md` file see
[https://vknight.org/rsd/extras/licences/](https://vknight.org/rsd/extras/licences/)
