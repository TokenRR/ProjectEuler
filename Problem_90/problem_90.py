import time
from itertools import combinations
from typing import List


def can_display_all_squares(cube1: List[str], cube2: List[str]) -> bool:
    """
    Check if all square numbers can be displayed
    """
    squares = ['01', '04', '09', '16', '25', '36', '49', '64', '81']
    return all((s[0] in cube1 and s[1] in cube2)
               or (s[1] in cube1 and s[0] in cube2)
               for s in squares)


def count_cube_pairs() -> int:
    """
    Count the number of possible cube pairs
    """
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cubes = [list(cube) + (['9'] if '6' in cube and '9' not in cube else []) +
            (['6'] if '9' in cube and '6' not in cube else [])
            for cube in combinations(digits, 6)]

    count = sum(can_display_all_squares(cubes[i], cubes[j])
                for i in range(len(cubes))
                for j in range(i, len(cubes)))
    return count


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {count_cube_pairs()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
