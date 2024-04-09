import time


def is_triangle_number(number):
    """
    Check if the number is triangular
    """
    n = (-1 + (1 + 8 * number)**0.5) / 2
    return n.is_integer()


def word_value(word):
    """
    Calculate the value of the word
    """
    return sum(ord(char) - 64 for char in word.strip('"'))


if __name__ == "__main__":
    start_time = time.time()
    # Reading words from a file
    with open('Problem_42\\0042_words.txt', 'r') as file:
        words = file.read().split(',')

    # Count the number of triangular words
    triangle_words_count = sum(1 for word in words if is_triangle_number(word_value(word)))
    print(f'Answer = {triangle_words_count}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
