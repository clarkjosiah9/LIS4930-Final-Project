import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def estimate_coef(x,y): #find b0 and b1
    n = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    #For calculating b1
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
    #Calculation
    b1 = SS_xy / SS_xx
    b0 = m_y - b1*m_x

    return(b0,b1)

def plot_regression_line(x, y, b):
  # plotting the actual points as scatter plot
  plt.scatter(x, y, color = "m",
        marker = "o", s = 30)

  # predicted response vector
  y_pred = b[0] + b[1]*x

  # plotting the regression line
  plt.plot(x, y_pred, color = "g")

  # putting labels
  plt.xlabel('x')
  plt.ylabel('y')

class fit: #class where each instance of x and y values contains its predicted linear equation and graph

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.b0, self.b1 = estimate_coef(self.x,self.y)
        self.b = (float(self.b0), float(self.b1))
    def __str__(self):
        return f'y = {self.b0}x + {self.b1}'  #prints linear equation of the instance
    def predict(self,x_0):
        y_pred = self.b1*(x_0) + self.b0
        return y_pred
    def graph(self, x_axis = 'x', y_axis = 'y'):
        plot_regression_line(self.x,self.y,self.b)
        plt.xlabel(f'{x_axis}')
        plt.ylabel(f'{y_axis}')
        plt.show()