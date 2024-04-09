import time
from itertools import permutations
from typing import Tuple


def is_valid(combination: Tuple[int, ...]) -> bool:
    """
    Check if the sum of each line is the same.

    Args:
    combination (Tuple[int, ...]): A tuple representing the ring of numbers.

    Returns:
    bool: True if all lines have the same sum, False otherwise.
    """
    a, b, c, d, e, f, g, h, i, j = combination
    line_sum = a + f + g
    return all((b + g + h == line_sum,
                c + h + i == line_sum,
                d + i + j == line_sum,
                e + j + f == line_sum))


def find_max_string() -> str:
    """
    Generate all possible permutations for the internal and external numbers
    and find the maximum 16-digit string that satisfies the magic ring condition.

    Returns:
        str: The maximum 16-digit string.
    """
    max_string = '0'
    for perm in permutations(range(1, 11)):
        if is_valid(perm):
            strings = []
            for i in range(5):
                strings.append(str(perm[i]) + str(perm[(i + 5) % 10]) + str(perm[(i + 1) % 5 + 5]))
            min_external = min(perm[:5])
            min_index = perm.index(min_external)
            strings = strings[min_index:] + strings[:min_index]
            magic_string = ''.join(strings)
            if magic_string > max_string:
                max_string = magic_string
    return max_string


if __name__ == '__main__':
    start_time = time.time()
    print(f'Answer = {find_max_string()}')
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
