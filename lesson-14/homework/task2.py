import numpy as np
def raise_to_pow(base, exponent):
    return base ** exponent
bases = [2, 3, 4, 5]
exponents = [1, 2, 3, 4]
vectorized_power = np.vectorize(raise_to_pow)
results = vectorized_power(bases, exponents)

print("Bases:     ", bases)
print("Exponents: ", exponents)
print("Results:   ", results)
