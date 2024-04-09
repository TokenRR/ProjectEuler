import time
import numpy as np
import heapq


def minimal_path_sum(matrix: np.ndarray) -> int:
    """
    Calculate the minimal path sum from the top left to the bottom right of the matrix,
    by moving up, down, left, or right.

    Args:
        matrix (np.ndarray): The matrix.

    Returns:
        int: The minimal path sum.
    """
    n = len(matrix)
    dist = np.full((n, n), np.inf)
    dist[0, 0] = matrix[0, 0]
    heap = [(dist[0, 0], 0, 0)]
    while heap:
        d, i, j = heapq.heappop(heap)
        if (i, j) == (n - 1, n - 1):
            return int(d)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                nd = d + matrix[ni, nj]
                if nd < dist[ni, nj]:
                    dist[ni, nj] = nd
                    heapq.heappush(heap, (nd, ni, nj))


if __name__ == "__main__":
    start_time = time.time()
    with open('Problem_83\\0083_matrix.txt', 'r') as file:
        matrix = np.loadtxt(file, delimiter=',')
    print(f"Answer = {minimal_path_sum(matrix)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
