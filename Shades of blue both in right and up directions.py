#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: september 15, 2022
#This program shows the shades of blue both in right and up directions


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
    t.color(0,i,i)
    t.forward(10)


t.penup()
for i in range(0,255,10):
    t.backward(10)

t.left(90)
t.pendown()

for i in range(0,255,10):
     t.pensize(i)		
     t.color(0,i,i)
     t.forward(10)



