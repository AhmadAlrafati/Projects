#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 10, 2022
#This program writes a given phrase backwards, backwards and uppercase, and it's abbreviation

userinput=input("input: ")

backwards=userinput[::-1]
print("user reverse:",backwards)

capbackwards=backwards.upper()
print("user reverse upper:",capbackwards)

split=userinput.split()

inputcut=""
for i in split:
    inputcut+=i[:1].upper()

print("user abbreviation:",inputcut)
