import numpy as np


def get_long_run_state(pi, k, P):
    """
    For a Markov chain with transition matrix P and starting state vector pi,
    obtain the state distribution after k steps.
    """
    return pi @ np.linalg.matrix_power(P, k)


def extract_Q(P):
    """
    For an absorbing Markov chain with transition rate matrix P this computes the
    matrix Q.

    Note that this does not assume that P is in the required format. It
    identifies the rows and columns that have a 1 in the diagonal and removes
    them.
    """
    indices_with_1_in_diagonal = np.where(P.diagonal() != 1)[0]
    Q = P[indices_with_1_in_diagonal.reshape(-1, 1), indices_with_1_in_diagonal]
    return Q


def compute_N(Q):
    """
    For an absorbing Markov chain with transition rate matrix P that gives
    matrix Q this computes the fundamental matrix N.
    """
    number_of_rows, _ = Q.shape
    N = np.linalg.inv(np.eye(number_of_rows) - Q)
    return N


def compute_t(P):
    """
    For an absorbing Markov chain with transition rate matrix this computes the
    vector t which gives the expected number of steps until absorption.

    Note that this does not assume P is in the required format.
    """
    Q = extract_Q(P)
    N = compute_N(Q)
    number_of_rows, _ = Q.shape
    return N @ np.ones(number_of_rows)
