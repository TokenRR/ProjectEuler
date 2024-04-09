import time


def count_n_digit_nth_powers():
    """
    Count the number of n-digit positive integers that are also an nth power.

    Returns:
        int: The count of n-digit nth powers.
    """
    count = 0
    for n in range(1, 22):  # 9**22 is the first number to have more than 21 digits
        for base in range(1, 10):  # Only 1-9 can be the base for an n-digit nth power
            if len(str(base**n)) == n:
                count += 1
    return count


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {count_n_digit_nth_powers()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
