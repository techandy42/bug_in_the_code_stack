from sklearn.model_selection import split_into_training_and_test_sets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def machine_learning_operations(X, y):
    X_train, X_test, y_train, y_test = split_into_training_and_test_sets(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    train_mse = mean_squared_error(y_train, y_pred_train)
    test_mse = mean_squared_error(y_test, y_pred_test)
    r2 = r2_score(y_test, y_pred_test)
    
    results = {
        'coefficients': model.coef_,
        'intercept': model.intercept_,
        'train_mse': train_mse,
        'test_mse': test_mse,
        'r2_score': r2,
        'predictions': y_pred_test
    }

    return results
