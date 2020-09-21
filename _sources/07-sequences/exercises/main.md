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

# Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. Using recursion, obtain the first 10 terms of the following sequences:
    1. $\left\{\begin{array}{l}a_1 = 1,\\a_n = 3a_{n - 1}, n > 1\end{array}\right.$
    2. $\left\{\begin{array}{l}a_1 = 3,\\a_n = 6a_{n - 1}, n > 1\end{array}\right.$
    3. $\left\{\begin{array}{l}a_1 = 3,\\a_n = 6a_{n - 1} + 3, n > 1\end{array}\right.$
    4. $\left\{\begin{array}{l}a_0 = 3,\\a_n = \sqrt{a_{n - 1}} + 3, n > 0\end{array}\right.$
2. Using recursion, obtain the first 5 terms of the Fibonacci sequence:
    $$\left\{\begin{array}{l}
        a_0 = 0,\\
        a_1 = 1,\\ 
        a_n = a_{n - 1} + a_{n - 2}, n \geq 2\end{array}\right.
    $$
3. A 40 year building programme for new houses began in Oldtown in the year 1951 (Year 1) and finished in 1990 (Year 40).

    The number of houses built each year form an arithmetic sequence with first term $a$ and common difference $d$.

    Given that 2400 new houses were built in 1960 and 600 new houses were built in 1990, find:

    1. The value of $d$.
    2. The value of $a$.
    3. The total number of houses built in Oldtown over 40 years.
    4. On a randomly chose day, the probability of an individual travelling to school by car, bicycle or on foot is $1/2$, $1/6$ and $1/3$ respectively. The probability of being late when using these methods of travel is $1/5$, $2/5$ and $1/10$ respectively.
4. A sequence is given by:

    $$
        \left\{\begin{array}{l}
        x_1 = 1\\
        x_{n + 1}= x_n(p + x_n), n > 1
        \end{array}\right.
    $$

    for $p\ne0$.

    1. Find $x_2$ in terms of $p$.
    2. Show that $x_3=1+3p+2p^2$.
    3. Given that $x_3=1$, find the value of $p$
