from turtle import *
speed(-0)
pensize(1)
colors=["red","green","blue","yellow"]
for i in range(500):
        color(colors[i%4])
    	for j in range(4):	 
        	bgcolor("black")
 	      	forward(i)
       		left(91)
exitonclick()

