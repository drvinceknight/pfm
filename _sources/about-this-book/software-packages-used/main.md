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

# List of software packages used

The following Python libraries and the specific versions are used in this book:

```{code-cell} ipython3
:tags: ["remove-input", "style-check-ignore", "nbval-ignore-output"]

import pathlib
from importlib.metadata import version, PackageNotFoundError

requirements_path = pathlib.Path("../../../requirements.txt")
libraries = requirements_path.read_text().split("\n")

for library in filter(lambda line: "#" not in line, libraries):
    try:
        print(f"{library} version: {version(library)}")
    except PackageNotFoundError:
        pass
```
