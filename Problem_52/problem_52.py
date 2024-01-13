import time


def find_integer_with_permuted_multiples():
    """
    Find the smallest positive integer x, such that 2x, 3x, 4x, 5x, and 6x contain the same digits.
    
    Returns:
    int: The smallest positive integer with the specified property.
    """
    x = 1
    while True:
        if all(sorted(str(x)) == sorted(str(x * i)) for i in range(2, 7)):
            return x
        x += 1


if __name__ == "__main__":
    start_time = time.time()
    result = find_integer_with_permuted_multiples()
    print(f'Answer = {result}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
