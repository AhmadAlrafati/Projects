#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 10, 2022
#This program writes inputted last name in full capital laters and adds "@hunter.cuny.edu" to the username of email

fullName=input('Enter name in format firstName lastName: ')
name=fullName.split(' ')
print("name in LASTNAME, firstName format: "+name[1].upper()+", "+name[0])
user=input('Enter user name of email: ')
email=user.lower()+"@hunter.cuny.edu"
print("email: "+email)

