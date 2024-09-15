import numpy as np
X = np.array([  [1, 2], 
                [3, 4], 
                [5, 6], 
                [7, 8]])
y = np.array([1, 2, 3, 4])

def shuffle_data(X, y, seed=None):
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx] 

X_shuffled, y_shuffled = shuffle_data(X, y, seed=42)

print("Shuffled X:\n", X_shuffled)
print("Shuffled y:\n", y_shuffled)
