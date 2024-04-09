import time


def fac(n):
    '''Factorization: 1319 -> [5, 7, 13, 29]'''
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n /= i
        i += 1
    primfac.append(int(n))
    return primfac


if __name__ == "__main__":
    '''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001`st prime number?
    '''
    timer_start = time.time()

    prime_lst = []
    number = 2
    while len(prime_lst) < 10001:
        if len(fac(number)) == 1 and number not in prime_lst:
            prime_lst.append(number)
        number += 1
    
    timer_stop = time.time()
    print(f'\nSpend time: {round(timer_stop-timer_start, 5)} seconds')
    print(f'Result: {prime_lst[-1]}')