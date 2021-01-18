import stats


def test_get_mean():
    """
    This tests the `get_mean` function for a small iterable
    """
    iterable = (1, 2, 3)
    assert stats.get_mean(iterable) == 2


def test_get_population_variance():
    """
    This tests the `get_population_variance` function for a small iterable
    """
    iterable = (1, 2, 3)
    assert round(stats.get_population_variance(iterable), 3) == 0.667


test_get_mean()
test_get_population_variance()
