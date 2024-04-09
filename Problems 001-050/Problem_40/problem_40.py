import time
import math


def find_fraction_digits():
    """
    Find the specified digits in the concatenated sequence of positive integers
    """
    limit = 1_000_000  # Search up to the millionth digit
    number = ''.join(str(i) for i in range(1, limit//2))
    digits = [int(number[10**j - 1]) for j in range(7)]
    return digits, math.prod(digits)


if __name__ == "__main__":
    start_time = time.time()
    digits, product = find_fraction_digits()
    print(f'Specified digits: {digits}')
    print(f'\nAnswer = {product}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
