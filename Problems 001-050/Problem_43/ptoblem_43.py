import itertools
import time


def has_substring_divisibility(num_str):
    """
    Checks if a string of numbers has the substring divisibility property.

    The substring divisibility property is that the number formed by every three consecutive digits
    of the string, starting from index i+1, is divisible by the i-th prime number from a list of prime numbers.

    Parameters:
    - num_str (str): The string of numbers to check.

    Returns:
    - bool: True if the string has the substring divisibility property, otherwise False.
    """
    primes = [2, 3, 5, 7, 11, 13, 17]
    return all(int(num_str[i+1:i+4]) % primes[i] == 0 for i in range(7))


if __name__ == '__main__':
    start_time = time.time()
    # Генерація всіх 0 до 9 пандігітальних чисел
    pandigitals = [''.join(p) for p in itertools.permutations('0123456789')]

    # Відбір чисел з потрібною властивістю та обчислення їх суми
    sum_of_numbers = sum(int(p) for p in pandigitals if has_substring_divisibility(p))

    print(f'Answer = {sum_of_numbers}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')

