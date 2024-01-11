import math
import time


def factorial_digit_sum(factorials):
    """
    Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    Note: 1! and 2! are not included as they are not sums.
    """
    upper_bound = 7 * factorials[9]
    curious_numbers = [num for num in range(10, upper_bound)
                       if num == sum(factorials[int(digit)] for digit in str(num))]
    return curious_numbers, sum(curious_numbers)


if __name__ == "__main__":
    start_time = time.time()
    factorials = [math.factorial(i) for i in range(10)]  #  Попередньо обчислити факторіали для цифр від 0 до 9
    numbers, total_sum = factorial_digit_sum(factorials)

    print(f'Curious numbers: {numbers}')
    print(f'\nAnswer = {total_sum}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')
