from turtle import *

speed(0)
setup(700,500)
bgcolor('black')
pencolor('green')
pensize(2)

for i in range(10):
    rad = 150
    for i in range(10):
        circle(rad)
        rad -=4
    right(36)
    
hideturtle()
done()
