import time


def str_to_matrix(str, i):
    'The function of creating a list from a string'
    lst = []
    tmp = list(str.split(':'))
    for line in tmp:
        line = line.split(' ')
        for el in line:
            line[i] = int(el)
            i+=1
        lst.append(line)
        i=0
    tmp.clear()  # may be better delete than cleaned
    return lst

def horizontal(grid, answers):
    'The function passes the grid horizontally and finds the maximum product of 4 adjacent elements'
    """
    1 1 1 1 0 0   ->    0 1 1 1 1 0   ->   ...   ->    0 0 0 0 0 0
    0 0 0 0 0 0   ->    0 0 0 0 0 0   ->   ...   ->    0 0 0 0 0 0
    0 0 0 0 0 0   ->    0 0 0 0 0 0   ->   ...   ->    0 0 0 0 0 0
    0 0 0 0 0 0   ->    0 0 0 0 0 0   ->   ...   ->    0 0 0 0 0 0
    0 0 0 0 0 0   ->    0 0 0 0 0 0   ->   ...   ->    0 0 0 0 0 0
    0 0 0 0 0 0   ->    0 0 0 0 0 0   ->   ...   ->    0 0 1 1 1 1      """

    MAX = 1
    tmp = []
    for i in grid[:-3:]: # Пошук найбільшого добутку сусідніх чотирьох цифр по горизонталі
        for j in range(0, len(grid)-3):
            if  MAX < i[j] * i[j+1] * i[j+2] * i[j+3]:
                MAX = i[j] * i[j+1] * i[j+2] * i[j+3]
                mult = [ i[j], i[j+1], i[j+2], i[j+3] ]
    tmp.extend([MAX, mult])

    answers.append(tmp)
    return answers

def vertical(grid, answers):
    'The function passes the grid vertically and finds the maximum product of 4 adjacent elements'
    """
    1 0 0 0 0 0   ->    0 0 0 0 0 0   ->   ...   ->    0 0 0 0 0 0
    1 0 0 0 0 0   ->    1 0 0 0 0 0   ->   ...   ->    0 0 0 0 0 0
    1 0 0 0 0 0   ->    1 0 0 0 0 0   ->   ...   ->    0 0 0 0 0 1
    1 0 0 0 0 0   ->    1 0 0 0 0 0   ->   ...   ->    0 0 0 0 0 1
    0 0 0 0 0 0   ->    1 0 0 0 0 0   ->   ...   ->    0 0 0 0 0 1
    0 0 0 0 0 0   ->    0 0 0 0 0 0   ->   ...   ->    0 0 0 0 0 1      """
    
    MAX = 1
    v = 0
    tmp = []
    while v < len(grid[0]): # Пошук найбільшого добутку сусідніх чотирьох цифр по вертикалі
        x = [x[v] for x in grid]
        for j in range(0, len(x)-3):
            if  MAX < x[j] * x[j+1] * x[j+2] * x[j+3]:
                MAX = x[j] * x[j+1] * x[j+2] * x[j+3]
                mult = [x[j], x[j+1], x[j+2], x[j+3]]
        v+=1
    
    tmp.append(MAX)
    tmp.append(mult)
    answers.append(tmp)
    return answers

def diagonal(grid, answers):
    'The function passes the grid in the direction of the main diagonal and finds the maximum product of 4 adjacent elements'

    MAX = 1
    tmp = []
    """
    * 1 0 0 0 0   ->    * 0 0 0 0 0   ->   ...   ->    * 0 1 0 0 0
    0 * 1 0 0 0   ->    0 * 1 0 0 0   ->   ...   ->    0 * 0 1 0 0
    0 0 * 1 0 0   ->    0 0 * 1 0 0   ->   ...   ->    0 0 * 0 1 0
    0 0 0 * 1 0   ->    0 0 0 * 1 0   ->   ...   ->    0 0 0 * 0 1    -> for elements above the main diagonal
    0 0 0 0 * 0   ->    0 0 0 0 * 1   ->   ...   ->    0 0 0 0 * 0       * - main diagonal
    0 0 0 0 0 *   ->    0 0 0 0 0 *   ->   ...   ->    0 0 0 0 0 *                                           """
    
    for j in range(0, len(grid[0])):  # Головна діагональ + елементи над нею
        i=0
        while i < len(grid)-j-3:
            # print([ grid[i][i+j], grid[i+1][i+j+1], grid[i+2][i+j+2] , grid[i+3][i+j+3] ])
            if  MAX < grid[i][i+j] * grid[i+1][i+j+1] * grid[i+2][i+j+2] * grid[i+3][i+j+3]:
                MAX = grid[i][i+j] * grid[i+1][i+j+1] * grid[i+2][i+j+2] * grid[i+3][i+j+3]
                mult = [ grid[i][i+j], grid[i+1][i+j+1], grid[i+2][i+j+2] , grid[i+3][i+j+3] ]
            i += 1

    """
    * 0 0 0 0 0   ->    * 0 0 0 0 0   ->   ...   ->    * 0 0 0 0 0
    1 * 0 0 0 0   ->    0 * 0 0 0 0   ->   ...   ->    0 * 0 0 0 0
    0 1 * 0 0 0   ->    0 1 * 0 0 0   ->   ...   ->    1 0 * 0 0 0
    0 0 1 * 0 0   ->    0 0 1 * 0 0   ->   ...   ->    0 1 0 * 0 0    -> for elements under the main diagonal
    0 0 0 1 * 0   ->    0 0 0 1 * 0   ->   ...   ->    0 0 1 0 * 0       * - main diagonal
    0 0 0 0 0 *   ->    0 0 0 0 1 *   ->   ...   ->    0 0 0 1 0 *                                           """

    for j in range(0, len(grid[0])):  # Головна діагональ + елементи під нею
        i=0
        while i < len(grid)-j-3:
            # print([ grid[i+j][i], grid[i+j+1][i+1], grid[i+j+2][i+2] , grid[i+j+3][i+3] ])
            if  MAX < grid[i+j][i] * grid[i+j+1][i+1] * grid[i+j+2][i+2] * grid[i+j+3][i+3]:
                MAX = grid[i+j][i] * grid[i+j+1][i+1] * grid[i+j+2][i+2] * grid[i+j+3][i+3]
                mult = [ grid[i+j][i], grid[i+j+1][i+1], grid[i+j+2][i+2] , grid[i+j+3][i+3] ]
            i += 1
    
    tmp.append(MAX)
    tmp.append(mult)
    answers.append(tmp)
    return answers

def reverse_diagonal(grid, answers):
    'The function passes the grid in the opposite direction to the main diagonal and finds the maximum product of 4 adjacent elements'

    MAX = 1
    tmp = []

    """
    0 0 0 0 0 *   ->    0 0 0 0 1 *   ->   ...   ->    0 0 0 1 0 *
    0 0 0 1 * 0   ->    0 0 0 1 * 0   ->   ...   ->    0 0 1 0 * 0
    0 0 1 * 0 0   ->    0 0 1 * 0 0   ->   ...   ->    0 1 0 * 0 0
    0 1 * 0 0 0   ->    0 1 * 0 0 0   ->   ...   ->    1 0 * 0 0 0    -> for elements above the main diagonal
    1 * 0 0 0 0   ->    0 * 0 0 0 0   ->   ...   ->    0 * 0 0 0 0       * - reverse diagonal
    * 0 0 0 0 0   ->    * 0 0 0 0 0   ->   ...   ->    * 0 0 0 0 0                                           """

    for j in range(1, len(grid[0])):  # reverse діагональ + елементи над нею
        i=0
        while i < len(grid)-j-2:
            # print([ grid[i][-j-i], grid[i+1][-j-i-1], grid[i+2][-j-i-2], grid[i+3][-j-i-3] ])
            if  MAX < grid[i][-j-i] * grid[i+1][-j-i-1] * grid[i+2][-j-i-2] * grid[i+3][-j-i-3]:
                MAX = grid[i][-j-i] * grid[i+1][-j-i-1] * grid[i+2][-j-i-2] * grid[i+3][-j-i-3]
                mult = [ grid[i][-j-i], grid[i+1][-j-i-1], grid[i+2][-j-i-2], grid[i+3][-j-i-3] ]
            i += 1

    """
    0 0 0 0 0 *   ->    0 0 0 0 0 *   ->   ...   ->    0 0 0 0 0 *
    0 0 0 0 * 0   ->    0 0 0 0 * 1   ->   ...   ->    0 0 0 0 * 0
    0 0 0 * 1 0   ->    0 0 0 * 1 0   ->   ...   ->    0 0 0 * 0 1
    0 0 * 1 0 0   ->    0 0 * 1 0 0   ->   ...   ->    0 0 * 0 1 0    -> for elements above the main diagonal
    0 * 1 0 0 0   ->    0 * 1 0 0 0   ->   ...   ->    0 * 0 1 0 0       * - reverse diagonal
    * 1 0 0 0 0   ->    * 0 0 0 0 0   ->   ...   ->    * 0 1 0 0 0                                           """

    for j in range(0, len(grid[0])):  # reverse діагональ + елементи під нею
        i=0
        while i < len(grid)-j-3:
            # print([ grid[-i-1][j+i], grid[-i-2][j+i+1], grid[-i-3][j+i+2], grid[-i-4][j+i+3] ])
            if  MAX < grid[-i-1][j+i] * grid[-i-2][j+i+1] * grid[-i-3][j+i+2] * grid[-i-4][j+i+3]:
                MAX = grid[-i-1][j+i] * grid[-i-2][j+i+1] * grid[-i-3][j+i+2] * grid[-i-4][j+i+3]
                mult = [ grid[-i-1][j+i], grid[-i-2][j+i+1], grid[-i-3][j+i+2], grid[-i-4][j+i+3] ]
            i += 1
    
    tmp.append(MAX)
    tmp.append(mult)
    answers.append(tmp)
    return answers

def solve():
    'The function of starting the search for the largest product of 4 adjacent numbers'
    grid = str_to_matrix(value, i=0)
    answers = []

    horizontal(grid, answers)
    vertical(grid, answers)
    diagonal(grid, answers)
    reverse_diagonal(grid, answers)
    for i in range(0, 4):
        MAX = answers[0][0]
        if  MAX < answers[i][0]:
            MAX = answers[i][0]
            mult = answers[i][1]
    print(f'Max = {MAX}')
    print(f'Mult = {mult}')


if __name__ == "__main__":
    '''
    In the 20x20 grid below, four numbers along a diagonal line have been marked in red.

    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

    The product of these numbers is 26 x 63 x 78 x 14 = 1788696.
    What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20x20 grid?
    '''

    value = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08:
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00:
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65:
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91:
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80:
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50:
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70:
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21:
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72:
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95:
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92:
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57:
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58:
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40:
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66:
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69:
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36:
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16:
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54:
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

    timer_start = time.time()

    solve()

    timer_stop = time.time()
    print(f'\nSpend time: {round(timer_stop-timer_start, 5)} seconds')
