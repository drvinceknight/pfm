![deploy-book](https://github.com/drvinceknight/pfm/workflows/deploy-book/badge.svg)

# Python for mathematics

## Development

The book is written in files found in `book/` in the [MyST markdown
format](https://myst-nb.readthedocs.io/en/latest/).

### Setup

Install [uv](https://docs.astral.sh/uv/) then run:

    uv sync --group dev

### Build the book

    uv run jb build book --path-output .

### Test the notebooks

    uv run pytest -vv --nbval --ignore=_build/ --current-env

### Test the testing chapter

    uv run pytest book/building-tools/07-testing/

### Check code style

    uv run stylecheck

### Check spelling

    uv run spellcheck

### Check prose

    uv run prosecheck
