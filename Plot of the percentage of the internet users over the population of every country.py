#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: october 16, 2022
#This program makes a plot of the percentage of the internet users over the population of every country, and store the plot in the output file the user specified.

import matplotlib.pyplot as plt
import pandas as pd

pd = pd.read_csv("country_internet.csv")
user_output = input("Enter ouput file name: ")
pd["Percentage"] = pd["Internet users"]/pd["Population"]*100

pd.plot(x="Country",y="Percentage")

plt.savefig(user_output)
plt.show()