"""
Simple linear regression example using numpy and matplotlib.

This script calculates the coefficients of a linear regression equation
from a set of data points, and plots the data points and the regression line.

"""
import numpy as np # for linear algebra
import matplotlib.pyplot as plt # for plotting


def calculate_coefficients(x, y):
    """
    Calculate the coefficients of a linear regression equation from a set of data points.

    Parameters
    ----------
    x : array_like
        The independent variable.
    y : array_like
        The dependent variable.

    Returns
    -------
    b0, b1 : float
        The coefficients of the linear regression equation.
    """
    n = len(x) # number of data points
    b1 = (np.sum(x*y) - n * np.mean(x) * np.mean(y)) / (np.sum(x**2) - n * np.mean(x)**2) # slope
    b0 = np.mean(y) - b1 * np.mean(x) # intercept 
    return b0, b1 


def plot_regression_line(x, y, b0, b1):
    """
    Plot the data points and the regression line.

    Parameters
    ----------
    x : array_like
        The independent variable.
    y : array_like
        The dependent variable.
    b0, b1 : float
        The coefficients of the linear regression equation.
    """
    plt.scatter(x, y, color="blue", label="data points")
    plt.plot(x, b0 + b1*x, color="red", label="regression line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Data points
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    # Calculate coefficients
    b0, b1 = calculate_coefficients(x, y)

    # Print coefficients
    print(f"Estimated coefficients:\nb0 = {b0}\nb1 = {b1}")

    # Plot data points and regression line
    plot_regression_line(x, y, b0, b1)
