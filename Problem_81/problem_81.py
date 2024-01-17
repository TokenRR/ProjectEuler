import time
import numpy as np


def minimal_path_sum(matrix: np.ndarray) -> int:
    """
    Calculate the minimal path sum from the top left to the bottom right of the matrix, by only moving right and down.

    Args:
        matrix (np.ndarray): The matrix.

    Returns:
        int: The minimal path sum.
    """
    n = len(matrix)
    dist = np.full((n, n), np.inf)
    dist[0, 0] = matrix[0, 0]
    for _ in range(2*n - 1):
        for i in range(n):
            for j in range(n):
                if i > 0:
                    dist[i, j] = min(dist[i, j], dist[i-1, j] + matrix[i, j])
                if j > 0:
                    dist[i, j] = min(dist[i, j], dist[i, j-1] + matrix[i, j])
    return int(dist[-1, -1])


if __name__ == "__main__":
    start_time = time.time()
    with open('Problem_81\\0081_matrix.txt', 'r') as file:
        matrix = np.loadtxt(file, delimiter=',')
    print(f"Answer = {minimal_path_sum(matrix)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
