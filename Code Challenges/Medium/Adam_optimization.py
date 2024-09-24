import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
    x = x0                         # the starting point
    m = np.zeros_like(x)          # the first moment vector (mean)
    v = np.zeros_like(x)          # the second moment vector (variance)

    for t in range(1, num_iterations + 1):  # Loop for specified number of iterations
        g = grad(x)                # Compute the gradient at x
        m = beta1 * m + (1 - beta1) * g  # Update biased first moment estimate
        v = beta2 * v + (1 - beta2) * g**2  # Update biased second raw moment estimate
        m_hat = m / (1 - beta1**t)  # Compute bias-corrected first moment estimate
        v_hat = v / (1 - beta2**t)  # Compute bias-corrected second moment estimate
        x = x - learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)  # Update parameters

    return x                      # Return the optimized parameters

# Define a simple quadratic function and its gradient
def f(x):
    return x**2

def grad(x):
    return 2 * x

# Initial guess
x0 = np.array([10.0])  # Start far from the minimum at 0

# Optimize using Adam
#optimized_x = adam_optimizer(f, grad, x0, learning_rate=0.1, num_iterations=100)

#optimized_x = adam_optimizer(f, grad, x0, learning_rate=0.01, num_iterations=100) #Reduced learning rate

optimized_x = adam_optimizer(f, grad, x0, learning_rate=0.1, num_iterations=500) #Increased number of iterations


print(f"Optimized x: {optimized_x}")

