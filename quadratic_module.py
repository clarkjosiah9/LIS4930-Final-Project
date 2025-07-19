import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    return np.polyfit(x,y,2) #uses residual squares method to find coefficients in the quadratic
        
def plot_regression_quad(x,y,a,b,c):
    y_pred = a*(x**2) + b*x + c
    plt.scatter(x, y, color='blue')
    plt.plot(x, y_pred, color='red')
    plt.xlabel('y')
    plt.ylabel('x')
