import time
from sympy import primerange


def find_longest_prime_sum(limit):
    """
    Find the prime below the limit that can be written as the sum of the most consecutive primes.
    
    Parameters:
    limit (int): The upper limit for the prime number search.
    
    Returns:
    tuple: The prime number and the length of the consecutive prime sum.
    """
    primes = list(primerange(2, limit))
    length_of_longest_sum = 0
    longest_prime_sum = 0
    
    for i in range(len(primes)):
        for j in range(i+length_of_longest_sum, len(primes)):
            prime_sum = sum(primes[i:j])
            if prime_sum < limit:
                if prime_sum in primes and (j-i) > length_of_longest_sum:
                    length_of_longest_sum = j-i
                    longest_prime_sum = prime_sum
            else:
                break
    return longest_prime_sum, length_of_longest_sum


if __name__ == "__main__":
    start_time = time.time()
    result, length = find_longest_prime_sum(1000000)
    print(f'Answer = {result}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
