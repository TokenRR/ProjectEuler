import time


def find_coefficients(limit):
    """
    This function returns the coefficients a and b for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

    Parameters:
    limit (int): The upper limit for the absolute values of the coefficients a and b.

    Returns:
    tuple: The coefficients a and b that produce the maximum number of primes for consecutive values of n.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_primes = 0
    best_a = 0
    best_b = 0

    for a in range(-limit + 1, limit):
        for b in range(-limit + 1, limit):
            n = 0
            while is_prime(abs(n**2 + a*n + b)):
                n += 1
            if n > max_primes:
                max_primes = n
                best_a = a
                best_b = b

    return best_a, best_b


if __name__ == "__main__":
    # Start the timer
    start_time = time.time()

    # Call the function
    a, b = find_coefficients(1000)

    # Stop the timer
    end_time = time.time()

    print(f'Answer = {a * b}')
    print(f'Elapsed time: {round(end_time - start_time, 2)} seconds')
