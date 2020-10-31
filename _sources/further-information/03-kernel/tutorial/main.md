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

# Tutorial

We are going to illustrate what a kernel does by letting python solve the
following problem:

## Solving the problem

````{admonition} Problem
What is the maximum of $e^{\pi}$ or $\pi ^ e$?
````

We start by creating variables and assigning them to have the value of the two
numbers we want to compare:

```{code-cell} ipython3
import sympy as sym

e_to_the_pi = sym.exp(sym.pi)
pi_to_the_e = sym.pi ** sym.exp(1)
```

We now compute the maximum using Python's `max` tool:

```{code-cell} ipython3
max(e_to_the_pi, pi_to_the_e)
```

## Making mistakes

For the rest of this tutorial we will make common mistakes when interactively
running code and show how to fix them.

### Undefined variables

Consider the common mistake of not running the first cell:

```python
import sympy as sym

e_to_the_pi = sym.exp(sym.pi)
pi_to_the_e = sym.pi ** sym.exp(1)
```

Running the second cell:

```python
max(e_to_the_pi, pi_to_the_e)
```

Figure {ref}`fig:name_error_because_of_not_running_a_cell` shows the error that
would occur:

```{figure} ./img/name_error_because_of_not_running_a_cell/main.png
---
width: 75%
name: fig:name_error_because_of_not_running_a_cell
---
Getting a name error when not running a cell
```

The error message is specifically telling us that the command `max(e_to_the_pi,
pi_to_the_e)` cannot be run because `e_to_the_pi` is not known.

To fix this we return the first cell and run it before running the second cell
again. This is shown in Figure {ref}`fig:rerunning_the_name_error`.

```{figure} ./img/rerunning_the_name_error/main.gif
---
width: 75%
name: fig:rerunning_the_name_error
---
Rerunning the first cell to properly define all needed variables
```

```{attention}
This approach is sometimes going to be necessary even if we run the first cell
but perhaps we had an error (a typo for example) in it at the time. In which
case, we fix the typo and run it again before running the second cell.
```

### Overwriting a tool

Another common mistake is to run some code that might not be the code that
was required.
At times this can be overcome by correcting the mistake but on other occasions
the code that was run might override and essentially delete something necessary.

As an example consider if the first cell was run correctly:

```python
import sympy as sym

e_to_the_pi = sym.exp(sym.pi)
pi_to_the_e = sym.pi ** sym.exp(1)
```

**However** the second cell was run with an error (not `max = (…)` as opposed
to `max(…)`):

```python
max = (e_to_the_pi, pi_to_the_e)
```

Figure {ref}`fig:type_error_because_of_overwriting_max` shows the error that
would occur after running the correct code:

```{figure} ./img/type_error_because_of_overwriting_max/main.png
---
width: 75%
name: fig:type_error_because_of_overwriting_max
---
Getting a type error when the `max` function has been overwritten
```

As Figure {ref}`fig:type_error_because_of_overwriting_max` shows the error is
due to the fact that the `max` tool has been overwritten to be a tuple
containing the two variables.

To fix this we need to _Restart the Kernel_ which allows us to forget the
outcome of all code that has been run and start from again. To restart the
kernel: click on `Kernel` and then `Restart`.

After doing this we can run the correct code as shown in Figure
{ref}`fig:restarting_the_kernel`.

```{figure} ./img/restarting_the_kernel/main.gif
---
width: 75%
name: fig:restarting_the_kernel
---
Restarting the kernel and running the code again.
```

```{important}
In this tutorial we have

- Seen how to rerun a cell if it is needed.
- Seen how to restart a kernel if it is needed.
```
