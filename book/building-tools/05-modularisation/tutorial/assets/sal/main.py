"""
Script to generate `main.csv` which contains the transition matrix for snakes
and ladders.
"""
import numpy as np

snakes_and_ladders = {
    3: 19,
    15: 37,
    22: 42,
    25: 64,
    41: 73,
    53: 74,
    63: 86,
    76: 91,
    84: 98,
    11: 7,
    18: 13,
    28: 12,
    36: 34,
    77: 16,
    47: 26,
    83: 39,
    92: 75,
    99: 70,
}


# Set up the transition matrix
P = np.zeros((101, 101))
for i in range(1, 101):
    P[i - 1, i : i + 6] = 1 / 6

P[100, 100] = 1

for i, row in enumerate(P):
    #  Apply snakes and ladders
    for square, target in snakes_and_ladders.items():
        if row[square] > 0:
            row[square], row[target] = 0, row[target] + row[square]
    # If you do not land on 100 you stay where you are
    if (row_sum := np.sum(row)) < 1:
        row[i] = 1 - row_sum

np.savetxt(fname="main.csv", X=P, delimiter=",", fmt="%f")
