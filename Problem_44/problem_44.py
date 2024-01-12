import time


def generate_pentagonal(n):
    """
    Generate the nth pentagonal number.
    
    Parameters:
    n (int): The order of the pentagonal number to generate.
    
    Returns:
    int: The nth pentagonal number.
    """
    return n * (3 * n - 1) // 2


def is_pentagonal(number):
    """
    Check if a number is pentagonal.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is pentagonal, False otherwise.
    """
    n = (1 + (1 + 24 * number)**0.5) / 6
    return n.is_integer()


def find_minimal_pentagonal_pair():
    """
    Find the pair of pentagonal numbers for which their sum and difference are pentagonal,
    and the difference is minimized.
    
    Returns:
    int: The minimal difference.
    """
    pentagonals = [generate_pentagonal(n) for n in range(1, 3000)]
    min_difference = None
    for i in range(len(pentagonals)):
        for j in range(i, len(pentagonals)):
            if is_pentagonal(pentagonals[i] + pentagonals[j]) and is_pentagonal(abs(pentagonals[j] - pentagonals[i])):
                difference = abs(pentagonals[j] - pentagonals[i])
                if min_difference is None or difference < min_difference:
                    min_difference = difference
    return min_difference


if __name__ == "__main__":
    start_time = time.time()
    result = find_minimal_pentagonal_pair()
    print(f'Answer = {result}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
