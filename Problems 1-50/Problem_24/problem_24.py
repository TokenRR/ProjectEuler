import itertools
import time


def lexicographic_permutations(digits):
    """
    This function generates all lexicographic permutations of a given set of digits.
    It returns a list of permutations.
    """
    return [''.join(p) for p in itertools.permutations(digits)]


def main():
    """
    This is the main function that calculates the millionth lexicographic permutation
    of the digits 0 through 9.
    """
    start_time = time.time()

    digits = '0123456789'
    permutations = lexicographic_permutations(digits)
    millionth_permutation = permutations[10**6 - 1]

    print(millionth_permutation)

    end_time = time.time()
    print(f'Execution time: {round(end_time - start_time, 2)} seconds')


if __name__ == '__main__':
    main()
