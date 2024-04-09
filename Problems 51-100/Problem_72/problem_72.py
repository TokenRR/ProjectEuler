import time


def sieve_phi(limit: int) -> list[int]:
    """
    Calculate the totient of each number up to the limit using the sieve of Eratosthenes.

    Args:
        limit (int): The upper bound for the calculation.

    Returns:
        list: A list of totients for each number up to the limit.
    """
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is a prime number
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
    return phi


def count_reduced_proper_fractions(limit: int) -> int:
    """
    Count the number of reduced proper fractions for d ≤ limit using the sieve of Eratosthenes.

    Args:
        limit (int): The upper bound for the denominator.

    Returns:
        int: The total number of reduced proper fractions.
    """
    phi = sieve_phi(limit)
    return sum(phi) - 1  # Subtract 1 to exclude phi(1)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {count_reduced_proper_fractions(1_000_000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
