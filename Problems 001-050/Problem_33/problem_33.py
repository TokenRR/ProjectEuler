import time
from math import gcd


def find_non_trivial_fractions():
    """
    Find the non-trivial fractions where cancelling out the common digits
    results in a correct simplified fraction.
    """
    return [(n, d) for n in range(10, 100) for d in range(n+1, 100)
            if any([n % 10 == d // 10 and n * (d % 10) == (n // 10) * d,
                    n // 10 == d % 10 and n * (d // 10) == (n % 10) * d])]


if __name__ == "__main__":
    start_time = time.time()
    non_trivial_fractions = find_non_trivial_fractions()
    product = [1, 1]
    for n, d in non_trivial_fractions:
        product[0] *= n
        product[1] *= d
        print(f'Non-trivial fraction: {n}/{d}')
    common_divisor = gcd(*product)
    simplified = [x // common_divisor for x in product]
    print(f'Product of fractions (simplified): {simplified[0]}/{simplified[1]}')
    print(f'\nAnswer: {simplified[1]}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
