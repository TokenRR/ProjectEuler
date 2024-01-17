import time
from decimal import Decimal, getcontext


def digital_sum(n: int) -> int:
    """
    Calculate the digital sum of the first 100 decimal digits of the square root of n.

    Args:
        n (int): The number to calculate the square root of.

    Returns:
        int: The digital sum of the first 100 decimal digits of the square root of n.
    """
    getcontext().prec = 102
    root = str(Decimal(n).sqrt()).replace('.', '')[:100]
    return sum(int(digit) for digit in root)


def total_digital_sum(limit: int) -> int:
    """
    Calculate the total of the digital sums of the first 100 decimal digits for all
    the irrational square roots of the first limit natural numbers.

    Args:
        limit (int): The upper bound for the natural numbers.

    Returns:
        int: The total of the digital sums.
    """
    return sum(digital_sum(n) for n in range(2, limit + 1) if int(n**0.5)**2 != n)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {total_digital_sum(100)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
