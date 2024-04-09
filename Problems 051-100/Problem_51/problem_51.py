import time
from sympy import isprime, primerange


def find_smallest_prime_family(family_size):
    """
    Find the smallest prime which, by replacing part of the number with the same digit,
    is part of a prime value family of the given size.
    
    Parameters:
    family_size (int): The size of the prime value family to find.
    
    Returns:
    int: The smallest prime in the family.
    """
    primes = list(primerange(2, 1000000))
    for prime in primes:
        prime_str = str(prime)
        for digit in '012':
            if prime_str.count(digit) > 1:
                pattern = prime_str.replace(digit, '.')
                family = [int(pattern.replace('.', str(d))) for d in range(10) if pattern[0] != '0']
                prime_family = [p for p in family if isprime(p) and len(str(p)) == len(prime_str)]
                if len(prime_family) == family_size:
                    return min(prime_family)
    return None


if __name__ == '__main__':
    start_time = time.time()
    print(f'Answer = {find_smallest_prime_family(8)}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')