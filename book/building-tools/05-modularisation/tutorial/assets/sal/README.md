# Snakes and ladders

This repository contains a script to generate [`main.csv`](./main.csv) which
contains the transition matrix for a Markov chain representation of the popular
board game Snakes and Ladders.

## Assumptions

The official rules are used: a player must land exactly on 100, if they do not
they stay where they are. This is reflected in the final rows of the matrix.

## Usage

To use generate the data:

    $ python main.py

To load the data as a numpy array:

    >>> import numpy as np
    >>> P = np.loadtxt(fname="main.csv", delimiter=",")

We can see we have a 101 by 101 array:

    >>> P.shape
    (101, 101)

The last row corresponds to the absorbing state of ending the game:

    >>> P[-1]
    array([0., 0., ... 0., 1.])

The penultimate row corresponding to the 99th square shows that 1/6 of the time
the game ends but 5/6th of the time the player stays where they are:

    >>> P[-2]
    array([0. ... 0.833333, 0.166667])

Similarly the row that corresponds to the 98th square captures that:

- 1/6 of the time they roll leads us to square 99 where there is a snake to square 70.
- 1/6 of the time the game ends
- 2/3 of the time the player stays where they are.

    >>> P[-3]
    array([0. ... 0.166667, ... 0.666667, 0.      , 0.166667])
    >>> P[-3, 70]
    0.166667

## To test that the results listed in this README are correct:

    $ python -m pytest --doctest-glob=README.md
