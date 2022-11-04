#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: october 16, 2022
#This program counts occurrences of a given character
 
def main() :
     
    # Count variable
    res = 0
     
    for i in range(len(s)) :
         
        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res

s= input("Enter a string: ")
c = input("Enter a char: ")
print("number of",c,"in",s,"is",main())