import time
from sympy import primerange
from itertools import combinations


def euler_totient(n: int, prime_factors: list) -> int:
    """
    Euler's totient function, computes the number of positive integers less than n
    that are relatively prime to n.

    Args:
        n (int): The input number.
        prime_factors (list): List of prime factors of n.

    Returns:
        int: The value of Euler's totient function for the given input.
    """
    result = n  # Initialize result as n

    # Adjust result by multiplying with (1 - 1/p) for each prime factor
    for p in prime_factors:
        result *= (1 - 1/p)

    return int(result)


def find_min_n_phi_permutation(limit: int) -> int:
    """
    Find the value of n < limit for which phi(n) is a permutation of n,
    and the ratio n/phi(n) produces a minimum.

    Args:
        limit (int): The upper bound for n.

    Returns:
        int: The value of n for which phi(n) is a permutation of n, and the ratio is minimized.
    """
    min_ratio = float('inf')
    result_n = 0
    primes = list(primerange(1000, 5000))  # Generate a list of primes within a suitable range

    for prime_pair in combinations(primes, 2):
        p1, p2 = prime_pair
        n = p1 * p2

        if n >= limit:
            continue

        phi_n = euler_totient(n, [p1, p2])

        if sorted(str(n)) == sorted(str(phi_n)):
            current_ratio = n / phi_n
            if current_ratio < min_ratio:
                min_ratio = current_ratio
                result_n = n
    return result_n


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_min_n_phi_permutation(10**7)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
