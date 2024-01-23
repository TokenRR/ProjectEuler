import math
import time
from typing import List


def fib_last_digits(n: int) -> int:
    """
    Calculate the last 9 digits of Fibonacci(n) using matrix exponentiation.

    Args:
        n (int): The index of the Fibonacci number.

    Returns:
        int: The last 9 digits of Fibonacci(n).
    """
    F = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0] % 1_000_000_000


def multiply(F: List[List[int]], M: List[List[int]]) -> None:
    """
    Helper function for fib_last_digits.

    Args:
        F (List[List[int]]): The first matrix.
        M (List[List[int]]): The second matrix.

    Returns:
        None
    """
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]
    F[0][0] = x % 1_000_000_000
    F[0][1] = y % 1_000_000_000
    F[1][0] = z % 1_000_000_000
    F[1][1] = w % 1_000_000_000


def power(F: List[List[int]], n: int) -> None:
    """
    Helper function for fib_last_digits.

    Args:
        F (List[List[int]]): The matrix to be powered.
        n (int): The power to which the matrix is raised.

    Returns:
        None
    """
    if n == 0 or n == 1:
        return
    M = [[1, 1], [1, 0]]
    power(F, n // 2)
    multiply(F, F)
    if n % 2 != 0:
        multiply(F, M)


def fib_first_digits(n: int) -> int:
    """
    Calculate the first 9 digits of Fibonacci(n) using logarithms.

    Args:
        n (int): The index of the Fibonacci number.

    Returns:
        int: The first 9 digits of Fibonacci(n).
    """
    phi = (1 + math.sqrt(5)) / 2
    x = n * math.log10(phi) - math.log10(5) / 2
    frac, whole = math.modf(x)
    return int(10**(frac + 8))


def is_pandigital(n: int) -> bool:
    """
    Check if n is 1-9 pandigital.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is 1-9 pandigital, False otherwise.
    """
    digits = [0] * 10
    for _ in range(9):
        digits[n % 10] += 1
        n //= 10
    return digits[1:] == [1] * 9 and digits[0] == 0


def find_pandigital_fibonacci() -> int:
    """
    Find the index of the first Fibonacci number that is pandigital in the first and last 9 digits.

    Returns:
        int: The index of the first pandigital Fibonacci number.
    """
    n = 1
    while True:
        if is_pandigital(fib_first_digits(n)) and is_pandigital(fib_last_digits(n)):
            return n
        n += 1


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_pandigital_fibonacci()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
