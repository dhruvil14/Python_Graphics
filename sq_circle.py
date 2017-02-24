import turtle
def sq(some) :
	for i in range (1 , 5) :
		some.forward(100)
		some.right(90)
def art() :
	window=turtle.Screen()
	window.bgcolor("black")
	a=turtle.Turtle()
	a.shape("turtle")
	a.color("white")
	a.speed(0)
	for i in range (1,75) :
		sq(a)
		a.right(5)
	window.exitonclick()
art()
