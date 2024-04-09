import time
from math import factorial
from typing import Dict


# Кешування факторіалів цифр для оптимізації
factorial_cache: Dict[int, int] = {i: factorial(i) for i in range(10)}


def sum_factorial_digits(n: int) -> int:
    """
    Return the sum of the factorial of each digit of n
    """
    return sum(factorial_cache[int(digit)] for digit in str(n))


def count_chains_with_sixty_terms(limit: int) -> int:
    """
    Count the number of chains with exactly sixty non-repeating terms
    """
    count = 0
    chain_cache: Dict[int, int] = {}
    for i in range(1, limit):
        chain = []
        while i not in chain and i not in chain_cache:
            chain.append(i)
            i = sum_factorial_digits(i)
        # Використання кешу для скорочення обчислень
        chain_length = len(chain) + chain_cache.get(i, 0)
        if chain_length == 60:
            count += 1
        # Збереження довжини ланцюга в кеш
        for j in chain:
            chain_cache[j] = chain_length - chain.index(j)
    return count


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {count_chains_with_sixty_terms(1_000_000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
