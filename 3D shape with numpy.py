#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 10, 2022
#This program Write a program that asks users for output file name to save the following image (T)

import numpy as np
import matplotlib.pyplot as plt

filename_output = input("Enter output file name:")

graph = np.empty([30,30,3])
graph[:,:,0] = 1.0
graph[:,:,1] = 1.0
graph[:,:,2] = 0

for i in range(5,8,1):
    for j in range(5,25,1):
        graph[i,j,0] = 0
        graph[i,j,1] = 0
        graph[i,j,2] = 1.0

for i in range(8,25,1):
    for j in range(13,16,1):
        graph[i,j,0]= 0
        graph[i,j,1] = 1.0
        graph[i,j,2] = 0

plt.imshow(graph)
plt.show()
plt.imsave(filename_output,graph)