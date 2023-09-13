import time


def sum_squares(lst):
    '''1^2 + 2^2 +...+ 10^2 = 385'''
    return sum([i**2 for i in lst])

def square_sum(lst):
    '''(1 + 2 +...+10)^2 = 55^2 = 3025'''
    return (sum(lst))**2


if __name__ == "__main__":
    '''
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 +...+ 10^2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 +...+10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
    3025 - 385 = 2640

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    '''
    timer_start = time.time()

    TO = 100 # до якого натурального числа треба рахувати
    lst = [i for i in range(1, TO+1)]

    print(f'\nThe sum of the squares of 1 to 100 = {sum_squares(lst)}')
    print(f'The square of the sum of 1 to 100 = {square_sum(lst)}')
    print(f'\nDifference between them = {square_sum(lst) - sum_squares(lst)}')
    
    timer_stop = time.time()
    print(f'\nSpend time: {round(timer_stop-timer_start, 5)} seconds')
