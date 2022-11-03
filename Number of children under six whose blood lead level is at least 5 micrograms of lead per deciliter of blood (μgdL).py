#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: october 16, 2022
#This program records the number of children under six whose blood lead level is at least 5 micrograms of lead per deciliter of blood (μg/dL) in the specific borough and year. Choose Option a to group by borough, report average of number of affected children in each borough. Enter a specific borough. Report the minimum, maximum, and average number of affected children in those years. Choose Option b to group by year, report average of number of affected children in each year. Enter a specific year. Report the minimum, maximum, and average number of affected children in the boroughs.


import matplotlib as plt
from numpy import maximum
import pandas as pd

user_choice = input("Enter a choice: \na. group by borough \nb. group by year \n")
pop = pd.read_csv("children_lead.csv")

if user_choice == "a":
    print("average number of affected children by borough")
    print(pop.groupby("borough")["affected_children"].mean())

    borough = input("Enter a borough: ")
    
    affectedNum = (pop[pop["borough"]==borough])["affected_children"]
    avergaeNum = affectedNum.mean()
    minNum = affectedNum.min()
    maxNum = affectedNum.max()

    print("average number of affected children of",borough,"is",avergaeNum)
    print("min number of affected children of",borough,"is",minNum)
    print("max number of affected chidlren of",borough,"is",maxNum)

if user_choice == "b":
    print("average number of affected chidlren by year")
    print(pop.groupby("year")["affected_children"].mean())

    user_year = input("Enter a year (2005-2016): ")

    affectedNum = (pop[pop["year"]==int(user_year)])["affected_children"]
    avergaeNum = affectedNum.mean()
    minNum = affectedNum.min()
    maxNum = affectedNum.max()

    print("average number of affected children of",user_year,"is",avergaeNum)
    print("min number of affected children of",user_year,"is",minNum)
    print("max number of affected children of",user_year,"is",maxNum)