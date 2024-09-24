#single float as input and return the value after applying the function
def relu(x):
    return max(0, x)

inputs = [-2.0, -1.0, 0.0, 1.0, 2.0]

outputs = [relu(x) for x in inputs]

for x, y in zip(inputs, outputs):
    print(f"ReLU({x}) = {y}")