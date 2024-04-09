import time


def find_min_n(target_value: int) -> int:
    """
    Find the minimum value of n for which p(n) is divisible by the target value.

    Args:
    target_value (int): The value to check divisibility against.

    Returns:
    int: The minimum value of n.
    """
    partitions = [1]
    n = 1

    while True:
        total = 0
        k = 1
        sign = 1

        while True:
            index1 = n - (k * (3 * k - 1)) // 2
            index2 = n - (k * (3 * k + 1)) // 2

            if index1 < 0 and index2 < 0:
                break

            if index1 >= 0:
                total += sign * partitions[index1]
            if index2 >= 0:
                total += sign * partitions[index2]

            sign *= -1
            k += 1

        partitions.append(total % 10**6)

        if partitions[n] % target_value == 0:
            return n

        n += 1


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_min_n(1_000_000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
