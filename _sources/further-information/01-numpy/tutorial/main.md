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

To demonstrate the use case of Numpy we will use it to explore the mathematics
of a [Galton Board](https://en.wikipedia.org/wiki/Bean_machine).

````{admonition} Problem

A Galton Board can be represented using a [Markov
Chain](https://en.wikipedia.org/wiki/Markov_chain) as shown in this diagram:

```{figure} ./img/galton_board/main.png
---
width: 75%
name: fig:galton_board
---
The state space for a Galton board
```

1. Write a function to generate all states of the Markov chain with $N$ rows:

   $$\{(i, j) \in \mathbb{Z} ^ 2 |\;0\leq i \leq N, 0<\leq j \leq i\}$$

2. For a given value of $p$ which corresponds to the probability of falling
   left, write a function to generate the transition rate matrix:

   $$
        P_{s^{(1)}, s^{(2)}} =
            \begin{cases}
                p &; \text{ if }s^{(2)} - s^{(1)} = (1, 0)\text{ and }{s_1^{(2)}} < N \\
            1 - p &; \text{ if }s^{(2)} - s^{(1)} = (1, 1)\text{ and }{s_1^{(2)}} < N \\
                1 &; \text{ if }s^{(2)} = N\\
                0 &; \text{otherwise} \\
            \end{cases}
   $$
3. Find the expected distribution of beans falling through the Galton board
   given by $\pi P ^N$ where $\pi = (1, 0, \dots 0)$ for $N=3$ and for $p$
   varying between 0 and 1.
4. Experiment with high values of $N$ to see how numpy performs on large
   matrices..
````

The first function is obtained using similar tools to the chapter on
combinatorics. Note however that we will be using `numpy` arrays instead of
tuples to represent the state space.

```{code-cell} ipython3
import numpy as np


def get_all_states(N):
    """
    Obtain all states for a Galton board with N rows.
    """
    return [np.array((i, j)) for i in range(N + 1) for j in range(i + 1)]


get_all_states(N=3)
```

Now we will implement a second function that takes two states and the parameters
of the problem to find the transition between two states:

```{code-cell} ipython3
def get_transition_probability(in_state, out_state, N, p):
    """
    Given two states, an in_state and an out_state this returns the probability
    of going from the in_state to the out_state.
    """
    if in_state[0] == N and np.array_equal(in_state, out_state):
        return 1

    if np.array_equal(out_state - in_state, np.array((1, 0))):
        return p

    if np.array_equal(out_state - in_state, np.array((1, 1))):
        return 1 - p

    return 0


in_state = np.array((2, 1))
out_state = np.array((3, 2))

get_transition_probability(in_state=in_state, out_state=out_state, N=5, p=0.3)
```

```{attention}
We compare numpy arrays using `numpy.array_equal`.
```

We can then create the matrix $P$ by iterating over the state space and finding
the probability of transition:

```{code-cell} ipython3
def get_transition_matrix(N, p):
    """
    Create the transition matrix for a Galton board with N rows and probability
    of falling to the left of p.

    This is done by creating an empty matrix of the required size and modifying
    the values in place.
    """
    states = get_all_states(N)
    number_of_states = len(states)
    P = np.zeros((number_of_states, number_of_states))

    for row, in_state in enumerate(states):
        for col, out_state in enumerate(states):
            P[row, col] = get_transition_probability(in_state, out_state, N, p)

    return P


get_transition_matrix(N=3, p=0.3)
```

```{attention}
In the above function we are using the base tool `enumerate` which is a powerful
Python tool that will iterate over elements in an iterable as well as return the
index of the items.
```

Now to find the expected distribution.

```{code-cell} ipython3
def get_distribution(N, p):
    """
    This returns the distribution of beans over the entire state space after the
    all fall.

    This is done by computing (pi P ^ N) where pi = (1, 0, \dots 0).
    """
    P = get_transition_matrix(N=N, p=p)
    number_of_rows = len(P)
    pi = np.zeros(number_of_rows)
    pi[0] = 1
    return pi @ (np.linalg.matrix_power(P, N))


get_distribution(N=3, p=0.5)
```

```{attention}
We calculate the matrix exponentiation using
`np.linalg.matrix_power`.
```

We can finally see how this distribution changes for different values of $p$:

```{code-cell} ipython3
for p in np.linspace(0, 1, 11):
    print(p, get_distribution(N=3, p=p)[-4:])
```

We see that as $p$ increases the beans end up more to the left.

We can see that the function runs in a reasonable time for $N=20$ which
corresponds to a matrix of size $\frac{(N+1)(N+2)}{2}=231$.

```{code-cell} ipython3
:tags: [nbval-ignore-output, style-check-ignore]

%timeit get_distribution(N=20, p=0.5)
```

```{important}
In this chapter we have:

- Written a function to create a `numpy` array.
- Used `numpy` to efficiently carry out matrix multiplication.
```
