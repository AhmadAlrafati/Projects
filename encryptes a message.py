#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 10, 2022
#This program encryptes a message based on caeser cipher when given a phrase and key

userphrase=input("Enter an all-small-letter string: ")


key=int(input("Enter a non-negative int to shift: "))

cipher=""
for i in userphrase:
    if ord(i)+key<=122:
        cipher+=chr(ord(i)+key)
    else:
        cipher+=chr(97+(ord(i)+key-123))

print("ciphered string:",cipher)
