#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: october 16, 2022
#This program makes a bar plot of the NO. OF Internet Plans of every country in the chosen region, and store the plot in the output file the user specified.

import matplotlib.pyplot as plt
import pandas as pd

pd = pd.read_csv("country_internet.csv")

byregion = pd.groupby("Continental region")
print(byregion["NO. OF Internet Plans"].mean())
print("Possible regions are")
print(byregion.groups.keys())

region_choice = input("choose a region: ")
print("In region",region_choice)

chosRegion = byregion.get_group(region_choice)

print("number of countries: "+ str(chosRegion['Country'].nunique()))
print("maximum number of internet plans: "+ str(chosRegion['NO. OF Internet Plans'].max()))
print("minimum number of internet plans: "+ str(chosRegion['NO. OF Internet Plans'].min()))

user_output = input("Please enter output file name: ")

chosRegion.plot.bar("Country","NO. OF Internet Plans")
    #the first parameter of bar method is the column name representing country, the second parameter is the number of internet plans
plt.gcf().subplots_adjust(bottom=0.25)
    #so that the country name is displayed in full
plt.xlabel(f"Country in {chosRegion}") #f and then {} turns it into a string
    #The parameter in xlabel should be "Country in ...", where ... is the name of chosen region. The region name should be exactly the same as the corresponding region the csv file.
plt.ylabel("NO. OF Internet Plans")
plt.savefig(user_output)
plt.show()