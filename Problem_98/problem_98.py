import time
import itertools
from typing import List, Tuple, Union


def is_square(n: int) -> bool:
    """
    Check if a number is a perfect square.

    Args:
        n (int): The number to check.

    Returns:
        bool:    True if the number is a perfect square, False otherwise.
    """
    return int(n**0.5)**2 == n


def get_square(word: str, letter_to_digit: dict) -> Union[int, bool]:
    """
    Get the square number corresponding to a word using a mapping of letters to digits.

    Args:
        word (str):             The word to convert to a square number.
        letter_to_digit (dict): A mapping of letters to digits.

    Returns:
        Union[int, bool]: The square number if it's a perfect square, False otherwise.
    """
    num = int(''.join(letter_to_digit[letter] for letter in word))
    return num if is_square(num) else False


def get_max_square(word_pairs: List[Tuple[str, str]]) -> int:
    """
    Find the maximum square number formed by anagrams in a list of word pairs.

    Args:
        word_pairs (List[Tuple[str, str]]): List of word pairs.

    Returns:
        int: The maximum square number formed by anagrams.
    """
    max_square = 0
    for word1, word2 in word_pairs:
        letter_set = {letter: str(index) for index, letter in enumerate(set(word1))}
        for digit_permutation in itertools.permutations('123456789', len(letter_set)):
            letter_to_digit = dict(zip(letter_set.keys(), digit_permutation))
            square1 = get_square(word1, letter_to_digit)
            square2 = get_square(word2, letter_to_digit)
            if square1 and square2:
                max_square = max(square1, square2, max_square)
    return max_square


def get_word_pairs(file_path: str) -> List[Tuple[str, str]]:
    """
    Read a file containing words and return a list of word pairs with the same set of letters.

    Args:
        file_path (str):       The path to the file containing words.

    Returns:
        List[Tuple[str, str]]: List of word pairs.
    """
    with open(file_path, 'r') as file:
        words = [(word[1:-1], sorted(word[1:-1])) 
            for word in file.read().split(',') if len(word) > 6]
    word_pairs = []
    while words:
        word, sorted_word = words.pop()
        word_pairs += [(word, other_word)
                       for other_word, other_sorted_word
                       in words
                       if sorted_word == other_sorted_word]
    return word_pairs


if __name__ == "__main__":
    start_time = time.time()
    word_pairs = get_word_pairs("Problem_98\\0098_words.txt")
    print(f"Answer = {get_max_square(word_pairs)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
