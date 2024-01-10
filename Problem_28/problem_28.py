import time


def find_diagonal_sum(spiral_size):
    """
    This function returns the sum of the numbers on the diagonals in a spiral of the specified size.

    Parameters:
    spiral_size (int): The size of the spiral.

    Returns:
    int: The sum of the numbers on the diagonals in the spiral.
    """
    if spiral_size < 1 or spiral_size % 2 == 0:
        return "Spiral size should be an odd positive integer."
    else:
        total = 1
        for layer in range(3, spiral_size + 1, 2):
            total += 4 * layer**2 - 6 * (layer - 1)
        return total


if __name__ == "__main__":
    # Start the timer
    start_time = time.time()

    # Call the function
    diagonal_sum = find_diagonal_sum(1001)

    # Stop the timer
    end_time = time.time()

    print(f'Answer = {diagonal_sum}')
    print(f'Elapsed time: {round(end_time - start_time, 2)} seconds')
