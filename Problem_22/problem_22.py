import time


def reading():
    'Function which reading file'
    file = open('problem_22.txt', 'r')
    names = list(file)
    names = str(names[0])
    names = names.replace('"', '')
    names = names.split(',')
    names.sort()
    return names

def score(name, lst, alp):
    '''
    Function which counting index + name score
    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
    is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
    '''
    
    acc = 0
    for l in name:
        l = l.lower()
        acc += alp.get(l)
    acc *= lst.index(name) +1  # names in list aren't repeat !
    return acc


if __name__ == "__main__":
    '''
    Using problem_22.txt, a 46K text file containing over five-thousand 
    first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each 
    name, multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
    is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

    What is the total of all the name scores in the file?
    '''
    ALPHABET = {'a':1,
                'b':2,
                'c':3,
                'd':4,
                'e':5,
                'f':6,
                'g':7,
                'h':8,
                'i':9,
                'j':10,
                'k':11,
                'l':12,
                'm':13,
                'n':14,
                'o':15,
                'p':16,
                'q':17,
                'r':18,
                's':19,
                't':20,
                'u':21,
                'v':22,
                'w':23,
                'x':24,
                'y':25,
                'z':26}
    result = 0
    timer_start = time.time()

    names = reading()  # list with all sorted names
    for name in names:
        result += score(name, names, ALPHABET)

    timer_stop = time.time()
    print(f'\nSpend time: {round(timer_stop-timer_start, 5)} seconds')
    print(f'\nResult = {result}')
    