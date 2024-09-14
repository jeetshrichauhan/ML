import numpy as np

def feature_scaling(data: np.ndarray) -> tuple[list[list[float]], list[list[float]]]:
    """
    Parameters:
    data (np.ndarray): The input data matrix where each row is a training example and each column is a feature.

    Returns:
    tuple: A tuple containing two lists:
        - Standardized data
        - Min-Max normalized data
    """
    # Standardization (Z-score normalization)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std

    # Min-Max Normalization
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    normalized_data = (data - min_val) / (max_val - min_val)

    # Round results to 4 decimal places and convert to lists
    return np.round(standardized_data, 4).tolist(), np.round(normalized_data, 4).tolist()

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
standardized, normalized = feature_scaling(data)
print("Standardized Data:", standardized)
print("Normalized Data:", normalized)
