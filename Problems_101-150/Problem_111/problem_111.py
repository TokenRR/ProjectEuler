import time
from typing import Iterator, List

import sympy


def calculate_prime_sum(DIGITS: int = 10) -> str:
    """
    Calculate the sum of prime numbers with a specific digit repetition pattern.

    Args:
        DIGITS (int): The number of digits. Defaults to 10.

    Returns:
        str: The sum of prime numbers.
    """
    return str(sum(
        next(
            sum(
                number
                for number in generate_prime_numbers(digit, repetitions, DIGITS)
                if sympy.isprime(number)
            )
            for repetitions in range(DIGITS, -1, -1)
            if any(
                sympy.isprime(number)
                for number in generate_prime_numbers(digit, repetitions, DIGITS)
            )
        )
        for digit in range(10)
    ))


def generate_prime_numbers(digit: int, repetitions: int, DIGITS: int) -> Iterator[int]:
    """
    Generate prime numbers with a specific digit repetition pattern.

    Args:
        digit (int): The digit to be repeated.
        repetitions (int): The number of repetitions.
        DIGITS (int): The total number of digits.

    Yields:
        int: The generated prime number.
    """
    digit_array = [0] * DIGITS
    for i in range(9 ** (DIGITS - repetitions)):
        digit_array[:repetitions] = [digit] * repetitions
        temp = i
        for j in range(DIGITS - repetitions):
            d = temp % 9
            if d >= digit:
                d += 1
            if j > 0 and d > digit_array[DIGITS - j]:
                break
            digit_array[-1 - j] = d
            temp //= 9
        else:
            digit_array.sort()
            while True:
                if digit_array[0] > 0:
                    yield int(''.join(map(str, digit_array)))
                if not permute_digits(digit_array):
                    break


def permute_digits(array: List[int]) -> bool:
    """
    Helper function to permute digits.

    Args:
        array (List[int]): The array to be permuted.

    Returns:
        bool: True if permutation is successful, False otherwise.
    """
    index = len(array) - 1
    while index > 0 and array[index - 1] >= array[index]:
        index -= 1
    if index <= 0:
        return False
    swap_index = len(array) - 1
    while array[swap_index] <= array[index - 1]:
        swap_index -= 1
    array[index - 1], array[swap_index] = array[swap_index], array[index - 1]
    array[index:] = array[len(array) - 1 : index - 1 : -1]
    return True


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {calculate_prime_sum()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
    