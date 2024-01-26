import time


def find_bouncy(ratio: float) -> int:
    """
    Find the least number for which the proportion of bouncy numbers is at least the specified ratio.

    Args:
        ratio (float): The target ratio.

    Returns:
        int: The least number for which the proportion of bouncy numbers is at least the specified ratio.
    """
    bouncy, number = 0, 100
    while bouncy / number < ratio:
        number += 1
        num_str = str(number)
        if num_str != ''.join(sorted(num_str)) and num_str != ''.join(sorted(num_str, reverse=True)):
            bouncy += 1
    return number


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_bouncy(0.99)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
