import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2, 5, 100) 
y = x*np.sin(5*x)

plt.plot(x, y, label='x*sin(5*x)', color = "red", linewidth = 5)

plt.title('My plot', fontsize=15) 
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('y', fontsize=12, color='blue')  
plt.legend()
plt.grid(True)
plt.show()