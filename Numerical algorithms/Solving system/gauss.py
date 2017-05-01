# To obtain the inverse matrix:
def inv(matrix):

    matrix_size = len(matrix)

    result = [[0 for i in range(0, matrix_size)] for j in range(0, matrix_size)]

    for i in range(0, matrix_size):
        column = for_column(matrix, i)
        for j in range(0, matrix_size):
            result[j][i] = column[j]

    return result

# To convert a matrix into an inverse matrix:
def for_column(our_matrix, column):

    matrix_size = len(our_matrix)
    mega_matrix = [[our_matrix[i][j] for j in range(matrix_size)] for i in range(matrix_size)]
    new_column = [0 for i in range(matrix_size)]

    for i in range(matrix_size):
        mega_matrix[i].append(float(i == column))

    for i in range(0, matrix_size):
        if mega_matrix[i][i] == 0:
            for j in range(i + 1, matrix_size):
                if mega_matrix[j][j] != 0:
                    mega_matrix[i], mega_matrix[j] = mega_matrix[j], mega_matrix[i]
        for j in range(i + 1, matrix_size):
            d = - mega_matrix[j][i] / mega_matrix[i][i]
            for k in range(0, matrix_size + 1):
                mega_matrix[j][k] += d * mega_matrix[i][k]

    for i in range(matrix_size - 1, -1, -1):
        for_result = 0
        for j in range(matrix_size):
            for_result += mega_matrix[i][j] * new_column[j]
        new_column[i] = (mega_matrix[i][matrix_size] - for_result) / mega_matrix[i][i]

    return new_column

# Multiplication of SLAU to column:
def multi(SLAU, column):

    column_size = len(column)
    result = [0 for j in range(column_size)]

    for j in range(column_size):
        for k in range(column_size):
            result[j] += column[k] * SLAU[j][k]

    return result
