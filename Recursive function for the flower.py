#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: october 23, 2022
#This program Write a function, flowerRecursion(), in recursive function for the flower in Problem 2.

def flowerRecursion(t, n):
   if n > 0:
      #draw one petal
        t.forward(100)
        t.left(105)
        t.forward(52)
        t.left(105)
        t.forward(100)

      #prepare to move direction to draw next petal
        t.right(170)
   
        flowerRecursion(t,n-1)