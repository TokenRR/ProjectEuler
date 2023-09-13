import time


def sim_div(n):  
    'func create a simple divide'
    suma = 0
    for r in range(2, n):
        for c in range(2, int(r**0.5)+1):
            if r % c == 0: break
        else: suma += r
    return suma


if __name__ == "__main__":
    '''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    '''
    tm = 2000000  # digit from task
    timer_start = time.time()

    sim_div(tm)
    print(f'The sum = {sim_div(tm)}')
    
    timer_stop = time.time()
    print(f'\nSpend time: {round(timer_stop-timer_start, 5)} seconds')
