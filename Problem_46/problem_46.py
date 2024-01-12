import time
from sympy import isprime, primerange


def is_twice_square(number):
    """
    Check if a number is twice a square.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is twice a square, False otherwise.
    """
    root = (number / 2)**0.5
    return root.is_integer()


def find_smallest_goldbach_other_conjecture():
    """
    Find the smallest odd composite that cannot be written as the sum of a prime and twice a square.
    
    Returns:
    int: The smallest odd composite that cannot be written as the sum of a prime and twice a square.
    """
    n = 9
    primes = list(primerange(2, 10000))
    while True:
        if not isprime(n):
            if not any(is_twice_square(n - p) for p in primes if p < n):
                return n
        n += 2


if __name__ == "__main__":
    start_time = time.time()
    result = find_smallest_goldbach_other_conjecture()
    print(f'Answer = {result}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
