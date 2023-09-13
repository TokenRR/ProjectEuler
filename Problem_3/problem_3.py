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
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    '''
    timer_start = time.time()

    NUMBER = 600851475143  # number from task
    print(f'Result = {max(fac(NUMBER))}')

    timer_stop = time.time()
    print(f'Spend time: {round(timer_stop-timer_start, 5)} seconds')