import numpy as np
import matplotlib.pyplot as plt

 
#Data points
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

#calculate coefficients
n = len(x)
b1 = (np.sum(x*y) -n * np.mean(x) * np.mean(y)) / (np.sum(x**2) - n * np.mean(x)**2)
b0 = np.mean(y) - b1 * np.mean(x)

#print coefficients
print(f"Estimated coefficients:\nb0 = {b0}\nb1 = {b1}")

#Plot data pints and regression line
plt.scatter(x,y, color="blue", label="data points")
plt.plot(x, b0 + b1*x, color="red", label="regression line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()