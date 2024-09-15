import math
def single_neuron_model(features, labels, weights, bias):
    probabilities = []
    #Converts linear combination of inputs into a probability between 0 and 1.
    for feature_vector in features:
        z = sum(weight * feature for weight, feature in zip(weights, feature_vector)) + bias
        prob = 1 / (1 + math.exp(-z))
        probabilities.append(round(prob, 4))
    #Measures how well the model is performing by comparing predicted probabilities to actual labels.
    mse = sum((prob - label) ** 2 for prob, label in zip(probabilities, labels)) / len(labels)
    mse = round(mse, 4)
    
    return probabilities, mse

#Test
features = [[0.5, 1.2], [1.5, 2.1], [2.0, 0.9]]
labels = [0, 1, 1]
weights = [0.4, 0.7]
bias = 0.2

probabilities, mse = single_neuron_model(features, labels, weights, bias)

print("Predicted probabilities:", probabilities)
print("Mean Squared Error:", mse)
