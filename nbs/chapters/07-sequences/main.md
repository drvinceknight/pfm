---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region -->
## Sequences

### Introduction

The formal definition of sequences is a collection of ordered objects with potential repetitions.

The study of these sequences leads to many interesting results. Here we will concentrate on using recursive definitions to generate the values in a sequence.

## Tutorial

We will solve the following problem using a computer to using a programming technique called **recursion**.

---

A sequence \\(a_1, a_2, a_3, …\\) is defined by:

\\[
    \left\{
    \begin{array}{l}
        a_1 = k,\\
        a_{n + 1} = 2a_n – 7, n \geq 1,
    \end{array}
    \right.
\\]

where \\(k\\) is a constant.


1. Write down an expression for \\(a_2\\) in terms of \\(k\\).
2. Show that \\(a_3 = 4k -21\\)
3. Given that \\(\sum_{r=1}^4 a_r = 43\\) find the value of \\(k\\).
---

We will use a Python to define a function that reproduces the mathematical definition of \\(a_k\\):
<!-- #endregion -->

```python
def generate_a(k_value, n):
    """
    Uses recursion to return a_n for a given value of k:

    a_1 = k
    a_n = 2a_n - 7
    """
    if n == 1:
        return k_value
    return 2 * generate_a(k_value, n - 1) - 7
```

**Note** that similarly to the mathematical definition the Python definition of the function refers to itself.


We can use this to compute \\(a_3\\) for \\(k=4\\):

```python
generate_a(k_value=4, n=3)
```

We can use this to compute \\(a_5\\) for \\(k=1\\):

```python
generate_a(k_value=1, n=5)
```

Finally it is also possible to pass a symbolic value to `k_value`. This allows us to answer the first question:

```python
import sympy as sym

k = sym.Symbol("k")
generate_a(k_value=k, n=2)
```

Likewise for \\(a_3\\):

```python
generate_a(k_value=k, n=3)
```

For the last question we start by computing the sum:

\\[
    \sum_{r=1}^4 a_r = 43
\\]

```python
sum_of_first_four_terms = sum(generate_a(k_value=k, n=r) for r in range(1, 5))
sum_of_first_four_terms
```

This allows us to create the given equation and solve it:

```python
equation = sym.Eq(sum_of_first_four_terms, 43)
sym.solveset(equation, k)
```

### How to

#### Define a function using recursion

It is possible to define a recursive expression using a recursive function in Python. This requires two things:

- A recursive rule: something that relates the current term to another one;
- A base case: a particular term that does not need the recursive rule to be calculated.

Consider the following mathematical expression:

\\[
    \left\{
    \begin{array}{l}
        a_1 = 1,\\
        a_n = 2a_{n - 1}, n > 1,
    \end{array}
    \right.
\\]

- The recursive rule is: \\(a_n = 2a_{n - 1}\\);
- The base case is: \\(a_1 = 1\\).

In Python this can be written as:

```python
def generate_sequence(n):
    """
    Generate the sequence defined by:

    a_1 = 1
    a_n = 2 a_{n - 1}

    This is done using recursion.
    """
    if n == 1:
        return 1
    return 2 * generate_sequence(n - 1)
```

Here we can get the first 7 terms:

```python
values_of_sequence = [generate_sequence(n) for n in range(1, 8)]
values_of_sequence
```

### Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. Using recursion, obtain the first 10 terms of the following sequences:
    1. \\(\left\{\begin{array}{l}a_1 = 1,\\a_n = 3a_{n - 1}, n > 1\end{array}\right.\\)
    2. \\(\left\{\begin{array}{l}a_1 = 3,\\a_n = 6a_{n - 1}, n > 1\end{array}\right.\\)
    3. \\(\left\{\begin{array}{l}a_1 = 3,\\a_n = 6a_{n - 1} + 3, n > 1\end{array}\right.\\)
    4. \\(\left\{\begin{array}{l}a_0 = 3,\\a_n = \sqrt{a_{n - 1}} + 3, n > 0\end{array}\right.\\)
2. Using recursion, obtain the first 5 terms of the Fibonacci sequence:
    \\[\left\{\begin{array}{l}
        a_0 = 0,\\
        a_1 = 1,\\ 
        a_n = a_{n - 1} + a_{n - 2}, n \geq 2\end{array}\right.
    \\]
3. A 40 year building programme for new houses began in Oldtown in the year 1951 (Year 1) and finished in 1990 (Year 40).

    The number of houses built each year form an arithmetic sequence with first term \\(a\\) and common difference \\(d\\).

    Given that 2400 new houses were built in 1960 and 600 new houses were built in 1990, find:

    1. The value of \\(d\\).
    2. The value of \\(a\\).
    3. The total number of houses built in Oldtown over 40 years.
    4. On a randomly chose day, the probability of an individual travelling to school by car, bicycle or on foot is \\(1/2\\), \\(1/6\\) and \\(1/3\\) respectively. The probability of being late when using these methods of travel is \\(1/5\\), \\(2/5\\) and \\(1/10\\) respectively.
4. A sequence is given by:

    \\[
        \left\{\begin{array}{l}
        x_1 = 1\\
        x_{n + 1}= x_n(p + x_n), n > 1
        \end{array}\right.
    \\]

    for \\(p\ne0\\).

    1. Find \\(x_2\\) in terms of \\(p\\).
    2. Show that \\(x_3=1+3p+2p^2\\).
    3. Given that \\(x_3=1\\), find the value of \\(p\\)

### References

#### What are the differences between recursion and iteration?

When giving instructions to a computer it is possible to use recursion to directly implement a common mathematical definition. For example consider the following sequence:

\\[
    \left\{\begin{array}{l}
    a_1 = 1\\
    a_{n + 1}= 3a_n, n > 1
    \end{array}\right.
\\]

We can define this in Python as follows:

```python
def generate_sequence(n):
    """
    Generate the sequence defined by:

    a_1 = 1
    a_n = 3 a_{n - 1}

    This is done using recursion.
    """
    if n == 1:
        return 1
    return 3 * generate_sequence(n - 1)
```

The first 6 terms:

```python
[generate_sequence(n) for n in range(1, 7)]
```

We note that in this case this corresponds to powers of \\(3\\), and indeed we can prove that: \\(a_n = 3 ^ {n - 1}\\). We will not carry out the proof here but one approach to doing it would be to use proof by induction which is closely related to recursive functions.

We can write a different python function that uses this formulae. This is called **iteration**:

```python
def calculate_sequence(n):
    """
    Calculate the nth term of the sequence defined by:

    a_1 = 1
    a_n = 3 a_{n - 1}

    This is done using iteration using the direct formula:

    a_n = 3 ^ n
    """
    return 3 ** (n - 1)
```

```python
[calculate_sequence(n) for n in range(1, 7)]
```

We can in fact use a Jupyter [magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html) to time the run of a command. It is clear that recursion is slower.

```python tags=["nbval-ignore-output"]
%timeit [generate_sequence(n) for n in range(1, 25)]
```

```python tags=["naval-ignore-output"]
%timeit [calculate_sequence(n) for n in range(1, 25)]
```

In practice:

- Using recursion is powerful as it can be used to directly implement recursive definitions.
- Using iteration is more computationally efficient but it is not always straightforward to obtain an iterative formula.

<!-- #region -->
#### What is caching

One of the reasons that recursion is computationally inefficient is that it always has to recalculate previously calculated values.

For example:


\\[
    \left\{\begin{array}{l}
    a_1 = 1\\
    a_{n + 1}= 3a_n, n > 1
    \end{array}\right.
\\]

One way to overcome this is to use caching which means that when a function is called for a value it has already computed it remembers the value.

Python has a caching tool available in the functools library:
<!-- #endregion -->

```python
import functools


def generate_sequence(n):
    """
    Generate the sequence defined by:

    a_1 = 1
    a_n = 3 a_{n - 1}

    This is done using recursion.
    """
    if n == 1:
        return 1
    return 3 * generate_sequence(n - 1)


@functools.lru_cache()
def cached_generate_sequence(n):
    """
    Generate the sequence defined by:

    a_1 = 1
    a_n = 3 a_{n - 1}

    This is done using recursion but also includes a cache.
    """
    if n == 1:
        return 1
    return 3 * cached_generate_sequence(n - 1)
```

Timing both these approaches confirms a substantial increase in time for the cached version.

```python tags=["nbval-ignore-output"]
%timeit [generate_sequence(n) for n in range(1, 25)]
```

```python tags=["nbval-ignore-output"]
%timeit [cached_generate_sequence(n) for n in range(1, 25)]
```
