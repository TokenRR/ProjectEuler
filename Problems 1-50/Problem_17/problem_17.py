import time


def solve(word_d,n):
    '9 -> `nine` -> 4 || 63 -> `sixtythree` -> 10 || 104 -> `onehundredandfour` -> 17'
    n = str(n)
    word = ''
    if len(n) == 2 and n[0] != '1':
        tmp_n = int(n[0]) * 10  # for ex, n=63 -> tmp_n = 60
        word = word_d.get(int(tmp_n)) + word_d.get(int(n[1]))
    elif len(n) == 3 and int(n) not in word_d:
        if n[1] == '0' or n[1] == '1':
            tmp_n = int(n[0]) * 100 # for ex, n=342 -> tmp_n = 300
            word = word_d.get(int(tmp_n)) + 'and' + word_d.get(int(n[1]+n[2]))
        else:
            tmp_n = int(n[0]) * 100 # for ex, n=342 -> tmp_n = 300
            tmp_n2 = int(n[1]) * 10 # for ex, n=342 -> tmp_n = 40
            word = word_d.get(int(tmp_n)) + 'and' + word_d.get(int(tmp_n2)) + word_d.get(int(n[2]))
    else: word = word_d.get(int(n))
    return len(word)


if __name__ == "__main__":
    '''
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
    there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
    words, how many letters would be used?

    Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
    contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
    The use of "and" when writing out numbers is in compliance with British usage.
    '''
    OF = 0  # need for range from task
    TO = 1000  # need for range from task
    acc = 0  # accumulator
    word_dict ={0:'',
                1:'one',
                2:'two',
                3:'three',
                4:'four',
                5:'five',
                6:'six',
                7:'seven',
                8:'eight',
                9:'nine',
                10:'ten',
                11:'eleven',
                12:'twelve',
                13:'thirteen',
                14:'fourteen',
                15:'fifteen',
                16:'sixteen',
                17:'seventeen',
                18:'eighteen',
                19:'nineteen',
                20:'twenty',
                30:'thirty',
                40:'forty',
                50:'fifty',
                60:'sixty',
                70:'seventy',
                80:'eighty',
                90:'ninety',
                100:'onehundred',
                200:'twohundred',
                300:'threehundred',
                400:'fourhundred',
                500:'fivehundred',
                600:'sixhundred',
                700:'sevenhundred',
                800:'eighthundred',
                900:'ninehundred',
                1000:'onethousand'}
    timer_start = time.time()

    for n in range(OF, TO+1):
        acc += solve(word_dict, n)

    timer_stop = time.time()
    print(f'\nSpend time: {round(timer_stop-timer_start, 5)} seconds')
    print(f'\nResult = {acc}')
    