### New materials for the course

This directory contains the notebooks for the new content.

See https://github.com/drvinceknight/cfm/issues/145

The notebooks are written both in `ipynb` format and `md` format. The `jupytext`
tool is used to go between them.

To create a paired `md` for a given `main.ipynb`:

```bash
jupytext --set-formats ipynb,md main.ipynb
```

To sync (using the `black` auto formatting tool):

```bash
jupytext --sync --pipe black main.ipynb
```
