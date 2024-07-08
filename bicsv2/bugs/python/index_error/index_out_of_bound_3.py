def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n*m):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n*m):
        matrix[i].reverse()
    return matrix
