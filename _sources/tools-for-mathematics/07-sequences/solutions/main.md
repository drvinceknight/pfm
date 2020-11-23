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

# Solutions

## Question 1

> `1`. Using recursion, obtain the first 10 terms of the following sequences:

> `1`. $\left\{\begin{array}{l}a_1 = 1,\\a_n = 3a_{n - 1}, n > 1\end{array}\right.$

```{code-cell} ipython3
def get_sequence_a(n):
    """
    Return the sequence a.
    """
    if n == 1:
        return 1
    return 3 * get_sequence_a(n - 1)


[get_sequence_a(n) for n in range(1, 11)]
```

> `2`. $\left\{\begin{array}{l}b_1 = 3,\\b_n = 6b_{n - 1}, n > 1\end{array}\right.$

```{code-cell} ipython3
def get_sequence_b(n):
    """
    Return the sequence b.
    """
    if n == 1:
        return 3
    return 6 * get_sequence_b(n - 1)


[get_sequence_b(n) for n in range(1, 11)]
```

> `3`. $\left\{\begin{array}{l}c_1 = 3,\\c_n = 6c_{n - 1} + 3, n > 1\end{array}\right.$

```{code-cell} ipython3
def get_sequence_c(n):
    """
    Return the sequence c.
    """
    if n == 1:
        return 3
    return 6 * get_sequence_c(n - 1) + 3


[get_sequence_c(n) for n in range(1, 11)]
```

> `4`. $\left\{\begin{array}{l}d_0 = 3,\\d_n = \sqrt{d_{n - 1}} + 3, n > 0\end{array}\right.$

```{code-cell} ipython3
import sympy as sym


def get_sequence_d(n):
    """
    Return the sequence c.
    """
    if n == 0:
        return 3
    return sym.sqrt(get_sequence_d(n - 1)) + 3


[get_sequence_d(n) for n in range(1, 11)]
```

We could use a `sqrt` from a different library. Choosing to use `sympy` as it
ensures the result is exact although not necessarily readable. Here is an
approximate approach:

```{code-cell} ipython3
import math


def get_sequence_d(n):
    """
    Return the sequence c.
    """
    if n == 0:
        return 3
    return math.sqrt(get_sequence_d(n - 1)) + 3


[get_sequence_d(n) for n in range(10)]
```

2. Using recursion, obtain the first 5 terms of the Fibonacci sequence:

   $$
       \left\{
       \begin{array}{l}
       a_0 = 0,\\
       a_1 = 1,\\
       a_n = a_{n - 1} + a_{n - 2}, n \geq 2\end{array}\right.
   $$

```{code-cell} ipython3
def get_fibonacci(n):
    """
    Return the nth term of the Fibonacci sequence
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return get_fibonacci(n - 1) + get_fibonacci(n - 2)


[get_fibonacci(n) for n in range(10)]
```

## Question 3

> `3`. A 40 year building programme for new houses began in Oldtown in the year
> 1951 (Year 1) and finished in 1990 (Year 40).

> The number of houses built each year form an arithmetic sequence with first
> term $a$ and common difference $d$.

> Given that 2400 new houses were built in 1960 and 600 new houses were built in
> 1990, find:

> `1`. The value of $d$.

An arithmetic sequence with first term $a$ and common difference $d$ is a
sequence of the form:

$$
  \left\{
    \begin{array}{l}
       a_1 = a,\\
       a_n = a_{n - 1} + d
    \end{array}
  \right.
$$

We will write a function to express this:

```{code-cell} ipython3
def get_arithmetic_sequence(n, first_term, common_difference):
    """
    Return the nth term of an arithmetic sequence with give first_term and
    common common_difference.
    """
    if n == 1:
        return first_term
    return (
        get_arithmetic_sequence(n - 1, first_term, common_difference)
        + common_difference
    )
```

We know that $a_{10}=2400$ and $a_{40}=600$ we can write down equations that
represent this:

```{code-cell} ipython3
a = sym.Symbol("a")
d = sym.Symbol("d")

a_10_equation = sym.Eq(
    get_arithmetic_sequence(n=10, first_term=a, common_difference=d), 2400
)
a_10_equation
```

```{code-cell} ipython3
a_40_equation = sym.Eq(
    get_arithmetic_sequence(n=40, first_term=a, common_difference=d), 600
)
a_40_equation
```

We will solve the first equation for $a$:

```{code-cell} ipython3
sym.solveset(a_10_equation, a)
```

We substitute this in to the other equation and solve it for $d$:

```{code-cell} ipython3
sym.solveset(a_40_equation.subs({a: 2400 - 9 * d}), d)
```

> `2`. The value of $a$.

We can substitute that value for $d$ back in to the expression for $a$:

```{code-cell} ipython3
(2400 - 9 * d).subs({d: -60})
```

> `3`. The total number of houses built in Oldtown over 40 years.

```{code-cell} ipython3
sum(
    get_arithmetic_sequence(n=n, first_term=2940, common_difference=-60)
    for n in range(1, 41)
)
```

## Question 4

> `4`. A sequence is given by:

> $$
> $$

        x_1 = 1\\
        x_{n + 1}= x_n(p + x_n), n > 1
        \end{array}\right.
    $$

> for $p\ne0$.

> `1`. Find $x_2$ in terms of $p$.

We start by defining a function:

```{code-cell} ipython3
def get_sequence(n, p):
    """
    Return the nth term of the sequence x_n for a given value of p
    """
    if n == 1:
        return 1
    return get_sequence(n - 1, p) * (p + get_sequence(n - 1, p))
```

Using this we can answer the question:

```{code-cell} ipython3
p = sym.Symbol("p")

x_2 = get_sequence(n=2, p=p)
x_2
```

> `2`. Show that $x_3=1+3p+2p^2$.

```{code-cell} ipython3
p = sym.Symbol("p")

x_3 = get_sequence(n=3, p=p)
sym.expand(x_3)
```

> `3`. Given that $x_3=1$, find the value of $p$

```{code-cell} ipython
equation = sym.Eq(x_3, 1)
sym.solveset(equation, p)
```

As $p\ne0$ this gives us that $p=-\frac{3}{2}$.
