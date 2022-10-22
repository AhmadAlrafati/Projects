#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 10, 2022
#This program prints out a given phrase by letter, the letter in ASCII, and the next two letters


userphrase=input("Enter a phrase: ")

print("letter","ASCII", "next_two_letter")

for i in userphrase:
    print("%6c %5i %15c"%(i,ord(i), chr(ord(i)+2)))
    
