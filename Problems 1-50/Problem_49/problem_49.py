import time
from sympy import isprime, primerange
from itertools import permutations


def find_prime_permutations_sequence(diff, num_digits):
    """
    Find the arithmetic sequence of prime permutations.
    
    Parameters:
    diff (int): The common difference between consecutive terms.
    num_digits (int): The number of digits in each prime number.
    
    Returns:
    str: The concatenated sequence of the prime permutations.
    """
    primes = [p for p in primerange(10**(num_digits-1), 10**num_digits) if p > 1487]
    for p in primes:
        perms = set(int(''.join(x)) for x in permutations(str(p)))
        sequence = [p + i * diff for i in range(3) if p + i * diff in perms]
        if len(sequence) == 3 and all(isprime(x) for x in sequence):
            return ''.join(str(x) for x in sequence)
    return "No sequence found."


if __name__ == "__main__":
    start_time = time.time()
    result = find_prime_permutations_sequence(3330, 4)
    print(f'Answer = {result}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
