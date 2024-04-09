import math
import time


def solve():
    'Find factorial and count digit in the number'
    acc = 0
    number = str(math.factorial(100))
    for i in number:
        acc += int(i)
    return acc


if __name__ == "__main__":
    '''
    n! means n x (n - 1) x ... x 3 x 2 x 1

    For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    '''
    timer_start = time.time()

    print(f'\nResult = {solve()}')

    timer_stop = time.time()
    print(f'\nSpend time: {round(timer_stop-timer_start, 5)} seconds')