import time


def digital_sum(number):
    """
    Calculate the digital sum of a number.

    Parameters:
    number (int): The number to calculate the digital sum of.

    Returns:
    int: The digital sum of the number.
    """
    return sum(int(digit) for digit in str(number))


def max_digital_sum(limit):
    """
    Find the maximum digital sum of \(a^b\) for \(a, b < limit\).

    Parameters:
    limit (int): The upper limit for \(a\) and \(b\).

    Returns:
    int: The maximum digital sum found.
    """
    return max(digital_sum(a ** b) for a in range(1, limit) for b in range(1, limit))

if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {max_digital_sum(100)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
