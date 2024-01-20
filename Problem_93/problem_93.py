import time
from typing import List, Union, Tuple, Generator


def generate_combinations(seq: List[int], length: int) -> Generator[List[int], None, None]:
    """
    Generate combinations of a given length from the input sequence.

    Args:
        seq (List[int]): The input sequence of integers.
        length (int): The desired length of combinations to generate.

    Yields:
        List[int]: A list of integers representing a combination.
    """
    if not length:
        yield []
    else:
        yield from ([seq[i]] + result
                    for i in range(len(seq))
                    for result in generate_combinations(seq[i + 1:], length - 1))


def next_permutation(num: List[int]) -> List[int]:
    """
    Find the next permutation of a given list of numbers.

    Args:
        num (List[int]): The input list of integers.

    Returns:
        List[int]: The next permutation of the input list.
    """
    if len(num) < 2:
        return num
    partition = -1
    for i in range(len(num) - 2, -1, -1):
        if num[i] < num[i + 1]:
            partition = i
            break
    if partition == -1:
        return num[::-1]
    for i in range(len(num) - 1, partition, -1):
        if num[i] > num[partition]:
            num[i], num[partition] = num[partition], num[i]
            break
    num[partition + 1:] = num[partition + 1:][::-1]
    return num


def operate(a: Union[int, None], b: Union[int, None], num: int) -> Union[int, float, None]:
    """
    Perform mathematical operations based on the given operation number.

    Args:
        a (Union[int, None]): The first operand.
        b (Union[int, None]): The second operand.
        num (int): The operation number (1: addition, 2: subtraction, 3: multiplication, 4: division).

    Returns:
        Union[int, float, None]: The result of the operation.
        Returns None for invalid operations or division by zero.
    """
    if a is None or b is None: return None
    if num == 1: return a + b
    if num == 2: return a - b
    if num == 3: return a * b
    return None if num == 4 and b == 0 else a / b


def find_best_result() -> Tuple[int, List[int]]:
    """
    Find the combination with the best result based on the given conditions.

    Returns:
        Tuple[int, List[int]]: A tuple containing the best result count and the corresponding combination.
    """
    numbers = [i for i in range(10)]
    combinations_list = list(generate_combinations(numbers, 4))
    
    best_premise = [0 for _ in range(4)]
    best_result = 0

    for premise in combinations_list:
        tmp = premise
        flag = 1
        num_list = [False] * (9 * 8 * 7 * 6)

        while tmp != premise or flag == 1:
            flag = 0
            for i in range(1, 5):
                for j in range(1, 5):
                    for k in range(1, 5):
                        num = operate(operate(operate(premise[0], premise[1], i), premise[2], j), premise[3], k)
                        if num is not None and num == int(num) and 0 < num < len(num_list):
                            num_list[int(num)] = True

                        num = operate(operate(premise[0], operate(premise[1], premise[2], j), i), premise[3], k)
                        if num is not None and num == int(num) and 0 < num < len(num_list):
                            num_list[int(num)] = True

                        num = operate(premise[0], operate(operate(premise[1], premise[2], j), premise[3], k), i)
                        if num is not None and num == int(num) and 0 < num < len(num_list):
                            num_list[int(num)] = True

                        num = operate(premise[0], operate(premise[1], operate(premise[2], premise[3], k), j), i)
                        if num is not None and num == int(num) and 0 < num < len(num_list):
                            num_list[int(num)] = True

                        num = operate(operate(premise[0], premise[1], i), operate(premise[2], premise[3], k), j)
                        if num is not None and num == int(num) and 0 < num < len(num_list):
                            num_list[int(num)] = True

            count = 1
            while num_list[count] is True:
                count += 1

            if count > best_result:
                best_result = count
                best_premise = premise

            premise = next_permutation([premise[i] for i in range(4)])   
    return best_result, ''.join(map(str, sorted(best_premise)))


if __name__ == "__main__":
    start_time = time.time()
    best_result, best_premise = find_best_result()
    print(f"Answer = {best_premise}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
