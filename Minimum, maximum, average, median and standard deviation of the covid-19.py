#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: october 16, 2022
#This program compute the minimum, maximum, average, median and standard deviation of the covid-19 cases of the borough entered by the user and then display the fraction of the covid-19 daily cases in that borough over time and saves it using the file name entered by the user.

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv(input("Enter a csv file: "))
borough = input("Enter borough(Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")
user_out = input("Enter output name: ")

minNumber = pop[borough].min()
maxNumber = pop[borough].max()
meanNumber = round(pop[borough].mean(),3)
medianNumber = pop[borough].median()
standardNumber = round(pop[borough].std(),3)

print("Min:",minNumber)
print("Max:",maxNumber)
print("Mean:",meanNumber)
print("Median:",medianNumber)
print("Standard Deviation:",standardNumber)

pop["Fraction"]=pop[borough]/pop['Case Count']

pop.plot(x='Date of Interest', y='Fraction')

#fig = pop.gfc()
#fig.getfig(out)

plt.savefig(user_out)
