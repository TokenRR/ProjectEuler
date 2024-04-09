import time
import math
import itertools


def find_least_n() -> str:
    """
    Find the least value of n for which the number of distinct solutions exceeds one-thousand.

    Returns:
        str: The least value of n for which the number of distinct solutions exceeds one-thousand.
    """
    for n in itertools.count(1):
        m = n  # We use a different variable here to avoid conflict
        count = 1
        end = math.isqrt(m)
        for i in itertools.count(2):
            if i > end:
                break
            if m % i == 0:
                j = 0
                while True:
                    m //= i
                    j += 1
                    if m % i != 0:
                        break
                count *= j * 2 + 1
                end = math.isqrt(m)
        if m != 1:  # Remaining largest prime factor
            count *= 3
        if (count + 1) // 2 > 1000:
            return str(n)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_least_n()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
    