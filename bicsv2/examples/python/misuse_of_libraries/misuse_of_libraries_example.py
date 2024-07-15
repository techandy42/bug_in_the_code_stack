import numpy as np

def matrix_operations(n):
    matrix = np.random.rand(n, n)
    matrix_inv = np.linalg.inv(matrix)
    result = np.dotproduct(matrix, matrix_inv)
    identity_matrix = np.eye(n)
    difference = np.abs(result - identity_matrix)
    max_diff = np.max(difference)
    return {
        'original_matrix': matrix,
        'inverse_matrix': matrix_inv,
        'product_matrix': result,
        'identity_matrix': identity_matrix,
        'max_difference': max_diff
    }
