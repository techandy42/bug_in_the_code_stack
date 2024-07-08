def spiral_order(matrix):
    result = []
    dimension = len(matrix) * len(matrix[0])
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for i in range(0, dimension):
                result.append(matrix[i].pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for i in range(0, dimension):
                result.append(matrix[::-1][i].pop(0))
    return result
