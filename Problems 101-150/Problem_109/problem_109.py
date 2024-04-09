import time
from typing import List


def calc_ways(ways: List[List[List[int]]], throws: int, total: int, max_index: int) -> int:
    """
    Calculate the number of ways to score 'total' points in 'throws' throws.
    
    Args:
        ways: A 3D list used for memoization.
        throws: The number of throws.
        total: The total score to achieve.
        max_index: The maximum index in the 'points' list that can be used.
    
    Returns:
        The number of ways to score 'total' points in 'throws' throws.
    """
    if ways[throws][total][max_index] is None:
        if throws == 0:
            ways[throws][total][max_index] = int(total == 0)
        else:
            ways[throws][total][max_index] = 0
            if max_index > 0:
                ways[throws][total][max_index] += calc_ways(ways, throws, total, max_index - 1)
            if points[max_index] <= total:
                ways[throws][total][max_index] += calc_ways(ways, throws - 1, total - points[max_index], max_index)
    return ways[throws][total][max_index]


def compute(points: List[int], double_points: List[int]) -> str:
    """
    Calculate the number of ways to checkout with a score less than 100.
    
    Args:
        points: A list of all possible scores that can be achieved with a single throw.
        double_points: A list of all possible scores that can be achieved with a double throw.
    
    Returns:
        The number of ways to checkout with a score less than 100 as a string.
    """
    return str(sum(calc_ways(ways, throws, remaining_points - p, len(points) - 1)
                   for remaining_points in range(1, 100)
                   for throws in range(3)
                   for p in double_points if p <= remaining_points))


if __name__ == "__main__":
    start_time = time.time()

    # All possible points that can be scored with one throw
    points = [i * j for i in range(1, 21) for j in range(1, 4)] + [25, 50]
    # Points that can be scored with a double thro
    double_points = [i * 2 for i in range(1, 21)] + [50]
    # Array for memoization
    ways = [[[None] * len(points) for _ in range(101)] for _ in range(3)]

    print(f"Answer = {compute(points, double_points)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
    