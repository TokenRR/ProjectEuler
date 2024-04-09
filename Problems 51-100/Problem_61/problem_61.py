import time
from itertools import permutations
from typing import Dict, List


def generate_polygonal(s: int, n: int) -> int:
    """
    Generate an s-gonal number.

    Args:
        s (int): The type of polygonal number (3 for triangle, 4 for square, etc.).
        n (int): The index of the polygonal number to generate.

    Returns:
        int: The nth s-gonal number.
    """
    if s == 3:
        return n * (n + 1) // 2
    if s == 4:
        return n**2
    if s == 5:
        return n * (3 * n - 1) // 2
    if s == 6:
        return n * (2 * n - 1)
    if s == 7:
        return n * (5 * n - 3) // 2
    if s == 8:
        return n * (3 * n - 2)


def is_cyclic(p1: int, p2: int) -> bool:
    """
    Check if two numbers are cyclic.

    Args:
        p1 (int): The first number.
        p2 (int): The second number.

    Returns:
        bool: True if p1 and p2 are cyclic, False otherwise.
    """
    return p1 % 100 == p2 // 100


def find_cyclical_set(figurate_numbers: Dict[int, List[int]]) -> List[int]:
    """
    Find a cyclical set from the given figurate numbers.

    Args:
        figurate_numbers (Dict[int, List[int]]): A dictionary of figurate numbers.

    Returns:
        List[int]: A list representing the cyclical set.
    """
    for perm in permutations(range(3, 9)):
        for p in figurate_numbers[perm[0]]:
            cyclical_set = [p]
            found = True

            for i in range(1, 6):
                p_next = [x for x in figurate_numbers[perm[i]] if is_cyclic(cyclical_set[-1], x)]
                if not p_next:
                    found = False
                    break
                cyclical_set.append(p_next[0])

            if found and is_cyclic(cyclical_set[-1], cyclical_set[0]):
                return cyclical_set
    return []


if __name__ == "__main__":
    start_time = time.time()

    figurate_numbers = {s: [] for s in range(3, 9)}
    for s in range(3, 9):
        n = 1
        while True:
            num = generate_polygonal(s, n)
            if num > 9999:
                break
            elif num > 999:
                figurate_numbers[s].append(num)
            n += 1

    cyclical_set = find_cyclical_set(figurate_numbers)
    print(f"Answer = {sum(cyclical_set)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
