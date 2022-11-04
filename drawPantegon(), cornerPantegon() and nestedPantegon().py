#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: october 23, 2022
#This program Writes three functions, drawPantegon(), cornerPantegon() and nestedPantegon()

import turtle
import math

#recursive function to draw a pantegon
def drawPantegon(t, length, numEdges):
   if numEdges > 0:
      t.forward(length) #move the turtle object, t, forward length steps
      t.left(72)        #t turn left 72 degrees
      drawPantegon(t, length,numEdges-1)  #call drawPantegon with t, length, and numEdges-1

#pseudocode of cornerPantegon, which draws pantegon nested in left corner.
def cornerPantegon(t, length):
   if length >= 25:
    drawPantegon(t, length,5) #call drawPantegon with t, length and 5
    length = length//2        #reduced length by half (use integer division)
    cornerPantegon(t,length)  #call cornerPantegon with t and length, that is, draw a pantegon with t and updated length

def nestedPantegon(t, length):
    if length >= 25:
       drawPantegon(t, length,5) #call drawPantegon with t, length, and 5
       t.forward(length/2)       #Turtle t moves forward length/2
       t.left(36)                # Turtle t turns left 36 degrees
       pos = t.position()        #call position function of t and put the return to variable pos
       nestedPantegon(t,length*math.sin(54/180*math.pi)) #call nestedPantegon with t, length * math.sin(54/180 * math.pi)