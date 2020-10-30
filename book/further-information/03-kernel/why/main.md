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

# Further information.

## What is a kernel

As described in the Jupyter notebook beginner guide
<https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html#kernel>:

> A notebook kernel is a "computational engine" that [runs] the code contained
> in a Notebook document. The ipython kernel, referenced in this guide, [runs]
> python code. Kernels for many other languages exist (official kernels).

As shown in Figure {ref}`fig:diagram_of_the_kernel_notebook_relationship` the
notebook is where the instructions are written but until they are sent to the
Kernel the instructions will not have any effect.

```{figure} ./img/diagram_of_the_kernel_notebook_relationship/main.png
---
width: 75%
name: fig:diagram_of_the_kernel_notebook_relationship
---
The relationship between the kernel and the notebook.
```

## What other kernels can be used

You can see a list of all the various programming languages for which a Jupyter
kernel exists here: <https://github.com/jupyter/jupyter/wiki/Jupyter-kernels>.
