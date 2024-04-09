import time
from typing import Set

from sympy import isprime


def concatenate_and_check(primes: Set[int],
                          n: int) -> bool:
    """
    Check if all concatenations of the primes with n result in a prime number.

    Args:
        primes (Set[int]): A set of prime numbers.
        n (int): A number to concatenate with each element of primes.

    Returns:
        bool: True if all concatenated numbers are prime, False otherwise.
    """
    return all(isprime(int(f"{p}{n}")) and isprime(int(f"{n}{p}")) for p in primes)


def find_prime_set(max_num: int = 10_000,
                   set_size: int = 5) -> Set[int]:
    """
    Find the set of primes for which any two primes concatenate to produce another prime.

    Args:
        max_num (int): The upper limit for the range of prime numbers.
        set_size (int): The desired size of the prime set.

    Returns:
        Set[int]: A set of prime numbers that fulfill the condition.
    """
    primes = {i for i in range(3, max_num) if isprime(i)}
    for p1 in primes:
        subset = {p for p in primes if p > p1 and concatenate_and_check({p1}, p)}
        if len(subset) >= set_size - 1:
            for p2 in subset:
                subset2 = {p for p in subset if p > p2 and concatenate_and_check({p1, p2}, p)}
                if len(subset2) >= set_size - 2:
                    for p3 in subset2:
                        subset3 = {p for p in subset2 if p > p3 and concatenate_and_check({p1, p2, p3}, p)}
                        if len(subset3) >= set_size - 3:
                            for p4 in subset3:
                                subset4 = {p for p in subset3 if p > p4 and concatenate_and_check({p1, p2, p3, p4}, p)}
                                if len(subset4) >= set_size - 4:
                                    return {p1, p2, p3, p4, next(iter(subset4))}
    return set()


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {sum(find_prime_set())}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
