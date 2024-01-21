import time


def read_sudoku(file: str) -> list:
    """
    Read a Sudoku puzzle from a file.

    Args:
        file (str): The path to the file containing the Sudoku puzzle.

    Returns:
        list:       A list of 9x9 Sudoku grids.
    """
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    grids = []
    for i in range(0, len(lines), 10):
        grid = [list(line) for line in lines[i + 1:i + 10]]
        grids.append(grid)
    return grids


def next_cell(mi: int, mj: int) -> tuple:
    """
    Get the coordinates of the next cell in the Sudoku grid.

    Args:
        mi (int): The current row index.
        mj (int): The current column index.

    Returns:
        tuple:    The coordinates (row, column) of the next cell.
    """
    n = 9
    if mj != n - 1:
        return mi, mj + 1
    elif mi != n - 1:
        return mi + 1, 0
    else:
        return -1, -1


def can_place(grid: list, mi: int, mj: int, num: int) -> bool:
    """
    Check if a number can be placed in a specific cell of the Sudoku grid.

    Args:
        grid (list): The Sudoku grid.
        mi (int):    The row index.
        mj (int):    The column index.
        num (int):   The number to be placed.

    Returns:
        bool:        True if the number can be placed, False otherwise.
    """
    n = 9
    for i in range(n):
        if grid[mi][i] == str(num):
            return False
        if grid[i][mj] == str(num):
            return False
    ni = (mi // 3) * 3
    nj = (mj // 3) * 3
    for i in range(ni, ni + 3):
        for j in range(nj, nj + 3):
            if grid[i][j] == str(num):
                return False
    return True


def solve(grid: list, mi: int, mj: int) -> bool:
    """
    Solve the Sudoku puzzle using a backtracking algorithm.

    Args:
        grid (list): The Sudoku grid.
        mi (int):    The current row index.
        mj (int):    The current column index.

    Returns:
        bool:        True if the puzzle is solved, False otherwise.
    """
    if mi == -1 and mj == -1:
        return True
    nxt = next_cell(mi, mj)
    if grid[mi][mj] != '0':
        return solve(grid, *nxt)
    else:
        for i in range(1, 10):
            if can_place(grid, mi, mj, i):
                grid[mi][mj] = str(i)
                if solve(grid, *nxt):
                    return True
                grid[mi][mj] = '0'
        return False


if __name__ == "__main__":
    start_time = time.time()
    grids: list = read_sudoku('Problem_96\\p096_sudoku.txt')
    total_sum: int = sum(int(''.join(grid[0][:3]))
                         for grid in grids
                         if solve(grid, 0, 0))
    print(f"Answer = {total_sum}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
