import numpy as np
matrix = np.random.rand(5, 5)
normalized_matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))

print("Original Matrix: ")
print(matrix)
print("Normalized Matrix: ")
print(normalized_matrix)