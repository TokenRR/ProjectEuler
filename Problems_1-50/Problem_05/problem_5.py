import time


def divide(of, to):
    '''The function of finding the smallest number by the brute force method'''
    n, i = 1, 0
    lst = [i for i in range(of, to+1)]

    while lst[i] != to:
        if n % lst[i] == 0:
            i += 1
        else: 
            n += 1
            i = 0
    return n


if __name__ == "__main__":
    '''
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    '''
    timer_start = time.time()

    print(f'\nResult = {divide(1, 20)} - The smallest number what divide by all of the nubers from 1 to 20')

    timer_stop = time.time()
    print(f'\nSpend time: {round(timer_stop-timer_start, 5)} seconds')
    # expected execution time = 115 seconds