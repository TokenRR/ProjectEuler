import time


def is_pandigital(num):
    """
    Check if a number is 1 to 9 pandigital
    """
    return len(num) == 9 and not '0' in num and len(set(num)) == 9


def largest_pandigital_multiple():
    """
    Find the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2,...,n) where n > 1
    """
    largest_pandigital = '0'
    for i in range(1, 10000):  # The number must be less than 5 digits
        concatenated_product = ''
        for n in range(1, 10):  # n will not be more than 9
            concatenated_product += str(i * n)
            if len(concatenated_product) > 9:
                break
            if is_pandigital(concatenated_product) and concatenated_product > largest_pandigital:
                largest_pandigital = concatenated_product
    return largest_pandigital


if __name__ == "__main__":
    start_time = time.time()
    result = largest_pandigital_multiple()
    print(f'Largest pandigital multiple: {result}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')



"""
# ----------------------------------------------------------
                    SECOND ATTEMPT
# ----------------------------------------------------------
import time


def largest_pandigital_multiple():
    is_pandigital = lambda x: len(x) == 9 and len(set(x)) == 9 and '0' not in x
    return max(''.join(str(i*n) for n in range(1, 10))[:9] 
               for i in range(1, 10000) if is_pandigital(''.join(str(i*n) for n in range(1, 10))[:9]))

               
if __name__ == "__main__":
    start_time = time.time()
    print(f'Largest pandigital multiple: {largest_pandigital_multiple()}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
"""