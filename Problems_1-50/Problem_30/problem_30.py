import time


def find_sum_of_digit_powers(power):
    """
    This function returns the sum of all numbers that can be written as the sum of fifth powers of their digits.

    Parameters:
    power (int): The power to which each digit is raised.

    Returns:
    int: The sum of all numbers that can be written as the sum of fifth powers of their digits.
    """
    if power <= 0:
        return "Power should be a positive integer."
    else:
        total = 0
        for i in range(2, (power + 1) * (9**power)):
            if i == sum(int(digit)**power for digit in str(i)):
                total += i
        return total


if __name__ == "__main__":
    # Start the timer
    start_time = time.time()

    # Call the function
    total = find_sum_of_digit_powers(5)

    # Stop the timer
    end_time = time.time()

    print(f'Answer = {total}')
    print(f'Elapsed time: {round(end_time - start_time, 2)} seconds')
