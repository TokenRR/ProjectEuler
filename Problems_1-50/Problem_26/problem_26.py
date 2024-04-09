import time


def find_longest_recurring_cycle(limit):
    """
    This function returns the number less than the limit that produces the longest recurring cycle in its decimal fraction part.

    Parameters:
    limit (int): The upper limit for the numbers to check.

    Returns:
    int: The number less than the limit that produces the longest recurring cycle in its decimal fraction part.
    """
    if limit <= 0:
        return "Input should be a positive integer."
    else:
        longest_cycle_length = 0
        number_with_longest_cycle = 0

        for i in range(2, limit):
            remainders = [0] * i
            value = 1
            position = 0

            while remainders[value] == 0 and value != 0:
                remainders[value] = position
                value *= 10
                value %= i
                position += 1

            if position - remainders[value] > longest_cycle_length:
                number_with_longest_cycle = i
                longest_cycle_length = position - remainders[value]

        return number_with_longest_cycle


if __name__ == "__main__":
    # Start the timer
    start_time = time.time()

    # Call the function
    number = find_longest_recurring_cycle(1000)

    # Stop the timer
    end_time = time.time()

    print(f'Answer = {number}')
    print(f'Elapsed time: {round(end_time - start_time, 2)} seconds')
