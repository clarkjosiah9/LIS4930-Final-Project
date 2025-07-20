import linear_module as lin
import quadratic_module as quad
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    #For Fourth Grade
    df_naep1 = pd.read_excel("2024 NAEP Results (4th,8th).xlsx", sheet_name= "Ach Level G4")
    df_naep2 = pd.read_excel("2024 NAEP Results (4th,8th).xlsx", sheet_name= "Ach Level G8")
    years = df_naep1.iloc[4, 3:18].values
    disadvantaged = df_naep1.iloc[19, 3:18].values #average scores for disadvantaged fourth graders on NAEP assessment as an array
    advantaged = df_naep1.iloc[20, 3:18].values #average scores for advantaged fourth graders on NAEP assessment as an array
    


    #Scores vs Years for Fourth Grade
    line1 = lin.fit(years,disadvantaged)
    line2 = lin.fit(years,advantaged)
    line1.graph('Years',"Score of Economically Disadvantaged 4th Grade Students")
    line2.graph('Years',"Score of Economically Advantaged 4th Grade Students")
    
    quad1 = quad.fit(years,disadvantaged)
    quad2 = quad.fit(years,advantaged)
    quad1.graph('Years',"Score of Economically Disadvantaged Students")
    quad2.graph('Years',"Score of Economically Advantaged Students")

    #Pre-COVID Plots
    pre_years = df_naep1.iloc[4, 3:15].values
    pre_disadvantaged = df_naep1.iloc[19, 3:15].values
    pre_advantaged = df_naep1.iloc[20, 3:15].values

    pre_line1 = lin.fit(pre_years,pre_disadvantaged)
    pre_line2 = lin.fit(pre_years,pre_advantaged)
    pre_line1.graph('Pre-COVID Years',"Score of Economically Disadvantaged 4th Grade Students")
    pre_line2.graph('Pre-COVID Years',"Score of Economically Advantaged 4th Grade Students")

    pre_quad1 = quad.fit(pre_years,pre_disadvantaged)
    pre_quad2 = quad.fit(pre_years,pre_advantaged)
    pre_quad1.graph('Pre-COVID Years',"Score of Economically Disadvantaged 4th Grade Students")
    pre_quad2.graph('Pre-COVID Years',"Score of Economically Advantaged 4th Grade Students")
#-------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
    #Scores vs Years for Eigth Grade
    disadvantaged1 = df_naep2.iloc[19, 3:18].values #average scores for disadvantaged fourth graders on NAEP assessment as an array
    advantaged1 = df_naep2.iloc[20, 3:18].values #average scores for advantaged fourth graders on NAEP assessment as an array
    line3 = lin.fit(years,disadvantaged1)
    line4 = lin.fit(years,advantaged1)
    line3.graph('Years',"Score of Economically Disadvantaged 8th Grade Students")
    line4.graph('Years',"Score of Economically Advantaged 8th Grade Students")
    
    quad1 = quad.fit(years,disadvantaged1)
    quad2 = quad.fit(years,advantaged1)
    quad1.graph('Years',"Score of Economically Disadvantaged Students")
    quad2.graph('Years',"Score of Economically Advantaged Students")

    #Pre-COVID
    pre_disadvantaged1 = df_naep2.iloc[19, 3:15].values
    pre_advantaged1 = df_naep2.iloc[20, 3:15].values
    pre_line1 = lin.fit(pre_years,pre_disadvantaged1)
    pre_line2 = lin.fit(pre_years,pre_advantaged1)
    pre_line1.graph('Pre-COVID Years',"Score of Economically Disadvantaged 8th Grade Students")
    pre_line2.graph('Pre-COVID Years',"Score of Economically Advantaged 8th Grade Students")

    pre_quad1 = quad.fit(pre_years,pre_disadvantaged1)
    pre_quad2 = quad.fit(pre_years,pre_advantaged1)
    pre_quad1.graph('Pre-COVID Years',"Score of Economically Disadvantaged 8th Grade Students")
    pre_quad2.graph('Pre-COVID Years',"Score of Economically Advantaged 8th Grade Students")
main()