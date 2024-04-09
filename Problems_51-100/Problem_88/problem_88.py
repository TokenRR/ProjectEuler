import time
from typing import List


def generate_product_sum(num: int, prod: int, summ: int, start: int,
                         limit: int, minimal_product_sums: List[int]) -> None:
    """
    Recursive function to generate product-sum numbers.

    Args:
        num (int):   The current number of factors.
        prod (int):  The current product.
        summ (int):  The current sum.
        start (int): The starting number for the set.
        limit (int): The upper limit for the numbers.
        minimal_product_sums (List[int]): A list to store the minimal product-sum numbers.
    """
    k = prod - summ + num
    if k <= limit:
        if prod < minimal_product_sums[k]:
            minimal_product_sums[k] = prod
    for i in range(start, limit // prod * 2 + 1):
        generate_product_sum(num + 1, prod * i, summ + i, i, limit, minimal_product_sums)


def find_minimal_product_sum(limit: int) -> int:
    """
    Find the sum of all minimal product-sum numbers for 2 ≤ k ≤ limit.

    Args:
        limit (int): The upper bound for k.

    Returns:
        int: The sum of all minimal product-sum numbers.
    """
    minimal_product_sums = [2 * limit] * (limit + 1)
    generate_product_sum(1, 1, 1, 2, limit, minimal_product_sums)
    return sum(set(minimal_product_sums[2:]))


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer: {find_minimal_product_sum(11_999)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
