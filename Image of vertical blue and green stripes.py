#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 10, 2022
#This program Creates a program that creates a image of vertical blue and green stripes

import matplotlib.pyplot as plt
import numpy as np

user_size = int(input("Enter the size:"))
filename_output = input("Enter output file:")

graph = np.zeros((user_size,user_size,3))

graph[:,:,:] = (0,255,0)
graph[:,::2,:] = (0,0,255)

plt.imshow(graph)
plt.show()
plt.imsave(filename_output,graph)