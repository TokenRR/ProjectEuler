import time
import math


def find_largest_line(file_path: str) -> int:
    """
    Find the line number with the largest value in a file containing pairs of base and exponent.

    Args:
        file_path (str): The path to the file containing base and exponent pairs.

    Returns:
        int: The line number with the largest value.
    """
    largest_value = 0
    line_number = 0
    with open(file_path, 'r') as file:
        for i, line in enumerate(file, start=1):
            base, exponent = map(int, line.split(','))
            current_value = exponent * math.log(base)  # Use properties of logarithms to simplify calculation
            if current_value > largest_value:
                largest_value = current_value
                line_number = i
    return line_number


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_largest_line('Problem_99/0099_base_exp.txt')}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
