import time
from typing import List


def prime_sieve(n: int) -> List[int]:
    """
    Generate all primes less than n.

    Args:
    n (int): The upper limit for generating primes.

    Returns:
    List[int]: A list of all primes less than n.
    """
    sieve = [True] * n
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]:
            for i in range(x*2, n, x):
                sieve[i] = False
    return [i for i in range(2, n) if sieve[i]]


def count_ways(n: int, primes: List[int]) -> int:
    """
    Count the number of ways n can be written as a sum of primes.

    Args:
    n (int): The number to be written as a sum of primes.
    primes (List[int]): The list of primes less than n.

    Returns:
    int: The number of ways n can be written as a sum of primes.
    """
    ways = [1] + [0] * n
    for p in primes:
        for i in range(p, n + 1):
            ways[i] += ways[i - p]

    return ways[n]


if __name__ == "__main__":
    start_time = time.time()
    TARGET_WAYS = 5000
    n = 10  # Початкове значення
    while count_ways(n, prime_sieve(n)) <= TARGET_WAYS:
        n += 1

    print(f"Answer = {n}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
