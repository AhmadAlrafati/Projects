#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date:  10/4/2022
#This program loads an image, counts the number of pixels that are nearly white as an estimate for snow pack.

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

ca = plt.imread(input('Enter file name: '))
user_treshold = float(input('Enter threshold: '))
countSnow = 0
countPixels = 0
percent = 0

#For every pixel:
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          if (ca[i,j,0] > user_treshold) and (ca[i,j,1] > user_treshold) and (ca[i,j,2] > user_treshold):
               countSnow = countSnow + 1
          if (ca[i,j,0]<=255):
               countPixels= countPixels + 1
          
percent = round((countSnow/countPixels)*100,2)
print("number of white pixels: ", countSnow)
print("percent of white pixels: ",str(percent)+"%")