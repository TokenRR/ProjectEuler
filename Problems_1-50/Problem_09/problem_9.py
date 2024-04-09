import time


def first():
    '''The first method of solving the problem'''
    # Брутфорс - не найкращий варіант, але генерувати трійки Піфагора впадло
    # Умова a < b < c - дає лише додатні a, b, c
    sq = [i**2 for i in range(1, 1000 + 1)]

    def f(lst):
        res = []
        for a in lst:
            for b in lst:
                for c in lst:
                    if a + b == c and a**0.5 + b**0.5 + c**0.5 == 1000:
                        res.append([int(a**0.5), int(b**0.5), int(c**0.5)])
                        res = res[0]
                        return res, int(a**0.5) * int(b**0.5) * int(c**0.5)
    print(f(sq))

def second():
    '''The second method of solving the problem'''
    lst = []
    MAX = 1000

    def pt(lst, MAX):
        # pt - Pythagorean triple (Пифагорова трійка)
        for n in range(1, int((MAX+1)**0.5)+1):
            for m in range(n+1, MAX+1, 2):
                for k in range(1, MAX+1):
                    c = k * (m*m + n*n)
                    if c > MAX: break
                    b = k * 2 * m * n
                    a = k * (m*m - n*n)
                    lst.append([a, b, c])
                    
    def f(lst):
        for i in lst: 
            if sum(i) == 1000: return i, i[0] * i[1] * i[2]

    pt(lst, MAX)
    print(f'Відповідь {f(lst)}')
    print(f'\nУсього Піфагорових трійок {len(lst)}\n')


if __name__ == "__main__":
    '''
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 5^2  |  9 + 16 = 25
    There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
    '''
    timer_start = time.time()

    # first() 

    second()
    
    timer_stop = time.time()
    print(f'Spend time: {round(timer_stop-timer_start, 5)} seconds')