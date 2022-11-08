#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: october 16, 2022
#This program Write a program that asks the user for the hour of the day (in 24 hour time), and prints "Good Morning" if it is strictly before 12,"Good Afternoon" if it is 12 or greater, but strictly before 17, and "Good Evening" otherwise.

user_time = int(input("Enter hour (in 24 hour time): "))

if user_time<12:
    print("Good Morning")
if 12<user_time<17:
    print("Good Afternoon")
else:
    print("Good Evening")