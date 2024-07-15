import numpy as np

def basic_linear_regression():
    np.rand.seed(0)
    X = 2 * np.rand.rand(100, 1)
    y = 4 + 3 * X + np.rand.randn(100, 1)
    
    X_b = np.c_[np.ones((100, 1)), X]  # add x0 = 1 to each instance
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    
    return theta_best
