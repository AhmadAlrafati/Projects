#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: october 16, 2022
#This program: If the choice is 1, then enter the name of an output file. Your program should then save the upper right quarter of the image to the output file specified by the user. If the choice is 2, then enter the name of an output file to save the middle portion (from 1/4 of height to 3/4 of height and from 1/4 of width to 3/4 of width) of the original figure.

from matplotlib import use
import matplotlib.pyplot as plt
import numpy as np

print("""Enter 1 to get upper right corner
Enter 2 to get middle portion""")

user_choice = input("Your choice: ")

if user_choice=="1":
    user_file = plt.imread(input("Enter input file name: "))
    user_output = input("Enter output file name: ")

    height = user_file.shape[0]
    width = user_file.shape[1]
    img2 = user_file[height//1/3:, :width//1/3]
    
    plt.imshow(img2)
    plt.show()
    plt.imsave(user_output,img2)

elif user_choice=="2":
    user_file = plt.imread(input("Enter input file name: "))
    user_output = input("Enter output file name: ")

    Height= user_file.shape[0]
    Width = user_file.shape[1]
    img2= user_file

    plt.imshow(img2)
    plt.show()
    plt.imsave(user_output,img2)
else:
    print("wrong choice")