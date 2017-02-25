from turtle import *
speed(0)
shape("circle")
shapesize(0)
pensize(2)
bgcolor("black")
colors=["red","green","blue","yellow"]
for j in range(100):
	#color(colors[j%4])
	#forward(j)
        left(85)

	for i in range(3):
        	
        	color(colors[j%4])
        	forward(j)
        	left(85)
exitonclick()
