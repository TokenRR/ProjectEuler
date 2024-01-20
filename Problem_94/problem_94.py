import time


def find_triangles(limit: int) -> int:
    """
    Find the sum of perimeters of triangles with integral side lengths and integral area
    that have one side with a length of 'x-1' and another with a length of 'x+1',
    where 'x' is a whole number representing the integral side length, and is less than the given limit.

    This function utilizes Diophantine equations to find integral solutions for triangles.
    
    The Diophantine equations used for triangles with side lengths (x, x, x-1) and (x, x, x+1) are derived from
    the geometric condition that the area of a triangle can be expressed as A = 0.5 * base * height.

    In this case, the base and height correspond to the side lengths of the triangle.
    For triangles with side lengths (x, x, x-1):
    -3a^2 - 2a + 4c^2 + 1 = 0

    For triangles with side lengths (x, x, x+1):
    -3a^2 + 2a + 4c^2 + 1 = 0

    Here, 'a' and 'c' are integers representing the side lengths of the triangle.

    Args:
        limit (int): The upper limit for the whole number representing the side length 'x'.

    Returns:
        int: The sum of perimeters of qualifying triangles.
    """
    total_sum = 0

    # Triangle type: (x, x, x-1)
    a = 1
    c = 1
    while 3 * a - 1 < limit:
        a_temp = a
        a = 7 * a - 8 * c + 2
        c = -6 * a_temp + 7 * c - 2
        area = (0.5 * (a - 1) * c) / 2
        if area == int(area) and 3 * a - 1 < limit:
            total_sum += 3 * a - 1

    # Triangle type: (x, x, x+1)
    a = 1
    c = 0
    while 3 * a - 1 < limit:
        a_temp = a
        a = 7 * a - 8 * c - 2
        c = -6 * a_temp + 7 * c + 2
        area = (0.5 * (a + 1) * c) / 2
        if area == int(area) and 3 * a + 1 < limit:
            total_sum += 3 * a + 1

    # This corrects for the first solution which PE considers degenerate
    return total_sum - 2


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {find_triangles(1_000_000_000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
    