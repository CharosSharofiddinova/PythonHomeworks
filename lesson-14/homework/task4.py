import numpy as np
A = np.array([
    [10, -2,  3],
    [-2,  8, -1],
    [ 3, -1,  6]
])
b = np.array([12, -5, 15])
currents = np.linalg.solve(A, b)
print(f"I1 = {currents[0]:.2f}")
print(f"I2 = {currents[1]:.2f}")
print(f"I3 = {currents[2]:.2f}")
