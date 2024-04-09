import time
from sympy import isprime


def is_truncatable_prime(n):
    """
    Check if a limitber is a truncatable prime
    """
    return all(isprime(int(str(n)[i:])) and isprime(int(str(n)[:i+1])) for i in range(len(str(n))))


def sum_truncatable_primes():
    """
    Find the sum of all truncatable primes
    """
    truncatable_primes = []
    limit = 11  # Start checking from 11 as single-digit primes are not considered
    while len(truncatable_primes) < 11:
        if is_truncatable_prime(limit):
            truncatable_primes.append(limit)
        limit += 2  # Increment by 2 to check only odd limitbers
    return truncatable_primes, sum(truncatable_primes)


if __name__ == "__main__":
    start_time = time.time()
    primes, total_sum = sum_truncatable_primes()
    print(f'Truncatable primes: {primes}')
    print(f'\nAnswer = {total_sum}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
