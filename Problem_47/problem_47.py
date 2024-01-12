import time
from sympy import primefactors


def find_consecutive_integers(num_factors, consecutive):
    """
    Find the first set of consecutive integers that have a given number of distinct prime factors each.
    
    Parameters:
    num_factors (int): The number of distinct prime factors to find.
    consecutive (int): The number of consecutive integers to find.
    
    Returns:
    list: The first set of consecutive integers that meet the criteria.
    """
    count = 0
    num = 2
    while True:
        if len(primefactors(num)) == num_factors:
            count += 1
            if count == consecutive:
                return list(range(num - consecutive + 1, num + 1))
        else:
            count = 0
        num += 1


if __name__ == "__main__":
    start_time = time.time()
    result = find_consecutive_integers(4, 4)
    print(f'Answer = {result[0]}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
