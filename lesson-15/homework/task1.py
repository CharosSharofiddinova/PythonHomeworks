import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 100)
y = x**2 - 4*x + 4
plt.plot(x, y)
plt.title('f(x) = x² - 4x + 4')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
