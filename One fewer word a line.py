#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 17, 2022
#This program asks the user for a message and then prints the message out, one fewer word a line until there is only one word, then continue to add one word a line until becoming the original message

user_message = input("Enter a phrase: ")
message_split = user_message.split(" ")


for i in range(len(message_split),0,-1):
    print(" ".join(message_split[:i]))

for i in range(len(message_split)-1):
    print(" ".join(message_split[:i+2]))
