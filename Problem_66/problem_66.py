import time
import math


def is_perfect_square(n: int) -> bool:
    """
    Determine if a number is a perfect square.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a perfect square, False otherwise.
    """
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n


def find_minimal_solution(D: int) -> int:
    """
    Find the minimal solution for x in the Pell equation x^2 - Dy^2 = 1.

    Args:
        D (int): The D value in the Pell equation.

    Returns:
        int: The minimal x solution.
    """
    m, d, a = 0, 1, int(math.sqrt(D))
    num1, num2 = 1, a
    den1, den2 = 0, 1

    while num2 * num2 - D * den2 * den2 != 1:
        m = d * a - m
        d = (D - m * m) // d
        a = (int(math.sqrt(D)) + m) // d
        num1, num2 = num2, a * num2 + num1
        den1, den2 = den2, a * den2 + den1

    return num2


def find_largest_z(limit: int) -> int:
    """
    Find the value of D < limit with the largest minimal solution for z.

    Args:
        limit (int): The upper bound for D.

    Returns:
        int: The value of D with the largest minimal solution for z.
    """
    largest_z, result_D = 0, 0

    for D in range(2, limit):
        if not is_perfect_square(D):
            z = find_minimal_solution(D)
            if z > largest_z:
                largest_z, result_D = z, D

    return result_D


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_largest_z(1000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
