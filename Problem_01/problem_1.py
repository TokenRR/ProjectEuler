import time


if __name__ == "__main__":
    '''
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    '''
    timer_start = time.time()

    start, result = 0, 0
    while start < 1000:
        if start % 3 == 0 or start % 5 == 0: 
            result += start
        start += 1
    
    timer_stop = time.time()
    print(f'\nSpend time: {round(timer_stop-timer_start, 5)} seconds')
    print(f'Result: {result}')