from itertools import chain, combinations
import time


def td(n):
    'Triangle digit'
    triangular = 0
    while n > 0:
        triangular += n
        n -= 1
    return triangular

def fac(n):
    'Factorization'
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n /= i
        i += 1
    primfac.append(int(n))
    return primfac

def pairs(i):  # We create unique pairs of numbers
    'pairs([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)'
    lst = list(i)
    return chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1))

def mult(i):  # Multiply all numbers in the iterable and return result
    '(2,2,7) --> 28'
    rv = 1
    for k in i:
        rv = rv * k
    return rv


if __name__ == '__main__':
    '''
    Крок 1. Знаходимо трикутне число
    Крок 2. Факторизуємо трикутне число
    Крок 3. Знаходимо всі дільники
    Крок 4. Повторюємо до тих пір поки не знайдемо число, яке матиме 500 дільників

    Доцільно використовувати пошук дільників починаючи з числа number^2

    Кращий час пошуку числа, яке має більше 500 дільників складає 0.012 секунди (number = 12375)
    Стандартний час пошуку числа, яке має більше 500 дільників складає 7.72824 секунди (number = 2)
    '''

    number = 2  # the number from which we start looking for triangular numbers
    need_div = 500  # what number of divisors we are looking for
    result = [1, ]
    timer_start = time.time()

    while len(result) <= need_div:
        triangular = td(number)
        k = pairs(fac(triangular))

        # Filter out anything from k thats shorter then 2
        # Add to list divisors after multiplicate
        for x in k:
            if len(x) > 1 and mult(x) not in result:
                result.append(mult(x))
        # result.extend(map(mult, (x for x in k if len(x)>1)))
    
        # Add the divisors that we got after factoring the number
        for x in fac(triangular):
            if x not in result:
                result.append(x)

        if len(result) <= need_div:
            result = [1, ]
        number += 1

    result.sort()
    print(f'\nFrom the number {number-1} we have triangular digit - {triangular}')
    print(f'\n{triangular} have {len(result)} divisors')
    # print(f'\nAll divisors is {result}')
    timer_stop = time.time()

    print(f'Time spent: {round(timer_stop-timer_start, 5)} sec')