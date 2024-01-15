import time
from collections import defaultdict
from typing import Dict, List


def is_cube(n: int) -> bool:
    """
    Check if a given number is a perfect cube.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a perfect cube, False otherwise.
    """
    return round(n ** (1/3)) ** 3 == n


def find_smallest_cube() -> int:
    """
    Find the smallest cube for which exactly five permutations of its digits are also cubes.

    Returns:
        int: The smallest cube that meets the condition.
    """
    cubes: Dict[str, List[int]] = defaultdict(list)
    n = 1
    while True:
        cube = n ** 3
        key = ''.join(sorted(str(cube)))
        cubes[key].append(cube)
        
        if len(cubes[key]) == 5:
            return min(cubes[key])
        
        n += 1


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_smallest_cube()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
