import json
import os
import numpy as np
import matplotlib.pyplot as plt


def f(x, A):
    return 0.5+(np.sin(x**2-A**2)**2)/(1+0.001*(x**2+A**2))


A = 0
x = np.linspace(-10, 10, 400)
y = f(x, A)
z = list(x)
v = list(y)
Data = {
    "x": z,
    "y": v
}
if not os.path.exists('results'):
    os.makedirs('results')

with open('results/values.json', 'w') as file:
    json.dump(data, file)
plt.figure(figsize=(16, 9))
plt.plot(x, y, label='f(x)', color='r')
plt.title('График')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
