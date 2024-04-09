import time


def is_origin_inside_triangle(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> bool:
    """
    Check if the origin is inside a given triangle.

    Args:
        x1 (int): x-coordinate of the first vertex.
        y1 (int): y-coordinate of the first vertex.
        x2 (int): x-coordinate of the second vertex.
        y2 (int): y-coordinate of the second vertex.
        x3 (int): x-coordinate of the third vertex.
        y3 (int): y-coordinate of the third vertex.

    Returns:
        bool: True if the origin is inside the triangle, False otherwise.
    """
    def sign(x1, y1, x2, y2, x3, y3):
        return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)

    d1 = sign(0, 0, x1, y1, x2, y2)
    d2 = sign(0, 0, x2, y2, x3, y3)
    d3 = sign(0, 0, x3, y3, x1, y1)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)


def count_triangles_containing_origin(filename: str) -> int:
    """
    Count the number of triangles containing the origin from a file.

    Args:
        filename (str): The path to the file containing triangle coordinates.

    Returns:
        int: The count of triangles containing the origin.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    count = 0

    for line in lines:
        coordinates = list(map(int, line.strip().split(',')))
        x1, y1, x2, y2, x3, y3 = coordinates

        if is_origin_inside_triangle(x1, y1, x2, y2, x3, y3):
            count += 1

    return count


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {count_triangles_containing_origin('Problem_102/0102_triangles.txt')}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
