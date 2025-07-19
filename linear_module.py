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
