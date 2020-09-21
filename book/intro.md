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

```{warning}
This book is a work in progress and should be considered currently to be in a
**pre** draft state. Work is actively taking place in preparation for October
2020.

If you happen to find this and notice any typos and/or have any suggestions
please open an issue on the github repo: <https://github.com/drvinceknight/pfm>
```

# Python for Mathematics

## Introduction

This book aims to introduce readers to programming for mathematics.

It is assumed that readers are used to solving high school mathematics problems
of the form:

---

```{admonition} Problem
Given the function $f:\mathbb{R}\to\mathbb{R}$ defined by
$f(x) = x ^ 2 - 3 x + 1$ obtain the global minima of the function.
```

```{admonition} Solution
:class: tip

To solve this we need to apply our **mathematical knowledge** which tells us to:

1. Differentiate $f(x)$ to get $\frac{df}{dx}$;
2. Equate $\frac{df}{dx}=0$;
3. Use the second derivative test on the solution to the previous equation.

For each of those 3 steps we will usually make use of our **mathematical
techniques**:

1. Differentiate $f(x)$:

   $$\frac{df}{dx} = 2 x - 3$$

2. Equate $\frac{df}{dx}=0$:

   $$2x-3 =0 \Rightarrow x = 3/2$$

3. Use the second derivative test on the solution:

   $$\frac{d^2f}{dx^2} = 2 > 0\text{ for all values of }x$$

   Thus $x=2/3$ is the global minima of the function.
```

```{attention}
As we progress as mathematicians **mathematical knowledge** is more prominent
than **mathematical technique**: often knowing what to do is the real problem as
opposed to having the technical ability to do it.
```

This is what this book will cover: **programming** allows us to instruct a
computer to carry out mathematical techniques.

We will for example learn how to solve the above problem by instructing a
computer which **mathematical technique** to carry out.

**This book will teach us how to give the correct instructions to a
computer.**

The following is an example, do not worry too much about the specific code used
for now:

1. Differentiate $f(x)$ to get $\frac{df}{dx}$;

```{code-cell} ipython3
import sympy as sym

x = sym.Symbol("x")
sym.diff(x ** 2 - 3 * x + 1, x)
```

2. Equate $\frac{df}{dx}=0$:

```{code-cell} ipython3
sym.solveset(2 * x - 3, x)
```

3. Use the second derivative test on the solution:

```{code-cell} ipython3
sym.diff(x ** 2 - 3 * x + 1, x, 2)
```

{ref}`Knowledge versus technique <fig:knowledge_vs_technique>` is a brief summary.

```{figure} ./img/knowledge_vs_technique/main.png
---
width: 50%
name: fig:knowledge_vs_technique
---
Knowledge versus technique in this book.
```

## How this book is structured

Most programming texts introduce readers to the building blocks of
programming and build up to using more sophisticated tools for a specific
purpose.

This is akin to teaching someone how to forge metal so as to make a nail and
then slowly work our way to using more sophisticated tools such as power tools
to build a house.

This book will do thing in a different way: we will start with using and
understanding tools that are helpful to mathematicians. In the later part of the
book we will cover the building blocks and you will be able to build your own
sophisticated tools.

The book is in two parts:

1. Tools for mathematics;
2. Building tools.

The first part of the book will not make use of any novel mathematics.
Instead we will consider a number of mathematics problem that are often covered
in secondary school.

- Algebraic manipulation
- Calculus (differentiation and integration)
- Permutations and combinations
- Probability
- Linear algebra

The questions we will tackle will be familiar in their presentation and
description. **What will be different** is that no **by hand** calculations will
be done. We will instead carry them all out using a programming language.

In the second part of the book you will be encouraged to build your own tools
to be able to tackle a problem type of your choice.

```{attention}
Every chapter will have 4 parts:

- A tutorial: you will be walked through solving a problem. You will be
  specifically told what to do and what to expect.
- A how to section: this will be a shorter more succinct section that will
  detail how to carry out specific things.
- A reference section: this will be a section with references to further
  resources as well as background information about specific things in the
  chapter.
- An exercise section: this will be a number of exercises that you can work on.
```
