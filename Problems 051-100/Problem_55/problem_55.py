import time


def is_lychrel(n):
    """
    Determine if a number is a Lychrel number.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is a Lychrel number, False otherwise.
    """
    for _ in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True


def count_lychrel_numbers(limit):
    """
    Count the number of Lychrel numbers below a given limit.

    Parameters:
    limit (int): The upper limit for counting Lychrel numbers.

    Returns:
    int: The count of Lychrel numbers below the given limit.
    """
    return sum(1 for i in range(1, limit) if is_lychrel(i))


if __name__ == "__main__":
    start_time = time.time()
    lychrel_count = count_lychrel_numbers(10000)
    print(f"Answer = {lychrel_count}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
