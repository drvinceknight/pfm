# Snakes and ladders

This directory contains a script to generate `main.csv` which contains a numpy
array for Snakes and ladders.

## Assumptions

The snakes and ladders are as described in the "Building Tools - Modularisation"
chapter tutorial.

Furthermore the official rules are used: a player must land exactly on 100, if
they do not they stay where they are. This is reflected in the final rows of the
matrix.

## Usage

To load the numpy array:

    >>> import numpy as np
    >>> P = np.loadtxt(fname="main.csv", delimiter=",")
