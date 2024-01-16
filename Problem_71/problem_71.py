import time


def left_fraction(denominator_limit: int) -> int:
    """
    Find the numerator of the fraction immediately to the left of 3/7 for d ≤ denominator_limit.

    Args:
        denominator_limit (int): The upper bound for the denominator.

    Returns:
        int: The numerator of the fraction immediately to the left of 3/7.
    """
    target_numerator, target_denominator = 3, 7
    max_numerator, max_denominator = 0, 1

    for d in range(2, denominator_limit + 1):
        n = (target_numerator * d - 1) // target_denominator
        if n * max_denominator > max_numerator * d:
            max_numerator, max_denominator = n, d

    return max_numerator

if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {left_fraction(1_000_000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
