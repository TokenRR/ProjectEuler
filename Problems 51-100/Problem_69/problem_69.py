import time
from sympy import primerange
from typing import List


def find_max_n_phi_ratio(limit: int) -> int:
    """
    Find the value of n <= limit for which n/phi(n) is a maximum.

    Args:
        limit (int): The upper bound for n.

    Returns:
        int: The value of n for which n/phi(n) is maximized.
    """
    n = 1
    for prime in primerange(1, limit):
        if n * prime > limit:
            break
        n *= prime
    return n


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_max_n_phi_ratio(1_000_000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
