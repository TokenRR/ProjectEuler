import time


def count_ways(n: int) -> int:
    """
    Count the number of ways n can be written as a sum of at least two positive integers
    """
    ways = [1] + [0] * n
    for num in range(1, n):
        for i in range(num, n + 1):
            ways[i] += ways[i - num]
    return ways[n]


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {count_ways(100)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
