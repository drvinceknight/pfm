import numpy as np

import absorption

def test_long_run_state_for_known_number_of_states():
    """
    This tests the `long_run_state` for a small example matrix
    """
    pi = np.array([1, 0, 0])
    P = np.array([[1 / 2, 1 / 4, 1 / 4], [1 / 3, 1 / 3, 1 / 3], [0, 0, 1]])
    pi_after_5_steps = absorption.get_long_run_state(pi=pi, k=5, P=P)
    assert np.array_equal(pi_after_5_steps, pi @ np.linalg.matrix_power(P, 5)), "Did not get expected result for pi after 5 steps"

def test_long_run_state_when_starting_in_absorbing_state():
    """
    This tests the `long_run_state` for a small example matrix.

    In this test we start in the absorbing state, the state vector should not
    change.
    """
    pi = np.array([0, 0, 1])
    P = np.array([[1 / 2, 1 / 4, 1 / 4], [1 / 3, 1 / 3, 1 / 3], [0, 0, 1]])
    pi_after_5_steps = absorption.get_long_run_state(pi=pi, k=5, P=P)
    assert np.array_equal(pi_after_5_steps, pi)

def test_extract_Q():
    """
    This tests that the submatrix Q can be extracted from a given matrix P.
    """
    P = np.array([[1 / 2, 1 / 4, 1 / 4], [1 / 3, 1 / 3, 1 / 3], [0, 0, 1]])
    Q = absorption.extract_Q(P)
    expected_Q = np.array([[1 / 2, 1 / 4], [1 / 3, 1 / 3]])
    assert np.array_equal(Q, expected_Q), f"The expected Q did not match, the code obtained {Q}"

def test_compute_N():
    """
    This tests the computation of the fundmantal matrix N
    """
    P = np.array([[1 / 2, 1 / 4, 1 / 4], [1 / 3, 1 / 3, 1 / 3], [0, 0, 1]])
    Q = absorption.extract_Q(P)
    N = absorption.compute_N(Q)
    expected_N = np.array([[8 / 3, 1], [4 / 3, 2]])
    assert np.allclose(N, expected_N), f"The expected N did not match, the code obtained {N}, the expected value was {expected_N}"

def test_compute_t():
    """
    This tests the computation of the number of steps until absorption t.
    """
    P = np.array([[1 / 2, 1 / 4, 1 / 4], [1 / 3, 1 / 3, 1 / 3], [0, 0, 1]])
    t = absorption.compute_t(P)
    expected_t = np.array([11 / 3, 10 / 3])
    assert np.allclose(t, expected_t), f"The expected t did not match, the code obtained {t}"


test_long_run_state_for_known_number_of_states()
test_long_run_state_when_starting_in_absorbing_state()
test_extract_Q()
test_compute_N()
test_compute_t()
