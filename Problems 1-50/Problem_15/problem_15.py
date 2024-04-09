def image(matrix):
    for raw in matrix:
        print(raw)

def create_m(matrix):
    matrix.append([1]*(len_column-1))  # верхній список з одиничками

    for i in range(len_raw-1):  # заповнюємо нулями матрицю, але на 1 строку менше від розміру і на 1 стовпчик менше
        matrix.append([0]*(len_column-1))

    for raw in matrix:  # додаємо одиниці зліва список з одиничками
        raw.insert(0, 1)
    return matrix

def modern_m(matrix):
    for raw in range(len(matrix)-1):
        for i in range(len(matrix[:])-1):
            matrix[raw+1][i+1] = matrix[raw][i+1] + matrix[raw+1][i]
    return matrix


if __name__ == '__main__':
    # matrix = [[1, 1, 1],
    #           [1, 2, 3],
    #           [1, 3, 6]]
    # matrix = [[1, 1, 1],
    #           [1, 0, 0],
    #           [1, 0, 0]]

    len_raw = 21
    len_column = 21
    matrix=[]

    create_m(matrix)
    image(matrix)
    modern_m(matrix)

    print()

    # image(matrix)
    print(matrix[-1][-1])