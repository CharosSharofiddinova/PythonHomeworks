import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x), 'r--', label='sin(x)')
plt.plot(x, np.cos(x), 'b-', label='cos(x)')
plt.legend()
plt.title('sin(x) and cos(x)')
plt.xlabel('x')
plt.ylabel('Value')
plt.grid(True)
plt.show()
