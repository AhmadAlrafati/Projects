#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 10, 2022
#This program Enters a list of names separated by semicolon. Display each name in a line, started by the first letter of first name, followed by a dot, a space, and last name.


user_input = input("Enter a list of names, separated by semicolon:")

user_input = user_input.split(";")

for i in range(len(user_input)):
    user_input[i] = user_input[i].split()

for i in user_input:
    print((i[0][0:1]) + ". " + i[1])
