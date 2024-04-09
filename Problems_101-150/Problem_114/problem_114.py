import time
from typing import List


def calculate_tiling_ways(row_length: int) -> str:
    """
    Calculate the number of ways to tile a row of a given length with red, green, and blue tiles.

    Args:
        row_length (int): The length of the row.

    Returns:
        str: The number of ways.
    """
    tiling_ways: List[int] = [1, 1, 1] + [0] * (row_length - 2)
    for current_length in range(3, row_length + 1):
        tiling_ways[current_length] = tiling_ways[current_length - 1] + sum(tiling_ways[:current_length - 3]) + 1
    return str(tiling_ways[-1])


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {calculate_tiling_ways(row_length=50)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
