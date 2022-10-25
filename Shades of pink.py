#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 15, 2022
#This program  shows the shades of pink and then repeats a similar loop where a loop variable goes from 255 (included) down to 0 (not included), gap step is decreased by 10 in each round


import turtle				

turtle.colormode(255)		
t = turtle.Turtle()		


t.penup()
t.backward(100)
t.left(90)
t.backward(100)
t.right(90) 
t.pendown()

for i in range(0,255,10):
    t.pensize(i)
    t.color(i,0,i)
    t.forward(10)


for i in range(255,0,-10):
    t.pensize(i)
    t.color(i,0,i)
    t.forward(10)
