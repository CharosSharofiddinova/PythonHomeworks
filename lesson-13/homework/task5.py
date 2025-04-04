import numpy as np

# Create a 10x10 array with random values
array = np.random.rand(10, 10)

# Find the minimum and maximum values in the array
min_value = np.min(array)
max_value = np.max(array)

# Print the results
print("Array:")
print(array)
print("Minimum value: ", min_value)
print("Maximum value: ", max_value)
