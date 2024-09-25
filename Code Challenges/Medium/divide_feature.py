import numpy as np
# Function to split the dataset X based on a feature and a threshold
def divide_on_feature(X, feature_i, threshold):

    split_func = None
    
    # Check if the threshold is numeric (integer or float)
    if isinstance(threshold, int) or isinstance(threshold, float):
        split_func = lambda sample: sample[feature_i] >= threshold
    else:
        split_func = lambda sample: sample[feature_i] == threshold

    # first subset (X_1) by applying the split function to select samples that meet the condition
    X_1 = np.array([sample for sample in X if split_func(sample)])

    # Create the second subset (X_2) by selecting samples that do not meet the condition
    X_2 = np.array([sample for sample in X if not split_func(sample)])

    return [X_1, X_2]

# Testing with example
if __name__ == "__main__":
    data = np.array([[1, 2],
                     [2, 3],
                     [3, 4],
                     [4, 5],
                     [5, 6]])
    
    feature_index = 0  
    threshold_value = 3  # split at 3
    
    subset1, subset2 = divide_on_feature(data, feature_index, threshold_value)
    
    print("Subset where feature >= threshold:")
    print(subset1)
    print("\nSubset where feature < threshold:")
    print(subset2)