import time


def solve():
    final_sum = 0
    tmp = []
    for n in range(1, 10001):
        divide_a = []
        for i in range(1, int(n/2 +1)):
            if n % i ==0:
                divide_a.append(i)

        divide_b = []
        k = sum(divide_a)
        for i in range(1, int(k/2 +1)):
            if k % i ==0:
                divide_b.append(i)

        g = [n, k]
        g.sort()
        if n == sum(divide_b) and k == sum(divide_a) and n != k and g not in tmp:
            tmp.append(g)
            final_sum = final_sum + n + k
    
    return final_sum



if __name__ == "__main__":
    '''
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called 
    amicable numbers.
   
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    '''
    timer_start = time.time()

    print(f'\nResult = {solve()}')

    timer_stop = time.time()
    print(f'\nSpend time: {round(timer_stop-timer_start, 5)} seconds')
    