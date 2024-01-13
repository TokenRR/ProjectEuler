import time
from math import factorial


def combinations_count_exceeding_million(n_max, threshold):
    """
    Count the number of combinations C(n, r) that exceed a given threshold.
    
    Parameters:
    n_max (int): The maximum value of n to consider.
    threshold (int): The threshold value that C(n, r) must exceed.
    
    Returns:
    int: The count of combinations exceeding the threshold.
    """
    count = 0
    for n in range(1, n_max + 1):
        for r in range(0, n + 1):
            if factorial(n) // (factorial(r) * factorial(n - r)) > threshold:
                count += 1
    return count


if __name__ == "__main__":
    start_time = time.time()
    result = combinations_count_exceeding_million(100, 1000000)
    print(f'Answer = {result}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
