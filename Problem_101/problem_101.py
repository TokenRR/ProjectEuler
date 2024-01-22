import time
from sympy import simplify
from typing import List, Tuple


def lagrange_interpolation(data_points: List[Tuple[int, int]], x: int) -> int:
    """
    Perform Lagrange interpolation to find the value at a specific point.

    Args:
        data_points (List[Tuple[int, int]]): List of data points as tuples (x, y).
        x (int): The point to evaluate the interpolation.

    Returns:
        int: The interpolated value at the given point.
    """
    result = 0
    n = len(data_points)

    for i in range(n):
        term = data_points[i][1]
        for j in range(n):
            if j != i:
                term *= (x - data_points[j][0]) / (data_points[i][0] - data_points[j][0])
        result += term
    
    return simplify(result)


def sum_of_FITs(k: int, sequence_length: int) -> int:
    """
    Calculate the sum of F.I.T.s (Fractional Iterative Terms) for the BOPs (Best Obtained Polynomials).

    Args:
        k (int): The degree of the polynomial.
        sequence_length (int): The length of the sequence.

    Returns:
        int: The sum of F.I.T.s for the BOPs.
    """
    total_fit_sum = 0

    for k_value in range(1, k + 1):
        data_points = [(i + 1, sequence[i]) for i in range(k_value)]

        # Check for BOP and calculate the FIT
        if sequence_length >= k_value + 1:
            next_term = lagrange_interpolation(data_points, k_value + 1)
            total_fit_sum += next_term

    return int(total_fit_sum)


if __name__ == "__main__":
    start_time = time.time()
    sequence = [1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10 for n in range(1, 12)]
    print(f"Answer = {sum_of_FITs(10, len(sequence))}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
