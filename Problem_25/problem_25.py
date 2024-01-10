import time


def fibonacci(n):
    """
    This function returns the nth Fibonacci number.

    Parameters:
    n (int): The index of the Fibonacci sequence to return.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b


def find_index_with_digit_count(digit_count):
    """
    This function returns the index of the first Fibonacci number with the specified number of digits.

    Parameters:
    digit_count (int): The number of digits in the Fibonacci number.

    Returns:
    int: The index of the first Fibonacci number with the specified number of digits.
    """
    if digit_count <= 0:
        return "Input should be a positive integer."
    else:
        index = 1
        while len(str(fibonacci(index))) < digit_count:
            index += 1
        return index


if __name__ == '__main__':
    # Start the timer
    start_time = time.time()

    # Call the function
    index = find_index_with_digit_count(1000)

    # Stop the timer
    end_time = time.time()

    print(f'Answer = {index}')
    print(f'Elapsed time: {round(end_time - start_time, 2)} seconds.')
