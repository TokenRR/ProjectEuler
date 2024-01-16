import time
from math import gcd
from typing import Tuple


def count_fractions_between(lower_limit: Tuple[int, int],
                            upper_limit: Tuple[int, int],
                            max_denominator: int) -> int:
    """
    Count the number of reduced proper fractions between two given fractions.

    Args:
        lower_limit (Tuple[int, int]): The lower limit fraction as a tuple (numerator, denominator).
        upper_limit (Tuple[int, int]): The upper limit fraction as a tuple (numerator, denominator).
        max_denominator (int): The maximum denominator to consider.

    Returns:
        int: The number of reduced proper fractions between the limits.
    """
    count = 0
    for d in range(2, max_denominator + 1):
        for n in range(d // 3 + 1, (d + 1) // 2):
            if gcd(n, d) == 1:
                if lower_limit[0] * d < n * lower_limit[1] and n * upper_limit[1] < upper_limit[0] * d:
                    count += 1
    return count


if __name__ == "__main__":
    start_time = time.time()
    
    lower_limit = (1, 3)  # Lower limit fraction
    upper_limit = (1, 2)  # Upper limit fraction
    max_denominator = 12000  # Maximum denominator
    
    print(f"Answer = {count_fractions_between(lower_limit, upper_limit, max_denominator)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
