import time
from math import isqrt


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def find_numbers(limit: int) -> int:
    """
    Find the count of numbers below a given limit that can be expressed as the sum of a prime square,
    prime cube, and prime fourth power.

    Args:
        limit (int): The upper bound for the numbers.

    Returns:
        int: The count of numbers that meet the criteria.
    """
    primes = [i for i in range(2, isqrt(limit)) if is_prime(i)]
    results = set()
    for x in primes:
        for y in primes:
            if x**2 + y**3 >= limit:
                break
            for z in primes:
                number = x**2 + y**3 + z**4
                if number >= limit:
                    break
                results.add(number)
    return len(results)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer: {find_numbers(50_000_000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
