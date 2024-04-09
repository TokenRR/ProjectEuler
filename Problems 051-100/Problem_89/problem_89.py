import time


def from_roman(num: str) -> int:
    """
    Convert a Roman numeral to an integer.

    Args:
        num (str): The Roman numeral to convert.

    Returns:
        int: The integer representation of the Roman numeral.
    """
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(num)):
        if i > 0 and roman_numerals[num[i]] > roman_numerals[num[i - 1]]:
            result += roman_numerals[num[i]] - 2 * roman_numerals[num[i - 1]]
        else:
            result += roman_numerals[num[i]]
    return result


def to_roman(num: int) -> str:
    """
    Convert an integer to a Roman numeral.

    Args:
        num (int): The integer to convert.

    Returns:
        str: The Roman numeral representation of the integer.
    """
    value_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                 (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ''
    for i, numeral in value_map:
        count = num // i
        result += numeral * count
        num -= i * count
    return result


def solve_problem() -> int:
    """
    Solve the problem of finding the difference between the original length of the Roman numerals
    and the minimal length of the Roman numerals.

    Returns:
        int: The difference between the original length and the minimal length.
    """
    with open('Problem_89\\0089_roman.txt', 'r') as file:
        lines = file.read().splitlines()
    original_length = sum(len(line) for line in lines)
    minimal_length = sum(len(to_roman(from_roman(line))) for line in lines)
    return original_length - minimal_length


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer: {solve_problem()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
