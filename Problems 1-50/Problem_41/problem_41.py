import time
from itertools import permutations

from sympy import isprime


def largest_pandigital_prime():
    """
    Find the largest n-digit pandigital prime number.

    A pandigital number is an integer that in a given base has among its significant
    digits each digit used in the base at least once.

    Returns:
        int: The largest pandigital prime number, or None if no such number exists.
    """
    return next((int(''.join(p)) for p in permutations('7654321') if isprime(int(''.join(p)))), None)


if __name__ == "__main__":
    start_time = time.time()
    largest_prime = largest_pandigital_prime()
    print(f'Answer = {largest_prime}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
