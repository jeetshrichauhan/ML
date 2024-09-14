import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Parameters:
    X (np.ndarray): input feature matrix, y (np.ndarray): target vector
    alpha (float): The learning rate for gradient descent
    iterations (int): The number of iterations for gradient descent

    Returns:
    np.ndarray: The vector of parameters (theta) for the linear regression model
    """
    m, n = X.shape
    theta = np.zeros((n, 1))  # Initialize parameters to zeros

    for _ in range(iterations):
        # Compute predictions
        predictions = X @ theta
        
        # Compute errors
        errors = predictions - y.reshape(-1, 1)
        
        # Compute gradient
        updates = X.T @ errors / m
        
        # Update theta
        theta -= alpha * updates

    # Return the final parameters rounded to 4 decimal places
    return np.round(theta.flatten(), 4)

# Example
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])
y = np.array([5, 7, 11, 8])
alpha = 0.01  
iterations = 1000  

theta = linear_regression_gradient_descent(X, y, alpha, iterations)
print(f"Computed theta (parameters): {theta}")
