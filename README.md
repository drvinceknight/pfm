# Python for mathematics

## Development

The book is written in files found in `nbs/book` in the [MySt markdown
format](https://myst-nb.readthedocs.io/en/latest/).

To install development dependencies:

    pip install -r requirements-dev.txt

To check the format of the python code in the markdown files:

    inv stylecheck

To check the spelling:

    inv spellcheck

To check the prose:

    inv prosecheck

To generate back up `ipynb` versions of the notebooks:

    inv backupbook

To test the notebooks:

    inv testnbs

The main purpose of backing up to `ipynb` and then testing is so that the CI can
confirm the results written in the book are what would be obtained when using
updated libraries.

To generate the book to the `book` directory:

    inv build
