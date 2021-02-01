[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4074114.svg)](https://doi.org/10.5281/zenodo.4074114)

![Validate notebooks on MacOS](https://github.com/drvinceknight/pfm/workflows/Validate%20notebooks%20on%20MacOS/badge.svg)

![Validate notebooks on ubuntu](https://github.com/drvinceknight/pfm/workflows/Validate%20notebooks%20on%20ubuntu/badge.svg)

![Validate notebooks on Windows](https://github.com/drvinceknight/pfm/workflows/Validate%20notebooks%20on%20Windows/badge.svg)

![Test prose and style](https://github.com/drvinceknight/pfm/workflows/Test%20prose%20and%20style/badge.svg)

![deploy-book](https://github.com/drvinceknight/pfm/workflows/deploy-book/badge.svg)

# Python for mathematics

## Development

The book is written in files found in `book/` in the [MySt markdown
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
