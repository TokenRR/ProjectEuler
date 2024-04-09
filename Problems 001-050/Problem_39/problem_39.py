import time
from collections import defaultdict


def count_right_triangle_solutions(perimeter_limit):
    """
    Count the number of solutions for each perimeter value up to the given limit
    """
    solution_count = defaultdict(int)
    for a in range(1, perimeter_limit // 3):
        for b in range(a, (perimeter_limit - a) // 2):
            c = (a**2 + b**2)**0.5
            if c.is_integer():
                p = a + b + int(c)
                if p <= perimeter_limit:
                    solution_count[p] += 1
    return max(solution_count, key=solution_count.get), max(solution_count.values())


if __name__ == "__main__":
    start_time = time.time()
    perimeter_limit = 1000
    p, max_solutions = count_right_triangle_solutions(perimeter_limit)
    print(f'Maximum number of solutions: {max_solutions}')
    print(f'\nAnswer = {p}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
