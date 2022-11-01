#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 10, 2022
#This program convert centimeters to feet, convert centimeters to feet and inches, convert feet and inches to centimeters

print("(a) convert centimeters to feet")
print("(b) convert centimeters to feet and inches")
print("(c) convert feet and inches to centimeters")

user_choice = input("Enter a or b or c: ")

if user_choice == "a":
    cm = float(input("Enter height in centimeters: "))
    print("heigt is",round(cm/30.48,2),"feet")
elif user_choice=='b':
    cm=float(input('Enter height in centimeters: '))
    ft=int(cm/30.48)
    inches = float((cm - ft*30.48)/2.54)
    if inches!=0:
        print("height is",ft,'feet and',round(inches,0),'inches')
    else:
        print("height is",ft,'feet')
elif user_choice=='c':
    feet_str, inches_str = input("Enter height in feet and inches, separated by a space: ").split()
    feet = int(feet_str)
    inches = int(inches_str)
    centimeters = (feet*30.48)+(inches*2.54)
    print("height is",round(centimeters,0),"cm")
else:
    print("Wrong choice, please enter only a or b or c.")
