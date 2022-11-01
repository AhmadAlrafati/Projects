#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date:  10/4/2022
#This program Write a program that asks the user for a list of words (separated by spaces), count number of words, and calculate those words ending with letter 'a' or 'b', then calculate its fraction rounded by two decimal numbers after the decimal point. Your program should output the total number of words and the fraction that end in 'a' or 'b'. Assume that words are separated by spaces (and ignore the possibility of tabs and punctuation between words.)

user_list = input("Enter a list of words, separated by a space:").split()
print("number of words: " + str(len(user_list)))

ab_count = len([i for i in user_list if i[-1]=='a' or i[-1]=='b'])

print("number of words ending with a or b: " + str(ab_count))

print("fraction of words starting with a or b: "+str(round(float(ab_count)/float(len(user_list)),2)))