import time
from fractions import Fraction


def generate_e_terms(n: int) -> list:
    """
    Generate the first n terms of the sequence for the continued fraction of e.

    Args:
        n (int): The number of terms to generate.

    Returns:
        list: The first n terms of the sequence for e.
    """
    e_terms = [2]
    k = 1
    while len(e_terms) < n:
        e_terms.extend([1, 2 * k, 1])
        k += 1
    return e_terms[:n]


def compute_convergent(n: int, e_terms: list) -> Fraction:
    """
    Compute the nth convergent for the continued fraction of e.

    Args:
        n (int): The index of the convergent to compute.
        e_terms (list): The sequence of terms for the continued fraction of e.

    Returns:
        Fraction: The nth convergent as a Fraction object.
    """
    convergent = Fraction(e_terms[n - 1])
    for i in range(n - 2, -1, -1):
        convergent = e_terms[i] + Fraction(1, convergent)
    return convergent


def sum_of_digits(number: Fraction) -> int:
    """
    Calculate the sum of digits in the numerator of a Fraction.

    Args:
        number (Fraction): The Fraction to calculate the sum of digits for.

    Returns:
        int: The sum of digits in the numerator.
    """
    return sum(int(digit) for digit in str(number.numerator))


if __name__ == "__main__":
    start_time = time.time()
    
    # Finding the 100th convergent
    n = 100
    e_terms = generate_e_terms(n)
    convergent_100 = compute_convergent(n, e_terms)

    print(f"Answer = {sum_of_digits(convergent_100)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
