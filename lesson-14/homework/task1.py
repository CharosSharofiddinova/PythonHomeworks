
import numpy as np
def f_to_c(f):
    return (f - 32) * 5 / 9
temps_f = [32, 68, 100, 212, 77]
f_to_c_vectorized = np.vectorize(f_to_c)

temps_c = f_to_c_vectorized(temps_f)
print("Temperatures in Fahrenheit:", temps_f)
print("Temperatures in Celsius:", temps_c)
