import time


if __name__ == "__main__":
    '''
    A palindromic number reads the same both ways. 
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    '''
    # Оскільки мін число - 100, а макс - 999, можемо зробити висновок, що наш поліндром буде мати або 5, або 6 символів.
    # За умовою задачі нам необхідно знайти "набільший поліндром" - поліндром із 5-ти символьного числа можна не шукати

    timer_start = time.time()

    max_val = 0 # Максимальне значення поліндрому
    first = 0 # Перший множник поліндрому
    second = 0 # Другий множник поліндрому

    for i in range(100, 1000):
        for j in range(100, 1000):
            tmp = list(str(i*j))

            if len(tmp) == 6:
                if tmp[0] == tmp[-1] and tmp[1] == tmp[-2] and tmp[2] == tmp[-3]:
                    if i*j > max_val:
                        max_val = i*j
                        first = i
                        second = j
    print(f'Result: {first} * {second} = {max_val}')

    timer_stop = time.time()
    print(f'Spend time: {round(timer_stop-timer_start, 5)} seconds')