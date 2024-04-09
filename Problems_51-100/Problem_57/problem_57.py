import time


def has_more_digits_in_numerator(numerator, denominator):
    """
    Check if the numerator has more digits than the denominator.

    Parameters:
    numerator (int): The numerator of the fraction.
    denominator (int): The denominator of the fraction.

    Returns:
    bool: True if the numerator has more digits, False otherwise.
    """
    return len(str(numerator)) > len(str(denominator))


def count_expansions_with_more_digits(limit):
    """
    Count the number of expansions where the numerator has more digits.

    Parameters:
    limit (int): The number of expansions to check.

    Returns:
    int: The count of expansions with more digits in the numerator.
    """
    count = 0
    numerator, denominator = 3, 2
    for _ in range(2, limit + 1):
        numerator, denominator = numerator + 2 * denominator, numerator + denominator
        if has_more_digits_in_numerator(numerator, denominator):
            count += 1
    return count


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {count_expansions_with_more_digits(1000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
