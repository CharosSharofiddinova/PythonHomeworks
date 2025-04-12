import numpy as np
import matplotlib.pyplot as plt
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
colors = np.random.rand(100)
markers = ['o', 's', 'D', '^', 'v', '<', '>']
marker = np.random.choice(markers)
plt.scatter(x, y, c=colors, cmap='viridis', marker=marker)
plt.title('Scatter Plot of 100 Random Points')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.show()
