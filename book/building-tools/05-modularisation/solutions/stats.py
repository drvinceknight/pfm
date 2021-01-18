def get_mean(iterable):
    """
    Returns the mean of a given iterable which is defined as the sum divided by
    the number of items.
    """
    return sum(iterable) / len(iterable)

def get_population_variance(iterable):
    """
    Returns the population variance of a given iterable which is defined as the
    mean square of the differences from the mean.
    """
    mean = get_mean(iterable)
    squares_of_differences = [(value - mean) ** 2 for value in iterable]
    return get_mean(squares_of_differences)
