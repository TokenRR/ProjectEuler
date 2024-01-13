import time
from sympy import isprime


def spiral_primes_ratio(side_length=1, prime_count=0, total_count=1):
    """
    Calculate the side length of the square spiral where the ratio of primes
    along both diagonals first falls below 10%.

    Parameters:
    side_length (int): The starting side length of the spiral.
    prime_count (int): The initial count of prime numbers on the diagonals.
    total_count (int): The initial total count of numbers on the diagonals.

    Returns:
    int: The side length of the square spiral.
    """
    number = 1  # Starting number in the center of the spiral
    while True:
        side_length += 2  # Increase the side length by 2 for each layer of the spiral
        for _ in range(4):
            number += side_length - 1  # Calculate the next number on the diagonal
            total_count += 1  # Increment the total count of numbers on the diagonals
            if isprime(number):
                prime_count += 1  # Increment the prime count if the number is prime
        if prime_count / total_count < 0.10:  # Check if the ratio falls below 10%
            return side_length  # Return the side length if the condition is met


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {spiral_primes_ratio()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
