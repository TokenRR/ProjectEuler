import time
from math import gcd
from typing import Union


def right_triangles(size: Union[int, float]) -> Union[int, float]:
    """
    Function to calculate the number of right triangles with sides lying on a grid of size 'size' x 'size'.
    
    Parameters:
        size (int, float): The size of the grid.

    Returns:
        triangles (int, float): The number of right triangles.
    """
    triangles = 3 * size * size
    for x in range(1, size + 1):
        for y in range(1, size + 1):
            fact = gcd(x, y)
            triangles += 2 * min(y * fact // x, (size - x) * fact // y)
    return triangles


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {right_triangles(50)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
