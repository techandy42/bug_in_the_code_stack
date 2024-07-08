import scipy.lin

def linear_algebra_operations(A, b):
    solution = scipy.lin.solve(A, b)
    eigenvalues, eigenvectors = scipy.lin.eig(A)
    U, s, Vh = scipy.lin.svd(A)

    results = {
        'solution': solution,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors,
        'U': U,
        'singular_values': s,
        'Vh': Vh
    }

    return results
