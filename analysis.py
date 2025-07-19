
import linear_module as lin
import quadratic_module as quad
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

class line_fit: #class where each instance of x and y values contains its predicted linear equation and graph

    def __init__(self,x,y,grade):
        self.x = x
        self.y = y
        self.grade = grade
        self.b0, self.b1 = lin.estimate_coef(self.x,self.y)
        self.b = (float(self.b0), float(self.b1))
    def __str__(self):
        return f'y = {self.b0}x + {self.b1}'  #prints linear equation of the instance
    def equation(self):
        y_pred = self.b1*(self.x) + self.b0
        return y_pred
    def graph(self):
        lin.plot_regression_line(self.x,self.y,self.b)
        plt.xlabel("Years")
        plt.ylabel(f"Average Scores of grade {self.grade}")
        plt.show()

class quad_fit: #class where each instance of x and y values contains its predicted quadratic equation and graph
    def __init__(self,x,y,grade):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.grade = grade
        self.a,self.b,self.c = quad.estimate_coef(self.x,self.y)
    def __str__(self):
        return f'y = {self.a}x^2 + {self.b}x + {self.c}'  
    def equation(self):
        y_pred = self.a*(self.x**2) + self.b*(self.x) + self.c
        return y_pred
    def graph(self):
        quad.plot_regression_quad(self.x,self.y,self.a,self.b,self.c)
        plt.xlabel("Years")
        plt.ylabel(f"Average Scores of grade {self.grade}")
        plt.show()

def main():
#Analyzing Trends concerning Math Education via data provided by the NAEP average math scores

#Analyzing NAEP Data with simple linear and quadratic regression techniques:
    df_naep1 = pd.read_excel("Data/2024 NAEP Results (4th,8th).xlsx", sheet_name= "Ach Level G4")
    df_naep2 = pd.read_excel("Data/2024 NAEP Results (4th,8th).xlsx", sheet_name= "Ach Level G8")
    years = df_naep1.iloc[4, 1:18].values
    avg_score1 = df_naep1.iloc[5, 1:18].values #average scores for fourth graders on NAEP assessment as an array
    avg_score2 = df_naep2.iloc[5, 1:18].values #average scores for eigth graders on NAEP assessment as an array

    
#Line of Best fit
    line1 = line_fit(years,avg_score1,4)
    line2 = line_fit(years,avg_score2,8)
    print(f' Line 1: {line1}')
    print(f' Line 2: {line2}')
    line1.graph()
    line2.graph()

    
#Clearly, line of best fit is inadequate. Quadratic?
    quad1 = quad_fit(x = years, y = avg_score1, grade = 4)
    quad2 = quad_fit(x = years, y = avg_score2, grade = 8)
    print(f' Quadratic 1: {quad1}')
    print(f' Quadratic 2: {quad2}')
    quad1.graph()
    quad2.graph()
    

main()