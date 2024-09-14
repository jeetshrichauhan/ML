import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    """
    Parameters:
    X (list[list[float]]): The input feature matrix where each inner list is a feature vector
    y (list[float]): The target vector

    Returns:
    list[float]: The vector of parameters (theta) for the linear regression model
    """
    # Convert lists to numpy arrays
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)  # Ensure y is a column vector

    # Add intercept term (bias) by adding a column of ones to X
    X_b = np.c_[np.ones((X.shape[0], 1)), X]

    # Compute the parameters using the normal equation: theta = (X^T X)^(-1) X^T y
    X_transpose = X_b.T
    theta = np.linalg.inv(X_transpose.dot(X_b)).dot(X_transpose).dot(y)
    
    # Round theta values to 4 decimal places and convert to list
    theta = np.round(theta, 4).flatten().tolist()
    
    return theta

# Example usage:
X = [[1, 2], [2, 3], [4, 5], [3, 6]]
y = [5, 7, 11, 8]

theta = linear_regression_normal_equation(X, y)
print(f"Computed theta (parameters): {theta}")
