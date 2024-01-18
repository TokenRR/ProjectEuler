import time


def closest_rectangles(target: int) -> int:
    """
    Find the area of the rectangle with the closest number of rectangles to the target.

    Args:
        target (int): The target number of rectangles.

    Returns:
        int: The area of the rectangle with the closest number of rectangles to the target.
    """
    closest_area = 0
    closest_difference = target

    for width in range(1, 100):
        for height in range(1, 100):
            rectangles = width * (width + 1) * height * (height + 1) // 4

            if abs(target - rectangles) < closest_difference:
                closest_difference = abs(target - rectangles)
                closest_area = width * height

            if rectangles > target:
                break

    return closest_area


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {closest_rectangles(2_000_000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
