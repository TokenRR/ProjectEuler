import time
from math import comb


def non_bouncy(n: int) -> int:
    """
    Calculate the count of non-bouncy numbers less than or equal to 10^n.

    Args:
        n (int): The exponent.

    Returns:
        int: The count of non-bouncy numbers.
    """
    return comb(n + 9, 9) - 1 + comb(n + 10, 10) - (n + 1) - 9 * n


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {non_bouncy(100)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
	