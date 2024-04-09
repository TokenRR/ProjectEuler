import time
from typing import List


def compute_special_sum(sets: List[List[int]]) -> str:
    """
    Compute the sum of special sets from the given list of sets.

    A set is considered special if it satisfies the conditions mentioned in the problem.

    Args:
        sets (List[List[int]]): List of sets.

    Returns:
        str: The sum of special sets.
    """
    return str(sum(sum(s) for s in sets if is_special_sum_set(s)))


def is_special_sum_set(s: List[int]) -> bool:
    """
    Check if the given set is a special sum set.

    A set is considered special if it satisfies the conditions mentioned in the problem.

    Args:
        s (List[int]): The set to check.

    Returns:
        bool: True if the set is special, False otherwise.
    """
    seen_sums = set()
    min_sum = [None] * (len(s) + 1)
    max_sum = [None] * (len(s) + 1)
    
    for i in range(2**len(s)):
        subset = [s[j] for j in range(len(s)) if (i & (1 << j)) != 0]
        sum_subset = sum(subset)
        count_subset = len(subset)
        seen_sums.add(sum_subset)
        if min_sum[count_subset] is None or sum_subset < min_sum[count_subset]:
            min_sum[count_subset] = sum_subset
        if max_sum[count_subset] is None or sum_subset > max_sum[count_subset]:
            max_sum[count_subset] = sum_subset
    
    return len(seen_sums) == 2**len(s) and all(max_sum[i] < min_sum[i + 1] for i in range(len(s)))


def read_file(file_path: str) -> List[List[int]]:
    """
    Read sets from a file and return a list of sets.

    Each line in the file should contain a comma-separated list of integers.

    Args:
        file_path (str): The path to the file.

    Returns:
        List[List[int]]: List of sets.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [[int(num) for num in line.strip().split(',')] for line in lines]


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {compute_special_sum(read_file('Problem_105/0105_sets.txt'))}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
    