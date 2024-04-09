import time
from sympy import isprime


def rotate_number(n):
    """
    Return all rotations of a number
    """
    rotations = []
    m = str(n)
    for i in range(len(m)):
        rotations.append(int(m[i:] + m[:i]))
    return rotations


def is_circular_prime(n):
    """
    Check if all rotations of a number are prime
    """
    return all(isprime(num) for num in rotate_number(n))


def count_circular_primes(limit):
    """Count all circular primes below a given limit
    """
    return sum(1 for i in range(2, limit) if is_circular_prime(i))


if __name__ == "__main__":
    start_time = time.time()
    limit = 1000000
    circular_primes_count = count_circular_primes(limit)
    print(f'Answer = {circular_primes_count}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
