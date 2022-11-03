#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date:  10/4/2022
#This program Implement the following pseudocode to convert a string to a decimal number. If the string contains any letter other than '0' or '1', exit and report errors.

string = input("Enter a string with 0 or 1 only: ")
num = 0
base = 2
weight = 1
length = len(string)
ch = ""

for i in string[::-1]:
    ch = i
    if ch=="1":
        num = num + weight
    elif ch!="0":
        print("Letter",ch,"is not allowed in binary string.")
        exit()
    weight = weight*base
print("num = "+str(num))