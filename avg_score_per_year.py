
import linear_module as lin
import quadratic_module as quad
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
#Analyzing Trends concerning Math Education via data provided by the NAEP average math scores

#Analyzing NAEP Data with simple linear and quadratic regression techniques:
    df_naep1 = pd.read_excel("2024 NAEP Results (4th,8th).xlsx", sheet_name= "Ach Level G4")
    df_naep2 = pd.read_excel("2024 NAEP Results (4th,8th).xlsx", sheet_name= "Ach Level G8")
    years = df_naep1.iloc[4, 1:18].values
    avg_score1 = df_naep1.iloc[5, 1:18].values #average scores for fourth graders on NAEP assessment as an array
    avg_score2 = df_naep2.iloc[5, 1:18].values #average scores for eigth graders on NAEP assessment as an array

    
#Line of Best fit
    line1 = lin.fit(years,avg_score1)
    line2 = lin.fit(years,avg_score2)
    print(f' Line 1: {line1}')
    print(f' Line 2: {line2}')
    line1.graph("Years", "Average NAEP Math Score for 4th Grade")
    line2.graph("Years", "Average NAEP Math Score for 8th Grade")
    print(line1.predict(2027))
    print(line2.predict(2027))
#Clearly, line of best fit is inadequate. Quadratic?
    quad1 = quad.fit(x = years, y = avg_score1)
    quad2 = quad.fit(x = years, y = avg_score2)
    print(f' Quadratic 1: {quad1}')
    print(f' Quadratic 2: {quad2}')
    quad1.graph("Years", "Average NAEP Math Score for 4th Grade")
    quad2.graph("Years", "Average NAEP Math Score for 8th Grade")
    print(quad1.predict(2027))
    print(quad2.predict(2027))


main()