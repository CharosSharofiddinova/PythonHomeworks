import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.1, 10, 100)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, x**3)
axs[0, 0].set_title('x³')
axs[0, 1].plot(x, np.sin(x))
axs[0, 1].set_title('sin(x)')
axs[1, 0].plot(x, np.exp(x))
axs[1, 0].set_title('e^x')
axs[1, 1].plot(x, np.log(x))
axs[1, 1].set_title('log(x)')
plt.tight_layout()
plt.show()

