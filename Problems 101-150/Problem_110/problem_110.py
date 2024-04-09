import time
from typing import List, Tuple


def return_factors(factors_of_input_val: List[Tuple[int, int]]) -> float:
    """
    Calculate the number of factors for a given list of prime factors.

    Args:
        factors_of_input_val (List[Tuple[int, int]]): List of tuples representing prime factors.

    Returns:
        float: The number of factors.
    """
    num_factors = 1
    for factor, exponent in factors_of_input_val:
        num_factors *= (2 * exponent + 1)
    return num_factors / 2 - 1


def prime_product(factors_of_input_val: List[Tuple[int, int]]) -> int:
    """
    Calculate the product of prime factors.

    Args:
        factors_of_input_val (List[Tuple[int, int]]): List of tuples representing prime factors.

    Returns:
        int: The product of prime factors.
    """
    prime_product = 1
    for factor, exponent in factors_of_input_val:
        prime_product *= (factor ** exponent)
    return prime_product


if __name__ == "__main__":
    start_time = time.time()

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    exponents = [3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    prime_tuples = list(zip(primes, exponents))

    print(f"Answer = {prime_product(prime_tuples)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
    