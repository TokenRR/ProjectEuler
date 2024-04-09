import time
from typing import Dict, List


# Create a dictionary to store already computed chains
memo: Dict[int, bool] = {89: True, 1: False}


def square_digits(n: int) -> int:
    """
    Function to calculate the sum of the squares of the digits of a number.
    
    Parameters:
    n (int): The number whose digits are to be squared.

    Returns:
    int: The sum of the squares of the digits of 'n'.
    """
    return sum(int(digit)**2 for digit in str(n))


def chain_ends_in_89(n: int) -> bool:
    """
    Function to check if a chain ends in 89.
    
    Parameters:
    n (int): The number to start the chain from.

    Returns:
    bool: True if the chain ends in 89, False otherwise.
    """
    chain: List[int] = []
    while n not in memo:
        chain.append(n)
        n = square_digits(n)
    ends_in_89 = memo[n]
    for num in chain:
        memo[num] = ends_in_89
    return ends_in_89


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {sum(chain_ends_in_89(n) for n in range(1, 10**7))}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
    