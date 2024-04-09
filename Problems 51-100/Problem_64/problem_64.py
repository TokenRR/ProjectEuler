import time
from math import sqrt


def continued_fraction_period(n):
    """
    Calculate the period of the continued fraction representation of the square root of n.

    Args:
        n (int): The number to calculate the continued fraction for.

    Returns:
        int: The period of the continued fraction.
    """
    m, d, a0 = 0, 1, int(sqrt(n))
    a = a0
    period = 0

    if a0 != sqrt(n):
        while a != 2 * a0:
            m = d * a - m
            d = (n - m * m) // d
            a = (a0 + m) // d
            period += 1

    return period


def count_odd_periods(limit):
    """
    Count how many continued fractions for N ≤ limit have an odd period.

    Args:
        limit (int): The upper limit for N.

    Returns:
        int: The count of numbers with an odd period.
    """
    count = 0
    for n in range(2, limit + 1):
        if continued_fraction_period(n) % 2 == 1:
            count += 1
    return count


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {count_odd_periods(10000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
