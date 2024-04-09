import time
import math


def calculate_catalan_number(n: int) -> int:
    """
    Calculate the nth Catalan number.

    The Catalan numbers are a sequence of natural numbers that occur in various counting problems,
    often involving recursively defined objects.

    Args:
        n (int): The index of the Catalan number to calculate.

    Returns:
        int: The nth Catalan number.
    """
    return math.comb(n * 2, n) // (n + 1)


def calculate_subset_pairs(set_size: int) -> str:
    """
    Calculate the sum of subset pairs for a given set size.

    The sum is calculated based on combinatorial properties.

    Args:
        set_size (int): The size of the set.

    Returns:
        str: The sum of subset pairs as a string.
    """
    return str(sum(math.comb(set_size, i * 2) * (math.comb(i * 2, i) // 2 - calculate_catalan_number(i))
                   for i in range(2, set_size // 2 + 1)))


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {calculate_subset_pairs(12)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
    