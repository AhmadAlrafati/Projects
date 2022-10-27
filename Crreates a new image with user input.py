#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 15, 2022
#This program  asks the user for a name of an image .png file and the name of an output file. Then the program creates a new image that sets red channel of the original image to be zero.

import matplotlib.pyplot as plt
import numpy as np

user_in=input("Enter name of the input file: ")
user_out=input("Enter name of the output file: ")

img = plt.imread(user_in)


copy_img2 = plt.imread(user_in)

img2 = copy_img2.copy()
img2[:,:,0]=0



plt.imsave(user_out, img2)

