import time


def generate_triangle(n):
    """
    Generate the nth triangle number.
    
    Parameters:
    n (int): The order of the triangle number to generate.
    
    Returns:
    int: The nth triangle number.
    """
    return n * (n + 1) // 2


def generate_pentagonal(n):
    """
    Generate the nth pentagonal number.
    
    Parameters:
    n (int): The order of the pentagonal number to generate.
    
    Returns:
    int: The nth pentagonal number.
    """
    return n * (3 * n - 1) // 2


def is_pentagonal(number):
    """
    Check if a number is pentagonal.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is pentagonal, False otherwise.
    """
    n = (1 + (1 + 24 * number)**0.5) / 6
    return n.is_integer()


def generate_hexagonal(n):
    """
    Generate the nth hexagonal number.
    
    Parameters:
    n (int): The order of the hexagonal number to generate.
    
    Returns:
    int: The nth hexagonal number.
    """
    return n * (2 * n - 1)


def is_hexagonal(number):
    """
    Check if a number is hexagonal.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is hexagonal, False otherwise.
    """
    n = (1 + (1 + 8 * number)**0.5) / 4
    return n.is_integer()


def find_next_tri_penta_hexa():
    """
    Find the next number that is triangle, pentagonal, and hexagonal.
    
    Returns:
    int: The next number that is triangle, pentagonal, and hexagonal.
    """
    n = 286  # Start searching from the next number after 285
    while True:
        triangle = generate_triangle(n)
        if is_pentagonal(triangle) and is_hexagonal(triangle):
            return triangle
        n += 1


if __name__ == "__main__":
    start_time = time.time()
    result = find_next_tri_penta_hexa()
    print(f'Answer = {result}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
