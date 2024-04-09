import time
from typing import Tuple, Union, List


def find_optimum_set(target_set_size: int,
                     max_set_sum: int) -> Union[None, Tuple[List[int], List[bool], List[int], List[int]]]:
    """
    Find an optimum set satisfying certain conditions.

    Args:
        target_set_size (int): The size of the target set.
        max_set_sum (int): The maximum sum of the set.

    Returns:
        Union[None, Tuple[List[int], List[bool], List[int], List[int]]]: The optimum set or None if not found.
    """
    return find_optimum_set_helper(([], [True], [0], [0]), target_set_size, max_set_sum, 1)


def find_optimum_set_helper(current_set: Tuple[List[int], List[bool], List[int], List[int]], 
                            remaining_size: int,
                            remaining_sum: int,
                            start_value: int) -> Union[None, Tuple[List[int], List[bool], List[int], List[int]]]:
    """
    Helper function for finding an optimum set.

    Args:
        current_set (Tuple[List[int], List[bool], List[int], List[int]]): The current set.
        remaining_size (int): Remaining size to be added to the set.
        remaining_sum (int): Remaining sum to be achieved in the set.
        start_value (int): The starting value for the new elements.

    Returns:
        Union[None, Tuple[List[int], List[bool], List[int], List[int]]]: The optimum set or None if not found.
    """
    if remaining_size == 0:
        return current_set

    if remaining_size >= 2 and start_value * remaining_size >= remaining_sum:
        return None

    end_value = remaining_sum
    if len(current_set[0]) >= 2:
        end_value = min(current_set[0][0] + current_set[0][1] - 1, end_value)

    for value in range(start_value, end_value + 1):
        temp_set = add_to_set(current_set, value)
        if temp_set is None:
            continue

        temp_set = find_optimum_set_helper(temp_set, remaining_size - 1, remaining_sum - value, value + 1)
        if temp_set is not None:
            return temp_set
    return None


def add_to_set(current_set: Tuple[List[int], List[bool], List[int], List[int]],
               value: int) -> Union[None, Tuple[List[int], List[bool], List[int], List[int]]]:
    """
    Add a value to the set.

    Args:
        current_set (Tuple[List[int], List[bool], List[int], List[int]]): The current set.
        value (int): The value to be added.

    Returns:
        Union[None, Tuple[List[int], List[bool], List[int], List[int]]]: The updated set or None if the value is invalid.
    """
    if value <= 0 or (len(current_set[0]) >= 1 and value <= current_set[0][-1]):
        raise ValueError("Invalid value")

    possible_values = current_set[1]
    if any((possible_values[i] and possible_values[i - value]) for i in range(value, len(possible_values))):
        return None

    new_set_size = len(current_set[0]) + 1
    new_min_values = [0] + [min(current_set[2][i], current_set[2][i - 1] + value)
                            for i in range(1, new_set_size)] + [current_set[2][-1] + value]
    new_max_values = [0] + [max(current_set[3][i], current_set[3][i - 1] + value)
                            for i in range(1, new_set_size)] + [current_set[3][-1] + value]

    if any((new_max_values[i] >= new_min_values[i + 1]) for i in range(new_set_size)):
        return None

    new_possible_values = possible_values + [False] * value
    for i in reversed(range(value, len(new_possible_values))):
        new_possible_values[i] |= new_possible_values[i - value]

    return (current_set[0] + [value], new_possible_values, new_min_values, new_max_values)


def compute_optimum_set_string() -> str:
    """
    Compute the optimum set as a string.

    Returns:
        str: The optimum set as a string.
    """
    TARGET_SET_SIZE = 7
    max_set_sum = 1

    while find_optimum_set(TARGET_SET_SIZE, max_set_sum) is None:
        max_set_sum *= 2

    increment = max_set_sum // 4
    while increment > 0:
        max_set_sum -= increment
        if find_optimum_set(TARGET_SET_SIZE, max_set_sum) is None:
            max_set_sum += increment
        increment //= 2

    result_set = find_optimum_set(TARGET_SET_SIZE, max_set_sum)
    return "".join(map(str, result_set[0]))


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {compute_optimum_set_string()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
    