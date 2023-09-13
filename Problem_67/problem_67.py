import time


def show(matrix):
    for row in matrix:
        print(row)
    print()

def solve(triangle):
    for row in range(len(triangle)-1):
        for el in range(row+1):
            if row > 0:
                if el == 0:
                    triangle[row+1][el] += triangle[row][el]
                    triangle[row+1][el+1] += triangle[row][el]
                else:
                    triangle[row+1][el+1] += triangle[row][el]
                    if triangle[row+1][el] < triangle[row+1][el] - triangle[row][el-1] + triangle[row][el]:
                        triangle[row+1][el] = triangle[row+1][el] - triangle[row][el-1] + triangle[row][el]
            else:
                triangle[row+1][el] += triangle[row][el]
                triangle[row+1][el+1] += triangle[row][el]

def create_triangle(path, lst):
    file = open(path, 'r')
    for row in file:
        tmp = []
        row = row.replace('\n', '')
        row = row.split(' ')
        for el in row:
            tmp.append(int(el))
        lst.append(tmp)
    return lst


if __name__ == "__main__":
    '''
    By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total 
    from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text 
    file containing a triangle with one-hundred rows.

    Note: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this 
    problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take 
    over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
    '''
    triangle = []
    time_start = time.time()

    create_triangle('problem_67.txt', triangle)
    # print('Start triangle is:\n')
    # show(triangle)

    solve(triangle)

    # print('Changed triangle is:\n')
    # show(triangle)

    time_stop = time.time()
    print(f'\nSpend time: {round(time_stop-time_start, 5)} seconds')
    print(f'\nResult = {max(triangle[-1])}')