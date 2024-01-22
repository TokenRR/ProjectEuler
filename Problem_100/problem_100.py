import time


def find_blue_disks() -> int:
    """
    Find the number of blue disks in the arrangement.

    Returns:
        int: The number of blue disks.
    """
    b, n = 15, 21
    while n < 10**12:
        b_temp = 3 * b + 2 * n - 2
        n_temp = 4 * b + 3 * n - 3
        b, n = b_temp, n_temp
    return b


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_blue_disks()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
