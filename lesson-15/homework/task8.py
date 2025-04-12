import matplotlib.pyplot as plt
import numpy as np
time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [50, 60, 70, 80]
category_B = [40, 30, 60, 90]
category_C = [30, 40, 20, 50]
plt.bar(time_periods, category_A, label='Category A', color='blue')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B', color='green')
plt.bar(time_periods, category_C, bottom=np.array(category_A) + np.array(category_B), label='Category C', color='red')
plt.title('Stacked Bar Chart of Categories Over Time')
plt.xlabel('Time Periods')
plt.ylabel('Contribution')
plt.legend(title='Categories')
plt.show()
