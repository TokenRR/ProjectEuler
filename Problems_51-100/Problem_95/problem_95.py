import time


def calculate_D(num: int = 1_000_000) -> list:
    """
    Calculate D values for the problem.

    Args:
        num (int): The upper limit for the calculation.

    Returns:
        list: List of calculated D values.
    """
    D = [0] * num
    for i in range(1, len(D)):
        D[i * 2::i] = [x + i for x in D[i * 2::i]]
    return D


def find_longest_chain() -> int:
    """
    Find the smallest member of the longest amicable chain.

    Returns:
        int: The smallest member of the longest amicable chain.
    """
    D = calculate_D(1_000_000)
    longest = []
    for i in range(1, len(D)):
        n, chain = i, []
        while D[n] < len(D):
            D[n], n = len(D), D[n]
            try:
                k = chain.index(n)
            except ValueError:
                chain.append(n)
            else:
                longest = max(longest, chain[k:], key=len)
    return min(longest)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_longest_chain()}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
