import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    return np.polyfit(x,y,2) #uses residual squares method to find coefficients in the quadratic (see https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html)
        
def plot_regression_quad(x,y,a,b,c):
    y_pred = a*(x**2) + b*x + c
    plt.scatter(x, y, color='blue')
    plt.plot(x, y_pred, color='red')
    plt.xlabel('x')
    plt.ylabel('y')

class fit: #class where each instance of x and y values contains its predicted quadratic equation and graph
    def __init__(self,x,y):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        
        self.a,self.b,self.c = estimate_coef(self.x,self.y)
    def __str__(self):
        return f'y = {self.a}x^2 + {self.b}x + {self.c}' #gives equation when printed
    def predict(self,x_0):
        y_pred = self.a*(x_0**2) + self.b*(x_0) + self.c #returns predicted value 
        return y_pred
    def graph(self, x_axis = '', y_axis = ''):
        plot_regression_quad(self.x,self.y,self.a,self.b,self.c) #plots and shows the graph of the quadratic
        plt.xlabel(f'{x_axis}')
        plt.ylabel(f'{y_axis}')
        plt.show()
