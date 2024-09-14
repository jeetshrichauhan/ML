from typing import List, Union

def matrix_dot_vector(a: List[List[Union[int, float]]], b: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Parameters:
    a (List[List[Union[int, float]]]): The input matrix
    b (List[Union[int, float]]): The input vector

    Returns:
    List[Union[int, float]]: The result of the matrix-vector multiplication, or -1 if dimensions do not match
    """

    if len(a[0]) != len(b):
        return -1  # Return -1 if dimensions do not match

    result = [] # Initialize the result list

    # Compute dot product for each row of the matrix
    for row in a:
        dot_product = sum(row[j] * b[j] for j in range(len(row)))
        result.append(dot_product)

    return result

# Example usage:
matrix = [[1, 2], [3, 4], [5, 6]]
vector = [7, 8]

result = matrix_dot_vector(matrix, vector)
print("Dot Product Result:", result)
