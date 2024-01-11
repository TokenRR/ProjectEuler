import time


def is_palindrome(num):
    """
    Check if a number is a palindrome
    """
    return str(num) == str(num)[::-1]


def sum_dual_base_palindromes(limit):
    """
    Calculate the sum of all numbers less than the limit that are palindromic in both base 10 and base 2
    """
    total_sum = 0
    for num in range(1, limit):
        if is_palindrome(num) and is_palindrome(bin(num)[2:]):
            total_sum += num
    return total_sum


if __name__ == "__main__":
    start_time = time.time()
    limit = 1000000
    result = sum_dual_base_palindromes(limit)
    print(f'Sum of dual-base palindromes: {result}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
