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

(chp:combinatorics)=

# Combinatorics

Combinatorics is the mathematical area interested in specific finite
sets. In a lot of instances this comes down to counting things and is
often first encountered by mathematicians through combinations and
permutations. Computers are useful when doing this as they can be used
to generate the finite sets considered. You can essentially count things
"by hand"' (using a computer) to confirm theoretic results.

```{important}
In this chapter you will cover:

-   Generating configurations of elements that correspond to
    permutations and/or combinations.
-   Counting these configurations.
-   Directly computing $^n C_i={n \choose i}$.
-   Directly computing $^n P_i$.
```
