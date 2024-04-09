import time
import math


def find_num_of_solutions() -> int:
    """
    Find the least value of M such that the number of solutions first exceeds one million.

    Returns:
        int: The least value of M.
    """
    M = 0
    count = 0
    while count < 10**6:
        M += 1
        for xy in range(2, 2*M + 1):
            path = math.sqrt(xy**2 + M**2)

            if path.is_integer():
                if xy <= M:
                    count += xy // 2
                else:
                    count += 1 + (M - (xy+1)//2)
    return M


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_num_of_solutions()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
