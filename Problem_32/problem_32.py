import time


def find_pandigital_products():
    """
    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.
    """
    products = set()
    for i in range(2, 60):
        start = 1234 if i < 10 else 123
        for j in range(start, 10000//i):
            if ''.join(sorted(f"{i}{j}{i*j}")) == "123456789":
                products.add(i * j)
    return sum(products)


if __name__ == "__main__":
    start_time = time.time()
    total = find_pandigital_products()
    print(f'Answer = {total}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
