import time


def last_ten_digits_of_series(limit):
    """
    Calculate the last ten digits of the series 1^1 + 2^2 + ... + n^n.
    
    Parameters:
    limit (int): The upper limit of the series.
    
    Returns:
    int: The last ten digits of the series.
    """
    total = 0
    for i in range(1, limit + 1):
        total += pow(i, i, 10**10)
    return total % 10**10


if __name__ == "__main__":
    start_time = time.time()
    result = last_ten_digits_of_series(1000)
    print(f'Answer = {result}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
