import numpy as np
def accuracy_score(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

y_true = np.array([15, 10, 12, 15, 10])
y_pred = np.array([20, 15, 12, 11, 9])

print(f"true: {y_true}, pred: {y_pred}")
accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy: {accuracy:.2f}")

