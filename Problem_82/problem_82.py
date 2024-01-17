import time
import numpy as np
import heapq


def minimal_path_sum(matrix: np.ndarray) -> int:
    """
    Calculate the minimal path sum from the left column to the right column of the matrix,
    by only moving up, down, or right.

    Args:
        matrix (np.ndarray): The matrix.

    Returns:
        int: The minimal path sum.
    """
    n = len(matrix)
    dist = np.full((n, n), np.inf)
    dist[:, 0] = matrix[:, 0]
    heap = [(dist[i, 0], i, 0) for i in range(n)]
    heapq.heapify(heap)
    while heap:
        d, i, j = heapq.heappop(heap)
        if j == n - 1:
            return int(d)
        for di, dj in [(0, 1), (-1, 0), (1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                nd = d + matrix[ni, nj]
                if nd < dist[ni, nj]:
                    dist[ni, nj] = nd
                    heapq.heappush(heap, (nd, ni, nj))


if __name__ == "__main__":
    start_time = time.time()
    with open('Problem_82\\0082_matrix.txt', 'r') as file:
        matrix = np.loadtxt(file, delimiter=',')
    print(f"Answer = {minimal_path_sum(matrix)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
