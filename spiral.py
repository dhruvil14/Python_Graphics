from turtle import *
speed(0)
pensize(2)
colors=["red","green","blue","yellow"]
for i in range(500):
	bgcolor("black")
        color(colors[i%4])
        forward(i)
        left(91)
exitonclick()
