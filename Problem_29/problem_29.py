import time


def count_distinct_powers(limit):
    """
    This function returns the number of distinct terms in the sequence generated by a^b for 2 <= a < limit and 2 <= b < limit.

    Parameters:
    limit (int): The upper limit for the values of a and b.

    Returns:
    int: The number of distinct terms in the sequence.
    """
    if limit < 2:
        return "Limit should be greater than or equal to 2."
    else:
        distinct_powers = set(a**b for a in range(2, limit) for b in range(2, limit))
        return len(distinct_powers)


if __name__ == "__main__":
    # Start the timer
    start_time = time.time()

    # Call the function
    count = count_distinct_powers(101)

    # Stop the timer
    end_time = time.time()

    print(f'Answer = {count}')
    print(f'Elapsed time: {round(end_time - start_time, 2)} seconds')
