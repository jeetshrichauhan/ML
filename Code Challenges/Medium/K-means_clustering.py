import numpy as np

def euclidean_distance(a, b):
    return np.sqrt(((a - b) ** 2).sum(axis=1)) #Euclidean distance between points

def k_means_clustering(points, k, initial_centroids, max_iterations):
    points = np.array(points) # Convert points and centroids to numpy arrays for easier manipulation
    centroids = np.array(initial_centroids)
    
    for iteration in range(max_iterations):
        # Assign points to the nearest centroid
        distances = np.array([euclidean_distance(points, centroid) for centroid in centroids])
        assignments = np.argmin(distances, axis=0)  # Determine the index of the closest centroid for each point

        new_centroids = np.array([points[assignments == i].mean(axis=0) if len(points[assignments == i]) > 0 else centroids[i] for i in range(k)])
        
        # Check for convergence
        # If centroids do not change anymore, the algorithm has converged
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids # Update for next iterations
        centroids = np.round(centroids,4)
    return [tuple(centroid) for centroid in centroids]

points = [
    [1.0, 2.0], [1.5, 1.8], [5.0, 8.0],
    [8.0, 8.0], [1.0, 0.6], [9.0, 11.0]
]
initial_centroids = [[1, 1], [5, 5]]
k = 2
max_iterations = 100

centroids = k_means_clustering(points, k, initial_centroids, max_iterations)
print("Final Centroids:", centroids)
